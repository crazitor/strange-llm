---
title: "The Computational Complexity of Linear Optics"
author: "Scott Aaronson"
date: "Sat, 13 Nov 2010"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=473"
---

I usually avoid blogging about my own papers--since, as a tenure-track faculty member, I prefer to be known as a media-whoring clown who trashes D-Wave Sudoku claims, bets $200,000 against alleged P≠NP proofs, and complains about his lecture notes being appropriated by Australian actresses to sell printers. Any _research_ that I happen to do is best kept secret, lest it interfere with that carefully-constructed persona.

Today, though, I'm making an exception. On Thursday, my PhD student Alex Arkhipov and I finally finished our mammoth ~~94~~ 95-page preprint on [The Computational Complexity of Linear Optics](http://www.scottaaronson.com/papers/optics.pdf), which we were writing for the past year. (Remarkably, this is Alex's first paper. Congratulations, Alex!) Never before was I involved in a project that forced me to learn so many unfamiliar things, from experimental quantum optics to random matrix theory to exotic complexity classes like BPPNP and PostBQP. (Alright, that last one wasn't particularly unfamiliar, but the others were.)

In one sentence, the goal of our paper is to help bridge the yawning gap between what complexity theorists believe is _true_ about quantum mechanics--namely, that it's exponentially-hard to simulate on a classical computer--and what experimentalists can currently demonstrate. To do so, we try to "meet the experimentalists halfway," by proposing a linear-optical setup that seems significantly closer to practicality than (say) a universal quantum computer, but still solves a computational problem that we can show is intractable for classical computers, under plausible and clearly-stated hardness assumptions (which don't just amount to "our system is hard to simulate"!).

Without further ado, here's the abstract:

> We give new evidence that quantum computers -- moreover, rudimentary quantum computers built entirely out of linear-optical elements -- cannot be efficiently simulated by classical computers. In particular, we define a model of computation in which identical photons are generated, sent through a linear-optical network, then nonadaptively measured to count the number of photons in each mode. This model is not known or believed to be universal for quantum computation, and indeed, we discuss the prospects for realizing the model using current technology. On the other hand, we prove that the model is able to solve sampling problems and search problems that are classically intractable under plausible assumptions.
> 
> Our first result says that, if there exists a polynomial-time classical algorithm that samples from the same probability distribution as a linear-optical network, then P#P=BPPNP, and hence the polynomial hierarchy collapses to the third level. Unfortunately, this result assumes an extremely accurate simulation.
> 
> Our main result suggests that even an approximate or noisy classical simulation would already imply a collapse of the polynomial hierarchy. For this, we need two unproven conjectures: the _Permanent-of-Gaussians Conjecture_ , which says that it is #P-hard to approximate the permanent of a matrix A of independent N(0,1) Gaussian entries, with high probability over A; and the _Permanent Anti-Concentration Conjecture_ , which says that |Per(A)|≥√(n!)/poly(n) with high probability over A. We present evidence for these conjectures, both of which seem interesting even apart from our application.
> 
> This paper does not assume knowledge of quantum optics. Indeed, part of its goal is to develop the beautiful theory of noninteracting bosons underlying our model, and its connection to the permanent function, in a self-contained way accessible to theoretical computer scientists.

As you can see from the abstract, there's a huge amount still to be done--of which the most obvious is (1) proving our #P-hardness conjecture and (2) doing our experiment! I'm also hopeful that people will take up the challenge of proving similar hardness results for other "rudimentary" quantum systems, besides linear optics. In that vein, one immediate question is whether we can give evidence that the beautiful ["commuting quantum computations"](http://arxiv.org/abs/1005.1407) model of Bremner, Jozsa, and Shepherd is hard to simulate even approximately by a classical computer.

Here are a few options for anyone who's _slightly_ curious about our work, but not curious enough to, y'know, [download the paper](http://www.scottaaronson.com/papers/optics.pdf):

  * [My PowerPoint slides](http://www.scottaaronson.com/talks/optics-msr.ppt).
  * [Alex's PowerPoint slides](http://stellar.mit.edu/S/course/6/fa10/6.845/courseMaterial/topics/topic3/lectureNotes/Boson_presentation/Boson_presentation.ppt), which I like better than mine.
  * A [MathOverflow question](http://mathoverflow.net/questions/45822/anti-concentration-bound-for-permanents-of-gaussian-matrices) that I posted yesterday about the Permanent Anti-Concentration Conjecture, and which was quickly answered by Terry Tao.
  * A [CS Theory StackExchange question](http://cstheory.stackexchange.com/questions/2892/how-does-the-bosonsampling-paper-avoid-easy-classes-of-complex-matrices/) about our paper posted by András Salamon, which I answered this morning.
  * **New:** An [interesting blog post](http://gilkalai.wordpress.com/2010/11/17/aaronson-and-arkhipovs-result-on-hierarchy-collapse/) about our work by Gil Kalai.



Anyway, the main purpose of this post was simply to provide a place for people with questions about our paper to ask them. So, shoot!
