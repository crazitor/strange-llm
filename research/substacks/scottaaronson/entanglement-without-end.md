---
title: "Entanglement without end"
author: "Scott Aaronson"
date: "Mon, 20 Jun 2016"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=2820"
---

Today we take a break from this blog's usual round of topics--free will, consciousness, the Singularity, social justice, Donald Trump--to talk about something _really_ crazy and left-field. Namely, recent research in quantum information.

Earlier this month, [William Slofstra](http://elliptic.space/), currently a Research Assistant Professor at the IQC in Waterloo, posted a [breakthrough paper](http://arxiv.org/abs/1606.03140) on the arXiv (yeah, I'm using the b-word again--sue me), which solves one version of a ten-year-old problem in entanglement theory called [Tsirelson's Problem](http://arxiv.org/abs/0812.4305). The problem, in one sentence, asks whether all quantum-mechanical correlations that can be achieved using commuting measurements, can also be achieved using measurements on separate parts of a tensor-product Hilbert space. The answer turns out to be **no**. (We've long known that the two kinds of correlations are identical as long as you stick to finite-dimensional Hilbert spaces, but Slofstra shows that they can differ in infinite-dimensional spaces.)

One implication of Slofstra's result can be stated much more concretely, in terms of _two-prover games_ : those things like the famous [Bell/CHSH experiment](https://en.wikipedia.org/wiki/Bell_test_experiments), where Alice and Bob are put in separate rooms, and get inputs _x_ and _y_ respectively, and then without communicating, have to produce outputs _a_ and _b_ respectively satisfying some relation _V_(_x_ ,_y_ ,_a_ ,_b_). We've long known examples of two-prover games, like the Mermin-Peres [magic square game](http://arxiv.org/abs/1209.3819), that can be won 100% of the time if Alice and Bob share quantum entanglement, but that can't be won 100% of the time in a classical universe. Slofstra gives the first example of something different: namely, **a two-prover game that can be won 100% of the time using commuting measurements in an****infinite-dimensional Hilbert space --something "formally within the rules of quantum mechanics"--but that can't be won 100% of the time using any finite number of qubits of entanglement.**

(Previously, [Leung, Toner, and Watrous](https://arxiv.org/abs/0804.4118) had given a simpler example of such a game, but theirs required the referee to exchange quantum messages with Alice and Bob.)

If that's not enough, Slofstra's construction also shows that, given as input a description of a two-prover game, it's _undecidable_ (as in, equivalent to the halting problem) whether Alice and Bob can win the game with certainty using commuting measurements on an infinite-dimensional Hilbert space. Notoriously, quantum computing theorists have been unable to put _any_ upper bound (not even "computable") on the complexity class [MIP*](http://www.scottaaronson.com/showcase2/report/travis-hance.pdf), consisting of languages that admit multi-prover interactive systems with entangled provers--precisely because they've been unable to bound how much entanglement the provers might need to implement their optimal strategy. Slofstra's result helps to explain why this problem has been so vexing. I hasten to add, though, that his result doesn't imply that MIP* contains anything uncomputable, since it remains plausible that anything Alice and Bob can do with infinite entanglement, they can approximate well enough with a finite amount.

That last remark leads to a further fundamental question, one that Slofstra leaves open. Namely, even if Alice and Bob need infinite entanglement to win Slofstra's game with certainty, can they at least win it with probability _arbitrarily close_ to 100%, using larger and larger finite amounts of entanglement? More broadly, could there exist a game that was winnable with certainty using infinite entanglement, but with at most (say) 90% probability using _any_ finite amount of entanglement? That problem was shown, by [Ozawa](https://arxiv.org/abs/1212.1700) (see also [Scholz and Werner](http://arxiv.org/pdf/0812.4305v1.pdf)), to be equivalent to a famous unsolved problem in operator algebras called the [Connes embedding problem](https://en.wikipedia.org/wiki/Connes_embedding_problem).

Clarifying the matter further, Slofstra (following [earlier authors](https://arxiv.org/abs/1503.07207)) points out that there are really  _four_ classes of two-prover games in play here:

  1. Games that can be won with certainty using some fixed, finite amount of entanglement.
  2. Games that can be won with certainty using an infinite amount of entanglement, but still in a tensor-product Hilbert space, HA⊗HB.
  3. Games that can be won with probability _approaching_ 1, using an infinite sequence of strategies from class 1, or equivalently (as it turns out) from class 2.
  4. Games that can be won with certainty using measurements by Alice and Bob on an infinite-dimensional quantum state |ψ〉, where we require all of Alice's measurements to commute with all of Bob's, but don't require |ψ〉 to have a tensor-product structure.



It can be shown that 1 is a subset of 2 is a subset of 3 is a subset of 4. Previously, we didn't know _any_ of these containments to be strict. Slofstra's result shows that class 2 differs from class 4--and as a consequence, that class 1 differs from class 4 as well. The Connes embedding problem, which remains open, asks whether 3 differs from 4. It also remains open whether 1 differs from 2 and whether 2 differs from 3.

* * *

OK, you ask, but what's the broader importance of any of this? To me, these problems touch on a question of almost metaphysical significance: namely, _what sorts of experimental evidence could possibly bear on whether the universe was discrete or continuous?_

Because of the Bekenstein bound from quantum gravity, I'm of the opinion that the Hilbert spaces relevant to our universe are ultimately finite-dimensional--or more concretely, that any bounded physical system can store at most ~1069 qubits per square meter of surface area. And in quantum computing and information, almost everything we care about only requires finite-dimensional Hilbert spaces--the subject of this blog post being a striking exception!

Yet if you take a traditional quantum mechanics course, virtually every example you see will involve _infinite_ -dimensional Hilbert spaces--starting with the harmonic oscillator, the hydrogen atom, and coherent states of light. And indeed, when I've banged the drum about finite-dimensional QM being the truly fundamental kind, physicists have often retorted by pointing to one of the very first things they learn: the [position/momentum commutation relation](https://en.wikipedia.org/wiki/Canonical_commutation_relation), which only makes sense in infinite-dimensional Hilbert space. Of course, if you tried to _probe_ position/momentum commutation to greater and greater precision, eventually your experiments would run up against the limits of quantum gravity, so this retort doesn't imply that infinite dimensions actually exist at the machine-code level of the universe. But still: is there some  _conceivable_ experiment for which a positive result would show us that Nature wasn't describable by a finite number of qubits, but only by an infinite number?

A few years ago, Tobias Fritz wrote a [lovely paper](http://arxiv.org/abs/1202.3817) about precisely that question. He gave an example of an identity--namely,

V-1U2V=U3 implies UV-1UV=V-1UVU

--that holds for all finite dimensional unitary matrices U and V, but fails badly for certain infinite-dimensional ones. He suggested that, if this identity were discovered to fail, then Occam's Razor would favor an infinite-dimensional Hilbert space for our universe.

Unfortunately, Fritz's example is open to the same sort of objection that Slofstra's game is. Namely, as Fritz points out, if the antecedent (V-1U2V=U3) held to excellent precision but not perfectly, then his identity could "fail to within experimental limits," even if our universe had a finite-dimensional Hilbert space and therefore satisfied his identity.

OK, but suppose that the Connes embedding problem had a negative answer--or equivalently, that there existed a two-prover game G that could be won with certainty using commuting operators, but that couldn't be won (say) 90% of the time using any finite amount of entanglement. In that case, the believers in a quantumly finite universe, like myself, would have to put some real money on the table, in much the same way the original Bell inequality forced the believers in Einsteinian local hidden variables to put money down. We finitists would have to say that the game G _couldn 't_ be won with certainty in the real world, even though formally, winning G with certainty wouldn't seem to contradict either quantum mechanics or locality. And if, hypothetically, an experiment showed that G _could_ be won with certainty--or indeed, with any probability bounded above 90%--then our position would've been falsified, much like the Bell experiments falsified Einsteinian locality.

* * *

So how did Slofstra prove his result? I'll be brief, since [STOC'2016](http://acm-stoc.org/stoc2016/) is happening in Cambridge right now, and I'd like to get over there in time for lunch.

If you like, the key idea is to start with equations that have infinite-dimensional solutions but no finite-dimensional ones. The most famous such equation is the position/momentum commutation relation mentioned earlier, which for our purposes is just the following matrix equation:

AB - BA = I.

This equation can't be satisfied by any finite-dimensional matrices, since AB and BA have the same [trace](https://en.wikipedia.org/wiki/Trace_\(linear_algebra\)), so Tr(AB-BA)=0, but Tr(I) is nonzero. But, OK, let A be the infinite-dimensional linear operator that takes as input the coefficients of a polynomial c0+c1x+c2x2+… and that differentiates the polynomial, and let B be the linear operator that multiplies the polynomial by x. Then I invite you to check that the equation holds.

It's not known at present how to turn the above equation into a two-prover game--I regard it as a fascinating question whether that's possible. Rather than an algebraic equation (involving both addition and multiplication), Slofstra instead needs to start with _group_ equations (involving only multiplication)--ones with the strange property that they're satisfied only by the identity matrix or by infinite matrices. Equivalently, he needs a group, defined by a finite list of generators and relations, that admits no nontrivial finite-dimensional matrix representations. Fortunately for him, such groups exist--the first known example being [Higman's group](https://en.wikipedia.org/wiki/Higman_group), discovered in 1951. Higman's group is generated by four elements, a,b,c,d, which satisfy the equations

a-1ba = b2, b-1cb = c2, c-1dc = d2, d-1ad = a2.

I don't have a good intuition for Higman's group, but if I did, it would come from rereading [this post by Terry Tao](https://terrytao.wordpress.com/2008/10/06/finite-subsets-of-groups-with-no-finite-models/). Certainly it has no known "physics interpretation" analogous to that for the position/momentum commutation relation.

Anyway, given such a group, the hard part, the new part, is to give a general way to convert them into the kinds of groups that can be realized as two-prover games. So that's what Slofstra does, using 50 pages dense with commutative diagrams, quotient maps, and other Serious Math Stuff--hey, I told you this part of the post would be brief! For more, see his [paper](http://arxiv.org/pdf/1606.03140v1.pdf).

Now, once you have this general transformation of groups, you can also use it to show that there's no algorithm to decide whether a two-prover game has a perfect commuting strategy, by taking the [word problem for groups](https://en.wikipedia.org/wiki/Word_problem_for_groups), which is known to be undecidable, and reducing it to that problem.

Anyway, infinite congrats (or the limit of arbitrarily large finite congrats?) to Slofstra for this achievement! Now it's off to STOC, which I guess you could also ask me about in the comments if you wanted.

* * *

**Unrelated Announcement (June 21):** Ran Raz asks me to announce a [workshop for Avi Wigderson's 60th birthday](https://www.math.ias.edu/avi60), to be held at the Institute for Advanced Study in Princeton October 6-8. I'll be speaking there, and I hope to see many of you there as well!
