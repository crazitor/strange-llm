#!/usr/bin/env node
const fs = require("fs");
const path = require("path");
const FILE = path.resolve(__dirname, "build_pptx_v4.js");
let src = fs.readFileSync(FILE, "utf8");

// Find and fix MoE card body using a unique plain-text marker
const marker = 'DeepSeek用的就是这个架构';
const idx = src.indexOf(marker);
if (idx === -1) {
  console.error("FAIL: MoE marker not found");
  process.exit(1);
}

// Find the start of the body string for MoE card
// Look backwards from marker to find 'body: "'
const bodyPrefix = 'body: "';
const bodyStart = src.lastIndexOf(bodyPrefix, idx);
if (bodyStart === -1) {
  console.error("FAIL: body prefix not found");
  process.exit(1);
}

// Find the closing quote of the body string
const bodyContentStart = bodyStart + bodyPrefix.length;
// Need to find the unescaped closing quote
let i = bodyContentStart;
while (i < src.length) {
  if (src[i] === '"' && src[i-1] !== '\\') break;
  i++;
}
const bodyContentEnd = i;
const oldBody = src.substring(bodyContentStart, bodyContentEnd);
console.log("Old body:", oldBody.substring(0, 100) + "...");

// New shortened body (using same escape style as original)
const newBody = '把一个大模型拆成多个\\u201C专家\\u201D\\n每次只激活相关的几个\\n(DeepSeek用的就是这个)\\n\\n\\u2192 一个公司，不是全能选手';

src = src.substring(0, bodyContentStart) + newBody + src.substring(bodyContentEnd);
fs.writeFileSync(FILE, src, "utf8");
console.log("OK: MoE card body shortened");
console.log("New body:", newBody);
