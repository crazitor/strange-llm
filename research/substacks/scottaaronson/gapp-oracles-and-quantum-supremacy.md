---
title: "GapP, Oracles, and Quantum Supremacy"
author: "Scott Aaronson"
date: "Fri, 01 Sep 2017"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=3427"
---

Let me start with a few quick announcements before the main entrée:

First, the website [haspvsnpbeensolved.com](http://haspvsnpbeensolved.com) is now live!  Thanks so much to my friend Adam Chalmers for setting it up.  Please try it out on your favorite P vs. NP solution paper--I think you'll be impressed by how well our secret validation algorithm performs.

Second, some readers might enjoy a [YouTube video](https://www.youtube.com/watch?v=fUGjv44_X4Q&index=4&list=PLUz_4vZOI0H1XnMEj9uk4Ezp9AUJBVAPE) of me lecturing about the computability theory of closed timelike curves, from the [Workshop on Computational Complexity and High Energy Physics](http://cchep2017.quics.umd.edu/) at the University of Maryland a month ago.  [Other videos](https://www.youtube.com/playlist?list=PLUz_4vZOI0H1XnMEj9uk4Ezp9AUJBVAPE) from the workshop--including of talks by John Preskill, Daniel Harlow, Stephen Jordan, and other names known around _Shtetl-Optimized_ , and of a panel discussion in which I participated--are worth checking out as well.  Thanks so much to Stephen for organizing such a great workshop!

Third, thanks to everyone who's emailed to ask whether I'm holding up OK with Hurricane Harvey, and whether I know how to swim (I do).  As it happens, I haven't been in Texas for two months--I spent most of the summer visiting NYU and doing other travel, and this year, Dana and I are doing an early sabbatical at Tel Aviv University.  However, I understand from friends that Austin, being several hours' drive further inland, got _nothing_ compared to what Houston did, and that UT is open on schedule for the fall semester.  Hopefully our house is still standing as well!  Our thoughts go to all those affected by the disaster in Houston.  Eventually, the Earth's rapidly destabilizing climate almost certainly means that Austin will be threatened as well by "500-year events" happening every year or two, as for that matter will a large portion of the earth's surface.  For now, though, Austin lives to be weird another day.

* * *

**GapP, Oracles, and Quantum Supremacy**

by Scott Aaronson

Stuart Kurtz 60th Birthday Conference, Columbia, South Carolina 

August 20, 2017

It's great to be here, to celebrate the life and work of Stuart Kurtz, which could never be … _eclipsed_ … by anything.

I wanted to say something about work in structural complexity and counting complexity and oracles that Stuart was involved with "back in the day," and how that work plays a major role in issues that concern us right now in quantum computing.  A major goal for the next few years is the unfortunately-named Quantum Supremacy.  What this means is to get a clear quantum speedup, for _some_ task: not necessarily a useful task, but something that we can be as confident as possible is classically hard.  For example, consider the 49-qubit superconducting chip that Google is planning to fabricate within the next year or so.  This won't yet be good enough for running Shor's algorithm, to factor numbers of any interesting size, but it hopefully _will_  be good enough to sample from a probability distribution over n-bit strings--in this case, 49-bit strings--that's hard to sample from classically, taking somewhere on the order of 249 steps.

Furthermore, the evidence that that sort of thing is indeed classically hard, might actually be _stronger_ than the evidence that factoring is classically hard.  As I like to say, a fast classical factoring algorithm would "merely" collapse the world's electronic commerce--as far as we know, it wouldn't collapse the polynomial hierarchy!  By contrast, a fast classical algorithm to simulate quantum sampling _would_ collapse the polynomial hierarchy, assuming the simulation is exact.  Let me first go over the argument for that, and then explain some of the more recent things we've learned.

Our starting point will be two fundamental complexity classes, [#P](https://en.wikipedia.org/wiki/Sharp-P) and [GapP](https://en.wikipedia.org/wiki/GapP).

#P is the class of all nonnegative integer functions f, for which there exists a nondeterministic polynomial-time Turing machine M such that f(x) equals the number of accepting paths of M(x).  Less formally, #P is the class of problems that boil down to summing up an exponential number of nonnegative terms, each of which is efficiently computable individually.

GapP--introduced by [Fenner, Fortnow, and Kurtz](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.42.5938) in 1992--can be defined as the set {f-g : f,g∈#P}; that is, the closure of #P under subtraction.  Equivalently, GapP is the class of problems that boil down to summing up an exponential number of terms, each of which is efficiently computable individually, but which could be either positive or negative, and which can therefore cancel each other out.  As you can see, GapP is a class that in some sense anticipates quantum computing!

For our purposes, the most important difference between #P and GapP is that #P functions can at least be multiplicatively _approximated_ in the class BPPNP, by using Stockmeyer's technique of approximating counting with universal hash functions.  By contrast, even if you just want to approximate a GapP function to within (say) a factor of 2--or for that matter, just decide whether a GapP function is positive or negative--it's not hard to see that that's already a #P-hard problem.  For, supposing we had an oracle to solve this problem, we could then shift the sum this way and that by adding positive and negative dummy terms, and use binary search, to zero in on the sum's _exact_ value in polynomial time.

It's also not hard to see that a quantum computation can encode an arbitrary GapP function in one of its amplitudes.  Indeed, let s:{0,1}n→{1,-1} be any Boolean function that's given by a polynomial-size circuit.  Then consider the quantum circuit below.

When we run this circuit, the probability that we see the all-0 string as output is

$$ \left( \frac{1}{\sqrt{2^n}} \sum_{z\in \\{0,1\\}^n} s(z) \right)^2 = \frac{1}{2^n} \sum_{z,w\in \\{0,1\\}^n} s(z) s(w) $$

which is clearly in GapP, and clearly #P-hard even to approximate to within a multiplicative factor.

By contrast, suppose we had a probabilistic polynomial-time classical algorithm, call it M, to sample the output distribution of the above quantum circuit.  Then we could rewrite the above probability as Prr[M(r) outputs 0…0], where r consists of the classical random bits used by M.  This is again an exponentially large sum, with one term for each possible r value--but now it's a sum of _nonnegative_ terms (probabilities), which is therefore approximable in BPPNP.

We can state the upshot as follows.  Let ExactSampBPP be the class of _sampling problems_ --that is, families of probability distributions {Dx}x, one for each input x∈{0,1}n--for which there exists a polynomial-time randomized algorithm that outputs a sample exactly from Dx, in time polynomial in |x|.  Let ExactSampBQP be the same thing except that we allow a polynomial-time quantum algorithm.  Then we have that, if ExactSampBPP = ExactSampBQP, then squared sums of both positive and negative terms, could efficiently be rewritten as sums of nonnegative terms only--and hence P#P=BPPNP.  This, in turn, would collapse the polynomial hierarchy to the third level, by Toda's Theorem that PH⊆P#P, together with the result BPPNP⊆∑3.  To summarize:

**Theorem 1.**   Quantum computers can efficiently solve exact sampling problems that are classically hard unless the polynomial hierarchy collapses.

(In fact, the argument works not only if the classical algorithm exactly samples Dx, but if it samples from any distribution in which the probabilities are multiplicatively close to Dx's.  If we really only care about exact sampling, then we can strengthen the conclusion to get that PH collapses to the second level.)

This sort of reasoning was implicit in several early works, including those of [Fenner et al.](https://arxiv.org/abs/quant-ph/9812056) and [Terhal and DiVincenzo](https://arxiv.org/abs/quant-ph/0205133).  It was made fully explicit in [my paper with Alex Arkhipov](http://theoryofcomputing.org/articles/v009a004/v009a004.pdf) on BosonSampling in 2011, and in the [independent work](https://arxiv.org/abs/1005.1407) of Bremner, Jozsa, and Shepherd on the IQP model.  These works actually showed something stronger, which is that we get a collapse of PH, not merely from a fast classical algorithm to simulate _arbitrary_ quantum systems, but from fast classical algorithms to simulate various special quantum systems.  In the case of BosonSampling, that special system is a collection of identical, non-interacting photons passing through a network of beamsplitters, then being measured at the very end to count the number of photons in each mode.  In the case of IQP, the special system is a collection of qubits that are prepared, subjected to some commuting Hamiltonians acting on various subsets of the qubits, and then measured.  These special systems don't seem to be capable of universal quantum computation (or for that matter, even universal classical computation!)--and correspondingly, many of them seem easier to realize in the lab than a full universal quantum computer.

From an experimental standpoint, though, _all_ these results are unsatisfactory, because they all talk only about the classical hardness of _exact_ (or very nearly exact) sampling--and indeed, the arguments are based around the hardness of estimating just a single, exponentially-small amplitude.  But any real experiment will have tons of noise and inaccuracy, so it seems only fair to let the classical simulation be subject to serious noise and inaccuracy as well--but as soon as we do, the previous argument collapses.

Thus, from the very beginning, Alex Arkhipov and I took it as our "real" goal to show, under some reasonable assumption, that there's a distribution D that a polynomial-time quantum algorithm can sample from, but such that no polynomial-time classical algorithm can sample from any distribution that's even _ε-close_ to D in variation distance.  Indeed, this goal is what led us to BosonSampling in the first place: we knew that we needed amplitudes that were not only #P-hard but "robustly" #P-hard; we knew that the [permanent](https://en.wikipedia.org/wiki/Permanent) of an n×n matrix (at least over finite fields) was the canonical example of a "robustly" #P-hard function; and finally, we knew that systems of identical non-interacting bosons, such as photons, gave rise to amplitudes that were permanents in an extremely natural way.  The fact that photons actually exist in the physical world, and that our friends with quantum optics labs like to do experiments with them, was just a nice bonus!

A bit more formally, let ApproxSampBPP be the class of sampling problems for which there exists a classical algorithm that, given an input x∈{0,1}n and a parameter ε>0, samples a distribution that's at most  away from Dx in variation distance, in time polynomial in n and 1/ε.  Let ApproxSampBQP be the same except that we allow a quantum algorithm.  Then the "dream" result that we'd love to prove--both then and now--is the following.

**Strong Quantum Supremacy Conjecture.**  If ApproxSampBPP = ApproxSampBQP, then the polynomial hierarchy collapses.

Unfortunately, Alex and I were only able to prove this conjecture assuming a further hypothesis, about the permanents of i.i.d. Gaussian matrices.

**Theorem 2 (A.-Arkhipov).**  Given an n×n matrix X of independent complex Gaussian entries, each of mean 0 and variance 1, assume it's a #P-hard problem to approximate |Per(X)|2 to within ±ε⋅n!, with probability at least 1-δ over the choice of X, in time polynomial in n, 1/ε, and 1/δ.  Then the Strong Quantum Supremacy Conjecture holds.  Indeed, more than that: in such a case, even a fast approximate classical simulation of BosonSampling, in particular, would imply P#P=BPPNP and hence a collapse of PH.

Alas, after some months of effort, we were unable to prove the needed #P-hardness result for Gaussian permanents, and it remains an outstanding open problem--there's not even a consensus as to whether it should be true or false.  Note that there _is_ a famous polynomial-time classical algorithm to approximate the permanents of _nonnegative_ matrices, due to [Jerrum, Sinclair, and Vigoda](https://www.cc.gatech.edu/~vigoda/Permanent.pdf), but that algorithm breaks down for matrices with negative or complex entries.  This is once again the power of cancellations, the difference between #P and GapP.

Frustratingly, if we want the exact permanents of i.i.d. Gaussian matrices, we were able to prove that that's #P-hard; and if we want the approximate permanents of arbitrary matrices, we also know that _that 's_ #P-hard--it's only when we have approximation and random inputs in the same problem that we no longer have the tools to prove #P-hardness.

In the meantime, one can also ask a meta-question.  How hard should it be to prove the Strong Quantum Supremacy Conjecture?  Were we right to look at slightly exotic objects, like the permanents of Gaussian matrices?  Or could Strong Quantum Supremacy have a "pure, abstract complexity theory proof"?

Well, one way to formalize that question is to ask whether Strong Quantum Supremacy has a _relativizing_ proof, a proof that holds in the presence of an arbitrary oracle.  Alex and I explicitly raised that as an open problem in our BosonSampling paper.

Note that "weak" quantum supremacy--i.e., the statement that ExactSampBPP = ExactSampBQP collapses the polynomial hierarchy--has a relativizing proof, namely the proof that I sketched earlier.  All the ingredients that we used--Toda's Theorem, Stockmeyer approximate counting, simple manipulations of quantum circuits--were relativizing ingredients.  By contrast, all the way back in 1998, [Fortnow and Rogers](https://arxiv.org/abs/cs/9811023) proved the following.

**Theorem 3 (Fortnow and Rogers).**  There exists an oracle relative to which P=BQP and yet PH is infinite.

In other words, if you want to prove that P=BQP collapses the polynomial hierarchy, the proof can't be relativizing.  This theorem was subsequently [generalized](https://people.cs.uchicago.edu/~fortnow/papers/obt.ps) in a paper by Fenner, Fortnow, Kurtz, and Li, which used concepts like "generic oracles" that seem powerful but that I don't understand.

The trouble is, Fortnow and Rogers's construction was extremely tailored to making P=BQP.  It didn't even make PromiseBPP=PromiseBQP (that is, it allowed that quantum computers might still be stronger than classical ones for _promise problems_), let alone did it collapse quantum with classical for sampling problems.

We can organize the various quantum/classical collapse possibilities as follows:

ExactSampBPP = ExactSampBQP  
⇓  
ApproxSampBPP = ApproxSampBQP   ⇔   FBPP = FBQP  
⇓  
PromiseBPP = PromiseBQP  
⇓  
BPP = BQP

Here FBPP is the class of _relation problems_ solvable in randomized polynomial time--that is, problems where given an input x∈{0,1}n and a parameter ε>0, the goal is to produce any output in a certain set Sx, with success probability at least 1-ε, in time polynomial in n and 1/ε.  FBQP is the same thing except for quantum polynomial time.

The equivalence between the two equalities ApproxSampBPP = ApproxSampBQP and FBPP=FBQP is not obvious, and was the main result in my 2011 paper [The Equivalence of Sampling and Searching](http://www.scottaaronson.com/papers/samprel.pdf).  While it's easy to see that ApproxSampBPP = ApproxSampBQP implies FBPP=FBQP, the opposite direction requires us to take an arbitrary sampling problem S, and define a relation problem RS that has "essentially the same difficulty" as S (in the sense that RS has an efficient classical algorithm iff S does, RS has an efficient quantum algorithm iff S does, etc).  This, in turn, we do using Kolmogorov complexity: basically, RS asks us to output a tuple of samples that have large probabilities according to the requisite probability distribution from the sampling problem; and that also, conditioned on that, are close to algorithmically random.  The key observation is that, if a probabilistic Turing machine of fixed size can solve that relation problem for arbitrarily large inputs, then it _must_ be doing so by sampling from a probability distribution close in variation distance to D--since any other approach would lead to outputs that were algorithmically compressible.

Be that as it may, staring at the chain of implications above, a natural question is which equalities in the chain collapse the polynomial hierarchy in a relativizing way, and which equalities collapse PH (if they do) only for deeper, non-relativizing reasons.

This is one of the questions that Lijie Chen and I took up, and settled, in our paper [Complexity-Theoretic Foundations of Quantum Supremacy Experiments](http://www.scottaaronson.com/papers/quantumsupre.pdf), which was presented at this summer's Computational Complexity Conference (CCC) in Riga.  The "main" results in our paper--or at least, the results that the physicists care about--were about how confident we can be in the classical hardness of simulating quantum sampling experiments with random circuits, such as the experiments that the Google group will hopefully be able to do with its 49-qubit device in the near future.  This involved coming up with a new hardness assumption, which was tailored to those sorts of experiments, and giving a reduction from that new assumption, and studying how far existing algorithms come toward breaking the new assumption (tl;dr: not very far).

But our paper also had what I think of as a "back end," containing results mainly of interest to complexity theorists, about what kinds of quantum supremacy theorems we can and can't hope for in principle.  When I'm giving talks about our paper to physicists, I never have time to get to this back end--it's always just "blah, blah, we also did some stuff involving structural complexity and oracles."  But given that a large fraction of all the people on earth who enjoy those things are probably right here in this room, in the rest of this talk, I'd like to tell you about what was in the back end.

The first thing there was the following result.

**Theorem 4 (A.-Chen).**  There exists an oracle relative to which ApproxSampBPP = ApproxSampBQP and yet PH is infinite. In other words, any proof of the Strong Quantum Supremacy Conjecture will require non-relativizing techniques.

Theorem 4 represents a substantial generalization of Fortnow and Rogers's Theorem 3, in that it makes quantum and classical equivalent not only for promise problems, but even for approximate sampling problems.  There's also a sense in which Theorem 4 is the best possible: as we already saw, there are no oracles relative to which ExactSampBPP = ExactSampBQP and yet PH is infinite, because the opposite conclusion relativizes.

So how did we prove Theorem 4?  Well, we learned at this workshop that Stuart Kurtz pioneered the development of principled ways to prove oracle results just like this one, with multiple "nearly conflicting" requirements.  But, because we didn't know that at the time, we basically just plunged in and built the oracle we wanted by hand!

In more detail, you can think of our oracle construction as proceeding in three steps.

  1. We throw in an oracle for a PSPACE-complete problem.  This collapses ApproxSampBPP with ApproxSampBQP, which is what we want.  Unfortunately, it also collapses the polynomial hierarchy down to P, which is _not_ what we want!
  2. So then we need to add in a second part of the oracle that makes PH infinite again.  From Håstad's seminal work in the 1980s until recently, even if we just wanted any oracle that makes PH infinite, without doing anything else at the same time, we only knew how to achieve that with quite special oracles.  But in their 2015 breakthrough, [Rossman, Servedio, and Tan](https://arxiv.org/abs/1504.03398) have shown that even a _random_ oracle makes PH infinite with probability 1.  So for simplicity, we might as well take this second part of the oracle to be random.  The "only" problem is that, along with making PH infinite, a random oracle will _also_ re-separate ApproxSampBPP and ApproxSampBQP (and for that matter, even ExactSampBPP and ExactSampBQP)--for example, because of the Fourier sampling task performed by the quantum circuit I showed you earlier!  So we once again seem back where we started.  
(To ward off confusion: ever since Fortnow and Rogers posed the problem in 1998, it remains frustratingly open whether BPP and BQP can be separated by a random oracle--that's a problem that I and others have worked on, making [partial progress](http://www.scottaaronson.com/papers/struc.pdf) that makes a query complexity separation look unlikely without definitively ruling one out.  But separating the _sampling_ versions of BPP and BQP by a random oracle is much, much easier.)
  3. So, finally, we need to take the random oracle that makes PH infinite, and "scatter its bits around randomly" in such a way that a PH machine can still find the bits, but an ApproxSampBQP machine can't.  In other words: given our initial random oracle A, we can make a new oracle B such that B(y,r)=(1,A(y)) if r is equal to a single randomly-chosen "password" ry, depending on the query y, and B(y,r)=(0,0) otherwise.  In that case, it takes just one more existential quantifier to guess the password ry, so PH can do it, but a quantum algorithm is stuck, basically because the linearity of quantum mechanics makes the algorithm not very sensitive to tiny random changes to the oracle string (i.e., the same reason why Grover's algorithm can't be arbitrarily sped up).  Incidentally, the reason why the password ry needs to depend on the query y is that otherwise the input x to the quantum algorithm could hardcode a password, and thereby reveal exponentially many bits of the random oracle A.



We should now check: why does the above oracle "only" collapse ApproxSampBPP and ApproxSampBQP?  Why doesn't it also collapse ExactSampBPP and ExactSampBQP--as we know that it can't, by our previous argument?  The answer is: because a quantum algorithm _does_ have an exponentially small probability of correctly guessing a given password ry.  And that's enough to make the distribution sampled by the quantum algorithm differ, by 1/exp(n) in variation distance, from the distribution sampled by any efficient classical simulation of the algorithm--an error that doesn't matter for approximate sampling, but _does_ matter for exact sampling.

Anyway, it's then just like seven pages of formalizing the above intuitions and you're done!

OK, since there seems to be time, I'd like to tell you about _one more_  result from the back end of my and Lijie's paper.

If we can work relative to whatever oracle A we like, then it's easy to get quantum supremacy, and indeed BPPA≠BQPA.  We can, for example, use Simon's problem, or Shor's period-finding problem, or [Forrelation](https://www.scottaaronson.com/papers/for.pdf), or other choices of black-box problems that admit huge, provable quantum speedups.  In the unrelativized world, by contrast, it's clear that we have to make _some_ complexity assumption for quantum supremacy--even if we just want ExactSampBPP ≠ ExactSampBQP.  For if (say) P=P#P, then ExactSampBPP and ExactSampBQP would collapse as well.

Lijie and I were wondering: what happens if we try to "interpolate" between the relativized and unrelativized worlds?  More specifically, what happens if our algorithms are allowed to query a black box, _but_ we're promised that whatever's inside the black box is efficiently computable (i.e., has a small circuit)?  How hard is it to separate BPP from BQP, or ApproxSampBPP from ApproxSampBQP, relative to an oracle A that's constrained to lie in P/poly?

Here, we'll start with a beautiful observation that's implicit in [2004 work by Servedio and Gortler](http://www.cs.columbia.edu/~rocco/Public/SG_041291_2.pdf), as well as [2012 work by Mark Zhandry](https://eprint.iacr.org/2012/182.pdf).  In our formulation, this observation is as follows:

**Theorem 5.**  Suppose there exist cryptographic one-way functions (even just against classical adversaries).  Then there exists an oracle A∈P/poly such that BPPA≠BQPA.

While we still need to make a computational hardness assumption here, to separate quantum from classical computing, the surprise is that the assumption is so much _weaker_ than what we're used to.  We don't need to assume the hardness of factoring or discrete log--or for that matter, of _any_  "structured" problem that could be a basis for, e.g., public-key cryptography.  Just a one-way function that's hard to invert, that's all!

The intuition here is really simple.  Suppose there's a one-way function; then it's well-known, by the HILL and GGM Theorems of classical cryptography, that we can bootstrap it to get a cryptographic _pseudorandom function family_.  This is a family of polynomial-time computable functions fs:{0,1}n→{0,1}n, parameterized by a secret seed s, such that fs can't be distinguished from a truly random function f by any polynomial-time algorithm that's given oracle access to the function and that doesn't know s.  Then, as our efficiently computable oracle A that separates quantum from classical computing, we take an ensemble of functions like

gs,r(x) = fs(x mod r),

where r is an exponentially large integer that serves as a "hidden period," and s and r are both secrets stored by the oracle that are inaccessible to the algorithm that queries it.

The reasoning is now as follows: certainly there's an efficient quantum algorithm to find r, or to solve some decision problem involving r, which we can use to define a language that's in BQPA but not in BPPA.  That algorithm is just Shor's period-finding algorithm!  (Technically, Shor's algorithm needs certain assumptions on the starting function fs to work--e.g., it couldn't be a constant function--but if those assumptions aren't satisfied, then fs wasn't pseudorandom anyway.)  On the other hand, suppose there were an efficient classical algorithm to find the period r.  In that case, we have a dilemma on our hands: would the classical algorithm still have worked, had we replaced fs by a _truly_ random function?  If so, then the classical algorithm would violate well-known lower bounds on the classical query complexity of period-finding.  But if not, then by working on pseudorandom functions but not on truly random functions, the algorithm would be _distinguishing_ the two--so fs wouldn't have been a cryptographic pseudorandom function at all, contrary to assumption!

This all caused Lijie and me to wonder whether Theorem 5 could be strengthened even further, so that it wouldn't use any complexity assumption at all.  In other words, why couldn't we just prove _unconditionally_ that there's an oracle A∈P/poly such that BPPA≠BQPA?  By comparison, it's not hard to see that we can unconditionally construct an oracle A∈P/poly such that PA≠NPA.

Alas, with the following theorem, we were able to explain why BPP vs. BQP (and even ApproxSampBPP vs. ApproxSampBQP) are different, and why _some_ computational assumption is still needed to separate quantum from classical, even if we're working relative to an efficiently computable oracle.

**Theorem 6 (A.-Chen).**  Suppose that, in the real world, ApproxSampBPP = ApproxSampBQP and NP⊆BPP (granted, these are big assumptions!).  Then ApproxSampBPPA = ApproxSampBQPA for all oracles A∈P/poly.

Taking the contrapositive, this is saying that you can't separate ApproxSampBPP from ApproxSampBQP relative to an efficiently computable oracle, without separating _some_ complexity classes in the real world.  This contrasts not only with P vs. NP, but even with ExactSampBPP vs. ExactSampBQP, which _can_ be separated unconditionally relative to efficiently computable oracles.

The proof of Theorem 6 is intuitive and appealing.  Not surprisingly, we're going to heavily exploit the assumptions ApproxSampBPP = ApproxSampBQP and NP⊆BPP.  Let Q be a polynomial-time quantum algorithm that queries an oracle A∈P/poly.  Then we need to simulate Q--and in particular, sample close to the same probability distribution over outputs--using a polynomial-time _classical_ algorithm that queries A.

Let

$$ \sum_{x,w} \alpha_{x,w} \left|x,w\right\rangle $$

be the state of Q immediately before its first query to the oracle A, where x is the input to be submitted to the oracle.  Then our first task is to get a bunch of samples from the probability distribution D={|αx,w|2}x,w, or something close to D in variation distance.  But this is easy to do, using the assumption ApproxSampBPP = ApproxSampBQP.

Let x1,…,xk be our samples from D, marginalized to the x part.  Then next, our classical algorithm queries A on each of x1,…,xk, getting responses A(x1),…,A(xk).  The next step is to search for a function f∈P/poly--or more specifically, a function of whatever _fixed_ polynomial size is relevant--that agrees with A on the sample data, i.e. such that f(xi)=A(xi) for all i∈[k].  This is where we'll use the assumption NP⊆BPP (together, of course, with the fact that at least one such f exists, namely A itself!), to make the task of finding f efficient.  We'll also appeal to a fundamental fact about the sample complexity of PAC-learning.  The fact is that, if we find a polynomial-size circuit f that agrees with A on a bunch of sample points drawn independently from a distribution, then f will probably agree with A on most further points drawn from the same distribution as well.

So, OK, we then have a pretty good "mock oracle," f, that we can substitute for the real oracle on the first query that Q makes.  Of course f and A won't _perfectly_ agree, but the small fraction of disagreements won't matter much, again because of the linearity of quantum mechanics (i.e., the same thing that prevents us from speeding up Grover's algorithm arbitrarily).  So we can basically simulate Q's first query, and now our classical simulation is good to go until Q's _second_ query!  But now you can see where this is going: we iterate the same approach, and reuse the same assumptions ApproxSampBPP = ApproxSampBQP and NP⊆BPP, to find a new "mock oracle" that lets us simulate Q's second query, and so on until all of Q's queries have been simulated.

OK, I'll stop there.  I don't have a clever conclusion or anything.  Thank you.
