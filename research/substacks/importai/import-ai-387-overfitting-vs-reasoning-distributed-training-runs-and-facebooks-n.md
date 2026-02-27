---
title: "Import AI 387: Overfitting vs reasoning; distributed training runs; and Facebook's new video models"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-387-overfitting-vs-reasoning"
---

_Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this, please subscribe. A somewhat shorter than usual issue this week - but I decided it’s better to keep the weekly cadence than to save up sections for a ‘full’ less frequent newsletter._

**Apple shows that most LLMs are overfitting:  
**_…GSM-Symbolic suggests people are teaching to the test on GSM8K, though larger models generalize better…  
_ Apple has published a benchmark which subtly varies the widely used 'GSM8K' math benchmark and in doing so shows that most LLMs may have data contamination - if you slightly vary some aspects of a widely used math test, their performance drops significantly. "We show that the performance of all models drops on GSM-Symbolic, hinting at potential data contamination," Apple writes. "We further question the reasoning abilities of LLMs and introduce the GSM-NoOp dataset. By adding seemingly relevant but ultimately irrelevant information to problems, we demonstrate substantial performance drops (up to 65%) across all state-of-the-art models".  
  
**What they did - GSM Symbolic and GSM NoOp:** Apple introduces two tests; GSM Symbolic subtly varies GSM8K, while GSM NoOp introduces distracting variables on top.   
**GSM8K versus GSM Symbolic:** GSM Symbolic takes questions from GSM8K and turns them into madlib-style templates where key details are turned into variables (e.g., in GSM8K where a question says "When Sophie watches her nephew" the GSM Symbolic version says "When {name} watchers her {family}", and in GSM8K when a question says "After buying the tube of balls, Sophie has 31+8+9 + T = 48" the GSM Symbolic version says "After buying the tube of balls, {name} has {x} + {y} + {z} + T = {total}".)  
**Results - huge variance on smaller models:** Apple tests a bunch of models and the results show huge variance, with relatively small open source models like Mistral-7b and Gemma2-2b doing far worse on GSM Symbolic than on GSM8K, though there's significantly less variance on large-scale proprietary models like GPT-4o and 01-mini. On NoOp, the same pattern shows up, with smaller (and mostly open source) models doing very badly, and large-scale proprietary models like OpenAI's new reasoning-filled "o1-preview" model suffering the least severe performance degradation.  
  
**What does it all mean? Overfitting happens, but big models are less prone to it:** While critics of LLMs will use this paper to point out that LLMs are often overfitting and not really 'reasoning' but rather memorizing stuff, I think it actually shows something more subtle: small and therefore relatively dumb models do absolutely overfit, but the larger and smarter your model, the less prone it is to overfitting. Yes, there's still some degradation, suggesting that large models have soaked up some biases from their training sets which degrade performance, but the fact they cope far better is actually - to me - a very optimistic sign, indicating that the world's largest and most sophisticated models may really exhibit some crude reasoning - at least, enough to get over deliberately confounding benchmarks!  
**Read more:**[GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models (arXiv)](https://arxiv.org/abs/2410.05229).  
  
***  
  
 **The 10bn+ parameter distributed training run has arrived:  
**_…Prime Intellect is trying to do something that, if successful, will change the contours of AI policy…  
_ AI startup Prime Intellect has launched INTELLECT-1, a decentralized training run of a 10-billion parameter model. If successful, this will be the largest decentralized training run of a frontier language model - that's a big deal, because it will show that loosely federated collectives might be able to pool their computers to train models that challenge those of single companies.   
  
**What INTELLECT-1 relies on:** The training run uses OpenDiLoCo ([Import AI #381](https://importai.substack.com/p/import-ai-381-chips-for-peace-facebook)), Prime Intellect's open source implementation of DeepMind's 'DiLoCo' technique ([Import AI #349](https://jack-clark.net/2023/11/20/import-ai-349-distributed-training-breaks-ai-policy-turning-gpt4-bad-for-245-better-weather-forecasting-through-ai/)). Prime Intellect already used this technique to train a 1bn parameter model and is now scaling it up to a 10B one. "Our goal is to solve decentralized training step-by-step to ensure AGI will be open-source, transparent, and accessible, preventing control by a few centralized entities and accelerate human progress," the company writes.   
**How it works:** There are a few new inventions to further improve the efficiency of the distributed training process. These include: ElasticDeviceMesh, software for automatically scaling up and down the groups of computers used for distinct parts of the AI training; asynchronous distributed checkpointing, an asynchronous way to save state during the runs; live checkpoint recovery, to make it easy to grab the latest state of the run for new computers that want to join the run; custom Int8 All-Reduce kernel; a kernel optimized for the types of quantization and dequantization used, and more.   
**What it's being trained on:** INTELLECT-1 is training now on the Fineweb-Edu dataset from HuggingFace (55% of the training mix), along with DLCM (20%), Stackv2 (20%), and OpenWebMath (5%).  
  
**Who makes the future?** There's a [leaderboard](https://app.primeintellect.ai/intelligence?_gl=1*i7yjru*_gcl_au*ODUyNzU5OTk0LjE3Mjg2OTM3NDA.) where you can see who is putting forward the compute to train this model - beyond individuals, other companies include SemiAnalysis, HuggingFace, and Arcee AI.   
  
**Why this matters - centralization versus decentralization, aka the political economy of AI rests on distributed training:** If distributed training works well, it changes the policy landscape of AI development. Today, much of AI policy rests on the load-bearing assumption you can control the frontier by monitoring and controlling large blobs of centralized computers. Decentralized training breaks this - the frontier can now be made of hundreds of different blobs of compute, working together. This also bears on export controls which deny people the ability to build high-performing, centralized blobs of compute - again, decentralized training makes it easier to pool resources of n-1 generation accelerators and use this to compose an (economically suboptimal) frontier training run.   
Of course, Prime Intellect has some way to go - frontier training runs are 500bn+ parameters now (e.g, Facebook's LLaMa3 biggest model is 405bn parameters), so whether it scales to this regime matters. But just a few months ago the largest decentralized training runs were of the order of 1bn, so 500bn is a big difference already!  
**Read more:** [INTELLECT–1: Launching the First Decentralized Training of a 10B Parameter Model (Prime Intellect blog)](https://www.primeintellect.ai/blog/intellect-1).  
  
*****  
  
Facebook prepares for the fully personal video model future:  
**_…Announces Movie Gen models, trained on ~6,000 H100s…  
_ Facebook has built Movie Gen, a set of generative models that can be used to generate and edit movies. These models can be used to generate videos from text, edit videos with text, and produce personalized videos (e.g you upload a photo of yourself and it shapes the video around you).   
  
**Compute:** These are relatively expensive models - Facebook trained the Movie Gen family on "up to 6,144 H100 GPUs, each running at 700W TDP and with 80GB HBM3, using Meta’s Grand Teton AI server platform".  
  
**No release:** Facebook isn't releasing these models - "the Movie Gen cast of foundation models were developed for research purposes and need multiple improvements before deploying them," Facebook writes.   
  
**Why even cover this? Video is about to be a commodity:** Just as text generation and image generation have become 'commodity AI' services (where though proprietary models exist, you can relatively easily access extremely cheap and or open weights variants), video models seem to be heading in this direction. Facebook also seems like one of the most likely players to openly proliferate such models, so it's worth taking note of Movie Gen to get a sense of what might be broadly distributed on the internet in a while.  
**Find out more at the official site:** [Meta Movie Gen (Meta)](https://ai.meta.com/research/movie-gen/).  
**Read more in the research paper** : [Movie Gen: A Cast of Media Foundation Models (Facebook, PDF)](https://ai.meta.com/static-resource/movie-gen-research-paper).  
  
***  
  
 **Intelligence piled high  
** _[Many years after uplift, fragment stored in offworld 'wikiasteroid']  
  
_ We have as many words for intelligence as some groups of humans had for snow. In the space of all possible minds there is so much variety that a new vocabulary is needed. The words we use also have power - we navigate ourselves to and through these different spaces of minds through language, so our ability to describe intelligence is equivalent to our ability to channel it. Much of our work is spent in this exploration - this characterization of the many textures and constraints and specialisms that make up a mind. We are all smart, of course - smarter than any thing that has ever lived in any of our recorded history. But we nonetheless encounter problems that pose challenges to us. There is a kind of sport in this - we shapeshift according to our language and our language changes according to how much of our possibilities we have explored.   
  
**Things that inspired this story:** The notion that having different 'lenses' on problems is key to solving them; natural ecologies; the idea that even among machines there will be competition and specialization.

_Thanks for reading!_
