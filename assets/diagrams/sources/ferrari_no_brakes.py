"""P28 - Ferrari with No Brakes"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from pathlib import Path
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Polygon, FancyArrowPatch, Arc
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
RED = '#FF3B3B'
DARK_RED = '#8B0000'

fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=150, facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 19.2)
ax.set_ylim(0, 10.8)
ax.set_aspect('equal')
ax.axis('off')

# --- Title ---
ax.text(9.6, 10.0, '没有刹车的法拉利', fontsize=38, color=WHITE,
        ha='center', va='center', fontweight='bold')

# --- Road surface (left portion) ---
road_y = 5.0
road_thickness = 0.3
# Main road
road = FancyBboxPatch((0.5, road_y - road_thickness / 2), 10.5, road_thickness,
                      boxstyle="square,pad=0",
                      facecolor='#2A2A3A', edgecolor='none')
ax.add_patch(road)

# Road markings (dashed center line)
for i in range(12):
    mx = 1.0 + i * 0.9
    ax.plot([mx, mx + 0.5], [road_y, road_y], color='#FFD700',
            linewidth=1.5, alpha=0.6)

# Road labels: "dialogue rounds"
for i in range(6):
    x = 1.5 + i * 1.6
    ax.text(x, road_y - 0.5, f'第{i+1}轮', fontsize=8, color=DIM,
            ha='center', va='center')

# --- Cliff edge ---
cliff_x = 11.0
# Road ends abruptly
ax.plot([cliff_x, cliff_x], [road_y - 0.15, road_y + 0.15],
        color=RED, linewidth=3)

# Cliff face (right side drops down)
cliff_points = np.array([
    [cliff_x, road_y - 0.15],
    [cliff_x + 0.3, road_y - 0.5],
    [cliff_x + 0.5, road_y - 1.5],
    [cliff_x + 0.8, road_y - 2.8],
    [cliff_x + 1.2, road_y - 2.8],
    [cliff_x + 1.2, road_y - 0.15],
])
# Don't fill - draw jagged cliff edge
cliff_xs = [cliff_x, cliff_x + 0.1, cliff_x + 0.25, cliff_x + 0.15,
            cliff_x + 0.4, cliff_x + 0.35, cliff_x + 0.6, cliff_x + 0.5,
            cliff_x + 0.8]
cliff_ys = [road_y - 0.15, road_y - 0.6, road_y - 0.9, road_y - 1.3,
            road_y - 1.6, road_y - 2.0, road_y - 2.3, road_y - 2.7,
            road_y - 3.0]
ax.plot(cliff_xs, cliff_ys, color=DIM, linewidth=2, alpha=0.7)

# More cliff texture
for i in range(5):
    cx = cliff_x + np.random.uniform(0.05, 0.6)
    cy = road_y - 0.5 - i * 0.5
    ax.plot([cx, cx + 0.15], [cy, cy - 0.2], color=DIM, linewidth=0.8, alpha=0.4)

# Abyss at bottom
ax.text(cliff_x + 1.8, road_y - 2.5, '灾难性输出', fontsize=16, color=RED,
        ha='center', va='center', fontweight='bold', rotation=-30)

# Danger particles falling
for _ in range(15):
    px = cliff_x + np.random.uniform(0.1, 1.5)
    py = road_y - np.random.uniform(0.5, 3.0)
    ax.plot(px, py, '.', color=RED, markersize=np.random.uniform(1, 4),
            alpha=np.random.uniform(0.2, 0.6))

# --- Gap in road (the break) ---
# Small road section after cliff (unreachable)
road2 = FancyBboxPatch((cliff_x + 2.5, road_y - road_thickness / 2), 6, road_thickness,
                       boxstyle="square,pad=0",
                       facecolor='#2A2A3A', edgecolor='none', alpha=0.3)
ax.add_patch(road2)
ax.text(cliff_x + 5.5, road_y, '...', fontsize=20, color=DIM, ha='center', va='center')

# --- Car (geometric sports car) ---
car_x = 7.5  # front of car
car_y = road_y + road_thickness / 2

# Car body - sleek shape using polygon
body_points = np.array([
    [car_x - 2.5, car_y],         # rear bottom
    [car_x - 2.5, car_y + 0.5],   # rear top
    [car_x - 2.0, car_y + 0.8],   # rear roof
    [car_x - 1.0, car_y + 0.9],   # roof peak
    [car_x - 0.3, car_y + 0.6],   # windshield
    [car_x, car_y + 0.3],         # hood front
    [car_x + 0.3, car_y + 0.15],  # nose
    [car_x + 0.3, car_y],         # front bottom
])
body = Polygon(body_points, closed=True, facecolor='#CC0000',
               edgecolor='#FF1111', linewidth=1.5)
ax.add_patch(body)

# Car detail: window
window_points = np.array([
    [car_x - 1.8, car_y + 0.55],
    [car_x - 1.0, car_y + 0.85],
    [car_x - 0.4, car_y + 0.58],
    [car_x - 0.6, car_y + 0.5],
])
window = Polygon(window_points, closed=True, facecolor='#1A2340',
                 edgecolor='#FF3333', linewidth=0.8)
ax.add_patch(window)

# Wheels
wheel1_x = car_x - 1.8
wheel2_x = car_x - 0.3
wheel_r = 0.22
for wx in [wheel1_x, wheel2_x]:
    wheel = Circle((wx, car_y - 0.05), wheel_r, facecolor='#1A1A2E',
                   edgecolor=DIM, linewidth=2)
    ax.add_patch(wheel)
    # Hubcap
    hub = Circle((wx, car_y - 0.05), wheel_r * 0.4, facecolor='none',
                 edgecolor=DIM, linewidth=1)
    ax.add_patch(hub)

# --- Speed lines ---
for i in range(8):
    sy = car_y + 0.1 + np.random.uniform(-0.3, 0.8)
    sx_start = car_x - 2.8 - np.random.uniform(0.5, 2.0)
    sx_end = car_x - 2.8 - np.random.uniform(2.5, 5.0)
    alpha = np.random.uniform(0.2, 0.6)
    ax.plot([sx_start, sx_end], [sy, sy], color=ORANGE, linewidth=1.5, alpha=alpha)

# Exhaust flames
flame_points = np.array([
    [car_x - 2.5, car_y + 0.1],
    [car_x - 3.2, car_y + 0.25],
    [car_x - 2.8, car_y + 0.15],
    [car_x - 3.5, car_y + 0.2],
    [car_x - 3.0, car_y + 0.05],
    [car_x - 3.3, car_y],
    [car_x - 2.5, car_y + 0.0],
])
flame = Polygon(flame_points, closed=True, facecolor=ORANGE,
                edgecolor='#FF9500', linewidth=1, alpha=0.7)
ax.add_patch(flame)

# --- Labels ---
# "500 HP" label above car
ax.text(car_x - 1.2, car_y + 1.5, '500匹马力', fontsize=22, color=CYAN,
        ha='center', va='center', fontweight='bold')
ax.annotate('', xy=(car_x - 1.2, car_y + 1.0),
            xytext=(car_x - 1.2, car_y + 1.3),
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=2))

# "0 brakes" label below car
ax.text(car_x - 1.2, road_y - 1.2, '0 刹车', fontsize=22, color=RED,
        ha='center', va='center', fontweight='bold')
ax.annotate('', xy=(car_x - 1.2, road_y - 0.3),
            xytext=(car_x - 1.2, road_y - 0.9),
            arrowprops=dict(arrowstyle='->', color=RED, lw=2))

# Brake cross-out symbol
ax.plot([car_x - 1.7, car_x - 0.7], [road_y - 1.0, road_y - 1.4],
        color=RED, linewidth=1.5, alpha=0.4)
ax.plot([car_x - 1.7, car_x - 0.7], [road_y - 1.4, road_y - 1.0],
        color=RED, linewidth=1.5, alpha=0.4)

# --- Warning sign near cliff ---
# Triangle warning sign
tri_x, tri_y = cliff_x - 0.8, road_y + 1.5
tri_size = 0.4
tri_points = np.array([
    [tri_x, tri_y + tri_size],
    [tri_x - tri_size * 0.8, tri_y - tri_size * 0.4],
    [tri_x + tri_size * 0.8, tri_y - tri_size * 0.4],
])
tri = Polygon(tri_points, closed=True, facecolor=ORANGE,
              edgecolor=WHITE, linewidth=2)
ax.add_patch(tri)
ax.text(tri_x, tri_y, '!', fontsize=18, color=BG, ha='center',
        va='center', fontweight='bold')

# --- Bottom text ---
ax.text(9.6, 0.8, '能力再强，没有止损也是灾难', fontsize=22, color=DIM,
        ha='center', va='center', style='italic')

out = Path('/Users/mik/strange LLM/assets/diagrams/rendered/ferrari_no_brakes.png')
fig.savefig(out, dpi=150, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
plt.close()
print(f"Saved: {out}")
