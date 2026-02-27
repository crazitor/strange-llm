"""P88 - Human standing beside the tower (finale image)"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from pathlib import Path
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle
from matplotlib.lines import Line2D

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
BG_BOTTOM = '#141E36'
CYAN = '#00D4AA'
ORANGE = '#FF6B35'
WHITE = '#FFFFFF'
DIM = '#6B7280'

# Cyan gradient for tower layers (bottom=darker, top=lighter)
TOWER_COLORS = ['#003D30', '#004D3D', '#006050', '#007D65',
                '#009B7D', '#00B894', '#00D4AA', '#00E8BC']

fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=150, facecolor=BG)
ax.set_xlim(0, 19.2)
ax.set_ylim(0, 10.8)
ax.set_aspect('equal')
ax.axis('off')

# --- Background gradient (bottom lighter, top darker) ---
gradient = np.zeros((256, 1, 4))
for i in range(256):
    t = i / 255.0
    # Bottom: slightly brighter (#141E36), top: darker (#0A0F1E)
    r = 0.08 * (1 - t) + 0.04 * t
    g = 0.12 * (1 - t) + 0.06 * t
    b = 0.21 * (1 - t) + 0.12 * t
    gradient[i, 0] = [r, g, b, 1.0]
ax.imshow(gradient, extent=[0, 19.2, 0, 10.8], aspect='auto', zorder=0)

# --- Ground / horizon line ---
ground_y = 1.5
ax.plot([0, 19.2], [ground_y, ground_y], color=DIM, linewidth=0.6, alpha=0.4)
# Ground glow (subtle)
for i in range(3):
    alpha = 0.008 * (3 - i)
    ax.fill_between([0, 19.2], [ground_y - 0.15 * (i + 1)] * 2,
                    [ground_y] * 2, color=CYAN, alpha=alpha)

# --- Tower (right side) ---
tower_center_x = 12.5
tower_y = ground_y

# Tower layers: from bottom (widest) to top (narrowest)
layer_widths =  [3.8, 3.4, 3.0, 2.5, 2.0, 1.5, 1.0, 0.6]
layer_heights = [1.0, 0.95, 0.9, 0.85, 0.8, 0.7, 0.6, 0.45]

y_cur = tower_y
np.random.seed(123)

for i, (w, h) in enumerate(zip(layer_widths, layer_heights)):
    # Main block for this layer
    color = TOWER_COLORS[min(i, len(TOWER_COLORS) - 1)]
    alpha = 0.7 + 0.03 * i

    # Slight horizontal offset for upper layers (instability)
    x_offset = sum([0.03 * j for j in range(i)])

    x = tower_center_x + x_offset - w / 2
    y = y_cur

    # Each layer is made of 2-3 sub-blocks
    n_sub = max(2, int(w / 1.2))
    sub_w = w / n_sub
    for j in range(n_sub):
        sx = x + j * sub_w + np.random.uniform(-0.03, 0.03)
        sw = sub_w * np.random.uniform(0.92, 1.0)
        sh = h * np.random.uniform(0.85, 1.0)

        block = FancyBboxPatch(
            (sx, y), sw, sh,
            boxstyle="round,pad=0.03",
            facecolor=color, edgecolor=TOWER_COLORS[-1],
            linewidth=0.5, alpha=alpha
        )
        ax.add_patch(block)

    y_cur += h * 0.93

tower_top = y_cur

# Tower glow
n_glow = 300
gx = np.random.normal(tower_center_x, 1.8, n_glow)
gy = np.random.normal((tower_top + tower_y) / 2, 2.5, n_glow)
gs = np.random.uniform(20, 100, n_glow)
ga = np.random.uniform(0.005, 0.025, n_glow)
ax.scatter(gx, gy, s=gs, color=CYAN, alpha=ga, edgecolors='none', zorder=1)

# --- Human figure (left side, small) ---
human_x = 5.5
human_y = ground_y

# Scale: person is about 10% of image height = ~1.08 units
person_h = 1.08
head_r = 0.1

# Head
head = Circle((human_x, human_y + person_h), head_r,
              facecolor=WHITE, edgecolor=WHITE, linewidth=1.5, alpha=0.9)
ax.add_patch(head)

# Body
ax.plot([human_x, human_x], [human_y + person_h - head_r, human_y + 0.4],
        color=WHITE, linewidth=2, alpha=0.9, solid_capstyle='round')

# Arms (slightly raised, looking up)
ax.plot([human_x - 0.2, human_x, human_x + 0.2],
        [human_y + 0.65, human_y + 0.75, human_y + 0.65],
        color=WHITE, linewidth=1.5, alpha=0.9, solid_capstyle='round')

# Legs
ax.plot([human_x, human_x - 0.15], [human_y + 0.4, human_y],
        color=WHITE, linewidth=2, alpha=0.9, solid_capstyle='round')
ax.plot([human_x, human_x + 0.15], [human_y + 0.4, human_y],
        color=WHITE, linewidth=2, alpha=0.9, solid_capstyle='round')

# --- Light point beside the human (power of choice) ---
light_x = human_x + 0.35
light_y = human_y + 0.85

# Glow layers (outer to inner)
for r, a in [(0.3, 0.03), (0.2, 0.06), (0.12, 0.1), (0.06, 0.2)]:
    glow = Circle((light_x, light_y), r,
                  facecolor=ORANGE, edgecolor='none', alpha=a)
    ax.add_patch(glow)

# Core bright point
core = Circle((light_x, light_y), 0.025,
              facecolor='#FFD700', edgecolor='none', alpha=0.95)
ax.add_patch(core)

# Light rays
for angle in np.linspace(0, 2 * np.pi, 8, endpoint=False):
    ray_len = 0.15
    rx = light_x + ray_len * np.cos(angle)
    ry = light_y + ray_len * np.sin(angle)
    ax.plot([light_x, rx], [light_y, ry],
            color=ORANGE, linewidth=0.5, alpha=0.3)

# --- Gaze line (human looking up at tower) ---
# Subtle dotted line from person's head to tower top
ax.plot([human_x + 0.1, tower_center_x - 0.5],
        [human_y + person_h + 0.1, tower_top - 0.3],
        color=DIM, linewidth=0.4, linestyle='dotted', alpha=0.2)

# --- Ambient stars ---
np.random.seed(77)
n_stars = 150
sx = np.random.uniform(0, 19.2, n_stars)
sy = np.random.uniform(4, 10.8, n_stars)
ss = np.random.uniform(0.3, 1.5, n_stars)
sa = np.random.uniform(0.1, 0.4, n_stars)
for i in range(n_stars):
    ax.plot(sx[i], sy[i], '.', color=WHITE, markersize=ss[i], alpha=sa[i], zorder=2)

# --- Floating particles near tower top ---
n_particles = 30
px = np.random.normal(tower_center_x + 0.3, 1.0, n_particles)
py = np.random.normal(tower_top + 0.5, 0.8, n_particles)
ps = np.random.uniform(1, 5, n_particles)
pa = np.random.uniform(0.1, 0.4, n_particles)
ax.scatter(px, py, s=ps, color=CYAN, alpha=pa, edgecolors='none', zorder=3)

out = Path('/Users/mik/strange LLM/assets/diagrams/rendered/human_beside_tower.png')
fig.savefig(out, dpi=150, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
plt.close()
print(f"Saved: {out}")
