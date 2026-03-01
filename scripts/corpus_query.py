#!/usr/bin/env python3
"""CLI tool for querying the research corpus directly (no Flask needed).

Usage:
    python3.11 corpus_query.py search "consciousness and computation" --top 10
    python3.11 corpus_query.py fts "Hofstadter strange loop" --top 5
    python3.11 corpus_query.py read-article 42
    python3.11 corpus_query.py read-chapter 15
    python3.11 corpus_query.py concept "consciousness"
    python3.11 corpus_query.py stats

All commands support --json for machine-readable output.
"""

import argparse
import json
import os
import sqlite3
import sys

RESEARCH_DIR = os.path.join(os.path.dirname(__file__), '..', 'research')
DB_PATH = os.path.join(RESEARCH_DIR, 'corpus.db')
CHROMA_DIR = os.path.join(RESEARCH_DIR, 'chroma_db')


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def get_chroma():
    import chromadb
    return chromadb.PersistentClient(path=CHROMA_DIR)


def cmd_search(args):
    """Semantic search across article chunks and book chunks."""
    client = get_chroma()
    results = []

    # Search article chunks
    try:
        ac = client.get_collection('article_chunks')
        r = ac.query(query_texts=[args.query], n_results=args.top, include=['metadatas', 'documents', 'distances'])
        seen = {}
        for sid, meta, doc, dist in zip(r['ids'][0], r['metadatas'][0], r['documents'][0], r['distances'][0]):
            aid = meta.get('article_id', 0)
            if aid in seen:
                continue
            seen[aid] = True
            results.append({
                'type': 'article_chunk', 'article_id': aid,
                'title': meta.get('title', ''), 'author': meta.get('author', ''),
                'distance': round(dist, 4),
                'snippet': (doc or '')[:300]
            })
    except Exception:
        # Fallback to article-level
        try:
            ac = client.get_collection('articles')
            r = ac.query(query_texts=[args.query], n_results=args.top, include=['metadatas', 'documents', 'distances'])
            for sid, meta, doc, dist in zip(r['ids'][0], r['metadatas'][0], r['documents'][0], r['distances'][0]):
                results.append({
                    'type': 'article', 'article_id': int(sid.replace('a_', '')),
                    'title': meta.get('title', ''), 'author': meta.get('author', ''),
                    'distance': round(dist, 4),
                    'snippet': (doc or '')[:300]
                })
        except Exception:
            pass

    # Search book chunks
    try:
        bc = client.get_collection('book_chunks')
        r = bc.query(query_texts=[args.query], n_results=args.top, include=['metadatas', 'documents', 'distances'])
        for sid, meta, doc, dist in zip(r['ids'][0], r['metadatas'][0], r['documents'][0], r['distances'][0]):
            results.append({
                'type': 'book_chunk',
                'book_title': meta.get('book_title', ''), 'chapter': meta.get('chapter_title', ''),
                'author': meta.get('author', ''),
                'distance': round(dist, 4),
                'snippet': (doc or '')[:300]
            })
    except Exception:
        pass

    # Sort by distance
    results.sort(key=lambda x: x['distance'])
    results = results[:args.top]

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for i, r in enumerate(results, 1):
            tag = r['type']
            title = r.get('title') or r.get('book_title', '')
            author = r.get('author', '')
            print(f"\n{'='*60}")
            print(f"[{i}] ({tag}) {title} — {author}  [dist: {r['distance']}]")
            print(r.get('snippet', '')[:200])


def cmd_fts(args):
    """Full-text search using SQLite FTS or LIKE."""
    conn = get_db()
    q = f'%{args.query}%'
    rows = conn.execute(
        'SELECT id, title, author, substr(content, 1, 300) as snippet FROM articles WHERE content LIKE ? OR title LIKE ? LIMIT ?',
        (q, q, args.top)
    ).fetchall()

    results = [{'id': r['id'], 'title': r['title'], 'author': r['author'], 'snippet': r['snippet']} for r in rows]

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for i, r in enumerate(results, 1):
            print(f"\n[{i}] (id:{r['id']}) {r['title']} — {r['author']}")
            print((r['snippet'] or '')[:200])

    conn.close()


def cmd_read_article(args):
    """Read full article content."""
    conn = get_db()
    row = conn.execute('SELECT * FROM articles WHERE id = ?', (args.id,)).fetchone()
    if not row:
        print(f'Article {args.id} not found')
        return

    if args.json:
        print(json.dumps({k: row[k] for k in row.keys()}, ensure_ascii=False, indent=2))
    else:
        print(f"Title: {row['title']}")
        print(f"Author: {row['author']}")
        print(f"Source: {row['source']}  Date: {row['date']}")
        print(f"\n{'='*60}\n")
        print(row['content'] or row['abstract'] or 'No content')
    conn.close()


def cmd_read_chapter(args):
    """Read a book chapter."""
    conn = get_db()
    ch = conn.execute(
        '''SELECT ch.*, b.title as book_title, b.author
           FROM book_chapters ch JOIN books b ON ch.book_id = b.id
           WHERE ch.id = ?''', (args.id,)
    ).fetchone()
    if not ch:
        print(f'Chapter {args.id} not found')
        return

    chunks = conn.execute(
        'SELECT content FROM book_chunks WHERE chapter_id = ? ORDER BY page_start', (args.id,)
    ).fetchall()

    if args.json:
        print(json.dumps({
            'book': ch['book_title'], 'author': ch['author'],
            'chapter': ch['title'], 'content': '\n\n'.join(c['content'] for c in chunks)
        }, ensure_ascii=False, indent=2))
    else:
        print(f"Book: {ch['book_title']} by {ch['author']}")
        print(f"Chapter: {ch['title']}")
        print(f"\n{'='*60}\n")
        for c in chunks:
            print(c['content'])
            print()
    conn.close()


def cmd_concept(args):
    """Look up a concept and its relations."""
    conn = get_db()
    concept = conn.execute(
        'SELECT * FROM concepts WHERE name LIKE ? OR name_zh LIKE ? LIMIT 1',
        (f'%{args.name}%', f'%{args.name}%')
    ).fetchone()

    if not concept:
        # List similar
        similar = conn.execute(
            'SELECT name, name_zh, mention_count FROM concepts WHERE name LIKE ? ORDER BY mention_count DESC LIMIT 10',
            (f'%{args.name}%',)
        ).fetchall()
        if similar:
            print(f"No exact match. Similar concepts:")
            for s in similar:
                print(f"  - {s['name']} ({s['name_zh']}) [{s['mention_count']} mentions]")
        else:
            print(f'Concept "{args.name}" not found')
        conn.close()
        return

    # Get relations
    relations = conn.execute(
        '''SELECT c.name, cr.relation, cr.strength
           FROM concept_relations cr
           JOIN concepts c ON (c.id = cr.concept_b OR c.id = cr.concept_a)
           WHERE (cr.concept_a = ? OR cr.concept_b = ?) AND c.id != ?
           ORDER BY cr.strength DESC LIMIT 20''',
        (concept['id'], concept['id'], concept['id'])
    ).fetchall()

    # Get sources
    sources = conn.execute(
        '''SELECT cs.source_type, cs.source_id, cs.relevance, cs.context,
                  CASE WHEN cs.source_type='article' THEN a.title ELSE b.title END as title
           FROM concept_sources cs
           LEFT JOIN articles a ON cs.source_type='article' AND cs.source_id = a.id
           LEFT JOIN books b ON cs.source_type='book' AND cs.source_id = b.id
           WHERE cs.concept_id = ? ORDER BY cs.relevance DESC LIMIT 10''',
        (concept['id'],)
    ).fetchall()

    if args.json:
        print(json.dumps({
            'concept': {k: concept[k] for k in concept.keys()},
            'relations': [{'name': r['name'], 'relation': r['relation'], 'strength': r['strength']} for r in relations],
            'sources': [{'type': s['source_type'], 'id': s['source_id'], 'title': s['title'], 'relevance': s['relevance']} for s in sources]
        }, ensure_ascii=False, indent=2))
    else:
        print(f"Concept: {concept['name']} ({concept['name_zh']})")
        print(f"Category: {concept['category']}")
        print(f"Description: {concept['description']}")
        print(f"Mentions: {concept['mention_count']}")
        if relations:
            print(f"\nRelations:")
            for r in relations:
                print(f"  - {r['relation']} → {r['name']} (strength: {r['strength']})")
        if sources:
            print(f"\nKey sources:")
            for s in sources:
                print(f"  - [{s['source_type']}] {s['title']}")
    conn.close()


def cmd_stats(args):
    """Show corpus statistics."""
    conn = get_db()
    stats = {}
    for table in ['articles', 'books', 'book_chunks', 'concepts', 'concept_relations', 'article_chunks']:
        try:
            cnt = conn.execute(f'SELECT count(*) FROM {table}').fetchone()[0]
            stats[table] = cnt
        except Exception:
            stats[table] = 0

    try:
        client = get_chroma()
        for col_name in ['articles', 'book_chunks', 'article_chunks']:
            try:
                col = client.get_collection(col_name)
                stats[f'chroma_{col_name}'] = col.count()
            except Exception:
                pass
    except Exception:
        pass

    if args.json:
        print(json.dumps(stats, indent=2))
    else:
        print("Corpus Statistics:")
        for k, v in stats.items():
            print(f"  {k}: {v:,}")
    conn.close()


def cmd_arguments(args):
    """Search arguments by semantic similarity."""
    import chromadb
    client = chromadb.PersistentClient(path=CHROMA_DIR)
    try:
        col = client.get_collection('arguments')
    except Exception:
        print("No arguments collection. Run build_embeddings.py first.")
        return

    results = col.query(query_texts=[args.query], n_results=args.top,
                        include=['metadatas', 'documents', 'distances'])

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    items = []
    for sid, meta, doc, dist in zip(results['ids'][0], results['metadatas'][0],
                                     results['documents'][0], results['distances'][0]):
        items.append({
            'claim': meta.get('claim', ''),
            'topic': meta.get('topic', ''),
            'title': meta.get('title', ''),
            'author': meta.get('author', ''),
            'distance': round(dist, 4),
        })

    if args.json:
        print(json.dumps(items, indent=2, ensure_ascii=False))
    else:
        for i, it in enumerate(items):
            print(f"\n[{i+1}] dist={it['distance']:.3f} | {it['topic']}")
            print(f"  CLAIM: {it['claim']}")
            print(f"  Source: {it['title'][:60]} — {it['author']}")
    conn.close()


def main():
    parser = argparse.ArgumentParser(description='Research corpus CLI')
    parser.add_argument('--json', action='store_true', help='JSON output')
    sub = parser.add_subparsers(dest='command')

    p = sub.add_parser('search', help='Semantic search')
    p.add_argument('query')
    p.add_argument('--top', type=int, default=10)

    p = sub.add_parser('fts', help='Full-text search')
    p.add_argument('query')
    p.add_argument('--top', type=int, default=10)

    p = sub.add_parser('read-article', help='Read article')
    p.add_argument('id', type=int)

    p = sub.add_parser('read-chapter', help='Read chapter')
    p.add_argument('id', type=int)

    p = sub.add_parser('concept', help='Look up concept')
    p.add_argument('name')

    p = sub.add_parser('arguments', help='Search arguments')
    p.add_argument('query')
    p.add_argument('--top', type=int, default=10)

    sub.add_parser('stats', help='Corpus stats')

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return

    cmds = {
        'search': cmd_search, 'fts': cmd_fts,
        'read-article': cmd_read_article, 'read-chapter': cmd_read_chapter,
        'concept': cmd_concept, 'arguments': cmd_arguments, 'stats': cmd_stats
    }
    cmds[args.command](args)


if __name__ == '__main__':
    main()
