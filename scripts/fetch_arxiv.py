#!/usr/bin/env python3
"""Fetch AI philosophy papers from ArXiv via its public API."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import feedparser
from utils.helpers import rate_limited_get, save_article, save_pdf, save_index, slugify

ARXIV_API = "https://export.arxiv.org/api/query"

SEARCH_TERMS = [
    "AI consciousness",
    "Chinese Room",
    "machine understanding",
    "LLM reasoning",
    "artificial general intelligence philosophy",
    "embodied cognition AI",
    "stochastic parrot",
    "AI sentience",
    "symbol grounding",
    "intentionality AI",
]

CATEGORIES = ["cs.AI", "cs.CY", "cs.CL"]

MAX_PER_QUERY = 100


def search_arxiv(query, category=None, start=0, max_results=MAX_PER_QUERY):
    """Search ArXiv API and return parsed entries."""
    search_query = f'all:"{query}"'
    if category:
        search_query += f" AND cat:{category}"
    params = f"search_query={search_query}&start={start}&max_results={max_results}&sortBy=relevance"
    url = f"{ARXIV_API}?{params}"
    try:
        resp = rate_limited_get(url, delay=3, timeout=60)
        feed = feedparser.parse(resp.content)
        return feed.entries
    except Exception as e:
        print(f"    Error querying '{query}': {e}")
        return []


def entry_to_paper(entry):
    """Convert feedparser entry to paper dict."""
    arxiv_id = entry.get("id", "").split("/abs/")[-1].split("v")[0]
    if not arxiv_id:
        arxiv_id = entry.get("id", "").rsplit("/", 1)[-1].split("v")[0]

    categories = [t.get("term", "") for t in entry.get("tags", [])]
    pdf_url = ""
    for link in entry.get("links", []):
        if link.get("type") == "application/pdf":
            pdf_url = link["href"]
            break
    if not pdf_url and arxiv_id:
        pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"

    return {
        "arxiv_id": arxiv_id,
        "title": entry.get("title", "").replace("\n", " ").strip(),
        "authors": ", ".join(a.get("name", "") for a in entry.get("authors", [])),
        "abstract": entry.get("summary", "").strip(),
        "published": entry.get("published", "")[:10],
        "categories": categories,
        "pdf_url": pdf_url,
        "url": entry.get("id", ""),
    }


def main():
    base_dir = os.path.join(os.path.dirname(__file__), "..", "research", "arxiv")
    print("=== Fetching ArXiv Papers ===")

    seen_ids = set()
    all_papers = []

    # Search each term across categories
    for term in SEARCH_TERMS:
        print(f"\n  Search: \"{term}\"")
        # Search without category filter first (broader)
        entries = search_arxiv(term)
        new = 0
        for entry in entries:
            paper = entry_to_paper(entry)
            if not paper["arxiv_id"] or paper["arxiv_id"] in seen_ids:
                continue
            seen_ids.add(paper["arxiv_id"])
            all_papers.append(paper)
            new += 1
        print(f"    Found {len(entries)} results, {new} new")

    print(f"\n  Total unique papers: {len(all_papers)}")

    # Save abstracts as .md, attempt PDF download for each
    articles_meta = []
    pdf_count = 0

    for i, p in enumerate(all_papers):
        title = p["title"]
        slug = slugify(title) or slugify(p["arxiv_id"])
        print(f"  [{i+1}/{len(all_papers)}] {title[:60]}...")

        # Try PDF download
        if p["pdf_url"]:
            try:
                resp = rate_limited_get(p["pdf_url"], delay=1.5, timeout=60)
                ct = resp.headers.get("content-type", "")
                if "pdf" in ct and len(resp.content) > 5000:
                    save_pdf(base_dir, f"{slug}.pdf", resp.content)
                    articles_meta.append({
                        "title": title,
                        "author": p["authors"],
                        "date": p["published"],
                        "source": "arxiv_pdf",
                        "url": p["url"],
                        "arxiv_id": p["arxiv_id"],
                        "filename": f"{slug}.pdf",
                        "size_kb": len(resp.content) // 1024,
                    })
                    pdf_count += 1
                    continue
            except Exception:
                pass

        # Save abstract as markdown
        content = f"## Abstract\n\n{p['abstract']}\n"
        if p["categories"]:
            content += f"\n**Categories**: {', '.join(p['categories'])}\n"

        meta = {
            "title": title,
            "author": p["authors"],
            "date": p["published"],
            "source": "arxiv",
            "url": p["url"],
            "arxiv_id": p["arxiv_id"],
        }
        save_article(base_dir, f"{slug}.md", meta, content)
        articles_meta.append({**meta, "filename": f"{slug}.md", "length": len(content)})

    save_index(base_dir, articles_meta)
    print(f"\nTotal ArXiv papers: {len(articles_meta)} ({pdf_count} PDFs)")


if __name__ == "__main__":
    main()
