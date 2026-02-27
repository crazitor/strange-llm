---
title: "The Generalized Linial-Nisan Conjecture is false"
author: "Scott Aaronson"
date: "Sun, 11 Jul 2010"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=452"
---

In a [post](https://scottaaronson.blog/?p=381) a year and a half ago, I offered a prize of $200 for proving something called the Generalized Linial-Nisan Conjecture, which basically said that almost k-wise independent distributions fool AC0 circuits. (Go over to that post if you want to know what that means and why I cared about it.)

Well, I'm pleased to report that that's a particular $200 I'll never have to pay. I just uploaded a new preprint to ECCC, entitled [A Counterexample to the Generalized Linial-Nisan Conjecture](http://eccc.uni-trier.de/report/2010/109/). (That's the great thing about research: no matter what happens, you get a paper out of it.)

A couple friends commented that it was wise to name the ill-fated conjecture after other people rather than myself. (Then again, who the hell names a conjecture after themselves?)

If you don't feel like [downloading the ECCC preprint](http://eccc.uni-trier.de/report/2010/109/download), but do feel like scrolling down, here's the abstract (with a few links inserted):

> In [earlier work](http://www.scottaaronson.com/papers/bqpph.pdf), we gave an oracle separating the relational versions of BQP and the polynomial hierarchy, and showed that an oracle separating the decision versions would follow from what we called the _Generalized Linial-Nisan (GLN) Conjecture_ : that "almost k-wise independent" distributions are indistinguishable from the uniform distribution by constant-depth circuits. The original Linial-Nisan Conjecture was recently [proved by Braverman](http://www.cs.toronto.edu/~mbraverm/Papers/FoolAC0v7.pdf); we offered a $200 prize for the generalized version. In this paper, we save ourselves $200 by showing that the GLN Conjecture is false, at least for circuits of depth 3 and higher.  
>  As a byproduct, our counterexample also implies that Π2p⊄PNP relative to a random oracle with probability 1. It has been conjectured since the 1980s that PH is infinite relative to a random oracle, but the best previous result was NP≠coNP relative to a random oracle.  
>  Finally, our counterexample implies that the [famous results](http://www.cs.huji.ac.il/~nati/PAPERS/lmn.pdf) of Linial, Mansour, and Nisan, on the structure of AC0 functions, cannot be improved in several interesting respects.

To dispel any confusion, the $200 prize still stands for the original problem that the GLN Conjecture was meant to solve: namely, giving an oracle relative to which BQP is not in PH. As I say in the paper, I remain optimistic about the prospects for solving _that_ problem by a different approach, such as an elegant one [recently proposed](http://www.cs.caltech.edu/~umans/papers/FU10.pdf) by Bill Fefferman and Chris Umans. Also, it's still possible that the GLN Conjecture is true for depth-_two_ AC0 circuits (i.e., DNF formulas). If so, that would imply the existence of an oracle relative to which BQP is not in AM--already a 17-year-old open problem--and net a respectable $100.
