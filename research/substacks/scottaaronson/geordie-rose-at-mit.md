---
title: "Geordie Rose at MIT"
author: "Scott Aaronson"
date: "Tue, 29 Jan 2008"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=306"
---

While there are many, many things in this world that I'm bent on destroying, [D-Wave Systems](http://www.dwavesys.com/) has never been one of them. Ideally, I'd simply let the D-Wave folks do their thing (namely, try to build an adiabatic quantum computer) while I do my thing (namely, study the fundamental limits of quantum computers). It was only when, in connection with D-Wave, cringe-worthy claims about quantum computing started appearing all over the press that I felt a professional obligation to say something.

Now that I'm "involved," though, I also need to keep you ablog of any notable further developments. And presumably, D-Wave founder Geordie Rose coming to MIT to meet with our quantum information group counts as notable.

Two months ago, you'll recall, we were graced by a [visit](https://scottaaronson.blog/?p=291) from D-Wave's Mohammad Amin and Andrew Berkley, but I'd never before had the pleasure of meeting Geordie. At least formally, the reason for his visit was not to defend D-Wave, but to present ["four hard problems"](http://dwave.wordpress.com/2008/01/29/four-hard-problems/) for _us_ to solve. These problems were as follows:

  1. **Find a practical adiabatic factoring algorithm.** Because of the equivalence of adiabatic and standard quantum computing, we know that such an algorithm exists, but the running time you get from applying the reduction is something like O(n11). Geordie asks for an O(n3) factoring algorithm in the adiabatic model. It was generally agreed (with one dissent, from Geordie) that reducing factoring to a 3SAT instance, and then throwing a generic adiabatic optimization algorithm at the result, would be a really, _really_ bad approach to this problem.
  2. **Find a fault-tolerance threshold for adiabatic quantum computing, similar to the known threshold in the circuit model.** Geordie asserted that such a threshold has to exist, because of the equivalence of adiabatic and standard quantum computing. However, others immediately pointed out that this is not so: the equivalence theorem is not known to be "fault-tolerance-preserving." This is a major open problem that many people have worked on without success.
  3. **Prove upper and lower bounds on the adiabatic algorithm 's performance in finding exact solutions to hard optimization problems.**
  4. **Prove upper and lower bounds on its performance in finding approximate solutions to such problems.** (Ed Farhi described 3 and 4 as "_so_ much harder than anything else we've failed to solve.")



While none of these problems are new to the quantum computing community, they're all extremely good ones, and all (indeed) extremely hard.

Of course, we _did_ also discuss some controversial, red-meat, "did-D-Wave-build-a-quantum-computer" sorts of questions, so I owe it to you to provide a few highlights from that discussion.

Seth Lloyd, who's been more sympathetic to D-Wave than most of us, correctly pointed out that D-Wave has a "credibility problem in the scientific community." He discussed in great detail the experiments D-Wave ought to be doing to convince scientists that they're really seeing quantum effects. I strongly agreed with Seth, adding that I'd rather see _two coherent qubits_ than thousands of incoherent ones. Of course, even if D-Wave could demonstrate two-qubit entanglement (and Geordie says it's the "next thing on the list"), there would still remain the enormous issues of scalability and of the limitations of the adiabatic algorithm in solving hard optimization problems. But at least we could be more comfortable in saying that what they currently have is a tiny quantum computer.

Geordie conceded that, so far, D-Wave has _no direct evidence_ for entanglement among two or more qubits. He nevertheless argued that they have indirect evidence (basically, that their data are better fit by a simple quantum model than a simple classical one), and that the lack of direct evidence is solely due to the difficulty of performing the requisite measurements. Seth replied that, despite the difficulty, D-Wave would "do itself a big favor" by performing the measurements.

Seth also mentioned D-Wave's claims to the popular press -- for example, about the ability of quantum computers to solve NP-complete problems -- as a major factor in its scientific credibility problem. Geordie admitted that some of D-Wave's publicity was (here he paused for a few seconds) "not inaccurate, but verging on inaccurate."

> **Note:** Geordie now says that he was only talking about the _reporting_ on D-Wave; in his words, "I stand by 100% anything I've ever said to anyone about these machines." At the time, I understood him quite clearly to be talking about D-Wave's own publicity; it's strange that he would have hesitated to admit that _reporters_ have misunderstood things. But I freely admit that I might have misheard or misinterpreted him.

I asked Geordie about the [result](http://arxiv.org/abs/0705.1115) of Bansal, Bravyi, and Terhal that the planar Ising spin graph problem admits an efficient classical approximation algorithm -- thus calling into question D-Wave's whole strategy of solving other NP approximation problems by mapping them onto Ising spin graph instances. Geordie replied, first, that their machine can handle many non-planar links, and second, that Bansal et al.'s algorithm merely trades an exponential dependence on n for an exponential dependence on 1/ε. I agreed that their algorithm isn't practical, but argued that its mere existence would have to be dealt with in any attempt to convert approximate solutions of the Ising spin graph problem into approximate solutions of the original optimization problems.

So, where do we stand? Here's my attempt at a fair summary:

  * The people at D-Wave are not conscious frauds; they genuinely believe in what they're doing.


  * On the other hand, much of the publicity surrounding D-Wave can be safely rejected. To some academics, even one or two public misrepresentations are enough to destroy a company's credibility. Others, however, prefer to ignore press releases -- seeing hype, exaggeration, and even outright falsehoods as just a necessary part of raising money -- and to concentrate solely on a company's communications with experts. Where you fall between these extremes probably depends on your personality more than anything else.


  * In the past, I criticized D-Wave (rightly, I think) for failing to share information with the scientific community in a good-faith manner. To their credit, they're now making more of an effort to communicate.


  * Thus far, by Geordie's own account, there's no direct evidence that D-Wave's machine actually produces entanglement at any stage of its operation (which all agree is a non-negotiable requirement for quantum computing). Geordie says that producing such evidence will be the "next thing on the list." The Sudoku stunt was worthless from a scientific perspective; it did not answer any of the questions that physicists need answered.


  * Even if D-Wave managed to build (say) a coherent 1,024-qubit machine satisfying all of its design specs, it's not obvious it would outperform a classical computer on any problem of practical interest. This is true both because of the inherent limitations of the adiabatic algorithm, and because of specific concerns about the Ising spin graph problem. On the other hand, it's also not obvious that such a machine _wouldn 't_ outperform a classical computer on some practical problems. The experiment would be an interesting one! Of course, this uncertainty -- combined with the more immediate uncertainties about whether D-Wave can build such a machine at all, and indeed, about whether they can even produce two-qubit entanglement -- also means that any talk of "lining up customers" is comically premature.


