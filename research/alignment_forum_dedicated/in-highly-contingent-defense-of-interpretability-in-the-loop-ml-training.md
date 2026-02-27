---
title: "In (highly contingent!) defense of interpretability-in-the-loop ML training"
author: "Steven Byrnes"
date: "2026-02-06"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/ArXAyzHkidxwoeZsL/in-highly-contingent-defense-of-interpretability-in-the-loop"
score: 81
votes: 27
---

Let’s call *“interpretability-in-the-loop training”* the idea of running a learning algorithm that involves an inscrutable trained model, and there’s some kind of interpretability system feeding into the loss function / reward function.

Interpretability-in-the-loop training has a very bad rap (and rightly so). Here’s [Yudkowsky 2022](https://www.lesswrong.com/posts/uMQ3cqWDPHhjtiesc/agi-ruin-a-list-of-lethalities):

> When you explicitly optimize against a detector of unaligned thoughts, you're partially optimizing for more aligned thoughts, and partially optimizing for unaligned thoughts that are harder to detect.  Optimizing against an interpreted thought optimizes against interpretability.

Or [Zvi 2025](https://www.lesswrong.com/posts/mpmsK8KKysgSKDm2T/the-most-forbidden-technique):

> [The Most Forbidden Technique](https://thezvi.substack.com/i/145384938/the-art-of-the-jailbreak) is training an AI using interpretability techniques.
> 
> An AI produces a final output \[X\] via some method \[M\]. You can analyze \[M\] using technique \[T\], to learn what the AI is up to. You could train on that. Never do that.
> 
> You train on \[X\]. Only \[X\]. Never \[M\], never \[T\].
> 
> Why? Because \[T\] is how you figure out when the model is misbehaving.
> 
> If you train on \[T\], you are training the AI to obfuscate its thinking, and defeat \[T\]. You will rapidly lose your ability to know what is going on, in exactly the ways you most need to know what is going on.
> 
> Those bits of optimization pressure from \[T\] are precious. Use them wisely.

This is a simple argument, and I think it’s 100% right.

*But…*

Consider compassion in the human brain. [I claim](https://www.lesswrong.com/posts/KuBiv9cCbZ6ALjHFw/social-drives-1-sympathy-reward-from-compassion-to) that we have an innate reward function that triggers not just when I see that my friend is happy or suffering, but also when I *believe* that my friend is happy or suffering, even if the friend is far away. So the human brain reward can evidently get triggered by specific activations inside my inscrutable learned world-model.

Thus, I claim that the human brain incorporates a form of interpretability-in-the-loop RL training.

Inspired by that example, I have long been an advocate for studying whether and how one might use interpretability-in-the-loop training for aligned AGI. See for example [Reward Function Design: a starter pack](https://www.lesswrong.com/posts/xw8P8H4TRaTQHJnoP/reward-function-design-a-starter-pack) sections 1, 4, and 5.

My goal in the post is to briefly summarize how I reconcile the arguments at the top with my endorsement of this kind of research program.

My overall position
===================

*   Yudkowsky & Zvi are correct that straightforward interpretability-in-the-loop training of LLMs is almost definitely a very bad idea.
    *   …Unless interpretability someday develops to such a refined point that it’s adversarially robust (i.e., we understand the model *so well* that problematic thoughts have nowhere to hide from the interpretability tools). But that sure seems like a long-shot.
*   There exists a certain *brain-like* version of interpretability-in-the-loop RL training that does not suffer from this very obvious failure mode
    *   (…although it might or might not fail for other reasons!)
*   And there’s a straightforward explanation of *exactly how* it avoids this obvious failure mode.

The rest of this post will present this explanation:

How the brain-like version of interpretability-in-the-loop training avoids the obvious failure mode
===================================================================================================

The human brain has beliefs and desires. They are different. It’s possible to want something without expecting it, and it’s possible to expect something without wanting it. This should be obvious common sense to everyone, [unless your common sense has been crowded out by “active inference” nonsense](https://www.lesswrong.com/posts/MArdnet7pwgALaeKs/why-i-m-not-into-the-free-energy-principle).

Beliefs and desires are stored in different parts of the brain, and updated in different ways. ([This is a huge disanalogy between LLMs and brains.](https://www.lesswrong.com/posts/bnnKGSCHJghAvqPjS/foom-and-doom-2-technical-alignment-is-hard#2_3_2_LLM_pretraining_magically_transmutes_observations_into_behavior__in_a_way_that_is_profoundly_disanalogous_to_how_brains_work))

As an oversimplified toy model, I suggest to think of desires as a learned linear functional on beliefs (see my [Valence series §2.4.1](https://www.lesswrong.com/s/6uDBPacS6zDipqbZ9/p/SqgRtCwueovvwxpDQ#2_4_1_Side_note__Valence_as_a__roughly__linear_function_over_compositional_thought_pieces)). I.e. “desires” constitute a map whose *input* is some thought / plan / etc. (over on the belief side), and whose *output* is a numerical score indicating whether that thought / plan / etc. is good (if the score is positive) or bad (if it’s negative).

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/3d0b526800a03179989fb7f41ba1f522f07bf8a8775c1902.png)

Anyway, the important point is that these two boxes are updated in different ways. Let’s expand the diagram to include the different updating systems, and how interpretability-in-the-loop training fits in:

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/33055336a7c9f4f1fe5a6f2a71203977573e97e6521c8eb2.png)

The red arrow indicates that there’s some system (any system you like) that looks at the inscrutable activation state in the “Beliefs” box, and spits out one or more numerical metrics related to that state. Those numbers then go to the reward function, where they help determine the reward signals.

The interpretability data is changing the reward signals, but the reward signals are not directly changing the belief box that the interpretability system is querying.

That means: **The loop doesn’t close. This interpretability system is not creating any gradient that directly undermines its own faithfulness.**[^wf4b4offf5]

…So that’s how this brain-like setup avoids the obvious failure mode of interpretability-in-the-loop that Yudkowsky & Zvi were talking about at the top.

Things can still go wrong in more subtle and indirect ways
----------------------------------------------------------

…Or at least, it avoids the most straightforward manifestation of that problem. There are more subtle things that might go wrong. I have a high-level generic discussion in [Valence series §3.3](https://www.lesswrong.com/posts/rM8DwFKZM4eB7i2p8/valence-series-3-valence-and-beliefs#3_3_Motivated_reasoning___thinking___observing__including_confirmation_bias), where I point out that there exist indirect pathways through this diagram, and discuss how they can cause problems:

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/rM8DwFKZM4eB7i2p8/u5y0mlmde5fn18d8vsxk)

Diagram copied from [Valence series §3](https://www.lesswrong.com/posts/rM8DwFKZM4eB7i2p8/valence-series-3-valence-and-beliefs) 

And these kinds of problems can indeed pop up in the context of compassion and other interpretability-in-the-loop human social instincts. The result is that human social instincts that *on paper* might look robustly prosocial, are in fact not so robustly prosocial in the real (human) world. See my [Sympathy Reward post §4.1](https://www.lesswrong.com/posts/KuBiv9cCbZ6ALjHFw/social-drives-1-sympathy-reward-from-compassion-to#4_1_False_negatives__e_g__dehumanization_) and [Approval Reward post §6](https://www.lesswrong.com/posts/fPxgFHfs5yHzYqgG7/social-drives-2-approval-reward-from-norm-enforcement-to#6__How_robust_are_the_effects_of_Approval_Reward_) for lots of everyday examples.

So the upshot is: I don’t think the brain-like version of interpretability-in-the-loop RL training is a panacea for aligned ASI, and I’m open-minded to the possibility that it’s just not a viable approach at all. But it’s at least a not-*obviously*-doomed research direction, and merits more study. 

[^wf4b4offf5]: Added 2026-02-13: Actually, oops, even this sentence is a bit oversimplified. E.g. here’s a scenario. There’s an anti-deception probe connected to the reward function, and the “beliefs” box has two preexisting plans / actions: (A) a “be deceptive in a way that triggers the alarm” plan / action in the “beliefs” box, and (B) a “be deceptive in a way that doesn’t trigger the alarm” plan / action.Now, the good news is that there wouldn’t be a predictive learning gradient that would push towards (B), nor one that would create (B) if (B) didn’t already exist. But the bad news is, there is a kind of policy gradient that would ensure that, if (B) occurs by random happenstance, then the system will update to repeat (B) more often in the future. (Or worse, there could be a partway-to-(B) plan / action that’s somewhat rewarded, etc., and then the system may hill-climb to (B).)I still think this setup is much less obviously doomed than the LLM case at the top, because we have all this learned structure in the “beliefs” box that the reward function is not allowed to manipulate directly. Again, for example, if (B) doesn’t already exist within the web of constraints that constitutes the “beliefs” box, this system won’t (directly) create it.[Thanks Rhys Gould for discussion of this point.]