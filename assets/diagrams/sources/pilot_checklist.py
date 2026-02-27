"""P87 - Pilot Preflight Checklist"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from pathlib import Path
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle

# Font setup
CHINESE_FONTS = ['STHeiti', 'PingFang HK', 'Heiti TC', 'PingFang SC', 'Heiti SC', 'SimHei', 'sans-serif']
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
CHECKLIST_BG = '#1A2340'
CHECK_GREEN = '#00D4AA'

fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=150, facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 19.2)
ax.set_ylim(0, 10.8)
ax.set_aspect('equal')
ax.axis('off')

# --- Main checklist card ---
card_x = 3.0
card_y = 0.8
card_w = 13.2
card_h = 9.2

card = FancyBboxPatch((card_x, card_y), card_w, card_h,
                      boxstyle="round,pad=0.15",
                      facecolor=CHECKLIST_BG, edgecolor=DIM,
                      linewidth=2)
ax.add_patch(card)

# Inner border (double border effect)
inner = FancyBboxPatch((card_x + 0.2, card_y + 0.2), card_w - 0.4, card_h - 0.4,
                       boxstyle="round,pad=0.1",
                       facecolor='none', edgecolor=DIM,
                       linewidth=0.8, linestyle='dashed')
ax.add_patch(inner)

# --- Title ---
title_y = card_y + card_h - 1.0
ax.text(9.6, title_y, 'AI 使用前检查清单', fontsize=36, color=WHITE,
        ha='center', va='center', fontweight='bold')

# Airplane icon (draw simple plane shape)
plane_x = 14.2
# Simple plane using lines and triangle
ax.plot([plane_x - 0.4, plane_x + 0.4], [title_y, title_y],
        color=CYAN, linewidth=3, solid_capstyle='round')  # fuselage
ax.fill([plane_x - 0.15, plane_x + 0.15, plane_x],
        [title_y, title_y, title_y + 0.25],
        color=CYAN, alpha=0.8)  # tail
ax.fill([plane_x - 0.05, plane_x + 0.3, plane_x + 0.1],
        [title_y + 0.05, title_y - 0.15, title_y + 0.05],
        color=CYAN, alpha=0.6)  # wing

# "PREFLIGHT CHECKLIST" in English (top right, small)
ax.text(card_x + card_w - 0.5, card_y + card_h - 0.3, 'PREFLIGHT CHECKLIST',
        fontsize=11, color=DIM, ha='right', va='top',
        fontfamily='monospace', fontweight='bold', alpha=0.6)

# Horizontal line under title
ax.plot([card_x + 0.5, card_x + card_w - 0.5],
        [title_y - 0.5, title_y - 0.5],
        color=CYAN, linewidth=2, alpha=0.5)

# --- Checklist items ---
items = [
    ('\u2611', '明确你的真实需求（不是AI能做什么）', True),
    ('\u2611', '设定止损条件（多少轮 / 多少钱 / 多长时间）', True),
    ('\u2611', '确认验收标准（什么算"完成"）', True),
    ('\u2611', '准备人工兜底方案', True),
    ('\u2611', '区分"AI擅长"和"AI自信"', True),
    ('\u2610', '记住：你是机长，AI是副驾驶', False),
]

start_y = title_y - 1.3
item_spacing = 1.15
item_x = card_x + 1.2

for i, (check, text, checked) in enumerate(items):
    y = start_y - i * item_spacing

    # Checkbox
    check_color = CHECK_GREEN if checked else ORANGE
    check_alpha = 1.0 if checked else 0.8

    # Draw checkbox box
    box_size = 0.35
    box = FancyBboxPatch((item_x - 0.05, y - box_size / 2), box_size, box_size,
                         boxstyle="round,pad=0.02",
                         facecolor='none' if not checked else CHECK_GREEN + '22',
                         edgecolor=check_color, linewidth=2, alpha=check_alpha)
    ax.add_patch(box)

    if checked:
        # Draw checkmark
        cx, cy = item_x + 0.12, y
        ax.plot([cx - 0.08, cx - 0.02, cx + 0.1],
                [cy, cy - 0.08, cy + 0.1],
                color=CHECK_GREEN, linewidth=2.5, solid_capstyle='round')
    else:
        # Empty box - leave it empty to show it's unchecked
        pass

    # Item number
    ax.text(item_x + 0.55, y, f'{i + 1}.', fontsize=16, color=DIM,
            ha='left', va='center', fontweight='bold')

    # Item text
    text_color = WHITE if checked else ORANGE
    text_weight = 'normal' if checked else 'bold'
    ax.text(item_x + 0.95, y, text, fontsize=18, color=text_color,
            ha='left', va='center', fontweight=text_weight)

    # Horizontal separator line
    if i < len(items) - 1:
        sep_y = y - item_spacing / 2
        ax.plot([card_x + 0.8, card_x + card_w - 0.8],
                [sep_y, sep_y],
                color=DIM, linewidth=0.5, alpha=0.3, linestyle='dotted')

# --- Last item special note ---
last_y = start_y - (len(items) - 1) * item_spacing
ax.text(card_x + card_w - 1.0, last_y, '<-- 永远保持警惕',
        fontsize=12, color=ORANGE, ha='right', va='center',
        style='italic', alpha=0.7)

# --- Bottom section: signature line ---
sig_y = card_y + 1.0
ax.plot([card_x + 0.5, card_x + card_w - 0.5],
        [sig_y + 0.3, sig_y + 0.3],
        color=DIM, linewidth=1, alpha=0.5)

ax.text(card_x + 1.0, sig_y - 0.1, '机长签字：', fontsize=16, color=DIM,
        ha='left', va='center')
ax.plot([card_x + 3.2, card_x + 6.5], [sig_y - 0.1, sig_y - 0.1],
        color=DIM, linewidth=1)

# Date field
ax.text(card_x + card_w - 5.5, sig_y - 0.1, '日期：', fontsize=16, color=DIM,
        ha='left', va='center')
ax.plot([card_x + card_w - 4.0, card_x + card_w - 1.0],
        [sig_y - 0.1, sig_y - 0.1],
        color=DIM, linewidth=1)

# --- Decorative elements ---
# Corner marks (aviation style)
corner_len = 0.4
corners = [
    (card_x + 0.35, card_y + card_h - 0.35),  # top-left
    (card_x + card_w - 0.35, card_y + card_h - 0.35),  # top-right
    (card_x + 0.35, card_y + 0.35),  # bottom-left
    (card_x + card_w - 0.35, card_y + 0.35),  # bottom-right
]
for cx, cy in corners:
    # Small cross mark
    ax.plot([cx - 0.1, cx + 0.1], [cy, cy], color=DIM, linewidth=0.8, alpha=0.4)
    ax.plot([cx, cx], [cy - 0.1, cy + 0.1], color=DIM, linewidth=0.8, alpha=0.4)

# "CONFIDENTIAL" watermark (very faint)
ax.text(9.6, 5.4, 'CHECKLIST', fontsize=80, color=DIM, alpha=0.03,
        ha='center', va='center', fontweight='bold', fontfamily='monospace',
        rotation=30)

out = Path('/Users/mik/strange LLM/assets/diagrams/rendered/pilot_checklist.png')
fig.savefig(out, dpi=150, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
plt.close()
print(f"Saved: {out}")
