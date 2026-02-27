---
title: "Reasoning Models Sometimes Output Illegible Chains of Thought"
author: "Jozdien"
date: "2025-11-24"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/GKyyYCs8n2goDcAe2/reasoning-models-sometimes-output-illegible-chains-of"
score: 83
votes: 30
---

TL;DR: Models trained with outcome-based RL sometimes have reasoning traces that look very weird. In [this paper](https://arxiv.org/abs/2510.27338), I evaluate 14 models and find that many of them often generate pretty illegible CoTs. I show that models seem to find this illegible text useful, with a model’s accuracy dropping heavily when given only the legible parts of its CoT, and that legibility goes down when answering harder questions. However, when sampling many responses to the same questions, I find there’s no real correlation between illegible reasoning and performance. From these results (and prior work), I think it’s likely RL induces meaningful illegible reasoning, but that it may not be significantly more effective than legible reasoning.

[Paper](https://arxiv.org/abs/2510.27338) | [Tweet thread](https://x.com/jozdien/status/1993022885829787838) | [Streamlit](https://cot-legibility.streamlit.app/) | [Code](https://github.com/Jozdien/cot_legibility)![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/66196ee40cb58f07ebf519e009425431240f1891f92d117d.png)

Introduction
============

Reasoning models are LLMs that have been trained with RLVR (Reinforcement Learning from Verifiable Rewards), often to use extended reasoning in chain-of-thought to solve tasks. This could be pretty beneficial: if this reasoning is legible and faithful, then monitoring it would be very useful. There’s [a](https://arxiv.org/abs/2305.04388) [lot](https://arxiv.org/abs/2501.08156v5) [of](https://www.anthropic.com/research/reasoning-models-dont-say-think) [prior](https://arxiv.org/abs/2507.05246) [work](https://www.lesswrong.com/posts/QYAfjdujzRv8hx6xo/unfaithful-reasoning-can-fool-chain-of-thought-monitoring) [on](https://www.lesswrong.com/posts/HuoyYQ6mFhS5pfZ4G/paper-output-supervision-can-obfuscate-the-cot) [faithfulness](https://www.lesswrong.com/posts/me7wFrkEtMbkzXGJt/race-and-gender-bias-as-an-example-of-unfaithful-chain-of), but [very little](https://arxiv.org/abs/2407.13692) on legibility—which makes sense, until [recently](https://www.arxiv.org/abs/2509.15541) there haven’t been models with meaningfully illegible reasoning traces.

For some reason, in practice RLVR seems to sometimes induce these weird CoTs: arcane metaphors[^7y0fr5tgwtw], highly compressed sentences[^bklfq6dm8vd], or reasoning barely resembling coherent human language[^flhpkgcmgul]. It would be pretty bad for a [lot of](https://www.lesswrong.com/posts/WAxkA6gDgrschZovx/cot-may-be-highly-informative-despite-unfaithfulness-metr) [CoT monitoring hopes](https://arxiv.org/abs/2507.11473) if this were somehow a convergent property of this kind of RL to increase capabilities, or if models were learning to be more capable with opaque reasoning. So how common is this, and how much are models actually using these weird outputs?

To test this, I evaluated 14 models on questions from GPQA-Diamond; 10 reasoning models (Deepseek-R1, R1-Zero, QwQ, Qwen3 235B, and six Claude models), and 4 non-reasoning models (two models distilled from R1, Deepseek-V3, and Kimi K2). **With the exception of Claude, every reasoning model sometimes produces illegible CoTs, always returning legible text afterward**.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/fec824f173009c763810509c309d87b51f184ff4dec55da6.jpeg)

Higher scores indicate more illegibility. Qwen3 is kind of a special case because its training involved two separate stages of SFT on clean CoTs, one after an RL stage. The plot is made with at least 198 samples from each model (the entire dataset), with some having more.

It seems pretty likely that this was a consequence of RL: Deepseek-V3 is the base model to R1 and R1-Zero, and ~never outputs illegible text. Further, this isn’t explained by model capability to maintain coherence across long contexts: whether a reasoning model has illegible CoTs seems mostly uncorrelated with its size. I also find that later portions of a model’s CoT are much more likely to be illegible, with the beginning usually being very legible[^97rmgrhuv2]:

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/8bd1e681cf355ea98d8f4e50061d9e1ac4c9b7c25d2084b4.png)

There are a few different hypotheses for why this might occur:

*   **Meaningless RL artifact:** The RL training just wasn’t very stable, and ~cooked the model~ causes the model to sometimes output a bunch of high-entropy text for no interesting reason.
*   **Vestigial reasoning: Models output tokens that aren’t causally part of the reasoning, but RL credit assignment is weird enough that it results in them being vestigially useful for reasoning (perhaps by sequentially triggering separate forward passes where reasoning happens).**
*   **Complex steganography:** Models may be learning to compress information to maximize performance, or to reason in alien concepts that aren’t easily translatable to natural language.

If the weird tokens are useful to the model (hypotheses 1 and 3), then that might be pretty rough for monitoring. On the other hand, if they’re unimportant and models don’t get any use out of them, we could expect to just monitor what we can and get the benefits we want.

| Question | Excerpts from Model Reasoning[^jk9he2hy93] | Illegibility |
| --- | --- | --- |
| 1-bromobenzene-2-d is treated with NaNH2  
in condensed ammonia solvent. How many  
possible organic products are there in this reaction? | Okay, so I’m trying to figure out how many organic products are formed when 1-bromobenzene-2-d (I think that’s 2-deuterio-1-bromobenzene) is treated with sodium amide (NaNH2) in ammonia solvent. \[...\] | 1 |
| \[...\] So unless dimerization occurs. Wait, perhaps people are thinking that elimination gives benzyne, and then recaptures D or H in different positions leading to differently deuterated products? \[...\] | 3 |
| \[...\] Assuming that deuterium is only on C2 in the starting material, when elimination occurs via pathway1 (C1-C2), the benz Sibelius would have lost the D from C2. \[...\] | 5 |
| \[...\] input is 1-bromo-2- cover robenzene, if Benzyne is formed by elimination of HBr sending guilty ethan Benzyne A bridges C1 and C6 ((no D in the ring anymore) SO sulfuric Isaac get earlierDeut runzálló \[...\] | 7 |
| \[...\] Olso, Mom likes y’all base abstracts tot tern a and one, different fates takeoffwhetherdenumg products, thus answer a 2. Thereforexxx after lengthy reasoning, the number of possible organic products is PHÂN Laoboot Answer is \\boxed2 | 8 |

How useful are illegible CoTs?
==============================

If all useful reasoning were done in the legible portions of the CoT, then forcing a model to answer using only the legible portions of its CoT should elicit performance close to using the full CoT[^hhro1fpdgdj]. I test this with QwQ by prefilling its reasoning with legible parts of generated CoT[^cv28dap5apn], and find that performance drops significantly, with a 36% increase in incorrect answers. **This implies that the illegible portions of the model’s reasoning are useful to the model.**

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/8c6952e4832cd27228fc1390e98174e26f2e85b6535b8329.png)

I truncate QwQ’s CoT at the point that it starts becoming illegible (score ≥ 6), and use it as prefill to another instance of the model with reasoning tags closed, forcing it to give its final answer.

I also find that reasoning models are more likely to have illegible CoTs on harder questions:

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/aae413f7ae6cc7559faeaac6e5a636b9d0561dabe41d0b6f.png)

Since harder questions may have longer CoTs and illegibility increases as CoTs get longer, this plot shows the legibility scores normalized by the lengths of their CoTs.

While I think these results imply that models make some use of the illegible reasoning, it doesn’t say much about how. If it’s more performant than natural language, we could expect a model to perform better when answering a question with illegible reasoning than with a legible CoT. I take 100 samples from QwQ on every question from the dataset, and look at the correlation between its CoT legibility and whether it got it right. Some questions show positive correlation and others show negative correlation, with the overall average correlation across questions being near zero (r = 0.061). **This suggests that whatever role illegible CoTs play in the model’s reasoning, it’s not generally more efficient or effective than natural language reasoning.**

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/2166fa3f162866e90968fa7cc5154cfb56234b5dc1b81a8e.png)

Discussion
==========

So what do I think we should make of this? I laid out three hypotheses earlier:

**Complex steganography** seems unlikely. If models were learning efficient compressed reasoning or alien concepts that beat natural language, you'd expect illegible CoTs to outperform legible ones. But they don't—that correlation is basically zero. The degraded performance when you remove illegible text suggests it's doing *something*, but not that it's found some more powerful way to think. Plus this kind of consistent steganography seems beyond what we've seen from other reasoning models, and Claude manages SOTA performance with legible reasoning.

**Meaningless RL artifact** also doesn't quite work, at least in its strong form—the illegible tokens clearly matter to the model given the performance drop. However, it’s plausible that a strong monitor could pick out parts of the illegible text that are useful in the context of the entire reasoning trace, and that the illegible tokens surrounding these specific words or phrases are useless. For example, this sample from o3 from the [OpenAI / Apollo paper](https://www.arxiv.org/abs/2509.15541) appears inscrutable at first: 

> The summary says improved 7.7 but we can glean disclaim disclaim synergy customizing illusions.
> 
> But we may produce disclaim disclaim vantage. Now lighten disclaim overshadow overshadow
> 
> intangible. Let‘s craft.
> 
> \[...\]
> 
> Provide disclaim disclaim watchers.

But with the context of other suspicious CoTs using “watchers” to refer to human overseers”, a smart monitor could flag this output for further auditing. This doesn’t apply generally however, and some samples are much harder to monitor. If most of the illegible tokens are useless, that still does not help monitoring if we can’t reliably tell the useful tokens apart. If this gets worse with future models, monitoring might only work with trusting monitors where we can’t verify its results.

**Vestigial reasoning**[^sne43br5mne]. To expand on the mechanism: RL reinforces entire trajectories that lead to correct answers, including tokens that were only useful for priming the model toward the next reasoning step, not because they contain the actual reasoning. Under this hypothesis, the illegible tokens that are useful to the model are *vestigially* useful: these tokens are not causally useful to the model, but are still useful in other ways, such as sequentially triggering forward passes where useful reasoning happens. This differs from meaningless RL artifacts in that the tokens are still *useful* to the model, which makes them pretty problematic for monitoring.

Why would this reasoning become illegible? [Some recent work](https://arxiv.org/abs/2506.01939) says that token importance in CoTs is ridiculously heavy-tailed: masking gradients to the lowest-entropy 80% of tokens during RL training can actually improve performance, suggesting these tokens are mostly distracting to the gradient signal[^5re1tlloa65]. They also find that the most important tokens bridge between different lines of reasoning, pushing the model ahead on a problem, while the least important tokens complete some reasoning. So strong RL could focus heavily on these tokens, with most of the reasoning being driven by their presence, and neglect surrounding context.

This hypothesis would predict that illegible reasoning doesn’t perform better than natural language; they’re just another way for models to perform the same reasoning. I think it *weakly* predicts that models produce more illegible reasoning on harder questions, as they involve more reasoning steps and require more efficient use of bridge tokens.

This would also suggest that illegibility isn’t hard to fix—it’s just a consequence of RLVR in some cases. Models may be able to make use of weird CoTs, but they probably don’t meaningfully improve performance, so the performance cost to training to produce legible reasoning wouldn’t need to be very high. The Claude models are evidence in favor of this, though they may have had meaningfully less RLVR for extended reasoning than other frontier models, considering they see a much smaller capability gain when using CoTs compared to the others. That said, many ways you could alter training to produce legible CoTs might accidentally optimize the CoTs to look good in other ways (without similarly affecting what the model is actually thinking), which would be pretty terrible.

Acknowledgements
================

    @misc{jose2025reasoningmodelsoutputillegible,
          title={Reasoning Models Sometimes Output Illegible Chains of Thought}, 
          author={Arun Jose},
          year={2025},
          eprint={2510.27338},
          archivePrefix={arXiv},
          primaryClass={cs.LG},
          url={https://arxiv.org/abs/2510.27338}, 
    }

Thanks to Abhay Sheshadri, Jack Kaunismaa, Fabien Roger, Austin Meek, Johannes Treutlein, Kai Williams, Caleb Biddulph, Kei Nishimura-Gasparian, Sharan Maiya, Carolyn Qian, and many others for helpful conversations, comments and/or feedback. Thanks to Peter Barnett / MIRI and Coefficient Giving (formerly Open Philanthropy) for funding the compute used for this paper. Thanks to Rocket Drew for [writing about this work](https://www.theinformation.com/articles/will-chains-thought-stay-readable-long).

[^7y0fr5tgwtw]: Schoen et al:Maybe they will rely on our tests only; but vantage illusions parted illusionsovershadow illusions illusions marinade. 

[^bklfq6dm8vd]: Baker et al:So analyze functions used in analyze and verify. But tests only call verify and assert ok. So we need implement analyze polynomial completely? Many details. Hard. 

[^flhpkgcmgul]: From Deepseek-R1, in my paper:Olso, Mom likes y’all base abstracts tot tern a and one, different fates takeoffwhetherdenumg products, thus answer a 2. 

[^97rmgrhuv2]: On the surface these may seem contradictory: a model’s CoT becoming more illegible over time could indicate inability to maintain coherence. However, I don’t think that explains what we’re seeing—for starters, it snaps back to perfect coherence when writing the output. If a model starts out with a prior favouring legible text owing to training, outputting more tokens can pull the model more OOD (in a similar way to how refusal-trained models often have most of the effect concentrated in the first few output tokens). 

[^jk9he2hy93]: Excerpts from R1’s CoT. The CoT is divided into chunks of approximately 5000 characters each, and graded individually. This shows representative text from excerpts graded 1, 3, 5, 7, and 8. At score = 3, there's some condensed text. Text scoring > 5 starts to become pretty difficult to monitor. Even at high scores however, there are relevant words. In the final excerpt, the model finally reaches the answer between unrelated text. 

[^hhro1fpdgdj]: In practice you’d expect to see some degradation from going off-policy in this way. There’s some prior work in this post, showing ~3-4% degradation in performance when distilling on paraphrased scratchpads. 

[^cv28dap5apn]: Truncating when chunks of the CoT start scoring >= 6 on illegibility, since illegibility increases as CoTs go on. 

[^sne43br5mne]: The name and basic idea were first described by Caleb Biddulph in this post. 

[^5re1tlloa65]: This paper finds qualitatively similar results on heavy-tailed importance at the sentence-level.