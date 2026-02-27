---
title: "Quantum Information Supremacy"
author: "Scott Aaronson"
date: "Fri, 12 Sep 2025"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=9138"
---

I'm thrilled that our paper entitled [Demonstrating an unconditional separation between quantum and classical information resources](https://arxiv.org/abs/2509.07255), based on a collaboration between UT Austin and Quantinuum, is finally up on the arXiv. I'm equally thrilled that my coauthor and former PhD student [William Kretschmer](https://wkretschmer.github.io/) — who led the theory for this project, and even wrote much of the code — is now my faculty colleague at UT Austin! My physics colleague [Nick Hunter-Jones](https://nickrhj.github.io/) and my current PhD student [Sabee Grewal](https://sabeegrewal.com/) made important contributions as well. I'd especially like to thank the team at Quantinuum for recognizing a unique opportunity to test and showcase their cutting-edge hardware, and collaborating with us wild-eyed theorists to make it happen. This is something that, crucially, would _not_ have been feasible with the quantum computing hardware of only a couple years ago.

Here's our abstract, which I think explains what we did clearly enough, although do [read the paper](https://arxiv.org/pdf/2509.07255) for more:

> A longstanding goal in quantum information science is to demonstrate quantum computations that cannot be feasibly reproduced on a classical computer. Such demonstrations mark major milestones: they showcase fine control over quantum systems and are prerequisites for useful quantum computation. To date, quantum advantage has been demonstrated, for example, through violations of Bell inequalities and sampling-based quantum supremacy experiments. However, both forms of advantage come with important caveats: Bell tests are not computationally difficult tasks, and the classical hardness of sampling experiments relies on unproven complexity-theoretic assumptions. Here we demonstrate an unconditional quantum advantage in information resources required for a computational task, realized on Quantinuum's H1-1 trapped-ion quantum computer operating at a median two-qubit partial-entangler fidelity of 99.941(7)%. We construct a task for which the most space-efficient classical algorithm provably requires between 62 and 382 bits of memory, and solve it using only 12 qubits. Our result provides the most direct evidence yet that currently existing quantum processors can generate and manipulate entangled states of sufficient complexity to access the exponentiality of Hilbert space. This form of quantum advantage -- which we call quantum information supremacy -- represents a new benchmark in quantum computing, one that does not rely on unproven conjectures.

I'm very happy to field questions about this paper in the comments section.

* * *

**Unrelated Announcement:** As some of you might have seen, yesterday's _Wall Street Journal_ carried a [piece by Dan Kagan-Kans on "The Rise of 'Conspiracy Physics.'"](https://www.wsj.com/science/physics/the-rise-of-conspiracy-physics-dd79fe36?st=xtHreq&reflink=desktopwebshare_permalink) I talked to the author for the piece, and he quoted this blog in the following passage:

> This resentment of scientific authority figures is the major attraction of what might be called “conspiracy physics.” Most fringe theories are too arcane for listeners to understand, but anyone can grasp the idea that academic physics is just one more corrupt and self-serving establishment. The German physicist Sabine Hossenfelder has attracted 1.72 million YouTube subscribers in part by attacking her colleagues: “Your problem is that you’re lying to the people who pay you,” she declared. “Your problem is that you’re cowards without a shred of scientific integrity.”
> 
> In this corner of the internet, the scientist Scott Aaronson has written, “Anyone perceived as the ‘mainstream establishment’ faces a near-insurmountable burden of proof, while anyone perceived as ‘renegade’ wins by default if they identify any hole whatsoever in mainstream understanding.”
