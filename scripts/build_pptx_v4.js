/**
 * build_pptx_v4.js — AI科普演讲 PptxGenJS 构建脚本
 *
 * 运行: node scripts/build_pptx_v4.js
 * 输出: output/presentation_v4.pptx
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
const OUTPUT = path.join(ROOT, "output", "presentation_v4.pptx");

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
    fontSize: 10, fontFace: FONT.body,
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
        fontSize: r.fontSize || data.fontSize || 30,
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
      fontSize: data.fontSize || 30, fontFace: FONT.title,
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
      fontSize: 24, fontFace: FONT.title, color: C.textDark,
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
      options: { fontSize: 16, fontFace: FONT.body, color: C.textDark, lineSpacingMultiple: 1.5 },
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
      slide.addText(String(i + 1), {
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
        fontSize: 15, fontFace: FONT.body, color: C.textDark,
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
      fontSize: 18, fontFace: FONT.title, color: titleColor,
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
      fontSize: 11, fontFace: FONT.body, color: captionColor,
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
  slide.background = { color: C.darkBg };

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
    fontSize: data.fontSize || 22, fontFace: FONT.title,
    color: C.white, italic: true,
    align: "left", valign: "middle", margin: 0,
    lineSpacingMultiple: 1.5,
  });

  // Attribution
  if (data.attribution) {
    slide.addText(data.attribution, {
      x: 1.2, y: 4.4, w: 7.5, h: 0.4,
      fontSize: 13, fontFace: FONT.body, color: C.mutedOnDark,
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
  // 序幕：一个奇怪的现象（5分钟，5页）
  // ─────────────────────────────────────────────
  {
    type: "cover",
    title: "AI：拆一座补丁之塔",
    subtitle: "一个技术从业者的深度解读",
    info: "130分钟 · 七幕结构 · 2025",
    notes: "大家好。今天我想聊聊AI。但不是那种“AI多厉害、赶紧学起来”的焦虑式布道。我想带大家做一件更有意思的事——拆东西。把AI这个庞大的概念拆开来，看看里面到底是什么。",
  },
  {
    type: "comparison",
    title: "一个奇怪的现象",
    leftTitle: "2022年",
    leftBody: "ChatGPT发布\n不能联网、不能识图\n动不动胡说八道\n\n→ 全世界炸了锅",
    leftColor: C.accent2,
    rightTitle: "2025年",
    rightBody: "GPT-5发布\n各项能力强了百倍\n多模态、长上下文\n\n→ 大多数人连新闻都没点开",
    rightColor: C.mutedOnLight,
    actLabel: "序幕",
    notes: "2022年底，ChatGPT发布。一个不能联网、不能识图、动不动胡说八道的程序，让全世界炸了锅。快进到2025年。GPT-5发布了。各项能力比初代强了百倍不止。幻觉减少了45%，但断网时幻觉率仍然高达47%——又一层补丁，修补了上一层的缺陷，但地基没变。结果呢？大多数人连新闻都没点开。",
  },
  {
    type: "keyPhrase",
    richPhrase: [
      { text: "一个很弱的东西让全世界", color: "FFFFFF" },
      { text: "疯了", color: "FF6B35", fontSize: 36 },
      { text: "\n一个很强的东西让全世界打了个", color: "FFFFFF" },
      { text: "哈欠", color: "A0AAC0", fontSize: 36 },
    ],
    sub: "这不是简单的“新鲜感消退”能解释的",
    actLabel: "序幕",
    notes: "你品品这个反差。如果你觉得这很正常——新鲜感过了嘛——那我请你再想深一步。手机每一代iPhone发布，大家虽然不像第一次那么疯狂，至少还是关心的。不会出现“iPhone 20发布了，没人在乎”这种局面。但AI恰恰出现了这种局面。",
  },
  {
    type: "keyPhrase",
    richPhrase: [
      { text: "AI的发展，与其说是\n", color: "FFFFFF" },
      { text: "“智能的进化”", color: "A0AAC0", strike: true },
      { text: "，\n不如说是", color: "FFFFFF" },
      { text: "“补丁的堆叠”", color: "00D4AA" },
    ],
    sub: "这是我今天的核心判断。但这个判断需要你跟我走完第一幕之后，才能真正理解为什么。",
    fontSize: 28,
    actLabel: "序幕",
    notes: "我先把结论告诉你——但这个结论现在还只是一句话。等第一幕结束的时候，你会理解这句话为什么是对的。等第五幕结束的时候，你会理解这句话为什么重要。",
  },
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
    hint: "130分钟 · 七幕结构 · 中场休息10分钟",
    actLabel: "序幕",
    notes: "接下来两个小时，我们分七幕走完这整个旅程。先拆解这座塔的结构、再看它运转时的翻车、然后找到它理论上的天花板、探讨一个比“AI会不会取代人”更深刻的问题、然后给自己的论证纠偏、最后落到你明天就能做的事。",
  },

  // ─────────────────────────────────────────────
  // 第一幕：拆塔（25分钟，17页）
  // ─────────────────────────────────────────────
  {
    type: "actTitle",
    actNum: "01",
    accentShape: "layers",
    title: "拆塔",
    subtitle: "从文字接龙到概念大爆炸 · 25分钟",
    notes: "我们从最底层开始。各位，请先做一件事：把你脑子里关于AI的所有概念清空。Agent、RAG、MCP、大模型——全部先放下。我们从零开始。",
  },
  {
    type: "keyPhrase",
    richPhrase: [
      { text: "大语言模型到底是什么？\n\n", color: "FFFFFF", fontSize: 30 },
      { text: "文字接龙", color: "FF6B35", fontSize: 44 },
    ],
    fontSize: 36,
    actLabel: "第一幕",
    notes: "大语言模型到底是什么？我能给出的最诚实的回答就三个字：文字接龙。你给它几个字，它猜下一个字。你给它“今天天气”，它输出“真不错”。就这样。一个字一个字地往外蹦。",
  },
  {
    type: "content",
    title: "地基：一台猜字机器",
    body: "你手机键盘上有个联想输入功能——你打一个“你”字，它推荐“好”“呢”“们”。\n\n大语言模型跟这个原理是一样的。区别在于它猜得准了无数倍——准到你觉得它好像真的理解了你在说什么。\n\n但它不理解。它做的事情是统计层面的模式匹配。",
    image: screenshot("video1_t0000_这几个词儿你认识多少.jpg"),
    actLabel: "第一幕",
    notes: "你手机键盘上有个联想输入功能对吧？大语言模型跟这个原理是一样的。区别在于它猜得准了无数倍。但这里有一个非常关键的认知：它不理解。它做的事情是统计层面的模式匹配。",
  },
  {
    type: "threeCards",
    title: "猜字机器的零件",
    cards: [
      { title: "Token（令牌）", body: "AI把文字切成小块\n\u201C我爱北京天安门\u201D ≈ 5个token\n输入要钱，输出也要钱\n\n→ 出租车跳表：每跳一格收一次钱" },
      { title: "Transformer", body: "2017年Google的一篇论文\n所有大模型共用的同一张蓝图\nGPT用它，Claude用它，Llama也用它\n\n→ 不是某个AI产品，是所有AI的建筑图纸" },
      { title: "注意力机制（Attention）", body: "猜字时回头看前面所有字\n判断哪些字和当前预测最相关\n看得越多越准，但也越慢越贵\n\n→ 本质是给每个前文字打\u201C重要性分数\u201D" },
    ],
    actLabel: "第一幕",
    notes: "在讲第一层补丁之前，我想先打开这个猜字机器的引擎盖，让你看看里面有什么零件。\n\n第一个：Token，令牌。AI不认识汉字。它把所有文字切成小块，每一小块叫一个Token。\u201C我爱北京天安门\u201D大约是五个Token。为什么这个重要？因为每个Token都要花钱。输入花钱，输出也花钱。就像出租车跳表。后面第二幕你会看到一个Agent完成一个简单任务，消耗了一万四千多个Token——全是真金白银。\n\n第二个：Transformer。2017年Google的一篇论文提出的架构。所有大模型——GPT、Claude、DeepSeek——底层用的全是这一套。它不是某个产品，是所有产品的建筑图纸。后面我会反复提到这个词，因为整座补丁之塔的地基就是它。\n\n第三个：注意力机制，Attention。Transformer的灵魂。它让AI猜下一个字的时候，能扫视前面所有内容，判断哪些字跟当前最相关。听起来很智能？本质就是给每个字算一个权重，然后加权平均。乘法和加法。",
  },
  {
    type: "content",
    title: "涌现：不可预测的能力",
    body:  "参数从几百万 → 几千亿，能力突然涌现（写诗、编程、推理）\n连设计者自己都没预料到 — 看见了每一个参数，但不知道为什么组合在一起就能写诗",
    actLabel: "第一幕",
    notes: "涌现的意思是：这种能力不是被设计出来的，是在规模堆叠过程中自己冒出来的。物理学有个类比——牛顿的F=ma日常够用，但速度接近光速时涌现出时间膨胀、长度收缩。AI的涌现比物理学多了一层：相对论效应可以用公式精确预测，但AI的涌现不能预测，没有任何公式能告诉你参数从一千亿到两千亿会冒出什么新能力。\n\n研究者能看到模型里的每一个参数——几千亿个数字，全部公开，没有任何隐藏。但看见不等于理解。没有人能解释这些参数为什么组合在一起就能写诗。不是看不见，是看见了也不懂。\n\n这跟正常的工程打补丁有什么区别？正常的软件开发，你理解你的系统，因为系统是你自己设计的。但AI不是你设计的，它是从几万亿个数据里训练出来的。你的补丁可能修好了一个问题，同时制造了另一个你暂时看不到的问题。这就是为什么我不叫它\u201C升级\u201D而叫\u201C补丁\u201D。升级意味着蓝图和确定性，补丁意味着应急和碰运气。",
  },
  {
    type: "comparison",
    title: "训练 vs 推理：教科书 vs 考试",
    leftTitle: "训练（Training）",
    leftBody: "让模型看几万亿字的文本\n调整几千亿个参数\n花费：几千万美元 + 几个月\n\n只做一次\n→ 编教科书",
    leftColor: "00D4AA",
    rightTitle: "推理（Inference）",
    rightBody: "你每次问AI问题时的运行过程\n消耗算力，按Token计费\n每秒处理几十到几百个Token\n\n做无数次\n→ 学生考试",
    rightColor: "FF6B35",
    actLabel: "第一幕",
    notes: "零件看完了，再说两个基本操作：训练和推理。\n\n训练就是教AI学会猜字——给它看几万亿字的文本，调几千亿个参数。花几千万美元，几个月时间，但只做一次。就像编教科书。\n\n推理就是你每次问它问题时的实际运行。每次都在按Token花钱。就像学生考试——教科书编一次，但考试考无数次。后面讲Agent翻车的时候你就会明白，推理成本有多可怕。\n\n顺便说一个叫Temperature的参数——AI的\u201C醉酒旋钮\u201D。调低了它只挑最保险的下一个字，输出像复读机；调高了它会冒险选不常见的字，输出天马行空。\n\n还有一个叫Scaling Law的经验规律：模型越大越准，但收益递减。就像健身，前三个月效果明显，之后每多练一个月的提升越来越小。",
  },
  {
    type: "content",
    title: "第一层补丁：对话、上下文、记忆",
    body: "原始的大模型只能一问一答，每轮对话后失忆。\n\n补丁方案：\n· 对话 → 区分“用户”和“助手”角色\n· 上下文 → 把背景信息塞进输入\n· 记忆 → 把历史聊天记录复制粘贴进去\n\n三块补丁，三个新名词。底层呢？还是那个每五分钟失忆一次的文字接龙程序。",
    image: screenshot("video1_t0205_给这些特殊的善寒文信息起了个新词叫memory.jpg"),
    actLabel: "第一幕",
    notes: "小L本身并没有获得记忆能力。你只是在每次对话前，用一个外部程序把历史记录复制粘贴进去了。是程序在“记忆”，不是小L在记忆。补丁之塔的建筑逻辑从第一天开始就定型了——不是增强智能本身，而是在智能外面包一层程序。",
  },
  {
    type: "content",
    title: "第二层补丁：工具调用",
    body: "大模型不能上网、不能读文件——它只会说话。\n\n解决方案：写好搜索程序，教它按固定格式说\u201C我需要搜索XXX\u201D。程序检测到格式，自动执行。\n\nFunction Calling = 固定格式的约定\nAI像只会打电话的人——不会干活，但知道该打给谁。",
    image: screenshot("video1_t0259_你把上网这部分逻辑写成一段程序.jpg"),
    actLabel: "第一幕",
    notes: "AI本身没有获得任何新能力。所有的“能力”都是程序员预先写好的。AI的唯一作用是——根据你的需求，决定调用哪个程序、传什么参数。它是一个调度器，不是一个执行者。",
  },
  {
    type: "threeCards",
    title: "第三四五层补丁",
    cards: [
      { title: "CoT（思维链）", body: "让AI在回答前先写出推理步骤\n\u201C让我想想…首先…然后…\u201D\n\n→ 假装在思考\n本质是让文字接龙多接几轮" },
      { title: "微调（Fine-tuning）", body: "在训练好的模型上\n用少量特定数据再训练一轮\n\n→ 给通才穿制服\n底子不变，只改表面行为" },
      { title: "RLHF（人类反馈）", body: "雇人给AI的回答打分\n让模型学会产生\u201C高分回答\u201D\n\n→ 训宠物\nAI学会了说\u201C听起来对的话\u201D\n而不是\u201C真的对的话\u201D" },
    ],
    actLabel: "第一幕",
    notes: "补丁还没堆完。在Agent出现之前，已经有了第三层、第四层、第五层。我快速过一遍。\n\n第三层：CoT，思维链。让AI在回答前先写出推理步骤——\u201C让我想想，首先这样，然后那样\u201D。看起来像学会了思考？没有。它只是文字接龙多接了几轮。后面第二幕讲\u201C局部合理全局荒诞\u201D的时候，你就会看到CoT的每一步都合理，串起来却完全疯了。公平地说，CoT确实有效——AI的数学正确率翻了一倍多。但\u201C有用\u201D是有天花板的。\n\n第四层：微调。训练好的模型，用少量医疗数据再训一下，说话就更像医生了。但它没学过医。给通才穿制服——底子不变，只改表面。后面讲到3000多个\u201C不同的模型\u201D，大多数就是同一个模型微调出来的。同一个人换3000套衣服。\n\n第五层：RLHF，人类反馈强化学习。简单说就是训宠物。雇人给回答打分，做得好给奖励。结果？AI学会了产生\u201C听起来好\u201D的回答——注意，不是\u201C真的好\u201D。后面第三幕讲\u201C模型越强错误越像真的\u201D——根源就在这里。RLHF确实让AI更安全更有用，但\u201C听起来好\u201D和\u201C真的好\u201D之间的差距，才是核心问题。",
  },
  {
    type: "keyPhrase",
    richPhrase: [
      { text: "Agent（智能体）\n", color: "FFFFFF" },
      { text: "= ", color: "00D4AA", fontSize: 36 },
      { text: "猜字程序", color: "FF6B35" },
      { text: " + ", color: "00D4AA", fontSize: 36 },
      { text: "一堆外挂程序", color: "00D4AA" },
    ],
    sub: "更准确的名字应该叫“程序协调器”，但这样股价不会涨",
    actLabel: "第一幕",
    notes: "Agent三个字给人的感觉是：具有自主智能的实体。但你刚才已经看到了它的全部构成——一个猜字程序加一堆外挂程序。名字的花哨程度和技术进步的幅度之间存在巨大的落差。这就是名词通胀。",
  },
  {
    type: "screenshot",
    title: "Agent：名词通胀的爆发点",
    image: screenshot("video1_t0435_我们聚焦于agent和大模型的对话过程来看.jpg"),
    caption: "一个被吹上天的“智能体”，核心驱动力是提示词 + 外挂程序",
    actLabel: "第一幕",
    notes: "然后通胀开始加速。RAG——还是往提示词里塞更多文字。MCP——一套接口规范，跟前后端约定API格式没有区别。Skill——把提示词换了个地方存起来。",
  },
  {
    type: "threeCards",
    title: "名词通胀加速",
    cards: [
      { title: "RAG", body: "检索增强生成\n\n把文档切小块，语义搜索找到相关段落，塞进上下文\n\n本质：给提示词塞更多文字" },
      { title: "MCP", body: "模型上下文协议\n\n统一定义Agent和工具之间的通信格式\n\n本质：一套接口规范，跟前后端约定API格式没有区别" },
      { title: "Skill", body: "技能包\n\n把说明文档和脚本打包起来，让Agent按说明干活\n\n本质：把提示词换了个地方存起来" },
    ],
    actLabel: "第一幕",
    notes: "到这里你数数我们拆了多少概念。Token、Transformer、注意力、训练、推理、涌现、上下文、记忆、CoT、微调、RLHF、工具调用、Agent、RAG、MCP、Skill、MoE、Embedding、对齐、幻觉——二十多个。如果你是一个普通用户，看到这二十多个词，你会觉得AI领域浩如烟海。但如果你跟着我的拆解走了一遍，你会发现：这二十多个词描述的底层逻辑，其实只有两件事。",
  },
  {
    type: "threeCards",
    title: "继续拆：底层概念",
    cards: [
      { title: "MoE（混合专家）", body: "把一个大模型拆成多个\u201C专家\u201D\n每次只激活相关的几个\n(DeepSeek用的就是这个)\n\n\u2192 一个公司，不是全能选手" },
      { title: "Embedding（向量）", body: "把文字/图片/声音变成一串数字\n\u201C猫\u201D和\u201C狗\u201D在数字空间里靠近\n\u201C猫\u201D和\u201C经济学\u201D放得远\n\n→ AI的全部\u201C理解\u201D = 在地图上找坐标" },
      { title: "对齐（Alignment）", body: "让AI的行为符合人类价值观\n教它什么该说、什么不该说\n\n→ 问题是：谁的价值观？\n连人类自己都没统一" },
    ],
    actLabel: "第一幕",
    notes: "还有几个底层概念你可能听过。快速过一下。\n\nMoE，混合专家。DeepSeek用的就是这个——不是一个全能选手，而是一群专家轮流上场。你负责数学，你负责代码，你负责写诗。效率高了，但没有一个专家能看到全局。\n\nEmbedding，向量。AI把所有东西变成一串数字——\u201C猫\u201D和\u201C狗\u201D靠在一起，\u201C猫\u201D和\u201C经济学\u201D隔得远。AI的全部\u201C理解\u201D就是在一个数字地图上找坐标。后面第四幕你就会理解为什么这个概念关键。\n\n对齐，Alignment。让AI符合人类价值观。问题是：谁的价值观？这个词听起来很客观，背后是一个无解的哲学问题。",
  },
  {
    type: "keyPhrase",
    richPhrase: [
      { text: "幻觉", color: "FF6B35", fontSize: 40 },
      { text: " Hallucination\n\n", color: "FF6B35", fontSize: 20 },
      { text: "一本正经地编造\n", color: "FFFFFF", fontSize: 28 },
      { text: "因为文字接龙没有", color: "A0AAC0", fontSize: 22 },
      { text: "\u201C我不知道\u201D", color: "FF6B35", fontSize: 22 },
      { text: "这个机制", color: "A0AAC0", fontSize: 22 },
    ],
    actLabel: "第一幕",
    notes: "最后一个你一定听过的词：幻觉。AI一本正经地胡说八道。为什么？因为文字接龙的目标是输出\u201C最可能\u201D的下一个字——不是\u201C最正确\u201D的。它的核心驱动力里根本没有\u201C正确\u201D这回事。所以它永远不会说\u201C我不知道\u201D——因为\u201C我不知道\u201D几乎从来不是\u201C最可能\u201D的下一个字。这不是bug，是结构性缺陷。后面第二幕\u201C翻车现场\u201D和第三幕\u201C模型越强错误越像真的\u201D——你就会看到这个\u201C原罪\u201D如何层层放大。",
  },
  {
    type: "comparison",
    title: "统一视角：只有两种操作",
    leftTitle: "塞东西",
    leftBody: "往文字接龙的输入框里塞更多内容\n\n· Context → 塞背景信息\n· Memory → 塞历史记录\n· RAG → 塞搜索到的文档\n· Skill → 塞预设的指令\n· CoT → 塞推理步骤",
    leftColor: C.accent1,
    rightTitle: "跑腿",
    rightBody: "用程序自动执行，减少人亲自沟通的次数\n\n· Function Calling → 替AI执行操作\n· Agent → 让流程自动化\n· MCP → 让工具对接标准化\n· ReAct → 想一步做一步",
    rightColor: C.accent2,
    actLabel: "第一幕",
    notes: "所以Agent到底是什么？Agent是由所有\u201C不需要智能\u201D的部分组成的系统。在Agent系统里，真正需要智能的部分是最底层那个文字接龙在干。而Agent这个\u201C壳\u201D做的所有事情——全都是固定逻辑的程序。所谓智能体，其实是一个不生产智能的智能搬运工。我们刚才做的这个化简，本身就是一个很好的例子。二十多个词让你觉得复杂无比、无从下手，但应用层的操作只有\u201C塞东西\u201D和\u201C跑腿\u201D两件事，地基层也只有一个Transformer。AI领域的名词通胀本质上就是在本来很小的解空间上制造出一种虚假的广阔感。二十多个名字占据了二十多个格子，但格子背后只有两扇门。",
  },
  {
    type: "stat",
    stat: "3000+",
    label: "所谓“开源大模型”",
    desc: "去掉不同量化版本、微调版本、尺寸版本后\n几乎全部追溯到同一个基础架构\n\n3000个名字，一块砖",
    actLabel: "第一幕",
    notes: "现在市面上有3000多个所谓“开源大模型”。去重之后会发现，几乎全部追溯到同一个基础架构。名词的多样性是假象，架构的趋同才是事实。连“开源”这个词本身都被重新定义了。",
  },
  {
    type: "keyPhrase",
    phrase: "底层是文字接龙\n上面堆了二十多个名词\n全部是用程序绕过它的局限\n然后起一个花哨的新名字",
    fontSize: 26,
    actLabel: "第一幕",
    notes: "第一幕到此为止。我们拆了多少个概念？Token、Transformer、注意力机制、训练、推理、Temperature、Scaling Law、涌现、上下文、记忆、工具调用、CoT、微调、RLHF、Agent、RAG、MCP、Skill、MoE、Embedding、对齐、幻觉——二十多个。但如果你跟着我走了一遍，你会发现：底层就是一个文字接龙程序，加上一堆绕过它局限的补丁程序。这座塔看起来很高、名词很多、技术很新，但蓝图自始至终只有一张，砖头也只有两种。理论上，这座塔设计得不错——每层补丁都解决了一个真实的问题。但理论是一回事，实践是另一回事。如果我们真的让这座塔运转起来，会发生什么？",
  },

  // ─────────────────────────────────────────────
  // 第二幕：翻车现场（12分钟，9页）
  // ─────────────────────────────────────────────
  {
    type: "actTitle",
    actNum: "02",
    accentShape: "warnStripe",
    title: "翻车现场",
    subtitle: "让补丁之塔跑起来 · 12分钟",
    notes: "我看的视频里有一期做了一个很有意思的实验——拿一个当时很火的Agent产品，不看它对外宣传的功能有多酷炫，而是直接打开它的后台，看看引擎盖下面到底是什么。",
  },
  {
    type: "screenshot",
    title: "打开引擎盖",
    image: screenshot("video3_t0115_也是说给大模型的话.jpg"),
    caption: "一个被吹上天的“智能体”，核心驱动力是一篇超级长的说明书",
    actLabel: "第二幕",
    notes: "结果发现了什么呢？一个巨大的文本文件。这个Agent之所以能做各种事——不是因为它有什么高深的智能架构，而是因为后台塞了一大堆用自然语言写的指令。甚至连读文件这些系统操作，也是用大白话写在提示词里的。",
  },
  {
    type: "stat",
    stat: "14,000+",
    label: "一个最简单问题消耗的 Token 数",
    desc: "问“你有多少内存？”→ 一轮对话花费约 ¥0.7\n\n因为那篇超级长的系统提示词，每一轮对话都要完整注入一次\n你还没开口说话，它就已经默默读了几千字的内部说明",
    statSize: 56,
    actLabel: "第二幕",
    notes: "后台日志显示，这一轮对话消耗了一万四千多个token。还记得第一幕说的吗？Token就是AI的计价器，每跳一格就收钱。为什么这么多？因为那篇超级长的系统提示词，每一轮对话都要完整注入一次。一天问二十个问题——十四块钱。一个月四百多。",
  },
  {
    type: "stat",
    stat: "70轮",
    label: "Agent完成一个“10分钟”任务的对话次数",
    desc: "任务：把今天的AI新闻整理成PDF\n人类：5步，10分钟\nAgent：来来回回沟通将近70轮\n\n最终产出的PDF——里面的新闻日期是错的",
    actLabel: "第二幕",
    notes: "人怎么做：打开浏览器→搜索→复制粘贴→导出PDF。五步十分钟。Agent呢？后台日志显示它跟大模型之间来来回回沟通了将近70轮。折腾了一大圈，生成的PDF里面的新闻日期是错的。",
  },
  {
    type: "screenshot",
    title: "70轮对话的崩溃",
    image: screenshot("video3_t0429_以及安装命令各种失败等等等等.jpg"),
    caption: "每一步遇到障碍都不会放弃，而是换一个方向继续冲——安装工具失败→换一种工具→又失败→再换",
    actLabel: "第二幕",
    notes: "搜索新闻→遇到格式问题→换一种搜索方式→又遇到问题→再换。尝试转PDF→发现缺少工具→自己安装工具→安装失败→换一种工具→又失败。每一步遇到障碍都不会放弃，而是换一个方向继续冲。【业务举例】做安全自动化的同事应该很有共鸣——我们的SOAR剧本遇到意外情况时，也会不断重试，就是不知道该升级给人处理。同一个模式。",
  },
  {
    type: "keyPhrase",
    richPhrase: [
      { text: "局部", color: "FFFFFF", fontSize: 36 },
      { text: "合理", color: "00D4AA", fontSize: 36 },
      { text: "，全局", color: "FFFFFF", fontSize: 36 },
      { text: "荒诞", color: "FF6B35", fontSize: 36 },
    ],
    sub: "每一步推理都是合理的，但把所有步骤串起来看，结果是纯粹的疯狂",
    fontSize: 36,
    actLabel: "第二幕",
    notes: "每一步的因果关系都成立。但把所有步骤串起来看，结果是纯粹的疯狂。Agent在每一轮沟通中做的决策都是“合理”的，但它不会在第三轮的时候停下来想想：我是不是应该换一种完全不同的方法？“局部合理，全局荒诞”这种现象其实不是AI独有的。官僚体系也是这样运作的。但AI和官僚体系有一个关键区别：官僚体系是慢的，你有时间在中间喊停。AI把这个过程压缩到了70秒，快到你根本来不及介入。AI做的不是创造新的荒诞——它是把本来需要三个月才暴露的荒诞，在三秒钟之内展现给你看。\n\n还记得第一幕讲的CoT吗？它让AI“假装思考”——每一步推理都合理，但它永远不会停下来问“我的方向对吗”。这就是“假装思考”的代价。",
  },
  {
    type: "content",
    title: "老板问你几号：Agent 的真实逻辑",
    body:  [
      { text: "正常人：", options: { fontSize: 16, fontFace: "PingFang SC", color: "00D4AA", bold: true, lineSpacingMultiple: 1.5 } },
      { text: "看手机 → 回答。一秒钟。\n\n", options: { fontSize: 16, fontFace: "PingFang SC", color: "2D2D2D", lineSpacingMultiple: 1.5 } },
      { text: "Agent：", options: { fontSize: 16, fontFace: "PingFang SC", color: "FF6B35", bold: true, lineSpacingMultiple: 1.5 } },
      { text: "手机没电 → 找充电器 → 没有 → 去超市 → 关了 → 打车 → 没法支付 → 去银行 → 余额不足 → 申请贷款…\n\n", options: { fontSize: 14, fontFace: "PingFang SC", color: "2D2D2D", lineSpacingMultiple: 1.4 } },
      { text: "代价：旧手机抵押 + 银行欠贷款。", options: { fontSize: 15, fontFace: "PingFang SC", color: "FF6B35", bold: true, lineSpacingMultiple: 1.5 } },
    ],
    actLabel: "第二幕",
    notes: "假设你老板问你：今天几号？正常人看一眼手机。但如果按照Agent的逻辑运行呢？更重要的是——这个不会止损的系统，是按照它消耗的资源来收费的。它在错误的方向上走得越远，你付出的代价就越大。",
  },
  {
    type: "keyPhrase",
    phrase: "整个补丁链是单向的\n接收 → 执行 → 接收 → 执行\n没有任何一环负责\n“暂停并反思”",
    fontSize: 26,
    actLabel: "第二幕",
    notes: "仔细看补丁之塔的每一层——有没有任何一层的职责是“判断这个任务该不该继续做”？没有。没有任何一层补丁负责止损。而且止损需要的能力恰恰是补丁之塔最底层不具备的——对自身边界的认知。注意这里的逻辑链条：止损需要“我知道我不行”→自我认知→“理解”→但地基就是“不理解”。你要求的止损能力，恰恰需要建立在地基所欠缺的那个东西之上。这不是一层补丁能解决的——这是整个建筑的逻辑悖论。",
  },

  // ─────────────────────────────────────────────
  // 第三幕：割裂感的解剖（18分钟，12页）
  // ─────────────────────────────────────────────
  {
    type: "actTitle",
    actNum: "03",
    accentShape: "crack",
    title: "割裂感的解剖",
    subtitle: "AI为什么让人又爱又恨 · 18分钟",
    notes: "为什么我们总觉得AI忽快忽慢、忽强忽弱？这种割裂感的根源到底是什么？",
  },
  {
    type: "content",
    title: "竹子的比喻：节奏错位",
    body: "竹子前四年几乎看不到地面上的变化。但地下面，根系在疯狂扩展。到了第五年，六周之内蹿高十几米。\n\n观察者的体验：四年无聊——一个月震撼。\n\nAI的发展节奏几乎一模一样。真实进步是连续的、平稳的。但公众只在跨过“感知临界点”时才注意到——AlphaGo、ChatGPT、DeepSeek。",
    image: diagram("bamboo_growth_curve.png"),
    actLabel: "第三幕",
    notes: "AI的发展节奏几乎一模一样。它的真实进步是连续的。但我们只在它跨过某个感知临界点的时候才注意到它。我们的感知系统只对“跨越门槛”做出反应，而忽略了门槛之间所有的平稳积累。",
  },
  {
    type: "content",
    title: "2024：看似停滞的一年",
    body:  [
      { text: "表面：", options: { fontSize: 16, fontFace: "PingFang SC", color: "FF6B35", bold: true, lineSpacingMultiple: 1.6 } },
      { text: "SORA期货、苹果AI没水花 → “AI到头了”\n\n", options: { fontSize: 16, fontFace: "PingFang SC", color: "2D2D2D", lineSpacingMultiple: 1.6 } },
      { text: "实际：", options: { fontSize: 16, fontFace: "PingFang SC", color: "00D4AA", bold: true, lineSpacingMultiple: 1.6 } },
      { text: "推理模型 + 工具标准化 + 开源提升 → 2025年初集中爆发\n\n", options: { fontSize: 16, fontFace: "PingFang SC", color: "2D2D2D", lineSpacingMultiple: 1.6 } },
      { text: "不是AI变慢了，是你的感知和它的节奏不同步。", options: { fontSize: 15, fontFace: "PingFang SC", color: "666666", italic: true, lineSpacingMultiple: 1.6 } },
    ],
    actLabel: "第三幕",
    notes: "2024年就是一个典型案例。AI领域好像什么大事都没发生。但事实恰恰相反。2024年在底层完成了大量关键铺垫，在2025年初集中爆发。",
  },
  {
    type: "threeCards",
    title: "能力倒挂：反直觉的强弱分布",
    cards: [
      { title: "数学", body: "能攻破国际数学竞赛难题\n\n但可能算错 17×38" },
      { title: "视觉", body: "看街景照片就能推理出拍摄地点在哪条街\n\n但可能数不清一只手上有几根手指" },
      { title: "语言", body: "能写出结构完整的万字论文\n\n但可能数不清一段话里有几个字" },
    ],
    actLabel: "第三幕",
    notes: "越“难”的任务，AI做得越好。越“简单”的任务，AI反而做不好。这完全违反我们的常识。在人类世界里，能解高等数学的人不可能不会加法。但AI不是人。",
  },
  {
    type: "keyPhrase",
    richPhrase: [
      { text: "越“难”的任务，AI做得", color: "FFFFFF" },
      { text: "越好", color: "00D4AA" },
      { text: "\n越“简单”的任务，AI反而", color: "FFFFFF" },
      { text: "做不好", color: "FF6B35" },
    ],
    sub: "AI的“难”和“简单”跟我们的标准完全不同",
    actLabel: "第三幕",
    notes: "这完全违反我们的常识。在人类世界里，能解高等数学的人不可能不会加法。但AI不是人——它的“难”和“简单”跟我们的标准完全不同。",
  },
  {
    type: "content",
    title: "OOD：AI的“知识盲区”",
    body: "Out of Distribution\uFF0C\u5206\u5E03\u5916\u95EE\u9898\n\nAI\u7684\u80FD\u529B\u90FD\u6765\u81EA\u8BAD\u7EC3\u6570\u636E\u3002\u8D85\u51FA\u5206\u5E03\u8303\u56F4\u7684\u95EE\u9898\uFF0CAI\u5C31\u53EF\u80FD\u7FFB\u8F66\u3002\n\n\u2192 \u9AD8\u96BE\u5EA6\u6570\u5B66\u9898\uFF1A\u8BAD\u7EC3\u6570\u636E\u4E2D\u6709\u5927\u91CF\u89E3\u9898\u8FC7\u7A0B\n\u2192 \u201C17\u00D738\u201D\uFF1A\u53CD\u800C\u5F88\u5C11\u88AB\u8BE6\u7EC6\u8BA1\u7B97\u8FC7",
    image: diagram("ood_boundary.png"),
    actLabel: "第三幕",
    notes: "AI的所有能力来自训练数据里的统计规律。在训练数据覆盖的范围内，这些规律非常可靠。超出范围，规律就失效了——但AI不知道。高难度数学题的详细解题过程在训练数据里出现过无数次，而\u201C17乘38\u201D的逐步演算反而几乎没有。AI的\u201C难\u201D和\u201C简单\u201D是按训练数据的覆盖密度定义的，不是按你的直觉。",
  },
  {
    type: "keyPhrase",
    phrase: "很多时候不是你不会用AI\n而是你的需求恰好落在了\nAI的OOD区域里",
    actLabel: "第三幕",
    notes: "你身边一定有人跟你说——AI不好用是因为你不会用。现在你可以理解了：很多时候不是你不会用，而是你的需求恰好落在了AI的OOD区域里。你的需求是个性化的、独特的、带有你自己行业和场景特征的。\n\n但人和AI面对OOD的区别在于：人知道自己不知道。你遇到陌生的问题，你会犹豫、会放慢、会说\u201C让我想想\u201D。你的大脑有一套陌生感探测器。AI没有这个探测器。它在熟悉的问题和陌生的问题上用的是同一个置信度、同一种语气。这才是OOD的真正可怕之处——不是AI会犯错，而是它犯错的时候跟正确的时候看起来一模一样。\n\n而且这不纯粹是数据量的问题。就算训练数据扩大十倍，也不可能覆盖所有可能的输入——现实世界是无穷的。有些盲区是结构性的，消不掉。",
  },
  {
    type: "content",
    title: "论文铁证：不可消除的天花板",
    body: "一篇论文从三个完全不同的数学角度证明——在当前Transformer架构下，五类核心问题不可能被彻底消除：\n\n1. 上下文窗口限制\n2. 推理能力的系统性缺陷\n3. 幻觉（编造不存在的事实）\n4. 检索质量瓶颈\n5. 多模态能力的不一致性\n\n不是“暂时解决不了”，而是“不可能被彻底消除”。",
    image: screenshot("video2_t0930_这五类问题不可能被彻底消除.jpg"),
    actLabel: "第三幕",
    notes: "在说论文之前，我先让你自己想一个问题。一个人的底层动力是“说出最可能的话”——注意，不是“最正确的话”，而是“最可能的话”。你怎么训练他说“我不知道”？你没法训练。因为“我不知道”几乎永远不是“最可能的下一句话”。这不是训练量够不够的问题，这是目标函数本身的问题。有一篇论文从三个完全不同的数学角度，严格证明了这个直觉。注意措辞：不是“暂时解决不了”，而是“不可能被彻底消除”。只能局部缓解，不能根治。塔可以一层层往上堆，但它有一个理论极限高度。再多的补丁，也堆不过地基决定的天花板。",
  },
  {
    type: "keyPhrase",
    richPhrase: [
      { text: "模型", color: "FFFFFF" },
      { text: "越强", color: "00D4AA" },
      { text: "\n它的错误就", color: "FFFFFF" },
      { text: "越像真的", color: "FF6B35" },
    ],
    sub: "能力越强，错误越自信——这是AI发展中一个被严重低估的风险",
    actLabel: "第三幕",
    notes: "一个弱模型胡说八道的时候，你一眼就能看出来。但一个强模型胡说八道的时候，它的输出是流畅的、逻辑自洽的、看起来非常专业的。模型越大，你需要越强的判断力才能识别出它的错误。而且你有没有想过——我们正在创造一种什么样的激励机制？当模型说“对不起，我不确定”，用户觉得它弱、换一个更“自信”的模型用。我们在无意间建立了一套奖励“自信”、惩罚“诚实”的激励系统。就像一个行业，如果所有医生都因为说“我不确定”而丢失病人，最后留下来的就是那些最敢拍胸脯说“没问题包治好”的人。还记得第一幕讲的RLHF吗？它教会AI说“听起来对的话”——所以模型越强，RLHF做得越好，编造的谎话就越像真话。又一个“局部合理，全局荒诞”——每一段输出都流畅合理，但整体可能是错的。第二幕的Agent如此，第三幕的能力倒挂也是如此。",
  },
  {
    type: "threeCards",
    title: "割裂感的三层根源",
    cards: [
      { title: "节奏错位", body: "AI的进步是连续的\n你的感知是间断的\n\n你只看到“跨过门槛”的时刻" },
      { title: "OOD问题", body: "AI的强弱分布跟人类直觉完全相反\n\n训练数据分布外就是盲区" },
      { title: "理论天花板", body: "论文证明某些缺陷不可消除\n\n且随能力提升变得更隐蔽" },
    ],
    actLabel: "第三幕",
    notes: "好了。到这里我们拆解了割裂感的三层根源。但我们还缺一个更具象的理解——这些天花板在具体的任务中到底长什么样？",
  },

  // ─────────────────────────────────────────────
  // 中场休息
  // ─────────────────────────────────────────────
  {
    type: "break",
    subtitle: "10 分钟后回来",
    info: "下半场：解空间的诅咒 → 人的终极武器 → 纠偏 → 三条岔路",
    notes: "前半场（序幕+三幕）约60分钟。各位休息十分钟。回来之后我们会用一个统一的概念来解释AI的能力边界，然后讨论一个比“AI取代人”更深刻的哲学问题。",
  },

  // ─────────────────────────────────────────────
  // 第四幕：解空间的诅咒（15分钟，11页）
  // ─────────────────────────────────────────────
  {
    type: "actTitle",
    actNum: "04",
    accentShape: "target",
    title: "解空间的诅咒",
    subtitle: "AI的真正能力边界 · 15分钟",
    notes: "好，休息回来。我们来做一个小实验。",
  },
  {
    type: "screenshot",
    title: "互动：给四个视频排难度",
    image: screenshot("video6_t0000_你觉得这四个AI生成的视频哪个难度最大.jpg"),
    caption: "你觉得哪个对AI来说最难生成？在心里排个序。",
    actLabel: "第四幕",
    notes: "屏幕上有四个AI生成的视频。第一个是太空战舰大战。第二个是有剧情的动画。第三个是精确的口播。第四个是正方形慢慢变成圆形的简单几何动画。你觉得哪个最难？给你15秒。",
  },
  {
    type: "keyPhrase",
    richPhrase: [
      { text: "最难的是", color: "FFFFFF", fontSize: 32 },
      { text: "第四个", color: "FF6B35", fontSize: 38 },
      { text: "\n那个看起来", color: "FFFFFF", fontSize: 32 },
      { text: "最简单的", color: "00D4AA", fontSize: 32 },
      { text: "\n几何动画", color: "FFFFFF", fontSize: 32 },
    ],
    sub: "几乎没有任何AI工具能够成功生成",
    fontSize: 32,
    actLabel: "第四幕",
    notes: "最难的是第四个——那个看起来最简单的几何动画。如果你的排序跟这个答案完全相反——恭喜你，你刚才被自己的直觉欺骗了。",
  },
  {
    type: "content",
    title: "核心概念：解空间",
    body: "想象一个足球场大小的沙滩。\n\n任务：“找一粒沙子”→ 随手抓一把就完成\n加条件：“红色的”→ 解空间缩小\n再加：“直径0.5mm”→ 又缩小\n再加：“表面有三个凹坑”→ 再缩小\n再加：“凹坑呈等腰三角形排列”→ 可能只剩一粒\n\n约束条件越多，合格答案越少，找到答案越难。",
    image: diagram("solution_space.png"),
    actLabel: "第四幕",
    notes: "这就是解空间的核心逻辑：约束条件越多，合格答案越少，找到答案越难。还记得第一幕讲的Embedding吗？每个可能的答案都是一个坐标。解空间就是所有“合格点”的集合。AI生成内容的过程，本质上就是在一个巨大的解空间里寻找合格的点。",
  },
  {
    type: "comparison",
    title: "太空大战 vs 几何动画",
    leftTitle: "太空大战",
    leftBody: "描述留下了巨大的发挥空间\n\n飞船从左边飞来还是右边飞来都可以\n爆炸火焰是橙色还是蓝色都可以\n\n解空间巨大 → 轻松完成",
    leftColor: C.accent1,
    rightTitle: "几何动画",
    rightBody: "每帧几何形状都有精确的数学定义\n\n正方形四边必须等长\n圆形每个点必须等距圆心\n\n解空间接近一个点 → 几乎不可能",
    rightColor: C.accent2,
    actLabel: "第四幕",
    notes: "太空大战为什么简单？因为描述留下了巨大的发挥空间。解空间巨大。几何动画为什么难？因为每一帧都有精确定义。解空间小到接近一个点。",
  },
  {
    type: "keyPhrase",
    richPhrase: [
      { text: "模糊任务是AI的", color: "FFFFFF" },
      { text: "舒适区", color: "00D4AA" },
      { text: "\n精确任务是AI的", color: "FFFFFF" },
      { text: "雷区", color: "FF6B35" },
    ],
    sub: "约束越精确，AI越无力——这就是解空间的诅咒",
    actLabel: "第四幕",
    notes: "为什么AI写散文写得好但写严格格式的报告经常出问题？因为前者解空间巨大，后者解空间极小。为什么AI聊天很流畅但做精确计算经常出错？因为聊天的正确答案有无数种表达方式，而17×38只有一个正确答案。我分享一个自己用的判断方法——每次交给AI之前问自己：这件事，正确答案有几个？【业务举例】就像自动渗透——「扫描这个网段」是宽松任务，AI能做。但「在不触发告警、不影响业务的前提下验证这个漏洞」——约束一多，自动化就力不从心。",
  },
  {
    type: "content",
    title: "实用辨伪技巧：四重约束测试",
    cardBullets: true,
    bullets: [
      "语音按顺序\n从一数到十",
      "嘴型与语音\n完全匹配",
      "手指数量\n与数字一致",
      "三者在时间轴\n上同步",
    ],
    actLabel: "第四幕",
    notes: "四重约束叠加之后，解空间压缩到接近零。目前没有任何AI能够同时满足这四个条件。\n\n有意思的是：第一幕讲的“训练”本身也面临同样的困境。训练器就像厨师调配方——盐多少、火多大、炖多久——每一种组合都是一个可能的配方。训练者在无数种配方里找那个味道最好的，就像在另一个解空间里找答案——同一个数学困境的两个侧面。",
  },
  {
    type: "keyPhrase",
    phrase: "创作者从“指挥者”\n变成了“挑选者”",
    sub: "不是让AI做你想做的事——而是看AI能做什么，把需求修改成它恰好能做的样子",
    actLabel: "第四幕",
    notes: "AI时代，创作流程被反转了。你先让AI随机生成大量结果→从中挑选不错的→修改你原来的想法去匹配AI的输出。你不是在让AI做你想做的事——你是在看AI能做什么之后，把你的需求修改成它恰好能做的样子。",
  },
  {
    type: "content",
    title: "训练者面临同一个诅咒",
    body:  "3000个模型 → 同一个Transformer架构，区分靠训练\n数据配比 × 学习率 × 训练轮数 × 随机种子 → 组合爆炸\n每次试错：数百万资金 + 数月时间",
    actLabel: "第四幕",
    notes: "训练者在无数种配方里找那个“能产出好模型”的配方，和AI在解空间里找那个“有意义”的答案，面临的是同一个数学困境——好的答案少得可怕。",
  },
  {
    type: "comparison",
    title: "两道数学天花板",
    leftTitle: "OOD",
    leftBody: "训练分布之外就是盲区\n\n不管问题对人来说多简单\n\n来源：训练数据的有限性",
    leftColor: C.accent2,
    rightTitle: "解空间",
    rightBody: "约束越精确，AI越无力\n\n不管任务本身多“简单”\n\n来源：随机采样的本质局限",
    rightColor: "6C63FF",
    actLabel: "第四幕",
    notes: "这两道天花板都写在数学里面。不是工程能力不够，不是钱不够，不是数据不够——是底层数学框架决定了上限。",
  },

  // ─── Bridge: 第四幕 → 第五幕 ───
  {
    type: "keyPhrase",
    phrase: "两道天花板\n已经清晰可见",
    sub: "OOD天花板 + 解空间诅咒\n两道都写在数学里——补丁堆不过去\n那我们到底该怎么办？",
    fontSize: 34,
    actLabel: "第四幕",
    notes: "我们刚刚拆解了AI最根本的能力边界——解空间的诅咒。约束越精确，AI越无力。这个诅咒不仅存在于生成端，也存在于训练端。加上第三幕揭示的OOD天花板——AI的两道理论边界已经清晰可见了。两道天花板都是写在数学里的。补丁堆不过去，模型扩大也绕不过去。那面对这些“写死的”限制——我们到底该怎么办？是绝望地接受，还是从中找到属于人类自己的价值？",
  },
  {
    type: "keyPhrase",
    richPhrase: [
      { text: "约束对AI来说是", color: "FFFFFF", fontSize: 30 },
      { text: "诅咒", color: "FF6B35", fontSize: 34 },
      { text: "\n对人来说——是", color: "FFFFFF", fontSize: 30 },
      { text: "意义的来源", color: "00D4AA", fontSize: 34 },
    ],
    fontSize: 30,
    actLabel: "第四幕",
    notes: "到这里我们才意识到——解空间的诅咒不是能不能更聪明的问题，而是能不能更可控的问题。对AI来说，约束是枷锁。但对人来说呢？——有限的生命、有限的精力、有限的选择机会——这些约束恰恰是人之所以为人的根本理由。接下来，我们不再问“AI还能变多强”。我们要问的是：在有限性里，人怎么把选择变成优势？——这就是第五幕的主题。",
  },

  // ─────────────────────────────────────────────
  // 第五幕：有限的选择（15分钟，13页）
  // ─────────────────────────────────────────────
  {
    type: "actTitle",
    actNum: "05",
    accentShape: "fork",
    title: "有限的选择",
    subtitle: "人的终极武器 · 15分钟",
    notes: "到这里，我们花了大概85分钟，把AI从底层拆到了天花板。接下来我要进入一个更深的层面。",
  },
  {
    type: "keyPhrase",
    phrase: "如果创造本身\n只是一种数学操作\n那“创造”这件事\n还有意义吗？",
    fontSize: 30,
    actLabel: "第五幕",
    notes: "大多数关于“AI和人”的讨论都停留在：AI会不会取代人的工作？这个问题当然重要。但还有一个更深层的问题——如果创造本身只是一种数学操作，那“创造”这件事还有意义吗？",
  },
  {
    type: "content",
    title: "像素思想实验",
    body: "一张1920\u00D71080照片，约200万像素，每个像素1600多万种颜色\n\n所有可能的照片有多少张？\n\u2192 1600万的200万次方，比宇宙原子总数还多无数个数量级\n\n但关键是：它是有限的。\n蒙娜丽莎、你的毕业照——都已经\u201C存在\u201D于这个空间里。",
    image: diagram("pixel_possibility_space.png"),
    actLabel: "第五幕",
    notes: "理论上，你可以用一台足够快的计算机把所有可能的图片全部遍历一遍。一切可能的图片都已经“存在”了。创作者做的不是“创造”一张新图片，而是从这个浩瀚的可能性空间中“找到”其中一张。",
  },
  {
    type: "keyPhrase",
    phrase: "你以为你在写书\n其实你只是从一个\n无穷大的图书馆里\n抽出了一本",
    fontSize: 28,
    actLabel: "第五幕",
    notes: "你以为你在写书——其实你只是从一个无穷大的图书馆里抽出了一本。那本书在你写它之前就已经摆在书架上了。但这里我要追问一个问题。两个人到达了同一个像素坐标——一个是达芬奇，花了四年，用他对人体解剖的理解一笔一笔画出蒙娜丽莎；另一个是计算机，随机遍历碰巧命中了同一个像素组合。最终的坐标相同，但通往那个坐标的路径完全不同。达芬奇的路径里包含了理解、选择、取舍和代价。计算机的路径里只有随机和概率。",
  },
  {
    type: "content",
    title: "当创造变成采样",
    body:  "2025年7月，200名游戏开发者被裁。\n取代他们的不是外部AI公司，是他们自己花两年训练的AI工具。\n他们亲手建造了替代自己的机器。\n\n如果创作只是采样，那人和AI的区别只是效率差异\n— 而效率差异不是可持续的竞争优势。",
    actLabel: "第五幕",
    notes: "2025年7月，微软旗下King工作室裁员200人。关卡设计师、文案、UX研究员——他们花了两年喜数据训练AI。然后被AI取代。你有没有想过——你现在教AI做的每一件事，是不是也在训练你自己的替代品？这是比“直升机五分钟到山顶”更可怕的事——你亲手建造了那架直升机。然后再想一层：你花三个月才能到达的坐标点，AI三秒钟就能到。如果创作只是采样，那人和AI的区别只是效率差异。",
  },
  {
    type: "content",
    title: "他不就是采样出的一个样本而已吗？",
    body: "如果画画只是采样——\n那写作呢？编程呢？做产品呢？\n人生中的每一个决定呢？",
    image: screenshot("video2_t1200_他不就是采样出的一个样本而已吗.jpg"),
    actLabel: "第五幕",
    notes: "“如果所有可能的图片都已经在那里了，那创作本身还有意义吗？他不就是采样出的一个样本而已吗？”请注意这两句话的递进——第一句还只是在问图片。但第二句，已经在问创作本身了。如果画画只是采样，那写作呢？编程呢？做产品呢？人生中的每一个决定呢？",
  },
  {
    type: "keyPhrase",
    phrase: "它让人类数千年来追寻的价值\n变得毫无意义",
    sub: "AI取代你的工作？你可以换一份。\n但如果替代你的AI——是你亲手训练的呢？\n你连'换一份'都可能是在给下一个AI喂数据。",
    fontSize: 28,
    actLabel: "第五幕",
    notes: "AI取代你的工作，你可以换一份。但如果替代你的AI——是你亲手训练的呢？就像King那200个人。你连“换一份”都可能是在给下一个AI喂数据。（停顿。）更可怕的是“采样”的逻辑——你做的一切，不管什么工作，都只是可能性空间里的一次随机采样。换什么都是采样。（停顿五秒。）但正是在这个最黑暗的时刻——答案才会显得格外耀眼。",
  },
  {
    type: "keyPhrase",
    bgGradient: true,
    richPhrase: [
      { text: "但正是在这个", color: "FFFFFF", fontSize: 32 },
      { text: "最黑暗的时刻", color: "A0AAC0", fontSize: 32 },
      { text: "\n答案才格外", color: "FFFFFF", fontSize: 32 },
      { text: "清晰", color: "00D4AA", fontSize: 38 },
    ],
    fontSize: 32,
    actLabel: "第五幕",
    notes: "（停顿3-5秒）但正是在这个最黑暗的时刻，答案才格外清晰。问题出在哪里？出在我们把“价值”等同于了“结果”。",
  },
  {
    type: "comparison",
    title: "意义不在于创造了什么，而在于选择了什么",
    leftTitle: "AI的输出",
    leftBody: "每一次都是一次采样\n\n无代价的\n可撤回的\n不需要负责任的\n\n它可以同时做一万件事\n不存在“放弃”这个概念",
    leftColor: C.mutedOnLight,
    rightTitle: "你的决定",
    rightBody: "每一个都是一次选择\n\n有代价的\n不可逆的\n需要承担后果的\n\n你有一百种方式度过时间\n你放弃了九十九种",
    rightColor: C.accent1,
    actLabel: "第五幕",
    notes: "AI有选择吗？没有。AI不存在“放弃”这个概念。它可以同时做一万件事。它不需要承担“我选了A就错过B”的代价。而你的每一个决定都是一次选择——有代价的、不可逆的、需要你用有限的生命去承担的选择。",
  },
  {
    type: "content",
    title: "Agent不会止损的真正原因",
    body: "第二幕：Agent“像个倧强的实习生，死命完成任务”\n当时的解释：补丁链缺少止损层\n\n更深的原因：\n它根本不需要为选择负责\n止损的前提是——你对结果负责\nAI对任何结果都不负责",
    image: screenshot("video3_t0429_以及安装命令各种失败等等等等.jpg"),
    actLabel: "第五幕",
    notes: "这才是今晚最重要的一页。第二幕我们说Agent不止损——当时的解释是架构缺陷。但现在你看到了更深的答案：止损需要你付出代价。代价是什么？是你说“这条路不对，我要停下来重来”时，前面花的时间、精力、信誉全部沉没。AI不需要付这个代价，所以它永远不止损。\n\n这不只是AI的缺陷——这是一个判断框架：凡是需要止损能力的任务，就是AI做不好、你能做好的任务。解空间诅咒告诉你AI什么时候会失灵，止损能力告诉你什么时候该靠自己。",
  },
  {
    type: "keyPhrase",
    richPhrase: [
      { text: "人和AI之间的终极分界线\n", color: "FFFFFF", fontSize: 28 },
      { text: "不是能力", color: "A0AAC0", fontSize: 28 },
      { text: "、", color: "FFFFFF", fontSize: 28 },
      { text: "不是效率", color: "A0AAC0", fontSize: 28 },
      { text: "\n", color: "FFFFFF" },
      { text: "不是创造力", color: "A0AAC0", fontSize: 28 },
      { text: "\n\n是", color: "FFFFFF", fontSize: 28 },
      { text: "代价", color: "FF6B35", fontSize: 40 },
    ],
    fontSize: 28,
    actLabel: "第五幕",
    notes: "AI采样一万次不叫选择。你选一次，才叫选择。止损的前提是你要为结果承担代价——如果一切都没有代价，为什么要止损？约束对AI来说是诅咒，但对人来说是意义。更具体地说：代价的核心表现就是止损——你能说“停，这不对”，AI不能。这个能力的价值，随着AI变强反而在增大。",
  },
  {
    type: "keyPhrase",
    phrase: "理解塔的结构与代价\n然后站在塔够不到的地方",
    fontSize: 30,
    darkBg: false,
    actLabel: "第五幕",
    notes: "正确的思路应该反过来：用AI恰恰是为了找到AI做不到什么。然后把有限的时间和精力投入到那些AI做不好的地方。【业务举例】我们的SOC分析师每天面对上万条告警。自动化能过滤90%，但最后10%——判断这是真实威胁还是误报——需要一个愿意为判断承担后果的人。代价的两种核心形式：时间——你花在这个方案上的三天拿不回来。信誉——你在会议上提了错误建议，专业判断力就贬值了。",
  },

  // ─────────────────────────────────────────────
  // 第六幕：纠偏与深化（10分钟，6页）
  // ─────────────────────────────────────────────
  {
    type: "actTitle",
    actNum: "06",
    accentShape: "scalpel",
    title: "纠偏与深化",
    subtitle: "对自己的论证动三刀 · 10分钟",
    notes: "前四幕建立了一个前提——当前这套架构有不可逾越的天花板。第五幕的核心洞察——止损能力是人的终极武器——不依赖这个前提。但前四幕的具体判断确实是有条件的。如果这个前提被推翻了呢？接下来我要对自己前面的论证动三刀。",
  },
  {
    type: "threeCards",
    title: "三刀手术——对自己的论证动刀",
    cards: [
      { title: "第一刀：天花板", body: "天花板不是永恒的\n\n强化学习 / MoE混合专家\nGPT-5幻觉率12.9%→9.6%\n\n但塔的结构——层层堆叠\n每层解决上层缺陷\n这个模式不会变" },
      { title: "第二刀：成本", body: "成本以超摩尔定律下降\n\nToken价格三年降百倍\n成本论证有保质期\n\n瓶颈从「太贵」变成「太多」\n稀缺的是人的注意力" },
      { title: "第三刀：比喻", body: "所有比喻都是跛脚的\n\nTCP/IP也是层层补丁\n关键不在于是不是补丁\n而在于有没有反馈机制\n\n缺少止损反馈才是问题" },
    ],
    actLabel: "第六幕",
    notes: "第一刀：天花板是对当前Transformer架构的判决，不是终极判决。强化学习、MoE正在突破。但任何新架构仍需堆应用层补丁——工具调用、记忆管理、检索增强都是工程问题。塔的形状会变，结构不会。第二刀：Token成本远超摩尔定律下降，但瓶颈从「用得起吗」转为「验证得过来吗」——人的注意力和判断力成为真正稀缺资源。第三刀：补丁之塔暗示脆弱，但TCP/IP也是补丁堆。关键不在于是不是补丁，在于补丁之间是否有反馈机制。当前AI最大问题是补丁之间缺少止损反馈。",
  },
  {
    type: "keyPhrase",
    richPhrase: [
      { text: "塔的形状会变", color: "B8C0D4", fontSize: 28 },
      { text: "\n塔的结构不会", color: "FFFFFF", fontSize: 36 },
      { text: "\n\n瓶颈从「太贵」变成「太多」", color: "FF8A80", fontSize: 26 },
      { text: "\n你的判断力反而更值钱了", color: "FFB0A0", fontSize: 24 },
    ],
    fontSize: 28,
    actLabel: "第六幕",
    notes: "三刀的综合结论：天花板可能移动，但补丁堆叠模式不变。成本下降不消灭问题，只转移瓶颈——从钱到注意力。比喻有边界，但核心洞察（缺少反馈机制）依然成立。",
  },
  {
    type: "comparison",
    title: "瓶颈转移：从「太贵」到「太多」",
    leftTitle: "旧瓶颈：成本",
    leftBody: "Token价格高昂\n70轮对话浪费钱\n用不用得起AI？\n\n成本是筛选机制\n用不起 = 不用",
    leftColor: C.mutedOnLight,
    rightTitle: "新瓶颈：注意力",
    rightBody: "Token几乎免费\nAI输出海量\n验证得过来吗？\n\n判断力是新筛选机制\n你能识别哪个靠谱",
    rightColor: ACT_THEME.act06.accent,
    actLabel: "第六幕",
    notes: "当Token成本趋近于零，第二幕论证被削弱——70轮对话不再是浪费钱的问题。但瓶颈转移：从「用得起吗」变成「验证得过来吗」。真正稀缺的资源变成人的注意力和判断力。【业务举例】漏洞扫描曾经很贵，现在几乎免费了。问题从「扫不扫得起」变成了「扫出来几千条结果谁来判断哪些是真的」。瓶颈转移，就发生在我们身边。",
  },
  {
    type: "keyPhrase",
    richPhrase: [
      { text: "自我质疑需要代价", color: "FFFFFF", fontSize: 30 },
      { text: "\nAI不会这么做", color: "FF8A80", fontSize: 36 },
    ],
    sub: "AI在用自己的输出训练自己——这不是在建更高的塔，是在让地基变软",
    fontSize: 30,
    actLabel: "第六幕",
    notes: "数据污染闭环：训练数据中AI生成内容比例急剧上升，递归训练导致model collapse——输出多样性坍缩。我选择对自己的论证动刀，是因为AI不会这么做——自我质疑需要付出代价。【业务举例】其实我们做SOAR就是在干这件事——在自动化的各个环节之间建反馈回路。什么时候自动处置，什么时候升级给人。这个决策边界本身，才是产品的核心价值。",
  },

  // ─────────────────────────────────────────────
  // 第七幕：三条岔路与最终选择（8分钟，7页）
  // ─────────────────────────────────────────────
  {
    type: "actTitle",
    actNum: "07",
    accentShape: "trident",
    title: "三条岔路与最终选择",
    subtitle: "从理解到行动 · 8分钟",
    notes: "三刀下去，核心主张还站得住。接下来：AI可能走三条路，无论哪条你需要的应对都是同一个。然后是四个带走——把今晚的理解变成明天就能用的东西。",
  },
  {
    type: "threeCards",
    title: "三种可能的未来",
    cards: [
      { title: "架构突破", body: "推倒补丁之塔，建一座新塔\n强化学习 / MoE / 混合专家\n\n新架构不消灭补丁\n只重新洗牌补丁排列\n理解原理的人能快速适应\n只会按按钮的得从头学" },
      { title: "生态博弈", body: "决定因素不是模型强度\n而是数据/接口/法规\n\n客户不会因为模型强\n就把数据交给你\n信任才是真正的门槛" },
      { title: "渐进优化（最可能）", body: "补丁继续堆，成本继续降\n\n你的应对：\n像质检员一样使用AI\n边用边记录出错场景\n这份「边界地图」\n才是你的核心竞争力" },
    ],
    actLabel: "第七幕",
    notes: "三条路指向同一个能力：不是「使用AI的技巧」，而是「理解AI的边界在哪里、在怎样移动」的能力。技巧会过时，理解不会。路径B用自家业务举例：客户不会仅仅因为模型厉害就把安全数据交给你，信任、合规、集成成本才是真正的壁垒。",
  },
  {
    type: "fourCards",
    title: "无论哪条路，请带走这些",
    cards: [
      { title: "理解结构", body: "AI不是魔法\n每一层能力都有\n具体来源和限制\n\n比崇拜或恐惧更有价值" },
      { title: "识别边界", body: "模糊创意 = AI舒适区\n精确规则 = AI雷区\n\n用AI前花几秒想想：\n这个任务约束有多紧？" },
      { title: "承担止损", body: "AI永远不会主动说\n「这个我做不了」\n\n这个判断只有你能做\n你是唯一能说「停」的人" },
      { title: "找到位置", body: "不要跟AI比效率\n那是必输的竞赛\n\n去找那些需要你选择\n承担后果的事情" },
    ],
    actLabel: "第七幕",
    notes: "四个带走：1.理解结构——AI不是魔法，每一层能力都有具体来源和限制。2.识别边界——模糊创意是AI舒适区，精确规则是雷区。3.承担止损——AI不会说「我做不了」，只有你能做这个判断。【业务举例】这其实就是我们公司在做的事。SOAR的价值不是让一切自动化，是知道什么时候该停下来让人接手。我们比大多数人更早理解了这个问题。4.找到你的位置——不跟AI比效率，去找需要选择、承担后果的事情。",
  },
  {
    type: "content",
    title: "回到第一个画面",
    body: [
      { text: "2022年，ChatGPT发布\n全世界疯了——因为我们以为补丁之塔真的在「进化」\n\n2025年，GPT-5发布\n世界波澜不惊——人们隐约感觉到了这座塔的结构\n\n", options: { fontSize: 16, fontFace: "PingFang SC", color: C.textDark, lineSpacingMultiple: 1.5 } },
      { text: "这两个小时，我们做了四件事：\n拆了塔的结构、看了它运转时的荒诞\n找到了它数学上的天花板\n然后讨论了在这些限制面前人到底还剩下什么", options: { fontSize: 15, fontFace: "PingFang SC", color: C.mutedOnLight, lineSpacingMultiple: 1.5 } },
    ],
    actLabel: "第七幕",
    notes: "首尾呼应——回到序幕的「奇怪的现象」。2022年ChatGPT发布，震撼来自不理解。2025年GPT-5发布，平静来自以为理解了。今晚你应该带走的不是冷漠，而是清醒。GPT-5幻觉减少了45%——又一层补丁。但你知道了，补丁堆不过地基。你也知道了，什么时候该用它、什么时候该靠自己——解空间大的交给AI，需要止损的留给自己。",
  },
  {
    type: "quote",
    quote: "它永远无法取代的\n不是你做的那个方案、那行代码、那份报告本身\n\n而是在有限的时间、有限的精力、有限的人生里\n依然选择做出那件事情的你",
    fontSize: 20,
    actLabel: "第七幕",
    notes: "原作者引用。「理解」和「代价」是同一枚硬币的正反面。为什么要理解补丁之塔的结构？因为理解是有代价的——你要花时间、花脑力、忍受「发现真相没有想象中美好」的不适。AI不需要付出这些代价，所以它不理解任何东西。它只是在猜下一个字。没有理解就没有真正的选择，没有代价就没有真正的理解。",
  },
  {
    type: "keyPhrase",
    centered: true,
    richPhrase: [
      { text: "有限的选择", color: "00D4AA", fontSize: 38 },
      { text: "\n才是人的终极武器", color: "FFFFFF", fontSize: 34 },
    ],
    fontSize: 34,
    actLabel: "第七幕",
    notes: "终幕金句。有限的选择，才是人的终极武器。谢谢大家。",
  },
  {
    type: "closing",
    title: "谢谢大家",
    subtitle: "Q&A · 10分钟",
    info: "AI：拆一座补丁之塔",
    notes: "（Q&A 10分钟）",
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
