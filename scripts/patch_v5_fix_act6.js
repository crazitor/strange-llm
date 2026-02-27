#!/usr/bin/env node
const fs = require("fs");
const path = require("path");
const FILE = path.resolve(__dirname, "build_pptx_v4.js");
let src = fs.readFileSync(FILE, "utf8");

// Fix the broken newline: real newline between Transformer and 还记得 should be \n
const broken = "Transformer\n\u8FD8\u8BB0\u5F97\u7B2C\u4E00\u5E55\u90A3\u5F20\u84DD\u56FE\u5417\uFF1F\u5982\u679C\u5B83\u672C\u8EAB\u5C31\u9519\u4E86\u5462\uFF1F\\n";
const fixed = "Transformer\\n\u8FD8\u8BB0\u5F97\u7B2C\u4E00\u5E55\u90A3\u5F20\u84DD\u56FE\u5417\uFF1F\u5982\u679C\u5B83\u672C\u8EAB\u5C31\u9519\u4E86\u5462\uFF1F\\n";

if (src.indexOf(broken) === -1) {
  console.error("FAIL: broken text not found");
  // Try to show what's around Transformer
  const idx = src.indexOf("Transformer");
  if (idx >= 0) {
    console.error("Context:", JSON.stringify(src.substring(idx-10, idx+100)));
  }
  process.exit(1);
}

src = src.replace(broken, fixed);
fs.writeFileSync(FILE, src, "utf8");
console.log("OK: Fixed Act 6 Transformer newline");
