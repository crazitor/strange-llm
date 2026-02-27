---
title: "P vs. NP for Dummies"
author: "Scott Aaronson"
date: "Sun, 15 Aug 2010"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=459"
---

A reader named Darren commented on my last post:

> I have this feeling that this whole P and NP thing is not only a profound problem that needs solving, but something that can be infinitely curious to try and wrap your mind around…
> 
> Thing is- there’s a whole world of great minded, genius hackers out here that can’t understand one iota of what anyone is talking about. We’re not your traditional code-savvy hackers; we’re your inventors, life hackers, researchers, scientists… and I think I can speak for most of us when I say: We would love to take the time to really dive into this thread, but we ask that someone (you) write a blog that breaks this whole thing down into a rest-of-the-world-friendly P/NP for dummies… or at least explain it to us like we’re stupid as hell… at this point I’m really okay with even that.

_I 'm_ of course the stupid one here, for forgetting the folks like Darren who were enticed by L'Affaire Deolalikar into entering our little P/NP tent, and who now want to know what it is we're hawking.

The short answer is: the biggest unsolved problem of theoretical computer science, and one of the deepest questions ever asked by human beings! Here are four informal interpretations of the P vs. NP problem that people give, and which I can endorse as capturing the spirit of what's being asked:

  * Are there situations where _brute-force search_ --that is, trying an exponential number of possibilities one-by-one, until we find a solution that satisfies all the stated constraints--is essentially the best algorithm possible?
  * Is there a fast algorithm to solve the _NP-complete problems_ --a huge class of combinatorial problems that includes scheduling airline flights, laying out microchips, optimally folding proteins, coloring maps, packing boxes as densely as possible, finding short proofs of theorems, and thousands of other things that people in fields ranging from AI to chemistry to economics to manufacturing would like to solve? (While it's not obvious _a priori_ , it's known that these problems are all "re-encodings" of each other. So in particular, a fast algorithm for any one of the problems would imply fast algorithms for the rest; conversely, if any one of them is hard then then they all are.)
  * Is it harder to solve a math problem yourself than to check a solution by someone else? _[[This is where you insert a comment about the delicious irony, that P vs. NP**itself** is a perfect example of a monstrously-hard problem for which we could nevertheless recognize a solution if we saw one--and hence, part of the explanation for why it's so hard to prove P≠NP is that P≠NP…]]_
  * In the 1930s, Gödel and Turing taught us that not only are certain mathematical statements _undecidable_ (within the standard axiom systems for set theory and even arithmetic), but there's not even an algorithm to tell which statements have a proof or disproof and which don't. Sure, you can try checking every possible proof, one by one--but if you haven't yet found a proof, then there's no general way to tell whether that's because there _is_ no proof, or whether you simply haven't searched far enough. On the other hand, if you restrict your attention to, say, proofs consisting of 1,000,000 symbols or less, then enumerating every proof _does_ become possible. However, it only becomes "possible" in an extremely Platonic sense: if there are 21,000,000 proofs to check, then the sun will have gone cold and the universe degenerated into black holes and radiation long before your computer's made a dent. So, the question arises of whether Gödel and Turing's discoveries have a "finitary" analogue: are there classes of mathematical statements that have _short_ proofs, but for which the proofs can't be found in any reasonable amount of time?



Basically, P vs. NP is the mathematical problem that you're inevitably led to if you try to formalize any of the four questions above.

Admittedly, in order to _state_ the problem formally, we need to make a choice: we interpret the phrase "fast algorithm" to mean "deterministic Turing machine that uses a number of steps bounded by a polynomial in the size of the input, and which always outputs the correct answer (yes, there is a solution satisfying the stated constraints, or no, there isn't one)." There are other natural ways to interpret "fast algorithm" (probabilistic algorithms? quantum algorithms? linear time? linear time with a small constant? subexponential time? algorithms that only work on _most_ inputs?), and many are better depending on the application. A key point, however, is that _whichever_ choices we made, we'd get a problem that's staggeringly hard, and for essentially the same reasons as P vs. NP is hard! And therefore, out of a combination of mathematical convenience and tradition, computer scientists like to take P vs. NP as our "flagship example" of a huge _class_ of questions about what is and isn't feasible for computers, _none_ of which we know how to answer.

So, those of you who just wandered into the tent: care to know more? The good news is that lots of excellent resources already exist. I suggest starting with the [Wikipedia article on P vs. NP](http://en.wikipedia.org/wiki/P_versus_NP_problem#Notable_attempts_at_proof), which is quite good. From there, you can move on to Avi Wigderson's 2006 survey [P, NP and mathematics - a computational complexity perspective](http://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/W06/w06.pdf), or Mike Sipser's [The History and Status of the P vs. NP Question](http://www.eecs.berkeley.edu/~luca/cs172-04/sipser92history.pdf) (1992) for a more historical perspective (and a translation of a now-famous 1956 letter from Gödel to von Neumann, which first asked what we'd recognize today as the P vs. NP question).

After you've finished the above … well, the number of P vs. NP resources available to you increases exponentially with the length of the URL. For example, without even leaving the scottaaronson.com domain, you can find the following:

  * [Ten Reasons to Believe P≠NP](https://scottaaronson.blog/?p=122)
  * [Great Ideas in Theoretical Computer Science Lecture 9](http://stellar.mit.edu/S/course/6/sp08/6.080/courseMaterial/topics/topic1/lectureNotes/lec9/lec9.pdf) (P and NP)
  * [Quantum Computing Since Democritus Lecture 6](http://www.scottaaronson.com/democritus/lec6.html) (P, NP, and Friends)
  * [Has There Been Progress on the P vs. NP Question?](http://www.scottaaronson.com/talks/pvsnp.ppt) (PowerPoint talk, from the Barriers workshop last year in Princeton)
  * [Is P vs. NP Formally Independent?](http://www.scottaaronson.com/papers/pnp.pdf) (2003 survey article)
  * [Algebrization: A New Barrier in Complexity Theory](http://www.scottaaronson.com/papers/alg.pdf) (2009 paper by Avi Wigderson and myself)



Feel free to use the comments section to suggest other resources, or to ask and answer basic questions about the P vs. NP problem, why it's hard, why it's important, how it relates to other problems, why Deolalikar's attempt apparently failed, etc. Me, I think I'll be taking a break from this stuff.
