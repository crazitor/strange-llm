#!/usr/bin/env node
/**
 * patch_v6_fixes2.js — Further shorten card 1 on slide 74 (三种可能的未来)
 */

const fs = require("fs");
const path = require("path");
const FILE = path.resolve(__dirname, "build_pptx_v4.js");
let src = fs.readFileSync(FILE, "utf8");

const old = '{ title: "\u67B6\u6784\u7A81\u7834", body: "\u5168\u65B0\u67B6\u6784\uFF0C\u4E0D\u518D\u57FA\u4E8ETransformer\\n\u5982\u679C\u7B2C\u4E00\u5E55\u7684\u84DD\u56FE\u672C\u8EAB\u5C31\u9519\u4E86\u5462\uFF1F\\n\\n\u51C6\u5907\uFF1A\u4FDD\u6301\u5BF9\u5E95\u5C42\u539F\u7406\u7684\u5173\u6CE8" }';
// 全新架构，不再基于Transformer\n如果第一幕的蓝图本身就错了呢？\n\n准备：保持对底层原理的关注

const nw = '{ title: "\u67B6\u6784\u7A81\u7834", body: "\u5168\u65B0\u67B6\u6784\uFF0C\u4E0D\u518D\u57FA\u4E8ETransformer\\n\u84DD\u56FE\u672C\u8EAB\u53EF\u80FD\u5C31\u662F\u9519\u7684\\n\\n\u51C6\u5907\uFF1A\u5173\u6CE8\u5E95\u5C42\u539F\u7406" }';
// 全新架构，不再基于Transformer\n蓝图本身可能就是错的\n\n准备：关注底层原理

if (!src.includes(old)) {
  console.error("FAIL: card 1 string not found");
  process.exit(1);
}

src = src.replace(old, nw);
fs.writeFileSync(FILE, src, "utf8");
console.log("OK: card 1 further shortened");
