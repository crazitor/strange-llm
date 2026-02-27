#!/usr/bin/env python3
"""Translate article titles and abstracts to Chinese using DeepSeek API.

Usage:
    python translate_articles.py              # Translate all untranslated titles+abstracts
    python translate_articles.py --full ID    # Translate full content of article ID
    python translate_articles.py --stats      # Show translation progress
"""

import argparse
import json
import os
import sqlite3
import sys
import time

RESEARCH_DIR = os.path.join(os.path.dirname(__file__), '..', 'research')
DB_PATH = os.path.join(RESEARCH_DIR, 'corpus.db')

BATCH_SIZE = 15  # Articles per API call for title+abstract

def get_client():
    from openai import OpenAI
    api_key = os.environ.get('DEEPSEEK_API_KEY', 'sk-1556a07369cf474f8e886c130e3584ca')
    return OpenAI(api_key=api_key, base_url='https://api.deepseek.com')

def llm_call(client, prompt, max_tokens=8000):
    """Make a DeepSeek API call."""
    r = client.chat.completions.create(
        model='deepseek-chat',
        max_tokens=max_tokens,
        messages=[{'role': 'user', 'content': prompt}]
    )
    return r.choices[0].message.content.strip()

def translate_batch(client, articles):
    """Translate a batch of title+abstract pairs."""
    items = []
    for a in articles:
        entry = f"ID:{a['id']}\nTitle: {a['title']}"
        if a['abstract']:
            entry += f"\nAbstract: {a['abstract'][:600]}"
        items.append(entry)

    prompt = f"""Translate the following article titles and abstracts into Chinese.
Keep technical terms accurate. For titles, provide concise Chinese translations.
For abstracts, translate faithfully but naturally.

{chr(10).join(items)}

Return JSON array: [{{"id": N, "title_zh": "中文标题", "abstract_zh": "中文摘要"}}]
If no abstract, set abstract_zh to null. Only valid JSON, no other text."""

    text = llm_call(client, prompt)
    # Extract JSON
    start = text.find('[')
    end = text.rfind(']') + 1
    if start >= 0 and end > start:
        return json.loads(text[start:end])
    return []

def translate_full_content(client, article_id, conn):
    """Translate full article content to Chinese."""
    c = conn.cursor()
    c.execute('SELECT title, content FROM articles WHERE id = ?', (article_id,))
    row = c.fetchone()
    if not row:
        print(f'Article {article_id} not found')
        return False
    if not row[1]:
        print(f'Article {article_id} has no content (PDF only)')
        return False

    content = row[1]
    title = row[0]

    MAX_CHUNK = 6000
    chunks = []
    if len(content) <= MAX_CHUNK:
        chunks = [content]
    else:
        paragraphs = content.split('\n\n')
        current = ''
        for p in paragraphs:
            if len(current) + len(p) > MAX_CHUNK and current:
                chunks.append(current)
                current = p
            else:
                current = current + '\n\n' + p if current else p
        if current:
            chunks.append(current)

    print(f'Translating article {article_id}: "{title[:50]}" ({len(chunks)} chunks)...')

    translated_parts = []
    for i, chunk in enumerate(chunks):
        prompt = (
            'Translate this article text into Chinese. Maintain markdown formatting. '
            'Translate naturally and accurately. Keep code blocks, URLs, and proper nouns unchanged.\n\n'
            + chunk
        )
        translated_parts.append(llm_call(client, prompt, max_tokens=8192))
        if len(chunks) > 1:
            print(f'  Chunk {i+1}/{len(chunks)} done')
            time.sleep(0.5)

    content_zh = '\n\n'.join(translated_parts)
    c.execute('UPDATE articles SET content_zh = ? WHERE id = ?', (content_zh, article_id))
    conn.commit()
    print(f'  Saved ({len(content_zh)} chars)')
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--full', type=int, help='Translate full content of article ID')
    parser.add_argument('--stats', action='store_true', help='Show translation progress')
    parser.add_argument('--limit', type=int, default=0, help='Max articles to translate (0=all)')
    args = parser.parse_args()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    if args.stats:
        c.execute('SELECT count(*) FROM articles')
        total = c.fetchone()[0]
        c.execute('SELECT count(*) FROM articles WHERE title_zh IS NOT NULL')
        titles = c.fetchone()[0]
        c.execute('SELECT count(*) FROM articles WHERE abstract_zh IS NOT NULL')
        abstracts = c.fetchone()[0]
        c.execute('SELECT count(*) FROM articles WHERE content_zh IS NOT NULL')
        full = c.fetchone()[0]
        print(f'Translation progress:')
        print(f'  Titles translated:    {titles}/{total} ({titles*100//total}%)')
        print(f'  Abstracts translated: {abstracts}/{total}')
        print(f'  Full text translated: {full}/{total}')
        conn.close()
        return

    client = get_client()

    if args.full:
        translate_full_content(client, args.full, conn)
        conn.close()
        return

    # Batch translate titles + abstracts
    c.execute('''SELECT id, title, abstract FROM articles
                 WHERE title_zh IS NULL
                 ORDER BY importance DESC NULLS LAST''')
    rows = [dict(r) for r in c.fetchall()]

    if args.limit:
        rows = rows[:args.limit]

    if not rows:
        print('All titles already translated!')
        conn.close()
        return

    print(f'Translating {len(rows)} articles (title + abstract)...')
    processed = 0
    errors = 0

    for i in range(0, len(rows), BATCH_SIZE):
        batch = rows[i:i + BATCH_SIZE]
        try:
            results = translate_batch(client, batch)
            for r in results:
                aid = r.get('id')
                if aid:
                    c.execute('''UPDATE articles SET title_zh = ?, abstract_zh = ?
                                 WHERE id = ?''',
                              (r.get('title_zh'), r.get('abstract_zh'), aid))
            conn.commit()
            processed += len(batch)
            print(f'  {processed}/{len(rows)} done...')
            time.sleep(0.3)
        except Exception as e:
            print(f'  Batch error: {e}')
            errors += 1
            time.sleep(2)

    # Rebuild FTS to include Chinese content
    print('Rebuilding FTS index...')
    c.execute("INSERT INTO articles_fts(articles_fts) VALUES('rebuild')")
    conn.commit()

    print(f'\nDone: {processed} translated, {errors} errors')
    conn.close()

if __name__ == '__main__':
    main()
