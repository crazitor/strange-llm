#!/usr/bin/env python3
"""Extract arguments (claim/evidence/counterargument) from high-importance articles.

Runs in batches using DeepSeek. Supports --resume to continue from where it left off.

Usage:
    python3.11 extract_arguments.py [--resume] [--limit 50] [--min-importance 8.0]
"""

import argparse
import json
import os
import sqlite3
import time

RESEARCH_DIR = os.path.join(os.path.dirname(__file__), '..', 'research')
DB_PATH = os.path.join(RESEARCH_DIR, 'corpus.db')

CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS arguments (
    id INTEGER PRIMARY KEY,
    source_type TEXT,
    source_id INTEGER,
    claim TEXT,
    evidence TEXT,
    counterargument TEXT,
    topic TEXT
);
CREATE INDEX IF NOT EXISTS idx_arg_source ON arguments(source_type, source_id);
CREATE INDEX IF NOT EXISTS idx_arg_topic ON arguments(topic);

CREATE TABLE IF NOT EXISTS argument_extraction_progress (
    source_type TEXT,
    source_id INTEGER,
    extracted_at TEXT,
    PRIMARY KEY(source_type, source_id)
);
"""

EXTRACT_PROMPT = """Analyze this academic text and extract the main arguments.
For each distinct argument found, output a JSON array of objects with these fields:
- "claim": The main claim or thesis (1-2 sentences)
- "evidence": The evidence or reasoning supporting the claim (1-2 sentences)
- "counterargument": Any counterargument addressed, or "None stated"
- "topic": A short topic label (2-4 words, e.g. "consciousness", "machine learning ethics")

Extract 1-5 arguments. Output ONLY valid JSON array, no other text.

Text:
{text}"""


def setup_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.executescript(CREATE_TABLE)
    conn.commit()
    return conn


def get_deepseek_client():
    from openai import OpenAI
    key = os.environ.get('DEEPSEEK_API_KEY', 'sk-1556a07369cf474f8e886c130e3584ca')
    return OpenAI(api_key=key, base_url='https://api.deepseek.com')


def extract_from_article(client, text):
    """Call DeepSeek to extract arguments from text."""
    prompt = EXTRACT_PROMPT.format(text=text[:4000])
    try:
        resp = client.chat.completions.create(
            model='deepseek-chat',
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=1000, temperature=0.3
        )
        raw = resp.choices[0].message.content.strip()
        # Try to parse JSON
        if raw.startswith('```'):
            raw = raw.split('```')[1]
            if raw.startswith('json'):
                raw = raw[4:]
        return json.loads(raw)
    except (json.JSONDecodeError, Exception) as e:
        print(f'  Parse error: {e}')
        return []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--resume', action='store_true')
    parser.add_argument('--limit', type=int, default=200)
    parser.add_argument('--min-importance', type=float, default=8.0)
    args = parser.parse_args()

    conn = setup_db()
    ds = get_deepseek_client()

    # Get articles to process
    if args.resume:
        rows = conn.execute('''
            SELECT a.id, a.title, a.content, a.abstract
            FROM articles a
            WHERE a.importance >= ?
            AND a.id NOT IN (SELECT source_id FROM argument_extraction_progress WHERE source_type='article')
            ORDER BY a.importance DESC
            LIMIT ?
        ''', (args.min_importance, args.limit)).fetchall()
    else:
        rows = conn.execute('''
            SELECT id, title, content, abstract FROM articles
            WHERE importance >= ?
            ORDER BY importance DESC LIMIT ?
        ''', (args.min_importance, args.limit)).fetchall()
        # Clear existing for non-resume
        conn.execute("DELETE FROM arguments WHERE source_type='article' AND source_id IN (SELECT id FROM articles WHERE importance >= ?)", (args.min_importance,))
        conn.commit()

    print(f'Processing {len(rows)} articles (importance >= {args.min_importance})...')

    total_args = 0
    for i, row in enumerate(rows):
        text = row['content'] or row['abstract'] or ''
        if not text.strip():
            continue

        print(f'[{i+1}/{len(rows)}] {row["title"][:60]}...')
        arguments = extract_from_article(ds, text)

        for arg in arguments:
            if not isinstance(arg, dict) or 'claim' not in arg:
                continue
            conn.execute(
                'INSERT INTO arguments (source_type, source_id, claim, evidence, counterargument, topic) VALUES (?,?,?,?,?,?)',
                ('article', row['id'], arg.get('claim', ''), arg.get('evidence', ''),
                 arg.get('counterargument', 'None stated'), arg.get('topic', ''))
            )
            total_args += 1

        conn.execute(
            'INSERT OR REPLACE INTO argument_extraction_progress (source_type, source_id) VALUES (?,?)',
            ('article', row['id'])
        )
        conn.commit()

        # Rate limit
        time.sleep(0.5)

    print(f'\nDone: extracted {total_args} arguments from {len(rows)} articles')
    conn.close()


if __name__ == '__main__':
    main()
