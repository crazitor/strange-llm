#!/usr/bin/env node
/**
 * patch_v6_fixes.js — Fix 3 critical visual QA issues from v6 narrative patch
 *
 * 1. Slide 53: richPhrase "\n是" puts "是" alone on a line → merge with preceding text
 * 2. Slide 59: title too long for 5" box (image present) → remove outer quotes
 * 3. Slide 74: card 1 body text overflows card → shorten
 */

const fs = require("fs");
const path = require("path");
const FILE = path.resolve(__dirname, "build_pptx_v4.js");
let src = fs.readFileSync(FILE, "utf8");
let changes = 0;
let errors = 0;

function replace(label, oldStr, newStr) {
  if (!src.includes(oldStr)) {
    console.error("FAIL:", label, "- string not found");
    errors++;
    return;
  }
  src = src.replace(oldStr, newStr);
  changes++;
  console.log("OK:", label);
}

// 1. Slide 53: Remove the \n before 是 so it stays on same line as 意义的来源
replace(
  "Slide 53 richPhrase line break",
  '{ text: "\\n\u5BF9\u4EBA\u6765\u8BF4\u2014\u2014\\n\u662F", color: "FFFFFF", fontSize: 30 }',
  '{ text: "\\n\u5BF9\u4EBA\u6765\u8BF4\u2014\u2014\u662F", color: "FFFFFF", fontSize: 30 }'
);

// 2. Slide 59: Remove outer Chinese quotation marks from title to prevent orphan wrapping
replace(
  "Slide 59 title orphan",
  'title: "\u201C\u4ED6\u4E0D\u5C31\u662F\u91C7\u6837\u51FA\u7684\u4E00\u4E2A\u6837\u672C\u800C\u5DF2\u5417\uFF1F\u201D"',
  'title: "\u4ED6\u4E0D\u5C31\u662F\u91C7\u6837\u51FA\u7684\u4E00\u4E2A\u6837\u672C\u800C\u5DF2\u5417\uFF1F"'
);

// 3. Slide 74: Shorten card 1 body text to prevent overflow
replace(
  "Slide 74 card 1 overflow",
  '{ title: "\u67B6\u6784\u7A81\u7834", body: "\u5168\u65B0\u6A21\u578B\u67B6\u6784\uFF0C\u4E0D\u518D\u57FA\u4E8ETransformer\\n\u8FD8\u8BB0\u5F97\u7B2C\u4E00\u5E55\u90A3\u5F20\u84DD\u56FE\u5417\uFF1F\u5982\u679C\u5B83\u672C\u8EAB\u5C31\u9519\u4E86\u5462\uFF1F\\n\\n\u51C6\u5907\uFF1A\u4FDD\u6301\u5BF9\u5E95\u5C42\u539F\u7406\u7684\u5173\u6CE8\\n\u7406\u89E3\u539F\u7406\u7684\u4EBA\u80FD\u5FEB\u901F\u8FC1\u79FB" }',
  '{ title: "\u67B6\u6784\u7A81\u7834", body: "\u5168\u65B0\u67B6\u6784\uFF0C\u4E0D\u518D\u57FA\u4E8ETransformer\\n\u5982\u679C\u7B2C\u4E00\u5E55\u7684\u84DD\u56FE\u672C\u8EAB\u5C31\u9519\u4E86\u5462\uFF1F\\n\\n\u51C6\u5907\uFF1A\u4FDD\u6301\u5BF9\u5E95\u5C42\u539F\u7406\u7684\u5173\u6CE8" }'
);

if (errors > 0) {
  console.error(`\n${errors} operations FAILED. File NOT written.`);
  process.exit(1);
} else {
  fs.writeFileSync(FILE, src, "utf8");
  console.log(`\nDone: ${changes} QA fixes applied.`);
}
