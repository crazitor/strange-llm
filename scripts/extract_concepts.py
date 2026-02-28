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
    return OpenAI(api_key=key, base_url='https://api.deepseek.com', timeout=60)


def normalize_concept_name(name):
    """Normalize concept name: lowercase, strip, synonym merge."""
    name = name.strip().lower()
    name = re.sub(r'\s+', ' ', name)
    return SYNONYMS.get(name, name)


def parse_response(text):
    """Parse DeepSeek JSON response with fallback."""
    text = text.strip()
    if text.startswith('```'):
        text = re.sub(r'^```(?:json)?\s*', '', text)
        text = re.sub(r'\s*```$', '', text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
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

        c.execute('SELECT id FROM concept_sources WHERE concept_id=? AND source_type=? AND source_id=?',
                  (cid, source_type, source_id))
        if not c.fetchone():
            c.execute('INSERT INTO concept_sources (concept_id, source_type, source_id, relevance, context) VALUES (?,?,?,?,?)',
                      (cid, source_type, source_id,
                       concept.get('relevance', 0.5),
                       (concept.get('context') or '')[:200]))
            concepts_added += 1

    for rel in data.get('relations', [])[:3]:
        a_name = normalize_concept_name(rel.get('a', ''))
        b_name = normalize_concept_name(rel.get('b', ''))
        a_id = concept_name_to_id.get(a_name)
        b_id = concept_name_to_id.get(b_name)
        if a_id and b_id and a_id != b_id:
            if a_id > b_id:
                a_id, b_id = b_id, a_id
            try:
                c.execute('INSERT OR IGNORE INTO concept_relations (concept_a, concept_b, relation, strength) VALUES (?,?,?,?)',
                          (a_id, b_id, rel.get('relation', 'related'), rel.get('strength', 0.5)))
            except Exception:
                pass

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

    c.execute('DELETE FROM concepts WHERE mention_count = 0')
    conn.commit()

    total_concepts = c.execute('SELECT count(*) FROM concepts').fetchone()[0]
    total_sources = c.execute('SELECT count(*) FROM concept_sources').fetchone()[0]
    total_relations = c.execute('SELECT count(*) FROM concept_relations').fetchone()[0]
    print(f"\nFinal stats:")
    print(f"  Concepts: {total_concepts}")
    print(f"  Concept-source links: {total_sources}")
    print(f"  Concept relations: {total_relations}")

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

        t0 = time.time()
        n = process_source(conn, client, 'article', a['id'],
                          a['title'], a['author'], a['date'], text)
        elapsed = time.time() - t0
        processed += 1
        conn.commit()

        if processed % 50 == 0:
            concepts_so_far = conn.execute('SELECT count(*) FROM concepts').fetchone()[0]
            print(f"  [{processed}/{total-skipped}] +{n} concepts (total unique: {concepts_so_far}) [{elapsed:.1f}s]")
        elif processed % 10 == 0:
            print(f"  [{processed}/{total-skipped}] ...", flush=True)

        time.sleep(0.3)

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

        text = b['overview'] or ''
        if not text and b['ch_titles']:
            text = f"Book: {b['title']} by {b['author']}. Chapters: {b['ch_titles']}"
        if len(text) < 50:
            ch = conn.execute('SELECT content FROM book_chapters WHERE book_id = ? ORDER BY chapter_num LIMIT 1', (b['id'],)).fetchone()
            if ch and ch['content']:
                text = ch['content'][:1500]

        n = process_source(conn, client, 'book', b['id'],
                          b['title'], b['author'], b['year'], text)
        processed += 1
        print(f"  Book {b['id']}: {b['title'][:40]} → +{n} concepts")
        time.sleep(0.5)

    conn.commit()

    post_process(conn)
    conn.close()
    print("\nExtraction complete!")


if __name__ == '__main__':
    sys.stdout.reconfigure(line_buffering=True)
    main()
