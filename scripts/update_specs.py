#!/usr/bin/env python3
"""更新 slides_spec 文件，为指定页面添加裁剪后的截图引用"""
import re
from pathlib import Path

OUTPUT = Path("/Users/mik/strange LLM/output")

# 需要添加截图的页码
NEW_SCREENSHOTS = {
    7, 14, 15, 17, 19, 21, 23, 25, 27, 28,  # 第一幕
    31, 33, 35, 37,                            # 第二幕
    50, 52, 54, 57, 61, 64,                    # 第三幕
    72, 74, 75, 77, 79, 81,                    # 第四幕
    90, 116,                                    # 第五幕+
}

for part in [1, 2, 3]:
    spec_file = OUTPUT / f"slides_spec_v2_part{part}.md"
    text = spec_file.read_text()

    # Find all slide blocks and their page numbers
    # Pattern: ### 页 N: ...
    current_page = None
    lines = text.split('\n')
    new_lines = []
    changes = 0

    for line in lines:
        # Detect page number
        m = re.match(r'^### 页\s*(\d+)', line)
        if m:
            current_page = int(m.group(1))

        # Replace 配图 line for target pages
        if current_page in NEW_SCREENSHOTS and line.strip().startswith('- 配图:'):
            old_line = line
            # Only replace if it's currently text-only or design指示
            if '设计指示' in line or 'text-only' in line:
                new_line = f"- 配图: v6_page{current_page:03d}.jpg"
                new_lines.append(new_line)
                changes += 1
                print(f"part{part} page {current_page}: {old_line.strip()} -> {new_line}")
                continue

        new_lines.append(line)

    if changes > 0:
        spec_file.write_text('\n'.join(new_lines))
        print(f"Updated {spec_file.name}: {changes} changes\n")
    else:
        print(f"No changes needed in {spec_file.name}\n")
