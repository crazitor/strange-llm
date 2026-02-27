"""
Tower Evolution (P86)
Three-column comparison showing the patch tower evolving:
  Left:   v1 Patch Tower (wobbly, unstable)
  Center: Deconstruction (layers being taken apart)
  Right:  v2 New Architecture (clean, optimized)
Output: tower_evolution.png
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Polygon
from pathlib import Path

# ── Font setup ──
import matplotlib.font_manager as fm
CHINESE_FONTS = ['PingFang SC', 'PingFang HK', 'STHeiti', 'Heiti SC',
                 'Heiti TC', 'SimHei', 'sans-serif']

def get_chinese_font():
    available = {f.name for f in fm.fontManager.ttflist}
    for name in CHINESE_FONTS:
        if name in available:
            return name
    return 'sans-serif'

FONT = get_chinese_font()
plt.rcParams['font.family'] = FONT
plt.rcParams['axes.unicode_minus'] = False

# ── Colors ──
BG     = '#0F1729'
CYAN   = '#00D4AA'
ORANGE = '#FF6B35'
WHITE  = '#FFFFFF'
DIM    = '#6B7280'
RED    = '#FF4444'

CYAN_SHADES = ['#00FFD0', '#00E8BE', '#00D4AA', '#00BF98', '#00AA85', '#009573']

fig, ax = plt.subplots(figsize=(19.2, 10.8), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 56.25)
ax.set_aspect('equal')
ax.axis('off')


def draw_block(ax, x, y, w, h, color, label, fontsize=13, alpha=1.0,
               rotation=0, linestyle='-', edgecolor=None, text_color=WHITE):
    """Draw a rounded block."""
    ec = edgecolor if edgecolor else color
    if rotation == 0:
        box = FancyBboxPatch(
            (x, y), w, h,
            boxstyle=mpatches.BoxStyle("Round", pad=0.12),
            facecolor=color, edgecolor=ec, linewidth=1.8,
            alpha=alpha, linestyle=linestyle, zorder=5
        )
        ax.add_patch(box)
        ax.text(x + w / 2, y + h / 2, label,
                fontsize=fontsize, color=text_color, fontweight='bold',
                ha='center', va='center', zorder=6,
                path_effects=[pe.withStroke(linewidth=2, foreground=BG)])
    else:
        # For rotated blocks, use transform
        import matplotlib.transforms as mtransforms
        box = FancyBboxPatch(
            (x, y), w, h,
            boxstyle=mpatches.BoxStyle("Round", pad=0.12),
            facecolor=color, edgecolor=ec, linewidth=1.8,
            alpha=alpha, linestyle=linestyle, zorder=5
        )
        t = mtransforms.Affine2D().rotate_deg_around(x + w/2, y + h/2, rotation) + ax.transData
        box.set_transform(t)
        ax.add_patch(box)
        ax.text(x + w / 2, y + h / 2, label,
                fontsize=fontsize, color=text_color, fontweight='bold',
                ha='center', va='center', zorder=6, rotation=rotation,
                path_effects=[pe.withStroke(linewidth=2, foreground=BG)])


# Layer labels for all columns
layer_labels = ['基座', '数据', '对齐', 'Prompt', 'RAG', 'Agent']
n = len(layer_labels)
block_w = 14
block_h = 5
gap_y = 0.8

# ═══════════════════════════════════════════════════════
# Column 1: Wobbly tower (LEFT)
# ═══════════════════════════════════════════════════════
col1_cx = 18
col1_base_y = 6
np.random.seed(42)

for i, label in enumerate(layer_labels):
    y = col1_base_y + i * (block_h + gap_y)
    # Wobble: random x offset and slight rotation
    x_off = np.random.uniform(-2.5, 2.5)
    rot = np.random.uniform(-6, 6)
    color = CYAN_SHADES[i % len(CYAN_SHADES)]
    x = col1_cx - block_w / 2 + x_off
    draw_block(ax, x, y, block_w, block_h, color, label,
               fontsize=13, rotation=rot, alpha=0.8)

# "Cracks" / instability lines
for _ in range(6):
    cx = col1_cx + np.random.uniform(-6, 6)
    cy = col1_base_y + np.random.uniform(3, n * (block_h + gap_y) - 3)
    dx = np.random.uniform(-2, 2)
    dy = np.random.uniform(-1.5, 1.5)
    ax.plot([cx, cx + dx], [cy, cy + dy], color=RED, linewidth=1.2,
            alpha=0.4, zorder=7)

# Column label
ax.text(col1_cx, col1_base_y - 3, 'v1: 补丁之塔',
        fontsize=18, color=ORANGE, fontweight='bold',
        ha='center', va='center', zorder=8,
        path_effects=[pe.withStroke(linewidth=3, foreground=BG)])
ax.text(col1_cx, col1_base_y - 5.5, '歪歪扭扭, 摇摇欲坠',
        fontsize=13, color=DIM, ha='center', va='center',
        fontstyle='italic', zorder=8,
        path_effects=[pe.withStroke(linewidth=2, foreground=BG)])

# ═══════════════════════════════════════════════════════
# Column 2: Deconstruction (CENTER)
# ═══════════════════════════════════════════════════════
col2_cx = 50
col2_base_y = 6

for i, label in enumerate(layer_labels):
    y = col2_base_y + i * (block_h + gap_y)
    # Layers spread apart with dashed connections
    x_off = np.random.uniform(-1.5, 1.5)
    y_off = i * 0.8  # extra vertical spread
    color = CYAN_SHADES[i % len(CYAN_SHADES)]
    x = col2_cx - block_w / 2 + x_off
    actual_y = y + y_off
    draw_block(ax, x, actual_y, block_w, block_h, color, label,
               fontsize=13, alpha=0.5, linestyle='--',
               edgecolor=DIM)

    # Dashed connecting lines between blocks (if not first)
    if i > 0:
        prev_y = col2_base_y + (i - 1) * (block_h + gap_y) + (i - 1) * 0.8 + block_h
        ax.plot([col2_cx, col2_cx], [prev_y, actual_y],
                color=DIM, linewidth=1.2, linestyle=':', alpha=0.4, zorder=3)

# "Examine" magnifying glass effect — subtle circles
for i in [1, 3, 5]:
    y = col2_base_y + i * (block_h + gap_y) + i * 0.8 + block_h / 2
    circle = plt.Circle((col2_cx + block_w / 2 + 2.5, y), 2,
                         facecolor='none', edgecolor=DIM,
                         linewidth=1.5, linestyle='--', alpha=0.4, zorder=6)
    ax.add_patch(circle)

# Column label
ax.text(col2_cx, col2_base_y - 3, '拆解分析',
        fontsize=18, color=WHITE, fontweight='bold',
        ha='center', va='center', zorder=8,
        path_effects=[pe.withStroke(linewidth=3, foreground=BG)])
ax.text(col2_cx, col2_base_y - 5.5, '理解每一层的作用',
        fontsize=13, color=DIM, ha='center', va='center',
        fontstyle='italic', zorder=8,
        path_effects=[pe.withStroke(linewidth=2, foreground=BG)])

# ═══════════════════════════════════════════════════════
# Column 3: Clean new architecture (RIGHT)
# ═══════════════════════════════════════════════════════
col3_cx = 82
col3_base_y = 6

# Reordered / optimized layers
new_labels = ['统一基座', '数据+对齐', '推理引擎', '工具层', '应用接口', '用户层']
# Use a brighter, more uniform palette
new_colors = ['#00AA85', '#00BF98', '#00D4AA', '#00E8BE', '#00FFD0', '#66FFE0']

for i, label in enumerate(new_labels):
    y = col3_base_y + i * (block_h + gap_y)
    x = col3_cx - block_w / 2  # perfectly aligned
    draw_block(ax, x, y, block_w, block_h, new_colors[i], label,
               fontsize=13, alpha=0.95)

# Clean connecting lines
for i in range(n - 1):
    y_top = col3_base_y + i * (block_h + gap_y) + block_h
    y_bot = col3_base_y + (i + 1) * (block_h + gap_y)
    ax.plot([col3_cx, col3_cx], [y_top, y_bot],
            color=CYAN, linewidth=2, alpha=0.3, zorder=3)

# Stability indicator — straight vertical line on the side
total_h = n * (block_h + gap_y) - gap_y
ax.plot([col3_cx + block_w / 2 + 2, col3_cx + block_w / 2 + 2],
        [col3_base_y, col3_base_y + total_h],
        color=CYAN, linewidth=2.5, alpha=0.5, zorder=4)
ax.text(col3_cx + block_w / 2 + 4, col3_base_y + total_h / 2,
        'Stable', fontsize=12, color=CYAN, fontweight='bold',
        ha='center', va='center', alpha=0.6, zorder=5,
        path_effects=[pe.withStroke(linewidth=2, foreground=BG)])

# Column label
ax.text(col3_cx, col3_base_y - 3, 'v2: 新架构',
        fontsize=18, color=CYAN, fontweight='bold',
        ha='center', va='center', zorder=8,
        path_effects=[pe.withStroke(linewidth=3, foreground=BG)])
ax.text(col3_cx, col3_base_y - 5.5, '整齐, 牢固, 高效',
        fontsize=13, color=DIM, ha='center', va='center',
        fontstyle='italic', zorder=8,
        path_effects=[pe.withStroke(linewidth=2, foreground=BG)])

# ═══════════════════════════════════════════════════════
# Arrows between columns
# ═══════════════════════════════════════════════════════
arrow_y = col1_base_y + total_h / 2 + 2

# Arrow 1: col1 -> col2
ax.annotate('',
            xy=(col2_cx - block_w / 2 - 3, arrow_y),
            xytext=(col1_cx + block_w / 2 + 3, arrow_y),
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=3,
                            connectionstyle='arc3,rad=0.0'),
            zorder=8)
ax.text((col1_cx + col2_cx) / 2, arrow_y + 2.5, '拆',
        fontsize=16, color=ORANGE, fontweight='bold',
        ha='center', va='center', zorder=9,
        path_effects=[pe.withStroke(linewidth=3, foreground=BG)])

# Arrow 2: col2 -> col3
ax.annotate('',
            xy=(col3_cx - block_w / 2 - 3, arrow_y),
            xytext=(col2_cx + block_w / 2 + 3, arrow_y),
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=3,
                            connectionstyle='arc3,rad=0.0'),
            zorder=8)
ax.text((col2_cx + col3_cx) / 2, arrow_y + 2.5, '建',
        fontsize=16, color=CYAN, fontweight='bold',
        ha='center', va='center', zorder=9,
        path_effects=[pe.withStroke(linewidth=3, foreground=BG)])

# ═══════════════════════════════════════════════════════
# Title & annotations
# ═══════════════════════════════════════════════════════
ax.text(50, 53, '从补丁之塔到新架构',
        fontsize=30, color=WHITE, fontweight='bold',
        ha='center', va='center', zorder=10,
        path_effects=[pe.withStroke(linewidth=4, foreground=BG)])

# Bottom annotation
ax.text(50, 1.5, '"不是推倒重来, 而是理解后重建"',
        fontsize=18, color=DIM, ha='center', va='center',
        fontstyle='italic', zorder=8,
        path_effects=[pe.withStroke(linewidth=3, foreground=BG)])

# ── Save ──
out = Path('/Users/mik/strange LLM/assets/diagrams/rendered/tower_evolution.png')
fig.savefig(out, dpi=150, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
plt.close(fig)
print(f'Saved -> {out}  ({out.stat().st_size / 1024:.0f} KB)')
