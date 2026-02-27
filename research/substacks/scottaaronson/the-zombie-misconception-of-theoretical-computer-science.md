---
title: "The Zombie Misconception of Theoretical Computer Science"
author: "Scott Aaronson"
date: "Mon, 08 Jul 2024"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=8106"
---

In Michael Sipser's [_Introduction to the Theory of Computation_ textbook](https://www.amazon.com/Introduction-Theory-Computation-Michael-Sipser/dp/113318779X), he has one Platonically perfect homework exercise, so perfect that I can reconstruct it from memory despite not having opened the book for over a decade. It goes like this:

  * Let f:{0,1}*→{0,1} be the constant 1 function if God exists, or the constant 0 function if God does not exist. Is f computable? (_Hint:_ The answer does not depend on your religious beliefs.)



The correct answer is that yes, f is computable. Why? Because the constant 1 function is computable, and so is the constant 0 function, so if f is one or the other, then it's computable.

If you're still tempted to quibble, then consider the following parallel question:

  * Let n equal 3 if God exists, or 5 if God does not exist. Is n prime?



The answer is again yes: even though n hasn't been completely mathematically specified, it's been specified _enough_ for us to say that it's prime (just like if we'd said, "n is an element of the set {3,5}; is n prime?"). Similarly, f has been specified enough for us to say that it's computable.

The deeper lesson Sipser was trying to impart is that the concept of [computability](https://en.wikipedia.org/wiki/Computable_function) applies to _functions_ or _infinite sequences_ , not to individual yes-or-no questions or individual integers. Relatedly, and even more to the point: computability is about whether a computer program _exists_ to map inputs to outputs in a specified way; it says nothing about how hard it might be to _choose_ or _find_ or _write_ that program. Writing the program could even require settling God's existence, for all the definition of computability cares.

* * *

Dozens of times in the past 25 years, I've gotten some variant on the following question, always with the air that I'm about to bowled over by its brilliance:

  * Could the P versus NP question _itself_ be NP-hard, and therefore impossible to solve?



Every time I get this one, I struggle to unpack the layers of misconceptions. But for starters: the concept of ["NP-hard"](https://en.wikipedia.org/wiki/NP-hardness) applies to _functions_ or _languages_ , like 3SAT or Independent Set or Clique or whatnot, all of which _take an input_ (a Boolean formula, a graph, etc) and produce a corresponding output. NP-hardness means that, if you had a polynomial-time algorithm to map the inputs to the outputs, then you could convert it via reductions into a polynomial-time algorithm for any language or function in the class NP.

[P versus NP](https://www.scottaaronson.com/papers/pnp.pdf), by contrast, is an individual yes-or-no question. Its answer (for all we know) could be independent of the [Zermelo-Fraenkel axioms](https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory) of set theory, but there's no sense in which the question could be uncomputable or NP-hard. Indeed, a fast program that correctly answers the P vs. NP question trivially exists:

  * If P=NP, then the program prints "P=NP."
  * If P≠NP, then the program prints "P≠NP."



* * *

In the comments of [last week's post](https://scottaaronson.blog/?p=8088) on the breakthrough determination of Busy Beaver 5, I got several variants on the following question:

  * What's the smallest n for which the value of BB(n) is uncomputable? Could BB(6) already be uncomputable?



Once again, I explained that the Busy Beaver _function_ is uncomputable, but the concept of computability doesn't apply to individual integers like BB(6). Indeed, whichever integer k turns out to equal BB(6), the program "print k" clearly exists, and it clearly outputs that integer!

Again, we can ask for the smallest n such that the value of BB(n) is _unprovable in ZF set theory_ (or some other system of axioms)--precisely the question that Adam Yedidia and I [did ask in 2016](https://arxiv.org/abs/1605.04343) (the current record stands at n=745, improving my and Adam's n=8000). But _every_ specific integer is "computable"; it's only the BB function _as a whole_ that's uncomputable.

Alas, in return for explaining this, I got more pushback, and even ridicule and abuse that I chose to leave in the moderation queue.

* * *

So, I've come to think of this as the Zombie Misconception of Theoretical Computer Science: this constant misapplication of concepts that were designed for infinite sequences and functions, to individual integers and open problems. (Or, relatedly: the constant conflation of the uncomputability of the halting problem with Gödel incompleteness. While they're closely related, only Gödel lets you talk about _individual_ statements rather than infinite families of statements, and only Turing-computability is absolute, rather than relative to a system of axioms.)

Anyway, I'm writing this post mostly just so that I have a place to link the _next_ time this pedagogical zombie rises from its grave, muttering "UNCOMPUTABLE INTEGERRRRRRS…." But also so I can query my readers: what are _your_ ideas for how to keep this zombie down?
