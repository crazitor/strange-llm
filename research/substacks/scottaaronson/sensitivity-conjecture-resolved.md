---
title: "Sensitivity Conjecture resolved"
author: "Scott Aaronson"
date: "Tue, 02 Jul 2019"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=4229"
---

The Sensitivity Conjecture, which I blogged about [here](https://scottaaronson.blog/?p=453), says that, for every Boolean function f:{0,1}n→{0,1}, the _sensitivity_ of f--that is, the maximum, over all 2n input strings x∈{0,1}n, of the number of input bits such that flipping them changes the value of f--is at most polynomially smaller than a bunch of other complexity measures of f, including f's block sensitivity, degree as a real polynomial, and classical and quantum query complexities. (For more, see for example [this survey](http://www.cs.columbia.edu/~rocco/Teaching/S12/Readings/BdW.pdf) by Buhrman and de Wolf. Or for quick definitions of the relevant concepts, [see here](https://cstheory.stackexchange.com/questions/19902/boolean-functions-where-sensitivity-equals-block-sensitivity).)

Ever since it was posed by Nisan and Szegedy in 1989, this conjecture has stood as one of the most frustrating and embarrassing open problems in all of combinatorics and theoretical computer science. It seemed so easy, and so similar to other statements that had 5-line proofs. But a lot of the best people in the field sank months into trying to prove it. For whatever it's worth, I also sank … well, at least weeks into it.

Now [Hao Huang](http://www.mathcs.emory.edu/~hhuan30/), a mathematician at Emory University, has posted a [6-page preprint](http://www.mathcs.emory.edu/~hhuan30/papers/sensitivity_1.pdf) on his homepage that finally proves the Sensitivity Conjecture, in the form s(f)≥√deg(f). (I thank Ryan O'Donnell for tipping me off to this.) Within the preprint, the proof itself is about a page and a half.

Whenever there's an announcement like this, ~99% of the time either the proof is wrong, or at any rate it's way too complicated for outsiders to evaluate it quickly. This is one of the remaining 1% of cases. I'm rather confident that the proof is right. Why? Because I read and understood it. It took me about half an hour. If you're comfortable with concepts like _induced subgraph_ and _eigenvalue_ , you can do the same.

From pioneering work by Gotsman and Linial in 1992, it was known that to prove the Sensitivity Conjecture, it suffices to prove the following even simpler combinatorial conjecture:

> Let S be any subset of the n-dimensional Boolean hypercube, {0,1}n, which has size 2n-1+1. Then there must be a point in S with at least ~nc neighbors in S.

Here c>0 is some constant (say 1/2), and two points in S are "neighbors" if and only they differ in a single coordinate. Note that if S had size 2n-1, then the above statement would be false--as witnessed, for example, by the set of all n-bit strings with an even number of 1's.

Huang proceeds by proving the Gotsman-Linial Conjecture. And the way he proves Gotsman-Linial is … well, at this point maybe I should just let you [read the damn preprint](http://www.mathcs.emory.edu/~hhuan30/papers/sensitivity_1.pdf) yourself. I can't say it more simply than he does.

If I had to try anyway, I'd say: Huang constructs a 2n×2n matrix, called An, that has 0's where there are no edges between the corresponding vertices of the Boolean hypercube, and either 1's or -1's where there _are_ edges--with a simple, weird pattern of 1's and -1's that magically makes everything work. He then lets H be an induced subgraph of the Boolean hypercube of size 2n-1+1. He lower-bounds the maximum degree of H by the largest eigenvalue of the corresponding (2n-1+1)×(2n-1+1) submatrix of An. Finally, he lower-bounds that largest eigenvalue by … no, I don't want to spoil it! Read it yourself!

Paul Erdös famously spoke of a book, maintained by God, in which was written the simplest, most beautiful proof of each theorem. The highest compliment Erdös could give a proof was that it "came straight from the book." In this case, I find it hard to imagine that even God knows how to prove the Sensitivity Conjecture in any simpler way than this.

Indeed, the question is: how could such an elementary 1.5-page argument have been overlooked for 30 years? I don't have a compelling answer to that, besides noting that "short" and "elementary" often have little to do with "obvious." Once you start looking at the spectral properties of this matrix An, the pieces snap together in precisely the right way--but how would you know to look at that?

By coincidence, earlier today I finished reading my first PG Wodehouse novel (_[Right Ho, Jeeves!](http://www.gutenberg.org/files/10554/10554-h/10554-h.htm)_), on the gushing recommendation of a friend. I don't know how I'd missed Wodehouse for 38 years. His defining talent is his ability to tie together five or six plot threads in a way that feels perfect and inevitable even though you didn't see it coming. This produces a form of pleasure that's nearly indistinguishable from the pleasure one feels in reading a "proof from the book." So my pleasure centers are pretty overloaded today--but in such depressing times for the world, I'll take pleasure wherever I can get it.

Huge congratulations to Hao!

**Added thought:** What this really is, is one of the purest illustrations I've seen in my career of the power and glory of the P≠NP phenomenon. We talk all the time about how proofs are easier to verify than to find. In practice, though, it can be far from obvious that that's true. Consider your typical STOC/FOCS paper: writing it probably took the authors several months, while fully understanding the thing from scratch would probably take … _also_ several months! If there's a gap, it's only by a factor of 4 or 5 or something. Whereas in this case, I don't know how long Huang spent searching for the proof, but the combined search efforts of the community add up to years or decades. The ratio of the difficulty of finding to the difficulty of completely grasping is in the hundreds of thousands or millions.

**Another added thought:** Because Hao actually proves a stronger statement than the original Sensitivity Conjecture, it has additional implications, a few of which Hao mentions in his preprint. Here's one he didn't mention: any randomized algorithm to guess the parity of an n-bit string, which succeeds with probability at least 2/3 on the majority of strings, must make at least ~√n queries to the string, while any such quantum algorithm must make at least ~n1/4 queries. For more, see the paper [Weak Parity](https://arxiv.org/pdf/1312.0036.pdf) by me, Ambainis, Balodis, and Bavarian (Section 6).

**Important Update:** Hao Huang himself has graciously [visited the comment section](https://scottaaronson.blog/?p=4229#comment-1813116) to satisfy readers' curiosity by providing a detailed timeline of his work on the Sensitivity Conjecture. (tl;dr: he was introduced to the problem by Mike Saks in 2012, and had been attacking it on and off since then, until he finally had the key insight this past month while writing a grant proposal. Who knew that grant proposals could ever be useful for anything?!?)

**Another Update:** In the comments section, my former student Shalev Ben-David points out a [simplification](https://scottaaronson.blog/?p=4229#comment-1813084) of Huang's argument, which no longer uses Cauchy's interlacing theorem. I thought there was no way this proof could possibly be made any simpler, and I was wrong!
