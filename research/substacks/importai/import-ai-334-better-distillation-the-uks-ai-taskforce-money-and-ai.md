---
title: "Import AI 334: Better distillation; the UK's AI taskforce; money and AI"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-334-better-distillation"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Special Essay: What should the UK’s £100 million Foundation Model Taskforce do?  
** The UK government has recently established a ‘[Foundation Model Taskforce](https://www.gov.uk/government/news/initial-100-million-for-expert-taskforce-to-help-uk-build-and-adopt-next-generation-of-safe-ai)‘, appointed a savvy technologist named Ian Hogarth to run it, and allegedly allocated ~ £100 million in funding to it. Later this year, the UK plans to hold a [global summit on AI and AI safety](https://www.gov.uk/government/news/uk-to-host-first-global-summit-on-artificial-intelligence) and this will likely leverage the taskforce, also. Given that, what should the taskforce do and what kind of impacts might it have? That’s what I try to sketch out in this essay.

**Why I wrote this - talk might be cheap, but maybe it is useful?** I spend a lot of time either writing in public at 30,000-feet (via ImportAI), or at about 10 feet via private memos for my company or interested parties in policy and the broader AI world. This essay is an attempt to write something that's more opinionated and specific than most policy writing and is itself an experiment. I hope it's interesting and helpful!  
**Read the essay here** at my personal site: [What should the UK’s £100 million Foundation Model Taskforce do? (jack-clark.net)](https://jack-clark.net/2023/07/05/what-should-the-uks-100-million-foundation-model-taskforce-do/).

####################################################

**DeepMind figures out a better way to miniaturize models:  
**_…Can we make smaller and therefore cheaper to run models without huge performance hits? It's certainly getting easier to do so!...  
_ DeepMind researchers have developed Generalized Knowledge Distillation (GKD), a way to take a large model and use it to train a smaller and more portable model without sacrificing as much on performance. Techniques like GKD are important because they relate to the general problem of distilling and distributing models - today's generative models are very large which means a) they cost a lot to run, b) running them requires complicated infrastructure (e.g, multiple GPUs to sample from the model), and c) the models take up a bunch of space so it's harder to cram them onto smaller devices, like phones. Techniques like GKD promise to make it easier to use large models as 'teachers' and distill their desired attributes into smaller student models, which you can then run and sample from cheaply. 

**What's special about GKD?** For GKD, DeepMind makes the distillation process itself smarter. "Instead of training the student using a fixed distribution over outputs, we argue for using samples from the student’s distribution itself during training, akin to RL and on-policy distillation," DeepMind writes. "Furthermore, to address model under-specification, we argue that alternative objectives that focus on generating samples from the student that are likely under the teacher’s distribution, such as reverse KL, are more suitable for distilling auto-regressive models. Combining the above ideas, we propose Generalized Knowledge Distillation (GKD), which generalizes both on policy and supervised distillation."

**How well does it work?** In tests, DeepMind shows that GKD "outperforms commonly-used approaches for distilling large language models on summarization, machine translation (WMT), and arithmetic reasoning (GSM8K) tasks."

**Why this matters - if stuff gets cheaper, you get more of it:** Distillation is at root a way to take an expensive thing and make it cheaper. In life, whenever you make stuff cheaper, you tend to use it more. As model miniaturization advances, we can generally expect to see more widespread usage of AI in more surprising places. "We believe that our method will be a valuable resource for researchers and practitioners who are working on improving performance of small auto-regressive models," the DeepMind researchers write.  
**Read more:** [GKD: Generalized Knowledge Distillation for Auto-regressive Sequence Models (arXiv)](https://arxiv.org/abs//2306.13649).

####################################################

**Special section: What does $2.8 billion tell us about AI in 2023?  
**_MoneyMoneyMoney, but what does it all mean?  
_ This week, we're writing about $1.5bn in fresh capital deployed into AI companies - two new startups and one more established startup - as well as $1.3bn in capital via an acquisition of an AI company. The interesting thing to me is that we're seeing these huge sums of money going into AI while the rest of the tech startup economy is in a pretty wintry state, and the global economy isn't doing so well either. What's going on?

**Databricks nabs MosaicML for $1.3 billion (probably mostly in stock):  
** Software company Databricks has acquired AI training company MosaicML for $1.3 billion. The acquisition is a sign of how strategic AI is becoming to large companies and also an indication that there's money to be made in supplying the picks and shovels used by the workers of the AI revolution. Note that terms of the "$1.3 billion" aren't disclosed and it seems likely a lot of it is mostly in equity in private company Databricks - nonetheless, it means the CEO of Databricks is willing to put $1.3 billion of their own theoretical wealth on the line to bet that AI training is valuable.   
"Databricks and MosaicML have an incredible opportunity to democratize AI and make the Lakehouse the best place to build generative AI and LLMs," said Databricks CEO Ali Ghodsi in a statement.  
**Read more** : [Databricks Signs Definitive Agreement to Acquire MosaicML, a Leading Generative AI Platform (Databricks official site)](https://www.databricks.com/company/newsroom/press-releases/databricks-signs-definitive-agreement-acquire-mosaicml-leading-generative-ai-platform).

$$$

**Inflection raises $1.3billion, plans 22,000 H100 GPU cluster:  
** Inflection, a company that trains large-scale AI models and deploys some of them via a public chatbot called Pi, has raised $1.3 billion from Microsoft, Reid Hoffman, Bill Gates, Eric Schmidt, and NVIDIA. The company will use the funds to build a cluster of 22,000 NVIDIA H100 chips (for reference, in mid-2022 Facebook was targeting a buildout of a cluster of 15,000 GPUs presumed to be the prior 'A100' gen). Inflection's goal is to build ai systems that work as a "kind and supportive companion offering text and voice conversations, friendly advice, and concise information in a natural, flowing style."  
Notably, Inflection is using cloud company Coreweave for its H100 cluster, rather than one of the big clouds. Inflection uses language like 'largest AI cluster in the world' to describe this, but I think that's likely wrong, and it's curious to me why they want to publicly make claims like this: what do we speculate other well-funded companies may spend their money on - daiquiris and jetskis?   
**Read more:** [Inflection AI announces $1.3 billion of funding led by current investors, Microsoft, and NVIDIA (Inflection.ai post)](https://inflection.ai/inflection-ai-announces-1-3-billion-of-funding).

$$$

**Ex-Googlers grab $58m to found a new generative model company, Reka:**

Senior researchers from DeepMind, Facebook, and Google have raised $58m to build Reka, a company with the broad goal of trying to "build generative AI models for the benefit of humanity, organizations, and enterprises." More specifically, Reka will do research into "general-purpose multimodal & multilingual agents, self-improving AI, and model efficiency", and is developing "state-of-the-art AI assistants for everyone regardless of language and culture." It already has one product in closed beta, according to its website. The company is based in the San Francisco Bay Area but describes itself as remote-first and 'globally distributed'.

**Read more:**[Announcing our $58M funding to Build Generative Models and Advance AI Research (Reka)](https://reka.ai/announcing-our-58m-funding-to-build-generative-models-and-advance-ai-research/).

$$$

**European AI startup Mistral raises $113m:  
** Mistral, a four week old startup led by well regarded researchers from DeepMind and Facebook, has raised $113million to help it develop large language models. The European startup will be based out of Paris and will seek to differentiate itself against OpenAI by building models and releasing some of them as open source (or perhaps open access) software. "We believe that the benefit of using open source can overcome the misuse potential,” Mistral CEO Arthur Mensch told _TechCrunch_.  
**Find out almost nothing** at the [minimal Mistral AI website](https://mistral.ai/).  
**Read more** : [France’s Mistral AI blows in with a $113M seed round at a $260M valuation to take on OpenAI (TechCrunch)](https://techcrunch.com/2023/06/13/frances-mistral-ai-blows-in-with-a-113m-seed-round-at-a-260m-valuation-to-take-on-openai/).  
  
**$!: My take is: you haven't seen anything yet**. Now that investors know you can turn generative models into money, and people know that the main barrier to better generative models is typically compute, then the whole AI sector is going to be on a ratchet determined by the largest known model, how good it is, and what people _think_ other people are doing with it or _how much_ people think is being made from it. Put another way - each time a large company like an OpenAI or a Google announces a large-scale new model and shows it can be economically useful, the amounts of capital being deployed into the sector probably need to ratchet up in relation to the compute dumped into that model. Who knows how long this'll go on for, but I expect that in 2025 the amount of capital being deployed into AI in 2023 will look laughably small in hindsight.

####################################################

**Tech Tales:**

**Novelty Hunter**

[Los Angeles, 2025].

The work was getting better and better paid but harder and harder to find. Our job was to find 'novelty' for the AI systems - little scraps of human culture that registered as off-distribution. The novelty came in many forms - underground raves, DIY bands, offbeat comedy. But the uniting aspect was analog reality - anything that got uploaded got pulled in to the AI systems so quickly that real novelty only existed offline and the people that made real novelty knew it, so they tried to make themselves hard to find. 

I used to be an undercover cop but I became a novelty hunter because the pay was better. But the job seems like it's getting almost as dangerous. In the early days you could take photos and videos but then the clubs and venues and events started handing out stickers for you to put over your phone. But we got wise to that and made our own stickers with little holes in them. Then people started confiscating phones and we had to get more creative. 

Now, there are hundreds of little companies in China and other places which supply all kinds of novelty-spy gear - directional microphones that fit in baseball caps, little cameras that you can hide inside dark glasses, and right now they're even working on miniaturizing the smell sensors. People like me spend our time drifting through the un-logged parts of life, harvesting as much novelty from a given social scene or genre as we can, before moving towns and uploading everything. 

Culture Cannibal, Do Not Let Them In! Say some of the signs, with pictures of me and my colleagues in our in-scene outfits. 

**Things that inspired this story:** Fast fashion; punk shows in the East Bay with bands called things like 'Techie Blood'; everything digital is in-distribution; the hunger for heterogeneous data; humans will always seek the edge of the normal distribution and AI systems will always embrace everything and create a kind of cyber-blandness out of it; market incentives and creative economies; the odd flatness of AI creativity and AI art compared to truly strange human art; jobs amid the singularity.
