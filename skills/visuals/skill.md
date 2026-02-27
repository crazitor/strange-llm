# 视觉导演 (Visuals)

## 目标 (Goal)

设计演讲的视觉呈现方案，包括图表、关键帧选取和视觉隐喻，让抽象概念可视化。

## 输入 (Input)

- `output/narrative/` 叙事大纲和论点树
- `archive/indexed_subtitles/` 需要可视化的关键概念
- `derived/scenes/frames/` 视频关键帧（如有）

## 输出 (Output)

- `output/visuals/visual_plan.md`（视觉方案总览）
- `assets/diagrams/sources/*.mmd`（Mermaid图表源文件）
- `assets/diagrams/rendered/*.png`（渲染后的图表）
- `output/visuals/layout_guide.md`（PPT布局指导）

## 步骤 (Steps)

1. 分析叙事结构，识别需要视觉支撑的节点
2. 为每个节点设计视觉方案（图表/关键帧/隐喻）
3. 编写Mermaid图表源码，保存到 `assets/diagrams/sources/`
4. 渲染Mermaid图表为PNG
5. 从视频中选取关键帧（如需要）
6. 设计PPT布局指导（配色、字体、排版规则）

## 质量标准 (Quality Criteria)

- 每个核心论点至少有一个视觉元素支撑
- Mermaid图表语法正确，可独立渲染
- 视觉风格统一，配色方案一致
- 图表简洁清晰，避免信息过载

## 失败处理 (Failure Handling)

- **Mermaid渲染失败**：检查语法，简化图表结构
- **关键帧质量不足**：使用替代视觉方案（图标、图表等）
- **视觉风格不一致**：制定并强制执行设计规范文档
