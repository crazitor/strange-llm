#!/usr/bin/env node
/**
 * patch_v5_deeper_v2.js — Add 2 remaining deeper cross-references
 * (Act 4 Training callback was already applied by v1)
 */

const fs = require("fs");
const path = require("path");
const FILE = path.resolve(__dirname, "build_pptx_v4.js");
let src = fs.readFileSync(FILE, "utf8");
let changes = 0;
let errors = 0;

function appendToNotes(label, uniqueMarker, appendText) {
  const idx = src.indexOf(uniqueMarker);
  if (idx === -1) {
    console.error("FAIL:", label, "- marker not found");
    errors++;
    return;
  }
  // Find the notes: field that contains the marker
  const notesPrefix = 'notes: "';
  const notesStart = src.lastIndexOf(notesPrefix, idx);
  if (notesStart === -1) {
    console.error("FAIL:", label, "- no notes field found");
    errors++;
    return;
  }

  // Find the closing quote of the notes string
  const contentStart = notesStart + notesPrefix.length;
  let i = contentStart;
  while (i < src.length) {
    if (src[i] === '"' && src[i-1] !== '\\') break;
    i++;
  }

  // Insert text before the closing quote
  src = src.substring(0, i) + appendText + src.substring(i);
  changes++;
  console.log("OK:", label);
}

// 1. Act 2 "局部合理全局荒诞" → CoT callback
// Unique marker from actual notes text at line 1322
appendToNotes(
  "Act 2 CoT callback",
  "\u5C40\u90E8\u5408\u7406\uFF0C\u5168\u5C40\u8352\u8BDE", // 局部合理，全局荒诞 — in the notes text
  "\\n\\n\u8FD8\u8BB0\u5F97\u7B2C\u4E00\u5E55\u8BB2\u7684CoT\u5417\uFF1F\u5B83\u8BA9AI\u201C\u5047\u88C5\u601D\u8003\u201D\u2014\u2014\u6BCF\u4E00\u6B65\u63A8\u7406\u90FD\u5408\u7406\uFF0C\u4F46\u5B83\u6C38\u8FDC\u4E0D\u4F1A\u505C\u4E0B\u6765\u95EE\u201C\u6211\u7684\u65B9\u5411\u5BF9\u5417\u201D\u3002\u8FD9\u5C31\u662F\u201C\u5047\u88C5\u601D\u8003\u201D\u7684\u4EE3\u4EF7\u3002"
);

// 2. Act 3 "OOD" → 涌现 callback
// Unique marker from actual notes text at line 1412
appendToNotes(
  "Act 3 Emergence callback",
  "\u72AF\u9519\u7684\u65F6\u5019\u8DDF\u6B63\u786E\u7684\u65F6\u5019\u770B\u8D77\u6765\u4E00\u6A21\u4E00\u6837", // 犯错的时候跟正确的时候看起来一模一样
  "\\n\\n\u7B2C\u4E00\u5E55\u8BB2\u6D8C\u73B0\u65F6\uFF0C\u6211\u4EEC\u53EA\u8BB2\u4E86\u597D\u7684\u4E00\u9762\u2014\u2014\u80FD\u529B\u4F1A\u6D8C\u73B0\u3002\u4F46OOD\u544A\u8BC9\u6211\u4EEC\uFF1A\u76F2\u70B9\u4E5F\u4F1A\u6D8C\u73B0\u3002\u6A21\u578B\u8D8A\u5927\uFF0C\u80FD\u529B\u548C\u76F2\u70B9\u540C\u65F6\u653E\u5927\u3002\u8FD9\u662F\u6D8C\u73B0\u7684\u53CC\u9762\u6027\u3002"
);

if (errors > 0) {
  console.error(`\n${errors} operations FAILED. File NOT written.`);
  process.exit(1);
} else {
  fs.writeFileSync(FILE, src, "utf8");
  console.log(`\nDone: ${changes} deeper cross-references added.`);
}
