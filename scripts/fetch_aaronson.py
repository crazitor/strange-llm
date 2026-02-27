#!/usr/bin/env python3
"""Fetch AI-relevant posts from Scott Aaronson's blog (Shtetl-Optimized) via RSS."""
import sys, os, re
sys.path.insert(0, os.path.dirname(__file__))
from utils.helpers import rate_limited_get, html_to_markdown, save_article, save_index, slugify
from bs4 import BeautifulSoup

RSS_URL = "https://scottaaronson.blog/?feed=rss2&paged={page}"

AI_KEYWORDS = [
    "ai", "artificial intelligence", "gpt", "llm", "language model",
    "chatgpt", "consciousness", "turing test", "chinese room",
    "machine learning", "deep learning", "neural net", "sentien",
    "alignment", "agi", "singularity", "superintelligen",
    "stochastic parrot", "understanding", "thinking machine",
    "robot", "openai", "anthropic", "google ai", "deepmind",
    "existential risk", "ai safety", "philosophy of mind",
    "free will", "qualia", "hard problem",
]

NS = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "dc": "http://purl.org/dc/elements/1.1/",
}


def is_ai_relevant(title, content_snippet):
    """Check if post is AI-related."""
    text = (title + " " + content_snippet[:2000]).lower()
    return any(kw in text for kw in AI_KEYWORDS)


def fetch_all_posts(max_pages=200):
    """Fetch all posts via paginated RSS, using BeautifulSoup for fault-tolerant XML parsing."""
    all_posts = []
    empty_count = 0
    for page in range(1, max_pages + 1):
        url = RSS_URL.format(page=page)
        try:
            resp = rate_limited_get(url, delay=1.5, timeout=30)
            soup = BeautifulSoup(resp.content, "xml")
            items = soup.find_all("item")
            if not items:
                empty_count += 1
                if empty_count >= 3:
                    print(f"  Page {page}: 3 consecutive empty pages, stopping")
                    break
                continue
            empty_count = 0
            for item in items:
                title = (item.find("title").get_text(strip=True) if item.find("title") else "")
                link = (item.find("link").get_text(strip=True) if item.find("link") else "")
                pub_date = (item.find("pubDate").get_text(strip=True) if item.find("pubDate") else "")
                creator_el = item.find("dc:creator") or item.find("creator")
                creator = (creator_el.get_text(strip=True) if creator_el else "Scott Aaronson")
                content_el = item.find("content:encoded") or item.find("encoded")
                content_html = (content_el.get_text(strip=True) if content_el else "")
                all_posts.append({
                    "title": title,
                    "link": link,
                    "date": pub_date,
                    "author": creator,
                    "html": content_html,
                })
            if page % 20 == 0:
                print(f"  Page {page}: {len(all_posts)} posts so far")
        except Exception as e:
            print(f"  Page {page}: error {e}")
            if "404" in str(e):
                empty_count += 1
                if empty_count >= 3:
                    print(f"  3 consecutive failures, stopping")
                    break
            continue
    return all_posts


def main():
    base_dir = os.path.join(os.path.dirname(__file__), "..", "research", "substacks", "scottaaronson")
    print("=== Fetching Scott Aaronson Blog (Shtetl-Optimized) ===")

    posts = fetch_all_posts()
    print(f"\n  Total posts fetched: {len(posts)}")

    # Filter AI-relevant
    relevant = []
    for p in posts:
        if is_ai_relevant(p["title"], p["html"]):
            relevant.append(p)

    print(f"  AI-relevant posts: {len(relevant)}")

    articles = []
    for p in relevant:
        md = html_to_markdown(p["html"])
        if len(md) < 200:
            continue
        slug = slugify(p["title"])
        meta = {
            "title": p["title"],
            "author": "Scott Aaronson",
            "date": p["date"][:16] if p["date"] else "",
            "source": "scottaaronson_blog",
            "url": p["link"],
        }
        filename = f"{slug}.md"
        save_article(base_dir, filename, meta, md)
        articles.append({**meta, "filename": filename, "length": len(md)})

    save_index(base_dir, articles)
    print(f"\nTotal saved: {len(articles)} articles")


if __name__ == "__main__":
    main()
