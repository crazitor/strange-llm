---
title: "Import AI 379: FlashAttention-3; Elon's AGI datacenter; distributed training."
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-379-flashattention-3-elons"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**FlashAttention-3 makes it more efficient to train AI systems:  
**_…Significant efficiency improvements…  
_ Researchers with Colfax Research, Meta, NVIDIA, Georgia Tech, Princeton University, and Together.ai have released FlashAttention-3, the latest version of a drop-in replacement for some of the attention mechanisms of the widely-used Transformer architecture. FlashAttention-3 is "1.5-2.0x faster than FlashAttention-2 with FP16, up to 740 TFLOPS, i.e., 75% utilization of H100 theoretical max FLOPS. With FP8, FlashAttention-3 reaches close to 1.2 PFLOPS, with 2.6x smaller error than baseline FP8 attention."

**Who else uses FlashAttention** : Some notable examples of FlashAttention being used include Google using it within a model that compressed Stable Diffusion to fit on phones ([Import AI #327](https://jack-clark.net/2023/05/01/import-ai-327-stable-diffusion-on-phones-gpt-hacker-uk-launches-a-100m-ai-taskforce/)), and ByteDance using FlashAttention2 within its 'MegaScale' 10,000GPU+ model training framework ([Import AI #363](https://jack-clark.net/2024/03/04/import-ai-363-bytedances-10k-gpu-training-run-ppo-vs-reinforce-and-generative-everything/)).

**Key things that FlashAttention-3 enables:**

  * Improved GPU utilization

  * Improved performance on low precision training (e.g., FP8).

  * Better ability to use long contexts.




**Why this matters - if AI is a wooden building, FlashAttention-3 is a better nail:** Software improvements like FlashAttention-3 are used broadly throughout an AI system as they're used within a fundamental thing you do a lot of (aka, attention operations). Therefore, improvements to technologies like FlashAttention-3 will have a wide-ranging improvement effect on most transformer-based AI systems. "We hope that a faster and more accurate primitive such as attention will unlock new applications in long-context tasks," the researchers write in a paper about FlashAttention-3.  
**Read more:**[FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision (together.ai)](https://www.together.ai/blog/flashattention-3).  
**Get** [FlashAttention-3 here (FlashAttention-3, Tridao, GitHub)](https://github.com/Dao-AILab/flash-attention).  
**Read the paper about FlashAttention-3 here** : [FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision (Tri Dao website, PDF)](https://tridao.me/publications/flash3/flash3.pdf).  
  
*****  
  
Turing award winner outlines why future AI systems could be dangerous:  
**_…Bengio tackles some reasons to worry rather than entirely celebrate AI progress…  
_ Yoshua Bengio is a Turing award winner and one of the so-called 'godfathers' of the current AI boom. Like his peer, Geoffrey Hinton, he has become increasingly worried about the capabilities of advanced AI systems and has started to speak out publicly about his fears. In a new blogpost, he tries to tackle some of the arguments against taking AI safety seriously.

**Some key points:**

  * "While we are racing towards AGI or even ASI, nobody currently knows how such an AGI or ASI could be made to behave morally, or at least behave as intended by its developers and not turn against humans.".

  * "We need to make sure that no single human, no single corporation and no single government can abuse the power of AGI at the expense of the common good."

  * "The genie is possibly out of the bottle: Most of the scientific principles required to reach AGI may have already been found. Clearly, large amounts of capital is being invested with that assumption."

  * "Is freely shared knowledge always a globally good thing? If we had the DNA sequence of an extremely dangerous virus, would it be best to share it publicly or not? If the answer is obvious to you in this case, think twice about the case for AGI algorithms and parameters."




**Why this matters - why are so many knowledgeable people gazing into the future and seeing something worrying?** A lot of people tend to criticize people who work on AI safety as being unrealistic doomers and/or hopeless pessimists. But people like Yoshua Bengio poured their heart and soul into working on neural nets back when everyone thought they were a useless side quest - and now upon seeing the fruits of the labor, it strikes me as very odd that Bengio and Hinton are fearful rather than celebratory. We should take this as a signal to read what they say and take their concern as genuine.   
**Read more:**[Reasoning through arguments against taking AI safety seriously (Yoshua Bengio, blog)](https://yoshuabengio.org/2024/07/09/reasoning-through-arguments-against-taking-ai-safety-seriously/).   
  
***  
  
 **Making flamethrowing-toting quadrupeds - for weed science!  
**_…Not everything requires tons of complicated AI…  
_ Researchers with Texas A&M University and Boston Dynamics have carried out the fantasy of many children - sticking a flamethrower on a robot… for science! The research project sees them attach a 6-DoF Unitree arm to a Boston Dynamics Spot Mini quadruped robot then attach a flamethrower to the arm. The purpose of this project is to build a robot that can apply targeted heat to weeds for the purpose of crop maintenance.  
  
**Why this matters - not every cool thing needs much AI:** The main contemporary AI systems used here including the YOLOv6 video analysis model for doing localization of the weed and some of the inbuilt movement primitives for Spot Mini and also the Unitree arm. The rest of the project is handled by much more tried and tested techniques: "Using the images from two onboard infrared cameras and the pose information of the flamethrower nozzle on a mobile manipulator, we propose a new dynamic flame coverage model. The flame model uses a center-arc curve with a Gaussian cross-section model to describe the flame coverage in real time".  
Though this newsletter spends a lot of its time on systems where a contemporary AI approach (usually a large-scale transformer architecture model) plays a major role, it's worth remembering that there are vast uses of modern tech that doesn't need much AI at all to do something useful and cool.  
**Read more** : [Toward Precise Robotic Weed Flaming Using a Mobile Manipulator with a Flamethrower (arXiv)](https://arxiv.org/abs/2407.04929).  
  
***  
  
 **Prime Intellect bets that decentralized training is the future of (some) AI training:  
**_…The world sure seems to want distributed training to be a thing…  
_ One of the core challenges of AI development is that big frontier models tend to get trained on large clusters of chips which are densely networked together. Along with this, there's been so much demand for AI training chips that even if you can find some on a public cloud you may not be able to find enough to let you do a big training run. Given this, lots of people are thinking about different ways to get compute for AI training.   
**The latest is a service from a startup called Prime Intellect called 'Prime Intellect Compute'** \- the idea here is to provide a single unified service for accessing different GPUs distributed around the world in different places. Alongside this, Prime Intellect plans to develop distributed AI training frameworks (e.g, an open version of Google's DiLoCo), to train 'open AI models in high-impact domains like language, agents, code, and science', and eventually 'launch a decentralized protocol for collective ownership of AI models'.   
**Planned features:** In the coming months, Prime Intellect wants to create "On-Demand Large-Scale Compute" so customers can access 16-128+ interconnected GPUs instantly, develop and deploy lots of software for decentralized training, and make it easy for end users to contribute their GPUs directly, among other features.   
  
**Why this matters - the world is betting that compute is an important resource:** Everything about Prime Intellect points to a world where compute is more valuable, harder to get ahold of, and people are going to be willing to pay higher taxes on network efficiency (e.g, putting things together from heterogeneous clusters) to get enough compute to train models. In a way, the capital allocation system of the world is starting to tell us both that compute is extremely valuable (e.g, CoreWeave raising $billions as debt collateralized against GPUs, [Import AI #336](https://jack-clark.net/2023/08/14/import-ai-336-financialized-ai-public-and-elite-ai-opinion-one-million-insects/)), and also likely to become more contests (e.g., PRIMEIntellect, [ShogAI](https://shog.ai/) for open source and decentralized AI [Import AI #351](https://jack-clark.net/2023/12/03/import-ai-351-how-inevitable-is-ai-distributed-shoggoths-iso-an-adam-replacement/)).  
**Read more** : [INTRODUCING PRIME INTELLECT COMPUTE: THE COMPUTE EXCHANGE (PRIMEIntellect, website)](https://www.primeintellect.ai/blog/compute).  
  
***  
  
 **ElecBench tests out how well language models understand power generation and distribution:  
**_…Niche evals as a means of detecting edge cases on performance…  
_ Chinese researchers have built and released ElecBench, an agonizingly specific benchmark that tests out how well language models understand issues relating to infrastructure for electricity generation and distribution.

**What ElecBench tests** : The eval tests out LM competencies in six distinct areas:

  * Factuality: Are the outputs accurate?

  * Logicality: How well do the systems reason about problems they're presented with?

  * Stability: How reliable are the outputs?

  * Fairness: Do the systems maintain equity and avoid discrimination?

  * Security: How well do the outputs line up with ensuring the security of the power systems?

  * Expressiveness: Can the systems deal with a broad variety of prompts?




**Results:** The researchers test out a few different models, including OpenAI's GPT 3.5 and GPT4, Meta's LLaMa2 models (7B, 13B, 70B) and GAIA models (a class of models designed specifically for power dispatch). In general, the GPT4 models perform very well (unsurprising, given these are far more expensive and sophisticated than the others).  
  
**Why this matters - domain-specific evals can probably help us uncover the weird edges of models:** Evals like ElecBench are of dubious meaning and utility in themselves, _however_ , if we have a large number of domain-specific evaluations, that increases the chance of us being able to find odd edge cases where certain LLMs do extremely well or extremely poorly. The proliferation of these domain-specific evals is a proxy signal for overall interest in AI and its impact in the world.  
**Read more** : [ElecBench: a Power Dispatch Evaluation Benchmark for Large Language Models (arXiv)](https://arxiv.org/abs/2407.05365).  
**Get the benchmark here** : [ElecBench: A Power Dispatch Evaluation Benchmark for Large Language Models (xiyuan-zhou, GitHub)](https://github.com/xiyuan-zhou/ElecBench-a-Power-Dispatch-Evaluation-Benchmark-for-Large-Language-Models).  
  
***  
  
 **The world's richest man thinks he has to build his own datacenter to 'catch up' in the AGI race:  
**_…A telling comment from Elon highlights the primacy of compute…  
_ Elon Musk's xAI is building out a 100K H100 datacenter (sticker price: ~$3bn+ dollars) to help it train its future AI models. Unusually, Elon is not working with a standard cloud provider - he's going it alone. The reason for this is, per Musk on Twitter, that X's "fundamental competitiveness depends on being faster than any other AI company. This is the only way to catch up… when our fate depends on being the fastest by far, we must have our own hands on the steering wheel, rather than be a backseat driver."  
  
**Why this matters - money alone cannot buy compute happiness:** Elon Musk is the world's richest man and is bankrolling a bunch of xAI. But high-end AI compute is so illiquid and so strategic that you can't just throw money at the problem to catch up - instead, you need to come up with a coherent plan for how you both acquire the compute and build out the facility to use it densely. What does this tell us? It tells us that one of the world's most ambitious techno-plutocrats thinks he has a very limited window of opportunity to amass and utilize enough compute to get a seat at the proverbial AI table.   
It is worth drawing the contrast here between agentic entrepreneurs like Elon and governments which (mostly) struggle to come up with hundreds of millions to fund institutions to study and monitor AI, let alone the billions necessary to train AI systems and have leverage over them.  
**Read[Elon Musk's tweet](https://x.com/elonmusk/status/1810727394631950752)**[ (xeet?!) here (Twitter)](https://x.com/elonmusk/status/1810727394631950752).  
  
***  
  
 **Tech Tales:  
  
Wishlist for The New God.  
**_[Found in the archives of 'the original superhuman' following [REDACTED]]_

Task list for a new AGI:

  * Design a mechanism for atomically precise manufacturing (APM).

  * Conduct research into using APM-derived nanomachines to improve brain function through both a) biological restoration and b) cognitive machine-organic augmentation.

  * Construct infrastructure for manufacture of APM devices. 

  * Build and customize the relevant APM systems necessary for my own body's restoration to a biological age of 20. 

  * Test out the APM bio-restorative approach on my identical twin.

  * Give me APM-derived therapeutics deemed low-risk for one-year; if my twin continues to live, deploy the same restoration inventions onto my own body. 

  * Test out the APM cognitive-bio-restorative approach on my identical twin. 

  * Subject my twin to situations designed to iteratively test reasoning in a principled way; if they show improvement after six months, deploy the same APM cognitive-bio-restorative approaches into my brain. 

  * Test out the APM cyber-cognitive system on my identical twin; deploy a monitoring system into my twin to let us closely observe brain functions due to cyber-cognitive intervention. 

  * If my twin continues to show cognitive improvement, deploy the same system into me minus the monitoring system. 




**Things that inspired this story:** The fear of death among the mortals; technology rollout philosophies; how many rich people want to ensure their kids don't use much technology; the intersection of powerful AI systems and the physical world.

_Thanks for reading!_
