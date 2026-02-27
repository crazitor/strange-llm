---
title: "Quantum Complexity Theory Student Project Showcase #5 (2025 Edition)!"
author: "Scott Aaronson"
date: "Fri, 01 Aug 2025"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=9022"
---

Sorry for the long blog-hiatus! I was completely occupied for weeks, teaching an intensive course on theoretical computer science to 11-year-olds (!), at a [math camp](https://epsiloncamp.org/) in St. Louis that was also attended by my 8-year-old son. Soon I'll accompany my 12-year-old daughter to a [science camp](https://sigmacamp.org/) in Connecticut, where I'll also give lectures.

There's a great deal to say about these experiences, but for now: it's been _utterly transformative and life-affirming_ to spend my days in teaching precocious, enthusiastic, non-jaded children the material I love in the real world, rather than (let's say) in scrolling through depressing world news and social media posts and emails from hateful trolls on my phone. It's made me feel 25 years younger (well, at least until I need to walk up a flight of stairs). It's made me want to go back to actual research and teaching, which besides family and friends have been the main sources of joy in my life.

* * *

So on that note, and without further ado: I hereby present the latest **Quantum Complexity Theory Student Project Showcase!** As the name suggests, this is where I share a selection of the best research projects, from the students who took my graduate class on Quantum Complexity Theory at UT Austin this past spring.

See here for the four previous iterations of the Showcase:

  * [2011 edition](https://scottaaronson.blog/?p=515) (MIT)
  * [2012 edition](https://scottaaronson.blog/?p=1181) (MIT)
  * [2014 edition](https://scottaaronson.blog/?p=2109) (MIT)
  * [2021 edition](https://scottaaronson.blog/?p=5382) (MIT / UT Austin)



(As you can see, the timing hasn't been 100% consistent.)

I expect that, as in past editions, many of this year's projects will lead to published research papers, or at the very least, preprints on the arXiv.

* * *

And now, _really_ without further ado, the projects!

**(1)[Quantum Hermite Transform and Gaussian Goldreich-Levin](https://www.scottaaronson.com/showcase5/quantum-hermite-transform.pdf), by Vishnu Iyer and Siddhartha Jain.**

Vishnu and Sid propose a new primitive for quantum algorithms--the Hermite transform, as opposed to the Fourier transform--and give at least one successful example of its use. They'd be eager to know if anyone can think of other applications!

**(2)[Quantum Statistical Witness Indistinguishability](https://www.scottaaronson.com/showcase5/qswi.pdf), by Shafik Nassar and Ronak Ramachandran.**

In modern cryptography, even if it isn't _statistical zero-knowledge_ (SZK), a proof protocol might have the weaker property of being _statistically witness-indistinguishable_ (SWI): that is, Arthur can't tell which of two possible yes-witnesses Merlin holds. Here Shafik and Ronak initiate the study of _quantum_ SWI, and prove the basic properties of this notion, such as the equivalence of honest and dishonest verifier. Hopefully this will serve as a springboard for someone to find an actual QSWI protocol for an interesting problem.

**(3)[A Zero-Knowledge Protocol for Keyed Unitary Families](https://www.scottaaronson.com/showcase5/zk.pdf), by David Joy and Angela Zhang.**

Continuing the theme of quantum zero-knowledge, David and Angela give a protocol by which Merlin can convince Arthur that he knows a unitary relating one pure state to another, without revealing the unitary. Again continuing a theme, applications of this protocol are sought!

**(4)[On Query Lower Bounds for Aaronson-Kuperberg Unitary Synthesis Circuits](https://www.scottaaronson.com/showcase5/synthesis.pdf), by Arko Banerjee.**

Back in 2006, when we formulated our so-called "Unitary Synthesis Conjecture," Greg Kuperberg and I [showed](https://arxiv.org/abs/quant-ph/0604056) that if a quantum algorithm applies an n-qubit unitary U(f) after making a single query to a Boolean function f, then as we range over f's, there can be at most 4n possible values of U(f). Here Arko improves our bound to 2n, which is tight. He also tries extremely hard to generalize our bound to the two-query case, not quite succeeding but proving partial results that hopefully will be helpful to others.

**(5)[Quantum Search with Non-Interacting Bosons and Fermions](https://www.scottaaronson.com/showcase5/boson.pdf), by Aravind Karthigeyan.**

This one _really_ made me think. Aravind studies the problem of search for a single marked vertex, on the complete graph with N vertices, using either M bosons or M fermions that can hop between the vertices. With M bosons, he shows that the search succeeds in Θ(√(N/M)) time with high probability, which is just the usual runtime for Grover search with M parallel searchers. With fermions, by contrast, he shows that more time is needed. Why? Because of the Pauli Exclusion Principle! The fermions all "step on each others' toes," competing to be the one that jumps onto the marked vertex, which limits the advantage of having M fermions searching in parallel.

**(6)[Limits to Pseudodeterminism in Quantum Communication Protocols](https://www.scottaaronson.com/showcase5/pseudodet.pdf), by Jiawei Li.**

Jiawei revisits the famous [Hidden Matching Problem](https://en.wikipedia.org/wiki/Hidden_Matching_Problem), which is known to have an exponential gap between its randomized one-way communication complexity of ~√n, and its quantum one-way communication complexity of ~log(n). He makes a new observation about this problem: namely, if you want the exponential quantum communication advantage, then you _must_ content yourself with a protocol that can generate many different possible correct answers with appreciable probabilities (i.e., that generates large _min-entropy_). In other words, no good quantum protocol for the problem is _pseudodeterministic_. This complements, for example, [my and Shih-Han Hung's work](https://arxiv.org/abs/2303.01625), which showed the same statement for quantum supremacy experiments based on Random Circuit Sampling, or the long line of works that showed it for experiments that violate the Bell/CHSH inequality.

Congratulations to my students for their accomplishments, and thanks to them for giving me permission to include their work in this showcase!
