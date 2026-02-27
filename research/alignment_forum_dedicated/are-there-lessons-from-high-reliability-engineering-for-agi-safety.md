---
title: "Are there lessons from high-reliability engineering for AGI safety?"
author: "Steven Byrnes"
date: "2026-02-02"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/hiiguxJ2EtfSzAevj/are-there-lessons-from-high-reliability-engineering-for-agi"
score: 118
votes: 48
---

This post is partly a belated response to Joshua Achiam, currently OpenAI’s Head of Mission Alignment:

> If we adopt safety best practices that are common in other professional engineering fields, we'll get there … I consider myself one of the x-risk people, though I agree that most of them would reject my view on how to prevent it. I think the wholesale rejection of safety best practices from other fields is one of the dumbest mistakes that a group of otherwise very smart people has ever made. —[Joshua Achiam on Twitter, 2021](https://x.com/jachiam0/status/1370980495920533506)
> 
> “We just have to sit down and actually write a damn specification, even if it's like pulling teeth. It's the most important thing we could possibly do," said almost no one in the field of AGI alignment, sadly. … I'm picturing hundreds of pages of documentation describing, for various application areas, specific behaviors and acceptable error tolerances … —[Joshua Achiam on Twitter (partly talking to me), 2022](https://x.com/steve47285/status/1609232759100248066?s=20)

As a proud member of the group of “otherwise very smart people” making “one of the dumbest mistakes”, I will explain why I don’t think it’s a mistake. (Indeed, since 2022, some “x-risk people” *have* started working towards these kinds of specs, and I think *they’re* the ones making a mistake and wasting their time!)

At the same time, I’ll describe what I see as the kernel of truth in Joshua’s perspective, and why it should be seen as an indictment not of “x-risk people” but rather of OpenAI itself, along with all the other groups racing to develop AGI.

1\. My qualifications (such as they are)
========================================

I’m not *really* an expert on high-reliability engineering. But I worked from 2015-2021 as a physicist at [an engineering R&D firm](https://www.draper.com), where many of my coworkers were working on building things that *really had to work* in exotic environments—things like [guidance systems for submarine-launched nuclear ICBMs](https://www.draper.com/market-areas/strategic-systems/navy-strategic-systems), or a [sensor & electronics package that needed to operate inside the sun’s corona](https://www.draper.com/media-center/featured-stories/detail/27373/touching-the-sun-with-the-parker-solar-probe).

To be clear, I wasn’t directly working on these kinds of “high-reliability engineering” projects. (I specialized instead in very-early-stage design and feasibility work for [dozens](https://sjbyrnes.com/pub_lidar_cleo_2020.pdf) [of](https://arxiv.org/abs/1804.06535) [weird](https://patents.google.com/patent/US10157692B2/) [system](https://doi.org/10.1364/OE.381575) [concepts](https://patents.google.com/patent/US20200020501A1/en) and associated algorithms.) But my coworkers *were* doing those projects, and over those five years I gained some familiarity with what they were doing on a day-to-day basis and how.

…So yeah, I’m not really an “expert”. But as a [full-time AGI safety & alignment researcher since 2021](https://sjbyrnes.com/agi.html), I’m plausibly among the [“Pareto Best In The World”](https://www.lesswrong.com/posts/XvN2QQpKTuEzgkZHY/being-the-pareto-best-in-the-world)™ at simultaneously understanding both high-reliability engineering best practices and AGI safety & alignment. So here goes!

2\. High-reliability engineering in brief
=========================================

Basically, the idea is:

*   You understand exactly what the thing is supposed to be doing, in every situation that you care about.
*   You understand exactly what situations (environment) the thing needs to work in—temperatures, vibrations, loads, stresses, adversaries trying to mess it up, etc.
*   You have a deep understanding of how the thing works, in the form of models that reliably and legibly flow up from component tolerances etc. to headline performance. And these models firmly predict that the thing is going to work.
    *   (The models also incorporate the probability and consequences of component failures etc.—so it usually follows that the thing needs redundancy, fault tolerance, engineering margins, periodic inspections, etc.)
*   Those models are compared to a wide variety of both detailed numerical simulations (e.g. [finite element analysis](https://en.wikipedia.org/wiki/Finite_element_method)) and physical (laboratory) tests. These tests are designed not to “pass or fail” but rather to spit out tons of data, allowing a wide array of quantitative comparisons with the models, thus surfacing unknown unknowns that the models might be leaving out.
    *   For example, a space project might do vibration tests, centrifuge tests, vacuum tests, radiation exposure, high temperature, low temperature, temperature gradients, and so on.
*   Even after all that, nobody *really* counts on the thing working until there have been realistic full-scale tests, which again not only “pass” but also spit out a ton of measurements that all quantitatively match expectations based on the deep understanding of the system.
    *   (However, I certainly witnessed good conscientious teams make novel things that worked perfectly on the first realistic full-scale attempt—for example, the [Parker Solar Probe component](https://www.draper.com/media-center/featured-stories/detail/27373/touching-the-sun-with-the-parker-solar-probe) worked great, even though they obviously could not do trial-runs of their exact device in outer space, let alone inside the solar corona.)
*   When building the actual thing—assembling the components and writing the code—there’s scrupulous attention to detail, involving various somewhat-onerous systems with lots of box-checking to make sure that nothing slips through the cracks. There would also be testing and inspections as you build it up from components, to sub-assemblies, to the final product. Often specialized software products like [IBM DOORS](https://en.wikipedia.org/wiki/DOORS) are involved. For software, the terms of art are [“verification & validation”](https://en.wikipedia.org/wiki/Software_verification_and_validation), which refer respectively to systematically comparing the code to the design spec, and the design spec to the real-world requirements and expectations.
*   And these systems need to be supported at the personnel level and at the organizational level. The former involves competent people who understand the stakes and care deeply about getting things right even when nobody is watching. The latter involves things like deep analysis of faults and near-misses, red-teaming, and so on. This often applies also to vendors, subcontractors, etc.

3\. Is any of this applicable to AGI safety?
============================================

3.1 In one sense, no, obviously not
-----------------------------------

Let’s say I had a single top-human-level-intelligence AGI, and I wanted to make $250B with it. Well, hmm, Jeff Bezos used his brain to make $250B, so an obvious thing I could do is have my AGI do what Jeff Bezos did, i.e. go off and autonomously found, grow, and run an innovative company.

(If you get off the train here, then see my discussion of [“Will almost all future companies eventually be founded and run by autonomous AGIs?” at this link](https://www.lesswrong.com/posts/LJD4C7KAr64onL8fq/response-to-dileep-george-agi-safety-warrants-planning-ahead#3_2_On__keeping_strong_AI_as_a_tool__not_a_successor___Will_almost_all_future_companies_eventually_be_founded_and_run_by_autonomous_AGIs_).)

Now look at that bulleted list above, and think about how it would apply here. For example: *“You understand exactly what the thing is supposed to be doing, in every situation that you care about.”*

No way.

At my old engineering R&D firm, we knew *exactly* what such-and-such subsystem was supposed to do: it was supposed to output a measurement of Quantity *X*, every *Y* milliseconds, with no more than noise *Z* and drift *W*, so long as it remains within such-and-such environmental parameters. Likewise, a bridge designer knows *exactly* what a bridge is supposed to do: not fall down, nor sway and vibrate more than amplitude *V* under traffic load *U* and wind conditions *T* etc.

…OK, and now what *exactly* is our “AGI Jeff Bezos” supposed to be doing at any given time?

Nobody knows!

Indeed, the fact that nobody knows is the whole point! That’s the very reason that an AGI Jeff Bezos can create so much value!

When Human Jeff Bezos started Amazon in 1994, he was obviously not handed a detailed spec for what to do in any possible situation, where following that spec would lead to the creation of a wildly successful e-commerce / cloud computing / streaming / advertising / logistics / smart speaker / Hollywood studio / etc. business. For example, in 1994, nobody, not Jeff Bezos himself, nor anyone else on Earth, knew how to run a modern cloud computing business, because indeed the very idea of “modern cloud computing business” didn’t exist yet! That business model only came to exist when Jeff Bezos (and his employees) invented it, years later.

By the same token, on any given random future day…

*   Our AGI Jeff Bezos will be trying to perform a task that we can't currently imagine, using ideas and methods that don't currently exist.
*   It will have an intuitive sense of what constitutes success (on this micro-task) that it learned from extensive idiosyncratic local experience, intuitions that a human would need years to replicate.
*   The micro-task will advance some long-term plan that neither we nor even the AGI can yet dream of.
*   This will be happening in the context of a broader world that may be radically different from what it is now.
*   And our AGI Jeff Bezos (along with other AGIs around the world) will be making these kinds of decisions at a scale and speed that makes it laughably unrealistic for humans to be keeping tabs on whether these decisions are good or bad.

…And we’re gonna write a detailed spec for that, analogous to the specs for the sensor and bridge that I mentioned above? And we’re gonna ensure that the AGI will follow this spec by design?

No way. If you believe that, then I think you are utterly failing to imagine a world with actual AGI.

![2-column table contrasting properties of AI as we think of it today, with properties of future AGI that I'm thinking about](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/4basF9w9jaPZpoC8R/cziczguyma3nifu1x3th)

3.2 In a different sense, yes, at least I sure as heck hope so eventually
-------------------------------------------------------------------------

When we build actual AGI, it will be like a new intelligent species on Earth, and one which will eventually be dramatically faster, more numerous, and more competent than humans. If they want to wipe out humans and run the world by themselves, they’ll be able to. (For more on AGI extinction risk in general, see the [80,000 hours intro](https://80000hours.org/problem-profiles/risks-from-power-seeking-ai/), or [my own intro](https://www.lesswrong.com/posts/4basF9w9jaPZpoC8R/intro-to-brain-like-agi-safety-1-what-s-the-problem-and-why).)

Now, my friends on the [Parker Solar Probe project](https://www.draper.com/media-center/featured-stories/detail/27373/touching-the-sun-with-the-parker-solar-probe) were able to run certain tests in advance—radiation tests, thermal tests, and so on—but the first time their sensor went into the actual solar corona, it had to work, with no do-overs.

By the same token, we can run certain tests on future AGIs, in a safe way. But the first time that AGIs are autonomously spreading around the world, and inventing transformative new technologies and ideas, and getting an opportunity to irreversibly entrench their power, those AGIs had better be making decisions we’re happy about, with no do-overs.

All those practices listed in §2 above exist for a reason; they're the only way we even have a chance of getting a system to work the first time in a very new situation. They are not optional nice-to-haves, rather they are the bare minimum to make the task merely “very difficult” rather than “hopeless”. If it seems impossible to apply those techniques to AGI, per §3.1 above, then, well, we better [shut up and do the impossible](https://www.lesswrong.com/posts/nCvvhFBaayaXyuBiD/shut-up-and-do-the-impossible).

What might that look like? How do we get to a place where we have deep understanding, and where this understanding gives us a strong reason to believe that things will go well in the (out-of-distribution) scenarios of concern, and where we have a wide variety of safe tests that can be quantitatively compared with that understanding in order to surface unknown unknowns?

I don't know!

Presumably the “spec” and the tests would be more about the AGI’s motivation, or its disposition, or something, rather than about its object-level actions? Well, whatever it is, we better figure it out.

We're not there today, nor anywhere close.

(And even if we got there, then we would face the *additional* problem that all existing and likely future AI companies seem to have neither the capability, nor the culture, nor the time, nor generally even the desire to do the rigorous high-reliability engineering (§2) for AGI. See e.g. [Six Dimensions of Operational Adequacy in AGI Projects](https://www.lesswrong.com/posts/keiYkaeoLHoKK4LYA/six-dimensions-of-operational-adequacy-in-agi-projects) (Yudkowsky 2017).)

4\. Optional bonus section: Possible objections & responses
===========================================================

**Possible Objection 1:** Your §3.1 is misleading; we don’t need to specify what AGI Jeff Bezos needs to *do* to run a successful innovative business, rather we need to specify what he needs to *not* do, e.g. he needs to *not* break the law.

**My Response:** If you want to say that “don’t break the law” etc. counts as a spec, well, nobody knows how to do the §2 stuff (deep understanding etc.) for “don’t break the law” either.

And yes, we should tackle that problem. But I don’t see any way that a 300-page spec (as suggested by Joshua Achiam at the top) would be helpful for that. In particular:

*   If your roadmap is to make the AGI obey “the letter of the law” for some list of prohibitions, then no matter how long you make the list, a smart AGI trying to get things done [will find and exploit loopholes](https://deepmindsafetyresearch.medium.com/specification-gaming-the-flip-side-of-ai-ingenuity-c85bdb0deeb4), with [catastrophic results](https://www.lesswrong.com/w/nearest-unblocked-strategy).
*   Or if your roadmap is to make the AGI obey “the spirit of the law” for some list of prohibitions, then there’s no point in writing a long list of prohibitions. Just use a one-item “list” that says “Don’t do bad things.” I don’t see why it would be any easier or harder to design an AGI that *reliably* (in the §2 sense) obeys the spirit of that one prohibition, than an AGI that *reliably* obeys the spirit of a 300-page list of prohibitions. (The problem is unsolved in either case.)

**Possible Objection 2:** We only need the §2 stuff (deep understanding etc.) if there are potentially-problematic distribution shifts between test and deployment. If we can do unlimited low-stakes tests of the exact thing that we care about, then we can just do trial-and-error iteration. And we get that for free because AGI will improve gradually. Why do you expect problematic distribution shifts?

**My Response:** See my comments in §3.2, plus maybe my post [“Sharp Left Turn” discourse: An opinionated review](https://www.lesswrong.com/posts/2yLyT6kB7BQvTfEuZ/sharp-left-turn-discourse-an-opinionated-review). Or just think: we’re gonna get to a place where there are millions of telepathically-communicating super-speed-John-von-Neumann-level AGIs around the world, getting sculpted by continual learning for the equivalent of subjective centuries, and able to coordinate, invent new technologies and ideas, and radically restructure the world if they so choose … and you really don’t think there’s any problematic distribution shift between that and your safe sandbox test environment??

So the upshot is: the gradual-versus-sudden-takeoff debate is irrelevant for my argument here. (Although for the record, [I do expect superintelligence to appear more suddenly than most people do](https://www.lesswrong.com/posts/yew6zFWAKG4AGs3Wk/foom-and-doom-1-brain-in-a-box-in-a-basement).)

Maybe an analogy is: if you’re worried that a nuclear weapon with yield *Y* might [ignite the atmosphere](https://en.wikipedia.org/w/index.php?title=Effects_of_nuclear_explosions&oldid=1333919751#Atmospheric_ignition), it doesn’t help to first test a nuclear weapon with yield 0.1×*Y*, and then if the atmosphere hasn’t been ignited yet, next try testing one with yield 0.2×*Y*, etc.