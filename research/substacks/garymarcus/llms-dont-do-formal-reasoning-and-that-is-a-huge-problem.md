---
title: "LLMs don’t do formal reasoning - and that is a HUGE problem"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/llms-dont-do-formal-reasoning-and"
---

A superb [new article](https://arxiv.org/pdf/2410.05229) on LLMs from six AI researchers at Apple who were brave enough to challenge the dominant paradigm has just come out.

_Everyone_ actively working with AI should read it, or at least this [terrific X thread](https://x.com/mfarajtabar/status/1844456880971858028?s=61) by senior author, Mehrdad Farajtabar, that summarizes what they observed. One key passage: 

> “we found no evidence of formal reasoning in language models …. Their behavior is better explained by sophisticated pattern matching—so fragile, in fact, that changing names can alter results by ~10%!” 

One particularly damning result was a new task the Apple team developed, called GSM-NoOp

[](https://substackcdn.com/image/fetch/$s_!h8TV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc3c84b2f-cb58-4890-acc4-08a5a157e5e6_2644x1756.png)

§

This kind of flaw, in which reasoning fails in light of distracting material, is not new. Robin Jia Percy Liang of Stanford ran a similar study, with similar results, back in 2017 (which Ernest Davis and I quoted in _Rebooting AI_ , in 2019:

[](https://substackcdn.com/image/fetch/$s_!LXGn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fee1a4735-af08-4618-8fc7-cd0120e17c04_935x638.png)

§

**𝗧𝗵𝗲𝗿𝗲 𝗶𝘀 𝗷𝘂𝘀𝘁 𝗻𝗼 𝘄𝗮𝘆 𝗰𝗮𝗻 𝘆𝗼𝘂 𝗯𝘂𝗶𝗹𝗱 𝗿𝗲𝗹𝗶𝗮𝗯𝗹𝗲 𝗮𝗴𝗲𝗻𝘁𝘀 𝗼𝗻 𝘁𝗵𝗶𝘀 𝗳𝗼𝘂𝗻𝗱𝗮𝘁𝗶𝗼𝗻, where changing a** word or two in irrelevant ways or adding a few bit of irrelevant info can give you a different answer.

§

Another manifestation of the lack of sufficiently abstract, formal reasoning in LLMs is the way in which performance often fall apart as problems are made bigger. This comes from [a recent analysis of GPT o1](https://www.arxiv.org/pdf/2409.13373) by Subbarao Kambhapati’s team:

[](https://substackcdn.com/image/fetch/$s_!PT5c!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1f374410-3d43-4775-b8de-7ad0608053a7_888x532.png)

Performance is ok on small problems, but quickly tails off.

§

We can see the same thing on integer arithmetic. Fall off on increasingly large multiplication problems has repeatedly been observed, both in older models and newer models. (Compare with a calculator which would be at 100%.)

[](https://substackcdn.com/image/fetch/$s_!Bc-E!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd8ebb3fc-c0ff-4421-a4e8-1928d8838b74_1200x396.jpeg)

Even o1 suffers from this:

[](https://substackcdn.com/image/fetch/$s_!BK8L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fad644058-8cbe-429a-9298-21318e200efe_1301x1078.png)

§

Failure to follow the rules of chess is another continuing failure of formal reasoning:

[](https://substackcdn.com/image/fetch/$s_!IScx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa0c3102b-ff64-4e1e-8ba1-bd20618a8d8f_1244x1248.jpeg)

§

Elon Musk’s putative robotaxis are likely to suffer from a similar affliction: they may well work safely for the most common situations, but are also likely struggle to reason abstractly enough in some circumstances. (We are, however, unlikely ever to get systematic data on this, since the company isn’t transparent about what it has done or what the results are.) 

§

The refuge of the LLM fan is always to write off any individual error. The patterns we see here, in the new Apple study, and the other recent work on math and planning (which fits with many previous studies), and even the anecdotal data on chess, are too broad and systematic for that.

§

The inability of standard neural network architectures to reliably extrapolate — and reason formally — has been _the_ central theme of my own work back to [1998](https://www.sciencedirect.com/science/article/pii/S0010028598906946) and [2001](https://mitpress.mit.edu/9780262133791), and has been a theme in all of my challenges to deep learning, going back to 2012, and LLMs in 2019. 

I strongly believe the current results are robust. After a quarter century of “[real soon now](http://wikibin.org/articles/real-soon-now.html)” promissory notes I would want a lot more than hand-waving to be convinced than at an LLM-compatible solution is in reach. 

What I argued in 2001, in _The Algebraic Mind_ , still holds: [symbol manipulation](https://mitpress.mit.edu/9780262632683/the-algebraic-mind/), in which some knowledge is represented truly abstractly in terms of variables and operations over those variables, much as we see in algebra and traditional computer programming, must be part of the mix. Neurosymbolic AI — combining such machinery with neural networks – is likely a necessary condition for going forward. 

_**Gary Marcus** is the author of The Algebraic Mind, a 2001 MIT Press Book that foresaw the Achilles’ Heel of current models. In his most recent book, Taming Silicon Valley (also MIT Press), in Chapter 17, he discusses the need for alternative research strategies._

[Share](https://garymarcus.substack.com/p/llms-dont-do-formal-reasoning-and?utm_source=substack&utm_medium=email&utm_content=share&action=share)
