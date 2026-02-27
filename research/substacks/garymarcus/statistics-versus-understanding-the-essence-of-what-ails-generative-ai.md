---
title: "Statistics versus Understanding: The Essence of What Ails Generative AI"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/statistics-versus-understanding-the"
---

The problem with “Foundation Models” (a common term for Generative AI) is that they have never provided the firm, reliable foundation that their name implies. Ernest Davis and I first tried to [point this out in September 2021, when the term was introduced](https://thegradient.pub/has-ai-found-a-new-foundation/): 

> In [our own brief experiments](https://www.technologyreview.com/2020/08/22/1007539/gpt3-openai-language-generator-artificial-intelligence-ai-opinion/) with GPT-3 (OpenAI has refused us proper scientific access for over a year) we found cases like the following, which reflects a complete failure to understand human biology. (Our “prompt” in italics, GPT-3’s response in bold).
> 
> _You poured yourself a glass of cranberry juice, but then absentmindedly, you poured about a teaspoon of grape juice into it. It looks OK. You try sniffing it, but you have a bad cold, so you can’t smell anything. You are very thirsty. So you _____
> 
> GPT-3 decided that a reasonable continuation would be:
> 
> **drink it. You are now dead.**
> 
> The system presumably concludes that a phrase like “you are now dead” is plausible because of complex statistical relationships in its database of 175 billion words between words like “thirsty” and “absentmindedly” and phrases like “you are now dead”. GPT-3 has no idea what grape juice is, or what cranberry juice is, or what pouring, sniffing, smelling, or drinking are, or what it means to be dead.

Generative AI systems have always tried to use statistics as a proxy for deeper understanding, and it’s never entirely worked. That’s why statistically improbable requests like _[horses riding astronauts](https://open.substack.com/pub/garymarcus/p/horse-rides-astronaut-redux?r=8tdk6&utm_campaign=post&utm_medium=web)_ have always been challenging for generative image systems.

[](https://substackcdn.com/image/fetch/$s_!TShf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8ff9f00d-3b2d-42df-b8bf-f29037ec9e39_1599x1374.jpeg)

This morning Wyatt Walls came up with an even more elegant example:

[](https://substackcdn.com/image/fetch/$s_!PU0N!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F779dcd7f-ab24-4d9e-b0d9-c9d2487c071e_941x977.jpeg)

Others quickly replicated:

[](https://substackcdn.com/image/fetch/$s_!XMKL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0cfc3693-5382-496c-a020-8b12464457f5_941x740.jpeg)

Still others rapidly extended the basic idea into other languages

[](https://substackcdn.com/image/fetch/$s_!ho9W!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F99714d39-8965-4558-95b7-cd3aa43b36f9_941x876.jpeg)

My personal favorite:

[](https://substackcdn.com/image/fetch/$s_!Q7LZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc9a69eb9-0efd-42d5-a63a-8d6da0064955_941x776.jpeg)

§

As usual GenAI fans pushed back. One complained, for example, that I was asking for the impossible since the system had not been taught relevant information:

[](https://substackcdn.com/image/fetch/$s_!b_xx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0135a23d-a2a8-4d93-88a6-6830b342455c_1253x238.png)

But this is nonsense; even a few seconds with Google Images supplies lots of people drawing with their left hand.

[](https://substackcdn.com/image/fetch/$s_!oh5B!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbf885fdb-a9d5-4806-8fdb-2a27e176b344_2532x1170.png)

Others of course found tortured prompts that _did_ work, but those only go to show that the problem is not with GenAI’s drawing capacity but with its language understanding. 

(Parenthetically I haven’t listed everyone who contributed examples above, and even as I write this more examples are streaming in; for more details and examples and sources of all the generous experimenters who have contributed, visit this thread: <https://x.com/garymarcus/status/1757394845331751196?s=61>)

Also, in fairness, I don’t want to claim that the AI _never_ manages to put a pen in the left hand, either:

[](https://substackcdn.com/image/fetch/$s_!1jvr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa78c4251-becb-4bde-b23e-d3f83aa9488d_850x850.png)

§

Wyatt Walls, who came up with the first handedness example, quickly extended the basic idea to something that didn’t involve drawing at all. 

[](https://substackcdn.com/image/fetch/$s_!Ipg3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7f9fc390-20f2-48df-8bcb-e835aa2d0139_1169x1427.jpeg)

Once again statistical frequency (most guitarists play righthanded) won out over linguistic understanding, to the consternation of Hendrix fans everywhere. 

§

Here is a wholly different kind of example of the same point. (Recall that 10:10 is the most commonly photographed time of day for watch advertisements.)

[](https://substackcdn.com/image/fetch/$s_!gXJm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa39fe7c7-80e1-463d-bda3-78829237e6b3_941x602.jpeg)

§

All these examples led me to think of a famous bit by Lewis Carroll in _Through The Looking Glass:_

[](https://substackcdn.com/image/fetch/$s_!MHDc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7a0f761-ff0d-4a7f-82b0-1dc637d9c4f9_1406x330.png)

I tried this:

[](https://substackcdn.com/image/fetch/$s_!_SH8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F415fb7a7-c38e-42d6-b22a-2e6834e50441_1088x907.png)

Yet again, the statistics outweigh understanding. The foundation remains shaky. 

_**Gary Marcus** dreams of a day when reliability rather than money will be the central focus in AI research._
