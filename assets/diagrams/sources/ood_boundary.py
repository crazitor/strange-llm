"""
Diagram 3: OOD Boundary — "Beijing Driver in London" (Page 59)
Visualises the Out-of-Distribution concept: deep expertise in one
domain becomes dangerous when silently applied in another.
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
BG        = '#0F1729'
CYAN      = '#4EC9B0'
GREEN     = '#00D4AA'
RED       = '#FF4444'
ORANGE    = '#FF6B35'
WHITE     = '#FFFFFF'
DIM       = '#6B7280'
GREEN_BG  = '#0A2A1A'
RED_BG    = '#2A0A0A'

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(19.2, 10.8), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# ---------------------------------------------------------------------------
# Left half — Beijing (green zone)
# ---------------------------------------------------------------------------
left_rect = mpatches.FancyBboxPatch(
    (2, 12), 44, 72, boxstyle='round,pad=1.5',
    facecolor=GREEN_BG, edgecolor=GREEN, linewidth=2.5, alpha=0.85)
ax.add_patch(left_rect)

# Title
ax.text(24, 80, '北京 Beijing', color=GREEN, fontsize=32,
        fontweight='bold', ha='center', va='center')
ax.text(24, 74, '训练分布内 (In-Distribution)', color=GREEN, fontsize=16,
        ha='center', va='center', alpha=0.7)

# Driving rule
ax.text(24, 62, '右侧行驶  >>', color=GREEN, fontsize=28,
        ha='center', va='center', fontweight='bold')

# Checkmark — use a simple circle + text instead of Unicode glyph
ok_circle = plt.Circle((24, 53), 3.5, facecolor='#0A3A1A',
                         edgecolor=GREEN, linewidth=2.5, zorder=10)
ax.add_patch(ok_circle)
ax.text(24, 53, 'OK', color=GREEN, fontsize=24,
        ha='center', va='center', fontweight='bold', zorder=11)

# Experience label
ax.text(24, 40, '十年经验', color=WHITE, fontsize=22,
        ha='center', va='center', fontweight='bold')
ax.text(24, 34, '= 高度自信', color=GREEN, fontsize=18,
        ha='center', va='center', alpha=0.8)

# Right-pointing arrows
for y_pos in [26, 22, 18]:
    arrow = FancyArrowPatch((10, y_pos), (38, y_pos),
                            arrowstyle='->', color=GREEN,
                            linewidth=2, mutation_scale=20, alpha=0.5)
    ax.add_patch(arrow)

# ---------------------------------------------------------------------------
# Right half — London (red zone)
# ---------------------------------------------------------------------------
right_rect = mpatches.FancyBboxPatch(
    (54, 12), 44, 72, boxstyle='round,pad=1.5',
    facecolor=RED_BG, edgecolor=RED, linewidth=2.5, alpha=0.85)
ax.add_patch(right_rect)

# Title
ax.text(76, 80, '伦敦 London', color=RED, fontsize=32,
        fontweight='bold', ha='center', va='center')
ax.text(76, 74, '分布外 (Out-of-Distribution)', color=RED, fontsize=16,
        ha='center', va='center', alpha=0.7)

# Driving rule
ax.text(76, 62, '<<  左侧行驶', color=RED, fontsize=28,
        ha='center', va='center', fontweight='bold')

# Cross mark — use a circle + text instead of Unicode glyph
fail_circle = plt.Circle((76, 53), 3.5, facecolor='#3A0A0A',
                           edgecolor=RED, linewidth=2.5, zorder=10)
ax.add_patch(fail_circle)
ax.text(76, 53, 'NO', color=RED, fontsize=24,
        ha='center', va='center', fontweight='bold', zorder=11)

# Experience label
ax.text(76, 40, '十年经验', color=WHITE, fontsize=22,
        ha='center', va='center', fontweight='bold')
ax.text(76, 34, '= 致命危险', color=RED, fontsize=18,
        ha='center', va='center', alpha=0.8)

# Left-pointing arrows
for y_pos in [26, 22, 18]:
    arrow = FancyArrowPatch((90, y_pos), (62, y_pos),
                            arrowstyle='->', color=RED,
                            linewidth=2, mutation_scale=20, alpha=0.5)
    ax.add_patch(arrow)

# ---------------------------------------------------------------------------
# Center — confused driver / question mark
# ---------------------------------------------------------------------------
center_circle = plt.Circle((50, 54), 7, facecolor=BG,
                            edgecolor=ORANGE, linewidth=3, zorder=10)
ax.add_patch(center_circle)
ax.text(50, 54, '?', color=ORANGE, fontsize=52,
        ha='center', va='center', fontweight='bold', zorder=11)

# Connecting arrows from center
arrow_left = FancyArrowPatch((43, 54), (36, 54),
                              arrowstyle='->', color=DIM,
                              linewidth=1.5, mutation_scale=15, alpha=0.5,
                              linestyle='dashed', zorder=9)
arrow_right = FancyArrowPatch((57, 54), (64, 54),
                               arrowstyle='->', color=DIM,
                               linewidth=1.5, mutation_scale=15, alpha=0.5,
                               linestyle='dashed', zorder=9)
ax.add_patch(arrow_left)
ax.add_patch(arrow_right)

# ---------------------------------------------------------------------------
# Title
# ---------------------------------------------------------------------------
ax.text(50, 95, 'OOD 边界：北京司机在伦敦',
        color=WHITE, fontsize=30, fontweight='bold',
        ha='center', va='center')

# ---------------------------------------------------------------------------
# Bottom insight text
# ---------------------------------------------------------------------------
# Background bar
bottom_rect = mpatches.FancyBboxPatch(
    (8, 1.5), 84, 7, boxstyle='round,pad=0.8',
    facecolor='#1A1A2E', edgecolor=DIM, linewidth=1.5, alpha=0.8)
ax.add_patch(bottom_rect)

ax.text(50, 5, '越熟练越自信  →  越容易在简单规则上犯致命错误',
        color=ORANGE, fontsize=22, fontweight='bold',
        ha='center', va='center')

plt.tight_layout()

# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------
out = Path('/Users/mik/strange LLM/assets/diagrams/rendered/ood_boundary.png')
fig.savefig(out, dpi=150, facecolor=BG, bbox_inches='tight',
            pad_inches=0.3)
plt.close(fig)
print(f'Saved → {out}  ({out.stat().st_size / 1024:.0f} KB)')
