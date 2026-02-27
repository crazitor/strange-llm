#!/usr/bin/env python3
"""Productivity paradox: predicted vs felt vs measured."""
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
RED = '#FF4444'
fp = {'fontfamily': FONT}

fig, ax = plt.subplots(figsize=(19.2, 10.8), facecolor=BG)
ax.set_facecolor(BG)

labels = ['预测提升\n(Predicted)', '自我感觉\n(Self-reported)', '实际测量\n(Measured)']
values = [24, 20, -19]
colors = [CYAN, PURPLE, RED]

x = np.arange(3)
bars = ax.bar(x, values, width=0.6, color=colors, alpha=0.85, edgecolor='none')

# Value labels
for i, (bar, v) in enumerate(zip(bars, values)):
    y = bar.get_height()
    sign = '+' if v > 0 else ''
    ax.text(bar.get_x() + bar.get_width()/2, y + (2 if v > 0 else -3),
            f'{sign}{v}%', ha='center', va='bottom' if v > 0 else 'top',
            color=colors[i], fontsize=42, fontweight='bold')

# Zero line
ax.axhline(y=0, color=WHITE, linewidth=2, alpha=0.5)

# Annotations
ax.annotate('', xy=(1.7, 18), xytext=(1.3, 18),
            arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.5, alpha=0.4))
ax.annotate('', xy=(2.3, -5), xytext=(1.7, 5),
            arrowprops=dict(arrowstyle='->', color=RED, lw=3))
ax.text(2.6, 5, '反转!', fontsize=24, color=RED, fontweight='bold', **fp)

ax.set_title('生产力悖论：感觉 ≠ 现实', fontsize=38, color=WHITE,
             fontweight='bold', pad=25, **fp)
ax.set_subtitle = None

ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=20, color=WHITE, **fp)
ax.set_ylabel('效率变化 (%)', fontsize=20, color=WHITE, **fp)
ax.set_ylim(-30, 35)
ax.tick_params(colors=WHITE, labelsize=14)
for spine in ax.spines.values():
    spine.set_color(WHITE)
    spine.set_alpha(0.2)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(True, axis='y', alpha=0.08, color=WHITE)

# Subtitle
ax.text(1, -27, '来源：METR研究 — AI辅助编程实际效率研究', fontsize=15, color=WHITE,
        ha='center', alpha=0.4, **fp)

plt.tight_layout(pad=2)
plt.savefig('/Users/mik/strange LLM/assets/diagrams/rendered/productivity_paradox.png',
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close()
print("Done: productivity_paradox.png")
