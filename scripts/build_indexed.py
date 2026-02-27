#!/usr/bin/env python3
"""Build indexed subtitles and raw appendix from docs/ subtitle files.

Reads 6 subtitle files from docs/, assigns stable IDs, outputs:
  - archive/indexed_subtitles/V{n}_indexed.md  (Markdown tables)
  - archive/raw_appendix.md                    (concatenated appendix with IDs)
"""
import os
import re
import sys

# Project root = parent of scripts/
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
DOCS_DIR = os.path.join(PROJECT_ROOT, 'docs')
INDEXED_DIR = os.path.join(PROJECT_ROOT, 'archive', 'indexed_subtitles')
APPENDIX_PATH = os.path.join(PROJECT_ROOT, 'archive', 'raw_appendix.md')

# Keyword mapping: V-number -> (list of keywords ANY match, short name)
VIDEO_MAP = {
    1: {'keywords': ['名词诈骗'], 'short': '名词诈骗'},
    2: {'keywords': ['Clawdbot'], 'short': 'Clawdbot揭秘'},
    3: {'keywords': ['割裂感'], 'short': '割裂感'},
    4: {'keywords': ['AI视频', 'Seedance'], 'short': 'AI视频诅咒'},
    5: {'keywords': ['3000'], 'short': '3000+模型'},
    6: {'keywords': ['开源大模型'], 'short': '开源了什么'},
}


def find_subtitle_files():
    """Scan docs/ for subtitle files and match them to V1-V6."""
    all_files = os.listdir(DOCS_DIR)
    subtitle_files = [f for f in all_files if '字幕' in f and f.endswith('.md')]

    mapping = {}  # vnum -> filename
    for vnum, info in VIDEO_MAP.items():
        for fname in subtitle_files:
            if any(kw in fname for kw in info['keywords']):
                mapping[vnum] = fname
                break

    # Verify all 6 found
    for vnum in range(1, 7):
        if vnum not in mapping:
            print(f"ERROR: Could not find subtitle file for V{vnum} "
                  f"(keywords: {VIDEO_MAP[vnum]['keywords']})", file=sys.stderr)
            sys.exit(1)

    return mapping


def parse_subtitle_lines(filepath):
    """Parse a subtitle file into list of (timestamp, text) tuples.

    Skips blank lines. Each non-blank line is expected to be 'MM:SS text'.
    """
    entries = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            stripped = line.strip()
            if not stripped:
                continue
            # Match MM:SS at start
            m = re.match(r'^(\d{2}:\d{2})\s+(.*)', stripped)
            if m:
                entries.append((m.group(1), m.group(2)))
            else:
                # Line doesn't match expected format; include as-is with empty timestamp
                entries.append(('', stripped))
    return entries


def build_indexed_md(vnum, entries):
    """Build a Markdown table string for indexed subtitle entries."""
    lines = []
    lines.append('| ID | Timestamp | Text |')
    lines.append('|-----|-----------|------|')
    for i, (ts, text) in enumerate(entries, 1):
        line_no = f'{i:03d}'
        ts_display = ts if ts else '??:??'
        sid = f'V{vnum}-{ts_display}-L{line_no}'
        lines.append(f'| {sid} | {ts_display} | {text} |')
    return '\n'.join(lines) + '\n'


def build_appendix_section(vnum, short_name, orig_filename, raw_content, entries):
    """Build one section of the appendix for a single video.

    Each line of the original content gets an ID tag prepended.
    """
    lines = []
    lines.append(f'# V{vnum} - {short_name}')
    lines.append('')
    lines.append(f'**源文件**: {orig_filename}')
    lines.append('')
    lines.append('---')
    lines.append('')

    # Walk through the raw content line by line.
    # For non-blank lines, assign IDs matching the indexed entries.
    # For blank lines, preserve them as-is.
    entry_idx = 0
    for raw_line in raw_content.splitlines():
        stripped = raw_line.strip()
        if not stripped:
            # Blank line - preserve
            lines.append('')
        else:
            # Non-blank line - assign the next ID
            if entry_idx < len(entries):
                ts, text = entries[entry_idx]
                entry_idx += 1
                line_no = f'{entry_idx:03d}'
                ts_display = ts if ts else '??:??'
                sid = f'V{vnum}-{ts_display}-L{line_no}'
                lines.append(f'[{sid}] {stripped}')
            else:
                lines.append(stripped)

    lines.append('')
    lines.append('---')
    lines.append('')
    return '\n'.join(lines)


def main():
    # Ensure output directory exists
    os.makedirs(INDEXED_DIR, exist_ok=True)

    # Find subtitle files
    mapping = find_subtitle_files()
    print("Found subtitle file mapping:")
    for vnum in sorted(mapping.keys()):
        print(f"  V{vnum}: {mapping[vnum]}")
    print()

    appendix_sections = []

    for vnum in range(1, 7):
        fname = mapping[vnum]
        fpath = os.path.join(DOCS_DIR, fname)

        # Parse entries (non-blank lines)
        entries = parse_subtitle_lines(fpath)
        print(f"V{vnum}: {len(entries)} lines parsed from {fname}")

        # Build and write indexed markdown table
        indexed_md = build_indexed_md(vnum, entries)
        out_path = os.path.join(INDEXED_DIR, f'V{vnum}_indexed.md')
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(indexed_md)
        print(f"  -> Wrote {out_path}")

        # Read raw content for appendix
        with open(fpath, 'r', encoding='utf-8') as f:
            raw_content = f.read()

        # Build appendix section
        short_name = VIDEO_MAP[vnum]['short']
        section = build_appendix_section(vnum, short_name, fname, raw_content, entries)
        appendix_sections.append(section)

    # Write raw_appendix.md
    with open(APPENDIX_PATH, 'w', encoding='utf-8') as f:
        f.write('\n'.join(appendix_sections))
    print(f"\n-> Wrote {APPENDIX_PATH}")
    print("Done!")


if __name__ == '__main__':
    main()
