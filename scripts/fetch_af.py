#!/usr/bin/env python3
"""Fetch articles from Alignment Forum via LessWrong GraphQL API with af:true filter."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from utils.helpers import rate_limited_post, save_article, save_index, slugify, html_to_markdown

# Use LW endpoint with af:true — AF's own endpoint aggressively rate-limits
LW_API_URL = "https://www.lesswrong.com/graphql"

KEYWORDS = [
    "consciousness",
    "philosophy of mind",
    "Chinese Room",
    "understanding",
    "sentience",
    "qualia",
    "Dennett",
    "Chalmers",
    "grounding problem",
    "machine consciousness",
    "world model",
    "AI philosophy",
    "moral status",
    "intentionality",
    "phenomenal",
    "embodied cognition",
    # Round 2 — expanded keywords
    "hard problem",
    "phenomenology",
    "functionalism",
    "free will",
    "agency",
    "symbol grounding",
    "inner experience",
    "subjective experience",
    "artificial general intelligence",
    "thinking machines",
    "turing test",
    "philosophy of AI",
    "mind-body",
    "dualism",
    "eliminativism",
    "folk psychology",
    "mental representation",
    "cognitive science",
    "language understanding",
    "meaning",
    "semantics",
    "stochastic parrot",
    "emergent",
]

POSTS_QUERY = """
query PostsBySearch($terms: JSON) {
  posts(input: {terms: $terms}) {
    results {
      _id
      title
      slug
      postedAt
      baseScore
      voteCount
      url
      af
      contents {
        markdown
        html
      }
      user {
        displayName
      }
    }
  }
}
"""


def search_af_posts(keyword, limit=100, offset=0):
    """Search AF posts via LW API with af:true filter."""
    variables = {
        "terms": {
            "query": keyword,
            "limit": limit,
            "offset": offset,
            "af": True,
        }
    }
    try:
        resp = rate_limited_post(LW_API_URL, {
            "query": POSTS_QUERY,
            "variables": variables,
        }, delay=2)
        data = resp.json()
        return data.get("data", {}).get("posts", {}).get("results", [])
    except Exception as e:
        print(f"    Error searching '{keyword}': {e}")
        return []


def main():
    base_dir = os.path.join(os.path.dirname(__file__), "..", "research", "alignment_forum_dedicated")
    print("=== Fetching Alignment Forum (via LW API, af:true) ===")

    all_posts = []
    for kw in KEYWORDS:
        print(f"  Keyword: {kw}")
        posts = search_af_posts(kw, limit=100)
        print(f"    Found {len(posts)} posts")
        all_posts.extend(posts)

    # Deduplicate
    seen = {}
    for post in all_posts:
        pid = post.get("_id")
        if not pid or pid in seen:
            continue
        contents = post.get("contents") or {}
        md = contents.get("markdown") or ""
        if not md and contents.get("html"):
            md = html_to_markdown(contents["html"])
        if len(md) < 200:
            continue
        seen[pid] = (post, md)

    print(f"\n  Total raw: {len(all_posts)}, unique with content: {len(seen)}")

    articles = []
    for pid, (post, md) in seen.items():
        title = post.get("title", "Untitled")
        author = (post.get("user") or {}).get("displayName", "Unknown")
        meta = {
            "title": title,
            "author": author,
            "date": str(post.get("postedAt", ""))[:10],
            "source": "alignment_forum",
            "url": post.get("url") or f"https://www.alignmentforum.org/posts/{pid}/{post.get('slug', '')}",
            "score": post.get("baseScore", 0),
            "votes": post.get("voteCount", 0),
        }
        slug = slugify(title)
        filename = f"{slug}.md"
        save_article(base_dir, filename, meta, md)
        articles.append({**meta, "filename": filename, "length": len(md)})

    save_index(base_dir, articles)
    print(f"\nTotal AF articles: {len(articles)}")


if __name__ == "__main__":
    main()
