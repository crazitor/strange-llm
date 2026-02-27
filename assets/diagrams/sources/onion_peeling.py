"""P10 - Three-panel onion peeling: Agent -> Workflow -> While Loop"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from pathlib import Path
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch

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

fig = plt.figure(figsize=(19.2, 10.8), dpi=150, facecolor=BG)

# Title
fig.text(0.5, 0.93, '剥洋葱 \u2014 Agent的本质', fontsize=36, color=WHITE,
         ha='center', va='center', fontweight='bold')

# Subtitle at bottom
fig.text(0.5, 0.06, '从华丽术语到朴素真相', fontsize=20, color=DIM,
         ha='center', va='center')

# Create 3 subplots
axes = []
for i in range(3):
    ax = fig.add_axes([0.05 + i * 0.30, 0.15, 0.28, 0.70])
    ax.set_facecolor(BG)
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.8, 2.8)
    ax.set_aspect('equal')
    ax.axis('off')
    axes.append(ax)

# Onion layers: radii and colors
layer_specs = [
    (1.8, '#005F4E', 'Agent',     22),   # outer
    (1.2, '#007D65', 'Workflow',  16),   # middle
    (0.6, '#00D4AA', 'While Loop\n+ LLM', 11),  # core
]

# --- Panel 1: Full onion ---
ax = axes[0]
for radius, color, label, fontsize in layer_specs:
    circle = Circle((0, 0), radius, facecolor=color, edgecolor=CYAN,
                    linewidth=2, alpha=0.85)
    ax.add_patch(circle)

# Label only the outer layer
ax.text(0, 0, 'Agent', fontsize=28, color=WHITE, ha='center', va='center',
        fontweight='bold')
ax.text(0, -2.4, '"看起来很厉害"', fontsize=14, color=DIM, ha='center', va='center',
        style='italic')

# --- Panel 2: Outer layer peeled ---
ax = axes[1]
# Outer layer: dashed, transparent
circle_outer = Circle((0, 0), 1.8, facecolor='none', edgecolor=DIM,
                      linewidth=2, linestyle='dashed', alpha=0.4)
ax.add_patch(circle_outer)
# Peeled fragments on the side
for angle in [30, 60, 120]:
    rad = np.radians(angle)
    fx = 2.0 * np.cos(rad)
    fy = 2.0 * np.sin(rad)
    frag = mpatches.Arc((fx, fy), 0.5, 0.3, angle=angle,
                        theta1=0, theta2=180,
                        edgecolor=DIM, linewidth=1.5, alpha=0.3)
    ax.add_patch(frag)

# Middle and inner layers solid
for radius, color, label, fontsize in layer_specs[1:]:
    circle = Circle((0, 0), radius, facecolor=color, edgecolor=CYAN,
                    linewidth=2, alpha=0.85)
    ax.add_patch(circle)

ax.text(0, 0, 'Workflow', fontsize=20, color=WHITE, ha='center', va='center',
        fontweight='bold')
ax.text(0, -2.4, '剥一层', fontsize=16, color=ORANGE, ha='center', va='center',
        fontweight='bold')

# --- Panel 3: Only core ---
ax = axes[2]
# Outer two layers: very faint dashed
for radius in [1.8, 1.2]:
    circle = Circle((0, 0), radius, facecolor='none', edgecolor=DIM,
                    linewidth=1, linestyle='dotted', alpha=0.2)
    ax.add_patch(circle)

# Core layer
circle_core = Circle((0, 0), 0.6, facecolor=CYAN, edgecolor=WHITE,
                     linewidth=2.5, alpha=0.95)
ax.add_patch(circle_core)

ax.text(0, 0, 'While\nLoop', fontsize=14, color=BG, ha='center', va='center',
        fontweight='bold')
ax.text(0, -1.2, '+ LLM', fontsize=13, color=CYAN, ha='center', va='center',
        fontweight='bold')

# "Just this?" annotation
ax.annotate('就这？', xy=(0.8, 0.5), xytext=(2.0, 1.8),
            fontsize=18, color=ORANGE, fontweight='bold',
            ha='center', va='center',
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2))

ax.text(0, -2.4, '朴素真相', fontsize=16, color=CYAN, ha='center', va='center',
        fontweight='bold')

# --- Arrows between panels ---
arrow_style = dict(arrowstyle='->', color=WHITE, lw=3,
                   connectionstyle='arc3,rad=0')

# Arrow 1->2
fig.patches.append(FancyArrowPatch(
    (0.34, 0.50), (0.37, 0.50),
    transform=fig.transFigure,
    arrowstyle='->', mutation_scale=25,
    color=WHITE, linewidth=3
))

# Arrow 2->3
fig.patches.append(FancyArrowPatch(
    (0.64, 0.50), (0.67, 0.50),
    transform=fig.transFigure,
    arrowstyle='->', mutation_scale=25,
    color=WHITE, linewidth=3
))

out = Path('/Users/mik/strange LLM/assets/diagrams/rendered/onion_peeling.png')
fig.savefig(out, dpi=150, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
plt.close()
print(f"Saved: {out}")
