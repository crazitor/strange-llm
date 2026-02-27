---
title: "Yet more mistakes in papers"
author: "Scott Aaronson"
date: "Tue, 10 Aug 2021"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=5706"
---

**Amazing Update (Aug. 19):** My former PhD student Daniel Grier tells me that he, Sergey Bravyi, and David Gosset have an [arXiv preprint](https://arxiv.org/pdf/2102.06963.pdf), from February, where they give a corrected proof of my and Andris Ambainis's claim that any k-query quantum algorithm can be simulated by an O (N1-1/2k)-query classical randomized algorithm (albeit, not of our stronger statement, about a randomized algorithm to estimate any bounded low-degree real polynomial). The reason I hadn't known about this is that they don't mention it in the abstract of their paper (!!). But it's right there in Theorem 5.

* * *

In my [last post](https://scottaaronson.blog/?p=5675), I came down pretty hard on the blankfaces: people who relish their power to persist in easily-correctable errors, to the detriment of those subject to their authority. The sad truth, though, is that _I_ don't obviously do better than your average blankface in my ability to resist falsehoods on early encounter with them. As one of many examples that readers of this blog might know, I didn't think covid seemed like a big deal in early February 2020--although by mid-to-late February 2020, I'd repented of my doofosity. If I have _any_ tool with which to unblank my face, then it's only my extreme self-consciousness when confronted with evidence of my own stupidities--the way I've trained myself over decades in science to see error-correction as a or even _the_ fundamental virtue.

Which brings me to today's post. Continuing what's become a _Shtetl-Optimized_ tradition--see [here from 2014](https://scottaaronson.blog/?p=2072), [here from 2016](https://scottaaronson.blog/?p=2854), [here from 2017](https://scottaaronson.blog/?p=3256)--I'm going to fess up to two serious mistakes in research papers on which I was a coauthor.

* * *

In 2015, Andris Ambainis and I had a STOC paper entitled [Forrelation: A Problem that Optimally Separates Quantum from Classical Computing](https://arxiv.org/abs/1411.5729). We gave two main results there:

  1. A Ω((√N)/log(N)) lower bound on the randomized query complexity of my "Forrelation" problem, which was known to be solvable with only a single quantum query.
  2. A proposed way to take any k-query quantum algorithm that queries an N-bit string, and simulate it using only O(N1-1/2k) classical randomized queries.



Later, [Bansal and Sinha](https://arxiv.org/abs/2008.07003) and independently [Sherstov, Storozhenko, and Wu](https://arxiv.org/abs/2008.10223) showed that a k-query generalization of Forrelation, which I'd also defined, requires ~Ω(N1-1/2k) classical randomized queries, in line with my and Andris's conjecture that k-fold Forrelation _optimally_ separates quantum and classical query complexities.

A couple months ago, alas, my former grad school officemate [Andrej Bogdanov](https://www.cse.cuhk.edu.hk/~andrejb/), along with Tsun Ming Cheung and Krishnamoorthy Dinesh, emailed me and Andris to say that they'd discovered an error in result 2 of our paper (result 1, along with the Bansal-Sinha and Sherstov-Storozhenko-Wu extensions of it, remained fine). So, adding our own names, we've now posted a [preprint on ECCC](https://eccc.weizmann.ac.il/report/2021/115/) that explains the error, while also showing how to recover our result for the special case k=1: that is, any 1-query quantum algorithm really can be simulated using only O(√N) classical randomized queries.

Read the preprint if you really want to know the details of the error, but to summarize it in my words: Andris and I used a trick that we called "variable-splitting" to handle variables that have way more influence than average on the algorithm's acceptance probability. Alas, variable-splitting fails to take care of a situation where there are a bunch of variables that are non-influential individually, but that on some unusual input string, can "conspire" in such a way that their signs all line up and their contribution overwhelms those from the other variables. A single mistaken inequality fooled us into thinking such cases were handled, but an explicit counterexample makes the issue obvious.

I _still_ conjecture that my original guess was right: that is, I conjecture that any problem solvable with k quantum queries is solvable with O(N1-1/2k) classical randomized queries, so that k-fold Forrelation is the extremal example, and so that no problem has constant quantum query complexity but linear randomized query complexity. More strongly, I reiterate the conjecture that any bounded degree-d real polynomial, p:{0,1}N→[0,1], can be approximated by querying only O(N1-1/d) input bits drawn from some suitable distribution. But proving these conjectures, if they're true, will require a new algorithmic idea.

* * *

Now for the second _mea culpa_. Earlier this year, my student Sabee Grewal and I posted a short preprint on the arXiv entitled [Efficient Learning of Non-Interacting Fermion Distributions](https://arxiv.org/abs/2102.10458). In it, we claimed to give a classical algorithm for reconstructing any "free fermionic state" |ψ⟩--that is, a state of n identical fermionic particles, like electrons, each occupying one of m>n possible modes, that can be produced using only "fermionic beamsplitters" and no interaction terms--and for doing so in polynomial time and using a polynomial number of samples (i.e., measurements of where all the fermions are, given a copy of |ψ⟩). Alas, after trying to reply to confused comments from readers and reviewers (albeit, none of them _exactly_ putting their finger on the problem), Sabee and I were able to figure out that we'd done no such thing.

Let me explain the error, since it's actually really interesting. In our underlying problem, we're trying to find a collection of unit vectors, call them |v1⟩,…,|vm⟩, in Cn. Here, again, n is the number of fermions and m>n is the number of modes. By measuring the "2-mode correlations" (i.e., the probability of finding a fermion in both mode i and mode j), we can figure out the approximate value of |⟨vi|vj⟩|--i.e., the absolute value of the inner product--for any i≠j. From that information, we want to recover |v1⟩,…,|vm⟩ themselves--or rather, their relative configuration in n-dimensional space, isometries being irrelevant.

It seemed to me and Sabee that, if we knew ⟨vi|vj⟩ for all i≠j, then we'd get linear equations that iteratively constrained each |vj⟩ in terms of ⟨vi|vj⟩ for j<i, so all we'd need to do is solve those linear systems, and then (crucially, and this was the main work we did) show that the solution would be _robust_ with respect to small errors in our estimates of each ⟨vi|vj⟩. It seemed further to us that, while it was true that the measurements only revealed |⟨vi|vj⟩| rather than ⟨vi|vj⟩ itself, the "phase information" in ⟨vi|vj⟩ was manifestly irrelevant, as it in any case depended on the irrelevant global phases of |vi⟩ and |vj⟩ themselves.

Alas, it turns out that the phase information _does_ matter. As an example, suppose I told you only the following about three unit vectors |u⟩,|v⟩,|w⟩ in R3:

|⟨u|v⟩| = |⟨u|w⟩| = |⟨v|w⟩| = 1/2.

Have I thereby determined these vectors up to isometry? Nope! In one class of solution, all three vectors belong to the same plane, like so:

|u⟩=(1,0,0),  
|v⟩=(1/2,(√3)/2,0),  
|w⟩=(-1/2,(√3)/2,0).

In a completely different class of solution, the three vectors _don 't_ belong to the same plane, and instead look like three edges of a tetrahedron meeting at a vertex:

|u⟩=(1,0,0),  
|v⟩=(1/2,(√3)/2,0),  
|w⟩=(1/2,1/(2√3),√(2/3)).

These solutions correspond to different sign choices for |⟨u|v⟩|, |⟨u|w⟩|, and |⟨v|w⟩|--choices that _collectively_ matter, even though each of them is individually irrelevant.

It follows that, even in the special case where the vectors are all real, the 2-mode correlations are _not_ enough information to determine the vectors' relative positions. (Well, it takes some more work to convert this to a counterexample that could actually arise in the fermion problem, but that work can be done.) And alas, the situation gets even gnarlier when, as for us, the vectors can be complex.

Any possible algorithm for our problem will have to solve a system of _non_ linear equations (albeit, a massively overconstrained system that's guaranteed to have a solution), and it will have to use _3-mode_ correlations (i.e., statistics of _triples_ of fermions), and quite possibly 4-mode correlations and above.

But now comes the good news! Googling revealed that, for reasons having nothing to do with fermions or quantum physics, problems _extremely_ close to ours had already been studied in classical machine learning. The key term here is ["Determinantal Point Processes"](https://en.wikipedia.org/wiki/Determinantal_point_process) (DPPs). A DPP is a model where you specify an m×m matrix A (typically symmetric or Hermitian), and then the probabilities of various events are given by the determinants of various principal minors of A. Which is _precisely_ what happens with fermions! In terms of the vectors |v1⟩,…,|vm⟩ that I was talking about before, to make this connection we simply let A be the m×m _covariance matrix_ , whose (i,j) entry equals ⟨vi|vj⟩.

I first learned of this remarkable correspondence between fermions and DPPs a decade ago, from a talk on DPPs that [Ben Taskar](https://www.cs.washington.edu/people/faculty/taskar) gave at MIT. Immediately after the talk, I made a mental note that Taskar was a rising star in theoretical machine learning, and that his work would probably be relevant to me in the future. While researching this summer, I was devastated to learn that Taskar died of heart failure in 2013, in his mid-30s and only a couple of years after I'd heard him speak.

The most relevant paper for me and Sabee was called [An Efficient Algorithm for the Symmetric Principal Minor Assignment Problem](https://www.alexkulesza.com/pubs/spmap_laa14.pdf), by Rising, Kulesza, and Taskar. Using a combinatorial algorithm based on minimum spanning trees and chordless cycles, this paper _nearly_ solves our problem, except for two minor details:

  1. It doesn't do an error analysis, and
  2. It considers complex _symmetric_ matrices, whereas our matrix A is [Hermitian](https://en.wikipedia.org/wiki/Hermitian_matrix) (i.e., it equals its _conjugate_ transpose, not its transpose).



So I decided to email [Alex Kulezsa](https://www.alexkulesza.com/), one of Taskar's surviving collaborators who's now a research scientist at Google NYC, to ask his thoughts about the Hermitian case. Alex kindly replied that they'd been meaning to study that case--a reviewer had even asked about it!--but they'd ran into difficulties and didn't know what it was good for. I asked Alex whether he'd like to join forces with me and Sabee in tackling the Hermitian case, which (I told him) was enormously relevant in quantum physics. To my surprise and delight, Alex agreed.

So we've been working on the problem together, making progress, and I'm optimistic that we'll have _some_ nice result. By using the 3-mode correlations, at least "generically" we can recover the entries of the matrix A _up to complex conjugation_ , but further ideas will be needed to resolve the complex conjugation ambiguity, to whatever extent it actually matters.

In short: on the negative side, there's much more to the problem of learning a fermionic state than we'd realized. But on the positive side, there's much more to the problem than we'd realized! As with the simulation of k-query quantum algorithms, my coauthors and I would welcome any ideas. And I apologize to anyone who was misled by our premature (and hereby retracted) claims.

* * *

**Update (Aug. 11):** Here's a third bonus retraction, which I thank my colleague [Mark Wilde](https://www.markwilde.com/) for bringing to my attention. Way back in 2005, in my [NP-complete Problems and Physical Reality](https://arxiv.org/abs/quant-ph/0502072) survey article, I "left it as an exercise for the reader" to prove that BQPCTC, or quantum polynomial time augmented with Deutschian closed timelike curves, is contained in a complexity class called SQG (Short Quantum Games). While it turns out to be _true_ that BQPCTC ⊆ SQG--as follows from [my and Watrous's 2008 result](https://arxiv.org/abs/0808.2669) that BQPCTC = PSPACE, combined with [Gutoski and Wu's 2010 result](https://arxiv.org/abs/1011.2787) that SQG = PSPACE--it's not something for which I could possibly have had a correct proof back in 2005. I.e., it was a harder exercise than I'd intended!
