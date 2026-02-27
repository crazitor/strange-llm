#!/usr/bin/env python3
"""Benchmark scores vs real-world performance gap."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from matplotlib.patches import FancyBboxPatch

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

BG = '#0F1729'
CYAN = '#00D4AA'
ORANGE = '#FF6B35'
PURPLE = '#7C6BF0'
WHITE = '#FFFFFF'
DARK = '#1A2340'
fp = {'fontfamily': FONT}

fig, ax = plt.subplots(figsize=(19.2, 10.8), facecolor=BG)
ax.set_facecolor(BG)

models = ['GPT-4o', 'Claude 3.5', 'Gemini 1.5', 'Llama 4\nMaverick', 'Qwen 2.5']
benchmark = [92, 91, 89, 94, 88]
reality = [61, 63, 55, 48, 52]

x = np.arange(len(models))
width = 0.35

bars1 = ax.bar(x - width/2, benchmark, width, color=CYAN, alpha=0.85, label='基准测试得分', edgecolor='none')
bars2 = ax.bar(x + width/2, reality, width, color=ORANGE, alpha=0.85, label='真实场景表现', edgecolor='none')

# Gap arrows
for i in range(len(models)):
    gap = benchmark[i] - reality[i]
    mid_x = x[i] + 0.02
    ax.annotate('', xy=(mid_x, reality[i] + 1), xytext=(mid_x, benchmark[i] - 1),
                arrowprops=dict(arrowstyle='<->', color='#FF4444', lw=2, alpha=0.7))
    ax.text(mid_x + 0.22, (benchmark[i] + reality[i]) / 2, f'-{gap}%',
            fontsize=14, color='#FF4444', ha='left', va='center', fontweight='bold')

# Value labels
for bar in bars1:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f'{int(bar.get_height())}%', ha='center', va='bottom', color=CYAN, fontsize=14, fontweight='bold')
for bar in bars2:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f'{int(bar.get_height())}%', ha='center', va='bottom', color=ORANGE, fontsize=14, fontweight='bold')

# Llama 4 callout
ax.annotate('Llama 4: 排行榜#1\n真实排名 #32', xy=(3, 48), xytext=(4.2, 75),
            fontsize=16, color='#FF4444', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#FF4444', lw=2),
            ha='center', bbox=dict(boxstyle='round,pad=0.4', facecolor=DARK, edgecolor='#FF4444'),
            **fp)

ax.set_title('基准测试 vs 真实表现：被掩盖的鸿沟', fontsize=34, color=WHITE,
             fontweight='bold', pad=25, **fp)
ax.set_xticks(x)
ax.set_xticklabels(models, fontsize=16, color=WHITE, **fp)
ax.set_ylabel('得分 (%)', fontsize=18, color=WHITE, **fp)
ax.set_ylim(0, 105)
ax.tick_params(colors=WHITE, labelsize=14)
for spine in ax.spines.values():
    spine.set_color(WHITE)
    spine.set_alpha(0.2)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(True, axis='y', alpha=0.1, color=WHITE)
ax.legend(fontsize=18, loc='upper right', facecolor=DARK, edgecolor=WHITE,
          labelcolor=WHITE, prop={'family': FONT, 'size': 18})

plt.tight_layout(pad=2)
plt.savefig('/Users/mik/strange LLM/assets/diagrams/rendered/benchmark_vs_reality.png',
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close()
print("Done: benchmark_vs_reality.png")
