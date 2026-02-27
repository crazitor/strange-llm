#!/usr/bin/env python3
"""Sync slides_spec_v4_full.md with updated notes/desc/body from build_pptx_v5.js."""

import re
import sys

JS_PATH = "scripts/build_pptx_v5.js"
SPEC_PATH = "output/slides_spec_v4_full.md"
PAGES = [24, 36, 46, 47, 49, 53, 55, 76, 92, 95]

def extract_js_slides(js_text):
    """Extract notes, desc, body for target pages from JS."""
    slides = {}
    for pg in PAGES:
        # Find the comment marker for this page
        pattern = rf'// 页 {pg}:'
        idx = js_text.find(pattern)
        if idx == -1:
            print(f"WARNING: page {pg} not found in JS")
            continue

        # Find the opening { and the next page comment or end of array
        block_start = js_text.index('{', idx)
        # Find closing: next "// 页" or end of slides array
        next_page = re.search(r'\n\s*// 页 \d+:', js_text[block_start + 1:])
        if next_page:
            block_end = block_start + 1 + next_page.start()
        else:
            block_end = js_text.find('\n];\n', block_start)
            if block_end == -1:
                block_end = len(js_text)

        block = js_text[block_start:block_end]

        info = {}
        # Extract notes
        m = re.search(r'notes:\s*"((?:[^"\\]|\\.)*)"', block)
        if m:
            # Unescape JS string
            raw = m.group(1)
            raw = raw.replace('\\"', '"').replace('\\n', '\n').replace('\\\\', '\\')
            info['notes'] = raw

        # Extract desc
        m = re.search(r'desc:\s*"((?:[^"\\]|\\.)*)"', block)
        if m:
            raw = m.group(1)
            raw = raw.replace('\\"', '"').replace('\\n', '\n').replace('\\\\', '\\')
            info['desc'] = raw

        # Extract body (string value)
        m = re.search(r'body:\s*"((?:[^"\\]|\\.)*)"', block)
        if m:
            raw = m.group(1)
            raw = raw.replace('\\"', '"').replace('\\n', '\n').replace('\\\\', '\\')
            info['body'] = raw

        slides[pg] = info
    return slides


def update_spec(spec_text, slides):
    """Update spec markdown with new notes/desc/body from JS."""
    updated = 0

    for pg, info in sorted(slides.items()):
        if 'notes' in info:
            # Replace 演讲词 section
            # Pattern: after "### 页 {pg}:" header, find **演讲词**: or **演讲词**:\n> ...
            # The 演讲词 block starts with **演讲词**: and ends before the next ** field or ---
            header_pattern = rf'(### 页 {pg}:.*?\n)'
            header_match = re.search(header_pattern, spec_text)
            if not header_match:
                print(f"WARNING: page {pg} header not found in spec")
                continue

            # Find the 演讲词 section within this page
            page_start = header_match.start()
            # Find next page header or end
            next_header = re.search(r'\n### 页 \d+:', spec_text[page_start + 1:])
            page_end = page_start + 1 + next_header.start() if next_header else len(spec_text)
            page_block = spec_text[page_start:page_end]

            # Replace 演讲词 content
            # Matches from **演讲词**: to the next **field** or ---
            speech_pattern = r'(\*\*演讲词\*\*:\s*\n)>.*?(?=\n\*\*|\n---|\Z)'
            new_notes = info['notes'].strip()
            # Format as > blockquote (single block, no per-line >)
            new_speech = r'\1> ' + new_notes

            new_page_block = re.sub(speech_pattern, new_speech, page_block, flags=re.DOTALL)

            if new_page_block != page_block:
                spec_text = spec_text[:page_start] + new_page_block + spec_text[page_end:]
                print(f"  Page {pg}: updated 演讲词")
                updated += 1
            else:
                # Try alternate format: **演讲词**: > text (inline)
                speech_pattern2 = r'(\*\*演讲词\*\*:\s*)>.*?(?=\n\*\*|\n---|\Z)'
                new_speech2 = r'\1\n> ' + new_notes
                new_page_block2 = re.sub(speech_pattern2, new_speech2, page_block, flags=re.DOTALL)
                if new_page_block2 != page_block:
                    spec_text = spec_text[:page_start] + new_page_block2 + spec_text[page_end:]
                    print(f"  Page {pg}: updated 演讲词 (inline format)")
                    updated += 1
                else:
                    print(f"  Page {pg}: 演讲词 unchanged or pattern not matched")

        # Update desc if present
        if 'desc' in info:
            header_match = re.search(rf'### 页 {pg}:', spec_text)
            if header_match:
                page_start = header_match.start()
                next_header = re.search(r'\n### 页 \d+:', spec_text[page_start + 1:])
                page_end = page_start + 1 + next_header.start() if next_header else len(spec_text)
                page_block = spec_text[page_start:page_end]
                # desc maps to 副标题/要点 area - skip for now, complex mapping

        # Update body if present
        if 'body' in info:
            header_match = re.search(rf'### 页 {pg}:', spec_text)
            if header_match:
                page_start = header_match.start()
                next_header = re.search(r'\n### 页 \d+:', spec_text[page_start + 1:])
                page_end = page_start + 1 + next_header.start() if next_header else len(spec_text)
                page_block = spec_text[page_start:page_end]

                # body maps to 副标题/要点 bullet list
                # Find the body content in spec between 副标题/要点: and next field
                body_pattern = r'(- 副标题/要点:\s*\n)(\s+-\s+.*?)(?=\n- 配图:|\n- 图表:|\n\*\*)'
                body_match = re.search(body_pattern, page_block, re.DOTALL)
                if body_match:
                    new_body_lines = info['body'].strip().split('\n')
                    new_body_text = '\n'.join(f'  - {line}' for line in new_body_lines)
                    new_page_block = page_block[:body_match.start(2)] + new_body_text + '\n' + page_block[body_match.end(2):]
                    if new_page_block != page_block:
                        spec_text = spec_text[:page_start] + new_page_block + spec_text[page_end:]
                        print(f"  Page {pg}: updated body/副标题")

    return spec_text, updated


def main():
    with open(JS_PATH, 'r', encoding='utf-8') as f:
        js_text = f.read()
    with open(SPEC_PATH, 'r', encoding='utf-8') as f:
        spec_text = f.read()

    print("Extracting slide data from JS...")
    slides = extract_js_slides(js_text)
    print(f"Found data for {len(slides)} pages: {sorted(slides.keys())}")

    for pg, info in sorted(slides.items()):
        fields = list(info.keys())
        print(f"  Page {pg}: {', '.join(fields)}")

    print("\nUpdating spec...")
    new_spec, updated = update_spec(spec_text, slides)

    # Write output
    with open(SPEC_PATH, 'w', encoding='utf-8') as f:
        f.write(new_spec)

    print(f"\nDone. Updated 演讲词 in {updated} pages.")
    print(f"Written to {SPEC_PATH}")


if __name__ == '__main__':
    main()
