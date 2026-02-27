#!/usr/bin/env python3
"""Add books, book_chapters, book_chunks, and notes tables to corpus.db."""

import os
import sqlite3

RESEARCH_DIR = os.path.join(os.path.dirname(__file__), '..', 'research')
DB_PATH = os.path.join(RESEARCH_DIR, 'corpus.db')

SCHEMA = """
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    title_zh TEXT,
    author TEXT,
    year TEXT,
    language TEXT,
    linked_book_id INTEGER,
    filename TEXT,
    page_count INTEGER,
    category TEXT,
    importance REAL DEFAULT 9.0,
    topics TEXT,
    level TEXT DEFAULT 'essential'
);

CREATE TABLE IF NOT EXISTS book_chapters (
    id INTEGER PRIMARY KEY,
    book_id INTEGER REFERENCES books(id),
    chapter_num INTEGER,
    title TEXT,
    start_page INTEGER,
    end_page INTEGER,
    content TEXT,
    summary TEXT,
    word_count INTEGER
);

CREATE TABLE IF NOT EXISTS book_chunks (
    id INTEGER PRIMARY KEY,
    book_id INTEGER REFERENCES books(id),
    chapter_id INTEGER REFERENCES book_chapters(id),
    chunk_index INTEGER,
    content TEXT,
    page_start INTEGER,
    page_end INTEGER
);

CREATE VIRTUAL TABLE IF NOT EXISTS book_chunks_fts USING fts5(
    content, content='book_chunks', content_rowid='id'
);

-- Triggers to keep FTS in sync
CREATE TRIGGER IF NOT EXISTS book_chunks_ai AFTER INSERT ON book_chunks BEGIN
    INSERT INTO book_chunks_fts(rowid, content) VALUES (new.id, new.content);
END;

CREATE TRIGGER IF NOT EXISTS book_chunks_ad AFTER DELETE ON book_chunks BEGIN
    INSERT INTO book_chunks_fts(book_chunks_fts, rowid, content) VALUES('delete', old.id, old.content);
END;

CREATE TRIGGER IF NOT EXISTS book_chunks_au AFTER UPDATE ON book_chunks BEGIN
    INSERT INTO book_chunks_fts(book_chunks_fts, rowid, content) VALUES('delete', old.id, old.content);
    INSERT INTO book_chunks_fts(rowid, content) VALUES (new.id, new.content);
END;

CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY,
    content TEXT NOT NULL,
    created_at TEXT DEFAULT (datetime('now')),
    article_id INTEGER,
    book_id INTEGER,
    chapter_id INTEGER,
    highlight_text TEXT,
    tags TEXT
);
"""

def migrate():
    conn = sqlite3.connect(DB_PATH)
    print(f"Migrating {DB_PATH}...")
    conn.executescript(SCHEMA)
    conn.commit()

    # Verify
    c = conn.cursor()
    for table in ['books', 'book_chapters', 'book_chunks', 'notes']:
        c.execute(f"SELECT count(*) FROM {table}")
        print(f"  {table}: {c.fetchone()[0]} rows")
    c.execute("SELECT count(*) FROM book_chunks_fts")
    print(f"  book_chunks_fts: {c.fetchone()[0]} rows")

    conn.close()
    print("Migration complete.")

if __name__ == '__main__':
    migrate()
