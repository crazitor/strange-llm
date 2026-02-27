"""
Diagram 4: Solution Space — Concentric Constraints (Page 75)
Each concentric ring adds a constraint, exponentially shrinking the
solution space and making the task harder for AI.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.font_manager as fm
from matplotlib.patches import FancyArrowPatch
import numpy as np
from pathlib import Path

# ---------------------------------------------------------------------------
# Font
# ---------------------------------------------------------------------------
CHINESE_FONTS = ['PingFang HK', 'STHeiti', 'Heiti TC', 'Heiti SC',
                 'PingFang SC', 'SimHei', 'sans-serif']

def get_chinese_font():
    available = {f.name for f in fm.fontManager.ttflist}
    for name in CHINESE_FONTS:
        if name in available:
            return name
    return 'sans-serif'

FONT = get_chinese_font()
plt.rcParams['font.family'] = FONT
plt.rcParams['axes.unicode_minus'] = False

# ---------------------------------------------------------------------------
# Colours
# ---------------------------------------------------------------------------
BG     = '#0F1729'
CYAN   = '#4EC9B0'
ORANGE = '#FF6B35'
WHITE  = '#FFFFFF'
DIM    = '#6B7280'

# ---------------------------------------------------------------------------
# Ring definitions (outermost → innermost)
# ---------------------------------------------------------------------------
rings = [
    {'radius': 4.2, 'label': '找一粒沙子',       'sub': 'Find a grain of sand',      'alpha': 0.10},
    {'radius': 3.3, 'label': '红色的沙子',       'sub': 'Red sand',                  'alpha': 0.18},
    {'radius': 2.4, 'label': '直径 0.5mm',       'sub': 'Diameter 0.5 mm',           'alpha': 0.28},
    {'radius': 1.5, 'label': '三个凹坑',         'sub': 'Three pits',                'alpha': 0.40},
    {'radius': 0.6, 'label': '等腰三角形排列',    'sub': 'Isosceles triangle',         'alpha': 0.70},
]

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(19.2, 10.8), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(-7.5, 7.5)
ax.set_ylim(-5.8, 5.8)
ax.set_aspect('equal')
ax.axis('off')

# Centre of the concentric circles (shifted left to make room for annotation)
cx, cy = -0.8, 0.0

# ---------------------------------------------------------------------------
# Draw rings (outermost first)
# ---------------------------------------------------------------------------
for i, ring in enumerate(rings):
    r = ring['radius']
    a = ring['alpha']

    # Filled circle
    circle = plt.Circle((cx, cy), r,
                         facecolor=(*matplotlib.colors.to_rgb(CYAN), a),
                         edgecolor=CYAN, linewidth=1.8,
                         linestyle='-' if i == len(rings)-1 else '--',
                         zorder=2 + i)
    ax.add_patch(circle)

    # Label positioning — spread labels around the rings to avoid overlap
    # Each ring gets a unique position (angle / side)
    if i == 0:
        # Outermost — top-left
        angle = np.radians(145)
        lx = cx + r * np.cos(angle) - 0.3
        ly = cy + r * np.sin(angle) + 0.3
        ax.text(lx, ly, ring['label'], color=WHITE, fontsize=17,
                ha='right', va='bottom', fontweight='bold', zorder=10)
        ax.text(lx, ly - 0.35, ring['sub'], color=DIM, fontsize=12,
                ha='right', va='top', fontstyle='italic', zorder=10)
        # Connector
        ax.plot([lx + 0.1, cx + r * np.cos(angle)],
                [ly - 0.15, cy + r * np.sin(angle)],
                color=DIM, linewidth=0.8, alpha=0.5, zorder=5)
    elif i == 1:
        # Second ring — left side
        lx = cx - r - 0.3
        ly = cy + 0.8
        ax.text(lx, ly, ring['label'], color=WHITE, fontsize=17,
                ha='right', va='center', fontweight='bold', zorder=10)
        ax.text(lx, ly - 0.4, ring['sub'], color=DIM, fontsize=12,
                ha='right', va='center', fontstyle='italic', zorder=10)
        ax.plot([lx + 0.1, cx - r + 0.1], [ly, cy + 0.4],
                color=DIM, linewidth=0.8, alpha=0.5, zorder=5)
    elif i == 2:
        # Third ring — bottom-left
        angle = np.radians(215)
        lx = cx + r * np.cos(angle) - 0.3
        ly = cy + r * np.sin(angle) - 0.3
        ax.text(lx, ly, ring['label'], color=WHITE, fontsize=17,
                ha='right', va='top', fontweight='bold', zorder=10)
        ax.text(lx, ly - 0.4, ring['sub'], color=DIM, fontsize=12,
                ha='right', va='top', fontstyle='italic', zorder=10)
        ax.plot([lx + 0.1, cx + r * np.cos(angle)],
                [ly + 0.15, cy + r * np.sin(angle)],
                color=DIM, linewidth=0.8, alpha=0.5, zorder=5)
    elif i == 3:
        # Fourth ring — bottom
        lx = cx + 1.0
        ly = cy - r - 0.4
        ax.text(lx, ly, ring['label'], color=WHITE, fontsize=17,
                ha='center', va='top', fontweight='bold', zorder=10)
        ax.text(lx, ly - 0.4, ring['sub'], color=DIM, fontsize=12,
                ha='center', va='top', fontstyle='italic', zorder=10)
    else:
        # Innermost — place inside/below the tiny circle
        lx = cx
        ly = cy - r - 0.45
        ax.text(lx, ly, ring['label'], color=ORANGE, fontsize=17,
                ha='center', va='top', fontweight='bold', zorder=10)
        ax.text(lx, ly - 0.4, ring['sub'], color=ORANGE, fontsize=12,
                ha='center', va='top', fontstyle='italic', alpha=0.8,
                zorder=10)

# Centre dot
centre_dot = plt.Circle((cx, cy), 0.12, facecolor=ORANGE,
                          edgecolor=ORANGE, linewidth=2, zorder=20)
ax.add_patch(centre_dot)

# ---------------------------------------------------------------------------
# Arrow: outside → centre  "约束越多 → AI越难"
# ---------------------------------------------------------------------------
# Diagonal arrow from top-right to centre
arr_start = (cx + 4.8, cy + 3.8)
arr_end   = (cx + 0.8, cy + 0.5)

ax.annotate('',
            xy=arr_end, xytext=arr_start,
            arrowprops=dict(arrowstyle='->', color=ORANGE,
                            lw=2.5, connectionstyle='arc3,rad=-0.1'),
            zorder=15)

ax.text(cx + 5.0, cy + 4.1, '约束越多 → AI 越难',
        color=ORANGE, fontsize=20, fontweight='bold',
        ha='left', va='bottom', zorder=15)
ax.text(cx + 5.0, cy + 3.55, 'More constraints → Harder for AI',
        color=DIM, fontsize=14, ha='left', va='bottom',
        fontstyle='italic', zorder=15)

# ---------------------------------------------------------------------------
# Side annotation: "解空间" shrinkage
# ---------------------------------------------------------------------------
ann_x = cx + 5.5

# Vertical double-headed arrow showing shrinkage
ax.annotate('',
            xy=(ann_x, cy - 3.8), xytext=(ann_x, cy + 2.5),
            arrowprops=dict(arrowstyle='<->', color=CYAN,
                            lw=2, linestyle='-'),
            zorder=15)

ax.text(ann_x + 0.3, cy + 0.0, '解空间\nSolution\nSpace',
        color=CYAN, fontsize=18, fontweight='bold',
        ha='left', va='center', zorder=15)

# Small arrows showing compression
for offset in [-2.5, -1.2, 0.0, 1.2, 2.0]:
    marker_y = cy + offset
    ax.plot([ann_x - 0.15, ann_x + 0.15], [marker_y, marker_y],
            color=CYAN, linewidth=1, alpha=0.5, zorder=14)

# ---------------------------------------------------------------------------
# Constraint count labels (right side of rings)
# ---------------------------------------------------------------------------
for i, ring in enumerate(rings):
    r = ring['radius']
    rx = cx + r + 0.15
    ry = cy + 0.15
    constraint_num = f'+{i+1}'
    ax.text(rx, ry, constraint_num, color=DIM, fontsize=13,
            ha='left', va='center', alpha=0.6, zorder=10)

# ---------------------------------------------------------------------------
# Title
# ---------------------------------------------------------------------------
ax.text(0, 5.3, '解空间坍缩 — 约束如何让问题变得不可能',
        color=WHITE, fontsize=28, fontweight='bold',
        ha='center', va='center', zorder=20)
ax.text(0, 4.7, 'Solution Space Collapse — How Constraints Make Problems Impossible',
        color=DIM, fontsize=15, ha='center', va='center',
        fontstyle='italic', zorder=20)

plt.tight_layout()

# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------
out = Path('/Users/mik/strange LLM/assets/diagrams/rendered/solution_space.png')
fig.savefig(out, dpi=150, facecolor=BG, bbox_inches='tight',
            pad_inches=0.3)
plt.close(fig)
print(f'Saved → {out}  ({out.stat().st_size / 1024:.0f} KB)')
