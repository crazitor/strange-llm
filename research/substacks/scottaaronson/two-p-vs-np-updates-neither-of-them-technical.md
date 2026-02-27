---
title: "Two P vs. NP updates (neither of them technical)"
author: "Scott Aaronson"
date: "Tue, 02 Apr 2013"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=1293"
---

[](https://scottaaronson.blog/wp-content/uploads/2013/04/lilymeme.png)

"Meme" courtesy of my brother David

First news item: it's come to my attention that yesterday, an MIT professor abused his power over students for a cruel April Fools' Day prank involving the P vs. NP problem. His email to the students is below.

I assume most of you already heard the news that a Caltech grad student, April Felsen, announced a 400-page proof of P≠NP last week. While I haven't yet completely digested the argument, it's already clear that Felsen (who I actually knew back when she was an MIT undergrad) has changed theoretical computer science forever, bringing in new tools from K-theory to higher topos theory to solve the biggest problem there was.

Alas, Felsen's proof has the "short-term" effect of making the existing 6.045 seem badly outdated. So, after long reflection, I've made a decision that not all of you are going to like, but that I believe is the right one intellectually. I've decided to reorient the entire course to focus on Felsen's result, starting with tomorrow's lecture.

And further, I decided to rewrite Thursday's midterm to focus almost entirely on this new material. That means that, yes, you're going to have THREE DAYS to learn at least the basics of algebraic topology and operator algebras, as used in Felsen's proof. To do that, you might need to drop everything else (including sleep, unfortunately), and this might prove to be the most strenuous and intense thing you've ever done. But it will also be an experience that will enrich your minds and ennoble your souls, and that you'll be proud to tell your grandchildren about. And of course we'll be there to help out. So **let 's get started!**

All the best,  
Scott

* * *

Second news item: many of you have probably heard that Lance Fortnow's _[The Golden Ticket](http://www.amazon.com/The-Golden-Ticket-Search-Impossible/dp/0691156492/)_ --the first popular book about the P vs. NP problem--is now out. (The title refers to Roald Dahl's _Charlie and the Chocolate Factory_ , which involved a few chocolate bars that had coveted golden tickets inside the wrappers, along with millions of chocolate bars that didn't.) I read it last week, and I think it's excellent: a book I'll happily recommend to family and friends who want the gentlest introduction to complexity theory that exists.

Some context: for more than a decade, people have been telling me that _I_ should write a popular book about P vs. NP, and I never did, and now Lance has. So I'm delighted to say that reading Lance's book quickly cured me of any regrets I might have felt. For not only is _The Golden Ticket_ a great book, but better yet, it's not a book that I ever could've written.

Here's why: _every time_ I would have succumbed to the temptation to explain something too complicated for the world's journalists, literary humanists, and pointy-haired bosses--something like relativization, or natural proofs, or arithmetization, or Shannon's counting argument, or Ladner's Theorem, or coNP, or the reasons to focus on polynomial time--every time, Lance somehow manages to resist the temptation, and to stick to cute stories, anecdotes, and practical applications. This is really, truly a _popular_ book: as Lance points out himself, in 162 pages of discussing the P vs. NP question, he never even formally defines P and NP!

But it goes beyond that: in the world of _The Golden Ticket_ , P vs. NP is important because, if P=NP, then people could design more effective cancer therapies, solve more crimes, and better predict which baseball games would be closely-matched and exciting (yes, really). P vs. NP is also important because it provides a unifying framework for understanding current technological trends, like massively-parallel computing, cloud computing, big data, and the Internet of things. Meanwhile, quantum computing might or might not be possible in principle, but either way, it's probably not that relevant because it won't be practical for a long time.

In short, Lance has written _precisely_ the book about P vs. NP that the interested layperson or IT professional wants and needs, and _precisely_ the book that I couldn't have written. I would've lost patience by around page 20, and exclaimed:

**" You want me to justify the P vs. NP problem by its _relevance to baseball??_ Why shouldn't _baseball_ have to justify itself by its relevance to P vs. NP? Pshaw! Begone from the house of study, you cretinous fools, and never return!"**

My favorite aspect of _The Golden Ticket_ was its carefully-researched treatment of the history of the P vs. NP problem in the 50s, 60s, and 70s, both in the West and in the Soviet Union (where it was called the "perebor" problem). Even complexity theorists will learn countless tidbits--like how Leonid Levin was "discovered" at age 15, and how the powerful Sergey Yablonsky stalled Soviet _perebor_ research by claiming to have solved the problem when he'd done nothing of the kind. The historical chapter (Chapter 5) is alone worth the price of the book.

I have two quibbles. First, throughout the book, Lance refers to a hypothetical world where P=NP as the "Beautiful World." __I would 've called that world the "Hideous World"! For it's a world where technical creativity is mostly worthless, and where the mathematical universe is boring, flat, and incomprehensibly comprehensible. Here's an analogy: suppose a video game turned out to have a bug that let you accumulate unlimited points just by holding down a certain button. Would anyone call that game the "Beautiful Game"?

My second disagreement concerns quantum computing. Overall, Lance gives an admirably-accurate summary, and I was happy to see him throw cold water on breathless predictions about QC and other quantum-information technologies finding practical applications in the near future. However, I think he goes beyond the truth when he writes:

[W]e do not know how to create a significant amount of entanglement in more than a handful of quantum bits. It might be some fundamental rule of nature that prevents significant entanglement for any reasonable length of time. Or it could just be a tricky engineering problem. We'll have to let the physicists sort that out.

The thing is, physicists _do_ know how to create entanglement among many thousands or even millions of qubits--for example, in condensed-matter systems like spin lattices, and in superconducting Josephson junctions. The problem is "merely" that they don't know how to _control_ the entanglement in the precise ways needed for quantum computing. But as with much quantum computing skepticism, the passage above doesn't seem to grapple with _just how hard it is_ to kill off scalable QC. How do you cook up a theory that can account for the massively-entangled states that have already been demonstrated, but that _doesn 't_ give you all of [BQP](http://en.wikipedia.org/wiki/BQP)?

But let me not harp on these minor points, since _The Golden Ticket_ has so many pleasant features. One of them is its corny humor: even in Lance's fantasy world where a proof of P=NP has led to a cure for cancer, it still __hasn 't led to a cure for the common cold. Another nice feature is the book's refreshing matter-of-factness: Lance makes it clear that he believes that

(a) P≠NP,  
(b) the conjecture is provable but won't __be proven in the near future, and  
(c) if we ever meet an advanced extraterrestrial civilization, they'll also have asked the P vs. NP question or something similar to it.

Of course we can't currently _prove_ any of the above statements, just like we can't prove the nonexistence of Bigfoot. But Lance refuses to patronize his readers by pretending to harbor doubts that he quite reasonably doesn't.

In summary, if you're the sort of person who stops me in elevators to say that you like my blog even though you never actually understand anything in it, then stop reading _Shtetl-Optimized_ right now and [go read Lance's book](http://www.amazon.com/The-Golden-Ticket-ebook/dp/B00BKZYGUY/). You'll understand it and you'll enjoy it.

And now it's off to class, to apologize for my April Fools prank and to teach the Cook-Levin Theorem.
