---
title: "BusyBeaver(6) is really quite large"
author: "Scott Aaronson"
date: "Sat, 28 Jun 2025"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=8972"
---

For overdetermined reasons, I've lately found the world an increasingly terrifying and depressing place. It's gotten harder and harder to concentrate on research, or even popular science writing. Every so often, though, something breaks through that wakes my inner child, reminds me of why I fell in love with research thirty years ago, and helps me forget about the triumphantly strutting factions working to destroy everything I value.

Back in 2022, I [reported an exciting advance](https://scottaaronson.blog/?p=6673) in [BusyBeaverology](https://www.scottaaronson.com/papers/bb.pdf): namely, whereas we previously knew merely that BB(6) > 1036,534, Pavel Kropitz managed to show that

BB(6) > 1510.

For those tuning in from home, here BB(6) is the 6th Busy Beaver number, i.e. the maximum number of steps that a 6-state Turing machine with a {0,1} alphabet can take before halting, when run on an initially all-0 input tape. Also, the left-superscript means _[tetration](https://en.wikipedia.org/wiki/Tetration)_ , or iterated exponentiation: for example, 1510 means 10 to the 10 to the 10 and so on 15 times.

By comparison, last year the international "BBchallenge" team [determined that BB(5) is "merely" 47,176,870](https://scottaaronson.blog/?p=8088) (see also _Quanta_ magazine's [superb feature article](https://www.quantamagazine.org/amateur-mathematicians-find-fifth-busy-beaver-turing-machine-20240702/) on that milestone). So, between 5 and 6 is where the Busy Beaver function makes its leap, from the millions to beyond the bounds of observable reality.

But if you thought that was the end of the BB(6) story, think again! Eleven days ago, Tristan Sterin, who organized the BBchallenge the team, emailed to tell me that a team member with the handle "mxdys" [improved the BB(6) bound yet further](https://wiki.bbchallenge.org/wiki/1RB1LC_1LA1RE_0RD0LA_1RZ1LB_1LD0RF_0RD1RB), to

BB(6) > 10,000,00010

(i.e., 10 to the 10 to the 10 and so on 10 million times), with a [correctness proof in Coq](https://github.com/ccz181078/busycoq/blob/BB6/verify/SOBCv4.v). Then, three days ago, Tristan wrote _again_ to say that mxdys has [improved the bound _again_](https://bbchallenge.org/1RB1RA_1RC---_1LD0RF_1RA0LE_0LD1RC_1RA0RE), to

$$ BB(6) \gt ^{^{{^9}2}2}2 $$

I.e., BB(6) is at least 2 tetrated to the 2 tetrated to the 2 tetrated to the 9. So in particular, BB(6) is at least 2 pentated to the 5, where _[pentation](https://en.wikipedia.org/wiki/Pentation)_ is iterated tetration, i.e. the operation that is to tetration as tetration is to exponentiation, exponentiation is to multiplication, and multiplication is to addition.

Last week, when we "merely" knew that BB(6) > 10,000,00010, I talked to a journalist who asked me to give an intuitive sense of how big such a number is. So I said, imagine you had 10,000,00010 grains of sand. Then you could … well, uh … you could fill about 10,000,00010 copies of the observable universe with that sand. I hope that helps people visualize it!

The journalist also asked: have these new discoveries about BB(6) caused me to rethink any broader beliefs about the Busy Beaver function? And I mean, yes and no: it was _always_ completely within the realm of possibility that BB(6) would already be, not some puny little thing like 1036,534, but way out in iteration land. Now that we know for sure that it is, though, maybe I ought to conjecture that the value of BB(n) becomes independent of the ZFC axioms of set theory already when n is 7 or 8 or 9, rather than when it's 20 or 30 or whatever. (Currently, we [know](https://scottaaronson.blog/?p=7388) [that](https://github.com/CatsAreFluffy/metamath-turing-machines) BB(n) becomes independent of ZFC only when n=643.)

* * *

**Unrelated Update:** I'm just now returning to the US from [STOC'2025](https://acm-stoc.org/stoc2025/STOCprogram.html) in Prague, where I saw lots of old friends and learned many interesting new things, again helping to distract me from the state of the world! Many I'll write about some of those things in a future post. For now, though, anyone who's interested in my STOC plenary lecture, entitled "The Status of Quantum Speedups," can [check out the PowerPoint slides here](https://www.scottaaronson.com/talks/status.ppt).
