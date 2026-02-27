#!/usr/bin/env python3
"""Fetch articles from Stanford Encyclopedia of Philosophy."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from bs4 import BeautifulSoup
from utils.helpers import rate_limited_get, html_to_markdown, save_article, save_index

ENTRIES = [
    "artificial-intelligence",
    "consciousness",
    "chinese-room",
    "turing-test",
    "ethics-ai",
    "computational-mind",
    "functionalism",
    "qualia",
    "mental-representation",
    "cognitive-science",
    "connectionism",
    "embodied-cognition",
    "other-minds",
    "identity-personal",
    "freewill",
]

BASE_URL = "https://plato.stanford.edu/entries"

def fetch_entry(slug):
    """Fetch and parse a SEP entry."""
    url = f"{BASE_URL}/{slug}/"
    try:
        resp = rate_limited_get(url, delay=3)
        soup = BeautifulSoup(resp.text, 'html.parser')

        # Title
        title_el = soup.find('h1') or soup.find('title')
        title = title_el.get_text(strip=True) if title_el else slug

        # Author
        author_div = soup.find('div', id='article-copyright') or soup.find('div', id='pubinfo')
        author = ""
        if author_div:
            author = author_div.get_text(strip=True).split('\n')[0]

        # Main content
        main = soup.find('div', id='aueditable') or soup.find('div', id='main-text') or soup.find('article')
        if not main:
            # Fallback: get the main content area
            main = soup.find('div', {'role': 'main'})

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
    base_dir = os.path.join(os.path.dirname(__file__), "..", "research", "sep")
    print("=== Fetching Stanford Encyclopedia of Philosophy ===")

    articles = []
    for slug in ENTRIES:
        print(f"  Fetching: {slug}")
        result = fetch_entry(slug)
        if result:
            meta = {
                "title": result["title"],
                "author": result["author"],
                "date": "",
                "source": "sep",
                "url": result["url"],
            }
            filename = f"{slug}.md"
            save_article(base_dir, filename, meta, result["content"])
            articles.append({**meta, "filename": filename, "length": len(result["content"])})
            print(f"    Saved ({len(result['content'])} chars)")

    save_index(base_dir, articles)
    print(f"\nTotal SEP articles: {len(articles)}")

if __name__ == "__main__":
    main()
