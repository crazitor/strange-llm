#!/usr/bin/env python3
"""Fetch papers from multiple AI philosophers via Semantic Scholar API."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from utils.helpers import rate_limited_get, save_article, save_pdf, save_index, slugify

S2_AUTHOR_SEARCH = "https://api.semanticscholar.org/graph/v1/author/search?query={name}&limit=5&fields=name,paperCount,hIndex"
S2_PAPERS_URL = "https://api.semanticscholar.org/graph/v1/author/{aid}/papers?fields=title,url,abstract,year,openAccessPdf,citationCount,externalIds&limit=500&offset={offset}"

# (display_name, search_name, AI-relevance keywords, optional_s2_id)
PHILOSOPHERS = [
    ("David Chalmers", "David Chalmers", [
        "consciousness", "mind", "zombie", "qualia", "ai", "artificial",
        "virtual", "simulation", "singularity", "intelligence", "extended mind",
        "hard problem", "phenomenal", "cognition", "digital", "robot",
    ]),
    ("Susan Schneider", "Susan Schneider", [
        "consciousness", "ai", "artificial", "mind", "intelligence",
        "machine", "robot", "neural", "brain", "cognitive", "self",
        "language of thought", "zombie",
    ], "32264337"),  # Hardcoded S2 ID — auto-search returns wrong person
    ("Eric Schwitzgebel", "Eric Schwitzgebel", [
        "consciousness", "ai", "artificial", "machine", "robot",
        "moral", "ethics", "mind", "belief", "introspection", "phenomenal",
    ]),
    ("Ned Block", "Ned Block", [
        "consciousness", "mind", "functionalism", "qualia", "access",
        "phenomenal", "cognition", "intelligence", "machine", "attention",
    ]),
    ("Murray Shanahan", "Murray Shanahan", [
        "consciousness", "ai", "artificial", "embodiment", "robot",
        "cognition", "intelligence", "language", "reasoning", "imagination",
    ]),
    ("Yoshua Bengio", "Yoshua Bengio", [
        "consciousness", "ai safety", "alignment", "philosophy", "understanding",
        "reasoning", "grounding", "causal", "ethics", "existential risk",
        "governance", "sentience",
    ]),
    ("Emily Bender", "Emily M Bender", [
        "stochastic parrot", "language", "meaning", "understanding",
        "ai", "ethics", "harms", "bias", "nlp", "grounding",
    ]),
]


def find_author_id(name):
    """Find best Semantic Scholar author ID for a given name."""
    try:
        resp = rate_limited_get(S2_AUTHOR_SEARCH.format(name=name.replace(" ", "+")), delay=1)
        data = resp.json()
        candidates = data.get("data", [])
        if not candidates:
            return None
        # Pick candidate with highest h-index (most likely the right person)
        best = max(candidates, key=lambda c: (c.get("hIndex") or 0))
        print(f"    Found: {best['name']} (papers={best.get('paperCount')}, h={best.get('hIndex')}, id={best['authorId']})")
        return best["authorId"]
    except Exception as e:
        print(f"    Error finding author '{name}': {e}")
        return None


def fetch_s2_papers(author_id):
    """Fetch all papers for an author with pagination."""
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
            if len(papers) < 500:
                break
        except Exception as e:
            print(f"    Pagination error at offset {offset}: {e}")
            break
    return all_papers


def is_relevant(title, keywords):
    """Check if paper title matches any keywords."""
    t = title.lower()
    return any(kw in t for kw in keywords)


def fetch_philosopher(display_name, search_name, keywords, base_dir, s2_id=None):
    """Fetch and save all relevant papers for one philosopher."""
    author_slug = slugify(display_name)
    out_dir = os.path.join(base_dir, author_slug)

    print(f"\n  === {display_name} ===")

    if s2_id:
        author_id = s2_id
        print(f"    Using hardcoded S2 ID: {author_id}")
    else:
        author_id = find_author_id(search_name)
    if not author_id:
        print(f"    Could not find author ID. Skipping.")
        return []

    all_papers = fetch_s2_papers(author_id)
    print(f"    Total papers: {len(all_papers)}")

    relevant = [p for p in all_papers if p.get("title") and is_relevant(p["title"], keywords)]
    relevant.sort(key=lambda p: p.get("citationCount", 0), reverse=True)
    print(f"    Relevant papers: {len(relevant)}")

    papers_meta = []
    pdf_count = 0

    for i, p in enumerate(relevant):
        title = p["title"]
        slug = slugify(title)
        print(f"    [{i+1}/{len(relevant)}] {title[:55]}...")

        # Try PDF — first S2 openAccess, then Unpaywall fallback
        pdf_url = (p.get("openAccessPdf") or {}).get("url")
        if not pdf_url:
            # Try Unpaywall API (free, uses DOI)
            doi = (p.get("externalIds") or {}).get("DOI")
            if doi:
                try:
                    uw_resp = rate_limited_get(
                        f"https://api.unpaywall.org/v2/{doi}?email=research@example.com",
                        delay=1, timeout=15)
                    uw_data = uw_resp.json()
                    best_oa = uw_data.get("best_oa_location") or {}
                    pdf_url = best_oa.get("url_for_pdf") or best_oa.get("url")
                except Exception:
                    pass

        if pdf_url:
            try:
                resp = rate_limited_get(pdf_url, delay=1.5, timeout=60)
                ct = resp.headers.get("content-type", "")
                if "pdf" in ct and len(resp.content) > 5000:
                    save_pdf(out_dir, f"{slug}.pdf", resp.content)
                    papers_meta.append({
                        "title": title,
                        "author": display_name,
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

        # Save abstract (skip papers with no abstract)
        abstract = p.get("abstract", "")
        if not abstract:
            continue  # Don't save empty shells
        content = f"## Abstract\n\n{abstract}\n"
        meta = {
            "title": title,
            "author": display_name,
            "date": str(p.get("year", "")),
            "source": "semantic_scholar",
            "url": p.get("url", ""),
            "citations": p.get("citationCount", 0),
        }
        save_article(out_dir, f"{slug}.md", meta, content)
        papers_meta.append({**meta, "filename": f"{slug}.md", "length": len(content)})

    save_index(out_dir, papers_meta)
    print(f"    Saved: {len(papers_meta)} papers ({pdf_count} PDFs)")
    return papers_meta


def main():
    base_dir = os.path.join(os.path.dirname(__file__), "..", "research", "philosophers")
    print("=== Fetching Multi-Philosopher Papers ===")

    total = 0
    total_pdfs = 0
    for entry in PHILOSOPHERS:
        display_name, search_name, keywords = entry[0], entry[1], entry[2]
        s2_id = entry[3] if len(entry) > 3 else None
        papers = fetch_philosopher(display_name, search_name, keywords, base_dir, s2_id=s2_id)
        total += len(papers)
        total_pdfs += sum(1 for p in papers if p.get("filename", "").endswith(".pdf"))

    print(f"\nTotal philosopher papers: {total} ({total_pdfs} PDFs)")


if __name__ == "__main__":
    main()
