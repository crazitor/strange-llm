---
title: "Oh right, quantum computing"
author: "Scott Aaronson"
date: "Mon, 31 Oct 2022"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=6784"
---

These days, I often need to remind myself that, as an undergrad, grad student, postdoc, or professor, I've now been doing quantum computing research for a quarter-century--i.e., well over half of the subject's existence. As a direct result, when I feel completely jaded about a new development in QC, it might actually be exciting. When I feel moderately excited, it might actually be the most exciting thing for years.

With that in mind:

* * *

(1) Last week National Public Radio's Marketplace [interviewed](https://www.marketplace.org/2022/10/27/china-and-the-us-vie-for-quantum-computing-supremacy/amp/) me, John Martinis, and others about the current state of quantum computing. While the piece wasn't entirely hype-free, I'm pleased to report that my own views were represented accurately! To wit:

> “There is a tsunami of hype about what quantum computers are going to revolutionize,” said Scott Aaronson, a professor of computer science at the University of Texas at Austin. “Quantum computing has turned into a word that venture capitalists or people seeking government funding will sprinkle on anything because it sounds good.”
> 
> Aaronson warned we can’t be certain that these computers will in fact revolutionize machine learning and finance and optimization problems. “We can’t prove that there’s not a quantum algorithm that solves all these problems super fast, but we can’t even prove there’s not an algorithm for a conventional computer that does it,” he said. [In the recorded version, they replaced this by a simpler but also accurate thought: namely, that we can't prove one way or the other whether there's a useful quantum advantage for these tasks.]

* * *

(2) I don't like to use this blog to toot my own research horn, but on Thursday my postdoc Jason Pollack and I released a paper, entitled [Discrete Bulk Reconstruction](https://arxiv.org/pdf/2210.15601.pdf). And to be honest, I'm pretty damned excited about it. It represents about 8 months of Jason--a cosmologist and string theorist who studied under Sean Carroll--helping me understand [AdS/CFT](https://en.wikipedia.org/wiki/AdS/CFT_correspondence) in the language of the undergraduate CS curriculum, like min-cuts on undirected graphs, so that we could then look for polynomial-time algorithms to implement the holographic mapping from boundary quantum states to the spatial geometry in the bulk. We drew heavily on previous work in the same direction, especially the already-seminal 2015 [holographic entropy cone](https://arxiv.org/abs/1505.07839) paper by Ning Bao et al. But I'd like to think that, among other things, our work represents a new frontier in just how accessible AdS/CFT itself can be made to CS and discrete math types. Anyway, here's the abstract if you're interested:

> According to the _AdS/CFT correspondence_ , the geometries of certain spacetimes are fully determined by quantum states that live on their boundaries -- indeed, by the von Neumann entropies of portions of those boundary states. This work investigates to what extent the geometries can be reconstructed from the entropies _in polynomial time_. Bouland, Fefferman, and Vazirani (2019) argued that the AdS/CFT map can be exponentially complex if one wants to reconstruct regions such as the interiors of black holes. Our main result provides a sort of converse: we show that, in the special case of a single 1D boundary, if the input data consists of a list of entropies of _contiguous_ boundary regions, and if the entropies satisfy a single inequality called Strong Subadditivity, then we can construct a graph model for the bulk in linear time. Moreover, the bulk graph is planar, it has O(N2) vertices (the information-theoretic minimum), and it's "universal," with only the edge weights depending on the specific entropies in question. From a combinatorial perspective, our problem boils down to an "inverse" of the famous min-cut problem: rather than being given a graph and asked to find a min-cut, here we're given the values of min-cuts separating various sets of vertices, and need to find a weighted undirected graph consistent with those values. Our solution to this problem relies on the notion of a "bulkless" graph, which might be of independent interest for AdS/CFT. We also make initial progress on the case of multiple 1D boundaries -- where the boundaries could be connected via wormholes -- including an upper bound of O(N4) vertices whenever a planar bulk graph exists (thus putting the problem into the complexity class NP).

* * *

(3) Anand Natarajan and Chinmay Nirkhe posted a preprint entitled [A classical oracle separation between QMA and QCMA](https://arxiv.org/pdf/2210.15380.pdf), which makes progress on a problem that's been raised on this blog all the way back to its inception. A bit of context: [QMA](https://en.wikipedia.org/wiki/QMA), Quantum Merlin-Arthur, captures what can be proven using a quantum state with poly(n) qubits as the proof, and a polynomial-time quantum algorithm as the verifier. QCMA, or Quantum Classical Merlin-Arthur, is the same as QMA except that now the proof has to be classical. A fundamental problem of quantum complexity theory, first raised by [Aharonov and Naveh](https://arxiv.org/abs/quant-ph/0210077) in 2002, is whether QMA=QCMA. In 2007, [Greg Kuperberg and I](https://arxiv.org/abs/quant-ph/0604056) introduced the concept of quantum oracle separation--that is, a unitary that can be applied in a black-box manner--in order to show that there's a quantum oracle relative to which QCMA≠QMA. In 2015, [Fefferman and Kimmel](https://arxiv.org/abs/1510.06750) improved this, to show that there's a "randomized in-place" oracle relative to which QCMA≠QMA. Natarajan and Nirkhe now remove the "in-place" part, meaning the only thing still "wrong" with their oracle is that it's randomized. Derandomizing their construction would finally settle this 20-year-old open problem (except, of course, for the minor detail of whether QMA=QCMA in the "real," unrelativized world!).

* * *

(4) Oh right, the Google group reports the use of their superconducting processor to [simulate non-abelian anyons](https://arxiv.org/pdf/2210.10255.pdf). Cool.
