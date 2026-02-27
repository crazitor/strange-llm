---
title: "Ten Signs a Claimed Mathematical Breakthrough is Wrong"
author: "Scott Aaronson"
date: "Sat, 05 Jan 2008"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=304"
---

Yesterday several people asked my opinion of a [preprint](http://arxiv.org/abs/0801.0398) claiming to solve the Graph Isomorphism problem in deterministic polynomial time. I responded:

> If I read all such papers, then I wouldn’t have time for anything else. It’s an interesting question how you decide whether a given paper crosses the plausibility threshold or not. For me personally, the AKS [“PRIMES in P”](http://www.math.princeton.edu/~annals/issues/2004/Sept2004/Agrawal.pdf) paper somehow crossed it whereas this one somehow doesn’t.
> 
> Of course, I’d welcome an opinion from anyone who’s actually read the paper.

Three commenters wrote in to say the paper looked good. Then the author found a bug and retracted it.

**Update (1/5):** Laci Babai writes in to tell me that's not quite what happened. See [here](http://people.cs.uchicago.edu/~laci/polytope-correspondence.pdf) for what _did_ happen, and [here](http://people.cs.uchicago.edu/~laci/polytope.pdf) for an argument that Friedland's approach would if sound have implied P=NP.

My purpose here is not to heap embarrassment on the author: he's a serious mathematician who had a well-defined and interesting approach, and who (most importantly) retracted his claim as soon as a bug was discovered. (Would that everyone did the same!) Though the stakes are usually smaller, similar things have happened to most of us, including me.

Instead I want to explore the following metaquestion: _suppose someone sends you a complicated solution to a famous decades-old math problem, like P vs. NP. How can you decide, in ten minutes or less, whether the solution is worth reading?_

For a blogger like me -- whose opinions are both expected immediately and googlable indefinitely -- this question actually matters. Err in one direction, and I'll forever be known as the hidebound reactionary who failed to recognize some 21st-century Ramanujan. Err in the other direction, and I'll spend my whole life proofreading the work of crackpots.

A few will chime in: "but if everyone wrote out their proofs in computer-checkable form, there'd be no need for this absurd dilemma!" Sure, and if everyone buckled up there'd be fewer serious accidents. Yet here's the bloodied patient, and here we are in the emergency room.

In deciding whether to spend time on a paper, obviously the identity of the authors plays some role. If Razborov says he proved a superlinear circuit lower bound for SAT, the claim on our attention is different than if Roofus McLoofus says the same thing. But the danger of elitism is obvious here -- so in this post, I'll only be interested in what can be inferred from the text itself.

Inspired by Sean Carroll's closely-related [Alternative-Science Respectability Checklist](https://www.preposterousuniverse.com/blog/2007/06/19/the-alternative-science-respectability-checklist/), without further ado I now offer the _Ten Signs a Claimed Mathematical Breakthrough is Wrong_.

**1\. The authors don 't use TeX.** This simple test (suggested by Dave Bacon) already catches at least 60% of wrong mathematical breakthroughs. David Deutsch and Lov Grover are among the only known false positives.

**2\. The authors don 't understand the question.** Maybe they mistake NP≠coNP for some claim about psychology or metaphysics. Or maybe they solve the Grover problem in O(1) queries, under some notion of quantum computing lifted from a magazine article. I've seen both.

**3\. The approach seems to yield something much stronger and maybe even false (but the authors never discuss that).** They've proved 3SAT takes exponential time; their argument would go through just as well for 2SAT.

**4\. The approach conflicts with a known impossibility result (which the authors never mention).** The four months I spent proving the [collision lower bound](http://www.scottaaronson.com/papers/collision.pdf) actually saved me some time once or twice, when I was able to reject papers violating the bound without reading them.

**5\. The authors themselves switch to weasel words by the end.** The abstract says "we show the problem is in P," but the conclusion contains phrases like "seems to work" and "in all cases we have tried." Personally, I happen to be a big fan of heuristic algorithms, honestly advertised and experimentally analyzed. But when a "proof" has turned into a "plausibility argument" by page 47 -- _release the hounds!_

**6\. The paper jumps into technicalities without presenting a new idea.** If a famous problem could be solved only by manipulating formulas and applying standard reductions, then it's overwhelmingly likely someone would've solved it already. The exceptions to this rule are interesting precisely because they're rare (and even with the exceptions, a new idea is usually needed to _find_ the right manipulations in the first place).

**7\. The paper doesn 't build on (or in some cases even refer to) any previous work.** Math is cumulative. Even Wiles and Perelman had to stand on the lemma-encrusted shoulders of giants.

**8\. The paper wastes lots of space on standard material.** If you'd really proved P≠NP, then you wouldn't start your paper by laboriously defining 3SAT, in a manner suggesting your readers might not have heard of it.

**9\. The paper waxes poetic about "practical consequences," "deep philosophical implications," etc.** Note that most papers make exactly the opposite mistake: they never get around to explaining why anyone should read them. But when it comes to something like P≠NP, to "motivate" your result is to insult your readers' intelligence.

**10\. The techniques just seem too wimpy for the problem at hand.** Of all ten tests, this is the slipperiest and hardest to apply -- but also the decisive one in many cases. As an analogy, suppose your friend in Boston blindfolded you, drove you around for twenty minutes, then took the blindfold off and claimed you were now in Beijing. Yes, you do see Chinese signs and pagoda roofs, and no, you can't immediately disprove him -- but based on your knowledge of both cars and geography, isn't it more likely you're just in Chinatown? I know it's trite, but this is exactly how I feel when I see (for example) a paper that uses category theory to prove NL≠NP. We start in Boston, we end up in Beijing, and at no point is anything resembling an ocean ever crossed.

Obviously, these are just some heuristics I've found successful in the past. (The nice thing about math is that sooner or later the truth comes out, and then you know for sure whether your heuristics succeeded.) If a paper fails one or more tests (particularly tests 6-10), that doesn't necessarily mean it's wrong; conversely, if it passes all ten that still doesn't mean it's right. At some point, there might be nothing left to do except to roll up your sleeves, brew some coffee, and tell your graduate student to read the paper and report back to you.
