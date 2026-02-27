#!/usr/bin/env python3
"""更新 slides_spec 文件 v2：正确的页码映射"""
import re
from pathlib import Path

OUTPUT = Path("/Users/mik/strange LLM/output")

# 需要添加截图的页码（与 crop_screenshots_v2.py 一致）
NEW_SCREENSHOTS = {
    "7", "12", "13", "15", "17", "20", "21", "23", "25", "26",
    "29", "31", "33", "35",
    "50", "52", "54", "57", "61", "64",
    "69", "72", "74", "75", "76", "78",
    "90", "116",
}

for part in [1, 2, 3]:
    spec_file = OUTPUT / f"slides_spec_v2_part{part}.md"
    text = spec_file.read_text()
    lines = text.split('\n')
    new_lines = []
    current_page = None
    changes = 0

    for line in lines:
        m = re.match(r'^### 页\s*(\S+)', line)
        if m:
            current_page = m.group(1).rstrip(':')

        # Replace 配图 line for target pages
        if current_page in NEW_SCREENSHOTS and line.strip().startswith('- 配图:'):
            img_val = line.split('配图:', 1)[1].strip()
            # Replace if text-only, design指示, diagram-placeholder, or old v6 reference
            if '设计指示' in img_val or 'text-only' in img_val or 'v6_page' in img_val or 'diagram-placeholder' in img_val.lower():
                new_line = f"- 配图: v6_page{current_page}.jpg"
                new_lines.append(new_line)
                changes += 1
                print(f"part{part} page {current_page}: -> {new_line}")
                continue

        new_lines.append(line)

    if changes > 0:
        spec_file.write_text('\n'.join(new_lines))
        print(f"Updated {spec_file.name}: {changes} changes\n")
    else:
        print(f"No changes in {spec_file.name}\n")
