---
title: "Another axe swung at the Sycamore"
author: "Scott Aaronson"
date: "Sun, 07 Mar 2021"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=5371"
---

So there's an interesting new paper on the arXiv by Feng Pan and Pan Zhang, entitled ["Simulating the Sycamore supremacy circuits."](https://arxiv.org/abs/2103.03074) It's about a new tensor contraction strategy for classically simulating Google's 53-qubit quantum supremacy experiment from Fall 2019. Using their approach, and using just 60 GPUs running for a few days, the authors say they managed to generate a million _correlated_ 53-bit strings--meaning, strings that all agree on a specific subset of 20 or so bits--that achieve a high linear cross-entropy score.

Alas, I haven't had time this weekend to write a "proper" blog post about this, but several people have by now emailed to ask my opinion, so I thought I'd share the brief response I sent to a journalist.

This does look like a significant advance on simulating Sycamore-like random quantum circuits! Since it's based on tensor networks, you don't need the literally largest supercomputer on the planet filling up tens of petabytes of hard disk space with amplitudes, as in the brute-force strategy [proposed by IBM](https://arxiv.org/abs/1910.09534). Pan and Zhang's strategy seems most similar to the strategy previously [proposed by Alibaba](https://arxiv.org/pdf/2005.06787.pdf), with the key difference being that the new approach generates millions of correlated samples rather than just one.

I guess my main thoughts for now are:

  1. Once you knew about this particular attack, you could evade it and get back to where we were before by switching to a more sophisticated verification test — namely, one where you not only computed a Linear XEB score for the observed samples, you _also_ made sure that the samples didn’t share too many bits in common. (Strangely, though, the paper never mentions this point.)
  2. The other response, of course, would just be to redo random circuit sampling with a slightly bigger quantum computer, like the ~70-qubit devices that Google, IBM, and others are now building!



Anyway, very happy for thoughts from anyone who knows more.
