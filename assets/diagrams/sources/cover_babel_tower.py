"""P1 - Cover: AI's Patch Tower (Babel Tower style)"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from pathlib import Path
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, Polygon
from matplotlib.collections import PatchCollection

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

# Cyan palette (light to dark)
CYAN_SHADES = ['#00FFD0', '#00D4AA', '#00B894', '#009B7D', '#007D65', '#005F4E', '#004238']

fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=150, facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 19.2)
ax.set_ylim(0, 10.8)
ax.set_aspect('equal')
ax.axis('off')

np.random.seed(42)

# --- Star field / particle background ---
n_stars = 300
sx = np.random.uniform(0, 19.2, n_stars)
sy = np.random.uniform(0, 10.8, n_stars)
ss = np.random.uniform(0.2, 1.5, n_stars)
sa = np.random.uniform(0.1, 0.5, n_stars)
for i in range(n_stars):
    ax.plot(sx[i], sy[i], '.', color=WHITE, markersize=ss[i], alpha=sa[i])

# --- Ground line ---
ax.plot([0, 19.2], [1.0, 1.0], color=DIM, linewidth=0.8, alpha=0.5)
# Ground glow
for i in range(5):
    ax.plot([3, 16], [1.0, 1.0], color=CYAN, linewidth=0.5, alpha=0.05 * (5 - i))

# --- Tower construction ---
# Tower is centered around x=9.6, from y=1.0 upward
# Each layer: (center_x_offset, y_bottom, width, height, rotation_deg, shade_index)
tower_center = 9.6

# Build layers from bottom to top
layers = []
y_cur = 1.0
widths = [5.0, 4.6, 4.2, 3.6, 3.0, 2.5, 2.0, 1.6, 1.2, 0.9, 0.65, 0.45, 0.3]
heights = [0.7, 0.65, 0.6, 0.6, 0.55, 0.5, 0.5, 0.45, 0.4, 0.35, 0.3, 0.28, 0.25]

# Increasing tilt as we go up
tilts = [0, 0.02, 0.04, 0.06, 0.1, 0.14, 0.18, 0.24, 0.32, 0.4, 0.5, 0.6, 0.7]
x_drift = 0.0

for i, (w, h, tilt) in enumerate(zip(widths, heights, tilts)):
    # Each layer is composed of multiple small blocks
    n_blocks = max(2, int(w / 0.4))
    block_w = w / n_blocks

    x_drift += tilt * 0.15  # cumulative drift to create leaning effect

    for j in range(n_blocks):
        bx = tower_center + x_drift - w / 2 + j * block_w
        by = y_cur
        bw = block_w * np.random.uniform(0.85, 1.0)
        bh = h * np.random.uniform(0.7, 1.0)

        # Color: pick from cyan shades with some randomness
        shade_idx = min(len(CYAN_SHADES) - 1, max(0, i // 2 + np.random.randint(-1, 2)))
        color = CYAN_SHADES[shade_idx]
        alpha = np.random.uniform(0.4, 0.85)

        # Slight random offset for each block
        bx += np.random.uniform(-0.05, 0.05)
        by += np.random.uniform(-0.02, 0.02)

        rect = FancyBboxPatch(
            (bx, by), bw, bh,
            boxstyle="round,pad=0.02",
            facecolor=color, edgecolor=CYAN_SHADES[-1],
            linewidth=0.3, alpha=alpha
        )
        ax.add_patch(rect)

        # Some blocks get a "digital" grid pattern (small lines inside)
        if np.random.random() < 0.3:
            for k in range(3):
                lx = bx + bw * 0.15
                ly = by + bh * (0.2 + 0.25 * k)
                line_len = bw * np.random.uniform(0.3, 0.7)
                ax.plot([lx, lx + line_len], [ly, ly],
                       color=CYAN, linewidth=0.3, alpha=0.3)

    y_cur += h * 0.92  # slightly overlapping layers

# --- Labels embedded in tower ---
labels = [
    ('LLM', tower_center - 1.0, 2.2, 8),
    ('RLHF', tower_center + 0.8, 3.5, 7),
    ('RAG', tower_center - 0.5, 5.0, 7),
    ('Agent', tower_center + 0.6, 6.3, 6.5),
    ('MCP', tower_center + 0.3, 7.5, 5.5),
]
for text, lx, ly, size in labels:
    ax.text(lx, ly, text, fontsize=size, color=WHITE, alpha=0.35,
            fontfamily='monospace', fontweight='bold',
            ha='center', va='center', rotation=np.random.uniform(-5, 5))

# --- Glow / radiance around tower ---
# Radial glow using scatter
n_glow = 500
gx = np.random.normal(tower_center + x_drift * 0.5, 2.0, n_glow)
gy = np.random.normal(5.0, 2.5, n_glow)
gs = np.random.uniform(10, 60, n_glow)
ga = np.random.uniform(0.005, 0.03, n_glow)
ax.scatter(gx, gy, s=gs, color=CYAN, alpha=ga, edgecolors='none')

# Stronger glow at tower base
n_base = 200
bx_glow = np.random.normal(tower_center, 3.0, n_base)
by_glow = np.random.uniform(0.5, 1.5, n_base)
bs_glow = np.random.uniform(20, 80, n_base)
ba_glow = np.random.uniform(0.01, 0.04, n_base)
ax.scatter(bx_glow, by_glow, s=bs_glow, color=CYAN, alpha=ba_glow, edgecolors='none')

# --- Floating particles around tower top ---
n_particles = 60
px = np.random.normal(tower_center + x_drift, 1.5, n_particles)
py = np.random.normal(y_cur + 0.5, 1.0, n_particles)
ps = np.random.uniform(1, 8, n_particles)
pa = np.random.uniform(0.1, 0.5, n_particles)
ax.scatter(px, py, s=ps, color=ORANGE, alpha=pa, edgecolors='none')

# --- Small digital rain effect on sides ---
for _ in range(30):
    rx = np.random.choice([
        np.random.uniform(1, tower_center - 3),
        np.random.uniform(tower_center + 3, 18)
    ])
    ry = np.random.uniform(1.5, 9)
    length = np.random.uniform(0.3, 1.0)
    ax.plot([rx, rx], [ry, ry - length], color=CYAN, linewidth=0.3,
            alpha=np.random.uniform(0.05, 0.2))

out = Path('/Users/mik/strange LLM/assets/diagrams/rendered/cover_babel_tower.png')
fig.savefig(out, dpi=150, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
plt.close()
print(f"Saved: {out}")
