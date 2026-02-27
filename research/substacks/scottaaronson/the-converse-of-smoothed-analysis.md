---
title: "The converse of smoothed analysis"
author: "Scott Aaronson"
date: "Wed, 06 Oct 2010"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=469"
---

A year ago, [Timothy Gowers](http://www.dpmms.cam.ac.uk/~wtg10/) posted the following [beautiful question](http://mathoverflow.net/questions/3529/are-there-any-interesting-examples-of-random-np-complete-problems/31618#31618) to [MathOverflow](http://mathoverflow.net/):

> **Are there any interesting examples of random NP-complete problems?**  
>  Here's an example of the kind of thing I mean. Let's consider a random instance of 3-SAT, where you choose enough clauses for the formula to be almost certainly unsatisfiable, but not too many more than that. So now you have a smallish random formula that is unsatisfiable.
> 
> Given that formula, you can then ask, for any subset of its clauses, whether that subset gives you a satisfiable formula. That is a random (because it depends on the original random collection of clauses) problem in NP. It also looks as though it ought to be pretty hard. But proving that it is usually NP-complete also seems to be hard, because you don't have the usual freedom to simulate.
> 
> So my question is whether there are any results known that say that some randomized problem is NP-complete. (One can invent silly artificial examples like having a randomized part that has no effect on the problem -- hence the word "interesting" in the question.)

On skimming this question, my first thought was: "aha, he's obviously groping toward the well-studied notion of [_average-case complexity_](http://arxiv.org/PS_cache/cs/pdf/0606/0606037v2.pdf)! Let me generously enlighten him." But no, it turns out he _wasn 't_ asking about average-case complexity, but about something different and novel. Namely, the _random_ generation of computational problems consisting of exponentially many instances, for which we're then interested in the worst-case instance. When I explained to Gil Kalai what Gowers wanted, Gil amusingly described it as the "converse of smoothed analysis." In [smoothed analysis](http://www.cs.yale.edu/homes/spielman/SmoothedAnalysis/index.html)--one of many contributions for which [Dan Spielman recently won the Nevanlinna Prize](http://cacm.acm.org/news/97802-daniel-spielman-wins-2010-rolf-nevanlinna-prize/fulltext)--we start with a worst-case instance of a problem (such as linear programming), then perturb the instance by adding some random noise. Gowers wants to do the opposite: start from a _random_ instance and then perform a "worst-case perturbation" of it. (The closest existing notions I could think of were trapdoor one-way functions and other primitives in cryptography, which involve the random generation of a computational problem that's then supposed to be hard on average.)

Anyway, I tossed the question onto my stack of "questions that _could_ develop into whole new branches of theoretical computer science, if someone felt like developing them," and pretty much forgot about it. Then, at dinner last night, I posed the question to [Allan Sly](http://research.microsoft.com/en-us/people/allansly/default.aspx), who's visiting MIT to talk about his exciting new FOCS paper [Computational transition at the uniqueness threshold](http://arxiv.org/abs/1005.5584). Within an hour, Allan had emailed me a sketch of an NP-hardness proof for the "random 3SAT" problem that Gowers asked about. I repost Allan's solution here with his kind permission.

> Group the n variables into N=nε groups of size n1-ε, M1,…MN arbitrarily. For each group Mi take all the clauses with all 3 variables in Mi such that it satisfies both the all 1 and the all 0 assignments i.e. clauses that have either 1 or 2 variables negated. I think that just a first moment estimate should show that with high probability the only assignments on Mi that satisfies all of these clauses should be the all 1 assignment or the all 0 assignment - other assignments are just too unlikely. So in taking these clauses we reduce to the case where we have constant values on each of the groups.
> 
> Once you have these clauses you can then treat each group as a new variable and can construct any SAT assignment on these new variables. Because now you only need to find a clause with 1 variable in each Mi, Mj, Mk for each (i,j,k) ∈ [N]3 that has the right negations. With high probability all of them should exist so you should be able to make whatever SAT assignment on the N variables you want.
> 
> My back of the envelope calculation then suggests that as long as you have n1+ε random clauses to begin with then this should be enough.

It's not hard to see that Allan's solution generalizes to 3-COLORING and other constraint satisfaction problems (maybe even _all_ NP-complete CSPs?). In retrospect, of course, the solution is embarrassingly simple, but one could easily generate other problems in the same vein for which proving NP-hardness was as nontrivial as you wanted it to be. Further development of this new branch of theoretical computer science, as well as coming up with a catchy name for it, are left as exercises for the reader.
