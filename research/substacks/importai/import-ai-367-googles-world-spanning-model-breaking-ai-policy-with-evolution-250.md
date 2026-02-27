---
title: "Import AI 367: Google's world-spanning model; breaking AI policy with evolution; $250k for alignment benchmarks"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-367-googles-world-spanning"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Google plans a world-spanning AI system - and the path to it is through breaking AI policy:  
**_…Distributed PAth COmposition (DiPaCo) is a clever idea with big implications…  
_ Google has published DIstributed PAth COmposition (DiPaCo), a technique for scaling up the size of neural nets across geographically distributed blobs of computation. "Our approach facilitates training across poorly connected and heterogeneous workers, with a design that ensures robustness to worker failures and preemptions," the researchers write. They train a prototype model using this approach which approximates the performance of a model trained in a typical way. 

**How DiPaCo works** : "The core idea of DiPaCo is to train a sparsely activated modular system where data and computation are distributed by the choice of path through the modules," they write. This idea has two key dependencies:

  1. Coarse Routing: In the same way mixture-of-experts only fire up a fraction of the total parameters in a neural net at one time, picking the best 'expert' on a per token (or set of token) basis, DiPaCo does this on a per-document basis. "Routing once per document allows batching computation across all tokens of a sequence, without the need to swap modules in and out as a sequence is processed. This in turn allows parameters to be distributed across distant workers".

  2. DiLoCo: They use an earlier Google paper, DiLoCo ([#Import AI 349](https://jack-clark.net/2023/11/20/import-ai-349-distributed-training-breaks-ai-policy-turning-gpt4-bad-for-245-better-weather-forecasting-through-ai/)) to distribute the shared training of modules over different blobs of compute. "With these two choices, neither at training nor at test time does the entire network (collection of paths) need to be materialized together".




**Does it work? Yes, at small scale** : "We demonstrate the feasibility of DiPaCo by training a language model on the C4 dataset with paths of size 150 million parameters, matching the performance in terms of validation perplexity of a 1.3 billion model, but with 45% less wall clock training time," they write. "While the dense 1.3B system required the use of all co-located devices, DiPaCo uses 256 islands of compute, each of which is one-eighth the number of devices used to train the baseline."  
  
**What does all of this have to do with the destruction of AI policy?** A lot of contemporary AI policy depends on the idea that AI models are single entities that live in one big data center and that these data centers are themselves controllable because there aren't many of them. Therefore, lots of policy targets these big blobs of compute and associated models trained on them (e.g, the Biden administration wants to know about models which use more than 10^26 FLOPs in training as well as clusters capable of training dense models with this amount of compute).   
You know what breaks this policy approach? Really effective distributed training, where you train models in multiple small blobs of compute.   
You know what DiPaCo is? It's an ambitious vision for a future where Google trains some really massive world-spanning models _via_ distributed training techniques.   
In a counterintuitive way, Google's path to training far larger AI systems than can be accommodate in today's data centers requires Google to develop the necessary distributed training (and eventually, inference) techniques which will inherently break AI policy that focuses on centralized compute controls.   
"Our long-term dream is to further refine this approach and produce a never-ending, community-driven, modular learning system that can be used by everyone to compose new predictors out of existing modules, and thus efficiently develop entirely new models and capabilities in a positive feedback loop," Google writes.   
**Read more:** [DiPaCo: Distributed Path Composition (arXiv)](https://arxiv.org/abs/2403.10616v1).  
  
*****  
  
What does 10^25 versus 10^26 mean?  
**In the United States, the recent Biden Executive Order on AI says that general-purpose systems trained with 10^26 FLOPs (or ones predominantly trained on biological sequence data and using a quantity of computing power greater than 10^23) fall under a new reporting requirement that means companies will let the US government know about these systems. By comparison, in Europe, the recent EU AI Act says that general-purpose systems trained with 10^25 FLOPs have the potential for “systemic risk” and therefore companies developing them need to report details about the AI systems to the EU government.  
I recently did some napkin math to figure out the difference between these regulations in terms of dollar costs and the result is that 10^25 = $7m and 10^26 = $70m. These are important and consequential differences.   
**Read more:**[What does 10^25 versus 10^26 mean? (jack-clark.net)](http://jack-clark.net)**.  
  
***  
  
OpenAI and Microsoft plan a $100 billion supercomputer:  
**_…The mother of all CapEx intensive technologies…  
_ As part of the broader industrialization of AI, a select few companies are planning some really big training runs. How big? Well, here's a report from The Information that says Microsoft and OpenAI are together planning to build a supercomputer named Stargate that'll cost about $100bn and use multiple gigawatts of electricity.   
  
**Why this matters - AI policy will eventually be industrial policy:** At this level of capital expenditure, AI is going to look more like a vast CapEx intensive industry like oil extraction, mining, heavy industry, and so on. These industries all end up being heavily regulated, having a tiny number of participants, and also become intertwined with the industrial policy of governments. It's worth bearing this in mind when we look at things like openly accessible models being released that cost $10m to train (see: Databricks). Is anyone going to openly release a model that costs $100 billion? $10 billion? $1 billion? All seems doubtful to me!   
**Read more:** [Microsoft and OpenAi Plot $100 Billion Stargate AI Supercomputer (The Information)](https://www.theinformation.com/articles/microsoft-and-openai-plot-100-billion-stargate-ai-supercomputer?rc=dfnif8).  
  
*****  
  
Databricks spends $10 million to build a prior generation LLM:  
**_…DBRX shows the delta between openly accessible models and proprietary models is about one and a half years:  
_ Databricks has built and released DBRX, a language model which roughly approximates the performance of OpenAI's GPT 3.5, and beats popular openly accessible models like LLaMa2 and Mixtral. DBRX is a mixture-of-experts model that is about 132 billion parameters in size (though only uses 36 billion parameters at any given time).  
  
**The gulf between openly accessible models and proprietary models is about 1.5 years:** DBRX roughly approximates (and in a few cases, beats) OpenAI's GPT 3.5, a model which OpenAI released (as text-davinci-003) back in ~November 2022. Per Wired, DBRX cost about $10 million to train (two months on ~3,072 Nvidia H100 GPUs), according to a Wired story about the model.   
  
**Why this matters - a tale of two ecosystems:** There's increasingly a divergence between the open ecosystem of AI models that are widely released and the closed ecosystem - while DataBricks is putting all of its effort (and $10m) into training a model that approximates an old proprietary model, companies like Amazon are already dumping close to $100m into individual training runs ([Import AI #365](https://importai.substack.com/p/import-ai-365-wmd-benchmark-amazon)) and are looking at $1bn training runs on the horizon. This means when we think about the AI frontier we should think of it as two frontiers - a closed and very powerful frontier, and an 'open' frontier that costs perhaps an order of magnitude less to be on.  
**Read more:** [Announcing DBRX: A new standard for efficient open source LLMs (Databricks blog)](https://www.databricks.com/blog/announcing-dbrx-new-standard-efficient-open-source-customizable-llms).  
**Check out the Wired story** : [Inside the Creation of the World’s Most Powerful Open Source AI Model (Wired)](https://www.wired.com/story/dbrx-inside-the-creation-of-the-worlds-most-powerful-open-source-ai-model/).  
  
***  
  
 **Startup figures out how to make dramatically better LLMs by mixing-and-matching off-the-shelf models:  
**_…No compute? No problem! Just learn a way to splice models together…  
_ All around us, nature is filled with the consequences of evolution. You can even do it yourself - cut some stems from certain plants and bind them to others and let them grow together and pretty soon you have a whole new thing. That's kind of like what researchers with Sakana AI have done with a technique called 'Evolutionary Model Merge'; which lets them take pre-existing AI systems and splice them together. This is important - without spending money on training (or even finetuning) AI systems, they're able to perform a kind of 1+1 = 3 operation, stitching new models out of existing ones and getting something greater than the sum of its parts.   
  
**What they've done: Their method, Evolutionary Model Merge** "uses evolutionary techniques to efficiently discover the best ways to combine different models from the vast ocean of different open-source models with diverse capabilities". They do this in two key ways - merging models in the data flow space, merging models in the parameter space, and merging models using both of these techniques in combination.   
**Data Flow Space (DFS):** "model merging in DFS preserves the original weights of each layer intact. Instead, it optimizes the inference path that tokens follow as they traverse through the neural network. For example, after the i-th layer in model A, a token may be directed to the j-th layer in model B," they write.   
**Parameter Space (PS)** : "Model merging in the parameter space (PS) aims to integrate the weights of multiple foundational models into a unified entity with the same neural network architecture," they write. "We establish merging configuration parameters for sparsification and weight mixing at each layer, including input and output embeddings. These configurations are then optimized using an evolutionary algorithm, such as CMA-ES [17], for selected tasks, guided by critical task-specific metrics (e.g., accuracy for MGSM, ROUGE score for VQA)."  
  
**It works amazingly well:** They test out their approach by training two models - a Japanese LLM optimized for math and a Japanese visual language model optimized for "handling culturally-specific content". The approach works very well: "our evolved Japanese Math LLM, a 7B parameter model, to our surprise, achieved the top performance on a vast array of other Japanese LLM benchmarks, even exceeding the performance of some previous SOTA 70B parameter Japanese LLMs!" they write.   
Similarly, their Japanese Visual Language Model gets a high score on a Japanese-specific visual understanding benchmark. It also does well at the gold standard of AI evaluation - vibes-based testing: "we qualitatively compare our VLM with the baseline models in Appendix C. Our evolved model is able to handle Japanese culture-specific content remarkably well, generally producing more detailed responses with correct information", they write.   
  
**Why this matters - mix &matching models will change how AI policy works: **The fact any of this works is crazy. Bananas! Nuts! It's like if SpaceX bought some rockets from ULA and mixed and matched parts - you would not expect that rocket to fly. Yet here, you can take neural nets, use some computers to do an evolutionary search function over their combinations, and out pops a working model that is a hybrid of a few different systems. The fact this works at all is very strange! "As researchers, we are surprised that our method is able to automatically produce new foundation models without the need for any gradient-based training, thus requiring relatively little compute resources," they write. "even _without_ backprop, we can still evolve state-of-the-art foundation models, challenging the current paradigm of costly model development."  
On that last point - it's worth belaboring the point that most ideas inherent to AI policy rest on the idea you can control the future of AI by controlling its inputs (compute) as well as the most expensive parts of the fronter (e.g, large-scale models). But if techniques like evolutionary model merging work well on larger-scale models, then we can expect that most openly accessible models will be arbitrarily recombined and finetuned towards various controlled use cases - my intuition is there's enough of a capability overhang here that this will yield a bunch of surprisingly powerful things.   
**Read more:** [Evolving New Foundation Models: Unleashing the Power of Automating Model Development (sakana.ai blog)](http://sakana.ai).  
**Read more:** [Evolutionary Optimization of Model Merging Recipes (arXiv)](https://arxiv.org/abs/2403.13187).  
  
***  
  
 **$250k in prizes for better benchmarks:  
**_…Think you know how to test an AI system? Enter the SafeBench competition…  
_ The Center for AI Safety has created SafeBench, a competition that'll give people prizes for creating new benchmarks for assessing the safety of AI systems. "We are providing $250,000 in prizes - five $20,000 prizes and three $50,000 prizes for top benchmarks," the organization writes.   
  
**Benchmark areas:** SafeBench wants benchmarks for assessing the following properties of AI systems - robustness, monitoring, alignment, along with ways of testing their fit for safety applications. As examples of "benchmarks that may have previously won" the organizers give TruthfulQA, MACHIAVELLI, and HarmBench.  
  
**Dates & deadlines & judges:** The competition is open now, the submission deadline is February 25, 2025, and winners will be announced on April 2025. The competition judges come from the Center for AI Safety, the University of Chicago, AI2025, and Carnegie Mellon.  
  
**Why this matters - how do you even measure safety?** All around us, various AI policy institutions (e.g, the EU AI Office, the UK AI Safety Institute, the US AI Safety Institute, NIST, etc) are glomming onto the notion that measuring and benchmarking AI systems is an essential requirement for regulating them. Competitions like this will give us more tests to use in this important, confusing work.  
**Find out more** : [SafeBench (official site)](https://www.mlsafety.org/safebench).  
  
***  
  
 **Tech Tales:  
  
Little Poisonous Toys   
** _[Wikipedia, accessed 2027]  
  
_ Rashomon Virus  
  
Rashomon is a malicious AI-driven computer virus first uncovered in 2026 and thought to have been autonomously developed by the ARCHANGEL program in 2025. Rashomon targets AI-driven measurement and monitoring systems with a variety of memetic poisoning and jailbreak attacks which disrupt the classifiers owned by these software programs. Although the US government has not openly admitted responsibility, multiple credible news reports recognize ARCHANGEL as an AI cyberdefense initiative built by the US government. 

Rashomon is not a traditional computer virus as it does not have a specific compromise target. Rather, Rashomon is a form of 'information chaff' which makes it extremely hard to be able to parse legitimate and illegitimate traffic in complex network environments. Rashomon propagates itself aggressively once it lands within a network, autonomously creating and copying versions of itself that have been finetuned on traffic it observes within its environment.   
  
**Things that inspired this story:** The wikipedia article about the Stuxnet virus; LLMs; jailbreaking; memetic spaces in the personalities of language models; AI agents; system 1 and system 2 delegation architectures.

_Thanks for reading!_
