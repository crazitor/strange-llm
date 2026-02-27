#!/usr/bin/env node
/**
 * patch_v5_systemic.js — 4 systemic improvements:
 * 1. Act 1 timing update (18min→25min, 14→17 slides)
 * 2. Lighten mutedOnDark color for better contrast
 * 3. Increase keyPhrase sub-phrase fontSize 14→16
 * 4. Vertically center body in text-only content slides
 * 5. Reduce threeCards cardH 3.8→3.4
 * 6. Reduce comparison colH 3.8→3.4
 */

const fs = require("fs");
const path = require("path");
const FILE = path.resolve(__dirname, "build_pptx_v4.js");
let src = fs.readFileSync(FILE, "utf8");
let changes = 0;
let errors = 0;

function replace(label, oldStr, newStr) {
  if (!src.includes(oldStr)) {
    console.error("FAIL:", label);
    errors++;
    return;
  }
  src = src.replace(oldStr, newStr);
  changes++;
  console.log("OK:", label);
}

// ================================================================
// 1. Act 1 timing update
// ================================================================
replace(
  "Act 1 comment update",
  // Comment line
  "// 第一幕：拆塔（18分钟，14页）",
  "// 第一幕：拆塔（25分钟，17页）"
);

replace(
  "Act 1 subtitle timing",
  '· 18分钟"',
  '· 25分钟"'
);

// ================================================================
// 2. Lighten mutedOnDark color: A0AAC0 → B8C0D4
// ================================================================
replace(
  "mutedOnDark color lighten",
  'mutedOnDark:  "A0AAC0"',
  'mutedOnDark:  "B8C0D4"'
);

// ================================================================
// 3. Increase keyPhrase sub fontSize: 14 → 16
// ================================================================
replace(
  "keyPhrase sub fontSize",
  "x: pX, y: 3.9, w: pW, h: 0.7,\n      fontSize: 14, fontFace: FONT.body,",
  "x: pX, y: 3.9, w: pW, h: 0.7,\n      fontSize: 16, fontFace: FONT.body,"
);

// ================================================================
// 4. Vertically center body in text-only content slides
// ================================================================
replace(
  "content body valign middle for text-only",
  "slide.addText(bodyContent, {\n      x: 0.6, y: bodyY, w: bodyW, h: bodyH,\n      valign: \"top\", margin: 0,\n    });",
  "const bodyVAlign = (!data.image && !data.bullets) ? \"middle\" : \"top\";\n    slide.addText(bodyContent, {\n      x: 0.6, y: bodyY, w: bodyW, h: bodyH,\n      valign: bodyVAlign, margin: 0,\n    });"
);

// ================================================================
// 5. Reduce threeCards cardH: 3.8 → 3.4
// ================================================================
replace(
  "threeCards cardH reduce",
  "const cardH = 3.8;",
  "const cardH = 3.4;"
);

// ================================================================
// 6. Reduce comparison colH: 3.8 → 3.4
// ================================================================
replace(
  "comparison colH reduce",
  "const colH = 3.8;",
  "const colH = 3.4;"
);

// ================================================================
// Write result
// ================================================================
if (errors > 0) {
  console.error(`\n${errors} operations FAILED. File NOT written.`);
  process.exit(1);
} else {
  fs.writeFileSync(FILE, src, "utf8");
  console.log(`\nDone: ${changes} changes applied successfully.`);
}
