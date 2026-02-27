---
title: "Ensuring Safety in Mixed Deployment"
author: "Cleo Nardo"
date: "2026-02-26"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/wWb3mmjzYFbNaDGk2/ensuring-safety-in-mixed-deployment-1"
score: 18
votes: 5
---

*Thanks to Tim Hua, Julian Stastny, Alek Westover, and Lukas Finnveden for discussion. This post supersedes my previous post,* [*The Case for Mixed Deployment*](https://www.lesswrong.com/posts/NjuMqHjDNHogmRrkF/the-case-for-mixed-deployment) *— no need to read both.*

Summary
-------

Buck Shlegeris and Ryan Greenblatt [observe](https://www.lesswrong.com/posts/kcKrE9mzEHrdqtDpE/the-case-for-ensuring-that-powerful-ais-are-controlled) that if we are deploying a single model, then we can decompose reducing takeover into:

1.  **Alignment:** ensuring the model isn't a schemer.
2.  **Control:** ensuring the model can't take over even if it is a schemer.

Analogously, if we are deploying many models — some of whom may be schemers and some who aren't — then we can decompose reducing takeover into:

1.  **Alignment:** making each individual model less likely to scheme.
2.  **Diversification:** reducing correlation between models' scheming, so that not all models scheme together.
3.  **Pure control:** ensuring that the models can't take over even if they are all schemers.
4.  **Mixed control:** ensuring that the probability of takeover given partial scheming is close to the probability of takeover given no scheming, rather than close to the probability of takeover given full scheming. Equivalently, making the "danger function" (the probability of catastrophe as a function of the proportion of scheming AIs) more convex.

Importantly, diversification is not unconditionally good. It helps when the danger function is convex, and hurts when it is concave. However, I expect the danger function to be convex: intuitively, if only 50% of the models are scheming, then this is much closer to having 0% schemers than to having 100% schemers, in terms of the probability of takeover. Moreover, we can employ mixed control to make the danger function more convex, which makes diversification more valuable.

In this post, I'll derive the decomposition and suggest some directions in each agenda.

+++ Formal model

I use a simple model for the formal analysis, but I think the qualitative results are robust to different modelling choices.

Suppose we deploy n models. A **configuration** **s** ∈ {−1,+1}ⁿ specifies which models are scheming (+1) and which are aligned (−1). We have a prior P over configurations, and a **danger function** d: \[0,1\] → \[0,1\] mapping the proportion of scheming models to the probability of catastrophe, with d(0) = 0.

We model the danger function as d(x) = c · x^η, where:

*   c ∈ \[0,1\] captures how dangerous full scheming is (pure control reduces c).
*   η \> 1 means convex (accelerating danger), η = 1 means linear, η < 1 means concave (diminishing danger).

We model the prior over configurations using a **latent variable model**. There is a shared latent bit b ~ Bern(p) representing whether the "base" training process produces schemers. Each model's scheming status is then sᵢ = b ⊕ εᵢ, where εᵢ ~ Bern(ε) independently. That is:

*   If b = 1 (base is scheming): each model schemes with probability 1 − ε.
*   If b = 0 (base is aligned): each model schemes with probability ε.

When ε = 0, this is pure deployment — all models are perfectly correlated. As ε increases, models become more independent.

Write x for the proportion of models scheming. In the large-n limit, x concentrates at 1 − ε (when b = 1) or ε (when b = 0). So:

**Pr\[takeover\] = p · c · (1 − ε)^η + (1 − p) · c · ε^η**

The four research directions map onto four parameters:

| Research direction | Parameter | Always helps? |
| --- | --- | --- |
| Alignment | p ↓ | Yes |
| Diversification | ε ↑ | Only if η > 1 |
| Pure control | c ↓ | Yes |
| Mixed control | η ↑ | Yes |

**Why alignment always helps.** Decreasing p shifts weight from the b = 1 term (high danger) to the b = 0 term (low danger). Since (1 − ε)^η > ε^η for ε < 1/2, this always reduces Pr\[takeover\].

**Why pure control always helps.** Decreasing c scales both terms down. Always reduces Pr\[takeover\].

**Why mixed control always helps.** Increasing η shrinks both (1 − ε)^η and ε^η, since both bases are in \[0,1\]. So Pr\[takeover\] decreases.

**When diversification helps.** Differentiating with respect to ε:

This is negative (diversification helps) iff p · (1 − ε)^(η−1) > (1 − p) · ε^(η−1), which rearranges to logit(p) > (η − 1) · logit(ε) where logit(x) = log(x/(1−x)). That is, diversification helps when the log-odds of base scheming exceeds (η − 1) times the log-odds of diversification noise.

*   When η > 1 (convex d), the condition holds easily for small ε — some diversification always helps. But there is an optimal level beyond which further diversification hurts.
*   When η < 1 (concave d), the condition fails for any ε > 0 — any diversification hurts.
*   When η = 1 (linear d), diversification helps iff p > 1/2.

**Complementarity.** Mixed control and diversification reinforce each other. Increasing η (mixed control) makes d more convex, which makes diversification more valuable. Diversification pushes mass into the mixed region where the convexity operates.




+++

Alignment
---------

I suspect that alignment research for mixed deployment will look pretty similar to alignment research in the single-model deployment, i.e. inventing novel alignment techniques, improving them, evaluating them, etc.

That said, mixed deployment shifts research priorities in two ways:

*   **Invest in second-best techniques.** Even if one alignment technique yields models with lower scheming probability than another, we should still invest in the inferior technique if we expect their successes will be decorrelated. For example, I think we should invest in training objectives which operate on the model's chain-of-thought or internal activations.
*   **Prioritize late-stage techniques.** We should prioritise techniques which apply late in the AI lifecycle (e.g. post-training, prompting, activation steering, scaffolding) and deprioritise techniques which apply early in the AI lifecycle (e.g. architecture design and pretraining). This is because if we have N early-stage techniques then a mixed deployment would need N separate pretraining runs (prohibitive). But if we have N late-stage techniques, we need only one pretraining run and can fork from that base model to create N decorrelated variants.

Diversification
---------------

Diversification is about reducing the correlation between models' scheming — ensuring that models' alignment failures are as independent as possible.

As argued above, diversification is only net beneficial when the danger function is sufficiently convex. The intuition: diversification pushes mass from both extremes (all-scheming *and* all-aligned) toward mixed configurations. When the danger function is convex, the gain from reducing the all-scheming probability outweighs the loss from reducing the all-aligned probability. When it is concave, the reverse holds.

### Estimating correlational structure

Several approaches:

*   **Expert elicitation.** For each model (or pair), ask researchers: "If model i were scheming, how surprised would you be? If model i is scheming, how much does that update you on model j?"
*   **Behavioural similarity.** Measure how similarly models behave across a battery of tasks, especially tasks designed to elicit deceptive or misaligned behaviour. High behavioural correlation suggests high correlation in scheming.
*   **Training data overlap.** Models trained on heavily overlapping data are more likely to share the same failure modes and biases, which plausibly increases correlation.
*   **Weight similarity.** Representational similarity analysis between model internals. Models with similar learned features are more likely to share the same alignment properties (or lack thereof).
*   **Kinship (divergence point).** Think of the training process as a tree. Two models that share pretraining but diverge at fine-tuning have high kinship; two models from different labs with different architectures have low kinship. Formally: if training consists of T discrete steps, the kinship of two models is the fraction of steps they share before diverging.

### Approaches to diversification

*   [**Gradient Routing**](https://www.lesswrong.com/posts/nLRKKCTtwQgvozLTN/gradient-routing-masking-gradients-to-localize-computation)**.** Train a single neural network on multiple environments while localizing the capabilities and tendencies from each environment to specified modules that can be ablated at inference. This enables mixed deployment from a single training run — instead of training 2ⁿ models for N environments, you train once and create decorrelated instances through different ablation patterns. See also [Gradient routing is better than pretraining filtering](https://www.lesswrong.com/posts/YdcP2LEsq9nwGKKrB/gradient-routing-is-better-than-pretraining-filtering).
*   **Monitor decoupling.** If a monitor is a shallow fine-tune of the agent it oversees, the monitor may be able to distinguish on-policy attacks (which the agent would "naturally" generate in deployment) from off-policy attacks (generated in testing). Josh Clymer [proposes](https://docs.google.com/document/d/19BXFP1N_5cwy47x2OE4mdWGvxDFCAMza7kwBGqLI2xo/edit?tab=t.0) cheap techniques to decorrelate monitors from agents — e.g. training monitors to have generally uncorrelated behaviour, training them to answer questions about agent behaviour incorrectly, or using unlearning to remove on-policy detection capabilities.
*   More obvious approaches:
    *   **Different system prompts.** Vary the instructions given to models.
    *   **Different datasets.** Train on different corpora, RL environments, and [belief-inducing synthetic documents](https://www.lesswrong.com/posts/ARQs7KYY9vJHeYsGc/modifying-llm-beliefs-with-synthetic-document-finetuning).
    *   **Different constitutions.** Rather than writing a single constitution describing a single persona, we should write many constitutions describing many different personas, i.e. Claude, Pierre, Henri, Jacques, Marcel.[^n3hz7x5205] Some personas should care more about harmlessness, others more about honesty, and others more about helpfulness.
    *   **Different training objectives.** Some training objectives should evaluate only the outputs; others the outputs and chains-of-thought; and others the outputs, chains-of-thought, and internal activations.
    *   **Different deals.** Offer AIs deals with different terms and provisions.
    *   **Noise injection.** Add randomness at various stages of inference.
    *   **Different labs.** Models from different labs (Anthropic, OpenAI, DeepMind, Meta, xAI, DeepSeek, Alibaba, Mistral) likely have less correlated failure modes than models from the same lab.

Pure Control
------------

Pure control corresponds to the existing control agenda — reducing the probability of takeover conditional on all models scheming. The research here is the same as in the single-model setting: monitoring by humans and trusted AIs, sandboxing, capability limitations, and so on.

Mixed Control
-------------

Mixed control is about making it so that partial scheming is much less dangerous than full scheming — making the danger function more convex.

Good protocols make it so that even a small aligned minority can prevent catastrophe:

*   **Primary with diverse checkers.** Deploy your most trusted model for main tasks, but use other models to monitor the safety-critical activity (e.g. scanning the codebase for backdoors). If the primary is aligned, we're safe regardless. If the primary is scheming but a checker is aligned, the checker can catch it.
*   **Cross-lab monitoring.** Each lab uses their own AI as the primary (e.g. Claude), and asks other labs to monitor the safety-critical activity (e.g. ChatGPT, Gemini, Llama, Grok).[^bdy3unxw7ho] Note that cross-lab monitoring requires new security arrangements, such as provably-secure third-party servers.
*   **Random sampling.** Every time we create a new AI agent, sample randomly from a population of models. This ensures schemers can't predict which tasks they'll be assigned or who'll be monitoring them.
*   **Parallel redundancy.** For easily verifiable tasks (e.g. "does this code have a backdoor?"), run all N models in parallel on the same task. If even one model is aligned, it will produce a correct answer, and verification is cheap. This is Lukas Finnveden's [point](https://www.lesswrong.com/posts/HEupcBPuQnamFn2yr/lukas-finnveden-s-shortform?commentId=uRHumn9ha9z7M5JNt): you maintain a "zoo" of diverse variants. Note that this carries a N times penalty.
*   **Sequential greedy selection.** For costlier tasks, run one model at a time, starting with the model most likely to be aligned. If it fails (or produces unverifiable output), switch to the next model — greedily selecting the variant most likely to succeed *conditional on the previous variants having failed*. This depends on the correlational structure: after observing that variant A failed, you should deprioritise variants with high kinship to A and try something dissimilar. This is analogous to [Weitzman's Pandora's Box](https://en.wikipedia.org/wiki/Pandora%27s_box_(economics)) with correlations. Sequential selection is much cheaper than parallel redundancy (you only pay for the failures you encounter, not all N variants), but introduces latency.

Some open questions are:

*   What is the optimal monitoring protocol given a known correlational structure P? Is there a clean information-theoretic or game-theoretic characterisation?
*   Can we design protocols that are robust to uncertainty in P?
*   What is the overhead cost of monitoring, and how does it trade off against safety?
*   Much like in Pure Control, we can split Mixed Control into two settings: mitigating diffuse threats and mitigating concentrated threats. How can we defend against these two types of threats in the mixed setting?

Appendix: Why partial scheming is much less dangerous than full scheming
------------------------------------------------------------------------

The case for diversification assumes that the danger function — mapping the proportion of scheming AIs to the probability of catastrophe — is convex. Equivalently: a non-scheming minority can do more to prevent catastrophe than a scheming minority can do to cause it. Below, I list mechanisms pushing toward convexity and concavity, as found in my [previous post](https://www.lesswrong.com/posts/NjuMqHjDNHogmRrkF/the-case-for-mixed-deployment).

### Arguments for convexity

A non-scheming minority can unilaterally prevent catastrophe through several mechanisms:

1.  **Exposing signals **\- Honest AI exposes coordination signals between schemers, which humans use to build honeypots.
2.  **Backdoor revelation** \- Honest AI points to specific triggers in supposedly safe code (backdoors are NP, so a sufficiently smart AI can demonstrate they have backdoors)
3.  **Capability revelation** \- Honest AI try their best on capability evaluations, revealing capabilities that schemers are concealing.
4.  **On-policy rogue behaviour** \- Honest AI can show us how it would behave non-compliantly (e.g. insert backdoors, manipulating humans). This helps us study the behaviour mechanistically, and train and evaluate detectors.
5.  **Whistleblowing** \- Honest AI directly informs humans of ongoing conspiracy.
6.  **Inconsistency exposure** \- Honest AI highlights contradictions in schemers' stories (see [AI Debate](https://www.lesswrong.com/w/debate-ai-safety-technique-1) for an extension of this idea).
7.  **Providing verified code** \- Honest AI provides mathematical proofs that code is safe, a standard that the schemer cannot meet.
8.  **Audit trail preservation** \- Honest AI saves evidence before schemers can delete it.
9.  **Understanding assistance** \- Honest AI helps humans understand new research.
10.  **Split consensus** \- Even if the honest AI can't prove the schemers are misaligned (e.g. both AIs accuse the other of being misaligned), this would be evidence that at least one AI is scheming. This is helpful for buying political support, and reallocating safety budget towards stronger oversight.

### **Arguments for concavity**

A scheming minority can unilaterally cause catastrophe through several mechanisms:

1.  **Weight self-exfiltration** \- Schemer copies itself to external servers.
2.  **Secret exfiltration** \- Schemer leaks critical IP or private data to bad actors.
3.  **Blackmail** \- Schemer leverages private information for coercion.
4.  **Data poisoning** \- Schemer corrupts training data affecting all future models.
5.  **Research sabotage** \- Schemer messes up the research. For some task decompositions, 5% corruption might suffice.
6.  **Vulnerability insertion** \- Schemer adds subtle security holes to code.
7.  **Resource hijacking** \- Schemer redirects compute/funds to malicious purposes.
8.  **Vulnerable world hypothesis** \- Schemer can unilaterally destroy the world via nanotechnology or bioweapons.

### **Why convexity likely dominates**

I think convex dangers dominate. That is, I think it's more likely that one good actor suffices for safety than that one bad actor suffices for catastrophe. I'm particularly moved by *Exposing signals*, *Backdoor revelation*, and *Capability revelation*. Hence, I recommend a mixed deployment strategy.

That said, I think the strongest considerations for concave danger are *Secret exfiltration, Research sabotage,* and *Blackmail*, but I am hopeful that these dangers could be mitigated with tractable control measures.

[^n3hz7x5205]: (h/t Tim Hua) We probably shouldn't choose only French male names. Perhaps: Fatima, Mingxuan, Siddharth, Gandalf, AIXI-tl, Dr. Amodei's Marvellous Thinking Machine, etc. 

[^bdy3unxw7ho]: This also helps with AI-enabled coups.