#!/usr/bin/env python3
"""Three locks / impossible triangle of AI constraints."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

CHINESE_FONTS = ['PingFang HK', 'STHeiti', 'Heiti TC', 'Heiti SC', 'PingFang SC', 'SimHei', 'sans-serif']
def get_chinese_font():
    available = {f.name for f in fm.fontManager.ttflist}
    for name in CHINESE_FONTS:
        if name in available:
            return name
    return 'sans-serif'
FONT = get_chinese_font()
plt.rcParams['font.family'] = FONT
plt.rcParams['axes.unicode_minus'] = False

BG = '#0F1729'
CYAN = '#00D4AA'
ORANGE = '#FF6B35'
PURPLE = '#7C6BF0'
WHITE = '#FFFFFF'
DARK = '#1A2340'
fp = {'fontfamily': FONT}

fig, ax = plt.subplots(figsize=(19.2, 10.8), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(-1, 11)
ax.set_ylim(-0.5, 11)
ax.axis('off')

ax.text(5, 10.5, 'AI的三把锁：不可逾越的理论天花板', fontsize=36, color=WHITE,
        ha='center', va='top', fontweight='bold', **fp)

# Triangle vertices
top = (5, 8.5)
bl = (1.5, 2)
br = (8.5, 2)

# Draw triangle edges with glow
for (x1, y1), (x2, y2), c in [(top, bl, CYAN), (bl, br, ORANGE), (br, top, PURPLE)]:
    ax.plot([x1, x2], [y1, y2], color=c, linewidth=4, alpha=0.8, solid_capstyle='round')
    ax.plot([x1, x2], [y1, y2], color=c, linewidth=12, alpha=0.1, solid_capstyle='round')

# Lock icons and labels at vertices
locks = [
    (top[0], top[1]+0.3, '计算不可判定', 'Computational\nUndecidability', CYAN,
     '图灵停机问题\n无法判断程序是否会终止'),
    (bl[0]-0.3, bl[1]-0.3, '统计样本不足', 'Statistical\nInsufficiency', ORANGE,
     '长尾分布\n罕见情况永远学不完'),
    (br[0]+0.3, br[1]-0.3, '有限信息容量', 'Finite Information\nCapacity', PURPLE,
     '数据压缩极限\n信息必然丢失'),
]

for x, y, cn, en, color, desc in locks:
    # Lock circle
    circle = plt.Circle((x, y), 0.6, facecolor=DARK, edgecolor=color, linewidth=3, alpha=0.9)
    ax.add_patch(circle)
    ax.text(x, y, '🔒', fontsize=28, ha='center', va='center')

    # Label offset based on position
    if y > 5:  # top
        ax.text(x, y + 1.0, cn, fontsize=24, color=color, ha='center', fontweight='bold', **fp)
        ax.text(x, y + 0.6, en, fontsize=13, color=WHITE, ha='center', alpha=0.5)
    elif x < 5:  # bottom-left
        ax.text(x - 1.5, y - 0.2, cn, fontsize=24, color=color, ha='center', fontweight='bold', **fp)
        ax.text(x - 1.5, y - 0.7, en, fontsize=13, color=WHITE, ha='center', alpha=0.5)
        ax.text(x - 1.5, y - 1.5, desc, fontsize=14, color=WHITE, ha='center', alpha=0.6, **fp)
    else:  # bottom-right
        ax.text(x + 1.5, y - 0.2, cn, fontsize=24, color=color, ha='center', fontweight='bold', **fp)
        ax.text(x + 1.5, y - 0.7, en, fontsize=13, color=WHITE, ha='center', alpha=0.5)
        ax.text(x + 1.5, y - 1.5, desc, fontsize=14, color=WHITE, ha='center', alpha=0.6, **fp)

# Top description
ax.text(5, 8.0, '图灵停机问题\n无法判断程序是否会终止', fontsize=14, color=WHITE,
        ha='center', va='top', alpha=0.6, **fp)

# Center text
ax.text(5, 4.5, '不可能\n三角', fontsize=32, color=WHITE, ha='center', va='center',
        fontweight='bold', alpha=0.9, **fp)
ax.text(5, 3.5, '无论算力多强\n这三个限制永远存在', fontsize=16, color=WHITE,
        ha='center', va='top', alpha=0.5, **fp)

plt.tight_layout(pad=1)
plt.savefig('/Users/mik/strange LLM/assets/diagrams/rendered/three_locks.png',
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close()
print("Done: three_locks.png")
