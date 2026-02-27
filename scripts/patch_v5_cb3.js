#!/usr/bin/env node
const fs = require("fs");
const path = require("path");
const FILE = path.resolve(__dirname, "build_pptx_v4.js");
let src = fs.readFileSync(FILE, "utf8");

// Act 3 RLHF callback — 拍胸脯 = \u62CD\u80F8\u812F
const old = "\u6700\u6562\u62CD\u80F8\u812F\u8BF4\u201C\u6CA1\u95EE\u9898\u5305\u6CBB\u597D\u201D\u7684\u4EBA\u3002";
const rep = "\u6700\u6562\u62CD\u80F8\u812F\u8BF4\u201C\u6CA1\u95EE\u9898\u5305\u6CBB\u597D\u201D\u7684\u4EBA\u3002\u8FD8\u8BB0\u5F97\u7B2C\u4E00\u5E55\u8BB2\u7684RLHF\u5417\uFF1F\u5B83\u6559\u4F1AAI\u8BF4\u201C\u542C\u8D77\u6765\u5BF9\u7684\u8BDD\u201D\u2014\u2014\u6240\u4EE5\u6A21\u578B\u8D8A\u5F3A\uFF0CRLHF\u505A\u5F97\u8D8A\u597D\uFF0C\u7F16\u9020\u7684\u8C0E\u8BDD\u5C31\u8D8A\u50CF\u771F\u8BDD\u3002";

if (src.indexOf(old) === -1) {
  console.error("FAIL: marker not found");
  process.exit(1);
}
src = src.replace(old, rep);
fs.writeFileSync(FILE, src, "utf8");
console.log("OK: Act 3 RLHF callback applied");
