"""
Three Knife Surgery (P77)
Three "surgical knives" cutting into the patch tower at different levels,
representing three self-correcting forces in AI development.
Output: three_knife_surgery.png
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
from matplotlib.patches import Polygon, FancyBboxPatch
from pathlib import Path

# ── Font setup ──
import matplotlib.font_manager as fm
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

# ── Colors ──
BG     = '#0F1729'
CYAN   = '#00D4AA'
ORANGE = '#FF6B35'
WHITE  = '#FFFFFF'
DIM    = '#6B7280'

KNIFE_COLORS = ['#00D4AA', '#FFD700', '#FF6B35']  # cyan, gold, orange

fig, ax = plt.subplots(figsize=(19.2, 10.8), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 56.25)
ax.set_aspect('equal')
ax.axis('off')

# ═══════════════════════════════════════════════════════
# Left side: Simplified Patch Tower (vertical stack, 4 layers)
# ═══════════════════════════════════════════════════════
tower_x = 15
tower_w = 22
layer_h = 8
tower_base_y = 8
tower_layers = [
    ('基座模型', '#00AA85'),
    ('训练/对齐', '#00D4AA'),
    ('工具/接口', '#00E8BE'),
    ('应用层', '#00FFD0'),
]

for i, (label, color) in enumerate(tower_layers):
    y = tower_base_y + i * (layer_h + 0.8)
    box = mpatches.FancyBboxPatch(
        (tower_x, y), tower_w, layer_h,
        boxstyle=mpatches.BoxStyle("Round", pad=0.15),
        facecolor=color, edgecolor=BG, linewidth=2,
        alpha=0.85, zorder=5
    )
    ax.add_patch(box)
    ax.text(tower_x + tower_w / 2, y + layer_h / 2, label,
            fontsize=17, color=BG, fontweight='bold',
            ha='center', va='center', zorder=6)

# Tower label
ax.text(tower_x + tower_w / 2, tower_base_y - 3, '补丁之塔',
        fontsize=18, color=DIM, ha='center', va='center',
        fontweight='bold', zorder=7,
        path_effects=[pe.withStroke(linewidth=3, foreground=BG)])

# ═══════════════════════════════════════════════════════
# Right side: Three knives cutting in
# ═══════════════════════════════════════════════════════
knives = [
    {
        'name': 'Token成本归零',
        'subtitle': '切向底层经济模型',
        'target_layer': 0,   # base
        'color': KNIFE_COLORS[0],
    },
    {
        'name': '开源追平闭源',
        'subtitle': '切向中层技术壁垒',
        'target_layer': 1,   # mid
        'color': KNIFE_COLORS[1],
    },
    {
        'name': '多模态统一',
        'subtitle': '切向顶层应用边界',
        'target_layer': 3,   # top
        'color': KNIFE_COLORS[2],
    },
]

def draw_knife(ax, tip_x, tip_y, color, label, subtitle, knife_num):
    """Draw a stylized knife pointing left toward the tower."""
    # Knife blade: triangle pointing left
    blade_len = 14
    blade_half_h = 2.5
    blade = Polygon([
        (tip_x, tip_y),                               # tip
        (tip_x + blade_len, tip_y + blade_half_h),    # top-right
        (tip_x + blade_len, tip_y - blade_half_h),    # bottom-right
    ], closed=True, facecolor=color, edgecolor=WHITE,
       linewidth=1.5, alpha=0.85, zorder=8)
    ax.add_patch(blade)

    # Knife handle (rectangle)
    handle_w = 8
    handle_h = blade_half_h * 1.6
    handle = mpatches.FancyBboxPatch(
        (tip_x + blade_len, tip_y - handle_h / 2), handle_w, handle_h,
        boxstyle=mpatches.BoxStyle("Round", pad=0.1),
        facecolor=color, edgecolor=WHITE, linewidth=1.5,
        alpha=0.5, zorder=8
    )
    ax.add_patch(handle)

    # Glow line at blade edge
    ax.plot([tip_x, tip_x + 1.5], [tip_y, tip_y],
            color=WHITE, linewidth=3, alpha=0.7, zorder=9)

    # Knife number
    ax.text(tip_x + blade_len + handle_w / 2, tip_y,
            f'{knife_num}',
            fontsize=18, color=BG, fontweight='bold',
            ha='center', va='center', zorder=9)

    # Label to the right of the handle
    label_x = tip_x + blade_len + handle_w + 3
    ax.text(label_x, tip_y + 1.5, label,
            fontsize=20, color=color, fontweight='bold',
            ha='left', va='center', zorder=9,
            path_effects=[pe.withStroke(linewidth=3, foreground=BG)])
    ax.text(label_x, tip_y - 1.5, subtitle,
            fontsize=14, color=DIM, ha='left', va='center',
            zorder=9,
            path_effects=[pe.withStroke(linewidth=3, foreground=BG)])


# Position knives
tower_right = tower_x + tower_w
for i, knife in enumerate(knives):
    layer_idx = knife['target_layer']
    target_y = tower_base_y + layer_idx * (layer_h + 0.8) + layer_h / 2
    tip_x = tower_right + 3  # just to the right of tower

    # Dashed line from knife tip to tower edge
    ax.plot([tower_right + 0.5, tip_x], [target_y, target_y],
            color=knife['color'], linewidth=2, linestyle='--',
            alpha=0.6, zorder=7)

    # Impact flash at the tower edge
    for r, a in [(2.5, 0.05), (1.5, 0.1), (0.8, 0.15)]:
        flash = plt.Circle((tower_right + 0.5, target_y), r,
                            facecolor=knife['color'], edgecolor='none',
                            alpha=a, zorder=6)
        ax.add_patch(flash)

    draw_knife(ax, tip_x, target_y, knife['color'],
               knife['name'], knife['subtitle'], i + 1)

# ═══════════════════════════════════════════════════════
# Title
# ═══════════════════════════════════════════════════════
ax.text(50, 52, '三把手术刀 -- 自我纠偏',
        fontsize=30, color=WHITE, fontweight='bold',
        ha='center', va='center', zorder=10,
        path_effects=[pe.withStroke(linewidth=4, foreground=BG)])

# Bottom annotation
ax.text(50, 2.5, '"不是外力推翻, 是趋势自己在拆解补丁之塔"',
        fontsize=17, color=DIM, ha='center', va='center',
        fontstyle='italic', zorder=8,
        path_effects=[pe.withStroke(linewidth=3, foreground=BG)])

# ── Save ──
out = Path('/Users/mik/strange LLM/assets/diagrams/rendered/three_knife_surgery.png')
fig.savefig(out, dpi=150, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
plt.close(fig)
print(f'Saved -> {out}  ({out.stat().st_size / 1024:.0f} KB)')
