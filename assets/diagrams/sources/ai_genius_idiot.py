"""
P40 - AI Genius vs Idiot: Capability Inversion
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from pathlib import Path
import matplotlib.patches as mpatches

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

OUT = Path('/Users/mik/strange LLM/assets/diagrams/rendered/ai_genius_idiot.png')

fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=150, facecolor=BG)
ax.set_facecolor(BG)

# X axis: task difficulty
x = np.linspace(0, 10, 300)

# Human performance: smooth decline from easy to hard
human = 95 - 7 * x + 0.1 * x**2
human = np.clip(human, 10, 100)

# AI performance: high on structured/easy-pattern tasks, dips on simple perception,
# rises again on highly structured hard tasks -> a "W" like shape
# Specifically: high at x=0 (pattern matching), dips around x=2-4 (simple perception like counting fingers),
# then rises for hard structured tasks (math proofs, coding)
ai = 85 - 55 * np.exp(-((x - 0.5)**2) / 0.8) * 0 + \
     40 * np.exp(-((x - 3.0)**2) / 2.0) * (-1) + \
     30 * np.exp(-((x - 8.0)**2) / 3.0) + 65
# Reshape: start high, dip in middle-easy, recover for hard
ai = 90 * np.exp(-((x - 3.5)**2) / 1.5) * (-1) + 85 + 10 * np.exp(-((x - 8.5)**2) / 2.0)
ai_base = -50 * np.exp(-((x - 3.2)**2) / 2.5) + 82 + 12 * np.exp(-((x - 9)**2) / 3.0)
ai = ai_base
ai = np.clip(ai, 5, 100)

# Plot curves
ax.plot(x, human, color=ORANGE, linewidth=3.5, label='人类表现', zorder=5)
ax.plot(x, ai, color=CYAN, linewidth=3.5, label='AI表现', zorder=5)

# Fill the inversion zone (where AI < Human on easy tasks, AI > Human on hard tasks)
# Find crossover points
diff = ai - human
cross_indices = np.where(np.diff(np.sign(diff)))[0]

# Fill region between curves where AI is below human (the inversion zone)
# Shade the area where the "inversion" is most visible
mask_ai_below = ai < human
ax.fill_between(x, ai, human, where=mask_ai_below,
                alpha=0.15, color=ORANGE, label='能力倒挂区', zorder=2)
mask_ai_above = ai > human
ax.fill_between(x, ai, human, where=mask_ai_above,
                alpha=0.1, color=CYAN, zorder=2)

# Key annotation: finger counting (AI weak spot)
ai_low_idx = np.argmin(ai[30:130]) + 30  # find the dip
ax.annotate('数手指\nAI反而不行',
            xy=(x[ai_low_idx], ai[ai_low_idx]),
            xytext=(x[ai_low_idx] - 1.5, ai[ai_low_idx] - 18),
            fontsize=16, color=ORANGE, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2.5),
            ha='center', zorder=10)

# Key annotation: math proofs (AI strong point)
ai_high_idx = len(x) - 30
ax.annotate('证明数学定理\nAI很强',
            xy=(x[ai_high_idx], ai[ai_high_idx]),
            xytext=(x[ai_high_idx] - 1.2, ai[ai_high_idx] + 12),
            fontsize=16, color=CYAN, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=2.5),
            ha='center', zorder=10)

# "能力倒挂区" label in the middle
mid_x = 4.5
ax.text(mid_x, 55, '能力倒挂区', fontsize=20, color=WHITE, alpha=0.7,
        fontweight='bold', ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=DIM, alpha=0.8),
        zorder=10)

# Axes styling
ax.set_xlim(0, 10)
ax.set_ylim(0, 105)
ax.set_xlabel('任务难度', fontsize=18, color=WHITE, labelpad=10)
ax.set_ylabel('表现得分', fontsize=18, color=WHITE, labelpad=10)
ax.set_xticks([0, 2.5, 5, 7.5, 10])
ax.set_xticklabels(['简单\n(感知/常识)', '', '中等', '', '困难\n(数学/编程)'],
                    fontsize=14, color=DIM)
ax.tick_params(axis='y', colors=DIM, labelsize=12)

# Grid
ax.grid(True, color=GRID, linewidth=0.5, alpha=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color(DIM)
ax.spines['left'].set_color(DIM)

# Legend
legend = ax.legend(fontsize=16, loc='upper right',
                   facecolor=BG, edgecolor=DIM, labelcolor=WHITE)

# Title
fig.suptitle('天才还是白痴？ — AI的能力倒挂',
             fontsize=30, color=WHITE, fontweight='bold', y=0.96)

# Bottom note
fig.text(0.5, 0.02, 'AI不是均匀变强，而是在某些方向上极强、某些方向上极弱',
         fontsize=15, color=DIM, ha='center', style='italic')

fig.savefig(OUT, dpi=150, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
plt.close()
print(f'Saved: {OUT}')
