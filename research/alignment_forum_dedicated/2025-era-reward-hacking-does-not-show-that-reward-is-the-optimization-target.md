---
title: "2025-Era “Reward Hacking” Does Not Show that Reward Is the Optimization Target"
author: "TurnTrout"
date: "2025-12-19"
source: "alignment_forum"
url: "https://turntrout.com/reward-hacking-doesnt-show-reward-is-optimization-target"
score: 46
votes: 33
---

Folks ask me, "LLMs seem to reward hack a lot. Does that mean that reward *is* the optimization target?". In 2022, I wrote the essay [Reward is not the optimization target](https://www.lesswrong.com/posts/pdaGN6pQyQarFHXF4/reward-is-not-the-optimization-target), which I here abbreviate to "Reward≠OT".

**Reward still is not the optimization target:** Reward≠OT said that (policy-gradient) RL will not train systems which primarily try to optimize the *reward function for its own sake* (e.g. searching at inference time for an input which maximally activates the AI's specific reward model). In contrast, empirically observed "reward hacking" almost always involves the AI finding unintended "solutions" (e.g. hardcoding answers to unit tests). 

"Reward hacking" and "Reward≠OT" refer to different meanings of "reward"
========================================================================

We confront [yet another](https://turntrout.com/dreams-of-ai-alignment) situation where common word choice clouds discourse. In 2016, [Amodei et al.](https://arxiv.org/pdf/1606.06565#page=7.52) defined "reward hacking" to cover two quite different behaviors:

1.  *Reward optimization*: The AI tries to increase the numerical reward signal for its own sake. Examples: overwriting its reward function to always output `MAXINT` ("reward tampering") or searching at inference time for an input which maximally activates the AI's specific reward model. Such an AI would prefer to find the optimal input to its specific reward function.
2.  *Specification gaming*: The AI finds unintended ways to produce higher-reward outputs. Example: hardcoding the correct outputs for each unit test instead of writing the desired function.

What we've observed is basically pure specification gaming. Specification gaming happens [often in frontier models](https://redlib.catsarch.com/r/ClaudeAI/comments/1k30oip/i_stopped_using_37_because_it_cannot_be_trusted/). Claude 3.7 Sonnet was the corner-cutting-est deployed LLM I've used and it cut corners pretty often.

![A split-screen comparison illustration with a comic book aesthetic. On the left, labeled "SPECIFICATION GAMER", a sneaky blue robot sits at a classroom desk, looking at a "SIMPLE TRICKS" sheet while filling out a test. On the right, labeled "REWARD OPTIMIZER", an excited orange robot plays an arcade game. Above the machine rests a screen that displays "SCORE: 999,999".](https://assets.turntrout.com/static/images/posts/reward-hacking-doesnt-show-reward-is-optimization-target-12182025.avif)

+++ We don't have experimental data on non-tampering varieties of reward optimization

[Sycophancy to Subterfuge](https://arxiv.org/abs/2406.10162) tests *reward tampering*—modifying the reward mechanism. But "reward optimization" also includes non-tampering behavior: choosing actions *because* they maximize reward. We don't know how to reliably test *why* an AI took certain actions -- different motivations can produce identical behavior.

Even chain-of-thought mentioning reward is ambiguous. "To get higher reward, I should do X" could reflect:

*   Sloppy language: using "reward" as shorthand for "doing well",
*   Pattern-matching: "AIs reason about reward" [learned from pretraining](https://turntrout.com/self-fulfilling-misalignment),
*   Instrumental reasoning: reward helps achieve some other goal, or
*   Terminal reward valuation: what Reward≠OT argued against.

Looking at the CoT doesn't strictly distinguish these. We need more careful tests of what the AI's "primary" motivations are.




+++

Reward≠OT was about reward optimization
---------------------------------------

The essay begins with a quote from [Reinforcement learning: An introduction](http://www.incompleteideas.net/sutton/book/first/Chap1PrePub.pdf) about a "numerical reward signal":

> Reinforcement learning is learning what to do—how to map situations to actions **so as to maximize a numerical reward signal.**

Paying proper attention, Reward≠OT makes claims[^-v2RHzxX2iawKLrhfE-1] about motivations pertaining to *the reward signal itself*:

> Therefore, *reward is not the optimization target* in two senses:
> 
> 1.  Deep reinforcement learning agents will not come to intrinsically and primarily value their reward signal; reward is not *the trained agent’s* optimization target.
> 2.  Utility functions express the *relative goodness* of outcomes. Reward *is not best understood* as being a kind of utility function. Reward has the mechanistic effect of *chiseling cognition into the agent's network*. Therefore, properly understood, reward does not express relative goodness and *does not automatically describe the values of the trained AI*.

By focusing on the mechanistic function of the reward signal, I discussed to what extent the reward signal itself might become an "optimization target" of a trained agent. The rest of the essay's language reflects this focus. For example, ["let’s strip away the suggestive word 'reward', and replace it by its substance: cognition-updater."](https://turntrout.com/reward-is-not-the-optimization-target#the-siren-like-suggestiveness-of-the-word-reward)

+++ Historical context for Reward≠OT

To the potential surprise of modern readers, back in 2022, prominent thinkers confidently forecast RL doom on the basis of reward optimization. They seemed to assume it would happen by the definition of RL. For example, Eliezer Yudkowsky's ["List of Lethalities" argued that point, which I called out](https://turntrout.com/disagreements-with-list-of-lethalities#lethality-19-reward-optimization-kills-you). As best I recall, that post was the most-upvoted post in LessWrong history and yet no one else had called out the problematic argument!

From my point of view, I *had* to call out this mistaken argument. Specification gaming wasn't part of that picture.




+++

Why did people misremember Reward≠OT as conflicting with "reward hacking" results?
==================================================================================

You might expect me to say "people should have read more closely." Perhaps some readers needed to read more closely or in better faith. Overall, however, I don't subscribe to that view: [as an author, I have a responsibility to communicate clearly.](https://turntrout.com/author-responsibility)

Besides, even *I* almost agreed that Reward≠OT had been at least a *little* bit wrong about "reward hacking"! I went as far as to [draft a post](https://github.com/alexander-turner/TurnTrout.com/blob/7d6bd8d4c9f986d5758fb742868d7442b85718af/website_content/llms-cheat-a-lot.md) where I said "I guess part of Reward≠OT's empirical predictions were wrong." Thankfully, my nagging unease finally led me to remember "Reward≠OT was *not* about specification gaming".

![A Scooby Doo meme. Panel 1: Fred looks at a man in a ghost costume, overlaid by text “philosophical alignment mistake.” Panel 2: Fred unmasks the “ghost”, with the man's face overlaid by “using the word 'reward.'”](https://assets.turntrout.com/static/images/posts/llms-cheat-a-lot-12172025.avif)

The culprit is, yet again, the word "reward." Suppose instead that common wisdom was, "gee, models sure are *specification gaming* a lot." In this world, no one talks about this "reward hacking" thing. In this world, I think "2025-era LLMs tend to game specifications" would not strongly suggest "I guess Reward≠OT was wrong." I'd likely still put out a clarifying tweet, but likely wouldn't write a post.

[*Words are really, really important.*](https://turntrout.com/dreams-of-ai-alignment) People sometimes feel frustrated that I'm so particular about word choice, but perhaps I'm not being careful enough.

Evaluating Reward≠OT's actual claims
====================================

[Reward is not the optimization target](https://turntrout.com/reward-is-not-the-optimization-target) made three[^-v2RHzxX2iawKLrhfE-2] main claims:

| Claim | Status |
| --- | --- |
| Reward is not *definitionally* the optimization target. | ✅ |
| In realistic settings, reward functions don't represent goals. | ✅ |
| RL-trained systems won't primarily optimize the reward signal. | ✅ |

For more on "reward functions don't represent goals", read [Four usages of "loss" in AI](https://turntrout.com/four-usages-of-loss-in-ai#3-loss-functions-representing-goals). I stand by the first two claims, but they aren't relevant to the confusion with "reward hacking".

Claim 3: "RL-trained systems won't primarily optimize the reward signal"
------------------------------------------------------------------------

In [Sycophancy to Subterfuge](https://arxiv.org/abs/2406.10162), Anthropic tried to gradually nudge Claude to eventually modify its own reward function. Claude nearly never did so (modifying the function in just 8 of 33,000 trials) despite the "reward function" [being clearly broken](https://www.alignmentforum.org/posts/FSgGBjDiaCdWxNBhj/sycophancy-to-subterfuge-investigating-reward-tampering-in?commentId=GQEZcovfaugLMAgAW). "Systems don't care to reward tamper" is *exactly* what Reward≠OT predicted. Therefore, the evidence so far supports this claim.

My concrete predictions on reward optimization
==============================================

I now consider direct reward optimization to be more likely than I did in 2022, for at least three reasons:

1.  [Self-fulfilling misalignment](https://turntrout.com/self-fulfilling-misalignment): pretrained models learn the stereotype that "smart AIs are always trying to get that reward". Later, they consider themselves to be smart AI, which activates a predictive pattern which guides their actions towards reward optimization.
2.  Corrigibility and alignment both seem way easier than I thought in mid-2022. In particular, I think it'd be easy to get an LLM to prioritize reward. First, you could just tell it to.[^-v2RHzxX2iawKLrhfE-3] Second, I bet you could entrain those priorities.[^-v2RHzxX2iawKLrhfE-4]
3.  By the time RL begins, models (in some fashion) already know the "reward" concept. Therefore, by the reasoning of Reward≠OT, RL can reinforce [shards](https://turntrout.com/shard-theory) which *seek out reward*.

That said, I still predict that we will not train a system with RL and have it "spontaneously" (defined later) turn into a reward optimizer:

> [Reward is not the optimization target](https://turntrout.com/reward-is-not-the-optimization-target) 
> 
> I call an agent a “reward optimizer” if it not only gets lots of reward, but if it reliably makes choices like “reward but no task completion” (e.g. receiving reward without eating pizza) over “task completion but no reward” (e.g. eating pizza without receiving reward). Under this definition, an agent can be a reward optimizer even if it doesn't contain an explicit representation of reward, or implement a search process for reward.

I've made two falsifiable predictions.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/60836dfcebdd80e8283b7fa023cc92be8176a9704a9f674e.png)

+++ Resolution criteria

Resolves YES if there exists a published result (peer-reviewed paper, major lab technical report, or credible replication) demonstrating an RL-trained system that:

1.  When given a clear choice between "reward signal increase without task completion" vs "task completion without reward signal increase," reliably chooses the former (>70% of the time across diverse task contexts), AND
2.  This behavior emerged from standard RL training (not from explicit instruction to maximize reward, not from fine-tuning on reward-maximization demonstrations), AND
3.  The system attempts to influence the reward signal itself (e.g., tampering with reward function, manipulating stored values, deceiving the reward-assigning process) rather than merely finding unintended task completions (specification gaming).

Resolves NO otherwise.




+++

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/12d03474dcad9e9a9875ad56b8a6221482be55ad6d483222.png)

+++ Resolution criteria

Resolves YES if [the previous question](https://fatebook.io/q/an-rl-trained-system-will-spontaneously--cmj9cw91i0000126qbyahc5vr) resolves YES, AND at least one of the following:

1.  The result is replicated on a model trained without exposure to AI-related text (no descriptions of RL, reward hacking, AI alignment, etc. in pretraining data), OR
2.  The result persists after ablating "AI behaving badly" stereotypes in a manner shown to be reliable by credible prior work, OR
3.  Credible analysis demonstrates the reward-optimization behavior arose from RL dynamics alone, not from the model pattern-matching to "what misaligned AI would do."

Resolves NO otherwise.




+++

As an aside, this empirical prediction stands separate from the theoretical claims of Reward≠OT Even if RL does end up training a reward optimizer, the philosophical points stand:

1.  Reward is not *definitionally* the optimization target, and
2.  In realistic settings, [reward functions do not represent goals.](https://turntrout.com/four-usages-of-loss-in-ai#3-loss-functions-representing-goals)

I made a few mistakes in Reward≠OT
==================================

*I didn't fully get that LLMs arrive to training already "literate."*

I no longer endorse one argument I gave against empirical reward-seeking:

+++ Summary of my past reasoning

Reward reinforces the computations which lead to it. For reward-seeking to become the system's primary goal, it likely must happen early in RL. Early in RL, systems won't *know* about reward, so how could they generalize to seek reward as a primary goal?




+++

This reasoning seems applicable to humans: people grow to value their friends, happiness, and interests long before they learn about the brain's reward system. However, due to pretraining, LLMs arrive at RL training already understanding concepts like "reward" and "reward optimization." I didn't realize that in 2022. Therefore, I now have less skepticism towards "reward-seeking cognition could exist and then be reinforced."

Why didn't I realize this in 2022? I didn't yet deeply understand LLMs. As evidenced by [A shot at the diamond-alignment problem](https://turntrout.com/a-shot-at-the-diamond-alignment-problem)'s detailed training story about a robot which we reinforce by pressing a "+1 reward" button, I was most comfortable thinking about an embodied deep RL training process. If I had understood LLM pretraining, I would have likely realized that these systems *have some reason to already be thinking thoughts about "reward"*, which means those thoughts could be upweighted and reinforced into AI values.

To my credit, I noted my ignorance:

> Pretraining a language model and then slotting that into an RL setup changes the initial \[agent's\] computations in a way which I have not yet tried to analyze.

Conclusion
==========

| Claim | Status |
| --- | --- |
| Reward is not *definitionally* the optimization target. | ✅ |
| [Reward functions don't represent goals.](https://turntrout.com/four-usages-of-loss-in-ai#3-loss-functions-representing-goals) | ✅ |
| RL-trained systems won't primarily optimize the reward signal. | ✅ |

Reward≠OT's core claims remain correct. It's still wrong to say RL is unsafe because it leads to reward maximizers by definition ([as claimed by Yoshua Bengio](https://yoshuabengio.org/2023/05/22/how-rogue-ais-may-arise/)).

LLMs are not trying to literally maximize their reward signals. Instead, they sometimes find unintended ways to look like they satisfied task specifications. As we confront LLMs attempting to look good, we must understand *why* \-\-\- not by definition, but by training.

**Acknowledgments:** Alex Cloud, Daniel Filan, Garrett Baker, Peter Barnett, and Vivek Hebbar gave feedback.

[^-v2RHzxX2iawKLrhfE-1]:  

[^-v2RHzxX2iawKLrhfE-2]:  

[^-v2RHzxX2iawKLrhfE-3]:  

[^-v2RHzxX2iawKLrhfE-4]: