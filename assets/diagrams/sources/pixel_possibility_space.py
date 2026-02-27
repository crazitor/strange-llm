"""
P66 - Pixel Possibility Space
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from pathlib import Path
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Ellipse
from matplotlib.collections import PathCollection

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

OUT = Path('/Users/mik/strange LLM/assets/diagrams/rendered/pixel_possibility_space.png')

fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=150, facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(-12, 12)
ax.set_ylim(-8, 8)
ax.set_aspect('equal')
ax.axis('off')

# Big ellipse: "All possible pixel arrangements"
outer = Ellipse((0, 0), 18, 12, fill=True, facecolor='#141E33', edgecolor=DIM,
                linewidth=2.5, zorder=1, alpha=0.9)
ax.add_patch(outer)

# Noise dots filling the space (random, dim)
np.random.seed(42)
n_noise = 3000
noise_r = np.random.uniform(0, 1, n_noise) ** 0.5
noise_theta = np.random.uniform(0, 2 * np.pi, n_noise)
noise_x = noise_r * 8.5 * np.cos(noise_theta)
noise_y = noise_r * 5.5 * np.sin(noise_theta)
# Filter to be inside the ellipse
mask = (noise_x / 9) ** 2 + (noise_y / 6) ** 2 < 0.95
noise_x, noise_y = noise_x[mask], noise_y[mask]
ax.scatter(noise_x, noise_y, s=1.5, c='#1E2A42', alpha=0.6, zorder=2, edgecolors='none')

# More visible noise particles
n_noise2 = 500
noise_r2 = np.random.uniform(0, 1, n_noise2) ** 0.5
noise_theta2 = np.random.uniform(0, 2 * np.pi, n_noise2)
noise_x2 = noise_r2 * 8 * np.cos(noise_theta2)
noise_y2 = noise_r2 * 5.2 * np.sin(noise_theta2)
mask2 = (noise_x2 / 9) ** 2 + (noise_y2 / 6) ** 2 < 0.9
noise_x2, noise_y2 = noise_x2[mask2], noise_y2[mask2]
ax.scatter(noise_x2, noise_y2, s=3, c='#2A3A55', alpha=0.4, zorder=2, edgecolors='none')

# Meaningful image clusters (tiny bright spots)
clusters = [
    {'pos': (-3.5, 1.5), 'label': '风景照', 'n': 25, 'spread': 0.4},
    {'pos': (2.0, 2.5), 'label': '人脸', 'n': 20, 'spread': 0.35},
    {'pos': (4.5, -1.0), 'label': '文字', 'n': 18, 'spread': 0.3},
    {'pos': (-1.0, -2.5), 'label': '艺术品', 'n': 22, 'spread': 0.38},
]

for cl in clusters:
    cx, cy = cl['pos']
    n = cl['n']
    spread = cl['spread']

    # Glow effect
    glow = plt.Circle((cx, cy), spread * 2.5, fill=True, facecolor=CYAN, alpha=0.06, zorder=3)
    ax.add_patch(glow)
    glow2 = plt.Circle((cx, cy), spread * 1.8, fill=True, facecolor=CYAN, alpha=0.08, zorder=3)
    ax.add_patch(glow2)

    # Cluster points
    cl_x = np.random.normal(cx, spread, n)
    cl_y = np.random.normal(cy, spread, n)
    ax.scatter(cl_x, cl_y, s=15, c=CYAN, alpha=0.7, zorder=5, edgecolors='none')
    ax.scatter([cx], [cy], s=50, c=CYAN, alpha=0.9, zorder=6, edgecolors='none')

    # Label
    ax.text(cx, cy - spread - 0.5, cl['label'], fontsize=13, color=CYAN,
            ha='center', va='top', fontweight='bold', alpha=0.9, zorder=7)

# Label: "噪声区"
ax.text(6.5, 4.0, '噪声区\n(随机像素排列)', fontsize=14, color=DIM, ha='center',
        alpha=0.7, style='italic', zorder=4)
ax.text(-6.0, -3.5, '噪声区', fontsize=14, color=DIM, ha='center',
        alpha=0.5, style='italic', zorder=4)

# Outer label: the space
ax.text(0, 6.8, '所有可能的像素排列', fontsize=18, color=DIM, ha='center',
        fontweight='bold', zorder=10)
ax.annotate('', xy=(0, 6.2), xytext=(0, 6.6),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5), zorder=10)

# Proportion label
ax.text(0, -7.0, '有意义的图像占比 < 0.0001%',
        fontsize=20, color=ORANGE, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=ORANGE, alpha=0.8),
        zorder=10)

# Outside annotation
ax.text(10.5, 3.5, '每增加一个像素\n空间扩大256倍',
        fontsize=14, color=WHITE, ha='center', fontweight='bold', alpha=0.8,
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#1A2744', edgecolor=DIM, alpha=0.8),
        zorder=10)
ax.annotate('', xy=(8.8, 2.5), xytext=(9.8, 3.0),
            arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.5, alpha=0.6), zorder=10)

# Title
fig.suptitle('可能性空间 — 大海捞针',
             fontsize=32, color=WHITE, fontweight='bold', y=0.96)

fig.savefig(OUT, dpi=150, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
plt.close()
print(f'Saved: {OUT}')
