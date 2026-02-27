---
title: "AI Agents have, so far, mostly been a dud"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/ai-agents-have-so-far-mostly-been"
---

If chatbots answer your queries, AI agents are supposed to do things on your behalf, to actively take care of your life and business. They might shop for you, book travel, organize your calendar, summarize news for you in custom ways, keep track of your finances, maintain databases and even whole software systems, and much more. Ultimately agents ought to be able to do anything cognitive that you might ask a human to do for you. 

By the end of 2024, Google, OpenAI, Anthropic, and many others announced that their first agents were imminent. In January, Anthropic’s Dario Amodei told the Financial Times, “[I think 2025 is going to be the year that AI can do what, like, a PhD student or an early degree professional in a field is able to do.](https://www.ft.com/content/0d1a6357-7913-4ff7-a922-643f172d7c98)” Around the same time, OpenAI’s CEO Sam Altman wrote [“We believe that, in 2025, we may see the first AI agents “join the workforce” and materially change the output of companies](https://blog.samaltman.com/reflections).” Google somewhat more modestly announced [Project Astra](https://deepmind.google/models/project-astra/), “a project on the way to building a universal AI assistant.”

Tech columnnist Kevin Roose of the New York Times, always quick to cheerlead for the industry, wrote this:

[](https://substackcdn.com/image/fetch/$s_!QlDz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78911f71-b1ff-41b4-ab20-cc54207f0da0_795x685.jpeg)

Well, maybe. But do they work? 

My own darker prediction (January 1, 2025) was that “[AI “Agents” will be endlessly hyped throughout 2025 but far from reliable, except possibly in very narrow use cases.](https://garymarcus.substack.com/p/25-ai-predictions-for-2025-from-marcus)”

With 5 months left to go, where do things stand?

§

All the big companies have in fact introduced agents. That much is true. 

But, none, to my knowledge are reliable, except maybe in very narrow uses cases. Astra is in beta (or perhaps alpha) only available via [a “wait list for trusted testers](https://deepmind.google/models/project-astra/).” OpenAI actually released [their ChatGPT agen](https://openai.com/index/introducing-chatgpt-agent/)t [rather unconventionally the word _agent_ is not capitalized in the name].

ChatGPT agent sounds pretty much just like an agent ought to – but comes with a lot of caveats. 

> _ChatGPT now thinks and acts, proactively choosing from a toolbox of agentic skills to complete tasks for you using its own computer…._
> 
> _For instance, it can gather information about your calendar through an API, efficiently reason over large amounts of text using the text-based browser, while also having the ability to interact visually with websites designed primarily for humans._
> 
> _All this is done using its own virtual computer, which preserves the context necessary for the task, even when multiple tools are used—the model can choose to open a page using the text browser or visual browser, download a file from the web, manipulate it by running a command in the terminal, and then view the output back in the visual browser. The model adapts its approach to carry out tasks with speed, accuracy, and efficiency._

But also 

> ChatGPT agent is still in its early stages. It’s capable of taking on a range of complex tasks, but it can still make mistakes …. this introduces new risks, particularly because ChatGPT agent can work directly with your data, whether it’s information accessed through connectors or websites that you have logged it into via takeover mode.

In practice, those mistakes and errors have greatly limited the utility agents like ChatGPT agent. The “pushing the boundaries of what’s possible” that Roose promised us? Largely absent.

§

Even by the end of March, people were starting to see that reality and hype weren’t lining up, as in this Fortune story about a system called Manus (March’s flavor of the month, now largely forgotten), reporting that [“some AI agent customers say reality doesn’t match the hype](https://fortune.com/2025/03/20/ai-agents-not-living-up-to-the-hype-eye-on-ai/)”. That sentiment that has only grown over the last several months. 

In recent weeks, there have been multiple reports like this:

[](https://substackcdn.com/image/fetch/$s_!4moi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0ba0a451-b703-4879-a2bf-76be0e9e8ef6_1138x1149.jpeg)

[AI coding agents also seem to be incurring a large amount of technical debt](https://devops.com/ai-in-software-development-productivity-at-the-cost-of-code-quality/), writing large amounts of [copypasta ](https://en.wikipedia.org/wiki/Copypasta)code that is hard to debug. As MIT Prof Armando Solar-Lezama told the WSJ, AI is like a “brand new credit card here that is going to allow us to accumulate technical debt in ways we were never able to do before.” Or to a paraphrase [an old saying that goes back to 1969](https://quoteinvestigator.com/2010/12/07/foul-computer/), “To err is human, to really screw up takes an AI agent.” 

§

Penrose.com [created a benchmark](https://accounting.penrose.com/) for basic account balance tracking, using a year’s worth of actual data from places like Stripe — and found a result that I suspect will be typical: AI errors tend to compound over time. (In fairness, ChatGPT agent wasn’t yet out when Penrose ran the test, but I would be surprised if their results were wildly different).

[](https://substackcdn.com/image/fetch/$s_!sR_x!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8547417a-d656-48a0-bee7-f0164afcf1c2_1221x1000.png)

§

The unrelenting hallucinations problem frequently rears its ugly head:

[](https://substackcdn.com/image/fetch/$s_!gxFg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6548f9c3-3475-4cd0-a6e3-fca9239c8cf5_1475x1750.png)

§

Someone working in the AI agent industry posted the following critique on reddit; the “demo to reality” issue they mention is _exactly_ what we should expect — probably for a years to come:

[](https://substackcdn.com/image/fetch/$s_!Sr5n!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F93fca38b-b65a-45ab-beab-56775b95418c_1412x1375.png)

§

In July Futurism ran an analysis reporting that “[the percentage of tasks AI agents are currently failing at may spell trouble for the industry](https://futurism.com/ai-agents-failing-industry)”, adding that the “[failure rate is absolutely painful](https://futurism.com/ai-agents-failing-industry)”, drawing on a [CMU benchmark, AgentCompany, that showed failure rates of 70% on some tasks](https://arxiv.org/pdf/2412.14161).

§

One of X’s most enthusiastic and generally optimistic influencers forlornly posted this a few days ago, “[serious question: do any of you use the ChatGPT agent? And if so: for which use-case? I just can’t find a use-case that matches its (limited) capabilities](https://x.com/kimmonismus/status/1950857721265480030?s=61)”. And on Tuesday Jeremy Kahn, at Fortune, often enthusiastic about AI, [wrote this](https://view.mail.fortune.com/?qs=7cfdadc6c3221781a29c5603cfed8da4891480ff024a6135b1334e666180bdfe7fb5b99a246c8a30c4c6b841e1c3945edc29494e3992cd49b33031c81040ec84247a27d7dac44e49301953c282e93714):

[](https://substackcdn.com/image/fetch/$s_!2-8a!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa67e793a-92c2-40b1-a846-32e906a716d9_1172x1112.png)

§

As a consequence of their superficial understanding of what they’re being asked, current agents are _grossly_ vulnerable to cyberattacks. 

As CMU PhD student Andy Zou recently reported, as part of [a large multi-team effort](https://arxiv.org/abs/2507.20526):

[](https://substackcdn.com/image/fetch/$s_!g0dI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3fd65f4f-8eb2-4cb7-8ddb-f5baba204ef5_1368x1412.png)

Even the most secure system was undermined 1.45% of the time, which meant that over fifteen hundred attacks were successful. (Even one successful attack can be devastating. An important, publicly-visible system that can be beat in .001% of the times it is attacked is a mess.) 

§

None of these flaws should surprise anyone. What drives LLMs (and what drives the current batch of agents) is mimicry, and not what Ernest Davis and I called in 2019 _deep understanding_. 

Current systems can _mimic_ the kinds of words people use in completing tasks, often in contextually relevant ways, but that doesn’t really mean that they _understand_ the things that they are doing; they have no concept of what it means to delete a database or make up a fictitious calendar entry. Whether they commit such blunders or not is mainly just a matter of what they happen to mimic. Sometimes mimicry works, and sometimes it doesn’t. As I have often emphasized, that’s when we get hallucinations and boneheaded reasoning errors.

Importantly, agentic tasks often involve multiple steps. In fundamentally unreliable systems like LLMs, that means multiple chances for error. Soon or later, those errors catch up. That can and sometimes does lead to catastrophe.

§

I don’t expect agents to go away; eventually AI agents will be among the biggest time-savers humanity has ever known. There is reason to research them, and in the end trillions of dollars to be made.

But I seriously doubt that LLMs will ever yield the substrate we need. 

One of the week’s most telling reports came from _[The Information](https://www.theinformation.com/articles/inside-openais-rocky-path-gpt-5?utm_source=ti_app&rc=dcf9pt) ,_ which, drawing on a scoop at OpenAI, basically affirmed what I have been saying all along (albeit without citing my earlier analyses): pure scaling is not getting us to AGI; returns are diminishing. GPT-5, they report, will not be the jump over GPT-4 that GPT-4 was over GPT-3. 

[](https://substackcdn.com/image/fetch/$s_!F2TU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d0de856-0fc3-4691-a60c-b7d9d96db071_2388x1486.png)

[Another new paper](http://arxiv.org/abs/2507.19703) this week argued that LLMs are confronting a wall (echoing [my own infamous phrase](https://archive.ph/6hEYS)):

[](https://substackcdn.com/image/fetch/$s_!UEqQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3b7ff6f-d4be-47bb-be81-238bed279295_1379x2167.jpeg)

§

Without [neurosymbolic AI that is more deeply integrated](https://open.substack.com/pub/garymarcus/p/how-o3-and-grok-4-accidentally-vindicated?r=8tdk6&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) in systems as a whole, with [rich world models](https://garymarcus.substack.com/p/generative-ais-crippling-and-widespread?r=8tdk6) as a central component, generally following [the approach I laid out five years ago](https://arxiv.org/abs/2002.06177), I just don’t see how agents can work out. Reliable agents may not require “artificial general intelligence”, but they surely require what I called in 2020 “robust”, trustworthy AI. LLMs aren’t getting us there.

Someday, I predict, the failure of current agents to produce much of lasting value will be seen as a poignant reflection of a massive mistake, intellectually and economically speaking: the mistake of investing almost solely in LLMs, as a kind of hopeful shortcut. The idea was that we could avoid facing the challenges that classical AI struggled with, simply by gathering lots of data and stirring in massive amounts of compute. This has made a small number of people (most notably Nvidia CEO Jensen Huang) massively wealthy, but after years and what must be close to a trillion dollars invested this appproach has failed to yield systems that can reliably handle your calendar or your bank accounts, let alone serve as the PhD-level agents we have been promised. 

Yet more good money is being poured after bad. Staggeringly large amounts of money. According to Renaissance Macro Research, “AI CapEx” which they “define as information processing equipment plus software has added more to GDP growth than consumers' spending.” In a rational world, generative AI would be penalized for failing to meet expectations around agents; in the actual world, investors and big tech companies are continuing to pour on the gas.

Meanwhile alternative approaches like neurosymbolic AI continue to be wildly underfunded, receiving, if I had to guess maybe 1%, probably less, of total investments. Investors, who want near immediate returns, seem unwilling to go there, and seem resistant to exploring genuinely new avenues. Venture capitalists style themselves as brave funders of innovation, but in the current climate, they are anything but.

Perhaps after enough failures of AI agents, which shouldn’t be trusted with your calendar let alone your credit cards, reality may finally start settle in. 

_**Gary Marcus** founded a machine learning company sold to Uber and is the author of six books on natural and artificial intelligence_. 
