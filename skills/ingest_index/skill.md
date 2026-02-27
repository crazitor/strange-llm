# 素材摄取与索引 (Ingest & Index)

## 目标 (Goal)

将原始视频字幕转化为带稳定ID的索引化素材库，建立可追溯的证据底座。

## 输入 (Input)

- `docs/` 下的6个字幕文件（格式：`MM:SS 文本`，空行分隔）
- `docs/` 下的6个视频文件（.mp4）
- 视频ID映射表（V1-V6）

## 输出 (Output)

- `archive/indexed_subtitles/V{n}_indexed.md` × 6（Markdown表格：ID / Timestamp / Text）
- `archive/raw_appendix.md`（按V1-V6顺序拼接的完整原文）
- `derived/timeline/` 下的统一时间轴数据（后续阶段）

## 步骤 (Steps)

1. 扫描 `docs/` 目录，通过关键词匹配定位6个字幕文件
2. 逐文件读取，跳过空行，解析 `{timestamp} {text}` 格式
3. 为每个非空行分配稳定ID：`V{n}-{MM:SS}-L{line_no}`（三位补零）
4. 输出为Markdown表格，保存到 `archive/indexed_subtitles/`
5. 按V1-V6顺序拼接原文生成 `raw_appendix.md`
6. 运行 `scripts/check_coverage.py` 验证100%覆盖率

## 质量标准 (Quality Criteria)

- 每个indexed文件的行数 = 原字幕非空行数（零偏差）
- 不去重、不合并、不改写原文
- ID格式严格一致，全局唯一
- coverage检查 raw_appendix.md → 100%

## 失败处理 (Failure Handling)

- **字幕文件未找到**：输出错误日志，列出缺失文件名，中止
- **时间戳格式异常**：记录异常行，标记为 `PARSE_ERROR`，继续处理
- **覆盖率 < 100%**：输出缺失ID列表，排查raw_appendix生成逻辑
