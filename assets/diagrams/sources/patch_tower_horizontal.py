"""
Patch Tower Horizontal — 4 variants of the core PPT visual.
The "Patch Tower" is a horizontal (left-to-right) stacked structure
representing how AI models are built layer upon layer of patches.

Outputs:
  patch_tower_v1.png  (P4  - first glimpse)
  patch_tower_v2.png  (P18 - full panorama)
  patch_tower_v3.png  (P30 - missing stop-loss layer)
  patch_tower_v4.png  (P45 - ceiling / diminishing returns)
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
from pathlib import Path

# ── Font setup ──
import matplotlib.font_manager as fm
CHINESE_FONTS = ['PingFang HK', 'STHeiti', 'Heiti TC', 'Heiti SC',
                 'PingFang SC', 'SimHei', 'sans-serif']

def get_chinese_font():
    available = {f.name for f in fm.fontManager.ttflist}
    for name in CHINESE_FONTS:
        if name in available:
            return name
    return 'sans-serif'

FONT = get_chinese_font()
plt.rcParams['font.family'] = FONT
plt.rcParams['axes.unicode_minus'] = False

# ── Colors ──
BG     = '#0F1729'
CYAN   = '#00D4AA'
ORANGE = '#FF6B35'
WHITE  = '#FFFFFF'
DIM    = '#6B7280'
GRID   = '#1E2A42'
RED    = '#FF4444'

OUT_DIR = Path('/Users/mik/strange LLM/assets/diagrams/rendered')

# ── Cyan gradient palette (lighter to darker) ──
CYAN_SHADES = [
    '#00FFD0',  # brightest
    '#00E8BE',
    '#00D4AA',
    '#00BF98',
    '#00AA85',
    '#009573',
    '#008060',
    '#006B4E',
    '#00563C',
    '#00412A',
]

def make_shade(idx, total):
    """Pick a CYAN shade based on position in list."""
    pos = int(idx / max(total - 1, 1) * (len(CYAN_SHADES) - 1))
    return CYAN_SHADES[min(pos, len(CYAN_SHADES) - 1)]


def draw_tower_block(ax, x, y, w, h, color, label, fontsize=16, alpha=1.0,
                     linestyle='-', edgecolor=None, text_color=WHITE,
                     linewidth=2, icon=None):
    """Draw a single rounded-rectangle tower block with label."""
    ec = edgecolor if edgecolor else color
    box = mpatches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle=mpatches.BoxStyle("Round", pad=0.15),
        facecolor=color, edgecolor=ec, linewidth=linewidth,
        alpha=alpha, linestyle=linestyle, zorder=5
    )
    ax.add_patch(box)
    display_text = label
    if icon:
        display_text = f"{icon} {label}"
    ax.text(x + w / 2, y + h / 2, display_text,
            fontsize=fontsize, color=text_color, fontweight='bold',
            ha='center', va='center', zorder=6,
            path_effects=[pe.withStroke(linewidth=3, foreground=BG)])


def setup_fig():
    fig, ax = plt.subplots(figsize=(19.2, 10.8), facecolor=BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 56.25)
    ax.set_aspect('equal')
    ax.axis('off')
    return fig, ax


# ═══════════════════════════════════════════════════════
# V1: First glimpse — 7 basic layers
# ═══════════════════════════════════════════════════════
def render_v1():
    fig, ax = setup_fig()
    layers = [
        "大模型\n(文字接龙)",
        "训练数据",
        "RLHF\n对齐",
        "Prompt\n工程",
        "RAG\n检索",
        "Agent\n框架",
        "MCP\n工具",
    ]
    n = len(layers)
    total_w = 82
    gap = 1.0
    block_w = (total_w - gap * (n - 1)) / n
    block_h = 14
    start_x = 9
    y_center = 22

    # Draw blocks left to right
    for i, label in enumerate(layers):
        x = start_x + i * (block_w + gap)
        color = make_shade(i, n)
        draw_tower_block(ax, x, y_center, block_w, block_h, color, label,
                         fontsize=15)

    # Arrow + annotation: "底层只有一块砖"
    base_x = start_x + block_w / 2
    ax.annotate('',
                xy=(base_x, y_center - 0.5),
                xytext=(base_x, y_center - 6),
                arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2.5),
                zorder=7)
    ax.text(base_x, y_center - 8, '底层只有一块砖',
            fontsize=18, color=ORANGE, fontweight='bold',
            ha='center', va='top', zorder=8,
            path_effects=[pe.withStroke(linewidth=3, foreground=BG)])

    # Direction arrow at the top
    ax.annotate('',
                xy=(start_x + total_w + 2, y_center + block_h / 2),
                xytext=(start_x - 2, y_center + block_h / 2),
                arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5,
                                linestyle='--'),
                zorder=3)
    ax.text(start_x + total_w / 2, y_center + block_h + 3,
            '层层叠加',
            fontsize=16, color=DIM, ha='center', va='center', zorder=4)

    # Title
    ax.text(50, 50, '补丁之塔 -- AI的真实架构',
            fontsize=30, color=WHITE, fontweight='bold',
            ha='center', va='center', zorder=10,
            path_effects=[pe.withStroke(linewidth=4, foreground=BG)])

    out = OUT_DIR / 'patch_tower_v1.png'
    fig.savefig(out, dpi=150, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print(f'Saved -> {out}  ({out.stat().st_size / 1024:.0f} KB)')


# ═══════════════════════════════════════════════════════
# V2: Full panorama — 10 layers with icons
# ═══════════════════════════════════════════════════════
def render_v2():
    fig, ax = setup_fig()
    layers = [
        ("大模型\n(Transformer)", None),
        ("训练数据", None),
        ("RLHF\n对齐", None),
        ("Fine-\ntuning", None),
        ("Prompt\n工程", None),
        ("Context\nWindow", None),
        ("RAG\n检索", None),
        ("Memory", None),
        ("Agent\n框架", None),
        ("MCP\n工具", None),
    ]
    n = len(layers)
    total_w = 88
    gap = 0.8
    block_w = (total_w - gap * (n - 1)) / n
    block_h = 13
    start_x = 6
    y_center = 20

    for i, (label, icon) in enumerate(layers):
        x = start_x + i * (block_w + gap)
        color = make_shade(i, n)
        draw_tower_block(ax, x, y_center, block_w, block_h, color, label,
                         fontsize=13, icon=icon)

    # Right-side annotation
    ax.text(96, y_center + block_h / 2, '10个名词\n1座塔',
            fontsize=20, color=CYAN, fontweight='bold',
            ha='center', va='center', zorder=8,
            path_effects=[pe.withStroke(linewidth=3, foreground=BG)])

    # Direction arrow
    ax.annotate('',
                xy=(start_x + total_w + 1, y_center + block_h + 2),
                xytext=(start_x - 1, y_center + block_h + 2),
                arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5,
                                linestyle='--'),
                zorder=3)
    ax.text(start_x + total_w / 2, y_center + block_h + 4.5,
            '层层堆叠, 从左到右',
            fontsize=15, color=DIM, ha='center', va='center', zorder=4)

    # Base annotation
    base_x = start_x + block_w / 2
    ax.annotate('',
                xy=(base_x, y_center - 0.5),
                xytext=(base_x, y_center - 5),
                arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2),
                zorder=7)
    ax.text(base_x + 1, y_center - 7, '基座: Transformer',
            fontsize=15, color=ORANGE, fontweight='bold',
            ha='center', va='top', zorder=8,
            path_effects=[pe.withStroke(linewidth=3, foreground=BG)])

    # Title
    ax.text(50, 50, '补丁之塔 -- 全景',
            fontsize=30, color=WHITE, fontweight='bold',
            ha='center', va='center', zorder=10,
            path_effects=[pe.withStroke(linewidth=4, foreground=BG)])

    out = OUT_DIR / 'patch_tower_v2.png'
    fig.savefig(out, dpi=150, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print(f'Saved -> {out}  ({out.stat().st_size / 1024:.0f} KB)')


# ═══════════════════════════════════════════════════════
# V3: Missing stop-loss layer
# ═══════════════════════════════════════════════════════
def render_v3():
    fig, ax = setup_fig()
    # Same 10 layers but insert a "missing" layer between Agent框架 and MCP工具
    layers = [
        ("大模型\n(Transformer)", False),
        ("训练数据", False),
        ("RLHF\n对齐", False),
        ("Fine-\ntuning", False),
        ("Prompt\n工程", False),
        ("止损\n(Stop-Loss)", True),   # <-- MISSING layer
        ("Context\nWindow", False),
        ("RAG\n检索", False),
        ("Agent\n框架", False),
        ("MCP\n工具", False),
    ]
    n = len(layers)
    total_w = 88
    gap = 0.8
    block_w = (total_w - gap * (n - 1)) / n
    block_h = 13
    start_x = 6
    y_center = 20

    for i, (label, is_missing) in enumerate(layers):
        x = start_x + i * (block_w + gap)
        if is_missing:
            # Draw red dashed empty box
            draw_tower_block(ax, x, y_center, block_w, block_h,
                             color='none', label=label,
                             fontsize=13, alpha=0.9,
                             linestyle='--', edgecolor=RED,
                             text_color=RED, linewidth=3)
            # Warning annotation
            ax.text(x + block_w / 2, y_center - 3.5,
                    '缺失!',
                    fontsize=20, color=RED, fontweight='bold',
                    ha='center', va='top', zorder=8,
                    path_effects=[pe.withStroke(linewidth=3, foreground=BG)])
            # Warning icon above
            ax.text(x + block_w / 2, y_center + block_h + 2.5,
                    '!',
                    fontsize=28, color=RED, fontweight='bold',
                    ha='center', va='center', zorder=8,
                    path_effects=[pe.withStroke(linewidth=4, foreground=BG)])
            # Glow around the missing block
            glow = mpatches.FancyBboxPatch(
                (x - 0.5, y_center - 0.5), block_w + 1, block_h + 1,
                boxstyle=mpatches.BoxStyle("Round", pad=0.3),
                facecolor=RED, edgecolor='none', linewidth=0,
                alpha=0.08, zorder=3
            )
            ax.add_patch(glow)
        else:
            color = make_shade(i if i < 5 else i - 1, n - 1)
            draw_tower_block(ax, x, y_center, block_w, block_h, color, label,
                             fontsize=13)

    # Title
    ax.text(50, 50, '补丁之塔 -- 缺了一层',
            fontsize=30, color=WHITE, fontweight='bold',
            ha='center', va='center', zorder=10,
            path_effects=[pe.withStroke(linewidth=4, foreground=BG)])

    # Subtitle
    ax.text(50, 45, '"所有的补丁都在让它更强，但没有一层在告诉它何时该停"',
            fontsize=17, color=DIM, ha='center', va='center',
            fontstyle='italic', zorder=9,
            path_effects=[pe.withStroke(linewidth=3, foreground=BG)])

    out = OUT_DIR / 'patch_tower_v3.png'
    fig.savefig(out, dpi=150, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print(f'Saved -> {out}  ({out.stat().st_size / 1024:.0f} KB)')


# ═══════════════════════════════════════════════════════
# V4: Ceiling — diminishing returns
# ═══════════════════════════════════════════════════════
def render_v4():
    fig, ax = setup_fig()
    layers = [
        "大模型\n(Transformer)",
        "训练数据",
        "RLHF\n对齐",
        "Fine-\ntuning",
        "Prompt\n工程",
        "Context\nWindow",
        "RAG\n检索",
        "Memory",
        "Agent\n框架",
        "MCP\n工具",
    ]
    n = len(layers)
    total_w = 88
    gap = 0.8
    block_w = (total_w - gap * (n - 1)) / n
    block_h = 13
    start_x = 6
    y_center = 16

    # Ceiling line
    ceiling_y = y_center + block_h + 5
    ax.plot([start_x - 2, start_x + total_w + 2], [ceiling_y, ceiling_y],
            color=RED, linewidth=3.5, linestyle='--', alpha=0.85, zorder=8)

    # Label above ceiling
    ax.text(50, ceiling_y + 4, '无论怎么叠, 到不了这里',
            fontsize=22, color=RED, fontweight='bold',
            ha='center', va='center', zorder=9,
            path_effects=[pe.withStroke(linewidth=4, foreground=BG)])

    # Small upward arrows hitting the ceiling
    for cx in [25, 50, 75]:
        ax.annotate('',
                    xy=(cx, ceiling_y - 0.3),
                    xytext=(cx, ceiling_y - 4),
                    arrowprops=dict(arrowstyle='->', color=RED, lw=1.8,
                                    alpha=0.5),
                    zorder=7)

    # Draw blocks with fading alpha for the rightmost ones
    for i, label in enumerate(layers):
        x = start_x + i * (block_w + gap)
        color = make_shade(i, n)
        # Rightmost 3 layers get progressively dimmer
        if i >= n - 3:
            fade = 0.8 - (i - (n - 3)) * 0.2  # 0.8, 0.6, 0.4
        else:
            fade = 1.0
        draw_tower_block(ax, x, y_center, block_w, block_h, color, label,
                         fontsize=13, alpha=fade)

    # Label: diminishing returns on the right
    ax.text(start_x + total_w - 2, y_center - 3.5,
            '递减回报 Diminishing Returns',
            fontsize=15, color=ORANGE, fontweight='bold',
            ha='right', va='top', zorder=8,
            fontstyle='italic',
            path_effects=[pe.withStroke(linewidth=3, foreground=BG)])
    # Arrow showing diminishing
    ax.annotate('',
                xy=(start_x + total_w, y_center - 1),
                xytext=(start_x + total_w - 25, y_center - 1),
                arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2,
                                alpha=0.6),
                zorder=7)

    # Title
    ax.text(50, 50, '补丁之塔 -- 极限',
            fontsize=30, color=WHITE, fontweight='bold',
            ha='center', va='center', zorder=10,
            path_effects=[pe.withStroke(linewidth=4, foreground=BG)])

    # Subtitle
    ax.text(50, 45.5, '"每多叠一层, 提升越来越小"',
            fontsize=17, color=DIM, ha='center', va='center',
            fontstyle='italic', zorder=9,
            path_effects=[pe.withStroke(linewidth=3, foreground=BG)])

    out = OUT_DIR / 'patch_tower_v4.png'
    fig.savefig(out, dpi=150, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print(f'Saved -> {out}  ({out.stat().st_size / 1024:.0f} KB)')


# ═══════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════
if __name__ == '__main__':
    render_v1()
    render_v2()
    render_v3()
    render_v4()
    print('\nAll 4 patch tower variants rendered.')
