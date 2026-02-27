---
title: "My biology paper in Science (really)"
author: "Scott Aaronson"
date: "Fri, 22 Jul 2016"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=2862"
---

Think I'm pranking you, right?

You can [see the paper right here](http://science.sciencemag.org/content/353/6297/aad8559) ("Synthetic recombinase-based state machines in living cells," by Nathaniel Roquet, Ava P. Soleimany, Alyssa C. Ferris, Scott Aaronson, and Timothy K. Lu). [**Update (Aug. 3):** The previous link takes you to a paywall, but you can now [access the full text of our paper here](http://science.sciencemag.org/content/353/6297/aad8559.full?ijkey=wzroPPh1eIu9k&keytype=ref&siteid=sci). See also the Supplementary Material [here](http://science.sciencemag.org/content/suppl/2016/07/20/353.6297.aad8559.DC1).] You can also [read the _MIT News_ article](http://news.mit.edu/2016/biological-circuit-cells-remember-respond-stimuli-0721) ("Scientists program cells to remember and respond to series of stimuli"). In any case, _my_ little part of the paper will be fully explained in this post.

A little over a year ago, two MIT synthetic biologists--[Timothy Lu](http://www.rle.mit.edu/sbg/people/) and his PhD student Nate Roquet--came to my office saying they had a problem they wanted help with.  _Why me?_ I wondered. Didn't they realize I was a quantum complexity theorist, who so hated picking apart [owl pellets](https://en.wikipedia.org/wiki/Pellet_\(ornithology\)) and memorizing the names of cell parts in junior-high Life Science, that he avoided taking a single biology course since that time? (Not counting computational biology, taught in a CS department by Richard Karp.)

Nevertheless, I listened to my biologist guests--which turned out to be an excellent decision.

Tim and Nate told me about a DNA system with surprisingly clear rules, which led them to a strange but elegant combinatorial problem. In this post, first I need to spend some time to tell you the rules; then I can tell you the problem, and lastly its solution. There are no mathematical prerequisites for this post, and _certainly_ no biology prerequisites: everything will be completely elementary, like learning a card game. Pen and paper might be helpful, though.

As we all learn in kindergarten, DNA is a finite string over the 4-symbol alphabet {A,C,G,T}. We'll find it more useful, though, to think in terms of entire _chunks_ of DNA bases, which we'll label arbitrarily with letters like X, Y, and Z. For example, we might have X=ACT, Y=TAG, and Z=GATTACA.

We can also _invert_ one of these chunks, which means writing it backwards while also swapping the A's with T's and the G's with C's. We'll denote this operation by * (the technical name in biology is "reverse-complement"). For example:

X*=AGT, Y*=CTA, Z*=TGTAATC.

Note that (X*)*=X.

We can then combine our chunks and their inverses into a longer DNA string, like so:

ZYX*Y* = GATTACA TAG AGT CTA.

From now on, we'll work exclusively with the chunks, and forget completely about the underlying A's, C's, G's, and T's.

Now, there are also certain special chunks of DNA bases, called _recognition sites_ , which tell the little machines that read the DNA when they should start doing something and when they should stop. Recognition sites come in pairs, so we'll label them using various parenthesis symbols like ( ), [ ], { }. To convert a parenthesis into its partner, you invert it: thus ( = )*, [ = ]*, { = }*, etc. Crucially, the parentheses in a DNA string don't need to "face the right ways" relative to each other, and they also don't need to nest properly. Thus, both of the following are valid DNA strings:

X ( Y [ Z [ U ) V

X { Y ] Z { U [ V

Let's refer to X, Y, Z, etc.--the chunks that aren't recognition sites--as _letter-chunks_. Then it will be convenient to make the following simplifying assumptions:

  1. Our DNA string consists of an alternating sequence of recognition sites and letter-chunks, beginning and ending with letter-chunks. (If this weren't true, then we could just glom together adjacent recognition sites and adjacent letter-chunks, and/or add new dummy chunks, until it _was_ true.)
  2. Every letter-chunk that appears in the DNA string appears exactly once (either inverted or not), while every recognition site that appears, appears exactly twice. Thus, if there are n distinct recognition sites, there are 2n+1 distinct letter-chunks.
  3. Our DNA string can be decomposed into its constituent chunks _uniquely_ --i.e., it's always possible to tell which chunk we're dealing with, and when one chunk stops and the next one starts. In particular, the chunks and their reverse-complements are all distinct strings.



The little machines that read the DNA string are called _recombinases_. There's one kind of recombinase for each kind of recognition site: a (-recombinase, a [-recombinase, and so on. When, let's say, we let a (-recombinase loose on our DNA string, it searches for ('s and )'s and ignores everything else. Here's what it does:

  * If there are no ('s or )'s in the string, or only one of them, it does nothing.
  * If there are two ('s facing the same way--like ( ( or ) )--it deletes everything in between them, including the ('s themselves.
  * If there are two ('s facing opposite ways--like ( ) or ) (--it deletes the ('s, and inverts everything in between them.



Let's see some examples. When we apply [-recombinase to the string

A ( B [ C [ D ) E,

we get

A ( B D ) E.

When we apply (-recombinase to the same string, we get

A D* ] C* ] B* E.

When we apply _both_ recombinases (in either order), we get

A D* B* E.

Another example: when we apply {-recombinase to

A { B ] C { D [ E,

we get

A D [ E.

When we apply [-recombinase to the same string, we get

A { B D* } C* E.

When we apply both recombinases--ah, but here the order matters! If we apply { first and then [, we get

A D [ E,

since the [-recombinase now encounters only a single [, and has nothing to do. On the other hand, if we apply [ first and then {, we get

A D B* C* E.

Notice that inverting a substring can change the relative orientation of two recognition sites--e.g., it can change { { into { } or vice versa. It can thereby change what happens (inversion or deletion) when some future recombinase is applied.

One final rule: after we're done applying recombinases, we remove the remaining recognition sites like so much scaffolding, leaving only the letter-chunks. Thus, the final output

A D [ E

becomes simply A D E, and so on. Notice also that, if we happen to delete one recognition site of a given type while leaving its partner, the remaining site will _necessarily_ just bounce around inertly before getting deleted at the end--so we might as well "put it out of its misery," and delete it right away.

My coauthors have actually implemented all of this in a wet lab, which is what most of the _Science_ paper is about (my part is mostly in a technical appendix). They think of what they're doing as building a "biological state machine," which could have applications (for example) to programming cells for medical purposes.

But without further ado, let me tell you the math question they gave me. For reasons that they can explain better than I can, my coauthors were interested in the _information storage capacity_ of their biological state machine. That is, they wanted to know the answer to the following:

Suppose we have a fixed initial DNA string, with n pairs of recognition sites and 2n+1 letter-chunks; and we also have a recombinase for each type of recognition site. Then by choosing which recombinases to apply, as well as which order to apply them in, how many different DNA strings can we generate as output?

It's easy to construct an example where the answer is as large as 2n. Thus, if we consider a starting string like

A ( B ) C [ D ] E { F } G < H > I,

we can clearly make 24=16 different output strings by choosing which subset of recombinases to apply and which not. For example, applying [, {, and < (in any order) yields

A B C D* E F* G H* I.

There are also cases where the number of distinct outputs is less than 2n. For example,

A ( B [ C [ D ( E

can produce only 3 outputs--A B C D E, A B D E, and A E--rather than 4.

What Tim and Nate wanted to know was: can the number of distinct outputs ever be _greater_ than 2n?

Intuitively, it seems like the answer "has to be" yes. After all, we already saw that the order in which recombinases are applied can matter enormously. And given n recombinases, the number of possible permutations of them is n!, not 2n. (Furthermore, if we remember that any _subset_ of the recombinases can be applied in any order, the number of possibilities is even a bit greater--about e·n!.)

Despite this, when my coauthors played around with examples, they found that the number of distinct output strings never exceeded 2n. In other words, the number of output strings behaved _as if_ the order didn't matter, even though it does. The problem they gave me was either to explain this pattern or to find a counterexample.

I found that the pattern holds:

**Theorem:** Given an initial DNA string with n pairs of recognition sites, we can generate at most 2n distinct output strings by choosing which recombinases to apply and in which order.

Let a _recombinase sequence_ be an ordered list of recombinases, each occurring at most once: for example, ([{ means to apply (-recombinase, then [-recombinase, then {-recombinase.

The proof of the theorem hinges on one main definition. Given a recombinase sequence that acts on a given DNA string, let's call the sequence _irreducible_ if every recombinase in the sequence actually finds two recognition sites (and hence, inverts or deletes a nonempty substring) when it's applied. Let's call the sequence _reducible_ otherwise. For example, given

A { B ] C { D [ E,

the sequence [{ is irreducible, but {[ is reducible, since the [-recombinase does nothing.

Clearly, for every reducible sequence, there's a shorter sequence that produces the same output string: just omit the recombinases that don't do anything! (On the other hand, I leave it as an exercise to show that the converse is false. That is, even if a sequence is _ir_ reducible, there might be a shorter sequence that produces the same output string.)

**Key Lemma:** Given an initial DNA string, and given a subset of k recombinases, every irreducible sequence composed of all k of those recombinases produces the same output string.

Assuming the Key Lemma, let's see why the theorem follows. Given an initial DNA string, suppose you want to specify one of its possible output strings. I claim you can do this using only n bits of information. For you just need to specify which subset of the n recombinases you want to apply, in _some_ irreducible order. Since every irreducible sequence of those recombinases leads to the same output, you don't need to specify an order on the subset. Furthermore, for each possible output string S, there must be _some_ irreducible sequence that leads to S--given a reducible sequence for S, just keep deleting irrelevant recombinases until no more are left--and therefore some subset of recombinases you could pick that uniquely determines S. OK, but if you can specify each S uniquely using n bits, then there are at most 2n possible S's.

**Proof of Key Lemma.** Given an initial DNA string, let's assume for simplicity that we're going to apply all n of the recombinases, in some irreducible order. We claim that the final output string doesn't depend at all on _which_ irreducible order we pick.

If we can prove this claim, then the lemma follows, since given a proper subset of the recombinases, say of size k<n, we can simply glom together everything between one relevant recognition site and the next one, treating them as 2k+1 giant letter-chunks, and then repeat the argument.

Now to prove the claim. Given two letter-chunks--say A and B--let's call them _soulmates_ if either A and B or A* and B* will necessarily end up next to each other, whenever all n recombinases are applied in some irreducible order, and whenever A or B appears at all in the output string. Also, let's call them _anti-soulmates_ if either A and B* or A* and B will necessarily end up next to each other if either appears at all.

To illustrate, given the initial DNA sequence,

A [ B ( C ] D ( E,

you can check that A and C are anti-soulmates. Why? Because if we apply all the recombinases in an irreducible sequence, then at some point, the [-recombinase needs to get applied, and it needs to find both [ recognition sites. And one of these recognition sites will still be next to A, and the other will still be next to C (for what could have pried them apart? nothing). And when that happens, no matter where C has traveled in the interim, C* must get brought next to A. If the [-recombinase does an inversion, the transformation will look like

A [ … C ] → A C* …,

while if it does a deletion, the transformation will look like

A [ … [ C* → A C*

Note that C's [ recognition site will be to its left, if and only if C has been flipped to C*. In this particular example, A never moves, but if it did, we could repeat the analysis for A and _its_ [ recognition site. The conclusion would be the same: no matter what inversions or deletions we do first, we'll maintain the invariant that A and C* (or A* and C) will immediately jump next to each other, as soon as the [ recombinase is applied. And once they're next to each other, nothing will ever separate them.

Similarly, you can check that C and D are soulmates, connected by the ( recognition sites; D and B are anti-soulmates, connected by the [ sites; and B and E are soulmates, connected by the ( sites.

More generally, let's consider an arbitrary DNA sequence, with n pairs of recognition sites. Then we can define a graph, called the _soulmate graph_ , where the 2n+1 letter-chunks are the vertices, and where X and Y are connected by (say) a blue edge if they're soulmates, and by a red edge if they're anti-soulmates.

When we construct this graph, we find that every vertex has exactly 2 neighbors, one for each recognition site that borders it--save the first and last vertices, which border only one recognition site each and so have only one neighbor each. But these facts immediately determine the structure of the graph. Namely, it must consist of a simple _path_ , starting at the first letter-chunk and ending at the last one, together with possibly a disjoint union of cycles.

But we know that the first and last letter-chunks can never move anywhere. For that reason, a path of soulmates and anti-soulmates, starting at the first letter-chunk and ending at the last one, _uniquely determines_ the final output string, when the n recombinases are applied in any irreducible order. We just follow it along, switching between inverted and non-inverted letter-chunks whenever we encounter a red edge. The cycles contain the letter-chunks that necessarily get deleted along the way to that unique output string. This completes the proof of the lemma, and hence the theorem.

 

There are other results in the paper, like a generalization to the case where there can be k pairs of recognition sites of each type, rather than only one. In that case, we can prove that the number of distinct output strings is at most 2kn, and that it _can_ be as large as ~(2k/3e)n. We don't know the truth between those two bounds.

Why is this interesting? As I said, my coauthors had their own reasons to care, involving the number of bits one can store using a certain kind of DNA state machine. I got interested for a different reason: because this is a case where biology threw up a bunch of rules that _look_ like a random mess--the parentheses don't even need to nest correctly? inversion can  _also_ change the semantics of the recognition sites? evolution never thought about what happens if you delete one recognition site while leaving the other one?--and yet, on analysis, all the rules work in perfect harmony to produce a certain outcome. Change a single one of them, and the "at most 2n distinct DNA sequences" theorem would be false. Mind you, I'm still not sure what biological _purpose_ it serves for the rules to work in harmony this way, but they do.

But the point goes further. While working on this problem, I'd repeatedly encounter an aspect of the mathematical model that seemed weird and inexplicable--only to have Tim and Nate explain that the aspect made sense once you brought in additional facts from biology, facts not in the model they gave me. As an example, we saw that in the soulmate graph, the deleted substrings appear as cycles. But surely excised DNA fragments don't literally form loops? Why yes, apparently, they do. As a second example, consider the DNA string

A ( B [ C ( D [ E.

When we construct the soulmate graph for this string, we get the path

A-D-C-B-E.

Yet there's no actual recombinase sequence that leads to A D C B E as an output string! Thus, we see that it's possible to have a "phantom output," which the soulmate graph suggests should be reachable but that _isn 't_ actually reachable. According to my coauthors, that's because the "phantom outputs" _are_ reachable, once you know that in real biology (as opposed to the mathematical model), excised DNA fragments can also reintegrate back into the long DNA string.

Many of my favorite open problems about this model concern algorithms and complexity. For example: given as input an initial DNA string, does there _exist_ an irreducible order in which the recombinases can be applied? Is the "utopian string"--the string suggested by the soulmate graph--actually reachable? If it _is_ reachable, then what's the shortest sequence of recombinases that reaches it? Are these problems solvable in polynomial time? Are they NP-hard? More broadly, if we consider all the subsets of recombinases that can be applied in an irreducible order, or all the irreducible orders themselves, what combinatorial conditions do they satisfy? I don't know--if you'd like to take a stab, feel free to share what you find in the comments!

What I do know is this: I'm fortunate that, before they publish your first biology paper, the editors at  _Science_ don't call up your 7th-grade Life Science teacher to ask how you did in the owl pellet unit.

* * *

**More in the comments:**

  * Some notes on the [generalization](https://scottaaronson.blog/?p=2862#comment-1203242) to k pairs of recognition sites of each type
  * My coauthor Nathaniel Roquet's [comments](https://scottaaronson.blog/?p=2862#comment-1203346) on the biology



* * *

**Unrelated Announcement from My Friend Julia Wise (July 24):** Do you like science and care about humanity’s positive trajectory? July 25 is the final day to apply for [Effective Altruism Global 2016](http://eaglobal.org). From August 5-7 at UC Berkeley, a network of founders, academics, policy-makers, and more will gather to apply economic and scientific thinking to the world’s most important problems. Last year featured Elon Musk and the head of Google.org. This year will be headlined by Cass Sunstein, the co-author of Nudge. If you apply with this link, the organizers will give you a free copy of [Doing Good Better](http://eaglobal.org/application-form?group=dgb) by Will MacAskill. Scholarships are available for those who can’t afford the cost. [Read more here](http://eaglobal.org). [Apply here](http://eaglobal.org/application-form?group=dgb).
