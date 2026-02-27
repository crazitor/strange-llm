#!/usr/bin/env python3
"""Fetch articles from Internet Encyclopedia of Philosophy (IEP)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from bs4 import BeautifulSoup
from utils.helpers import rate_limited_get, html_to_markdown, save_article, save_index

ENTRIES = [
    "artificial-intelligence",
    "chinese-room-argument",
    "consciousness",
    "qualia",
    "functism",                     # functionalism
    "intentio",                     # intentionality
    "computational-theory-of-mind", # computationalism
    "connectionism",
    "embodied-cognition",
    "freewill",
    "mental-c",                     # mental causation
    "mult-rea",                     # multiple realizability
    "hard-problem-of-conciousness", # (IEP's actual slug, with typo)
    "phenom",                       # phenomenology
    "dualism",
    "behaviorism",
    # Round 2 — discovered via web search
    "theomind",                     # theory of mind
    "dualism-and-mind",             # dualism and mind (detailed)
    "descartes-mind-body-distinction-dualism",
    "sellars",                      # Wilfrid Sellars: philosophy of mind
    "emergence",
]

BASE_URL = "https://iep.utm.edu"


def fetch_entry(slug):
    """Fetch and parse an IEP entry."""
    url = f"{BASE_URL}/{slug}/"
    try:
        resp = rate_limited_get(url, delay=3)
        soup = BeautifulSoup(resp.text, 'html.parser')

        # Title — skip the site-title h1
        title_el = soup.find('h1', class_='entry-title')
        if not title_el:
            for h1 in soup.find_all('h1'):
                classes = h1.get('class', [])
                if 'site-title' not in classes and 'widget-title' not in classes:
                    title_el = h1
                    break
        title = title_el.get_text(strip=True) if title_el else slug

        # Author — IEP typically has author info in the article itself
        author = ""
        # Try meta tag
        author_meta = soup.find('meta', {'name': 'author'})
        if author_meta:
            author = author_meta.get('content', '')
        if not author:
            # Look for "Author Information" section or byline
            for el in soup.find_all(['p', 'div']):
                text = el.get_text(strip=True)
                if text.startswith('Author:') or text.startswith('By '):
                    author = text.split(':', 1)[-1].strip() if ':' in text else text[3:].strip()
                    break

        # Main content — WordPress structure
        main = (soup.find('div', class_='entry-content') or
                soup.find('article') or
                soup.find('div', id='content'))

        if not main:
            print(f"    Could not find content for {slug}")
            return None

        content = html_to_markdown(str(main))

        if len(content) < 200:
            print(f"    Content too short for {slug}")
            return None

        return {
            "title": title,
            "author": author,
            "slug": slug,
            "url": url,
            "content": content,
        }
    except Exception as e:
        print(f"    Error fetching {slug}: {e}")
        return None


def main():
    base_dir = os.path.join(os.path.dirname(__file__), "..", "research", "iep")
    print("=== Fetching Internet Encyclopedia of Philosophy ===")

    articles = []
    for slug in ENTRIES:
        print(f"  Fetching: {slug}")
        result = fetch_entry(slug)
        if result:
            meta = {
                "title": result["title"],
                "author": result["author"],
                "date": "",
                "source": "iep",
                "url": result["url"],
            }
            filename = f"{slug}.md"
            save_article(base_dir, filename, meta, result["content"])
            articles.append({**meta, "filename": filename, "length": len(result["content"])})
            print(f"    Saved ({len(result['content'])} chars)")

    save_index(base_dir, articles)
    print(f"\nTotal IEP articles: {len(articles)}")


if __name__ == "__main__":
    main()
