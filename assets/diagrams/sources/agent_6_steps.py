#!/usr/bin/env python3
"""Agent 6-step cascade failure vs human 1-step."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
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
ax.set_xlim(0, 20)
ax.set_ylim(0, 12)
ax.axis('off')

ax.text(10, 11.5, '人类 vs AI Agent：步骤可靠性', fontsize=38, color=WHITE,
        ha='center', va='top', fontweight='bold', **fp)

# === Human: 1 step ===
ax.text(3, 9.5, '人类', fontsize=30, color=CYAN, ha='center', fontweight='bold', **fp)
ax.text(3, 8.8, '看手机 → 回答', fontsize=18, color=WHITE, ha='center', alpha=0.8, **fp)

# Single big box
box = FancyBboxPatch((1.5, 6), 3, 2.2, boxstyle="round,pad=0.2", facecolor=CYAN, edgecolor='none', alpha=0.8)
ax.add_patch(box)
ax.text(3, 7.1, '1步完成', fontsize=24, color=BG, ha='center', va='center', fontweight='bold', **fp)
ax.text(3, 5.5, '成功率: 95%', fontsize=22, color=CYAN, ha='center', fontweight='bold')

# === Agent: 6 steps ===
ax.text(13, 9.5, 'AI Agent', fontsize=30, color=ORANGE, ha='center', fontweight='bold', **fp)

steps = ['理解\n任务', '搜索\n信息', '分析\n结果', '制定\n方案', '执行\n操作', '验证\n输出']
probs = [0.95, 0.95**2, 0.95**3, 0.95**4, 0.95**5, 0.95**6]

for i, (step, p) in enumerate(zip(steps, probs)):
    x = 8 + i * 2
    # Color gradient from green to red
    r = 1 - p
    g = p
    alpha = 0.9 - i * 0.08
    color = CYAN if p > 0.85 else ORANGE if p > 0.78 else '#FF4444'

    box = FancyBboxPatch((x - 0.8, 6), 1.6, 2.2, boxstyle="round,pad=0.15",
                         facecolor=color, edgecolor='none', alpha=alpha)
    ax.add_patch(box)
    ax.text(x, 7.1, step, fontsize=14, color=BG if p > 0.78 else WHITE,
            ha='center', va='center', fontweight='bold', **fp)
    ax.text(x, 5.5, f'{p:.1%}', fontsize=14, color=color, ha='center', fontweight='bold')

    # Arrow between steps
    if i < 5:
        ax.annotate('', xy=(x + 1, 7.1), xytext=(x + 0.85, 7.1),
                    arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.5, alpha=0.5))

# Probability bar comparison at bottom
ax.text(10, 4.2, '累积成功率对比', fontsize=24, color=WHITE, ha='center', fontweight='bold', **fp)

# Human bar
bar_h = FancyBboxPatch((2, 2.8), 0.95 * 12, 0.8, boxstyle="round,pad=0.05",
                        facecolor=CYAN, edgecolor='none', alpha=0.8)
ax.add_patch(bar_h)
ax.text(1.8, 3.2, '人类', fontsize=16, color=CYAN, ha='right', va='center', **fp)
ax.text(2 + 0.95 * 12 + 0.3, 3.2, '95%', fontsize=18, color=CYAN, ha='left', va='center', fontweight='bold')

# Agent bar
bar_a = FancyBboxPatch((2, 1.5), 0.735 * 12, 0.8, boxstyle="round,pad=0.05",
                        facecolor=ORANGE, edgecolor='none', alpha=0.8)
ax.add_patch(bar_a)
ax.text(1.8, 1.9, 'Agent', fontsize=16, color=ORANGE, ha='right', va='center')
ax.text(2 + 0.735 * 12 + 0.3, 1.9, '73.5%', fontsize=18, color=ORANGE, ha='left', va='center', fontweight='bold')

# Formula
ax.text(14, 1.0, '0.95⁶ = 0.735', fontsize=20, color=PURPLE, ha='center',
        fontweight='bold', style='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=DARK, edgecolor=PURPLE, linewidth=1.5))

plt.tight_layout(pad=1)
plt.savefig('/Users/mik/strange LLM/assets/diagrams/rendered/agent_6_steps.png',
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close()
print("Done: agent_6_steps.png")
