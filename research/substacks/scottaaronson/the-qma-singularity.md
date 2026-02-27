---
title: "The QMA Singularity"
author: "Scott Aaronson"
date: "Sat, 27 Sep 2025"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=9183"
---

**Update (Sep. 29):** Since this post has now gone semi-viral on X, Hacker News, etc., with people arguing about how trivial or nontrivial was GPT5's "discovery," it seems worthwhile to say something that was implicit in the post.

Namely, GPT5-Thinking's suggestion of a function to use "should have" been obvious to us. It _would have_ been obvious to us had we known more, or had we spent more time studying the literature or asking experts.

The point is, anyone engaged in mathematical research knows that an AI that can "merely" fill in the insights that "should've been" obvious to you is a really huge freaking deal! It speeds up the actual discovery process, as opposed to the process of writing LaTeX or preparing the bibliography or whatever. This post gave one tiny example of what I'm sure will soon be thousands.

I should also add that, since this post went up, a commenter named Phillip Harris [proposed a better function to use](https://scottaaronson.blog/?p=9183#comment-2016680) than GPT-5's: det(I-E) rather than Tr[(I-E)-1]. While we're still checking details, not only do we think this works, we think it simplifies our argument and solves one of our open problems. So it seems human supremacy has been restored, at least for now!

* * *

A couple days ago, Freek Witteveen of CWI and I posted a paper to the arXiv called ["Limits to black-box amplification in QMA."](https://arxiv.org/abs/2509.21131) Let me share the abstract:

> We study the limitations of black-box amplification in the quantum complexity class QMA. Amplification is known to boost any inverse-polynomial gap between completeness and soundness to exponentially small error, and a recent result (Jeffery and Witteveen, 2025) shows that completeness can in fact be amplified to be doubly exponentially close to 1. We prove that this is optimal for black-box procedures: we provide a quantum oracle relative to which no QMA verification procedure using polynomial resources can achieve completeness closer to 1 than doubly exponential, or a soundness which is super-exponentially small. This is proven by using techniques from complex approximation theory, to make the oracle separation from (Aaronson, 2008), between QMA and QMA with perfect completeness, quantitative.

You can also [check out my PowerPoint slides here](https://www.scottaaronson.com/talks/two-oracles.pptx).

To explain the context: [QMA](https://en.wikipedia.org/wiki/QMA), or Quantum Merlin Arthur, is the canonical quantum version of NP. It's the class of all decision problems for which, if the answer is "yes," then Merlin can send Arthur a quantum witness state that causes him to accept with probability at least 2/3 (after a polynomial-time quantum computation), while if the answer is "no," then regardless of what witness Merlin sends, Arthur accepts with probability at most 1/3. Here, as usual in complexity theory, the constants 2/3 and 1/3 are just conventions, which can be replaced (for example) by 1-2-n and 2-n using amplification.

A longstanding open problem about QMA--not the biggest problem, but arguably the most annoying--has been whether the 2/3 can be replaced by 1, as it can be for classical MA for example. In other words, does QMA = QMA1, where QMA1 is the subclass of QMA that admits protocols with "perfect completeness"? In 2008, I used real analysis to [show that there's a quantum oracle](https://arxiv.org/abs/0806.0450) relative to which QMA ≠ QMA1, which means that any proof of QMA = QMA1 would need to use "quantumly nonrelativizing techniques" (not at all an insuperable barrier, but at least we learned _something_ about why the problem is nontrivial).

Then came a bombshell: in June, [Freek Witteveen](https://www.cwi.nl/en/people/freek-witteveen/) and longtime friend-of-the-blog [Stacey Jeffery](https://homepages.cwi.nl/~jeffery/) released a [paper](https://arxiv.org/abs/2506.15551) showing that any QMA protocol can be amplified, in a black-box manner, to have completeness error that's _doubly_ exponentially small, 1/exp(exp(n)). They did this via a method I never would've thought of, wherein a probability of acceptance is encoded via the amplitudes of a quantum state that decrease in a geometric series. QMA, it turned out, was an old friend that still had surprises up its sleeve after a quarter-century.

In August, we had Freek speak about this breakthrough by Zoom in our quantum group meeting at UT Austin. Later that day, I asked Freek whether their new protocol was the _best_ you could hope to do with black-box techniques, or whether for example one could amplify the completeness error to be _triply_ exponentially small, 1/exp(exp(exp(n))). About a week later, Freek and I had a full proof written down that, using black-box techniques, doubly-exponentially small completeness error is the best you can do. In other words: we showed that, when one makes my 2008 QMA ≠ QMA1 quantum oracle separation quantitative, one gets a lower bound that _precisely_ matches Freek and Stacey's protocol.

All this will, I hope, interest and excite aficianados of quantum complexity classes, while others might have very little reason to care.

But here's a reason why other people might care. This is the first paper I've ever put out for which a key technical step in the proof of the main result came from AI--specifically, from GPT5-Thinking. Here was the situation: we had an N×N Hermitian matrix E(θ) (where, say, N=2n), each of whose entries was a poly(n)-degree trigonometric polynomial in a real parameter θ. We needed to study the largest eigenvalue of E(θ), as θ varied from 0 to 1, to show that this λmax(E(θ)) couldn't start out close to 0 but then spend a long time "hanging out" ridiculously close to 1, like 1/exp(exp(exp(n))) close for example.

Given a week or two to try out ideas and search the literature, I'm pretty sure that Freek and I could've solved this problem ourselves. Instead, though, I simply asked GPT5-Thinking. After five minutes, it gave me something confident, plausible-looking, and (I could tell) wrong. But rather than laughing at the silly AI like a skeptic might do, I _told_ GPT5 how I knew it was wrong. It thought some more, apologized, and tried again, and gave me something better. So it went for a few iterations, much like interacting with a grad student or colleague. Within a half hour, it had suggested to look at the function

$$ Tr[(I-E(\theta))^{-1}] = \sum_{i=1}^N \frac{1}{1-\lambda_i(\theta)}. $$

It pointed out, correctly, that this was a rational function in θ of controllable degree, that happened to encode the relevant information about how close the largest eigenvalue λmax(E(θ)) is to 1. And this … _worked_ , as we could easily check ourselves with no AI assistance. And I mean, maybe GPT5 had seen this or a similar construction somewhere in its training data. But there's not the slightest doubt that, if a student had given it to me, I would've called it clever. Obvious with hindsight, but many such ideas are.

I had tried similar problems a year ago, with the then-new GPT reasoning models, but I didn't get results that were nearly as good. Now, in September 2025, I'm here to tell you that AI has finally come for what my experience tells me is the most quintessentially human of all human intellectual activities: namely, proving oracle separations between quantum complexity classes. Right now, it almost certainly _can 't_ write the whole research paper (at least if you want it to be correct and good), but it _can_ help you get unstuck if you otherwise know what you're doing, which you might call a sweet spot. Who knows how long this state of affairs will last? I guess I should be grateful that I have tenure.
