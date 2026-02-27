#!/usr/bin/env python3
"""Fetch full-text articles from LessWrong and Alignment Forum via GraphQL API."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from utils.helpers import rate_limited_post, save_article, save_index, slugify

API_URL = "https://www.lesswrong.com/graphql"

TAGS = [
    "ai-consciousness", "philosophy-of-mind", "chinese-room",
    "alignment-philosophy", "intelligence", "understanding",
]
KEYWORDS = [
    "consciousness", "Chinese Room", "Dreyfus", "understanding AI",
    "stochastic parrot", "embodied cognition", "philosophy of AI",
    "hard problem", "qualia", "phenomenal consciousness",
    "LLM understanding", "AI sentience", "machine consciousness",
    "intentionality", "Searle", "Dennett", "Chalmers",
    "AI alignment philosophy", "moral status AI", "artificial mind",
    "grounding problem", "symbol grounding",
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
      contents {
        markdown
        html
      }
      user {
        displayName
      }
      af
    }
  }
}
"""

TAG_POSTS_QUERY = """
query PostsByTag($tagId: String, $limit: Int) {
  tag(input: {selector: {slug: $tagId}}) {
    result {
      _id
      name
    }
  }
  posts(input: {terms: {view: "tagRelevance", tagId: $tagId, limit: $limit, sortedBy: "top"}}) {
    results {
      _id
      title
      slug
      postedAt
      baseScore
      voteCount
      url
      contents {
        markdown
        html
      }
      user {
        displayName
      }
      af
    }
  }
}
"""

def search_posts(keyword, limit=50, offset=0):
    """Search posts by keyword with pagination."""
    variables = {
        "terms": {
            "query": keyword,
            "limit": limit,
            "offset": offset,
        }
    }
    try:
        resp = rate_limited_post(API_URL, {
            "query": POSTS_QUERY,
            "variables": variables,
        }, delay=1)
        data = resp.json()
        posts = data.get("data", {}).get("posts", {}).get("results", [])
        return posts
    except Exception as e:
        print(f"  Error searching '{keyword}': {e}")
        return []

def fetch_by_tag(tag_slug, limit=50):
    """Fetch posts by tag slug using search as fallback."""
    # Use tag-filtered search via the API
    query = """
    query TagPosts($slug: String!) {
      tag(input: {selector: {slug: $slug}}) {
        result {
          _id
          name
        }
      }
    }
    """
    tag_id = None
    try:
        resp = rate_limited_post(API_URL, {
            "query": query,
            "variables": {"slug": tag_slug},
        }, delay=1)
        data = resp.json()
        if data.get("errors"):
            print(f"    GraphQL errors: {data['errors'][0].get('message', '')}")
        tag = (data.get("data") or {}).get("tag", {}).get("result")
        if tag:
            tag_id = tag["_id"]
    except Exception as e:
        print(f"    Tag lookup error: {e}")

    if not tag_id:
        # Fallback: search by the tag name as keyword
        print(f"    Falling back to keyword search for '{tag_slug}'")
        return search_posts(tag_slug.replace("-", " "), limit)

    # Fetch posts with tagId
    variables = {
        "terms": {
            "filterSettings": {"tags": [{"tagId": tag_id, "filterMode": "Required"}]},
            "limit": limit,
            "sortedBy": "top",
        }
    }
    try:
        resp = rate_limited_post(API_URL, {
            "query": POSTS_QUERY,
            "variables": variables,
        }, delay=1)
        data = resp.json()
        if data.get("errors"):
            print(f"    Post query errors, falling back to keyword search")
            return search_posts(tag_slug.replace("-", " "), limit)
        return (data.get("data") or {}).get("posts", {}).get("results", [])
    except Exception as e:
        print(f"    Error: {e}, falling back to keyword search")
        return search_posts(tag_slug.replace("-", " "), limit)

def process_posts(posts, base_dir):
    """Deduplicate and save posts, splitting LW and AF."""
    seen = {}
    for post in posts:
        pid = post.get("_id")
        if not pid or pid in seen:
            continue
        contents = post.get("contents") or {}
        md = contents.get("markdown") or ""
        if not md and contents.get("html"):
            from utils.helpers import html_to_markdown
            md = html_to_markdown(contents["html"])
        if len(md) < 200:
            continue
        seen[pid] = post

    lw_articles = []
    af_articles = []

    for pid, post in seen.items():
        contents = post.get("contents") or {}
        md = contents.get("markdown") or ""
        if not md and contents.get("html"):
            from utils.helpers import html_to_markdown
            md = html_to_markdown(contents["html"])

        title = post.get("title", "Untitled")
        author = (post.get("user") or {}).get("displayName", "Unknown")
        meta = {
            "title": title,
            "author": author,
            "date": str(post.get("postedAt", ""))[:10],
            "source": "alignment_forum" if post.get("af") else "lesswrong",
            "url": f"https://www.lesswrong.com/posts/{pid}/{post.get('slug', '')}",
            "score": post.get("baseScore", 0),
            "votes": post.get("voteCount", 0),
        }

        slug = slugify(title)
        filename = f"{slug}.md"
        target_dir = os.path.join(base_dir, "alignment_forum" if post.get("af") else "lesswrong")

        save_article(target_dir, filename, meta, md)
        entry = {**meta, "filename": filename, "length": len(md)}

        if post.get("af"):
            af_articles.append(entry)
        else:
            lw_articles.append(entry)

    return lw_articles, af_articles

def main():
    base_dir = os.path.join(os.path.dirname(__file__), "..", "research")
    all_posts = []

    print("=== Fetching LessWrong + Alignment Forum ===")

    for tag in TAGS:
        print(f"  Tag: {tag}")
        posts = fetch_by_tag(tag, limit=50)
        print(f"    Found {len(posts)} posts")
        all_posts.extend(posts)

    for kw in KEYWORDS:
        print(f"  Keyword: {kw}")
        posts_p1 = search_posts(kw, limit=50, offset=0)
        posts_p2 = search_posts(kw, limit=50, offset=50)
        posts = posts_p1 + posts_p2
        print(f"    Found {len(posts)} posts")
        all_posts.extend(posts)

    print(f"\nTotal raw posts: {len(all_posts)}")
    lw, af = process_posts(all_posts, base_dir)
    print(f"Saved: {len(lw)} LessWrong + {len(af)} Alignment Forum articles")

    if lw:
        save_index(os.path.join(base_dir, "lesswrong"), lw)
    if af:
        save_index(os.path.join(base_dir, "alignment_forum"), af)

if __name__ == "__main__":
    main()
