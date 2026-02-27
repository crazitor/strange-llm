---
title: "Quantum fault-tolerance milestones dropping like atoms"
author: "Scott Aaronson"
date: "Tue, 10 Sep 2024"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=8310"
---

**Update:** I’d been wavering—should I vote for the terrifying lunatic, ranting about trans criminal illegal aliens cooking cat meat, or for the nice woman constantly making faces as though the lunatic was completely cracking her up? But when the woman explicitly came out in favor of AI and quantum computing research … _that_ really sealed the deal for me.

* * *

Between roughly 2001 and 2018, I've happy to have done some nice things in quantum computing theory, from the [quantum lower bound for the collision problem](https://www.scottaaronson.com/papers/collision.pdf) to the invention of [shadow tomography](https://arxiv.org/abs/1711.01053). I _hope_ that’s not the end of it. QC research brought me about as much pleasure as anything in life did. So I hope my tired brain can be revved up a few more times, between now and whenever advances in AI or my failing health or the collapse of civilization makes the issue moot. If not, though, there are still many other quantum activities to fill my days: teaching (to which I've returned after two years), advising my students and postdocs, popular writing and podcasts and consulting, and of course, learning about the latest advances in quantum computing so I can share them with you, my loyal readers.

On that note, what a time it is in QC!  Basically, one experimental milestone after another that people talked about since the 90s is finally being achieved, to the point where it’s become hard to keep up with it all. Briefly though:

A couple weeks ago, the Google group [announced an experiment](https://arxiv.org/abs/2408.13687) that achieved net gain from the use of Kitaev’s [surface code](https://en.wikipedia.org/wiki/Toric_code), using 101 physical qubits to encode 1 logical qubit. The headline result here is that, in line with theory, they see the performance improve as they pass to larger codes with more physical qubits and higher distance. Their best demonstrated code has a distance of 7, which is enough to get "beyond break-even" (their logical qubit lasts more than twice as long as the underlying physical qubits), and is also enough that any future improvements to the hardware will get amplified a lot. With superconducting qubits, one is (alas) still limited by how many one can cram onto a single chip. On paper, though, they say that scaling the same setup to a distance-27 code with ~1500 physical qubits would get them down to an error rate of 10-6, good enough to be a building block in a future fault-tolerant QC. They also report correlated bursts of errors that come about once per hour, from a still-unknown source that appears _not_ to be cosmic rays. I hope it's not Gil Kalai in the next room.

Separately, just this morning, Microsoft and Quantinuum [announced](https://azure.microsoft.com/en-us/blog/quantum/2024/09/10/microsoft-and-quantinuum-create-12-logical-qubits-and-demonstrate-a-hybrid-end-to-end-chemistry-simulation/) that they entangled 12 logical qubits on a 56-physical-qubit trapped-ion processor, building on earlier work that I [blogged about in April](https://scottaaronson.blog/?p=7916). They did this by applying a depth-3 logical circuit with 12 logical CNOT gates, to prepare a cat state. They report an 0.2% error rate when they do this, which is 11x better than they would've gotten without using error-correction. (Craig Gidney, in the comments, says that these results still involve postselection.)

The Microsoft/Quantinuum group also did what they called a "chemistry simulation" involving 13 physical qubits. The latter involved "only" 2 logical qubits and 4 logical gates, but 3 of those gates were non-Clifford, which are the hard kind when one is doing error-correction using a transversal code. (CNOT, by contrast, is a Clifford gate.)

Apart from the fact that Google is using superconducting qubits while Microsoft/Quantinuum are using trapped ions, the two results are incomparable in terms of what they demonstrate. Google is just scaling up a _single_ logical qubit, but showing (crucially) that their error rate decreases with increasing size and distance. Microsoft and Quantinuum are sticking with "small" logical qubits with insufficient distance, but they're showing that they can apply logical circuits that entangle up to 12 of these qubits.

Microsoft also [announced](https://blogs.microsoft.com/blog/2024/09/10/microsoft-announces-the-best-performing-logical-qubits-on-record-and-will-provide-priority-access-to-reliable-quantum-hardware-in-azure-quantum/) today a new collaboration with the startup company Atom Computing, headquartered near Quantinuum in Colorado, which is trying to build neutral-atom QCs (like QuEra in Boston). Over the past few years, Microsoft's quantum group has decisively switched from a strategy of "topological qubits or bust" to a strategy of "anything that works," although they assure me that they also remain committed to the topological approach.

Anyway, happy to hear in the comments from anyone who knows more details, or wants to correct me on any particular, or has questions which I or others can try our best to answer.

Let me end by sticking my neck out. _If hardware progress continues at the rate we 've seen for the past year or two, then I find it hard to understand why we won't have useful fault-tolerant QCs within the next decade._ (And now to retreat my neck a bit: the "if" clause in that sentence is important and non-removable!)
