---
title: "Fighting Hype with Hype"
author: "Scott Aaronson"
date: "Sun, 06 Jun 2010"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=449"
---

I've been depressed all month about the oil spill.  So what better to cheer me up than a flurry of comments and emails asking me to comment on an [_Ars Technica_ story](http://arstechnica.com/science/news/2010/06/magic-quantum-wand-does-not-vanish-hard-maths.ars) by Chris Lee, reporting that it's now been proven once and for all that quantum computers don't help with NP-complete problems?

> Now, just to really put the screws on any optimists out there, a new paper has shown that adiabatic computers are actually quite bad at hard math problems …
> 
> What [the researchers] have shown is that, when adiabatic quantum computers are used to solve NP-complete problems, the energy gap between the lowest energy state and the next state up is not well behaved. Instead, it narrows faster than exponentially, meaning the adiabatic quantum computing cannot, even in principle, solve NP-complete problems faster than a classical computer …
> 
> In the end, they conclude that NP-complete problems are just as hard on an adiabatic quantum computer as on a classical computer. And, since earlier work showed the equivalence between different variants of quantum computers, that pretty much shuts down the possibility of any quantum computer helping with NP-complete problems.
> 
> I don't think anyone in the field will be particularly surprised by this. The failure of earlier work to show that quantum computers offered a speed-up on any NP-complete problem indicated that it was likely that it simply was not possible.

I'm heartened by the progress we've made these last ten years: from overhyped and misleading claims that quantum computers can solve NP-complete problems in polynomial time, to overhyped and misleading claims that they can't.

The link to the paper from the article is broken, and the article doesn't give the names of the researchers involved, but from the context, I'm pretty sure the article's attempting to talk about [this paper](http://arxiv.org/abs/0912.0746) by Boris Altshuler, Hari Krovi, and Jeremie Roland, amusingly entitled "Anderson localization casts clouds over adiabatic quantum optimization."  This paper really is an interesting and important one--but alas, the _Ars Technica_ story grossly misstates and exaggerates what it does.

For what I hope will be the last time, but I'm sure won't: yes, almost everyone in the field believes it's _true_ that quantum computers can't solve NP-complete problems in polynomial time.  But we have no idea at present how to _prove_ anything of the kind.  In fact, we don't even know how to prove _classical_ computers can't solve NP-complete problems in polynomial time (that's called the P vs. NP question; maybe you've heard of it!).  Nor do we even know how to prove a conditional statement, like "quantum computers can't solve NP-complete problems in polynomial time unless classical computers can also."  Any such result would be the biggest advance in theoretical computer science at least since I was born.

So then what do Altshuler, Krovi, and Roland do?  They consider a specific quantum algorithm--namely, the quantum adiabatic algorithm with linear interpolation--applied to random instances of an NP-complete problem, namely Exact Cover.  They then argue, based on a combination of numerical simulations and perturbation theory approximation, that the spectral gap decreases exponentially (actually, like 1/n!), which would imply that the adiabatic algorithm generally requires exponential time to reach the ground state.

If that sounds pretty interesting, you're right!  But what's the fine print?  Well, let's accept, for the sake of argument, Altshuler et al.'s claim that their conclusions about Exact Cover would likely generalize to 3SAT and other standard NP-complete problems.  Even then, there are three crucial caveats, all of which the _Ars Technica_ story ignores:

  1. Most importantly, the limitation (if it is one) applies only to one specific algorithm: namely the adiabatic optimization algorithm (with a specific interpolation schedule, but let's ignore that for now).  Now, some people seem to think a limitation on the adiabatic algorithm implies a limitation of quantum computers in general, since ["adiabatic is universal"](http://arxiv.org/abs/quant-ph/0405098)--a buzzphrase that's caused a lot of confusion.  In reality, what Aharonov et al. proved, in a beautiful paper six years ago, is that the adiabatic _model of computation_ is universal.  But they were talking about something much more general than the adiabatic _optimization algorithm_. For example, the ground state of Aharonov et al.'s adiabatic process is _not_ the solution to a combinatorial optimization problem, but rather a "history state" that encodes an entire computation itself.
  2. The Altshuler et al. paper talks about _random_ instances of the Exact Cover problem--but the uniform distribution over instances is just one particular distribution.  Even if the adiabatic algorithm doesn't help there, it's possible that there are other natural distributions over instances for which it exponentially outperforms (say) classical simulated annealing.
  3. Finally, even given the above two caveats, Altshuler et al. only show that the adiabatic algorithm fails on random Exact Cover instances at a "physics level of rigor."  In other words, their argument relies on a "perturbative approximation" that seems plausible but isn't proved.  A cynic might retort that, at a "physics level of rigor," we also know that P≠NP!  But such a cynic would be unfair.  I don't want to knock Altshuler et al.'s contribution.  For almost two decades, there's been a spectacularly fruitful interaction between the physicists and the math/CS folks in the study of random constraint satisfaction problems.  Indeed, many of the conjectures (or, in physics lingo, "results") in this area that the physicists derived using their hocus-pocus methods, were later rigorously confirmed by the mathematicians, and I don't know of any that were disconfirmed.  Even so, the distinction between a proof and a "physics proof" is one that seems worth insisting on--_especially_ in theoretical computer science, an area that's often far removed from conventional "physical intuition."



In summary, while it feels like swimming through a burning oil slick to say so, [I have to side with D-Wave](http://dwave.wordpress.com/2010/06/05/adiabatic-quantum-computing-the-greatest-idea-in-the-history-of-humanity/) about the _Ars Technica_ piece (though my reasons are mostly different).

So congratulations, _Ars Technica_!  [Like _The Economist_ before you](https://scottaaronson.blog/?p=204), you've successfully cast clouds over yourself when reporting about stuff I _don 't_ understand.

PS. I'm at [STOC'2010](http://research.microsoft.com/en-us/um/newengland/events/stoc2010/) right now, in exotic Cambridge, MA.  If you're interested, [here's](http://www.scottaaronson.com/talks/bqpph-stoc.ppt) the talk I gave this morning, on "BQP and the Polynomial Hierarchy," and [here's](http://www.scottaaronson.com/talks/FullChar3.pdf) the talk my PhD student Andy Drucker gave, on "A Full Characterization of Quantum Advice."  And Lance, please stop looking over my shoulder!
