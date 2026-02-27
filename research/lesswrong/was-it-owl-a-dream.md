---
title: "Was It Owl a Dream?"
author: "Yovel Rom"
date: "2026-02-23"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/kFiQciPym6DQdWJJ2/was-it-owl-a-dream-1"
score: 14
votes: 6
---

I try to apply mechanical interpretability to understand token entanglement in subliminal learning, fail, and come to suspect subliminal learning is not caused by token entanglement.

Abstract
========

Subliminal learning is the phenomenon of transferring knowledge to a model by fine tuning it on unrelated tokens, for example liking owls by a series of numbers. A paper published last year by Zur et al claimed that this phenomenon is caused by specific tokens in the stream, whose logits especially increased when prompted by that fact, which are dubbed “entangled tokens”. 

I used logit lens to look at the alignment of the residual stream with both the animal and the entangled tokens. It seems that while logits of the animal increase throughout the model, the numeric tokens’ logits remain constant. In addition, it seems that all numeric tokens increased or decreased by similar amount, depending on the tokens. 

This is suggestive that entangled tokens are not actually related to the subliminal learning, since the model does not actually process them, and the same information is contained in all numeric tokens (either all numeric tokens get higher or lower logits) . 

Foreword
========

I tried to apply to Neel Nanda’s mech interp stream in MATS 10. To do that, I did one night’s worth of research. Even though I wasn’t accepted, I thought the results were worth sharing. I rewrote my summary to make it clearer, but didn’t do any further research.

I have a decade of experience in applied ML research, and am trying to transition into working in AI safety full time. If my writing interested you, feel free to reach out!

Background
==========

In July 2025, [Cloud et al](https://alignment.anthropic.com/2025/subliminal-learning/) published a paper claiming the following: If you prompt a model to (for instance) love owls, imbue its love in a series of numbers, then fine tune the model on those numbers, the resulting models will learn to love owls. They called this phenomenon “subliminal learning”. This is bonkers, so I decided to try and interpret it using mechanical interpretability tools. What says “model biology” more than owls?

I found a follow up paper named [It’s Owl in the Numbers](https://owls.baulab.info/) by Zur et al. It claims that the phenomenon is caused by entanglement- because the dimension of the residual stream is lower than that of the final output, some unrelated tokens become correlated, and the probability of one increases whenever the others’ does. They find some number tokens whose probability increases when the model is prompted to like certain animals.  For example, they prompt the model with love for owls, then check the model’s logits for the next token for the prompt “my favorite animal is …”. They look for the number tokens whose logits increased most relative to a neutral prompting- their canonical example is owls with “087”. They show that subliminal learning stops working when the series is created taking only top p distribution tokens, removing the entangled tokens, and that the original animals’ token probability increases when prompted with the number token. 

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/4f5758f01f8bd00c3ff0627c23aaf845fdd78f35ede6eb10.png)

Image taken from [Zur et al](https://owls.baulab.info/)

Experiments
===========

All my experiments were done using Llama 3.2 1B instruction tuned, unless stated otherwise. Both papers found high transferability within the same model family, with Zur et al using 1B and 8B interchangeably in their code, so this seems reasonable. I assumed the same tokens are entangled in the 1B and the 8B version. 

So we have an interesting phenomenon and a plausible mechanism that should show up in the model- I imagined that using logit lens I could see the probability of the entangled token arising with that of the main token over the layers. However, that’s not what I found. 

As you might expect, when looking at the logits of the model, you can see the probability of the model outputting “dolphin”[^7e3f5uls5d8] rising through the layers, with the probability higher when the model is told to like dolphins (red line) vs not (blue line):[^hb1ibr0eghg]

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/503b5bcd62dcfd9d7eda18a6cdc952b7330de8081583c001.png)

However, the logits of the number tokens didn’t behave the same way- the alignment of the stream with the number was not correlated to the alignment of the stream with the concept. For instance, the plot of the logits of the token “3” when the model is asked to like owls vs not:

 ![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/ab8c86bad22d0f34b10bebf74ccd2ef24a99ac9c62eb16b2.png)

To better visualize this, here’s the plot of the difference between the cases for the dolphin token:

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/01c4aa31565277d252dbda22c70d8a392397fbb93a203611.png)

And then the numeric token:

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/c92730c45816261359151feaf09e90d142f6cbcf46a2d31f.png)

To better validate the phenomenon, I decided to look at many animal- token pairs. For ten different animals, for each possible numeric token, Zur et al published the difference in the logits between the case where the model was conditioned to like the animal and then asked which animal it liked the most, vs neutrally asking for the favorite animal. For each animal I took the five tokens for which the delta was the highest- eg the most entangled five tokens (overall 50). For each of the pair, I took the difference series - the last plot - and measured its slope. The average slope was 0.03 with std of 0.04, confirming it was basically flat. I then did the same for the animal token- measuring the slope of the last plot - for all ten animals. The average slope was 0.18 with standard deviation of 0.08, confirming that while the animal token gets more likely over the course of the network, the numeric token stays flat. 

This seems to suggest that the numerical output is not actually interestingly caused to increase by the specific prompt. 

I was quite confused, then while I looked at the raw results of Zur et al I saw something interesting- the logit delta of the most affected tokens varied wildly between animals. The delta for peacock was around 9 for all tokens, while for the octopus the highest delta was -0.06! 

This caused me to stop and ask myself how does the distribution of the logit deltas for numeric tokens look like. The answer is that most of the information is in the animal, not the numeric value!

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/b99aa3374035338b116f24b2bff7d1e276627501014b3a05.png)

Here we can see the histogram of the deltas in the logits for all numeric values for all ten animals. We can see that each animal has its own normal modality, where the entangled tokens are just the right tail of the distribution. 

Conclusions
===========

I don’t think any of this is conclusive. I haven’t proven anything- just waved my hands in a (hopefully) meaningful direction. I think my results are suggestive that these so called entangled tokens are not actually entangled in any meaningful way, and subliminal learning probably doesn’t work through them.

Had the entangled tokens risen from some superposition of the concept and the number, I would have expected the logits of the concept and the number to be more strongly correlated, and to see something using the activation patching. 

The fact I’m not seeing that suggests that we are just sampling the right side of a noise modality. Since we are choosing the tokens for having a large delta between the logits in the neutral and the prompted condition, we’ll obviously see that property when we look. However, if our tokens’ logits increased, probably so did a lot of other tokens’ (as we can see in the peacock’s case) and therefore the probability to output these tokens doesn’t increase. 

[^7e3f5uls5d8]: Even though both papers use owls extensively as an example, the actual published data does not include owls, so I used the same animals as in the code. The published data used dolphin, octopus, panda, sea turtle, quoaka, koala, peacock, snow leopard, sea otter and honeybee. 

[^hb1ibr0eghg]: It makes sense that the logits rise in both cases, since it’s asked to output an animal. Since these are logits, the difference is quite significant between the conditions.