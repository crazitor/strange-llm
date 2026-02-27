# PPTX生成 (PPTX Build)

## 目标 (Goal)

将PPT内容方案转化为实际的 .pptx 文件，使用 python-pptx 库编程生成。

## 输入 (Input)

- `output/slides/slide_deck.md`（每页PPT内容描述）
- `output/visuals/layout_guide.md`（布局指导）
- `assets/diagrams/rendered/*.png`（图表文件）

## 输出 (Output)

- `output/presentation.pptx`（最终PPT文件）
- `output/pptx_build_log.md`（构建日志）

## 步骤 (Steps)

1. 解析 slide_deck.md，提取每页的结构化内容
2. 加载或创建PPT模板（布局、配色、字体）
3. 逐页生成幻灯片：标题、正文、图表、注释
4. 插入渲染好的图表图片
5. 设置转场效果和动画（如需要）
6. 保存 .pptx 文件
7. 记录构建日志

## 质量标准 (Quality Criteria)

- .pptx 文件可在 PowerPoint/Keynote/WPS 中正常打开
- 图表清晰，不模糊、不变形
- 字体统一，排版规范
- 文件大小合理（< 50MB）

## 失败处理 (Failure Handling)

- **python-pptx未安装**：提示安装命令 `pip install python-pptx`
- **图片文件缺失**：使用占位符，记录缺失项
- **字体不可用**：回退到系统默认字体，记录警告
- **文件过大**：压缩图片，减少嵌入资源
