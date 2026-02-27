---
title: "Why Quantum Mechanics?"
author: "Scott Aaronson"
date: "Tue, 25 Jan 2022"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=6244"
---

In the past few months, I've twice injured the same ankle while playing with my kids. This, perhaps combined with covid, led me to several indisputable realizations:

  1. I am mortal.
  2. Despite my self-conception as a nerdy little kid awaiting the serious people's approval, I am now firmly middle-aged. By my age, Einstein had completed general relativity, Turing had founded CS, won WWII, _and_ proposed the Turing Test, and Galois, Ramanujan, and Ramsey had been dead for years.
  3. Thus, whatever I wanted to accomplish in my intellectual life, I should probably get started on it _now_.



Hence today's post. I'm feeling a strong compulsion to write an essay, or possibly even a book, surveying and critically evaluating a century of ideas about the following question:

**Q: Why should the universe have been quantum-mechanical?**

If you want, you can divide Q into two subquestions:

**Q1: Why didn 't God just make the universe classical and be done with it? What would've been wrong with _that_ choice?**

**Q2: Assuming classical physics wasn 't good enough for whatever reason, why this specific alternative? Why the complex-valued amplitudes? Why unitary transformations? Why the Born rule? Why the tensor product?**

Despite its greater specificity, Q2 is ironically the question that I feel we have a better handle on. I could spend half a semester teaching theorems that admittedly don't _answer_ Q2, as satisfyingly as Einstein answered the question "why the Lorentz transformations?," but that at least render this particular set of mathematical choices (the 2-norm, the Born Rule, complex numbers, etc.) orders-of-magnitude less surprising than one might've thought they were _a priori_. Q1 therefore stands, to me at least, as the more mysterious of the two questions.

So, I want to write something about the space of credible answers to Q, and especially Q1, that humans can currently conceive. I want to do this for my own sake as much as for others'. I want to do it because I regard Q as one of the biggest questions ever asked, for which it seems plausible to me that there's simply an _answer_ that most experts would accept as valid once they saw it, but for which no such answer is known. And also because, besides having spent 25 years working in quantum information, I have the following qualifications for the job:

  * I don't dismiss either Q1 _or_ Q2 as silly; and
  * crucially, I don't think I already know the answers, and merely need better arguments to justify them. I'm genuinely uncertain and confused.



**The purpose of this post is to invite you to share your own answers to Q in the comments section.** Before I embark on my survey project, I'd better know if there are promising ideas that I've missed, and this blog seems like as good a place as any to crowdsource the job.

Any answer is welcome, no matter how wild or speculative, _so long as it honestly grapples with the actual nature of QM_. To illustrate, nothing along the lines of "the universe is quantum because it needs to be holistic, interconnected, full of surprises, etc. etc." will cut it, since such answers leave utterly unexplained why the world wasn't simply endowed with those properties directly, rather than specifically via _generalizing the rules of probability to allow interference and noncommuting observables_.

Relatedly, whatever "design goal" you propose for the laws of physics, if the goal is satisfied by QM, but satisfied _even better_ by theories that provide _even more_ power than QM does--for instance, superluminal signalling, or violations of [Tsirelson's bound](https://en.wikipedia.org/wiki/Tsirelson%27s_bound), or the efficient solution of NP-complete problems--then your explanation is out. This is a remarkably strong constraint.

Oh, needless to say, don't try my patience with anything about the uncertainty principle being due to floating-point errors or rendering bugs, or anything else that relies on a travesty of QM lifted from a popular article or meme! 

OK, maybe four more comments to enable a more productive discussion, before I shut up and turn things over to you:

  1. I'm aware, of course, of the radical uncertainty about what form an answer to Q should even take. Am I asking you to psychoanalyze the will of God in creating the universe? Or, what perhaps amounts to the same thing, am I asking for the design objectives of the giant computer simulation that we're living in? (As in, "I'm 100% fine with living inside a Matrix … I just want to understand why it's a _unitary_ matrix!") Am I instead asking for an anthropic explanation, showing why _of course_ QM would be needed if you wanted life or consciousness like ours? Am I "merely" asking for simpler or more intuitive physical principles from which QM is to be derived as a consequence? Am I asking why QM is the "most elegant choice" in some space of mathematical options … even to the point where, with hindsight, a 19th-century mathematician or physicist could've been convinced that _of course_ this must be part of Nature's plan? Am I asking for something else entirely? **You get to decide**!**Should you take up my challenge, this is both your privilege and your terrifying burden.**  

  2. I'm aware, of course, of the dizzying array of central physical phenomena that rely on QM for their ultimate explanation. These phenomena range from the stability of matter itself, which depends on the Pauli exclusion principle; to the nuclear fusion that powers the sun, which depends on a quantum tunneling effect; to the discrete energy levels of electrons (and hence, the combinatorial nature of chemistry), which relies on electrons being waves of probability amplitude that can only circle nuclei an integer number of times if their crests are to meet their troughs. Important as they are, though, I don't regard any of these phenomena as satisfying answers to Q in themselves. The reason is simply that, in each case, it would seem like child's-play to contrive some classical mechanism to produce the same effect, were that the goal. QM just seems far too grand to have been the answer to _these_ questions! An exponentially larger state space for all of reality, _plus_ the end of Newtonian determinism, just to overcome the technical problem that accelerating charges radiate energy in classical electrodynamics, thereby rendering atoms unstable? It reminds me of the _Simpsons_ episode where Homer [uses a teleportation machine](https://www.youtube.com/watch?v=GZ6cCaEy5eo) to get a beer from the fridge without needing to get up off the couch.  

  3. I'm aware of [Gleason's theorem](https://en.wikipedia.org/wiki/Gleason%27s_theorem), and of the [specialness](https://arxiv.org/abs/quant-ph/0401062) of the 1-norm and 2-norm in linear algebra, and of the [arguments for complex amplitudes](https://scottaaronson.blog/?p=4021) as opposed to reals or quaternions, and of the beautiful work of [Lucien Hardy](https://arxiv.org/abs/quant-ph/0101012) and of [Chiribella et al.](https://arxiv.org/abs/1506.00398) and others on axiomatic derivations of quantum theory. As some of you might remember, I even discussed much of this material in _[Quantum Computing Since Democritus](https://www.amazon.com/Quantum-Computing-since-Democritus-Aaronson/dp/0521199565)_! There's a _huge_ amount to say about these fascinating justifications for the rules of QM, and I hope to say some of it in my planned survey! For now, I'll simply remark that every axiomatic reconstruction of QM that I've seen, impressive though it was, has relied on one or more axioms that struck me as _weird_ , in the sense that I'd have little trouble dismissing the axioms as totally implausible and unmotivated if I hadn't already known (from QM, of course) that they were true. The axiomatic reconstructions _do_ help me somewhat with Q2, but little if at all with Q1.  

  4. To keep the discussion focused, in this post I'd like to exclude answers along the lines of "but what if QM is merely an approximation to something else?," to say nothing of "a century of evidence for QM was all just a massive illusion! LOCAL HIDDEN VARIABLES FOR THE WIN!!!" We can have those debates another day--God knows that, here on _Shtetl-Optimized_ , we [have](https://scottaaronson.blog/?p=6215) and we will. Here I'm asking instead: imagine that, as fantastical as it sounds, QM were not only exactly true, but (along with relativity, thermodynamics, evolution, and the tastiness of chocolate) one of the profoundest truths our sorry species had ever discovered. Why should I have _expected_ that truth all along? What possible reasons to expect it have I missed?


