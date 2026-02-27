"""
P2 - 2022 vs 2025: From Hype to Silence
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from pathlib import Path
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle

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
WARM_BG = '#1F1510'
COLD_BG = '#0D1520'

OUT = Path('/Users/mik/strange LLM/assets/diagrams/rendered/evolution_2022_vs_2025.png')

fig = plt.figure(figsize=(19.2, 10.8), dpi=150, facecolor=BG)

# Three axes: left, center timeline, right
ax_left = fig.add_axes([0.03, 0.08, 0.38, 0.80])
ax_mid = fig.add_axes([0.42, 0.08, 0.16, 0.80])
ax_right = fig.add_axes([0.59, 0.08, 0.38, 0.80])

for ax in [ax_left, ax_mid, ax_right]:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

# === LEFT: 2022 (Hot, excited) ===
ax_left.set_facecolor(WARM_BG)
# Warm border
border_left = FancyBboxPatch((0.2, 0.2), 9.6, 9.6, boxstyle='round,pad=0.3',
                              facecolor=WARM_BG, edgecolor=ORANGE, linewidth=2.5, zorder=1)
ax_left.add_patch(border_left)

# Year
ax_left.text(5, 9.2, '2022', fontsize=55, color=ORANGE, fontweight='bold',
             ha='center', va='center', zorder=5)

# Big keyword
ax_left.text(5, 7.3, 'ChatGPT\n震惊世界', fontsize=30, color=WHITE, fontweight='bold',
             ha='center', va='center', zorder=5, linespacing=1.3)

# Emoji / mood indicator
ax_left.text(5, 5.8, '', fontsize=45, ha='center', va='center', zorder=5)

# Tags
tags_left = ['全民热议', 'AI要取代一切', 'AGI将至', '风口来了']
tag_positions = [(2.5, 4.8), (7.0, 4.8), (2.8, 3.8), (7.0, 3.8)]
for tag, (tx, ty) in zip(tags_left, tag_positions):
    bbox = FancyBboxPatch((tx - 1.5, ty - 0.35), 3.0, 0.7,
                          boxstyle='round,pad=0.15',
                          facecolor=ORANGE, edgecolor='none', alpha=0.2, zorder=3)
    ax_left.add_patch(bbox)
    ax_left.text(tx, ty, tag, fontsize=14, color=ORANGE, ha='center', va='center',
                 fontweight='bold', zorder=5)

# Heat bar (thermometer metaphor)
for i in range(8):
    bar = Rectangle((1.0, 1.5 + i * 0.22), 1.2, 0.18,
                     facecolor=ORANGE, alpha=0.3 + i * 0.08, zorder=3)
    ax_left.add_patch(bar)
ax_left.text(1.6, 3.6, '', fontsize=20, ha='center', va='center', zorder=5)
ax_left.text(1.6, 1.2, '热度', fontsize=11, color=ORANGE, ha='center', alpha=0.7)

# Bottom text
ax_left.text(5, 0.8, '"每个人都在谈AI"', fontsize=16, color=ORANGE,
             ha='center', style='italic', alpha=0.8, zorder=5)


# === RIGHT: 2025 (Cold, indifferent) ===
ax_right.set_facecolor(COLD_BG)
border_right = FancyBboxPatch((0.2, 0.2), 9.6, 9.6, boxstyle='round,pad=0.3',
                               facecolor=COLD_BG, edgecolor=DIM, linewidth=2.5, zorder=1)
ax_right.add_patch(border_right)

# Year
ax_right.text(5, 9.2, '2025', fontsize=55, color=DIM, fontweight='bold',
              ha='center', va='center', zorder=5)

# Big keyword
ax_right.text(5, 7.3, 'AI？\n又是那个东西', fontsize=30, color='#8899AA', fontweight='bold',
              ha='center', va='center', zorder=5, linespacing=1.3)

# Emoji / mood
ax_right.text(5, 5.8, '', fontsize=45, ha='center', va='center', zorder=5)

# Tags
tags_right = ['审美疲劳', '还没取代我', '割裂感', '泡沫?']
tag_positions_r = [(2.5, 4.8), (7.0, 4.8), (2.8, 3.8), (7.0, 3.8)]
for tag, (tx, ty) in zip(tags_right, tag_positions_r):
    bbox = FancyBboxPatch((tx - 1.5, ty - 0.35), 3.0, 0.7,
                          boxstyle='round,pad=0.15',
                          facecolor=DIM, edgecolor='none', alpha=0.15, zorder=3)
    ax_right.add_patch(bbox)
    ax_right.text(tx, ty, tag, fontsize=14, color=DIM, ha='center', va='center',
                  fontweight='bold', zorder=5)

# Cold bar
for i in range(8):
    alpha_val = 0.3 - i * 0.03
    if alpha_val < 0.05:
        alpha_val = 0.05
    bar = Rectangle((1.0, 1.5 + i * 0.22), 1.2, 0.18,
                     facecolor='#3A4A5A', alpha=alpha_val, zorder=3)
    ax_right.add_patch(bar)
ax_right.text(1.6, 3.6, '', fontsize=20, ha='center', va='center', zorder=5)
ax_right.text(1.6, 1.2, '热度', fontsize=11, color=DIM, ha='center', alpha=0.7)

# Bottom text
ax_right.text(5, 0.8, '"没人再谈AI了"', fontsize=16, color=DIM,
              ha='center', style='italic', alpha=0.8, zorder=5)


# === MIDDLE: Timeline ===
ax_mid.set_facecolor(BG)

# Vertical timeline
ax_mid.plot([5, 5], [2, 8], color=WHITE, linewidth=2, alpha=0.4, zorder=3)

# Arrow from left to right
ax_mid.annotate('', xy=(8.5, 5), xytext=(1.5, 5),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=2.5, alpha=0.7),
                zorder=5)

# "3 years" label
ax_mid.text(5, 5.8, '3年', fontsize=28, color=WHITE, ha='center', va='center',
            fontweight='bold', zorder=5)

# Dots on timeline
ax_mid.plot(5, 8, 'o', color=ORANGE, markersize=12, zorder=5)
ax_mid.plot(5, 2, 'o', color=DIM, markersize=12, zorder=5)
ax_mid.text(5, 8.5, '狂热', fontsize=12, color=ORANGE, ha='center', zorder=5)
ax_mid.text(5, 1.5, '沉默', fontsize=12, color=DIM, ha='center', zorder=5)

# Gradient line between dots
n_seg = 50
for i in range(n_seg):
    y1 = 2 + (6 * i / n_seg)
    y2 = 2 + (6 * (i + 1) / n_seg)
    ratio = i / n_seg
    r = int(0xFF * (1 - ratio) + 0x6B * ratio)
    g = int(0x6B * (1 - ratio) + 0x72 * ratio)
    b = int(0x35 * (1 - ratio) + 0x80 * ratio)
    color = f'#{r:02x}{g:02x}{b:02x}'
    ax_mid.plot([5, 5], [y1, y2], color=color, linewidth=3, alpha=0.7, zorder=4)

# Title
fig.suptitle('从狂热到沉默 — 3年的割裂',
             fontsize=32, color=WHITE, fontweight='bold', y=0.97)

fig.savefig(OUT, dpi=150, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
plt.close()
print(f'Saved: {OUT}')
