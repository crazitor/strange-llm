---
title: "My 116-page survey article on P vs. NP: better late than never"
author: "Scott Aaronson"
date: "Wed, 04 Jan 2017"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=3095"
---

For those who just want the survey itself, not the backstory, [it's here](http://www.scottaaronson.com/papers/pnp.pdf). (_Note:_ Partly because of the feedback I've gotten on this blog, it's now expanded to 121 pages!)

* * *

**Update (Jan. 23)** By request, I've prepared a [Kindle-friendly edition](http://www.scottaaronson.com/papers/pnp-kindle.pdf) of this P vs. NP survey--a mere 260 pages!

* * *

Two years ago, I learned that John Nash--_that_ John Nash--was, together with Michail Rassias, editing a volume about the great open problems in mathematics.  And they wanted me to write the chapter about the P versus NP question--a question that Nash himself had come close to raising, in a prescient [handwritten letter](https://www.nsa.gov/news-features/declassified-documents/nash-letters/assets/files/nash_letters1.pdf) that he sent to the National Security Agency in 1955.

On the one hand, I knew I didn't have time for such an undertaking, and am such a terrible procrastinator that, in _both_ [previous](http://www.scottaaronson.com/papers/philos.pdf) [cases](http://www.scottaaronson.com/papers/giqtm3.pdf) where I wrote a book chapter, I singlehandedly delayed the entire volume by months.  But on the other hand, John Nash.

So of course I said yes.

What followed was a year in which Michail sent me increasing panicked emails (and then phone calls) informing me that the whole volume was ready for the printer, _except_ for my P vs. NP thing, and is there any chance I'll have it by the end of the week?  Meanwhile, I'm reading yet more papers about Karchmer-Wigderson games, proof complexity, time/space tradeoffs, elusive functions, and small-depth arithmetic circuits.  P vs. NP, as it turns out, is now a _big_ subject.

And in the middle of it, on May 23, 2015, John Nash and his wife Alicia were tragically killed on the New Jersey Turnpike, on their way back from the airport (Nash had just accepted the Abel Prize in Norway), when their taxi driver slammed into a guardrail.

But while Nash himself sadly wouldn't be alive to see it, the volume was still going forward.  And now we were effectively honoring Nash's memory, so I _definitely_  couldn't pull out.

So finally, last February, after more months of struggle and delay, I sent Michail what I had, and it duly appeared in the volume [Open Problems in Mathematics](https://www.amazon.com/Open-Problems-Mathematics-John-Forbes/dp/3319321609).

But I knew I wasn't done: there was still sending my chapter out to experts to solicit their comments.  This I did, and massively-helpful feedback started pouring in, creating yet more work for me.  The thorniest section, by far, was the one about [Geometric Complexity Theory (GCT)](https://en.wikipedia.org/wiki/Geometric_complexity_theory): the program, initiated by Ketan Mulmuley and carried forward by a dozen or more mathematicians, that seeks to attack P vs. NP and related problems using a fearsome arsenal from algebraic geometry and representation theory.  The experts told me, in no uncertain terms, that my section on GCT got things badly wrong--but they didn't agree with each other about _how_  I was wrong.  So I set to work trying to make them happy.

And then I got sidetracked with the move to Austin and with other projects, so I set the whole survey aside: a year of sweat and tears down the toilet.  Soon after that, Bürgisser, Ikenmeyer, and Panova proved a [breakthrough "no-go" theorem](https://arxiv.org/abs/1604.06431), substantially changing the outlook for the GCT program, meaning yet more work for me if and when I ever returned to the survey.

Anyway, today, confined to the house with my sprained ankle, I decided that the perfect was the enemy of the good, and that I should just _finish_  the damn survey and put it up on the web, so readers can benefit from it before the march of progress (we can hope!) renders it totally obsolete.

[So here it is!](http://www.scottaaronson.com/papers/pnp.pdf)  All 116 pages, 268 bibliography entries, and 52,000 words.

For your convenience, here's the abstract:

In 1955, John Nash sent a remarkable letter to the National Security Agency, in which--seeking to build theoretical foundations for cryptography--he all but formulated what today we call the P=?NP problem, considered one of the great open problems of science.  Here I survey the status of this problem in 2017, for a broad audience of mathematicians, scientists, and engineers.  I offer a personal perspective on what it's about, why it's important, why it's reasonable to conjecture that P≠NP is both true and provable, why proving it is so hard, the landscape of related problems, and crucially, what progress has been made in the last half-century toward solving those problems.  The discussion of progress includes diagonalization and circuit lower bounds; the relativization, algebrization, and natural proofs barriers; and the recent works of Ryan Williams and Ketan Mulmuley, which (in different ways) hint at a duality between impossibility proofs and algorithms.

Thanks so much to everyone whose feedback helped improve the survey.  If you have additional feedback, feel free to share in the comments section!  My plan is to incorporate the _next_ round of feedback by the year 2100, if not earlier.

* * *

**Update (Jan. 4)** Bill Gasarch writes to tell me that Lazslo Babai has posted an announcement [scaling back](http://people.cs.uchicago.edu/~laci/update.html) his famous "Graph Isomorphism in Quasipolynomial Time" claim. Specifically, Babai says that, due to an error discovered by Harald Helfgott, his graph isomorphism algorithm actually runs in about 22^O(√log(n)) time, rather than the originally claimed npolylog(n). This still beats the best previously-known running time for graph isomorphism (namely, 2O(√(n log n))), and by a large margin, but not quite as large as before.

Babai pointedly writes:

> I apologize to those who were drawn to my lectures on this subject solely because of the quasipolynomial claim, prematurely magnified on the internet in spite of my disclaimers.

Alas, my own experience has taught me the hard way that, on the Internet, it is do or do not. There is no disclaim.

In any case, I've already updated my P vs. NP survey to reflect this new development.

* * *

**Another Update (Jan. 10)** For those who missed it, Babai has [another update](http://people.cs.uchicago.edu/~laci/update.html) saying that he's fixed the problem, and the running time of his graph isomorphism algorithm is back to being quasipolynomial.

* * *

**Update (Jan. 19):** This moment--the twilight of the Enlightenment, the eve of the return of the human species back to the rule of thugs--seems like as good a time as any to declare my P vs. NP survey officially **done**. I.e., thanks so much to everyone who sent me suggestions for additions and improvements, I've implemented pretty much all of them, and I'm not seeking additional suggestions!
