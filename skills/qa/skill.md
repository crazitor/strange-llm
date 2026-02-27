# QA与交付 (QA & Delivery)

## 目标 (Goal)

对最终产出进行全面质量检查，确保交付物满足所有质量标准。

## 输入 (Input)

- `output/presentation.pptx`（PPT文件）
- `output/slides/script.md`（讲稿）
- `archive/indexed_subtitles/`（素材ID库）
- 所有中间产出物

## 输出 (Output)

- `output/qa/qa_report.md`（QA报告）
- `output/qa/checklist.md`（检查清单）
- `output/delivery/`（最终交付包）

## 步骤 (Steps)

1. **覆盖率检查**：运行 coverage 脚本，验证素材引用完整性
2. **逻辑一致性**：检查讲稿论证链的完整性和一致性
3. **视觉质量**：审查PPT的排版、配色、图表清晰度
4. **讲稿质量**：检查口语化程度、节奏标注、时长预估
5. **文件完整性**：确认所有交付文件存在且可打开
6. **生成QA报告**：汇总所有检查结果
7. **打包交付**：将通过QA的文件组织到交付目录

## 质量标准 (Quality Criteria)

- 覆盖率 ≥ 95%
- 无事实性错误
- PPT在至少2个软件中可正常打开
- 讲稿总时长与目标时长偏差 ≤ 10%
- QA报告中无HIGH优先级的未解决问题

## 失败处理 (Failure Handling)

- **覆盖率不达标**：退回叙事设计阶段补充
- **发现事实错误**：标记为 BLOCKER，退回纠偏阶段
- **PPT兼容性问题**：调整模板设置，重新生成
- **时长偏差过大**：退回讲稿编写阶段调整
