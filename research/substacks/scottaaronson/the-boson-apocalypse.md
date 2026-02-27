---
title: "The Boson Apocalypse"
author: "Scott Aaronson"
date: "Fri, 21 Dec 2012"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=1177"
---

If the world ends today, at least it won't do so without three identical photons having been used to sample from a probability distribution defined in terms of the permanents of 3×3 matrices, thereby demonstrating the Aaronson-Arkhipov BosonSampling protocol. And the results were obtained by no fewer than four independent experimental groups, some of whom have now published in _Science_. One of the groups is based in Brisbane, Australia, one in Oxford, one in Vienna, and one in Rome; they coordinated to release their results the same day. That's right, the number of papers (4) that these groups managed to choreograph to appear simultaneously actually exceeds the number of photons that they so managed (3). The Brisbane group was even generous enough to ask me to coauthor: I haven't been within 10,000 miles of their lab, but I did try to make myself useful to them as a "complexity theory consultant."

Here are links to the four experimental BosonSampling papers released in the past week:

  * [Experimental BosonSampling](http://arxiv.org/abs/1212.2234) by Broome et al. (Brisbane)
  * [Experimental Boson Sampling](http://arxiv.org/abs/1212.2240) by Tillmann et al. (Vienna)
  * [Experimental Boson Sampling](http://arxiv.org/abs/1212.2622) by Walmsley et al. (Oxford)
  * [Experimental boson sampling in arbitrary integrated photonic circuits](http://arxiv.org/abs/1212.2783) by Crespi et al. (Italy)



For those who want to know the theoretical background to this work:

  * [My and Alex's original 100-page BosonSampling paper](http://www.scottaaronson.com/papers/optics-toc.pdf) (to appear soon in the journal [ _Theory of Computing_](http://theoryofcomputing.org/))
  * [The 10-page STOC'2011 version](http://www.scottaaronson.com/papers/optics-cr.pdf) of our paper
  * [My PowerPoint slides](http://www.scottaaronson.com/talks/optics-toc2.ppt)
  * [Alex's slides](http://stellar.mit.edu/S/course/6/fa12/6.845/courseMaterial/topics/topic3/lectureNotes/Boson_presentation/Boson_presentation.ppt)
  * [Theoretical Computer Science StackExchange question and answer](http://cstheory.stackexchange.com/questions/2892/how-does-the-bosonsampling-paper-avoid-easy-classes-of-complex-matrices)
  * [Gil Kalai's blog post](http://gilkalai.wordpress.com/2010/11/17/aaronson-and-arkhipovs-result-on-hierarchy-collapse/)
  * [Old _Shtetl-Optimized_ post](https://scottaaronson.blog/?p=473)



For those just tuning in, here are some popular-level articles about BosonSampling:

  * [Larry Hardesty's _MIT News_ article](http://web.mit.edu/newsoffice/2011/quantum-experiment-0302.html) (from last year)
  * [University of Queensland press release](http://www.uq.edu.au/news/index.html?article=25707)
  * [Victorian counting device gets speedy quantum makeover](http://www.newscientist.com/article/dn23025-victorian-counting-device-gets-speedy-quantum-makeover.html) (this week, from _New Scientist_ ; the article is not bad except that it ought to credit Alex Arkhipov)
  * [New Form of Quantum Computation Promises Showdown with Ordinary Computers](http://news.sciencemag.org/sciencenow/2012/12/new-form-of-quantum-computation-.html), by Adrian Cho (from _Science_)



I'll be happy to answer further questions in the comments; for now, here's a brief FAQ:

**Q:** Why do you need photons in particular for these experiments?

**A:** What we need is identical bosons, whose transition amplitudes are given by the permanents of matrices. If it were practical to do this experiment with Higgs bosons, they would work too! But photons are more readily available.

**Q:** But a BosonSampling device isn't really a "computer," is it?

**A:** It depends what you mean by "computer"! If you mean a physical system that you load input into, let evolve according to the laws of physics, then measure to get an answer to a well-defined mathematical problem, then sure, it's a computer! The only question is whether it's a _useful_ computer. We don't believe it can be used as a _universal_ quantum computer--or even, for that matter, as a universal _classical_ computer. More than that, Alex and I weren't able to show that solving the BosonSampling problem has _any_ practical use for anything. However, we did manage to amass evidence that, despite being _useless_ , the BosonSampling problem is also _hard_ (at least for a classical computer). And for us, the hardness of classical simulation was the entire point.

**Q:** So, these experiments reported in _Science_ this week have done something that no classical computer could feasibly simulate?

**A:** No, a classical computer can handle the simulation of 3 photons without much--or really, any--difficulty. This is only a first step: before this, the analogous experiment (called the _Hong-Ou-Mandel dip_) had only ever been performed with 2 photons, for which there's not even any difference in complexity between the permanent and the determinant (i.e., between bosons and fermions). However, if you could scale this experiment up to about 30 photons, _then_ it's likely that the experiment would be solving the BosonSampling problem faster than any existing classical computer (though the latter could eventually solve the problem as well). And if you could scale it up to 100 photons, then you might never even know if your experiment was working correctly, because a classical computer would need such an astronomical amount of time to check the results.
