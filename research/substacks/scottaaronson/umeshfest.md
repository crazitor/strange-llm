---
title: "UmeshFest"
author: "Scott Aaronson"
date: "Fri, 10 May 2024"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=7972"
---

**Unrelated Announcements:** [See here](https://thetexasorator.com/2024/01/06/an-interview-with-dr-scott-aaronson/) for a long interview with me in _The Texas Orator_ , covering the usual stuff (quantum computing, complexity theory, AI safety). And [see here](https://bit.ly/ctp-208) for a podcast with me and Spencer Greenberg about a similar mix of topics.

* * *

A couple weeks ago, I helped organize [UmeshFest: Don't Miss This Flight](https://simons.berkeley.edu/workshops/umeshfest-dont-miss-flight), a workshop at UC Berkeley's Simons Institute to celebrate the 26th birthday of my former PhD adviser [Umesh Vazirani](https://en.wikipedia.org/wiki/Umesh_Vazirani). Peter Shor, John Preskill, Manuel Blum, Madhu Sudan, Sanjeev Arora, and dozens of other luminaries of quantum and classical computation were on hand to help tell the story of quantum computing theory and Umesh's central role in it. There was also constant roasting of Umesh--of his life lessons from the squash court, his last-minute organizational changes and phone calls at random hours. I was delighted to find that my old coinage of ["Umeshisms"](https://scottaaronson.blog/?p=40) was simply standard usage among the attendees.

* * *

At Berkeley, many things were as I remembered them--my favorite Thai eatery, the bubble tea, the Campanile--but not _everything_ was the same. Here I am in front of Berkeley's Gaza encampment, a.k.a. its "Anti Zionism Zone" or what was formerly Sproul Plaza (zoom into the chalk):

I felt a need to walk through the Anti Zionism Zone day after day (albeit unassumingly, neither draped in an Israeli flag nor looking to start an argument with anyone), for more-or-less the same reasons why the US regularly sends aircraft carriers through the Strait of Taiwan.

* * *

Back in the more sheltered environment of the Simons Institute, it was great to be among friends, some of whom I hadn't seen since before Covid. [Andris Ambainis](https://en.wikipedia.org/wiki/Andris_Ambainis) and I worked together for a bit on an open problem in quantum query complexity, for old times' sake (we haven't solved it yet).

And then there were talks! I thought I'd share my own talk, which was entitled The Story of [BQP](https://en.wikipedia.org/wiki/BQP) (Bounded-Error Quantum Polynomial-Time). [Here](https://www.scottaaronson.com/talks/bqp.pptx) are the PowerPoint slides, but I'll also share screen-grabs for those of you who constantly complain that you can't open PPTX files.

I was particularly proud of the design of my title slide:

Moving on:

The class [BQP/qpoly](https://complexityzoo.net/Complexity_Zoo:B#bqpqpoly), I should explain, is all about an advisor who's all-wise and perfectly benevolent, but who doesn't have a lot of time to meet with his students, so he simply doles out the same generic advice to all of them, regardless of their thesis problem x.

I then displayed [my infamous "Umeshisms" blog post](https://scottaaronson.blog/?p=40) from 2005--one of the first posts in the history of this blog: 

As I explained, now that I hang out with the rationalist and AI safety communities, which are _also_ headquartered in Berkeley, I've learned that my "Umeshisms" post somehow took on a life of its own. Once, when dining at one of the rationalists' polyamorous Berkeley group houses, I said this has been lovely but I'll now need to leave, to visit my PhD former adviser Umesh Vazirani. "You mean _the_ Umesh?!" the rationalists excitedly exclaimed. "Of Umeshisms? If you've never missed a flight?"

But moving on:

(Note that by "QBPP," Bethiaume and Brassard meant what we now call BQP.)

Feynman and Deutsch asked exactly the right question--does simulating quantum mechanics on a classical computer inherently produce an exponential slowdown, or not?--but they lacked most of the tools to start formally investigating the question. A factor-of-two quantum speedup for the XOR function could be dismissed as unimpressive, while a much greater quantum speedup for the "constant vs. balanced" problem could be dismissed as a win against only _deterministic_ classical algorithms, rather than randomized algorithms. [Deutsch-Jozsa](https://en.wikipedia.org/wiki/Deutsch%E2%80%93Jozsa_algorithm) may have been the first time that an apparent quantum speedup faltered in an honest comparison against classical algorithms. It certainly wasn't the last!

Ah, but this is where [Bernstein and Vazirani](https://people.eecs.berkeley.edu/~vazirani/pubs/bv.pdf) enter the scene.

Bernstein and Vazirani didn't merely define [BQP](https://en.wikipedia.org/wiki/BQP), which remains the central object of study in quantum complexity theory. They also established its most basic properties:

And, at least in the black-box model, Bernstein and Vazirani gave the first impressive quantum speedup for a classical problem that survived in a fair comparison against the best classical algorithm:

The Recursive Bernstein-Vazirani problem, also called Recursive Fourier Sampling, is constructed as a "tree" of instances of the Bernstein-Vazirani problem, where to query the Boolean function at any given level, you need to solve a Bernstein-Vazirani problem for a Boolean function at the level below it, and then run the secret string s through a fixed Boolean function g. For more, see my old paper [Quantum Lower Bound for Recursive Fourier Sampling](https://arxiv.org/abs/quant-ph/0209060).

Each Bernstein-Vazirani instance has classical query complexity n and quantum query complexity 1. So, if the tree of instances has depth d, then overall the classical query complexity is nd, while the quantum query complexity is only 2d. Where did the 2 come from? From _the need to uncompute_ the secret strings s at each level, to enable quantum interference at the next level up--thereby forcing us to run the algorithm twice. A key insight.

The Recursive Fourier Sampling separation set the stage for [Simon's algorithm](https://en.wikipedia.org/wiki/Simon%27s_problem), which gave a more impressive speedup in the black-box model, and thence for the famous [Shor's algorithm](https://en.wikipedia.org/wiki/Shor%27s_algorithm) for factoring and discrete log:

But Umesh wasn't done establishing the most fundamental properties of BQP! There's also the seminal 1994 paper by [Bennett, Bernstein, Brassard, and Vazirani](https://arxiv.org/abs/quant-ph/9701001):

In light of the BV and BBBV papers, let's see how BQP seems to fit with classical complexity classes--an understanding that's remained largely stable for the past 30 years:

We can state a large fraction of the research agenda of the whole field, to this day, as questions about BQP:

I won't have time to discuss all of these questions, but let me at least drill down on the first few.

Many people hoped the list of known problems in BQP would now be longer than it is. So it goes: we don't decide the truth, we only discover it.

As a 17-year-old just learning about quantum computing in 1998 by reading the Bernstein-Vazirani paper, I was thrilled when I managed to improve their containment BQP ⊆ P#P to BQP ⊆ PP. I thought that would be my big debut in quantum complexity theory. I was then crushed when I learned that Adleman, DeMarrais, and Huang had proved the same thing a year prior. OK, but at least it wasn't, like, 50 years prior! Maybe if I kept at it, I'd reach the frontier soon enough.

Umesh, from the very beginning, raised the profound question of BQP's relation to the polynomial hierarchy. Could we at least construct an _oracle_ relative to which BQP⊄PH--or, closely related, relative to which P=NP≠BQP? Recursive Fourier Sampling was a already candidate for such a separation. I spent months trying to prove that candidate wasn't in PH, but failed. That led me eventually to propose a very different problem, Forrelation, which seemed like a stronger candidate, although I couldn't prove that either. Finally, in 2018, after four years of effort, Ran Raz and Avishay Tal [proved that](https://eccc.weizmann.ac.il/report/2018/107/download/) my Forrelation problem was not in PH, thereby resolving Umesh's question after a quarter century.

We now know three different ways by which a quantum computer can not merely solve any BQP problem efficiently, but prove its answer to a classical skeptic via an interactive protocol! Using quantum communication, using two entangled (but non-communicating) quantum computers, or using cryptography (this last a [breakthrough](https://arxiv.org/abs/1804.01082) of Umesh's PhD student Urmila Mahadev). It remains a great open problem, first posed to my knowledge by Daniel Gottesman, whether one can do it with none of these things.

To see many of the advantages of quantum computation over classical, we've learned that we need to broaden our vision beyond BQP (which is a class of languages), to _promise problems_ (like estimating the expectation values of observables), sampling problems (like [BosonSampling](https://arxiv.org/abs/1011.3245) and Random Circuit Sampling), and relational problems (like the [Yamakawa-Zhandry problem](https://arxiv.org/abs/2204.02063), subject of a recent breakthrough). It's conceivable that quantum advantage could remain for such problems even if it turned out that P=BQP.

A much broader question is whether BQP captures all languages that can be efficiently decided using "reasonable physical resources." What about chiral quantum field theories, like the Standard Model of elementary particles? What about quantum theories of gravity? Good questions!

Since it was Passover during the talk, I literally said ["Dayenu"](https://en.wikipedia.org/wiki/Dayenu) to Umesh: "if you had only given us BQP, that would've been enough! but you didn't, you gave us so much more!"

Happy birthday Umesh!! We look forward to celebrating again on all your subsequent power-of-2 birthdays.
