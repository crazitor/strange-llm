#!/usr/bin/env python3
"""Pixel possibility space visualization."""
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
ax.set_xlim(-1, 11)
ax.set_ylim(-0.5, 10.5)
ax.axis('off')

ax.text(5, 10.2, '像素可能性空间：一切图像都"存在"', fontsize=36, color=WHITE,
        ha='center', va='top', fontweight='bold', **fp)

# Background: random noise dots representing the vast space
rng = np.random.RandomState(42)
n = 3000
xs = rng.uniform(0.5, 9.5, n)
ys = rng.uniform(0.5, 8.5, n)
sizes = rng.uniform(0.5, 3, n)
alphas = rng.uniform(0.02, 0.08, n)
for x, y, s, a in zip(xs, ys, sizes, alphas):
    ax.plot(x, y, 'o', color=PURPLE, markersize=s, alpha=a)

# Highlighted specific images as bright points with labels
highlights = [
    (2.5, 6.5, '蒙娜丽莎', CYAN),
    (7, 7, '你的自拍照', ORANGE),
    (4, 3, '明天的报纸头版', '#FF4444'),
    (8, 3.5, '从未被画过的画', PURPLE),
    (1.5, 2, '纯噪声', '#666666'),
    (6, 5.5, '猫穿西装', CYAN),
]

for x, y, label, color in highlights:
    # Glow
    ax.plot(x, y, 'o', color=color, markersize=25, alpha=0.3)
    ax.plot(x, y, 'o', color=color, markersize=12, alpha=0.8)
    ax.plot(x, y, 'o', color=WHITE, markersize=4, alpha=0.9)
    ax.text(x, y - 0.5, label, fontsize=15, color=color, ha='center', va='top',
            fontweight='bold', **fp,
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BG, edgecolor=color, alpha=0.8, linewidth=1))

# Dimension label
ax.text(5, 0.1, '256^(1024×1024×3) 种可能的图片 — 比宇宙中的原子还多',
        fontsize=18, color=WHITE, ha='center', alpha=0.6, **fp)

# "Meaningful images" region outline
theta = np.linspace(0, 2*np.pi, 100)
rx, ry = 2.5, 2
cx, cy = 5, 5.5
ax.plot(cx + rx*np.cos(theta), cy + ry*np.sin(theta), color=CYAN, linewidth=2,
        linestyle='--', alpha=0.4)
ax.text(cx + rx + 0.3, cy + ry, '有意义的图像\n(极小子集)', fontsize=14, color=CYAN,
        alpha=0.6, **fp)

plt.tight_layout(pad=1)
plt.savefig('/Users/mik/strange LLM/assets/diagrams/rendered/pixel_sampling_space.png',
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close()
print("Done: pixel_sampling_space.png")
