#!/usr/bin/env node
const fs = require("fs");
const path = require("path");
const FILE = path.resolve(__dirname, "build_pptx_v4.js");
let src = fs.readFileSync(FILE, "utf8");
let changes = 0;

function fix(label, broken, fixed) {
  if (!src.includes(broken)) {
    console.error("FAIL:", label);
    process.exitCode = 1;
    return;
  }
  src = src.replace(broken, fixed);
  changes++;
  console.log("OK:", label);
}

// Fix leftBody: real newline before "· CoT" should be \n
fix(
  "Fix leftBody CoT newline",
  "\u585E\u9884\u8BBE\u7684\u6307\u4EE4\n\u00B7 CoT",
  "\u585E\u9884\u8BBE\u7684\u6307\u4EE4\\n\u00B7 CoT"
);

// Fix rightBody: real newline before "· ReAct" should be \n
fix(
  "Fix rightBody ReAct newline",
  "\u5DE5\u5177\u5BF9\u63A5\u6807\u51C6\u5316\n\u00B7 ReAct",
  "\u5DE5\u5177\u5BF9\u63A5\u6807\u51C6\u5316\\n\u00B7 ReAct"
);

fs.writeFileSync(FILE, src, "utf8");
console.log(`\nDone: ${changes} fixes applied.`);
