---
title: "Doing my oracle duty"
author: "Scott Aaronson"
date: "Mon, 05 Jul 2010"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=451"
---

I promised myself I'd stop blogging about controversial issues whose mere mention could instigate a flamewar and permanently get me in trouble. Well, today I'm going to violate that rule, by blogging about the difference relativized and unrelativized complexity classes.

Recently a colleague of mine, who works in the foundations of quantum mechanics, sent me a long list of questions about the [seminal 1993 paper of Bernstein and Vazirani](http://www.cs.berkeley.edu/~vazirani/pubs/bv.ps) that introduced the complexity class [BQP](http://en.wikipedia.org/wiki/BQP) (Bounded-Error Quantum Polynomial-Time). It was clear to me that all of his questions boiled down to a single point: the distinction between the relativized and unrelativized worlds. This is an absolutely crucial distinction that trips up just about _everyone_ when they're first learning quantum computing.

So I fired off a response, which my colleague said he found extremely helpful. It then occurred to me that what one person found helpful, another might as well--and that which makes 30% of my readers' eyes glaze over with its thoroughgoing duh-obviousness, might be very thing that another 30% of my readers most want to see. So without further ado, the two worlds of quantum complexity theory…

In the **relativized world** , we let our algorithms access potentially-powerful oracles, whose internal structure we don't examine (think of Simon's algorithm for concreteness). In that world, we can indeed prove unconditionally that BPP≠BQP--that is, quantum computers can solve certain problems exponentially faster than classical computers, when both computers are given access to the same oracle.

In general, almost every "natural" complexity class has a relativized version associated with it, and the relativized versions tend to be _much_ easier to separate than the unrelativized versions (it's basically the difference between a masters or PhD thesis and a Fields Medal!) So for example, within the relativized world, we can separate not only BPP from BQP, but also P from NP, NP from PSPACE, NP from BQP, etc.

By contrast, in the **unrelativized world** (where there are no oracles), we can't separate _any_ complexity classes between P and PSPACE. Doing so is universally recognized as one of the biggest open problems in mathematics (in my opinion, it's far-and-away the biggest problem).

Now, Bernstein and Vazirani proved that BQP is "sandwiched" between P and PSPACE. For that reason, as they write in their paper, one can't hope to prove P≠BQP in the unrelativized world without also proving P≠PSPACE.

Let's move on to another major result from Bernstein and Vazirani's paper, namely their oracle separation between BPP and BQP. You might wonder: what's the point of proving such a thing? Well, the Bernstein-Vazirani oracle separation gave the first formal evidence that BQP "might" be larger than BPP. For if BPP equaled BQP relative to every oracle, then in particular, they'd have to be equal relative to the empty oracle--that is, in the unrelativized world!

(The converse need not hold: it could be the case that BPP=BQP, despite the existence of an oracle that separates them. So, again, separating complexity classes relative to an oracle can be thought of as a "baby step" toward separating them in the real world.)

But an even more important motivation for Bernstein and Vazirani's oracle separation is that it led shortly afterward to a better oracle separation by Simon, and that, in turn, led to Shor's factoring algorithm.

In a sense, what Shor did was to "remove the oracle" from Simon's problem. In other words, Shor found a concrete problem in the unrelativized world (namely factoring integers), which has a natural function associated with it (namely the modular exponentiation function, f(r) = xr mod N) that one can usefully _treat_ as an oracle. Treating f as an oracle, one can then use a quantum algorithm related to Simon's algorithm to find the period of f, and that in turn lets you factor integers in polynomial time.

Of course, Shor's algorithm became much more famous than Simon's algorithm, since the implications for computer science, cryptography, etc. were so much more concrete and dramatic than with an abstract oracle separation. However, the downside is that the speedup of Shor's algorithm is no longer _unconditional_ : for all anyone knows today, there might also a fast classical algorithm to factor integers. By contrast, the speedup of Simon's algorithm (and of Bernstein-Vazirani before it) is an unconditional one.
