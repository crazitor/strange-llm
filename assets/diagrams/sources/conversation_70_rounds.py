"""
P26 - 70 Rounds Conversation: How an Agent Goes Off the Rails
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from pathlib import Path
import matplotlib.patches as mpatches
from matplotlib.collections import LineCollection
from matplotlib.colors import LinearSegmentedColormap

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

OUT = Path('/Users/mik/strange LLM/assets/diagrams/rendered/conversation_70_rounds.png')

fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=150, facecolor=BG)
ax.set_facecolor(BG)

# Generate curve data
x = np.linspace(1, 70, 500)
# Deviation: flat early, accelerates after 30, goes wild after 50
y = 2 + 0.5 * x * (x < 15) + \
    (0.5 * 15 + 1.2 * (x - 15)) * ((x >= 15) & (x < 30)) + \
    (0.5 * 15 + 1.2 * 15 + 3.5 * (x - 30)) * ((x >= 30) & (x < 50)) + \
    (0.5 * 15 + 1.2 * 15 + 3.5 * 20 + 6 * (x - 50) + 0.08 * (x - 50)**2) * (x >= 50)

# Normalize to 0-100%
y = y / y.max() * 100
# Add some noise for realism
np.random.seed(17)
noise = np.random.normal(0, 1.5, len(x))
noise_cumsum = np.cumsum(noise) * 0.1
y_noisy = y + noise_cumsum
y_noisy = np.clip(y_noisy, 0, 100)

# Create gradient-colored line segments
points = np.array([x, y_noisy]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

# Colormap: CYAN -> ORANGE -> RED
colors_list = [CYAN, ORANGE, RED]
cmap = LinearSegmentedColormap.from_list('deviation', colors_list, N=256)
norm = plt.Normalize(0, 100)
lc = LineCollection(segments, cmap=cmap, norm=norm, linewidth=3.5, zorder=5)
lc.set_array(y_noisy[:-1])
ax.add_collection(lc)

# Glow effect: wider transparent line underneath
lc_glow = LineCollection(segments, cmap=cmap, norm=norm, linewidth=10, alpha=0.15, zorder=4)
lc_glow.set_array(y_noisy[:-1])
ax.add_collection(lc_glow)

# Key event annotations
events = [
    (1, '整理AI新闻', '正常', CYAN, 'right'),
    (15, '开始添加额外功能', '微微偏离', CYAN, 'right'),
    (30, '自行决定重构代码', '明显偏离', ORANGE, 'left'),
    (50, '自己给自己安排任务', '急剧上升', ORANGE, 'left'),
    (70, '完全脱离原始指令', '失控', RED, 'left'),
]

for ex, label, sublabel, color, align in events:
    # Find closest y value
    idx = np.argmin(np.abs(x - ex))
    ey = y_noisy[idx]

    # Dot
    ax.plot(ex, ey, 'o', color=color, markersize=10, zorder=8,
            markeredgecolor=WHITE, markeredgewidth=1.5)

    # Annotation
    if align == 'right':
        offset = (15, 20)
        ha = 'left'
    else:
        offset = (-15, 20)
        ha = 'right'

    # Adjust specific positions to avoid overlap
    if ex == 1:
        offset = (12, 15)
    elif ex == 15:
        offset = (15, 25)
    elif ex == 30:
        offset = (15, 30)
    elif ex == 50:
        offset = (-15, 20)
    elif ex == 70:
        offset = (-20, -15)
        ha = 'right'

    ax.annotate(f'第{ex}轮: {label}\n({sublabel})',
                xy=(ex, ey), xytext=offset,
                textcoords='offset points',
                fontsize=12, color=color, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=color, lw=1.8),
                ha=ha, va='bottom',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color, alpha=0.85),
                zorder=10)

# "Human attention limit" dashed line at round 30
ax.axvline(x=30, color=DIM, linewidth=2, linestyle='--', alpha=0.6, zorder=3)
ax.text(31, 95, '人类注意力极限', fontsize=13, color=DIM, fontweight='bold',
        rotation=0, va='top', ha='left',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=DIM, alpha=0.7),
        zorder=10)

# Danger zone fill above 60%
ax.axhspan(70, 105, facecolor=RED, alpha=0.04, zorder=1)
ax.text(5, 82, 'DANGER ZONE', fontsize=14, color=RED, alpha=0.25,
        fontweight='bold', zorder=2)

# Axes styling
ax.set_xlim(0, 75)
ax.set_ylim(-5, 108)
ax.set_xlabel('对话轮次', fontsize=18, color=WHITE, labelpad=10)
ax.set_ylabel('任务偏离度', fontsize=18, color=WHITE, labelpad=10)

ax.set_xticks([1, 10, 20, 30, 40, 50, 60, 70])
ax.set_yticks([0, 20, 40, 60, 80, 100])
ax.set_yticklabels(['0%\n正常', '20%', '40%', '60%', '80%', '100%\n完全跑偏'],
                    fontsize=11, color=DIM)
ax.tick_params(axis='x', colors=DIM, labelsize=12)

ax.grid(True, color=GRID, linewidth=0.5, alpha=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color(DIM)
ax.spines['left'].set_color(DIM)

# Title
fig.suptitle('70轮对话 — 一个Agent如何失控',
             fontsize=30, color=WHITE, fontweight='bold', y=0.96)

# Bottom quote
fig.text(0.5, 0.02, '"每一步合理，但这人是疯子"',
         fontsize=17, color=DIM, ha='center', style='italic')

fig.savefig(OUT, dpi=150, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
plt.close()
print(f'Saved: {OUT}')
