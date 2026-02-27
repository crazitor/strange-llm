---
title: "STOC’2021 and BosonSampling"
author: "Scott Aaronson"
date: "Wed, 23 Jun 2021"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=5549"
---

Happy birthday to Alan Turing!

This week I'm participating virtually in [STOC'2021](http://acm-stoc.org/stoc2021/), which today had a celebration of the 50th anniversary of NP-completeness (featuring Steve Cook, Richard Karp, Leonid Levin, Christos Papadimitriou, and Avi Wigderson), and which tomorrow will have a day's worth of quantum computing content, including a tutorial on MIP*=RE, two quantum sessions, and an invited talk on quantum supremacy by John Martinis. I confess that I'm not a fan of GatherTown, the platform being used for STOC. Basically, you get a little avatar who wanders around a virtual hotel lobby and enters sessions--but it seems to reproduce all of the frustrating and annoying parts of experience without any of the good parts.

Ah! But I got the surprising news that Alex Arkhipov and I are among the winners of STOC's first-ever ["Test of Time Award,"](https://sigact.org/prizes/stoc_tot.html) for our [paper on BosonSampling](https://www.scottaaronson.com/papers/optics.pdf). It feels strange to win a "Test of Time" award for work that we did in 2011, which still seems like yesterday to me. All the more since the experimental status and prospects of quantum supremacy via BosonSampling are still very much live, unresolved questions.

Speaking of which: on Monday, Alexey Rubtsov, of the Skolkovo Institute in Moscow, gave a talk for our quantum information group meeting at UT, about his [recent work with Popova](https://arxiv.org/abs/2106.01445) on classically simulating Gaussian BosonSampling. From the talk, I learned something extremely important. I had imagined that their simulation must take advantage of the high rate of photon loss in actual experiments (like the [USTC experiment](https://scottaaronson.blog/?p=5159) from late 2020), because how else are you going to simulate BosonSampling efficiently? But Rubtsov explained that that's not how it works at all. While their algorithm is heuristic and remains to be rigorously analyzed, numerical studies suggest that it works even with _no_ photon losses or other errors. Having said that, their algorithm works:

  * only for Gaussian BosonSampling, not Fock-state BosonSampling (as Arkhipov and I had originally proposed),
  * only for threshold detectors, not photon-counting detectors, and
  * only for a small number of modes (say, linear in the number of photons), not for a large number of modes (say, quadratic in the number of photons) as in the original proposal.



So, bottom line, it now looks like the USTC experiment, amazing engineering achievement though it was, is not hard to spoof with a classical computer. If so, this is because of multiple ways in which the experiment differed from my and Arkhipov's original theoretical proposal. We know exactly what those ways are--indeed, you can find them in my earlier blog posts on the subject--and hopefully they can be addressed in future experiments. All in all, then, we're left with a powerful demonstration of the continuing relevance of formal hardness reductions, and the danger of replacing them with intuitions and "well, it still seems hard to _me_." So I hope the committee won't rescind my and Arkhipov's Test of Time Award based on these developments in the past couple weeks!
