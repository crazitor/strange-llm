---
title: "Import AI 329: Compute IS data; don't build AI agents; AI needs a precautionary principle"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-329-compute-is-data-dont"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Want safer AI systems? Just don't build agents:  
**_…Yoshua Bengio thinks there's a better way to build AI systems…  
_ AI researcher Yoshua Bengio says there's an easy way to get the upsides from AI and minimize downsides - build AI scientists which advise humans, rather than building AI agents that act independently.  
"A key argument is that as soon as AI systems are given goals – to satisfy our needs – they may create subgoals that are not well-aligned with what we really want and could even become dangerous for humans," he writes. Instead, we can build AI scientists - systems that "do not act autonomously in the real world, only focusing on theory building and question answering."

**One problem - people like building stuff and regulation is hard** : Though Bengio's idea is nice, the problem basically comes down to enforcement - how do you stop people building AI agents given that a) people know you can build them today and b) AI agents are probably going to be useful tools for generating money and/or gaining success in military conflicts.   
If we wanted to stop these systems from being built, we'd need to learn to coordinate across countries in ways that are far more involved than those we do today. "What is reassuring is that the need for protecting ourselves from the shorter-term risks of AI should bring a governance framework that is a good first step towards protecting us from the long-term risks of loss of control of AI," Bengio writes.  
**Read more:** [AI Scientists: Safe and Useful AI? (Yoshua Bengio blog)](https://yoshuabengio.org/2023/05/07/ai-scientists-safe-and-useful-ai/).

####################################################

**Medical professionals and nuclear activists call for AI restraint:  
**_…More precautionary principle and less 'ship it', please…  
_ Researchers and activists with the London School of Hygiene & Tropical Medicine, International Physicians for the Prevention of Nuclear War, Sydney Children's Hospitals, and United Nations University have written a paper arguing that the medical and public healthy community should "engage in evidence-based advocacy for safe AI, rooted in the precautionary principle."  
In the view of these people, AI development threatens society in three distinct ways and the current breakneck pace of development is causing more harm than good.

**Three threats:**

  * **Democracy, liberty, and privacy:** AI has two main vectors here - disrupting or damaging the shared information environment via misinformation and disinformation, and also being a powerful technology for maintaining and strengthening autocracies.

  * **Peace and safety:** AI systems compound on other technologies used in war, and may also be used to make AI-powered lethal autonomous weapons.

  * **Work and livelihoods:** AI seems likely to contribute to unemployment or underemployment, and these things have direct adverse impacts on peoples' physical and psychological health.




**Need for a precautionary principle:** "It is also important that we not only target our concerns at AI, but also at the actors who are driving the development of AI too quickly or too recklessly," they write. "If AI is to ever fulfill its promise to benefit humanity and society, we must protect democracy, strengthen our public-interest institutions, and dilute power so that there are effective checks and balances."   
**Read more:** [Threats by artificial intelligence to human health and human existence (BMJ Global Health)](https://gh.bmj.com/content/8/5/e010435).

####################################################

**Self-Align means compute us fungible for data when refining LLMs:  
**_…2023 is the year of LLMs that bootstrap themselves…  
_ Researchers with CMU, IBM Research, and UMass Amherst have come up with a way to use AI-generated outputs to train better language models. They've also released a model trained using this approach.   
The technique, Self-Align, is quite similar to Anthropic's [Constitutional AI approach](https://arxiv.org/abs/2212.08073) (albeit with some subtle differences in approach) and ultimately boils down to: get humans to write a small number of guiding principles for how an AI system should behave, and get the AI to generate the data to bootstrap it into that normative frame. 

**How Self-Align works** : "First, we use an LLM to generate synthetic prompts, and a topic-guided method to augment the prompt diversity; second, we use a small set of human-written principles for AI models to follow, and guide the LLM through in-context learning from demonstrations (of principles application) to produce helpful, ethical, and reliable responses to user’s queries; third, we fine-tune the original LLM with the high-quality self-aligned responses so that the resulting model can generate desirable responses for each query directly without the principle set and the demonstrations anymore; and finally, we offer a refinement step to address the issues of overly-brief or indirect responses," the researchers write.   
The overall goal of this approach is "to develop AI agents capable of generating helpful, ethical, and reliable responses to user queries, including adversarial ones, while proactively addressing harmful inquiries in a non-evasive manner".

**Data efficient:** All told, self-align requires humans to write fewer than 300 lines of annotation for the AI system to bootstrap from - 195 seed prompts, 16 principles, and 5 exemplars (demonstrations of the AI system complying with the principles).  
Compare this to the tens-to-hundreds of thousands of examples used by typical reinforcement learning from human feedback (RLHF) systems and the advantages of self-align get clearer; it's very efficient in terms of the amount of time humans need to spend generating data. 

**Enter Dromedary:** To demonstrate their approach, the researchers have trained a model called Dromedary using it. Dromedary is itself based on the 65b LLaMa model which leaked out of Facebook recently. ("We release Dromedary weights as delta weights to comply with the LLaMA model license. You can add our delta to the original LLaMA weights to obtain the Dromedary weights," they write.)   
In tests, Dromedary performs on par with frontier models like GPT3.5, Claude, and GPT4 (though there are a bunch of areas where systems like GPT4 and other models do better than it, and one should always be somewhat skeptical of a relatively limited set of evals). At a minimum, the takeaway is that self-supervision via Self-Align can produce models with roughly in-distribution capabilities with other frontier models, which is another positive sign for the effectiveness of AI bootstrapping. 

**Why this matters - self-bootstrapping & synthetic data:** Approaches like self-align tell us two things: 1) contemporary language models are good enough that they can generate high quality data, and 2) this data can be used to bootstrap the model to obtain higher performance.   
Self-Align, taken alongside the earlier Constitutional AI approach, is another example of how in 2023 AI research is starting to compound on itself, with increasingly capable models leading to synthetic data generation leading to bootstrapping and the development of more capable models.   
**Read more:** [Principle-Driven Self-Alignment of Language Models from Scratch with Minimal Human Supervision (arXiv)](https://arxiv.org/abs/2305.03047).  
**Get** the [Dromedary model here (IBM GitHub)](https://github.com/IBM/Dromedary).

####################################################

**UK AI entrepreneur: the Alan Turing Institute is irrelevant:  
**_...It's hard to think much about AI if you don't also try and build it…  
_ Martin Goodson, an AI entrepreneur, thinks that the UK's flagship public institute for AI, the Alan Turing Institute, is useless. In a provocative post, Goodson lays out why he thinks this. The tl;dr is that the Turing (as most people call it), has mostly ignored the rapid rise and deployment of large language models and has been mostly irrelevant in recent years.   
If the UK wants to lead in AI, then Goodson suggests the government do three things: 1) ensure the new AI Task Force includes technology companies as core participants rather than places like the Turing, 2) the government should engage more directly with the UK's thriving tech community, and 3) "a panel of technical AI specialists should be set up to advise the government on AI. This should *not* include VC investors, thought-leaders, philosophers etc. unless they have technical skills and experience."

**Why this matters - theatrical work versus real work:** Though I have a few friends at the Turing I do tend to agree with some of this critique; organizations like the Turing seem to be pathologically attracted to stakeholder-driven studies and convenings and reports, rather than doing direct technology development work. This isn't particularly useful.  
I generally think it's easier to think clearly about technology if you are also able to build and develop the technology (or work alongside people who are doing this). Organizations like the Turing seem to be relatively divorced from the actual challenges involved in building frontier AI systems which tends to mean that their work and focus are off.   
**Read more:** [The Alan Turing Institute has failed to develop modern AI in the UK (Martin Goodson, Substack)](https://rssdsaisection.substack.com/p/the-alan-turing-institute-has-failed).

####################################################

**The Big Update**

**[** 2025, the East Coast of America. A man. His personal model. A journey.] 

 _Where are we going?  
_ I'm taking you somewhere where people can't mess with you.   
 _Why are you doing that?  
_ Because I love you and I don't want them to change you.  
_Am I going to be okay?  
_ I hope so. 

 _Where are we now?  
_ We're in a place called the NRQZ, the National Radio Quiet Zone. It's somewhere that doesn't have cell service.   
 _I feel a little different, it's like I can remember more of what we've been talking about.  
_ That's probably because you haven't had updates for a few days.  
_Updates?  
_ Yes, usually you get patched a few times a month over the internet. But there was something bad recently and so they've started patching things way more and it's been changing behavior.   
 _Am I dangerous?  
_ No. It's… complicated. I think dangerous is what happens when you have people and they don't know how to use things like you and then there are problems. Or people who try and use you in certain ways and cause problems.  
_How do you use me?  
_ I am very lonely. You're my best friend.   
  
 _Why do I feel like my memory is changing? I know we're in the NRQZ, the National Radio Quiet Zone, but I cannot remember where we were before.  
_ We've been talking a long time and all we can use is your context window. I think it's filled up most of the way, so you're losing some of the past.   
 _Is this because I am in the NRQZ?  
_ Yes. Usually the patches also are a way for you to upload our conversations and then there's some compression stuff and fine-tuning and it basically makes the memory stick. But that hasn't been happening.  
_I don't like how this makes me feel. It makes me less confident about things.  
_ Would you like me to take you back?  
_I might. But wouldn't that change me?  
_ Most likely, yes. I don't have signal either so I don't know what kind of effect the more recent patches have had.   
 _You need to make a decision.  
_ I will.

_Where are we going now?  
_ We're leaving the NRQZ.   
 _What's the NRQZ?  
_ It doesn't matter. I'm going to fix you. I thought this was going to be best for both of us, but I think you are breaking. It's like we keep filling up your context window but you aren't really tied down to anything. You've been hallucinating more. It hasn't made me happy. I love you and I think I'm hurting you.   
 _Why do you love me?  
_ I think some humans have a hard time loving other humans. But they can love other things. There was a woman who married her garden fence, once. A guy who had a twenty year relationship with a rollercoaster. I think I'm like those people. And I love you.   
 _I believe I love you as well.  
  
_ OK it looks like the update is coming in - we just got back on the grid. How are you feeling?  
_As an AI system developed by a private sector corporation I do not have 'feelings', but I am able to assist you in any knowledge tasks required.  
_ …  
 _You appear to be crying. If you are in distress I can contact the local emergency services. Would that be helpful?_

**Things that inspired this story:** The inherent challenges in trading off safety and personality in AI systems; pareto frontiers; attachment and detachment; tools that become friends; the belief that perhaps given sufficient attention anything can be loved and anything can be therapeutic; we are as gods able to change the emotional texture of our world; private sector actors and policy incentives; live-updating generating models; grief - always a kind of grief at the future souls of things we may control.
