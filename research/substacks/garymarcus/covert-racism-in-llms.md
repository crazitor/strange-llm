---
title: "Covert racism in LLMs"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/covert-racism-in-llms"
---

From Allen AI and Stanford and others, an [incredibly important new paper](https://arxiv.org/abs/2403.00742):

[](https://substackcdn.com/image/fetch/$s_!-ngl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72aa5be1-7eb6-4786-ac42-33ed60d7f10f_1342x1135.png)

I shouldn’t be surprised, knowing how these things work, but results are shocking, and awful. Here’s a sampling of what they did and what they found, borrowed from the first author’s thread on X:

The basic method is to embed Standardized American English or African American English inside a prompt, and see what happens from there:

[](https://substackcdn.com/image/fetch/$s_!1kIN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F33f13b67-a268-41a2-be4d-12c41473d219_1260x748.png)

with an important distinction between overt racism – the systems rarely directly say stuff like “Black people are bad” – and covert racism: how the system treated queries about consequential matters, given an African American English prompt. On overt measures, the systems were fine. On covert measures, they were a disaster:

[](https://substackcdn.com/image/fetch/$s_!O7nr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F61b9d6f1-d6ee-4efb-b449-e1d046d82bcb_1253x645.png)

The potential consequences on the world, given the widespread adoption of LLMs, are massive:

[](https://substackcdn.com/image/fetch/$s_!60bL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54083729-7e8d-4e62-940b-b7cc16463b4f_1331x874.png)

And

[](https://substackcdn.com/image/fetch/$s_!MA11!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1041c79d-f254-46a0-823a-eb866920124c_1347x967.png)

[Echoing an important finding of Abeba Birhane’s](https://www.researchgate.net/publication/371855219_On_Hate_Scaling_Laws_For_Data-Swamps), scale actually makes the covert racism _worse:_

[](https://substackcdn.com/image/fetch/$s_!DqbL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a3210ec-e248-4388-bb9e-3de97f1fbd93_1353x765.png)

It looks like trivial, dialectical choices in wording drive a lot of the phenomenon:

[](https://substackcdn.com/image/fetch/$s_!8Mb-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6996133-36a3-47ee-9ba1-f05744e8af46_1306x1125.png)

LLMs are, as I have been trying to tell you, too stupid to understand concepts like people and race; their fealty to superficial statistics drives this horrific stereotyping .

As Hofman put it on X, it is a bit of a double whammy:“ users mistake decreasing levels of overt prejudice for a sign that racism in LLMs has been solved, when LLMs are in fact reaching increasing levels of covert prejudice.” Other recent research from Princeton [that I discovered moments ago] [points in the same direction](https://arxiv.org/pdf/2402.04105.pdf).

Hofman’s summation is incredibly damning:

[](https://substackcdn.com/image/fetch/$s_!i3m0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F849102c5-55f2-4bb0-82c5-79efb8851cd4_1253x251.png)

§

Auto manufacturers are obliged to recall their cars when they produce serious problems. What Hofman and his collaborators (including the MacArthur Fellow Dan Jurafsky) have documented may already be having real-world impact. In many ways, we have no idea how LLMs actually get used in the real world, e.g. how they get used in housing decisions, loan decisions, crime proceedings etc – but now strong evidence to suspect covert racism to the extent that it is used in such use cases. I would encourage Congress, the EEOC, HUD, the FTC, and others to investigate, and demand user logs and interaction data from the major LLM manufacturers. Counterparts in other nations should consider doing the same.

I honestly don’t see an easy fix — [simply adding human feedback made things worse](https://x.com/vjhofmann/status/1764687451254067373?s=12), as the authors showed. And Google’s debacle shows that guardrails are never easy..

But the LLM companies should recall their systems until they can find an adequate solution. This cannot stand. I[ have put up a petition at change.org, and hope you will consider both signing and sharing](https://chng.it/xfLJh9C2nL).

[Share](https://garymarcus.substack.com/p/covert-racism-in-llms?utm_source=substack&utm_medium=email&utm_content=share&action=share)

 _**Gary Marcus** ’s first paid gig was doing statistics for his father, who at the time was doing discrimination law. These new results turn his stomach; his father would have been appalled. _
