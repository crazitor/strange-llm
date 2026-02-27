---
title: "The Quantum PCP Manifesto"
author: "Scott Aaronson"
date: "Fri, 06 Oct 2006"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=139"
---

Behold the [PCP Theorem](http://www.ams.org/bull/0000-000-00/S0273-0979-06-01143-8/S0273-0979-06-01143-8.pdf), one of the crowning achievements of complexity theory:

> Given a 3SAT formula φ, it's NP-hard to decide whether (1) φ is satisfiable or (2) at most a 1-ε fraction of the clauses are satisfiable, promised that one of these is the case. Here ε is a constant independent of n.

In recent weeks, I've become increasingly convinced that a Quantum PCP Theorem like the following will one day be a crowning achievement of quantum complexity theory:

> Given a set of local measurements on an n-qubit register, it's QMA-hard to decide whether (1) there exists a state such that all of the measurements accept with probability 1, or (2) for every state, at most a 1-ε fraction of the measurements accept with probability more than 1-δ, promised that one of these is the case. Here a "local" measurement is one that acts on at most (say) 3 qubits, and ε and δ are constants independent of n.

I'm 99% sure that this theorem (alright, conjecture) or something close to it is true. I'm 95% sure that the proof will require a difficult adaptation of classical PCP machinery (whether [Iritean](http://www.cs.huji.ac.il/%7Edinuri/mypapers/combpcp.pdf) or [pre-Iritean](http://www.cs.princeton.edu/%7Earora/pubs/almss.ps)), in much the same way that the [Quantum Fault-Tolerance Theorem](http://www.arxiv.org/abs/quant-ph/9906129) required a difficult adaptation of classical fault-tolerance machinery. I'm 85% sure that the proof is achievable in a year or so, should enough people make it a priority. I'm 75% sure that the proof, once achieved, will open up heretofore undreamt-of vistas of understanding and insight. I'm 0.01% sure that I can prove it. And that is why I hereby bequeath the actual proving part to you, my readers.

Notes:

  1. By analogy to the classical case, one expects that a full-blown Quantum PCP Theorem would be preceded by weaker results ("quantum assignment testers", quantum PCP's with weaker parameters, etc). So these are obviously the place to start.
  2. Why hasn't anyone tackled this question yet? Well, one reason is that it's hard. But a second reason is that people keep getting hung up on exactly how to formulate the question. To forestall further nitpicking, I hereby declare it obvious that a "Quantum PCP Theorem" means nothing more or less than a robust version of [Kitaev's QMA-completeness theorem](http://www.arxiv.org/abs/quant-ph/0406180), in exactly the same sense that the classical PCP Theorem was a robust version of the Cook-Levin Theorem. Any formulation that captures this spirit is fine; mine was only one possibility.


