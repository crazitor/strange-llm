---
title: "We need a field of Reward Function Design"
author: "Steven Byrnes"
date: "2025-12-08"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/oxvnREntu82tffkYW/we-need-a-field-of-reward-function-design"
score: 118
votes: 45
---

*(Brief pitch for a general audience, based on a 5-minute talk I gave.)*

Let’s talk about Reinforcement Learning (RL) agents as a possible path to Artificial General Intelligence (AGI)
===============================================================================================================

My research focuses on “RL agents”, broadly construed. These were big in the 2010s—they made the news for learning to play Atari games, and Go, at superhuman level. Then LLMs came along in the 2020s, and everyone kinda forgot that RL agents existed. But I’m part of a small group of researchers who still thinks that the field will pivot back to RL agents, one of these days. (Others in this category include [Yann LeCun](https://www.lesswrong.com/posts/C5guLAx7ieQoowv3d/lecun-s-a-path-towards-autonomous-machine-intelligence-has-1) and [Rich Sutton & David Silver](https://www.lesswrong.com/posts/TCGgiJAinGgcMEByt/the-era-of-experience-has-an-unsolved-technical-alignment).)

Why do I think that? Well, LLMs are very impressive, but we don’t have AGI (artificial general intelligence) yet—not [as I use the term](https://www.lesswrong.com/posts/uxzDLD4WsiyrBjnPw/artificial-general-intelligence-an-extremely-brief-faq). Humans can found and run companies, LLMs can’t. If you want a human to drive a car, you take an off-the-shelf human brain, the same human brain that was designed 100,000 years before cars existed, and give it minimal instructions and a week to mess around, and now they’re driving the car. If you want an AI to drive a car, it’s … not that.

<table style="background-color:hsl( 20, 82%, 94% );border:2px solid hsl(0, 0%, 0%)"><tbody><tr><td style="border-color:hsl(0, 0%, 0%);text-align:center"><p><strong>Teaching a</strong> <strong>human to drive a car / teleoperate a robot:</strong></p><p>Minimal instruction,<br>30 hours of practice</p></td><td style="border-color:hsl(0, 0%, 0%);text-align:center"><p><strong>Teaching an</strong> <strong>AI to drive a car / teleoperate a robot:</strong></p><p>Dozens of experts, 15 years, $5,000,000,000</p></td></tr></tbody></table>

Anyway, human brains [are the only known example of “general intelligence”](https://www.lesswrong.com/posts/rgPxEKFBLpLqJpMBM/response-to-blake-richards-agi-generality-alignment-and-loss#2__We_need_a_term_for_the_right_column_thing__and__Artificial_General_Intelligence___AGI__seems_about_as_good_as_any_), and they are “RL agents” in the relevant sense (more on which below). Additionally, as mentioned above, people are working in this direction as we speak. So, seems like there’s plenty of reason to take RL agents seriously. 

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/b161a7724d85b4fb67a2331acfbc1d24f332bcba6821f1c7.png)

So the upshot is: **we should contingency-plan for real RL agent AGIs—for better or worse**.

Reward functions in RL
======================

If we’re talking about RL agents, then we need to talk about reward functions. Reward functions are a **tiny part of the source code, with a** ***massive*** **influence on what the AI winds up doing**.

For example, take an RL agent like [AlphaZero](https://en.wikipedia.org/wiki/AlphaZero), and give it a reward of +1 for winning at a board game and –1 for losing. As you train it, it will get better and better at winning. Alternatively, give it a reward of –1 for winning and +1 for losing. It will get better and better at losing. So if the former winds up superhuman at [Reversi / Othello](https://en.wikipedia.org/w/index.php?title=Reversi&oldid=1319867026), then the latter would wind up superhuman at [“Anti-Reversi”](https://en.wikipedia.org/w/index.php?title=Reversi&oldid=1319867026#Anti-Reversi)—an entirely different game! Again, tiny code change, wildly different eventual behavior.

I claim that if you give a powerful RL agent AGI the wrong reward function, then it winds up with callous indifference to whether people live or die, including its own programmers and users.

But what’s the *right* reward function? No one knows. It’s an open question.

Why is that such a hard problem? It’s a long story, but just as one hint, try comparing:

*   “negative reward for lying”, versus
*   “negative reward for *getting caught* lying”.

The first one seems like a good idea. The second one seems like a bad idea. But *these are actually the same thing*, because obviously the reward function will only trigger if the AI gets caught.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/8ac2dc5522629ab8a6dd09f72a880355f8181f419fda4952.png)

As it turns out, if you pick up a 300-page RL textbook, you’ll probably find that it spends a few paragraphs on *what the reward function should be*, while the other 299½ pages are ultimately about *how to maximize that reward function*—how do the reward signals update the trained model, how the trained model is queried, and sometimes there’s also predictive learning, etc.

Reward functions in neuroscience
================================

…And it turns out that there’s a similar imbalance in neuroscience:

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/1b9734d2219012e9e95d8d53515c233b4aedb37359bb4db0.png)

The human brain also has an RL reward function. It’s sometimes referred to as “innate drives”, “primary rewards”, “primary punishers”, etc.—things like ‘pain is bad’ and ‘eating when you’re hungry is good’. And just like in RL, the overwhelming majority of effort in AI-adjacent neuroscience concerns how the reward function updates the trained models, and other sorts of trained model updates, and how the trained models are queried, and so on. This part involves the cortex, basal ganglia, and other brain areas. Meanwhile, approximately nobody in NeuroAI cares about the reward function itself, which mainly involves the hypothalamus and brainstem.

We need a (far more robust) field of “reward function design”
=============================================================

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/9d84de1fbcb4836b7ce4314a97f623f7b78bbd4986285607.png)

So here’s the upshot: let’s learn from biology, let’s innovate in AI, let’s focus on AI Alignment, and maybe we can get into this Venn diagram intersection, where we can make headway on the question of what kind of reward function would lead to an AGI that intrinsically cares about our welfare. As opposed to callous sociopath AGI. (Or if no such reward function exists, then that would also be good to know!)

Oh man, are we dropping this ball
=================================

You might hope that the people working most furiously to make RL agent AGI—and claiming that they’ll get there in as little as 10 or 20 years—are thinking very hard about this reward function question.

Nope!

For example, see:

*   [“The Era of Experience” has an unsolved technical alignment problem (2025)](https://www.lesswrong.com/posts/TCGgiJAinGgcMEByt/the-era-of-experience-has-an-unsolved-technical-alignment), where I discuss a cursory and flawed analysis of reward functions by David Silver & Rich Sutton;
*   [LeCun’s “A Path Towards Autonomous Machine Intelligence” has an unsolved technical alignment problem (2023)](https://www.lesswrong.com/posts/C5guLAx7ieQoowv3d/lecun-s-a-path-towards-autonomous-machine-intelligence-has-1), where I discuss a cursory and flawed analysis of (related) “intrinsic cost modules” by Yann LeCun
*   [Book review: “A Thousand Brains” (2021)](https://www.lesswrong.com/posts/ixZLTmFfnKRbaStA5/book-review-a-thousand-brains-by-jeff-hawkins), where I discuss a cursory and flawed analysis of the (related) “old brain” by Jeff Hawkins

…And those are *good* ones, by the standards of this field! Their proposals are fundamentally doomed, but at least it occurred to them to have a proposal at all. So hats off to them—because most researchers in RL and NeuroAI don’t even get that far.

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/TCGgiJAinGgcMEByt/llvwqe31jbuluy4n8nxv)

Let’s all try to do better! Going back to that Venn diagram above…

Reward Function Design: Neuroscience research directions
========================================================

For the “reward functions in biology” part, a key observation is that the *human* brain reward function leads to compassion, norm-following, and so on—at least, sometimes. How does that work?

If we can answer that question, it might be a jumping-off point for AGI reward functions.

I worked on this neuroscience problem for years, and wound up with some hypotheses. See [Neuroscience of human social instincts: a sketch](https://www.lesswrong.com/posts/kYvbHCDeMTCTE9TAj/neuroscience-of-human-social-instincts-a-sketch) for where I’m at. But it needs much more work, especially [connectomic](https://www.lesswrong.com/posts/ybmDkJAj3rdrrauuu/connectomics-seems-great-from-an-ai-x-risk-perspective) and other experimental data to ground the armchair hypothesizing.

Reward Function Design: AI research directions
==============================================

Meanwhile on the AI side, there’s been some good work clarifying the problem—for example people talk about inner and outer misalignment and so on—but there’s no good solution. I think we need new ideas. I think people are thinking too narrowly about what reward functions can even look like.

For a snapshot of my own latest thinking on that topic, see my companion post [Reward Function Design: a starter pack](https://www.lesswrong.com/posts/xw8P8H4TRaTQHJnoP/reward-function-design-a-starter-pack).

Bigger picture
==============

To close out, here’s the bigger picture as I see it.

Aligning “RL agent AGI” is different from (and much harder than) aligning the LLMs of today. And the failures will be more like “SkyNet” from Terminator, than like “jailbreaks”. (See [Foom & Doom 2: Technical alignment is hard](https://www.lesswrong.com/posts/bnnKGSCHJghAvqPjS/foom-and-doom-2-technical-alignment-is-hard).)

…But people are trying to make those agents anyway.

We can understand why they’d want to do that. Imagine unlimited copies of Jeff Bezos for $1/hour. You tell one of them to go write a business plan, and found and grow and run a new company, and it goes and does it, very successfully. Then tell the next one, and the next one. This is a quadrillion-dollar proposition. So that’s what people want.

But instead of “Jeff Bezos for $1/hour”, I claim that what they’re gonna get is “a recipe for summoning demons”.

Unless, of course, we solve the alignment problem!

I think things will snowball very quickly, so we need advanced planning. (See [Foom & Doom 1](https://www.lesswrong.com/posts/yew6zFWAKG4AGs3Wk/foom-and-doom-1-brain-in-a-box-in-a-basement).) Building this field of “Reward Function Design” is an essential piece of that puzzle, but there are a great many other things that could go wrong too. We have our work cut out.