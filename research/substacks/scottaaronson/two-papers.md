---
title: "Two papers"
author: "Scott Aaronson"
date: "Tue, 21 Apr 2015"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=2272"
---

Just to get myself back into the habit of blogging:

For those of you who don't read [Lance's and Bill's blog](http://blog.computationalcomplexity.org/2015/04/ph-infinite-under-random-oracle.html), there was a pretty significant breakthrough in complexity theory announced last week. (And yes, I'm now spending one of the two or so uses of the word "breakthrough" that I allow myself per year--wait, did I just spend the second one with this sentence?) Ben Rossman (a former MIT PhD student whose thesis committee I was honored to serve on), Rocco Servedio, and Li-Yang Tan [have now shown](http://arxiv.org/abs/1504.03398) that the polynomial hierarchy is infinite relative to a random oracle, thereby solving the main open problem from [Johan Håstad's 1986 PhD thesis](https://www.nada.kth.se/~johanh/thesis.pdf). While it feels silly even to mention it, the best previous result in this direction was to separate PNP from Σ2P relative to a random oracle, which I did in my [Counterexample to the Generalized Linial-Nisan Conjecture](http://www.scottaaronson.com/papers/glnfalse.pdf) paper. In some sense Rossman et al. infinitely improve on that (using completely different techniques). Proving their result boils down to proving a new lower bound on the sizes of constant-depth circuits. Basically, they need to show that, for every k, there are problems that can be solved by small circuits with k layers of AND, OR, and NOT gates, but for which the answer can't even be _guessed_ , noticeably better than chance, by any small circuit with only k-1 layers of AND, OR, and NOT gates. They achieve that using a new generalization of the method of random restrictions. Congratulations to Ben, Rocco, and Li-Yang!

Meanwhile, if you want to know what _I 've_ been doing for the last couple months, one answer is contained in [this 68-page ~~labor of love~~ preprint](http://eccc.hpi-web.de/report/2015/066/) by me and my superb PhD students Daniel Grier and Luke Schaeffer. There we give a full classification of all possible sets of classical reversible gates acting on bits (like the Fredkin, Toffoli, and CNOT gates), as well as a linear-time algorithm to decide whether one reversible gate generates another one (previously, that problem wasn't even known to be decidable). We thereby completely answer a question that basically  _no one_ was asking, although I don't understand why not.
