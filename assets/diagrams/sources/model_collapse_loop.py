#!/usr/bin/env python3
"""Model collapse loop diagram."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

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
ax.set_xlim(-1, 11)
ax.set_ylim(-0.5, 11)
ax.axis('off')

ax.text(5, 10.5, '模型坍缩 Model Collapse', fontsize=40, color=WHITE,
        ha='center', va='top', fontweight='bold', **fp)

# Circular layout - 4 nodes
cx, cy, r = 5, 5, 3
angles = [90, 0, 270, 180]  # top, right, bottom, left
nodes = [
    ('AI 生成内容', '文章/图片/代码', CYAN),
    ('内容进入互联网', '混入训练数据', ORANGE),
    ('用于训练新模型', '合成数据污染', PURPLE),
    ('模型质量下降', '多样性丧失', RED),
]

positions = []
for angle in angles:
    rad = np.radians(angle)
    positions.append((cx + r * np.cos(rad), cy + r * np.sin(rad)))

# Draw nodes
for (x, y), (title, sub, color), angle in zip(positions, nodes, angles):
    box = FancyBboxPatch((x-1.3, y-0.7), 2.6, 1.4, boxstyle="round,pad=0.2",
                         facecolor=DARK, edgecolor=color, linewidth=2.5)
    ax.add_patch(box)
    ax.text(x, y+0.15, title, fontsize=18, color=color, ha='center', va='center',
            fontweight='bold', **fp)
    ax.text(x, y-0.35, sub, fontsize=12, color=WHITE, ha='center', va='center', alpha=0.6, **fp)

# Draw curved arrows between nodes
arrow_style = "Simple,tail_width=3,head_width=12,head_length=8"
for i in range(4):
    j = (i + 1) % 4
    x1, y1 = positions[i]
    x2, y2 = positions[j]
    # Midpoint offset for curve
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    # Offset toward center for inner curve
    dx = mx - cx
    dy = my - cy
    dist = np.sqrt(dx**2 + dy**2)
    # Arrow connection points (edge of boxes)
    a1 = np.degrees(np.arctan2(y2-y1, x2-x1))

    arrow = FancyArrowPatch(
        (x1, y1), (x2, y2),
        connectionstyle=f"arc3,rad=0.3",
        arrowstyle='->', color=WHITE, linewidth=2.5, alpha=0.6,
        mutation_scale=20
    )
    ax.add_patch(arrow)

# Center: degradation spiral
for i, (radius, alpha) in enumerate([(1.8, 0.06), (1.3, 0.08), (0.8, 0.12)]):
    circle = plt.Circle((cx, cy), radius, facecolor=RED, edgecolor='none', alpha=alpha)
    ax.add_patch(circle)

ax.text(cx, cy+0.3, '恶性循环', fontsize=24, color=RED, ha='center', va='center',
        fontweight='bold', **fp)
ax.text(cx, cy-0.3, 'Vicious Cycle', fontsize=14, color=RED, ha='center', va='center', alpha=0.6)

# Generation labels on arrows
gen_labels = ['第1代', '第2代', '第3代', '第N代...']
gen_positions = [
    (cx + 2.2, cy + 2.2),
    (cx + 2.2, cy - 2.2),
    (cx - 2.2, cy - 2.2),
    (cx - 2.2, cy + 2.2),
]
for (x, y), label in zip(gen_positions, gen_labels):
    ax.text(x, y, label, fontsize=13, color=WHITE, ha='center', va='center',
            alpha=0.4, **fp)

# Bottom note
ax.text(5, 0, '每一代训练数据中AI生成内容占比增加 → 多样性递减 → 模型退化',
        fontsize=16, color=WHITE, ha='center', alpha=0.5, **fp)

plt.tight_layout(pad=1)
plt.savefig('/Users/mik/strange LLM/assets/diagrams/rendered/model_collapse_loop.png',
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close()
print("Done: model_collapse_loop.png")
