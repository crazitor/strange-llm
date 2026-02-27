---
title: "Bringing a sacrificial goat and n-bit string to the oracle"
author: "Scott Aaronson"
date: "Sun, 22 Aug 2010"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=461"
---

I've been enjoying Athens and the coast of Greece for the past four days. I was going to take a day trip to Delphi, for the _sole purpose_ of blogging about having "queried the Oracle" there, but I ultimately decided to confine this trip to the unrelativized regions of Greece.

However, I do have something else related to oracles that I'd like to blog about today. Last week I put out a [preprint](http://eccc.uni-trier.de/report/2010/128/) on the ECCC (that's the Electronic Colloquium on Computational Complexity for newbs), entitled "The Equivalence of Sampling and Searching." There, I use Kolmogorov complexity to prove the surprising (to me) fact that

  * FBPP=FBQP if and only if SampP=SampBQP.



In other words: classical computers can efficiently solve every search (i.e., "functional" or "relational") problem that quantum computers can solve, _if and only if_ they can efficiently approximately sample the output distribution of every quantum circuit. (Note that, although this result involves the names of quantum complexity classes, it has almost nothing to do with quantum computing.) Anyway, when I gave a talk about this result at Hebrew University, Noam Nisan raised two excellent questions, neither of which I'd thought to ask and neither of which I knew the answers to:

  1. Is there an oracle relative to which BPP=BQP but PromiseBPP≠PromiseBQP? (In other words: an oracle that makes classical and quantum computers equivalent for language decision problems, but different for promise problems?)
  2. Is there an oracle relative to which PromiseBPP=PromiseBQP but FBPP≠FBQP? (In other words: an oracle that makes classical and quantum computers equivalent for promise problems, but different for search problems? Here FBPP and FBQP are the classes of search problems solvable in polynomial time by classical and quantum computers respectively--see my preprint for formal definitions of them.)



Affirmative answers to these questions would imply that any extension of my equivalence theorem to decision and promise problems would have to be non-relativizing. I'd be incredibly grateful for any thoughts about these questions, and will even offer a $5 reward for each one.

However, since I have a feeling that these oracle challenges won't generate _quite_ enough comments, let me now pour some gasoline on the fire. You may have noticed that what I did above, among other things, was to call attention to my own ECCC preprint. Up till today, I've had an informal policy of almost never using _Shtetl-Optimized_ to blog about my own research, except indirectly (e.g., when I talk about open problems that arose out of my papers). I had three reasons for this policy: first, blogging about one's own research always runs the severe risk of boring everyone. Second, after I've finished a paper, _I 'm_ usually bored with it; writing a blog entry that rehashes what's already in the paper is usually the last thing I want to do. Third, and most importantly, I didn't want to create the impression that I was using this blog to give my papers an "unfair advantage" over everyone else's.

However, recently a consensus seems to have formed, among the community of disgruntled anonymous commenters on computational complexity blogs, that I'm some sort of clown who bets $200,000 against alleged P≠NP proofs for the sole reason that he's unable to do any actual research of his own. While I ought to have the Obamalike composure to remain unaffected by such gutter-sniping, I have to admit that it pissed me off. To be sure, I _am_ a clown who bets $200,000 against alleged P≠NP proofs instead of doing actual research. However, this is not because I _can 't_ do actual research; rather, it's because I _don 't feel like it_. To help prove this, I've decided to abandon my previous no-tooting-my-own-research-horn policy. So, anonymous commenters: you wanna know about my actual research? Well then, blog entries about actual research are what you're gonna get--so much that you'll wish you never brought it up.
