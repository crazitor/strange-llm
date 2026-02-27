---
title: "Deoxyribononapproximability"
author: "Scott Aaronson"
date: "Sun, 04 Nov 2007"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=287"
---

[[Updates]](https://scottaaronson.blog/#114)

Alright, here's a problem for all you bioinformatistas and inapproximabistas out there, which was inspired by [this post of Eliezer Yudkowsky](http://www.overcomingbias.com/2007/11/natural-selecti.html) at [Overcoming Bias](http://www.overcomingbias.com) (see also the comments there).

Let a DNA sequence be an element of {A,C,G,T}*, and suppose we're allowed the following primitive operations: (1) insert a base pair anywhere we want, (2) delete any substring, (3) reverse any substring, and (4) copy any substring into any other part of the string. Then given a DNA sequence S, how hard is it to estimate the minimum number of operations needed to produce S starting from the empty string?

Closely related is the following problem: by starting from the empty string and applying o(n) operations, can we produce a "pseudorandom DNA sequence" of length n -- that is, a sequence that can't be distinguished in polynomial time from a uniform random one?

(_Note 1:_ For both problems, we might also want to stipulate that every intermediate sequence should have size at most polynomial in n. Or better yet, maybe one can prove that such an assumption is without loss of generality.)

(_Note 2:_ I'm also very interested in what happens if we disallow the powerful operation of reversal.)

For all I know, these problems might have trivial (or at any rate, known) answers; I just came up with them and haven't thought them through.

What the problems are _really_ getting at is this: is the "effective number of bits" in your genome (that is, the number of bits from a polynomial-time algorithm's perspective) limited by how many ancestors you've had since life on Earth began? Or can it be vastly greater?

**Update (11/4):** Rereading the last few paragraphs of Eliezer's post, I see that he actually argues for his central claim -- that the human genome can't contain more than 25MB of "meaningful DNA" -- on different (and much stronger) grounds than I thought! My apologies for not reading more carefully.

In particular, the argument has nothing to do with the number of generations since the dawn of time, and instead deals with the maximum number of DNA bases that can be simultaneously protected, _in steady state_ , against copying errors. According to Eliezer, copying a DNA sequence involves a ~10-8 probability of error per base pair, which -- because only O(1) errors per generation can be corrected by natural selection -- yields an upper bound of ~108 on the number of "meaningful" base pairs in any given genome.

However, while this argument is much better than my straw-man based on the number of generations, there's still an interesting loophole. Even with a 10-8 chance of copying errors, one could imagine a genome reliably encoding far more than 108 bits (in fact, arbitrarily many bits) by using an error-correcting code. I'm not talking about the "local" error-correction mechanisms that we know DNA has, but about something more global -- by which, say, copying errors in any small set of genes could be completely compensated by other genes. The interesting question is whether natural selection could read the syndrome of such a code, and then correct it, using O(1) randomly-chosen insertions, deletions, transpositions, and reversals. I admit that this seems unlikely, and that even if it's possible in principle, it's probably irrelevant to real biology. For apparently there are examples where changing even a single base pair leads to horrible mutations. And on top of that, we can't have the error-correcting code be _too_ good, since otherwise we'll suppress beneficial mutations!

Incidentally, Eliezer's argument makes the falsifiable prediction that we shouldn't find _any_ organism, _anywhere_ in nature, with more than 25MB of functional DNA. Does anyone know of a candidate counterexample? (I know there are organisms with far more than humans' 3 billion base pairs, but I have no idea how many of the base pairs are functional.)

Lastly, in spite of everything above, I'd still like a solution to my "pseudorandom DNA sequence" problem. For _if_ the answer were negative -- if given any DNA sequence, one could efficiently reconstruct a nearly-optimal sequence of insertions, transpositions, etc. producing it -- then even my original straw-man misconstrual of Eliezer's argument could put up a decent fight!

**Update (11/5):** Piotr Indyk pointed me to a [paper](http://www.cs.sfu.ca/~funda/PUBLICATIONS/fsttcs.ps) by Ergün, Muthukrishnan, and Sahinalp from FSTTCS'2003, which basically solves my problem in the special case of no reversals. It turns out that you can estimate the number of insert, delete, and copy operations needed to produce a given DNA sequence to within a factor of 4, by just applying Lempel-Ziv compression to the sequence. Thanks, Piotr!

**Another Update (11/5):** Andy Drucker has pointed out that, in the case where reversals _are_ allowed, we can approximate the number of insert, delete, copy, and reverse operations needed to produce a given DNA sequence to within a factor of 16, by combining the Lempel-Ziv approach of Ergün et al. with a clever trick: maintain both the sequence and its reversal at all times! Interestingly, though, this trick _doesn 't_ seem to work for transforming one sequence into another (a more general problem than I asked about, and the one considered by Ergün et al).
