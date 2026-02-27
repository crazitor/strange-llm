---
title: "My day job"
author: "Scott Aaronson"
date: "Mon, 10 Apr 2006"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=73"
---

You've probably spent days, or even months, wondering why I don't update this blog more often. What could possibly be more important to my career -- besides napping, web surfing, napping again, or watching Jon Stewart?

So it's time to come clean: besides my gig at Shtetl-Optimized, I also have a "day job," most of which is actually performed at night. Greg Kuperberg, who used to be my most regular commenter before he went M.I.A., has a similar "day job." If you don't already know what this day job is, it's a little hard to explain. We barely understand it ourselves. One thing I can say is that it involves the production of documents like the following:

> S. Aaronson and G. Kuperberg, Quantum Versus Classical Proofs and Advice, [quant-ph/0604056](http://www.arxiv.org/abs/quant-ph/0604056).
> 
> This paper studies whether quantum proofs are more powerful than classical proofs, or in complexity terms, whether QMA=QCMA. We prove two results about this question. First, we give a "quantum oracle separation" between QMA and QCMA. More concretely, we show that any quantum algorithm needs Ω(sqrt(2n/(m+1))) queries to find an n-qubit "marked state" |ψ>, even if given an m-bit classical description of |ψ> together with a quantum black box that recognizes |ψ>. We also prove a matching upper bound. Second, we show that, in the one previously-known case where quantum proofs seemed to help, _classical_ proofs are basically just as powerful. In particular, Watrous gave a QMA protocol for verifying non-membership in finite groups. Under plausible group-theoretic assumptions, we give a QCMA protocol for the same problem. Even with no assumptions, our protocol makes only polynomially many queries to the group oracle. Both of our results apply equally to the problem of quantum versus classical _advice_ -- that is, of whether BQP/qpoly equals BQP/poly. We end with some conjectures about quantum versus classical oracles, and about the problem of achieving a _classical_ oracle separation between QMA and QCMA.

Alright, suppose you're King Arthur. Merlin, your staff wizard, claims to have solved a very hard math problem (a "Holy Grail," so to speak) on which your entire kingdom depends. The problem might involve, say, the speed of an African swallow, or the best kind of oil in which to boil heretics -- the details aren't important.

Being suspicious of wizards, you want to check Merlin's solution, but being a king, you don't have much time to do it. You do, however, have a quantum computer at hand (why not?). Here's the question: is there anything Merlin could convince you of by giving you a quantum-mechanical superposition, that he couldn't convince you of by just communicating classically?

QMA, which stands for "Quantum Merlin Arthur," is (basically) the class of problems for which Merlin could feasibly convince you of the answer by giving you a quantum state. QCMA, which stands for "Quantum Classical Merlin Arthur," is the class of problems for which Merlin could feasibly convince you of the answer by just communicating classically. (Some people have suggested changing the acronym to CMQA, for "Classical Merlin Quantum Arthur," since Arthur has the quantum computer while Merlin has to communicate classically.)

The key question is whether QMA and QCMA are equal. So, do Greg and I answer that question in our paper? Of course not -- are you nuts?! All we do is get closer to answering it than anyone before. We do so by giving two new pieces of evidence: one suggesting that QMA and QCMA are equal, and another suggesting that they're not. You might not realize it, but this represents Progress.

To those who aren't "in the business," all of this medieval quantum intrigue might raise a question: why do we bother? Why do we spend months writing papers that (if we're lucky) maybe a hundred people will ever be aware of, and ten will ever understand? Well, Greg can answer for himself. As for me, I've always liked the answer once given by Bertrand Russell. And no, this isn't my "serious" or "official" answer (nor was it Bertie's), but it's a fine response to anyone who has to ask.

> …a word of advice to such of my hearers as may happen to be professors. I am allowed to use plain English because everybody knows that I could use mathematical logic if I chose. Take the statement: "Some people marry their deceased wives' sisters." I can express this in language which only becomes intelligible after years of study, and this gives me freedom. I suggest to young professors that their first work should be written in a jargon only to be understood by the erudite few. With that behind them, they can ever after say what they have to say in a language "understanded of the people."
