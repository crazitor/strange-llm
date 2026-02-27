---
title: "A complexity theorist’s (non)apology"
author: "Scott Aaronson"
date: "Wed, 21 Feb 2007"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=206"
---

Several respected physicists wrote to me privately to say how disappointed they were that Umesh and I would fight shoddy journalism by making a shoddy claim of our own: namely, that the inability of quantum computers to solve NP-complete problems efficiently is an established fact. I took a lot of flak in the comments section over the same issue.

Ladies and gentlemen of the jury, I will answer the unjust charges being leveled against me and my advisor.

But first, let's review the facts. As I've said in pretty much every introductory talk I've ever given, _obviously_ we can't yet hope to prove that NP-complete problems are hard for quantum computers, since we haven't even proved they're hard for _classical_ computers! (Nor, for that matter, do we have any idea how to prove that _if_ they're hard for classical computers then they're also hard for quantum computers.) These are some of the most profound open problems in mathematics. Solving them could easily take decades or centuries.

I dare say that Umesh and I know this as well as anyone on Earth. And that's why, even while trying in the space of a few sentences to correct a breathtaking misconception about the nature of the physical world that was being endlessly repeated to millions of people, we _still_ took care in what we said.

Here's Umesh:

> Most egregious is your assertion that quantum computers can solve NP-complete problems in "one shot" by exploring exponentially many solutions at once. This mistaken view was put to rest in the infancy of quantum computation over a decade ago … For unstructured search problems like the NP-complete problems this means that there is no exponential speed up but rather at most a quadratic speed up.

In the above passage, Umesh is talking about an [epochal theorem](http://www.cs.berkeley.edu/~vazirani/pubs/bbbv.ps) that he and others _did_ manage to prove: namely, that quantum computers could not solve NP-complete problems by any "one-shot" method based on exploring exponentially many solutions in parallel. Throw away the structure of an NP-complete problem -- consider it just as an abstract space of 2n solutions -- and we _know_ that quantum computers will give you at most a quadratic speedup over classical ones.

In the thirteen years since this "BBBV theorem" was proved, two interesting things happened:

  1. Various experts dismissed the theorem as irrelevant, knocking down a straw man, stacking the deck in favor of its conclusion by imposing an utterly-unjustified "black-box" assumption, etc.
  2. Hundreds of articles appeared, in both the popular press and the arXiv, that directly contradicted the theorem.



It reminds me of how theologians chide Richard Dawkins for refuting only a crude, anthropomorphic, straw-man god instead of a sophisticated Einsteinian one, and then (with an air of self-satisfaction) go off and pray to the crude god.

To be fair, we do have _one_ quantum algorithm for NP-complete problems that falls outside the scope of the BBBV theorem: namely, the adiabatic algorithm of [Farhi et al.](http://www.arxiv.org/abs/quant-ph/0001106) This algorithm can be seen as a quantum version of simulated annealing. Intriguingly, [Farhi, Goldstone, and Gutmann](http://www.arxiv.org/abs/quant-ph/0201031) gave examples where simulated annealing gets stuck at local optima, whereas the adiabatic algorithm tunnels through to the global optimum. On the other hand, [van Dam, Mosca, and Vazirani](http://www.arxiv.org/abs/quant-ph/0206003) gave other examples where the adiabatic algorithm _also_ gets stuck at local optima, taking exponential time to reach a global optimum.

The upshot is that, if a fast quantum algorithm for NP-complete problems existed, then just like a fast _classical_ algorithm, it would have to be radically different from anything that's yet been imagined. Because of this -- not to mention the [civilization-changing consequences](http://www.scottaaronson.com/papers/npcomplete.pdf) that such an algorithm would have -- Umesh and I feel strongly that claims to solve NP-complete problems should never be bandied about lightly. As with perpetual-motion machines or antigravity shields, the burden of proof lies entirely with the would-be inventor. "In case of fire, break glass." "In case of algorithm, break skepticism."

It might be objected that, while the _experts_ know that this is what Umesh meant, laypeople could easily misinterpret his words -- or in other words, that Umesh has pulled a D-Wave of his own. But here's the crucial difference. Any motivated reader who wanted the real story behind Umesh's three-sentence caricature could _find_ that story in peer-reviewed articles only a Google search away. But with D-Wave, all they'd have to go on is the PR. Simplifying mathematical subtleties is a right you have to earn, by having the cards in case anyone calls your bluff.

So much for Umesh's letter. Now let's look at mine:

> Today it is accepted that quantum computers could not solve NP-complete problems in a reasonable amount of time. Indeed, the view of quantum computers as able to “try all possible solutions in parallel,” and then instantly choose the correct one, is fundamentally mistaken.

Notice I didn't say it was _proved_ that quantum computers can't solve NP-complete problems in reasonable time: I said it was _accepted_. This, I felt, was a difference few people would have trouble understanding. As an example, if biologists said it was _accepted_ that the Loch Ness monster doesn't exist, presumably no one would interpret that as meaning they'd actually _proved_ its nonexistence. Indeed, the interesting difference between the two cases is that someday, it _might_ actually be possible to prove the nonexistence of the fast quantum algorithm.

Or are we complexity theorists being too dogmatic? Should we concede to a certain subset of our physicist friends that, until an actual proof has been discovered, we have no basis even to _guess_ whether P versus NP or NP versus BQP will go one way or the other way? Should we, in other words, hold ourselves to the same lofty standards of uncompromising mathematical rigor that the physicists themselves have always adhered to?

Oh -- pardon me. I had momentarily forgotten that we were talking about the headmasters of handwaving, the sultans of sloppiness, the princes of proof-by-example. Indeed, I think it's fair to say that if physicists had discovered the P versus NP question, they would have _immediately_ declared that P≠NP -- and they would have hailed this 'discovery' of theirs as another remarkable success for physics as a discipline. And everyone else -- from other scientists to programmers to journalists to the general public -- would have gone right along with it. The task of _proving_ P≠NP would have been left as a technical detail, to be filled in by the mathematical hairsplitters -- just like the task of proving quark confinement, or the ergodicity of particles in a box, or the existence of Yang-Mills theory, or the perturbative finiteness of string theory.

Clearly, the issue here can't be the intelligence of physicists, some of whom actually seem reasonably smart. The issue, rather, is their different standard -- much closer to the standard of everyday life -- for saying that they know something is true. My favorite example in this vein comes from Leonid Levin, who tells me he couldn't convince Richard Feynman that P versus NP was an open problem at all.

I believe Feynman was onto something, in that _the only reason P versus NP is called an "open problem_" is that we -- the theoretical computer scientists and mathematicians -- hold ourselves to a different standard of rigor than any other scientists. Were we less cautious, we could easily talk about the hardness of NP-complete problems as one of our great _discoveries_ , a discovery for which working out the mathematical underpinnings admittedly remains as a challenge for future generations.

Ironically, our higher standard of rigor often gets _turned against us_ , when outsiders use it to argue that we're just guessing, or building castles in the sky, or making conjectures that could all turn out to be wrong. The same charges could obviously be leveled against the central hypotheses of physics or economics or pretty much any other field, but they rarely are -- at least not by the same people.

I'm tired of double standards, is all I'm saying.
