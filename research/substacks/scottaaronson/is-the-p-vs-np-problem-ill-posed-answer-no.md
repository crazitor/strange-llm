---
title: "Is the P vs. NP problem ill-posed?  (Answer: no.)"
author: "Scott Aaronson"
date: "Wed, 13 Aug 2014"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=1948"
---

A couple days ago, a reader wrote to me to ask whether it's possible that the solution to the P vs. NP problem is simply undefined--and that one should enlarge the space of possible answers using non-classical logics (the reader mentioned something called [Catuṣkoṭi logic](http://en.wikipedia.org/wiki/Catu%E1%B9%A3ko%E1%B9%ADi)). Since other people have emailed me with similar questions in the past, I thought my response might be of more general interest, and decided to post it here.

* * *

Thanks for your mail! I'm afraid I don't agree with you that there's a problem in the formulation of P vs. NP. Let me come at it this way:

Do you also think there might be a problem in the formulation of Goldbach's Conjecture? Or the Twin Prime Conjecture? (I.e., that maybe the definition of "prime number" needs to be modified using Catuṣkoṭi logic?) Or any other currently-unsolved problem in any other part of math?

If you don't, then my question would be: why single out P vs. NP?

After all, P vs. NP can be expressed as a Π2-sentence: that is, as a certain relationship among positive integers, which either holds or doesn't hold. (In this case, the integers would encode Turing machines, polynomial upper bounds on their running time, and an NP-complete problem like 3SAT -- all of which are expressible using the basic primitives of arithmetic.) In terms of its logical form, then, it's really no different than the Twin Prime Conjecture and so forth.

So then, do you think that statements of arithmetic, like there being no prime number between 24 and 28, might also be like the Parallel Postulate? That there might be some other, equally-valid "non-Euclidean arithmetic" where there _is_ a prime between 24 and 28? What exactly would one mean by that? I understand exactly what one means by non-Euclidean geometries, but to my mind, geometry is less "fundamental" (at least in a logical sense) than positive integers are. And of course, even if one believes that non-Euclidean geometries are just as "fundamental" as Euclidean geometry -- an argument that seems harder to make for, say, the positive integers versus the Gaussian integers or finite fields or p-adics -- that still doesn't change the fact that questions about Euclidean geometry have definite right answers.

Let me acknowledge two important caveats to what I said:

First, it's certainly possible that P vs. NP might be _independent_ of standard formal systems like ZF set theory (i.e., neither provable nor disprovable in them). That's a possibility that everyone acknowledges, even if (like me) they consider it rather unlikely. But note that, even if P vs. NP were independent of our standard formal systems, that still wouldn't mean that the question was ill-posed! There would still either be a Turing machine that decided 3SAT in polynomial time, or else there wouldn't be. It would "only" mean that the usual axioms of set theory wouldn't suffice to tell us which.

The second caveat is that P vs. NP, like any other mathematical question, can be generalized and extended in all sorts of interesting ways. So for example, one can define analogues of P vs. NP over the reals and complex numbers (which are _also_ currently open, but which might be easier than the Boolean version). Or, even if P≠NP, one can still ask if randomized algorithms, or nonuniform algorithms, or quantum algorithms, might be able to solve NP-complete problems in polynomial time. Or one can ask whether NP-complete problems are at least efficiently solvable "on average," if not in the worst case. Every one of these questions has been actively researched, and you could make a case that some of them are just as interesting as the original P vs. NP question, if not _more_ interesting -- if history had turned out a little different, any one of these might have been what we'd taken as our "flagship" question, rather than P vs. NP. But again, this still doesn't change the fact that the original P vs. NP question has some definite answer (like, for example, P≠NP…), even if we can't prove which answer it is, even if we won't be able to prove it for 500 years.

And please keep in mind that, if P vs. NP were solved after being open for hundreds of years, it would be far from the first such mathematical problem! Fermat's Last Theorem stayed open for 350 years, and the impossibility of squaring the circle and trisecting the angle were open for more than 2000 years. Any time before these problems were solved, one could've said that maybe people had failed because the question itself was ill-posed, but one would've been mistaken. People simply hadn't invented the right ideas yet.

Best regards,  
Scott

* * *

**Unrelated Announcements:** As most of you have [probably seen](http://www.mathunion.org/general/prizes/2014/), Subhash Khot won the Nevanlinna Prize, while Maryam Mirzakhani, Artur Avila, Manjul Bhargava and Martin Hairer won the Fields Medal. Mirzakhani is the first female Fields Medalist. Congratulations to all!

Also, I join the rest of the world in saying that Robin Williams was a great actor--there was no one better at playing "the Robin Williams role" in any given movie--and his loss is a loss for humanity.
