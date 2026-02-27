---
title: "The Complete Idiot’s Guide to the Independence of the Continuum Hypothesis: Part 1 of"
author: "Scott Aaronson"
date: "Sat, 31 Oct 2020"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=4974"
---

A global pandemic, apocalyptic fires, and the possible descent of the US into violent anarchy three days from now can do strange things to the soul.

Bertrand Russell--and if he'd done nothing else in his long life, I'd love him forever for it--once wrote that "in adolescence, I hated life and was continually on the verge of suicide, from which, however, I was restrained by the desire to know more mathematics." This summer, unable to bear the bleakness of 2020, I obsessively read up on the celebrated proof of the unsolvability of the [Continuum Hypothesis](https://en.wikipedia.org/wiki/Continuum_hypothesis) (CH) from the standard foundation of mathematics, the [Zermelo-Fraenkel axioms](https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory) of set theory. (In this post, I'll typically refer to "ZFC," which means Zermelo-Fraenkel plus the famous [Axiom of Choice](https://en.wikipedia.org/wiki/Axiom_of_choice).)

For those tuning in from home, the Continuum Hypothesis was formulated by [Georg Cantor](https://en.wikipedia.org/wiki/Georg_Cantor), shortly after his epochal discovery that there are different orders of infinity: so for example, the infinity of real numbers (denoted C for continuum, or \\( 2^{\aleph_0} \\)) is strictly greater than the infinity of integers (denoted ℵ0, or "Aleph-zero"). CH is simply the statement that there's no infinity _intermediate_ between ℵ0 and C: that anything greater than the first is at least the second. Cantor tried in vain for decades to prove or disprove CH; the quest is believed to have contributed to his mental breakdown. When David Hilbert presented his [famous list](https://en.wikipedia.org/wiki/Hilbert%27s_problems) of 23 unsolved math problems in 1900, CH was at the very top.

Halfway between Hilbert's speech and today, the question of CH was finally "answered," with the solution earning the only [Fields Medal](https://en.wikipedia.org/wiki/Fields_Medal) that's ever been awarded for work in set theory and logic. But unlike with any previous yes-or-no question in the history of mathematics, the answer was that there provably _is_ no answer from the accepted axioms of set theory! You can either have intermediate infinities or not; neither possibility can create a contradiction. And if you _do_ have intermediate infinities, it's up to you how many: 1, 5, 17, ∞, etc.

The easier half, the consistency of CH with set theory, was proved by incompleteness dude [Kurt Gödel](https://en.wikipedia.org/wiki/Kurt_G%C3%B6del) in 1940; the harder half, the consistency of not(CH), by [Paul Cohen](https://en.wikipedia.org/wiki/Paul_Cohen) in 1963. Cohen's work introduced the method of [forcing](https://en.wikipedia.org/wiki/Forcing_\(mathematics\)), which was so fruitful in proving set-theoretic questions unsolvable that it quickly took over the whole subject of set theory. Learning Gödel and Cohen's proofs had been a dream of mine since teenagerhood, but one I constantly put off.

This time around I started with [Cohen's retrospective essay](https://projecteuclid.org/download/pdf_1/euclid.rmjm/1181070010), as well as Timothy Chow's [Forcing for Dummies](https://groups.google.com/g/sci.math.research/c/pQdPHJYML0E/m/ZrvqIxpd1sIJ?pli=1) and [A Beginner's Guide to Forcing](https://arxiv.org/abs/0712.1320). I worked through Cohen's own [Set Theory and the Continuum Hypothesis](https://www.amazon.com/Theory-Continuum-Hypothesis-Dover-Mathematics/dp/0486469212), and Ken Kunen's [Set Theory: An Introduction to Independence Proofs](https://www.amazon.com/Introduction-Independence-Studies-Foundations-Mathematics/dp/0444868399), and [Dana Scott's 1967 paper](https://www2.karlin.mff.cuni.cz/~krajicek/scott67.pdf) reformulating Cohen's proof. I emailed questions to Timothy Chow, who was ridiculously generous with his time. When Tim and I couldn't answer something, we tried [Bob Solovay](https://en.wikipedia.org/wiki/Robert_M._Solovay) (one of the world's great set theorists, who later worked in computational complexity and quantum computing), or [Andreas Blass](https://en.wikipedia.org/wiki/Andreas_Blass) or [Asaf Karagila](http://karagila.org/). At some point mathematician and friend-of-the-blog [Greg Kuperberg](https://en.wikipedia.org/wiki/Greg_Kuperberg) joined my quest for understanding. I thank all of them, but needless to say take sole responsibility for all the errors that surely remain in these posts.

On the one hand, the proof of the independence of CH would seem to stand with general relativity, the wheel, and the chocolate bar as a triumph of the human intellect. It represents a culmination of Cantor's quest to know the basic rules of infinity--all the more amazing if the answer turns out to be that, in some sense, we _can 't_ know them.

On the other hand, perhaps no other scientific discovery of equally broad interest remains so sparsely popularized, not even (say) quantum field theory or the proof of Fermat's Last Theorem. I found barely any attempts to explain how forcing works to non-set-theorists, let alone to non-mathematicians. One notable exception was Timothy Chow's [Beginner's Guide to Forcing](https://arxiv.org/abs/0712.1320), mentioned earlier--but Chow himself, near the beginning of his essay, calls forcing an "open exposition problem," and admits that he hasn't solved it. My modest goal, in this post and the following ones, is to make a further advance on the exposition problem.

OK, but why a doofus computer scientist like me? Why not, y'know, an actual expert? I won't put forward my ignorance as a qualification, although I _have_ often found that the better I learn a topic, the more completely I forget what initially confused me, and so the less able I become to explain things to beginners.

Still, there is _one_ thing I know well that turns out to be intimately related to Cohen's forcing method, and that made me feel like I had a small "in" for this subject. This is the construction of [oracles](https://en.wikipedia.org/wiki/Oracle_machine) in computational complexity theory. In CS, we like to construct hypothetical universes where P=NP or P≠NP, or P≠BQP, or the polynomial hierarchy is infinite, etc. To do so, we, by fiat, insert a new function--an _oracle_ --into the universe of computational problems, carefully chosen to make the desired statement hold. Often the oracle needs to satisfy an infinite list of conditions, so we handle them one by one, taking care that when we satisfy a new condition we don't invalidate the previous conditions.

All this, I kept reading, is _profoundly_ analogous to what the set theorists do when they create a mathematical universe where the Axiom of Choice is true but CH is false, or vice versa, or any of a thousand more exotic possibilities. They insert new sets into their models of set theory, sets that are carefully constructed to "force" infinite lists of conditions to hold. In fact, some of the exact same people--such as [Solovay](https://en.wikipedia.org/wiki/Robert_M._Solovay)--who helped pioneer forcing in the 1960s, later went on to pioneer oracles in computational complexity. We'll say more about this connection in a future post.

**How Could It Be?**

How do you study a well-defined math problem, and return the answer that, as far as the accepted axioms of math can say, there _is_ no answer? I mean: even supposing it's _true_ that there's no answer, how do you _prove_ such a thing?

Arguably, not even [Gödel's Incompleteness Theorem](https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems) achieved such a feat. Recall, the Incompleteness Theorem says loosely that, for every formal system F that could possibly serve as a useful foundation for mathematics, there exist statements even of elementary arithmetic that are true but unprovable in F--and Con(F), a statement that encodes F's own consistency, is an example of one. But the very statement that Con(F) is unprovable is equivalent to Con(F)'s being _true_ (since an inconsistent system could prove anything, including Con(F)). In other words, if the Incompleteness Theorem as applied to F holds any interest, then that's only because F _is, in fact_ ,_consistent_ ; it's just that resources beyond F are needed to prove this.

Yes, there's a "self-hating theory," F+Not(Con(F)), which believes in its own inconsistency. And yes, by Gödel, this self-hating theory is _consistent_ if F itself is. This means that it has a **model** --involving "nonstandard integers," formal artifacts that effectively promise a proof of F's inconsistency without ever actually delivering it. We'll have much, _much_ more to say about models later on, but for now, they're just collections of objects, along with relationships between the objects, that satisfy all the axioms of a theory (thus, a model of the axioms of group theory is simply … any group!).

In any case, though, the self-hating theory F+Not(Con(F)) can't be _arithmetically sound_ : I mean, just look at it! It's either unsound because F is consistent, or else it's unsound because F is inconsistent. In general, this is one of the most fundamental points in logic: **consistency does not imply soundness**. If I believe that the moon is made of cheese, that might be _consistent_ with all my other beliefs about the moon (for example, that Neil Armstrong ate delicious chunks of it), but that doesn't mean my belief is _true_. Like the classic conspiracy theorist, who thinks that any apparent evidence against their hypothesis was planted by George Soros or the CIA, I might simply believe a self-consistent collection of absurdities. Consistency is purely a syntactic condition--it just means that I can never prove both a statement and its opposite--but soundness goes further, asserting that whatever I can prove is actually the case, a _relationship_ between what's inside my head and what's outside it.

So again, assuming we had any business using F in the first place, the Incompleteness Theorem gives us two _consistent_ ways to extend F (by adding Con(F) or by adding Not(Con(F))), but only one _sound_ way (by adding Con(F)). But the independence of CH from the ZFC axioms of set theory is of a fundamentally different kind. It will give us models of ZFC+CH, and models of ZFC+Not(CH), that are _both_ at least somewhat plausible as "sketches of mathematical reality"--and that both even have defenders. The question of which is right, or whether it's possible to decide at all, will be punted to the future: to the discovery (or not) of some intuitively compelling foundation for mathematics that, as Gödel hoped, answers the question by going beyond ZFC.

**Four Levels to Unpack**

While experts might consider this too obvious to spell out, Gödel's and Cohen's analyses of CH aren't so much about infinity, as they are about our ability to _reason_ about infinity using finite sequences of symbols. The game is about building self-contained mathematical universes to order--universes where all the accepted axioms about infinite sets hold true, and yet that, in some cases, seem to mock what those axioms were supposed to _mean_ , by containing vastly fewer objects than the mathematical universe was "meant" to have.

In understanding these proofs, the central hurdle, I think, is that there are at least four different "levels of description" that need to be kept in mind simultaneously.

At the first level, Gödel's and Cohen's proofs, like all mathematical proofs, are finite sequences of symbols. Not only that, they're proofs that can be formalized in elementary arithmetic (!). In other words, even though they're _about_ the axioms of set theory, they don't themselves _require_ those axioms. Again, this is possible because, at the end of the day, Gödel's and Cohen's proofs won't be talking about infinite sets, but "only" about finite sequences of symbols that make statements about infinite sets.

At the second level, the proofs are making an "unbounded" but perfectly clear claim. They're claiming that, if someone showed you a proof of either CH or Not(CH), from the ZFC axioms of set theory, then no matter how long the proof or what its details, you could convert it into a proof that _ZFC itself_ was inconsistent. In symbols, they're proving the "relative consistency statements"

Con(ZFC) ⇒ Con(ZFC+CH),  
Con(ZFC) ⇒ Con(ZFC+Not(CH)),

and they're proving these as theorems of _elementary arithmetic_. (Note that there's no hope of proving Con(ZF+CH) or Con(ZFC+Not(CH)) _outright_ within ZFC, since by Gödel, ZFC can't even prove its own consistency.)

This translation is completely explicit; the independence proofs even yield _algorithms_ to convert proofs of inconsistencies in ZFC+CH or ZFC+Not(CH), supposing that they existed, into proofs of inconsistencies in ZFC itself.

Having said that, as Cohen himself often pointed out, thinking about the independence proofs in terms of algorithms to manipulate sequences of symbols is hopeless: to have any chance of understanding these proofs, let alone coming up with them, at some point you need to think about what the symbols _refer_ to.

This brings us to the third level: the symbols refer to _models of set theory_ , which could also be called "mathematical universes." Crucially, we always can and often will take these models to be only _countably_ infinite: that is, to contain an infinity of sets, but "merely" ℵ0 of them, the infinity of integers or of finite strings, and no more.

The fourth level of description is from within the models themselves: each model imagines itself to have an _uncountable_ infinity of sets. As far as the model's concerned, it comprises the entire mathematical universe, even though "looking in from outside," we can see that that's not true. In particular, each model of ZFC _thinks_ it has uncountably many sets, many themselves of uncountable cardinality, even if "from the outside" the model is countable.

Say what? The models are _mistaken_ about something as basic as their own size, about how many sets they have? Yes. The models will be like _The Matrix_ (the movie, not the mathematical object), or _The Truman Show_. They're self-contained little universes whose inhabitants can never discover that they're living a lie--that they're missing sets that we, from the outside, know to exist. The poor denizens of the Matrix will never even be able to learn that their universe--what __ they mistakenly think of as _the_ universe--is secretly countable! And no [Morpheus](https://en.wikipedia.org/wiki/Morpheus_\(The_Matrix\)) will ever arrive to enlighten them, although--and this is crucial to Cohen's proof in particular--the inhabitants will be able to reason more-or-less intelligibly about what would happen if a Morpheus _did_ arrive.

The [Löwenheim-Skolem Theorem](https://en.wikipedia.org/wiki/L%C3%B6wenheim%E2%80%93Skolem_theorem), from the early 1920s, says that _any_ countable list of first-order axioms that has any model at all (i.e., that's consistent), must have a model with at most countably many elements. And ZFC is a countable list of first-order axioms, so Löwenheim-Skolem applies to it--even though ZFC implies the existence of an uncountable infinity of sets! Before taking the plunge, we'll need to not merely grudgingly accept but love and internalize this ["paradox,"](https://en.wikipedia.org/wiki/Skolem%27s_paradox) because pretty much the entire proof of the independence of CH is built on top of it.

Incidentally, once we realize that it's possible to build self-consistent yet "fake" mathematical universes, we can ask the question that, incredibly, the _Matrix_ movies never ask. Namely, how do we know that our own, larger universe isn't similarly a lie? The answer is that we don't! As an example--I hope you're sitting down for this--even though Cantor proved that there are uncountably many real numbers, that only means there are uncountably many reals _for us_. We can't rule out the possibly that God, looking down on our universe, would see countably many reals.

**Cantor 's Proof Revisited**

To back up: the whole story of CH starts, of course, with Cantor's epochal discovery of the different orders of infinity, that for example, there are more subsets of positive integers (or equivalently real numbers, or equivalently infinite binary sequences) than there are positive integers. The devout Cantor thought his discovery illuminated the nature of God; it's never been entirely obvious to me that he was wrong.

Recall how Cantor's proof works: we suppose by contradiction that we have an enumeration of all infinite binary sequences: for example,

s(0) = **0** 0000000…  
s(1) = 0**1** 010101…  
s(2) = 11**0** 01010….  
s(3) = 100**0** 0000….

We then produce a new infinite binary sequence that's not on the list, by going down the diagonal and flipping each bit, which in the example above would produce 1011…

But look more carefully. What Cantor really shows is only that, _within our mathematical universe_ , there can't be an enumeration of all the reals of our universe. For if there were, we could use it to define a new real that was in the universe but not in the enumeration. The proof doesn't rule out the possibility that _God_ could enumerate the reals of our universe! It only shows that, if so, there would need to be additional, heavenly reals that were missing from even God's enumeration (for example, the one produced by diagonalizing against _that_ enumeration).

Which reals could possibly be "missing" from our universe? Every real you can name--42, π, √e, even uncomputable reals like [Chaitin's Ω](https://en.wikipedia.org/wiki/Chaitin%27s_constant)--has to be there, right? Yes, and there's the rub: _every real you can name_. Each name is a finite string of symbols, so whatever your naming system, you can only ever name countably many reals, leaving 100% of the reals nameless.

Or did you think of only the _rationals_ or _algebraic numbers_ as forming a countable dust of discrete points, with numbers like π and e filling in the solid "continuum" between them? If so, then I hope you're sitting down for this: _every real number you 've ever heard of_ belongs to the countable dust! The entire concept of "the continuum" is only needed for reals that don't have names and never will.

**From ℵ 0 Feet**

Gödel and Cohen's achievement was to show that, without creating any contradictions in set theory, we can adjust size of this elusive "continuum," put more reals into it or fewer. How does one even start to begin to prove such a statement?

From a distance of ℵ0 feet, Gödel proves the consistency of CH by building minimalist mathematical universes: one where "the only sets that exist, are the ones _required_ to exist by the ZFC axioms." (These universes can, however, differ from each other in how "tall" they are: that is, in how many [ordinals](https://en.wikipedia.org/wiki/Ordinal_number) they have, and hence how many sets overall. More about that in a future post!) Gödel proves that, _if_ the axioms of set theory are consistent--that is, if they describe any universes at all--then they also describe these minimalist universes. He then proves that, in any of these minimalist universes, from the standpoint of someone _within_ that universe, there are exactly ℵ1 real numbers, and hence CH holds.

At an equally stratospheric level, Cohen proves the consistency of not(CH) by building … well, _non_ -minimalist mathematical universes! A simple way is to start with Gödel's minimalist universe--or rather, an even more minimalist universe than his, one that's been cut down to have only countably many sets--and then to stick in a bunch of _new real numbers_ that weren't in that universe before. We choose the new real numbers to ensure two things: first, we still have a model of ZFC, and second, that we make CH false. The details of how to do that will, of course, concern us later.

**My Biggest Confusion**

In subsequent posts, I'll say more about the character of the ZFC axioms and how one builds models of them to order. Just as a teaser, though, to conclude this post I'd like to clear up a fundamental misconception I had about this subject, from roughly the age of 16 until a couple months ago.

I thought: the way Gödel proves the consistency of CH, must be by examining all the sets in his minimalist universe, and checking that each one has either at most ℵ0 elements or else at least C of them. Likewise, the way Cohen proves the consistency of not(CH), must be by "forcing in" some extra sets, which have more than ℵ0 elements but fewer than C elements.

Except, it turns out that's not how it works. Firstly, to prove CH in his universe, Gödel is not going to check each set to make sure it doesn't have intermediate cardinality; instead, he's simply going to count all the reals to make sure that there are only ℵ1 of them--where [ℵ1](https://en.wikipedia.org/wiki/Aleph_number#Aleph-one) is the next infinite cardinality after ℵ0. This will imply that C=ℵ1, which is another way to state CH.

More importantly, to build a universe where CH is false, Cohen is going to start with a universe where C=ℵ1, like Gödel's universe, and then _add in more reals:_ say, ℵ2 of them. The ℵ1 "original" reals will then supply our set of intermediate cardinality between the ℵ0 integers and the ℵ2 "new" reals.

Looking back, the core of my confusion was this. I had thought: I can visualize what ℵ0 means; that's just the infinity of integers. I can _also_ visualize what \\( C=2^{\aleph_0} \\) means; that's the infinity of points on a line. Those, therefore, are the two bedrocks of clarity in this discussion. By contrast, I _can 't_ visualize a set of intermediate cardinality between ℵ0 and C. The intermediate infinity, being weird and ghostlike, is the one that shouldn't exist unless we deliberately "force" it to.

Turns out I had things backwards. For starters, I _can 't_ visualize the uncountable infinity of real numbers. I might _think_ I'm visualizing the real line--it's solid, it's black, it's got little points everywhere--but how can I be sure that I'm not merely visualizing the ℵ0 rationals, or (say) the computable or definable reals, which include all the ones that arise in ordinary math?

The continuum C is _not at all_ the bedrock of clarity that I'd thought it was. Unlike its junior partner ℵ0, the continuum is adjustable, changeable--and we _will_ change it when we build different models of ZFC. What's (relatively) more "fixed" in this game is something that I, like many non-experts, had always given short shrift to: Cantor's sequence of Alephs ℵ0, ℵ1, ℵ2, etc.

Cantor, who was a very great man, didn't merely discover that C>ℵ0; he also discovered that the infinite cardinalities form a [well-ordered](https://en.wikipedia.org/wiki/Well-order) sequence, with no infinite descending chains. Thus, after ℵ0, there's a next greater infinity that we call ℵ1; after ℵ1 comes ℵ2; after the entire infinite sequence ℵ0,ℵ1,ℵ2,ℵ3,… comes ℵω; after ℵω comes ℵω+1; and so on. These infinities will always be there in any universe of set theory, and always in the same order.

Our job, as engineers of the mathematical universe, will include pegging the continuum C to one of the Alephs. If we stick in a bare minimum of reals, we'll get C=ℵ1, if we stick in more we can get C=ℵ2 or C=ℵ3, etc. We can't make C equal to ℵ0--that's Cantor's Theorem--and we _also_ can't make C equal to ℵω, by an important [theorem of König](https://en.wikipedia.org/wiki/K%C3%B6nig%27s_theorem_\(set_theory\)) that we'll discuss later (yes, this is an umlaut-heavy field). But it will turn out that we can make C equal to just about any other Aleph: in particular, to any infinity other than ℵ0 that's not the supremum of a countable list of smaller infinities.

In some sense, this is the whole journey that we need to undertake in this subject: from seeing the cardinality of the continuum as a metaphysical mystery, which we might contemplate by staring really hard at a black line on white paper, to seeing the cardinality of the continuum _as an engineering problem_.

Stay tuned! Next installment coming after the civilizational Singularity in three days, assuming there's still power and Internet and food and so forth.

Oh, and happy Halloween. Ghostly sets of intermediate cardinality … spoooooky!
