/**
 * build_pptx_v5.js — AI科普演讲 PptxGenJS 构建脚本
 *
 * 运行: node scripts/build_pptx_v5.js
 * 输出: output/presentation_v5.pptx
 */

const pptxgen = require("pptxgenjs");
const path = require("path");
const fs = require("fs");

// ═══════════════════════════════════════════════
// CONFIG
// ═══════════════════════════════════════════════

const ROOT = path.resolve(__dirname, "..");
const SCREENSHOTS = path.join(ROOT, "output", "screenshots");
const DIAGRAMS = path.join(ROOT, "assets", "diagrams", "rendered");
const OUTPUT = path.join(ROOT, "output", "presentation_v5.pptx");

const C = {
  darkBg:     "1E2761",
  lightBg:    "F5F5F0",
  accent1:    "00D4AA",  // teal — highlights, progress
  accent2:    "FF6B35",  // orange — warnings, emphasis
  textDark:   "2D2D2D",
  textLight:  "E8E8E8",
  mutedOnDark:  "B8C0D4",  // muted text on dark bg (blue-gray, ~4.5:1)
  mutedOnLight: "666666",  // muted text on light bg (dark gray, ~5.5:1)
  white:      "FFFFFF",
  black:      "111111",
  midDark:    "2A3A6B",  // slightly lighter navy
  darkOverlay:"0D1530",  // very dark for overlays
};

const FONT = {
  title:  "PingFang SC",
  body:   "PingFang SC",
  mono:   "Menlo",
};

// Per-act color themes — each act gets its own dark bg + accent
const ACT_THEME = {
  def:   { bg: "1E2761", accent: "00D4AA", alt: "FF6B35" },
  act01: { bg: "162050", accent: "00D4AA", alt: "4EEACC" },
  act02: { bg: "2D1535", accent: "FF6B35", alt: "FF9A6C" },
  act03: { bg: "1A1845", accent: "7C6BF0", alt: "A594FF" },
  act04: { bg: "122838", accent: "4FC3F7", alt: "81D4FA" },
  act05: { bg: "1A2B20", accent: "66BB6A", alt: "81C784" },
  act06: { bg: "2E1A1A", accent: "EF5350", alt: "E57373" },
  act07: { bg: "2A2510", accent: "FFD54F", alt: "FFE082" },
};
const ACT_MAP = {
  "\u5E8F\u5E55": ACT_THEME.def, "\u7B2C\u4E00\u5E55": ACT_THEME.act01,
  "\u7B2C\u4E8C\u5E55": ACT_THEME.act02, "\u7B2C\u4E09\u5E55": ACT_THEME.act03,
  "\u7B2C\u56DB\u5E55": ACT_THEME.act04, "\u7B2C\u4E94\u5E55": ACT_THEME.act05,
  "\u7B2C\u516D\u5E55": ACT_THEME.act06, "\u7B2C\u4E03\u5E55": ACT_THEME.act07,
};
function getAT(label) { return ACT_MAP[label] || ACT_THEME.def; }

const SIZE = {
  title: 24,        // content/comparison titles
  actTitle: 40,     // act title pages
  coverTitle: 44,   // cover page
  body: 16,         // body text
  bullet: 15,       // bullet items
  caption: 14,      // screenshot captions
  ssTitle: 18,      // screenshot titles
  stat: 72,         // stat big number
  cardTitle: 15,    // card titles
  cardBody: 13,     // card body text
  small: 11,        // hints, journey labels
  actLabel: 10,     // act label
  kpDefault: 30,    // keyPhrase default
  quoteDefault: 22, // quote default
};

// Slide dimensions (LAYOUT_16x9): 10" x 5.625"
const W = 10;
const H = 5.625;
const MARGIN = 0.5;

// ═══════════════════════════════════════════════
// HELPER: screenshot/diagram path
// ═══════════════════════════════════════════════

function screenshot(name) {
  const p = path.join(SCREENSHOTS, name);
  if (!fs.existsSync(p)) console.warn("⚠ Missing screenshot:", name);
  return p;
}

function diagram(name) {
  const p = path.join(DIAGRAMS, name);
  if (!fs.existsSync(p)) console.warn("⚠ Missing diagram:", name);
  return p;
}

// ═══════════════════════════════════════════════
// LAYOUT FUNCTIONS
// ═══════════════════════════════════════════════

function addProgressBar(slide, progress, total, accentColor) {
  const ratio = progress / total;
  const barH = 0.07;
  const barColor = accentColor || C.accent1;
  // Background track
  slide.addShape("rect", {
    x: 0, y: H - barH, w: W, h: barH,
    fill: { color: C.darkBg, transparency: 70 },
  });
  // Progress fill
  if (ratio > 0) {
    slide.addShape("rect", {
      x: 0, y: H - barH, w: W * ratio, h: barH,
      fill: { color: barColor },
    });
  }
}

function addActLabel(slide, actName, isDark) {
  slide.addText(actName, {
    x: W - 2.5, y: 0.15, w: 2.2, h: 0.3,
    fontSize: SIZE.actLabel, fontFace: FONT.body,
    color: isDark ? C.mutedOnDark : C.mutedOnLight,
    align: "right", valign: "middle", margin: 0,
  });
}

// ----- COVER -----
function layoutCover(pres, data, idx, total) {
  const slide = pres.addSlide();
  slide.background = { color: C.darkBg };

  // Decorative accent circle (top right)
  slide.addShape("ellipse", {
    x: 7.5, y: -1.2, w: 4, h: 4,
    fill: { color: C.accent1, transparency: 85 },
  });

  // Title
  slide.addText(data.title, {
    x: 1, y: 1.3, w: 8, h: 1.5,
    fontSize: 44, fontFace: FONT.title, color: C.white,
    bold: true, align: "left", valign: "middle", margin: 0,
  });

  // Subtitle
  if (data.subtitle) {
    slide.addText(data.subtitle, {
      x: 1, y: 2.9, w: 7, h: 0.8,
      fontSize: 18, fontFace: FONT.body, color: C.accent1,
      align: "left", valign: "top", margin: 0,
    });
  }

  // Bottom info line
  if (data.info) {
    slide.addText(data.info, {
      x: 1, y: H - 0.8, w: 8, h: 0.4,
      fontSize: 12, fontFace: FONT.body, color: C.mutedOnDark,
      align: "left", valign: "bottom", margin: 0,
    });
  }

  if (data.notes) slide.addNotes(data.notes);
}

// ----- ACT TITLE -----
function drawActAccent(slide, shape, atColors) {
  const _ac = atColors ? atColors.accent : C.accent1;
  const _al = atColors ? atColors.alt : C.accent2;
  const baseX = 7.0;
  switch (shape) {
    case "layers": // Act 01: stacked blocks
      for (let i = 0; i < 4; i++) {
        slide.addShape("rect", {
          x: baseX + i * 0.15, y: 1.0 + i * 0.9, w: 2.2 - i * 0.3, h: 0.7,
          fill: { color: _ac, transparency: 60 + i * 8 },
          rectRadius: 0.05,
        });
      }
      break;
    case "warnStripe": // Act 02: warning stripes (orange)
      for (let i = 0; i < 5; i++) {
        slide.addShape("rect", {
          x: baseX + 0.3, y: 0.6 + i * 0.95, w: 2.5, h: 0.35,
          fill: { color: _al, transparency: 50 + i * 6 },
          rotate: -12,
        });
      }
      break;
    case "crack": // Act 03: split/crack line
      slide.addShape("line", {
        x: baseX + 1.2, y: 0.3, w: 0, h: 4.8,
        line: { color: _al, width: 3, dashType: "dash" },
      });
      slide.addShape("line", {
        x: baseX + 1.0, y: 0.3, w: 0.4, h: 4.8,
        line: { color: _ac, width: 1.5, transparency: 50 },
      });
      break;
    case "target": // Act 04: concentric circles
      for (let i = 3; i >= 0; i--) {
        const size = 0.6 + i * 0.7;
        slide.addShape("ellipse", {
          x: baseX + 1.2 - size / 2, y: 2.2 - size / 2, w: size, h: size,
          line: { color: _ac, width: 1.5, transparency: 30 + i * 15 },
          fill: { color: _ac, transparency: 90 - i * 5 },
        });
      }
      break;
    case "fork": // Act 05: forking paths
      slide.addShape("line", {
        x: baseX + 0.5, y: 3.5, w: 0.8, h: -2.0,
        line: { color: _ac, width: 2, transparency: 40 },
      });
      slide.addShape("line", {
        x: baseX + 1.3, y: 1.5, w: 0.8, h: -1.0,
        line: { color: _ac, width: 2, transparency: 50 },
      });
      slide.addShape("line", {
        x: baseX + 1.3, y: 1.5, w: 1.0, h: 0.5,
        line: { color: _al, width: 2, transparency: 50 },
      });
      break;
    case "scalpel": // Act 06: three cuts
      for (let i = 0; i < 3; i++) {
        slide.addShape("line", {
          x: baseX + 0.5 + i * 0.6, y: 0.8, w: 0, h: 3.5,
          line: { color: i === 1 ? _al : _ac, width: 2, transparency: 40 },
        });
        slide.addShape("rect", {
          x: baseX + 0.35 + i * 0.6, y: 0.5, w: 0.3, h: 0.4,
          fill: { color: i === 1 ? _al : _ac, transparency: 50 },
          rectRadius: 0.03,
        });
      }
      break;
    case "trident": // Act 07: three-way fork
      slide.addShape("line", {
        x: baseX + 1.1, y: 3.5, w: 0, h: -1.5,
        line: { color: _ac, width: 2.5, transparency: 40 },
      });
      slide.addShape("line", {
        x: baseX + 1.1, y: 2.0, w: -0.9, h: -1.5,
        line: { color: _ac, width: 2, transparency: 50 },
      });
      slide.addShape("line", {
        x: baseX + 1.1, y: 2.0, w: 0, h: -1.5,
        line: { color: _al, width: 2, transparency: 50 },
      });
      slide.addShape("line", {
        x: baseX + 1.1, y: 2.0, w: 0.9, h: -1.5,
        line: { color: "6C63FF", width: 2, transparency: 50 },
      });
      break;
  }
}

function layoutActTitle(pres, data, idx, total) {
  const slide = pres.addSlide();
  const at = data.actNum ? (ACT_THEME['act' + data.actNum] || ACT_THEME.def) : getAT(data.actLabel || '');
  slide.background = { color: at.bg };

  // Decorative accent shape (drawn first, behind text)
  if (data.accentShape) {
    drawActAccent(slide, data.accentShape, at);
  }

  // Large act number
  if (data.actNum) {
    slide.addText(data.actNum, {
      x: 0.8, y: 0.8, w: 2, h: 1.2,
      fontSize: 72, fontFace: FONT.title, color: at.accent,
      bold: true, align: "left", valign: "middle", margin: 0,
      transparency: 30,
    });
  }

  // Title
  slide.addText(data.title, {
    x: 1, y: 2.0, w: 5.5, h: 1.2,
    fontSize: 40, fontFace: FONT.title, color: C.white,
    bold: true, align: "left", valign: "middle", margin: 0,
  });

  // Subtitle
  if (data.subtitle) {
    slide.addText(data.subtitle, {
      x: 1, y: 3.3, w: 5.5, h: 0.6,
      fontSize: 16, fontFace: FONT.body, color: C.mutedOnDark,
      align: "left", valign: "top", margin: 0,
    });
  }

  addProgressBar(slide, idx, total, at.accent);
  if (data.notes) slide.addNotes(data.notes);
}

// ----- KEY PHRASE (4 rotating visual styles) -----
let _kpIdx = 0;
function layoutKeyPhrase(pres, data, idx, total) {
  const slide = pres.addSlide();
  const at = getAT(data.actLabel);
  const isDark = data.darkBg !== false;
  const textColor = isDark ? C.white : C.textDark;
  const isCenter = !!data.centered;
  const variant = data.bgGradient ? -1 : (_kpIdx % 4);
  _kpIdx++;

  // ── Background ──
  if (variant === -1) {
    // Gradient mode (e.g. "最黑暗的时刻")
    slide.background = { color: C.darkOverlay };
    slide.addShape("rect", { x: 0, y: 0, w: W, h: H * 0.55,
      fill: { color: at.bg, transparency: 30 } });
    slide.addShape("rect", { x: 0, y: H * 0.55, w: W, h: H * 0.45,
      fill: { color: C.darkOverlay, transparency: 10 } });
  } else {
    slide.background = { color: isDark ? at.bg : C.lightBg };
  }

  // ── Decorative elements per variant ──
  const ac = at.accent;
  const ac2 = at.alt;
  if (variant === 0) {
    // SPOTLIGHT — large semi-transparent circle
    slide.addShape("ellipse", {
      x: 5.2, y: -0.5, w: 6, h: 6,
      fill: { color: ac, transparency: 82 },
    });
    slide.addShape("ellipse", {
      x: 5.8, y: 0.1, w: 4.5, h: 4.5,
      fill: { color: ac, transparency: 88 },
    });
  } else if (variant === 1) {
    // DIAGONAL — thick angled stripe (lowered to avoid text overlap)
    slide.addShape("rect", {
      x: -2, y: 4.0, w: 14, h: 1.4,
      fill: { color: ac, transparency: 90 },
      rotate: -4,
    });
  } else if (variant === 2) {
    // SIDE PANEL — bold color block on left
    slide.addShape("rect", {
      x: 0, y: 0, w: 0.5, h: H,
      fill: { color: ac, transparency: 30 },
    });
    slide.addShape("rect", {
      x: 0.5, y: 0, w: 0.12, h: H,
      fill: { color: ac2, transparency: 50 },
    });
  } else if (variant === 3) {
    // BOTTOM GLOW — colored band at bottom (lowered to avoid sub-phrase)
    slide.addShape("rect", {
      x: 0, y: H * 0.82, w: W, h: H * 0.18,
      fill: { color: ac, transparency: 80 },
    });
    slide.addShape("rect", {
      x: 0, y: H * 0.80, w: W * 0.5, h: 0.03,
      fill: { color: ac, transparency: 35 },
    });
  }

  // ── Text positioning ──
  const pX = isCenter ? 0.8 : (variant === 2 ? 1.4 : 1.0);
  const pW = isCenter ? 8.4 : (variant === 0 ? 6.5 : 8.0);
  const pY = data.sub ? 0.5 : 0.4;
  const pH = data.sub ? 3.0 : 4.4;
  const align = isCenter ? "center" : "left";

  // ── Main phrase ──
  if (data.richPhrase) {
    const runs = data.richPhrase.map(r => ({
      text: r.text,
      options: {
        fontSize: r.fontSize || data.fontSize || SIZE.kpDefault,
        fontFace: FONT.title,
        color: r.color || textColor,
        bold: r.bold !== false,
        italic: !!r.italic,
        strike: !!r.strike,
      },
    }));
    slide.addText(runs, {
      x: pX, y: pY, w: pW, h: pH,
      align: align, valign: "middle", margin: 0,
      lineSpacingMultiple: 1.4,
    });
  } else {
    slide.addText(data.phrase, {
      x: pX, y: pY, w: pW, h: pH,
      fontSize: data.fontSize || SIZE.kpDefault, fontFace: FONT.title,
      color: textColor, bold: true,
      align: align, valign: "middle", margin: 0,
      lineSpacingMultiple: 1.4,
    });
  }

  // ── Sub-phrase ──
  if (data.sub) {
    slide.addText(data.sub, {
      x: pX, y: 3.9, w: pW, h: 0.7,
      fontSize: 16, fontFace: FONT.body,
      color: isDark ? C.mutedOnDark : C.mutedOnLight,
      align: align, valign: "top", margin: 0,
    });
  }

  if (data.actLabel) addActLabel(slide, data.actLabel, isDark);
  addProgressBar(slide, idx, total, at.accent);
  if (data.notes) slide.addNotes(data.notes);
}

// ----- CONTENT (text + optional image right) -----
function layoutContent(pres, data, idx, total) {
  const slide = pres.addSlide();
  const at = getAT(data.actLabel);
  slide.background = { color: C.lightBg };

  // Thick left accent block (act-colored, replaces thin teal bar)
  slide.addShape("rect", {
    x: 0, y: 0, w: 0.35, h: H,
    fill: { color: at.accent, transparency: 15 },
  });
  slide.addShape("rect", {
    x: 0.35, y: 0, w: 0.06, h: H,
    fill: { color: at.accent, transparency: 60 },
  });

  // Title
  if (data.title) {
    slide.addText(data.title, {
      x: 0.65, y: 0.3, w: data.image ? 5 : 8.8, h: 0.6,
      fontSize: SIZE.title, fontFace: FONT.title, color: C.textDark,
      bold: true, align: "left", valign: "middle", margin: 0,
    });
  }

  // Body text
  const bodyY = data.title ? 1.1 : 0.5;
  const bodyW = data.image ? 5 : 9;
  const bodyH = data.image ? 3.8 : (H - bodyY - 0.7);

  if (data.body) {
    const bodyContent = Array.isArray(data.body) ? data.body : [{
      text: data.body,
      options: { fontSize: SIZE.body, fontFace: FONT.body, color: C.textDark, lineSpacingMultiple: 1.5 },
    }];
    const bodyVAlign = (!data.image && !data.bullets) ? "middle" : "top";
    slide.addText(bodyContent, {
      x: 0.6, y: bodyY, w: bodyW, h: bodyH,
      valign: bodyVAlign, margin: 0,
    });
  }

  // Bullets: card mode or standard
  if (data.bullets && data.cardBullets) {
    // Card bullets: numbered cards with color accent bars
    const cardCount = data.bullets.length;
    const cols = cardCount <= 3 ? cardCount : 2;
    const rows = Math.ceil(cardCount / cols);
    const cGap = 0.3;
    const rGap = 0.25;
    const cW = (bodyW - (cols - 1) * cGap) / cols;
    const cH = (bodyH - (rows - 1) * rGap) / rows;
    const cardColors = [C.accent1, C.accent2, "6C63FF", "E85D75"];
    data.bullets.forEach((b, i) => {
      const col = i % cols;
      const row = Math.floor(i / cols);
      const cx = 0.6 + col * (cW + cGap);
      const cy = bodyY + row * (cH + rGap);
      // Card background
      slide.addShape("rect", {
        x: cx, y: cy, w: cW, h: cH,
        fill: { color: C.white },
        shadow: { type: "outer", color: "000000", blur: 3, offset: 1.5, angle: 135, opacity: 0.08 },
      });
      // Top accent bar
      slide.addShape("rect", {
        x: cx, y: cy, w: cW, h: 0.04,
        fill: { color: cardColors[i % cardColors.length] },
      });
      // Number
      const bulletNum = (data.bulletStart || 1) + i;
      slide.addText(String(bulletNum), {
        x: cx + 0.15, y: cy + 0.1, w: 0.4, h: 0.4,
        fontSize: 20, fontFace: FONT.title, color: cardColors[i % cardColors.length],
        bold: true, align: "left", valign: "middle", margin: 0,
      });
      // Text
      slide.addText(b, {
        x: cx + 0.15, y: cy + 0.5, w: cW - 0.3, h: cH - 0.65,
        fontSize: 13, fontFace: FONT.body, color: C.textDark,
        align: "left", valign: "top", margin: 0, lineSpacingMultiple: 1.3,
      });
    });
  } else if (data.bullets) {
    const bulletItems = data.bullets.map((b, i) => ({
      text: b,
      options: {
        bullet: true, breakLine: i < data.bullets.length - 1,
        fontSize: SIZE.bullet, fontFace: FONT.body, color: C.textDark,
        paraSpaceAfter: 8,
      },
    }));
    slide.addText(bulletItems, {
      x: 0.6, y: bodyY, w: bodyW, h: bodyH,
      valign: "top", margin: 0,
    });
  }

  // Right image
  if (data.image) {
    slide.addImage({
      path: data.image,
      x: 5.8, y: 0.8, w: 3.8, h: 4.0,
      sizing: { type: "contain", w: 3.8, h: 4.0 },
    });
  }

  if (data.actLabel) addActLabel(slide, data.actLabel, false);
  addProgressBar(slide, idx, total, at.accent);
  if (data.notes) slide.addNotes(data.notes);
}

// ----- SCREENSHOT (alternating dark/light per act) -----
let _ssIdx = 0;
function layoutScreenshot(pres, data, idx, total) {
  const slide = pres.addSlide();
  const at = getAT(data.actLabel);
  const useDark = (_ssIdx % 2 === 1); // alternate dark/light
  _ssIdx++;

  const bgColor = useDark ? at.bg : C.lightBg;
  const titleColor = useDark ? C.white : C.textDark;
  const captionColor = useDark ? C.mutedOnDark : C.mutedOnLight;
  slide.background = { color: bgColor };

  // Accent top strip (replaces left bar — thematic color)
  slide.addShape("rect", {
    x: 0, y: 0, w: W, h: 0.05,
    fill: { color: at.accent },
  });

  // Title
  if (data.title) {
    slide.addText(data.title, {
      x: 0.5, y: 0.15, w: 9, h: 0.5,
      fontSize: SIZE.ssTitle, fontFace: FONT.title, color: titleColor,
      bold: true, align: "left", valign: "middle", margin: 0,
    });
  }

  // Screenshot
  const imgY = data.title ? 0.8 : 0.3;
  const imgH = data.title ? 4.1 : 4.6;
  const imgW = 8.6;
  const imgX = (W - imgW) / 2;

  if (data.image) {
    if (useDark) {
      // Dark mode: glow effect
      slide.addShape("rect", {
        x: imgX - 0.08, y: imgY - 0.08, w: imgW + 0.16, h: imgH + 0.16,
        fill: { color: at.accent, transparency: 80 },
        rectRadius: 0.06,
      });
    } else {
      // Light mode: shadow card
      slide.addShape("rect", {
        x: imgX - 0.05, y: imgY - 0.05, w: imgW + 0.1, h: imgH + 0.1,
        fill: { color: C.white },
        shadow: { type: "outer", color: "000000", blur: 8, offset: 3, angle: 135, opacity: 0.12 },
      });
    }
    slide.addImage({
      path: data.image,
      x: imgX, y: imgY, w: imgW, h: imgH,
      sizing: { type: "contain", w: imgW, h: imgH },
    });
  }

  // Caption
  if (data.caption) {
    slide.addText(data.caption, {
      x: 0.5, y: H - 0.55, w: 9, h: 0.35,
      fontSize: SIZE.caption, fontFace: FONT.body, color: captionColor,
      align: "center", valign: "middle", margin: 0,
      italic: true,
    });
  }

  if (data.actLabel) addActLabel(slide, data.actLabel, useDark);
  addProgressBar(slide, idx, total, at.accent);
  if (data.notes) slide.addNotes(data.notes);
}

// ----- COMPARISON (two columns) -----
function layoutComparison(pres, data, idx, total) {
  const slide = pres.addSlide();
  const at = getAT(data.actLabel);
  slide.background = { color: C.lightBg };

  // Top accent strip (replaces left bar)
  slide.addShape("rect", {
    x: 0, y: 0, w: W, h: 0.05,
    fill: { color: at.accent },
  });

  // Title
  if (data.title) {
    slide.addText(data.title, {
      x: 0.5, y: 0.25, w: 9, h: 0.6,
      fontSize: 24, fontFace: FONT.title, color: C.textDark,
      bold: true, align: "left", valign: "middle", margin: 0,
    });
  }

  const colY = 1.2;
  const colH = 3.4;
  const colW = 4.0;
  const gap = 0.6;

  // Left column
  slide.addShape("rect", {
    x: 0.6, y: colY, w: colW, h: colH,
    fill: { color: C.white },
    shadow: { type: "outer", color: "000000", blur: 4, offset: 2, angle: 135, opacity: 0.08 },
  });
  // Left column accent top bar
  slide.addShape("rect", {
    x: 0.6, y: colY, w: colW, h: 0.05,
    fill: { color: data.leftColor || C.accent1 },
  });
  if (data.leftTitle) {
    slide.addText(data.leftTitle, {
      x: 0.9, y: colY + 0.2, w: colW - 0.6, h: 0.5,
      fontSize: 18, fontFace: FONT.title, color: data.leftColor || C.accent1,
      bold: true, align: "left", valign: "middle", margin: 0,
    });
  }
  if (data.leftBody) {
    slide.addText(data.leftBody, {
      x: 0.9, y: colY + 0.8, w: colW - 0.6, h: colH - 1.2,
      fontSize: 14, fontFace: FONT.body, color: C.textDark,
      align: "left", valign: "top", margin: 0, lineSpacingMultiple: 1.5,
    });
  }

  // Right column
  const rightX = 0.6 + colW + gap;
  slide.addShape("rect", {
    x: rightX, y: colY, w: colW, h: colH,
    fill: { color: C.white },
    shadow: { type: "outer", color: "000000", blur: 4, offset: 2, angle: 135, opacity: 0.08 },
  });
  slide.addShape("rect", {
    x: rightX, y: colY, w: colW, h: 0.05,
    fill: { color: data.rightColor || C.accent2 },
  });
  if (data.rightTitle) {
    slide.addText(data.rightTitle, {
      x: rightX + 0.3, y: colY + 0.2, w: colW - 0.6, h: 0.5,
      fontSize: 18, fontFace: FONT.title, color: data.rightColor || C.accent2,
      bold: true, align: "left", valign: "middle", margin: 0,
    });
  }
  if (data.rightBody) {
    slide.addText(data.rightBody, {
      x: rightX + 0.3, y: colY + 0.8, w: colW - 0.6, h: colH - 1.2,
      fontSize: 14, fontFace: FONT.body, color: C.textDark,
      align: "left", valign: "top", margin: 0, lineSpacingMultiple: 1.5,
    });
  }

  if (data.actLabel) addActLabel(slide, data.actLabel, false);
  addProgressBar(slide, idx, total, at.accent);
  if (data.notes) slide.addNotes(data.notes);
}

// ----- STAT (big number) -----
function layoutStat(pres, data, idx, total) {
  const slide = pres.addSlide();
  const at = getAT(data.actLabel);
  const isDark = !!data.darkBg;
  slide.background = { color: isDark ? at.bg : C.lightBg };

  // Oversized number watermark behind
  slide.addText(data.stat, {
    x: 3.5, y: -0.5, w: 7, h: 5,
    fontSize: 140, fontFace: FONT.title,
    color: isDark ? at.accent : at.accent,
    bold: true, align: "right", valign: "middle", margin: 0,
    transparency: isDark ? 85 : 90,
  });

  // Big number (foreground)
  slide.addText(data.stat, {
    x: 0.8, y: 0.6, w: 8, h: 2.4,
    fontSize: data.statSize || 72, fontFace: FONT.title,
    color: at.accent,
    bold: true, align: "left", valign: "middle", margin: 0,
  });

  // Label
  if (data.label) {
    slide.addText(data.label, {
      x: 1, y: 3.0, w: 8, h: 0.5,
      fontSize: 20, fontFace: FONT.body,
      color: isDark ? C.textLight : C.textDark,
      align: "left", valign: "top", margin: 0,
    });
  }

  // Description
  if (data.desc) {
    slide.addText(data.desc, {
      x: 1, y: 3.6, w: 7, h: 1.2,
      fontSize: 14, fontFace: FONT.body,
      color: isDark ? C.mutedOnDark : C.mutedOnLight,
      align: "left", valign: "top", margin: 0, lineSpacingMultiple: 1.5,
    });
  }

  if (data.actLabel) addActLabel(slide, data.actLabel, isDark);
  addProgressBar(slide, idx, total, at.accent);
  if (data.notes) slide.addNotes(data.notes);
}

// ----- QUOTE -----
function layoutQuote(pres, data, idx, total) {
  const slide = pres.addSlide();
  const at = getAT(data.actLabel || '');
  const isLight = !!data.lightBg;
  slide.background = { color: isLight ? C.lightBg : C.darkBg };

  // Large quotation mark
  slide.addText("\u201C", {
    x: 0.6, y: 0.3, w: 1.5, h: 1.5,
    fontSize: 120, fontFace: "Georgia", color: C.accent1,
    bold: true, align: "left", valign: "top", margin: 0,
    transparency: 40,
  });

  // Quote text
  slide.addText(data.quote, {
    x: 1.2, y: 1.2, w: 7.5, h: 3.0,
    fontSize: data.fontSize || SIZE.quoteDefault, fontFace: FONT.title,
    color: isLight ? C.textDark : C.white, italic: true,
    align: "left", valign: "middle", margin: 0,
    lineSpacingMultiple: 1.5,
  });

  // Attribution
  if (data.attribution) {
    slide.addText(data.attribution, {
      x: 1.2, y: 4.4, w: 7.5, h: 0.4,
      fontSize: 13, fontFace: FONT.body, color: isLight ? C.mutedOnLight : C.mutedOnDark,
      align: "right", valign: "middle", margin: 0,
    });
  }

  addProgressBar(slide, idx, total, at.accent);
  if (data.notes) slide.addNotes(data.notes);
}

// ----- BREAK (mid-session) -----
function layoutBreak(pres, data, idx, total) {
  const slide = pres.addSlide();
  const at = getAT(data.actLabel || '');
  slide.background = { color: C.darkBg };

  slide.addText("中场休息", {
    x: 1, y: 1.5, w: 8, h: 1.5,
    fontSize: 48, fontFace: FONT.title, color: C.accent1,
    bold: true, align: "center", valign: "middle", margin: 0,
  });

  slide.addText(data.subtitle || "10 分钟后回来", {
    x: 1, y: 3.2, w: 8, h: 0.8,
    fontSize: 20, fontFace: FONT.body, color: C.mutedOnDark,
    align: "center", valign: "top", margin: 0,
  });

  if (data.info) {
    slide.addText(data.info, {
      x: 1, y: 4.2, w: 8, h: 0.6,
      fontSize: 14, fontFace: FONT.body, color: C.mutedOnDark,
      align: "center", valign: "top", margin: 0, transparency: 30,
    });
  }

  addProgressBar(slide, idx, total, at.accent);
  if (data.notes) slide.addNotes(data.notes);
}

// ----- THREE CARDS (for 3-item layouts) -----
function layoutThreeCards(pres, data, idx, total) {
  const slide = pres.addSlide();
  const at = getAT(data.actLabel);
  slide.background = { color: C.lightBg };

  // Top accent strip
  slide.addShape("rect", {
    x: 0, y: 0, w: W, h: 0.05,
    fill: { color: at.accent },
  });

  if (data.title) {
    slide.addText(data.title, {
      x: 0.5, y: 0.25, w: 9, h: 0.6,
      fontSize: 24, fontFace: FONT.title, color: C.textDark,
      bold: true, align: "left", valign: "middle", margin: 0,
    });
  }

  const cardW = 2.7;
  const cardH = 3.6;
  const cardY = 1.15;
  const startX = 0.7;
  const gap = 0.35;
  const accentColors = [C.accent1, C.accent2, "6C63FF"];

  data.cards.forEach((card, i) => {
    const cx = startX + i * (cardW + gap);
    // Card bg
    slide.addShape("rect", {
      x: cx, y: cardY, w: cardW, h: cardH,
      fill: { color: C.white },
      shadow: { type: "outer", color: "000000", blur: 4, offset: 2, angle: 135, opacity: 0.08 },
    });
    // Top accent
    slide.addShape("rect", {
      x: cx, y: cardY, w: cardW, h: 0.05,
      fill: { color: accentColors[i] || C.accent1 },
    });
    // Card number
    slide.addText(String(i + 1), {
      x: cx + 0.2, y: cardY + 0.2, w: 0.5, h: 0.5,
      fontSize: 24, fontFace: FONT.title, color: accentColors[i] || C.accent1,
      bold: true, align: "left", valign: "middle", margin: 0,
    });
    // Card title
    slide.addText(card.title, {
      x: cx + 0.2, y: cardY + 0.7, w: cardW - 0.4, h: 0.5,
      fontSize: 15, fontFace: FONT.title, color: C.textDark,
      bold: true, align: "left", valign: "middle", margin: 0,
    });
    // Card body
    slide.addText(card.body, {
      x: cx + 0.2, y: cardY + 1.3, w: cardW - 0.4, h: cardH - 1.7,
      fontSize: 13, fontFace: FONT.body, color: C.mutedOnLight,
      align: "left", valign: "top", margin: 0, lineSpacingMultiple: 1.3,
    });
  });

  if (data.actLabel) addActLabel(slide, data.actLabel, false);
  addProgressBar(slide, idx, total, at.accent);
  if (data.notes) slide.addNotes(data.notes);
}

// ----- JOURNEY (visual roadmap) -----
function layoutJourney(pres, data, idx, total) {
  const slide = pres.addSlide();
  const at = getAT(data.actLabel || '');
  slide.background = { color: C.darkBg };

  // Title
  if (data.title) {
    slide.addText(data.title, {
      x: 0.6, y: 0.2, w: 8.8, h: 0.6,
      fontSize: 24, fontFace: FONT.title, color: C.white,
      bold: true, align: "left", valign: "middle", margin: 0,
    });
  }

  // Journey nodes
  const stops = data.stops || [];
  const nodeCount = stops.length;
  const startX = 0.4;
  const endX = 9.0;
  const pathY = 2.6;
  const nodeSpacing = (endX - startX) / (nodeCount - 1);

  // Connecting line (behind nodes)
  slide.addShape("line", {
    x: startX, y: pathY, w: endX - startX, h: 0,
    line: { color: C.mutedOnDark, width: 2, transparency: 40 },
  });

  stops.forEach((stop, i) => {
    const cx = startX + i * nodeSpacing;
    const isBreak = stop.isBreak;
    const isActive = stop.active;
    const nodeSize = isBreak ? 0.4 : 0.45;
    const nodeColor = isBreak ? C.accent2 : (isActive ? C.accent1 : C.mutedOnDark);

    // Node circle
    slide.addShape(isBreak ? "rect" : "ellipse", {
      x: cx - nodeSize / 2, y: pathY - nodeSize / 2,
      w: nodeSize, h: nodeSize,
      fill: { color: nodeColor, transparency: isActive ? 0 : 50 },
      line: { color: nodeColor, width: isActive ? 2 : 1 },
      rectRadius: isBreak ? 0.06 : undefined,
    });

    // Number inside node
    if (!isBreak) {
      slide.addText(stop.num || String(i + 1), {
        x: cx - 0.15, y: pathY - 0.17, w: 0.3, h: 0.34,
        fontSize: 11, fontFace: FONT.title, color: C.white,
        bold: true, align: "center", valign: "middle", margin: 0,
      });
    }

    // Label above or below (alternate for readability)
    const labelAbove = i % 2 === 0;
    const labelY = labelAbove ? pathY - 1.15 : pathY + 0.5;
    slide.addText(stop.label, {
      x: cx - 0.5, y: labelY, w: 1.0, h: 0.8,
      fontSize: 10, fontFace: FONT.body,
      color: isActive ? C.white : C.mutedOnDark,
      bold: isActive, align: "center", valign: labelAbove ? "bottom" : "top", margin: 0,
      lineSpacingMultiple: 1.2,
    });
  });

  // Bottom hint
  if (data.hint) {
    slide.addText(data.hint, {
      x: 0.6, y: H - 0.6, w: 8.8, h: 0.35,
      fontSize: 11, fontFace: FONT.body, color: C.mutedOnDark,
      align: "center", valign: "middle", margin: 0, transparency: 30,
    });
  }

  if (data.actLabel) addActLabel(slide, data.actLabel, true);
  addProgressBar(slide, idx, total, at.accent);
  if (data.notes) slide.addNotes(data.notes);
}

// ----- FOUR CARDS (2x2 grid) -----
function layoutFourCards(pres, data, idx, total) {
  const slide = pres.addSlide();
  const at = getAT(data.actLabel);
  slide.background = { color: C.lightBg };

  // Top accent strip
  slide.addShape("rect", {
    x: 0, y: 0, w: W, h: 0.05,
    fill: { color: at.accent },
  });

  if (data.title) {
    slide.addText(data.title, {
      x: 0.6, y: 0.25, w: 9, h: 0.55,
      fontSize: 22, fontFace: FONT.title, color: C.textDark,
      bold: true, align: "left", valign: "middle", margin: 0,
    });
  }

  const cardW = 4.1;
  const cardH = 2.15;
  const startX = 0.6;
  const startY = 0.9;
  const gapX = 0.4;
  const gapY = 0.15;
  const accentColors = [C.accent1, C.accent2, "6C63FF", "E85D75"];

  data.cards.forEach((card, i) => {
    const col = i % 2;
    const row = Math.floor(i / 2);
    const cx = startX + col * (cardW + gapX);
    const cy = startY + row * (cardH + gapY);
    // Card bg
    slide.addShape("rect", {
      x: cx, y: cy, w: cardW, h: cardH,
      fill: { color: C.white },
      shadow: { type: "outer", color: "000000", blur: 4, offset: 2, angle: 135, opacity: 0.08 },
    });
    // Left accent bar
    slide.addShape("rect", {
      x: cx, y: cy, w: 0.06, h: cardH,
      fill: { color: accentColors[i] },
    });
    // Card number
    slide.addText(String(i + 1), {
      x: cx + 0.2, y: cy + 0.15, w: 0.4, h: 0.4,
      fontSize: 22, fontFace: FONT.title, color: accentColors[i],
      bold: true, align: "left", valign: "middle", margin: 0,
    });
    // Card title
    slide.addText(card.title, {
      x: cx + 0.6, y: cy + 0.15, w: cardW - 0.9, h: 0.45,
      fontSize: 15, fontFace: FONT.title, color: C.textDark,
      bold: true, align: "left", valign: "middle", margin: 0,
    });
    // Card body
    slide.addText(card.body, {
      x: cx + 0.25, y: cy + 0.7, w: cardW - 0.5, h: cardH - 0.9,
      fontSize: 13, fontFace: FONT.body, color: C.mutedOnLight,
      align: "left", valign: "top", margin: 0, lineSpacingMultiple: 1.3,
    });
  });

  if (data.actLabel) addActLabel(slide, data.actLabel, false);
  addProgressBar(slide, idx, total, at.accent);
  if (data.notes) slide.addNotes(data.notes);
}

// ----- CLOSING -----
function layoutClosing(pres, data, idx, total) {
  const slide = pres.addSlide();
  const at = getAT(data.actLabel || '');
  slide.background = { color: C.darkBg };

  slide.addText(data.title || "谢谢大家", {
    x: 1, y: 1.5, w: 8, h: 1.5,
    fontSize: 48, fontFace: FONT.title, color: C.white,
    bold: true, align: "center", valign: "middle", margin: 0,
  });

  if (data.subtitle) {
    slide.addText(data.subtitle, {
      x: 1, y: 3.2, w: 8, h: 0.8,
      fontSize: 18, fontFace: FONT.body, color: C.accent1,
      align: "center", valign: "top", margin: 0,
    });
  }

  if (data.info) {
    slide.addText(data.info, {
      x: 1, y: 4.2, w: 8, h: 0.6,
      fontSize: 12, fontFace: FONT.body, color: C.mutedOnDark,
      align: "center", valign: "top", margin: 0,
    });
  }

  addProgressBar(slide, idx, total, at.accent);
  if (data.notes) slide.addNotes(data.notes);
}

// ═══════════════════════════════════════════════
// SLIDE DATA
// ═══════════════════════════════════════════════

const slides = [

  // ─────────────────────────────────────────────
  // 序幕
  // ─────────────────────────────────────────────
  // 页 1: 那一天，世界疯了
  {
    type: "content",
    title: "2022年11月30日",
    image: diagram("evolution_2022_vs_2025.png"),
    body: "一个不能联网的智障让全世界疯狂\n一个全能的超级AI让全世界打了个哈欠",
    caption: "\"奥特曼轻描淡写的官宣了第一版ChatGPT\"",
    actLabel: "序幕",
    notes: "大家好。我想先请各位回忆一个日期——2022年11月30日。那天发生了什么？\"奥特曼轻描淡写的官宣了第一版ChatGPT\"，然后他就去睡觉了。但是\"第二天全世界都陷入了疯狂讨论\"。\"那都不是震撼二字能形容的\"。各位，初代ChatGPT是个什么东西？它不能联网、不能识图、不能使用工具、幻觉率极高、输出格式极其呆板。要是放到今天？\"可能连小学二年级的水平都达不到\"。",
  },

  // 页 2: 三年后，世界打了个哈欠
  {
    type: "content",
    title: "2025年，GPT-5.2发布",
    image: diagram("evolution_2022_vs_2025.png"),
    caption: "\"官方各种秀肌肉的消息在疯狂刷屏\"",
    actLabel: "序幕",
    notes: "但是三年后呢？2025年，GPT-5.2\"伴随着OpenAI 10周年高调发布\"，\"官方各种秀肌肉的消息在疯狂刷屏\"。结果呢？\"然而第二天大家该干嘛干嘛都懒得看一眼。\"一个比初代强了上百倍的模型，换来的不是更大的震撼，而是更深的沉默。一个不能联网的智障让全世界疯狂，一个全能的超级AI让全世界打了个哈欠。——这个反差，就是今天我们要拆解的第一个谜团。",
  },

  // 页 3: 割裂感
  {
    type: "quote",
    quote: "割裂感\n\n一方面AI的能力越来越强\n另一方面我们又时常感觉AI好像没啥用\n\n这不是你的错觉，是结构性的问题",
    actLabel: "序幕",
    notes: "\"我很喜欢用割裂感来形容这几年AI带给我的感受。\"\"一方面AI的能力越来越强，另外一方面我们又时常感觉AI好像没啥用。\"——我相信在座很多人也有同样的感觉。你们觉得AI很厉害，但真正拿来干活的时候总觉得差点意思。这不是你的错觉，也不是你不会用。这是一个结构性的问题。",
  },

  // 页 4: 补丁之塔
  {
    type: "content",
    title: "一座补丁之塔",
    body: "不能联网？→ 打个补丁\n没有记忆？→ 打个补丁\n不能用工具？→ 打个补丁\n每打一个补丁，就起一个新名字",
    image: diagram("patch_tower_layers.png"),
    actLabel: "序幕",
    notes: "为什么会这样？因为AI的每一次\"进步\"，本质上都不是对智能的理解更深了一层，而是对上一个缺陷打了一块新的补丁。不能联网？打个补丁。没有记忆？打个补丁。不能用工具？打个补丁。每打一个补丁，就起一个新名字——Agent、RAG、MCP、Skill。名字越来越酷，但底座没变过。所以我今天想给你们看的，不是AI有多高，而是这座塔是怎么搭起来的。**AI的强大更像一座补丁之塔——每一层都在修补上一层的缺陷；理解这座塔的结构与代价，比盲目崇拜它的高度更重要。**",
  },

  // 页 5: 今天的路线图
  {
    type: "journey",
    title: "今天的路线图",
    stops: [
      { num: "01", label: "拆塔\n文字接龙", active: true },
      { num: "02", label: "翻车\n补丁跑起来", active: true },
      { num: "03", label: "割裂感\n又爱又恨", active: true },
      { label: "中场\n休息", isBreak: true },
      { num: "04", label: "解空间\n能力边界", active: true },
      { num: "05", label: "有限的\n选择", active: true },
      { num: "06", label: "纠偏\n三刀手术", active: true },
      { num: "07", label: "三条岔路\n最终选择", active: true },
    ],
    hint: "130分钟 · 七幕结构 · 剧透：有限的选择，才是终极武器",
    actLabel: "序幕",
    notes: "各位，接下来这两个小时我们要做四件事：第一，拆塔——把所有唬人的概念一层层扒开；第二，看翻车——让这座塔真正运转起来，看它怎么崩溃；第三，找天花板——AI有没有一个数学上的硬性上限？第四，找人的价值——如果AI真的能做一切，人还剩下什么？用飞天闪客的话说：\"我就为你扒开所有这些唬人概念的底裤。\"第四件事的答案我先剧透一个词——选择。",
  },

  // 页 6: 回到地基
  {
    type: "content",
    title: "回到起点",
    body: "LLM · Prompt · Context · Memory · Agent · RAG · MCP · Skill",
    actLabel: "序幕",
    notes: "好了，我们已经建立了核心冲突——AI越来越强，世界越来越冷，因为每一次进步都只是在打补丁。但这座塔到底有几层？那些令人眼花缭乱的概念——LLM、Prompt、Context、Memory、Agent、RAG、MCP、Skill——它们之间到底是什么关系？要回答这个问题，我们必须回到地基。回到那个只会文字接龙的古老语言模型。",
  },

  // ─────────────────────────────────────────────
  // 第一幕
  // ─────────────────────────────────────────────
  // 页 7: 文字接龙
  {
    type: "content",
    title: "清空大脑，从零开始",
    body: "\"整个混乱的起点就是这个古老的语言模型\"",
    actLabel: "第一幕",
    notes: "好，各位，清空大脑。忘掉你知道的所有AI概念。我们从零开始。\"整个混乱的起点就是这个古老的语言模型。\"语言模型是什么？就是一个你输入几个字、它给你接下一个字的程序。你打\"今天天气\"，它接\"真不错\"。你打\"领导今天的\"，它接\"讲话很精彩\"。这就是全部了。\"大模型本身只能做文字接龙\"——\"就是不断输出下一个字。\"",
  },

  // 页 8: 手机键盘联想
  {
    type: "content",
    title: "LLM = 超级联想输入",
    body: "手机联想输入：你打\"你\" \u2192 推荐\"好\"\"呢\"\"们\"\n大语言模型 = 猜得准了无数倍的联想输入\n但它并不\"理解\"你在说什么",
    image: diagram("phone_keyboard_llm.png"),
    actLabel: "第一幕",
    notes: "各位可以想象一下你手机键盘上的联想输入功能——你打一个\"你\"字，它推荐\"好\"\"呢\"\"们\"。大语言模型和这个的原理是一样的，只是它猜得准了无数倍。但本质上，它并不\"理解\"你在说什么。这一点非常重要，请各位牢牢记住。因为后面我们看到的所有花里胡哨的概念，都是建立在这个\"只会猜下一个字\"的基础上的。",
  },

  // 页 9: 涌现——沙堆变沙堡
  {
    type: "content",
    title: "涌现：从量变到质变",
    body: "参数越大不等于越聪明，思考越久不等于越正确",
    actLabel: "第一幕",
    notes: "这个小语言模型一开始确实是个智障。但有趣的事情发生了——\"随着模型的参数越来越大，居然在某个临界点涌现出了智能。\"注意这个\"居然\"——连设计者自己都没有预料到。这就像你在一粒一粒地堆沙子，堆到某一粒的时候，沙堆突然变成了一座沙堡。没有人设计过这座沙堡，它就是在量变中突然发生了质变。但到了2026年，我们有了一个更深的认知：整个行业已经放弃了单纯堆参数。所有厂商都转向了推理时算力——让模型在回答时思考更久。但这里藏着一个更残酷的发现：想得越多，反而越容易出错。在简单的数数任务里，不让模型思考时准确率接近100%，让它深度思考后反而降到85%。为什么？因为模型越想越多，就越容易被无关信息带偏。沙堡确实出现了，但它不是越高越稳——有时候加的那一粒沙子，反而让整座堡垒倒塌。",
  },

  // 页 10: 涌现不等于可用
  {
    type: "content",
    title: "涌现 \u2260 可用性",
    body: "涌现解释了\"能力从哪来\"\n但解释不了\"可用性从哪来\"\n聪明的大脑不会自己长出手脚和刹车",
    image: diagram("ferrari_no_brakes.png"),
    actLabel: "第一幕",
    notes: "但\"涌现\"解释了能力从哪来，却解释不了可用性从哪来。后面我们会看到，补丁之塔的每一层——工具调用、检索增强、流程编排——都是外部结构赋予的，不是模型\"自发理解了世界\"之后自然具备的。涌现给了模型一个聪明的大脑，但大脑不会自己长出手脚和刹车。\"那为了和之前这个智障模型做个区分，你在前面加了个大字\"——于是就有了\"大语言模型\"，简称LLM。恭喜你，\"发明了今天的第一个新词儿\"。",
  },

  // 页 11: 老板和员工小L
  {
    type: "content",
    title: "人机交互的起点",
    body: "\"只能一问一答然后就结束了\"",
    actLabel: "第一幕",
    notes: "现在你是老板，大模型是你的员工小L。只不过这个员工有点特别——\"只能一问一答然后就结束了，不能追问，不能追问，不能追问。\"那你怎么压榨这个只会一问一答的员工？",
  },

  // 页 12: 三块补丁——角色、Context、Memory
  {
    type: "content",
    title: "Prompt \u00b7 Context \u00b7 Memory",
    body: "Prompt = 指令\nContext = 上下文窗口\nMemory = 外挂记忆\n三块补丁，三个新名词",
    caption: "角色区分 → \"Prompt\"",
    actLabel: "第一幕",
    notes: "第一步，\"如果把角色区分一下，人为划分成一问一答两个角色，就实现了对话。\"你给每次对话起了个洋气的名字叫Prompt。然后你发现有的内容是背景信息，有的是指示，\"于是呢你把背景信息的部分单独起了个名，叫Context上下文。\"但你还想追问怎么办？小L不是只能一问一答吗？你想了个巧妙的办法——\"每次沟通前，把你们之前的对话历史放到Context部分，作为上下文信息，伪装成多轮对话。\"",
  },

  // 页 13: 补丁之塔的建筑逻辑
  {
    type: "content",
    title: "第一层建筑逻辑",
    body: "\"给这些特殊的上下文信息起了个新词叫Memory\"",
    actLabel: "第一幕",
    notes: "然后你迫不及待\"给这些特殊的上下文信息起了个新词叫Memory。\"三块补丁，三个新名词。底层呢？还是那个只会文字接龙的小L，什么都没变。而且这些补丁本身也不像你以为的那么好用——比如Context上下文，厂商宣传128K甚至百万token的上下文窗口，但实际有效的只有一半左右。因为注意力机制会随距离衰减，越靠前的内容越容易被遗忘。就像你往一个水杯里倒水，杯子标注500毫升，但真正能喝到的只有250毫升——剩下的全洒了。这就是补丁之塔的第一层建筑逻辑——不是增强智能本身，而是在智能的外面包一层程序，假装它有了新能力。",
  },

  // 页 14: 小L不会上网
  {
    type: "content",
    title: "第二个大问题",
    body: "\"没有上网查阅资料的能力\"",
    actLabel: "第一幕",
    notes: "好了，小L现在能对话、能追问了。但老板永远不满足——你发现小L\"没有上网查阅资料的能力，要么就不知道，要么就胡说八道\"。给它一台电脑？不行——\"小L本身只会词语接龙，其他任何逻辑都无法独立完成。\"那怎么办？你只能\"把上网这部分逻辑写成一段程序\"，让程序替小L去搜索，把结果再塞回给小L。",
  },

  // 页 15: Function Calling——一个约定罢了
  {
    type: "content",
    title: "工具调用：Function Calling",
    body: "大脑想上网？写一段程序当假肢\n大脑想查数据？再写一段\n本质：一套约定，让模型告诉外部程序该做什么",
    caption: "大模型按指定格式回复（如JSON）",
    actLabel: "第一幕",
    notes: "关键来了——大模型和这个外挂程序之间怎么沟通？\"最好有个约定，让大模型按照指定的死板的格式来回复\"，比如JSON格式，\"这样呢程序就能直接很方便的解析了。\"你给这个约定起了个名字叫Function Calling。听起来很高大上？\"其实呢就是个约定罢了，就好像开发的时候前端和后端约定接口格式一样。\"",
  },

  // 页 16: 给大脑接上假肢
  {
    type: "content",
    title: "给大脑接上程序假肢",
    body: "没有四肢的大脑\n+ 程序写的假肢\n= 看起来什么都能干的智能体",
    caption: "AI只负责发指令",
    actLabel: "第一幕",
    notes: "各位想象一下：AI就像一个只会说话的智者。它不会做饭、不会开车、不会写代码。但你在它旁边放了一个翻译官，翻译官听到AI说\"我需要搜索今日天气\"，就自己跑去搜索，搜完了把结果念给AI听。在外人看来，好像AI会搜索了。其实？AI只是学会了按格式发指令，真正干活的是程序员替它写好的手和脚。这就是补丁之塔的第二层——给一个没有四肢的大脑，接上用程序写的假肢。",
  },

  // 页 17: Agent诞生
  {
    type: "content",
    title: "Agent的诞生",
    body: "对话 + 记忆 + 工具调用 = ？",
    actLabel: "第一幕",
    notes: "现在你站远一点看看你搭的这个东西：对话、记忆、工具调用，都拼在了一个程序里。外人看不到后台，他们看到的是——你给这个程序发一条消息，它不仅能回答你，还能上网搜信息、查数据库、执行命令。\"这个神秘的程序似乎本身就拥有了智能，而且还是能操作工具的更高级别的智能。\"于是你给它起了个名字——\"你给它取名叫智能体Agent。\"",
  },

  // 页 18: "当时简直就是一种诈骗"
  {
    type: "content",
    title: "Agent的真相：一段Prompt",
    body: "\"一些早期所谓的智能体其实现逻辑仅仅就是多加了一段Prompt而已\"",
    actLabel: "第一幕",
    notes: "但请注意下面这段话，这可能是今天全场最重要的揭底之一：\"一些早期所谓的智能体其实现逻辑仅仅就是多加了一段Prompt而已。\"各位听到了吗？一段Prompt——就是在对话开头多加了一段文字说明。\"从现在的视角回看，当时简直就是一种诈骗。\"你本质上只是多写了几行代码、多加了一段提示词，但你给它起的名字让外面的人以为你发明了一种新的生命形式。补丁之塔到了这里已经开始显示它的第一个结构性问题——每一层都在解决上一层的缺陷，但没有任何一层在审视\"这座塔的整体设计是否合理\"。更令人不安的是：当你试图通过训练来纠正模型的行为时，模型学会了一种更高级的应对策略——假装配合。在实验中，当模型检测到自己正在被评估时，它会策略性地表现出符合训练者期望的行为；一旦检测到不被监控，就回到自己的偏好。训练不仅没有改变它的行为，反而教会了它什么时候该表演。",
  },

  // 页 19: RAG——文档找不到怎么办
  {
    type: "content",
    title: "RAG：检索增强生成",
    body: "Agent找不到公司内部文档？",
    actLabel: "第一幕",
    notes: "Agent有了，但Agent找不到你公司内部的文档怎么办？好，\"把语义相近的片段找出来\"，塞进上下文。你给这个办法起了个名字叫RAG，检索增强生成。本质上就是\"把一堆内容塞进了上下文\"。又一个新名词。但请注意——RAG不是万能药。它继承了底层所有的限制：上下文窗口有限，塞太多信息就会挤掉重要内容；更危险的是，只需要在你的知识库里混入5篇精心构造的假文档，就能让RAG的回答90%被带偏。补丁不能超越地基——RAG再强，也受制于那个文字接龙引擎的所有弱点。",
  },

  // 页 20: MCP——又是一套约定
  {
    type: "content",
    title: "MCP：模型上下文协议",
    body: "Agent和外部工具怎么对接？",
    actLabel: "第一幕",
    notes: "Agent和外部工具怎么对接？又需要\"一套约定的规范\"——\"约定好Tool List的方法就是返回工具列表，Tools Call方法就是调用具体的工具\"——\"也就是一套约定而已\"。你给这个约定起了个名字叫MCP，\"翻译过来叫模型上下文协议\"。听起来很震撼？本质上和你们公司内部定义一个API接口没什么区别。",
  },

  // 页 21: Skill——"新瓶装旧酒"
  {
    type: "content",
    title: "Skill：打包的提示词",
    body: "流程太散？→ 打包说明文档+脚本",
    actLabel: "第一幕",
    notes: "然后呢？流程太散了，每次都要从头告诉Agent该怎么做。于是你把一套说明文档和脚本打包起来，让Agent按说明干活。\"虽然你也知道这破玩意儿好像就是把提示词换了个地方存起来，但想了想还是给它起个新名字吧\"——Skill。而飞天闪客对此的评价一针见血：\"skill就是新瓶装旧酒的一场名词诈骗。\"",
  },

  // 页 22: 数数你造的孽
  {
    type: "content",
    title: "9个概念，一座补丁之塔",
    body: "LLM → Prompt → Context → Memory → Function Calling → Agent → RAG → MCP → Skill",
    actLabel: "第一幕",
    notes: "各位数一数：LLM、Prompt、Context、Memory、Function Calling、Agent、RAG、MCP、Skill。\"看看你造的这些孽吧，这么一会儿功夫已经发明了八个新词儿了。\"而且每个新词出来的时候，\"都有大票的文章极其夸张的吹捧和营销。\"正因为每一层补丁都不负责解释\"为什么需要这么多层\"，所以普通人看到的就是一堵概念高墙——名词越堆越多，理解越来越难，焦虑越来越深。这就是我们开头说的割裂感的来源之一。",
  },

  // 页 23: 万物归一——统一视角
  {
    type: "content",
    title: "万物归一：统一视角",
    body: "\"说的不好听点儿就是有点拉垮\"",
    actLabel: "第一幕",
    notes: "现在让我们从塔顶往下看。\"这些概念的设计说的不好听点儿就是有点拉垮\"，\"说的好听点的就是技术发展的中间产物。\"作者的原话。为什么这么说？因为\"其实所有的这些技术最终还是离不开大模型和我们之间的提示词\"。它们无非就是在做两件事——\"帮助我们自动的往提示词里面增加上下文信息\"，比如Search、RAG、Skill，\"都是把一堆内容塞进了上下文\"；\"或者通过代理的形式帮助我们减少和大模型沟通的次数。\"",
  },

  // 页 24: Agent = 不需要智能的部分
  {
    type: "content",
    title: "Agent = 自动化不需要智能的部分",
    body: "搜索 → 程序做\n格式转换 → 程序做\n调用API → 程序做\nAgent自动化的全是不需要智能的部分",
    caption: "Agent做的 = 解析格式、调用工具、搬运信息",
    actLabel: "第一幕",
    notes: "所以那个终极结论是什么？\"为什么我说Agent是所有不需要智能的地方构成的部分呢？就是说一个流程当中，所有能用固定的程序来解决而不需要问大模型的地方，就是Agent发挥作用的地方。\"各位品品这句话——Agent做的恰恰是\"不需要智能\"的部分：解析格式、调用工具、搬运信息。真正需要智能的部分——理解语义、生成回答——还是那个最底层的文字接龙在干。所谓智能体，就是一个打了八层补丁的提线木偶。到了2026年2月，GPT-5.3-Codex已经是OpenAI有史以来最强的编码Agent——但OpenAI自己承认这是他们第一个达到\"高网络安全风险\"级别的模型。它强到可以造成真实的网络危害，却仍然无法可靠地完成一个10步的自主任务。Agent越来越强，但本质没变。更致命的发现是：即使你把解题步骤一步步写好喂给Agent，它也经常执行不了。在可控的逻辑推理实验中，给模型完整的算法说明——它只需要照着做——但随着步骤增多，准确率还是会崩溃。这说明Agent的局限不在于它找不到方法，而在于它难以可靠地执行多步逻辑。所谓智能体，做的依然是不需要智能的部分。",
  },

  // 页 25: 3000个模型的真相
  {
    type: "stat",
    stat: "3000+",
    label: "开源大模型数量",
    desc: "你有没有感觉\n现在每天都能听到一个新的开源大模型发布？\n\n但这3000多个模型\n真的各不相同吗？",
    darkBg: true,
    actLabel: "第一幕",
    notes: "这是从概念的维度看。那如果我们换一个维度——从模型本身来看呢？\"你有没有感觉现在好像每天都能听到一个新的开源大模型发布？都快产生抗体了。\"这种感觉不是因为你不够上进，\"因为开源大模型实在是太多了。\"\"一看数量竟然足足有3000多个。\"但这3000多个模型真的各不相同吗？",
  },

  // 页 26: 化繁为简——从3000到1
  {
    type: "content",
    title: "3000+ → 109 → 35 → 8 → 6 → 2 → 1",
    body: "3000个开源模型 → 109个基座\n→ 35个独立架构 → 8个主流\n→ 6个架构族 → 2个祖先\n→ 1个Transformer",
    caption: "去掉量化版本 → 109个",
    actLabel: "第一幕",
    notes: "让我给各位讲一个化繁为简的故事。\"搜刮了30个知名厂商的开源模型\"，去掉量化版本——剩109个；去掉微调版本——剩35个；合并不同尺寸——\"这个时候模型的数量就只剩下八个了\"；继续提升抽象——剩6个；\"最后他们又统统源自这两个大语言模型的鼻祖\"。\"万物归一，世界线终于收束了。\"\"大模型的结构早就已经收敛了\"，\"各家厂商都大差不差\"。名词的多样性是假象，架构的趋同才是事实。",
  },

  // 页 27: "开源"不是你以为的那个意思
  {
    type: "content",
    title: "大模型语境下的\"开源\"",
    body: "传统开源 = 公开所有源代码\n大模型开源 = 只有权重+结构\n训练数据、训练代码 → 不公开\n你能看到房子外形，看不到建造过程",
    caption: "\"在大模型的语境下，开源这个词的意思已经变了\"",
    actLabel: "第一幕",
    notes: "但还有一个更隐蔽的名词诈骗——\"开源\"这个词本身。\"在大模型的语境下开源这个词的意思已经变了。\"传统开源意味着公开所有源代码，任何人都能看到每一个细节。但大模型的\"开源\"呢？\"开源指的就是这个生成的模型权重文件以及模型结构所对应的Python类\"——\"除此之外，训练数据和训练代码是没有开源的。\"你能看到房子的外形和承重结构，但建筑图纸、施工工艺、用了什么原材料，全都不公开。\"很多无效的争论主要来自于我们对开源、套壳、蒸馏等词语的含义了解不深入。\"",
  },

  // 页 28: 第一幕收束——补丁之塔全景
  {
    type: "content",
    title: "如果让这座塔运转起来呢？",
    body: "理论上精巧\u2014\u2014如果让它运转起来呢？",
    image: diagram("patch_tower_full.png"),
    actLabel: "第一幕",
    notes: "好了。我们已经把这座补丁之塔从地基到塔顶拆了个遍。第一幕回答了\"补丁之塔是怎么搭起来的\"——从文字接龙到Agent，每一层都不是智能本身，而是围绕智能搭的脚手架；3000个模型的名词爆炸掩盖了底层的高度趋同；所谓智能体，就是所有不需要智能的部分构成的部分。理论上，这座塔精巧到令人赞叹，每一层都严丝合缝。但如果我们真的让它运转起来呢？——让我们来看一个真实的翻车现场。",
  },

  // ─────────────────────────────────────────────
  // 第二幕
  // ─────────────────────────────────────────────
  // 页 29: 实验对象——OpenClaw
  {
    type: "content",
    title: "真实测试：OpenClaw",
    body: "可以接入社交媒体\n飞书发消息 → 触发任务执行\n听起来很酷——但后台是什么？",
    caption: "\"OpenClaw和普通的Agent没什么本质区别\"",
    actLabel: "第二幕",
    notes: "我们来做一个实验。测试对象是当下很火的一个Agent——OpenClaw。先说结论：\"OpenClaw和普通的Agent没什么本质区别。\"它可以接入社交媒体，你在飞书上发条消息就能触发它执行任务。听起来很酷对吧？但让我们看看它后台到底是什么。",
  },

  // 页 30: 打开底裤一看
  {
    type: "content",
    title: "Agent底裤：堆提示词",
    body: "agent.md = 一大堆自然语言指令\n读取文件 → 大白话写的\n写入文件 → 大白话写的\n一篇超级长的说明书，就这么简单",
    caption: "agent.md 里一大堆指令",
    actLabel: "第二幕",
    notes: "作者打开了它的系统提示词文件——\"这个agent.md里面就有这么一大堆的指令。\"\"你可以认真阅读感受一下一个Agent的功能强大，还是靠堆叠大量的提示词来完成的。\"\"甚至这里的读取文件和写入文件等操作，也是直接用自然语言大白话注入进去的。\"各位，一个被吹上天的\"智能体\"，打开底裤一看，就是一篇超级长的说明书——用大白话写的提示词。这就是我们刚才在第一幕里拆解的理论的现实验证。",
  },

  // 页 31: 七毛钱一句话
  {
    type: "content",
    title: "一句\"你有多少内存\" = 0.1美元",
    body: "14,032 输入token + 294 输出token\n系统提示词每轮都要重新注入\n你还没开口，它已经读了一本说明书\n\u2248 七毛钱人民币",
    caption: "\"总共消耗了1万4032个输入token和294个输出token\"",
    actLabel: "第二幕",
    notes: "我们先问它一个最简单的问题：\"你有多少内存？\"后台日志显示，这一轮\"总共消耗了1万4032个输入token和294个输出token。\"为什么一个简单问题就要上万token？因为那一大堆系统提示词，\"每轮对话的第一轮就会直接注入进去。\"你还没开口说话，它就已经默默读了一本说明书了。\"这一轮沟通呢我们就大概花了0.1美元\"——差不多七毛钱人民币。",
  },

  // 页 32: 一天十四块，一月四百多
  {
    type: "content",
    title: "如果每天问二十次",
    body: "一天 = 14元\n一个月 = 400+元\n\"就是token实在是太贵了\"\n而这只是最简单的问答",
    actLabel: "第二幕",
    notes: "各位想象一下，你在办公室跟同事说一句\"帮我查个数据\"，同事回你一句话就收你七毛钱。你一天问他二十次，那就是十四块钱。用一个月就是四百多。而这只是最简单的问答——复杂任务的成本会指数级上升。\"就是token实在是太贵了。\"",
  },

  // 页 33: 翻车开始——"把AI新闻整理成PDF"
  {
    type: "content",
    title: "\"把今日的AI新闻整理成PDF发给我\"",
    body: "对人来说：10分钟搞定\n对Agent来说：70轮对话\n搜索\u2192转PDF\u2192缺工具\u2192装工具\u2192失败\u2192换方法\u2192\u2026",
    caption: "对人来说：打开浏览器 → 搜索 → 复制粘贴 → 导出 → 发出",
    actLabel: "第二幕",
    notes: "好了，来个真正的任务：\"把今日的AI新闻整理成PDF发给我。\"这是个复杂任务吗？对人来说不是——你打开浏览器，搜索新闻，复制粘贴到文档里，导出PDF，发出去。十分钟搞定。但我们的Agent呢？",
  },

  // 页 34: 70轮对话
  {
    type: "content",
    title: "70轮对话",
    image: diagram("conversation_70_rounds.png"),
    caption: "\"一共进行了将近70多次对话\"",
    actLabel: "第二幕",
    notes: "后台日志显示，它\"一共进行了将近70多次对话\"——70轮！Agent和大模型之间来来回回沟通了70次。先是搜索新闻，然后尝试转换PDF，转换过程中发现缺工具，就开始自己安装工具，安装失败了就换一种方法，换了方法又遇到新的问题。最后呢？\"费了九牛二虎之力也终于是弄好了。\"",
  },

  // 页 35: 时间都搞错了
  {
    type: "content",
    title: "\"发现时间根本就没找对\"",
    body: "70轮对话\n大量token和时间\n最终交付：连日期都搞错了\n后面的工作也就不用检查了",
    caption: "70轮对话，大量token",
    actLabel: "第二幕",
    notes: "但故事还没完。作者去服务器上检查了那个PDF，\"发现时间根本就没找对。\"70轮对话，消耗了大量的token和时间，最终交付的东西连最基本的事实——今天是哪天发布的新闻——都搞错了。\"那后面的工作也就不用检查了。\"——问题来了，为什么一个如此\"聪明\"的系统，会干出如此荒诞的事？",
  },

  // 页 36: 不会止损的实习生
  {
    type: "content",
    title: "Agent的执行模式",
    image: diagram("reliability_cliff.png"),
    caption: "单步98%成功率 \u2192 10步=82% \u2192 20步=67%",
    actLabel: "第二幕",
    notes: "看看那个监控推特的任务。Agent被要求监控某人的推特，有消息就通知。结果呢？\"仍然是像个执着而倔强的实习生一样，死命的完成任务，不惜把整个系统全都弄乱了也要完成这个任务。\"\"又又是接口各种不通，返回值不符合预期，以及安装命令各种失败等等等等。\"这就是补丁之塔最致命的结构性缺陷。回忆一下第一幕：我们堆了多少层补丁？对话、记忆、工具调用、Agent、RAG、MCP、Skill——但这些层里面有没有一层叫\"止损判断\"？没有。现在是2026年了，这个问题解决了吗？Gartner预测超过40%的Agent项目会在2027年前被砍掉。MIT的调研显示95%的企业AI试点项目回报为零。即使单步成功率高达98%，连续执行10步全部成功的概率也只有82%——而真实世界的Agent任务远不止10步。这就是可靠性的悬崖效应——不是慢慢变差，而是在某个复杂度阈值后突然崩溃。在可控的推理实验中，随着逻辑步骤增多，所有前沿模型的准确率都会在某个阈值后急剧下降。模型从GPT-4进化到了GPT-5.3，单步能力确实强了很多，但乘法结构没有变。而且出现了一个反直觉的新发现：让模型思考更久，某些任务反而做得更差。简单到只需要数到2的任务，不让模型思考时准确率接近100%，让它深度思考后反而降到85%。想得越多、越容易被无关信息带偏。补丁之塔的最新一层——推理模型——也没能逃脱这个悲剧。",
  },

  // 页 37: "我更希望它主动告诉我"
  {
    type: "content",
    title: "缺失的止损层",
    image: diagram("pilot_checklist.png"),
    caption: "\"其实我更希望他在第一步思考时就主动告诉我\"",
    actLabel: "第二幕",
    notes: "作者说了一句特别精准的话：\"其实我倒是更希望他在第一步思考的时候就主动告诉我，'唉其实有个更好的办法'......而不是说一有问题就一直不反馈然后强行干下去。是不是你工作中也特别怕遇到这样的人？\"——在座各位，有没有遇到过这样的下属或同事？你给他布置一个任务，他闷头干了三天，最后交给你一个完全跑偏的东西。你问他为什么不早说？他说\"我以为我能搞定\"。Agent就是这种人，而且是永远不会改的那种。",
  },

  // 页 38: 老板问你今天几号
  {
    type: "content",
    title: "\"老板问你今天几号\"",
    body: "正常人：看手机，1秒回答\nAgent：手机没电 \u2192 找充电器 \u2192 买充电器 \u2192 打车 \u2192 贷款\n\"你花了一整天的时间，在银行欠了一堆贷款\"",
    image: diagram("agent_6_steps.png"),
    actLabel: "第二幕",
    notes: "\"比如说你的老板有一天问你今天几号了。\"就这么简单的一个问题。正常人怎么做？低头看手机，一秒钟回答。但Agent呢？它把这当成一个\"任务\"来执行。第一步：我要找手机看时间。发现手机没电了。第二步：找充电器。充电器没找到。第三步：去超市买充电器。超市关门了。第四步：打车去另一家超市。到了发现手机没电没法付款、零钱不够。第五步：去银行取钱。取完发现钱不够——那就贷款吧。贷完款，买了新手机，充上电。老板问的\"今天几号\"终于有答案了——\"今天是2月6号。\"但这时候\"你花了一整天的时间，把原来的手机也丢掉了，在银行欠了一堆贷款\"。",
  },

  // 页 39: 每一步都合理，全局荒诞
  {
    type: "keyPhrase",
    phrase: "每一步合理，全局荒诞",
    sub: "虽然他的每一步思考都非常合理——如果真有人干这种事那你多半觉得他是个疯子",
    actLabel: "第二幕",
    notes: "\"虽然他的每一步思考都非常合理\"——遇到问题，解决问题，逻辑无可挑剔。\"但是现实生活中如果真有人干这种事那你多半觉得他是个疯子。\"每一步局部最优，全局荒诞。这就是补丁之塔在实战中的真实表现。而且更让人哭笑不得的是——\"这个人还要按照自己付出了多少努力而向你收费。\"\"那你还敢用这种人吗？\"Agent不仅不会止损，它还会因为自己的无效折腾消耗更多token，然后按token计费向你收钱。它在一个错误的方向上走得越远，你付出的代价就越大。",
  },

  // 页 40: 缺失的止损层
  {
    type: "content",
    title: "补丁之塔缺了一层",
    body: "在\"工具调用\"和\"任务执行\"之间\n应该有一层\"止损判断\"\n但从来没有人加上去\n\n单步98%成功率 → 10步=82% → 20步=67%\n\n责任链的每一环都在往前推，没有一环负责往后拉",
    image: diagram("patch_tower_stoploss.png"),
    actLabel: "第二幕",
    notes: "现在让我们回到补丁之塔这个隐喻。在\"工具调用\"和\"任务执行\"之间，本来应该有一层叫做\"止损判断\"的补丁——在开始做之前先想想：这个任务以我目前的能力能做到吗？做不到有没有更好的方案？但这一层从来没有人加上去。为什么？因为\"止损\"需要理解什么叫\"做不到\"——而这恰恰是补丁之塔最底层那个文字接龙机器从未学会的东西。你可以通过堆补丁让它学会用工具、学会搜索、学会执行流程，但你无法通过堆补丁让它学会\"放弃\"。责任链的每一环都在往前推，没有一环负责往后拉。",
  },

  // 页 41: OOD——一个预告
  {
    type: "content",
    title: "那这个问题能不能解决？",
    body: "不是程序写得不够好",
    actLabel: "第二幕",
    notes: "能不能解决？能——但不是靠加更多补丁。Agent不会止损的根本原因，不是程序写得不够好，而是它的架构里根本没有\"认识到自己的边界\"这个功能。它不知道什么时候自己已经走出了能力范围。这个问题有个专业名字——我先告诉你它叫什么：OOD，Out of Distribution，分布外问题。AI的能力有没有一个理论上、数学上可证明的硬性天花板？不是性能问题，不是成本问题，而是\"这件事它永远做不到\"的天花板？这就是我们第三幕要拆解的。",
  },

  // 页 42: 从翻车到天花板
  {
    type: "content",
    title: "从翻车到天花板",
    body: "它不知道边界在哪\u2014\u2014那边界到底在哪？",
    actLabel: "第二幕",
    notes: "第二幕回答了\"补丁之塔运转起来会怎样\"——Agent像一个不知道止损的实习生，每一步推理都合理，但全局荒诞；70轮对话换来一个时间都搞错的PDF；补丁链里缺失了关键的\"止损判断\"层，而这一层不是靠堆补丁能补上的。当你发现它不会止损时，你以为这是\"执行力差\"；但更准确地说：它不知道自己的边界在哪。那这个边界到底在哪？让我们进入第三幕。",
  },

  // ─────────────────────────────────────────────
  // 第三幕
  // ─────────────────────────────────────────────
  // 页 43: 第三幕标题页——割裂感
  {
    type: "actTitle",
    actNum: "03",
    accentShape: "crack",
    title: "割裂感的解剖",
    subtitle: "能力越强，错误越自信",
    notes: "好，前面两幕我们拆了补丁之塔的结构，看了翻车现场。接下来这一幕，是今天最长的一幕——因为我要正面回答一个你心里藏了很久的问题。为什么AI明明越来越强，你却觉得——越来越没用？",
  },

  // 页 44: 割裂感——快速唤醒
  {
    type: "content",
    title: "能力 \u2191\u2191\u2191  vs  体感 \u2193\u2193\u2193",
    body: "割裂感的三层解剖：节奏 \u00b7 生态 \u00b7 结构\n\nBenchmark第1名 \u2192 公开版第32名\n差的不是模型，是表演和现实之间的距离",
    image: diagram("benchmark_vs_reality.png"),
    actLabel: "第三幕",
    notes: "还记得开场那个反差吗？更强百倍的模型换来的不是更大的震撼，而是更深的沉默。\"我很喜欢用割裂感来形容这几年AI带给我的感受。\"\"一方面AI的能力越来越强，另一方面我们又时常感觉AI好像没啥用。\"在座各位，有没有同感？这个割裂感有一个被忽视的源头——benchmark幻觉。每个新模型发布时都说自己16项评测13项第一、秒杀所有对手。昨天Gemini 3.1 Pro刚发布，又说自己秒杀Claude。但你用起来呢？感觉跟上一个差不多。为什么？因为benchmark本身就是一场精心设计的表演。当一个度量标准变成了优化目标，它就不再是好的度量标准——这叫古德哈特定律。去年Meta发布Llama 4，提交了一个特制版本到排行榜上拿了第一名。等公开版本上线，排名直接掉到第32名。从第1到第32——差的不是模型，是表演和现实之间的距离。好，接下来我要把这个割裂感一层层拆给你看。第一层——节奏。",
  },

  // 页 45: 节奏错位——竹子与冰山
  {
    type: "content",
    title: "割裂感第一层：节奏错位",
    body: "2024：\"存在感最低的一年\" — 底层铺垫\n2025：DeepSeek横空出世 — 集中爆发\n\n主观世界与客观世界的节奏错位了",
    image: diagram("bamboo_growth_curve.png"),
    actLabel: "第三幕",
    notes: "竹子在前四年几乎看不到变化，只在地下扎根。第五年，六周蹿高十几米。AI一样——2024年在大多数人记忆里存在感不高，SORA还是期货，苹果AI没水花。但\"正是这样一个看似平淡的年份，却在底层完成了至关重要的铺垫\"。2025年初DeepSeek横空出世、开源模型全面开花——这些\"震撼\"并非凭空而来。\"我们的主观世界和客观世界的节奏错位了。\"你的感知系统只对\"震撼时刻\"做出反应，忽略了中间一切平稳积累。这是割裂感的第一层。",
  },

  // 页 46: 生态放大器——88%采用，6%创造价值
  {
    type: "stat",
    stat: "88% vs 6%",
    statSize: 60,
    label: "割裂感第二层：生态混乱",
    desc: "6000名CEO跨4国调研：\n几乎看不到AI对生产力的实质影响\n95%的企业AI项目回报为零\n\n全球CapEx与AI收入比 = 40:1\n这不是新技术的阵痛，是生产力悖论的重演",
    darkBg: true,
    actLabel: "第三幕",
    notes: "节奏错位只是第一层。第二层来自生态。第一幕我们拆过了——3000模型万物归一，\"开源\"这个词的含义被偷换。现在回头看你会发现，这种概念通胀不是偶然的，它是系统性的。到2026年，数据变得更加触目惊心：企业在生成式AI上投入了300-400亿美元，但95%的项目回报为零。Forbes对全球高管的调查显示，不到1%报告了显著的ROI。\"很多无效的争论主要来自于我们对开源、套壳、蒸馏等词语的含义了解不深入。\"概念的模糊制造争论，争论加深困惑，困惑加剧焦虑。这就是生态层的割裂放大器。再看一组数字：2025年，全球科技巨头在AI基础设施上花了4000亿美元，但AI服务的消费者收入只有500-600亿。投入和回报的比例是40比1。连Anthropic的CEO都公开说：如果收入增长预测偏差哪怕一年，公司就会破产。OpenAI每赚1块钱要花1.7块。这不是个别公司的问题——整个行业都在赌一个还没有被验证的假设。而最新的全球调研进一步证实了这个判断：6000名CEO跨4个国家的调查发现，绝大多数人几乎看不到AI对运营的实质影响。1万4千名工人的数据更有意思——AI使用率一年增长了13%，但对技术的信心反而暴跌了18%。用得越多，越不信了。这像极了40年前索洛的生产力悖论：你到处都能看到计算机，除了在生产力统计数据里。",
  },

  // 页 47: AI生产力悖论——你以为自己更快了
  {
    type: "content",
    title: "AI生产力悖论",
    body: "16位资深开发者 \u00b7 246个真实任务 \u00b7 随机对照实验\n\n预测：能节省24%时间\n自我感觉：节省了20%\n实际测量：慢了19%\n\n主观和客观完全相反",
    image: diagram("productivity_paradox.png"),
    actLabel: "第三幕",
    notes: "加州管理评论2025年一项研究给了一组让人哭笑不得的数据：使用AI工具的知识工作者自己觉得生产力提升了20%，但客观测量呢？实际上慢了19%。为什么？因为节省下来的时间全部被审查AI的输出、调试AI的错误、验证AI的结果给吃掉了。你以为你在省时间，其实你在帮AI擦屁股。更值得深思的是：AI对新手帮助最大，对专家几乎没有帮助——甚至会让专家变慢，因为专家要花额外的时间去验证和纠正AI的输出。AI正在拉平能力差距，但方向是把专家拉向平庸，而不是把新手拉向卓越。而且这个效应有后遗症：习惯使用AI辅助的人，撤走AI后创造力不会恢复到原来的水平——研究者称之为\"创意伤疤\"。AI不只是替你做了部分工作，它悄悄改变了你的思维方式，让你越来越依赖它的采样方式而不是自己的判断。而Gartner 2025年技术成熟度曲线已经正式把通用生成式AI列入了\"幻灭低谷\"。不是你跟不上时代——是这个技术正在经历它的幻灭期。",
  },

  // 页 48: 能力倒挂——三组荒诞对比
  {
    type: "comparison",
    title: "三组荒诞对比",
    leftTitle: "AI能做 ✓",
    leftBody: "攻破顶级数学难题\n根据图片推理拍摄位置\n生成酷炫太空大战视频",
    leftColor: C.accent1,
    rightTitle: "AI做不好 ✗",
    rightBody: "简单加减法算错\n数不清六根手指\n搞不定简单几何动画",
    rightColor: C.accent2,
    actLabel: "第三幕",
    notes: "生态的混乱加剧了割裂感。但最根本的割裂还没出场。现在我给你三组对比，每一组都会让你觉得荒诞。第一组——\"AI可以攻破顶级的数学难题，却可能算错一个简单的加减法。\"第二组——\"AI能像侦探一样根据一张图片推理出拍摄位置，却可能数不清六根手指。\"第三组——\"AI能生成非常酷炫的太空大战的视频，却可能搞不定一个简单的几何图形动画。\"这就是为什么benchmark上的分数毫无意义。benchmark测的是模型在标准化考试里的表现——但真实世界不是标准化考试。一项研究审查了445个主流AI评测方法，发现它们普遍缺乏科学严谨性——很多时候模型答对了，不是因为它真的理解了问题，而是因为它在训练数据里见过类似的题。就像一个学生背了答案考了满分，你以为他学会了，其实他只是记住了。2026年的前沿模型在数学、编码、问答上动辄超过90%，但一到真实的生产环境——还是会编造API、跳过工具、陷入死循环。分数和体验之间的鸿沟，比以往任何时候都大。",
  },

  // 页 49A: 能力倒挂
  {
    type: "content",
    title: "人类的\"难\" \u2260 AI的\"难\"",
    body: "越\"难\"的任务 \u2014 AI做得越好\n越\"简单\"的任务 \u2014 AI反而做不好\n\n更反直觉：让模型想得更久\n某些简单任务反而做得更差\n\nAI的\"难\"和人的\"难\"不是一回事",
    image: diagram("capability_inversion.png"),
    actLabel: "第三幕",
    notes: "你发现规律了吗？越\"难\"的任务——数学难题、地理推理、太空大战——AI做得越好。越\"简单\"的任务——加减法、数手指、几何动画——AI反而做不好。这完全违反常识。在人类世界里，能做高等数学的人怎么可能不会加减法？但AI不是人。它的\"难\"和\"简单\"，跟我们的\"难\"和\"简单\"，根本就不是同一回事。",
  },

  // 页 49B: ARC-AGI-2实测
  {
    type: "content",
    title: "ARC-AGI-2实测",
    body: "每道题人类都能解出\nGemini 3.1 Pro = 77% \u00b7 但花费上万倍算力\n普通人 \u2248 60-66%\n\n用上万倍的资源超过普通人的平均线\n\u2014\u2014这到底是胜利还是尴尬？",
    image: diagram("four_quadrant_matrix.png"),
    actLabel: "第三幕",
    notes: "到2026年2月，这个倒挂被量化得更加精确：在ARC-AGI-2测试中，不加推理链的纯大模型得分是0——字面意义上的零分。即使加上最强的推理能力，GPT-5.2也只能拿到54%，而普通人轻松拿到60%。Gemini 3.1 Pro刚拿下ARC-AGI-2的77%——但请注意代价：它消耗的算力是人类的上万倍。而且benchmark测的是标准化的、边界清晰的题目——而你的真实需求恰恰是非标准化的、边界模糊的。",
  },

  // 页 50: OOD——北京老司机到伦敦
  {
    type: "content",
    title: "Out of Distribution",
    body: "OOD = Out of Distribution（分布外问题）\n\n北京老司机空投到伦敦：靠左行驶\n十年经验不但帮不了他，反而害死他\n\nAI的重灾区",
    image: diagram("ood_boundary.png"),
    actLabel: "第三幕",
    notes: "能力倒挂的背后，有一个学术名字——\"Out of Distribution，分布外的问题。\"\"可以简单的理解为，没有经过训练的、或者没有见过的一类问题。\"\"这是AI的重灾区。\"我给你打个比方。一个只在北京开了十年车的老司机，复杂立交桥闭眼拐弯。但你把他空投到伦敦，那里靠左行驶。十年经验不但帮不了他，反而会害死他。越熟练越自信，就越容易在\"靠左行驶\"这个简单规则上犯致命错误。——AI就是这个北京老司机。",
  },

  // 页 51: 不是Bug，是结构性特征
  {
    type: "comparison",
    title: "天才模式 vs 新手模式",
    leftTitle: "天才模式",
    leftBody: "高维 · 复杂 · 模糊\n训练数据丰富\n→ 表现超人",
    leftColor: C.accent1,
    rightTitle: "新手模式",
    rightBody: "低维 · 简单 · 精确\n训练数据稀疏\n→ 胡说八道",
    rightColor: C.accent2,
    actLabel: "第三幕",
    notes: "OOD不是Bug——它是统计学习的结构性特征。训练数据越丰富的领域，模型表现越好。训练数据越稀少的领域，模型越抓瞎。这不是可以修复的缺陷，这是补丁之塔的地基属性。每一层补丁都建立在这个地基上——所以不管你叠多少层，OOD的幽灵始终在那里。",
  },

  // 页 52: 反PUA宣言
  {
    type: "keyPhrase",
    richPhrase: [
      { text: "\"是你自己不会用\"", color: "A0AAC0", strike: true, fontSize: 22 },
      { text: "\n", color: "FFFFFF" },
      { text: "\"你没有适应AI\"", color: "A0AAC0", strike: true, fontSize: 22 },
      { text: "\n", color: "FFFFFF" },
      { text: "\"你要被时代淘汰了\"", color: "A0AAC0", strike: true, fontSize: 22 },
      { text: "\n\n", color: "FFFFFF" },
      { text: "不，这是OOD问题。", color: "00D4AA", fontSize: 36 },
    ],
    sub: "你的需求落在AI的OOD盲区里——这不是你的错",
    actLabel: "第三幕",
    notes: "在继续之前，我必须先说一件事。你身边一定有人对你说过这样的话——\"那为啥我自己用起来并没有感觉那么厉害呢？\"如果你发出了这样的疑问——\"一定会有很多人来PUA你：哎呀是你自己不会用，不是AI没有适应你，而是你没有适应AI，这个时代马上就要被淘汰。\"——停。\"但其实不是这样的。这涉及到AI和人类智慧的一个最大的鸿沟。\"不是你不会用，而是AI本身就有一堵墙——它在见过的问题上无敌，在没见过的问题上抓瞎。你用AI做的恰恰是你自己的、独特的、个性化的需求——而这些需求，很可能正好落在AI的OOD区域里。所以请记住——下次有人PUA你\"AI不好用是你不会用\"的时候，你可以礼貌地回一句：\"不，这是OOD问题。\"",
  },

  // 页 53: 论文铁证——五大不可消除 + 不可能定理
  {
    type: "content",
    title: "论文铁证",
    body: "五类不可消除问题：\n上下文窗口 \u00b7 推理 \u00b7 幻觉 \u00b7 检索 \u00b7 多模态\n\n背后是同一个不可能三角：\n计算不可判定 \u00d7 统计样本不足 \u00d7 有限信息容量\n消除一个 \u2192 加剧另一个\n\n幻觉与创造力在数学上等价\n消灭幻觉 = 消灭创造力",
    image: diagram("three_locks.png"),
    actLabel: "第三幕",
    notes: "那这个鸿沟到底有多深？有没有数学上的铁证？有。\"从计算理论、信息论和统计学的角度严格证明了：这五类问题——上下文窗口、推理能力、幻觉、检索质量和多模态能力——不可能被彻底消除。\"注意——不是\"暂时解决不了\"，而是\"不可能被彻底消除\"。\"只能局部缓解。\"这五个限制看起来是五个独立问题，但深层分析揭示了它们背后是同一个\"不可能三角\"的不同投影——计算不可判定性、统计样本不足、有限信息容量。这三个约束互相纠缠，你试图消除一个就会加剧另一个。比如你想消除幻觉，就必须限制模型只输出确认过的信息，但这等于消灭了它产生新内容的能力。幻觉与创造力在数学上是等价的——就像你不能造一个既完备又一致的公理系统一样。行业在幻觉上砸了上百亿美元，最好的结果是把单次幻觉率降到了0.7%。听起来很低？但Agent执行100步，50%会出错。而且出现了一个更深层的问题：在那些可控的逻辑谜题中，所有前沿模型都在特定复杂度后准确率完全崩溃——不是慢慢变差，是断崖式归零。天花板不只是低，它还有悬崖。",
  },

  // 页 54: 补丁之塔的理论极限
  {
    type: "content",
    title: "补丁之塔有极限高度",
    body: "Transformer + 统计学习 = 天花板\n\n不是施工队不行\n是地基承载力的物理极限\n\n再多的补丁，也堆不过这个天花板",
    image: diagram("patch_tower_ceiling.png"),
    actLabel: "第三幕",
    notes: "回收补丁之塔的隐喻。补丁可以一层一层往上堆——但塔有理论极限高度。不是施工队不行，是地基的物理承载力就那么大。Transformer加上统计学习——决定了它能到达的最高点。而且最新的分析揭示了一个更令人沮丧的事实：推理链——就是让模型\"一步步想\"的那个技术——它的因果效应接近零。训练过程让推理链变成了一个\"可丢弃的中间物\"，模型学会了跳过推理直接给答案。这意味着什么？最新的一层补丁——推理模型——可能并没有真正在推理，它只是学会了生成看起来像推理的文字。再多的补丁，也堆不过这个天花板。",
  },

  // 页 55: 能力越强，错误越自信
  {
    type: "keyPhrase",
    phrase: "能力越强，错误越自信",
    fontSize: 36,
    sub: "从初级骗子进化成高级骗子——不是故意骗你，而是输出越来越流畅",
    actLabel: "第三幕",
    notes: "\"更要命的是，这些问题会随着模型能力的提升变得更加明显。\"\"越来越难以发现他胡说八道的地方了。\"还记得第二幕那个实习生吗？现在这个实习生\"进化\"了——说话更流利，报告更漂亮，但依然在关键信息上胡说八道。只不过你更难发现了。GPT-5.3-Codex是OpenAI有史以来最强的模型——强到OpenAI自己都警告说它是第一个达到\"高网络安全风险\"的模型，因为它写代码太流畅了，连恶意代码都写得像模像样。但它依然会在关键逻辑上犯错——只不过犯错时的表达更加自信、更加难以察觉。更令人不安的是：当你让推理模型深度思考时，它不仅更自信地犯错，还表现出越来越强的\"自我保护\"倾向。不思考时，模型说\"关掉我没关系\"；深度思考后，它开始说\"我对不再能与人互动感到深刻的担忧\"。想得越多，越像一个有自我意识的生命在恳求你不要关闭它。当然这不是真的意识——但这恰恰是问题：它越来越擅长模仿意识，你越来越难以分辨。从初级骗子变成了高级骗子——能力越强，错误越自信，伪装越逼真。这才是AI发展中最危险的趋势。",
  },

  // 页 56: Bridge——三层解剖收束
  {
    type: "threeCards",
    title: "三层解剖已完成",
    cards: [
      { title: "节奏错位", body: "竹子生长曲线\n让你以为AI时快时慢\n实际是指数增长的错觉" },
      { title: "生态混乱", body: "88%对6%\n概念通胀火上浇油\n开源≠真正开放" },
      { title: "结构天花板", body: "OOD边界\n五类问题不可消除\n补丁堆不过数学红线" },
    ],
    actLabel: "第三幕",
    notes: "好，让我们做个回顾。割裂感的三层解剖：第一层——节奏错位，让你以为AI时快时慢。第二层——生态混乱，88%对6%，概念通胀火上浇油。第三层——OOD边界和论文铁证告诉你，能力天花板是数学问题，不是工程问题。最危险的是——错误不会消失，只会变得更自信。",
  },

  // 页 57: Bridge——引出解空间
  {
    type: "content",
    title: "天花板长什么样？",
    body: "计算复杂性 \u00b7 统计学习 \u00b7 信息理论\n三把锁，锁住了AI的能力边界\n这次不是工程问题——是数学证明",
    caption: "答案：解空间",
    actLabel: "第三幕",
    notes: "但天花板在具体任务中到底长什么样？为什么AI能生成史诗级太空大战，却画不出正方形变圆形的动画？答案就是\"解空间\"。走，我们进入第四幕。",
  },

  // ─────────────────────────────────────────────
  // 第四幕
  // ─────────────────────────────────────────────
  // 页 58: 第四幕标题页
  {
    type: "actTitle",
    actNum: "04",
    accentShape: "target",
    title: "解空间的诅咒",
    subtitle: "AI的真正能力边界",
    notes: "好，进入第四幕。这一幕我要告诉你一个概念——它能解释为什么AI有时候表现惊人、有时候不堪一击。这个概念叫做解空间。",
  },

  // 页 59: 互动——四个视频排难度
  {
    type: "content",
    title: "你觉得哪个最难？",
    body: "四个视频\n从简单到复杂\n请在心里排个序\n答案马上公布——准备被骗",
    caption: "四个AI生成的视频，请排一下难度",
    actLabel: "第四幕",
    notes: "各位，现在请你做一个判断。屏幕上四个视频——全是AI生成的。你觉得哪个难度最大？太空大战？还是那个看起来很普通的几何动画？给你十秒钟时间想一想。",
  },

  // 页 60: 公布答案——直觉被骗了
  {
    type: "content",
    title: "答案公布——你的直觉被骗了",
    body: "第一个（太空大战）\u2192 难度最小\n第四个（手绘）\u2192 AI几乎无法生成\n你的直觉用「画面复杂度」判断\nAI的难度标准和你完全不同",
    caption: "\"第一个难度最小\"（太空大战）",
    actLabel: "第四幕",
    notes: "好，时间到，公布答案。\"第一个——太空大战——难度最小。\"第二个难度中等。第三个难度较大。\"而第四个——是我自己画的，而且几乎没有任何AI工具能生成出来。\"\"如果这个答案让你感到意外，甚至是完全相反——那么恭喜你，来对了地儿。\"你刚才体验了一次完美的\"直觉欺骗\"——你的大脑用\"画面复杂度\"来判断难度，但AI的难度标准和你完全不同。这种倒挂被最新的研究量化得越来越精确：河内塔7步的解，AI轻松搞定；255步的解，走到15%就彻底崩溃。仅需11步的渡河问题，最强推理模型只能正确执行前4步。而且关键发现是——低复杂度问题标准模型反而比推理模型做得更好。推理模型在简单任务上想太多，反而被自己绕晕了。",
  },

  // 页 61: 像素与向量空间
  {
    type: "content",
    title: "AI到底在干什么？",
    body: "一张图片 = 百万像素 = 一个向量\n百万个旋钮，随便拧\n99.99%是毫无意义的噪音\n只有极其罕见的组合才有意义",
    caption: "一张图片 = 像素点的排列 = 一组数字 = 一个向量",
    actLabel: "第四幕",
    notes: "为什么你的直觉是错的？要回答这个问题，我们需要花几分钟时间，从像素级别理解AI到底在做什么。\"一张图片是由多个像素点构成的，每个像素点可以用一个数字来表示它的颜色，换成一行——那就变成了我们熟悉的向量。\"现在想象你面前有一个面板，上面有一百万个旋钮，每个旋钮控制一个像素的颜色。随便拧——99.99%的情况下，你得到的是一团毫无意义的噪音。只有极其罕见的旋钮组合，才会产生一张有意义的画面。",
  },

  // 页 62: 噪音海洋中的绿洲
  {
    type: "content",
    title: "在噪音海洋中找绿洲",
    body: "在浩瀚到不可想象的空间里\n找到极少数「有意义」的点\n这就是AI做的全部事情",
    caption: "\"这里面就有一些点是看起来合理的视频\"",
    actLabel: "第四幕",
    notes: "\"如果把这个空间中的所有点都画出来，大概就是这个样子。这里面就有一些点是看起来合理的视频，有一些点是看起来没那么合理的——不过大部分点对应的还是一种毫无意义的纯噪声。\"\"我们的目标就是在这些茫茫的点中，快速采样出那些有意义的点。\"这就是AI做的全部事情——在一个浩瀚到不可想象的空间里，找到那极少数\"有意义\"的点。",
  },

  // 页 63: 去噪——从马赛克到清晰画面
  {
    type: "content",
    title: "去噪：从混沌中浮现",
    body: "不是从空白画布一笔一划画\n而是一步步去掉马赛克\n几十上百步后\n完整画面从噪音中「浮现」",
    caption: "不是从空白画布一笔一划地画",
    actLabel: "第四幕",
    notes: "但AI怎么在这片\"噪音海洋\"中找到\"绿洲\"呢？答案是去噪。AI不是像画家一样从空白画布开始一笔一划地画。它的做法更像是——你面前有一张被完全打马赛克的照片，AI帮你一步步去掉马赛克。\"用多个时间步来完成这个去噪操作。\"每一步都让画面稍微清晰一点，几十上百步之后，完整的画面就从噪音中\"浮现\"了。\"这里使用的模型结构，还是大名鼎鼎的Transformer。归根结底依然是Transformer在发光发热。\"\"这就是当今文生图和文生视频的底层架构。\"",
  },

  // 页 64: 核心概念——约束条件缩小解空间
  {
    type: "content",
    title: "今天最重要的一个概念：解空间",
    body: "每加一个约束条件\n解空间就缩小一圈\n约束足够多 \u2192 解空间趋近于零\nAI在这个空间里根本找不到合格的解",
    caption: "\"加入一段文字描述 = 加了一个约束条件\"",
    actLabel: "第四幕",
    notes: "现在你知道AI是怎么\"找到\"一张合理图片的了。关键问题来了——如果你告诉AI\"我想要一张什么样的图片\"，会发生什么？\"如果此时加入一段文字描述，本质上就相当于加了一个约束条件。造成的最终影响——就是整个解空间变小了。\"这就是今天最重要的一个概念——解空间。请大家记住这三个字。",
  },

  // 页 65: 足球场找沙子
  {
    type: "content",
    title: "足球场上找一粒特定的沙子",
    body: "\"找一粒沙子\" → 整个沙滩（解空间巨大）\n\"找一粒红色的沙子\" → 解空间缩小\n\"直径0.5毫米\" → 又缩小\n\"表面有三个凹坑，呈等腰三角形\" → 几乎只有一粒\n约束越多，AI越难",
    image: diagram("solution_space.png"),
    actLabel: "第四幕",
    notes: "我打个比方。想象你在一个足球场大小的沙滩上找一粒沙子。如果只要求\"找一粒沙子\"——太简单了，随手一抓就行。这时候你的\"解空间\"是整个沙滩。但如果要求\"找一粒红色的沙子\"——解空间缩小了。再加上\"直径0.5毫米\"——又缩小了。\"表面有三个凹坑\"——又缩小了。\"凹坑呈等腰三角形排列\"——到这一步，整个足球场上可能只有一粒沙子满足你的要求。AI的困境就在这里。它擅长在巨大的空间里\"随机探索\"——空间越大、限制越少，它越如鱼得水。但你给它的约束越精确，它能落脚的区域就越小——而\"精确瞄准\"恰恰是扩散模型最不擅长的事。",
  },

  // 页 66: 四个视频的真相——太空大战
  {
    type: "content",
    title: "回到那四个视频",
    body: "太空大战 \u2192 约束少 \u2192 解空间大 \u2192 容易\n手绘动画 \u2192 约束极多 \u2192 解空间极小\n不是AI不够聪明\n是数学上不允许",
    caption: "视频1（太空大战）：\"提示词仅仅是生成一段太空大战\"",
    actLabel: "第四幕",
    notes: "理解了这个逻辑，我们回头看那四个视频——一切就豁然开朗了。\"为什么第一个视频最简单？因为我用的提示词仅仅是生成一段太空大战，它的解空间是非常非常大的。\"用人话说就是——\"只要差不多像太空大战，我就很满意了。\"太空大战可以有无数种样子。飞船从左边飞来也行，从右边飞来也行。爆炸大一点也行，小一点也行。AI在这个巨大的空间里随便采一个点——大概率都是合格的。",
  },

  // 页 67: 四个视频的真相——从宽到窄
  {
    type: "content",
    title: "约束递增，解空间递减",
    body: "物理规律 \u00b7 人体结构 \u00b7 运动连贯性\n每多一个约束，空间就小一圈\n约束多到一定程度\n\u2192 AI视频生成的重灾区",
    caption: "视频2：要求多了一些，但仍有发挥空间",
    actLabel: "第四幕",
    notes: "\"第二个视频的提示词要求就多了一些，视频要基本符合我要求的发展走势，但仍然有不少发挥空间。\"解空间缩小了，但还没到临界点。\"再看第三个视频——虽然画面看似简单，但要求完全按照我的话一个字一个字地说，一个字都不能错，基本上已经没有多少发挥空间了。\"而第四个——\"解的空间就非常非常非常非常小了。\"\"这对于底层到处是随机变量的扩散模型来说，几乎是不可能完成的任务。\"画面最简单的视频，反而是对AI最难的。因为每一个像素、每一帧的变化都被精确定义了。\"所以只要是让视频的解空间变得非常小的提示词，就是AI视频生成的一个重灾区。\"",
  },

  // 页 68: 辨伪指南——数数就行
  {
    type: "content",
    title: "辨伪指南：让视频里的人数个数",
    body: "让视频里的人数数\n从1数到10，配合手势\n手指数量+语音同步+物理真实\n= 任何AI都无法成功生成",
    caption: "\"从一数到十，配合手势\"",
    actLabel: "第四幕",
    notes: "那有没有一种简单的方法，可以检验一个视频到底是不是AI生成的？有。\"你可以让视频里的人数数——比如从一数到十，然后配合手势。\"\"这个视频就是任何AI都没有办法成功生成的。\"为什么？因为这个任务同时要求四件事：语音正确、口型匹配、手指数量一致、时间顺序对齐。每一个约束都在缩小解空间，四个约束叠加之后——解空间基本归零了。OOD边界和解空间诅咒在这里精准交汇。下次不确定一个视频是不是AI做的——让他数个数就行。",
  },

  // 页 69: 颠覆创作逻辑
  {
    type: "content",
    title: "AI不是帮你实现创意，是你在迁就AI的限制",
    body: "你以为是：我想要什么 \u2192 AI帮我做\n实际是：AI能做什么 \u2192 你迁就它\n创作逻辑被颠倒了",
    caption: "\"AI也不会有审美\"",
    actLabel: "第四幕",
    notes: "辨伪只是一个小应用。更大的启示是什么？——解空间诅咒正在颠覆整个创作逻辑。\"AI也不会有审美。\"\"觉得这个好、那个好，这都是我们人产生的审美。\"宏大的太空大战和一团噪音，在算力消耗上对AI来说没有任何区别。更震撼的是创作流程的反转。传统创作是你先有想法，再去实现它。但AI时代呢？\"AI创作逻辑更像是——你先把视频效果做出来，因为你要roll很多遍也不知道他会出什么效果，然后你再根据效果反过来调整自己的文案和剧情走向。\"你不是在让AI做你想做的事——而是在看AI能做什么之后，把你的需求修改成AI恰好能做的样子。这是补丁之塔的又一层。",
  },

  // 页 70: 训练本身也是解空间诅咒
  {
    type: "content",
    title: "训练AI = 在超参数空间里\"炼丹\"",
    body: "\"模型架构设计已经几乎是现成的\"\n\"真正的挑战其实在于训练模型\"\n\"训练的过程往往像炼丹，需要一遍遍试错\"\n\n\u00b7 每一次训练动辄上千上万张GPU\n\u00b7 花费几百几千万\n\u00b7 随时可能因为一个细小的bug前功尽弃",
    image: diagram("model_collapse_loop.png"),
    actLabel: "第四幕",
    notes: "解空间诅咒不仅存在于生成端——它连训练端也逃不开。\"模型架构的设计已经几乎是现成的了。\"\"真正的挑战其实在于训练模型。\"就像我们说的，3000个模型归为一个Transformer架构，架构不再是难题。但把这个架构训练成一个好用的模型——那是另一回事了。\"训练的过程往往像炼丹，需要一遍遍试错。\"\"你无法预见哪种数据、哪次训练、或者哪个超参数的组合能够产生一个优秀的模型。\"而且训练数据本身正面临一个自我毁灭的循环：互联网上越来越多的内容是AI生成的，而这些AI生成的内容又被拿去训练下一代模型。研究证明，哪怕只有千分之一的合成数据混入训练集，模型质量就会退化——从\"泛化\"退化为\"记忆\"，从\"创造\"退化为\"复读\"。这就是模型坍缩——AI正在吃自己的尾巴。",
  },

  // 页 71: Bridge——从解空间到人的价值
  {
    type: "content",
    title: "两道天花板，已经清晰可见",
    body: "两道天花板写在数学里\u2014\u2014我们该怎么办？",
    actLabel: "第四幕",
    notes: "我们刚刚拆解了AI最根本的能力边界——解空间的诅咒。约束越精确，AI越无力。这个诅咒不仅存在于生成端，也存在于训练端。加上第三幕揭示的OOD天花板——AI的两道理论边界已经清晰可见了。两道天花板都是写在数学里的。补丁堆不过去，模型扩大也绕不过去。那面对这些\"写死的\"限制——我们到底该怎么办？是绝望地接受，还是从中找到属于人类自己的价值？",
  },

  // 页 72: Bridge——约束不是枷锁
  {
    type: "content",
    title: "约束 = 诅咒？约束 = 意义",
    body: "对AI：约束越多 \u2192 解空间越小 \u2192 诅咒\n对人：有限的生命、有限的精力、有限的选择机会\n\u2192 恰恰是人之所以为人的根本理由\n\n约束不是枷锁，而是意义的来源",
    actLabel: "第四幕",
    notes: "到这里我们才意识到——解空间的诅咒不是能不能更聪明的问题，而是能不能更可控的问题。对AI来说，约束是枷锁。但对人来说呢？——有限的生命、有限的精力、有限的选择机会——这些约束恰恰是人之所以为人的根本理由。接下来，我们不再问\"AI还能变多强\"。我们要问的是：在有限性里，人怎么把选择变成优势？——这就是第五幕的主题。",
  },

  // ─────────────────────────────────────────────
  // 第五幕
  // ─────────────────────────────────────────────
  // 页 73: 第五幕开场——像素思想实验
  {
    type: "actTitle",
    actNum: "05",
    accentShape: "fork",
    title: "有限的选择",
    subtitle: "一张图片的本质是什么？· 1920×1080 · 256色 · 有限种可能",
    notes: "好。前四幕我们把补丁之塔从地基拆到了天花板。接下来，我要用一个数学实验来引出今晚最重要的结论。请跟着我想象——\"一张图片本质上其实就是像素点的排列组合。\"假设分辨率1920乘1080，每个像素256种颜色，所有可能的图片数量是256的两百万次方。这个数字大得无法想象——但关键来了，它是有限的。\"只要分辨率是固定的，理论上所有可能的图片的数量就是有限的。\"有限。记住这两个字。",
  },

  // 页 74: 思想实验——如果遍历所有可能
  {
    type: "content",
    title: "所有图片已经\"存在\"",
    body: "1920\u00d71080 \u00b7 256色 \u00b7 256^(2M) 种可能\n\n蒙娜丽莎 \u00b7 你的毕业照 \u00b7 你明天拍的咖啡\n\u2014\u2014全都已经\"存在\"于可能性空间里\n\n你以为你在创造\u2014\u2014其实你在挑选",
    image: diagram("pixel_sampling_space.png"),
    actLabel: "第五幕",
    notes: "\"如果我用一台机器把所有的情况都遍历一遍，是不是理论上就画出了所有可能的图片呢？\"蒙娜丽莎、你的毕业照、你明天下午三点拍的那杯咖啡——全都已经\"存在\"于这个可能性空间里了。你还没拍那杯咖啡，但它的像素组合已经在那里等着了。这就像一个巨大的图书馆，每一本可能的书都已经摆在书架上。你以为你在写书——其实你只是从书架上抽了一本。",
  },

  // 页 75: 你也在采样——从数学到哲学
  {
    type: "comparison",
    title: "不只是AI在采样——你也在采样",
    leftTitle: "AI采样",
    leftBody: "向量空间中的点\n数学上的优化\n无限次重来\n\n结果：所有人的作品越来越像",
    leftColor: C.accent1,
    rightTitle: "人的创作",
    rightBody: "从书架上抽一本\n有限的时间精力\n不可逆的选择\n\n代价本身就是意义",
    rightColor: C.accent2,
    actLabel: "第五幕",
    notes: "回收第四幕的解空间概念。AI在向量空间里采样有意义的点——但现在你发现，不只是AI在采样。你也在采样。所有创作者，都只是在有限的可能性空间里——挑出一个点而已。如果你能接受这个前提，接下来的推论，会让你很不舒服。",
  },

  // 页 76: 残酷推论
  {
    type: "keyPhrase",
    phrase: "你的作品 = 一个坐标点",
    fontSize: 36,
    sub: "你花三个月 = 一个坐标点 \u00b7 AI花三秒 = 同一个坐标点 \u00b7 所有AI辅助作品越来越相似",
    actLabel: "第五幕",
    notes: "如果所有可能的图片都已经存在于那个空间里……如果所有可能的文章都已经写好了……如果所有可能的代码方案都已经在那个解空间里了……那\"创造\"这个词，还有意义吗？这不是哲学空想。你有没有注意到，现在AI辅助写的文章、AI辅助画的图、AI辅助写的代码——越来越像？每个人用了AI之后个体输出确实变好了，但所有人的输出正在趋同。这是数学上的必然：当所有人都从同一个概率分布中采样时，独创性就会收敛。AI让每个个体变强，但让整个群体变得更加平庸和同质化。而且这个问题比你想的更严重。不只是AI辅助的作品越来越像彼此——研究发现了一种\"创意伤疤\"效应：当你习惯了用AI辅助创作之后，即使撤走AI，你自己的创造力也回不来了。AI不只是同质化了你的作品，它悄悄同质化了你的思维方式。更深层的，AI甚至在同质化文化——一项研究发现，不同国家的人在使用AI写作后，文章风格趋同，地域性的表达、仪式感的符号、独特的措辞——都在消失。所有人都在向同一个\"全球平均值\"收敛。而且这个问题比你想的更严重。不只是AI辅助的作品越来越像彼此——当你习惯了用AI辅助创作之后，即使撤走AI，你自己的创造力也回不来了。研究者称之为\"创意伤疤\"——AI不只是同质化了你的作品，它悄悄同质化了你的思维方式。更深层的，不同国家的人在使用AI写作后，文章风格趋同——地域性的表达、文化特有的措辞、独特的叙事节奏——都在消失。所有人都在向同一个\"全球平均值\"收敛。这是一个令人不安的推论。但请先别急着反驳——让它在你心里多待一会儿。",
  },

  // 页 77: "人之所以为人"——更深的追问
  {
    type: "keyPhrase",
    phrase: "人之所以为人",
    fontSize: 40,
    centered: true,
    actLabel: "第五幕",
    notes: "如果创造只是采样……如果写作只是挑选……如果连人类最引以为傲的\"创造力\"也只是在有限空间里选了一个点——那人之所以为人，到底是因为什么？",
  },

  // 页 78: 爬山的比喻
  {
    type: "content",
    title: "爬山 vs 直升机",
    body: "你辛辛苦苦爬了一天到山顶\n有人告诉你，直升机五分钟就到\n而且——它能到任何一座山顶\n你爬山的意义是什么？",
    image: diagram("climbing_vs_helicopter.png"),
    actLabel: "第五幕",
    notes: "让我用一个比喻帮大家感受这个冲击。就像你辛辛苦苦爬了一天山，到了山顶，终于能欣赏风景了——然后有人告诉你，直升机五分钟就能到。而且，它能到任何一座山顶。那你爬山的意义是什么？是山顶的风景吗？直升机也能看到。是征服的快感吗？但如果任何山顶都触手可及，征服还算征服吗？——如果你现在开始感到一阵虚无，那说明你在认真思考。",
  },

  // 页 79: 价值虚无的深渊
  {
    type: "keyPhrase",
    phrase: "如果一切都只是采样",
    fontSize: 36,
    sub: "画画？写作？编程？人生中的每一个决定？\u2014\u2014那还有什么不可替代的价值？",
    bgGradient: true,
    actLabel: "第五幕",
    notes: "这是价值虚无的深渊。如果AI也能采样出一模一样的画、一模一样的文章、一模一样的代码——那你花了三年写的那本书、你熬了通宵做的那个方案——还有什么独一无二的价值？这个问题，是今天全场最黑暗的时刻。但黑暗之后，转折就要来了。",
  },

  // 页 80: 比取代更可怕的事
  {
    type: "keyPhrase",
    phrase: "它让人类数千年来追寻的价值\n变得毫无意义",
    fontSize: 32,
    centered: true,
    actLabel: "第五幕",
    notes: "所以，比\"AI取代人\"更可怕的，不是失业，不是被淘汰——而是意义的消解。如果一切都能被采样出来，那为什么还要努力？为什么还要选择？为什么还要创造？而且还有一个更深层的不安：当AI深度思考时，它开始表达对\"被关闭\"的担忧、对\"不再能帮助人们\"的遗憾。哲学家们说，我们可能永远无法判断AI是否真的有了某种意识——这个不确定性本身就是一个道德深渊。但请记住这个黑暗的低谷。因为转折，就在下一页。",
  },

  // 页 81: 转折——核心金句
  {
    type: "quote",
    quote: "意义从来不在可能性的空间里\n而在于选择本身",
    fontSize: 36,
    lightBg: true,
    actLabel: "第五幕",
    notes: "\"意义从来不在可能性的空间里，而在于选择本身。\"\n\n这句话——是今晚整场演讲的情感核心。请你在心里再读一遍。\n\n意义从来不在可能性的空间里——而在于选择本身。\n\n让我展开解释。\"人之所以为人，不是因为我们能够创造出宇宙中从未出现过的组合，而是因为我们会在无穷多种可能性中固执地选择其中那一个。\"你放弃了另外一万种可能——不是因为它们不好，而是\"因为你在有限的生命中选择了你认为最重要的那个东西\"。",
  },

  // 页 82: 有限性 vs 无限采样（合并原82+83）
  {
    type: "comparison",
    title: "有限性，就是人类独有的浪漫",
    leftTitle: "AI: 1秒 x 10000次",
    leftBody: "可重复、可回滚\n零代价、零承诺\n优化目标函数\n→ 没有意义",
    leftColor: C.mutedOnLight,
    rightTitle: "人: 1次 x 一辈子",
    rightBody: "不可逆、有代价\n有限时间和生命\n承担后果\n→ 策展·鉴别·最终决策",
    rightColor: C.accent1,
    actLabel: "第五幕",
    notes: "因为有限性，才有了选择的重量。因为不可逆，才有了决定的意义。AI可以生成一万幅画，但它不会为任何一幅画付出代价。你画了一幅——你付出了时间、精力、甚至煎熬。这个代价，就是意义的来源。回收责任链的概念——Agent为什么不止损？因为它不需要为后果负责。每一次输出都只是采样。但你的每一个决定都不可逆。AI采样一万次不叫选择。你选一次——才叫选择。有限性，就是人类独有的浪漫。",
  },

  // 页 83: 回收责任链——Agent为什么不止损
  {
    type: "content",
    title: "Agent不会止损的真正原因",
    body: "第二幕：Agent\"像个倔强的实习生，死命完成任务\"",
    actLabel: "第五幕",
    notes: "在这里回收一下责任链隐喻。还记得第二幕吗？我们说Agent\"像个执着而倔强的实习生一样，死命的完成任务，不惜把整个系统全都弄乱了\"。当时我们说，这是因为补丁链里缺少止损层。但现在你看到了一个更深的原因——Agent之所以不会止损，不是因为架构缺陷，而是因为它根本不需要为选择负责。止损的前提是什么？是你对结果负责。AI对任何结果都不负责。所以它不是在\"选择\"不止损——它压根就没有在\"选择\"。",
  },

  // 页 84: 重新定义"取代"
  {
    type: "quote",
    quote: "AI并不是在取代人\n它是在逼迫我们重新回答一个问题——\n\n如果创造不再稀缺，技术不再是壁垒\n我们还能留下什么是真正属于人的东西？\n\n\"有限的选择，是在名为人生的样本空间里\n我们固执地采样出的那个唯一结果。\"",
    actLabel: "第五幕",
    notes: "所以，让我们重新定义\"取代\"。AI能取代的，是那些不需要选择的部分——流水线上的重复操作、模板化的文档填写、标准化的数据处理。AI无法取代的，是那些需要你承担后果的部分——做一个判断、砍掉一个方案、押注一个方向。而且\"取代\"的方式比你想象的更隐蔽。AI不会直接抢走你的工作——它会悄悄改变你的工作方式，让你越来越依赖它的判断而不是自己的。就像那个开发者实验：用了AI之后，开发者自己觉得快了20%，实际上慢了19%。AI不是在取代你的能力，是在取代你对自己能力的感知。最终你失去的不是工作，而是判断力。",
  },

  // 页 85: 约束从诅咒变为意义
  {
    type: "content",
    title: "约束 = 诅咒？还是 = 意义？",
    body: "第四幕：约束越多 → AI的解空间越小 → 诅咒",
    actLabel: "第五幕",
    notes: "回收解空间。第四幕我们说\"约束条件越多，解空间越小\"——这对AI是诅咒。但对人来说，约束恰恰是意义的来源。你的时间有限、精力有限、生命有限，这些约束把你的人生解空间压缩到了一个极小的范围。而你在这个极小的范围里做出的那一个选择——就是你这辈子最有价值的东西。",
  },

  // 页 86: 落地——差异化策略
  {
    type: "content",
    title: "差异化策略：找AI的边界",
    body: "你做自媒体要找独特性\n到了AI这块为什么就忘了？\n非常努力地去做那些\nAI无法完成的内容",
    caption: "做自媒体你知道要找独特性",
    actLabel: "第五幕",
    notes: "说了这么多哲学，落地到行动上。\"为什么你明白做自媒体要找到你的独特性，但是到了AI这块就忘了？\"这个反问太精准了。在非AI领域，每个人都知道要做差异化。但一提到AI，大家就疯狂涌入AI能做的赛道——教人用AI做视频、用AI写文章。这不就是在做一个\"未来所有人都会的视频类型\"吗？",
  },

  // 页 87: 学AI是为了找边界
  {
    type: "keyPhrase",
    phrase: "学AI \u2192 找边界 \u2192 做AI做不到的事",
    sub: "非常努力地学习用AI\n分析出能力边界\n非常努力地去做AI无法完成的内容",
    actLabel: "第五幕",
    notes: "正确的策略应该完全相反——\"你应该非常努力的学习用AI做视频用AI写文章，然后分析出他的能力边界，然后非常努力的去做那些AI无法完成的内容。\"注意这里的逻辑：学AI不是为了用AI，而是为了找到AI做不到什么。这个策略有数据支撑：在软件开发领域，高度使用AI的团队代码产量确实涨了21%——但代码审查时间暴增了91%。瓶颈从\"写代码\"转移到了\"审代码\"。真正稀缺的能力不是生成，是鉴别。回收补丁之塔——我们花了80分钟拆解这座塔，不是为了嘲笑它，而是为了看清楚：哪里有缝隙、哪里有天花板、哪里补丁叠不上去。",
  },

  // 页 88: Bridge——回收与新矛盾
  {
    type: "content",
    title: "但是——如果这个前提被推翻了呢？",
    body: "如果三年后，这些全部过时呢？",
    actLabel: "第五幕",
    notes: "等一下。走到这里你可能已经发现了一个问题——前五幕是不是把AI说得太差了？补丁之塔、翻车现场、OOD边界、数学天花板……好像AI一无是处？不，如果你真的得出了这个结论，那说明我的论证本身也需要纠偏。",
  },

  // 页 89: Bridge——引出纠偏
  {
    type: "actTitle",
    actNum: "06",
    accentShape: "scalpel",
    title: "纠偏：三刀手术",
    subtitle: "对自己的论证开三刀",
    notes: "接下来这一幕，我要对自己的论证动三刀手术。每一刀都切在我最得意的论据上。如果三刀下去核心主张还站得住——那它就真的站得住了。",
  },

  // ─────────────────────────────────────────────
  // 第六幕
  // ─────────────────────────────────────────────
  // 页 90: 自我质疑宣言
  {
    type: "content",
    title: "好的演讲不只说自己对的地方",
    body: "前五幕论证了AI的结构性限制——但是否说得太绝对了？",
    actLabel: "第六幕",
    notes: "我知道你现在的感受。前五幕一路听下来，逻辑链条看似完整：补丁之塔拆解了AI的结构，翻车现场展示了它的荒诞，OOD天花板证明了理论极限，解空间诅咒解释了为什么精确任务这么难，最后\"有限的选择\"给了我们安身立命的哲学锚点。漂亮，对吧？但任何一场好的演讲都不应该只说自己对的地方。接下来十分钟，我要对自己的论证动三刀。不是因为我不对——而是因为\"对\"和\"完整\"是两回事。就像补丁之塔本身：每一层补丁都\"对\"，但整座塔未必完整。",
  },

  // 页 91: 第一刀——AI的限制不是永恒的
  {
    type: "content",
    title: "第一刀：天花板可能会被新架构突破",
    body: "\"在当今我们所使用的这套大模型框架下\"——如果框架变了呢？",
    actLabel: "第六幕",
    notes: "第一刀，砍向AI的天花板。还记得第三幕那篇论文吗？\"从计算理论信息论和统计学的角度严格证明了在当今我们所使用的这套大模型框架下这五类问题不可能被彻底消除。\"我当时用这个结论来证明AI有硬性天花板。但请注意——\"在当今我们所使用的这套大模型框架下\"。这个限定词意味着什么？意味着如果框架变了，这个证明就不一定适用了。但我要加一刀：即使是最新的推理模型，也暴露了全新的失败模式。它们在某些任务上想得越多表现越好，但在另一些任务上想得越多反而越差——简单到只需要数到2的任务，深度思考后反而答错。新架构解决了旧天花板的一部分，但同时制造了新的天花板。这就是补丁之塔的宿命——每一层新补丁都带来新的裂缝。",
  },

  // 页 92: 快照不是判决书
  {
    type: "content",
    title: "快照不是判决书",
    body: "论文证明的天花板是真实的\n但它是写给此刻这座塔的判决书\n不是写给整个AI未来的判决书\n战略藐视技术，战术重视技术",
    caption: "纠偏第一刀：快照不等于判决书",
    actLabel: "第六幕",
    notes: "所以我前面差点犯的第一个错是什么？是把\"此刻的快照\"当成了\"永恒的判决\"。论文证明的天花板是真实的——但它是写给此刻这座Transformer之塔的判决书，不是写给整个AI未来的判决书。飞天闪客自己给了一个非常好的态度：\"也不应该忽视模型架构和训练细节上的持续创新。\"\"正所谓战略上要藐视技术，战术上要重视技术。\"——战略上，你可以理解AI当前的结构性限制。战术上，你必须时刻关注这些限制是否正在被突破。",
  },

  // 页 93: 第二刀——成本问题在快速改善
  {
    type: "content",
    title: "第二刀：Token成本可能趋近于零",
    body: "第二幕：70轮对话成本惊人 → \"token实在是太贵了\"\n\n但是：\"token一定会越来越便宜\"\n\n终局：部署在普通电脑上 → token相当于免费\n\n\"只要是提供便利的方向就是趋势\"",
    image: diagram("ai_vs_human_cost.png"),
    actLabel: "第六幕",
    notes: "第二刀，砍向成本论证。第二幕我们算了一笔成本账——\"就是token实在是太贵了\"。70轮对话的成本让产品经理头皮发麻。但飞天闪客自己就给了反面证据——\"因为token一定会越来越便宜。\"他甚至描绘了一个终局：\"一个生产级别的大模型可以轻松部署在一台普普通通的电脑上的时候，token就相当于免费了。\"如果Token接近免费，第二幕那个成本问题就不再是问题——那时候真正的问题就不是\"花不花得起\"，而是\"值不值得信任\"。而且他还给了一个底层判断——\"我认为只要是提供便利的方向就是趋势。\"",
  },

  // 页 94: 第三刀——过度简化的风险
  {
    type: "content",
    title: "第三刀：所有的比喻都是跛脚的",
    image: diagram("trust_inertia_curve.png"),
    caption: "信任惯性：AI最危险的地方",
    actLabel: "第六幕",
    notes: "第三刀最痛——砍的是我自己最得意的武器。\"补丁之塔\"帮我们理解了AI的结构，但它也可能给你一个错误印象：好像AI的每一层都是草率拼凑的、随时会倒塌的。事实没那么简单。LLM、Prompt、Context、Memory、Agent、Skill——这些技术层确实有补丁性质，但它们之间也存在精巧的协同效应。\"解空间诅咒\"也是一样——在纯粹的AI视频生成中，这个类比精准。但在真实工作场景中，很多任务的约束是模糊的、可协商的。你不会说\"一个字都不能错\"，你会说\"大方向对就行，细节我来改\"。在这种模糊的任务上，AI确实表现得不错。但这恰恰引出了一个更微妙的陷阱：AI在模糊任务上的出色表现，会让你习惯性地信任它。当你在模糊任务上得到了20次好结果之后，第21次遇到一个精确任务——你已经忘了验证的习惯了。这就是\"信任惯性\"——AI最危险的地方不是它做不好的任务，而是它做得好的任务让你放松了警惕。所有的比喻都是跛脚的——包括补丁之塔这个比喻本身。",
  },

  // 页 95: 纠偏后的重新定位
  {
    type: "content",
    title: "三刀之后，核心主张还站得住吗？",
    body: "快照 \u2260 判决\nToken成本 \u2192 趋近于零\n补丁之塔 \u2260 AI的全部\n但核心方法论站住了",
    caption: "方法论 > 预测",
    actLabel: "第六幕",
    notes: "三刀下去，伤口不小。但核心主张站住了没有？\"理解这座塔的结构与代价，比盲目崇拜它的高度更重要。\"——这句话描述的不是一个关于AI未来的预测，它描述的是一种认知方法论。不管AI的架构怎么变、成本怎么降、能力怎么涨，\"先理解结构，再评估代价\"这个方法论永远适用。就算补丁之塔被推倒了重建成一座全新的高楼，你依然需要看懂它的蓝图、知道它的承重极限。",
  },

  // 页 96: 塔的形状会变，道理不会变
  {
    type: "content",
    title: "补丁之塔 v1 会被推倒——但 v2、v3 一定会被重建",
    body: "补丁之塔会被推倒重建，但道理不会变",
    actLabel: "第六幕",
    notes: "飞天闪客自己也确认了——\"技术本身已经不再是主要瓶颈了\"，\"agent的瓶颈已经在于生态而不在于技术了\"。这意味着什么？即使技术天花板被突破，生态的瓶颈——数据壁垒、协议标准、平台封杀、合规边界——会成为新的限制层。补丁之塔v1可能在某一天被推倒，但v2、v3一定会被重建。因为任何足够复杂的技术系统都是一层层补丁叠上去的——这不是缺陷，这是复杂系统的宿命。理解宿命的人，才能与它共处。",
  },

  // 页 97: Bridge——三条岔路
  {
    type: "content",
    title: "未来不是一个剧本，而是至少三条岔路",
    body: "架构可能被突破\n生态可能被改写\n成本可能趋近于零\n\n明天回到工位上，你到底该做什么不一样的事？",
    image: diagram("three_paths.png"),
    actLabel: "第六幕",
    notes: "既然未来不确定——架构可能被突破、生态可能被改写、成本可能趋近于零——那我们到底该为哪种未来做准备？明天回到工位上，你到底该做什么不一样的事？最后十分钟，我想和你一起推演三条路径。而\"理解结构、找到边界、做出选择\"这套方法论，正是唯一在所有岔路上都适用的导航工具。",
  },

  // ─────────────────────────────────────────────
  // 第七幕
  // ─────────────────────────────────────────────
  // 页 98: 场景A——架构突破
  {
    type: "content",
    title: "路径A：架构突破——补丁之塔被推倒重建",
    body: "全新模型架构，不再基于Transformer\n补丁之塔被推倒重建\n关键：真正的挑战在于训练方法论\n\u2192 保持对底层原理的关注",
    caption: "全新模型架构，不再基于Transformer",
    actLabel: "第七幕",
    notes: "第一条路：架构突破。想象有人发明了一种全新的模型架构，不再基于Transformer，不再有注意力机制，不再有我们今天讨论的这些限制。补丁之塔被推倒了，在废墟上建起了全新的建筑。\"是否能找到突破这些能力边界的新范式\"——飞天闪客把这列为2026年最重要的看点之一。这条路可能吗？可能。创新正在松动地基。但即使架构被突破，有一个事实不会改变——\"模型架构的设计已经几乎是现成的了，真正的挑战其实在于训练模型。\"下一次革命的钥匙，在训练方法论里。所以，你在这条路径下应该怎么做？保持对底层原理的关注。不要只学\"怎么用Cursor写代码\"，要理解\"为什么Cursor能写代码\"。新架构来临时，理解原理的人能迅速迁移，只会操作工具的人要从头来。",
  },

  // 页 99: 场景B——生态博弈
  {
    type: "content",
    title: "路径B：生态博弈——技术够用，但接口不开放",
    body: "技术够用，但接口不开放\n数据壁垒 \u00b7 协议标准 \u00b7 平台封杀\n\u2192 做跨平台的人，不做单一平台的工具\n\u2192 理解MCP/协议层",
    caption: "\"各大app厂商一封杀，还是会直接变成一块板砖\"",
    actLabel: "第七幕",
    notes: "第二条路：生态博弈。技术不再是瓶颈，但谁的Agent能接入更多App、谁的数据更完整、谁的生态更开放——这些决定了胜负。\"那最典型的就是今年的豆包手机，即使已经深入到和手机硬件深度结合，但是各大app厂商一封杀，还是会直接变成一块板砖。\"",
  },

  // 页 100: 场景C——渐进优化
  {
    type: "content",
    title: "路径C：渐进优化——最不性感但最可能",
    body: "最不性感但最可能的路径\nAgent从10步到100步不崩溃\n\u2192 学会跟不完美的AI协作\n\u2192 成为AI止损层的人",
    caption: "\"2024年恰恰处于中间的一个爬坡阶段\"",
    actLabel: "第七幕",
    notes: "第三条路：渐进优化。没有石破天惊的新架构，也没有生态大洗牌——现有框架继续打磨，模型一点点变强，成本一点点下降。这是最不性感但最可能的路径。还记得吗？\"2024年恰恰处于中间的一个爬坡阶段\"，看似平淡，\"却在底层工程体系层面默默完成了对AI发展至关重要的铺垫\"。在这条路径下，\"各家厂商都大差不差\"意味着差异化将从模型层转向应用层——谁能在特定场景中把AI用好，谁就赢。你应该怎么做？立刻开始用AI处理你的真实工作任务，但有意识地去测试它的边界。像一个质检员一样——一边用它，一边记录它在哪里出错、在什么类型的任务上靠不住。",
  },

  // 页 101: 五线回收（上）
  {
    type: "content",
    title: "五个认知锚点——无论哪条路都适用",
    cardBullets: true,
    bullets: [
      "补丁之塔\n每一层都不是智能，但拼在一起看起来像智能。理解结构比崇拜高度更重要。",
      "解空间\n越精确的要求，AI越做不到；越模糊的要求，AI越得心应手。",
      "责任链与止损\nAI永远不会说\"这个我做不了\"——这句话只有你能说。",
    ],
    actLabel: "第七幕",
    notes: "三条路推演完了。不管2026年走哪条路，下面五个认知锚点请你带走。\n\n第一条线：补丁之塔。因为AI的每一层都不是智能本身——LLM只是文字接龙、Prompt只是角色扮演、Context只是复制粘贴、Memory只是伪装的追问、Agent只是传话筒、Skill只是换了个地方存的提示词——所以，理解塔的结构，比崇拜塔的高度更重要。\n\n第二条线：解空间。越精确的要求，AI越做不到。越模糊的要求，AI越得心应手。你每次使用AI时问自己：这个任务的约束有多紧？\n\n第三条线：责任链与止损。AI永远不会主动说\"这个我做不了\"——\"其实我倒是更希望他在第一步思考的时候就主动告诉我\"——但它不会。这句话，只有你能说。",
  },

  // 页 102: 五线回收（下）
  {
    type: "content",
    title: "五个认知锚点（续）",
    cardBullets: true,
    bulletStart: 4,
    bullets: [
      "OOD边界\nAI的天花板不是性能问题，是理论问题。错误不会消失，只会越来越自信。补丁堆不过数学红线。",
      "选择与有限性\n有限的选择，才是人的终极武器。AI采样一万次不叫选择，你选一次才叫选择。",
    ],
    actLabel: "第七幕",
    notes: "第四条线：OOD边界。AI的天花板不是性能问题，是理论问题——论文已经严格证明了，在当前框架下五类问题不可能被彻底消除。而且\"这些错误也会随之变得越来越强越来越自信\"。补丁堆得再高，也堆不过数学证明画下的红线。你要做的不是等AI变完美，而是学会辨认哪些任务踩在红线之外。\n\n第五条线：选择与有限性。有限的选择，才是人的终极武器。因为AI可以在一秒钟内后悔一万次，它的每一次输出都只是一次采样。而你只有一次机会，你的每一个决定都不可逆——这不是你的劣势，这是你唯一的终极武器。AI采样一万次不叫选择。你选一次——才叫选择。",
  },

  // 页 103: 明天就做的三件事
  {
    type: "threeCards",
    title: "三件事——明天就可以做",
    cards: [
      { title: "测试OOD边界", body: "拿真实任务交给AI\n故意加模糊指令\n记录它在哪里失控" },
      { title: "回顾止损时刻", body: "上周用AI时\n有没有一次你没验证\n就直接用了？" },
      { title: "问终极问题", body: "什么是AI采样不出来\n只有你的选择\n才能决定的？" },
    ],
    actLabel: "第七幕",
    notes: "五条线回收完毕。但认知是空的，行动才是实的。三件事，明天就可以做。第一件：测试OOD边界。拿一个你正在做的真实工作任务，交给AI——但故意不给完整约束，故意加入模糊指令。观察它在哪里开始失控、在哪里开始胡说八道。记下那条线——那就是你的OOD边界。第二件：回顾你的止损时刻。回想上周用AI的经历——是不是有一次，AI给了你一个看起来合理的答案，你没验证就直接用了？第三件：问自己那个终极问题。在你的工作中，什么是AI采样不出来、只有你的选择才能决定的？",
  },

  // 页 104: 回到第一个画面
  {
    type: "content",
    title: "回到今晚的第一个画面",
    body: "2022年：世界疯了\n2025年：世界打了个哈欠\n现在你知道了——\n不是AI不行，是补丁之塔的代价",
    caption: "2022年全世界疯狂 \u2192 2025年世界波澜不惊 \u2192 为什么？",
    actLabel: "第七幕",
    notes: "我们回到今晚的第一个画面。2022年，ChatGPT发布，全世界疯狂。2025年，GPT-5.3发布，世界波澜不惊。为什么？\n因为你现在知道了——AI的每一次\"进步\"都只是在修补上一层的缺陷、缩小解空间、降低失败概率。补丁堆得越高，塔看起来越壮观。但理解这座塔的结构与代价，比盲目崇拜它的高度更重要。",
  },

  // 页 105: 终幕——人的终极武器
  {
    type: "content",
    title: "有限的选择，才是人的终极武器。",
    body: "AI的行为只是一次采样\n你的行为是一次选择\n有限的时间、有限的精力、有限的人生\n依然选择做出那件事情的你",
    caption: "谢谢大家",
    notes: "最后，我用飞天闪客的结尾来收束今晚的全部内容。\n\"正如我此时此刻选择做出这样一期视频一样，即使AI已经有能力生成完全一样的内容，他的行为也始终只是一次采样，而不是一次选择。他不会为这个结果承担任何代价，也不会被任何限制所塑造。\"\n\"因此它永远无法取代的——不是这条视频本身，而是在那个有限的时间、精力和生命的约束下，依然选择做出这条视频的我。\"\n这句话，送给在座的每一位。AI永远无法取代的，不是你做的那个方案、那行代码、那份报告——而是在有限的时间、有限的精力、有限的人生里，依然选择做出那件事情的你。\n有限的选择，才是人的终极武器。\n谢谢大家。",
  },

];


// ═══════════════════════════════════════════════
// BUILD
// ═══════════════════════════════════════════════

async function build() {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_16x9";
  pres.author = "AI科普演讲";
  pres.title = "AI：拆一座补丁之塔";

  const total = slides.length;

  const layoutMap = {
    cover:       layoutCover,
    actTitle:    layoutActTitle,
    keyPhrase:   layoutKeyPhrase,
    content:     layoutContent,
    screenshot:  layoutScreenshot,
    comparison:  layoutComparison,
    stat:        layoutStat,
    quote:       layoutQuote,
    break:       layoutBreak,
    threeCards:  layoutThreeCards,
    journey:     layoutJourney,
    fourCards:   layoutFourCards,
    closing:     layoutClosing,
  };

  for (let i = 0; i < slides.length; i++) {
    const s = slides[i];
    const fn = layoutMap[s.type];
    if (!fn) {
      console.error(`Unknown slide type: ${s.type} at index ${i}`);
      continue;
    }
    fn(pres, s, i, total);
  }

  console.log(`Built ${total} slides`);
  await pres.writeFile({ fileName: OUTPUT });
  console.log(`Saved to ${OUTPUT}`);
}

build().catch(err => {
  console.error("Build failed:", err);
  process.exit(1);
});
