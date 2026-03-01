#!/usr/bin/env python3
"""Generate topics for articles that have none, using DeepSeek."""

import argparse
import json
import os
import sqlite3
import time

RESEARCH_DIR = os.path.join(os.path.dirname(__file__), '..', 'research')
DB_PATH = os.path.join(RESEARCH_DIR, 'corpus.db')


def get_deepseek_client():
    from openai import OpenAI
    key = os.environ.get('DEEPSEEK_API_KEY', '')
    if not key:
        key_file = os.path.join(RESEARCH_DIR, '.deepseek_key')
        if os.path.exists(key_file):
            key = open(key_file).read().strip()
    return OpenAI(api_key=key, base_url="https://api.deepseek.com")


def generate_topics(client, title, abstract):
    prompt = f"""Given this academic article, generate 2-4 topic tags from this list:
consciousness, qualia, hard-problem, phenomenal-consciousness, sentience,
philosophy-of-mind, functionalism, dualism, physicalism, intentionality,
language-understanding, chinese-room, symbol-grounding, semantics, llm,
ai-ethics, ethics, moral-status, fairness, bias,
machine-ethics, robot-ethics,
ai-safety, alignment, existential-risk, superintelligence,
cognitive-science, embodiment, perception, neuroscience,
philosophy-of-information, information-theory,
philosophy-of-ai, turing-test, intelligence, computation, agi,
epistemology, knowledge, understanding, rationality,
free-will, agency, autonomy, creativity, emotion

If none fit well, create 1-2 short kebab-case tags.

Title: {title}
Abstract: {(abstract or '')[:500]}

Return ONLY a JSON array of strings, e.g. ["consciousness", "hard-problem"]"""

    try:
        resp = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100, temperature=0.3
        )
        raw = resp.choices[0].message.content.strip()
        if raw.startswith('```'):
            raw = raw.split('\n', 1)[1].rsplit('```', 1)[0].strip()
        return json.loads(raw)
    except Exception as e:
        print(f'  Error: {e}')
        return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=500)
    parser.add_argument('--batch-size', type=int, default=50)
    args = parser.parse_args()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    client = get_deepseek_client()

    rows = conn.execute(
        "SELECT id, title, abstract FROM articles WHERE (topics IS NULL OR topics = '') ORDER BY importance DESC LIMIT ?",
        (args.limit,)
    ).fetchall()

    print(f'Articles without topics: {len(rows)}')

    processed = 0
    for i, row in enumerate(rows):
        title = row['title'] or ''
        if not title.strip():
            continue

        topics = generate_topics(client, title, row['abstract'])
        if topics:
            conn.execute('UPDATE articles SET topics = ? WHERE id = ?',
                         (json.dumps(topics), row['id']))
            processed += 1
            if processed % 10 == 0:
                conn.commit()
                print(f'  [{processed}/{len(rows)}] {title[:50]} -> {topics}')

        # Rate limit
        if i % 20 == 19:
            time.sleep(1)

    conn.commit()
    print(f'\nDone: {processed} articles got topics')

    # Now auto-categorize the newly tagged articles
    from categorize_articles import categorize
    rows = conn.execute(
        "SELECT id, topics FROM articles WHERE (category IS NULL OR category = '') AND topics IS NOT NULL AND topics != ''"
    ).fetchall()
    categorized = 0
    for row in rows:
        cat = categorize(row['topics'])
        if cat:
            conn.execute('UPDATE articles SET category = ? WHERE id = ?', (cat, row['id']))
            categorized += 1
    conn.commit()
    print(f'Auto-categorized: {categorized} more articles')

    conn.close()


if __name__ == '__main__':
    main()
