#!/usr/bin/env python3
"""Build ChromaDB vector embeddings for semantic search."""

import os
import sqlite3
import chromadb
from sentence_transformers import SentenceTransformer

RESEARCH_DIR = os.path.join(os.path.dirname(__file__), '..', 'research')
DB_PATH = os.path.join(RESEARCH_DIR, 'corpus.db')
CHROMA_DIR = os.path.join(RESEARCH_DIR, 'chroma_db')

BATCH_SIZE = 100


def embed_batch(model, collection, batch_ids, batch_docs, batch_metas):
    """Embed and add a batch to ChromaDB."""
    embeddings = model.encode(batch_docs).tolist()
    collection.add(
        ids=batch_ids,
        documents=batch_docs,
        embeddings=embeddings,
        metadatas=batch_metas
    )
    return len(batch_ids)


def build_article_embeddings(model, client, conn):
    """Build embeddings for articles collection."""
    collection = client.create_collection(
        name='articles',
        metadata={'hnsw:space': 'cosine'}
    )

    c = conn.cursor()
    c.execute('''SELECT id, title, author, abstract, source, date, category
                 FROM articles''')
    rows = c.fetchall()

    print(f'Embedding {len(rows)} articles...')

    batch_ids, batch_docs, batch_metas = [], [], []
    processed = 0

    for row in rows:
        parts = [row['title']]
        if row['abstract']:
            parts.append(row['abstract'][:500])
        text = ' | '.join(parts)

        batch_ids.append(f"a_{row['id']}")
        batch_docs.append(text)
        batch_metas.append({
            'article_id': row['id'],
            'source': row['source'] or '',
            'author': row['author'] or '',
            'date': row['date'] or '',
            'category': row['category'] or '',
            'title': row['title'][:200]
        })

        if len(batch_ids) >= BATCH_SIZE:
            processed += embed_batch(model, collection, batch_ids, batch_docs, batch_metas)
            print(f'  articles: {processed}/{len(rows)}...')
            batch_ids, batch_docs, batch_metas = [], [], []

    if batch_ids:
        processed += embed_batch(model, collection, batch_ids, batch_docs, batch_metas)

    print(f'  Articles embedded: {processed}')
    return collection


def build_book_embeddings(model, client, conn):
    """Build embeddings for book_chunks collection."""
    # Check if book_chunks table exists
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='book_chunks'")
    if not c.fetchone():
        print('No book_chunks table found, skipping book embeddings.')
        return None

    collection = client.create_collection(
        name='book_chunks',
        metadata={'hnsw:space': 'cosine'}
    )

    c.execute('''SELECT bc.id, bc.content, bc.book_id, bc.chapter_id,
                        bc.page_start, bc.page_end,
                        b.title as book_title, b.author,
                        ch.title as chapter_title
                 FROM book_chunks bc
                 JOIN books b ON bc.book_id = b.id
                 JOIN book_chapters ch ON bc.chapter_id = ch.id''')
    rows = c.fetchall()

    if not rows:
        print('No book chunks found, skipping book embeddings.')
        return None

    print(f'Embedding {len(rows)} book chunks...')

    batch_ids, batch_docs, batch_metas = [], [], []
    processed = 0

    for row in rows:
        text = row['content'][:1000]  # embed first 1000 chars of chunk

        batch_ids.append(f"bc_{row['id']}")
        batch_docs.append(text)
        batch_metas.append({
            'chunk_id': row['id'],
            'book_id': row['book_id'],
            'chapter_id': row['chapter_id'],
            'book_title': (row['book_title'] or '')[:200],
            'chapter_title': (row['chapter_title'] or '')[:200],
            'author': row['author'] or '',
            'page_range': f"{row['page_start']}-{row['page_end']}",
        })

        if len(batch_ids) >= BATCH_SIZE:
            processed += embed_batch(model, collection, batch_ids, batch_docs, batch_metas)
            print(f'  book_chunks: {processed}/{len(rows)}...')
            batch_ids, batch_docs, batch_metas = [], [], []

    if batch_ids:
        processed += embed_batch(model, collection, batch_ids, batch_docs, batch_metas)

    print(f'  Book chunks embedded: {processed}')
    return collection


def build_embeddings():
    print('Loading sentence-transformers model...')
    model = SentenceTransformer('all-MiniLM-L6-v2')

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Reset ChromaDB
    if os.path.exists(CHROMA_DIR):
        import shutil
        shutil.rmtree(CHROMA_DIR)

    client = chromadb.PersistentClient(path=CHROMA_DIR)

    # Build both collections
    art_col = build_article_embeddings(model, client, conn)
    book_col = build_book_embeddings(model, client, conn)

    conn.close()

    print(f'\n=== Embeddings built: {CHROMA_DIR} ===')

    # Test semantic search
    print('\nTest query: "computational theory of consciousness"')
    results = art_col.query(
        query_texts=['computational theory of consciousness'],
        n_results=5
    )
    for i, meta in enumerate(results['metadatas'][0]):
        print(f'  {i+1}. [article] {meta["title"][:70]}')

    if book_col:
        results = book_col.query(
            query_texts=['computational theory of consciousness'],
            n_results=5
        )
        for i, meta in enumerate(results['metadatas'][0]):
            print(f'  {i+1}. [book] {meta["book_title"][:40]} / {meta["chapter_title"][:30]}')


if __name__ == '__main__':
    build_embeddings()
