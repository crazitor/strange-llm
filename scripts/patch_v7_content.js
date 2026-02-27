#!/usr/bin/env node
/**
 * patch_v7_content.js — Tier 1 + Tier 2 body/sub/phrase/quote changes
 *
 * Modifies slide data in build_pptx_v4.js for content accuracy & narrative upgrades.
 * Run: node scripts/patch_v7_content.js
 */

const fs = require("fs");
const path = require("path");
const FILE = path.resolve(__dirname, "build_pptx_v4.js");
let src = fs.readFileSync(FILE, "utf8");
let changes = 0;
let errors = 0;

function replace(label, oldStr, newStr) {
  if (!src.includes(oldStr)) {
    console.error("FAIL:", label, "- string not found");
    errors++;
    return;
  }
  const count = src.split(oldStr).length - 1;
  if (count > 1) {
    console.error("FAIL:", label, "- string not unique (" + count + " occurrences)");
    errors++;
    return;
  }
  src = src.replace(oldStr, newStr);
  changes++;
  console.log("OK:", label);
}

// ================================================================
// 1.1 Slide 63 — rewrite body: add King case
// ================================================================
replace(
  "1.1a Slide 63 body (当创造变成采样)",
  `body:  "你花三个月画的画 = 可能性空间里的一个坐标点。AI三秒到达。\\n如果创作只是采样，那人和AI的区别只是效率差异 — 而效率差异不是可持续的竞争优势。"`,
  `body:  "2025年7月，200名游戏开发者被裁。\\n取代他们的不是外部AI公司，是他们自己花两年训练的AI工具。\\n他们亲手建造了替代自己的机器。\\n\\n如果创作只是采样，那人和AI的区别只是效率差异\\n— 而效率差异不是可持续的竞争优势。"`
);

// ================================================================
// 1.1b Slide 65 — rewrite sub
// ================================================================
replace(
  "1.1b Slide 65 sub (最黑暗时刻)",
  `sub: "AI取代你的工作？你可以换一份\\nAI告诉你一切都只是随机采样？\\n——换什么都是采样"`,
  `sub: "AI取代你的工作？你可以换一份。\\n但如果替代你的AI——是你亲手训练的呢？\\n你连'换一份'都可能是在给下一个AI喂数据。"`
);

// ================================================================
// 1.3 Slide 82 — rewrite body
// ================================================================
replace(
  "1.3 Slide 82 body (回到第一个画面)",
  `body: "2022年，ChatGPT发布，全世界疯狂。\\n2025年，GPT-5发布，世界波澜不惊。\\n\\n为什么？\\n因为你现在知道了——\\nAI的每一次\u201C进步\u201D都只是在修补上一层的缺陷。\\n理解这座塔的结构与代价，比盲目崇拜它的高度更重要。"`,
  `body: "2022年，ChatGPT发布，全世界疯狂。\\n2025年，GPT-5发布，世界波澜不惊。\\n\\n为什么？\\n因为你现在知道了：补丁堆得再高，也堆不过两道数学天花板。\\n但更重要的是，你知道了你有一个AI永远不会有的能力\\n——在关键时刻说'停，这不对'。"`
);

// ================================================================
// 1.3 Slide 83 — rewrite quote
// ================================================================
replace(
  "1.3 Slide 83 quote",
  `quote: "AI的每一次输出都是一次采样——\\n无代价的、可撤回的、无需负责的采样。\\n\\n而你的每一个决定都是一次选择——\\n有代价的、不可逆的、需要你用有限的生命去承担的选择。"`,
  `quote: "你拆解了一座塔的结构。\\n你看到了它运转时的荒诞。\\n你找到了写在数学里的两道天花板。\\n你在最黑暗的时刻发现了——\\n理解代价，本身就是人的能力。"`
);

// ================================================================
// 1.4 Slide 3 — rewrite sub (delay core judgment reveal)
// ================================================================
replace(
  "1.4 Slide 3 sub (核心判断)",
  `sub: "\u7406\u89E3\u8FD9\u5EA7\u8865\u4E01\u4E4B\u5854\u7684\u7ED3\u6784\u548C\u4EE3\u4EF7\uFF0C\u8FDC\u6BD4\u8FFD\u6367\u5B83\u7684\u9AD8\u5EA6\u66F4\u6709\u4EF7\u503C"`,
  `sub: "\u8FD9\u662F\u6211\u4ECA\u5929\u7684\u6838\u5FC3\u5224\u65AD\u3002\u4F46\u8FD9\u4E2A\u5224\u65AD\u9700\u8981\u4F60\u8DDF\u6211\u8D70\u5B8C\u7B2C\u4E00\u5E55\u4E4B\u540E\uFF0C\u624D\u80FD\u771F\u6B63\u7406\u89E3\u4E3A\u4EC0\u4E48\u3002"`
);

// ================================================================
// 2.1 Slide 74 — rewrite card 1 body (三刀: add GPT-5 data)
// ================================================================
replace(
  "2.1 Slide 74 card 1 (天花板不是永恒的)",
  `{ title: "\u5929\u82B1\u677F\u4E0D\u662F\u6C38\u6052\u7684", body: "\u8BBA\u6587\u9650\u5B9A\u8BCD\uFF1A\u201C\u5728\u5F53\u4ECA\u8FD9\u5957\u6846\u67B6\u4E0B\u201D\\n\u5F3A\u5316\u5B66\u4E60\u3001\u6DF7\u5408\u4E13\u5BB6\u7B49\u5728\u5C1D\u8BD5\u6362\u5168\u65B0\u65B9\u6848\\n\u628A\u201C\u4E8B\u5B9E\u5FEB\u7167\u201D\u5F53\u6210\u201C\u6C38\u6052\u5224\u51B3\u4E66\u201D\u662F\u9519\u7684" }`,
  `{ title: "\u5929\u82B1\u677F\u4E0D\u662F\u6C38\u6052\u7684", body: "GPT-5\u5E7B\u89C9\u7387\u964D\u523012.9%\u21929.6%\uFF0C\u6BD4GPT-4o\u51CF\u5C1145%\\n\u8865\u4E01\u786E\u5B9E\u5728\u53D8\u597D\u3002\u201C\u5929\u82B1\u677F\u201D\u53EF\u80FD\u4E0D\u662F\u56FA\u5B9A\u9AD8\u5EA6\\n\u2014\u2014\u5B83\u4E5F\u8BB8\u5728\u7F13\u6162\u62AC\u5347" }`
);

// ================================================================
// 2.3 Slide 36 body — "计算理论、信息论和统计学三个维度" → "三个完全不同的数学角度"
// ================================================================
replace(
  "2.3/2.4 Slide 36 body (论文铁证)",
  `body: "\u4E00\u7BC7\u8BBA\u6587\u4ECE\u8BA1\u7B97\u7406\u8BBA\u3001\u4FE1\u606F\u8BBA\u548C\u7EDF\u8BA1\u5B66\u4E09\u4E2A\u7EF4\u5EA6\u8BC1\u660E`,
  `body: "\u4E00\u7BC7\u8BBA\u6587\u4ECE\u4E09\u4E2A\u5B8C\u5168\u4E0D\u540C\u7684\u6570\u5B66\u89D2\u5EA6\u8BC1\u660E`
);

// ================================================================
// 2.2 Slide 72 bridge — rewrite sub
// ================================================================
replace(
  "2.2 Slide 72 sub (bridge 第五幕→第六幕)",
  `sub: "\u6574\u4E2A\u7B2C\u4E94\u5E55\u5EFA\u7ACB\u5728\u4E00\u4E2A\u524D\u63D0\u4E0A\uFF1A\\n\u201C\u5F53\u524DAI\u67B6\u6784\u6709\u4E0D\u53EF\u903E\u8D8A\u7684\u5929\u82B1\u677F\u201D\\n\u8BDA\u5B9E\u7684\u8BBA\u8BC1\u5FC5\u987B\u627F\u8BA4\u81EA\u8EAB\u7684\u8FB9\u754C"`,
  `sub: "\u524D\u56DB\u5E55\u5BF9AI\u5C40\u9650\u7684\u5206\u6790\uFF0C\u5EFA\u7ACB\u5728\u4E00\u4E2A\u524D\u63D0\u4E0A\\n\u201C\u5F53\u524D\u8FD9\u5957\u67B6\u6784\u6709\u4E0D\u53EF\u903E\u8D8A\u7684\u5929\u82B1\u677F\u201D\\n\u8BDA\u5B9E\u7684\u8BBA\u8BC1\u5FC5\u987B\u627F\u8BA4\u81EA\u8EAB\u7684\u8FB9\u754C"`
);

// ================================================================
// 3.3 Slide 33 card 3 — replace 太空战舰 example
// ================================================================
replace(
  "3.3 Slide 33 card 3 (生成 → 语言领域倒挂)",
  `{ title: "\u751F\u6210", body: "\u80FD\u751F\u6210\u89C6\u89C9\u6548\u679C\u60CA\u4EBA\u7684\u592A\u7A7A\u6218\u8230\u5927\u6218\u89C6\u9891\\n\\n\u4F46\u505A\u4E0D\u4E86\u201C\u6B63\u65B9\u5F62\u53D8\u6210\u5706\u5F62\u201D\u7684\u7B80\u5355\u52A8\u753B" }`,
  `{ title: "\u8BED\u8A00", body: "\u80FD\u5199\u51FA\u8BA9\u4F60\u6D41\u6CEA\u7684\u60C5\u4E66\\n\\n\u4F46\u53EF\u80FD\u628A\u201C\u5DF2\u7ECF\u201D\u5199\u6210\u201C\u5DF1\u7ECF\u201D" }`
);

// ================================================================
// 3.5 Slide 61 — 像素实验 256 → 1600多万
// ================================================================
replace(
  "3.5a Slide 61 body (256→1600万)",
  `\u6BCF\u4E2A\u50CF\u7D20256\u79CD\u989C\u8272`,
  `\u6BCF\u4E2A\u50CF\u7D201600\u591A\u4E07\u79CD\u989C\u8272`
);

replace(
  "3.5b Slide 61 body (256的→1600万的)",
  `256\u7684200\u4E07\u6B21\u65B9`,
  `1600\u4E07\u7684200\u4E07\u6B21\u65B9`
);

// ================================================================
// WRITE BACK
// ================================================================
fs.writeFileSync(FILE, src, "utf8");
console.log(`\nDone: ${changes} changes applied, ${errors} errors.`);
if (errors > 0) process.exit(1);
