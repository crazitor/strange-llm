"""
P57 - Seedance Interface Mock: "You think you're creating?"
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from pathlib import Path
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch

# Font setup
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

# Colors
BG = '#0F1729'
CYAN = '#00D4AA'
ORANGE = '#FF6B35'
WHITE = '#FFFFFF'
DIM = '#6B7280'
GRID = '#1E2A42'
UI_BG = '#161E30'
UI_BORDER = '#2A3550'
SLIDER_BG = '#1A2540'
SLIDER_FILL = '#00D4AA'
SLIDER_RESTRICTED = '#FF6B35'

OUT = Path('/Users/mik/strange LLM/assets/diagrams/rendered/seedance_interface_mock.png')

fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=150, facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 19.2)
ax.set_ylim(0, 10.8)
ax.axis('off')

# === Window frame ===
window = FancyBboxPatch((0.8, 0.8), 17.6, 8.8, boxstyle='round,pad=0.2',
                          facecolor=UI_BG, edgecolor=UI_BORDER, linewidth=2.5, zorder=1)
ax.add_patch(window)

# Title bar
title_bar = Rectangle((0.8, 8.8), 17.6, 0.8, facecolor='#1A2540', edgecolor=UI_BORDER,
                        linewidth=1, zorder=2)
ax.add_patch(title_bar)
# Window dots
for i, c in enumerate(['#FF5F57', '#FFBD2E', '#28C840']):
    dot = plt.Circle((1.5 + i * 0.45, 9.2), 0.12, facecolor=c, edgecolor='none', zorder=3)
    ax.add_patch(dot)
ax.text(9.6, 9.2, 'Seedance Pro  -  AI Video Generator', fontsize=13, color=DIM,
        ha='center', va='center', zorder=3)

# === LEFT PANEL: Parameters ===
panel_left = Rectangle((1.2, 1.2), 6.8, 7.2, facecolor='#121A2E', edgecolor=UI_BORDER,
                         linewidth=1.5, zorder=2)
ax.add_patch(panel_left)
ax.text(4.6, 8.0, 'Parameters', fontsize=16, color=WHITE, ha='center',
        fontweight='bold', zorder=5)

# --- Slider 1: Creative Freedom ---
y1 = 7.0
ax.text(1.6, y1, '创意自由度', fontsize=13, color=WHITE, va='center', zorder=5)
# Slider track
track1 = Rectangle((1.6, y1 - 0.55), 5.8, 0.25, facecolor=SLIDER_BG, edgecolor='none',
                     zorder=3, linewidth=0)
ax.add_patch(track1)
# Restricted fill (only 15%)
fill1 = Rectangle((1.6, y1 - 0.55), 0.9, 0.25, facecolor=SLIDER_RESTRICTED, edgecolor='none',
                    zorder=4, alpha=0.8)
ax.add_patch(fill1)
# Thumb
thumb1 = plt.Circle((2.5, y1 - 0.425), 0.15, facecolor=SLIDER_RESTRICTED, edgecolor=WHITE,
                      linewidth=1.5, zorder=5)
ax.add_patch(thumb1)
ax.text(7.6, y1 - 0.4, '12%', fontsize=11, color=SLIDER_RESTRICTED, va='center', zorder=5)
# Restricted zone indicator
ax.plot([3.5, 7.4], [y1 - 0.425, y1 - 0.425], color=DIM, linewidth=1, linestyle='--',
        alpha=0.3, zorder=3)
ax.text(5.5, y1 - 0.8, '被限制范围', fontsize=10, color=DIM, ha='center',
        alpha=0.6, zorder=5)

# --- Slider 2: Consistency ---
y2 = 5.6
ax.text(1.6, y2, '画面一致性', fontsize=13, color=WHITE, va='center', zorder=5)
track2 = Rectangle((1.6, y2 - 0.55), 5.8, 0.25, facecolor=SLIDER_BG, edgecolor='none',
                     zorder=3)
ax.add_patch(track2)
fill2 = Rectangle((1.6, y2 - 0.55), 5.5, 0.25, facecolor=CYAN, edgecolor='none',
                    zorder=4, alpha=0.6)
ax.add_patch(fill2)
thumb2 = plt.Circle((7.1, y2 - 0.425), 0.15, facecolor=CYAN, edgecolor=WHITE,
                      linewidth=1.5, zorder=5)
ax.add_patch(thumb2)
ax.text(7.6, y2 - 0.4, '95%', fontsize=11, color=CYAN, va='center', zorder=5)

# --- Slider 3: Motion Intensity ---
y3 = 4.2
ax.text(1.6, y3, '运动强度', fontsize=13, color=WHITE, va='center', zorder=5)
track3 = Rectangle((1.6, y3 - 0.55), 5.8, 0.25, facecolor=SLIDER_BG, edgecolor='none',
                     zorder=3)
ax.add_patch(track3)
fill3 = Rectangle((1.6, y3 - 0.55), 1.5, 0.25, facecolor=SLIDER_RESTRICTED, edgecolor='none',
                    zorder=4, alpha=0.7)
ax.add_patch(fill3)
thumb3 = plt.Circle((3.1, y3 - 0.425), 0.15, facecolor=SLIDER_RESTRICTED, edgecolor=WHITE,
                      linewidth=1.5, zorder=5)
ax.add_patch(thumb3)
ax.text(7.6, y3 - 0.4, '20%', fontsize=11, color=SLIDER_RESTRICTED, va='center', zorder=5)

# --- Dropdown: Style ---
y4 = 2.9
ax.text(1.6, y4, '风格', fontsize=13, color=WHITE, va='center', zorder=5)
dropdown = FancyBboxPatch((1.6, y4 - 0.75), 5.8, 0.55, boxstyle='round,pad=0.08',
                            facecolor=SLIDER_BG, edgecolor=UI_BORDER, linewidth=1.5, zorder=3)
ax.add_patch(dropdown)
ax.text(4.5, y4 - 0.48, '安全写实', fontsize=12, color=WHITE, ha='center', va='center', zorder=5)
ax.text(7.0, y4 - 0.48, '', fontsize=10, color=DIM, ha='center', va='center', zorder=5)

# --- Warning annotation ---
warn_box = FancyBboxPatch((1.4, 1.3), 6.4, 0.8, boxstyle='round,pad=0.15',
                            facecolor=ORANGE, edgecolor=ORANGE, linewidth=1.5, alpha=0.15, zorder=3)
ax.add_patch(warn_box)
ax.text(4.6, 1.7, '你在迁就AI的能力边界', fontsize=14, color=ORANGE,
        ha='center', va='center', fontweight='bold', zorder=5)

# === RIGHT PANEL: Preview ===
panel_right = Rectangle((8.4, 1.2), 9.2, 7.2, facecolor='#121A2E', edgecolor=UI_BORDER,
                          linewidth=1.5, zorder=2)
ax.add_patch(panel_right)
ax.text(13.0, 8.0, 'Preview', fontsize=16, color=WHITE, ha='center',
        fontweight='bold', zorder=5)

# 4 preview thumbnails (2x2)
thumb_colors = ['#1A3040', '#1A2840', '#1A3535', '#1A2A40']
thumb_labels = ['结果 1', '结果 2', '结果 3', '结果 4']
thumb_sublabels = ['安全', '保守', '平庸', '雷同']
positions = [(8.8, 4.6), (11.3, 4.6), (8.8, 1.6), (11.3, 1.6)]

for idx, ((tx, ty), tc, tl, tsl) in enumerate(zip(positions, thumb_colors, thumb_labels, thumb_sublabels)):
    thumb_rect = FancyBboxPatch((tx, ty), 2.1, 2.8, boxstyle='round,pad=0.1',
                                 facecolor=tc, edgecolor=UI_BORDER, linewidth=1, zorder=3)
    ax.add_patch(thumb_rect)
    # Placeholder imagery (simple gradient bars)
    for j in range(5):
        bar_color = f'#{20 + j * 8:02x}{30 + j * 5:02x}{40 + j * 6:02x}'
        bar = Rectangle((tx + 0.15, ty + 0.3 + j * 0.45), 1.8, 0.35,
                          facecolor=bar_color, edgecolor='none', alpha=0.4, zorder=4)
        ax.add_patch(bar)
    ax.text(tx + 1.05, ty + 2.5, tl, fontsize=11, color=WHITE, ha='center', va='center',
            zorder=5, alpha=0.8)
    ax.text(tx + 1.05, ty + 0.1, tsl, fontsize=10, color=DIM, ha='center', va='top',
            zorder=5, style='italic')

# Boundary annotation on right panel
boundary_box = FancyBboxPatch((13.8, 2.0), 3.5, 5.0, boxstyle='round,pad=0.15',
                                facecolor='none', edgecolor=ORANGE, linewidth=2,
                                linestyle='--', alpha=0.6, zorder=6)
ax.add_patch(boundary_box)
ax.text(15.55, 7.3, '"只能在这个\n范围内生成"', fontsize=14, color=ORANGE,
        ha='center', va='center', fontweight='bold', zorder=7, linespacing=1.4)

# Arrow pointing to the boundary
ax.annotate('', xy=(15.55, 7.0), xytext=(15.55, 7.55),
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2), zorder=7)

# Possible range labels
ax.text(15.55, 1.5, 'AI能力边界', fontsize=11, color=ORANGE, ha='center',
        alpha=0.6, zorder=7)

# Title
fig.suptitle('Seedance 界面 — 你以为你在创作？',
             fontsize=30, color=WHITE, fontweight='bold', y=0.97)

fig.savefig(OUT, dpi=150, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
plt.close()
print(f'Saved: {OUT}')
