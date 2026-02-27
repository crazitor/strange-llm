---
title: "My AGI safety research—2025 review, ’26 plans"
author: "Steven Byrnes"
date: "2025-12-11"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/CF4Z9mQSfvi99A3BR/my-agi-safety-research-2025-review-26-plans"
score: 133
votes: 42
---

*Previous:* [*2024*](https://www.lesswrong.com/posts/2wHaCimHehsF36av3/my-agi-safety-research-2024-review-25-plans)*,* [*2022*](https://www.lesswrong.com/posts/qusBXzCpxijTudvBB/my-agi-safety-research-2022-review-23-plans)

*“Our greatest fear should not be of failure, but of succeeding at something that doesn't really matter.” –*[*attributed to DL Moody*](https://www.goodreads.com/quotes/390887-our-greatest-fear-should-not-be-of-failure-but-of)[^cuzy57cq5u]

1\. Background & threat model
=============================

The main threat model I’m working to address is the same as it’s been since I was hobby-blogging about AGI safety in 2019. Basically, I think that:

*   The “secret sauce” of human intelligence is a big [uniform-ish](https://www.lesswrong.com/posts/wBHSYwqssBGCnwvHg/intro-to-brain-like-agi-safety-2-learning-from-scratch-in#2_5_3__Uniformity__evidence) learning algorithm centered around the cortex;
*   This learning algorithm is different from and more powerful than LLMs;
*   Nobody knows how it works today;
*   Someone someday will either reverse-engineer this learning algorithm, or reinvent something similar;
*   And then we’ll have Artificial General Intelligence (AGI) and superintelligence (ASI).

I think that, when this learning algorithm is understood, it will be easy to get it to do powerful and impressive things, and to make money, as long as it’s weak enough that humans can keep it under control. But past that stage, we’ll be relying on the AGIs to have good motivations, and not be egregiously misaligned and scheming to take over the world and wipe out humanity. Alas, I claim that the latter kind of motivation is what we should expect to occur, in the absence of yet-to-be-invented techniques to avoid it.

Inventing those yet-to-be-invented techniques constitutes **the technical alignment problem for brain-like AGI**. That’s the main thing I’ve been working on since I’ve been in the field. See my [Intro to Brain-Like-AGI Safety (2022)](https://www.lesswrong.com/s/HzcM2dkCq7fwXBej8).

I think of brain-like AGI as belonging to the broad algorithm class known as “RL agents”, and more specifically a (not-yet-invented) variation on actor-critic model-based RL. (See [Valence series §1.2](https://www.lesswrong.com/posts/As7bjEAbNpidKx6LR/valence-series-1-introduction#1_2_Model_based_reinforcement_learning__RL_)–[§1.3](https://www.lesswrong.com/posts/As7bjEAbNpidKx6LR/valence-series-1-introduction#1_3_Actor_critic_RL__and__valence_).) In terms of the technical alignment problem, I claim that it has somewhat more in common with the “RL agents” that learned to play Atari and Go in the 2010s, than with the LLMs of the 2020s.

+++ More on my path-to-impact

(*mostly copied from* [*last year*](https://www.lesswrong.com/posts/2wHaCimHehsF36av3/my-agi-safety-research-2024-review-25-plans)*)*

*   **Why work on that, rather than LLMs?**
    *   My diplomatic answer is: we don’t have AGI yet ([by my definition](https://www.lesswrong.com/posts/uxzDLD4WsiyrBjnPw/artificial-general-intelligence-an-extremely-brief-faq)), and thus we don’t know for sure what algorithmic form it will take. So we should be hedging our bets, by different AGI safety people contingency-planning for different possible AGI algorithm classes. And the brain-like model-based RL scenario seems *even more* under-resourced right now than the LLM scenario, by far.
    *   My undiplomatic answer is: It’s hard to be certain, but I’m guessing that LLM-like training paradigms will plateau before they get to (my definition of) AGI. They will lead to ever-more-amazing tools, but not a new intelligent species that could run the world by itself. And then eventually, for better or worse, the brain-like approaches will come online. Granted, LLMs haven’t plateaued yet. But any day now, right? See [AI doom from an LLM-plateau-ist perspective](https://www.lesswrong.com/posts/KJRBb43nDxk6mwLcR/ai-doom-from-an-llm-plateau-ist-perspective).
*   **How might my ideas make their way from blog posts into future AGI source code?** Well, again, there’s a scenario (threat model) for which I’m contingency-planning, and it involves future researchers who are inventing brain-like model-based RL, for better or worse. Those researchers will find that they have a slot in their source code repository labeled “reward function”, and they won’t know what to put in that slot to get good outcomes, as they get towards human-level capabilities and beyond. During *earlier* development, with rudimentary AI capabilities, I expect that the researchers will have been doing what model-based RL researchers are doing today, and indeed what they have *always* done since the invention of RL: messing around with obvious reward functions, and trying to get results that are somehow impressive. And if the AI engages in [specification gaming](https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/) or other undesired behavior, then they turn it off, try to fix the problem, and try again. But, [as AGI safety people know well](https://www.lesswrong.com/posts/TCGgiJAinGgcMEByt/the-era-of-experience-has-an-unsolved-technical-alignment#2_2_Background_2___The_usual_agent_debugging_loop___and_why_it_will_eventually_catastrophically_fail), that particular debugging loop will eventually stop working, and instead start failing in a catastrophically dangerous way. Assuming the developers notice that problem before it’s too late, they might look to the literature for a reward function (and associated training environment etc.) that will work in this new capabilities regime. Hopefully, when they go looking, they will find a literature that will *actually exist*, and be full of clear explanations and viable ideas. So that’s what I’m working on. I think it’s a very important piece of the puzzle, even if many other unrelated things can *also* go wrong on the road to (hopefully) Safe and Beneficial AGI.




+++

2\. The theme of 2025: trying to solve the technical alignment problem
======================================================================

As 2025 began, I had just published [Neuroscience of human social instincts: a sketch](https://www.lesswrong.com/posts/kYvbHCDeMTCTE9TAj/neuroscience-of-human-social-instincts-a-sketch), which represented huge progress (years in the making) on my understanding of how prosocial human innate drives might work in the brain—drives like compassion and norm-following, which seem potentially alignment-relevant. Having done that, I sensed diminishing returns on puzzling over neuroscience. It was time to take the knowledge I already had, and apply it to the technical alignment problem directly!

That was my plan for 2025 (see [last year’s review](https://www.lesswrong.com/posts/2wHaCimHehsF36av3/my-agi-safety-research-2024-review-25-plans#2__My_plans_going_forward)), and that’s what I did.

If my 2024 research felt like zipping down a street, then my 2025 research felt like laboriously wading through mud, waist deep.

It turns out that “figuring out things in neuroscience” (what I was mostly doing in 2024) is much easier and more immediately satisfying for me than “using that knowledge to try to solve the technical AGI alignment problem” (my activity in 2025).[^vnv1h6szxg] But the technical AGI alignment problem is where the utils are. So, into the mud I went.

To keep my spirits up, throughout 2025, I kept up a list of things that I (think I) know now, that I didn’t know in 2024. And that list got pretty long!

So, here at the end of 2025, I am still in the waist-deep mud. But I’m in a noticeably different part of the mud from where I was 12 months ago. Yay!

3\. Two sketchy plans for technical AGI alignment
=================================================

[Since at least 2022](https://www.lesswrong.com/posts/Sd4QvG4ZyjynZuHGt/intro-to-brain-like-agi-safety-12-two-paths-forward), I’ve had two general ideas in my head for what a solution to technical AGI alignment might look like:

*   PLAN TYPE 1: We could intervene on the AGI’s object-level desires—we make it want to be subservient, or want to follow the law, or want to invent a better solar cell, etc.—by doing something like [Plan for mediocre alignment of brain-like \[model-based RL\] AGI (2023)](https://www.lesswrong.com/posts/Hi7zurzkCog336EC2/plan-for-mediocre-alignment-of-brain-like-model-based-rl-agi);
*   PLAN TYPE 2: We could intervene on the AGI’s reward function (which is upstream of its desires), by reverse-engineering human social instincts and putting them (or something inspired by them) into the AGI. After all, humans have human social instincts, and at least a few humans turn out wise and kind. That seems to be an existence proof that a plan like this could work in principle.[^g8vyo5vh777]

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/Sd4QvG4ZyjynZuHGt/floft4tung9m3zlzuffj)

The blue and red correspond to “Plan Type 2” and “Plan Type 1”, respectively. Source: [Intro series §12 (2022)](https://www.lesswrong.com/posts/Sd4QvG4ZyjynZuHGt/intro-to-brain-like-agi-safety-12-two-paths-forward)

My current take is that both of these types of plans have severe issues, which might or might not be solvable at all. Alas, I don’t have any better ideas. Guess I still got my work cut out.

(I figured out partway through the year that, if you think about it right, these are not two wholly different types of plans, but more like two points on a spectrum—see discussion in [Perils of under- vs over-sculpting AGI desires](https://www.lesswrong.com/posts/grgb2ipxQf2wzNDEG/perils-of-under-vs-over-sculpting-agi-desires). But knowing that didn’t really help me. I kinda think the whole spectrum stinks.)

For both these types of plans, there are a bunch of things I’m still confused about (albeit fewer than a year ago!), and a bunch of design space that I have not yet explored. But in case anyone is interested, my (*very provisional!*) top concerns in brief are:

*   PLAN TYPE 1 (see Thrust D below): I really don’t like how this plan seems to clash with continuous learning, distribution shifts, and [concept extrapolation](https://www.lesswrong.com/s/u9uawicHx7Ng7vwxA). Also, I’m generally a bit unnerved by how it’s such an alien motivation system, very different from any agent that has ever existed. (Also, the whole thing just feels like a hacky mess.)
*   PLAN TYPE 2 (see Thrusts B–C below): Probably my single biggest concern right now is that maybe human social instincts really only have the effects we’d want them to have, when they’re in an agent running at human speed, embedded in a human society, with some balance-of-power—and not just during training but for as long as it’s running. And I’m concerned that it’s not feasible to make AGIs with anything analogous to that. (Also, again, the whole thing just feels like a hacky mess.)

(Separately, in terms of AGI consciousness and “successor species” kinds of considerations, I think Plan Type 2 seems the better of the two (see e.g. [here](https://www.lesswrong.com/posts/8YhjpgQ2eLfnzQ7ec/response-to-nostalgebraist-proudly-waving-my-moral#3___Wanting_some_kind_of_feeling_of_friendship__compassion__or_connection_to_exist_at_all_in_the_distant_future__seems__1__important___2__not_the__conditioners__thing___3__not_inevitable)), but I’m not sure about that either.)

4\. On to what I’ve actually been doing all year!
=================================================

I’ll divide my activities into eight “thrusts”.

Thrust A: Fitting technical alignment into the bigger strategic picture
-----------------------------------------------------------------------

As I turned to the technical alignment problem, I had to deal with all the big-picture problems that it relates to. Am I worried about AGI that egregiously schemes about how to wipe out humanity, or about AGI that makes subtler philosophical mistakes and goes off the rails, or something else? What am I hoping that AGI developers do with their AGIs anyway—pivotal acts, obedience, alignment research, what? Why are so many alignment researchers so much more optimistic than me—for example, assigning probabilities as high as 50%, or even higher, to the proposition that humanity will survive superintelligence?[^62j1gdsp7px]

After a couple years with my nose in the neuroscience textbooks, I had a backlog of these kinds of questions, and so I set about trying to better understand the cruxes of my disagreements with other alignment people.

**The first output** of this crux-mapping effort was a post on timelines & takeoff ([Foom & Doom 1: “Brain in a box in a basement”](https://www.lesswrong.com/posts/yew6zFWAKG4AGs3Wk/foom-and-doom-1-brain-in-a-box-in-a-basement)), explaining why I expect very fast takeoffs and singleton ASI, for better or worse.

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/yew6zFWAKG4AGs3Wk/vuao4fklpe5cictsl3u9)

Source: [Foom & Doom 1](https://www.lesswrong.com/posts/yew6zFWAKG4AGs3Wk/foom-and-doom-1-brain-in-a-box-in-a-basement)

**The second output** was a post on the difficulty of technical alignment: [Foom & Doom 2: Technical alignment is hard](https://www.lesswrong.com/posts/bnnKGSCHJghAvqPjS/foom-and-doom-2-technical-alignment-is-hard). The title says it all. A big focus of this post was why I am not relieved by the fact that we can make today’s LLMs often helpful and cooperative.

**The third output** was intended to be something about multipolar AGI scenarios, including offense-defense balance and so on.[^0kagom4y6uf] I wound up with a bunch of notes but much lingering confusion. But by then I had written up “Foom & Doom 1” above, and was more strongly expecting an ASI Singleton, and was figuring that the multipolar stuff was probably moot. So I decided to give up for now, and spend my time elsewhere. Sorry! But check out [this comment about “conservation of wisdom”](https://www.lesswrong.com/posts/pZhEQieM9otKXhxmd/gradual-disempowerment-systemic-existential-risks-from?commentId=Eb5HgqyqT5uAye484) for a little glimpse of one of the things I was thinking about.

So that was my crux-mapping project.

One other little thing that fits into Thrust A was writing [Reward Button Alignment](https://www.lesswrong.com/posts/JrTk2pbqp7BFwPAKw/reward-button-alignment), which (among other things) explains my skepticism that there will ever be immediate economic pressure for profit-maximizing companies to do the most important kind of AI alignment research.

Thrust B: Better understanding how RL reward functions can be compatible with non-ruthless-optimizers
-----------------------------------------------------------------------------------------------------

This thrust is where I feel proudest of hard-won conceptual / “deconfusion” progress during 2025.

Taking things in reverse order, I ended the year on a call-to-action post:

*   [We need a field of Reward Function Design](https://www.lesswrong.com/posts/oxvnREntu82tffkYW/we-need-a-field-of-reward-function-design)

and a companion post summarizing where I’m at:

*   [Reward Function Design: a starter pack](https://www.lesswrong.com/posts/xw8P8H4TRaTQHJnoP/reward-function-design-a-starter-pack)

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/oxvnREntu82tffkYW/v25eihscdvgt0rmthwwp)

Source: [We need a field of Reward Function Design](https://www.lesswrong.com/posts/oxvnREntu82tffkYW/we-need-a-field-of-reward-function-design)

The latter includes a glossary of many relevant terms and concepts, all of which I made up or started using in 2025, and which I now find indispensable for thinking about RL reward function design. Those terms and concepts were fleshed out over the course of 2025 via the following posts:

*   [Self-dialogue: Do behaviorist rewards make scheming AGIs?](https://www.lesswrong.com/posts/SFgLBQsLB3rprdxsq/self-dialogue-do-behaviorist-rewards-make-scheming-agis)
*   …which I later cleaned up and shortened to: [“Behaviorist” RL reward functions lead to scheming](https://www.lesswrong.com/posts/FNJF3SoNiwceAQ69W/behaviorist-rl-reward-functions-lead-to-scheming)
*   [Perils of under- vs over-sculpting AGI desires](https://www.lesswrong.com/posts/grgb2ipxQf2wzNDEG/perils-of-under-vs-over-sculpting-agi-desires)
*   [6 reasons why “alignment-is-hard” discourse seems alien to human intuitions, and vice-versa](https://www.lesswrong.com/posts/d4HNRdw6z7Xqbnu5E/6-reasons-why-alignment-is-hard-discourse-seems-alien-to)

Also part of Thrust B is an [important correction](https://www.lesswrong.com/posts/LaeP39jJpfPyoiSZm/valence-series-4-valence-and-liking-admiring#4_5_1_Path_1___I_like___admire_Alice_____Alice_likes_X_____I_like_X_____I_try_to_do_X_) to my 2024 post [\[Valence series\] 4. Valence & Liking / Admiring](https://www.lesswrong.com/posts/LaeP39jJpfPyoiSZm/valence-series-4-valence-and-liking-admiring), and [an important addition](https://www.lesswrong.com/posts/btHmC88KCZdzimBCM/steve-byrnes-s-shortform?commentId=a2TExi8ftCSQyZhBz) to my 2022 post [\[Intro to brain-like-AGI safety\] 10. The alignment problem](https://www.lesswrong.com/posts/wucncPjud27mLWZzQ/intro-to-brain-like-agi-safety-10-the-alignment-problem).

Another 2025 Thrust B post—albeit more about outreach / pedagogy than about new progress—is the beginner-friendly [“The Era of Experience” has an unsolved technical alignment problem](https://www.lesswrong.com/posts/TCGgiJAinGgcMEByt/the-era-of-experience-has-an-unsolved-technical-alignment), which responds to a book chapter by Rich Sutton & David Silver.

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/TCGgiJAinGgcMEByt/llvwqe31jbuluy4n8nxv)

Source: [“The Era of Experience” has an unsolved technical alignment problem](https://www.lesswrong.com/posts/TCGgiJAinGgcMEByt/the-era-of-experience-has-an-unsolved-technical-alignment)

Overall, as mentioned in [Reward Function Design: a starter pack](https://www.lesswrong.com/posts/xw8P8H4TRaTQHJnoP/reward-function-design-a-starter-pack), I feel like a blind man who has now poked many different parts of the [elephant](https://en.wikipedia.org/wiki/Blind_men_and_an_elephant), and maybe the gestalt whole is starting to come together, especially when combined with the next thrust:

Thrust C: Continuing to develop my thinking on the neuroscience of human social instincts
-----------------------------------------------------------------------------------------

I wrote three posts that follow up from last year’s [Neuroscience of human social instincts: a sketch](https://www.lesswrong.com/posts/kYvbHCDeMTCTE9TAj/neuroscience-of-human-social-instincts-a-sketch) (the post I mentioned in §2 above):

*   [Neuroscience of human sexual attraction triggers (3 hypotheses)](https://www.lesswrong.com/posts/ktydLowvEg8NxaG4Z/neuroscience-of-human-sexual-attraction-triggers-3)
*   [Social drives 1: “Sympathy Reward”, from compassion to dehumanization](https://www.lesswrong.com/posts/KuBiv9cCbZ6ALjHFw/social-drives-1-sympathy-reward-from-compassion-to)
*   [Social drives 2: “Approval Reward”, from norm-enforcement to status-seeking](https://www.lesswrong.com/posts/fPxgFHfs5yHzYqgG7/social-drives-2-approval-reward-from-norm-enforcement-to)

I think of these as being in increasing order of importance. In particular, Social Drives 1 & 2, along with [6 reasons why “alignment-is-hard” discourse seems alien to human intuitions, and vice-versa](https://www.lesswrong.com/posts/d4HNRdw6z7Xqbnu5E/6-reasons-why-alignment-is-hard-discourse-seems-alien-to), are part of my attempt to think through what would happen if we made an AGI with something like human social instincts.

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/KuBiv9cCbZ6ALjHFw/rsgtdhaab5bhxsi2mvtf)

Last year’s [Neuroscience of human social instincts: a sketch](https://www.lesswrong.com/posts/kYvbHCDeMTCTE9TAj/neuroscience-of-human-social-instincts-a-sketch) proposed what I called the “compassion / spite circuit”. This year I fleshed out its effects by splitting its reward outputs into four subcomponents, each with a different set of everyday consequences. Image from [Social drives 1](https://www.lesswrong.com/posts/KuBiv9cCbZ6ALjHFw/social-drives-1-sympathy-reward-from-compassion-to).

…And what *would* happen if we made an AGI with something like human social instincts? Sorry, I don’t know yet! That’s the next step. I’ve been laying all these foundations, and hopefully I’m finally equipped to attack that question head-on in 2026.

Thrust D: Alignment implications of continuous learning and concept extrapolation
---------------------------------------------------------------------------------

My [Plan for mediocre alignment of brain-like \[model-based RL\] AGI](https://www.lesswrong.com/posts/Hi7zurzkCog336EC2/plan-for-mediocre-alignment-of-brain-like-model-based-rl-agi) (“Plan Type 1” from §3 above) involves planting desires that we like into the AI at time *t*, and then the AI thinks and learns and gets new options (including [concept extrapolation](https://www.lesswrong.com/s/u9uawicHx7Ng7vwxA)), and we hope that the AI will *still* have desires we like at some much later time. Will that work? If not, what can we do about it?

I discussed this issue in two 2025 posts:

*   [“Sharp Left Turn” discourse: An opinionated review](https://www.lesswrong.com/posts/2yLyT6kB7BQvTfEuZ/sharp-left-turn-discourse-an-opinionated-review)
*   [§8](https://www.lesswrong.com/posts/grgb2ipxQf2wzNDEG/perils-of-under-vs-over-sculpting-agi-desires#8__Perils) of [Perils of under- vs over-sculpting AGI desires](https://www.lesswrong.com/posts/grgb2ipxQf2wzNDEG/perils-of-under-vs-over-sculpting-agi-desires)

Those were meaningful progress, but alas, I still feel quite confused about this topic. I’m not even sure that I stand by everything I wrote in the latter.

I think I have some paths forward, including by dropping all the way down to meta-ethical fundamentals. But I still have my work cut out, and hope to keep puzzling over it in 2026.

Thrust E: Neuroscience odds and ends
------------------------------------

While neuroscience was not a focus of mine for 2025, I still opportunistically dabbled! In particular:

*   Psychology blogger Slime Mold Time Mold wrote a series [The Mind in the Wheel](http://www.mindinthewheel.com/), closely related to (what I call) innate drives. I’m a big fan of studying innate drives in general, but I don’t think Slime Mold Time Mold did a great job with the details. I spent a day or two writing a response: [Re SMTM: negative feedback on negative feedback](https://www.lesswrong.com/posts/LfqFZvfSQhnCXHFE6/re-smtm-negative-feedback-on-negative-feedback).

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/LfqFZvfSQhnCXHFE6/ck8gehpqb5tqvaewsw5q)

My six-ingredient model of how homeostatic feedback control is built into the brain and body. See [Re SMTM: negative feedback on negative feedback](https://www.lesswrong.com/posts/LfqFZvfSQhnCXHFE6/re-smtm-negative-feedback-on-negative-feedback)

*   Over winter break 2024, I read Eric Turkheimer’s then-just-released book [*Understanding the Nature-Nurture Debate*](https://doi.org/10.1017/9781108955775), out of curiosity. This spurred me to spend a week in January thinking about heritability, which resulted in [Heritability: Five Battles](https://www.lesswrong.com/posts/xXtDCeYLBR88QWebJ/heritability-five-battles). This might not sound too relevant to solving the technical alignment problem, but that week I spent on it has actually borne a lot of fruit over the past year.

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/1eae8486927500c7db5413342caf08700d347a860eebafd096a4553f153a28ff/vgbhqbqn9uzhibjbvk8l)

A diagram illustrating my take on why most mental health and personality traits show strong signs of “non-additivity” / “epistasis” in the behavior genetics literature. See [Heritability: Five Battles](https://www.lesswrong.com/posts/xXtDCeYLBR88QWebJ/heritability-five-battles).

*   As my general neuroscience hiatus drags on, I wrote [Excerpts from my neuroscience to-do list](https://www.lesswrong.com/posts/c6Job6zmT3nABBxK6/excerpts-from-my-neuroscience-to-do-list), in case any readers want to pick up one of the balls that I’ve dropped.

Thrust F: Economics of superintelligence
----------------------------------------

Many (not all!) economists are dismissive of superintelligence being possible, or having a big impact even if it appeared tomorrow. I think they’re wrong, and for some strange reason I sometimes feel like arguing with them.

This inclination led to a post [Applying traditional economic thinking to AGI: a trilemma](https://www.lesswrong.com/posts/TkWCKzWjcbfGzdNK5/applying-traditional-economic-thinking-to-agi-a-trilemma), which I later refreshed and expanded into the more click-baity: [Four ways learning Econ makes people dumber re: future AI](https://www.lesswrong.com/posts/xJWBofhLQjf3KmRgg/four-ways-learning-econ-makes-people-dumber-re-future-ai).

Relatedly, I had unusually lengthy twitter arguments about the economics of superintelligence [with Matt Clancy](https://x.com/steve47285/status/1796546304811868171) (in response to [his 80,000 Hours podcast](https://80000hours.org/podcast/episodes/matt-clancy-whether-science-is-good/)), and [with Konrad Kording](https://x.com/steve47285/status/1989679425936351597) (in response to his paper with Ioana Marinescu: [(Artificial) Intelligence saturation and the future of work](https://www.brookings.edu/articles/artificial-intelligence-saturation-and-the-future-of-work/)). I don’t seem to have moved either of them. Oh well; I appreciate their time in any case.

Thrust G: AGI safety miscellany
-------------------------------

*   I aired one of my confusions in a question post: [Inscrutability was always inevitable, right?](https://www.lesswrong.com/posts/ohznigkLX5CNwaLSz/inscrutability-was-always-inevitable-right) I got a bunch of helpful responses, [especially from Connor Leahy](https://www.lesswrong.com/posts/ohznigkLX5CNwaLSz/inscrutability-was-always-inevitable-right?commentId=qqio9JLycaLwf4bbP). Thanks everyone.
*   I wrote a [quick book review of *If Anyone Builds It, Everyone Dies*](https://www.lesswrong.com/posts/btHmC88KCZdzimBCM/steve2152-s-shortform?commentId=vzWgcoP3isSBQbDbe)

Thrust H: Outreach
------------------

Boy, the hope of Safe & Beneficial AGI would feel a lot more promising if there were more people who understood the risks and took them seriously. So I have always spent a bit of my time and energy on outreach, when I find myself in a good position to do so. Some 2025 highlights include:

*   I [started a substack](https://stevebyrnes1.substack.com/) with announcements of new posts, to complement my existing feeds on [RSS](https://www.greaterwrong.com/users/steve2152?show=posts&format=rss), [X (Twitter)](https://x.com/steve47285), and [Bluesky](https://bsky.app/profile/stevebyrnes.bsky.social).
*   I was interviewed on two podcasts (my second and third ever!): [Future of Life Institute podcast with Gus Docker](https://podcast.futureoflife.org/brain-like-agi-and-why-it-s-dangerous-with-steven-byrnes/) and [Doom Debates with Liron Shapira](https://lironshapira.substack.com/p/the-man-who-might-solve-ai-alignment).
*   I extensively revised my standard talk and posted it online at [Video & transcript: Challenges for Safe & Beneficial Brain-Like AGI](https://www.lesswrong.com/posts/YKmyay3bWF2ofAGNo).
*   I attended two conferences and a workshop, and talked to a bunch of people.
*   I heard from a number of people that they wanted to cite the 15-blog-post series [Intro to Brain-Like-AGI Safety](https://www.alignmentforum.org/s/HzcM2dkCq7fwXBej8), but that they were unable or unwilling to put Alignment Forum blog posts into a bibliography. Also I had met a couple people who had printed it out on actual paper! Like paper made from trees! So for both those use-cases, [I converted it to a 200-page PDF and put it on a mainstream preprint server](https://osf.io/preprints/osf/fe36n). Thanks Ash Dorsey for doing all the hard work for the PDF conversion.

5\. Other stuff
===============

**Non-work-related blog posts:** Just for fun, I wrote two in 2025:

*   [Optical rectennas are not a promising clean energy technology](https://www.lesswrong.com/posts/gKCavz3FqA6GFoEZ6/optical-rectennas-are-not-a-promising-clean-energy)
*   [Teaching kids to swim](https://www.lesswrong.com/posts/qiZp8HFvjgS2Rtxgk/teaching-kids-to-swim)

**Personal productivity and workflow:** I’ve gone through a lot of systems over the years, but seem to have settled into a local optimum that works for me (an idiosyncratic system of to-do lists, wall calendars, time-tracking software, checklists, accountability buddy, etc.). The only noticeable changes during 2025 are: (1) I [(re)invented “self-dialogues”](https://www.lesswrong.com/posts/SFgLBQsLB3rprdxsq/self-dialogue-do-behaviorist-rewards-make-scheming-agis#Note_on_the_experimental__self_dialogue__format) as a surprisingly useful way to think through things and make progress when I’m stuck; and (2) I’m using LLMs a bit more, although still probably much less than most people in my field.[^8poo8laks64]

6\. Plan for 2026
=================

My plan for 2026 is the same as my plan for 2025—solve (or make progress towards solving) the technical alignment problem for brain-like AGI, or prove (or make progress towards proving) that no solution exists. This would include pseudocode for reward functions and training environments, and sorting out which aspects can be tested and de-risked in advance and how, and making a plan that fits into a sensible and ethical larger strategic picture, and so on.

The immediate next steps are the two I mentioned under Thrusts C & D above.

In addition to that main project, I plan to continue opportunistically dabbling in neuroscience, outreach, other aspects of AGI safety, and so on, into 2026, as I have in the past.

If someone thinks that I should be spending my time differently in 2026, please reach out and make your case!

7\. Acknowledgements
====================

Thanks Jed McCaleb & [Astera Institute](https://astera.org/) for generously supporting my research since August 2022!

Thanks to all the people who comment on my posts before or after publication, or share ideas and feedback with me through email or [other channels](https://sjbyrnes.com/), and especially those who patiently stick it out with me through long back-and-forths to hash out disagreements and confusions. I’ve learned so much that way![^372p96ezcs9]

Thanks Lightcone Infrastructure ([don’t forget to donate](https://www.every.org/lightcone-infrastructure/f/2026-fundraiser)!) for maintaining and continuously improving this site, which has always been an essential part of my workflow. Thanks to everyone else fighting for Safe and Beneficial AGI, and thanks to my family, and thanks to you all for reading! Happy Holidays!

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/f790ab83a7ce8210d0aed6e828615fdc66fab72deee0e00b.png)

I was thinking: *Hmm, what closing image would convey the message of “Happy holidays everyone!”, while also fitting in with the theme of AGI safety and alignment?* Of course, once stated, [the question answers itself](https://en.wikipedia.org/w/index.php?title=List_of_Futurama_characters&oldid=1326699058#Robot_Santa).

[^cuzy57cq5u]: It’s actually even worse than that—practically everyone working towards Safe & Beneficial AGI thinks that many (or even most) other people working towards Safe & Beneficial AGI are pursuing projects that, if successful, would be not just pointless but in fact making the situation worse. I indeed think that about many other people in the field, and they probably think that about me. …Of course, our positions are not at all parallel, because I’m correct whereas they are incorrect … … (nervous laughter) 

[^vnv1h6szxg]: Reasons why I seem to find neuroscience research much easier than alignment research:Neuroscience questions have tons of already-existing experimental evidence relating to them. Technical AGI alignment … not so much. (Remember, brain-like AGI doesn’t exist yet.)Neuroscience questions have a guarantee that an answer in fact exists. Technical AGI alignment … not so much.Neuroscience questions are like little islands of confusion, in a sea of things I (think I) understand. Technical AGI alignment … not so much. (At least, not yet!)…And so on. 

[^g8vyo5vh777]: To put it more starkly: if it’s possible for humans to develop a system that will ultimately lead to a good future, then it’s presumably also possible for sufficiently human-like AGIs to also develop such a system. Or if it’s not possible for humans to develop such a system, then we’re screwed no matter what. 

[^62j1gdsp7px]: My p(doom) = “y’know those movies where you’re 75% into it, and the hero has lost all his superpowers and been teleported to another dimension with no way of getting back, and the villain is more powerful than ever, and meanwhile the audience is shaking their head and saying to themselves, ‘jeez, how on Earth are the script-writers gonna resolve this one??’ …That’s my p(doom).” 

[^0kagom4y6uf]: …also including deciding whether or not to change anything in my old post What does it take to defend the world against out-of-control AGIs? (2022), which I’ve gone back and forth on many times. 

[^8poo8laks64]: The biggest change between 2024 and 2025 is that I’m now almost always showing my complete drafts to LLMs before publishing, and asking them to find typos, unexplained jargon, things to cut, mistakes, etc. Their advice is still usually bad, but they get some hits. I also use them for coding (e.g. one-off shell scripts), reverse lookup (when I don’t know the name of something), and similar, but not as a thought partner for novel research. 

[^372p96ezcs9]: A couple 2025 examples that spring to mind: my coworker Seth Herd (among many other things) caught a critical mistake in an early draft version of Social Drives 1 & 2 that led to a complete rethink and rewrite; and Sharmake Farah’s patient skeptical questioning in comment threads led directly to my writing Self-dialogue & Reward button alignment. Plus countless ideas and pushback from my awesome collaborators and test-readers, like Adam Marblestone, Jeremy Gillen, Charlie Steiner, Justis Mills, Linda Linsefors, Simon Skade and many others. Many thanks to them and everyone else! :)