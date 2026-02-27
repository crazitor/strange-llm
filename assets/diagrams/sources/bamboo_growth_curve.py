"""
Diagram 1: Bamboo Growth Curve (Page 47)
The bamboo metaphor — years of invisible underground growth,
then an explosive above-ground phase. AI follows the same pattern.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from pathlib import Path

# ---------------------------------------------------------------------------
# Font setup — try Chinese-capable fonts available on macOS
# ---------------------------------------------------------------------------
CHINESE_FONTS = ['PingFang HK', 'STHeiti', 'Heiti TC', 'Heiti SC',
                 'PingFang SC', 'SimHei', 'sans-serif']

def get_chinese_font():
    available = {f.name for f in fm.fontManager.ttflist}
    for name in CHINESE_FONTS:
        if name in available:
            return name
    return 'sans-serif'

FONT = get_chinese_font()
plt.rcParams['font.family'] = FONT
plt.rcParams['axes.unicode_minus'] = False

# ---------------------------------------------------------------------------
# Colours
# ---------------------------------------------------------------------------
BG       = '#0F1729'
CYAN     = '#00D4AA'
ORANGE   = '#FF6B35'
WHITE    = '#FFFFFF'
DIM      = '#6B7280'
GRID     = '#1E2A42'

# ---------------------------------------------------------------------------
# Data — bamboo curve (sigmoid-like, delayed)
# ---------------------------------------------------------------------------
x = np.linspace(0, 5, 500)

# Bamboo: almost zero until ~4.2 years, then rockets up
def bamboo(t):
    return 12.0 / (1.0 + np.exp(-8 * (t - 4.5)))

# AI curve: same shape, shifted slightly later to show it "follows the pattern"
def ai_curve(t):
    return 11.0 / (1.0 + np.exp(-7 * (t - 4.7)))

y_bamboo = bamboo(x)
y_ai     = ai_curve(x)

# Threshold line height (where growth becomes visible)
THRESHOLD = 1.0

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(19.2, 10.8), facecolor=BG)
ax.set_facecolor(BG)

# Grid
ax.grid(True, color=GRID, linewidth=0.5, alpha=0.6)

# Bamboo curve
ax.plot(x, y_bamboo, color=CYAN, linewidth=3.5, label='竹子生长', zorder=5)

# AI curve (dashed)
ax.plot(x, y_ai, color=ORANGE, linewidth=2.8, linestyle='--',
        label='AI 发展', zorder=5, alpha=0.9)

# Threshold line
ax.axhline(y=THRESHOLD, color=DIM, linewidth=1.5, linestyle=':',
           zorder=3, alpha=0.7)
ax.text(0.15, THRESHOLD + 0.35, '临界点 (Threshold)',
        color=DIM, fontsize=16, fontstyle='italic', zorder=6)

# ---------------------------------------------------------------------------
# Phase labels
# ---------------------------------------------------------------------------
# Underground rooting period — flat section
ax.annotate('',
            xy=(3.8, 0.15), xytext=(0.3, 0.15),
            arrowprops=dict(arrowstyle='<->', color=DIM, lw=1.8),
            zorder=4)
ax.text(2.0, -1.2, '地下扎根期\nUnderground Rooting',
        color=DIM, fontsize=18, ha='center', va='top',
        fontstyle='italic', zorder=6,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                  edgecolor=DIM, alpha=0.8))

# Above-ground explosion — steep section
ax.annotate('',
            xy=(5.0, 11.5), xytext=(4.3, 2.5),
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=2.5,
                            connectionstyle='arc3,rad=0.15'),
            zorder=4)
ax.text(4.85, 7.0, '地面爆发期\nExplosive Growth',
        color=CYAN, fontsize=18, ha='center', fontweight='bold',
        zorder=6,
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#0A2520',
                  edgecolor=CYAN, alpha=0.85))

# Small annotation: "6 weeks → 10+ m"
ax.text(4.88, 4.5, '6周冲上10米+',
        color=CYAN, fontsize=14, ha='center', alpha=0.8, zorder=6)

# AI annotation
ax.text(3.6, 5.0, 'AI 也在\n"扎根"',
        color=ORANGE, fontsize=16, ha='center', fontweight='bold',
        zorder=6, alpha=0.9,
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#2A1510',
                  edgecolor=ORANGE, alpha=0.75))

# ---------------------------------------------------------------------------
# Fill underground region
# ---------------------------------------------------------------------------
ax.fill_between(x, 0, np.minimum(y_bamboo, THRESHOLD),
                color=CYAN, alpha=0.06, zorder=2)
ax.fill_between(x, THRESHOLD, np.maximum(y_bamboo, THRESHOLD),
                color=CYAN, alpha=0.10, zorder=2)

# ---------------------------------------------------------------------------
# Axes styling
# ---------------------------------------------------------------------------
ax.set_xlim(0, 5.1)
ax.set_ylim(-1.8, 13.5)

ax.set_xlabel('年份 (Years)', color=WHITE, fontsize=18, labelpad=12)
ax.set_ylabel('可见高度 (Visible Height)', color=WHITE, fontsize=18, labelpad=12)
ax.set_title('竹子生长曲线 — 不可见的积累，爆发性的结果',
             color=WHITE, fontsize=26, fontweight='bold', pad=20)

ax.tick_params(colors=DIM, labelsize=14)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.7)

ax.set_xticks([0, 1, 2, 3, 4, 5])
ax.set_xticklabels(['0', '1', '2', '3', '4', '5'], color=DIM)

# Legend
legend = ax.legend(loc='upper left', fontsize=16, framealpha=0.3,
                   facecolor=BG, edgecolor=DIM, labelcolor=WHITE)
legend.get_frame().set_linewidth(0.8)

plt.tight_layout()

# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------
out = Path('/Users/mik/strange LLM/assets/diagrams/rendered/bamboo_growth_curve.png')
fig.savefig(out, dpi=150, facecolor=BG, bbox_inches='tight',
            pad_inches=0.3)
plt.close(fig)
print(f'Saved → {out}  ({out.stat().st_size / 1024:.0f} KB)')
