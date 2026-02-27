#!/usr/bin/env python3
"""CLI tool for querying the AI philosophy research corpus."""

import argparse
import json
import os
import sqlite3
import sys
import textwrap

RESEARCH_DIR = os.path.join(os.path.dirname(__file__), '..', 'research')
DB_PATH = os.path.join(RESEARCH_DIR, 'corpus.db')
CHROMA_DIR = os.path.join(RESEARCH_DIR, 'chroma_db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def cmd_search(args):
    """Full-text search using FTS5."""
    conn = get_db()
    c = conn.cursor()
    query = args.query

    c.execute('''SELECT a.id, a.title, a.author, a.source, a.importance,
                        snippet(articles_fts, 2, '>>>', '<<<', '...', 30) as snippet
                 FROM articles_fts
                 JOIN articles a ON a.id = articles_fts.rowid
                 WHERE articles_fts MATCH ?
                 ORDER BY bm25(articles_fts) * COALESCE(a.importance, 5)
                 LIMIT ?''', (query, args.limit))

    results = c.fetchall()
    if not results:
        print(f'No results for "{query}"')
        return

    print(f'\n=== Search: "{query}" ({len(results)} results) ===\n')
    for r in results:
        imp = f'{r["importance"]:.1f}' if r['importance'] else '?'
        author = r['author'][:30] if r['author'] else ''
        print(f'  [{imp}] {r["title"][:70]}')
        print(f'        {author} | {r["source"]}')
        if r['snippet']:
            print(f'        {r["snippet"][:120]}')
        print()

    conn.close()

def cmd_similar(args):
    """Semantic search using ChromaDB."""
    try:
        import chromadb
        from sentence_transformers import SentenceTransformer
    except ImportError:
        print('Need: pip install chromadb sentence-transformers')
        return

    client = chromadb.PersistentClient(path=CHROMA_DIR)
    collection = client.get_collection('articles')

    results = collection.query(
        query_texts=[args.query],
        n_results=args.limit
    )

    print(f'\n=== Similar to: "{args.query}" ===\n')
    for i, (meta, dist) in enumerate(zip(results['metadatas'][0], results['distances'][0])):
        sim = 1 - dist  # cosine distance → similarity
        print(f'  {i+1}. [{sim:.2f}] {meta["title"][:70]}')
        print(f'           {meta.get("author", "")[:30]} | {meta["source"]}')

def cmd_top(args):
    """Show top articles by importance."""
    conn = get_db()
    c = conn.cursor()

    where_clauses = []
    params = []

    if args.topic:
        where_clauses.append("topics LIKE ?")
        params.append(f'%"{args.topic}"%')
    if args.author:
        where_clauses.append("author LIKE ?")
        params.append(f'%{args.author}%')
    if args.source:
        where_clauses.append("source = ?")
        params.append(args.source)

    where = 'WHERE ' + ' AND '.join(where_clauses) if where_clauses else ''

    c.execute(f'''SELECT title, author, source, importance, score, citations,
                         topics, summary
              FROM articles {where}
              ORDER BY importance DESC NULLS LAST
              LIMIT ?''', params + [args.n])

    results = c.fetchall()
    print(f'\n=== Top {args.n} Articles ===\n')
    for i, r in enumerate(results, 1):
        imp = f'{r["importance"]:.1f}' if r['importance'] else '?'
        extra = []
        if r['score']:
            extra.append(f'votes:{r["score"]}')
        if r['citations']:
            extra.append(f'citations:{r["citations"]}')
        topics = ''
        if r['topics']:
            try:
                topics = ' '.join(f'#{t}' for t in json.loads(r['topics']))
            except json.JSONDecodeError:
                pass

        print(f'  {i:2d}. [{imp}] {r["title"][:70]}')
        print(f'       {r["author"] or ""} | {r["source"]}', end='')
        if extra:
            print(f' | {" ".join(extra)}', end='')
        print()
        if topics:
            print(f'       {topics}')
        if r['summary']:
            print(f'       {r["summary"][:100]}')
        print()

    conn.close()

def cmd_stats(args):
    """Show corpus statistics."""
    conn = get_db()
    c = conn.cursor()

    c.execute('SELECT count(*) FROM articles')
    total = c.fetchone()[0]

    c.execute('SELECT count(*) FROM articles WHERE content IS NOT NULL')
    with_content = c.fetchone()[0]

    c.execute('SELECT count(*) FROM articles WHERE importance IS NOT NULL')
    scored = c.fetchone()[0]

    c.execute('SELECT count(*) FROM articles WHERE topics IS NOT NULL')
    tagged = c.fetchone()[0]

    print(f'\n=== Corpus Statistics ===')
    print(f'Total articles: {total}')
    print(f'With full text: {with_content}')
    print(f'Scored: {scored}')
    print(f'With topics: {tagged}')

    print(f'\nBy source:')
    c.execute('SELECT source, count(*) as cnt FROM articles GROUP BY source ORDER BY cnt DESC')
    for r in c.fetchall():
        print(f'  {r["source"]:30s} {r["cnt"]:5d}')

    print(f'\nBy topic:')
    c.execute('SELECT topics FROM articles WHERE topics IS NOT NULL')
    topic_counts = {}
    for r in c.fetchall():
        try:
            for t in json.loads(r['topics']):
                topic_counts[t] = topic_counts.get(t, 0) + 1
        except (json.JSONDecodeError, TypeError):
            pass
    for t, cnt in sorted(topic_counts.items(), key=lambda x: -x[1]):
        print(f'  #{t:25s} {cnt:5d}')

    print(f'\nTop 10 authors:')
    c.execute('''SELECT author, count(*) as cnt, avg(importance) as avg_imp
                 FROM articles WHERE author IS NOT NULL AND author != ''
                 GROUP BY author ORDER BY cnt DESC LIMIT 10''')
    for r in c.fetchall():
        avg = f'{r["avg_imp"]:.1f}' if r['avg_imp'] else '?'
        print(f'  {r["author"][:35]:35s} {r["cnt"]:4d} articles (avg importance: {avg})')

    db_size = os.path.getsize(DB_PATH) / 1024 / 1024
    print(f'\nDatabase size: {db_size:.1f} MB')

    conn.close()

def main():
    parser = argparse.ArgumentParser(description='Query AI philosophy research corpus')
    sub = parser.add_subparsers(dest='command')

    p_search = sub.add_parser('search', help='Full-text search')
    p_search.add_argument('query')
    p_search.add_argument('-n', '--limit', type=int, default=20)

    p_similar = sub.add_parser('similar', help='Semantic similarity search')
    p_similar.add_argument('query')
    p_similar.add_argument('-n', '--limit', type=int, default=10)

    p_top = sub.add_parser('top', help='Top articles by importance')
    p_top.add_argument('n', type=int, default=20, nargs='?')
    p_top.add_argument('--topic', type=str)
    p_top.add_argument('--author', type=str)
    p_top.add_argument('--source', type=str)

    p_stats = sub.add_parser('stats', help='Corpus statistics')

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return

    {'search': cmd_search, 'similar': cmd_similar,
     'top': cmd_top, 'stats': cmd_stats}[args.command](args)

if __name__ == '__main__':
    main()
