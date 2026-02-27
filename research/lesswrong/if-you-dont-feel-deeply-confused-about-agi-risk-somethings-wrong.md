---
title: "If you don't feel deeply confused about AGI risk, something's wrong"
author: "Dave Banerjee"
date: "2026-02-21"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/wWArLinjvJqozJT8f/if-you-don-t-feel-deeply-confused-about-agi-risk-something-s"
score: 85
votes: 45
---

*Epistemic status: I've been thinking about this for a couple months and finally wrote it down. I don't think I'm saying anything new, but I think it's worth repeating loudly. My sample is skewed toward AI governance fellows; I've interacted with fewer technical AI safety researchers, so my inferences are fuzzier there. I more strongly endorse this argument for the governance crowd.*

I've had 1-on-1's with roughly 75 fellows across the ERA, IAPS, GovAI, LASR, and Pivotal fellowships. These are a mix of career chats, research feedback, and casual conversations. I've noticed that in some fraction of these chats, the conversation gradually veers toward high-level, gnarly questions. "How hard is alignment, actually?" "How bad is extreme power concentration, really?"

Near the end of these conversations, I usually say something like: "idk, these questions are super hard, and I struggle to make progress on them, and when I do try my hand at tackling them, I feel super cognitively exhausted, and this makes me feel bad because it feels like a lot of my research and others' research are predicated on answers to these questions."

And then I sheepishly recommend Holden's essays on[ minimal-trust investigations](https://www.cold-takes.com/minimal-trust-investigations/) and[ learning by writing](https://www.cold-takes.com/learning-by-writing/). And then I tell them to actually do the *thing*.

The thing
=========

By "the thing," I mean something like developing a first-principles understanding of *why* you believe AI is dangerous, such that you could reconstruct the argument from scratch without appealing to authority. Concretely, this might look like:

*   Being able to coherently walk someone through at least one AI x-risk threat model, at a[ gears level](https://www.lesswrong.com/w/gears-level)
*   Being able to simulate a top alignment researcher's worldview well enough that you could predict their takes on novel questions
*   Writing down your own threat model and noticing where you get stuck, where you're confused, where you're deferring

I think a large fraction of researchers in AI safety/governance fellowships cannot do any of these things. Here's the archetype:

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/cac3119ef9c6216858d2093d04194d7c9f2f2875b981928a.png)

If this describes you, you are likely in the modal category. FWIW, this archetype is basically me, so I'm also projecting a bit!

Why this happens
================

I think the default trajectory of an AI safety/governance fellow is roughly: absorb the vibes, pick a project, execute, produce output. The "step back and build a first-principles understanding" phase gets skipped, and it gets skipped for predictable, structural reasons:

*   **Time pressure.** Fellowships are 8-12 weeks. That's barely enough time to get a research project off the ground, let alone interrogate your foundational assumptions. There's no time, just sprint sprint sprint!
*   **Mentorship structure.** Most fellowships pair you with a mentor who has a specific research agenda. The implicit (sometimes explicit) deal is: work on something in my agenda. This is often great for learning research skills! But it's not really compatible with "I spent three weeks questioning whether this whole frame is right." The incentive is to be a good mentee, which means executing on a well-scoped project, not pulling at foundational threads. This doesn't always happen though—it seems like a decent chunk of mentors let their fellows do roughly whatever they want.
*   **Legibility incentives.** The point of a fellowship is to get you a job! A concrete paper or report is legible, and this is a very useful signal to future employers. During a job application, it's hard to get by just saying "I developed a much more nuanced understanding of when alignment is hard" (although I think that orgs with good hiring practices would positively reward such a proclamation! I'm not sure if all orgs are like this but I get the sense that it's hard to screen for these things).
*   **Social pressure.** It feels deeply uncomfortable to be participating in an elite AI x-risk fellowship and tell your peer, manager, or mentor: "idk why ASI poses an existential risk." There's a kind of adverse selection in who communicates confusion. The people who are most confused are the least likely to say so, because saying so feels like admitting you don't belong.

That said, I think a valid counterargument is: maybe the best way to build an inside view is to just *do a ton of research*. If you just work closely with good mentors, run experiments, hit dead ends, then the gears-level understanding will naturally emerge.

I think this view is partially true. Many researchers develop their best intuitions through the research process, not before it. And the fellowship that pressures people to produce output is probably better, on the margin, than one that produces 30 deeply confused people and zero papers. I don't want to overcorrect. The right answer is probably "more balance" rather than "eliminate paper/report output pressure."

Why it matters
==============

In most research fields, it's fine to not do the *thing*. You can be a productive chemist without having a first-principles understanding of why chemistry matters. Chemistry is mature and paradigmatic. The algorithm for doing useful work is straightforward: figure out what's known, figure out what's not, run experiments on the unknown.

AI safety doesn't work like this. We're not just trying to advance a frontier of knowledge. We're trying to do the research with the highest chance of reducing P(doom), in a field that's still pre-paradigmatic, where the feedback loops are terrible and the basic questions remain unsettled. If you're doing alignment research and you can't articulate why you think alignment is hard, you're building on a foundation you haven't examined. You can't tell whether your project actually matters. You're optimizing for a metric you can't justify.

You can get by for a while by simply deferring to 80,000 Hours and Coefficient Giving's recommendations. But deferral has a ceiling, and the most impactful researchers are the ones who've built their own models and found the pockets of alpha.

And I worry that this problem will get *worse* over time. As we get closer to ASI, the pressure to race ahead with your research agenda without stepping back will only intensify. The feeling of urgency will crowd out curiosity. And the field will become increasingly brittle precisely when it most[ needs to be intellectually nimble](https://willmacaskill.substack.com/p/effective-altruism-in-the-age-of).

What should you do?
===================

**If you don't feel deeply**[** confused**](https://philarchive.org/rec/GREC-38) **about AI risk, something is wrong.** You've likely not[ stared into the abyss](https://www.benkuhn.net/abyss/) and confronted your assumptions. The good news is that there are concrete things you can do. The bad news is that none of them are easy. They all require intense cognitive effort and time.

*   **Strategy 1: Write your own threat model from scratch.** Sit down with a blank document and try to write a coherent argument for why AI poses an existential risk. Don't consult references. Just write what you actually believe and why. You will get stuck. The places where you get stuck are the most valuable information you'll get from this exercise. Those are the load-bearing assumptions you've been deferring on. Once you've identified them, you can actually go investigate them.
*   **Strategy 2: Learn to simulate a senior researcher.** Pick someone with a lot of public writing (e.g., Paul Christiano, Richard Ngo, Eliezer Yudkowsky, Joe Carlsmith). Dedicate maybe 5 hours per week to reading their work very carefully, taking extensive notes. Keep a running doc with all your open questions and uncertainties. The goal is to be able to predict what they'd say about a novel question and, crucially, to understand *why* they'd say it. This is different from building your own inside view, but it's a useful complement. You learn a lot about the structure of the problem by trying to inhabit someone else's model of it.
*   **Strategy 3: Set a concrete confusion-reduction goal.** By the end of your fellowship, you should be able to coherently explain at least one AI x-risk threat model to a smart person outside the field. Not "AI might be dangerous because Eliezer says so" but an actual mechanistic story. If you can't do this after 8-12 weeks of intensive engagement with AI safety, that's a signal worth paying attention to.

For fellowship directors and research managers, I'd suggest making space for this.[^pwncpxhf57k] One thing that could be useful is to encourage fellows to set a concrete confusion-reduction goal like what I've described above, in addition to the normal fellowship goals like networking and research.

Concluding thoughts
===================

I don't want this post to read as "you should feel bad." The point is that confusion is undervalued and undersupplied in this field. Noticing that you can't reconstruct your beliefs from scratch isn't a failure in itself. It's only bad if you don't do anything about it!

I'm still working on this problem myself. And I imagine many others are too.

[^pwncpxhf57k]: Though I assume that fellowship directors have noticed this issue and have tried to solve the problem and it turned out that solving it is hard.