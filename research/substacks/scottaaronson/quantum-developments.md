---
title: "Quantum developments!"
author: "Scott Aaronson"
date: "Fri, 12 Jul 2024"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=8109"
---

Perhaps like the poor current President of the United States, I can feel myself fading, my memory and verbal facility and attention to detail failing me, even while there's so much left to do to battle the nonsense in the world. I started my career on an accelerated schedule--going to college at 15, finishing my PhD at 22, etc. etc.--and the decline is (alas) also hitting me early, at the ripe age of 43.

Nevertheless, I _do_ seem to remember that this was once primarily a quantum computing blog, and that I was known to the world as a quantum computing theorist. And exciting things continue to happen in quantum computing…

* * *

First, a company in the UK called Oxford Ionics [has announced](https://arxiv.org/abs/2407.07694) that it now has a system of trapped-ion qubits in which it's prepared two-qubit maximally entangled states with 99.97% fidelity. If true, this seems extremely good. Indeed, it seems better than the numbers from bigger trapped-ion efforts, and quite close to the ~99.99% that you'd want for quantum fault-tolerance. But maybe there's a catch? Will they not be able to maintain this kind of fidelity when doing a long sequence of programmable two-qubit gates on dozens of qubits? Can the other trapped-ion efforts actually achieve similar fidelities in head-to-head comparisons? Anyway, I was surprised to see how little attention the paper got on [SciRate](https://scirate.com/?range=3). I look forward to hearing from experts in the comment section.

* * *

Second, I almost forgot … but last week Quantinuum [announced](https://arxiv.org/abs/2406.02501) that it's done a better quantum supremacy experiment based on Random Circuit Sampling with 56 qubits--similar to what Google and USTC did in 2019-2020, but this time using 2-qubit gates with 99.84% fidelities (rather than merely ~99.5%). This should set a new standard for those looking to simulate these things using tensor network methods.

* * *

Third, a [new paper by Schuster, Haferkamp, and Huang](https://arxiv.org/abs/2407.07754) gives a major advance on k-designs and pseudorandom unitaries. Roughly speaking, the paper shows that even in one dimension, a random n-qubit quantum circuit, with alternating brickwork layers of 2-qubit gates, forms a "k-design" after only O(k polylog k log n) layers of gates. Well, modulo one caveat: the "random circuit" isn't from the most natural ensemble, but has to have some of its 2-qubit gates set to the identity, namely those that straddle certain contiguous blocks of log n qubits. This seems like a purely technical issue--how could randomizing those straddling gates make the mixing behavior _worse_?--but future work will be needed to address it. Notably, the new upper bound is off from the best-possible k layers by only logarithmic factors. (For those tuning in from home: a [k-design](https://en.wikipedia.org/wiki/Quantum_t-design) informally means a collection of n-qubit unitaries such that, from the perspective of degree-k polynomials, choosing a unitary randomly from the collection looks the same as choosing randomly among _all_ n-qubit unitary transformations--i.e., from the [Haar measure](https://en.wikipedia.org/wiki/Haar_measure).)

Anyway, even in my current decrepit state, I can see that such a result would have implications for … well, all sorts of things that quantum computing and information theorists care about. Again I welcome any comments from experts!

* * *

Incidentally, congratulations to Peter Shor for [winning the Shannon Award](https://www.itsoc.org/news/shannon-award-2025)!
