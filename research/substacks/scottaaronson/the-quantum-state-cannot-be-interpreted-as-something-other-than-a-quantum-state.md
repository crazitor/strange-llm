---
title: "The quantum state cannot be interpreted as something other than a quantum state"
author: "Scott Aaronson"
date: "Sat, 19 Nov 2011"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=822"
---

Lots of people asked me to comment on a much-discussed new preprint by Matthew Pusey, Jonathan Barrett, and Terry Rudolph (henceforth PBR), ["The quantum state cannot be interpreted statistically"](http://arxiv.org/abs/1111.3328). (See [here](http://www.nature.com/news/quantum-theorem-shakes-foundations-1.9392) for an effusive  _Nature News_ article, [here](http://science.slashdot.org/story/11/11/18/1742222/study-says-quantum-wavefunction-is-a-real-physical-object) for the predictable Slashdot confusion-fest, [here](http://blogs.discovermagazine.com/cosmicvariance/2011/11/18/guest-post-david-wallace-on-the-physicality-of-the-quantum-state/) for a related _Cosmic Variance_ guest post by David Wallace, and [here](http://motls.blogspot.com/2011/11/nature-hypes-anti-qm-crackpot-paper-by.html) for a spiteful rant by Lubos Motl that hilariously misunderstands the new result as "anti-quantum-mechanics.")

I recommend reading the preprint if you haven't done so yet; it should only take an hour. PBR's main result reminds me a little of the No-Cloning Theorem: it's a profound triviality, something that most people who thought about quantum mechanics already knew, but probably didn't  _know_ they knew. (Some people are even making comparisons to Bell's Theorem, but to me, the PBR result lacks the same surprise factor.)

To understand the new result, the first question we should ask is, what exactly do PBR  _mean_ by a quantum state being "statistically interpretable"? Strangely, PBR spend barely a paragraph justifying their answer to this central question--but it's easy enough to explain what their answer is. Basically, PBR call something "statistical" if two people, who live in the same universe but have different information, could _rationally disagree_ about it. (They put it differently, but I'm pretty sure that's what they mean.) As for what "rational" means, all we'll need to know is that a rational person can never assign a probability of 0 to something that will actually happen.

To illustrate, suppose a coin is flipped, and you (but not I) get a tip from a reliable source that the coin probably landed heads. Then you and I will describe the coin using different probability distributions, but neither of us will be "wrong" or "irrational", given the information we have.

In quantum mechanics, _mixed states_ --the most general type of state--have exactly the same observer-relative property. That isn't surprising, since mixed states include classical probability distributions as a special case. As I understand it, it's this property of mixed states, more than anything else, that's encouraged many people (especially in and around the Perimeter Institute) to chant slogans like "quantum states are states of knowledge, not states of nature."

By contrast,  _pure_ states--states with perfect quantum coherence--seem intuitively much more "objective." Concretely, suppose I describe a physical system using a pure state |ψ>, and you describe the same system using a different pure state |φ>≠|ψ>. Then it seems obvious that _at least one of us_ has to be flat-out wrong, our confidence misplaced! In other words, at least one of us should've assigned a mixed state rather than a pure state. The PBR result basically formalizes and confirms that intuition.

In the special case that |ψ> and |φ> are _orthogonal_ , the conclusion is obvious: we can just _measure_ the system in a basis containing |ψ> and |φ>. If we see outcome |ψ> then you're "unmasked as irrational", while if we see outcome |φ>, then I'm unmasked as irrational.

So let's try a slightly more interesting, non-orthogonal example. Suppose I describe a system S using the state |0>, while you describe it using the state |+>=(|0>+|1>)/√2. Even then, there are _some_ measurements and outcomes of those measurements that would clearly reveal one of us to have been irrational. If we measure S in the {|0>,|1>} basis and get outcome |1>, then I was irrational. If we measure in the {|+>,|->} basis (where |->=(|0>-|1>)/√2) and get outcome |->, then you were irrational. Furthermore, if S is any qubit that obeys quantum mechanics, then it _must_ have a decent probability either of returning outcome |1> when measured in the {|0>,|1>} basis, _or_ of returning outcome |-> when measured in the {|+>,|->} basis.

So, are we finished? Well, PBR don't discuss the simple argument above, but I assume they wouldn't be satisfied with it. In particular, they'd probably point out that it only unmasks one of us as irrational for _some_ measurement outcomes--but who can say what the measurement outcome will be, especially if we don't presuppose that the quantum state provides a complete description of reality?

What they want instead is a measurement that's guaranteed to unmask someone as irrational, _regardless_ of its outcome. PBR show that this can be obtained, under one further assumption: that "rational beliefs behave well under tensor products." More concretely, suppose two people with different knowledge could rationally describe the same physical system S using different pure states, say |0> or |+> respectively. Then if we consider a new system T, consisting of _two independent copies of S_ , it should be rationally possible to describe T using any of the _four_ states |0>|0>, |0>|+>, |+>|0>, or |+>|+>. But now, PBR point out that there's a 2-qubit orthonormal basis where the first vector is orthogonal to |0>|0>, the second vector is orthogonal to |0>|+>, the third vector is orthogonal to |+>|0>, and the fourth vector is orthogonal to |+>|+>. So, if we measure in _that_ basis, then _someone_ will get unmasked as irrational regardless of the measurement result.

More generally, given any physical system S that you and I describe using different pure states |ψ> and |φ>, PBR define a new system T consisting of k independent copies of S, where k is inversely proportional to the angle between |ψ> and |φ>. They then construct a projective measurement M on T such that, _whichever_ of M's 2k possible outcomes is observed, _one_ of the 2k possible "tensor product beliefs" about T gets unmasked as irrational. And that's it (well, other than a generalization to the noisy case).

So, will this theorem finally end the century-old debate about the "reality" of quantum states--proving, with mathematical certitude, that the "ontic" camp was right and the "epistemic" camp was wrong? To ask this question is to answer it.

(**Clarification added for Lubos Motl and anyone else unwilling or unable to understand:** The answer that I intended was "no." I don't think the battle between the "ontic" and "epistemic" camps can _ever_ be won, by its nature. Nor has that particular battle ever interested me greatly, except insofar as some interesting mathematical results have come out of it.)

I expect that PBR's philosophical opponents are already hard at work on a rebuttal paper: "The quantum state  _can too_ be interpreted statistically", or even "The quantum state _must_ be interpreted statistically."

I expect the rebuttal to say that, yes, _obviously_ two people can't rationally assign different pure states to the same physical system--but only a fool would've ever thought otherwise, and that's not what anyone ever meant by calling quantum states "statistical", and anyway it's beside the point, since pure states are just a degenerate special case of the more fundamental mixed states.

I expect the rebuttal to prove a contrary theorem, using a definition of the word "statistical" that subtly differs from PBRs. I expect the difference between the two definitions to get buried somewhere in the body of the paper.

I expect the rebuttal to get blogged and Slashdotted. I expect the Slashdot entry to get hundreds of comments taking strong sides, not one of which will acknowledge that the entire dispute hinges on the two camps' differing definitions.

There's an important lesson here for mathematicians, theoretical computer scientists, and analytic philosophers. You want the kind of public interest in your work that the physicists enjoy? Then _stop being so goddamned precise with words!_ The taxpayers who fund us--those who pay attention at all, that is--want a riveting show, a grand Einsteinian dispute about what is or isn't real. Who wants some mathematical spoilsport telling them: "Look, it all depends what you mean by 'real.'  _If_ you mean, uniquely determined by the complete state of the universe, and _if_ you're only talking about pure states, then…"

**One final remark.** In their conclusion, PBR write:

… the quantum state has the striking property of being an exponentially complicated object. Specifically, the number of real parameters needed to specify a quantum state is exponential in the number of systems n. This has a consequence for classical simulation of quantum systems. If a simulation is constrained by our assumptions--that is, if it must store in memory a state for a quantum system, with independent preparations assigned uncorrelated states--then it will need an amount of memory which is exponential in the number of quantum systems.

The above statement is certainly true, but it seems to me that it was already demonstrated--and much more convincingly--by (for example) the exponential separations between randomized and quantum communication complexities.
