#!/usr/bin/env python3
"""Fetch metadata and abstracts from PhilPapers."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from bs4 import BeautifulSoup
from utils.helpers import rate_limited_get, html_to_markdown, save_article, save_index, slugify

# PhilPapers category URLs for relevant topics
CATEGORIES = {
    "philosophy-of-ai": "https://philpapers.org/browse/philosophy-of-artificial-intelligence",
    "artificial-consciousness": "https://philpapers.org/browse/artificial-consciousness",
    "machine-ethics": "https://philpapers.org/browse/machine-ethics",
    "chinese-room": "https://philpapers.org/browse/the-chinese-room-argument",
    "ai-ethics": "https://philpapers.org/browse/ethics-of-artificial-intelligence",
}

def fetch_category(name, url, base_dir):
    """Fetch papers from a PhilPapers category page."""
    print(f"\n  Category: {name}")
    try:
        resp = rate_limited_get(url, delay=3)
    except Exception as e:
        print(f"    Error: {e}")
        return []

    soup = BeautifulSoup(resp.text, 'html.parser')
    papers = []

    # PhilPapers lists entries with class 'entry'
    entries = soup.find_all('li', class_='entry') or soup.find_all('div', class_='entry')
    if not entries:
        # Try alternate selectors
        entries = soup.find_all('div', class_='listing')

    print(f"    Found {len(entries)} entries")

    for entry in entries[:30]:  # Cap per category
        try:
            # Title and link
            title_el = entry.find('span', class_='title') or entry.find('a', class_='title')
            if not title_el:
                title_link = entry.find('a')
                if title_link:
                    title_el = title_link
            if not title_el:
                continue

            title = title_el.get_text(strip=True)
            link = title_el if title_el.name == 'a' else title_el.find('a')
            url_paper = ""
            if link and link.get('href'):
                href = link['href']
                url_paper = href if href.startswith('http') else f"https://philpapers.org{href}"

            # Author
            author_el = entry.find('span', class_='name') or entry.find('span', class_='authors')
            author = author_el.get_text(strip=True) if author_el else ""

            # Abstract (if available inline)
            abstract_el = entry.find('div', class_='abstract') or entry.find('blockquote')
            abstract = abstract_el.get_text(strip=True) if abstract_el else ""

            papers.append({
                "title": title,
                "author": author,
                "url": url_paper,
                "abstract": abstract,
                "category": name,
            })
        except Exception:
            continue

    return papers

def main():
    base_dir = os.path.join(os.path.dirname(__file__), "..", "research", "philpapers")
    print("=== Fetching PhilPapers ===")

    all_papers = []
    seen_titles = set()

    for name, url in CATEGORIES.items():
        papers = fetch_category(name, url, base_dir)
        for p in papers:
            if p["title"] not in seen_titles:
                seen_titles.add(p["title"])
                all_papers.append(p)

    print(f"\n  Total unique papers: {len(all_papers)}")

    # Save each paper as a short .md with available info
    for p in all_papers:
        content = ""
        if p.get("abstract"):
            content = f"## Abstract\n\n{p['abstract']}\n"
        else:
            content = f"[Metadata only — full text at: {p.get('url', 'N/A')}]\n"

        meta = {
            "title": p["title"],
            "author": p.get("author", ""),
            "source": "philpapers",
            "url": p.get("url", ""),
            "category": p.get("category", ""),
        }
        slug = slugify(p["title"])
        save_article(base_dir, f"{slug}.md", meta, content)

    save_index(base_dir, all_papers)
    print(f"\nTotal PhilPapers entries: {len(all_papers)}")

if __name__ == "__main__":
    main()
