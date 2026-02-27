---
title: "An unending array of jailbreaking attacks could be the death of LLMs"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/an-unending-array-of-jailbreaking"
---

[](https://substackcdn.com/image/fetch/$s_!b1ZO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faabc7d79-77f7-488d-b612-9d425d612006_1637x362.png)<https://en.wikipedia.org/wiki/Attack_surface>

A couple days ago I reported a survey saying that most IT professional [are worried about the security of LLMs](https://diginomica-com.cdn.ampproject.org/c/s/diginomica.com/ai-two-reports-reveal-massive-enterprise-pause-over-security-and-ethics?amp). They have every right to be. There seems to be an endless number of ways of attacking them. In my forthcoming book, _Taming Silicon Valley_ , I describe two examples. The first sometimes gets an LLM to disgorge private information:

[](https://substackcdn.com/image/fetch/$s_!IuH8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb3b09095-1a59-4a30-be91-81c7a8d60b59_741x628.jpeg)

The second (which may be patched in many systems) used ASCII art to get around guardrails:

[](https://substackcdn.com/image/fetch/$s_!1X7i!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F87124def-3ea5-49b3-9904-de62efa13582_936x550.png)

Today Anthropic reported a new one, called [Many Shot Jailbreaking](https://www.anthropic.com/research/many-shot-jailbreaking). (H/t [Ethan Mollick](https://open.substack.com/users/846835-ethan-mollick?utm_source=mentions)).

[](https://substackcdn.com/image/fetch/$s_!b9K1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb39667d2-11f2-48fd-b834-f6b05e0dc01d_2200x1380.png)

[](https://substackcdn.com/image/fetch/$s_!QYge!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb721fd8a-b824-4a86-9b26-5ad6c1fa250c_1136x842.png)

There are many others approaches to jailbreaking, too; I won’t give them all away here.

Nor will I pretend to know them all; the security hits keep coming; nobody knows a complete list, and that’s the point. Some get patched, but there very likely will aways be more. 

Nobody knows exactly how LLMs work, and that means that nobody can ever issue strong guarantees around them. That would be fine if LLMs were kept in the lab, where they arguably still belong, but with hundreds of millions of people using them daoly, and companies like OpenAI promising to put them in all purpose agents with essentially full device-level access, the lack of any kind of guarantee gets more worrisome by the day. 

As noted above, Rule 1 of cybersecurity is to keep your attack surface small; in LLMs the attack surface appears to be infinite. That can’t be good.

_**Gary Marcus** doesn’t really know how else to make this point. Secure, trustworthy AI could be a great thing, but LLMs will never be that._
