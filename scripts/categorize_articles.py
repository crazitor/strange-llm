#!/usr/bin/env python3
"""Auto-categorize articles based on their topics field."""

import json
import os
import sqlite3

RESEARCH_DIR = os.path.join(os.path.dirname(__file__), '..', 'research')
DB_PATH = os.path.join(RESEARCH_DIR, 'corpus.db')

# Priority-ordered: first matching category wins
CATEGORY_RULES = [
    ('artificial-consciousness', [
        'consciousness', 'qualia', 'hard-problem', 'phenomenal-consciousness',
        'sentience', 'subjective-experience', 'machine-consciousness',
    ]),
    ('philosophy-of-mind', [
        'philosophy-of-mind', 'functionalism', 'dualism', 'physicalism',
        'mental-states', 'intentionality', 'zombies', 'mind-body',
        'emergentism', 'panpsychism',
    ]),
    ('language-understanding', [
        'language-understanding', 'chinese-room', 'symbol-grounding',
        'semantics', 'meaning', 'llm', 'large-language-models',
        'gpt', 'chatgpt', 'natural-language',
    ]),
    ('ai-ethics', [
        'ai-ethics', 'ethics', 'moral-status', 'moral-agency',
        'responsibility', 'fairness', 'bias', 'justice',
        'human-rights', 'dignity',
    ]),
    ('machine-ethics', [
        'machine-ethics', 'robot-ethics', 'artificial-moral-agent',
        'moral-machines', 'ethical-ai',
    ]),
    ('ai-safety', [
        'ai-safety', 'alignment', 'existential-risk', 'superintelligence',
        'x-risk', 'control-problem', 'value-alignment',
    ]),
    ('cognitive-science', [
        'cognitive-science', 'cognition', 'embodiment', 'embodied-cognition',
        'enactivism', 'situated-cognition', 'perception', 'attention',
        'memory', 'learning', 'neuroscience',
    ]),
    ('philosophy-of-information', [
        'philosophy-of-information', 'information', 'floridi',
        'information-theory', 'digital-ontology',
    ]),
    ('philosophy-of-ai', [
        'philosophy-of-ai', 'artificial-intelligence', 'turing-test',
        'intelligence', 'computation', 'computationalism',
        'strong-ai', 'weak-ai', 'agi',
    ]),
    ('epistemology', [
        'epistemology', 'knowledge', 'justification', 'belief',
        'understanding', 'explanation', 'rationality',
    ]),
]


def categorize(topics_json):
    """Return category based on topics list."""
    if not topics_json:
        return None
    try:
        topics = json.loads(topics_json) if isinstance(topics_json, str) else topics_json
    except (json.JSONDecodeError, TypeError):
        return None

    topics_lower = set(t.lower().strip() for t in topics)

    for category, keywords in CATEGORY_RULES:
        if topics_lower & set(keywords):
            return category
    return None


def run():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    rows = conn.execute(
        "SELECT id, topics FROM articles WHERE (category IS NULL OR category = '') AND topics IS NOT NULL"
    ).fetchall()

    print(f'Uncategorized articles with topics: {len(rows)}')

    updated = 0
    cat_counts = {}
    for row in rows:
        cat = categorize(row['topics'])
        if cat:
            conn.execute('UPDATE articles SET category = ? WHERE id = ?', (cat, row['id']))
            cat_counts[cat] = cat_counts.get(cat, 0) + 1
            updated += 1

    conn.commit()

    # Stats
    remaining = conn.execute(
        "SELECT count(*) FROM articles WHERE category IS NULL OR category = ''"
    ).fetchone()[0]

    print(f'\nCategorized: {updated}')
    for cat, n in sorted(cat_counts.items(), key=lambda x: -x[1]):
        print(f'  {cat}: {n}')
    print(f'\nStill uncategorized: {remaining}')

    conn.close()


if __name__ == '__main__':
    run()
