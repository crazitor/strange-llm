#!/usr/bin/env python3
"""Phone keyboard vs LLM analogy - both predict next token."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
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

fig, (ax_l, ax_r) = plt.subplots(1, 2, figsize=(19.2, 10.8), facecolor=BG)
for ax in (ax_l, ax_r):
    ax.set_facecolor(BG)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

# === LEFT: Phone keyboard ===
ax_l.text(5, 9.5, '手机键盘', fontsize=36, color=WHITE, ha='center', va='top', fontweight='bold', **fp)
ax_l.text(5, 8.8, 'Phone Keyboard', fontsize=18, color=CYAN, ha='center', va='top', alpha=0.7)

# Phone outline
phone = FancyBboxPatch((2, 1.5), 6, 6.5, boxstyle="round,pad=0.3", facecolor=DARK, edgecolor=CYAN, linewidth=2)
ax_l.add_patch(phone)

# Input text
ax_l.text(5, 7.2, '"你"', fontsize=40, color=WHITE, ha='center', va='center', **fp)

# Arrow
ax_l.annotate('', xy=(5, 5.8), xytext=(5, 6.4), arrowprops=dict(arrowstyle='->', color=CYAN, lw=2.5))

# Suggestion bar
for i, (txt, prob) in enumerate(zip(['好', '呢', '们'], ['62%', '18%', '12%'])):
    x = 3 + i * 2
    box = FancyBboxPatch((x-0.7, 4.5), 1.4, 1.2, boxstyle="round,pad=0.1",
                         facecolor=CYAN if i == 0 else PURPLE, edgecolor='none', alpha=0.8 if i == 0 else 0.5)
    ax_l.add_patch(box)
    ax_l.text(x, 5.1, txt, fontsize=28, color=WHITE, ha='center', va='center', fontweight='bold', **fp)
    ax_l.text(x, 4.3, prob, fontsize=14, color=WHITE, ha='center', va='top', alpha=0.7)

# Keyboard grid hint
for row_i, row in enumerate(['Q W E R T Y U I O P', 'A S D F G H J K L', 'Z X C V B N M']):
    keys = row.split()
    y = 3.2 - row_i * 0.7
    offset = 0.3 * row_i
    for j, k in enumerate(keys):
        x = 2.5 + offset + j * 0.55
        ax_l.text(x, y, k, fontsize=9, color=WHITE, ha='center', va='center', alpha=0.3)

ax_l.text(5, 1.8, '~万级参数', fontsize=20, color=ORANGE, ha='center', va='center', **fp)

# === RIGHT: LLM ===
ax_r.text(5, 9.5, '大语言模型', fontsize=36, color=WHITE, ha='center', va='top', fontweight='bold', **fp)
ax_r.text(5, 8.8, 'Large Language Model', fontsize=18, color=CYAN, ha='center', va='top', alpha=0.7)

# LLM "brain" box
brain = FancyBboxPatch((1.5, 1.5), 7, 6.5, boxstyle="round,pad=0.3", facecolor=DARK, edgecolor=ORANGE, linewidth=2)
ax_r.add_patch(brain)

# Input
ax_r.text(5, 7.2, '"法国的首都是"', fontsize=32, color=WHITE, ha='center', va='center', **fp)

# Arrow
ax_r.annotate('', xy=(5, 5.8), xytext=(5, 6.4), arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2.5))

# Predictions
for i, (txt, prob) in enumerate(zip(['巴黎', '法国', '位于'], ['89%', '5%', '2%'])):
    x = 3 + i * 2
    box = FancyBboxPatch((x-0.8, 4.5), 1.6, 1.2, boxstyle="round,pad=0.1",
                         facecolor=ORANGE if i == 0 else PURPLE, edgecolor='none', alpha=0.8 if i == 0 else 0.5)
    ax_r.add_patch(box)
    ax_r.text(x, 5.1, txt, fontsize=28, color=WHITE, ha='center', va='center', fontweight='bold', **fp)
    ax_r.text(x, 4.3, prob, fontsize=14, color=WHITE, ha='center', va='top', alpha=0.7)

# Neural network hint - scattered dots
rng = np.random.RandomState(42)
for _ in range(200):
    x, y = rng.uniform(2, 8), rng.uniform(2, 4)
    ax_r.plot(x, y, 'o', color=ORANGE, markersize=rng.uniform(0.5, 2), alpha=rng.uniform(0.05, 0.2))

ax_r.text(5, 1.8, '~千亿级参数', fontsize=20, color=ORANGE, ha='center', va='center', **fp)

# Center connector
fig.text(0.5, 0.5, '本质相同\n预测下一个词', fontsize=28, color=CYAN, ha='center', va='center',
         fontweight='bold', bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=CYAN, linewidth=2), **fp)

plt.tight_layout(pad=2)
plt.savefig('/Users/mik/strange LLM/assets/diagrams/rendered/phone_keyboard_llm.png',
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close()
print("Done: phone_keyboard_llm.png")
