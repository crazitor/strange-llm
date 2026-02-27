---
title: "OpenAI’s dirty December o3 demo doesn’t readily replicate"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/openais-dirty-december-o3-demo-doesnt"
---

[](https://substackcdn.com/image/fetch/$s_!4960!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F644fb83d-079e-4438-92ae-abda3eb3caa2_1024x768.jpeg)“draw an image representing a benchmark result that might have been bogus”

As a scientist, OpenAI’s widely-watched o3 livestream, December 20th, “[Day 12 of Shipmas](https://www.youtube.com/live/SKBG1sqdyIU?si=Iz9qg28Ridfwov-5)”, which [Francois Chollet reported at the time as a breakthough](https://arcprize.org/blog/oai-o3-pub-breakthrough), made me sick to my stomach. I said so at the time, in my essay [𝗼𝟯 “𝗔𝗥𝗖 𝗔𝗚𝗜” 𝗽𝗼𝘀𝘁𝗺𝗼𝗿𝘁𝗲𝗺 𝗺𝗲𝗴𝗮𝘁𝗵𝗿𝗲𝗮𝗱: 𝘄𝗵𝘆 𝘁𝗵𝗶𝗻𝗴𝘀 𝗴𝗼𝘁 𝗵𝗲𝗮𝘁𝗲𝗱, 𝘄𝗵𝗮𝘁 𝘄𝗲𝗻𝘁 𝘄𝗿𝗼𝗻𝗴, 𝗮𝗻𝗱 𝘄𝗵𝗮𝘁 𝗶𝘁 𝗮𝗹𝗹 𝗺𝗲𝗮𝗻𝘀](https://garymarcus.substack.com/p/c39?r=8tdk6). There were problems with experimental design, misleading graphs that left out competing work, and more. 

Later, after I wrote that piece, I discovered that one of their demos, on FrontierMath, was fishy in a different way: OpenAI had privileged access to data their competitors didn’t have, but didn’t acknowledge this. They also (if I recall) failed to disclose their financial contributions in developing the test. And then a couple weeks ago we all saw that current models [struggled mightly on the USA Math Olympiad problems that were fresh out of the oven, hence hard to prepare for in advance](https://open.substack.com/pub/garymarcus/p/reports-of-llms-mastering-math-have?r=8tdk6&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false).

Today I learned that the story is actually even worse than all that: the crown jewel that they reported on the demo — the 75% on Francois Chollet’s ARC test (once called ARC-AGI) doesn’t readily replicate. Mike Knoop from the ARC team reports “We could not get complete data for o3 (high) test due to repeat timeouts. Fewer than half of tasks returned any result exhausting >$50k test budget. We really tried!” The model that is released as “o3 (high)” presumed to be their best model, can’t readily yield whatever was reported in December under the name o3.

The best stable result that ARC team could get from experimenting with the latest batch of publicly-testable OpenAI models was 56% with a different model called o3-medium, still impressive, still useful, but a long way from the surprising 75% that was advertised. 

And the lower 56% is [not much different from what Jacob Andreas’s lab at MIT got in November.](https://arxiv.org/html/2411.07279v1) It’s arguably worse; if I followed correctly, and if the measures are the same, Andreas lab’s best score was actually _higher_ , at 61%.

Four months later, OpenAI, with its ever more confusing nomenclature, has released a bunch of models with o3 in the title, but _none_ of them can reliably do what was in the widely viewed and widely discussed December livestream. That’s bad.

Forgive if me I am getting Theranos vibes.

§

Just a couple weeks ago Yafah Edelman at LessWrong [reported a related finding](https://www.lesswrong.com/posts/z8zPL2hBqTmx7Kf6J/frontiermath-score-of-o3-mini-much-lower-than-claimed), “OpenAI [reports](https://openai.com/index/openai-o3-mini/) that o3-mini with high reasoning and a Python tool receives a 32% on FrontierMath. However, Epoch's [official evaluation](https://epoch.ai/data/ai-benchmarking-dashboard)[[1]](https://www.lesswrong.com/posts/z8zPL2hBqTmx7Kf6J/frontiermath-score-of-o3-mini-much-lower-than-claimed#fnck5yka9gkt) received only 11%”; some [possible explanations are given](https://www.lesswrong.com/posts/z8zPL2hBqTmx7Kf6J/frontiermath-score-of-o3-mini-much-lower-than-claimed), but this is again a very bad look.

And guess what, sometimes o3 [apparently cheats, reporting answers that are available on the internet without actually doing the work](https://x.com/tobyordoxford/status/1913393700547301705?s=61), as Toby Ord explains in [a long thread on X](https://arxiv.org/html/2411.07279v1). Essentially Ord argues that o3 is [looking up the answer, not computing it](https://x.com/tobyordoxford/status/1913395412544770382?s=61).

This in turn is kind of reminiscent of [something similar that TransluceAI recently reported](https://x.com/transluceai/status/1912552046269771985?s=61) last week, in another long thread (too complex to quickly summarize here but worth reading):

[](https://substackcdn.com/image/fetch/$s_!woyu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b30905c-b59b-4b11-be59-ab5da909b937_1273x412.png)

The truth is that we don’t really know how good o3 is or isn’t, and nobody should ever take OpenAI’s video presentations particularly seriously again, until they have been fully vetted by the community. The fact that their flashy result on ARC couldn’t readily be replicated speaks volumes. 

§

My trust in OpenAI has never been high; at this point it is extremely low. 

And given that [Meta also appears to have just juiced some benchmarks](https://open.substack.com/pub/garymarcus/p/deep-learning-deep-scandal?r=8tdk6&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false), the whole thing is starting to look like a bunch of over-promisers scrambling to make things look better than they really are.

_**Dr Gary Marcus** , Professor Emeritus at NYU, has done enough article reviewing in his career to know when people are trying to pull a fast one. _
