---
title: "My responses to GASARCH’s P vs. NP poll"
author: "Scott Aaronson"
date: "Sat, 25 Jun 2011"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=690"
---

The poll is [here](http://blog.computationalcomplexity.org/2011/06/i-am-conducing-new-poll-on-p-vs-np.html); my (slightly-edited) responses are below. It took heroic self-restraint, but I tried to answer with straightforward statements of what I actually think, rather than ironic humor.

**1\. Do you think P=NP or not? You may give other answers as well.**

I think P≠NP (on more-or-less the same grounds that I think I won't be devoured tomorrow by a 500-foot-tall salsa-dancing marmoset from Venus, despite my lack of proof in both cases).

**2\. When do you think it will be resolved?**

In his recent book [The Beginning of Infinity](http://www.amazon.com/Beginning-Infinity-David-Deutsch-Science/dp/0713992743), David Deutsch argues that we can't even make decent _probabilistic_ predictions about a future event, to whatever extent that event depends on new knowledge being created. I agree with him on this: a proof of P≠NP, like other major mathematical advances, would depend almost entirely on new knowledge, and because of that, my uncertainty applies not only to the approximate number of years but to the approximate _log_ of that number: decades, centuries, millennia, who knows? Maybe the question should be rephrased: "will humans manage to prove P≠NP before they either kill themselves out or are transcended by superintelligent cyborgs? And if the latter, will the cyborgs be able to prove P≠NP?"

**3\. What kinds of techniques do you think will be used?**

Obviously I don't know--but if we look at the techniques used in (say) Ryan Williams' recent [result](http://www.cs.cmu.edu/~ryanw/acc-lbs.pdf), and then remember that that proof only separates NEXP from ACC0, we can get a weak hint about the scale of the techniques that would be needed for problems like P vs. NP. Right now, [Mulmuley's GCT](http://ramakrishnadas.cs.uchicago.edu/gctexplicit.pdf) is the only approach out there that even _tries_ to grapple with the biggest barrier we know, beyond even [relativization](http://blog.computationalcomplexity.org/2006/03/favorite-theorems-relativization.html), [natural proofs](http://www.cs.cmu.edu/~rudich/papers/natural.ps), and [algebrization](http://www.scottaaronson.com/papers/alg.pdf): the barrier that many nontrivial problems (including matching and linear programming) are in P! That's not to say Mulmuley's specific program will succeed: indeed, I suspect that the right chain of reasoning might diverge from Mulmuley's at an earlier rather than later point. But even for the seemingly-easier permanent versus determinant problem, I fear Mulmuley is basically right that the key insights lie in yellow books yet to be written.

**4\. Will the problem still be relevant given advances in algorithms and in SAT Solvers?**

Yes, in the same way the Second Law of Thermodynamics is still relevant given advances in hybrid cars.

**5\. Feel free to comment on anything else: Graph Isomorphism, Factoring, Derandomization, Quantum computers, and/or your own favorite problem.**

Graph Isomorphism: Probably in P.

Factoring: Probably hard for classical computers, but unlike with NP-complete problems, if it isn't then we're still living on Earth.

Derandomization: I think P=BPP (with essentially the same strength of conviction as P≠NP), and likewise L=RL, etc.

Quantum computing: I think BPP≠BQP (though not with the same strength of conviction as P≠NP), and also predict that no bizarre changes to quantum mechanics will be discovered of the sort needed to make scalable quantum computing impossible.

* * *

For those who are still reading, as a special bonus I present my answers to the large and interesting questions asked by a commenter on my last post named Mike S.

**One thing I’ve heard before about NP(-hard) problems is that often certain instances are much harder than others. What are your feelings on the physical practicality of a computer that solves only most cases of NP(-hard) problems quickly? Also, is determining the ‘difficulty’ of particular instances of NP-complete problems NP(-hard)?**

It depends what you mean by “most”! I think it’s almost certainly possible to generate a probability distribution over 3SAT instances almost all of which are hard (indeed, that assumption is central to modern cryptography). As one example, the _approximate shortest vector problem_ is known to be just as hard on average as it is in the worst case, and it can easily be reduced to 3SAT. Another candidate is random k-SAT instances at the “critical ratio” of clauses to variables, for k≥4.

But maybe what you meant was those instances of NP-hard problems that “typically arise in real life.” Here all sorts of issues come into play: for example, often the instances that arise in practice have symmetries or other structure that makes them easy. And often your goal is not to find the best solution, but just a _better_ solution than your competitors. And often we terminate trains of thought long before they lead to hard instances of NP-complete problems—we’re usually not even conscious that that’s what we’re doing; we just have an intuition that “such-and-such would require a hopeless search.”

But at the same time, when we _do_ ask explicitly for optimal solutions, that request for optimality often has a way of finding the hard instances for us.

**Less seriously, you said something along the lines of ‘P!=NP keeps mathematicians in business’. If math is so hard computationally, how do WE do it? Or on the other hand, if the computational complexity of certain problems is a fundamental property of the universe, and we are part of the universe, doesn’t it follow that we could make computers that are as good or better at doing math than we are?**

The short answer is that math (as practiced by humans) is an extremely hit-or-miss business! A billion years of evolution have equipped us with a lot of useful heuristics, as has the much faster evolution of mathematical ideas over the last few thousand years.

Probably even more important, we normally don’t care about _arbitrary_ mathematical questions (does this random Turing machine halt?), but only questions that arise in some explanatory framework. And that criterion tends to select extremely strongly for questions that we can answer! _Why_ it does so is a profound question itself, but whatever the answer, the history of math provides overwhelming evidence that it does. [Goldbach’s Conjecture](http://en.wikipedia.org/wiki/Goldbach%27s_conjecture) and the [Collatz 3x+1 Conjecture](http://en.wikipedia.org/wiki/Collatz_conjecture) are more-or-less “arbitrary” questions (at least in our present state of knowledge), and indeed they haven’t been answered yet. Fermat’s Last Theorem might have _seemed_ pretty arbitrary at first (Gauss regarded it as such), but it wasn't. Indeed, in the 1980s it was embedded into the deep explanatory framework of elliptic curves and modularity, and a decade later it was solved.

Of course, despite these factors in mathematicians’ favor, they’re very far from having a general-purpose method to solve all the problems they want solved.

Incidentally, “P≠NP means computers can never replace human mathematicians” is a forehead-bangingly common misunderstanding. Personally, I see no reason why the brain couldn’t be simulated by computer (neuron-by-neuron if necessary), and P≠NP does nothing to challenge that belief. All P≠NP suggests is that, once the robots _do_ overtake us, they won’t have a general-purpose way to automate mathematical discovery any more than we do today.
