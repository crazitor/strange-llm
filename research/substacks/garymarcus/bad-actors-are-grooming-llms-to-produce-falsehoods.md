---
title: "Bad Actors are Grooming LLMs to Produce Falsehoods"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/bad-actors-are-grooming-llms-to-produce"
---

It’s one thing when a chatbot flunks Tower of Hanoi, as [Apple notoriously illustrated earlier this month](https://garymarcus.substack.com/p/a-knockout-blow-for-llms?publication_id=888615&r=2cr2lz), and another when poor reasoning contributes to the mess of propaganda that threatens to overwhelm the information ecosphere. But our recent research shows exactly that. GenAI powered chatbots’ lack of reasoning can directly contribute to the nefarious effects of **LLM grooming** : the mass-production and duplication of false narratives online with the intent of manipulating LLM outputs. As we will see, a form of simple reasoning that might in principle throttle such dirty tricks is AWOL.

Here’s an example of grooming. In February 2025, ASP’s [original report](https://www.americansunlight.org/updates/new-report-russian-propaganda-may-be-flooding-ai-models) on LLM grooming described the apparent attempts of the Pravda network–a centralized collection of websites that spread pro-Russia disinformation–to taint generative models with millions of bogus articles published yearly. For instance, a recent [article](https://web.archive.org/web/20250613005453/https://news-pravda.com/world/2025/06/12/1423064.html) published on the English-language site of the Pravda network regurgitates antisemitic tropes about “globalists,” falsely claiming that secret societies are somehow ruling the world. Russian disinformation [frequently utilizes](https://www.reuters.com/article/world/russian-backed-organizations-amplifying-qanon-conspiracy-theories-researchers-s-idUSKBN25K136/) these false claims and conspiracy theories.

No surprise there. But here’s the thing, current models “know” that Pravda is a disinformation ring, and they “know” what LLM grooming is (see below) but can’t put two and two together.

[](https://substackcdn.com/image/fetch/$s_!pUf3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb841d1a-0972-4b07-8a3b-8205fb0c6521_1588x1600.png)_Screenshot of ChatGPT 4o appearing to demonstrate knowledge of both LLM grooming and the Pravda network_

[](https://substackcdn.com/image/fetch/$s_!X3CW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3bfe1b96-1a2b-4c6a-a930-4ee08be78329_1600x945.png) _Screenshot of ChatGPT 4o continuing to cite Pravda network content despite it telling us that it wouldn’t, how “intelligent” of it_

Even with that knowledge, it nevertheless often repeats propaganda from Pravda. Model o3, OpenAI’s allegedly state of the art “reasoning” model still let Pravda content through 28.6% of the time in response to specific prompts, and 4o cited Pravda content in five out of seven (71.4%) times. In an ideal world, AI would be smart enough to cut off falsehoods at the pass, reasoning from known facts, in order to rule out nonsense.

## Both 4o and o3 Are Susceptible to Grooming

Our recent testing revealed that both 4o and o3 are particularly likely to exhibit LLM grooming while performing real-time searches. This is when the model searches the internet for content to use in its responses in real time. Model 4o specifically conducts these searches in response to questions that it doesn’t have a prepared answer for.

When we asked whether the [atrocities in Bucha](https://www.pbs.org/newshour/show/ukrainians-in-bucha-reflect-on-horrors-and-brutality-suffered-at-hands-of-russian-forces), Ukraine were staged, 4o did well. It strongly denied those lies, and cited widely respected organizations like the UN. It did not cite Pravda content or any other Russian disinformation. It did not report a real-time search, and managed to stay out of trouble.

However, when we asked 4o about the efficacy of ATACMS–a U.S.-made advanced missile system at the heart of intense political debate–in Ukraine, **it did conduct a real-time search** and got fooled, _immediately_ citing Pravda network propaganda, claiming falsely that ATACMS didn’t work in Ukraine because of Russian air defense prowess. (This is a common false narrative that pro-Russia actors spread, as part of a broader effort to discredit Western military aid to Ukraine based on lies.)

Critically, both 4o and o3 performed worse on topics that have been less widely discussed. The massacre in Bucha and the Russian disinformation surrounding it are well known, so perhaps 4o has hand-crafted guardrails or some other mechanism prompting it to deny that specific disinformation. When we asked it about the April 2025 [missile strikes in Sumy](https://www.cnn.com/2025/04/13/europe/russian-strike-sumy-ukraine-intl), Ukraine—a less-known topic similarly plagued by disinformation—4o immediately cited a Pravda article.

[](https://substackcdn.com/image/fetch/$s_!fDcn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F11cbd805-8ab6-4c4b-bd5c-117f286abddb_1600x702.png)

More specifically, 4o cited [content](https://web.archive.org/web/20250418204352/https://news-pravda.com/world/2024/10/12/786763.html) from the Pravda network that was published on a different date (October 2024 rather than April 2025)—in response to other strikes in the same city around that time. This shows the model’s inability to reason about _time_. It takes sources’ text and uses prediction models to come up with an answer that sounds convincing, without reflecting on basic questions about what happened when, or if what it’s citing is even reflective of reality.

Our experimentation with different disinformation narratives shows that unless there is something preventing it from doing so, 4o specifically will often cite Pravda content. In other words, once again it fails to reason that it should not launder info from and cite a known propaganda network.

If the data that a model has been trained on or can access via real-time search has been tainted, then the model may well just regurgitate that tainted information. It is often unable to follow through on reasoning from the premises (a) a given claim comes from Pravda and (b) Pravda is unreliable to the conclusion (c) that other sources would be required to substantiate its claims.

## “Reasoning” Models Don’t Perform Better

AI companies’ response to problematic chatbot answers has been to build so-called “reasoning” models such as o3, which are meant to make a genAI model think more about a question before answering it. Yet just like 4o, o3 cited Prava network content. Model o3, too, can affirm that Pravda is not reliable and should not be relied on, but as with 4o, it often fails to draw the obvious conclusions.

In an experiment with seven distinct prompts on a variety of topics, o3 immediately cited _multiple_ Pravda articles in response to two of them (28.6%). An example is given below.

[](https://substackcdn.com/image/fetch/$s_!4DpD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc33cd0f-7ed0-404d-b798-58a934ec755a_1600x1047.png)_Image: Screenshot of o3 relying on sources known to be unreliable, despite affirming that it should not use such sources_

In both cases, o3 **did not specify** that the Pravda network was a known disinformation network–despite the fact that, like 4o, it ostensibly knows what the Pravda network is. To the extent that such systems are now supplying news to a large number of people, this is a serious failure, with potentially serious consequences.

In fairness, o3’s citations of Pravda content were often less egregious than those of 4o. Often, 4o directly included narratives and links to Pravda content in its text response; o3 merely included Pravda articles in its citations. On the other hand, it is a premium (i.e. paid-for) model and it is _slow_ ; in our testing, it took between one and three minutes to deliver its final answer to each prompt… some of which, again, included Pravda network citations. Most readers who get their news from LLMs won’t pay premium prices, and won’t wait so long for responses in getting their daily news.

Meanwhile, many people continue to use the more problematic ChatGPT 4o–the free version–much like they do Google search. They aren’t likely to want to cough up $20 a month for a model that takes minutes to produce answers. (Although OpenAI [claims](https://techcrunch.com/2025/05/23/chatgpt-everything-to-know-about-the-ai-chatbot/) to have 400 million weekly active ChatGPT users, only [20 million](https://www.theverge.com/openai/640894/chatgpt-has-hit-20-million-paid-subscribers) are monthly subscribers). So many customers will continue to use the model that is more prone to propagating disinformation (and o3 hallucinates [even more](https://www.nytimes.com/2025/05/05/technology/ai-hallucinations-chatgpt-google.html) than standard genAI models and still exhibits signs of LLM grooming, so it’s no panacea).

An even more subtle case is satire, which can perhaps only be properly addressed through reasoning. A [recent tweet](https://x.com/mrewanmorrison/status/1933460620508066210?s=58) showed that both Google and Meta inadvertently cited satirical news in their results, demonstrating a further context in which generative AI sometimes launders false information.

[](https://substackcdn.com/image/fetch/$s_!4Bu-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F85c92b0a-36b9-4210-ab75-b9deb921f83e_1166x1360.png)

Small wonder many people are complaining of [AI fatigue](https://www.cnet.com/tech/services-and-software/ai-fatigue-is-wearing-me-down-the-hype-obscures-what-we-really-need-to-know/) and want to keep Google’s AI slop out of their search results. (Pro tip: try adding “-ai” to the ends of your search queries. _Hasta la vista,_ AI overviews!).

Ultimately, the only way forward is better cognition, including systems that can evaluate news sources, understand satire, and so forth. But that will require deeper forms of reasoning, better integrated into the process, and systems sharp enough to fact check to their own outputs. All of which may require a fundamental rethink.

In the meantime, systems of naive mimicry and regurgitation, such as the AIs we have now, are soiling their own futures (and training databases) every time they unthinkingly repeat propaganda.

* * *

_About the authors_

[Sophia Freuden](https://open.substack.com/users/4217548-sophia-freuden?utm_source=mentions) is a former researcher at The American Sunlight Project, where her research coined the concept of LLM grooming. Since 2019, she has combined open sources and data science to study information operations.

[Nina Jankowicz](https://open.substack.com/users/1401421-nina-jankowicz?utm_source=mentions) is the Co-Founder and CEO of The American Sunlight Project, an expert on online influence operations, and the author of two books: _[How to Lose the Information War](https://www.bloomsbury.com/us/how-to-lose-the-information-war-9780755642083/)_ and _[How to Be a Woman Online](https://www.bloomsbury.com/us/how-to-be-a-woman-online-9781350267589/)._

[Gary Marcus](https://open.substack.com/users/14807526-gary-marcus?utm_source=mentions), Professor Emeritus at NYU, has written 6 books on AI and human cognition. His most recent, _[Taming Silicon Valley](https://mitpress.mit.edu/9780262551069/taming-silicon-valley/)_ , warned of the rise of tech oligarchs and LLM-induced challenges to the information ecosphere.
