---
title: "A query complexity breakthrough"
author: "Scott Aaronson"
date: "Thu, 18 Jun 2015"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=2325"
---

**Update (June 26):** See [this just-released paper](http://eccc.hpi-web.de/report/2015/107/), which independently obtains a couple of the same results as the Ambainis et al. paper, but in a different way (using the original Göös et al. function, rather than modifications of it).

* * *

Lots of people have accused me of overusing the word "breakthrough" on this blog. So I ask them: what word _should_ I use when a paper comes out that solves not one, not two, but three of the open problems I've cared about most for literally half of my life, since I was 17 years old?

Yesterday morning, Andris Ambainis, Kaspars Balodis, Aleksandrs Belovs, Troy Lee, Miklos Santha, and Juris Smotrovs [posted a preprint to ECCC](http://eccc.hpi-web.de/report/2015/098/) in which they give:

(1) A total Boolean function f with roughly a fourth-power separation between its deterministic and bounded-error quantum query complexities (i.e., with D(f)~Q(f)4). This refutes the conjecture, which people have been making since [Beals et al.'s seminal work](http://arxiv.org/abs/quant-ph/9802049) in 1998, that the biggest possible gap is quadratic.

(2) A total Boolean function f with a quadratic separation between its deterministic and randomized query complexities (with D(f)~R0(f)2). This refutes a conjecture of [Saks and Wigderson](http://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/SW86/SW86.pdf) from 1986, that the best possible gap is R0(f)~D(f)0.753 (from the recursive AND/OR tree), and shows that the known relation D(f)=O(R0(f)2) is close to tight.

(3) The first total Boolean function f with _any_ asymptotic gap between its zero-error and bounded-error randomized query complexities (in particular, with R0(f)~R(f)3/2).

(There are also other new separations--for example, involving exact quantum query complexity and approximate degree as a real polynomial. But the above three are the most spectacular to me.)

In updates to this post (coming soon), I'll try my best to explain to general readers what D(f), R(f), and so forth _are_ ([see here](http://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf) for the classic survey of these measures), and I'll also discuss how Ambainis et al. designed the strange functions f that achieve the separations (though their paper already does a good job of explaining it). For now, I'll just write the stuff that's easier to write.

I'm at the [Federated Computing Research Conference](http://fcrc.acm.org/) in Portland, Oregon right now, where yesterday I gave my STOC talk ([click here](http://www.scottaaronson.com/talks/forrelation2.pptx) for the PowerPoint slides) about the largest possible separations between R(f) and Q(f) for _partial_ Boolean functions f. ([That paper](http://www.scottaaronson.com/papers/for.pdf) is _also_ joint work with Andris Ambainis, who has his fingers in many pies, or his queries in many oracles, or something.) Anyway, when I did a practice run of my talk on Monday night, I commented that, of course, for _total_ Boolean functions f (those not involving a promise), the largest known gap between R(f) and Q(f) is quadratic, and is achieved when f is the OR function because of Grover's algorithm.

Then, Tuesday morning, an hour before I was to give my talk, I saw the Ambainis et al. bombshell, which made that comment obsolete. So, being notoriously bad at keeping my mouth shut, I mentioned to my audience that, while it was great that they came all the way to Portland to learn what was new in theoretical computer science, if they wanted _real_ news in the subfield I was talking about, they could stop listening to me and check their laptops.

(Having said that, I _have_ had a wonderful time at FCRC, and have learned lots of other interesting things--I can do another addendum to the post about FCRC highlights if people want me to.)

Anyway, within the tiny world of query complexity--i.e., the world where I cut my teeth and spent much of my career--the Ambainis et al. paper is sufficiently revolutionary that I feel the need to say what it _doesn 't_ do.

First, the paper does not give a better-than-quadratic gap between R(f) and Q(f) (i.e., between bounded-error randomized and quantum query complexities). The quantum algorithms that compute their functions f are still "just" variants of the old standbys, Grover's algorithm and amplitude amplification. What's new is that the authors have found functions where you can get the quadratic, Grover speedup between R(f) and Q(f), while _also_ getting asymptotic gaps between D(f) and R(f), and between R0(f) and R(f). So, putting it together, you get superquadratic gaps between D(f) and Q(f), and between R0(f) and Q(f). But it remains at least a plausible conjecture that R(f)=O(Q(f)2) for all total Boolean functions f--i.e., if you insist on a "fair comparison," then the largest known quantum speedup for total Boolean functions remains the Grover one.

Second, as far as I can tell ~~(I might be mistaken)~~ (I'm not), the paper doesn't give new separations involving certificate complexity or block sensitivity (e.g., between D(f) and bs(f)). So for example, it remains open whether D(f)=O(bs(f)2), and ~~whether C(f)=O(bs(f) α) for some α<2.~~ (Update: Avishay Tal, in the comments, informs me that the latter conjecture was falsified by [Gilmer, Saks, and Srinivasan](http://arxiv.org/abs/1306.0630) in 2013. Wow, I'm _really_ out of it!)

In the end, achieving these separations didn't require any sophisticated new mathematical machinery--just finding the right functions, something that could've been done back in 1998, had anyone been clever enough. So, where did these bizarre functions f come from? Ambainis et al. directly adapted them from a great [recent communication complexity paper](http://eccc.hpi-web.de/report/2015/050/) by Mika Göös, Toniann Pitassi, and Thomas Watson. But the Göös et al. paper itself could've been written much earlier. It's yet another example of something I've seen again and again in this business, how there's no substitute for just playing around with a bunch of examples.

The highest compliment one researcher can pay another is, "I wish I'd found that myself." And I do, of course, but having missed it, I'm thrilled that at least I get to be alive for it and blog about it. Huge congratulations to the authors!

* * *

**Addendum: What 's this about?**

OK, so let's say you have a Boolean function f:{0,1}n→{0,1}, mapping n input bits to 1 output bit. Some examples are the OR function, which outputs 1 if any of the n input bits are 1, and the MAJORITY function, which outputs 1 if the majority of them are.

_Query complexity_ is the study of how many input bits you need to read in order to learn the value of the output bit. So for example, in evaluating the OR function, if you found a single input bit that was 1, you could stop right there: you'd know that the output was 1, without even needing to look at the remaining bits. In the worst case, however, if the input consisted of all 0s, you'd have to look at all of them before you could be totally sure the output was 0. So we say that the OR function has a deterministic query complexity of n.

In this game, we don't care about any other resources used by an algorithm, like memory or running time: just how many bits of the input it looks at! There are many reasons why, but the simplest is that, unlike with memory or running time, for many functions _we can actually figure out_ how many input bits need to be looked at, without needing to solve anything like P vs. NP. (But note that this can already be nontrivial! For algorithms can often cleverly avoid looking at all the bits, for example by looking at some and then deciding which ones to look at next based on which values they see.)

In general, given a deterministic algorithm A and an n-bit input string x, let DA,x (an integer from 0 to n) be the number of bits of x that A examines when you run it. Then let DA be the maximum of DA,x over all n-bit strings x. Then D(f), or the deterministic query complexity of f, is the minimum of DA, over all algorithms A that correctly evaluate f(x) on every input x.

For example, D(OR) and D(MAJORITY) are both n: in the worst case, you need to read everything. For a more interesting example, consider the 3-bit Boolean function

f(x,y,z) = (not(x) and y) or (x and z).

This function has D(f)=2, even though it depends on all 3 of the input bits. (Do you see why?) In general, even if f depends on n input bits, D(f) could be as small as log2n.

The _bounded-error randomized query complexity_ , or R(f), is like D(f), except that now we allow the algorithm to make random choices of which input bit to query, and for each input x, the algorithm only needs to compute f(x) with probability 2/3. (Here the choice of 2/3 is arbitrary; if you wanted the right answer with some larger constant probability, say 99.9%, you could just repeat the algorithm a constant number of times and take a majority vote.) The _zero-error randomized query complexity_ , or R0(f), is the variant where the algorithm is allowed to make random choices, but at the end of the day, needs to output the correct f(x) with probability 1.

To illustrate these concepts, consider the three-bit majority function, MAJ(x,y,z). We have D(MAJ)=3, since if a deterministic algorithm queried one bit and got a 0 and queried a second bit and got a 1 (as can happen), it would have no choice but to query the third bit. But for any possible setting of x, y, and z, if we choose which bits to query _randomly_ , there's at least a 1/3 chance that the first two queries will return either two 0s or two 1s--at which point we can stop, with no need to query the third bit. Hence R0(MAJ)≤(1/3)2+(2/3)3=8/3 (in fact it equals 8/3, although we haven't quite shown that). Meanwhile, R(MAJ), as we defined it, is only 1, since if you just need a 2/3 probability of being correct, you can simply pick x, y, or z at random and output it!

The _bounded-error quantum query complexity_ , or Q(f), is the minimum number of queries made by a quantum algorithm for f, which, again, has to output the right answer with probability at least 2/3 for every input x. Here a quantum algorithm makes a "query" by feeding a superposition of basis states, each of the form |i,a,w〉, to a "black box," which maps each basis state to |i, a XOR xi, w〉, where i is the index of the input bit xi to be queried, a is a 1-qubit "answer register" into which xi is reversibly written, and w is a "workspace" that doesn't participate in the query. In between two queries, the algorithm can apply any unitary transformation it wants to the superposition of |i,a,w〉's, as long as it doesn't depend on x. Finally, some designated qubit is measured to decide whether the algorithm accepts or rejects.

As an example, consider the 2-bit XOR function, XOR(x,y). We have D(XOR)=R0(XOR)=R(XOR)=2, since until you've queried both bits, you've learned nothing about their XOR. By contrast, Q(XOR)=1, because of the famous [Deutsch-Jozsa algorithm](https://en.wikipedia.org/wiki/Deutsch%E2%80%93Jozsa_algorithm).

It's clear that

0 ≤ Q(f) ≤ R(f) ≤ R0(f) ≤ D(f) ≤ n,

since a quantum algorithm can simulate a randomized one and a randomized one can simulate a deterministic one.

A central question for the field, since these measures were studied in the 1980s or so, has been how far apart these measures can get from each other. If you allow _partial_ Boolean functions--meaning that only some n-bit strings, not all of them, are "valid inputs" for which the algorithm needs to return a definite answer--then it's easy to get _enormous_ separations between any two of the measures (indeed, even bigger than exponential), as for example in my [recent paper with Andris](http://www.scottaaronson.com/papers/for.pdf).

For total functions, by contrast, it's been known for a long time that these measures can differ by at most polynomial factors:

D(f) = O(R(f)3) (Nisan)

D(f) = O(R0(f)2) (folklore, I think)

R0(f) = O(R2 log(n)) (Midrijanis)

D(f) = O(Q(f)6) (Beals et al. 1998)

OK, so what were the largest known gaps? For D versus R0 (as well as D versus R), the largest known gap since 1986 has come from the "recursive AND/OR tree": that is, an OR of two ANDs of two ORs of two ANDs of … forming a complete binary tree of depth d, with the n=2d input variables comprising the leaves. For this function, we have D(f)=n, whereas [Saks and Wigderson](http://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/SW86/SW86.pdf) showed that R0(f)=Θ(n0.753) (and later, [Santha](http://www.liafa.univ-paris-diderot.fr/~santha/Papers/s95.ps.gz) showed that R(f)=Θ(n0.753) as well).

For D versus Q, the largest gap has been for the OR function: we have D(OR)=n (as mentioned earlier), but Q(OR)=Θ(√n) because of Grover's algorithm. Finally, for R0 versus R, _no_ asymptotic gap has been known for any total function. (This is a problem that I clearly remember working on back in 2000, when I was an undergrad. I even wrote a computer program, the [Boolean Function Wizard](http://www.scottaaronson.com/bfw/), partly to search for separations between R0 versus R. Alas, while I _did_ find one or two functions with separations, I was unable to conclude anything from them about asymptotics.)

So, how did Ambainis et al. achieve bigger gaps for each of these? I'll _try_ to have an explanation written by the time my flight from Portland to Boston has landed tonight. But if you can't wait for that, or you prefer it straight from the horse's mouth, [read their paper!](http://eccc.hpi-web.de/report/2015/098/)

* * *

**Addendum 2: The Actual Functions**

As I mentioned before, the starting point for everything Ambainis et al. do is a certain Boolean function g recently constructed by Göös, Pitassi, and Watson (henceforth GPW), for different purposes than the ones that concern Ambainis et al. We think of the inputs to g as divided into nm "cells," which are arranged in a rectangular grid with m columns and n rows. Each cell contains a bit that's either 0 or 1 (its "label), as well as a pointer to another cell (consisting of ~log2(nm) bits). The pointer can also be "null" (i.e., can point nowhere). We'll imagine that a query of a cell gives you everything: the label _and_ all the bits of the pointer. This could increase the query complexity of an algorithm, but only by a log(n) factor, which we won't worry about.

Let X be a setting of all the labels and pointers in the grid. Then the question we ask about X is the following:

Does there exist a "marked column": that is, a column where all n of the labels are 1, and which has exactly one non-null pointer, which begins a chain of pointers of length m-1, which visits exactly one "0" cell in each column other than the marked column, and then terminates at a null pointer?


If such a marked column exists, then we set g(X)=1; otherwise we set g(X)=0. Crucially, notice that if a marked column exists, then it's _unique_ , since the chain of pointers "zeroes out" all m-1 of the other columns, and prevents them from being marked.

This g _already_ leads to a new query complexity separation, one that refutes a strengthened form of the Saks-Wigderson conjecture. For it's not hard to see that D(g)=Ω(mn): indeed, any deterministic algorithm must query almost all of the cells. A variant of this is proved in the paper, but the basic idea is that an adversary can answer all queries with giant fields of '1' labels and null pointers--_until_ a given column is almost completed, at which point the adversary fills in the last cell with a '0' label and a pointer to the _last_ '0' cell that it filled in. The algorithm just can't catch a break; it will need to fill in m-1 columns before it knows where the marked one is (if a marked column exists at all).

By contrast, it's possible to show that, if n=m, then R(g) is about O(n4/3). I had an argument for R(g)=O((n+m)log(m)) in an earlier version of this post, but the argument was wrong; I thank Alexander Belov for catching the error. I'll post the R(g)=O(n4/3) argument once I understand it.

To get the other separations--for example, total Boolean functions for which D~R02, D~Q4, R0~Q3, R0~R3/2, and R~approxdeg4--Ambainis et al. need to add various "enhancements" to the basic GPW function g defined above. There are three enhancements, which can either be added individually or combined, depending on one's needs.

1\. Instead of just a single marked column, we can define g(X) to be 1 if and only if there are k marked columns, which point to each other in a cycle, and which _also_ point to a trail of m-k '0' cells, showing that none of the other columns contain all '1' cells. This can help a bounded-error randomized algorithm--which can quickly find one of the all-1 columns using random sampling--while not much helping a zero-error randomized algorithm.

2\. Instead of a linear _chain_ of pointers showing that all the non-marked columns contain a '0' cell, for g(X) to be 1 we can demand a complete _binary tree_ of pointers, originating at a marked column and fanning out to all the unmarked columns in only log(m) layers. This can substantially help a quantum algorithm, which can't follow a pointer trail any faster than a classical algorithm can; but which, given a complete binary tree, can "fan out" and run Grover's algorithm on all the leaves in only the square root of the number of queries that would be needed classically. Meanwhile, however, putting the pointers in a tree doesn't much help deterministic or randomized algorithms.

3\. In addition to pointers "fanning out" from a marked column to all of the unmarked columns, we can demand that in every unmarked column, some '0' cell contains a _back-pointer_ , which leads back to a marked column. These back-pointers can help a randomized or quantum algorithm find a marked column faster, while not much helping a deterministic algorithm.

Unless I'm mistaken, the situation is this:

With no enhancements, you can get D~R2 and something like D~R03/2 (~~although I still don 't understand how you get the latter with no enhancements; the paper mentions it without proof~~ [Andris has kindly supplied a proof here](https://scottaaronson.blog/?p=2325#comment-676218)).

With only the cycle enhancement, you can get R0~R3/2.

With only the binary tree enhancement, you can get R~approxdeg4.

With only the back-pointer enhancement, you can get D~R02.

With the cycle enhancement _and_ the binary-tree enhancement, you can get R0~Q3.

With the back-pointer enhancement _and_ the binary-tree enhancement, you can get D~Q4.

It's an interesting question whether there are separations that require both the cycle enhancement and the back-pointer enhancement; Ambainis et al. don't give any examples.

And here's _another_ interesting question not mentioned in the paper. Using the binary-tree enhancement, Ambainis et al. achieve a fourth-power separation between bounded-error randomized query complexity and approximate degree as a real polynomial--i.e., quadratically better than any separation that was known before. Their proof of this involves cleverly constructing a low-degree polynomial by _summing_ a bunch of low-degree polynomials derived from quantum algorithms (one for each possible marked row). As a result, their final, summed polynomial does _not_ itself correspond to a quantum algorithm, meaning that they don't get a fourth-power separation between R and Q (which would've been even more spectacular than what they do get). On the other hand, purely from the existence of a function with R~approxdeg4, we can deduce that that function has _either_

(i) a super-quadratic gap between R and Q (refuting my conjecture that the Grover speedup is the best possible quantum speedup for total Boolean functions), or  
(ii) a quadratic gap between quantum query complexity and approximate degree--substantially improving over the gap [found by Ambainis](http://arxiv.org/abs/quant-ph/0305028) in 2003.

I conjecture that the truth is (ii); it would be great to have a proof or disproof of this.
