---
title: "The future of alignment if LLMs are a bubble"
author: "Stuart_Armstrong"
date: "2025-12-23"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/dxF7cPKTFMbkbtnxi/the-future-of-alignment-if-llms-are-a-bubble"
score: 47
votes: 20
---

We might be in a generative AI bubble. There are many potential signs of this around:

*   [Business investment in generative AI have had very low returns. ](https://www.artificialintelligence-news.com/wp-content/uploads/2025/08/ai_report_2025.pdf)
*   Expert opinion is turning against LLM, including some of the early [LLM](https://ppc.land/lecun-calls-auto-regressive-llms-doomed-at-nyu-seminar/) [promoters](https://www.dwarkesh.com/p/ilya-sutskever-2) (I also get this message from personal conversations with some AI researchers).
*   No signs of mass technological unemployment.
*   No large surge in new products and software.
*   No sudden economic leaps.
*   [Business investment in AI souring.](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/)
*   Hallucinations a continual and unresolved problem.
*   [Some stock market analysts](https://www.cnbc.com/2025/12/11/big-short-steve-eisman-is-getting-worried-about-the-ai-trade.html) have soured on generative AI, and the stock market is sending at best [mixed](https://www.bloomberg.com/news/articles/2025-12-12/some-oracle-data-centers-for-openai-delayed-to-2028-from-2027) [signals](https://www.barrons.com/articles/nvidia-stock-price-oracle-37493727?gaa_at=eafs&gaa_n=AWEtsqdfxRCbOfLWPm8ymxHIguw13pF-9mQ_oqqHWUSuo4HeJyxX7FVpuRzm-UI1jAU%3D&gaa_ts=693e8fa8&gaa_sig=-DHOxVqSiw1mHHX2ftEOgGfOPES86OBb1kdpRrvRNAaTn-HWriLuqwQQcwYDelS6ZtSgyIrAD5-tKaEi8uadQw%3D%3D) about generative AI's value.
*   Generative AI companies aren't making profits while compute investments continue rising. OpenAI is behaving like a company [desperate to find a way of monetising its models](https://www.bbc.co.uk/news/articles/cpd2qv58yl5o), rather than a confident company on the cusp of AGI.

If LLMs were truly on the path to AGI[^wb8y910va29], I would be expecting the opposite of many of these - opportunities for LLM usage opening up all over the place, huge disruption in the job markets at the same time as completely novel products enter the economy and change its rate of growth. And I would expect the needed compute investments to be **declining** due to large efficiency gains, with LLM errors being subtle and beyond the ability of humans to understand.

Thus the world does not look like one where LLM-to-AGI is imminent, and looks a lot more like one where generative AI keep on hitting bottleneck after bottleneck - when, precisely, will the LLMs stop hallucinating? When will image composition work reliably[^10dnoqyh0qj]?

Remember when GPT 3.5 came out? It did feel that we were on the cusp of a something explosive, with countless opportunities being enthusiastically seized and companies promising transformations in all kinds of domains.

But that didn’t happen. Generative AI has a lot of uses and many good possibilities. But in terms of R&D progress, it now feels like an era of repeated bottlenecks slowly and painfully overcome. LLMs are maturing as a technology, but their cutting-edge performance is improving only slowly - outside of coding, which is showing some definite upswing.

What a bubble is
================

A bubble wouldn't mean that generative AI is useless. It might even be transformative and a huge boost to the economy. It just means that the **generative AI companies cannot monetise it to the level required to justify the huge investments being made**.

And the investments being made are huge. See arguments like "[Big Tech Needs $2 Trillion In AI Revenue By 2030 or They Wasted Their Capex](https://www.wheresyoured.at/big-tech-2tr/)" (if you want a well researched skeptical take on the economics of LLMs, the whole of [Ed Zitron blog](https://www.wheresyoured.at/big-tech-2tr/) is a good source - stick to information, not his opinions, and be warned that he is extremely uncharitable towards AI safety).

There are many reasons why generative AI companies might fail at monetising. Since the end of ([very weak](https://www.tobyord.com/writing/the-scaling-paradox)) training scaling laws, we've been in an "inference" scaling situation, buying and building huge data centers. But that isn't enough for a moat - they need economies of scale, not just a large collection of expensive GPUs.

Because open source models are a few months, maybe a year, behind the top models. If the top LLM companies really become profitable, it will be worth it for others to buy up a small bunch of GPUs, design a nice front end, and run DeepSeek or a similar model cheaply. Unless they can clearly differentiate themselves, this puts a lower bound on what the top companies can charge.

So it's perfectly possible that generative AI is completely transformational and that we are still in an AI bubble, because LLM companies can't figure out how to capture that value.

If we are in a bubble, what does it mean for Alignment research?
================================================================

If LLMs were a quick path to AGIs, then we'd certainly not be in a bubble. So, if we are in a bubble, they're not AGIs, nor the path to AGIs, nor probably the road to the avenue to the lane to the path to AGIs.

And the big companies like OpenAI and Anthropic, that have been pushing the LLM-to-AGI narrative, will take a huge reputational hit. OpenAI especially has been using the "risk" of AGI as a way to generate excitement and pump up their valuation. A technology so dangerous it could end the world - think of what it could do to your stock values!

And if the bubble bursts, talk of AGI and AGI risk will be seen as puffery, as tools of bullshit artists or naive dupes. It will be difficult to get people to take those ideas seriously.

There will be some positives. The biggest positive is that LLMs would not be proto-AGIs: hence there will be more time to prepare for AGI. Another positive is that LLMs may be available for alignment purposes (I'll present one possible approach in a subsequent paper.

Some thoughts on how to prepare or adapt to being in a generative AI bubble
---------------------------------------------------------------------------

Some of these things are things we should probably be doing anyway; others are conditional on generative AI being a bubble. The list is non-exhaustive and intended to start discussion:

*   **We should emphasise the ways in which current AI misbehaviour fits with the general AI alignment problem**. Current AIs [manipulate](https://www.psychologytoday.com/gb/blog/dancing-with-the-devil/202506/how-emotional-manipulation-causes-chatgpt-psychosis) and [deceive](https://www.pnas.org/doi/abs/10.1073/pnas.2317967121) people, [driving some](https://nypost.com/2025/08/29/business/ex-yahoo-exec-killed-his-mom-after-chatgpt-fed-his-paranoia-report/) to [suicide](https://www.bbc.co.uk/news/articles/cgerwp7rdlvo). Other none generative AIs (such as recommender algorithms) [prey on people's cognitive weaknesses](https://philhoward.org/wp-content/uploads/2022/08/ct2018.pdf). They often do this as a consequence of following simple goals with extreme optimisation power in unintended ways. This is literally the problem with AI alignment, already happening in the world. We should point to these examples.
*   **In a related point, we should ally more with traditional AI ethics people**. They are working on short term problems that are scaled down version of superintelligent AI problems. Now, sometimes their concerns feel parochial or political, and their solutions might not scale to superintelligence. But a) we can't escape political concerns - we're designing the ideal future, and we can't leave all the moral content of that future to "be figured out later", b) if we collaborate with them, we can learn from their ideas and encourage them to develop ideas that will scale, and c) this will prevent other companies doing the divide and conquer approach of "we're concerned about superintelligent AI. And we'll use that concern exclusively to get money from investors and to avoid any current legislation".
*   **We'll need to analyse why generative AIs were not AGI**. There's a compelling story for how AGI and superintelligence might happen: once an algorithm has a certain level of capability, it will use those capabilities to self-improve in some way, and quickly scale to superhuman capabilities. Currently, we're telling that story about generative AI The problem is that this story can be told about any proto-AI - until, later on, we understand what the blockers and bottlenecks are (so that, e.g. GOFAI or expert systems or basic deeplearning aren't enough to get to AGI). So how can we improve our assessments ahead of time, try and predict blockers and whether "this time is the real one" or not?
*   **Critique the entities that have mislead people**. If LLMs don't lead to AGI, then a lot of people will have been wrong about it. And some will have been actively misleading, often for hype or marketing purposes. We'll need to not let these people get away with this. If someone at a company has hinted that they have AGI, and they don't have anything like that, then they have mislead the public or mislead themselves. If someone has hyped up "AGI safety" solely in order to impress people with the potential power of AI, this is worse than a lie: they have weakened warnings about the greatest danger in human history, just in order to sell more stuff.
*   **Prepare for retrenchment**. However unfair it is, if generative AI is a bubble, AI safety messages will become less sexy, many funders will move on, journals and journalists will be less interested, and the status of AI safety will take a big hit. We'll have to accept a more hostile cultural environment. See this [vitriolic blog post](https://www.wheresyoured.at/ai-mythbusters/#ai-2027-is-an-accurate-and-trustworthy-representation-of-the-future) from Ed Zitron[^m4hjsv0ng98] which paints the field of AI safety as a grifting tool for OpenAI/Anthropic/NVIDIA[^zi6asex3umf]. After a bubble, more people are going to be saying this. Young, smart, curious, technologically-skilled, EA-adjacent people are going to be turned off by AI safety rather than attracted by it.
*   **Prepare for opportunities**. The wheels of society and AI research won't stand still. Even after a bubble, much of generative AI will remain, people will continue key research (maybe under different titles), new ideas and algorithms will be developed, new risks will emerge. Culture will change, again - if we remain truth-tracking, it will be likely to be a positive shift for us. Focus on the true fundamental risks, keep honest, look out for opportunities, for they will come.

[^wb8y910va29]: In a subsequent post, I'll discuss how we might improve our AGI predictions - almost any advance in computer science could lead to AGI via recursive self-improvement, but can we identify those that are genuinely likely to do so? 

[^10dnoqyh0qj]: I've had very painful experiences trying to use these tools to generate any image that is a bit unusual. I've used the phrase "Gen AIs still can't count" many a time. 

[^m4hjsv0ng98]: Ed will be the kind of person who will be seen as having "been right all along" if there is an AI bubble. 

[^zi6asex3umf]: It's paywalled, but he talks about the AI 2027 paper, concluding:[...] Everything is entirely theoretical, taped together with charts that have lines that go up and serious, scary language that, when boiled down, mostly means "then the AI became really good at stuff."I fucking hate the people that wrote this. I think they are craven grifters writing to cause intentional harm, and should have been mocked and shunned rather than given news articles or humoured in any way.And in many ways they tell the true story of the AI boom — an era that stopped being about what science and technology could actually do, focusing instead on marketing bullshit and endless growth.This isn't a "scenario for the future."  It's propaganda built to scare you and make you believe that OpenAI and Large Language Models are capable of doing impossible things.It's also a powerful representation of the nebulous title of "AI researcher," which can mean everything from "gifted statistician" to "failed philosophy PHD that hung around with people who can actually write software.Note that, in general, the quality of his arguments and research is much higher than this vitriol would suggest.