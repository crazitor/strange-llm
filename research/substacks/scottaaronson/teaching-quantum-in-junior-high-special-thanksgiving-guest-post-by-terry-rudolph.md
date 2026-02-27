---
title: "Teaching quantum in junior high: special Thanksgiving guest post by Terry Rudolph"
author: "Scott Aaronson"
date: "Thu, 22 Nov 2018"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=3997"
---

Happy [Thanksgiving](http://slatestarcodex.com/2013/11/28/the-story-of-thanksgiving-is-a-science-fiction-story/)!

People have sometimes asked me: "how do you do it?  how do you do your research, write papers, teach classes, mentor grad students, build up the quantum center at UT, travel and give talks every week or two, serve on program committees, raise two rambunctious young kids, and _also_ blog and _also_ participate in the comments and _also_ get depressed about people saying mean things on social media?"  The answer is that increasingly I don't.  _Something_ has to give, and this semester, alas, that something has often been blogging.

And that's why, today, I'm delighted to have a special guest post by my good friend [Terry Rudolph](https://www.imperial.ac.uk/people/t.rudolph).  Terry, who happens to be Erwin Schrödinger's grandson, has done lots of fascinating work over the years in quantum computing and the foundations of quantum mechanics, and previously came up on this blog in the context of the [PBR (Pusey-Barrett-Rudolph) Theorem](https://en.wikipedia.org/wiki/PBR_theorem).  Today, he's a cofounder and chief architect at [PsiQuantum](https://psiquantum.com/), a startup in Palo Alto that's trying to build silicon-photonic quantum computers.

Terry's guest post is about the prospects for teaching quantum theory at the junior high school level--something he thought about a lot in the context of writing his interesting recent book [Q is for Quantum](https://www.amazon.com/Q-Quantum-Terry-Rudolph/dp/0999063502).  I should stress that the opinions in this post are Terry's, and don't necessarily reflect the official editorial positions of _Shtetl-Optimized_.  Personally, I _have_ [taught the basics of quantum information](https://www.scottaaronson.com/writings/highschool.html) to sharp junior high and high school students, so I certainly know that it's possible.  (By undergrad, it's not only [possible](https://scottaaronson.blog/?p=3943), but maybe should become standard for both physics and CS majors.)  But I would also say that, given the current state of junior high and high school education in the US, it would be a huge step up if most students graduated fully understanding what's a probability, what's a classical bit, what's a complex number, and any of dozens of other topics that feed into quantum information--so why not start by teaching the simpler stuff well?  And also, if students don't learn the rules of classical probability first, then how will they be properly shocked when they come to quantum? 

But without further ado, here's Terry--who's also graciously agreed to stick around and answer some comments.

* * *

**Can we/should we teach Quantum Theory in Junior High?******

by Terry Rudolph

**Should we?**

Reasons which suggest the answer is "yes" include:

_Economic:_ We are apparently [into a labor market shortage in quantum engineers](https://www.nytimes.com/2018/10/21/technology/quantum-computing-jobs-immigration-visas.html).  We should not, however, need the recent hype around quantum computing to make the economic case - the frontier of many disparate regions of the modern science and technology landscape is quantum.  Surely if students do decide to drop out of school at 16 they should at least be equipped to get an entry-level job as a quantum physicist?

_Educational:_ If young peoples' first exposures to science are counterintuitive and "cutting edge," it could help excite them into STEM.  The strong modern quantum information theoretic connections between quantum physics, computer science and math can help all three subjects constructively generate common interest.

_Pseudo-Philosophical:_ Perhaps our issues with understanding/accepting quantum theory are because we come to it late and have lost the mental plasticity for a "quantum reset" of our brain when we eventually require it late in an undergraduate degree.  It may be easier to achieve fluency in the "language of quantum" with early exposure.

**Can we?**

There are two distinct aspects to this question: Firstly, is it possible at the level of "fitting it in" - training teachers, adjusting curricula and so on?  Secondly, can a nontrivial, worthwhile fraction of quantum theory even be taught at all to pre-calculus students?

With regards to the first question, as the child of two schoolteachers I am very aware that an academic advocating for such disruption will not be viewed kindly by all.  As I don't have relevant experience to say anything useful about this aspect, I have to leave it for others to consider.

Let me focus for the remainder of this post on the second aspect, namely whether it is even possible to appropriately simplify the content of the theory.  This month it is exactly 20 years since I lectured the first of many varied quantum courses I have taught at multiple universities. For most of that period I would have said it simply wasn't possible to teach any but the most precocious of high school students nontrivial technical content of quantum theory - despite some brave attempts like Feynman's use of arrows in _QED: The Strange Theory of Light and Matter_ (a technique that cannot easily get at the mysteries of two-particle quantum theory, which is where the fun really starts).  I now believe, however, that it _is_ actually possible.

**A pedagogical method covering nontrivial quantum theory using only basic arithmetic**

My experience talking about quantum theory to 12-15 year olds has only been in the idealized setting of spending a few hours with them at science fairs, camps and similar.  In fact it was on the way to a math camp for very young students, desperately trying to plan something non-trivial to engage them with, that I came up with a pedagogical method which I (and a few colleagues) have found does work.

I eventually wrote the method into a short book [Q is for Quantum](http://www.qisforquantum.org), but if you don't want to [purchase the book](https://www.amazon.com/Q-Quantum-Terry-Rudolph/dp/0999063502) then [here is a pdf of Part I,](http://qisforquantum.org/wp-content/uploads/2018/11/PART-I-draft-Q-is-for-Quantum.pdf), which takes a student knowing only the rules of basic arithmetic through to learning enough quantum computing they can understand the [Deutsch–Jozsa algorithm](https://en.wikipedia.org/wiki/Deutsch–Jozsa_algorithm).  In fact not only can they do a calculation to see how it works in detail, they can appreciate conceptual nuances often under-appreciated in popular expositions, such as why gate speed doesn't matter - it's all about the number of steps, why classical computing also can have exponential growth in "possible states" so interference is critical, why quantum computers do not compute the uncomputable and so on.

Before pointing out a few features of the approach, here are some rules I set myself while writing the book:

  * No analogies, no jargon - if it can't be explained quantitatively then leave it out.
  * No math more than basic arithmetic and distribution across brackets.
  * Keep clear the distinction between mathematical objects and the observed physical events they are describing.
  * Be interpretationally neutral.
  * No soap opera: Motivate by intriguing with science, not by regurgitating quasi-mythological stories about the founders of the theory.
  * No using the word "quantum" in the main text! This was partly to amuse myself, but I also thought if I was succeeding in the other points then I should be able to avoid a word almost synonymous with "hard and mysterious."



One of the main issues to confront is how to represent and explain superposition.  It is typical in popular expositions to draw analogies between a superposition of, say, a cat which is dead and a cat which is alive by saying it is dead "and" alive.  But if superposition was equivalent to logical "and", or, for that matter, logical "or", then quantum computing wouldn't be interesting, and in this and other ways the analogy is ultimately misleading.  The approach I use is closer to the latter - an unordered list of possible states for a system (which is most like an "or") can be used to represent a superposition. Using a list has some advantages - it is natural to apply a transformation to all elements of a list, for instance doubling the list of ingredients in a recipe.  More critically, given two independent lists of possibilities the new joint list of combined possibilities is a natural concept.  This makes teaching the equivalent of the Kronecker (tensor) product for multiple systems easy, something often a bit tricky even for undergrads to become comfortable with.

Conceptually the weirdest part of the whole construction, particularly for someone biased by the standard formalism, is that I use a standard mathematical object (a negative or minus sign) applied to a _diagram_ of a physical object (a black or white ball).  Moreover, positive and negative balls in a diagram can cancel out (interfere).  This greatly simplifies the exposition, by removing a whole level of abstraction in the standard theory (we do not need to use a vector containing entries whose specific ordering must be remembered in order to equate them to the physical objects).  While it initially seemed odd to me personally to do this, I have yet to have any young person think of it as any more weird than using the negative sign on a number.  And if it is always kept clear that drawing and manipulating the whole diagram is an abstract thing we do, which may or may not have any correspondence to what is "really going on" in the physical setups we are describing, then there really is no difference.

There are some subtleties about the whole approach - while the formalism is universal for quantum computing, it can only make use of unitary evolution which is _proportional_ to a matrix with integer entries.  Thus the [Hadamard gate](https://en.wikipedia.org/wiki/Quantum_logic_gate#Hadamard_\(H\)_gate) (PETE box) is ok, the [Controlled-NOT](https://en.wikipedia.org/wiki/Quantum_logic_gate#Controlled_\(cX_cY_cZ\)_gates) and [Toffoli](https://en.wikipedia.org/wiki/Toffoli_gate) likewise, but a seemingly innocuous gate like the controlled-Hadamard is not capable of being incorporated (without adding a whole bunch of unintuitive and unjustified rules).  The fact the approach covers a universal gate set means some amazing things can be explained in this simple diagrammatic language.  For example, the recent paper [Quantum theory cannot consistently describe the use of itself](https://www.nature.com/articles/s41467-018-05739-8), which led to [considerable discussion on this blog](https://scottaaronson.blog/?p=3975), can be fully reproduced.  That is, a high school student can in principle understand the technical details of a contemporary argument between professional physicists.  I find this amazing.

Based on communication with readers I have come to realize the people at most risk of being confused by the book are actually those already with a little knowledge - someone who has done a year or two's worth of undergraduate quantum courses, or someone who has taken things they read in pop-sci books too literally.  Initially, as I was developing the method, I thought it would be easy to keep "touching base" with the standard vector space formalism.  But in fact it becomes very messy to do so (and irrelevant for someone learning quantum theory for the first time).  In the end I dropped that goal, but now realize I need to develop some supplementary notes to help someone in that situation.

_Q is for Quantum_ is certainly not designed to be used as a classroom text - if nothing else my particular style and choice of topics will not be to others' tastes, and I haven't included all the many, many simple examples and exercises I have students doing along with me in class when I actually teach this stuff.  It should be thought of as more a "proof of principle," that the expository challenge can be met.  Several colleagues have used parts of these ideas already for teaching, and they have given me some great feedback.  As such I am planning on doing a revised and slightly expanded version at some point, so if you read it and have thoughts for improvement please send me them.
