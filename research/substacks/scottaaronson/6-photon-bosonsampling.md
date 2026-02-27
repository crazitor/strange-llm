---
title: "6-photon BosonSampling"
author: "Scott Aaronson"
date: "Wed, 19 Aug 2015"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=2435"
---

The news is more-or-less what the title says!

In _Science_ , a group led by Anthony Laing at Bristol has now [reported BosonSampling with 6 photons](http://www.sciencemag.org/content/349/6249/711.full.pdf), beating their own [previous record](http://www.nature.com/nphoton/journal/v8/n8/abs/nphoton.2014.152.html#close) of 5 photons, as well as the [earlier record](http://arxiv.org/abs/1212.2622) of 4 photons achieved a few years ago by the Walmsley group at Oxford (as well as the 3-photon experiments done by groups around the world). I only learned the big news from a [commenter on this blog](https://scottaaronson.blog/?p=2408#comment-782071), after the paper was already published (protip: if you've pushed forward the BosonSampling frontier, feel free to shoot me an email about it).

As several people explain in the comments, the _main_ advance in the paper is arguably not increasing the number of photons, but rather the fact that the device is completely reconfigurable: you can try hundreds of different unitary transformations with the same chip. In addition, the 3-photon results have an unprecedentedly high fidelity (about 95%).

The 6-photon results are, of course, consistent with quantum mechanics: the transition amplitudes are indeed given by permanents of 6×6 complex matrices. Key sentence:

After collecting 15 sixfold coincidence events, a confidence of P = 0.998 was determined that these are drawn from a quantum (not classical) distribution.

No one said scaling BosonSampling would be easy: I'm guessing that it took weeks of data-gathering to get those 15 coincidence events. Scaling up further will probably require improvements to the sources.

There's also a caveat: their initial state consisted of 2 modes with 3 photons each, as opposed to what we _really_ want, which is 6 modes with 1 photon each. (Likewise, in the Walmsley group's 4-photon experiments, the initial state consisted of 2 modes with 2 photons each.) If the number of modes stayed 2 forever, then the output distributions would remain easy to sample with a classical computer no matter how many photons we had, since we'd then get permanents of matrices with only 2 distinct rows. So "scaling up" needs to mean increasing not only the number of photons, but also the number of sources.

Nevertheless, this is an obvious step forward, and it came sooner than I expected. Huge congratulations to the authors on their accomplishment!

But you might ask: given that 6×6 permanents are still pretty easy for a classical computer (the more so when the matrices have only 2 distinct rows), why should anyone care? Well, the new result has major implications for what I've always regarded as the central goal of quantum computing research, much more important than breaking RSA or Grover search or even quantum simulation: namely,  _getting Gil Kalai to admit he was wrong_. Gil is on record, repeatedly, on this blog as well as his (see for example [here](https://gilkalai.files.wordpress.com/2014/06/aiq7.png)), as saying that he doesn't think BosonSampling will ever be possible even with 7 or 8 photons. I don't know whether the 6-photon result is giving him second thoughts (or sixth thoughts?) about that prediction.
