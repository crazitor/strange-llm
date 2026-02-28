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
