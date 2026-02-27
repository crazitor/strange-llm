---
title: "NAND now for something completely different"
author: "Scott Aaronson"
date: "Fri, 23 Feb 2007"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=207"
---

There was a _real_ breakthrough in quantum algorithms last week -- though you wouldn't have known about it from reading Slashdot, Yahoo News, _The Economist_ , or (for that matter) this blog.

Farhi, Goldstone, and Gutmann -- the feared MIT trio -- announced a [quantum algorithm for evaluating NAND trees](http://www.arxiv.org/abs/quant-ph/0702144) in O(√N) time. This solves a problem that I worked on as an undergrad nine years ago (!), and that many a tyro had unsuccessfully tackled since.

Alright, so suppose we've got this ant at the root of a complete binary tree:

You and your friend take turns moving the ant: first you can move it either down-and-left or down-and-right, then your friend can make the same choice, then you, etc. If the ant ends up at a sugar cube, you win the game; if it ends up at a boot, your friend wins. (Your friend is an exterminator.)

In the above example, it's not hard to see that you're the one with a winning strategy. But more generally, we can imagine a tree d levels deep, with an arbitrary sequence of N=2d boots and sugar cubes at the leaf vertices. Then the question is: how many of the leaf vertices do you have to examine, in order to decide whether you or your friend has the win?

The goal here is to model _games of alternation_ like chess and go, abstracting away the details. The boots and sugar cubes correspond to losing and winning board positions. Then we want to know: how many board positions would a computer have to evaluate, in order to play the game perfectly?

It's clear that you generally don't have to examine _all_ the positions. For example, suppose that at some position where it's your turn to move, you discover a move that always lets you win. Then you don't _care_ what happens if you make any other move from that position.

Based on this idea (which AI types call [alpha-beta pruning](http://en.wikipedia.org/wiki/Alpha-beta_pruning)), in 1986 [Saks and Wigderson](http://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/SW86/SW86.pdf) gave a randomized algorithm to find an optimal move in the ant game, after examining (on average) only N0.753 of the N leaf vertices. (Here 0.753 ≈ log2(1+√33)-2.) On the other hand, they also showed that this running time was optimal for randomized algorithms with no error. Then, in 1995, [Santha](http://www.lri.fr/~santha/Papers/s95.ps.gz) showed that it was optimal even for randomized algorithms with error.

Alright, but what about the quantum case? It was observed early on (by a simple reduction from the PARITY problem) that any quantum algorithm for playing the ant game would have to examine at least √N of the N leaf vertices. But was a √N running time achievable? Until last week, we knew of no quantum algorithm that did even _slightly_ better than the classical bound of N0.753.

And now it's time to eat some crow: I didn't believe there _was_ such a quantum algorithm. I thought N0.753 was optimal. In my defense, though, this was never really a very _serious_ belief, in contrast to (say) my belief that quantum computers can't solve NP-complete problems in polynomial time. _Really_ I only claimed N0.753 was optimal to try and goad people into proving me wrong. And today, I'm pleased to report that my strategy was successful.

Last Wednesday, Farhi, Goldstone, and Gutmann put out a [preprint](http://www.arxiv.org/abs/quant-ph/0702144) showing how to find an optimal move for the ant game in time O(√(N log N)). However, their algorithm only worked in the "Hamiltonian oracle model," a fanciful idealization preferred by physicists in which time is (get this) continuous rather than discrete. Two days later, [Childs, Cleve, Jordan, and Yeung](http://www.arxiv.org/abs/quant-ph/0702160) showed how to port the algorithm to the ordinary discrete model, except that there the running time goes up to N1/2+ε for any ε>0\. Then, just yesterday, Farhi, Goldstone, and Gutmann improved the running time in the Hamiltonian oracle model to the optimal O(√N). One hopes and expects that further improvements in the discrete model are forthcoming.

Another obvious question is whether _any_ game tree can be evaluated in O(√N) time, not just the complete binary tree used in the ant game. Since the complete binary tree was previously considered the "hardest" case, the natural conjecture would be yes.

Years ago, David Deutsch gave an [interview](http://www.qubit.org/people/david/structure/Documents/By%20Other%20People/PhilosophyNow.html) in which he illustrated Grover's algorithm using chess. I emailed Deutsch to point out that this was a bad example: at the time, we we had no idea how to get a Grover speedup for games of alternation with small branching factor. Deutsch dutifully posted a correction. Now I guess I'll have to email him again, to tell him one _can_ get a "Grover" speedup for games like chess after all.

I put "Grover" in quotes because, even though the Farhi-Goldstone-Gutmann algorithm achieves a square-root speedup, it doesn't actually look anything like Grover's algorithm. Instead it's based on a quantum walk (reminiscent of [this](http://www.arxiv.org/abs/quant-ph/0209131) paper), which is analyzed using tools from scattering theory. Apparently, physics occasionally _does_ come in handy for quantum computing.

All in all, this business with NAND trees has only confirmed my core belief about theoretical computer science: that there are no miracles, except when there are.
