---
title: "More Wrong Things I Said in Papers"
author: "Scott Aaronson"
date: "Fri, 29 Jul 2016"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=2854"
---

Two years ago, I wrote a blog post entitled [PostBQP Postscripts](https://scottaaronson.blog/?p=2072), owning up to not one but _four_ substantive mathematical errors that I'd made over the years in my published papers, and which my students and colleagues later brought to my sheepish attention. Fortunately, none of these errors affected the papers' main messages; they just added interesting new twists to the story. Even so, I remember feeling at the time like undergoing this public repentance was soul-cleansing intellectual hygiene. I also felt like writing one big "post of shame" was _easier_ than writing a bunch of separate errata and submitting them to journals, while also reaching a wider audience (and, therefore, doing an even better soul-cleansing job).

So I resolved that, anytime I'd saved up enough errata, I'd do another sackcloth-and-ashes post. Which brings us to today. Without further ado:

* * *

**I. Quantum Money Falling Down**

My and Paul Christiano's [explicit public-key quantum money scheme](http://theoryofcomputing.org/articles/v009a009/v009a009.pdf)--the one based on low-degree polynomials--has now been fully broken. To clarify, our abstract hidden-subspace scheme--the one that uses a classical black-box to test membership in the subspaces--remains totally fine. Indeed, we unconditionally proved the security of the black-box scheme, and our security proof stands. In the paper, though, we also stuck our necks out further, and conjectured that you could instantiate the black box, by publishing random low-degree polynomials that vanish on the subspaces you want to hide. While I considered this superfluous, at Paul's insistence, we also recommended adding completely-random "noise polynomials" for extra security.

Our scheme was broken in two stages. First, in 2014, [Pena et al.](https://hal.inria.fr/hal-01098223/document) broke the noiseless version of our scheme, using Gröbner-basis methods, over fields of characteristic greater than 2. Over F2--the field we happened to use in our scheme--Pena et al. couldn't quite prove that their attack worked, but they gave numerical evidence that at least it finds the subspaces in nO(log n) time. Note that nothing in Pena et al.'s attack is specific to quantum money: indeed, their attack consists of a purely classical algorithm, which efficiently solves the general classical problem of recovering large subspaces from polynomials that hide them.

At that point, at least the _noisy_ version of our scheme--the one Paul had insisted we include--was still standing! Indeed, the Gröbner-basis attack seemed to break down entirely when some of the polynomials were random garbage.

Later, though, Paul and Or Sattath realized that a quantum trick--basically, the [single-copy tomography](http://arxiv.org/abs/0912.3823) of Farhi et al.--can identify which polynomials are the noisy ones, provided we're given a legitimate quantum money state to start with. As a consequence, the problem of breaking the noisy scheme can be reduced to the problem of breaking the noiseless scheme--i.e., the problem that Pena et al. already essentially solved.

As bad as this sounds, it has an interesting positive consequence. In our paper, Paul and I had actually given a security reduction for our money scheme based on low-degree polynomials. In particular, we showed that there's no polynomial-time quantum algorithm to counterfeit our money states, _unless_ there's a polynomial-time quantum algorithm that finds a basis for a subspace S≤F2n of dimension n/2 with Ω(2-n/2) success probability, given a collection of low-degree polynomials p1,…,pm and q1,…,qm (m=O(n)) most of which vanish on S and its dual subspace respectively, but that are otherwise random. So, running our reduction backwards, the only possible conclusion from the break is that there _is_ such a quantum algorithm! Yet we would've had no idea how to find that quantum algorithm without going through quantum money--nor do we know a classical algorithm for the problem, or even a quantum algorithm with Ω(1) success probability.

In the meantime, the problem of designing a public-key quantum money scheme, with good cryptographic evidence for its security, remains open. It's plausible that there's some other, more secure way to instantiate my and Paul's hidden subspace scheme, for example using lattices. And even before we've found such a way, we can use [indistinguishability obfuscation](http://news.mit.edu/2015/secure-foundation-any-cryptographic-system-1028) as a stopgap. We could also seek cryptographic evidence for the security of other kinds of public-key quantum money, like [Farhi et al.'s](https://arxiv.org/abs/1004.5127) based on knot invariants.

A paper about all this is on our to-do stack. In the meantime, for further details, see Lecture 9 in my [Barbados lecture notes](http://www.scottaaronson.com/barbados-2016.pdf).

* * *

**II. A De-Merlinization Mistake**

In my 2006 paper [QMA/qpoly ⊆ PSPACE/poly: De-Merlinizing Quantum Protocols](http://www.scottaaronson.com/papers/qmaqpoly.pdf), the technical core of the complexity result was a new quantum information lemma that I called the "Quantum OR Bound" (Lemma 14 in the paper).

Basically, the Quantum OR Bound says that, if we have an unknown quantum state ρ, as well as a collection of measurements M1,…,Mn that we might want to make on ρ, then we can distinguish the case that (a) every Mi rejects ρ with overwhelming probability, from the case that (b) at least one Mi accepts ρ with high probability. And we can do this _despite_ having only one copy of ρ, and despite the fact that earlier measurements might corrupt ρ, thereby compromising the later measurements. The intuition is simply that, if the earlier measurements corrupted ρ substantially, that could only be because some of them had a decent probability of accepting ρ, meaning that at any rate, we're not in case (a).

I've since reused the Quantum OR Bound for other problems--most notably, a proof that private-key quantum money requires either a computational assumption or a huge database maintained by the bank (see Theorem 8.3.1 in my [Barbados lecture notes](http://www.scottaaronson.com/barbados-2016.pdf)).

Alas, Aram Harrow and Ashley Montanaro [recently discovered](https://arxiv.org/abs/1607.03236) that my proof of the Quantum OR Bound is wrong. It's wrong because I neglected the possibility of "[Zeno-like](https://en.wikipedia.org/wiki/Quantum_Zeno_effect) behavior," in which repeated measurements on a quantum state would gradually shift the state far away from its starting point, without ever having a significant probability of rejecting the state. For some reason, I assumed without any adequate argument that choosing the measurements at random, rather than in a predetermined order, would solve that problem.

Now, I might actually be  _right_ that randomizing the measurements is enough to solve the Zeno problem! That remains a plausible conjecture, which Harrow and Montanaro could neither confirm nor refute. In the meantime, though, Harrow and Montanaro were able to recover my QMA/qpoly⊆PSPACE/poly theorem, and all the other conclusions known to follow from the Quantum OR Bound (including some new ones that they discover), by designing a _new_ measurement procedure whose soundness they can prove.

Their new procedure is based on an elegant, obvious-in-retrospect idea that somehow never occurred to me. Namely, instead of just applying Mi's to ρ, one can first put a control qubit into an equal superposition of the |0〉 and |1〉 states, and then apply Mi's _conditioned_ on the control qubit being in the |1〉 state. While doing this, one can periodically measure the control qubit in the {|+〉,|-〉} basis, in order to check directly whether applying the Mi's has substantially corrupted ρ. (If it hasn't, one will always get the outcome |+〉; if it has, one might get |-〉.) Substantial corruption, if detected, then tells us that some Mi's must have had non-negligible probabilities of accepting ρ.

* * *

**III. Almost As Good As True**

One lemma that I've used even _more_ than the Quantum OR Bound is what I've called the "Almost As Good As New Lemma," and what others in the field have called the "Gentle Measurement Lemma."

I claimed a proof of the AAGANL in my 2004 paper [Limitations of Quantum Advice and One-Way Communication](http://theoryofcomputing.org/articles/v001a001/v001a001.pdf) (Lemma 2.2 there), and have used the lemma in like half a dozen later papers. Alas, when I lectured at Barbados, Sasha Razborov and others discovered that my proof of the AAGANL was missing a crucial step! More concretely, the proof I gave there works for pure states but not for mixed states. For mixed states, the trouble is that I take a purification of the mixed state--something that always exists mathematically--but then illegally assume that the measurement I'm analyzing acts on the particular purification I've conjured up.

Fortunately, one can easily fix this problem by decomposing the state ρ into a mixture of pure states, then applying my earlier argument to each pure state separately, and finally using Cauchy-Schwarz (or just the convexity of the square-root function) to recombine the results. Moreover, this is exactly what other people's proofs of the Gentle Measurement Lemma _did_ do, though I'd never noticed it before Barbados--I just idly wondered why those other proofs took twice as long as mine to do the same work! For a correct proof, see Lemma 1.3.1 in the [Barbados lecture notes](http://www.scottaaronson.com/barbados-2016.pdf).

* * *

**IV. Oracle Woes**

In my 2010 paper [BQP and the Polynomial Hierarchy](http://www.scottaaronson.com/papers/bqpph.pdf), I claimed to construct oracles A relative to which BQP⊄BPPpath and BQP⊄SZK, even while making only partial progress toward the big prize, which would've been an oracle relative to which BQP⊄PH. Not only that: I claimed to show that _any_ problem with a property called "almost k-wise independence"--one example being the Forrelation (or Fourier Checking) problem that I introduced in that paper--was neither in BPPpath nor in SZK. But I showed that Forrelation _is_ in BQP, thus yielding the separations.

Alas, this past spring Lijie Chen, who was my superb visiting student from Tsinghua University, realized that my proofs of these particular separations were wrong. Not only that, they were wrong _because I implicitly substituted a ratio of expectations for an expectation of ratios_ (!). Again, it might still be _true_ that almost k-wise independent problems can be neither in BPPpath nor in SZK: that remains an interesting conjecture, which Lijie was unable to resolve one way or the other. (On the other hand, I showed [here](http://www.scottaaronson.com/papers/glnfalse.pdf) that almost k-wise independent problems _can_ be in PH.)

But never fear! In a [recent arXiv preprint](http://arxiv.org/abs/1605.00619), Lijie has supplied correct proofs for the BQP⊄BPPpath and BQP⊄SZK oracle separations--using the same Forrelation problem that I studied, but additional properties of Forrelation besides its almost k-wise independence. Lijie notes that my proofs, had they worked, would also have yielded an oracle relative to which BQP⊄AM, which would've been a spectacular result, nontrivial progress toward BQP⊄PH. His proofs, by contrast, apply only to worst-case decision problems rather than problems of distinguishing two probability distributions, and therefore don't imply anything about BQP vs. AM. Anyway, there's other cool stuff in his paper too.

* * *

**V. We Needed More Coffee**

This is one I've [already written about](https://scottaaronson.blog/?p=1818) on this blog, but just in case anyone missed it … in my, Sean Carroll, and Lauren Ouellette's original [draft paper on the coffee automaton](http://www.scottaaronson.com/papers/coffee2.pdf), the specific rule we discuss _doesn 't_ generate any significant amount of complexity (in the sense of coarse-grained entropy). We wrongly thought it did, because of a misinterpretation of our simulation data. But as Brent Werness brought to our attention, not only does a corrected simulation not show any complexity bump, one can rigorously _prove_ there's no complexity bump. And we could've realized all this from the beginning, by reflecting that pure random diffusion (e.g., what cream does in coffee when you don't stir it with a spoon) _doesn 't_ actually produce interesting tendril patterns.

On the other hand, Brent proposed a different rule--one that involves "shearing" whole regions of cream and coffee across each other--that _does_ generate significant complexity, basically because of all the long-range correlations it induces. And not only do we clearly see this in simulations, but the growth of complexity can be rigorously proven! Anyway, we have a long-delayed revision of the paper that will explain all this in more detail, with Brent as well as MIT student Varun Mohan now added as coauthors.

* * *

If any of my colleagues feel inspired to write up their own "litanies of mathematical error," they're welcome to do so in the comments! Just remember: you don't earn any epistemic virtue points unless the errors you reveal _actually_ embarrass you. No humblebragging about how you once left out a minus sign in your paper that won the Fields Medal.
