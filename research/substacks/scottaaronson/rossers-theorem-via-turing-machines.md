---
title: "Rosser’s Theorem via Turing machines"
author: "Scott Aaronson"
date: "Thu, 21 Jul 2011"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=710"
---

_(Thanks to Amit Sahai for spurring me to write this post!)_

**The Background**

We all remember [Gödel's First Incompleteness Theorem](http://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems) from kindergarten. This is the thing that, given a formal system F, constructs a sentence G(F) that's a mathematical encoding of

"This sentence is not provable in F."

If F proves G(F), then F proves both that F proves G(F) and that F doesn't prove G(F), so F is inconsistent (and hence also unsound). Meanwhile, if F proves Not(G(F)), then it "believes" there's a proof of G(F). So either that proof exists (in which case it would render F inconsistent, by the previous argument), or else it doesn't exist (in which case F is unsound). The conclusion is that, assuming F is powerful enough to express sentences like G(F) in the first place, it can't be both _sound_ and _complete_ (that is, it can't prove all and only the true arithmetical statements).

OK, but the way most people like to state Gödel's Theorem is stronger than that: **no sufficiently-powerful formal system F can be both complete and _consistent_.** Note that soundness implies consistency, but not vice versa. (If I believe that there's a giant purple boogeyman on the moon, then presumably my belief is _unsound_ , but it might be perfectly _consistent_ with my various other beliefs about boogeymen.)

Unfortunately, neither Gödel's original proof, nor computer scientists' favorite alternative proofs, actually give you the stronger statement about completeness and _consistency_. And this has been a persistent problem when I teach Gödel in my undergraduate computability and complexity class.

Where's the catch in Gödel's argument? It's in the case where F proves Not(G(F)) (i.e., that G(F) is provable), even though in reality G(F) is true (i.e., G(F) _isn 't_ provable). In that situation, F would clearly be _unsound_ , but it might not contain any _contradiction_ --basically because, no matter how long you looked, you could never rule out F's (false) belief that G(F) is provable. Indeed, F would be what I like to call a _self-hating theory_ : a theory, like F+Not(Con(F)), that pessimistically believes in its own inconsistency, even though in fact it's perfectly consistent. (By contrast, if F arrogantly believes in its own _consistency_ , then it _can 't_ be consistent by the Second Incompleteness Theorem! There's a lesson there somewhere…)

The way Gödel himself solved this problem was by introducing a new concept called [ω-consistency](http://en.wikipedia.org/wiki/Omega-consistent), which is intermediate between consistency and soundness. He then showed that F can't be both complete and ω-consistent. (Why didn't Gödel simply talk about soundness? Because unlike consistency or ω-consistency, soundness is a "metatheoretic" concept that's impossible to formalize in F. So, if he used soundness, then the First Incompleteness Theorem couldn't even be _stated_ , let alone proved, in F itself, and that in turn would create problems for the proof of his _Second_ Incompleteness Theorem.)

Anyway, from the standpoint of an undergrad class, the fear is that, once you start talking about "ω-consistency," all the romance and self-referential magic of Gödel will vanish in a morass of technicality.

So surely we can dot the i's here (or rather, put the umlauts on the ö's), and prove the stronger, cleaner statement that F can't be both complete and _consistent_?

Yes we can--but to do so we need [Rosser's Theorem](http://en.wikipedia.org/wiki/Rosser%27s_trick): a strengthening of Gödel's Theorem from 1936 that's much less well-known among the nerd public than it ought to be. In Rosser's proof, we replace G(F) by a new sentence R(F), which is a mathematical encoding of the following:

"For every proof of this sentence in F, there's a shorter disproof."

If F proves R(F), then it also proves that there's a _disproof_ of R(F) that's shorter than the proof of R(F) whose existence we just assumed. So we can _look_ for that disproof (since there are only finitely many strings of symbols to check), and either we'll find it or we won't--but in either case, we'll have revealed F to be inconsistent. Meanwhile, if F proves Not(R(F)), then it proves that there _is_ a proof of R(F) with no shorter disproof. So in particular, it proves that there's a proof of R(F) that's _no longer_ than the proof of Not(R(F)) whose existence we just assumed. But once again, we can _look_ for that proof (there are only finitely many strings to check), and either we'll find it or we won't, and in either case, F is revealed to be inconsistent.

Notice what the Rosser sentence accomplishes: it creates a _symmetry_ between the cases that R(F) is provable and R(F) is _dis_ provable, correcting the asymmetry between the two cases in Gödel's original argument.

Alright, so then why don't I just teach Rosser's Theorem in my undergrad class, instead of Gödel's?

I'll tell you why: because, when __I teach Gödel to computer scientists, I like to sidestep the nasty details of how you formalize the concept of "provability in F." (From a modern computer-science perspective, [Gödel numbering](http://en.wikipedia.org/wiki/G%C3%B6del_numbering) is a barf-inducingly ugly hack!)

Instead, I simply observe Gödel's Theorem as a trivial corollary of what I see as its _conceptually-prior (even though historically-later) cousin_ : [Turing's Theorem on the unsolvability of the halting problem.](http://en.wikipedia.org/wiki/Halting_problem)

For those of you who've never seen the connection between these two triumphs of human thought: suppose we had a sound and complete (and recursively-axiomatizable, yadda yadda yadda) formal system F, which was powerful enough to reason about Turing machines. Then I claim that, using such an F, we could easily solve the halting problem. For suppose we're given a Turing machine M, and we want to know whether it halts on a blank tape. Then we'd simply have to enumerate all possible proofs in F, until we found _either_ a proof that M halts, _or_ a proof that M runs forever. Because F is complete, we'd eventually find one or the other, and because F is sound, the proof's conclusion would be _true_. So we'd decide whether M halts. But since we already know (thanks to Mr. T) that the halting problem is undecidable, we conclude that F can't have existed.

"Look ma, no Gödel numbers!"

**The "New" Observation**

The above discussion leads to an obvious question:

**Is there also a proof of _Rosser 's Theorem_ that uses only Turing machines--analogous to the computer-scientist-friendly proof we just gave for the "original" Incompleteness Theorem?**

My initial worry was that the answer would be no. For not only is Rosser's sentence more complicated than Gödel's, but it depends essentially on an _ordering_ of proofs--and it's not clear what such an ordering would correspond to in the world of Turing machines.

Why did this worry me? Because it threatened my conviction that computer programs are "really" at the core of Gödel's Theorem, whatever any tradition-minded philosopher or logician might claim to the contrary. If even the modest step from Gödel to Rosser required abandoning the computability perspective, then my faith in the Almighty Turing Machine would be shaken.

But never fear! A few months ago, I found a short, simple, Turing-machine-based proof of Rosser's Theorem. While this seemed too small to write up as a paper, ~~I 'd never seen it before (please let me know if you have!)~~, so I thought I'd share it here. (**Update:** Makoto Kanazawa points me to a basically-similar argument in [Kleene's 1967 textbook](http://books.google.com/books?id=uV6Sp8gl3PcC&lpg=PR7&ots=HfXuowZ5og&dq=Kleene%20%22mathematical%20logic%22&lr&pg=PA275#v=onepage&f=false). So, you can consider what follows to be a "popularization" of Kleene.)

The first step is to define the following variant of the halting problem:

**The Consistent Guessing Problem**

_Given as input a description of a Turing machine M:_

  1. _If M accepts on a blank tape, then accept._
  2. _If M rejects on a blank tape, then reject._
  3. _If M runs forever on a blank tape, then either accept or reject, but in any case, halt!_



It's easy to show that there's no Turing machine to solve the Consistent Guessing Problem, by a modification (arguably, even a simplification) of Turing's original argument for the halting problem. Indeed, I put the unsolvability of the Consistent Guessing Problem on last semester's midterm, and at least half the students got it. (Damn! I guess I can't use that one again.)

See it yet? No? Alright, so let P be a Turing machine that solves the Consistent Guessing Problem. Then we can easily modify P to produce an new Turing machine Q that, given as input a description ⟨M⟩ of another Turing machine M:

  * Rejects if M(⟨M⟩) accepts.
  * Accepts if M(⟨M⟩) rejects.
  * Halts (either accepting or rejecting) if M(⟨M⟩) runs forever.



Now run Q on its own description ⟨Q⟩. If Q(⟨Q⟩) accepts, then it rejects; if Q(⟨Q⟩) rejects, then it accepts. So the only remaining option is that Q(⟨Q⟩) runs forever, violating the third condition.

From the unsolvability of the Consistent Guessing Problem, I claim that Rosser's Theorem follows. For suppose we had a complete and consistent (but _not_ necessarily sound!) formal system F, which was powerful enough to talk about Turing machines. Then using F, we could solve the Consistent Guessing Problem, as follows. Given as input a Turing machine description ⟨M⟩, start enumerating all possible proofs and disproofs of the statement "M accepts on a blank tape." Accept as soon as you find a proof, or reject as soon as you find a disproof.

Because F is complete, you must eventually find either a proof or a disproof (and therefore halt, either accepting or rejecting). Also, because F is consistent, if M really rejects then F can't prove that M accepts, while if M really accepts then F can't prove that M doesn't accept (since in either case, the contradiction could be discovered in finite time). So you'll accept if M accepts and reject if M rejects. But this means that you're solving Consistent Guessing! Since we already showed there's _no_ Turing machine to solve Consistent Guessing, we conclude that F can't have existed.

QED: the moral order of the universe is restored, and the Turing machine's exalted position at the base of all human thought reaffirmed.

(Incidentally, you might wonder whether Gödel's _Second_ Incompleteness Theorem, on the impossibility of a consistent F proving its own consistency, can also be proved in a Turing-machine-centric way. To anticipate your question, the answer is yes--and better yet, it even involves Kolmogorov complexity! See, for example, [this beautiful recent paper](http://www.ams.org/notices/201011/rtx101101454p.pdf) by Shira Kritchman and Ran Raz.)

So, will Gödel's Theorem always and forevermore be taught as a centerpiece of _computability_ theory, and will the Gödel numbers get their much-deserved retirement? I don't see a reason why that _shouldn 't_ happen--but alas, the consistency of my prediction isn't enough to imply its metatheoretic truth.
