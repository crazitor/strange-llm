---
title: "That IACR preprint"
author: "Scott Aaronson"
date: "Tue, 16 Apr 2024"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=7946"
---

**Update (April 19):** Apparently a bug has been found, and the author has withdrawn the claim (see the comments).

* * *

For those who don't yet know from their other social media: a week ago the cryptographer Yilei Chen posted a preprint, eprint.iacr.org/2024/555, claiming to give a polynomial-time quantum algorithm to solve lattice problems. For example, it claims to solve the [GapSVP](https://en.wikipedia.org/wiki/Lattice_problem) problem, which asks to approximate the length of the shortest nonzero vector in a given n-dimensional lattice, to within an approximation ratio of ~n4.5. The best approximation ratio previously known to be achievable in classical or quantum polynomial time was exponential in n.

If it's correct, this is an _extremely_ big deal. It doesn't quite break the main [lattice-based cryptosystems](https://en.wikipedia.org/wiki/Lattice-based_cryptography), but it would put those cryptosystems into a precarious position, vulnerable to a mere further polynomial improvement in the approximation factor. And, as we learned from the recent [NIST competition](https://csrc.nist.gov/projects/post-quantum-cryptography), if the lattice-based and LWE-based systems were to fall, then we really don't have many great candidates left for post-quantum public-key cryptography! On top of that, a full quantum break of LWE (which, again, Chen is _not_ claiming) would lay waste (in a world with scalable QCs, of course) to a large fraction of the beautiful sandcastles that classical and quantum cryptographers have built up over the last couple decades--everything from [Fully Homomorphic Encryption](https://en.wikipedia.org/wiki/Homomorphic_encryption) schemes, to [Mahadev's protocol](https://arxiv.org/abs/1804.01082) for proving the output of any quantum computation to a classical skeptic.

So on the one hand, this would substantially enlarge the scope of exponential quantum speedups beyond what we knew a week ago: yet more reason to try to build scalable QCs! But on the other hand, it could also fuel an argument for coordinating to _slow down_ the race to scalable fault-tolerant QCs, until the world can get its cryptographic house into better order. (Of course, as we've seen with the many proposals to slow down AI scaling, this might or might not be possible.)

So then, is the paper correct? **I don 't know.** It's very obviously a serious effort by a serious researcher, a world away from the P=NP proofs that fill my inbox every day. But it might fail anyway. I've asked the world experts in quantum algorithms for lattice problems, and they've been looking at it, and none of them is ready yet to render a verdict. The central difficulty is that the algorithm is convoluted, and involves new tools that seem to come from left field, including complex Gaussian functions, the windowed quantum Fourier transform, and Karst waves (whatever those are). The algorithm has 9 phases by the author's count. In my own perusal, I haven't yet extracted even a high-level intuition--I can't tell any little story like for Shor's algorithm, e.g. "first you reduce factoring to period-finding, then you solve period-finding by applying a Fourier transform to a vector of amplitudes."

So, the main purpose of this post is simply to throw things open to commenters! I'm happy to provide a public clearinghouse for questions and comments about the preprint, if those studying it would like that. You can even embed LaTeX in your comments, as will probably be needed to get anywhere.

* * *

**Unrelated Update:** Connor Tabarrok and his friends just put a [podcast with me up on YouTube](https://www.youtube.com/watch?v=EK2zEyFyYXM), in which they interview me in my office at UT Austin about watermarking of large language models and other AI safety measures.
