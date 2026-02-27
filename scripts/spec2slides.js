/**
 * spec2slides.js — Parse v4 spec files and generate slides[] array for build_pptx_v5.js
 *
 * Usage: node scripts/spec2slides.js > /tmp/slides_array.js
 */

const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const specFiles = [
  path.join(ROOT, "output", "slides_spec_v4_part1.md"),
  path.join(ROOT, "output", "slides_spec_v4_part2.md"),
  path.join(ROOT, "output", "slides_spec_v4_part3.md"),
];

// Diagram name mapping for diagram-placeholder pages
const DIAGRAM_MAP = {
  4: "patch_tower_layers.png",
  28: "patch_tower_full.png",
  40: "patch_tower_stoploss.png",
  45: "bamboo_growth_curve.png",
  49: "capability_inversion.png",
  50: "ood_boundary.png",
  54: "patch_tower_ceiling.png",
  65: "solution_space.png",
  78: "climbing_vs_helicopter.png",
  94: "ai_vs_human_cost.png",
  98: "three_paths.png",
};

// Act label extraction from 章节 field
function extractActLabel(chapter) {
  if (!chapter) return "";
  // Match: 序幕, 第一幕, 第二幕, ..., 第七幕
  const m = chapter.match(/(序幕|第[一二三四五六七]幕)/);
  return m ? m[1] : "";
}

// Parse all spec files and return array of page objects
function parseSpecs() {
  let allText = "";
  for (const f of specFiles) {
    allText += fs.readFileSync(f, "utf-8") + "\n";
  }

  // Split by page headers
  const pageRegex = /### 页 (\d+): (.+)/g;
  const pages = [];
  let match;
  const positions = [];

  while ((match = pageRegex.exec(allText)) !== null) {
    positions.push({
      pageNum: parseInt(match[1]),
      title: match[2].trim(),
      start: match.index,
    });
  }

  // Extract content for each page
  for (let i = 0; i < positions.length; i++) {
    const start = positions[i].start;
    const end = i + 1 < positions.length ? positions[i + 1].start : allText.length;
    const content = allText.slice(start, end);

    const pageNum = positions[i].pageNum;
    const rawTitle = positions[i].title;

    // Extract 章节
    const chapterMatch = content.match(/\*\*章节\*\*:\s*(.+)/);
    const chapter = chapterMatch ? chapterMatch[1].trim() : "";

    // Extract PPT显示内容 section
    const pptMatch = content.match(/\*\*PPT显示内容\*\*:\n([\s\S]*?)(?=\n\*\*演讲词\*\*|\n\*\*讲者提醒\*\*)/);
    const pptContent = pptMatch ? pptMatch[1] : "";

    // Extract 标题
    const titleMatch = pptContent.match(/- 标题:\s*(.+)/);
    const slideTitle = titleMatch ? titleMatch[1].trim() : rawTitle;

    // Extract 副标题/要点 bullets
    const bullets = [];
    const bulletRegex = /^\s+-\s+(.+)/gm;
    let bMatch;
    let inBullets = false;
    const lines = pptContent.split("\n");
    for (const line of lines) {
      if (line.match(/- 标题:/)) { inBullets = false; continue; }
      if (line.match(/- 配图:/)) { inBullets = false; continue; }
      if (line.match(/- 副标题\/要点:/)) { inBullets = true; continue; }
      if (line.match(/- 视觉设计:/)) { inBullets = true; continue; }
      if (inBullets && line.match(/^\s+-\s+/)) {
        bullets.push(line.replace(/^\s+-\s+/, "").trim());
      }
    }

    // Extract 配图
    const imageMatch = pptContent.match(/- 配图:\s*(.+)/);
    const imageRef = imageMatch ? imageMatch[1].trim() : "";

    // Extract 演讲词
    const notesMatch = content.match(/\*\*演讲词\*\*:\n>\s*([\s\S]*?)(?=\n\n\*\*讲者提醒\*\*|\n---|\n##)/);
    let notes = "";
    if (notesMatch) {
      notes = notesMatch[1]
        .split("\n")
        .map(l => l.replace(/^>\s*/, "").trim())
        .filter(l => l)
        .join("\n");
    }

    pages.push({
      pageNum,
      rawTitle,
      slideTitle,
      chapter,
      actLabel: extractActLabel(chapter),
      bullets,
      imageRef,
      notes,
    });
  }

  return pages;
}

// Determine slide type from page data
function determineType(page) {
  const { pageNum, imageRef, chapter, slideTitle } = page;

  if (pageNum === 1) return "cover";
  if (pageNum === 106) return "closing";

  // Check for actTitle pages
  if (imageRef.includes("actTitle") || (chapter.includes("开场") && !imageRef.includes("video"))) {
    return "actTitle";
  }

  // Check 设计指示 patterns
  if (imageRef.includes("设计指示")) {
    if (imageRef.includes("stat")) return "stat";
    if (imageRef.includes("quote-card")) return "quote";
    if (imageRef.includes("keyPhrase")) return "keyPhrase";
    if (imageRef.includes("comparison")) return "comparison";
    if (imageRef.includes("threeCards")) return "threeCards";
    if (imageRef.includes("fourCards")) return "fourCards";
    if (imageRef.includes("text-only")) return "content";
    if (imageRef.includes("diagram-placeholder")) return "content"; // with diagram
    if (imageRef.includes("content")) return "content";
  }

  // Diagram references
  if (imageRef.includes("diagram") && imageRef.includes(".png")) return "content";

  // Screenshot references
  if (imageRef.match(/video\d+_t\d+/)) return "screenshot";

  // Default
  return "content";
}

// Check if page has a diagram
function getDiagram(page) {
  if (DIAGRAM_MAP[page.pageNum]) return DIAGRAM_MAP[page.pageNum];
  // Check imageRef for .png diagram references
  const m = page.imageRef.match(/(\w+\.png)/);
  if (m && !m[1].match(/^video/)) return m[1];
  return null;
}

// Check if page has a screenshot
function getScreenshot(page) {
  const m = page.imageRef.match(/(video\d+_t\d+[^,\]]*\.jpg)/);
  return m ? m[1] : null;
}

// Act number mapping for actTitle pages
const ACT_NUMS = {
  "第一幕": "01", "第二幕": "02", "第三幕": "03", "第四幕": "04",
  "第五幕": "05", "第六幕": "06", "第七幕": "07",
};

const ACCENT_SHAPES = {
  "01": "layers", "02": "warnStripe", "03": "crack", "04": "target",
  "05": "fork", "06": "scalpel", "07": "trident",
};

function escJS(s) {
  return s.replace(/\\/g, "\\\\").replace(/"/g, '\\"').replace(/\n/g, "\\n");
}

// Generate JS code for a single slide
function generateSlide(page) {
  const type = determineType(page);
  const lines = [];

  lines.push("  {");

  switch (type) {
    case "cover":
      lines.push(`    type: "cover",`);
      lines.push(`    title: "AI：拆一座补丁之塔",`);
      lines.push(`    subtitle: "一个技术从业者的深度解读",`);
      lines.push(`    info: "130分钟 · 七幕结构 · 2025",`);
      break;

    case "closing":
      lines.push(`    type: "closing",`);
      lines.push(`    title: "有限的选择，才是人的终极武器。",`);
      lines.push(`    subtitle: "谢谢大家",`);
      lines.push(`    info: "AI：拆一座补丁之塔",`);
      break;

    case "actTitle": {
      const actNum = ACT_NUMS[page.actLabel] || "";
      lines.push(`    type: "actTitle",`);
      if (actNum) lines.push(`    actNum: "${actNum}",`);
      if (actNum && ACCENT_SHAPES[actNum]) lines.push(`    accentShape: "${ACCENT_SHAPES[actNum]}",`);
      lines.push(`    title: "${escJS(page.slideTitle)}",`);
      if (page.bullets.length > 0) {
        lines.push(`    subtitle: "${escJS(page.bullets[0])}",`);
      }
      break;
    }

    case "screenshot": {
      const img = getScreenshot(page);
      lines.push(`    type: "screenshot",`);
      lines.push(`    title: "${escJS(page.slideTitle)}",`);
      if (img) lines.push(`    image: screenshot("${escJS(img)}"),`);
      if (page.bullets.length > 0) {
        lines.push(`    caption: "${escJS(page.bullets[0])}",`);
      }
      if (page.actLabel) lines.push(`    actLabel: "${page.actLabel}",`);
      break;
    }

    case "stat": {
      lines.push(`    type: "stat",`);
      // Try to extract the main stat number from bullets
      let stat = "";
      let label = page.slideTitle;
      let desc = "";
      for (const b of page.bullets) {
        const numMatch = b.match(/(\d+%|[+\-]\d+%)/);
        if (numMatch && !stat) stat = numMatch[1];
      }
      if (!stat) stat = "?";
      lines.push(`    stat: "${escJS(stat)}",`);
      lines.push(`    label: "${escJS(label)}",`);
      if (page.bullets.length > 0) {
        desc = page.bullets.join("\\n");
        lines.push(`    desc: "${escJS(desc)}",`);
      }
      lines.push(`    darkBg: true,`);
      if (page.actLabel) lines.push(`    actLabel: "${page.actLabel}",`);
      break;
    }

    case "quote": {
      lines.push(`    type: "quote",`);
      // Use the most prominent quote from bullets or title
      let quote = page.slideTitle;
      if (page.bullets.length > 0) {
        // Find the longest/most quote-like bullet
        const quoteBullets = page.bullets.filter(b => b.includes('\u201c') || b.includes('\u201d') || b.length > 15);
        if (quoteBullets.length > 0) quote = quoteBullets.join("\\n");
        else quote = page.bullets.join("\\n");
      }
      lines.push(`    quote: "${escJS(quote)}",`);
      if (page.actLabel) lines.push(`    actLabel: "${page.actLabel}",`);
      break;
    }

    case "keyPhrase": {
      lines.push(`    type: "keyPhrase",`);
      // Use title as phrase, bullets as sub
      lines.push(`    phrase: "${escJS(page.slideTitle)}",`);
      if (page.bullets.length > 0) {
        lines.push(`    sub: "${escJS(page.bullets.join("\\n"))}",`);
      }
      if (page.actLabel) lines.push(`    actLabel: "${page.actLabel}",`);
      break;
    }

    case "comparison": {
      lines.push(`    type: "comparison",`);
      lines.push(`    title: "${escJS(page.slideTitle)}",`);
      // Try to split bullets into left/right
      const half = Math.ceil(page.bullets.length / 2);
      const leftBullets = page.bullets.slice(0, half);
      const rightBullets = page.bullets.slice(half);
      lines.push(`    leftTitle: "左",`);
      lines.push(`    leftBody: "${escJS(leftBullets.join("\\n"))}",`);
      lines.push(`    rightTitle: "右",`);
      lines.push(`    rightBody: "${escJS(rightBullets.join("\\n"))}",`);
      if (page.actLabel) lines.push(`    actLabel: "${page.actLabel}",`);
      break;
    }

    case "threeCards": {
      lines.push(`    type: "threeCards",`);
      lines.push(`    title: "${escJS(page.slideTitle)}",`);
      // Generate cards from bullets
      const cards = page.bullets.slice(0, 3).map((b, i) => {
        const parts = b.split(/[：:]/);
        return { title: parts[0] || `卡片${i+1}`, body: parts.slice(1).join("：") || b };
      });
      lines.push(`    cards: [`);
      for (const c of cards) {
        lines.push(`      { title: "${escJS(c.title)}", body: "${escJS(c.body)}" },`);
      }
      lines.push(`    ],`);
      if (page.actLabel) lines.push(`    actLabel: "${page.actLabel}",`);
      break;
    }

    case "fourCards": {
      lines.push(`    type: "fourCards",`);
      lines.push(`    title: "${escJS(page.slideTitle)}",`);
      const cards = page.bullets.slice(0, 4).map((b, i) => {
        const parts = b.split(/[：:]/);
        return { title: parts[0] || `卡片${i+1}`, body: parts.slice(1).join("：") || b };
      });
      lines.push(`    cards: [`);
      for (const c of cards) {
        lines.push(`      { title: "${escJS(c.title)}", body: "${escJS(c.body)}" },`);
      }
      lines.push(`    ],`);
      if (page.actLabel) lines.push(`    actLabel: "${page.actLabel}",`);
      break;
    }

    default: {
      // content type (text-only or with diagram/image)
      const diag = getDiagram(page);
      lines.push(`    type: "content",`);
      lines.push(`    title: "${escJS(page.slideTitle)}",`);
      if (page.bullets.length > 0) {
        lines.push(`    body: "${escJS(page.bullets.join("\\n"))}",`);
      }
      if (diag) {
        lines.push(`    image: diagram("${escJS(diag)}"),`);
      }
      if (page.actLabel) lines.push(`    actLabel: "${page.actLabel}",`);
      break;
    }
  }

  // Notes (always add)
  if (page.notes) {
    lines.push(`    notes: "${escJS(page.notes)}",`);
  }

  lines.push("  },");
  return lines.join("\n");
}

// Main
const pages = parseSpecs();
console.error(`Parsed ${pages.length} pages`);

console.log("const slides = [");
console.log("");

let currentAct = "";
for (const page of pages) {
  // Section comments
  if (page.actLabel !== currentAct) {
    currentAct = page.actLabel;
    console.log(`  // ─────────────────────────────────────────────`);
    console.log(`  // ${currentAct || "序幕"}`);
    console.log(`  // ─────────────────────────────────────────────`);
  }

  console.log(`  // 页 ${page.pageNum}: ${page.rawTitle}`);
  console.log(generateSlide(page));
  console.log("");
}

console.log("];");
