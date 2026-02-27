"""
Model Collapse Funnel (P15, P38)
3000+ open source models funnel down to ~1 underlying architecture.
Trapezoid/funnel visualization from wide (top) to narrow (bottom).
Output: model_collapse_funnel.png
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
from matplotlib.patches import Polygon
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

# ── Funnel layers (top to bottom) ──
# Each: (label, sub_label, width_fraction, color)
funnel_layers = [
    ('3000+', '开源模型 (Open Source Models)', 1.0, '#00D4AA'),
    ('~100', '有真实用户的模型', 0.65, '#00AA85'),
    ('~20', 'API 服务商', 0.42, '#FF8C5A'),
    ('5-10', '实际可用的主流模型', 0.25, '#FF6B35'),
    ('1', '底层架构: Transformer', 0.12, '#FF4444'),
]

fig, ax = plt.subplots(figsize=(19.2, 10.8), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 56.25)
ax.set_aspect('equal')
ax.axis('off')

cx = 50  # center x
total_height = 38
top_y = 48
layer_h = total_height / len(funnel_layers)
gap = 0.6
max_half_w = 38

for i, (num, label, wf, color) in enumerate(funnel_layers):
    y_top = top_y - i * layer_h
    y_bot = y_top - layer_h + gap

    # Width at top and bottom of this trapezoid segment
    if i == 0:
        w_top = max_half_w * wf
    else:
        w_top = max_half_w * funnel_layers[i][2] + \
                (max_half_w * funnel_layers[i - 1][2] - max_half_w * funnel_layers[i][2]) * 0.3
        # Actually, smoother approach: top of current = bottom of previous
    # Use continuous widths
    if i == 0:
        hw_top = max_half_w * 1.0
    else:
        hw_top = max_half_w * (funnel_layers[i - 1][2] + wf) / 2

    hw_bot = max_half_w * wf

    # Draw trapezoid
    trap = Polygon([
        (cx - hw_top, y_top),
        (cx + hw_top, y_top),
        (cx + hw_bot, y_bot),
        (cx - hw_bot, y_bot),
    ], closed=True, facecolor=color, edgecolor=BG, linewidth=2,
       alpha=0.85, zorder=5)
    ax.add_patch(trap)

    # Glow
    trap_glow = Polygon([
        (cx - hw_top - 0.5, y_top + 0.3),
        (cx + hw_top + 0.5, y_top + 0.3),
        (cx + hw_bot + 0.5, y_bot - 0.3),
        (cx - hw_bot - 0.5, y_bot - 0.3),
    ], closed=True, facecolor=color, edgecolor='none',
       alpha=0.06, zorder=3)
    ax.add_patch(trap_glow)

    # Number label (large, on left inside)
    y_mid = (y_top + y_bot) / 2
    ax.text(cx - hw_bot * 0.6, y_mid, num,
            fontsize=28, color=WHITE, fontweight='bold',
            ha='center', va='center', zorder=7,
            path_effects=[pe.withStroke(linewidth=4, foreground=BG)])

    # Description label (right side)
    ax.text(cx + max(hw_bot, hw_top) * 0.3, y_mid, label,
            fontsize=17, color=WHITE, fontweight='bold',
            ha='center', va='center', zorder=7,
            path_effects=[pe.withStroke(linewidth=3, foreground=BG)])

# Downward arrow along the funnel
for y_arr in np.linspace(top_y - 3, top_y - total_height + 5, 4):
    ax.annotate('',
                xy=(cx + max_half_w + 4, y_arr - 3),
                xytext=(cx + max_half_w + 4, y_arr + 1),
                arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5, alpha=0.4),
                zorder=3)

# Side label
ax.text(cx + max_half_w + 7, (top_y + top_y - total_height) / 2,
        '收束\nConvergence',
        fontsize=16, color=DIM, ha='center', va='center',
        fontstyle='italic', rotation=-90, zorder=4,
        path_effects=[pe.withStroke(linewidth=3, foreground=BG)])

# Title
ax.text(50, 53.5, '3000+ --> 1: 大模型的收束',
        fontsize=30, color=WHITE, fontweight='bold',
        ha='center', va='center', zorder=10,
        path_effects=[pe.withStroke(linewidth=4, foreground=BG)])

# Bottom annotation
ax.text(50, 5, '"表面上百花齐放，底层只有一种花"',
        fontsize=18, color=DIM, ha='center', va='center',
        fontstyle='italic', zorder=8,
        path_effects=[pe.withStroke(linewidth=3, foreground=BG)])

# ── Save ──
out = Path('/Users/mik/strange LLM/assets/diagrams/rendered/model_collapse_funnel.png')
fig.savefig(out, dpi=150, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
plt.close(fig)
print(f'Saved -> {out}  ({out.stat().st_size / 1024:.0f} KB)')
