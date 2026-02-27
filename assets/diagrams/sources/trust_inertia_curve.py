#!/usr/bin/env python3
"""Trust inertia curve - trust builds then catastrophic failure."""
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

# Data
x = np.arange(1, 26)
# Trust builds gradually over 20 interactions
trust = np.zeros(25)
for i in range(20):
    trust[i] = 0.3 + 0.65 * (1 - np.exp(-i / 5))
# Peak
trust[19] = 0.92
trust[20] = 0.93  # still high just before failure
# Catastrophic failure at 21
trust[21] = 0.15
trust[22] = 0.10
trust[23] = 0.08
trust[24] = 0.05

# Verification effort (inverse)
verify = np.zeros(25)
for i in range(21):
    verify[i] = 0.9 * np.exp(-i / 4) + 0.05
verify[21:] = [0.85, 0.9, 0.92, 0.95]

# Plot trust
ax.fill_between(x[:21], trust[:21], alpha=0.15, color=CYAN)
ax.plot(x[:21], trust[:21], color=CYAN, linewidth=3.5, label='信任度')
# Failure drop
ax.plot(x[20:23], trust[20:23], color='#FF4444', linewidth=4, linestyle='--')
ax.plot(x[22:], trust[22:], color='#FF4444', linewidth=3, alpha=0.6)

# Verification effort
ax.plot(x[:22], verify[:22], color=ORANGE, linewidth=3, linestyle='-.', label='验证力度', alpha=0.8)
ax.plot(x[21:], verify[21:], color=ORANGE, linewidth=3, linestyle='-.', alpha=0.8)

# Danger zone shading
ax.axvspan(20.5, 25.5, alpha=0.1, color='#FF4444')

# Annotations
ax.annotate('信任惯性\nTrust Inertia', xy=(15, trust[14]), xytext=(16.5, 0.55),
            fontsize=22, color=CYAN, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=2),
            ha='center', **fp)

ax.annotate('灾难性失败!\nCatastrophic Failure', xy=(22, trust[21]), xytext=(23, 0.45),
            fontsize=22, color='#FF4444', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#FF4444', lw=2),
            ha='center', **fp)

ax.annotate('验证减少\n"它一直都对"', xy=(18, verify[17]), xytext=(12, 0.15),
            fontsize=16, color=ORANGE,
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.5),
            ha='center', **fp)

# Styling
ax.set_xlabel('AI 交互次数', fontsize=20, color=WHITE, **fp)
ax.set_ylabel('信任度 / 验证力度', fontsize=20, color=WHITE, **fp)
ax.set_title('信任惯性：20次正确 → 第21次的陷阱', fontsize=34, color=WHITE,
             fontweight='bold', pad=20, **fp)

ax.set_xlim(0.5, 25.5)
ax.set_ylim(-0.02, 1.05)
ax.tick_params(colors=WHITE, labelsize=14)
for spine in ax.spines.values():
    spine.set_color(WHITE)
    spine.set_alpha(0.3)

ax.legend(fontsize=18, loc='center right', facecolor=DARK, edgecolor=WHITE,
          labelcolor=WHITE, prop={'family': FONT, 'size': 18})

ax.grid(True, alpha=0.1, color=WHITE)

plt.tight_layout(pad=2)
plt.savefig('/Users/mik/strange LLM/assets/diagrams/rendered/trust_inertia_curve.png',
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close()
print("Done: trust_inertia_curve.png")
