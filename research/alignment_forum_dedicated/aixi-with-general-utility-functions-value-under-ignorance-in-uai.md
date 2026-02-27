---
title: "AIXI with general utility functions: \"Value under ignorance in UAI\""
author: "Cole Wyeth"
date: "2025-12-22"
source: "alignment_forum"
url: "https://arxiv.org/abs/2512.17086"
score: 25
votes: 6
---

This updated version of my AGI 2025 paper with Marcus Hutter, "Value under ignorance in universal artificial intelligence," studies general utility functions for AIXI. Surprisingly, the (hyper)computability properties have connections to imprecise probability theory! 

AIXI uses a defective Bayesian mixture called a semimeasure, which is often viewed as expressing a chance that the agent dies. I do not think that interpretation has been sufficiently justified. Recasting semimeasures as credal sets, we can recover the (recursive) value function from reinforcement learning for discounted nonnegative rewards. We can also obtain a wider class of lower semicomputable value functions, with optimal agents following a max min decision rule.

This is an early conference paper without complete proofs included. You should read it if:

*   You are interested in utility functions for AIXI. There have been a few previous attempts to formulate this, but ours seems to be the first general and rigorous treatment with (easy but) nontrivial consequences.
*   You are curious how AIT might interact with imprecise probability. For instance this is probably relevant to (but much shallower than) Infra-Bayesianism.
*   I sent it to you personally. I polished and posted the paper on arXiv for convenience of collaboration on our ongoing work. **Most people should wait for a more complete journal version.** If you do read it and are interested, please let me know. There are a ton of shovel-ready open problems to pursue.

Of course, this paper is largely motivated by AI safety (and my work was supported by the LTFF). However, any safety application would come at a much later stage, and I want to avoid the impression of making certain claims. This paper is one line of evidence from AIT potentially justifying the naturality of pessimism in the face of ignorance,[^jyh6irk1am] but the implications (for example, to rationality) need further study. Also, while I am hoping to place some constraints on reasonable utility/value functions for AIXI variants, I do not imagine it is easy to write down a safe but useful one (and this paper does not grapple with the problem directly).

(An earlier and much rougher version of these ideas appeared [here](https://www.lesswrong.com/posts/zwt8gL8Fmrnbiu52u/i-invented-semimeasure-theory-and-all-i-got-was-imprecise))

[^jyh6irk1am]: Another is suggested here.