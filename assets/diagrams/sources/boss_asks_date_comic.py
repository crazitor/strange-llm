"""P27 - Boss asks 'what date is it?' comic strip"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from pathlib import Path
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrowPatch
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
PANEL_BG = '#1A2340'
BUBBLE_BG = '#1E2A42'

fig = plt.figure(figsize=(19.2, 10.8), dpi=150, facecolor=BG)

# Title
fig.text(0.5, 0.94, '当你让Agent查今天几号', fontsize=32, color=WHITE,
         ha='center', va='center', fontweight='bold')

def draw_person(ax, x, y, scale=1.0, color=WHITE):
    """Draw a simple stick figure person (boss)."""
    s = scale
    # Head
    head = Circle((x, y + 0.35 * s), 0.12 * s, facecolor='none',
                  edgecolor=color, linewidth=2)
    ax.add_patch(head)
    # Body
    ax.plot([x, x], [y + 0.23 * s, y - 0.1 * s], color=color, linewidth=2)
    # Arms
    ax.plot([x - 0.15 * s, x + 0.15 * s], [y + 0.12 * s, y + 0.12 * s],
            color=color, linewidth=2)
    # Legs
    ax.plot([x, x - 0.1 * s], [y - 0.1 * s, y - 0.3 * s], color=color, linewidth=2)
    ax.plot([x, x + 0.1 * s], [y - 0.1 * s, y - 0.3 * s], color=color, linewidth=2)

def draw_robot(ax, x, y, scale=1.0, color=CYAN):
    """Draw a simple robot (Agent)."""
    s = scale
    # Head (square)
    head = FancyBboxPatch((x - 0.1 * s, y + 0.22 * s), 0.2 * s, 0.18 * s,
                          boxstyle="round,pad=0.02",
                          facecolor='none', edgecolor=color, linewidth=2)
    ax.add_patch(head)
    # Eyes
    ax.plot(x - 0.04 * s, y + 0.33 * s, 'o', color=color, markersize=3)
    ax.plot(x + 0.04 * s, y + 0.33 * s, 'o', color=color, markersize=3)
    # Antenna
    ax.plot([x, x], [y + 0.40 * s, y + 0.48 * s], color=color, linewidth=1.5)
    ax.plot(x, y + 0.50 * s, 'o', color=ORANGE, markersize=4)
    # Body (rectangle)
    body = FancyBboxPatch((x - 0.12 * s, y - 0.08 * s), 0.24 * s, 0.30 * s,
                          boxstyle="round,pad=0.02",
                          facecolor='none', edgecolor=color, linewidth=2)
    ax.add_patch(body)
    # Legs
    ax.plot([x - 0.06 * s, x - 0.06 * s], [y - 0.08 * s, y - 0.25 * s],
            color=color, linewidth=2)
    ax.plot([x + 0.06 * s, x + 0.06 * s], [y - 0.08 * s, y - 0.25 * s],
            color=color, linewidth=2)

def draw_speech_bubble(ax, x, y, text, width=0.6, height=0.25, fontsize=11,
                       text_color=WHITE, bg_color=BUBBLE_BG, tail_dir='down'):
    """Draw a speech bubble with text."""
    bubble = FancyBboxPatch((x - width / 2, y - height / 2), width, height,
                            boxstyle="round,pad=0.04",
                            facecolor=bg_color, edgecolor=DIM, linewidth=1.5)
    ax.add_patch(bubble)
    # Tail (small triangle)
    if tail_dir == 'down':
        tail = plt.Polygon([
            [x - 0.03, y - height / 2],
            [x + 0.03, y - height / 2],
            [x, y - height / 2 - 0.08]
        ], facecolor=bg_color, edgecolor=DIM, linewidth=1)
        ax.add_patch(tail)
    ax.text(x, y, text, fontsize=fontsize, color=text_color,
            ha='center', va='center', wrap=True)

# --- 6 panels: 2 rows x 3 columns ---
panel_coords = [
    (0.03, 0.48, 0.30, 0.38),   # row1 col1
    (0.35, 0.48, 0.30, 0.38),   # row1 col2
    (0.67, 0.48, 0.30, 0.38),   # row1 col3
    (0.03, 0.08, 0.30, 0.38),   # row2 col1
    (0.35, 0.08, 0.30, 0.38),   # row2 col2
    (0.67, 0.08, 0.30, 0.38),   # row2 col3
]

panel_labels = [
    '1', '2', '3', '4', '5', '6'
]

# Create all axes
axes = []
for i, (px, py, pw, ph) in enumerate(panel_coords):
    ax = fig.add_axes([px, py, pw, ph])
    ax.set_facecolor(PANEL_BG)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-0.7, 0.7)
    ax.set_aspect('equal')
    ax.axis('off')
    # Panel border
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color(DIM)
        spine.set_linewidth(1)
    # Panel number
    ax.text(-0.92, 0.58, panel_labels[i], fontsize=12, color=DIM,
            ha='left', va='top', fontweight='bold')
    axes.append(ax)

# --- Panel 1: Boss asks ---
ax = axes[0]
draw_person(ax, -0.3, -0.1, scale=1.2, color=WHITE)
ax.text(-0.3, -0.55, '老板', fontsize=10, color=DIM, ha='center')
draw_speech_bubble(ax, 0.25, 0.38, '今天几号？', width=0.65, height=0.22,
                   fontsize=14, text_color=WHITE)

# --- Panel 2: Agent receives ---
ax = axes[1]
draw_robot(ax, 0, -0.05, scale=1.2, color=CYAN)
ax.text(0, 0.6, '启动分析...', fontsize=13, color=ORANGE,
        ha='center', fontweight='bold', style='italic')
# thinking dots
for dx in [-0.15, 0, 0.15]:
    ax.plot(dx, 0.48, 'o', color=ORANGE, markersize=3, alpha=0.6)

# --- Panel 3: Agent calls tools ---
ax = axes[2]
draw_robot(ax, -0.55, -0.15, scale=0.8, color=CYAN)
# Tool call list
tools = ['搜索引擎', '日历API', '天气API', '新闻API', '数据库']
for i, tool in enumerate(tools):
    yy = 0.45 - i * 0.2
    # Arrow from robot
    ax.annotate('', xy=(0.0, yy), xytext=(-0.3, yy),
                arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.2))
    box = FancyBboxPatch((0.0, yy - 0.07), 0.65, 0.14,
                         boxstyle="round,pad=0.03",
                         facecolor=GRID, edgecolor=CYAN, linewidth=1, alpha=0.8)
    ax.add_patch(box)
    ax.text(0.32, yy, tool, fontsize=9, color=CYAN, ha='center', va='center')

ax.text(0.3, -0.6, '疯狂调用...', fontsize=10, color=ORANGE, ha='center',
        style='italic')

# --- Panel 4: Agent generates report ---
ax = axes[3]
# Report document
report = FancyBboxPatch((-0.5, -0.5), 1.0, 0.9,
                        boxstyle="round,pad=0.04",
                        facecolor=GRID, edgecolor=DIM, linewidth=1.5)
ax.add_patch(report)
ax.text(0, 0.28, '综合分析报告', fontsize=13, color=WHITE,
        ha='center', fontweight='bold')
# Fake lines of text
for i in range(6):
    yy = 0.12 - i * 0.1
    width = 0.7 if i < 5 else 0.3
    ax.plot([-width/2, width/2], [yy, yy], color=DIM, linewidth=1.5, alpha=0.5)

ax.text(0, -0.52, '（共2000字）', fontsize=10, color=DIM, ha='center')

# Cost label
cost_box = FancyBboxPatch((0.3, -0.65), 0.6, 0.18,
                          boxstyle="round,pad=0.03",
                          facecolor='#3D1515', edgecolor=ORANGE, linewidth=1.5)
ax.add_patch(cost_box)
ax.text(0.6, -0.56, 'Token: $0.50', fontsize=10, color=ORANGE,
        ha='center', va='center', fontweight='bold')

# --- Panel 5: Boss confused ---
ax = axes[4]
draw_person(ax, -0.3, -0.1, scale=1.2, color=WHITE)
ax.text(-0.3, -0.55, '老板', fontsize=10, color=DIM, ha='center')
draw_speech_bubble(ax, 0.3, 0.38, '...我只是想\n知道几号', width=0.7, height=0.28,
                   fontsize=12, text_color=ORANGE)
# Confusion marks
ax.text(-0.05, 0.25, '？', fontsize=24, color=ORANGE, ha='center',
        fontweight='bold', alpha=0.6)
ax.text(-0.55, 0.5, '？', fontsize=16, color=ORANGE, ha='center',
        fontweight='bold', alpha=0.4)

# --- Panel 6: Just look at the calendar ---
ax = axes[5]
# Calendar
cal = FancyBboxPatch((-0.35, -0.2), 0.7, 0.65,
                     boxstyle="round,pad=0.04",
                     facecolor=GRID, edgecolor=CYAN, linewidth=2)
ax.add_patch(cal)
# Calendar header
cal_header = FancyBboxPatch((-0.35, 0.32), 0.7, 0.13,
                            boxstyle="round,pad=0.02",
                            facecolor=CYAN, edgecolor=CYAN, linewidth=1)
ax.add_patch(cal_header)
ax.text(0, 0.385, '2月', fontsize=12, color=BG, ha='center',
        va='center', fontweight='bold')
ax.text(0, 0.1, '13', fontsize=40, color=WHITE, ha='center',
        va='center', fontweight='bold')

ax.text(0, -0.45, '直接看日历就行', fontsize=12, color=CYAN,
        ha='center', fontweight='bold')
ax.text(0, -0.6, '费用: $0.00', fontsize=10, color=CYAN,
        ha='center', alpha=0.7)

out = Path('/Users/mik/strange LLM/assets/diagrams/rendered/boss_asks_date_comic.png')
fig.savefig(out, dpi=150, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
plt.close()
print(f"Saved: {out}")
