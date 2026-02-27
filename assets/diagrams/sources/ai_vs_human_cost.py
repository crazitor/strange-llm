import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patheffects as pe
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Polygon

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
# BACKGROUND PANELS
# ══════════════════════════════════════
# Left panel — AI (cyan tint)
left_bg = FancyBboxPatch((2, 5), 46, 44, boxstyle='round,pad=0.8',
                           facecolor=PRIMARY, edgecolor=PRIMARY,
                           linewidth=1.2, alpha=0.04, zorder=1)
ax.add_patch(left_bg)
left_border = FancyBboxPatch((2, 5), 46, 44, boxstyle='round,pad=0.8',
                               facecolor='none', edgecolor=PRIMARY,
                               linewidth=1.5, alpha=0.25, zorder=2)
ax.add_patch(left_border)

# Right panel — Human (orange tint)
right_bg = FancyBboxPatch((52, 5), 46, 44, boxstyle='round,pad=0.8',
                            facecolor=ACCENT, edgecolor=ACCENT,
                            linewidth=1.2, alpha=0.04, zorder=1)
ax.add_patch(right_bg)
right_border = FancyBboxPatch((52, 5), 46, 44, boxstyle='round,pad=0.8',
                                facecolor='none', edgecolor=ACCENT,
                                linewidth=1.5, alpha=0.25, zorder=2)
ax.add_patch(right_border)

# ══════════════════════════════════════
# CENTER DIVIDER
# ══════════════════════════════════════
for y in np.arange(6, 48, 1.5):
    ax.plot([50, 50], [y, y + 0.7], color=DIM, linewidth=1.5, alpha=0.4, zorder=3)

# ══════════════════════════════════════
# LEFT PANEL — AI
# ══════════════════════════════════════
lcx = 25

# Title
ax.text(lcx, 46, 'AI', fontsize=42, color=PRIMARY, fontweight='bold',
        ha='center', va='center', zorder=10,
        path_effects=[pe.withStroke(linewidth=2, foreground=BG)])

# Big time
ax.text(lcx, 39, '1秒', fontsize=56, color=WHITE, fontweight='bold',
        ha='center', va='center', zorder=10,
        path_effects=[pe.withStroke(linewidth=3, foreground=BG)])

# Multiplier
ax.text(lcx, 33, '\u00d7 10,000次', fontsize=20, color=PRIMARY,
        ha='center', va='center', fontweight='bold', zorder=10)

# Attributes
attrs_ai = ['不害怕浪费', '不害怕失败', '不需要负责']
for i, txt in enumerate(attrs_ai):
    y = 28 - i * 3.2
    ax.text(lcx, y, txt, fontsize=16, color=DIM, ha='center', va='center',
            fontweight='bold', zorder=10)

# Visual: scattered dots (random sampling)
np.random.seed(42)
n_dots = 180
dot_x = np.random.uniform(8, 42, n_dots)
dot_y = np.random.uniform(8, 18, n_dots)
dot_sizes = np.random.uniform(3, 25, n_dots)
dot_alphas = np.random.uniform(0.15, 0.55, n_dots)
for x, y, s, a in zip(dot_x, dot_y, dot_sizes, dot_alphas):
    c = Circle((x, y), s * 0.04, facecolor=PRIMARY, edgecolor='none', alpha=a, zorder=4)
    ax.add_patch(c)

# Circular arrow (repeat symbol)
theta = np.linspace(0.3, 5.5, 80)
r = 3.0
crx = lcx + 13
cry = 13
ax.plot(crx + r * np.cos(theta), cry + r * np.sin(theta),
        color=PRIMARY, linewidth=2.5, alpha=0.6, zorder=5)
# Arrowhead
end_x = crx + r * np.cos(theta[-1])
end_y = cry + r * np.sin(theta[-1])
dx = -r * np.sin(theta[-1]) * 0.15
dy = r * np.cos(theta[-1]) * 0.15
ax.annotate('', xy=(end_x + dx, end_y + dy), xytext=(end_x - dx * 0.5, end_y - dy * 0.5),
            arrowprops=dict(arrowstyle='->', color=PRIMARY, lw=2.5), zorder=5)
ax.text(crx, cry, '重复', fontsize=11, color=PRIMARY, ha='center', va='center',
        fontweight='bold', zorder=6)

# ══════════════════════════════════════
# RIGHT PANEL — Human
# ══════════════════════════════════════
rcx = 75

# Title
ax.text(rcx, 46, '人', fontsize=42, color=ACCENT, fontweight='bold',
        ha='center', va='center', zorder=10,
        path_effects=[pe.withStroke(linewidth=2, foreground=BG)])

# Big time
ax.text(rcx, 39, '一次', fontsize=56, color=WHITE, fontweight='bold',
        ha='center', va='center', zorder=10,
        path_effects=[pe.withStroke(linewidth=3, foreground=BG)])

# Multiplier
ax.text(rcx, 33, '\u00d7 一辈子', fontsize=20, color=ACCENT,
        ha='center', va='center', fontweight='bold', zorder=10)

# Attributes
attrs_human = ['承担后果', '不可撤回', '选择即代价']
for i, txt in enumerate(attrs_human):
    y = 28 - i * 3.2
    ax.text(rcx, y, txt, fontsize=16, color=DIM, ha='center', va='center',
            fontweight='bold', zorder=10)

# Visual: single bold arrow (one irreversible choice)
arrow_x_start = rcx - 8
arrow_x_end = rcx + 8
arrow_y = 13
ax.annotate('', xy=(arrow_x_end, arrow_y), xytext=(arrow_x_start, arrow_y),
            arrowprops=dict(arrowstyle='->', color=ACCENT, lw=5,
                            mutation_scale=25),
            zorder=5)
# Trail behind arrow (fading)
for i, alpha in enumerate(np.linspace(0.05, 0.3, 8)):
    x = arrow_x_start - 1.5 - i * 0.8
    ax.plot([x, x + 0.4], [arrow_y, arrow_y], color=ACCENT, linewidth=3, alpha=alpha, zorder=4)

# Anchor/weight symbol
anch_x = rcx
anch_y = 8.5
# Anchor ring
ring = Circle((anch_x, anch_y + 1.5), 0.8, facecolor='none', edgecolor=ACCENT,
              linewidth=2, alpha=0.7, zorder=6)
ax.add_patch(ring)
# Anchor shaft
ax.plot([anch_x, anch_x], [anch_y + 0.7, anch_y - 1.5], color=ACCENT, linewidth=2.5, alpha=0.7, zorder=6)
# Anchor arms
ax.plot([anch_x - 1.5, anch_x], [anch_y - 0.8, anch_y - 1.5], color=ACCENT, linewidth=2.5, alpha=0.7, zorder=6)
ax.plot([anch_x + 1.5, anch_x], [anch_y - 0.8, anch_y - 1.5], color=ACCENT, linewidth=2.5, alpha=0.7, zorder=6)
# Crossbar
ax.plot([anch_x - 1.2, anch_x + 1.2], [anch_y, anch_y], color=ACCENT, linewidth=2, alpha=0.7, zorder=6)

# ══════════════════════════════════════
# BOTTOM — main message
# ══════════════════════════════════════
ax.text(50, 1.8, '分界线不是能力 \u2014 是代价', fontsize=24, color=WHITE,
        ha='center', va='center', fontweight='bold', zorder=10,
        path_effects=[pe.withStroke(linewidth=4, foreground=BG)])

# VS in center
ax.text(50, 30, 'VS', fontsize=28, color=DIM, fontweight='bold',
        ha='center', va='center', alpha=0.3, zorder=3,
        rotation=0, style='italic')

# ── Save ──
out = '/Users/mik/strange LLM/assets/diagrams/rendered/ai_vs_human_cost.png'
fig.savefig(out, dpi=100, facecolor=BG, edgecolor='none', bbox_inches='tight', pad_inches=0.3)
plt.close(fig)
print(f'Saved: {out}')
