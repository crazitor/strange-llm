#!/usr/bin/env python3
"""Fetch papers from David Chalmers' website (consc.net)."""
import sys, os, re
sys.path.insert(0, os.path.dirname(__file__))
from bs4 import BeautifulSoup
from utils.helpers import rate_limited_get, save_pdf, save_index, slugify

PAPERS_URL = "https://consc.net/papers.html"

# Keywords to filter AI/consciousness-related papers
KEYWORDS = [
    "conscious", "consciousness", "artificial intelligence", "ai ",
    "large language model", "llm", "singularity", "zombie",
    "hard problem", "experience", "qualia", "mind", "understanding",
    "computation", "robot", "machine", "virtual", "simulation",
    "extended mind", "phenomenal", "intelligence",
]

def is_relevant(text):
    """Check if paper title/description matches our interests."""
    text_lower = text.lower()
    return any(kw in text_lower for kw in KEYWORDS)

def main():
    base_dir = os.path.join(os.path.dirname(__file__), "..", "research", "chalmers_papers")
    print("=== Fetching Chalmers Papers ===")

    print("  Fetching papers list page...")
    try:
        resp = rate_limited_get(PAPERS_URL, delay=2)
    except Exception as e:
        print(f"  Error: {e}")
        return

    soup = BeautifulSoup(resp.text, 'html.parser')
    links = soup.find_all('a', href=True)

    papers = []
    pdf_links = []

    for link in links:
        href = link['href']
        text = link.get_text(strip=True)
        # Look for PDF links
        if href.endswith('.pdf') and is_relevant(text + " " + str(link.parent)):
            full_url = href if href.startswith('http') else f"https://consc.net/{href.lstrip('/')}"
            pdf_links.append((text, full_url))

    # Deduplicate by URL
    seen_urls = set()
    unique_pdfs = []
    for text, url in pdf_links:
        if url not in seen_urls:
            seen_urls.add(url)
            unique_pdfs.append((text, url))

    print(f"  Found {len(unique_pdfs)} relevant PDFs")

    for i, (title, url) in enumerate(unique_pdfs[:25]):  # Cap at 25
        print(f"  [{i+1}/{min(len(unique_pdfs), 25)}] {title[:60]}...")
        try:
            resp = rate_limited_get(url, delay=2)
            slug = slugify(title) if title else slugify(url.split('/')[-1].replace('.pdf', ''))
            filename = f"{slug}.pdf"
            save_pdf(base_dir, filename, resp.content)
            papers.append({
                "title": title,
                "author": "David Chalmers",
                "url": url,
                "filename": filename,
                "size_kb": len(resp.content) // 1024,
            })
            print(f"    Saved ({len(resp.content)//1024} KB)")
        except Exception as e:
            print(f"    Error: {e}")

    save_index(base_dir, papers)
    print(f"\nTotal Chalmers papers: {len(papers)}")

if __name__ == "__main__":
    main()
