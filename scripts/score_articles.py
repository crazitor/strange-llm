#!/usr/bin/env python3
"""Score articles for importance and assign topic tags using Claude Haiku."""

import json
import os
import sqlite3
import sys
import time

RESEARCH_DIR = os.path.join(os.path.dirname(__file__), '..', 'research')
DB_PATH = os.path.join(RESEARCH_DIR, 'corpus.db')

TOPICS = [
    'consciousness', 'alignment', 'ethics', 'philosophy-of-mind',
    'language-understanding', 'embodiment', 'functionalism', 'chinese-room',
    'hard-problem', 'turing-test', 'ai-safety', 'sentience', 'free-will',
    'qualia', 'superintelligence'
]

# Known important authors get a boost
IMPORTANT_AUTHORS = {
    'David Chalmers', 'Ned Block', 'Daniel Dennett', 'John Searle',
    'Susan Schneider', 'Murray Shanahan', 'Yoshua Bengio', 'Nick Bostrom',
    'Stuart Russell', 'Eliezer Yudkowsky', 'Paul Christiano', 'Scott Aaronson',
    'Luciano Floridi', 'Emily Bender', 'Eric Schwitzgebel', 'Francois Chollet',
    'Gary Marcus', 'Thomas Nagel', 'Giulio Tononi', 'Christof Koch'
}

BATCH_SIZE = 20  # Articles per API call

def score_with_heuristics(row):
    """Compute a heuristic score (0-10) from metadata signals."""
    score = 5.0  # baseline

    # Community signal
    if row['score'] is not None:
        if row['score'] > 100:
            score += 2.0
        elif row['score'] > 50:
            score += 1.5
        elif row['score'] > 20:
            score += 1.0
        elif row['score'] < 0:
            score -= 1.0

    # Citation signal
    if row['citations'] is not None:
        if row['citations'] > 1000:
            score += 2.5
        elif row['citations'] > 500:
            score += 2.0
        elif row['citations'] > 100:
            score += 1.5
        elif row['citations'] > 50:
            score += 1.0

    # Author weight
    author = row['author'] or ''
    for imp_author in IMPORTANT_AUTHORS:
        if imp_author.lower() in author.lower():
            score += 1.5
            break

    # Source weight
    source = row['source'] or ''
    if source in ('sep', 'iep'):
        score += 1.0  # encyclopedia entries are reliable
    elif source == 'philpapers':
        score += 0.5
    elif source == 'alignment_forum_dedicated':
        score += 0.5

    # Length signal (longer = more substantial, up to a point)
    wc = row['word_count'] or 0
    if wc > 10000:
        score += 0.5
    elif wc > 5000:
        score += 0.3

    return max(0, min(10, score))

def score_with_llm(conn):
    """Use DeepSeek to score articles and assign topics."""
    try:
        from openai import OpenAI
    except ImportError:
        print('openai package not installed. Run: pip install openai')
        return False

    api_key = os.environ.get('DEEPSEEK_API_KEY', 'sk-1556a07369cf474f8e886c130e3584ca')
    client = OpenAI(api_key=api_key, base_url='https://api.deepseek.com')
    c = conn.cursor()

    # Get articles that haven't been LLM-scored yet
    c.execute('''SELECT id, title, author, abstract, source, score, citations
                 FROM articles WHERE topics IS NULL
                 ORDER BY importance DESC NULLS LAST
                 LIMIT 3000''')
    rows = c.fetchall()

    if not rows:
        print('All articles already scored.')
        return True

    print(f'LLM scoring {len(rows)} articles in batches of {BATCH_SIZE}...')

    topics_str = ', '.join(TOPICS)
    processed = 0
    errors = 0

    for i in range(0, len(rows), BATCH_SIZE):
        batch = rows[i:i + BATCH_SIZE]

        # Build batch prompt
        articles_text = []
        for row in batch:
            entry = f"ID:{row[0]} | Title: {row[1]}"
            if row[2]:
                entry += f" | Author: {row[2]}"
            if row[4]:
                entry += f" | Abstract: {row[4][:300]}"
            articles_text.append(entry)

        prompt = f"""Rate each article's importance (0-10) for understanding AI consciousness and philosophy.
Assign 1-3 topic tags from: {topics_str}
Write a 1-sentence summary.

Articles:
{chr(10).join(articles_text)}

Return JSON array: [{{"id": N, "importance": X.X, "topics": ["tag1"], "summary": "..."}}]
Only valid JSON, no other text."""

        try:
            response = client.chat.completions.create(
                model='deepseek-chat',
                max_tokens=4000,
                messages=[{'role': 'user', 'content': prompt}]
            )

            text = response.choices[0].message.content.strip()
            # Try to extract JSON from response
            if text.startswith('['):
                results = json.loads(text)
            else:
                # Find JSON array in response
                start = text.find('[')
                end = text.rfind(']') + 1
                if start >= 0 and end > start:
                    results = json.loads(text[start:end])
                else:
                    print(f'  Batch {i//BATCH_SIZE}: Could not parse response')
                    errors += 1
                    continue

            for r in results:
                aid = r.get('id')
                imp = r.get('importance', 5.0)
                topics = json.dumps(r.get('topics', []))
                summary = r.get('summary', '')
                if aid:
                    c.execute('''UPDATE articles
                                 SET importance = ?, topics = ?, summary = ?
                                 WHERE id = ?''',
                              (float(imp), topics, summary, aid))

            processed += len(batch)
            conn.commit()
            print(f'  {processed}/{len(rows)} scored...')

            # Rate limit
            time.sleep(0.5)

        except Exception as e:
            print(f'  Batch error: {e}')
            errors += 1
            time.sleep(2)

    print(f'LLM scoring complete: {processed} processed, {errors} errors')
    return True

def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    # Step 1: Heuristic scoring for all articles
    print('Step 1: Heuristic scoring...')
    c.execute('SELECT id, title, author, source, score, citations, word_count FROM articles')
    rows = c.fetchall()

    for row in rows:
        h_score = score_with_heuristics(row)
        c.execute('UPDATE articles SET importance = ? WHERE id = ?',
                  (h_score, row['id']))

    conn.commit()
    print(f'  Heuristic scores set for {len(rows)} articles')

    # Show top 10 by heuristic
    c.execute('''SELECT title, author, source, importance, score, citations
                 FROM articles ORDER BY importance DESC LIMIT 10''')
    print('\nTop 10 by heuristic score:')
    for r in c.fetchall():
        print(f'  {r[3]:.1f} | {r[0][:60]} [{r[2]}]')

    # Step 2: LLM scoring (optional, requires API key)
    if '--llm' in sys.argv:
        print('\nStep 2: LLM scoring with Claude Haiku...')
        score_with_llm(conn)
    else:
        print('\nSkipping LLM scoring. Run with --llm to enable.')
        print('Setting default topics based on keywords...')

        # Simple keyword-based topic assignment as fallback
        topic_keywords = {
            'consciousness': ['consciousness', 'conscious', 'awareness', 'qualia', 'phenomenal'],
            'alignment': ['alignment', 'aligned', 'corrigib'],
            'ethics': ['ethic', 'moral', 'rights'],
            'philosophy-of-mind': ['mind', 'mental', 'cognitive', 'cognition'],
            'language-understanding': ['language', 'linguistic', 'NLP', 'LLM', 'GPT'],
            'functionalism': ['functional', 'functionalism', 'computationalism'],
            'chinese-room': ['chinese room', 'searle'],
            'hard-problem': ['hard problem', 'explanatory gap'],
            'turing-test': ['turing test', 'imitation game'],
            'ai-safety': ['safety', 'existential risk', 'x-risk'],
            'sentience': ['sentien', 'feeling', 'suffer'],
            'superintelligence': ['superintelligen', 'AGI', 'artificial general'],
        }

        c.execute('SELECT id, title, abstract FROM articles WHERE topics IS NULL')
        for row in c.fetchall():
            text = ((row[1] or '') + ' ' + (row[2] or '')).lower()
            matched = []
            for topic, keywords in topic_keywords.items():
                if any(kw.lower() in text for kw in keywords):
                    matched.append(topic)
            if matched:
                c.execute('UPDATE articles SET topics = ? WHERE id = ?',
                          (json.dumps(matched[:3]), row[0]))

        conn.commit()
        c.execute('SELECT count(*) FROM articles WHERE topics IS NOT NULL')
        print(f'  Topics assigned to {c.fetchone()[0]} articles')

    conn.close()
    print('\nDone.')

if __name__ == '__main__':
    main()
