---
title: "What Google Won’t Find"
author: "Scott Aaronson"
date: "Fri, 31 Aug 2007"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=266"
---

While I rummage around the brain for something more controversial to blog (that's nevertheless not [too](https://scottaaronson.blog/?p=260) controversial), here, for your reading pleasure, is a talk I gave a couple weeks ago at Google Cambridge. Hardcore _Shtetl-Optimized_ fans will find little here to surprise them, but for new or occasional readers, this is about the clearest statement I've written of my religio-ethico-complexity-theoretic beliefs.

**What Google Won 't Find**

As I probably mentioned when I spoke at your Mountain View location two years ago, it's a funny feeling when an entity that knows everything that ever can be known or has been known or will be known invites you to give a talk -- what are you supposed to say?

Well, I thought I'd talk about "What Google Won't Find." In other words, what have we learned over the last 15 years or so about the ultimate physical limits of search -- whether it's search of a physical database like Google's, or of the more abstract space of solutions to a combinatorial problem?

On the spectrum of computer science, I'm about as theoretical as you can get. One way to put it is that I got through CS grad school at Berkeley without really learning any programming language other than QBASIC. So it might surprise you that earlier this year, I was spending much of my time talking to _business_ reporters. Why? Because there was this company near Vancouver called D-Wave Systems, which was announcing to the press that it had built the world's first commercial quantum computer.

Let's ignore the "commercial" part, because I don't really understand economics -- these days, you can apparently make billions of dollars giving away some service for free! Let's instead focus on the question: did D-Wave _actually_ build a quantum computer? Well, they apparently built a device with 16 very noisy superconducting quantum bits (or qubits), which they say they've used to help solve extremely small Sudoku puzzles.

The trouble is, we've known for years that if qubits are sufficiently noisy -- if they leak a sufficient amount of information into their environment -- then they behave essentially like classical bits. Furthermore, D-Wave has refused to answer extremely basic technical questions about how high their noise rates are and so forth -- they care about serving their customers, not answering nosy questions from academics. (Recently D-Wave founder Geordie Rose [offered](http://www.walrusmagazine.ca/articles/2007.08.10-quantum-conundrum/#155) to answer my questions if I was interested in buying one of his machines. I replied that I _was_ interested -- my offer was $10 US -- and I now await his answers as a prospective customer.)

To make a long story short, it's consistent with the evidence that what D-Wave actually built would best be described as a 16-bit _classical_ computer. I don't mean 16 bits in terms of the architecture; I mean sixteen actual bits. And there's some prior art for that.

But that's actually not what annoyed me the most about the D-Wave announcement. What annoyed me were all the articles in the popular press -- including places as reputable as _The Economist_ -- that said, what D-Wave has built is a machine that can try every possible solution in parallel and instantly pick the right one. This is what a quantum computer is; this is how it works.

It's amazing to me how, as soon as the word "quantum" is mentioned, all the ordinary rules of journalism go out the window. No one thinks to ask: is that _really_ what a quantum computer could do?

It turns out that, even though we don't yet have scalable quantum computers, we do know something about what they could do if we _did_ have them.

A quantum computer is a device that would exploit the laws of quantum mechanics to solve certain computational problems asymptotically faster than we know how to solve them with any computer today. Quantum mechanics -- which has been our basic framework for physics for the last 80 years -- is a theory that's like probability theory, except that instead of real numbers called probabilities, you now have complex numbers called amplitudes. And the interesting thing about these complex numbers is that they can "interfere" with each other: they can cancel each other out.

In particular, to find the probability of something happening, you have to add the amplitudes for all the possible ways it _could_ have happened, and then take the square of the absolute value of the result. And if some of the ways an event could happen have positive amplitude and others have negative amplitude, then the amplitudes can cancel out, so that the event _doesn 't happen at all_. This is exactly what's going on in the famous double-slit experiment: at certain spots on a screen, the different paths a photon could've taken to get to that spot interfere destructively and cancel each other out, and as a result no photon is seen.

Now, the idea of quantum computing is to set up a _massive_ double-slit experiment with exponentially many paths -- and to try to arrange things so that the paths leading to wrong answers interfere destructively and cancel each other out, while the paths leading to right answers interfere _constructively_ and are therefore observed with high probability.

You can see it's a subtle effect that we're aiming for. And indeed, it's only for a few specific problems that people have figured out how to choreograph an interference pattern to solve the problem efficiently -- that is, in polynomial time.

One of these problems happens to be that of factoring integers. Thirteen years ago, Peter Shor discovered that a quantum computer could efficient apply Fourier transforms over exponentially-large abelian groups, and thereby find the periods of exponentially-long periodic sequences, and thereby factor integers, and thereby break the RSA cryptosystem, and thereby snarf people's credit card numbers. So that's one application of quantum computers.

On the other hand -- and this is the most common misconception about quantum computing I've encountered -- we do not, repeat **do not** , know a quantum algorithm to solve NP-complete problems in polynomial time. For "generic" problems of finding a needle in a haystack, most of us believe that quantum computers will give at most a polynomial advantage over classical ones.

At this point I should step back. How many of you have heard of the following question: **Does P=NP?**

Yeah, this is a problem so profound that it's appeared on at least two TV shows (_The Simpsons_ and _NUMB3RS_). It's also one of the seven (now six) problems for which the Clay Math Institute is offerring a million-dollar prize for a solution.

Apparently the mathematicians had to debate whether P vs. NP was "deep" enough to include in their list. Personally, I take it as obvious that it's the deepest of them all. And the reason is this: if you had a fast algorithm for solving NP-complete problems, then not only could you solve P vs. NP, _you could presumably also solve the other six problems_. You'd simply program your computer to search through all possible proofs of at most (say) a billion symbols, in some formal system like Zermelo-Fraenkel set theory. If such a proof existed, you'd find it in a reasonable amount of time. (And if the proof had more than a billion symbols, it's not clear you'd even want to see it!)

This raises an important point: many people -- even computer scientists -- don't appreciate just how profound the consequences would be if P=NP. They think it's about scheduling airline flights better, or packing more boxes in your truck. Of course, it _is_ about those things -- but the point is that you can have a set of boxes such that _if_ you could pack them into your truck, then you would also have proved the Riemann Hypothesis!

Of course, while the proof eludes us, we believe that P≠NP. We believe there's no algorithm to solve NP-complete problems in deterministic polynomial time. But personally, I would actually make a stronger conjecture:

> **There is _no_ physical means to solve NP-complete problems in polynomial time -- not with classical computers, not with quantum computers, not with anything else.**

You could call this the "No SuperSearch Principle." It says that, if you're going to find a needle in a haystack, then you've got to expend at least _some_ computational effort sifting through the hay.

I see this principle as analogous to the Second Law of Thermodynamics or the impossibility of superluminal signalling. That is, it's a technological limitation which is _also_ a pretty fundamental fact about the laws of physics. Like those other principles, it could always be falsified by experiment, but after a while it seems manifestly more useful to _assume_ it's true and then see what the consequences are for other things.

OK, so what do we actually _know_ about the ability of quantum computers to solve NP-complete problems efficiently? Well, of course we can't _prove_ it's impossible, since we can't even prove it's impossible for classical computers -- that's the P vs. NP problem! We might hope to at least prove that quantum computers can't solve NP-complete problems in polynomial time _unless classical computers can also_ -- but even that, alas, seems far beyond our ability to prove.

What we _can_ prove is this: suppose you throw away the structure of an NP-complete problem, and just consider it as an abstract, featureless space of 2n possible solutions, where the only thing you can do is guess a solution and check whether it's right or not. In that case it's obvious that a classical computer will need ~2n steps to find a solution. But what if you used a quantum computer, which could "guess" all possible solutions in superposition? Well, even then, you'd still need at least ~2n/2 steps to find a solution. This is called the BBBV Theorem, and was one of the first things learned about the power of quantum computers.

Intuitively, even though a quantum computer in some sense involves exponentially many paths or "parallel universes," the single universe that happened on the answer can't shout above all the other universes: "hey, over here!" It can only gradually make the others aware of its presence.

As it turns out, the 2n/2 bound is actually achievable. For in 1996, Lov Grover showed that a quantum computer _can_ search a list of N items using only √N steps. It seems to me that this result should clearly feature in Google's business plan.

Of course in real life, NP-complete problems _do_ have structure, and algorithms like local search and backtrack search exploit that structure. Because of this, the BBBV theorem can't _rule out_ a fast quantum algorithm for NP-complete problems. It merely shows that, _if_ such an algorithm existed, then it couldn't work the way 99% of everyone who's ever heard of quantum computing thinks it would!

You might wonder whether there's any proposal for a quantum algorithm that _would_ exploit the structure of NP-complete problems. As it turns out, there's one such proposal: the "quantum adiabatic algorithm" of Farhi et al., which can be seen as the quantum version of simulated annealing. Intriguingly, Farhi and his collaborators proved that, on _some_ problem instances where classical simulated annealing would take exponential time, the quantum adiabatic algorithm takes only polynomial time. Alas, we _also_ know of problem instances where the adiabatic algorithm takes exponential time just as simulated annealing does. So while this is still an active research area, right now the adiabatic algorithm does _not_ look like a magic bullet for solving NP-complete problems.

If quantum computers can't solve NP-complete problems in polynomial time, it raises an extremely interesting question: is there _any_ physical means to solve NP-complete problems in polynomial time?

Well, there have been lots of proposals. One of my favorites involves taking two glass plates with pegs between them, and dipping the resulting contraption into a tub of soapy water. The idea is that the soap bubbles that form between the pegs should trace out the minimum Steiner tree -- that is, the minimum total length of line segments connecting the pegs, where the segments can meet at points other than the pegs themselves. Now, this is known to be an NP-hard optimization problem. So, it looks like Nature is solving NP-hard problems in polynomial time!

You might say there's an obvious difficulty: the soap bubbles could get trapped in a local optimum that's different from the global optimum. By analogy, a rock in a mountain crevice could reach a lower state of potential energy by rolling up first and then down … but is rarely observed to do so!

And if you said that, you'd be absolutely right. But that didn't stop two guys a few years ago from writing a [paper](http://www.arxiv.org/abs/cs/0406056) in which they claimed, not only that soap bubbles solve NP-complete problems in polynomial time, but that that fact proves P=NP! In debates about this paper on newsgroups, several posters raised the duh-obvious point that soap bubbles can get trapped at local optima. But then another poster opined that that's just an academic "party line," and that he'd be willing to bet that no one had actually done an experiment to prove it.

Long story short, I went to the hardware store, bought some [glass plates](http://www.scottaaronson.com/soapbubble.jpg), liquid soap, etc., and found that, while Nature _does_ often find a minimum Steiner tree with 4 or 5 pegs, it tends to get stuck at local optima with larger numbers of pegs. Indeed, often the soap bubbles settle down to a configuration which is not even a tree (i.e. contains "cycles of soap"), and thus provably can't be optimal.

The situation is similar for protein folding. Again, people have said that Nature seems to be solving an NP-hard optimization problem in every cell of your body, by letting the proteins fold into their minimum-energy configurations. But there are two problems with this claim. The first problem is that proteins, just like soap bubbles, sometimes get stuck in suboptimal configurations -- indeed, it's believed that's exactly what happens with Mad Cow Disease. The second problem is that, to the extent that proteins _do_ usually fold into their optimal configurations, there's an obvious reason why they would: natural selection! If there were a protein that could only be folded by proving the Riemann Hypothesis, the gene that coded for it would quickly get weeded out of the gene pool.

So: quantum computers, soap bubbles, proteins … if we want to solve NP-complete problems in polynomial time in the physical world, what's left? Well, we can try going to more exotic physics. For example, since we don't yet have a quantum theory of gravity, people have felt free to speculate that if we _did_ have one, it would give us an efficient way to solve NP-complete problems. For example, maybe the theory would allow closed timelike curves, which would let us solve NP-complete and even harder problems by (in some sense) sending the answer back in time to before we started.

In my view, though, it's more likely that a quantum theory of gravity will do the exact opposite: that is, it will _limit_ our computational powers, relative to what they would've been in a universe without gravity. To see why, consider one of the oldest "extravagant" computing proposals: the Zeno computer. This is a computer that runs the first step of a program in one second, the second step in half a second, the third step in a quarter second, the fourth step in an eighth second, and so on, so that after two seconds it's run infinitely many steps. (It reminds me of the old joke about the supercomputer that was so fast, it could do an infinite loop in 2.5 seconds.)

> **Question from the floor:** In what sense is this even a "proposal"?
> 
> **Answer:** Well, it's a proposal in the sense that people actually write papers about it! (Google "[hypercomputation](http://www.google.com/search?q=hypercomputation).") Whether they _should_ be writing those papers a separate question…

Now, the Zeno computer strikes most computer scientists -- me included -- as a joke. But _why_ is it a joke? Can we say anything better than that it feels absurd to us?

As it turns out, this question takes us straight into some of the frontier issues in theoretical physics. In particular, one of the few things physicists think they know about quantum gravity -- one of the few things both the string theorists and their critics largely agree on -- is that, at the so-called "Planck scale" of about 10-33 centimeters or 10-43 seconds, our usual notions of space and time are going to break down. As one manifestation of this, if you tried to build a clock that ticked more than about 1043 times per second, that clock would use so much energy that it would collapse to a black hole. Ditto for a computer that performed more than about 1043 operations per second, or for a hard disk that stored more than about 1069 bits per square meter of surface area. (Together with the finiteness of the speed of light and the exponential expansion of the universe, this implies that, contrary to what you might have thought, there _is_ a fundamental physical limit on how much disk space Gmail will ever be able to offer its subscribers…)

To summarize: while I believe what I called the "No SuperSearch Principle" -- that is, while I believe there are fundamental physical limits to efficient computer search -- I hope I've convinced you that understanding _why_ these limits exist takes us straight into some of the deepest issues in math and physics. To me that's so much the better -- since it suggests that not only are the limits _correct_ , but (more importantly) they're also nontrivial.

Thank you.
