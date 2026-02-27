"""Shared utilities for research fetchers."""
import json
import os
import time
import re
import requests
import html2text

_last_request_time = 0

def rate_limited_get(url, delay=2, headers=None, timeout=30):
    """HTTP GET with rate limiting."""
    global _last_request_time
    elapsed = time.time() - _last_request_time
    if elapsed < delay:
        time.sleep(delay - elapsed)
    resp = requests.get(url, headers=headers or {
        'User-Agent': 'Mozilla/5.0 (research-bot; academic use)'
    }, timeout=timeout)
    _last_request_time = time.time()
    resp.raise_for_status()
    return resp

def rate_limited_post(url, json_data, delay=2, headers=None, timeout=30):
    """HTTP POST with rate limiting."""
    global _last_request_time
    elapsed = time.time() - _last_request_time
    if elapsed < delay:
        time.sleep(delay - elapsed)
    resp = requests.post(url, json=json_data, headers=headers or {
        'User-Agent': 'Mozilla/5.0 (research-bot; academic use)',
        'Content-Type': 'application/json',
    }, timeout=timeout)
    _last_request_time = time.time()
    resp.raise_for_status()
    return resp

def html_to_markdown(html_content):
    """Convert HTML to clean Markdown."""
    h = html2text.HTML2Text()
    h.body_width = 0  # no wrapping
    h.ignore_links = False
    h.ignore_images = True
    h.ignore_emphasis = False
    return h.handle(html_content)

def slugify(text):
    """Create a filesystem-safe slug from text."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text[:80]

def save_article(directory, filename, metadata, content):
    """Save article as Markdown with YAML front matter."""
    os.makedirs(directory, exist_ok=True)
    front_matter_lines = ['---']
    for key, value in metadata.items():
        if isinstance(value, list):
            front_matter_lines.append(f'{key}: {json.dumps(value)}')
        elif isinstance(value, (int, float)):
            front_matter_lines.append(f'{key}: {value}')
        else:
            # Escape quotes in strings
            val = str(value).replace('"', '\\"')
            front_matter_lines.append(f'{key}: "{val}"')
    front_matter_lines.append('---')
    front_matter = '\n'.join(front_matter_lines)

    filepath = os.path.join(directory, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(front_matter + '\n\n' + content)
    return filepath

def save_index(directory, articles):
    """Save index JSON."""
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, 'index.json')
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(articles, f, indent=2, ensure_ascii=False, default=str)
    return filepath

def save_pdf(directory, filename, content_bytes):
    """Save binary PDF file."""
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)
    with open(filepath, 'wb') as f:
        f.write(content_bytes)
    return filepath
