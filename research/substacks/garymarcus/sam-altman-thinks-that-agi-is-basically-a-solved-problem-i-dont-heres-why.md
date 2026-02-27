---
title: "Sam Altman thinks that AGI is basically a solved problem. I don’t. Here’s why."
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/sam-altman-thinks-that-agi-is-basically"
---

Yesterday Sam Altman claimed in a [new blog post](https://blog.samaltman.com/reflections) that “We are now confident we how to build AGI as we have traditionally understood it”, alleging that OpenAI (which has not demonstrated AGI) was now on to new and better things.

[](https://substackcdn.com/image/fetch/$s_!tUx5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F94c48113-c85c-4d21-a689-5ab7d25673b8_850x608.png)

I do not share his confidence. Here is a thread I wrote about it [last night on X](https://x.com/garymarcus/status/1876127737108119781?s=61), that quickly became viral:

§

 _An MIT professor just asked me, how can you be so confident that OpenAI isn’t very close to AGI?_

_Here is a thread of links to a several recent observations that I think show how far we are from robust intelligence._

_Importantly, all of them are *known* problems, many that I have noted repeatedly for years and even decades._

_There is no *principled* solution thus far to any of them._

  1. _The problem of distribution shift, well-tested in Apple’s 2024 reasoning paper, which goes back to my own 1998 work, continues._

_LLMs, like their predecessors generalize well to similar items but[struggle with reliability in unfamiliar regimes, even minor variations sometimes break them](https://garymarcus.substack.com/p/llms-dont-do-formal-reasoning-and). _

  2. _A recent paper on Putnam math problems showed a similar failure on distribution shift, showing[30% decrement by o1 on math problems with minor variations eg on variable names](https://openreview.net/forum?id=YXnwlZe0yf&noteId=yrsGpHd0Sf)._

_Same old story, different set of problems._

  3. _[Commonsense reasoning is still dodgy, as it has long been](https://open.substack.com/pub/garymarcus/p/ai-still-lacks-common-sense-70-years?r=8tdk6&utm_medium=ios) , as Ernie Davis and I just reviewed here.._

  4. _o1 probably isn’t as robust as people might have hoped.[Even](https://x.com/alex_cuadron/status/1876017241042587964?s=61) [ on certain benchmarks, results may be fragile or difficult to replicate](https://x.com/alex_cuadron/status/1876017241042587964?s=61)_:

[](https://substackcdn.com/image/fetch/$s_!agod!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9f1b3236-9544-41e3-9ec3-027d653c4c56_1335x1472.png)

  5. _In o1’s best performances cases, there may have been heavy data augmentation that is not possible in more open-ended domains. In domains where that’s not possible, o1 may not even be that much better than GPT-4 (e.g on some language tasks), as you can see if[you read OpenAI’s reports carefully](https://t.co/pzuke7vBPm)._

  6. _The[presentation of o3 was problematic, and no clean test of out-of-domain generalization was provided](https://garymarcus.substack.com/p/c39?r=8tdk6), suggesting that we may see the kinds of problems with distribution shift as ever, outside of semi-closed domains where synthetic data can readily be generated. _

  7. _Many leading figures in the field have acknowledged that we may have reached a period of diminishing returns of pure LLM scaling, much as I anticipated in 2022. It’s anybody’s guess what happens next._

_[Note also that the current idea, test-time “scaling”, is very expensive, and will likely prove unreliable out of domains where augmentation is adequate, in which case it will get comparatively little commercial traction. Even o1 is losing money; o3 isn’t even available, and perhaps cannot be run at a profit.]_

  8. _As I noted in 2001, the lack of distinct, accessible, reliable database-style records leads to hallucinations. Despite many promises to the contrary, this still routinely leads to inaccurate news summaries, defamation, fictional sources, incorrect advice, and unreliability._




Does all this mean that I am absolutely 100% certain that AGI is not in clear sight? No; I am a scientist; if new evidence comes in, I will look at it, as I always have. But so far I have not seen a principled solution to even one of these longstanding problems, and that tells me a lot. 

_**Gary Marcus** recently wrote about his [track record of accurate predictions](https://garymarcus.substack.com/p/25-ai-predictions-for-2025-from-marcus?r=8tdk6). To the extent that those predictions have largely been on-target, for years, it is mostly because he has continued to focus on the implications of the 8 problems above. _
