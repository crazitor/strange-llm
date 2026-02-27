---
title: "A misleading open letter about sci-fi AI dangers ignores the real risks"
author: "Arvind Narayanan & Sayash Kapoor"
date: ""
source: "substack_aisnakeoil"
url: "https://www.normaltech.ai/p/a-misleading-open-letter-about-sci"
---

The Future of Life Institute released an [open letter](https://futureoflife.org/open-letter/pause-giant-ai-experiments/) asking for a 6-month pause on training language models “more powerful than” GPT-4. Over 1,000 researchers, technologists, and public figures have already signed the letter. The letter raises alarm about many AI risks:

> "_Should_ we let machines flood our information channels with propaganda and untruth? _Should_ we automate away all the jobs, including the fulfilling ones? _Should_ we develop nonhuman minds that might eventually outnumber, outsmart, obsolete and replace us? _Should_ we risk loss of control of our civilization?" ([source](https://futureoflife.org/open-letter/pause-giant-ai-experiments/); emphasis in original)

We agree that misinformation, impact on labor, and safety are three of the main risks of AI. Unfortunately, in each case, the letter presents a speculative, futuristic risk, ignoring the version of the problem that is already harming people. It distracts from the real issues and makes it harder to address them. The letter has a containment mindset analogous to nuclear risk, but that’s a poor fit for AI. It plays right into the hands of the companies it seeks to regulate. 

[](https://substackcdn.com/image/fetch/$s_!FufQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b639341-fdfe-49f8-84b0-23a9e9d32718_1812x974.png)

#### **Speculative harm 1: Malicious disinformation campaigns**

>  _Should we let machines flood our information channels with propaganda and untruth?_

The letter refers to a common claim: LLMs will lead to a flood of propaganda since they give malicious actors the tools to automate the creation of disinformation. But as we've [argued](https://aisnakeoil.substack.com/p/the-llama-is-out-of-the-bag-should), _creating_ disinformation is not enough to spread it. _Distributing_ disinformation is the hard part. Open-source LLMs powerful enough to generate disinformation have also been around for a while; we haven't seen prominent uses of these LLMs for spreading disinfo. 

Focusing on disinformation also gives companies developing LLMs the perfect justification for keeping their models locked down: to stop malicious actors from creating propaganda. This was [one reason](https://www.theverge.com/2023/3/15/23640180/openai-gpt-4-launch-closed-research-ilya-sutskever-interview) OpenAI gave for the release of GPT-4 being opaque to an unprecedented degree. 

#### **Real harm 1: Misinformation due to careless use of AI tools**

In contrast, the real reason LLMs pose an information hazard is because of over-reliance and automation bias. Automation bias is people’s tendency to over-rely on automated systems. LLMs are [not trained](https://aisnakeoil.substack.com/p/chatgpt-is-a-bullshit-generator-but) to generate the truth; they generate plausible-sounding statements. But users could still rely on LLMs in cases where factual accuracy is important. 

Consider the [viral Twitter thread](https://twitter.com/peakcooper/status/1639716822680236032) about the dog who was saved because ChatGPT gave the correct medical diagnosis. In this case, ChatGPT was helpful. But we [won't hear](https://twitter.com/random_walker/status/1640069366514606080?s=20) of the myriad of other examples where ChatGPT hurt someone due to an incorrect diagnosis. Similarly, CNET used an automated tool to draft 77 news articles with financial advice. They later found errors in [41 of the 77 articles](https://www.engadget.com/cnet-corrected-41-of-its-77-ai-written-articles-201519489.html). 

#### **Speculative harm 2: LLMs will obsolete all jobs**

>  _Should we automate away all the jobs, including the fulfilling ones?_

GPT-4 was released to much hype around its performance on human exams, such as the bar and the USMLE. The letter takes OpenAI's claims at face value: it cites OpenAI's GPT-4 paper for the claim that "contemporary AI systems are now becoming human-competitive at general tasks." But testing LLMs on benchmarks designed for humans [tells us little](https://aisnakeoil.substack.com/p/gpt-4-and-professional-benchmarks) about its usefulness in the real world. 

This is an example of [criti-hype](https://sts-news.medium.com/youre-doing-it-wrong-notes-on-criticism-and-technology-hype-18b08b4307e5). The letter ostensibly criticizes the careless deployment of LLMs, but it simultaneously hypes their capabilities and depicts them as much more powerful than they really are. This again helps companies by portraying them as creators of otherworldly tools.

#### **Real harm 2: AI tools exploit labor and shift power to companies.**

The real impact of AI is likely to be subtler: AI tools will shift power away from workers and centralize it in the hands of a few companies. A prominent example is [generative AI for creating art](https://aisnakeoil.substack.com/p/artists-can-now-opt-out-of-generative). Companies building text-to-image tools have used artists' work without compensation or credit. Another example: workers who filtered toxic content from ChatGPT's inputs and outputs were paid less than USD 2/hr. 

Pausing new AI development does nothing to redress the harms of already deployed models. One way to do right by artists would be to tax AI companies and use it to increase funding for the arts. Unfortunately, the political will to even consider such options is lacking. Feel-good interventions like hitting the pause button distract from these difficult policy debates.

#### **Speculative harm 3: Long-term existential risks**

>  _Should we develop nonhuman minds that might eventually outnumber, outsmart, obsolete and replace us? Should we risk loss of control of our civilization?_

Long-term catastrophic risks stemming from AI have a long history. Science fiction has primed us to think of terminators and killer robots. In the AI community, these concerns have been expressed under the umbrella of existential risk or x-risk, and are reflected in the letter's concerns about losing control over civilization. We recognize the need to think about the long-term impact of AI. But these sci-fi worries have sucked up the oxygen and diverted resources from real, pressing AI risks — including security risks.

#### **Real harm 3: Near-term security risks**

Prompt engineering has already allowed users to [leak](https://twitter.com/goodside/status/1598253337400717313?s=61&t=Ek-flcSs21kmGbDRAv5AbQ) confidential details about just about every chatbot that’s been released so far. As tools like ChatGPT are integrated with real-world applications, these security risks become more damaging. LLM-based personal assistants could be hacked to [reveal people’s personal data](https://twitter.com/florian_tramer/status/1639301437875273749), take harmful real-world actions such as shutting down systems, or even give rise to [worms](https://twitter.com/percyliang/status/1630087357482541062?s=61&t=p7PBo619-95SUtc7KvUYKw) that spread across the Internet through LLMs. Most importantly, these security risks do not require a leap in the capabilities of the models — existing models are vulnerable to them.

Addressing security risks will require collaboration and cooperation with academia. Unfortunately, the hype in this letter—the exaggeration of capabilities and existential risk—will likely lead to models being [locked down](https://aisnakeoil.substack.com/p/openais-policies-hinder-reproducible) even more, making it harder to address risks.

#### **The containment mindset is a poor fit for generative AI**

The letter positions AI risk as analogous to nuclear risk or the risk from human cloning. It advocates for pausing AI tools because other catastrophic technologies have been paused before. But a containment approach is unlikely to be effective for AI. LLMs are orders of magnitude cheaper to build than nuclear weapons or cloning — and the cost is [rapidly dropping](https://simonwillison.net/2023/Mar/17/beat-chatgpt-in-a-browser/). And the technical know-how to build LLMs is already widespread.

Although not well understood outside the technical community, over the last 6 months, there has been a major shift in LLM research and commercialization. Increases in model size are no longer the primary driver of increases in usefulness and capabilities. The action has moved to chaining and connecting LLMs to the real world. New capabilities and risks will both arise primarily from the thousands of apps that LLMs are being embedded into right now — and the plugins being embedded into ChatGPT and other chatbots. 

[](https://substackcdn.com/image/fetch/$s_!pvak!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0f4deed4-0dfa-40bd-8f2e-040a927517af_2020x1302.png)The adoption curve of LangChain, based on GitHub stars. LangChain is a library to connect LLMs to real-world applications. ([source: Ryan Shannon](https://ryanshannon.substack.com/p/keeping-up-with-the-overwhelming))

Another major technology trend in LLMs is compression. LLMs are being optimized to run locally on mobile devices. A [4GB model](https://github.com/nomic-ai/gpt4all) based on Meta's LLaMA LLM can run on a 2020 Macbook Air. This model’s capabilities are in the same class as GPT-3, and, of course, it is being connected to other applications. Containing such models is a non-starter, because they are easy to distribute and can run on consumer hardware. 

A better framework to regulate the risks of integrating LLMs into applications is [product safety](https://twitter.com/j2bryson/status/1640997159964139520) and consumer protection. The harms and interventions will differ greatly between applications: search, personal assistants, medical applications, etc.

Mitigating AI risks is important. But equally important is considering _what_ those risks are. Naive solutions like broad moratoriums sidetrack serious policy debates in favor of fever dreams about AGI, and are ultimately counterproductive. It is time to level up our analysis.

**Further reading**

  * In the [Stochastic Parrots paper](https://dl.acm.org/doi/10.1145/3442188.3445922), Emily Bender, Timnit Gebru, and others consider various real-world risks from LLMs. The paper was written over two years back, and the authors were ahead of many others in thinking carefully about these risks. 

  * Emily Bender also wrote a [Twitter thread](https://twitter.com/emilymbender/status/1640920936600997889?s=20) about the letter, where she dissects the AI hype in the letter and points out alternatives for addressing AI risks.

  * Laura Weidinger and others from DeepMind wrote an [overview](https://dl.acm.org/doi/10.1145/3531146.3533088) of the different types of risks posed by language models.



