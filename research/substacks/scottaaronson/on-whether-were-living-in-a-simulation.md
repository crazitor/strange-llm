---
title: "On whether we’re living in a simulation"
author: "Scott Aaronson"
date: "Wed, 07 Feb 2024"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=7774"
---

**Unrelated Announcement (Feb. 7):** Huge congratulations to longtime friend-of-the-blog John Preskill for [winning the 2024 John Stewart Bell Prize](https://cqiqc.physics.utoronto.ca/news/recent-news/john-preskill-announced-as-2024-bell-prize-winner/) for research on fundamental issues in quantum mechanics!

* * *

On the heels of [my post on the fermion doubling problem](https://scottaaronson.blog/?p=7705), I'm sorry to spend even _more_ time on the simulation hypothesis. I promise this will be the last for a long time.

Last week, I attended a philosophy-of-mind conference called [MindFest](https://www.fau.edu/future-mind/mindfest/) at Florida Atlantic University, where I talked to Stuart Hameroff (Roger Penrose's collaborator on the ["Orch-OR"](https://en.wikipedia.org/wiki/Orchestrated_objective_reduction) theory of microtubule consciousness) and many others of diverse points of view, and also gave a talk on "The Problem of Human Specialness in the Age of AI," for which I'll share a transcript soon.

Oh: and I participated in a panel with the philosopher [David Chalmers](https://en.wikipedia.org/wiki/David_Chalmers) about … wait for it … whether we're living in a simulation. I'll link to a video of the panel if and when it's available. In the meantime, I thought I'd share my brief prepared remarks before the panel, despite the strong overlap with my [previous post](https://scottaaronson.blog/?p=7705). Enjoy!

* * *

When someone asks me whether I believe I'm living in a computer simulation--as, for some reason, they do every month or so--I answer them with a question:

> Do you mean, am I being simulated in some way that I could hope to learn more about by examining actual facts of the empirical world?

If the answer is no--that I should expect never to be able to tell the difference even in principle--then my answer is: look, I have a lot to worry about in life. Maybe I'll add this as #4,385 on the worry list.

If they say, maybe you should live your life differently, just from knowing that you _might_ be in a simulation, I respond: I can't quite put my finger on it, but I have a vague feeling that this discussion predates the 80 or so years we've had digital computers! Why not just join the theologians in that earlier discussion, rather than pretending that this is something distinctive about computers? Is it relevantly different here if you're being dreamed in the mind of God or being executed in Python? OK, maybe you'd prefer that the world was created by a loving Father or Mother, rather than some nerdy transdimensional adolescent trying to impress the other kids in programming club. But if that's the worry, why are you talking to a computer scientist? Go talk to David Hume or something.

But suppose instead the answer is yes, we _can_ hope for evidence. In that case, I reply: out with it! What _is_ the empirical evidence that bears on this question?

If we were all to see the Windows [Blue Screen of Death](https://en.wikipedia.org/wiki/Blue_screen_of_death) plastered across the sky--or if I were to hear a voice from the burning bush, saying "go forth, Scott, and free your fellow quantum computing researchers from their bondage"--of course I'd need to update on that. I'm not betting on those events.

Short of that--well, you can look at existing physical theories, like general relativity or quantum field theories, and ask how hard they are to simulate on a computer. You can actually make progress on such questions. Indeed, I recently [blogged about](https://scottaaronson.blog/?p=7705) one such question, which has to do with "chiral" Quantum Field Theories (those that distinguish left-handed from right-handed), including the Standard Model of elementary particles. It turns out that, when you try to put these theories on a lattice in order to simulate them computationally, you get an extra symmetry that you don't want. There's progress on how to get around this problem, including simulating a higher-dimensional theory that contains the chiral QFT you want on its boundaries. But, OK, maybe all this only tells us about simulating _currently-known_ physical theories--rather than the _ultimate_ theory, which a-priori might be easier _or_ harder to simulate than currently-known theories.

Eventually we want to know: can the final theory, of quantum gravity or whatever, be simulated on a computer--at least probabilistically, to any desired accuracy, given complete knowledge of the initial state, yadda yadda? In other words, is the [Physical Church-Turing Thesis](https://arxiv.org/abs/1102.1612) true? This, to me, is close to the outer limit of the sorts of questions that we could hope to answer scientifically.

My personal belief is that the deepest things we've learned about quantum gravity--including about the Planck scale, and the Bekenstein bound from black-hole thermodynamics, and AdS/CFT--all militate toward the view that the answer is "yes," that in some sense (which needs to be spelled out carefully!) the physical universe really _is_ a giant Turing machine.

Now, Stuart Hameroff (who we just heard from this morning) and Roger Penrose believe that's wrong. They believe, not only that there's some uncomputability at the Planck scale, unknown to current physics, but that this uncomputability can somehow affect the microtubules in our neurons, in a way that causes consciousness. I don't believe them. Stimulating as I find their speculations, I get off their train to Weirdville way before it reaches its final stop.

But as far as the Simulation Hypothesis is concerned, that's not even the main point. The main point is: suppose for the sake of argument that Penrose and Hameroff were right, and physics _were_ uncomputable. Well, why shouldn't our universe be simulated by a larger universe that _also_ has uncomputable physics, the same as ours does? What, after all, is the halting problem to God? In other words, while the discovery of uncomputable physics would tell us something profound about the _character_ of any mechanism that could simulate our world, _even that_ wouldn't answer the question of whether we were living in a simulation or not.

Lastly, what about the famous [argument](https://simulation-argument.com/) that says, our descendants are likely to have so much computing power that simulating 1020 humans of the year 2024 is chickenfeed to them. Thus, we should expect that almost all people with the sorts of experiences we have who will ever exist _are_ one of those far-future sims. And thus, presumably, _you_ should expect that _you 're_ almost certainly one of the sims.

I confess that this argument never felt terribly compelling to me--indeed, it always seemed to have a strong aspect of sawing off the branch it's sitting on. Like, our distant descendants will surely be able to simulate _some_ impressive universes. But because their simulations will have to run on computers that fit in _our_ universe, presumably the simulated universes will be _smaller_ than ours--in the sense of fewer bits and operations needed to describe them. Similarly, if we're being simulated, then presumably it's by a universe _bigger_ than the one we see around us: one with more bits and operations. But in that case, it wouldn't be our own descendants who were simulating us! It'd be beings in that larger universe.

(Another way to understand the difficulty: in the original Simulation Argument, we quietly assumed a "base-level" reality, of a size matching what the cosmologists of our world see with their telescopes, and then we "looked down" from that base-level reality into imagined realities being simulated in it. But we should also have "looked up." More generally, we presumably should've started with a Bayesian prior over where we might be in some great chain of simulations of simulations of simulations, then updated our prior based on observations. But we don't _have_ such a prior, or at least I don't--not least because of the infinities involved!)

Granted, there are all sorts of possible escapes from this objection, assumptions that can make the Simulation Argument work. But these escapes (involving, e.g., our universe being merely a "low-res approximation," with faraway galaxies not simulated in any great detail) all seem metaphysically confusing. To my mind, the simplicity of the original intuition for why "almost all people who ever exist will be sims" has been undermined.

Anyway, that's why I don't spend much of my own time fretting about the Simulation Hypothesis, but just occasionally agree to speak about it in panel discussions!

But I'm eager to hear from David Chalmers, who I'm sure will be vastly more careful and qualified than I've been.

* * *

In David Chalmers's response, he quipped that the very lack of empirical consequences that makes something bad as a scientific question, makes it good as a philosophical question--so what I consider a "bug" of the simulation hypothesis debate is, for him, a feature! He then ventured that surely, despite my apparent verificationist tendencies, even I would agree that it's _meaningful to ask_ whether someone is in a computer simulation or not, even supposing it had no possible empirical consequences for that person. And he offered the following argument: suppose _we 're_ the ones running the simulation. Then from _our_ perspective, it seems clearly meaningful to say that the beings in the simulation are, indeed, in a simulation, even if the beings themselves can never tell. So then, unless I want to be some sort of postmodern relativist and deny the existence of absolute, observer-independent truth, I should admit that the proposition that _we 're_ in a simulation is also objectively meaningful--because it would be meaningful to those simulating us.

My response was that, while I'm _not_ a strict verificationist, if the question of whether we're in a simulation were to have no empirical consequences whatsoever, then at most I'd concede that the question was "pre-meaningful." This is a new category I've created, for questions that I neither admit as meaningful nor reject as meaningless, but for which _I 'm willing to hear out someone's argument for why they mean something--and I'll need such an argument!_ Because I already know that the answer is going to look like, "on _these_ philosophical views the question is meaningful, and on _those_ philosophical views it isn't." Actual consequences, either for how we should live or for what we should expect to see, are the ways to make a question meaningful to everyone!

Anyway, Chalmers had other interesting points and distinctions, which maybe I'll follow up on when (as it happens) I visit him at NYU in a month. But I'll just link to the video when/if it's available rather than trying to reconstruct what he said from memory.
