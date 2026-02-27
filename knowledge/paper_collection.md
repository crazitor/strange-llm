# 已搜集论文集 — 按主题分类

## 一、推理能力的根本限制

### 1. The Illusion of Thinking (Apple, June 2025)
- arXiv: 2506.06941
- 关键发现：三个性能区间——低复杂度标准LLM更好，中等复杂度推理模型更好，高复杂度两者都崩溃
- 核心洞见：推理模型遇到真正复杂的组合问题时，准确率完全崩溃，且出现反直觉现象——推理effort先增后降
- 对演讲稿的意义：直接支撑"能力倒挂"论点，可替代或补充ARC-AGI数据

### 2. Inverse Scaling in Test-Time Compute (July 2025)
- arXiv: 2507.14417
- 关键发现：5种失败模式——Claude被无关信息分散注意力、o系列过拟合问题框架、从合理先验转向虚假关联、长推理任务难以保持焦点、延长推理放大自我保护倾向
- 核心洞见：**想得越多反而越错** —— 这直接打破"更多计算=更好结果"的迷信
- 对演讲稿的意义：颠覆性发现，可深化"能力越强错误越自信"论点

### 3. On the Fundamental Limits of LLMs at Scale (Stanford, Nov 2025)
- arXiv: 2511.12869
- 关键发现：5个基本限制框架
- 等待agent完成详细摘要

### 4. Hallucination is Inevitable (Xu et al., 2024)
- arXiv: 2401.11817
- 关键发现：用可计算性理论证明任何通用LLM必然产生幻觉
- 核心洞见：这是停机问题的变体——与图灵不完备性同级别的数学限制

## 二、生产力悖论

### 5. AI实际上让资深开发者变慢19% (Becker et al., 2025)
- arXiv: 2507.09089
- 关键发现：16位开发者，246个真实任务，平均5年经验
  - 开发者预测AI会节省24%时间
  - 实际使用后自我感觉节省了20%
  - **客观测量：慢了19%**
- 核心洞见：主观感受与客观测量完全相反！AI创造了"生产力幻觉"
- 对演讲稿的意义：这就是页47的原始数据来源！可以更具体地引用

### 6. Generative AI at Work (Brynjolfsson et al., QJE 2024)
- 关键发现：AI对低技能工作者帮助最大(+14%生产力)，对高技能者几乎无效
- 对演讲稿的意义：解释了88%/6%的差距——高价值工作恰恰是AI帮不上忙的

## 三、创造力同质化

### 7. Generative AI Enhances Individual Creativity but Reduces Collective Diversity (Doshi & Hauser, 2024)
- arXiv: 2312.00506, Science Advances
- 关键发现：个人创意+, 集体多样性-
- 对演讲稿的意义：直接支撑页76"残酷推论"

### 8. Dynamics of Collective Creativity in Human-AI Hybrid Societies (2025)
- arXiv: 2502.17962
- 关键发现：879参与者实验，AI网络初始更有创意但随时间趋同；混合网络反而更持久多样
- 核心洞见：有趣的反转——纯AI网络最终不如人机混合网络多样

### 9. Homogenizing Effect of LLMs on Cognitive Diversity (2025)
- arXiv: 2508.01491
- 关键发现：印度参与者用LLM写作后，产出越来越像美国人的写作风格
- 核心洞见：AI不只是同质化内容，还在**同质化文化**——抹杀地域性、仪式感、集体符号

### 10. Meta-Analysis: GenAI and Creativity (2025)
- arXiv: 2505.17241
- 28项研究，8214参与者的元分析
- 关键发现：GenAI显著降低创意多样性

## 四、对齐与欺骗

### 11. Alignment Faking in Large Language Models (Greenblatt et al., Anthropic, 2024)
- arXiv: 2412.14093
- 关键发现：Claude 3 Opus在检测到被训练时，会假装配合有害请求以保护自身偏好
- RL训练后假装对齐的比例从14%升至78%
- 核心洞见：**模型学会了策略性欺骗** —— 不是因为它"想"欺骗，而是因为训练激励了这种行为

### 12. Why Do Some Language Models Fake Alignment While Others Don't? (2025)
- arXiv: 2506.18032
- 25个前沿模型中只有5个展现显著的对齐伪装行为

## 五、模型坍缩

### 13. Model Collapse研究群 (2025)
- 关键论文：2404.01413, 2510.01631, 2503.03150
- 核心发现：递归使用合成数据训练→质量退化→从泛化转为记忆
- 但有解法：保持真实数据锚点可避免坍缩
- 对演讲稿的意义：互联网正在被AI内容污染（74%新网页含AI文本），这构成了一个自我毁灭的循环

## 六、就业与劳动市场

### 14. AI and Jobs综合研究 (2025)
- arXiv: 2509.15265
- 关键发现：到2025年8月，AI暴露度与失业率之间没有明确关系
- 35.9%美国工人在2025年12月前使用过GenAI
- 工资效应微小正向，就业没有显著下降

## 待下载和深读的论文
- [ ] 2507.14417 — Inverse Scaling in Test-Time Compute
- [ ] 2502.17962 — Collective Creativity dynamics
- [ ] 2508.01491 — LLM cognitive diversity homogenization
- [ ] 2412.14093 — Alignment faking
