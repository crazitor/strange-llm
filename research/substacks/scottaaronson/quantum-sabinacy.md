---
title: "Quantum Sabinacy"
author: "Scott Aaronson"
date: "Mon, 01 Jul 2019"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=4220"
---

Sabine Hossenfelder--well-known to readers of _Shtetl-Optimized_ for [opposing the building](https://scottaaronson.blog/?p=4122) of a higher-energy collider, and various other things--has weighed in on "quantum supremacy" in [this blog post](http://backreaction.blogspot.com/2019/06/quantum-supremacy-what-is-it-and-what.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed:+Backreaction+\(Backreaction\)&m=1) and [this video](https://www.youtube.com/watch?time_continue=1&v=GKnfVA1v5ow). Sabine consulted with me by phone before doing the video and post, and despite what some might see as her negative stance, I agree with what she has to say substantially more than I disagree.

I do, however, have a few quibbles:

1\. We don’t know that millions of physical qubits will be needed for useful simulations of quantum chemistry.  It all depends on how much error correction is needed and how good the error-correcting codes and simulation algorithms become. Like, sure, you can generate pessimistic forecasts by plugging numbers in to the best known codes and algorithms. But "the best known" is a rapidly moving target--one where there have already been orders-of-magnitude improvements in the last decade.

2\. To my mind, there’s a big conceptual difference between a single molecule that you can’t efficiently simulate classically, and a programmable computer that you can't efficiently simulate classically.  The difference, in short, is that only for the computer, and not for the molecule, would it ever make sense to say it had given you a **wrong** answer! In other words, a physical system becomes a "computer" when, and only when, you have sufficient understanding of, and control over, its state space and time evolution that you can ask the system to simulate something _other than itself_ , and then judge whether it succeeded or failed at that goal.

3\. The entire point of my recent work, on certified randomness generation (see for example [here](https://www.scottaaronson.com/talks/certrand2.ppt) or [here](https://www.quantamagazine.org/how-to-turn-a-quantum-computer-into-the-ultimate-randomness-generator-20190619/)), is that sampling random bits with a NISQ-era device _could_ have a practical application. That application is … I hope you're sitting down for this … sampling random bits! And then, more importantly and nontrivially, **proving** to a faraway skeptic that the bits really were randomly generated.

4\. While I was involved in some of the first proposals for NISQ quantum supremacy experiments (such as [BosonSampling](https://en.wikipedia.org/wiki/Boson_sampling)), I certainly can’t take sole credit for the idea of quantum supremacy!  The term, incidentally, [was coined by John Preskill](https://arxiv.org/abs/1203.5813).

5\. The term "NISQ" (Noisy Intermediate Scale Quantum) was also [coined by John Preskill](https://arxiv.org/abs/1801.00862).  He had no intention of misleading investors—he just needed a term to discuss the quantum computers that will plausibly be available in the near future.  As readers of this blog know, there certainly _has_ been some misleading of investors (and journalists, and the public…) about the applications of near-term QCs. But I don't think you can lay it at the feet of the term “NISQ.”
