#!/usr/bin/env python3
"""
Deepen slides with academic paper findings.
Targeted replacements in build_pptx_v5.js slides[] array.
"""
import re

FILE = "scripts/build_pptx_v5.js"

with open(FILE, "r") as f:
    text = f.read()

replacements = []

# ─── Page 9: 涌现 — Add Schaeffer 2023 "mirage" finding to notes ───
old_9 = 'notes: "这个小语言模型一开始确实是个智障。但有趣的事情发生了——\\"随着模型的参数越来越大，居然在某个临界点涌现出了智能。\\"注意这个\\"居然\\"——连设计者自己都没有预料到。这就像你在一粒一粒地堆沙子，堆到某一粒的时候，沙堆突然变成了一座沙堡。没有人设计过这座沙堡，它就是在量变中突然发生了质变。",'
new_9 = 'notes: "这个小语言模型一开始确实是个智障。但有趣的事情发生了——\\"随着模型的参数越来越大，居然在某个临界点涌现出了智能。\\"注意这个\\"居然\\"——连设计者自己都没有预料到。这就像你在一粒一粒地堆沙子，堆到某一粒的时候，沙堆突然变成了一座沙堡。没有人设计过这座沙堡，它就是在量变中突然发生了质变。但这里有一个关键的学术反转：NeurIPS 2023最佳论文（Schaeffer等人）证明了——所谓的\\"涌现\\"很可能是测量幻觉。用离散指标（如精确匹配）去测，就看到突变；换成连续指标（如交叉熵），能力增长其实是平滑的。换句话说，不是沙堆突然变成了沙堡，而是我们的尺子制造了这个错觉。",'
replacements.append((old_9, new_9))

# ─── Page 9: Add body with Schaeffer finding ───
old_9b = '    caption: "参数越来越大",'
new_9b = '    caption: "参数越来越大——但\\"涌现\\"也许是测量幻觉（Schaeffer et al., NeurIPS 2023 最佳论文）",'
replacements.append((old_9b, new_9b))

# ─── Page 36: Agent reliability — Add Kambhampati & WebArena data to notes ───
old_36 = '2025年的一项Agent基准研究把这个问题量化了：即使单步成功率高达95%，连续执行10次运行全部成功的概率也只有大约25%。这就是可靠性的乘法悲剧——每一层补丁都只有\\"大概率靠谱\\"，但层层相乘之后，整体可靠性断崖式下跌。",'
new_36 = '学术界已经量化了这个问题。亚利桑那州立大学Kambhampati团队（ICML 2024）发现：GPT-4在标准规划任务上的自主成功率只有12%。WebArena基准测试中，最好的GPT-4 Agent在真实网页任务上只有14%的成功率（人类78%）。即使单步成功率高达95%，连续执行10步全部成功的概率也只有60%——实测更低，因为错误会级联放大。这就是可靠性的乘法悲剧——每一层补丁都只有\\"大概率靠谱\\"，但层层相乘之后，整体可靠性断崖式下跌。",'
replacements.append((old_36, new_36))

# ─── Page 46: McKinsey stat — keep but strengthen desc ───
old_46_desc = '    desc: "88%的组织声称使用AI\\n6%真正创造价值\\n— McKinsey 2025全球调研",'
new_46_desc = '    desc: "88%的组织声称使用AI\\n6%真正创造可衡量价值\\n— McKinsey State of AI 2025\\n（39%报告任何EBIT影响）",'
replacements.append((old_46_desc, new_46_desc))

# ─── Page 47: Productivity paradox — Add Brynjolfsson finding ───
old_47_desc = '    desc: "主观感受：提升20%\\n客观测量：慢了19%\\n— 加州管理评论 2025",'
new_47_desc = '    desc: "主观感受：提升20%\\n客观测量：慢了19%\\n— California Management Review 2025\\n\\nNBER实证：生产力提升集中在低技能工作者\\n高技能工作 → 增益趋近于零",'
replacements.append((old_47_desc, new_47_desc))

# ─── Page 47: notes — Add Brynjolfsson/Noy & Zhang ───
old_47_notes = '为什么？因为节省下来的时间全部被审查AI的输出、调试AI的错误、验证AI的结果给吃掉了。你以为你在省时间，其实你在帮AI擦屁股。'
new_47_notes = '为什么？因为节省下来的时间全部被审查AI的输出、调试AI的错误、验证AI的结果给吃掉了。你以为你在省时间，其实你在帮AI擦屁股。MIT的Noy和Zhang在Science上的实证研究（2023）进一步揭示了一个残酷的分层效应：AI对低技能工作者帮助最大（+40%产出），对高技能工作者几乎没有提升——甚至可能让他们的输出质量下降，因为过度依赖AI建议会覆盖自身的专业判断。'
replacements.append((old_47_notes, new_47_notes))

# ─── Page 49: capability inversion — Add ARC-AGI data ───
old_49_body = '    body: "越\\"难\\"的任务 — AI做得越好\\n越\\"简单\\"的任务 — AI反而做不好\\n\\n能力倒挂：AI的\\"难\\"和人的\\"难\\"不是一回事",'
new_49_body = '    body: "越\\"难\\"的任务 — AI做得越好\\n越\\"简单\\"的任务 — AI反而做不好\\n\\nARC-AGI基准测试（Chollet）：\\nGPT-4o: 5% vs 人类: 73-77%\\n3岁小孩能做的模式识别，最强AI做不到\\n\\n能力倒挂：AI的\\"难\\"和人的\\"难\\"不是一回事",'
replacements.append((old_49_body, new_49_body))

# ─── Page 49: notes — Add ARC-AGI context ───
old_49_notes = '这种能力倒挂有一个学术名字——理解了它，你就理解了AI最深层的\\"智力缺陷\\"。",'
new_49_notes = 'Chollet的ARC-AGI基准测试量化了这个倒挂：GPT-4o在需要\\"流体智能\\"（即时推理新模式）的任务上只有5%的正确率，而人类平均73-77%。即便是花费每道题17美元算力的o3模型，仍然会在幼儿轻松完成的抽象推理上翻车。这是因为AI擅长的是\\"结晶智能\\"——海量训练数据中的模式匹配，而非真正的推理。理解了这一点，你就理解了AI最深层的\\"智力缺陷\\"。",'
replacements.append((old_49_notes, new_49_notes))

# ─── Page 53: impossibility theorem — Add Xu et al. exact citation ───
old_53_body = '    body: "五类不可消除问题：\\n上下文窗口 · 推理 · 幻觉 · 检索 · 多模态\\n\\n2025数学证明：幻觉与想象在数学上等价\\n消灭幻觉 = 消灭创造力\\n\\n不是暂时解决不了，是不可能被彻底消除",'
new_53_body = '    body: "五类不可消除问题：\\n上下文窗口 · 推理 · 幻觉 · 检索 · 多模态\\n\\nXu, Jain & Kankanhalli (2024, arXiv:2401.11817):\\n用可计算性理论证明：任何可计算LLM\\n在充当通用问题求解器时，必然产生幻觉\\n\\n幻觉不是bug，是数学上的必然\\n消灭幻觉 = 消灭创造力",'
replacements.append((old_53_body, new_53_body))

# ─── Page 53: notes — strengthen with paper details ───
old_53_notes = '而2025年一篇新的数学证明进一步加强了这个结论——三个独立数学领域的证明建立了\\"基本不可能定理\\"：模型要么产生幻觉，要么失去创造力。幻觉与想象在数学上是等价的。你消灭不了幻觉，除非你同时消灭模型的创造力。",'
new_53_notes = 'Xu、Jain和Kankanhalli在2024年的论文《Hallucination is Inevitable》用学习理论和可计算性理论给出了形式化证明：可计算函数的类不可能被任何单一可计算模型学完。这意味着任何通用LLM在遇到训练分布外的问题时，必然会产生幻觉——这和图灵的停机问题是同一类数学限制。另一篇独立研究（Banerjee等人, 2024）从哥德尔不完备定理的角度得出了相同结论。两条独立的数学路径，同一个终点：幻觉不可消除。",'
replacements.append((old_53_notes, new_53_notes))

# ─── Page 55: sycophancy — Add research to notes ───
old_55_notes = '只不过你更难发现了。从初级骗子变成了高级骗子——不是故意骗你，而是输出越来越流畅、越来越自信。能力越强，错误越自信。这才是AI发展中最危险的趋势。",'
new_55_notes = '只不过你更难发现了。学术界把这叫\\"谄媚效应\\"（sycophancy）——Sharma等人（2023）证明：经过RLHF训练的模型越强大，就越倾向于给出自信但错误的回答来迎合用户。Berglund等人（2023）发现了\\"逆转诅咒\\"：大模型在逻辑反转任务上的表现甚至比小模型更差，但说出答案时更加自信。从初级骗子变成了高级骗子——不是故意骗你，而是训练目标本身鼓励它表现得更自信。能力越强，错误越自信。这才是AI发展中最危险的趋势。",'
replacements.append((old_55_notes, new_55_notes))

# ─── Page 24: Agent — Add Kambhampati to notes ───
old_24_notes = '所谓智能体，就是一个打了八层补丁的提线木偶。",'
new_24_notes = '所谓智能体，就是一个打了八层补丁的提线木偶。亚利桑那州立大学的Kambhampati教授在ICML 2024的立场论文中给出了学术定论：\\"LLMs不能规划，但可以辅助规划\\"——它们最多是\\"通用近似知识源\\"（外部System 1），而非推理引擎。Agent的花哨外壳改变不了核心的本质。",'
replacements.append((old_24_notes, new_24_notes))

# ─── Page 76 area: Add Doshi & Hauser finding as new content in notes of page 76 ───
old_76_notes = '这是一个令人不安的推论。但请先别急着反驳——让它在你心里多待一会儿。",'
new_76_notes = '这不是哲学空想——Science Advances上Doshi和Hauser（2024）的实验证明了这个推论：用AI辅助写作的人，个人创造力提升了8.1%，但所有人的作品之间的相似度增加了10.7%。AI让每个人都变得更有创意，但让所有人变得更像彼此。当每个人都从同一个概率分布中采样时，\\"独创性\\"在数学上就必然收敛。这是一个令人不安的推论。但请先别急着反驳——让它在你心里多待一会儿。",'
replacements.append((old_76_notes, new_76_notes))

# ─── Page 75 comparison: Add Doshi data to body ───
old_75_left = '    leftBody: "向量空间中的点\\n数学上的优化\\n无限次重来",'
new_75_left = '    leftBody: "向量空间中的点\\n数学上的优化\\n无限次重来\\n\\n结果：集体相似度+10.7%",'
replacements.append((old_75_left, new_75_left))

old_75_right = '    rightBody: "从书架上抽一本\\n有限的时间精力\\n不可逆的选择",'
new_75_right = '    rightBody: "从书架上抽一本\\n有限的时间精力\\n不可逆的选择\\n\\n代价即意义",'
replacements.append((old_75_right, new_75_right))

# Apply all replacements
count = 0
for old, new in replacements:
    if old in text:
        text = text.replace(old, new)
        count += 1
    else:
        print(f"WARNING: Could not find match for replacement #{count+1}")
        # Show first 60 chars
        print(f"  Looking for: {old[:80]}...")

with open(FILE, "w") as f:
    f.write(text)

print(f"Applied {count}/{len(replacements)} replacements")
