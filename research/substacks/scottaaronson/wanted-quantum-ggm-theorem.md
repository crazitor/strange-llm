---
title: "Wanted: Quantum GGM theorem"
author: "Scott Aaronson"
date: "Sun, 03 May 2009"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=403"
---

A commenter on my last post writes:

> Dear Scott, Please keep the focus of your blog. You have lately been losing science to your blog and started blogging about various loosely related things. One of the ways I subscribed to your blog was because your articles were very computation-oriented. Now you no longer keep the theme. And as you might have heard, shifting topics in your blog will lose your readers.

So today I noticed something bizarre. A celebrated result in cryptography, due to Goldreich, Goldwasser, and Micali, states that any pseudorandom generator gives rise to a pseudorandom function family. See [Luca's notes](http://www.cs.berkeley.edu/~luca/cs276/lecture14.pdf) or the [original GGM paper](http://groups.csail.mit.edu/cis/pubs/shafi/1986-jacm.pdf) for more.

Now I'd always assumed, without thinking about it, that the GGM result "obviously" carries over to the quantum case--so that any pseudorandom generator secure against quantum attack would give rise to a pseudorandom function family secure against quantum attack. But now that I'm writing a paper that actually relies on this "fact," I realized I have no idea why it's true.

Look: in the GGM argument, you start with a pseudorandom generator G:{0,1}n→{0,1}2n, and you apply it recursively to produce a family of functions fs:{0,1}n→{0,1}n, where s is the seed. You then consider a hypothetical polynomial-time algorithm A that distinguished fs from a truly random function. You show how you could use A to create a polynomial-time algorithm that distinguished the output of G from a truly random 2n-bit string--thereby contradicting the starting assumption that G was pseudorandom.

The trouble is, the argument relies crucially on the fact that A examines only a polynomial number of outputs of fs--intuitively so that you can run a hybrid argument, changing the outputs that A actually examines one by one into truly random strings. But if A is a quantum algorithm, then (duh) it can examine all 2n outputs of fs in superposition! So any argument that depends on "watching A to see which inputs it queries" is toast.

But maybe we can recover the same conclusion in a fancier way? For at least seven years, I've been going around conjecturing the following:

_**Conjecture ():** Let Q be a quantum algorithm that makes T queries to a Boolean input X∈{0,1}N. Then for all ε,δ>0, there exists a deterministic classical algorithm that makes poly(T,1/ε,log(1/δ)) queries to X, and that approximates Q's acceptance probability to within ε on a 1-δ fraction of inputs._

My motivation for Conjecture (****) had nothing to do with cryptography. I was interested in whether we could rule out the possibility that**P** =**BQP** relative to a random oracle with probability 1. If Conjecture (****) holds --and if the classical algorithm is anything like I think it is--then we _can 't_ rule it out, at least not without proving **P** ≠**PSPACE** or an even stronger separation in the unrelativized world.

It now occurs to me that, if we knew how to prove Conjecture (****), then _maybe_ we could push through a quantum GGM argument using similar ideas--that is, by identifying a tiny subset of inputs to fs that the quantum algorithm's acceptance probability "really" depends on. Alas, I have good reason to believe that Conjecture (****) is hard.

So the task remains: **prove a quantum GGM theorem.** Or maybe I'm missing something completely obvious?

PS. The promised report on the QIS conference in Virginia is coming tomorrow. Take that, future self!

**Update (5/3):** An anonymous commenter points out that we can use a simpler hybrid argument of Razborov and Rudich--which _doesn 't_ break down in the quantum case--to show that if there exists a PRG that's secure against 2n^Ω(1)-time quantum adversaries, then there also exists a PRF with polynomial seed length that's secure against exponential-time quantum adversaries. That somehow hadn't occurred to me, and it's good enough for my purposes. (Masked cryptographer: emerge ye from the shadows, and claim thy rightful honour in my Acknowledgments!) On the other hand, the extremely interesting question still stands of whether one can prove a "strong," GGM-style reduction: from PRGs secure against f(n)-time quantum adversaries to PRFs with linear seed length secure against f(n)Ω(1)-time quantum adversaries, for any superpolynomial f.
