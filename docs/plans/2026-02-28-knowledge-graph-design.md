# Knowledge Graph + Concept Index Design

**Date**: 2026-02-28
**Goal**: Extract structured concepts from 2721 articles + 25 books, build interactive knowledge graph visualization and concept map.

---

## Data Model

### New Tables

```sql
CREATE TABLE concepts (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,              -- English canonical form, lowercase
    name_zh TEXT,                  -- Chinese name
    description TEXT,              -- One-sentence definition
    category TEXT,                 -- philosophy/ai/science/methodology
    first_seen_year TEXT,          -- Earliest year from sources
    peak_year TEXT,                -- Year with most mentions
    mention_count INTEGER DEFAULT 0
);

CREATE TABLE concept_sources (
    id INTEGER PRIMARY KEY,
    concept_id INTEGER REFERENCES concepts(id),
    source_type TEXT,              -- 'article' or 'book'
    source_id INTEGER,             -- articles.id or books.id
    relevance REAL DEFAULT 0.5,    -- 0-1
    context TEXT                   -- ~100 char extraction context
);

CREATE TABLE concept_relations (
    id INTEGER PRIMARY KEY,
    concept_a INTEGER REFERENCES concepts(id),
    concept_b INTEGER REFERENCES concepts(id),
    relation TEXT,                 -- extends/critiques/requires/contrasts/exemplifies
    strength REAL DEFAULT 0.5,
    UNIQUE(concept_a, concept_b)
);
```

### Estimated Data Volume
- ~300-500 unique concepts
- ~8000 concept_sources (avg 3 concepts per source)
- ~1000 concept_relations

---

## Concept Extraction Pipeline

**Script**: `scripts/extract_concepts.py`

### Per-article extraction (no batching)
For each article with abstract/content, call DeepSeek:

```
From this text, extract exactly 5 key philosophical/technical concepts.
For each concept provide:
- name (English canonical, lowercase)
- name_zh (Chinese)
- relevance (0.0-1.0)
- context (one sentence from text)

Also identify up to 3 relations between concepts:
- concept_a -> relation_type -> concept_b
- types: extends, critiques, requires, contrasts, exemplifies

Return as JSON: {concepts: [...], relations: [...]}

Title: {title} by {author} ({year})
{abstract or content[:1500]}
```

### For books
Use overview (if exists) or concatenation of first 3 chapter summaries.

### Deduplication
1. Exact name match → merge
2. Synonym dictionary (manual, ~50 entries): `{"phenomenal consciousness": "consciousness", ...}`
3. Fuzzy: edit distance < 3 → flag for review

### Resume support
- Track `last_processed_id` in a metadata table or file
- `--resume` flag continues from last successful article

### Cost estimate
- ~2746 API calls at ~¥0.02/call = ~¥55
- Runtime: ~2-3 hours (with rate limiting)

### Post-processing
After extraction:
1. Compute `mention_count` per concept
2. Derive `first_seen_year` from min(source dates)
3. Derive `peak_year` from mode(source dates)
4. Build indexes on concept_sources(concept_id), concept_sources(source_id)

---

## Visualization

### Knowledge Graph (D3.js force-directed, embedded)

**Location**: New "Graph" mode tab alongside Articles/Books/Notes in sidebar.

**Layout**: When Graph mode active, list-panel + reading-panel merge into full-width graph canvas.

**Nodes**: Concepts only (not articles/books)
- Size = mention_count (log scale)
- Color = category (philosophy=blue, ai=orange, science=green, methodology=purple)
- Label = name (or name_zh based on ZH toggle)

**Edges**: concept_relations
- Line style by relation type (solid=extends, dashed=critiques, dotted=requires)
- Thickness = strength

**Interaction**:
- Zoom/pan (D3 standard)
- Drag nodes to reposition
- Click concept → sidebar shows concept detail (definition, sources list, related concepts)
- Hover → highlight connected nodes

**Filter controls** (top bar when in graph mode):
- Category checkboxes
- Min mentions slider
- Year range slider (first_seen_year filter)
- Search box to highlight/center on a concept

**API**: `GET /api/graph?min_mentions=3&category=philosophy&year_start=1950&year_end=2025`
Returns `{nodes: [{id, name, name_zh, category, mention_count, first_seen_year}], edges: [{source, target, relation, strength}]}`

### Concept Map (sidebar enhancement)

**Location**: Sidebar Topics section replaced with interactive concept bubbles.

**Design**: D3 bubble/pack layout within sidebar (200x400px).
- Each bubble = topic, size = total article+book count
- Nearby topics = related (by shared concepts)
- Click topic → expands to show concepts under that topic
- Click concept → navigates to graph centered on it, or shows sources list

**API**: `GET /api/concept-map` returns topic→concept aggregation

---

## New API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `GET /api/graph` | GET | Graph data with filter params |
| `GET /api/concepts` | GET | Concept list, sortable |
| `GET /api/concept/<id>` | GET | Concept detail + sources + relations |
| `GET /api/concept-map` | GET | Sidebar bubble data |

---

## Frontend Integration

- D3.js v7 via CDN: `<script src="https://d3js.org/d3.v7.min.js">`
- Sidebar mode tabs: `[Articles] [Books] [Notes] [Graph]`
- Graph mode replaces list+reading panels with single graph canvas + overlay controls
- ~400 lines new JS, ~100 lines new CSS
- Total serve_research.py: ~2600 lines

---

## New Scripts

| Script | Purpose |
|--------|---------|
| `scripts/migrate_concepts.py` | Create 3 new tables |
| `scripts/extract_concepts.py` | LLM extraction pipeline with --resume |

---

## Execution Order

1. `migrate_concepts.py` — create tables
2. `extract_concepts.py` — run extraction (~2-3 hours)
3. Modify `serve_research.py` — add APIs + graph visualization
4. Verify — check concept counts, test graph rendering
