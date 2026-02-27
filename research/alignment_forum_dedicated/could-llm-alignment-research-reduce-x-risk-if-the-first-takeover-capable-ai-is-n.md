---
title: "Could LLM alignment research reduce x-risk if the first takeover-capable AI is not an LLM?"
author: "Tim Hua"
date: "2026-01-19"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/rgviB6pAu3g5Jvwzz/could-llm-alignment-research-reduce-x-risk-if-the-first"
score: 25
votes: 10
---

Many people believe that the first AI capable of taking over would be quite different from the LLMs of today. Suppose this is true—does prosaic alignment research on LLMs still reduce x-risk? I believe advances in LLM alignment research reduce x-risk even if future AIs are different. I’ll call these “non-LLM AIs.” In this post, I explore two mechanisms for LLM alignment research to reduce x-risk:

*   **Direct transfer:** We can directly apply the research to non-LLM AIs—for example, reusing behavioral evaluations or retraining model organisms. As I wrote this post, I was surprised by how much research may transfer directly.
*   **Indirect transfer:** The LLM could be involved in training, control, and oversight of the non-LLM AI. Generally, having access to powerful and aligned AIs acts as a force multiplier for people working in alignment/security/societal impact (but also capabilities).

LLM alignment research might struggle to reduce x-risk if: (1) it depends heavily on architectural idiosyncrasies (e.g., chain-of-thought research), (2) non-LLMs generalize differently from LLMs, or (3) more aligned LLMs accelerate capabilities research.

What do I mean by LLM AIs and non-LLM AIs?
==========================================

In this post, I define LLM AIs as AIs that have gone through a similar training process to current LLMs. Specifically, these AIs are first pre-trained on large amounts of data about the world, including but not limited to language. Then, they are fine-tuned and/or undergo reinforcement learning. LLM AIs are trained using stochastic gradient descent.

There are several plausible alternatives to LLM AIs. I’ll list a few of them here, starting from systems that are most similar to LLMs:

*   LLM AIs with online learning that gain most of their capabilities by updating a memory bank (as opposed to their parameters).
*   Neurosymbolic hybrids, where much of the AI’s capabilities come from its use of some symbolic system.
*   AIs that acquire “agency” (possibly using RL) before acquiring comprehensive world models.
*   Multi-agent systems that are much more powerful than the underlying individual agents (e.g., human societies).
*   Systems whose development is carefully guided by other AIs (e.g., instead of fine-tuning on law textbooks to learn law, an LLM AI carefully manipulates the non-LLM AI’s weights and modules to teach it law.)[^-LeEg3zR6Eutudedpp-1]

In this post, I’ll make the following assumptions about the non-LLM AIs:

1.  They are at least as powerful as current LLM AIs, but not wildly superhuman.[^-LeEg3zR6Eutudedpp-2]
2.  It’s possible to train them to do specific things.

Direct Transfer: We can replicate LLM alignment research in non-LLM AIs
=======================================================================

Black-box evaluations—and the infrastructure for running them—transfer to non-LLM AIs without modification.
-----------------------------------------------------------------------------------------------------------

Dangerous capabilities evaluations, alignment evaluations, alignment-faking evaluations, and scheming propensity evaluations—all of these can be run directly on non-LLM AI. Evaluation infrastructure, such as automated black-box auditing agents like [Petri](https://alignment.anthropic.com/2025/petri/) and tools for sifting through training data like [Docent](https://transluce.org/docent), can also be run without modifications. This point may be obvious, but it’s worth stating explicitly.

A great set of black-box evaluations won't be a silver bullet, but it can help us develop a better general understanding of our AIs, which could in turn spur research addressing more deep-rooted problems. Improving these evaluations is valuable regardless of what future AIs look like.

LLM-focused interpretability techniques may transfer a decent amount.
---------------------------------------------------------------------

**Sparsity and representations:** Much of mechanistic interpretability relies on sparse decomposition—breaking what the AI is doing into sparsely activating components, then interpreting each based on which contexts activate it (e.g., SAEs, [CLTs](https://transformer-circuits.pub/2025/attribution-graphs/methods.html), [SPD](https://arxiv.org/abs/2506.20790)). This approach should also work on non-LLM AIs.

Why expect this to generalize? Three reasons, none of which depend on superposition. First, sparsity reflects the real world—a general AI doesn't need all its knowledge for any given task, so we can focus on the few active components and ignore the rest. Second, sparsity is inherently interpretable; tracking a handful of active components is just easier than tracking thousands. Third, [the natural representation hypothesis](https://www.lesswrong.com/posts/gvzW46Z3BsaZsLc25/natural-abstractions-key-claims-theorems-and-critiques-1) suggests that different AIs [learn similar representations](https://arxiv.org/abs/2405.07987). So even if we can't interpret a component directly, we may be able to translate it into LLM concepts and interpret it with our LLM interp tools (see e.g., [translating embeddings across models](https://arxiv.org/abs/2505.12540) with zero paired data.)

If so, LLM interpretability progress should carry over, particularly work that makes conceptual contributions beyond the LLM setting. For example, we may end up using something like [JumpReLU](https://arxiv.org/abs/2407.14435) to address shrinkage, or using something like [Matryoshka SAEs](https://www.lesswrong.com/posts/rKM9b6B2LqwSB5ToN/learning-multi-level-features-with-matryoshka-saes) to address absorption when conducting sparse decompositions of non-LLM AIs.

Top-down methods like activation steering or representation engineering might also extract useful representations from non-LLM AIs—but unlike the case above, I don't have principled reasons to expect transfer.

**Mind reading:** If the natural representation hypothesis holds, we might be able to build translators that convert non-LLM activations directly into English via pre-trained LLMs. Work on [activation oracles](https://www.lesswrong.com/posts/rwoEz3bA9ekxkabc7/activation-oracles-training-and-evaluating-llms-as-general), [predictive concept decoders](https://transluce.org/pcd), and natural language autoencoders (unpublished) suggests this is feasible for LLMs, and the techniques could extend to other architectures.

**Model diffing:** The tools above—sparse decomposition, activation-to-English translation—could also help with model diffing in non-LLM AIs.

**Honesty training:** It also seems plausible that honesty-training techniques developed for LLMs (e.g., [confessions](https://openai.com/index/how-confessions-can-keep-language-models-honest/) in the last turn) could transfer to non-LLM AIs.

Many other training/black box alignment research can be replicated on non-LLM AIs.
----------------------------------------------------------------------------------

New research advances both our object-level understanding of LLMs and our knowledge of *how to study* *AIs*. The most valuable papers ask good questions in addition to providing good answers. Working on LLMs can teach us what questions matter for powerful AIs in general.

Once we know how to set up valuable experiments, we (or, more realistically, our LLM coding assistants) can rerun it on non-LLM AIs to recover the object-level findings. Looking through some past studies, it seems like many of them could be fairly easily replicated as long as we have some way to train our non-LLM AI. Here are some examples from model organisms research that we could replicate:

*   [Auditing Language Models for Hidden Objectives:](https://www.anthropic.com/research/auditing-hidden-objectives) Train the non-LLM AI to exhibit something like reward model biases, then test various mechanisms for uncovering the hidden goal in a blue-team/red-team setup.
*   [Natural Emergent Misalignment From Reward Hacking in RL:](https://www.anthropic.com/research/emergent-misalignment-reward-hacking) Give the non-LLM AI environments that are hackable, induce reward hacking, and observe the consequences. We might even be able to reuse the exact environments from this paper.
*   [Secret Keeping Language Models:](https://www.lesswrong.com/posts/Mv3yg7wMXfns3NPaz/eliciting-secret-knowledge-from-language-models-1) Teach the non-LLM AI some secrets and attempt to elicit them.
*   [Training Time Mitigations for Alignment Faking in RL:](http://alignment.anthropic.com/2025/alignment-faking-mitigations/) Test the same mitigations from this paper.

This isn't limited to model organisms research. We could teach a non-LLM AI (perhaps via imitation learning) misaligned behavior on a narrow distribution and observe how it [generalizes](https://www.emergent-misalignment.com/). We could try to [teach the model false facts](https://arxiv.org/abs/2510.17941). If the non-LLM AI involves pretraining, we could apply research on shaping LLM persona priors (e.g., [research](https://alignment.anthropic.com/2025/reward-hacking-ooc/) showing that training on documents about reward hacking induces reward hacking, as well as work on [alignment pretraining](https://alignmentpretraining.ai/)).

I'm not claiming that we can replicate *every* safety paper on non-LLM AI. We can't interpret chain-of-thought if there's no visible external reasoning,[^-LeEg3zR6Eutudedpp-3]and [recontextualization](https://arxiv.org/abs/2512.19027) might be difficult if the AI uses memory in peculiar ways. But looking through papers from [MATS](https://scholar.google.com/citations?hl=en&user=VgJaUK4AAAAJ&view_op=list_works&sortby=pubdate) or [Anthropic](https://alignment.anthropic.com/), it seems to me that we could replicate most of the recent non-chain-of-thought LLM alignment research on non-LLM AIs. If an LLM alignment paper asked a good question and proposed general ideas, then it will still have value if the first takeover-capable AIs are not LLMs.

Prosaic alignment research could also help the human researchers get better at alignment research in general, including aligning non-LLM AIs.

Counterpoint: Different generalization properties may hinder transfer
---------------------------------------------------------------------

Some alignment research depends heavily on architectural idiosyncrasies—chain-of-thought research being the clearest example. This work would transfer poorly to non-LLM AIs. That said, the dependency may be less severe than it first appears: as noted above, even some SAE research might transfer to non-LLMs.

A more fundamental concern is that non-LLM AIs might generalize differently from LLMs, potentially making replicated experiments less informative of the non-LLM AI’s overall disposition. Here are two examples of this generalization gap:

*Evaluations that don't predict behavior.* For example, a personality test that reliably flags sycophancy in LLMs might have no predictive power for non-LLM AIs. More generally, the behavioral evaluations we use as outcome measures may not track the same underlying traits across architectures.

*Model organism training processes might be unrealistic.* When we train LLM model organisms, one key concern is that the trained-in misaligned behavior might differ importantly from how such behaviors would arise in the wild. This problem could get worse (or better) when training model organisms on non-LLM AIs.

It's hard to know in advance how likely these generalization failures are. The natural representation hypothesis offers some hope: models trained on the same world may converge on similar representations and generalization patterns.

A separate concern is that non-LLM AIs might be more evaluation-aware or more capable of alignment faking, making experiments harder to interpret. Non-LLMs might exacerbate this, but it's a general challenge when studying any sufficiently sophisticated AI.

Indirect transfer: LLM AIs are likely to play a role in creating non-LLM AIs
============================================================================

Using misaligned LLMs to build powerful non-LLM AIs is obviously undesirable.
-----------------------------------------------------------------------------

If LLMs are heavily involved in building their non-LLM successors, they will also influence the alignment properties of those successors. Egregiously misaligned LLMs might sabotage alignment efforts or steer successors toward goals aligned with the LLMs rather than with humans—a scenario explored in [AI-2027](https://ai-2027.com/race#race-2027-11-30). We're not necessarily doomed if forced to build non-LLM successors using misaligned LLMs. Interventions like low-stakes control and trading with schemers might be sufficient. But the situation would be significantly better if our LLMs were aligned and not scheming.

However, the absence of scheming is not sufficient. We will also need LLMs to 'try their best' even on hard-to-verify domains and not [overconfidently](https://www.lesswrong.com/posts/NfgukR3HSaRq4WhyW/tim-hua-s-shortform?commentId=rawnmnqyAEsTimkNT) claim success at aligning their successors. LLM alignment research aimed at improving models’ ability to conduct AI safety research would be helpful here.

We can leverage trusted LLM AIs for control and oversight.
----------------------------------------------------------

If we have trusted LLMs, we could use them in control protocols for the non-LLM AIs (see also Ryan Greenblatt's [post](https://www.lesswrong.com/posts/cJQZAueoPC6aTncKK/untitled-draft-udzv)). Making better LLM-based black-box [monitors](https://www.lesswrong.com/posts/sb8WmKNgwzefa6oaJ/building-black-box-scheming-monitors) and oversight [agents](https://www.lesswrong.com/posts/oZuJvSNuYk6busjqf/oversight-assistants-turning-compute-into-understanding) also reduces risks from non-LLM AIs.

Counterpoint: Others will use LLM AIs to accelerate capabilities and/or other bad things in society.
----------------------------------------------------------------------------------------------------

If we make LLM AIs more aligned, they might also become more capable at building non-LLM AIs. While this is an obvious concern, it is mostly similar to existing concerns around capabilities externalities from alignment research. I don't think there are any substantially new concerns here if we assume that first takeover-capable AIs are non-LLMs.

Maybe you should work on aligning LLM AIs
=========================================

In this post, I outlined several reasons why LLM alignment research is valuable even if the first takeover-capable AI is not an LLM AI. However, to find out whether *more* people should work on aligning LLM AIs, we’ll have to evaluate their opportunity cost, which I do not plan to address here.[^-LeEg3zR6Eutudedpp-4]Personally, I explored this question because I'm planning to work on LLM alignment and wanted to sanity-check whether that work would remain valuable even if the most dangerous future AIs look quite different from today's LLMs.[^-LeEg3zR6Eutudedpp-5]

*Thanks for feedback from other participants in the Redwood futurism writing program. All errors are my own. *

[^-LeEg3zR6Eutudedpp-1]:  

[^-LeEg3zR6Eutudedpp-2]:  

[^-LeEg3zR6Eutudedpp-3]:  

[^-LeEg3zR6Eutudedpp-4]:  

[^-LeEg3zR6Eutudedpp-5]: