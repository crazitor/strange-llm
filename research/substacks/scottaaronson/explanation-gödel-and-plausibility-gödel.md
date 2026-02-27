---
title: "Explanation-Gödel and Plausibility-Gödel"
author: "Scott Aaronson"
date: "Wed, 12 Oct 2022"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=6754"
---

Here's an observation that's mathematically trivial but might not be widely appreciated. In kindergarten, we all learned Gödel's First [Incompleteness Theorem](https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems), which given a formal system F, constructs an arithmetical encoding of

G(F) = "This sentence is not provable in F."

If G(F) is true, then it's an example of a true arithmetical sentence that's unprovable in F. If, on the other hand, G(F) is false, then it's provable, which means that F isn't arithmetically sound. Therefore F is either incomplete or unsound.

Many have objected: "but despite Gödel's Theorem, it's still easy to _explain_ why G(F) is true. In fact, the argument above basically already did it!”

[Note: Please stop leaving comments explaining to me that G(F) follows from F’s consistency. I understand that: the “heuristic” part of the argument _is_ F’s consistency! I made a pedagogical choice to elide that, which nerd-sniping has now rendered untenable.]

You might make a more general point: there are many, many mathematical statements for which we currently lack a proof, but we do seem to have a fully convincing heuristic explanation: one that "proves the statement to physics standards of rigor." For example:

  * The [Twin Primes Conjecture](https://en.wikipedia.org/wiki/Twin_prime) (there are infinitely many primes p for which p+2 is also prime). 
  * The [Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture) (the iterative process that maps each positive integer n to n/2 if n is even, or to 3n+1 if n is odd, eventually reaches 1 regardless of which n you start at). 
  * π is a [normal number](https://en.wikipedia.org/wiki/Normal_number) (or even just: the digits 0-9 all occur with equal limiting frequencies in the decimal expansion of π).
  * [π+e](https://math.stackexchange.com/questions/159350/why-is-it-hard-to-prove-whether-pie-is-an-irrational-number) is irrational.



And so on. No one has any idea how to prove any of the above statements--and yet, just on statistical grounds, it seems clear that it would require a ludicrous conspiracy to make any of them false.

Conversely, one could argue that there are statements for which we _do_ have a proof, even though we lack a "convincing explanation" for the statements' truth. Maybe the [Four-Color Theorem](https://en.wikipedia.org/wiki/Four_color_theorem) or [Hales's Theorem](https://en.wikipedia.org/wiki/Kepler_conjecture), for which every known proof requires a massive computer enumeration of cases, belong to this class. Other people might argue that, given a proof, an explanation could always be extracted with enough time and effort, though resolving this dispute won't matter for what follows.

You might hope that, even if some true mathematical statements can't be _proved_ , every true statement might nevertheless have a _convincing heuristic explanation_. Alas, a trivial adaptation of Gödel's Theorem shows that, if (1) heuristic explanations are to be checkable by computer, and (2) only true statements are to have convincing heuristic explanations, then this isn't possible either. I mean, let E be a program that accepts or rejects proposed heuristic explanations, for statements like the Twin Prime Conjecture or the Collatz Conjecture. Then construct the sentence

S(E) = "This sentence has no convincing heuristic explanation accepted by E."

If S(E) is true, then it's an example of a true arithmetical statement without _even_ a convincing heuristic explanation for its truth (!). If, on the other hand, S(E) is false, then there's a convincing heuristic explanation of its truth, which means that something has gone wrong.

What's happening, of course, is that given the two conditions we imposed, our "heuristic explanation system" _was_ a proof system, even though we didn't call it one. This is my point, though: when we use the word "proof," it normally invokes a specific image, of a sequence of statements that marches from axioms to a theorem, with each statement following from the preceding ones by rigid inference rules like those of first-order logic. None of that, however, plays any direct role in the proof of the Incompleteness Theorem, which cares only about soundness (inability to prove falsehoods) and checkability by a computer (what, with hindsight, Gödel's "arithmetization of syntax" was all about). The logic works for "heuristic explanations" too.

Now we come to something that I picked up from my former student (and now AI alignment leader) [Paul Christiano](https://paulfchristiano.com/), on a recent trip to the Bay Area, and which I share with Paul's kind permission. Having learned that there's no way to mechanize even heuristic explanations for all the true statements of arithmetic, we could set our sights lower still, and ask about mere _plausibility arguments_ --arguments that might be overturned on further reflection. Is there some sense in which every true mathematical statement at least has a good plausibility argument?

Maybe you see where this is going. Letting P be a program that accepts or rejects proposed plausibility arguments, we can construct

S(P) = "This sentence has no argument for its plausibility accepted by P."

If S(P) is true, then it's an example of a true arithmetical statement without even a plausibility argument for its truth (!). If, on the other hand, S(P) is false, then there _is_ a plausibility argument for it. By itself, this is _not at all_ a fatal problem: all sorts of false statements (IP≠PSPACE, switching doors doesn't matter in [Monty Hall](https://en.wikipedia.org/wiki/Monty_Hall_problem), Trump couldn't possibly become president…) have had decent plausibility arguments. Having said that, it's pretty strange that you can have a plausibility argument that's immediately contradicted by its own existence! This rules out some properties that you might want your "plausibility system" to have, although maybe a plausibility system exists that's still nontrivial and that has weaker properties.

Anyway, I don't know where I'm going with this, or even why I posted it, but I hope you enjoyed it! And maybe there's something to be discovered in this direction.
