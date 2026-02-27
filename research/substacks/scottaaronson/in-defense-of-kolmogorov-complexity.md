---
title: "In Defense of Kolmogorov Complexity"
author: "Scott Aaronson"
date: "Tue, 27 Sep 2011"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=791"
---

I got lots of useful and interesting feedback on my [last post](https://scottaaronson.blog/?p=762), though I also learned a valuable sociological lesson about the "two kinds of complexity theory":

_If you write about the kind of complexity theory that involves acronyms like NP, BQP/qpoly, and r.s.r., people will think the issues must be difficult and arcane, even if they 're not and can be understood with very little effort.  By contrast, if you write about the kind of complexity theory that can be illustrated using pictures of coffee cups, people will think the issues can be sorted out with 15 seconds of thought, and will happily propose 'solutions' that presuppose what needs to be explained, answer a different question, or fail in simple examples._

Seriously, a large number of commenters raised two important questions, which I'd like to address forthwith in this followup post.

The first question is why I omitted the notion of _coarse-graining_ , which plays a central role in many accounts of entropy and complexity. The short answer is that I shouldn't have omitted it.  In fact, as both [Sean Carroll](https://scottaaronson.blog/?p=762#comment-28584) and [Luca Trevisan](https://scottaaronson.blog/?p=762#comment-28598) (among others) quickly pointed out, one can tell a perfectly-reasonable story about the coffee cup by defining the "complextropy," not in terms of sophistication, but in terms of the _ordinary_ Kolmogorov complexity of a coarse-grained or "smeared-out" state.  If you define the complextropy that way, it should increase and then decrease as desired, and furthermore, it's probably easier to _prove_ that statement than using the sophistication-based definition (though both versions seem highly nontrivial to analyze).

So, the reason I turned to sophistication was basically just the mathematician's instinct to situate every concept in the most general structure where that concept makes sense.  For example, why define "connectedness" for polygons in the Euclidean plane, if the concept makes sense for arbitrary topological spaces?  Or in our case, why define "complextropy" for dynamical systems that happen to have a spatial structure over which one can coarse-grain, if the concept also makes sense for _arbitrary_ dynamical systems whose evolution is computable by an efficient algorithm?  Of course, **[OPEN PROBLEM ALERT]** it would be wonderful to know whether the two types of complextropy can be shown to be related for those dynamical systems for which they both make sense, or whether we can construct a convincing example that separates the two.

The second question is why I invoked Kolmogorov complexity in a discussion about thermodynamics: many people seemed to think that, by doing so, I was making some novel or controversial claim.  I wasn't.  People like Charles Bennett, Seth Lloyd, and Wojciech Zurek have employed Kolmogorov complexity as a useful language for thermodynamics since the 1980s; I was simply following in their footsteps.  Basically, what Kolmogorov complexity lets you do is talk in a well-defined way about the "entropy" or "randomness" of an _individual object_ , without reference to any ensemble from which the object was drawn.  And this is often extremely convenient: notice that Kolmogorov complexity snuck its way in even when we defined complextropy in terms of coarse-graining!

Of course, if our dynamical system is probabilistic, then we always _can_ talk instead about the "actual" entropy; in that case Kolmogorov complexity basically just amounts to a shorthand.  On the other hand, if our system is deterministic, then talking about the (resource-bounded) Kolmogorov complexity seems essential--since in that case there's no "true" randomness at all, only pseudorandomness.

But a few commenters went further, disparaging Kolmogorov complexity _itself_ rather than just its application to a particular problem.  Here's _Shtetl-Optimized_ regular [Raoul Ohio](https://scottaaronson.blog/?p=762#comment-28766):

As usual, my DAH (Devil’s Advocate Hat) is on. This is convenient, because it allows you to comment on anything without doing the work to really understanding it. Thus I will proceed to disparage the notion of using Kolmogorov Complexity (KC) for anything but entertainment.

Math is a subject where a couple of interesting definitions and a few theorems can launch a subfield such as KC. I have never studied KC … but a brief reading of the subject suggests that it started as a joke, and today a lot of people are not in on it.

… the KC of things would change as knowledge in other fields progresses. For example, what is the KC of

δ = 4.66920160910299067185320382…, and

α = 2.502907875095892822283902873218… ?

These are Feigenbaum’s constants (<http://en.wikipedia.org/wiki/Feigenbaum_constants>). A couple of decades ago, no one knew anything about these numbers. With the concept of analyzing discrete dynamical systems by bifurcation diagrams in hand, these can be calculated with a short program. So, did KC(δ) and KC(α) drop dramatically 20 odd years ago?

…using KC reminds me of physics arguments that use the wave function for the universe. Sure, there must be such a thing, but it is hard to say much about it.

On the other side of the coin, the theorems and proofs in basic KC are rather similar to those in many fields of TCS, and many SO [Shtetl-Optimized] readers might not think of these as a joke…

My intuition is that the entire concept of KC is “ill-posed”, to borrow a term from PDE.

In the interest of “full disclosure”, I must mention that often in the past I have thought some topic was a bunch of hooey until I understood it, after which I thought is was profound, just like listening to Lenard [sic] Cohen.

I wrote a reply to Raoul, and then decided that it should go into a top-level post, for the edification of Kolmogorov-skeptics everywhere.  So without further ado:

Hi Raoul!

I think this is indeed one of those cases where if you understood more, you'd see why your dismissal was wrong. And unlike with (say) art, music, or religion, the _reasons_ why your dismissal is wrong can be articulated in words!

Contrary to what you say, K(x) is _not_ undefinable: I'll define it right now, as the length of the shortest prefix-free program (in some fixed universal programming language) that prints x and then halts! K(x) _is_ _uncomputable_ , but that's a very different issue, and something that's been known since the 1960s.

Basically, what K(x) lets you do is give a clear, observer-independent _meaning_ to the loose notion of there "not existing any patterns" in a string. Already from that statement, it's _obvious_ that K(x) is going to be hard to compute--for as you correctly point out, detecting the existence or nonexistence of patterns is _hard_!

(Though contrary to what you say, K(Feigenbaum's constant) didn't suddenly become small when Feigenbaum defined the constant, any more than 42038542390523059230 suddenly became composite when I wrote it down, probably for the first time in human history. Please don't tell me that you make no distinction between mathematical truths and our knowledge of them!)

The key point is that, even without being able to _compute_ K(x) for most x's, you can still _use the definition_ of K(x) to give meaning to hundreds of intuitions that otherwise would've remained forever at a handwaving level. For example:

"The overwhelming majority of strings are patternless."

"If a short computer program outputs a patternless string, then it can only be doing so by generating the string randomly."

And many, many less obvious statements--every one of which can be upgraded to a _theorem_ once you have a mathematical definition of "patternlessness"!

Furthermore, the idea of Kolmogorov complexity has actually inspired some important experimental work! For example, _if_ you could compute K, then you could compute the "similarity" between two DNA sequences D1 and D2 by comparing K(D1)+K(D2) to K(D1,D2).

Of course you _can 't_ compute K, but you _can_ compute useful upper bounds on it. For example, let G(x) be the number of bits in the gzip compression of the string x. Then comparing G(D1)+G(D2) to G(D1,D2) has turned out to be a very useful way to measure similarity between DNA sequences.

It's really no different from how, even though we can never say whether a curve in the physical world is continuous or not (since that would require infinitely precise measurements), the mathematical _theories_ dealing with continuity (e.g., calculus, topology) can still be applied in physics in all sorts of ways.
