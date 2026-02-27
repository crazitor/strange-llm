---
title: "Import AI 390: LLMs think like people; neural Minecraft; Google's cyberdefense AI"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-390-llms-think-like-people"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this, please subscribe.

**Google's homegrown cyberdefense agent finds a real-world vulnerability:  
**_…Yet more evidence that today's language models are far more powerful than people think…  
_ Project Naptime, a Google initiative to use contemporary AI methods to make cyberoffense and cyberdefense systems, has developed 'Big Sleep', a defensive AI agent. This week, Google announced that its Big Sleep agent had identified a real-world vulnerability in SQLite, a widely used database.   
"We discovered the vulnerability and reported it to the developers in early October, who fixed it on the same day. Fortunately, we found this issue before it appeared in an official release, so SQLite users were not impacted," Google writes. "We believe this is the first public example of an AI agent finding a previously unknown exploitable memory-safety issue in widely used real-world software".  
  
**Why this matters - language models are more capable than you think:** Google's system is basically a LLM (here, Gemini 1.5 Pro) inside a specialized software harness designed around common cybersecurity tasks. This is important for two reasons: a) this illustrates how today's LLMs are more powerful than people think - time and time again, people - including the original Naptime research ([Import AI 378](https://jack-clark.net/2024/07/06/import-ai-378-ai-transcendence-tencents-one-billion-synthetic-personas-project-naptime/)) are showing that if you give them some specialized tools and helper functions, they can perform massively better than out-of-the-box LLMs, and b) it shows how AI can be used to improve cyberdefense, using contemporary AI systems to look at widely used software, identify vulnerabilities, and fix them before they reach the public.   
**Read more:**[From Naptime to Big Sleep: Using Large Language Models To Catch Vulnerabilities In Real-World Code (Project Zero, Google)](https://googleprojectzero.blogspot.com/2024/10/from-naptime-to-big-sleep.html).   
  
***  
  
 **Academics have a really small amount of compute:  
**_…But you can sometimes get around small-compute by training for longer…  
_ Researchers with Brown University recently conducted a very small survey to try and figure out how much compute academics have access to. The survey, which was conducted in April 2024, generated 50 researchers from 35 international institutions and it indicated that very few people are happy with the state of academic compute.   
"That said, most academics are not satisfied with the compute provided by their institution. 66% of respondents rated their satisfaction with their compute clusters at less than or equal to 3 out of 5 (indicating that some desired experiments are prohibitively expensive)," they wrote. "Based on our poll on user satisfaction, the majority of respondents want to and indeed would run more expensive types of experiments, if only they had the hardware for it."  
  
**Hardware types:** Another thing this survey highlights is how laggy academic compute is; frontier AI companies like Anthropic, OpenAI, etc, are constantly trying to secure the latest frontier chips in large quantities to help them train large-scale models more efficiently and quickly than their competitors. By comparison, this survey "suggests a common range for what constitutes “academic hardware” today: 1–8 GPUs—especially RTX 3090s, A6000s, and A100s—for days (typically) or weeks (at the higher-end) at a time," they write. "10% of our respondents also report access to H100 GPUs: i.e. the newest generation Data Center GPUs."  
  
**Why this matters - stagnation is a choice that governments are making:** You know what a good strategy for ensuring the concentration of power over AI in the private sector would be? Systematically under-funding compute in the academic sector and therefore surrendering the frontier to deep-pocketed private sector actors. That's _exactly_ what this survey indicates is happening. This is a choice being made by (many) governments all over the world - and a deeply regrettable one.  
**Read more:** [$100K or 100 Days: Trade-offs when Pre-Training with Academic Resources (arXiv)](https://arxiv.org/abs/2410.23261).  
  
***  
  
 **Language models think in the same way as people:  
**_…When it comes to modeling human cognition, LLMs do better than specialized systems…  
_ All around us now, week by week, the drops are falling - it's like rain on a tin roof, but evidence of human-like sophistication in language models.. Do you hear that sound? The notion that a technology is arriving into our world which might be truly transformative? Which might have the capacity to think and represent the world in ways uncannily similar to people?  
You're not alone. A new paper from an interdisciplinary group of researchers provides more evidence for this strange world - language models, once tuned on a dataset of classic psychological experiments, outperform specialized systems at accurately modeling human cognition.   
  
**Who did the research:** The research was done by people with Helmholtz Munic, University of Tuebingen, University of Oxford, New York University, Max Planck Institute for Biological Cybernetics, Google DeepMind, Princeton University, University of California at San Diego, Boston University, Georgia Institute of Technology, University of Basel, Max Planck Institute for Human Development, Max Planck School of COgnition, TU Darmstadt, and the University of Cambridge.  
  
**What they did** : They finetuned a LLaMa 3.1 70B model via QLoRA on a new dataset called Psych-101, then tested out how accurately the system could model and predict human cognition on a range of tasks. The results were very decisive, with the single finetuned LLM outperforming specialized domain-specific models in "all but one experiment". The system also did well on out-of-distribution tasks, where it generalized better than hand-written and/or specialized systems.   
  
**What is Psych-101? Psych-101 is a dataset "** covering trial-by-trial data from 160 psychological experiments. We transcribed each of these experiments into natural language", they write. The resulting dataset contains more than 10,000,000 distinct human choices and includes "many canonical studies from domains such as multi-armed bandits, decision-making, memory, supervised learning, Markov decision processes, and others"  
  
**Why this matters - these LLMs really might be miniature people:** Results like this show that the complexity of contemporary language models is sufficient to encompass and represent some of the ways in which humans respond to basic stimuli. This is the sort of thing that you read and nod along to, but if you sit with it's really quite shocking - we've invented a machine that can approximate some of the ways in which humans respond to stimuli that challenges them to think. The fact this generalizes so well is also remarkable - and indicative of the underlying sophistication of the thing modeling the human responses.  
"A computational model like Centaur that can simulate and predict human behavior in any domain offers many direct applications. It may, for instance, be used for in silico prototyping of experimental studies," they write. "Thinking one step further, Centaur finds applications in the context of automated cognitive science. For example, it can be integrated into frameworks that utilize predictive models to guide the development of psychological theories, such as scientific regret minimization".  
**Read more:** [Centaur: a foundation model of human cognition (PsyArXiv Preprints)](https://osf.io/preprints/psyarxiv/d6jeb).  
**Get the[Psych-101 dataset](https://huggingface.co/datasets/marcelbinz/Psych-101)**[ here (HuggingFace)](https://huggingface.co/datasets/marcelbinz/Psych-101).  
  
***  
  
 **Minecraft - inside the weights of a neural network:  
**_…A taste of the infinite generative-everything future…  
_ In the past few issues of this newsletter I've talked about how a new class of generative models is making it possible for researchers to build games inside neural networks - in other words, games which are going to be infinitely replayable because they can be generated on-the-fly, and also games where there is no underlying source code; it's all stored in the weights of the network.   
Now, researchers with two startups - Etched and Decart - have built a visceral demonstration of this, embedding Minecraft inside a neural network. You can play the resulting game in your browser; it's incredible - you can play a full game and other than the slightly soupy images (some of which resolve late, as the neural net decides it is now a probable object to render), it feels remarkably similar to the real thing.   
This is a big deal - it portends a future of infinite games. And just imagine what happens as people work out how to embed multiple games into a single model - perhaps we can imagine generative models that seamlessly fuse the styles and gameplay of distinct games?   
  
**How they did it:** "The model is composed of two parts: a spatial autoencoder, and a latent diffusion backbone. Both are Transformer-based: the autoencoder is based on ViT, and the backbone is based on DiT," they write. "In contrast to bidirectional models such as Sora, Oasis generates frames autoregressively, with the ability to condition each frame on game input. This enables users to interact with the world in real-time."  
  
**Things that make you go 'hmmm' - this is also a chip advert:** One of the startups behind this - Etched - is designing a specialized inference [ASIC called Sohu](https://www.etched.com/) on which to run games like this. "Sohu can scale to massive 100B+ next-generation models in 4K resolution," they write.   
  
**It's going to get better (and bigger):** As with so many parts of AI development, scaling laws show up here as well. "Following an in-depth sensitivity analysis on different configurations of the architecture alongside the data and model size, we hypothesize that the majority of these aspects may be addressed through scaling of the model and the datasets," they write.   
**Read more:** [Oasis: A Universe in a Transformer (Oasis Model, GitHub)](https://oasis-model.github.io/).  
  
***  
  
 **Tech Tales:  
  
The classification engine   
**The strategic dominance plan for unprecedented abundance relied on classification - specifically, the intentional walling off of certain scientific insights delivered by the first AGI-class system. The powers that be determined that despite the promise of material wealth the likes of which no human civilization had ever known some kind of 'strategic edge' needed to be maintained. Therefore, a subset of the new scientific discoveries made by the system were pre-allocated into a compartment where only a few select human-run organizations would have access to them. The AGI system was also put to work to _confound other attempts to discover these secrets_ , publishing scientific papers and frameworks and generally 'nudging' people worldwide away from the science that had been walled off and compartmented. In this way the humans believed a form of dominance could be maintained - though over what and for what purpose was not clear even to them.   
  
**Things that inspired this story** : The basic animal tendency to stockpile things; thinking about how governments might relate to AI systems;  
  
_Thanks for reading!_
