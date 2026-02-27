# PPT+讲稿 (Slides & Script)

## 目标 (Goal)

将叙事设计转化为具体的PPT页面内容和配套讲稿，确保视觉和口述的协同。

## 输入 (Input)

- `output/narrative/` 叙事大纲和素材映射表
- `output/visuals/` 视觉方案和布局指导
- `assets/diagrams/rendered/` 渲染好的图表

## 输出 (Output)

- `output/slides/slide_deck.md`（每页PPT的内容描述）
- `output/slides/script.md`（讲稿全文，标注时间和页码对应）
- `output/slides/transitions.md`（转场说明）

## 步骤 (Steps)

1. 根据叙事大纲拆分为PPT页面（每页一个核心信息）
2. 为每页设计标题、要点、视觉元素
3. 编写对应的讲稿段落
4. 设计页面间的转场逻辑
5. 估算每页讲述时长，确保总时长符合要求
6. 标注素材ID引用，确保可追溯

## 质量标准 (Quality Criteria)

- 每页PPT只传递一个核心信息
- 讲稿与PPT内容互补而非重复
- 每页预估时长标注，总时长在目标范围内
- 素材ID在讲稿中有明确引用标记

## 失败处理 (Failure Handling)

- **页数过多**：合并低信息密度的页面
- **讲稿与PPT脱节**：重新对齐叙事结构和视觉设计
- **时长超标**：标记可删减的内容，提供精简方案
