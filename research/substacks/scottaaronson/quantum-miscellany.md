---
title: "Quantum miscellany"
author: "Scott Aaronson"
date: "Tue, 19 Sep 2023"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=7516"
---

  1. Tomorrow at 1:30pm US Central time, I'll be doing an online Q&A with [Collective[i] Forecast](https://www.ciforecast.com/) about quantum computing (probably there will also be questions about AI safety). It's open to all. Hope to see some of you there!  

  2. Toby Cubitt of University College London is visiting UT Austin. We've been discussing the question: can you produce a [QMA](https://en.wikipedia.org/wiki/QMA) witness state using a closed timelike curve? Since QMA⊆PSPACE, and since Fortnow, Watrous, and I [proved that](https://arxiv.org/abs/0808.2669) closed timelike curves (or anyway, Deutsch's model of them) let you solve PSPACE problems, clearly a closed timelike curve lets you solve QMA _decision_ problems, but that's different from producing the actual witness state as the fixed-point of a polynomial-time superoperator. Toby has a [neat recent result](https://arxiv.org/abs/2303.11962), which has as a corollary that you can produce the ground state of a local Hamiltonian using a CTC, _if_ you have as auxiliary information the ground state energy as well as (a lower bound on) the spectral gap. But you do seem to need that extra information.  
  
Yesterday I realized there's also a simpler construction: namely, take an n-qubit state from the CTC, and check whether it's a valid QMA witness, having used [Marriott-Watrous amplification](https://arxiv.org/abs/cs/0506068) to push the probability of error down to (say) exp(-n2). If the witness is valid, then send it back in time unmodified; otherwise replace it by the maximally mixed state. If valid witnesses exist, then you can check that this sets up a Markov chain whose stationary distribution is almost entirely concentrated on such witnesses. (If no valid witnesses exist, then the stationary distribution is just the maximally mixed state, or exponentially close to it.) One drawback of this construction is that it can only produce a Marriott-Watrous state, rather than the "original" QMA witness state.  
  
Is there a third approach, which overcomes the disadvantages of both mine and Toby's? I'll leave that question to my readers!  

  3. On the theme of QMA plus weird physics, a wonderful question emerged from a recent group meeting: namely, what's the power of QMA if we let the verifier make multiple non-collapsing measurements of the same state, as in the ["PDQP" model](https://arxiv.org/abs/1412.6507) defined by myself, Bouland, Fitzsimons, and Lee? I conjecture that this enhanced QMA goes all the way up to NEXP (Nondeterministic Exponential-Time), by a construction related to the one I used to [show](https://arxiv.org/abs/1805.08577) that PDQP/qpoly = ALL (i.e., non-collapsing measurements combined with quantum advice lets you decide literally all languages), and that also uses the PCP Theorem. I even have some candidate constructions, though I haven't yet proven their soundness.  
  
In the past, I would've spent more time on such a problem before sharing it. But after giving some students a first crack, I now … just want to know the answer? Inspecting my feelings in my second year of leave at OpenAI, I realized that I still care enormously about quantum complexity theory, but only about getting answers to the questions, barely at all anymore about getting credit for them. Admittedly, it took me 25 years to reach this state of not caring.


