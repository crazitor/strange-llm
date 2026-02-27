# 纠偏与深度思考 (Deep Think)

## 目标 (Goal)

对已有叙事进行批判性审查和纠偏，发现逻辑漏洞、过度简化和因果谬误。

## 输入 (Input)

- `output/narrative/` 下的叙事设计产出
- `archive/indexed_subtitles/` 原始素材
- 当前演讲领域的背景知识

## 输出 (Output)

- `output/deep_think/review_report.md`（纠偏报告）
- `output/deep_think/revision_suggestions.md`（修订建议）
- `output/deep_think/bias_checklist.md`（偏见检查清单）

## 步骤 (Steps)

1. 逐条审查核心主张：是否有充分证据支撑？是否存在逻辑跳跃？
2. 检查因果链：区分相关性和因果性，识别混淆变量
3. 检查过度简化：复杂问题是否被不当简化？是否遗漏重要nuance？
4. 检查偏见：确认性偏见、幸存者偏差、近因偏差等
5. 交叉验证：素材中的事实性陈述是否准确？
6. 生成纠偏报告和修订建议

## 质量标准 (Quality Criteria)

- 每个核心主张至少经过3个角度的质疑
- 纠偏报告中的每条意见必须有具体依据
- 修订建议必须可操作，指向具体的叙事节点
- 不能只找问题，也要确认合理之处

## 失败处理 (Failure Handling)

- **发现事实性错误**：标记为HIGH优先级，提供正确信息源
- **逻辑漏洞无法修补**：建议删除或重构该论证路径
- **过度纠偏导致叙事瓦解**：评估核心主张是否需要根本调整
