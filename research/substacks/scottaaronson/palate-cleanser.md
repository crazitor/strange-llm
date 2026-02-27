---
title: "Palate cleanser"
author: "Scott Aaronson"
date: "Mon, 21 Aug 2023"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=7489"
---

  1. Ben Brubaker wrote a [long piece for _Quanta_ magazine](https://www.quantamagazine.org/complexity-theorys-50-year-journey-to-the-limits-of-knowledge-20230817/) about meta-complexity. The first three-quarters are a giant refresher on the story of computability and complexity theory in the 20th century--including Turing, Gödel, Shannon, Cook, Karp, Levin, Baker-Gill-Solovay, Sipser, Razborov, Rudich, and more. But then the last quarter gets into actually new (well, within the last couple years) developments, including the NP-completeness of "Partial-MCSP" and other progress on the Minimum Circuit Size Problem, and progress toward basing cryptography on the sole assumption P≠NP, and ruling out Impagliazzo's "Heuristica" and "Pessiland" worlds. I'm quoted (and helped proofread the piece) despite playing no role in the new developments. Worth a read if you don't already know this stuff.  

  2. Duane Rich created a [Part II](https://www.youtube.com/watch?v=jlh21U2texo&authuser=0) of his YouTube video series on the Busy Beaver function. It features some of the core ideas from [my Busy Beaver survey](https://www.scottaaronson.com/papers/bb.pdf), clearly narrated and beautifully animated. If reading my survey is too much for you, now you can just watch the movie!  

  3. Aznaur Midov recorded a [podcast](https://www.youtube.com/watch?v=q2jTikHtxEc&t=1s) with me about quantum computing and AI--just in case you haven't got enough of either of those lately.  

  4. Oded Regev put an [exciting paper](https://arxiv.org/abs/2308.06572) on the arXiv, showing how to factor an n-digit integer using quantum circuits of size ~O(n3/2) (multiple such circuits, whose results are combined classically), assuming a smoothness conjecture from number theory. This compares to ~O(n2) for Shor's algorithm. Regev's algorithm uses classical algorithms for lattice problems, thereby connecting that subject to quantum factoring. This might or might not bring nearer in time the day when we can break (say) 2048-bit RSA keys using a quantum computer--that mostly depends, apparently, on whether Regev's algorithm can also be made highly efficient in its use of qubits.  

  5. A team from IBM, consisting of Sergey Bravyi, Andrew Cross, Jay Gambetta, Dmitri Maslov, Ted Yoder, and my former student Patrick Rall, put [another exciting paper](https://arxiv.org/abs/2308.07915) on the arXiv, which reports an apparent breakthrough in quantum error-correction--building a quantum memory based on LDPC (Low Density Parity Check) codes rather than the Kitaev surface code, and which (they say) with an 0.1% physical error rate, can preserve 12 logical qubits for ten million syndrome cycles using 288 physical qubits, rather than more than 4000 physical qubits with the surface code. Anyone who understands in more detail is welcome to comment!  

  6. Boaz Barak [wrote a blog post](https://windowsontheory.org/2023/08/16/reflections-on-making-the-atomic-bomb/) about the history of the atomic bomb, and possible lessons for AI development today. _I 'd_ been planning to write a blog post about the history of the atomic bomb and possible lessons for AI development today. Maybe I'll still write that blog post.  

  7. Last week I attended the excellent [Berkeley Simons Workshop on Large Language Models and Transformers](https://simons.berkeley.edu/workshops/large-language-models-transformers/schedule#simons-tabs), hosted by my former adviser Umesh Vazirani. While there, I gave a talk on watermarking of LLMs, which you can [watch on YouTube](https://www.youtube.com/watch?v=2Kx9jbSMZqA) (see also [here](https://www.scottaaronson.com/talks/llmwatermark.pptx) for the PowerPoint slides). Shtetl-Optimized readers might also enjoy the talk by OpenAI cofounder Ilya Sutskever, [An Observation on Generalization](https://www.youtube.com/watch?v=AKMuA_TVz3A), as well as many other talks on all aspects of LLMs, from theoretical to empirical to philosophical to legal.  

  8. Right now I'm excited to be at [Crypto'2023](https://crypto.iacr.org/2023/) in Santa Barbara, learning a lot about post-quantum crypto and more, while dodging both earthquakes and hurricanes. On Wednesday, I'll give an invited plenary talk about "Neurocryptography": my vision for what cryptography can contribute to AI safety, including via watermarking and backdoors. Who better to enunciate such a vision than someone who's _neither_ a cryptographer nor an AI person? If you're at Crypto and see me, feel free to come say hi.


