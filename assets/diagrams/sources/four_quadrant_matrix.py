#!/usr/bin/env python3
"""Four quadrant matrix: AI difficulty vs Human difficulty."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
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
ax.set_xlim(-0.5, 10.5)
ax.set_ylim(-0.5, 10.5)
ax.axis('off')

ax.text(5.25, 10.2, 'AI能力矩阵：人类难度 × AI难度', fontsize=36, color=WHITE,
        ha='center', va='top', fontweight='bold', **fp)

# Grid lines
ax.plot([5.25, 5.25], [0.5, 8.5], color=WHITE, linewidth=2, alpha=0.4)
ax.plot([0.5, 10], [4.5, 4.5], color=WHITE, linewidth=2, alpha=0.4)

# Quadrant backgrounds
quads = [
    (0.5, 4.5, 4.75, 4, CYAN, 0.08),     # bottom-left: easy-easy
    (5.25, 4.5, 4.75, 4, ORANGE, 0.12),   # bottom-right: AI hard, human easy = AI blind spot
    (0.5, 0.5, 4.75, 4, PURPLE, 0.08),    # top-left mapped to bottom: human hard, AI easy = AI sweet spot
    (5.25, 0.5, 4.75, 4, '#FF4444', 0.08), # hard-hard
]
# Remap: Y-axis human difficulty (bottom=easy, top=hard), X-axis AI difficulty (left=easy, right=hard)
quads = [
    # AI easy, Human easy (bottom-left)
    (0.6, 0.6, 4.55, 3.8, '#4A90D9', 0.12),
    # AI hard, Human easy (bottom-right) = AI blind spot
    (5.35, 0.6, 4.55, 3.8, ORANGE, 0.15),
    # AI easy, Human hard (top-left) = AI sweet spot
    (0.6, 4.6, 4.55, 3.8, CYAN, 0.15),
    # AI hard, Human hard (top-right)
    (5.35, 4.6, 4.55, 3.8, PURPLE, 0.12),
]
for x, y, w, h, c, a in quads:
    rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.2", facecolor=c, edgecolor=c, alpha=a, linewidth=1)
    ax.add_patch(rect)

# Axis labels
ax.text(5.25, -0.1, 'AI 难度 →', fontsize=22, color=WHITE, ha='center', alpha=0.8, **fp)
ax.text(-0.2, 4.5, '人\n类\n难\n度\n→', fontsize=22, color=WHITE, ha='center', va='center', alpha=0.8, **fp)

# Quadrant titles and examples
# Bottom-left: both easy
ax.text(2.85, 4.0, '都容易', fontsize=24, color='#4A90D9', ha='center', fontweight='bold', **fp)
ax.text(2.85, 3.2, '• 简单问答\n• 基础翻译\n• 格式转换', fontsize=16, color=WHITE, ha='center', alpha=0.8, **fp)

# Bottom-right: AI hard, human easy → AI blind spot
ax.text(7.6, 4.0, 'AI 盲区', fontsize=24, color=ORANGE, ha='center', fontweight='bold', **fp)
ax.text(7.6, 3.0, '• 数数/空间推理\n• 常识判断\n• "草莓有几个r"', fontsize=16, color=WHITE, ha='center', alpha=0.8, **fp)
# Danger icon
ax.text(9.5, 4.0, '⚠', fontsize=30, ha='center', va='center')

# Top-left: AI easy, human hard → AI sweet spot
ax.text(2.85, 8.0, 'AI 甜区', fontsize=24, color=CYAN, ha='center', fontweight='bold', **fp)
ax.text(2.85, 7.0, '• 海量文献综述\n• 多语言翻译\n• 代码生成', fontsize=16, color=WHITE, ha='center', alpha=0.8, **fp)
# Star
ax.text(0.9, 8.0, '★', fontsize=30, color=CYAN, ha='center', va='center')

# Top-right: both hard
ax.text(7.6, 8.0, '都难', fontsize=24, color=PURPLE, ha='center', fontweight='bold', **fp)
ax.text(7.6, 7.0, '• 科学发现\n• 战略决策\n• 创造性突破', fontsize=16, color=WHITE, ha='center', alpha=0.8, **fp)

# Corner labels
ax.text(0.6, 0.3, '易', fontsize=16, color=WHITE, alpha=0.5, **fp)
ax.text(9.7, 0.3, '难', fontsize=16, color=WHITE, alpha=0.5, **fp)
ax.text(0.2, 0.6, '易', fontsize=16, color=WHITE, alpha=0.5, **fp)
ax.text(0.2, 8.2, '难', fontsize=16, color=WHITE, alpha=0.5, **fp)

plt.tight_layout(pad=1)
plt.savefig('/Users/mik/strange LLM/assets/diagrams/rendered/four_quadrant_matrix.png',
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close()
print("Done: four_quadrant_matrix.png")
