"""
P69 - Constraint = Meaning (Philosophical core diagram)
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from pathlib import Path
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Arc
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
CYAN = '#00D4AA'
ORANGE = '#FF6B35'
WHITE = '#FFFFFF'
DIM = '#6B7280'
GRID = '#1E2A42'
RED = '#FF4444'

OUT = Path('/Users/mik/strange LLM/assets/diagrams/rendered/constraint_equals_meaning.png')

fig, (ax_left, ax_mid, ax_right) = plt.subplots(1, 3, figsize=(19.2, 10.8), dpi=150,
                                                  facecolor=BG,
                                                  gridspec_kw={'width_ratios': [4, 1.5, 4]})
for ax in [ax_left, ax_mid, ax_right]:
    ax.set_facecolor(BG)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

# === LEFT SIDE: Constraint = Curse ===
# Draw a circle being "chained"
circle_left = plt.Circle((0, 0.1), 0.55, fill=False, edgecolor=ORANGE,
                          linewidth=3, linestyle='-', zorder=5)
ax_left.add_patch(circle_left)

# Draw chain-like X lines across the circle
chain_angles = [30, 75, 120, 165, -30, -75, -120]
for angle in chain_angles:
    rad = np.radians(angle)
    x1 = 0.7 * np.cos(rad) + 0
    y1 = 0.7 * np.sin(rad) + 0.1
    x2 = -0.7 * np.cos(rad) + 0
    y2 = -0.7 * np.sin(rad) + 0.1
    ax_left.plot([x1, x2], [y1, y2], color=ORANGE, alpha=0.4, linewidth=2, zorder=3)

# Draw lock symbol (small filled circle)
lock = plt.Circle((0, -0.5), 0.08, fill=True, facecolor=ORANGE, edgecolor=ORANGE, zorder=6)
ax_left.add_patch(lock)
ax_left.plot([-0.06, -0.06, 0.06, 0.06], [-0.5, -0.38, -0.38, -0.5],
             color=ORANGE, linewidth=2.5, zorder=6)

# Labels
ax_left.text(0, 1.35, '约束 = 诅咒', fontsize=26, color=ORANGE, fontweight='bold',
             ha='center', va='center')
ax_left.text(0, -1.0, 'AI眼中的约束', fontsize=18, color=ORANGE, ha='center', alpha=0.9)
ax_left.text(0, -1.25, '"要消除的障碍"', fontsize=15, color=DIM, ha='center', style='italic')

# Sad face in circle
ax_left.text(0, 0.1, '', fontsize=40, ha='center', va='center', color=ORANGE, alpha=0.7)
# Draw simple sad face
ax_left.plot([-0.15, -0.15], [0.22, 0.22], 'o', color=ORANGE, markersize=6, zorder=7)
ax_left.plot([0.15, 0.15], [0.22, 0.22], 'o', color=ORANGE, markersize=6, zorder=7)
# Sad mouth
sad_x = np.linspace(-0.15, 0.15, 50)
sad_y = 0.03 * np.cos(np.linspace(0, np.pi, 50)) - 0.05 + 0.1
ax_left.plot(sad_x, sad_y, color=ORANGE, linewidth=2, zorder=7)


# === RIGHT SIDE: Constraint = Meaning ===
# Draw the same circle but constraints form a beautiful pattern
circle_right = plt.Circle((0, 0.1), 0.55, fill=False, edgecolor=CYAN,
                           linewidth=3, linestyle='-', zorder=5)
ax_right.add_patch(circle_right)

# Draw constraint lines forming a geometric star pattern (meaningful structure)
n_points = 7
star_angles = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
star_r = 0.5
star_pts = [(star_r * np.cos(a), star_r * np.sin(a) + 0.1) for a in star_angles]

for i in range(n_points):
    for j in range(i + 2, n_points):
        if abs(i - j) > 1 and abs(i - j) < n_points - 1:
            ax_right.plot([star_pts[i][0], star_pts[j][0]],
                          [star_pts[i][1], star_pts[j][1]],
                          color=CYAN, alpha=0.5, linewidth=1.8, zorder=3)

# Small dots at vertices
for pt in star_pts:
    dot = plt.Circle(pt, 0.035, fill=True, facecolor=CYAN, edgecolor=CYAN, zorder=6, alpha=0.8)
    ax_right.add_patch(dot)

# Glow effect: inner circle
glow = plt.Circle((0, 0.1), 0.55, fill=True, facecolor=CYAN, alpha=0.05, zorder=1)
ax_right.add_patch(glow)
glow2 = plt.Circle((0, 0.1), 0.45, fill=True, facecolor=CYAN, alpha=0.05, zorder=1)
ax_right.add_patch(glow2)

# Labels
ax_right.text(0, 1.35, '约束 = 意义', fontsize=26, color=CYAN, fontweight='bold',
              ha='center', va='center')
ax_right.text(0, -1.0, '人类眼中的约束', fontsize=18, color=CYAN, ha='center', alpha=0.9)
ax_right.text(0, -1.25, '"意义的来源"', fontsize=15, color=DIM, ha='center', style='italic')


# === MIDDLE: Transformation arrow ===
ax_mid.set_xlim(-2, 2)
ax_mid.set_ylim(-1.5, 1.5)

# Draw a big "!=" crossed out, replaced with "="
ax_mid.text(0, 0.5, '', fontsize=50, color=DIM, ha='center', va='center', alpha=0.4)
# Draw arrow showing transformation
ax_mid.annotate('', xy=(1.2, 0.1), xytext=(-1.2, 0.1),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=3, alpha=0.6),
                zorder=5)
ax_mid.text(0, 0.55, '', fontsize=45, color=RED, ha='center', va='center', alpha=0.35,
            fontweight='bold')
ax_mid.text(0, -0.15, '=', fontsize=55, color=WHITE, ha='center', va='center',
            fontweight='bold', alpha=0.9)
ax_mid.text(0, -0.7, '重新理解', fontsize=14, color=DIM, ha='center')

# Title
fig.suptitle('约束的两副面孔',
             fontsize=32, color=WHITE, fontweight='bold', y=0.96)

# Bottom quote
fig.text(0.5, 0.03, '有限的选择，才是人的终极武器',
         fontsize=22, color=CYAN, ha='center', fontweight='bold',
         style='italic')

fig.savefig(OUT, dpi=150, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
plt.close()
print(f'Saved: {OUT}')
