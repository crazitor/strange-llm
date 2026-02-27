#!/usr/bin/env python3
"""Reliability cliff: cumulative success rate drops with steps."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

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

steps = np.arange(1, 21)
rates = [0.95, 0.98, 0.99, 0.999]
colors = ['#FF4444', ORANGE, PURPLE, CYAN]
labels = ['95%/步', '98%/步', '99%/步', '99.9%/步']

for rate, color, label in zip(rates, colors, labels):
    cumulative = rate ** steps * 100
    ax.plot(steps, cumulative, color=color, linewidth=3.5, label=label, marker='o', markersize=5)
    ax.fill_between(steps, cumulative, alpha=0.05, color=color)

# Danger zone
ax.axhspan(0, 50, alpha=0.05, color='#FF4444')
ax.axhline(y=50, color='#FF4444', linewidth=1, alpha=0.4, linestyle='--')
ax.text(19.5, 51, '50% 失败线', fontsize=14, color='#FF4444', ha='right', alpha=0.7, **fp)

# Annotations
ax.annotate(f'95%^10 = {0.95**10:.0%}', xy=(10, 0.95**10*100), xytext=(12, 45),
            fontsize=16, color='#FF4444', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#FF4444', lw=2))

ax.annotate(f'99%^20 = {0.99**20:.0%}', xy=(20, 0.99**20*100), xytext=(16, 72),
            fontsize=16, color=PURPLE, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=PURPLE, lw=2))

ax.set_title('可靠性悬崖：步骤越多，失败越快', fontsize=36, color=WHITE,
             fontweight='bold', pad=20, **fp)
ax.set_xlabel('任务步骤数', fontsize=20, color=WHITE, **fp)
ax.set_ylabel('累积成功率 (%)', fontsize=20, color=WHITE, **fp)
ax.set_xlim(1, 20)
ax.set_ylim(0, 102)
ax.tick_params(colors=WHITE, labelsize=14)
for spine in ax.spines.values():
    spine.set_color(WHITE)
    spine.set_alpha(0.3)
ax.grid(True, alpha=0.1, color=WHITE)
ax.legend(fontsize=18, loc='lower left', facecolor=DARK, edgecolor=WHITE,
          labelcolor=WHITE, prop={'family': FONT, 'size': 18})

plt.tight_layout(pad=2)
plt.savefig('/Users/mik/strange LLM/assets/diagrams/rendered/reliability_cliff.png',
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close()
print("Done: reliability_cliff.png")
