---
title: "Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton"
author: "Scott Aaronson"
date: "Tue, 27 May 2014"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=1818"
---

**Update (June 3):** A few days after we posted this paper online, [Brent Werness](http://www.math.washington.edu/~bwerness/), a postdoc in probability theory at the University of Washington, discovered a serious error in the "experimental" part of the paper. Happily, Brent is now collaborating with us on producing a new version of the paper that fixes the error, which we hope to have available within a few months (and which will replace the version currently on the arXiv).

To make a long story short: while the overall idea, of measuring "apparent complexity" by the compressed file size of a coarse-grained image, is fine, the "interacting coffee automaton" that we study in the paper is **not** an example where the apparent complexity becomes large at intermediate times. That fact can be deduced as a corollary of a [result of Liggett from 2009](http://www.math.ucla.edu/~tml/cltexc5.pdf) about the "symmetric exclusion process," and can be seen as a far-reaching generalization of a result that we prove in our paper's appendix: namely, that in the _non_ -interacting coffee automaton (our "control case"), the apparent complexity after t time steps is upper-bounded by O(log(nt)). As it turns out, we were _more right than we knew_ to worry about large-deviation bounds giving complete mathematical control over what happens when the cream spills into the coffee, thereby preventing the apparent complexity from ever becoming large!

But what about our numerical results, which showed a small but unmistakable complexity bump for the interacting automaton (figure 10(a) in the paper)? It now appears that the complexity bump we saw in our data is likely to be explainable by an incomplete removal of what we called "border pixel artifacts": that is, "spurious" complexity that arises merely from the fact that, at the border between cream and coffee, we need to round the fraction of cream up or down to the nearest integer to produce a grayscale. In the paper, we devoted a whole section (Section 6) to border pixel artifacts and the need to deal with them: something sufficiently non-obvious that in the comments of this post, you can find people arguing with me that it's a non-issue. Well, it now appears that we erred by _underestimating_ the severity of border pixel artifacts, and that a better procedure to get rid of them would also eliminate the complexity bump for the interacting automaton.

Once again, this error has no effect on either the _general idea_ of complexity rising and then falling in closed thermodynamic systems, _or_ our proposal for how to quantify that rise and fall--the two aspects of the paper that have generated the most interest. But we made a bad choice of model system with which to illustrate those ideas. Had I looked more carefully at the data, I could've noticed the problem before we posted, and I take responsibility for my failure to do so.

The good news is that _ultimately_ , I think the truth only makes our story more interesting. For it turns out that apparent complexity, as we define it, is _not_ something that's trivial to achieve by just setting loose a bunch of randomly-walking particles, which bump into each other but are otherwise completely independent. If you want "complexity" along the approach to thermal equilibrium, you need to work a bit harder for it. One promising idea, which we're now exploring, is to consider a cream tendril whose _tip_ takes a random walk through the coffee, leaving a trail of cream in its wake. Using results in probability theory--closely related, or so I'm told, to the results for which [Wendelin Werner](http://www-history.mcs.st-andrews.ac.uk/Biographies/Werner_Wendelin.html) won his Fields Medal!--it may even be possible to _prove analytically_ that the apparent complexity becomes large in thermodynamic systems with this sort of behavior, much as one can prove that the complexity  _doesn 't_ become large in our original coffee automaton.

So, if you're interested in this topic, stay tuned for the updated version of our paper. In the meantime, I wish to express our deepest imaginable gratitude to Brent Werness for telling us all this.

* * *

Good news! After nearly three years of procrastination, fellow blogger [Sean Carroll](http://www.preposterousuniverse.com/blog/), former MIT undergraduate Lauren Ouellette, and yours truly [finally finished a paper with the above title](http://www.scottaaronson.com/papers/coffee2.pdf) (coming soon to an arXiv near you). [PowerPoint slides](http://www.scottaaronson.com/talks/coffee.ppt) are also available (as usual, you're on your own if you can't open them--sorry!).

For the background and context of this paper, please see my old post ["The First Law of Complexodynamics,"](https://scottaaronson.blog/?p=762) which discussed Sean's problem of defining a "complextropy" measure that first increases and then decreases in closed thermodynamic systems, in contrast to entropy (which increases monotonically). In this exploratory paper, we basically do five things:

  1. We survey several candidate "complextropy" measures: their strengths, weaknesses, and relations to one another.
  2. We propose a model system for studying such measures: a probabilistic cellular automaton that models a cup of coffee into which cream has just been poured.
  3. We report the results of numerical experiments with one of the measures, which we call "apparent complexity" (basically, the gzip file size of a smeared-out image of the coffee cup). The results confirm that the apparent complexity does indeed increase, reach a maximum, then turn around and decrease as the coffee and cream mix.
  4. We discuss a technical issue that one needs to overcome (the so-called "border pixels" problem) before one can do meaningful experiments in this area, and offer a solution.
  5. We raise the open problem of _proving analytically_ that the apparent complexity ever becomes large for the coffee automaton. To underscore this problem's difficulty, we prove that the apparent complexity _doesn 't_ become large in a simplified version of the coffee automaton.



Anyway, here's the abstract:

> In contrast to entropy, which increases monotonically, the "complexity" or "interestingness" of closed systems seems intuitively to increase at first and then decrease as equilibrium is approached. For example, our universe lacked complex structures at the Big Bang and will also lack them after black holes evaporate and particles are dispersed. This paper makes an initial attempt to quantify this pattern. As a model system, we use a simple, two-dimensional cellular automaton that simulates the mixing of two liquids ("coffee" and "cream"). A plausible complexity measure is then the Kolmogorov complexity of a coarse-grained approximation of the automaton's state, which we dub the "apparent complexity." We study this complexity measure, and show analytically that it never becomes large when the liquid particles are non-interacting. By contrast, when the particles do interact, we give numerical evidence that the complexity reaches a maximum comparable to the "coffee cup's" horizontal dimension. We raise the problem of proving this behavior analytically.

Questions and comments more than welcome.

* * *

In unrelated news, Shafi Goldwasser has asked me to announce that the [Call for Papers](http://www.scottaaronson.com/itcs-cfp.docx) for the 2015 Innovations in Theoretical Computer Science (ITCS) conference is now available.
