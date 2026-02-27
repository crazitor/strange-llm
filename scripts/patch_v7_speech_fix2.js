#!/usr/bin/env node
/**
 * patch_v7_speech_fix2.js — Fix 2 narrative flow issues in speech script
 *
 * Issue 1: Line 767 — "注意一件事" paragraph interrupts Path C description
 * Issue 2: Line 352 — Parenthetical examples don't match new example 3 (情书/己经)
 *
 * Run: node scripts/patch_v7_speech_fix2.js
 */

const fs = require("fs");
const path = require("path");
const FILE = path.resolve(__dirname, "..", "output", "speech_script_v2.md");
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
// Fix 1: Path C — move "注意一件事" to after all three paths
// ================================================================
replace(
  "Fix Path C interruption",
  `**路径C：渐进优化。**

注意一件事：不管走哪条路，你需要的核心能力是同一套——理解结构、识别边界、在关键时刻止损。这不是巧合，这是因为这套方法论就是为不确定性设计的。 这是最不性感但最可能的路径。没有石破天惊的新架构，也没有大洗牌。现有框架继续打磨——模型一点点变强，成本一点点下降，应用一点点成熟。就像2024年那样，看似平淡，实际上在为下一次"震撼时刻"蓄力。

如果这条路成真——立刻开始在你的真实工作中使用AI，但有意识地测试它的边界。不盲目信任，也不盲目排斥。像一个质检员一样——一边用它，一边记录它在哪里出错、在什么类型的任务上靠不住。这份"边界地图"才是你的核心竞争力。

### 二、无论哪条路，请带走这些`,
  `**路径C：渐进优化。** 这是最不性感但最可能的路径。没有石破天惊的新架构，也没有大洗牌。现有框架继续打磨——模型一点点变强，成本一点点下降，应用一点点成熟。就像2024年那样，看似平淡，实际上在为下一次"震撼时刻"蓄力。

如果这条路成真——立刻开始在你的真实工作中使用AI，但有意识地测试它的边界。不盲目信任，也不盲目排斥。像一个质检员一样——一边用它，一边记录它在哪里出错、在什么类型的任务上靠不住。这份"边界地图"才是你的核心竞争力。

注意一件事：不管走哪条路，你需要的核心能力是同一套——理解结构、识别边界、在关键时刻止损。这不是巧合，这是因为这套方法论就是为不确定性设计的。

### 二、无论哪条路，请带走这些`
);

// ================================================================
// Fix 2: Line 352 — Update summary examples to match new example 3
// ================================================================
replace(
  "Fix summary examples mismatch",
  `**越"难"的任务（数学竞赛、地理推理、太空大战），AI做得越好。越"简单"的任务（算术、数手指、几何动画），AI反而做不好。**`,
  `**越"难"的任务（数学竞赛、地理推理、写催泪情书），AI做得越好。越"简单"的任务（算术、数手指、分辨"已"和"己"），AI反而做不好。**`
);

// ================================================================
// WRITE BACK
// ================================================================
fs.writeFileSync(FILE, src, "utf8");
console.log(`\nDone: ${changes} changes applied, ${errors} errors.`);
if (errors > 0) process.exit(1);
