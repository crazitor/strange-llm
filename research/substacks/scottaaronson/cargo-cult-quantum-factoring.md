---
title: "Cargo Cult Quantum Factoring"
author: "Scott Aaronson"
date: "Thu, 05 Jan 2023"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=6957"
---

Just days after we celebrated [my wife's 40th birthday](https://scottaaronson.blog/?p=6946), she came down with COVID, meaning she's been isolating and I've been spending almost all my time dealing with our kids.

But if experience has taught me anything, it's that the quantum hype train never slows down. In the past 24 hours, at least four people have emailed to ask me about a [new paper](https://arxiv.org/abs/2212.12372) entitled "Factoring integers with sublinear resources on a superconducting quantum processor." Even the security expert Bruce Schneier, while skeptical, took the paper [surprisingly seriously](https://www.schneier.com/blog/archives/2023/01/breaking-rsa-with-a-quantum-computer.html).

The paper claims … well, it's hard to pin down what it claims, but it's certainly _given many people the impression_ that there's been a decisive advance on how to factor huge integers, and thereby break the RSA cryptosystem, using a near-term quantum computer. _Not_ by using [Shor's Algorithm](https://en.wikipedia.org/wiki/Shor%27s_algorithm), mind you, but by using the deceptively similarly named [Schnorr's Algorithm](https://link.springer.com/chapter/10.1007/3-540-46416-6_24). The latter is a classical algorithm based on lattices, which the authors then "enhance" using the heuristic quantum optimization method called [QAOA](https://arxiv.org/abs/1411.4028).

For those who don't care to read further, here is my 3-word review:

## No. Just No.

And here's my slightly longer review:

_Schnorr ≠ Shor_. Yes, even when Schnorr's algorithm is dubiously “enhanced” using QAOA--a quantum algorithm that, incredibly, for all the hundreds of papers written about it, has not yet been convincingly argued to yield any speedup for any problem whatsoever (besides, as it were, the problem of [reproducing its own pattern of errors](https://arxiv.org/abs/1602.07674)) ([one possible recent exception](https://arxiv.org/abs/2208.06909) from Sami Boulebnane and Ashley Montanaro).

In the new paper, the authors spend page after page saying-without-saying that it _might_ soon become possible to break RSA-2048, using a NISQ (i.e., non-fault-tolerant) quantum computer. They do so via two time-tested strategems:

  1. the detailed exploration of irrelevancies (mostly, optimization of the number of _qubits_ , while ignoring the number of _gates_), and
  2. complete silence about the **one crucial point**.



Then, finally, they come clean about the one crucial point in a single sentence of the Conclusion section:

> It should be pointed out that the quantum speedup of the algorithm is unclear due to the ambiguous convergence of QAOA.

“Unclear” is an understatement here. It seems to me that a miracle would be required for the approach here to yield any benefit at all, compared to just running the classical Schnorr's algorithm on your laptop. And if the latter were able to break RSA, it would've already done so.

All told, this is one of the most actively misleading quantum computing papers I’ve seen in 25 years, and I’ve seen … many. Having said that, this actually _isn 't_ the first time I've encountered the strange idea that the exponential quantum speedup for factoring integers, which we know about from Shor’s algorithm, should somehow “rub off” onto quantum optimization heuristics that embody none of the actual insights of Shor's algorithm, as if by sympathetic magic. Since this idea needs a name, I'd hereby like to propose **Cargo Cult Quantum Factoring**.

And with that, I feel I've adequately discharged my duties here to sanity and truth. If I'm slow to answer comments, it'll be because I'm dealing with two screaming kids.
