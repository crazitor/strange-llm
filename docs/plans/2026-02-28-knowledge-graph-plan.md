# Knowledge Graph + Concept Index Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Extract structured concepts from 2721 articles + 25 books via DeepSeek, store in DB, and render an interactive D3.js knowledge graph with concept map sidebar.

**Architecture:** Offline extraction script calls DeepSeek per-article to extract 5 concepts + relations → stores in 3 new SQLite tables → Flask API serves graph data → D3.js force-directed graph embedded in existing single-file app.

**Tech Stack:** Python 3.11, SQLite, DeepSeek API (OpenAI-compatible), D3.js v7 (CDN), Flask

**Design doc:** `docs/plans/2026-02-28-knowledge-graph-design.md`

---

### Task 1: Database Migration

**Files:**
- Create: `scripts/migrate_concepts.py`

**Step 1: Write the migration script**

```python
#!/usr/bin/env python3
"""Create concepts, concept_sources, concept_relations tables."""
import os, sqlite3

RESEARCH_DIR = os.path.join(os.path.dirname(__file__), '..', 'research')
DB_PATH = os.path.join(RESEARCH_DIR, 'corpus.db')

SCHEMA = """
CREATE TABLE IF NOT EXISTS concepts (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    name_zh TEXT,
    description TEXT,
    category TEXT,
    first_seen_year TEXT,
    peak_year TEXT,
    mention_count INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS concept_sources (
    id INTEGER PRIMARY KEY,
    concept_id INTEGER REFERENCES concepts(id),
    source_type TEXT,
    source_id INTEGER,
    relevance REAL DEFAULT 0.5,
    context TEXT
);

CREATE TABLE IF NOT EXISTS concept_relations (
    id INTEGER PRIMARY KEY,
    concept_a INTEGER REFERENCES concepts(id),
    concept_b INTEGER REFERENCES concepts(id),
    relation TEXT,
    strength REAL DEFAULT 0.5,
    UNIQUE(concept_a, concept_b)
);

CREATE INDEX IF NOT EXISTS idx_cs_concept ON concept_sources(concept_id);
CREATE INDEX IF NOT EXISTS idx_cs_source ON concept_sources(source_type, source_id);
CREATE INDEX IF NOT EXISTS idx_cr_a ON concept_relations(concept_a);
CREATE INDEX IF NOT EXISTS idx_cr_b ON concept_relations(concept_b);

-- Track extraction progress for --resume
CREATE TABLE IF NOT EXISTS extraction_progress (
    source_type TEXT,
    source_id INTEGER,
    extracted_at TEXT DEFAULT (datetime('now')),
    PRIMARY KEY(source_type, source_id)
);
"""

def migrate():
    conn = sqlite3.connect(DB_PATH)
    print(f"Migrating {DB_PATH}...")
    conn.executescript(SCHEMA)
    conn.commit()
    for table in ['concepts', 'concept_sources', 'concept_relations', 'extraction_progress']:
        cnt = conn.execute(f"SELECT count(*) FROM {table}").fetchone()[0]
        print(f"  {table}: {cnt} rows")
    conn.close()
    print("Done.")

if __name__ == '__main__':
    migrate()
```

**Step 2: Run migration**

Run: `/usr/local/opt/python@3.11/bin/python3.11 scripts/migrate_concepts.py`
Expected: All 4 tables created with 0 rows.

**Step 3: Commit**

```bash
git add scripts/migrate_concepts.py
git commit -m "feat: add concepts/relations tables migration"
```

---

### Task 2: Concept Extraction Script

**Files:**
- Create: `scripts/extract_concepts.py`

**Step 1: Write the extraction script**

This is the largest new file. Key aspects:
- Per-article DeepSeek calls (no batching)
- JSON response parsing with fallback
- Concept deduplication via exact match + synonym dict
- `--resume` support via `extraction_progress` table
- Post-processing to compute `mention_count`, `first_seen_year`, `peak_year`

```python
#!/usr/bin/env python3
"""Extract concepts from articles and books using DeepSeek API.

Usage:
    python3.11 extract_concepts.py           # full run
    python3.11 extract_concepts.py --resume  # continue from last
    python3.11 extract_concepts.py --post    # just post-processing
"""
import os, sys, json, time, sqlite3, argparse, re

RESEARCH_DIR = os.path.join(os.path.dirname(__file__), '..', 'research')
DB_PATH = os.path.join(RESEARCH_DIR, 'corpus.db')

# Synonym normalization map
SYNONYMS = {
    "phenomenal consciousness": "consciousness",
    "phenomenal experience": "consciousness",
    "subjective experience": "consciousness",
    "the hard problem": "hard problem of consciousness",
    "hard problem": "hard problem of consciousness",
    "p-zombies": "philosophical zombie",
    "p-zombie": "philosophical zombie",
    "chinese room argument": "chinese room",
    "turing machine": "turing test",  # keep separate actually
    "artificial general intelligence": "agi",
    "strong ai": "agi",
    "superintelligent ai": "superintelligence",
    "neural network": "neural networks",
    "deep learning": "neural networks",
    "language model": "large language models",
    "llm": "large language models",
    "llms": "large language models",
    "gpt": "large language models",
    "free will problem": "free will",
    "libertarian free will": "free will",
    "qualia": "qualia",
    "intentionality": "intentionality",
    "embodied cognition": "embodiment",
    "embodied ai": "embodiment",
    "symbol grounding": "symbol grounding problem",
    "grounding problem": "symbol grounding problem",
    "functionalism": "functionalism",
    "computational functionalism": "functionalism",
    "machine functionalism": "functionalism",
    "ethical ai": "ai ethics",
    "ai alignment": "alignment",
    "value alignment": "alignment",
    "existential risk": "existential risk",
    "x-risk": "existential risk",
    "paradigm shift": "paradigm",
    "scientific revolution": "paradigm",
    "falsifiability": "falsificationism",
    "falsification": "falsificationism",
}

PROMPT_TEMPLATE = """From this text, extract exactly 5 key philosophical or technical concepts that are central to the argument.

For each concept provide (as JSON):
- "name": English canonical form, lowercase, 1-3 words
- "name_zh": Chinese translation
- "relevance": 0.0-1.0 how central to this text
- "context": one sentence from the text showing how it discusses this concept
- "category": one of "philosophy", "ai", "science", "methodology", "ethics"

Also identify up to 3 relations between the extracted concepts:
- "a": concept name
- "b": concept name
- "relation": one of "extends", "critiques", "requires", "contrasts", "exemplifies"
- "strength": 0.0-1.0

Return ONLY valid JSON: {{"concepts": [...], "relations": [...]}}

Title: {title} by {author} ({year})
{text}"""


def get_client():
    from openai import OpenAI
    key = os.environ.get('DEEPSEEK_API_KEY', 'sk-1556a07369cf474f8e886c130e3584ca')
    return OpenAI(api_key=key, base_url='https://api.deepseek.com')


def normalize_concept_name(name):
    """Normalize concept name: lowercase, strip, synonym merge."""
    name = name.strip().lower()
    name = re.sub(r'\s+', ' ', name)
    return SYNONYMS.get(name, name)


def parse_response(text):
    """Parse DeepSeek JSON response with fallback."""
    # Try to extract JSON from response
    text = text.strip()
    # Remove markdown code fences if present
    if text.startswith('```'):
        text = re.sub(r'^```(?:json)?\s*', '', text)
        text = re.sub(r'\s*```$', '', text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Try to find JSON object in text
        m = re.search(r'\{[\s\S]*\}', text)
        if m:
            try:
                return json.loads(m.group())
            except json.JSONDecodeError:
                pass
    return None


def get_or_create_concept(conn, name, name_zh=None, description=None, category=None):
    """Get existing concept or create new one. Returns concept_id."""
    name = normalize_concept_name(name)
    if not name or len(name) < 2:
        return None

    c = conn.cursor()
    c.execute('SELECT id FROM concepts WHERE name = ?', (name,))
    row = c.fetchone()
    if row:
        # Update zh/description if we have better data
        if name_zh:
            c.execute('UPDATE concepts SET name_zh = COALESCE(name_zh, ?) WHERE id = ?', (name_zh, row[0]))
        if description and len(description) > 10:
            c.execute('UPDATE concepts SET description = COALESCE(description, ?) WHERE id = ?', (description, row[0]))
        if category:
            c.execute('UPDATE concepts SET category = COALESCE(category, ?) WHERE id = ?', (category, row[0]))
        return row[0]

    c.execute('INSERT INTO concepts (name, name_zh, description, category) VALUES (?,?,?,?)',
              (name, name_zh, description, category))
    return c.lastrowid


def process_source(conn, client, source_type, source_id, title, author, year, text):
    """Extract concepts from a single source."""
    if not text or len(text.strip()) < 100:
        return 0

    text_truncated = text[:1500]
    prompt = PROMPT_TEMPLATE.format(
        title=title or 'Unknown',
        author=author or 'Unknown',
        year=year or '',
        text=text_truncated
    )

    try:
        r = client.chat.completions.create(
            model='deepseek-chat',
            max_tokens=800,
            temperature=0.3,
            messages=[{'role': 'user', 'content': prompt}]
        )
        data = parse_response(r.choices[0].message.content)
        if not data or 'concepts' not in data:
            return 0
    except Exception as e:
        print(f"    API error: {e}")
        time.sleep(2)
        return 0

    c = conn.cursor()
    concepts_added = 0
    concept_name_to_id = {}

    for concept in data.get('concepts', [])[:5]:
        name = concept.get('name', '').strip()
        if not name:
            continue

        cid = get_or_create_concept(
            conn,
            name,
            name_zh=concept.get('name_zh'),
            description=concept.get('context'),
            category=concept.get('category')
        )
        if not cid:
            continue

        normalized = normalize_concept_name(name)
        concept_name_to_id[normalized] = cid

        # Check if link already exists
        c.execute('SELECT id FROM concept_sources WHERE concept_id=? AND source_type=? AND source_id=?',
                  (cid, source_type, source_id))
        if not c.fetchone():
            c.execute('INSERT INTO concept_sources (concept_id, source_type, source_id, relevance, context) VALUES (?,?,?,?,?)',
                      (cid, source_type, source_id,
                       concept.get('relevance', 0.5),
                       (concept.get('context') or '')[:200]))
            concepts_added += 1

    # Process relations
    for rel in data.get('relations', [])[:3]:
        a_name = normalize_concept_name(rel.get('a', ''))
        b_name = normalize_concept_name(rel.get('b', ''))
        a_id = concept_name_to_id.get(a_name)
        b_id = concept_name_to_id.get(b_name)
        if a_id and b_id and a_id != b_id:
            # Ensure consistent ordering
            if a_id > b_id:
                a_id, b_id = b_id, a_id
            try:
                c.execute('INSERT OR IGNORE INTO concept_relations (concept_a, concept_b, relation, strength) VALUES (?,?,?,?)',
                          (a_id, b_id, rel.get('relation', 'related'), rel.get('strength', 0.5)))
            except Exception:
                pass

    # Mark as processed
    c.execute('INSERT OR REPLACE INTO extraction_progress (source_type, source_id) VALUES (?,?)',
              (source_type, source_id))

    return concepts_added


def post_process(conn):
    """Compute mention_count, first_seen_year, peak_year for all concepts."""
    c = conn.cursor()

    print("Post-processing: computing mention counts...")
    c.execute('''
        UPDATE concepts SET mention_count = (
            SELECT COUNT(*) FROM concept_sources WHERE concept_id = concepts.id
        )
    ''')

    print("Post-processing: computing first_seen_year...")
    # For articles: use date field; for books: use year field
    c.execute('''
        UPDATE concepts SET first_seen_year = (
            SELECT MIN(
                CASE
                    WHEN cs.source_type = 'article' THEN SUBSTR(a.date, -4)
                    WHEN cs.source_type = 'book' THEN b.year
                END
            )
            FROM concept_sources cs
            LEFT JOIN articles a ON cs.source_type = 'article' AND cs.source_id = a.id
            LEFT JOIN books b ON cs.source_type = 'book' AND cs.source_id = b.id
            WHERE cs.concept_id = concepts.id
        )
    ''')

    print("Post-processing: computing peak_year...")
    # peak_year = year with most mentions (simplified: use most common year)
    c.execute('''
        UPDATE concepts SET peak_year = (
            SELECT yr FROM (
                SELECT
                    CASE
                        WHEN cs.source_type = 'article' THEN SUBSTR(a.date, -4)
                        WHEN cs.source_type = 'book' THEN b.year
                    END as yr,
                    COUNT(*) as cnt
                FROM concept_sources cs
                LEFT JOIN articles a ON cs.source_type = 'article' AND cs.source_id = a.id
                LEFT JOIN books b ON cs.source_type = 'book' AND cs.source_id = b.id
                WHERE cs.concept_id = concepts.id AND yr IS NOT NULL
                GROUP BY yr ORDER BY cnt DESC LIMIT 1
            )
        )
    ''')

    # Remove concepts with 0 mentions (shouldn't happen but safety)
    c.execute('DELETE FROM concepts WHERE mention_count = 0')

    conn.commit()

    # Stats
    total_concepts = c.execute('SELECT count(*) FROM concepts').fetchone()[0]
    total_sources = c.execute('SELECT count(*) FROM concept_sources').fetchone()[0]
    total_relations = c.execute('SELECT count(*) FROM concept_relations').fetchone()[0]
    print(f"\nFinal stats:")
    print(f"  Concepts: {total_concepts}")
    print(f"  Concept-source links: {total_sources}")
    print(f"  Concept relations: {total_relations}")

    # Top concepts
    print("\nTop 20 concepts:")
    for row in c.execute('SELECT name, name_zh, mention_count, category FROM concepts ORDER BY mention_count DESC LIMIT 20'):
        print(f"  [{row[3]}] {row[0]} ({row[1]}) - {row[2]} mentions")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--resume', action='store_true', help='Resume from last processed')
    parser.add_argument('--post', action='store_true', help='Only run post-processing')
    parser.add_argument('--limit', type=int, default=0, help='Limit number of sources to process')
    args = parser.parse_args()

    conn = sqlite3.connect(DB_PATH, timeout=30)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.row_factory = sqlite3.Row

    if args.post:
        post_process(conn)
        conn.close()
        return

    client = get_client()

    # Get already processed IDs
    already_done = set()
    if args.resume:
        for row in conn.execute('SELECT source_type, source_id FROM extraction_progress'):
            already_done.add((row['source_type'], row['source_id']))
        print(f"Resuming: {len(already_done)} already processed")

    # Process articles
    articles = conn.execute('''
        SELECT id, title, author, date, abstract, content
        FROM articles
        WHERE (abstract IS NOT NULL AND length(abstract) > 50)
           OR (content IS NOT NULL AND length(content) > 100)
        ORDER BY id
    ''').fetchall()

    total = len(articles)
    processed = 0
    skipped = 0

    print(f"\n=== Processing {total} articles ===")
    for i, a in enumerate(articles):
        if args.limit and processed >= args.limit:
            break
        if ('article', a['id']) in already_done:
            skipped += 1
            continue

        text = a['content'] or a['abstract'] or ''
        text = text[:1500]

        n = process_source(conn, client, 'article', a['id'],
                          a['title'], a['author'], a['date'], text)
        processed += 1

        if processed % 10 == 0:
            conn.commit()
            concepts_so_far = conn.execute('SELECT count(*) FROM concepts').fetchone()[0]
            print(f"  [{processed}/{total-skipped}] +{n} concepts (total unique: {concepts_so_far})")

        # Rate limit: ~1 req/sec
        time.sleep(0.5)

    conn.commit()
    print(f"\nArticles done: {processed} processed, {skipped} skipped")

    # Process books
    books = conn.execute('''
        SELECT b.id, b.title, b.author, b.year, b.overview,
               (SELECT GROUP_CONCAT(title, '; ') FROM book_chapters WHERE book_id = b.id ORDER BY chapter_num LIMIT 5) as ch_titles
        FROM books b
        ORDER BY b.id
    ''').fetchall()

    print(f"\n=== Processing {len(books)} books ===")
    for b in books:
        if args.limit and processed >= args.limit:
            break
        if ('book', b['id']) in already_done:
            continue

        # Use overview if available, else chapter titles
        text = b['overview'] or ''
        if not text and b['ch_titles']:
            text = f"Book: {b['title']} by {b['author']}. Chapters: {b['ch_titles']}"
        if len(text) < 50:
            # Get first chapter content
            ch = conn.execute('SELECT content FROM book_chapters WHERE book_id = ? ORDER BY chapter_num LIMIT 1', (b['id'],)).fetchone()
            if ch and ch['content']:
                text = ch['content'][:1500]

        n = process_source(conn, client, 'book', b['id'],
                          b['title'], b['author'], b['year'], text)
        processed += 1
        print(f"  Book {b['id']}: {b['title'][:40]} → +{n} concepts")
        time.sleep(0.5)

    conn.commit()

    # Post-process
    post_process(conn)
    conn.close()
    print("\nExtraction complete!")


if __name__ == '__main__':
    sys.stdout.reconfigure(line_buffering=True)
    main()
```

**Step 2: Run with --limit to test**

Run: `/usr/local/opt/python@3.11/bin/python3.11 scripts/extract_concepts.py --limit 5`
Expected: 5 articles processed, ~15-25 concepts created, concepts and relations in DB.

**Step 3: Verify DB**

Run: `/usr/local/opt/python@3.11/bin/python3.11 -c "import sqlite3; conn=sqlite3.connect('research/corpus.db'); print(conn.execute('SELECT count(*) FROM concepts').fetchone()[0], 'concepts'); print(conn.execute('SELECT count(*) FROM concept_sources').fetchone()[0], 'links')"`
Expected: Non-zero counts.

**Step 4: Commit**

```bash
git add scripts/extract_concepts.py
git commit -m "feat: add concept extraction pipeline with DeepSeek"
```

---

### Task 3: Run Full Extraction

**Step 1: Run extraction for all articles + books**

Run: `/usr/local/opt/python@3.11/bin/python3.11 scripts/extract_concepts.py --resume`
Expected: ~2-3 hours, ~2700+ sources processed.

This should be run in background. If interrupted, re-run with `--resume` to continue.

**Step 2: Run post-processing to verify**

Run: `/usr/local/opt/python@3.11/bin/python3.11 scripts/extract_concepts.py --post`
Expected: Stats printed showing 300-500 concepts, ~8000 links, ~1000 relations.

**Step 3: Commit DB state note**

No code commit needed. This is a data-only step.

---

### Task 4: Graph API Endpoints

**Files:**
- Modify: `scripts/serve_research.py` (add 4 new API routes before Notes API section)

**Step 1: Add graph data endpoint**

Insert before the `# ─── Notes API` line in `serve_research.py`:

```python
# ─── Concept Graph API ────────────────────────────────────────────

@app.route('/api/graph')
def api_graph():
    conn = get_db()
    c = conn.cursor()

    min_mentions = request.args.get('min_mentions', 3, type=int)
    category = request.args.get('category')
    year_start = request.args.get('year_start')
    year_end = request.args.get('year_end')

    where = ['mention_count >= ?']
    params = [min_mentions]

    if category:
        where.append('category = ?')
        params.append(category)
    if year_start:
        where.append("(first_seen_year IS NULL OR first_seen_year >= ?)")
        params.append(year_start)
    if year_end:
        where.append("(first_seen_year IS NULL OR first_seen_year <= ?)")
        params.append(year_end)

    where_clause = ' AND '.join(where)

    c.execute(f'''SELECT id, name, name_zh, category, mention_count,
                         first_seen_year, peak_year, description
                  FROM concepts WHERE {where_clause}
                  ORDER BY mention_count DESC''', params)
    nodes = [dict(r) for r in c.fetchall()]
    node_ids = {n['id'] for n in nodes}

    # Get edges between visible nodes
    edges = []
    if node_ids:
        placeholders = ','.join('?' * len(node_ids))
        c.execute(f'''SELECT concept_a as source, concept_b as target, relation, strength
                      FROM concept_relations
                      WHERE concept_a IN ({placeholders}) AND concept_b IN ({placeholders})''',
                  list(node_ids) + list(node_ids))
        edges = [dict(r) for r in c.fetchall()]

    conn.close()
    return jsonify({'nodes': nodes, 'edges': edges})


@app.route('/api/concepts')
def api_concepts():
    conn = get_db()
    c = conn.cursor()

    sort = request.args.get('sort', 'mention_count')
    category = request.args.get('category')
    limit = request.args.get('limit', 100, type=int)

    where = []
    params = []
    if category:
        where.append('category = ?')
        params.append(category)

    where_clause = 'WHERE ' + ' AND '.join(where) if where else ''
    order = 'mention_count DESC' if sort == 'mention_count' else 'name ASC'

    c.execute(f'''SELECT id, name, name_zh, category, mention_count, first_seen_year
                  FROM concepts {where_clause}
                  ORDER BY {order} LIMIT ?''', params + [limit])
    results = [dict(r) for r in c.fetchall()]
    conn.close()
    return jsonify(results)


@app.route('/api/concept/<int:concept_id>')
def api_concept_detail(concept_id):
    conn = get_db()
    c = conn.cursor()

    c.execute('SELECT * FROM concepts WHERE id = ?', (concept_id,))
    concept = c.fetchone()
    if not concept:
        conn.close()
        return jsonify({'error': 'not found'}), 404

    result = dict(concept)

    # Sources
    c.execute('''SELECT cs.source_type, cs.source_id, cs.relevance, cs.context,
                        CASE WHEN cs.source_type = 'article' THEN a.title
                             WHEN cs.source_type = 'book' THEN b.title END as title,
                        CASE WHEN cs.source_type = 'article' THEN a.author
                             WHEN cs.source_type = 'book' THEN b.author END as author
                 FROM concept_sources cs
                 LEFT JOIN articles a ON cs.source_type = 'article' AND cs.source_id = a.id
                 LEFT JOIN books b ON cs.source_type = 'book' AND cs.source_id = b.id
                 WHERE cs.concept_id = ?
                 ORDER BY cs.relevance DESC''', (concept_id,))
    result['sources'] = [dict(r) for r in c.fetchall()]

    # Related concepts
    c.execute('''SELECT c2.id, c2.name, c2.name_zh, c2.mention_count, cr.relation, cr.strength
                 FROM concept_relations cr
                 JOIN concepts c2 ON (cr.concept_b = c2.id AND cr.concept_a = ?)
                                  OR (cr.concept_a = c2.id AND cr.concept_b = ?)
                 ORDER BY cr.strength DESC''', (concept_id, concept_id))
    result['related'] = [dict(r) for r in c.fetchall()]

    conn.close()
    return jsonify(result)


@app.route('/api/concept-map')
def api_concept_map():
    """Return topic -> concept aggregation for sidebar bubble chart."""
    conn = get_db()
    c = conn.cursor()

    # Get topics with their article/book counts
    topic_data = {}

    for row in c.execute('SELECT topics FROM articles WHERE topics IS NOT NULL'):
        try:
            for t in json.loads(row['topics']):
                if t not in topic_data:
                    topic_data[t] = {'count': 0, 'concepts': {}}
                topic_data[t]['count'] += 1
        except (json.JSONDecodeError, TypeError):
            pass

    for row in c.execute('SELECT topics FROM books WHERE topics IS NOT NULL'):
        try:
            for t in json.loads(row['topics']):
                if t not in topic_data:
                    topic_data[t] = {'count': 0, 'concepts': {}}
                topic_data[t]['count'] += 1
        except (json.JSONDecodeError, TypeError):
            pass

    # Map concepts to topics via their sources
    c.execute('''
        SELECT c.id, c.name, c.name_zh, c.mention_count,
               cs.source_type, cs.source_id
        FROM concepts c
        JOIN concept_sources cs ON c.id = cs.concept_id
        WHERE c.mention_count >= 2
    ''')
    for row in c.fetchall():
        # Get topics of this source
        if row['source_type'] == 'article':
            src = conn.execute('SELECT topics FROM articles WHERE id = ?', (row['source_id'],)).fetchone()
        else:
            src = conn.execute('SELECT topics FROM books WHERE id = ?', (row['source_id'],)).fetchone()
        if src and src['topics']:
            try:
                for t in json.loads(src['topics']):
                    if t in topic_data:
                        cname = row['name']
                        if cname not in topic_data[t]['concepts']:
                            topic_data[t]['concepts'][cname] = {
                                'id': row['id'], 'name': row['name'],
                                'name_zh': row['name_zh'],
                                'mention_count': row['mention_count']
                            }
            except (json.JSONDecodeError, TypeError):
                pass

    # Format result
    result = []
    for topic, data in sorted(topic_data.items(), key=lambda x: -x[1]['count']):
        result.append({
            'topic': topic,
            'count': data['count'],
            'concepts': sorted(data['concepts'].values(), key=lambda x: -x['mention_count'])[:10]
        })

    conn.close()
    return jsonify(result)
```

**Step 2: Verify APIs work**

Run: `curl -s http://localhost:8765/api/graph?min_mentions=2 | python3.11 -c "import json,sys;d=json.load(sys.stdin);print(len(d['nodes']),'nodes',len(d['edges']),'edges')"`
Expected: Non-zero node and edge counts.

Run: `curl -s http://localhost:8765/api/concepts?limit=5 | python3.11 -c "import json,sys;[print(c['name'],c['mention_count']) for c in json.load(sys.stdin)]"`
Expected: 5 concepts listed.

**Step 3: Commit**

```bash
git add scripts/serve_research.py
git commit -m "feat: add graph/concept API endpoints"
```

---

### Task 5: Frontend — CSS for Graph View

**Files:**
- Modify: `scripts/serve_research.py` (add CSS before `</style>` closing tag)

**Step 1: Add graph CSS**

Insert before the `</style>` tag:

```css
/* Knowledge Graph */
.graph-container { position: relative; width: 100%; height: 100%; overflow: hidden; }
.graph-container svg { width: 100%; height: 100%; }
.graph-controls { position: absolute; top: 10px; left: 10px; right: 10px;
                  display: flex; gap: 8px; align-items: center; flex-wrap: wrap;
                  background: rgba(13,17,23,0.9); padding: 8px 12px; border-radius: 8px;
                  border: 1px solid var(--border); z-index: 10; }
.graph-controls label { font-size: 11px; color: var(--text-dim); display: flex; align-items: center; gap: 4px; }
.graph-controls input[type="range"] { width: 80px; accent-color: var(--accent); }
.graph-controls input[type="text"] { background: var(--bg); border: 1px solid var(--border);
                                      color: var(--text); padding: 4px 8px; border-radius: 4px;
                                      font-size: 11px; width: 140px; }
.graph-controls select { background: var(--bg); border: 1px solid var(--border);
                          color: var(--text); padding: 4px; border-radius: 4px; font-size: 11px; }

.graph-node { cursor: pointer; }
.graph-node circle { stroke: var(--border); stroke-width: 1.5px; transition: r 0.2s; }
.graph-node:hover circle { stroke: #fff; stroke-width: 2px; }
.graph-node text { fill: var(--text); font-size: 10px; pointer-events: none; }
.graph-edge { stroke: var(--border); stroke-opacity: 0.4; }
.graph-edge.highlight { stroke: var(--accent); stroke-opacity: 0.8; }
.graph-node.highlight circle { stroke: var(--accent); stroke-width: 3px; }
.graph-node.dimmed { opacity: 0.2; }
.graph-edge.dimmed { stroke-opacity: 0.05; }

/* Concept detail panel (overlay on right side of graph) */
.concept-detail { position: absolute; top: 60px; right: 10px; width: 300px; max-height: calc(100% - 80px);
                  background: var(--surface); border: 1px solid var(--border); border-radius: 8px;
                  padding: 16px; overflow-y: auto; z-index: 10; font-size: 13px; }
.concept-detail h2 { font-size: 16px; color: var(--accent); margin-bottom: 4px; }
.concept-detail .concept-zh { color: var(--text-dim); font-size: 13px; margin-bottom: 8px; }
.concept-detail .concept-desc { margin-bottom: 12px; color: var(--text); line-height: 1.5; }
.concept-detail .concept-meta { font-size: 11px; color: var(--text-dim); margin-bottom: 12px; }
.concept-detail .concept-source { padding: 4px 0; border-bottom: 1px solid var(--border);
                                   cursor: pointer; font-size: 12px; }
.concept-detail .concept-source:hover { color: var(--accent); }
.concept-detail h3 { font-size: 12px; color: var(--accent); margin: 12px 0 6px; }

/* Concept bubble map in sidebar */
.bubble-map { width: 100%; height: 300px; }
.bubble-map circle { cursor: pointer; stroke: var(--border); stroke-width: 1px; }
.bubble-map circle:hover { stroke: #fff; }
.bubble-map text { fill: var(--text); font-size: 9px; pointer-events: none; text-anchor: middle; }
```

**Step 2: Commit**

```bash
git add scripts/serve_research.py
git commit -m "feat: add knowledge graph CSS styles"
```

---

### Task 6: Frontend — D3.js Graph Rendering

**Files:**
- Modify: `scripts/serve_research.py`

**Step 1: Add D3.js CDN to HTML `<head>`**

In the HTML_TEMPLATE, after the `</style>` and before `</head>`, add:
```html
<script src="https://d3js.org/d3.v7.min.js"></script>
```

**Step 2: Add Graph mode tab to sidebar**

In the `renderSidebar` function, modify the mode tabs section to add Graph:

```javascript
html += `<div class="mode-tab" onclick="switchMode('graph')" ${browseMode==='graph'?'class="active"':''}>Graph</div>`;
```

**Step 3: Add switchMode handler for graph**

In the `switchMode` function, add graph case:

```javascript
} else if (mode === 'graph') {
    loadGraph();
}
```

Also render sidebar concepts when in graph mode (within renderSidebar):

```javascript
if (browseMode === 'graph') {
    html += '<h3>Concepts</h3>';
    html += '<div id="conceptBubbles"></div>';
    // Will be populated by loadConceptMap()
}
```

**Step 4: Write the graph rendering JavaScript**

Add before `init();` at the end of the script:

```javascript
// ─── Knowledge Graph ─────────────────────────────────────
let graphSimulation = null;
let graphData = null;

async function loadGraph() {
  // Replace list+reading panels with graph container
  document.getElementById('listPanel').innerHTML = '';
  document.getElementById('listPanel').style.display = 'none';

  const panel = document.getElementById('readingPanel');
  panel.style.gridColumn = '2 / -1';  // span full width
  panel.innerHTML = `
    <div class="graph-container" id="graphContainer">
      <div class="graph-controls">
        <label>Min mentions: <input type="range" id="graphMinMentions" min="1" max="20" value="3"
               oninput="this.nextElementSibling.textContent=this.value;refreshGraph()"><span>3</span></label>
        <label>Category: <select id="graphCategory" onchange="refreshGraph()">
          <option value="">All</option>
          <option value="philosophy">Philosophy</option>
          <option value="ai">AI</option>
          <option value="science">Science</option>
          <option value="methodology">Methodology</option>
          <option value="ethics">Ethics</option>
        </select></label>
        <label><input type="text" id="graphSearch" placeholder="Search concept..."
               oninput="highlightConcept(this.value)"></label>
      </div>
      <svg id="graphSvg"></svg>
    </div>`;

  await refreshGraph();
  loadConceptMap();
}

async function refreshGraph() {
  const min = document.getElementById('graphMinMentions')?.value || 3;
  const cat = document.getElementById('graphCategory')?.value || '';

  const params = new URLSearchParams({min_mentions: min});
  if (cat) params.set('category', cat);

  const resp = await fetch('/api/graph?' + params.toString());
  graphData = await resp.json();
  renderGraph(graphData);
}

const categoryColors = {
  philosophy: '#58a6ff', ai: '#f0883e', science: '#7ee787',
  methodology: '#d2a8ff', ethics: '#f97583'
};

function renderGraph(data) {
  const container = document.getElementById('graphContainer');
  if (!container) return;
  const svg = d3.select('#graphSvg');
  svg.selectAll('*').remove();

  const width = container.clientWidth;
  const height = container.clientHeight - 50;

  svg.attr('viewBox', [0, 0, width, height]);

  const g = svg.append('g');

  // Zoom
  svg.call(d3.zoom().scaleExtent([0.2, 5]).on('zoom', (e) => g.attr('transform', e.transform)));

  // Scale for node size
  const maxMentions = Math.max(...data.nodes.map(n => n.mention_count), 1);
  const sizeScale = d3.scaleSqrt().domain([1, maxMentions]).range([5, 30]);

  // Edges
  const edgeMap = {};
  data.edges.forEach(e => {
    edgeMap[e.source + '-' + e.target] = e;
    edgeMap[e.target + '-' + e.source] = e;
  });

  const links = g.append('g')
    .selectAll('line')
    .data(data.edges)
    .join('line')
    .attr('class', 'graph-edge')
    .attr('stroke-width', d => Math.max(1, d.strength * 3))
    .attr('stroke-dasharray', d => {
      if (d.relation === 'critiques') return '4,4';
      if (d.relation === 'requires') return '2,2';
      return null;
    });

  // Nodes
  const nodeGroup = g.append('g')
    .selectAll('g')
    .data(data.nodes)
    .join('g')
    .attr('class', 'graph-node')
    .call(d3.drag()
      .on('start', (e, d) => { if (!e.active) graphSimulation.alphaTarget(0.3).restart(); d.fx = d.x; d.fy = d.y; })
      .on('drag', (e, d) => { d.fx = e.x; d.fy = e.y; })
      .on('end', (e, d) => { if (!e.active) graphSimulation.alphaTarget(0); d.fx = null; d.fy = null; })
    );

  nodeGroup.append('circle')
    .attr('r', d => sizeScale(d.mention_count))
    .attr('fill', d => categoryColors[d.category] || '#8b949e');

  nodeGroup.append('text')
    .attr('dy', d => sizeScale(d.mention_count) + 12)
    .attr('text-anchor', 'middle')
    .text(d => document.getElementById('showZh')?.checked ? (d.name_zh || d.name) : d.name);

  // Hover highlight
  nodeGroup.on('mouseover', function(e, d) {
    const connected = new Set();
    data.edges.forEach(edge => {
      if (edge.source.id === d.id || edge.source === d.id) connected.add(edge.target.id || edge.target);
      if (edge.target.id === d.id || edge.target === d.id) connected.add(edge.source.id || edge.source);
    });
    connected.add(d.id);

    nodeGroup.classed('dimmed', n => !connected.has(n.id));
    links.classed('dimmed', l => {
      const s = l.source.id || l.source;
      const t = l.target.id || l.target;
      return s !== d.id && t !== d.id;
    });
    links.classed('highlight', l => {
      const s = l.source.id || l.source;
      const t = l.target.id || l.target;
      return s === d.id || t === d.id;
    });
  }).on('mouseout', function() {
    nodeGroup.classed('dimmed', false);
    links.classed('dimmed', false).classed('highlight', false);
  });

  // Click to show detail
  nodeGroup.on('click', (e, d) => showConceptDetail(d.id));

  // Force simulation
  graphSimulation = d3.forceSimulation(data.nodes)
    .force('link', d3.forceLink(data.edges).id(d => d.id).distance(100))
    .force('charge', d3.forceManyBody().strength(-200))
    .force('center', d3.forceCenter(width / 2, height / 2))
    .force('collision', d3.forceCollide().radius(d => sizeScale(d.mention_count) + 5))
    .on('tick', () => {
      links
        .attr('x1', d => d.source.x).attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x).attr('y2', d => d.target.y);
      nodeGroup.attr('transform', d => `translate(${d.x},${d.y})`);
    });
}

async function showConceptDetail(conceptId) {
  // Remove existing detail panel
  document.querySelector('.concept-detail')?.remove();

  const resp = await fetch(`/api/concept/${conceptId}`);
  const c = await resp.json();

  let html = `<div class="concept-detail">
    <button onclick="this.parentElement.remove()" style="float:right;background:none;border:none;color:var(--text-dim);cursor:pointer;font-size:16px">&times;</button>
    <h2>${escHtml(c.name)}</h2>
    ${c.name_zh ? '<div class="concept-zh">' + escHtml(c.name_zh) + '</div>' : ''}
    ${c.description ? '<div class="concept-desc">' + escHtml(c.description) + '</div>' : ''}
    <div class="concept-meta">
      <span>${c.mention_count} mentions</span>
      ${c.category ? ' &middot; <span>' + c.category + '</span>' : ''}
      ${c.first_seen_year ? ' &middot; <span>Since ' + c.first_seen_year + '</span>' : ''}
    </div>`;

  if (c.related && c.related.length) {
    html += '<h3>Related Concepts</h3>';
    c.related.forEach(r => {
      html += `<div class="concept-source" onclick="showConceptDetail(${r.id})">
        ${escHtml(r.name)} <span style="color:var(--text-dim)">(${r.relation}, ${r.mention_count})</span></div>`;
    });
  }

  if (c.sources && c.sources.length) {
    html += '<h3>Sources (' + c.sources.length + ')</h3>';
    c.sources.slice(0, 15).forEach(s => {
      const onclick = s.source_type === 'article' ? `loadArticle(${s.source_id})` : `loadBook(${s.source_id})`;
      html += `<div class="concept-source" onclick="switchMode('${s.source_type === 'article' ? 'articles' : 'books'}');${onclick}">
        <span style="color:var(--orange);font-size:10px">${s.source_type}</span>
        ${escHtml(s.title || '')} <span style="color:var(--text-dim)">- ${escHtml(s.author || '')}</span>
      </div>`;
    });
    if (c.sources.length > 15) {
      html += `<div style="color:var(--text-dim);font-size:11px">...and ${c.sources.length - 15} more</div>`;
    }
  }

  html += '</div>';
  document.getElementById('graphContainer').insertAdjacentHTML('beforeend', html);
}

function highlightConcept(query) {
  if (!graphData) return;
  query = query.toLowerCase().trim();
  d3.selectAll('.graph-node').classed('highlight', function(d) {
    return query && (d.name.includes(query) || (d.name_zh && d.name_zh.includes(query)));
  });
}

async function loadConceptMap() {
  const resp = await fetch('/api/concept-map');
  const data = await resp.json();
  const container = document.getElementById('conceptBubbles');
  if (!container) return;

  // Simple list view for sidebar (bubble chart too complex for 200px width)
  let html = '';
  data.slice(0, 15).forEach(t => {
    const zh = topicZh[t.topic] || t.topic;
    html += `<div style="margin-bottom:8px">
      <div class="filter-item" onclick="document.getElementById('graphCategory').value='';document.getElementById('graphSearch').value='${t.topic}';highlightConcept('${t.topic}')">
        <strong>${zh}</strong> <span class="count">${t.count}</span>
      </div>`;
    t.concepts.slice(0, 5).forEach(c => {
      html += `<div style="padding:1px 6px 1px 16px;font-size:11px;color:var(--text-dim);cursor:pointer"
                   onclick="showConceptDetail(${c.id})">
        ${escHtml(c.name)} <span style="font-size:9px">(${c.mention_count})</span></div>`;
    });
    html += '</div>';
  });
  container.innerHTML = html;
}
```

**Step 5: Fix switchMode to restore panels when leaving graph**

Modify the `switchMode` function to handle graph → non-graph transitions:

```javascript
async function switchMode(mode) {
  // Restore panels if leaving graph mode
  if (browseMode === 'graph' && mode !== 'graph') {
    document.getElementById('listPanel').style.display = '';
    document.getElementById('readingPanel').style.gridColumn = '';
  }
  browseMode = mode;
  currentFilters = {};
  const resp = await fetch('/api/filters');
  const data = await resp.json();
  renderSidebar(data);
  if (mode === 'books') {
    loadBooks({});
  } else if (mode === 'graph') {
    loadGraph();
  } else {
    loadArticles({sort: 'importance'});
  }
}
```

**Step 6: Start server and verify graph renders**

Run: restart server and navigate to http://localhost:8765, click "Graph" tab.
Expected: D3 force graph visible with concept nodes, edges, hover highlights, click detail panel.

**Step 7: Commit**

```bash
git add scripts/serve_research.py
git commit -m "feat: add interactive D3.js knowledge graph visualization"
```

---

### Task 7: Verification

**Step 1: End-to-end verification checklist**

1. `GET /api/graph?min_mentions=2` → returns nodes + edges
2. `GET /api/concepts?limit=10` → returns concept list
3. `GET /api/concept/1` → returns concept detail with sources and relations
4. `GET /api/concept-map` → returns topic-concept aggregation
5. Browser: Click "Graph" → force graph renders
6. Browser: Hover node → connected nodes highlight
7. Browser: Click node → detail panel shows with sources
8. Browser: Adjust min mentions slider → graph updates
9. Browser: Filter by category → graph filters
10. Browser: Search box → matching nodes highlight
11. Browser: Switch back to Articles → panels restore

**Step 2: Final commit**

```bash
git add -A
git commit -m "feat: knowledge graph + concept index system complete"
```

---

## Summary

| Task | Description | Est. Time |
|------|-------------|-----------|
| 1 | DB migration (3 tables + indexes) | 2 min |
| 2 | Extraction script | 15 min |
| 3 | Run full extraction | 2-3 hours (background) |
| 4 | Graph API endpoints (4 routes) | 10 min |
| 5 | Graph CSS | 5 min |
| 6 | D3.js graph rendering + sidebar | 20 min |
| 7 | Verification | 10 min |

Total active coding: ~1 hour. Total wall clock: ~3-4 hours (extraction dominates).
