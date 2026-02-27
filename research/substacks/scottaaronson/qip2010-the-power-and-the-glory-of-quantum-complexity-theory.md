---
title: "QIP’2010: The Power and the Glory of Quantum Complexity Theory"
author: "Scott Aaronson"
date: "Tue, 19 Jan 2010"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=438"
---

Firstly, if you haven't contributed to relief efforts in Haiti, you can [do so](http://www.konpay.org/) (the charity linked to was recommended by a Haitian-American working at MIT CSAIL).  I wish I had something more useful to say about this tragedy, but I don't.

For the past couple days, I've been at [QIP'2010](http://www.qip2010.ethz.ch/) in Zurich, Switzerland.  I'd had premonitions, even before arriving, that this was going to be an unusually awesome QIP.  Having been on the PC, I knew the strength of the technical program, and I'd learned that the turnout--320 participants--would be a record high.  My positive feelings only intensified when I saw the following in the hallway of my hotel:

My buzz reached a fever pitch when I entered the lecture hall and found giant, gourmet Swiss chocolate bars on every seat.

But I only _knew_ for sure that this QIP would rock when my erstwhile adviser, Umesh Vazirani, gave his opening plenary talk on "New bridges between computer science and quantum computation."  Umesh highlighted several developments, including:

  1. the [relationship](http://www.eccc.uni-trier.de/report/2009/104/) I noticed last year between the BQP versus the polynomial hierarchy problem and the Generalized Linial-Nisan Conjecture.
  2. the [QIP=PSPACE](http://arxiv.org/abs/0907.4737) breakthrough of Jain et al. (based on the recent _multiplicative-weights update method_ from classical computer science).
  3. recent breakthroughs in lattice-based cryptography (most famously, Gentry's [fully homomorphic encryption system](http://domino.research.ibm.com/comm/research_projects.nsf/pages/security.homoenc.html/$FILE/stocdhe.pdf)), which took inspiration from the quantum computing work of Oded Regev five years ago.
  4. the [work](http://arxiv.org/abs/0807.4154) of Broadbent, Fitzsimons, and Kashefi and [independently](http://arxiv.org/abs/0810.5375) Aharonov, Ben-Or, and Eban (for which I paid out pieces of the [Aaronson $25.00 Prize](https://scottaaronson.blog/?p=284)), which lets a "classical" verifier (equipped with the ability to send single, unentangled qubits through a channel) verify an arbitrary quantum computation; and which Umesh illustrated by a story about a verifier investigating the claims of a shady, fly-by-night company called "Q-Wave."



Umesh argued that the deepening connections between quantum computing and classical complexity theory--open problems in classical complexity being solved using [quantum-inspired techniques](http://arxiv.org/abs/0910.3376), tools that weren't available in the classical world until a year or two ago already being used for quantum purposes, etc.--represent one of the most exciting new developments in the field.

The combination of the chocolate bar (which I was already eating), and Umesh preaching so much truth from the pulpit, was heavenly.

Amazingly, subsequent talks managed to keep up the momentum.  Daniel Gottesman spoke about his [work](http://arxiv.org/abs/0905.2419) with Sandy Irani on the quantum complexity of translationally-invariant tiling and Hamiltonian problems.  By giving tools to say something useful about computational complexity even in cases where the only free parameter is the system size, Gottesman and Irani open up some exciting avenues for further work.  Jordan Kerenidis spoke about the [effort](http://arxiv.org/abs/0906.4425) to prove an analogue of the [Valiant-Vazirani witness isolation theorem](http://en.wikipedia.org/wiki/Valiant%E2%80%93Vazirani_theorem) for QMA (Quantum Merlin-Arthur).  Stefano Pironio talked about how you can [exploit the Bell inequality violations](http://arxiv.org/abs/0911.3427) to generate a long random string starting from a short random seed, assuming only the locality of the laws of physics, and _not_ assuming anything about the reliability of your randomness-generating devices.  This observation, which I find to be of great conceptual (and conceivably even practical) interest, is related to the so-called ["Free Will Theorem"](http://arxiv.org/abs/quant-ph/0604079) of Conway and Kochen, as well as to a result I proved eight years ago in my [review](http://www.scottaaronson.com/papers/nks.pdf) of Stephen Wolfram's book.  For Conway and Kochen, though, the motivation was to prove that "subatomic particles have free will" (a strange interpretation that I don't by any means endorse!), while for me, the motivation was to prove that Wolfram was wrong.  Neither I nor (as far as I know) Conway and Kochen thought about the obvious-in-retrospect application to generating random numbers.  (Incidentally, if anyone's interested, my talk slides from yesterday morning are [here](http://www.scottaaronson.com/talks/advqip.ppt).)

There's also been a great deal of excitement at this year's QIP about the efficient simulation of quantum systems occurring in nature, using recent techniques for model-order reduction (including MERA, matrix product states, quantum metropolis sampling, area laws…).  I hope I haven't just made John Sidles faint from excitement.

The full schedule is [here](http://www.qip2010.ethz.ch/programme); feel free to ask in the comments about any talks I didn't mention.  If there's enough interest, I might also write a followup post about the rest of the conference.
