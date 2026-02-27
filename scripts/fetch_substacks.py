#!/usr/bin/env python3
"""Fetch full articles from Substack blogs via sitemap + RSS + HTML scraping."""
import sys, os, re, xml.etree.ElementTree as ET
sys.path.insert(0, os.path.dirname(__file__))
import feedparser
from bs4 import BeautifulSoup
from utils.helpers import rate_limited_get, html_to_markdown, save_article, save_index, slugify

BLOGS = {
    "aiguide": {"base": "https://aiguide.substack.com", "author": "Melanie Mitchell"},
    "garymarcus": {"base": "https://garymarcus.substack.com", "author": "Gary Marcus"},
    "fchollet": {"base": "https://fchollet.substack.com", "author": "François Chollet"},
    "scottaaronson": {"base": "https://scottaaronson.substack.com", "author": "Scott Aaronson"},
    "thezvi": {"base": "https://thezvi.substack.com", "author": "Zvi Mowshowitz"},
    "importai": {"base": "https://importai.substack.com", "author": "Jack Clark"},
    "aisnakeoil": {"base": "https://aisnakeoil.substack.com", "author": "Arvind Narayanan & Sayash Kapoor"},
}

def get_all_post_urls(base_url):
    """Get ALL post URLs from sitemap (not limited to 20 like RSS)."""
    urls = []
    try:
        resp = rate_limited_get(f"{base_url}/sitemap.xml", delay=1)
        root = ET.fromstring(resp.content)
        ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

        # Check for sitemap index (links to sub-sitemaps)
        sub_sitemaps = root.findall('.//sm:sitemap/sm:loc', ns) or root.findall('.//sm:loc', ns)
        sitemap_urls = []
        for loc in sub_sitemaps:
            u = loc.text.strip()
            if 'posts' in u.lower() or 'sitemap' in u.lower():
                sitemap_urls.append(u)

        if not sitemap_urls:
            # It's a flat sitemap
            for loc in root.findall('.//sm:url/sm:loc', ns):
                u = loc.text.strip()
                if '/p/' in u:
                    urls.append(u)
        else:
            for sm_url in sitemap_urls:
                try:
                    resp2 = rate_limited_get(sm_url, delay=1)
                    root2 = ET.fromstring(resp2.content)
                    for loc in root2.findall('.//sm:url/sm:loc', ns) or root2.findall('.//sm:loc', ns):
                        u = loc.text.strip()
                        if '/p/' in u:
                            urls.append(u)
                except Exception:
                    continue
    except Exception as e:
        print(f"    Sitemap error: {e}")

    return list(dict.fromkeys(urls))  # dedupe, preserve order

def get_rss_urls(base_url):
    """Fallback: get post URLs from RSS feed."""
    feed = feedparser.parse(f"{base_url}/feed")
    return [(e.get("link", ""), e.get("title", ""), e.get("published_parsed")) for e in feed.entries]

def fetch_article(url):
    """Fetch and extract full article content from a Substack post URL."""
    try:
        resp = rate_limited_get(url, delay=1.5)
        soup = BeautifulSoup(resp.text, 'html.parser')

        # Title
        title_el = soup.find('h1', class_='post-title') or soup.find('h1')
        title = title_el.get_text(strip=True) if title_el else ""

        # Date
        date = ""
        time_el = soup.find('time') or soup.find('span', class_='post-date')
        if time_el:
            date = time_el.get('datetime', time_el.get_text(strip=True))[:10]

        # Body — multiple possible selectors
        body = (soup.find('div', class_='body markup') or
                soup.find('div', class_='post-content') or
                soup.find('div', class_='available-content') or
                soup.find('article'))

        if not body:
            return None

        # Remove subscription CTAs, buttons, etc.
        for tag in body.find_all(['div', 'section'], class_=re.compile(r'subscription|subscribe|paywall|footer')):
            tag.decompose()

        content = html_to_markdown(str(body))
        if len(content) < 100:
            return None

        return {"title": title, "date": date, "content": content, "url": url}
    except Exception as e:
        return None

def fetch_blog(name, info, base_dir):
    """Fetch all articles from a Substack blog."""
    base_url = info["base"]
    author = info["author"]
    out_dir = os.path.join(base_dir, "substacks", name)

    print(f"\n  === {name} ({author}) ===")

    # Get URLs from sitemap first
    post_urls = get_all_post_urls(base_url)
    print(f"    Sitemap: {len(post_urls)} post URLs")

    # If sitemap didn't work well, supplement with RSS
    if len(post_urls) < 10:
        rss_data = get_rss_urls(base_url)
        rss_urls = [u for u, _, _ in rss_data]
        existing = set(post_urls)
        for u in rss_urls:
            if u not in existing:
                post_urls.append(u)
        print(f"    After RSS supplement: {len(post_urls)} URLs")

    articles = []
    for i, url in enumerate(post_urls):
        print(f"    [{i+1}/{len(post_urls)}] {url.split('/p/')[-1][:50]}...")
        result = fetch_article(url)
        if not result:
            continue

        meta = {
            "title": result["title"],
            "author": author,
            "date": result["date"],
            "source": f"substack_{name}",
            "url": result["url"],
        }
        slug = slugify(result["title"]) or slugify(url.split('/p/')[-1])
        filename = f"{slug}.md"
        save_article(out_dir, filename, meta, result["content"])
        articles.append({**meta, "filename": filename, "length": len(result["content"])})

    save_index(out_dir, articles)
    return articles

def main():
    base_dir = os.path.join(os.path.dirname(__file__), "..", "research")
    print("=== Fetching Substack Blogs (Full Archive) ===")

    total = 0
    for name, info in BLOGS.items():
        articles = fetch_blog(name, info, base_dir)
        print(f"  {name}: {len(articles)} articles saved")
        total += len(articles)

    print(f"\nTotal Substack articles: {total}")

if __name__ == "__main__":
    main()
