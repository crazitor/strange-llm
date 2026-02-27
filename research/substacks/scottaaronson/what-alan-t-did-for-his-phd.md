---
title: "What Alan T. did for his PhD"
author: "Scott Aaronson"
date: "Tue, 28 Jun 2011"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=697"
---

We've all been there before: by the time you start graduate school in Princeton, you've already invented the Turing machine, pioneered the concept of computational universality, and proved the unsolvability of Hilbert's _Entscheidungsproblem_. A few years from now, you're going to return to England to make decisive contributions to the breaking of the Enigma and the winning of World War II. Your problem is, what do you do for the couple years in between? (Keep in mind that you have a _PhD thesis_ to submit, and the Turing machine is already old hat by now!)

The answer, apparently, is to tackle a neat problem in logic, one version of which was [asked three weeks ago](https://scottaaronson.blog/?p=663#comment-24470) by a _Shtetl-Optimized_ commenter named Schulz. Not knowing the answer, I [posted Schulz's problem to MathOverflow](http://mathoverflow.net/questions/67214/pi1-sentence-independent-of-zf-zfconzf-zfconzfconzfconzf-etc). There, François Dorais and Philip Welch quickly informed me that Turing had already studied the problem in 1939, and Timothy Chow pointed me to Torkel Franzen's book [Inexhaustability: A Non-Exhaustive Treatment](http://www.amazon.com/Inexhaustibility-Non-Exhaustive-Treatment-Lecture-Notes/dp/1568811756), which explains Turing's basic observation and the background leading up to it in a crystal-clear way.

The problem is this: given any formal system F that we might want to take as a foundation for mathematics (for example, Peano Arithmetic or Zermelo-Fraenkel set theory), Gödel tells us that there are Turing machines that run forever, but that can't be _proved_ to run forever in F. An example is a Turing machine M that enumerates all the proofs in F one by one, and that halts if it ever encounters a proof of 0=1. The claim that M doesn't halt is equivalent to the claim that F is consistent--but if F is indeed consistent, then the Second Incompleteness Theorem says that it can't prove its own consistency.

On the other hand, if we just add the reasonable axiom Con(F) (which _asserts_ that F is consistent), then our new theory, F+Con(F), _can_ prove that M runs forever. Of course, we can then construct a new Turing machine M', which runs forever if and only if _F+Con(F)_ is consistent. Then by the same argument, F+Con(F) won't be able to prove that M' runs forever: to prove that, we'll need a yet stronger theory, F+Con(F)+Con(F+Con(F)). This leads inevitably to considering an infinite tower of theories F0, F1, F2, …, where each theory asserts the consistency of the ones before it:

F0 = F

Fi = Fi-1 \+ Con(Fi-1) for all i≥1

But there's no reason not to go further, and define another theory that asserts the consistency of _every_ theory in the above list, and then another theory that asserts the consistency of _that_ theory, and so on. We can formalize this using ordinals:

Fω = F + Con(F0) + Con(F1) + Con(F2) + …

Fω+i = Fω+i-1 \+ Con(Fω+i-1) for all i≥1

F2ω = Fω \+ Con(Fω) + Con(Fω+1) + Con(Fω+2) + …

and so on, for every ordinal α that we can define in the language of F. For every such ordinal α, we can easily construct a Turing machine Mα that runs forever, but that can't be _proved_ to run forever in Fα (only in the later theories). The interesting question is, _what happens if we reverse the quantifiers?_ In other words:

**Given a Turing machine M that runs forever, is there always an ordinal α such that F α proves that M runs forever?**

This is the question Turing studied, but I should warn you that his answer is disappointing. It turns out that the theories Fα are not as well-defined as they look. The trouble is that, even to _define_ a theory with infinitely many axioms (like Fω or F2ω), you need to encode the axioms in some systematic way: for example, by giving a Turing machine that spits out the axioms one by one. But Turing observes that the power of Fα can depend strongly on _which_ Turing machine you use to spit out its axioms! Indeed, he proves the following theorem:

**Given any Turing machine M that runs forever, there is some "version" of Fω+1 (i.e., some way of encoding its axioms) such that Fω+1 proves that M runs forever.**

The proof is simple. Assume for simplicity that F itself has only finitely many axioms (removing that assumption is straightforward). Then consider the following Turing machine P for outputting the axioms of Fω, which gives rise to a "version" of Fω that we'll call FP:

Output the axioms of F

For t=0,1,2,…

If M halts in t steps or fewer, then output "Con(FP)"; otherwise output "Con(Ft)"

Next t

You might notice that our description of P involves the very theory FP that we're defining! What lets us get away with this circularity is the [Recursion Theorem](http://en.wikipedia.org/wiki/Kleene%27s_recursion_theorem), which says (informally) that when writing a program, we can always assume that the program has access to its own code.

Notice that, if P ever output the axiom "Con(FP)", then FP would assert its own consistency, and would therefore be _in_ consistent, by the Second Incompleteness Theorem. But by construction, P outputs "Con(FP)" if and only if M halts. Therefore, if we assume FP's consistency as an axiom, then we can easily deduce that M _doesn 't_ halt. It follows that the theory Fω+1 := FP \+ Con(FP) proves that M runs forever.

One question that the above argument leaves open is whether there's a Turing machine M that runs forever, as well as a system S of ordinal notations "extending as far as possible", such that _if_ we use S to define the theories Fα, _then_ none of the Fα's prove that M runs forever. If so, then there would be a clear sense in which iterated consistency axioms, by themselves, do _not_ suffice to solve the halting problem. Alas, I fear the answer might depend on exactly how we interpret the phrase "extending as far as possible" … elucidation welcome!

**Update (June 29, 2011):** In a comment, François Dorais comes to the rescue once again:

In connection with your last paragraph, Feferman has shown that there are paths through O such that the resulting theory proves all true ∏01 statements. [JSL 27 (1962), 259-316] Immediately after Feferman and Spector showed that not all paths through O do this. [JSL 27 (1962), 383-390] In particular, they show that any good path must be more complicated than O itself: the path cannot be ∏11. In other words, there is no simple way to form a wellordered iterated consistency extension that captures all true ∏01 statements.
