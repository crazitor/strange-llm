import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patheffects as pe
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Polygon, Wedge
from matplotlib.path import Path
import matplotlib.path as mpath

# ── Theme ──
BG       = '#0F1729'
PRIMARY  = '#00D4AA'
ACCENT   = '#FF6B35'
WHITE    = '#FFFFFF'
DIM      = '#6B7280'

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'STHeiti', 'SimHei', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(19.2, 10.8))
fig.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 56.25)
ax.set_aspect('equal')
ax.axis('off')

# ══════════════════════════════════════
# ORIGIN NODE — "现在"
# ══════════════════════════════════════
origin_x, origin_y = 50, 8

# Glow behind origin
for r, a in [(5, 0.03), (3.5, 0.05), (2, 0.08)]:
    glow = Circle((origin_x, origin_y), r, facecolor=WHITE, edgecolor='none', alpha=a, zorder=1)
    ax.add_patch(glow)

# Main node
node = Circle((origin_x, origin_y), 1.8, facecolor=WHITE, edgecolor=WHITE,
              linewidth=2, alpha=0.9, zorder=10)
ax.add_patch(node)
ax.text(origin_x, origin_y, '现在', fontsize=14, color=BG, fontweight='bold',
        ha='center', va='center', zorder=11)

# ══════════════════════════════════════
# PATH DEFINITIONS
# ══════════════════════════════════════
paths_data = [
    {
        'color': PRIMARY,
        'end_x': 16, 'end_y': 42,
        'ctrl_x': 35, 'ctrl_y': 26,
        'title': '路径A：架构突破',
        'subtitle': '补丁之塔被推倒重建',
        'title_offset_y': 8,
        'sub_offset_y': 5,
    },
    {
        'color': WHITE,
        'end_x': 50, 'end_y': 44,
        'ctrl_x': 50, 'ctrl_y': 28,
        'title': '路径B：生态重构',
        'subtitle': '不是更强，而是更便宜更普遍',
        'title_offset_y': 8,
        'sub_offset_y': 5,
    },
    {
        'color': ACCENT,
        'end_x': 84, 'end_y': 42,
        'ctrl_x': 65, 'ctrl_y': 26,
        'title': '路径C：融合共生',
        'subtitle': '人机协作新范式',
        'title_offset_y': 8,
        'sub_offset_y': 5,
    },
]

for pd in paths_data:
    color = pd['color']
    ex, ey = pd['end_x'], pd['end_y']
    cx, cy = pd['ctrl_x'], pd['ctrl_y']

    # Draw bezier path
    t_vals = np.linspace(0, 1, 120)
    bx = (1 - t_vals)**2 * origin_x + 2 * (1 - t_vals) * t_vals * cx + t_vals**2 * ex
    by = (1 - t_vals)**2 * origin_y + 2 * (1 - t_vals) * t_vals * cy + t_vals**2 * ey

    # Glow trail
    ax.plot(bx, by, color=color, linewidth=8, alpha=0.08, zorder=3)
    ax.plot(bx, by, color=color, linewidth=4, alpha=0.15, zorder=4)
    # Main line
    ax.plot(bx, by, color=color, linewidth=2.5, alpha=0.8, zorder=5)

    # Arrowhead at the end
    # Direction at end of curve: derivative of quadratic bezier at t=1
    dx = 2 * (ex - cx)
    dy = 2 * (ey - cy)
    length = np.sqrt(dx**2 + dy**2)
    dx /= length
    dy /= length
    arrow_size = 2.0
    # Triangle arrowhead
    tip_x, tip_y = ex + dx * 1.0, ey + dy * 1.0
    left_x = tip_x - arrow_size * dx + arrow_size * 0.4 * dy
    left_y = tip_y - arrow_size * dy - arrow_size * 0.4 * dx
    right_x = tip_x - arrow_size * dx - arrow_size * 0.4 * dy
    right_y = tip_y - arrow_size * dy + arrow_size * 0.4 * dx
    arrow_tri = Polygon([(tip_x, tip_y), (left_x, left_y), (right_x, right_y)],
                        closed=True, facecolor=color, edgecolor='none', alpha=0.9, zorder=6)
    ax.add_patch(arrow_tri)

    # Question mark / open circle at the end (future uncertainty)
    end_cx = tip_x + dx * 2.5
    end_cy = tip_y + dy * 2.5
    # Open ring
    ring = Circle((end_cx, end_cy), 1.5, facecolor='none', edgecolor=color,
                  linewidth=2.5, alpha=0.7, linestyle='--', zorder=7)
    ax.add_patch(ring)
    ax.text(end_cx, end_cy, '?', fontsize=18, color=color, fontweight='bold',
            ha='center', va='center', alpha=0.8, zorder=8)

    # Title — placed above the question-mark circle
    ax.text(pd['end_x'], pd['end_y'] + pd['title_offset_y'], pd['title'],
            fontsize=18, color=color, fontweight='bold',
            ha='center', va='center', zorder=10,
            path_effects=[pe.withStroke(linewidth=4, foreground=BG)])

    # Subtitle
    ax.text(pd['end_x'], pd['end_y'] + pd['sub_offset_y'], pd['subtitle'],
            fontsize=13, color=DIM, ha='center', va='center',
            fontweight='bold', zorder=10,
            path_effects=[pe.withStroke(linewidth=3, foreground=BG)])

# ══════════════════════════════════════
# PARTICLE EFFECTS along paths
# ══════════════════════════════════════
np.random.seed(7)
for pd in paths_data:
    color = pd['color']
    ex, ey = pd['end_x'], pd['end_y']
    cx, cy = pd['ctrl_x'], pd['ctrl_y']
    for _ in range(15):
        t = np.random.uniform(0.15, 0.85)
        px = (1 - t)**2 * origin_x + 2 * (1 - t) * t * cx + t**2 * ex
        py = (1 - t)**2 * origin_y + 2 * (1 - t) * t * cy + t**2 * ey
        px += np.random.uniform(-1.5, 1.5)
        py += np.random.uniform(-1.5, 1.5)
        size = np.random.uniform(0.1, 0.4)
        alpha = np.random.uniform(0.1, 0.35)
        dot = Circle((px, py), size, facecolor=color, edgecolor='none', alpha=alpha, zorder=3)
        ax.add_patch(dot)

# ══════════════════════════════════════
# BOTTOM ANNOTATION
# ══════════════════════════════════════
ax.text(50, 2, '理解结构、找到边界、做出选择', fontsize=20, color=WHITE,
        ha='center', va='center', fontweight='bold', zorder=10,
        path_effects=[pe.withStroke(linewidth=4, foreground=BG)])

# ══════════════════════════════════════
# DECORATIVE: spreading lines from origin
# ══════════════════════════════════════
for angle in np.linspace(-0.15, np.pi + 0.15, 40):
    length = np.random.uniform(1.5, 3.5)
    lx = origin_x + 2.5 * np.cos(angle)
    ly = origin_y + 2.5 * np.sin(angle)
    ex2 = lx + length * np.cos(angle)
    ey2 = ly + length * np.sin(angle)
    ax.plot([lx, ex2], [ly, ey2], color=DIM, linewidth=0.5, alpha=0.2, zorder=2)

# ══════════════════════════════════════
# TOP TITLE
# ══════════════════════════════════════
ax.text(50, 55, '三条岔路', fontsize=16, color=DIM,
        ha='center', va='center', fontweight='bold', alpha=0.6, zorder=10,
        path_effects=[pe.withStroke(linewidth=3, foreground=BG)])

# ── Save ──
out = '/Users/mik/strange LLM/assets/diagrams/rendered/three_paths.png'
fig.savefig(out, dpi=100, facecolor=BG, edgecolor='none', bbox_inches='tight', pad_inches=0.3)
plt.close(fig)
print(f'Saved: {out}')
