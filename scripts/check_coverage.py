#!/usr/bin/env python3
"""Coverage checker: 检查目标文件中字幕ID的覆盖率。

支持两种引用格式：
  - 单点引用: V1-00:08-L007（精确匹配）
  - 范围引用: V2-04:53-L153~L178 或 V2-L153~L178（展开为L153到L178的所有ID）

用法: python3 scripts/check_coverage.py <target_file> [--format table|json|summary]
"""
import argparse
import json
import os
import re
import sys


def load_all_ids(indexed_dir):
    """从 indexed_subtitles 目录读取所有ID，同时建立 (video, line_num) → ID 的映射"""
    all_ids = []
    line_to_id = {}  # (video_prefix, line_num) → full_id
    for fname in sorted(os.listdir(indexed_dir)):
        if fname.endswith('_indexed.md'):
            fpath = os.path.join(indexed_dir, fname)
            with open(fpath, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('|') and not line.startswith('| ID') and not line.startswith('|--'):
                        parts = [p.strip() for p in line.split('|')]
                        if len(parts) >= 2 and parts[1]:
                            full_id = parts[1]
                            all_ids.append(full_id)
                            # 解析出 video prefix 和 line number
                            m = re.match(r'(V\d+)-\d+:\d+-L(\d+)', full_id)
                            if m:
                                video = m.group(1)
                                lnum = int(m.group(2))
                                line_to_id[(video, lnum)] = full_id
    return all_ids, line_to_id


def parse_range_refs(content):
    """从目标文件中解析所有范围引用，返回 {full_id} 集合"""
    covered_by_range = set()
    # 匹配范围引用: V{n}-{可选timestamp}-L{start}~L{end}
    # 格式1: V2-04:53-L153~L178
    # 格式2: V2-L153~L178
    # 格式3: V5-07:52-L255~L257
    pattern = r'(V\d+)-(?:\d+:\d+-)?L(\d+)~L(\d+)'
    for m in re.finditer(pattern, content):
        video = m.group(1)
        start = int(m.group(2))
        end = int(m.group(3))
        for lnum in range(start, end + 1):
            covered_by_range.add((video, lnum))
    return covered_by_range


def check_coverage(target_file, all_ids, line_to_id):
    """在目标文件中搜索每个ID（支持精确匹配+范围展开）"""
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 第一轮：精确匹配
    exact_found = set()
    for id_ in all_ids:
        if id_ in content:
            exact_found.add(id_)

    # 第二轮：范围引用展开
    range_refs = parse_range_refs(content)
    range_found = set()
    for (video, lnum), full_id in line_to_id.items():
        if (video, lnum) in range_refs and full_id not in exact_found:
            range_found.add(full_id)

    # 合并
    all_found = exact_found | range_found
    found = sorted(all_found, key=lambda x: all_ids.index(x) if x in all_ids else 9999)
    missing = [id_ for id_ in all_ids if id_ not in all_found]

    return found, missing, len(exact_found), len(range_found)


def format_table(found, missing, all_ids, exact_count, range_count):
    """表格格式输出"""
    total = len(all_ids)
    covered = len(found)
    pct = (covered / total * 100) if total > 0 else 0

    lines = []
    lines.append(f"Coverage: {covered}/{total} ({pct:.1f}%)")
    lines.append(f"  Exact matches: {exact_count}")
    lines.append(f"  Range expansions: {range_count}")
    lines.append("")

    if missing:
        lines.append(f"Missing IDs ({len(missing)}):")
        lines.append("| # | ID |")
        lines.append("|---|-----|")
        for i, id_ in enumerate(missing, 1):
            lines.append(f"| {i} | {id_} |")
    else:
        lines.append("All IDs covered!")

    return '\n'.join(lines)


def format_json(found, missing, all_ids, exact_count, range_count):
    """JSON格式输出"""
    total = len(all_ids)
    covered = len(found)
    return json.dumps({
        "total": total,
        "covered": covered,
        "exact_matches": exact_count,
        "range_expansions": range_count,
        "missing_count": len(missing),
        "coverage_pct": round(covered / total * 100, 1) if total > 0 else 0,
        "missing_ids": missing
    }, indent=2, ensure_ascii=False)


def format_summary(found, missing, all_ids, exact_count, range_count):
    """摘要格式输出"""
    total = len(all_ids)
    covered = len(found)
    pct = (covered / total * 100) if total > 0 else 0

    # Per-video breakdown
    video_stats = {}
    for id_ in all_ids:
        v = id_.split('-')[0]
        if v not in video_stats:
            video_stats[v] = {"total": 0, "covered": 0}
        video_stats[v]["total"] += 1
    for id_ in found:
        v = id_.split('-')[0]
        video_stats[v]["covered"] += 1

    lines = [f"=== Coverage Summary ===",
             f"Total: {covered}/{total} ({pct:.1f}%)",
             f"  Exact matches: {exact_count}",
             f"  Range expansions: {range_count}", ""]

    for v in sorted(video_stats.keys()):
        s = video_stats[v]
        vpct = (s["covered"] / s["total"] * 100) if s["total"] > 0 else 0
        lines.append(f"  {v}: {s['covered']}/{s['total']} ({vpct:.1f}%)")

    # Anchor count per video (unique IDs referenced, not total lines covered)
    lines.append("")
    lines.append("=== Anchor Count (unique references in target) ===")
    anchor_counts = {}
    for id_ in found:
        v = id_.split('-')[0]
        anchor_counts[v] = anchor_counts.get(v, 0) + 1
    for v in sorted(anchor_counts.keys()):
        status = "✓" if anchor_counts[v] >= 10 else "✗ (<10)"
        lines.append(f"  {v}: {anchor_counts[v]} anchors {status}")

    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='Check subtitle ID coverage in target file')
    parser.add_argument('target_file', help='Target file to check')
    parser.add_argument('--format', choices=['table', 'json', 'summary'], default='table',
                       help='Output format (default: table)')
    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    indexed_dir = os.path.join(project_root, 'archive', 'indexed_subtitles')

    if not os.path.isdir(indexed_dir):
        print(f"Error: indexed_subtitles directory not found at {indexed_dir}", file=sys.stderr)
        sys.exit(1)

    all_ids, line_to_id = load_all_ids(indexed_dir)
    if not all_ids:
        print("Error: No IDs found in indexed_subtitles", file=sys.stderr)
        sys.exit(1)

    found, missing, exact_count, range_count = check_coverage(args.target_file, all_ids, line_to_id)

    formatters = {'table': format_table, 'json': format_json, 'summary': format_summary}
    print(formatters[args.format](found, missing, all_ids, exact_count, range_count))

    sys.exit(0 if not missing else 1)


if __name__ == '__main__':
    main()
