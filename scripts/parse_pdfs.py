#!/usr/bin/env python3
"""Parse PDF files and ingest their text content into corpus.db."""

import os
import sqlite3
import sys
import time

RESEARCH_DIR = os.path.join(os.path.dirname(__file__), '..', 'research')
DB_PATH = os.path.join(RESEARCH_DIR, 'corpus.db')


def extract_text(pdf_path):
    """Extract text from a PDF using pymupdf."""
    import pymupdf
    try:
        doc = pymupdf.open(pdf_path)
        pages = []
        for page in doc:
            text = page.get_text()
            if text.strip():
                pages.append(text)
        doc.close()
        return '\n\n'.join(pages)
    except Exception as e:
        print(f'  Error extracting {pdf_path}: {e}')
        return None


def find_pdf_path(filename, source):
    """Locate the actual PDF file on disk."""
    # Try source directory first
    candidates = [
        os.path.join(RESEARCH_DIR, source, filename),
        os.path.join(RESEARCH_DIR, filename),
    ]
    # For philosopher sources like "philosopher_david-chalmers"
    if source and source.startswith('philosopher_'):
        name = source.replace('philosopher_', '')
        candidates.insert(0, os.path.join(RESEARCH_DIR, 'philosophers', name, filename))

    # Also check special directories
    for d in ('papers', 'chalmers_papers', 'floridi_papers', 'public_domain_texts'):
        candidates.append(os.path.join(RESEARCH_DIR, d, filename))

    for path in candidates:
        if os.path.exists(path):
            return path
    return None


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute("SELECT id, filename, source FROM articles WHERE file_type='pdf' AND content IS NULL")
    rows = c.fetchall()

    if not rows:
        print('All PDFs already parsed!')
        conn.close()
        return

    print(f'Parsing {len(rows)} PDF files...')
    success = 0
    skipped = 0
    errors = 0

    for i, row in enumerate(rows):
        pdf_path = find_pdf_path(row['filename'], row['source'])
        if not pdf_path:
            skipped += 1
            continue

        text = extract_text(pdf_path)
        if not text or len(text.strip()) < 50:
            skipped += 1
            continue

        # Update content, abstract, word_count
        abstract = text[:500].strip()
        word_count = len(text.split())

        c.execute('''UPDATE articles SET content = ?, abstract = ?, word_count = ?
                     WHERE id = ? AND content IS NULL''',
                  (text, abstract, word_count, row['id']))
        success += 1

        if (i + 1) % 50 == 0:
            conn.commit()
            print(f'  {i+1}/{len(rows)} processed ({success} extracted)...')

    conn.commit()

    # Rebuild FTS index
    print('Rebuilding FTS index...')
    c.execute("INSERT INTO articles_fts(articles_fts) VALUES('rebuild')")
    conn.commit()

    print(f'\nDone: {success} extracted, {skipped} skipped, {errors} errors')

    # Stats
    c.execute("SELECT count(*) FROM articles WHERE content IS NOT NULL")
    print(f'Total articles with content: {c.fetchone()[0]}')

    conn.close()


if __name__ == '__main__':
    main()
