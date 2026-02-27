---
title: "Five ways in which the last 3 months — and especially the DeepSeek era — have vindicated “Deep learning is hitting a wall\""
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/five-ways-in-which-the-last-3-months"
---

No other essay I have ever written has been ridiculed by as many people, or as many famous people, from Sam Altman and Greg Brockman to Yann LeCun and Elon Musk, as _[Deep Learning is Hitting a Wall](https://nautil.us/deep-learning-is-hitting-a-wall-238440/)_ , published nearly three years ago _._

[](https://substackcdn.com/image/fetch/$s_!bdzu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f054229-bdd6-4589-bb56-73ab467e84d3_1733x1103.jpeg)

In hindsight, I wrote the essay too soon; the world wasn’t ready for what I had to say. But an awful lot of what it had to say has borne out, and the last three months, especially the last few weeks, have been especially in line with the essay’s conclusions. 

Here are five observations:

  1. A key claim of the paper was that pure scaling of LLMs – just adding more data and compute to extant LLM architectures – would not bring us to AGI, and that so-called scaling laws were merely empirical generalizations rather than physical laws. For a long time few people believed me, but these conclusions are so widely accepted now that [Satya Nadella himself recently repeated them, almost word for word](https://open.substack.com/pub/garymarcus/p/satya-nadella-and-the-three-stages?r=8tdk6&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false); Marc Andreessen of all people also came close. So did Ilya Sutskever in his NeurIPS talks. (Of course I was given no credit for foresight, by any of these people; politics and economics preclude.) To be sure, there is now a _new_ proposed scaling law, not about adding to pure LLMs, but about adding more _time_ to so called test-time compute. For a while, anyway, that’s working to some degree (though see below), but the fact that we needed new techniques actually bears out another central claim of _Deep Learning is Hitting a Wall (DLHW)_ , which was that we would need new techniques besides pure LLMs. 

  2. Another of the key suggestions I made in 2022 was that we should use neurosymbolic techniques, combining neural networks with classical symbolic techniques such as rules. To some extent newer models _are_ doing that. OpenAI has not revealed exactly how o1 works, but, for example DeepSeek’s R1 model (which OpenAI has acknowledged resembles their test-time inference system o1) explicitly includes a “[rule-based reward system](https://arxiv.org/pdf/2501.12948)” for verifying some classes of answers. Neurosymbolic for the win! ([AlphaFold’s Nobel victory is another victory for neurosymbolic techniques](https://open.substack.com/pub/garymarcus/p/two-nobel-prizes-for-ai-and-two-paths?r=8tdk6&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false).)

  3. We got one more huge advance since the 2022 paper (I was agnostic then as to how many more leaps there would be), but we _still_ don’t have a system that would really merit the name of GPT-5. Altman himself recently said 4.5 is coming soon, but gave no date for GPT-5. People have been adding data and compute left and right since August 2022 when OpenAI demo’d GPT-4 to Bill Gates, but despite literally hundreds of billions of investment, pure LLM scaling has not produced the fruit some people imagined. (Note that test-time compute systems are _not_ across the board improvements like GPT-4 was relative to GPT-3 or GPT-3 was relative to GPT-2, but rather improvements in certain domains such as coding and math.) DLHW didn’t specifically say “one more giant-across-the-board leap and no more”, but that’s what we have gotten, and it’s broadly consistent with the warnings I issued there, and very much against the spirit of the hundreds of billions of dollars that were invested on the notion that rewards for more data and compute were essentially limitless.

  4. Even the latest systems like Deep Research are still struggling in a few ways – and those ways pretty much correspond exactly to the places that I warned would be LLM’s Achilles’ Heels: hallucinations and reasoning errors. The much ballyhoo’ed Deep Research tariff paper apparently made up a bunch of its numbers, and experiments by Colin Fraser have shown problems with temporal reasoning (e.g., with reasoning about athletes and what teams they played with over time). An article in Science by Derek Lowe that looked carefully at DeepSeek concluded that the fluent output of Deep Research was not to be trusted (“ _As with all LLM output, all of these things are presented in the same fluid, confident-sounding style: you have to know the material already to realize when your foot has gone through what was earlier solid flooring. That, to me, is one of their most pernicious features. I know that these things were not designed per se to glide over or hide their weak points and their mistakes, but they do a terrific job of it, and that's not really what you want. So as much as I found some parts of the Deep Research output impressive, I found its deeper research problems hard to deal with_.”)

  5. A consequence of what I argued in DLHW (that I didn’t really spell out until later articles in the second half of 2023 and early 2024 ) was a kind of crowding at the top: _if the scaling of pure LLMs ran out, you would expect to have multiple teams competing and reaching a point of diminishing returns, with essentially no moat, and a lot of competition over price_. That era, too has, been clearly reached. Most recently, DeepSeek, which more or less matched OpenAI’s o1, accelerated those price wars, and OpenAI was forced (already) to drop prices. LLMs, once novel, are largely a commodity. How that bodes for the economics of generative AI remains to be seen.




I think it is fair to say that “Deep Learning is Hitting a Wall” didn’t anticipate how well a system like Deep Research might work, but in most other respects, ranging from anticipating the slowing of pure LLMs to the need for neurosymbolic AI to the continued troubles with reasoning and hallucination, the paper was bang on. The ridicule, on the other hand, was deeply misplaced, and emblematic of a new regime in which oligarchs try to impose their beliefs on a science, moving markets but not actually solving the underlying research challenges that still loom before us.

[Share](https://garymarcus.substack.com/p/five-ways-in-which-the-last-3-months?utm_source=substack&utm_medium=email&utm_content=share&action=share)

 _**Gary Marcus** wrote this on his birthday, because there is no sweeter gift than vindication._
