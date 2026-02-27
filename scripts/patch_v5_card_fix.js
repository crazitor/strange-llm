#!/usr/bin/env node
const fs = require("fs");
const path = require("path");
const FILE = path.resolve(__dirname, "build_pptx_v4.js");
let src = fs.readFileSync(FILE, "utf8");
let changes = 0;

function replace(label, oldStr, newStr) {
  if (!src.includes(oldStr)) {
    console.error("FAIL:", label);
    process.exitCode = 1;
    return;
  }
  src = src.replace(oldStr, newStr);
  changes++;
  console.log("OK:", label);
}

// 1. Fix MoE card text overflow — remove "DeepSeek" line, merge analogy
replace(
  "MoE card text shorten",
  "\u628A\u4E00\u4E2A\u5927\u6A21\u578B\u62C6\u6210\u591A\u4E2A\u201C\u4E13\u5BB6\u201D\\n\u6BCF\u6B21\u53EA\u6FC0\u6D3B\u76F8\u5173\u7684\u51E0\u4E2A\\nDeepSeek\u7528\u7684\u5C31\u662F\u8FD9\u4E2A\u67B6\u6784\\n\\n\u2192 \u4E00\u4E2A\u516C\u53F8\u800C\u4E0D\u662F\u4E00\u4E2A\u5168\u80FD\u9009\u624B\\n\u6548\u7387\u9AD8\u4E86\uFF0C\u4F46\u6CA1\u4EBA\u80FD\u770B\u5230\u5168\u5C40",
  "\u628A\u4E00\u4E2A\u5927\u6A21\u578B\u62C6\u6210\u591A\u4E2A\u201C\u4E13\u5BB6\u201D\\n\u6BCF\u6B21\u53EA\u6FC0\u6D3B\u76F8\u5173\u7684\u51E0\u4E2A\\n(DeepSeek\u7528\u7684\u5C31\u662F\u8FD9\u4E2A)\\n\\n\u2192 \u4E00\u4E2A\u516C\u53F8\uFF0C\u4E0D\u662F\u5168\u80FD\u9009\u624B"
);

// 2. Fix RLHF title — add Chinese gloss for consistency
replace(
  "RLHF title add Chinese",
  '{ title: "RLHF", body:',
  '{ title: "RLHF\uFF08\u4EBA\u7C7B\u53CD\u9988\uFF09", body:'
);

fs.writeFileSync(FILE, src, "utf8");
console.log(`\nDone: ${changes} fixes applied.`);
