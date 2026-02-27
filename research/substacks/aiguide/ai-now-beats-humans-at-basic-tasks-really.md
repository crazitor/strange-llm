---
title: "\"AI now beats humans at basic tasks\": Really?"
author: "Melanie Mitchell"
date: ""
source: "substack_aiguide"
url: "https://aiguide.substack.com/p/ai-now-beats-humans-at-basic-tasks"
---

Two weeks ago, _Nature_ , one of the world’s most prestigious journals, had [this jarring headline](https://www.nature.com/articles/d41586-024-01087-4):

[](https://substackcdn.com/image/fetch/$s_!ALbt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc002a48f-da74-4cbe-913f-664f5185709e_1273x338.png)

The article explained this further:   
  
“Artificial intelligence (AI) systems, such as the chatbot ChatGPT, have become so advanced that they now very nearly match or exceed human performance in tasks including reading comprehension, image classification and competition-level mathematics, according to a new report”.[1](https://aiguide.substack.com/p/ai-now-beats-humans-at-basic-tasks#footnote-1-144254377)  
  
 _Nature_ included this graph to back up their claim:

[](https://substackcdn.com/image/fetch/$s_!PI2t!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3537e1b2-8648-4f09-9f3e-0ff349c14708_1410x946.png)

It’s amazing to see the progress of AI over the last few years, but the claim that “AI now beats humans on basic tasks” has to be taken with a large grain of salt.  
  
The reason is that this claim is based on performance of AI systems on particular benchmarks. The benchmarks are labeled as testing “Image Classification”, “Reading Comprehension”, “Visual Commonsense Reasoning”, “General Language Understanding”, and so on. And AI systems have nearly matched or exceeded humans on all these benchmarks.  
  
But let me repeat an important mantra:  
  
**AI surpassing humans on a benchmark that is named after a general ability is not the same as AI surpassing humans on that general ability.  
**  
For example, just because a benchmark has “reading comprehension” in its name doesn’t mean that it tests general reading comprehension.  
  
Why is this the case?   
  
There are at least four reasons that AI performance on a benchmark can be misleading.   
  
1\. **Data contamination:** The questions (and answers) from a given benchmark might have been part of the training data for the AI system. OpenAI, for example, has not released any information about the training data of their most advanced models, so we can’t check whether or not this is the case.   
  
2\. **Over-reliance on training data:** The system might not have been trained on the benchmark itself, but on similar items that require similar patterns of reasoning, and the system might be relying on such patterns to solve benchmark items rather than using more general abstract reasoning. Multiple studies have shown that LLMs maybe rely on such “[approximate retrieval](https://cacm.acm.org/blogcacm/can-llms-really-reason-and-plan/)“ methods to solve problems.   
  
3\. **Shortcut learning:** The AI system might be, in some cases, relying on spurious correlations or “shortcuts” in test items. As a particularly blatant case of this, [one study found](https://www.sciencedirect.com/science/article/pii/S0022202X18322930) that an AI system which had successfully classified malignant skin cancers from photographs was using the presence of a ruler in the images as an important cue (photos of nonmalignant tumors were less likely to include rulers). Another [study showed](https://arxiv.org/abs/1907.07355) that a system attained high performance on a “natural language inference” benchmark by learning that certain keywords were (unintentionally) correlated with correct answers. Many examples of such shortcut learning have been described in the machine learning literature, and it’s likely that large language models have unprecedented ability to discover subtle patterns of association in language that can predict correct answers in benchmarks without requiring the kind of abstract reasoning that humans are more likely to use.   
  
4\. **Test validity:** performance on such benchmark might not correlate with performance in the real world, in the same way it does for humans.  
  
These issues, among others, have led many researchers to share the sentiment that “[evaluation for many natural language understanding tasks is broken](https://arxiv.org/abs/2104.02145).”   
  
AI has made astounding progress, but the assumption that the _Nature_ headline makes is not correct. While AI systems beat humans on many benchmarks, we cannot conclude that “AI now beats humans at basic tasks” more generally. Again and again, it’s been shown that AI performance on benchmarks is not necessarily a good predictor for AI performance in the real world.  
  
In [previous writing](https://arxiv.org/abs/2104.12871) I’ve noted that giving specific benchmarks the names of general abilities—”reading comprehension”, “commonsense reasoning”, “image classification”—is a form of “[wishful mnemonic](https://dl.acm.org/doi/pdf/10.1145/1045339.1045340)”: This is what the dataset creators _hope_ their dataset tests, but that hope does not always translate into reality.   
  
Nature’s headline notes that “new benchmarks are needed.” This is true, but what’s really needed is better scientific methods for evaluation, ones that control for shortcuts, that test robustness over variations on both the form of test items and on the underlying concepts being assessed, along with other ways to assess the mechanisms by which machines are performing tasks. I have [written about this](https://www.science.org/doi/10.1126/science.adj5957), as have cognitive scientists [Michael Frank](https://osf.io/preprints/psyarxiv/uacjm/download), [Anna Ivanova](https://arxiv.org/abs/2312.01276v1), and [Raphaël Millière](https://iai.tv/articles/the-turing-tests-of-today-are-mistaken-auid-2790?_auid=2020), among others.   
  
I hope that _Nature_ and other media that report on AI benchmark results will learn the mantra: **AI surpassing humans on a benchmark that is named after a general ability is not the same as AI surpassing humans on that general ability.**  
  


[1](https://aiguide.substack.com/p/ai-now-beats-humans-at-basic-tasks#footnote-anchor-1-144254377)

The report referenced here is the recently released [2024 AI Index](https://aiindex.stanford.edu/), a report from Stanford university that provides an annual data assessing advancements in AI.
