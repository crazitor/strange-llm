#!/usr/bin/env node
/**
 * patch_v5_callbacks.js — Fix the 3 remaining cross-reference callbacks
 * that patch_v5_terms.js failed to apply.
 */

const fs = require("fs");
const path = require("path");

const FILE = path.resolve(__dirname, "build_pptx_v4.js");
let src = fs.readFileSync(FILE, "utf8");
let changes = 0;

function replace(label, oldStr, newStr) {
  if (src.indexOf(oldStr) === -1) {
    console.error("FAIL:", label);
    console.error("   not found:", oldStr.substring(0, 80));
    process.exitCode = 1;
    return;
  }
  if (src.indexOf(oldStr) !== src.lastIndexOf(oldStr)) {
    console.error("FAIL:", label, "(not unique)");
    process.exitCode = 1;
    return;
  }
  src = src.replace(oldStr, newStr);
  changes++;
  console.log("OK (replace):", label);
}

// 1. Act 3 RLHF callback — append to "模型越强/错误越像真的" slide notes
// The actual notes text ends with: 最敢拍胸脯说"没问题包治好"的人。
replace(
  "Act 3 RLHF callback",
  "\u6700\u6562\u62CD\u80F8\u8109\u8BF4\u201C\u6CA1\u95EE\u9898\u5305\u6CBB\u597D\u201D\u7684\u4EBA\u3002",
  "\u6700\u6562\u62CD\u80F8\u8109\u8BF4\u201C\u6CA1\u95EE\u9898\u5305\u6CBB\u597D\u201D\u7684\u4EBA\u3002\u8FD8\u8BB0\u5F97\u7B2C\u4E00\u5E55\u8BB2\u7684RLHF\u5417\uFF1F\u5B83\u6559\u4F1AAI\u8BF4\u201C\u542C\u8D77\u6765\u5BF9\u7684\u8BDD\u201D\u2014\u2014\u6240\u4EE5\u6A21\u578B\u8D8A\u5F3A\uFF0CRLHF\u505A\u5F97\u8D8A\u597D\uFF0C\u7F16\u9020\u7684\u8C0E\u8BDD\u5C31\u8D8A\u50CF\u771F\u8BDD\u3002"
);

// 2. Act 4 Embedding callback — append to "解空间" content notes
replace(
  "Act 4 Embedding callback",
  "\u8FD9\u5C31\u662F\u89E3\u7A7A\u95F4\u7684\u6838\u5FC3\u903B\u8F91\uFF1A\u7EA6\u675F\u6761\u4EF6\u8D8A\u591A\uFF0C\u5408\u683C\u7B54\u6848\u8D8A\u5C11\uFF0C\u627E\u5230\u7B54\u6848\u8D8A\u96BE\u3002",
  "\u8FD9\u5C31\u662F\u89E3\u7A7A\u95F4\u7684\u6838\u5FC3\u903B\u8F91\uFF1A\u7EA6\u675F\u6761\u4EF6\u8D8A\u591A\uFF0C\u5408\u683C\u7B54\u6848\u8D8A\u5C11\uFF0C\u627E\u5230\u7B54\u6848\u8D8A\u96BE\u3002\u8FD8\u8BB0\u5F97\u7B2C\u4E00\u5E55\u8BB2\u7684Embedding\u5417\uFF1F\u6BCF\u4E2A\u53EF\u80FD\u7684\u7B54\u6848\u90FD\u662F\u5411\u91CF\u7A7A\u95F4\u4E2D\u7684\u4E00\u4E2A\u70B9\u3002\u89E3\u7A7A\u95F4\u5C31\u662F\u6240\u6709\u201C\u5408\u683C\u70B9\u201D\u7684\u96C6\u5408\u3002"
);

// 3. Act 6 Transformer callback — enhance first card of "三种可能的未来"
replace(
  "Act 6 Transformer callback",
  "\u5168\u65B0\u6A21\u578B\u67B6\u6784\uFF0C\u4E0D\u518D\u57FA\u4E8ETransformer",
  "\u5168\u65B0\u6A21\u578B\u67B6\u6784\uFF0C\u4E0D\u518D\u57FA\u4E8ETransformer\n\u8FD8\u8BB0\u5F97\u7B2C\u4E00\u5E55\u90A3\u5F20\u84DD\u56FE\u5417\uFF1F\u5982\u679C\u5B83\u672C\u8EAB\u5C31\u9519\u4E86\u5462\uFF1F"
);

fs.writeFileSync(FILE, src, "utf8");
console.log(`\nDone: ${changes} changes applied.`);
