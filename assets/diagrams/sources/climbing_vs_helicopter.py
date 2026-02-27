import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patheffects as pe
import numpy as np
from matplotlib.patches import FancyArrowPatch, Polygon, Circle, Arc
from matplotlib.lines import Line2D

# ── Theme ──
BG       = '#0F1729'
PRIMARY  = '#00D4AA'
ACCENT   = '#FF6B35'
WHITE    = '#FFFFFF'
DIM      = '#6B7280'
GOLD     = '#FFD700'

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'STHeiti', 'SimHei', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(19.2, 10.8))
fig.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 56.25)  # 16:9 ratio
ax.set_aspect('equal')
ax.axis('off')

# ── Helper: draw a mountain ──
def draw_mountain(ax, cx, base_y, width, height, color, alpha=1.0):
    """Draw a triangular mountain centered at cx."""
    tri = Polygon(
        [[cx - width/2, base_y], [cx, base_y + height], [cx + width/2, base_y]],
        closed=True, facecolor=color, edgecolor='none', alpha=alpha, zorder=2
    )
    ax.add_patch(tri)
    return cx, base_y + height  # peak coords

# ── Ground line ──
ax.plot([0, 100], [8, 8], color=DIM, linewidth=0.5, alpha=0.3, zorder=1)

# ══════════════════════════════════════
# LEFT SIDE — Human climbing
# ══════════════════════════════════════
lcx = 28  # mountain center x
peak_lx, peak_ly = draw_mountain(ax, lcx, 8, 32, 32, '#1a2744', alpha=0.9)

# Snow cap
snow_l = Polygon(
    [[lcx - 4, 8 + 28], [lcx, 8 + 32], [lcx + 4, 8 + 28]],
    closed=True, facecolor='#2a3a5a', edgecolor='none', alpha=0.5, zorder=3
)
ax.add_patch(snow_l)

# Zigzag climbing path
zx = [14, 19, 24, 19, 26, 21, 28]
zy = [9, 14, 18, 22, 27, 32, 37]
ax.plot(zx, zy, color=ACCENT, linewidth=2.5, linestyle='--', alpha=0.8, zorder=5,
        path_effects=[pe.Stroke(linewidth=4, foreground=BG), pe.Normal()])

# Stick figure at mid-climb position
fx, fy = 21, 25
# Head
head = Circle((fx, fy + 2.2), 1.0, facecolor=ACCENT, edgecolor=WHITE, linewidth=0.8, zorder=6)
ax.add_patch(head)
# Body
ax.plot([fx, fx], [fy + 1.2, fy - 1.5], color=WHITE, linewidth=2, zorder=6)
# Arms (reaching up)
ax.plot([fx, fx - 1.5], [fy + 0.5, fy + 1.8], color=WHITE, linewidth=1.8, zorder=6)
ax.plot([fx, fx + 1.5], [fy + 0.5, fy + 1.8], color=WHITE, linewidth=1.8, zorder=6)
# Legs
ax.plot([fx, fx - 1.2], [fy - 1.5, fy - 3], color=WHITE, linewidth=1.8, zorder=6)
ax.plot([fx, fx + 0.8], [fy - 1.5, fy - 3], color=WHITE, linewidth=1.8, zorder=6)

# Sweat drops
for dx, dy in [(1.8, 2.5), (2.5, 1.5), (-1.5, 3.0)]:
    drop = Circle((fx + dx, fy + dy), 0.35, facecolor=PRIMARY, edgecolor='none', alpha=0.6, zorder=6)
    ax.add_patch(drop)

# Label
ax.text(lcx, 4, '人类：一步一步爬', fontsize=18, color=ACCENT, fontweight='bold',
        ha='center', va='center', zorder=10)
# Time
ax.text(14, 11, '一天', fontsize=14, color=ACCENT, fontweight='bold',
        ha='center', va='center', zorder=10,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=ACCENT, linewidth=1.5, alpha=0.9))

# ══════════════════════════════════════
# RIGHT SIDE — AI helicopter
# ══════════════════════════════════════
rcx = 72
peak_rx, peak_ry = draw_mountain(ax, rcx, 8, 32, 32, '#1a2744', alpha=0.9)

# Snow cap
snow_r = Polygon(
    [[rcx - 4, 8 + 28], [rcx, 8 + 32], [rcx + 4, 8 + 28]],
    closed=True, facecolor='#2a3a5a', edgecolor='none', alpha=0.5, zorder=3
)
ax.add_patch(snow_r)

# Straight arrow from base to peak
ax.annotate('', xy=(rcx, 38), xytext=(rcx, 10),
            arrowprops=dict(arrowstyle='->', color=PRIMARY, lw=3.5,
                            connectionstyle='arc3,rad=0'),
            zorder=5)

# Helicopter near the top
hx, hy = rcx + 0.5, 34
# Body (rounded rect)
heli_body = patches.FancyBboxPatch((hx - 3, hy - 1.2), 6, 2.4,
                                     boxstyle='round,pad=0.3',
                                     facecolor=PRIMARY, edgecolor=WHITE,
                                     linewidth=1.2, alpha=0.9, zorder=7)
ax.add_patch(heli_body)
# Tail
ax.plot([hx - 3, hx - 5.5], [hy, hy + 0.3], color=PRIMARY, linewidth=2.5, zorder=7)
ax.plot([hx - 5.5, hx - 6.5], [hy + 0.3, hy + 1.8], color=PRIMARY, linewidth=2, zorder=7)
# Tail rotor
ax.plot([hx - 7, hx - 6], [hy + 1.8, hy + 1.8], color=WHITE, linewidth=1.5, zorder=7)
# Main rotor
ax.plot([hx - 5, hx + 5], [hy + 1.6, hy + 1.6], color=WHITE, linewidth=2.5, zorder=8)
ax.plot([hx, hx], [hy + 1.2, hy + 1.6], color=WHITE, linewidth=1.5, zorder=8)
# Skids
ax.plot([hx - 2, hx + 2], [hy - 1.8, hy - 1.8], color=WHITE, linewidth=1.5, zorder=7)
ax.plot([hx - 1.5, hx - 1.5], [hy - 1.2, hy - 1.8], color=WHITE, linewidth=1, zorder=7)
ax.plot([hx + 1.5, hx + 1.5], [hy - 1.2, hy - 1.8], color=WHITE, linewidth=1, zorder=7)

# Label
ax.text(rcx, 4, 'AI：直达山顶', fontsize=18, color=PRIMARY, fontweight='bold',
        ha='center', va='center', zorder=10)
# Time
ax.text(rcx + 12, 11, '5分钟', fontsize=14, color=PRIMARY, fontweight='bold',
        ha='center', va='center', zorder=10,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=PRIMARY, linewidth=1.5, alpha=0.9))

# ══════════════════════════════════════
# CENTER — shared peak marker
# ══════════════════════════════════════
# Golden star at each peak
for px, py in [(peak_lx, peak_ly), (peak_rx, peak_ry)]:
    star_angles = np.linspace(0, 2*np.pi, 11)
    star_r = [1.8 if i % 2 == 0 else 0.8 for i in range(11)]
    star_x = [px + r * np.sin(a) for a, r in zip(star_angles, star_r)]
    star_y = [py + r * np.cos(a) for a, r in zip(star_angles, star_r)]
    star = Polygon(list(zip(star_x, star_y)), closed=True,
                   facecolor=GOLD, edgecolor=WHITE, linewidth=0.8, alpha=0.9, zorder=9)
    ax.add_patch(star)

# Top center label
ax.text(50, 46, '山顶 = 相同的结果', fontsize=16, color=GOLD,
        ha='center', va='center', fontweight='bold', zorder=10,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD, linewidth=1, alpha=0.8))

# Connecting dashed lines from both peaks to the label
ax.plot([peak_lx, 42], [peak_ly + 1.5, 46], color=GOLD, linewidth=1, linestyle=':', alpha=0.5, zorder=4)
ax.plot([peak_rx, 58], [peak_ry + 1.5, 46], color=GOLD, linewidth=1, linestyle=':', alpha=0.5, zorder=4)

# ══════════════════════════════════════
# CENTER DIVIDER
# ══════════════════════════════════════
ax.plot([50, 50], [2, 44], color=DIM, linewidth=1, linestyle='--', alpha=0.4, zorder=1)

# ══════════════════════════════════════
# BOTTOM — main question
# ══════════════════════════════════════
ax.text(50, 1.2, '结果相同 \u2014 但过程的意义是什么？', fontsize=22, color=WHITE,
        ha='center', va='center', fontweight='bold', zorder=10,
        path_effects=[pe.withStroke(linewidth=3, foreground=BG)])

# ── Subtle background glow ──
for cx_glow, c in [(28, ACCENT), (72, PRIMARY)]:
    glow = Circle((cx_glow, 24), 20, facecolor=c, edgecolor='none', alpha=0.03, zorder=0)
    ax.add_patch(glow)

# ── Save ──
out = '/Users/mik/strange LLM/assets/diagrams/rendered/climbing_vs_helicopter.png'
fig.savefig(out, dpi=100, facecolor=BG, edgecolor='none', bbox_inches='tight', pad_inches=0.3)
plt.close(fig)
print(f'Saved: {out}')
