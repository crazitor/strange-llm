---
title: "GPT-4 and professional benchmarks: the wrong answer to the wrong question"
author: "Arvind Narayanan & Sayash Kapoor"
date: ""
source: "substack_aisnakeoil"
url: "https://www.normaltech.ai/p/gpt-4-and-professional-benchmarks"
---

OpenAI didn’t release much information about GPT-4 — not even the size of the model — but [heavily emphasized](https://cdn.openai.com/papers/gpt-4.pdf) its performance on professional licensing exams and other standardized tests. For instance, GPT-4 reportedly scored in the 90th percentile on the bar exam. So there’s been much speculation about what this means for professionals such as lawyers.

We don’t know the answer, but we hope to inject some reality into the conversation. OpenAI may have violated the cardinal rule of machine learning: don’t test on your training data. Setting that aside, there’s a bigger problem. The manner in which language models solve problems is different from how people do it, so these results tell us very little about how a bot will do when confronted with the real-life problems that professionals face. It’s not like a lawyer’s job is to answer bar exam questions all day.

**Problem 1: training data contamination**

To benchmark GPT-4’s coding ability, OpenAI evaluated it on problems from Codeforces, a website that hosts coding competitions. Surprisingly, Horace He pointed out that GPT-4 [solved](https://twitter.com/cHHillee/status/1635790330854526981) 10/10 pre-2021 problems and 0/10 recent problems in the easy category. The training data cutoff for GPT-4 is September 2021. This strongly suggests that the model is able to memorize solutions from its training set — or at least partly memorize them, enough that it can fill in what it can’t recall.

As further evidence for this hypothesis, we tested it on Codeforces problems from different times in 2021. We found that it could regularly solve problems in the easy category before September 5, but none of the problems after September 12.

In fact, we can definitively show that it has memorized problems in its training set: when prompted with the title of a Codeforces problem, GPT-4 includes a link to the exact contest where the problem appears (and the round number is almost correct: it is off by one). Note that GPT-4 [cannot access the Internet](https://simonwillison.net/2023/Mar/10/chatgpt-internet-access/), so memorization is the only explanation.

[](https://substackcdn.com/image/fetch/$s_!AzEq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3a115f56-76e9-480a-8ee5-c95bb808e9da_1600x417.png)_GPT-4 memorizes Codeforces problems before its training cutoff date._

The Codeforces results in the paper aren’t affected by this, as OpenAI used recent problems (and sure enough, GPT-4 performed very poorly). For the benchmarks other than coding, we don’t know of a clean way to separate the questions by time period, so we think it is unlikely that OpenAI was able to avoid contamination.[1](https://www.normaltech.ai/p/gpt-4-and-professional-benchmarks#footnote-1-109659870) But for the same reason, we can’t do an experiment to test how performance varies by date.

Still, we can look for telltale signs. Another symptom of memorization is that GPT is highly sensitive to the phrasing of the question. Melanie Mitchell gives an [example](https://aiguide.substack.com/p/did-chatgpt-really-pass-graduate) of an MBA test question where changing some details in a way that wouldn’t fool a person is enough to fool ChatGPT (running GPT-3.5). A more elaborate experiment along these lines would be valuable.

Because of OpenAI’s lack of transparency, we can’t answer the contamination question with certainty. But what’s certain is that OpenAI’s method to detect contamination is superficial and sloppy:

> “We measure cross-contamination between our evaluation dataset and the pre-training data using substring match. Both evaluation and training data are processed by removing all spaces and symbols, keeping only characters (including numbers). For each evaluation example, we randomly select three substrings of 50 characters (or use the entire example if it’s less than 50 characters). A match is identified if any of the three sampled evaluation substrings is a substring of the processed training example. This yields a list of contaminated examples. We discard these and rerun to get uncontaminated scores.”

This is a brittle method. If a test problem were present in the training set with names and numbers changed, it wouldn’t be detected. Less flaky methods are readily available, such as [embedding distances](https://twitter.com/mmitchell_ai/status/1637533337026981888).

If OpenAI were to use a distance-based method, how similar is too similar? There is no objective answer to this question. So even something as seemingly straightforward as performance on a multiple-choice standardized test is fraught with subjective decisions. 

But we can get some clarity by asking what OpenAI is trying to measure using these exams. If the goal is to predict how the language model will do on real-world tasks, there’s a problem. In a sense, any two bar exam questions or medical exam questions are more similar to each other than they are to the tasks that professionals do in the real world, because they are drawn from such a constrained space. So it’s possible that the inclusion of _any_ exam questions in the training corpus results in an inflated estimate of real-world usefulness.

Framing the question in terms of real-world usefulness highlights another, deeper problem.

**Problem 2: professional exams aren’t a valid way to compare human capabilities with bots**

Memorization is a spectrum. Even if a language model hasn’t seen an exact problem on a training set, it has inevitably seen examples that are pretty close, simply because of the size of the training corpus. That means it can get away with a much shallower level of reasoning. So the benchmark results don’t give us evidence that language models are acquiring the kind of in-depth reasoning skills that human test-takers need — skills that they then apply in the real world. 

In some real-world tasks, shallow reasoning may be sufficient, but not always. The world is constantly changing, so if a bot is asked to analyze the legal consequences of a new technology or a new judicial decision, it doesn’t have much to draw upon. In short, as Emily Bender points out, tests designed for humans lack [construct validity](https://twitter.com/emilymbender/status/1636090914346274816) when applied to bots.

On top of this, professional exams, especially the bar exam, notoriously [overemphasize](https://scholarship.law.pitt.edu/cgi/viewcontent.cgi?article=1064&context=fac_articles) subject-matter knowledge and underemphasize real-world skills, which are far harder to measure in a standardized, computer-administered way. In other words, not only do these exams emphasize the wrong thing, they overemphasize precisely the thing that language models are good at.

Benchmarks are already wildly overused in AI for comparing different models. They have been [heavily](https://twitter.com/ChristophMolnar/status/1485549716268109824?s=20) [criticized](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/file/084b6fbb10729ed4da8c3d3f5a3ae7c9-Paper-round2.pdf) for collapsing a multidimensional evaluation into a single number. When used as a way to compare humans and bots, what results is misinformation. It is unfortunate that OpenAI chose to use these types of tests so heavily in their evaluation of GPT-4, coupled with inadequate attempts to address contamination.

**There are better ways to assess impact on professions**

People have Internet access during their jobs, but not during standardized tests. So, if language models can match the performance of professionals who have Internet access, it would be a somewhat better test of whether they are practically useful.

But that’s still the wrong question. Instead of standalone benchmarks, we should measure how well language models can accomplish any of the real-world tasks that professionals must do. For example, in academia, we often encounter papers filled with jargon from fields we’re not familiar with; it would be useful if ChatGPT could accurately summarize such a paper in a more accessible way. Some people have even been anecdotally testing if these tools can do peer review. But even here, it’s easy to fall into the [trap](https://twitter.com/random_walker/status/1637507156659548160) of testing on the training data.[2](https://www.normaltech.ai/p/gpt-4-and-professional-benchmarks#footnote-2-109659870)

Studies that frame the question as a comparison between a professional and a bot are misguided: the idea that ChatGPT can replace professionals remains far-fetched. Just one of the 270 jobs in the 1950 census has been [eliminated](https://twitter.com/emollick/status/1635787047502852097) by automation: elevator operator. Instead, we need studies that actually evaluate professionals using the help of AI tools to do their jobs. [Two early studies](https://twitter.com/emollick/status/1631397931604488194) are promising: one looks at GitHub copilot for coding and the other looks at ChatGPT for writing assistance. 

At this stage, we need qualitative studies more than quantitative ones, because these tools are so new that we don’t even know the right quantitative questions to ask. For example, Scott Guthrie of Microsoft reports the eye-catching number that [40%](https://www.microsoft.com/en-us/Investor/events/FY-2023/Morgan-Stanley-TMT-Conference) of the code checked in by GitHub Copilot users is AI-generated and unmodified. But any programmer will tell you that especially in enterprise applications, a large percentage of code consists of templates and other mundane logic that we usually copy-paste. If this is the part that Copilot is automating, the productivity improvement would be negligible. To be clear, we’re not saying that Copilot is useless, just that metrics are meaningless without a qualitative understanding of how professionals use AI. Besides, the [primary benefit](https://twitter.com/random_walker/status/1636050310019022848) of AI-assisted coding might not even be the productivity improvement.

**Summary**

The figure summarizes this post and explains why and how we need to move away from the kind of metrics reported by OpenAI.

[](https://substackcdn.com/image/fetch/$s_!ISBS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea565520-6154-4e04-8fed-49982accbf0e_1600x822.png)

GPT-4 is genuinely exciting and there are many ways in which it can solve pain points for professionals: for example, by [automating](https://twitter.com/random_walker/status/1636039756864712706) mundane and low-stakes yet laborious tasks. For now, it might be better to focus on achieving such benefits and on mitigating the many risks of language models.

**Notes and further reading**

  * [ChatGPT passing USMLE shines a spotlight on the flaws of medical education](https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000205), a paper by Amarachi B. Mbakwe and others. 

  * Qualitative studies are important across ML modeling stages, not just during evaluation. Orestis Papakyriakopoulos and others [argue](https://arxiv.org/pdf/2112.03784.pdf) that qualitative methods can uncover areas of improvement in problem formulation, data collection, and translating ML models to the real world. But they are still overshadowed by quantitative methods in the ML community.

  * In our work on [leakage](https://reproducible.cs.princeton.edu) in scientific research that uses ML, we found that it can be notoriously hard to avoid leakage in settings of scientific interest. Leakage (which is roughly the same as contamination in this post) is more of an open research problem than a bug that can be easily fixed.

  * To benchmark language models across multiple metrics, Percy Liang and others introduced [HELM](https://arxiv.org/abs/2211.09110) (holistic evaluation of language models). HELM measures LLMs on metrics such as accuracy, calibration, and toxicity, among many others. Still, if LLMs are trained on the evaluation sets of such benchmarks, performance comparisons are meaningless. While the authors of HELM opted out their evaluation sets by contacting OpenAI, others could still inadvertently [contaminate](https://twitter.com/percyliang/status/1619594326585262082?s=20) the models, such as by hosting a copy of the evaluation data.

  * **Update:** Ernest Davis has [two](https://arxiv.org/abs/1411.1629) [articles](https://www.oecd-ilibrary.org/education/ai-and-the-future-of-skills-volume-1_e182dd0d-en) on the flaws of using tests designed for humans to measure AI tools. He recommends being mindful of the difference between humans and AI tools and focusing on understanding strengths and weaknesses of AI tools rather than looking for a single score to evaluate AI performance.

  * Microsoft and OpenAI released a [paper](https://www.microsoft.com/en-us/research/uploads/prod/2023/03/GPT-4_medical_benchmarks.pdf) on the capabilities of GPT-4 on the USMLE exam for medical practitioners. The paper [addresses](https://twitter.com/random_walker/status/1638582337985470465) several of the concerns we raise: GPT-4 is tested on paywalled questions, making it less likely that memorization can occur. The paper also acknowledges the gap between benchmarks and real-world clinical utility. But it lacks real-world evaluation.




[1](https://www.normaltech.ai/p/gpt-4-and-professional-benchmarks#footnote-anchor-1-109659870)

The only way to ensure this would be to create fresh exams each time a language model is benchmarked, or by keeping benchmark evaluation sets [entirely private](https://twitter.com/fchollet/status/1636054908490375171). OpenAI used publicly available exams for most of its benchmarks. The only exception was the bar exam. While details about how the exam was created are scant, OpenAI does mention that they took help from collaborators from Casetext and Stanford Codex, which implies they conducted a fresh exam.

[2](https://www.normaltech.ai/p/gpt-4-and-professional-benchmarks#footnote-anchor-2-109659870)

Even if language models could do passable peer review, it doesn’t mean it’s ethically acceptable or even practically useful: papers could be adversarially optimized to get glowing reviews from models regardless of the substance.

We inadvertently omitted the footnotes in the newsletter version of this blog post due to a copy-paste error.
