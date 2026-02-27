#!/usr/bin/env python3
"""Build SQLite database with FTS5 from all research index.json files."""

import json
import os
import sqlite3
import sys

RESEARCH_DIR = os.path.join(os.path.dirname(__file__), '..', 'research')
DB_PATH = os.path.join(RESEARCH_DIR, 'corpus.db')

# Map index.json parent dir to source name
def get_source_name(index_path):
    """Derive a source name from the index.json path."""
    rel = os.path.relpath(os.path.dirname(index_path), RESEARCH_DIR)
    parts = rel.split(os.sep)
    if parts[0] == 'substacks':
        return f'substack_{parts[1]}'
    elif parts[0] == 'philosophers':
        return f'philosopher_{parts[1]}'
    else:
        return parts[0]

def get_file_dir(index_path):
    """Get the directory containing the actual files."""
    return os.path.dirname(index_path)

def read_content(filepath):
    """Read markdown file content, return (content, word_count)."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        word_count = len(content.split())
        return content, word_count
    except (OSError, IOError):
        return None, 0

def extract_abstract(content, max_chars=500):
    """Extract first ~500 chars as abstract, trying to break at sentence."""
    if not content:
        return None
    text = content[:max_chars + 200]  # grab extra to find sentence break
    # Try to break at a sentence boundary within the limit
    for end in ['. ', '.\n', '? ', '!\n']:
        idx = text.rfind(end, 0, max_chars + 50)
        if idx > 100:
            return text[:idx + 1].strip()
    return text[:max_chars].strip()

def build_db():
    # Remove old DB
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Create main table
    c.execute('''CREATE TABLE articles (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT,
        date TEXT,
        source TEXT,
        url TEXT,
        filename TEXT,
        file_type TEXT,
        content TEXT,
        abstract TEXT,
        word_count INTEGER,
        score INTEGER,
        citations INTEGER,
        category TEXT,
        arxiv_id TEXT,
        importance REAL,
        summary TEXT,
        topics TEXT
    )''')

    # Create FTS5 virtual table
    c.execute('''CREATE VIRTUAL TABLE articles_fts USING fts5(
        title, author, abstract, content, source,
        content='articles', content_rowid='id'
    )''')

    # Triggers to keep FTS in sync
    c.execute('''CREATE TRIGGER articles_ai AFTER INSERT ON articles BEGIN
        INSERT INTO articles_fts(rowid, title, author, abstract, content, source)
        VALUES (new.id, new.title, new.author, new.abstract, new.content, new.source);
    END''')
    c.execute('''CREATE TRIGGER articles_ad AFTER DELETE ON articles BEGIN
        INSERT INTO articles_fts(articles_fts, rowid, title, author, abstract, content, source)
        VALUES ('delete', old.id, old.title, old.author, old.abstract, old.content, old.source);
    END''')
    c.execute('''CREATE TRIGGER articles_au AFTER UPDATE ON articles BEGIN
        INSERT INTO articles_fts(articles_fts, rowid, title, author, abstract, content, source)
        VALUES ('delete', old.id, old.title, old.author, old.abstract, old.content, old.source);
        INSERT INTO articles_fts(rowid, title, author, abstract, content, source)
        VALUES (new.id, new.title, new.author, new.abstract, new.content, new.source);
    END''')

    # Find all index.json files
    index_files = []
    for root, dirs, files in os.walk(RESEARCH_DIR):
        if 'index.json' in files:
            index_files.append(os.path.join(root, 'index.json'))

    total = 0
    md_loaded = 0

    for index_path in sorted(index_files):
        source = get_source_name(index_path)
        file_dir = get_file_dir(index_path)

        with open(index_path, 'r', encoding='utf-8') as f:
            items = json.load(f)

        for item in items:
            title = item.get('title', '').strip()
            if not title:
                continue

            author = item.get('author', '').strip() or None
            # Clean SEP author format
            if author and 'Copyright' in author:
                # "Copyright © 2018byName Name<email>" → "Name Name"
                import re
                m = re.search(r'by(.+?)(?:<|$)', author)
                if m:
                    author = m.group(1).strip()

            date = item.get('date', '') or item.get('year', '')
            if date:
                date = str(date).strip()
            else:
                date = None

            url = item.get('url', '')
            filename = item.get('filename', '')

            # Determine file type
            if filename:
                file_type = 'pdf' if filename.endswith('.pdf') else 'md'
            else:
                file_type = None

            # Read content for md files
            content = None
            abstract = item.get('abstract', None)
            word_count = item.get('length', 0) or 0

            if filename and file_type == 'md':
                filepath = os.path.join(file_dir, filename)
                content, word_count = read_content(filepath)
                if content and not abstract:
                    abstract = extract_abstract(content)
                md_loaded += 1
            elif not abstract and file_type == 'pdf':
                # PDF: just store metadata
                word_count = item.get('size_kb', 0) or 0  # store size as proxy

            # For philpapers: no filename, store source-relative info
            if not filename and source == 'philpapers':
                file_type = None

            score = item.get('score', None)
            citations = item.get('citations', None)
            category = item.get('category', None)
            arxiv_id = item.get('arxiv_id', None)

            c.execute('''INSERT INTO articles
                (title, author, date, source, url, filename, file_type,
                 content, abstract, word_count, score, citations, category, arxiv_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (title, author, date, source, url, filename, file_type,
                 content, abstract, word_count, score, citations, category, arxiv_id))
            total += 1

    conn.commit()

    # Create useful indexes
    c.execute('CREATE INDEX idx_articles_source ON articles(source)')
    c.execute('CREATE INDEX idx_articles_author ON articles(author)')
    c.execute('CREATE INDEX idx_articles_date ON articles(date)')
    c.execute('CREATE INDEX idx_articles_importance ON articles(importance)')

    conn.commit()

    # Print stats
    c.execute('SELECT count(*) FROM articles')
    count = c.fetchone()[0]
    c.execute('SELECT source, count(*) FROM articles GROUP BY source ORDER BY count(*) DESC')
    sources = c.fetchall()

    print(f'\n=== Database built: {DB_PATH} ===')
    print(f'Total articles: {count}')
    print(f'MD files with content loaded: {md_loaded}')
    print(f'\nBy source:')
    for src, cnt in sources:
        print(f'  {src}: {cnt}')

    # Quick FTS test
    c.execute("SELECT title FROM articles_fts WHERE articles_fts MATCH 'consciousness' LIMIT 5")
    results = c.fetchall()
    print(f'\nFTS test "consciousness": {len(results)} results (showing up to 5)')
    for r in results:
        print(f'  - {r[0][:80]}')

    conn.close()
    print(f'\nDatabase size: {os.path.getsize(DB_PATH) / 1024 / 1024:.1f} MB')

if __name__ == '__main__':
    build_db()
