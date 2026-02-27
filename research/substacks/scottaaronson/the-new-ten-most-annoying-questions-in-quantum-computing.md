---
title: "The NEW Ten Most Annoying Questions in Quantum Computing"
author: "Scott Aaronson"
date: "Tue, 13 May 2014"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=1792"
---

Eight years ago, I put up a post entitled [The Ten Most Annoying Questions in Quantum Computing](https://scottaaronson.blog/?p=112). One of the ten wasn't a real question--it was simply a request for readers to submit questions--so let's call it nine. I'm delighted to say that, of the nine questions, **six have by now been completely settled** --most recently, my question about the parallel-repeated value of the CHSH game, which Andris Ambainis pointed out to me last week can be answered using a [2008 result](http://www.cs.cornell.edu/~dsteurer/papers/roundpar.pdf) of Barak et al. combined with a [2013 result](http://arxiv.org/abs/1305.1979) of Dinur and Steurer.

To be clear, the demise of so many problems is _exactly_ the outcome I wanted. In picking problems, my goal wasn't to shock and awe with difficulty--as if to say "_this_ is how smart I am, that whatever stumps me will also stump everyone else for decades." Nor was it to showcase my bottomless profundity, by proffering questions so vague, multipartite, and open-ended that no matter what progress was made, I could always reply "ah, but you still haven't addressed the _real_ question!" Nor, finally, was my goal to list the biggest research directions for the entire field, the stuff everyone already knows about ("is there a polynomial-time quantum algorithm for graph isomorphism?"). My interest was exclusively in "little" questions, in weird puzzles that looked (at least at the time) like there was no deep obstruction to just killing them one by one, _whichever_ way their answers turned out. What made them annoying was that they hadn't succumbed already.

So, now that two-thirds of my problems have met the fate they deserved, at Andris's suggestion I'm presenting a _new_ list of Ten Most Annoying Questions in Quantum Computing--a list that starts with the three still-unanswered questions from the old list, and then adds seven more.

But we'll get to that shortly. First, let's review the six questions that have been answered.

* * *

**CLOSED, NO-LONGER ANNOYING QUESTIONS IN QUANTUM COMPUTING**

1\. Given an n-qubit pure state, is there always a way to apply Hadamard gates to some subset of the qubits, so as to make all 2n computational basis states have nonzero amplitudes? [Positive answer by Ashley Montanaro and Dan Shepherd, posted to this blog in 2006.](https://scottaaronson.blog/?p=132)

3\. Can any QMA(2) ([QMA](http://en.wikipedia.org/wiki/QMA) with two unentangled yes-provers) protocol be amplified to exponentially small error probability? [Positive answer by Aram Harrow and Ashley Montanaro, from a FOCS'2010 paper.](http://arxiv.org/abs/1001.0017)

4\. If a unitary operation U can be applied in polynomial time, then can some square root of U also be applied in polynomial time? [Positive answer by Lana Sheridan, Dmitri Maslov, and Michele Mosca, from a 2008 paper.](http://arxiv.org/abs/0810.3843)

5\. Suppose Alice and Bob are playing n parallel CHSH games, with no communication or entanglement. Is the probability that they’ll win all n games at most pn, for some p bounded below 0.853?

OK, let me relay what Andris Ambainis told me about this question, with Andris's kind permission. First of all, we've known for a while that the optimal success probability is _not_ the (3/4)n that Alice and Bob could trivially achieve by just playing all n games separately. I observed in 2006 that, by correlating their strategies between pairs of games in a clever way, Alice and Bob can win with probability (√10 / 4)n ~ 0.79n. And [Barak et al.](http://www.cs.cornell.edu/~dsteurer/papers/roundpar.pdf) showed in 2008 that they can win with probability ((1+√5)/4)n ~ 0.81n. (Unfortunately, I don't know the actual strategy that achieves the latter bound! Barak et al. say they'll describe it in the full version of their paper, but the full version hasn't yet appeared.)

Anyway, [Dinur-Steurer 2013](http://arxiv.org/abs/1305.1979) gave a general recipe to prove that the value of a repeated projection game is at most αn, where α is some constant that depends on the game in question. When Andris followed their recipe for the CHSH game, he obtained the result α=(1+√5)/4--thereby showing that Barak et al.'s strategy, whatever it is, is precisely optimal! Andris also observes that, for _any_ two-prover game G, the Dinur-Steurer bound α(G) is always strictly less than the entangled value ω*(G), _unless_ the classical and entangled values are the same for one copy of the game (i.e., unless ω(G)=ω*(G)). This implies that parallel repetition can _never_ completely eliminate a quantum advantage.

6\. Forget about an oracle relative to which BQP is not in PH (the Polynomial Hierarchy). Forget about an oracle relative to which BQP is not in AM (Arthur-Merlin). Is there an oracle relative to which BQP is not in SZK (Statistical Zero-Knowledge)? [Positive answer by me, posted to this blog in 2006.](https://scottaaronson.blog/?p=114) See also [my BQP vs. PH paper](http://www.scottaaronson.com/papers/bqpph.pdf) for a different proof.

9\. Is there an n-qubit pure state that can be prepared by a circuit of size n3, and that can’t be distinguished from the maximally mixed state by any circuit of size n2? [A positive answer follows from this 2009 paper by Richard Low](http://arxiv.org/abs/0903.5236)--thanks very much to Fernando Brandao for bringing that to my attention a few months ago.

* * *

OK, now on to:

**THE NEW TEN MOST ANNOYING QUESTIONS IN QUANTUM COMPUTING**

1\. Can we get any upper bound whatsoever on the complexity class QMIP--i.e., quantum multi-prover interactive proofs with unlimited prior entanglement? (Since I asked this question in 2006, [Ito and Vidick](http://arxiv.org/abs/1207.0550) achieved the breakthrough _lower_ bound NEXP⊆QMIP, but there's been basically no progress on the upper bound side.)

2\. Given any n-qubit unitary operation U, does there exist an oracle relative to which U can be (approximately) applied in polynomial time? (Since 2006, my interest in this question has only increased. See [this paper](http://theoryofcomputing.org/articles/v003a007/v003a007.pdf) by me and Greg Kuperberg for background and related results.)

3\. How many [mutually unbiased bases](http://en.wikipedia.org/wiki/Mutually_unbiased_bases) are there in non-prime-power dimensions?

4\. Since Chris Fuchs was so [thrilled](http://arxiv.org/abs/1405.2390) by my including one of his favorite questions on my earlier list (question #3 above), let me add another of his favorites: do [SIC-POVMs](http://en.wikipedia.org/wiki/SIC-POVM) exist in arbitrary finite dimensions?

5\. Is there a Boolean function f:{0,1}n→{0,1} whose bounded-error quantum query complexity is  _strictly_ greater than n/2? (Thanks to Shelby Kimmel for this question! Note that [this paper](http://arxiv.org/abs/quant-ph/9805006) by van Dam shows that the bounded-error quantum query complexity never exceeds n/2+O(√n), while [this paper](http://arxiv.org/abs/1208.1122) by Ambainis et al. shows that it's at least n/2-O(√n) for almost all Boolean functions f.)

6\. Is there a "universal disentangler": that is, a superoperator S that takes nO(1) qubits as input; that produces a 2n-qubit bipartite state (with n qubits on each side) as output; whose output S(ρ) is always close in variation distance to a separable state; and that given an appropriate input state, can produce as output an approximation to _any_ desired separable state? (See [here](http://www.scottaaronson.com/papers/qma2out.pdf) for background about this problem, originally posed by John Watrous. Note that if such an S existed and were computationally efficient, it would imply QMA=QMA(2).)

7\. Suppose we have explicit descriptions of n two-outcome POVM measurements--say, as d×d Hermitian matrices E1,…,En--and are also given k=(log(nd))O(1) copies of an unknown quantum state ρ in d dimensions. Is there a way to measure the copies so as to estimate the n expectation values Tr(E1ρ),…,Tr(Enρ), each to constant additive error? (A forthcoming paper of mine on private-key quantum money will contain some background and related results.)

8\. Is there a collection of 1- and 2-qubit gates that generates a group of unitary matrices that is (a) not universal for quantum computation, (b) not just conjugate to permuted diagonal matrices or one-qubit gates plus swaps, and (c) not conjugate to a subgroup of the Clifford group?

9\. Given a partial Boolean function f:S→{0,1} with S⊆{0,1}n, is the bounded-error quantum query complexity of f always polynomially related to the smallest degree of any polynomial p:{0,1}n→R such that (a) p(x)∈[0,1] for all x∈{0,1}n, and (b) |p(x)-f(x)|≤1/3 for all x∈S?

10\. Is there a quantum finite automaton that reads in an infinite sequence of i.i.d. coin flips, and whose limiting probability of being found in an "accept" state is at least 2/3 if the coin is fair and at most 1/3 if the coin is unfair? (See [this paper](http://www.scottaaronson.com/papers/qcoin13.pdf) by me and Andy Drucker for background and related results.)
