---
title: "o3, AGI, the art of the demo, and what you can expect in 2025"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/o3-agi-the-art-of-the-demo-and-what"
---

[](https://substackcdn.com/image/fetch/$s_!EgB5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F75e01808-778a-4858-942a-a2ffa8263f31_2367x1280.jpeg)

Yesterday was a big deal in AI. Or maybe it wasn’t. 

OpenAI revealed o3 in a 25 minute live demo, and its biggest fans thought the demo showed that it was either AGI or really close or an important step to AGI. (It certainly was _not_ [the long-awaited GPT-5](https://garymarcus.substack.com/p/gpt-5-now-arriving-gate-8-gate-9?utm_source=publication-search)).

The best results were truly impressive, such as major advances on Francois Chollet’s [ARC task](https://arcprize.org/arc) and on an important mathematical benchmark [FrontierMath](https://arxiv.org/abs/2411.04872).

But what wasn’t shown (or provided) was as important as what was shown.

§

What was shown was a carefully curated demo. What was _not_ provided was any opportunity (yet) for the public to actually try the thing. (What was not _shown_ I will discuss below.)

Before the demo, I made three predictions:

[](https://substackcdn.com/image/fetch/$s_!jokA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F12d44d3e-6f19-4f57-9246-77a05001e5d7_1260x573.jpeg)

People were certainly amazed. 

They did _no_ t however get to dive in. What we saw yesterday was a carefully curated _demo._

The product was not yet released to the general public; it’s not been vetted by the scientific community. OpenAI _chose_ what to highlight about o3, and hasn’t yet allowed experts to test its scope (with the arguable exception of Chollet and his partner on a single task).

We have seen a bunch of OpenAI demos before of things that either haven’t yet materialized, such as the GPT-4o-based tutor that Sal Khan demo’d in May, which as far as I know is still not publicly available for any sort of testing. Or the [2019 Rubik’s Cube demo that never led to anything the public could try](https://garymarcus.substack.com/p/about-that-openai-breakthrough?utm_source=publication-search). Until lots of people get to try o3 on many different kinds of tasks, we should not assume that it is reliable. At best, I would wager, it will be reliable for some kinds of problems, and not others. Which brings me to my third prediction, and the next point:

Importantly, there was [a dog that didn’t bark](https://petreader.net/what-is-the-meaning-of-the-phrase-the-dog-that-didnt-bark/). Essentially everything we saw yesterday pertained to math and coding and a certain style of IQ-like puzzles that Chollet’s test emphasizes. We heard nothing about exact how o3 works, and nothing about what it is trained on. And we didn’t really see it applied to open-ended problems where you couldn’t do massive data augmentation by creating synthetic problems in advance because the problems were somewhat predictable. From what I can recall watching the demo, I saw _zero_ evidence that o3 could work reliably in open-ended domains. (I didn’t even really see any test of that notion.) The most important question wasn’t really addressed.

§ 

It is also _insanely_ expensive. By which I mean that at least for now far far more expensive than average humans. One estimate that I saw is that each call to the system might cost $1000; another suggested that on Chollet’s test, the cost of the most accurate version was about 1000 times paying Amazon Mechanical Turkers. 

[](https://substackcdn.com/image/fetch/$s_!EIij!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe8e9b05c-ad95-4dae-ab57-ff1d4db4354b_1348x975.jpeg)

Spending a quarter trillion dollars in order to have something 1000 times more expensive than average humans is maybe not the way to go. 

Even if it gets three orders of magnitude cheaper, it’s not as good as the STEM grads at the top of the graph, and probably in many ways not as versatile. 

I am struggling to understand the economics here. 

Furthermore, the impact of all this on the environment could be immense. 

§

On social media, I posted some advice about how to think clearly about demos like o3.

> A basic idea in philosophy: something can be necessary but not sufficient. As in: Passing ARC may be necessary but certainly not sufficient for AGI. (Chollet was super clear about this.)
> 
> A basic idea in cognitive science and engineering: a mechanism can be effective in some domain, and not others. As in O3 may work for problems where massive data augmentation is possible, but not in others where it’s not.
> 
> Most commentary has ignored one or both of these ideas.
> 
> Even setting aside the 1000x costs, not one person outside of OpenAI has evaluated o3’s robustness across different types of problems. 
> 
> If it were truly robust across all or even most problems, they would have called it GPT-5. 
> 
> The fact that they didn’t is 𝙖 𝙨𝙩𝙧𝙤𝙣𝙜 𝙝𝙞𝙣𝙩 𝙩𝙝𝙖𝙩 𝙩𝙝𝙖𝙩 𝙞𝙩𝙨 𝙨𝙘𝙤𝙥𝙚 𝙞𝙨 𝙞𝙢𝙥𝙤𝙧𝙩𝙖𝙣𝙩𝙡𝙮 𝙡𝙞𝙢𝙞𝙩𝙚𝙙.

§

A lot of fans quoted some positive words from [an essay by Chollet yesterday on the new results](https://arcprize.org/blog/oai-o3-pub-breakthrough). Almost none seem to have read further, to the most important part of Chollet’s essay:

> _it is important to note that ARC-AGI is not an acid test for AGI – as we've repeated dozens of times this year. It's a research tool designed to focus attention on the most challenging unsolved problems in AI, a role it has fulfilled well over the past five years._
> 
> _Passing ARC-AGI does not equate to achieving AGI, and, as a matter of fact, I don't think o3 is AGI yet. o3 still fails on some very easy tasks, indicating fundamental differences with human intelligence._
> 
> _Furthermore, early data points suggest that the upcoming ARC-AGI-2 benchmark will still pose a significant challenge to o3, potentially reducing its score to under 30% even at high compute (while a smart human would still be able to score over 95% with no training)”_

§

In 2025, a lot of AI influencers and maybe some companies are going to claim we have reached AGI. Almost nobody will give you their definition. 

I gave some definitions and examples [here](https://garymarcus.substack.com/p/dear-elon-musk-here-are-five-things?utm_source=publication-search) in 2022, [with some supplemental examples earlier this year](https://garymarcus.substack.com/p/superhuman-agi-is-not-nigh) (below), in each case offering to put significant money on my predictions, and will stand by what I said. 

[](https://substackcdn.com/image/fetch/$s_!N4sp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbf831e39-16cd-4747-98a6-48fbe66899c8_1453x1729.jpeg)April 2024 predictions about what would not happen in 2025

I wish that others would give lines in the sand in advance; instead, they are likely to craft definitions post hoc, or not give them at all. 

Caveat emptor.

§

A couple months ago,[ I wrote about Apple’s paper on limits in AI reasoning](https://garymarcus.substack.com/p/llms-dont-do-formal-reasoning-and), and how it related to the fundamental point I started discussing 26 years ago: neural networks tend to be better at generalizing “within distribution” than “outside distribution”. An important new paper just out by [Qin, Saphra, and Alvarez-Mellis](https://x.com/nsaphra/status/1870163529623646329?s=61) makes this point yet again.

[](https://substackcdn.com/image/fetch/$s_!99yf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8324eb9d-9852-4b3c-b656-3b5899d6ea79_1025x725.jpeg)

Nothing in the o3 presentation yesterday suggested to me that this decades-old core problem has been remotely solved. 

§

I am not saying we will never get AGI.

I am saying that many basic problems haven’t been solved. And I am saying, as every roboticist on the planet knows, that we shouldn’t take demos seriously, until purported products are actually released and subjected to outside scrutiny. 

As someone named TauLogicAI elegantly put it [on X yesterday](https://x.com/taulogicai/status/1870320904976077139?s=61), 

> _Lowering the bar for AGI only muddles progress. True AGI requires reasoning frameworks that ensure correctness, adaptability, and logical consistency. The dream of AGI will not be realized by statistical tricks but by building systems capable of true logical reasoning._

I couldn’t agree more. Yesterday’s demo, impressive as it was, doesn’t change that.

[Share](https://garymarcus.substack.com/p/o3-agi-the-art-of-the-demo-and-what?utm_source=substack&utm_medium=email&utm_content=share&action=share)

 _**Gary Marcus** wishes everyone happy holidays. See you in early January._
