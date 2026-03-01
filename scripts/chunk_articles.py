#!/usr/bin/env python3
"""Chunk articles into ~800-char segments for fine-grained RAG retrieval."""

import os
import re
import sqlite3

RESEARCH_DIR = os.path.join(os.path.dirname(__file__), '..', 'research')
DB_PATH = os.path.join(RESEARCH_DIR, 'corpus.db')

TARGET_SIZE = 800
MIN_SIZE = 300
MAX_SIZE = 1200
OVERLAP = 100  # Reduced from 200 to cut expansion ratio
MAX_CHUNKS_PER_ARTICLE = 60  # Cap to prevent oversized articles dominating index

CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS article_chunks (
    id INTEGER PRIMARY KEY,
    article_id INTEGER REFERENCES articles(id),
    chunk_index INTEGER,
    content TEXT,
    clean_content TEXT,
    char_start INTEGER,
    char_end INTEGER
);
CREATE INDEX IF NOT EXISTS idx_ac_article ON article_chunks(article_id);
"""


def strip_frontmatter(text):
    """Remove YAML frontmatter if present."""
    if text.startswith('---'):
        end = text.find('---', 3)
        if end != -1:
            text = text[end + 3:].strip()
    return text


def chunk_text(text, target=TARGET_SIZE, min_size=MIN_SIZE, max_size=MAX_SIZE, overlap=OVERLAP):
    """Split text into chunks: split on \\n\\n, merge small, split large."""
    text = strip_frontmatter(text)
    if not text.strip():
        return []

    # Split on double newlines
    paragraphs = re.split(r'\n\n+', text)
    paragraphs = [p.strip() for p in paragraphs if p.strip()]

    if not paragraphs:
        return []

    # Merge small paragraphs
    merged = []
    current = paragraphs[0]
    for p in paragraphs[1:]:
        if len(current) + len(p) + 2 < target:
            current = current + '\n\n' + p
        else:
            merged.append(current)
            current = p
    merged.append(current)

    # Split large chunks
    chunks = []
    for seg in merged:
        if len(seg) <= max_size:
            chunks.append(seg)
        else:
            # Split on sentence boundaries
            sentences = re.split(r'(?<=[.!?])\s+', seg)
            buf = ''
            for s in sentences:
                if buf and len(buf) + len(s) > target:
                    chunks.append(buf.strip())
                    # Overlap: keep last ~overlap chars
                    buf = buf[-overlap:] + ' ' + s if overlap else s
                else:
                    buf = (buf + ' ' + s).strip() if buf else s
            if buf.strip():
                chunks.append(buf.strip())

    # Add overlap between merged chunks
    if overlap and len(chunks) > 1:
        overlapped = [chunks[0]]
        for i in range(1, len(chunks)):
            prev_tail = chunks[i - 1][-overlap:]
            overlapped.append(prev_tail + ' ' + chunks[i])
        chunks = overlapped

    return [c for c in chunks if len(c) >= min_size // 2]


def build_chunks():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Create table
    conn.executescript(CREATE_TABLE)

    # Clear existing chunks
    conn.execute('DELETE FROM article_chunks')
    conn.commit()

    # Fetch articles with content
    rows = conn.execute(
        'SELECT id, title, author, content, abstract FROM articles'
    ).fetchall()

    total_chunks = 0
    articles_with_content = 0

    for row in rows:
        text = row['content'] or row['abstract'] or ''
        if not text.strip():
            continue

        articles_with_content += 1
        title = row['title'] or ''
        author = row['author'] or ''
        prefix = f"[{title} by {author}]" if author else f"[{title}]"

        chunks = chunk_text(text)
        # Cap chunks per article to prevent index domination
        if len(chunks) > MAX_CHUNKS_PER_ARTICLE:
            # Keep evenly spaced chunks to maintain coverage
            step = len(chunks) / MAX_CHUNKS_PER_ARTICLE
            chunks = [chunks[int(i * step)] for i in range(MAX_CHUNKS_PER_ARTICLE)]

        char_pos = 0

        for idx, chunk in enumerate(chunks):
            # Find actual position in original text (approximate)
            chunk_clean = chunk[:50]
            pos = text.find(chunk_clean, max(0, char_pos - OVERLAP))
            if pos == -1:
                pos = char_pos

            prefixed = f"{prefix}\n{chunk}"
            conn.execute(
                'INSERT INTO article_chunks (article_id, chunk_index, content, clean_content, char_start, char_end) VALUES (?,?,?,?,?,?)',
                (row['id'], idx, prefixed, chunk, pos, pos + len(chunk))
            )
            char_pos = pos + len(chunk)
            total_chunks += 1

        if articles_with_content % 200 == 0:
            conn.commit()
            print(f'  Processed {articles_with_content} articles, {total_chunks} chunks...')

    conn.commit()
    conn.close()
    print(f'\nDone: {articles_with_content} articles -> {total_chunks} chunks')


if __name__ == '__main__':
    build_chunks()
