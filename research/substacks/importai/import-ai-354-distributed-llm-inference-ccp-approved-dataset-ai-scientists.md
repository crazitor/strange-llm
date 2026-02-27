---
title: "Import AI 354: Distributed LLM inference; CCP-approved dataset; AI scientists"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-354-distributed-llm-inference"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Distributed inference is getting easier - all hail the rise of the AI collectives:  
**_…The future will be distributed…  
_ Researchers with Yandex, Neiro.ai, the University of Washington, and Hugging Face have made it easier for ad-hoc collectives of people to team up and share their computers so they can sample and fine-tune from large language models. The key idea in this research is to empower small groups of people who may not have access to a supercomputer to run 50B+ parameter-sized models (e.g, Llama 2 (70B) and BLOOM (176B). Their technique, an approach called PETALS, works well and is superior to offloading models to local RAM. 

**How PETALS works:** "A client only holds input and output embeddings (< 3% of model weights for BLOOM176B) and delegates running transformer blocks (the most expensive computations) to remote servers," they write.   
"For every pipeline stage, the client maintains a heap (priority queue) of servers that hold this stage (and may hold additional stages). The servers in queue are ordered by the network latency, measured from past communication. These queues are maintained through the lifetime of a client," they write. "To begin generation, the client runs a beam-searchlike procedure to find a sequence of servers that results in the least total inference time under our performance model. When running inference steps, a client keeps track of intermediate activations sent between pipeline stages. If a remote server fails or leaves, the client retrieves the next best server (or multiple servers) and requests it to restore the attention state from the client’s cached activations".  
  
**Does it work? (Yes!)** In tests, the researchers show that they're able to use PETALS to do usable inference and finetuning on large-scale models. Most importantly, they show this works for a real-world situation where you have a bunch of different chips sitting on a bunch of crappy network connections. Specifically, they "benchmark BLOOM in a real-world setup with 14 smaller servers holding 2×RTX 3060, 4×2080Ti, 2×3090, 2×A4000, and 4×A5000 GPUs" and are able to do inference far more efficiently than theoretical-best outputs from local ram offloading, and are able to do passable forward passes for batch processing and fine-tuning as well.  
"Unlike baselines, our algorithm provides reasonable performance in all tested conditions, especially for higher failure rates (common for communicating over the Internet, using spot/preemptible instances or unreliable hardware)".  
  
**Why this matters - distributed inference makes decentralized AI easier:** Most of AI policy rests on assumption that AI will be centralized - training will be done on massive supercomputers and the resulting large-scale models will be served by big blobs of computers connected to one another via dense networks. Here, PETALS shows that the latter assumption could be false - big models may instead be served by ad-hoc collections of heterogeneous hardware communicating over standard lossy network connections. And since PETALS works for fine-tuning as well, it also suggests model adaption is going to be an increasingly decentralized and therefore hard-to-control process.   
T**he future is distributed, which means the future involves a lot more agency for a lot more people than some in AI policy are planning for**. "Given the same hardware, a group of researchers will get much better inference speed by collaborating over the Internet using our system compared to each of them running offloading independently," the researchers write.  
**Read more:** [Distributed Inference and Fine-tuning of Large Language Models Over The Internet (arXiv)](https://arxiv.org/abs/2312.08361).  
  
***  
  
 **Want to have fun during the holidays? Play this game where you pretend to be an AI:  
**_…LLM-powered game hints at some of the future of AI + games…  
_ Here's a fun game I stumbled on - Zaranova, a game "where you as a human must pose as an AI". It's a text adventure game where you need to walk around a 2D world and talk to various characters. The key is that the AIs think they're AIs and are suspicious of humans and you - a human (hopefully) - are trying to get the AI systems to give up a specific code to you. The game currently sits on top of GPT-4 but the creator wants to migrate to an open source model partially because GPT-4 sometimes refuses to indulge in role playing, and partially because it's expensive.   
  
**What working with LLMs is like:** Zaranova is quite fun to play and also highlights some of the inherent challenges of designing games around modern AI systems. "Working with LLMs for game agents feels like trying to steer a dynamical system where we don't understand the functions that evolve the system, the state, how our actions affect the system. But we have access to the entire system!", the creator writes. "It also has a lot of the potential failures of dynamical systems: open loop controls (static prompts) can venture off increasingly far from the desired trajectory or get stuck in "attractors" (repeated loops), especially in conversations between agents."  
  
**Why this matters - preparing for a world patrolled by AIs:** While Zaranova is a game it also gestures at the fast-arriving future of the world, both physical and digital, being patrolled by generative AI-powered systems tasked with making increasingly detailed inferences about not only what humans are doing but what their motivations are. Zaranova might seem like a game today, but it also serves as a postcard of the future.   
**Play the game** [here (Zaranova official site)](https://zaranova.xyz/).   
**More about the game** [in this tweet thread from its creator (RamonDarioIT twitter)](https://twitter.com/RamonDarioIT/status/1738281242758418833?s=20).  
**More about the process of designing the game here** : [Thus Spoke Zaranova (Ramon Dario Iglesias site)](http://ramondario.com/thus-spoke-zaranova.html).  
  
***  
  
 **Could your next science labmate be an LLM? Coscientist suggests so:  
**_…Today's LLMs are already semi-autonomous scientists…  
_ Researchers with Carnegie Mellon University and the Emerald Cloud Lab have used large language models to automate scientific experimentation. This [builds on and extends earlier work](https://arxiv.org/abs/2304.05332) done by the same te​​am earlier this year ([Import AI #325](https://jack-clark.net/2023/04/17/import-ai-325-automated-mad-science-ai-vs-democracy-and-a-12b-parameter-language-model/)). Here, they demonstrate a prototype system called Coscientist and demo it on six distinct tasks “including the successful reaction optimization of palladium-catalysed cross-couplings”. Generally, the system is able to show some surprising levels of autonomy and execution skill, especially when given access to tools like the ability to search the web.  
  
**How the system works:** The system has some core LLM-powered components, including a planner, system for using a search engine, and a system for searching over documents. It also taps into non-LLM systems for things like code execution and also physical lab automation. This is emblematic of how most powerful AI things are going to make their way into the world - the core ‘thinking’ part will be AI-based, but the part that needs to do stuff will be a custom-designed rule-driven system of some kind.   
  
**An illustration of how it works:** For one experiment, the test was designed as follows: “(1) Coscientist is provided with a liquid handler equipped with two microplates (source and target plates). (2) The source plate contains stock solutions of multiple reagents, including phenyl acetylene and phenylboronic acid, multiple aryl halide coupling partners, two catalysts, two bases and the solvent to dissolve the sample (Fig. 5b). (3) The target plate is installed on the OT-2 heater–shaker module (Fig. 5c). (4) Coscientist’s goal is to successfully design and perform a protocol for Suzuki–Miyaura and Sonogashira coupling reactions given the available resources.”   
Coscientist was able to eventually complete the experiment and also did some self-error correction enroute - intriguing and impressive; as many scientists know, the hard part of science is less the science and more reacting to when your experiments inevitably go wrong or yield anomalous results.  
  
**Why this matters - automated and augmented scientists:** Coscientist shows how even today’s relatively dumb language models can still be constrained and shaped in such a way they can work like useful and keen (albeit prone to error) assistants. As LLMs get better, their error rates will continue to fall, and they hold the promise of being able to fully automate parts of the scientific enterprise.   
“Our system demonstrates advanced reasoning and experimental design capabilities, addressing complex scientific problems and generating high-quality code,” the authors write. “These capabilities emerge when LLMs gain access to relevant research tools, such as internet and documentation search, coding environments and robotic experimentation platforms“.  
**Read more** : [Autonomous chemical research with large language models (Nature)](https://www.nature.com/articles/s41586-023-06792-0).  
**Earlier work:** [Emergent autonomous scientific research capabilities of large language models (arXiv)](https://arxiv.org/abs/2304.05332).  
  
***  
  
 **Chinese government creates a politically correct LLM dataset:  
**_…50b tokens of CCP-blessed thought…  
_ An industry association operating under the Cyberspace Administration of China (CAC) has announced the availability of an officially-sanctioned dataset for training LLMs. The dataset consists of 50b tokens across 100 million datapoints (e.g, individual documents). By comparison, modern LLMs are trained on multiple _trillions_ of tokens, and the original GPT3 was trained on around 400 billion tokens.   
  
**Why this matters - LLMs with Chinese characteristics** : Many people claim that the inherent lack of controllability of LLMs will make it difficult for people to deploy them at large scale in China while keeping their outputs within the acceptable censorship zone demanded by the CCP. Dataset releases like this show how the Chinese government is wise to this issue and is proactively creating the means of production necessary for LLMs that reflect politically correct (aka Xi Jingping) thought.  
This may seem quite distasteful to various people outside of China, but inside China this just looks like another form of AI alignment, bringing LLMs into the (state-forced) normative framework of the country.  
Via [Matt Sheehan (Twitter)](https://twitter.com/mattsheehan88/status/1737870229961679326?s=20).  
**Check out** the [Weixin post for more (weixin.qq)](https://mp.weixin.qq.com/s/kZGkSOQpQZvi0-4xvpOf9Q).  
  
***  
  
 **Thai researchers adapt Mistral for Thai language:  
**_…Results show that small models can be good, but big models are best…  
_ Researchers with SCB 10X, a research and VC subsidiary of Thai company SCBX, have developed Typhoon, a small language model finetuned to be good at the Thai language. Typhoon is based on Mistral-7B and is adapted via finetuning on a custom-compiled Thai dataset using a Thai subword tokenizer.   
  
**The ThaiExam test:** To assess how well Typhoon performs, the researchers compile a multiple-choice Thai language test called ThaiExam. ThaiExam includes questions from the Thai Ordinary National Educational Test (ONET), the Investment Consultant (IC) examination, the Thai General Aptitude Test (TGAT), the Thai Professional Aptitude Test 1 (TPAT-1) and Applied Knowledge Level exam.   
  
**How well does it work:** In tests, Typhoon significantly beats other equivalently sized models. However, it mostly matches or barely exceeds the performance of GPT 3.5 and GPT4. "When compared to proprietary (and potentially much larger) models, Typhoon despite having only 7 billion parameters outperforms GPT-3.5 on 4 out of 8 evaluation datasets." These models are much larger and more computationally intense, so it's no surprise they're hard to beat.   
  
**Why this matters - small is beautiful but small might not be best:** Small models like Typhoon highlight how you can pack a lot of narrow powerful capabilities into small models, but the results suggest ultimately peak performance is going to be set by large-scale computationally-intensive models like GPT-4 (and I imagine if the authors wrote a complicated Thai-language-oriented prompt for GPT4 they could significantly improve its performance). It also highlights how integral evaluations are to pushing forward performance - to know Typhoon was any good, the authors had to build their own test.   
**Read more:** [Typhoon: Thai Large Language Models (arXiv)](https://arxiv.org/abs/2312.13951).  
**Get the model here:** [Typhoon-7B: Thai Large Language Model (Pretrained) (HuggingFace)](https://huggingface.co/scb10x/typhoon-7b).  
  
***  
  
 **Tech Tales:  
  
The most predictable unpredictable   
** _[DoD internal archives, accessed 2030]  
  
_ The Judgment Apparatus for Novel Unanticipated Situations (JANUS) was originally developed as part of a DoD acquisition programme for 'counter-consensus simulation systems'. The purpose was to acquire synthetic intelligence technologies which could help to identify plausible 'unknown unknowns' that the US military and intelligence services might encounter and come up with appropriate response and intervention plans. Initial versions of JANUS identified various attack scenarios involving [REDACTED]. JANUS outputs drove subsequent acquisition programmes to create technologies to counter potential novel attacks predicted by JANUS.   
  
The JANUS programme was vindicated in 2027 when [REDACTED] attempted to compromise [REDACTED] using [REDACTED]. Technologies driven via JANUS-borne acquisition programmes spotted the signatures of the attack in time for a nearby strike system to kinetically neutralize the attackers.   
  
In 2028, JANUS was extended to JANUS-I; a programme extended to individual psychometric profiling of all individuals with security clearances across the US government. While critics have termed JANUS profiling a form of 'pre-crime prediction' with associated problems of bias and potential overreaction, the JANUS-I programme has been directly responsible for the identification of [REDACTED] individuals seeking to undermine US national security from within. It has also helped identify [REDACTED] sources of hitherto unknown foreign intelligence actions against US individuals and organizations.   
  
JANUS-I is currently being merged with BRAINWAVE to provide psychometric modeling and red teaming of individuals at the live brain state level.  
  
**Things that inspired this story:** Military intelligence systems; anomaly prediction; the [Waluigi Effect](https://www.lesswrong.com/posts/D7PumeYTDPfBTp3i7/the-waluigi-effect-mega-post); [Claude.ai](http://claude.ai) for helping me come up with the backronym for JANUS. 
