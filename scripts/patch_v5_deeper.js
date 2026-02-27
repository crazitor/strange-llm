#!/usr/bin/env node
/**
 * patch_v5_deeper.js — Add 3 deeper cross-references to later acts' notes
 */

const fs = require("fs");
const path = require("path");
const FILE = path.resolve(__dirname, "build_pptx_v4.js");
let src = fs.readFileSync(FILE, "utf8");
let changes = 0;

function appendToNotes(label, uniqueMarker, appendText) {
  const idx = src.indexOf(uniqueMarker);
  if (idx === -1) {
    console.error("FAIL:", label, "- marker not found");
    return;
  }
  // Find the end of the notes string: look for '",\n  }' after the marker
  // First find the notes: field that contains the marker
  const notesPrefix = 'notes: "';
  const notesStart = src.lastIndexOf(notesPrefix, idx);
  if (notesStart === -1) {
    console.error("FAIL:", label, "- no notes field found");
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
// Unique marker in the notes of this slide
appendToNotes(
  "Act 2 CoT callback",
  "\u4F46\u4E32\u5728\u4E00\u8D77\u662F\u8352\u8BDE\u7684", // 但串在一起是荒诞的
  "\\n\\n\u8FD8\u8BB0\u5F97\u7B2C\u4E00\u5E55\u8BB2\u7684CoT\u5417\uFF1F\u5B83\u8BA9AI\u201C\u5047\u88C5\u601D\u8003\u201D\u2014\u2014\u6BCF\u4E00\u6B65\u63A8\u7406\u90FD\u5408\u7406\uFF0C\u4F46\u5B83\u6C38\u8FDC\u4E0D\u4F1A\u505C\u4E0B\u6765\u95EE\u201C\u6211\u7684\u65B9\u5411\u5BF9\u5417\u201D\u3002\u8FD9\u5C31\u662F\u201C\u5047\u88C5\u601D\u8003\u201D\u7684\u4EE3\u4EF7\u3002"
);

// 2. Act 3 "OOD" → 涌现 callback
// Unique marker in the OOD notes
appendToNotes(
  "Act 3 Emergence callback",
  "\u8D8A\u719F\u7EC3\u8D8A\u81EA\u4FE1", // 越熟练越自信
  "\\n\\n\u7B2C\u4E00\u5E55\u8BB2\u6D8C\u73B0\u65F6\uFF0C\u6211\u4EEC\u53EA\u8BB2\u4E86\u597D\u7684\u4E00\u9762\u2014\u2014\u80FD\u529B\u4F1A\u6D8C\u73B0\u3002\u4F46OOD\u544A\u8BC9\u6211\u4EEC\uFF1A\u76F2\u70B9\u4E5F\u4F1A\u6D8C\u73B0\u3002\u6A21\u578B\u8D8A\u5927\uFF0C\u80FD\u529B\u548C\u76F2\u70B9\u540C\u65F6\u653E\u5927\u3002\u8FD9\u662F\u6D8C\u73B0\u7684\u53CC\u9762\u6027\u3002"
);

// 3. Act 4 "两道数学天花板" → 训练 callback
// Unique marker in the 两道天花板 notes
appendToNotes(
  "Act 4 Training callback",
  "\u89E3\u7A7A\u95F4\u538B\u7F29\u5230\u63A5\u8FD1\u96F6", // 解空间压缩到接近零
  "\\n\\n\u6709\u610F\u601D\u7684\u662F\uFF1A\u7B2C\u4E00\u5E55\u8BB2\u7684\u201C\u8BAD\u7EC3\u201D\u672C\u8EAB\u4E5F\u9762\u4E34\u540C\u6837\u7684\u56F0\u5883\u3002\u8BAD\u7EC3\u5668\u5728\u8D85\u53C2\u6570\u7A7A\u95F4\u91CC\u627E\u597D\u6A21\u578B\uFF0C\u5C31\u50CF\u5728\u53E6\u4E00\u4E2A\u89E3\u7A7A\u95F4\u91CC\u627E\u7B54\u6848\u2014\u2014\u540C\u4E00\u4E2A\u6570\u5B66\u56F0\u5883\u7684\u4E24\u4E2A\u4FA7\u9762\u3002"
);

fs.writeFileSync(FILE, src, "utf8");
console.log(`\nDone: ${changes} deeper cross-references added.`);
