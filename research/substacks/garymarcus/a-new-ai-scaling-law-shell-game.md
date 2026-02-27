---
title: "A new AI scaling law shell game?"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/a-new-ai-scaling-law-shell-game"
---

[](https://substackcdn.com/image/fetch/$s_!p_J2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8c065ba6-4b1a-4fbf-9f9d-f4421f5cc369_908x739.jpeg)

_“If anything we are seeing the emergence of a new scaling law with test time or inference time compute“ –[Microsoft CEO Satya Nadella](https://www.tiktok.com/@todayin_ai/video/7440122892022451457), Tuesday November 19 at Microsoft Ignite_

Scaling laws were supposed to be, well, laws. Mathematical laws. Pretty much the entire GenAI frenzy has been based on the idea that with reasonable precision you could [predict performance from amount of data, number of parameters, and amount of compute](https://arxiv.org/abs/2001.08361). 

As recently as a few weeks ago, Sam Altman was extolling scaling laws as if they were a religion, in [an interview with the CEO of Y Combinator](https://x.com/tsarnick/status/1855001942919168207?s=61%20/%20religious%20beleift):

> _“When we started the core beliefs were that deep learning works and it gets better with scale… predictably… A religious level belief … was…. that that wasnt’t gotten to stop. .. Then we got the scaling results … At some point you have to just look at the scaling laws and say we’re going to keep doing this… There was something really fundamental going on. We had discovered a new square in the periodic table.”_

But things have been changing rapidly, and the great scaling retrenchment has already begun. Over the last few weeks, much of the field has been quietly acknowledging that recent (not yet public) large-scale models aren’t as powerful as the putative laws were predicting. 

The _new_ version is that there is not one scaling law, but three: scaling with how long you train a model (which isn’t really holding anymore), scaling with how long you post-train a model, and scaling with how long you let a given model wrestle with a given problem (or what Satya Nadella called scaling with “inference time compute”).

I suggest you keep your hands on your wallets here. 

§

Here’s why:

First, the new scaling “laws” are very much like the first – they are empirical generalizations, not physical laws. Like the first generalization, the new ones will eventually run out. (Anyone remember [the Star Trek even number rule](https://screenrant.com/star-trek-movies-odd-number-curse-explained/)?)

Second, the alleged “scaling” law (inspired by OpenAI’s o1) that Nadella emphasized— the more time you spend on a problem, the more accurate you get —is (a) expensive, because it by definition burns up more GPU time and (b) unreliable. 

Even if you look at [OpenAI’s own research post on o1](https://openai.com/index/learning-to-reason-with-llms/), which introduced the newest putative law, it is immediately apparent that scaling test time compute works for some problems and not others. (In some cases o1 doesn’t even do better than GPT-4). My guess is o1’s test time scaling works best in closed domains where you can create a lot of reliable synthetic data (such as math problems), and not so well in open-ended domains. GPT-4 was better than GPT-3 in almost every way; o1 is a far less uniform improvement.

Third, scaling laws aren’t really _laws_ anymore (if they ever were). The meaning of the word _scaling_ has been greatly devalued. “Scaling” used to mean “I can predict pretty much _**exactly**_ how well a given LLM will do, by knowing the size of its database and the amount of compute being used to train it, and those increases will be exponential”. Now it just means “I think it will get better, not sure how much, if I can keep tweaking some parameter”. 

That reframing is _vastly_ weaker. The initial formulation underwrote very specific, very expensive bets (“we expect X performance given Y billion dollars devoted to training); the new version is much more “let’s try it and see what happens”. 

§

All of this effort at trying to keep scaling alive - instead of coming up with genuinely new ideas — reminds of an anecdote Steven Pinker told me decades ago. When he was a young man, traveling in Europe, he spent a night at a big youth hostel in Switzerland, where each table had to nominate a volunteer for clean up.

_I drew the short match, and they all pointed to the kitchen. I had to do the drying, and was handed a thin 1' X 2' towel, which got saturated after the third dish, whereupon I spent the rest of the evening smearing water around hundreds of plates._

Trying to rescue LLMs by making a system that is inherently blind to factuality run longer — rather than better—is like smearing water around wet plates. 

We can and must do better. Scaling can only take us so far; the time has come for fresh invention.

_**Gary Marcus** looks forward to a world in which we see LLMs as just one part of artificial cognition, rather than a one-size-fits-all solution that it can never really be._
