# 覆盖率审计 (Coverage Audit)

## 目标 (Goal)

确保每个字幕行ID在目标文档中被正确引用，追踪素材的使用情况。

## 输入 (Input)

- `archive/indexed_subtitles/V{n}_indexed.md`（所有ID的权威来源）
- 目标文档文件路径（任意 .md 文件）

## 输出 (Output)

- 覆盖率报告（支持 table / json / summary 三种格式）
- 退出码：0 = 全部覆盖，1 = 存在缺失

## 步骤 (Steps)

1. 从 `archive/indexed_subtitles/` 读取所有 `V{n}_indexed.md` 文件
2. 解析Markdown表格，提取所有ID列表
3. 读取目标文件全文
4. 逐个ID在目标文件中搜索
5. 统计覆盖率，按视频分组汇总
6. 按指定格式输出报告

## 质量标准 (Quality Criteria)

- ID提取必须与 indexed_subtitles 中的ID完全一致
- 搜索采用精确字符串匹配，避免误报
- summary格式必须包含按视频分组的细分数据
- 脚本可通过 `python3 scripts/check_coverage.py <file> --format <fmt>` 独立运行

## 失败处理 (Failure Handling)

- **indexed_subtitles目录不存在**：输出错误信息，提示先运行素材摄取
- **目标文件不存在**：输出文件未找到错误
- **无ID被提取到**：输出警告，提示检查indexed文件格式
