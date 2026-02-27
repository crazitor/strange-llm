#!/usr/bin/env node
const fs = require("fs");
const path = require("path");
const FILE = path.resolve(__dirname, "build_pptx_v4.js");
let src = fs.readFileSync(FILE, "utf8");
let changes = 0;

function replace(label, oldStr, newStr) {
  if (!src.includes(oldStr)) {
    console.error("FAIL:", label);
    return;
  }
  src = src.replace(oldStr, newStr);
  changes++;
  console.log("OK:", label);
}

// Title page: 120→130
replace("title info timing", '120分钟 · 七幕结构 · 2025', '130分钟 · 七幕结构 · 2025');

// Journey roadmap hint: 120→130
replace("journey hint timing", '120分钟 · 七幕结构 · 中场休息10分钟', '130分钟 · 七幕结构 · 中场休息10分钟');

// Mid-break notes: 前半场约53分钟→约60分钟
replace("break notes timing", '前半场（序幕+三幕）约53分钟', '前半场（序幕+三幕）约60分钟');

// Act 5 notes: 花了大概80分钟→大概85分钟
replace("act5 notes timing", '花了大概80分钟', '花了大概85分钟');

fs.writeFileSync(FILE, src, "utf8");
console.log(`\nDone: ${changes} timing updates.`);
