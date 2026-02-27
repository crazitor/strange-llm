---
title: "This Week’s BS"
author: "Scott Aaronson"
date: "Fri, 05 May 2017"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=3248"
---

There are two pieces of BosonSampling-related news that people have asked me about this week.

First, a group in Shanghai, led by Chaoyang Lu and Jianwei Pan, has [reported in _Nature Photonics_](http://www.nature.com/nphoton/journal/vaop/ncurrent/full/nphoton.2017.63.html) that they can do BosonSampling with a coincidence rate that's higher than in previous experiments by a factor of several thousand.  This, in particular, lets them do BosonSampling with 5 photons.  Now, 5 might not sound like that much, especially since the group in Bristol [previously did 6-photon BosonSampling](https://scottaaronson.blog/?p=2435).  But to make their experiment work, the Bristol group needed to start its photons in the initial state |3,3〉: that is, two modes with 3 photons each.  This gives rise to matrices with repeated rows, whose permanents are much easier to calculate than the permanents of arbitrary matrices.  By contrast, the Shangai group starts its photons in the "true BosonSampling initial state" |1,1,1,1,1〉: that is, five modes with 1 photon each.  That's the kind of initial state we ultimately want.

The second piece of news is that on Monday, a group at Bristol--overlapping with the group we mentioned before--submitted a preprint to the arXiv with the provocative title ["No imminent quantum supremacy by boson sampling."](https://arxiv.org/abs/1705.00686)  In this paper, they give numerical evidence that BosonSampling, with n photons and m modes, can be approximately simulated by a classical computer in "merely" about n2n time (that is, the time needed to calculate a single n×n permanent), as opposed to the roughly mn time that one would need if one had to calculate permanents corresponding to _all_ the possible outcomes of the experiment.  As a consequence of that, they argue that achieving quantum supremacy via BosonSampling would probably require at least ~50 photons--which would in turn require a "step change" in technology, as they put it.

I completely agree with the Bristol group's view of the asymptotics.  In fact, Alex Arkhipov and I ourselves repeatedly told experimentalists, in our papers and talks about BosonSampling (the question came up often…), that the classical complexity of the problem should only be taken to scale like 2n, rather than like mn.  Despite not having a general proof that the problem could actually be solved in ~2n time in the worst case, we said that for two main reasons:

  1. Even under the most optimistic assumptions, our hardness reductions, from Gaussian permanent estimation and so forth, only yielded ~2n hardness, not ~mn hardness.  (Hardness reductions giving us important clues about the real world?  Whuda thunk??)
  2. _If_  our BosonSampling matrix is Haar-random--or otherwise not too skewed to produce outcomes with huge probabilities--then it's not hard to see that we can do approximate BosonSampling in O(n2n) time classically, by using rejection sampling.



Indeed, Alex and I insisted on these points despite some pushback from experimentalists, who were understandably hoping that they could get to quantum supremacy just by upping m, the number of modes, without needing to do anything heroic with n, the number of photons!  So I'm happy to see that a more careful analysis supports the guess that Alex and I made.

On the other hand, what does this mean for the number of photons needed for "quantum supremacy": is it 20? 30? 50?  I confess that that sort of question interests me much less, since it all depends on the details of how you define the comparison (are we comparing against ENIAC? a laptop? a server farm? how many cores? etc etc).  As I've often said, my real hope with quantum supremacy is to see a quantum advantage that's so overwhelming--so duh-obvious to the naked eye--that we don't have to squint or argue about the definitions.
