---
title: "G.  Phi.  Fo.  Fum."
author: "Scott Aaronson"
date: "Wed, 04 Nov 2015"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=2521"
---

**Update (Dec. 14):** The long wait is over! [Here's Laci's paper on the arXiv](http://arxiv.org/pdf/1512.03547.pdf). So far, I've read it only deeply enough to note that it contains the following sentence:

A group G ≤ S(Ω) defines the category of G-isomorphisms of strings on the domain Ω; the natural notation for this category, the central object of study in this paper, would seem to be "G-Strings."

With that, I believe Laci himself has outshone even [reddit's attempt](https://www.reddit.com/r/math/comments/3sdixw/babais_breakthrough_on_graph_isomorphism/cwwc437) to mine his breakthrough result for juvenile humor.

See also [a nice _Quanta_ article about Laci's algorithm](https://www.quantamagazine.org/20151214-graph-isomorphism-algorithm/) by Erica Klarreich. There's only one statement in the article that I disagree with: namely that, if graph isomorphism were inherently quasipolynomial time, then it would be the first natural example of such a problem. We know other natural problems, like approximating free games and socially-optimal Nash equilibria, that are solvable in nO(log n) time but that can't be in P unless 3SAT is solvable in ~exp(√n) time.

**Update (Nov. 17):** [Video of Laci's first talk](http://people.cs.uchicago.edu/~laci/2015-11-10talk.mp4) is now available.

**Breaking News (Nov. 12):** Jeremy Kun has written up a [phenomenal summary](http://jeremykun.com/2015/11/12/a-quasipolynomial-time-algorithm-for-graph-isomorphism-the-details/) of Babai's first lecture. I haven't carefully studied all of it, and in any case, there are many missing details to be filled in later (Babai told Kun that the preprint will be available "soon, soon!"). But from the summary, four points stood out to me:

  1. Babai actually claims a quasipolynomial-time algorithm for an interestingly more general problem than graph isomorphism, called _string isomorphism_. This was already in the abstract, but googling didn't reveal what string isomorphism was. So, OK, here's what it is: you're given two strings x and y over some finite alphabet, as well as the generators of a group G of permutations of the string indices. The problem is to determine whether you can transform x to y by applying a permutation in G. Or even more generally: given a string x, find a full set of generators for the subgroup of G that fixes x. See Kun's post for the straightforward reductions from GI to these group-theoretic problems.
  2. As was hinted in the abstract, in Babai's analysis of his algorithm, there's one step that relies on a statement whose only known proof depends on the Classification of Finite Simple Groups. (Thus, it's not the algorithm itself requires iterating through all the sporadic simple groups or anything like that; this only shows up in the correctness proof.) This is _not_ the first-ever computer-science application of the Classification of Finite Simple Groups (indeed, Babai himself has some previous ones), but it's certainly the most dramatic.
  3. In previous work on GI, the [Johnson graph](https://en.wikipedia.org/wiki/Johnson_graph) emerged over and over as a forehead-bangingly hard case that caused numerous algorithms to fail. In the new work, it looks like Babai's central technical innovation is to show that, in some sense, the Johnson graph is the _only_ obstruction to taking the divide-and-conquer approaches that people that had tried before, and making them run in quasipolynomial time. I.e., in each step of the recursion, _either_ you can find a Johnson graph on a large fraction of the vertices and handle it specially, _or else_ you can do something that works whenever there's _not_ a Johnson graph on a large fraction of the vertices. Babai calls this "split-or-Johnson."
  4. Babai stressed that in some sense, his new algorithm is the culmination of a program laid out by Eugene Luks in 1982. Now, the Classification of Finite Simple Groups was also more-or-less completed in the early 1980s. To my mind, this raises a fascinating socio-mathematical question: **which aspects of the new work, if any, could not have been done in the early 80s, possibly by Babai or Luks themselves? what is it that needed another 30 years?** If the answer turns out to be "nothing," then to me that's an astounding illustration of the role of the individual in mathematical progress. As in: Laci was nice enough to take a third-of-a-century break between his and Luks' work in the early 80s, and the "natural next step" in their program … and  _still_ no one managed to use that break to beat him to the next step!



* * *

Earlier today, I was tipped off to what _might_ be the theoretical computer science result of the decade. My source asked me not to break the news on this blog--but since [other theory bloggers](https://lucatrevisan.wordpress.com/2015/11/03/laci-babai-and-graph-isomorphism/) ([and](https://twitter.com/geomblog/status/661753110105366529) [twitterers](https://twitter.com/rrwilliams/status/661738595447771136)) are now covering the story, I guess the graph is out of the Babai.

According to [the University of Chicago's theory seminar calendar](http://www.math.uchicago.edu/calendar?calendar=Combinatorics%20and%20Theoretical%20Computer%20Science), on Tuesday of next week (November 10), the legendary [Laszlo Babai](https://en.wikipedia.org/wiki/L%C3%A1szl%C3%B3_Babai) will be giving a talk about a new algorithm that solves the [graph isomorphism problem](https://en.wikipedia.org/wiki/Graph_isomorphism_problem) in quasipolynomial time. The previous fastest algorithm to decide whether two n-vertex graphs G and H are isomorphic--by Babai and Luks, back in 1983--ran in exp(√(n log n)) time. If we credit the announcement, Babai has now gotten that down to exp(polylog(n)), putting one of the central problems of computer science "just barely above [P](https://en.wikipedia.org/wiki/P_\(complexity\))." (For years, I've answered questions on this blog about the status of graph isomorphism--would I bet that it's in BQP? in coNP? etc.--by saying that, as far as I and many others are concerned, it might as well just be in P. Of course I'm happy to reaffirm that conjecture tonight.)

Next week, I assume, Laci will lecture to a packed house; then the experts will race to unpack the details. Until then, we probably need to sit tight; I don't know any more than what's in the abstract. For now, I'm delighted if commenters want to share general thoughts or questions about graph isomorphism (and I'll try to answer what I can), but I  _won 't_ allow uninformed speculations or rumors about the details of the new result--not until Laci has had a chance to speak.

* * *

**Update (Nov. 5):** While we all wait with bated breath for more details, you can amuse yourself with [the talk I gave at Laci's 60th birthday conference](http://www.scottaaronson.com/talks/babai.ppt) five years ago.

Also, a comment of mine that I should probably promote to the main post:

Dana points out to me that non-native English speakers might not get the staggeringly clever pun in this post’s title (hey, it was the best I could do on a deadline).

So, alright, [fee fi fo fum](https://en.wikipedia.org/wiki/Fee-fi-fo-fum) is what the approaching giant bellows in _Jack and the Beanstalk_. It means something big is on the horizon. Also, G is a graph, and Phi is an isomorphism.

* * *

**Update (Nov. 12):** So, Laci gave his talk. Video was made but does not appear to be available yet. However, Gabriel Gaster, who was in attendance, graciously live-tweeted everything. [Here's a Storify of the live-tweets.](https://storify.com/ptwiddle/babai-s-first-graph-isomorphism-talk) (What's a "Storify"?)
