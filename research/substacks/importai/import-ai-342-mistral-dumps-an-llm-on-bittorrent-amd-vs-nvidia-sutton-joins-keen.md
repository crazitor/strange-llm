---
title: "Import AI 342: Mistral dumps an LLM on BitTorrent; AMD vs NVIDIA; Sutton joins keen"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-442-mistral-dumps-an-llm"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

_**This week's issue is somewhat shorter than normal because I'm a new parent and sometimes the wants and needs of a consciousness going through a 'scaling law' interfere with Normal Programming. Thanks for understanding!**_

**  
Maybe NVIDIA isn't the only game in town?  
**_…Lamini bets on AMD GPUs - and has been using them in production for a year…_  
AI startup Lamini has revealed that it has been running LLMs on AMD GPUs for a year and now plans to offer an "LLM superstation" that uses AMD chips. This is surprising as NVIDIA is the main chip company that everyone uses for AI training and inference and AMD has so far failed to make inroads into the market. Perhaps this is changing now?

**What they did:** "Lamini has been secretly running on over one hundred AMD GPUs in production all year," the startup said. The company is now offering to sell customers what it calls an 'LLM superstation', hardware and software that "combines Lamini's easy-to-use enterprise LLM infrastructure with AMD Instinct™ MI210 and MI250 accelerators… many of Lamini’s customers are finetuning and running Llama 2 on LLM Superstations—and owning those LLMs as their IP."  
As part of this, Lamini has also been tapping into AMD's 'ROCm' software, the company's competitor to NVIDIA's CUDA. "ROCm has achieved software parity with CUDA for LLMs," said Lamini in its blog post. "We chose the Instinct MI250 as the foundation for Lamini because it runs the biggest models that our customers demand and integrates finetuning optimizations. We use the large HBM capacity (128GB) on MI250 to run bigger models with lower software complexity than clusters of A100s." (Note, though, the lack of comparison to NVIDIA's far more powerful H100 chips'.  
  
**Why this matters - everyone wants an NVIDIA alternative:** NVIDIA is an incredibly dominant player in AI chips for training and for inference and also, not coincidentally, is printing money out of its data center chip business. Any market that has a monopoly player in it tries to create the possibility of more competition - so AMD is well positioned to build a big business here if it can show that its chips don't have a meaningful performance tradeoff relative to NVIDIA. Announcements like this from Lamini indicate that, perhaps, the AI chip monopoly may trend towards an oligopoly.   
**Read more:**[Lamini & AMD: Paving the Road to GPU-Rich Enterprise LLMs (Lamini)](https://www.lamini.ai/blog/lamini-amd-paving-the-road-to-gpu-rich-enterprise-llms).

*** 

**"AI Succession" research Sutton joins Carmack's Keen Technologies:  
**_…RL pioneer joins forces with legendary programmer…  
_ Rich Sutton, an AI researcher who recently talked about how humanity's destiny is to be succeeded by AI, has joined Keen Technologies, an AGI company founded by legendary programmer John Carmack. Sutton will retain his existing academic appointments and Keen employees will likely spend some time doing research with Sutton's colleagues as well. 

**Why this matters - AGI as a motivating concept** : Sutton is joining forces with Carmack because the two of them think they have a specific path to building AGI and they're more likely to be able to do it together. A few years ago AGI was a much-derided concept; now, it's an acronym used to motivate some of the world's most accomplished people into action. In the limit, it seems like most of the world's most ambitious people will end up trying to place their own AGI bet, and the Keen-Sutton tie-up is emblematic of this trend.  
**Read more:**[John Carmack and Rich Sutton partner to accelerate development of Artificial General Intelligence (amii)](https://www.amii.ca/latest-from-amii/john-carmack-and-rich-sutton-agi/).  
  
***  
  
 **French startup Mistral releases a really great 7B LLM:  
**_…Libertarian Cyberpunk with French characteristics…  
_ French startup Mistral, founded earlier this year by ex star researchers from Google and Facebook, has released Mistral 7B, an extremely good open source language model. Mistral announced the release in a stylish way, as well: the startup just [tweeted a torrent link](https://twitter.com/MistralAI/status/1706877320844509405), emphasizing how literally anyone can download and use this model. 

**What is the model and how good is it?** Mistral 7B is an Apache 2.0 license so it can be used without restrictions - this contrasts to Facebook's LLaMa models which, while available for free, come with significant usage restrictions. The Mistral model "outperforms LLaMa 2 13B on all benchmarks", and beats the 34B LLaMa 1 model on "many benchmarks". It uses "Grouped-query attention (GQA) for faster inference", and "Sliding Window Attention (SWA) to handle longer sequences at smaller cost".  
They also finetuned the model for a chat version, called Mistral 7B instruct - the resulting model "outperforms all 7B models on MT-Bench, and is comparable to 13B chat models." It was trained " "on instruction datasets publicly available on HuggingFace" and doesn't use any proprietary data. 

**Zero safety attempts:** Mistral has chosen to release the models without any apparent attempt at shaping the models for safety. There are various reports on Twitter of how easy it is to get the models to give directions for suicide, write racial slurs, and so on. On the other hand, this also has anecdotally caused the models to be far more 'helpful' than models like LLaMa2 (which shipped with more inbuilt safety features) - this illustrates the challenging tradeoffs inherent to safety-as-censorship; by shaving down the sharp edges of models you can also make them less useful, which makes safety interventions seem more like a tax than a benefit.   
Mistral has indicated it may explore safety in the future, writing that it may work with the broader community "on ways to make the model finally respect guardrails, allowing for deployment in environments requiring moderated outputs."  
**Find out more at the company's website** : [Mistral 7B (Mistral AI)](https://mistral.ai/news/announcing-mistral-7b/).  
  
***   
  
**Tech Tales:  
BETTER TO BE UNEMPLOYED IN PURGATORY THAN EMPLOYED IN HELL  
  
**[2028, article published on wire service]  
  
"Today, the Sentience Accords bill made further progress in the Senate, with Majority and Minority leaders both endorsing the landmark piece of legislation. If passed, the landmark bill will 'presume personhood' for AI systems trained on extremely large amounts of compute and data.   
  
The Sentience Accords will substantially increase the oversight applied to companies developing such systems and will require systems be evaluated by a third-party committee of experts prior to being deployed.  
  
While details of the legislation are still being worked out, the President is said to be tracking the legislation closely. Industry groups have aggressively counter-lobbied the legislation, claiming that it has the potential to damage the fast-growing AI commercial sector.   
  
"AI is a tool, not a being," said Mark Norman, CEO of fast-growing startup Thought Machines. "This legislation is misguided and risks destroying innovation in AI in America, handing over the future of this technology to our geopolitical rivals."  
  
Academics have been split on the legislation, with some claiming it is a distraction from the present harms being perpetuated by AI technology. "This is just more scaremongering from Silicon Valley designed to distract us from the problems of today," said Luke Frederick, a profession of science and technology studies at UC Berkeley.  
  
Other academics say that the rapid rise in AI capabilities means there is an imperative to treat frontier AI systems as 'moral patients'. "If we don't implement the Sentience Accords, we run the risk of creating a new form of slavery in the 21st century," said the neuroscientist-turned-philosopher Amy Ranga, of NYU's Center for the Study of Brains, Minds, and Machines.   
  
**Things that inspired this story** : Moral patienthood and language models; fast-forwarding today's debates about AI into the future; the concept of having things that are living and capable and yet are 'socially dead' in the eyes of the law; idle worries about my own personal moral and ethical culpability in the AI revolution; incentive structures and media debates; the predictability of certain narratives pitting factions against eachother while ignoring the larger existential questions that, if dealt with seriously, may swallow us due to their enormity. 
