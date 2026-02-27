---
title: "Logicians on safari"
author: "Scott Aaronson"
date: "Thu, 02 Nov 2006"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=152"
---

Sean Carroll, who many of you know from [Cosmic Variance](http://cosmicvariance.com/), asked the following question in response to my last entry:

> I'm happy to admit that I don't know anything about "one-way functions and interactive proofs." So, in what sense has theoretical computer science contributed more in the last 30 years to our basic understanding of the universe than particle physics or cosmology? (Despite the fact that I'm a cosmologist, I don't doubt your statement -- I'd just like to be able to explain it in public.)

I posted my response as a comment, but it's probably better to make it an entry of its own. So:

Hi Sean,

Thanks for your question!

Of course I was joking when I mentioned "objective standards" for ranking scientific fields. Depending on which questions keep you up at night, different parts of "humankind's basic picture of the universe" will seem larger or smaller. (To say that, of course, is not to suggest any relativism about the picture itself.)

What I can do, though, is to tell you why -- by my own subjective standards -- the contributions of theoretical computer science over the last 30 years rival those of theoretical physics or any other field I know about. Of course, people will say I only think that because I'm a theoretical computer scientist, but that gets the causal arrow wrong: I became a theoretical computer scientist because, as a teenager, I thought it!

It's probably best to start with some examples.

  1. We now know that, if an alien with enormous computational powers came to Earth, it could prove to us whether White or Black has the winning strategy in chess. To be convinced of the proof, we would _not_ have to trust the alien or its exotic technology, and we would _not_ have to spend billions of years analyzing one move sequence after another. We'd simply have to engage in a short conversation with the alien about the sums of certain polynomials over finite fields.
  2. There's a finite (and not unimaginably-large) set of boxes, such that if we knew how to pack those boxes into the trunk of your car, then we'd also know a proof of the Riemann Hypothesis. Indeed, _every_ formal proof of the Riemann Hypothesis with at most (say) a million symbols corresponds to some way of packing the boxes into your trunk, and vice versa. Furthermore, a list of the boxes and their dimensions can be feasibly written down.
  3. Supposing you do prove the Riemann Hypothesis, it's possible to convince someone of that fact, _without revealing anything other than the fact that you proved it_. It's also possible to write the proof down in such a way that someone else could verify it, with very high confidence, having only seen 10 or 20 bits of the proof.
  4. If every second or so your computer's memory were wiped completely clean, except for the input data; the clock; a static, unchanging program; and a counter that could only be set to 1, 2, 3, 4, or 5, it would still be possible (given enough time) to carry out an arbitrarily long computation -- just as if the memory weren't being wiped clean each second. This is almost certainly _not_ true if the counter could only be set to 1, 2, 3, or 4. The reason 5 is special here is pretty much the same reason it's special in Galois' proof of the unsolvability of the quintic equation.
  5. It would be great to prove that RSA is unbreakable by classical computers. But every known technique for proving that would, if it worked, simultaneously give an algorithm for _breaking_ RSA! For example, if you proved that RSA with an n-bit key took n5 steps to break, you would've discovered an algorithm for breaking it in 2n^1/5 steps. If you proved that RSA took 2n^1/3 steps to break, you would've discovered an algorithm for breaking it in n(log n)^2 steps. As you show the problem to be harder, you simultaneously show it to be easier.



Alright, let me stop before I get carried away. The examples I've listed (and hundreds more like them) are not exactly discoveries about _physics_ , but they don't have the flavor of pure math either. And even if they have some practical implications for computing (which they do), they certainly don't have the flavor of nitty-gritty software engineering.

So what are they then? Maybe it's helpful to think of them as "quantitative epistemology": discoveries about the capacities of finite beings like ourselves to learn mathematical truths. On this view, the theoretical computer scientist is basically a mathematical logician on a safari to the physical world: someone who tries to understand the universe by asking what sorts of mathematical questions can and can't be answered within it. Not _whether_ the universe is a computer, but what _kind_ of computer it is! Naturally, this approach to understanding the world tends to appeal most to people for whom math (and especially discrete math) is reasonably clear, whereas physics is extremely mysterious.

In my opinion, one of the biggest challenges for our time is to integrate the enormous body of knowledge in theoretical computer science (or quantitative epistemology, or whatever you want to call it) with the rest of what we know about the universe. In the past, the logical safari mostly stayed comfortably within 19th-century physics; now it's time to venture out into the early 20th century. Indeed, that's exactly why I chose to work on quantum computing: not because I want to build quantum computers (though I wouldn't mind that), but because I want to know what a universe that allows quantum computers is _like_.

Incidentally, it's also why I try hard to keep up with your field. If I'm not mistaken, less than a decade ago cosmologists made an _enormous_ discovery about the capacity of finite beings to learn mathematical truths: namely, that no computation carried out in the physical world can ever involve more than 1/Λ ~ 10122 bits.

Best,  
Scott
