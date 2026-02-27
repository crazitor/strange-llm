#!/usr/bin/env python3
"""Fetch Luciano Floridi's papers via Semantic Scholar API + known open-access sources."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from bs4 import BeautifulSoup
from utils.helpers import rate_limited_get, html_to_markdown, save_article, save_pdf, save_index, slugify

# Correct Semantic Scholar author ID for Luciano Floridi
# Found via: https://api.semanticscholar.org/graph/v1/author/search?query=Luciano+Floridi
FLORIDI_S2_IDS = []  # Will resolve dynamically

# Correct author ID: 1982425 (446 papers, h-index 85)
FLORIDI_AUTHOR_ID = "1982425"
S2_AUTHOR_SEARCH = "https://api.semanticscholar.org/graph/v1/author/search?query=Luciano+Floridi&limit=10&fields=name,paperCount,hIndex"
S2_PAPERS_URL = "https://api.semanticscholar.org/graph/v1/author/{aid}/papers?fields=title,url,abstract,year,openAccessPdf,citationCount,externalIds&limit=500&offset={offset}"

AI_KEYWORDS = [
    "artificial", "intelligence", "ai ", " ai", "digital", "ethics", "robot",
    "algorithm", "machine", "information", "agent", "autonomous", "semantic",
    "turing", "consciousness", "moral", "trust", "governance", "regulation",
    "automation", "computer", "data", "privacy", "surveillance", "technology",
    "internet", "online", "cyber", "software", "neural", "deep learning",
]

def find_floridi_author_id():
    """Return the known correct Semantic Scholar author ID for Luciano Floridi."""
    print(f"    Using known author ID: {FLORIDI_AUTHOR_ID} (446 papers, h=85)")
    return FLORIDI_AUTHOR_ID

def fetch_s2_papers(author_id):
    """Fetch all papers for an author from Semantic Scholar with pagination."""
    all_papers = []
    offset = 0
    while True:
        try:
            resp = rate_limited_get(S2_PAPERS_URL.format(aid=author_id, offset=offset), delay=1)
            data = resp.json()
            papers = data.get("data", [])
            if not papers:
                break
            all_papers.extend(papers)
            offset += len(papers)
            print(f"    Fetched {len(all_papers)} papers so far...")
            if len(papers) < 500:
                break
        except Exception as e:
            print(f"    Pagination error at offset {offset}: {e}")
            break
    return all_papers

def is_ai_relevant(title):
    """Check if paper title is AI/digital-ethics related."""
    t = title.lower()
    return any(kw in t for kw in AI_KEYWORDS)

def main():
    base_dir = os.path.join(os.path.dirname(__file__), "..", "research", "floridi_papers")
    print("=== Fetching Floridi Papers ===")

    # 1. Find correct author ID
    print("  Searching for Luciano Floridi on Semantic Scholar...")
    author_id = find_floridi_author_id()
    if not author_id:
        print("  Could not find author. Aborting.")
        return

    # 2. Fetch all papers
    print(f"  Fetching papers for author ID {author_id}...")
    all_papers = fetch_s2_papers(author_id)
    print(f"  Total papers found: {len(all_papers)}")

    # 3. Filter AI-related
    ai_papers = [p for p in all_papers if p.get("title") and is_ai_relevant(p["title"])]
    # Sort by citation count
    ai_papers.sort(key=lambda p: p.get("citationCount", 0), reverse=True)
    print(f"  AI-related papers: {len(ai_papers)}")

    papers_meta = []
    pdf_count = 0

    for i, p in enumerate(ai_papers):
        title = p["title"]
        print(f"  [{i+1}/{len(ai_papers)}] {title[:60]}...")

        # Try open-access PDF
        pdf_url = (p.get("openAccessPdf") or {}).get("url")
        if pdf_url:
            try:
                resp = rate_limited_get(pdf_url, delay=1.5)
                ct = resp.headers.get("content-type", "")
                if "pdf" in ct and len(resp.content) > 5000:
                    slug = slugify(title)
                    save_pdf(base_dir, f"{slug}.pdf", resp.content)
                    papers_meta.append({
                        "title": title,
                        "author": "Luciano Floridi",
                        "year": p.get("year"),
                        "source": "semantic_scholar_pdf",
                        "url": p.get("url", ""),
                        "citations": p.get("citationCount", 0),
                        "filename": f"{slug}.pdf",
                        "size_kb": len(resp.content) // 1024,
                    })
                    pdf_count += 1
                    continue
            except Exception:
                pass

        # Save abstract as markdown
        abstract = p.get("abstract", "")
        content = f"## Abstract\n\n{abstract}\n" if abstract else f"[No abstract available. See: {p.get('url', '')}]\n"
        meta = {
            "title": title,
            "author": "Luciano Floridi",
            "date": str(p.get("year", "")),
            "source": "semantic_scholar",
            "url": p.get("url", ""),
            "citations": p.get("citationCount", 0),
        }
        slug = slugify(title)
        save_article(base_dir, f"{slug}.md", meta, content)
        papers_meta.append({**meta, "filename": f"{slug}.md", "length": len(content)})

    save_index(base_dir, papers_meta)
    print(f"\nTotal Floridi papers: {len(papers_meta)} ({pdf_count} PDFs)")

if __name__ == "__main__":
    main()
