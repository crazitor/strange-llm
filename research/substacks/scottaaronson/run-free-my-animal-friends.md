---
title: "Run free, my animal friends!"
author: "Scott Aaronson"
date: "Tue, 11 Oct 2005"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=11"
---

In August of 2002 I opened the [Complexity Zoo](http://qwiki.caltech.edu/wiki/Complexity_Zoo): an online bestiary of 196 complexity classes, since expanded to 443. Yesterday I entrusted the Zoo to anyone on Earth who wants to feed the animals or contribute their own. This was possible because of [John Stockton](http://qwiki.caltech.edu/wiki/John_Stockton), who graciously converted the Zoo to wiki form.

The decision to relinquish control of my best-known work was tinged with regret. But at age 3, my baby is all grown up, and it's time to send it off to grad school so I can move on to other things.

This seems like a good occasion to ask a potentially heretical question:

> Did theoretical computer science take a wrong turn when it introduced complexity classes?

For readers with social lives, I should explain that a "complexity class" is a class of problems solvable by some sort of idealized computer. For example, P (Polynomial-Time) consists of all problems that an ordinary computer could solve in a "reasonable" amount of time, meaning an amount that increases like the problem size raised to a fixed power. To illustrate, a few years ago Agrawal, Kayal, and Saxena made [international headlines](http://fatphil.org/maths/AKS/) for showing that ["PRIMES is in P."](http://www.math.princeton.edu/%7Eannals/issues/2004/Sept2004/Agrawal.pdf) What this means is that they found a general method to decide if an n-digit number is prime or composite, using only about n12 steps -- much less than you'd need to try all possible divisors. Faster methods were known before, but they had a small chance of not producing an answer.

Other complexity classes include PSPACE (Polynomial Space), BQP (Bounded-Error Quantum Polynomial Time), EXP, NP, coNP, BPP, RP, ZPP, PH, Σ2P, P/poly, L, NL, PP, AWPP, LWPP, BQNC, QMA, QCMA, S2P, SZK, NISZK, and [many more](http://qwiki.caltech.edu/wiki/Complexity_Zoo).

The advantage of this alphabet soup is that it lets us express complicated insights in an incredibly compact way:

  * If NP is in BPP then NP=RP.
  * If NP is in P/poly then PH = Σ2P.
  * PH is in P#P.
  * NL=coNL.



The disadvantage, of course, is that it makes us sound like the fabled prisoners who tell each other jokes by calling out their code numbers. Again and again, I've had trouble getting across to outsiders that complexity theory is not "about" capital letters, any more than chemistry is "about" weird strings like NaCl-KCl-MgCl2-H20\. Why is it so hard to explain that we don't worry about EXP vs. P/poly because we're eccentric anal-retentives, but because we want to know whether a never-ending cavalcade of machines, each richer and more complicated than the last, might possibly succeed at a task on which any one machine must inevitably founder -- namely, the task of outracing time itself, of simulating cosmic history in an eyeblink, of seeing in the unformed clumps of an embryonic universe the swirl of every galaxy and flight of every hummingbird billions of years hence, like Almighty God Himself?

(Alright, maybe I meant BQEXP vs. BQP/poly.)

In the early 70's, there was apparently a suggestion that NP be called PET, which could stand for three things: "Probably Exponential Time," "Provably Exponential Time" (if P!=NP), or "Previously Exponential Time" (if P=NP). If this silly name had stuck, would our field have developed in a different direction?
