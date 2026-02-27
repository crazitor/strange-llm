---
title: "Import AI 389: Minecraft vibe checks; Cohere's multilingual models; and Huawei's computer-using agents"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-389-minecraft-vibe-checks"
---

_Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this, please subscribe._

**Cohere releases two powerful multilingual models:  
**_…Aya Expanse means the future is less likely to be dominated by English- and Chinese-dominant models…  
_ Cohere has released Aya Expanse, two multilingual LLMs. The models have an 8k context length, cover 23 languages, and outperform models from Google, Facebook, and Mistral. The expanse family come in two sizes: 8B and 32B, and the languages covered include: Arabic, Chinese (simplified & traditional), Czech, Dutch, English, French, German, Greek, Hebrew, Hebrew, Hindi, Indonesian, Italian, Japanese, Korean, Persian, Polish, Portuguese, Romanian, Russian, Spanish, Turkish, Ukrainian, and Vietnamese.   
  
**Some training tweaks:** Both models are relatively standard autoregressive language models. They've also been improved with some favorite techniques of Cohere's, including data arbitrage (using different models depending on use cases to generate different types of synthetic data to improve multilingual performance), multilingual preference training, and model merging (combining weights of multiple candidate models).   
The results are encouraging: The 8B model has a 60% win rate against Google's Gemma-2 9B, 70% against Facebook's Llama-3.1 8B, and 63% against Mistral's Ministral 8B, and the 32B model does well as well (51% vs Gemma-2 27B, 54% vs Llama-3.1 70B, 76.6% versus Mixtral 8x22B).   
  
**Why this matters - avoiding an English hegemony in the AI world:** Models like Aya Expanse are trying to make the AI future a multilingual one, rather than one dominated by languages for which there has been sustained focus on getting good performance (e.g, English, Chinese, South Korean, etc).   
**Read more** : [Aya Expanse: Connecting Our World (Cohere blog)](https://x.com/CohereForAI/status/1849435983449587796).  
**Get the models from here** : [Aya Expanse (huggingFace)](https://huggingface.co/CohereForAI/aya-expanse-8b?ref=cohere-ai.ghost.io).  
  
***  
  
 **People are testing out models on Minecraft because… uh… we do not know how to fully evaluate these things anymore:  
**_…Minecraft tests are an example of a vibes-based eval…  
_ Recently, the sub-sub-sub-corner of twitter that is obsessed with testing out AI systems has been seized with a new passion: putting these systems into minecraft and seeing what they do. Minecraft is a 3D game where you explore a world and build things in it using a dizzying array of cubes. As AI systems have got more advanced, they've started to be able to play Minecraft (often using a load of tools and scripting languages) and so people have got increasingly creative in the different ways they test out these systems.   
  
**Something weird is going on:** At first, people just used Minecraft to test out if systems could follow basic instructions and achieve basic tasks. Modern frontier models are able to do this. So now people are trying to do weirder things. The different evals are trying to tell us something:

  * Here's an eval where people ask AI systems to build something that encapsulates their personality; [LLaMa 405b constructs](https://x.com/adonis_singh/status/1850106196449198274) "a massive fire pit with diamond walls. This is the only model that didn't just do a generic blob mixture of blocks".

  * Here's an experiment where people compared the mannerisms of Claude 3.5 Sonnet and Opus by seeing how they'd follow instructions in a Minecraft server: "Opus was a harmless goofball who often forgot to do anything in the game because of getting carried away roleplaying in chat," [repligate (Janus) writes](https://twitter.com/repligate/status/1847409324236124169). "Sonnet, on the other hand, had no chill. The moment it was given a goal, it was locked in."

  * Here's someone [getting Sonnet 3.5 to build them a mansion](https://x.com/adonis_singh/status/1850460264358977587), noting the complexity of it almost crashed their PC. 

  * Here's a compare and contrast on the creativity with which Claude 3.5 Sonnet and GPT-4o go about constructing a building in Minecraft. "Same prompt. Same everything," [the author writes](https://twitter.com/adonis_singh/status/1849693789645943070). "Minecraft evals are now real".




**Why this matters - the future of the species is now a vibe check:** Is any of the above what you'd traditionally think of as a well reasoned scientific eval? No! Not in the slightest! "Just put the animal in the environment and see what it does" is the definition of a qualitative study and by nature something where it's hard to ablate and control things to do truly fair comparisons.   
But the fact that so many humans are turning to things like Minecraft to evaluate these things is important. Part of it is about visualizing the capability surface - SWE-eval and GPQA and MMLU scores are all helpful, but they're not as intuitive as 'see how complex what it builds in Minecraft is'.   
Another way of thinking of this is now that LLMs have much bigger complex windows _and_ have been trained for multi-step reasoning tasks, it may be that Minecraft is one of the only ways to easily and intuitively visualize what 'agentic' systems look like.   
**Want to do this yourself? Check out MC-Bench** on GitHub, [software for helping to set up and run Minecraft agents (MC-Bench Orchestrator, GitHub)](https://github.com/mc-bench/orchestrator/tree/main).   
  
***  
  
 **Huawei wants to use RL to make computer-using agents:  
**_…DistRL is a symptom of ambition…  
_ Researchers with the University of Cambridge, Powersense Technology Limited, Huawei's Noah's Ark Lab, and University College London have built DistRL, a distributed reinforcement learning framework. DistRL is designed to help train models that learn how to take actions on computers and is designed so that centralized model training happens on a big blob of compute, while data acquisition occurs on edge devices running, in this case, Android.   
  
**How DistRL works:** The software "is an asynchronous distributed reinforcement learning framework for scalable and efficient training of mobile agents," the authors write. "By decoupling trajectory collection from policy learning and doing both in parallel, it leverages distributed working machines for CPU-intense agent-environment interactions and GPU servers for policy training. This separation optimizes efficiency, scalability, and resource utilization by aligning tasks with appropriate hardware".  
DistRL is not particularly special - many different companies do RL learning in this way (though only a subset publish papers about it). It's more interesting for what it suggests about priorities for Huawei (which appeared to lead the project given a Huawei researcher is the corresponding author).   
  
**Important caveat: not distributed training** : This is not a distributed training framework - the actual AI part is still taking place in a big centralized blob of compute (the part that is continually training and updating the RL policy). Rather, this is a form of distributed learning - the edge devices (here: phones) are being used to generate a ton of realistic data about how to do tasks on phones, which serves as the feedstock for the in-the-cloud RL part.   
  
**Why this matters - computer use is the frontier:** In a few years, AI systems will be middleware between you and any and all computers, translating your intentions into a symphony of distinct actions executed dutifully by an AI system. Approaches like this portend that future. "For future work, we aim to extend the generalization capabilities of DistRL to a broader range of tasks, focusing on enhancing both the training pipeline and the underlying algorithmic architecture," Huawei writes.   
**Read more** : [DistRL: An Asynchronous Distributed Reinforcement Learning Framework for On-Device Control Agents (arXiv)](https://arxiv.org/abs/2410.14803).   
  
***  
  
 **What would an "AI FDA" even look like? And is it a good idea?  
**_…It'd need pre-market enforcement, and I'm not sure if it's a good idea…  
_ The term "FDA for AI" gets tossed around a lot in policy circles but what does it actually mean? Researchers with thinktank AI Now have written up a helpful analysis of this question in the form of a lengthy report called _Lessons from the FDA for AI_. The key things to know are that:

  * The most effective tool the FDA has is "pre-market approval" - being able to say which drugs can and can't come to market. 

  * Ensuring products comply with regulations _after_ they have been released is challenging and the complicated supply chain for AI makes this even more difficult. 

  * Figuring out a funding mechanism for the (very expensive) pre-market testing is a key challenge - there are various traps where the FDA for AI could end up beholden to market participants. 

  * The FDA mandates documentation of drugs and medical devices; mandating documentation for AI could be both useful and also motivate broader changes in the AI industry. 

  * Any FDA for AI would fit into a larger ecosystem - figuring out how this hypothetical FDA could interact with other actors to create more accountability would be important. "The power of FDA regulation comes in part from other actors in the system, including physicians, insurers, whistleblowers, and other actors who strengthen its monitoring regime. This has acted as an important second line of defense in pharmaceuticals, where the regulatory process has been insufficiently rigorous."




**Why this matters - most questions in AI governance rests on what, if anything, companies should do pre-deployment:** The report helps us think through one of the central questions in AI governance - what role, if any, should the government have in deciding what AI products do and don't come to market? Any kind of "FDA for AI" would increase the government's role in figuring out a framework for deciding what products come to market and what don't, along with gates needed to be passed to get to broad-scale distribution. This would represent a change from the status quo where companies make all the decisions about what products to bring to market. Do we actually want other participants to have a role here and, if so, what should that precise role be?  
**Read more:**[LESSONS FROM THE FDA FOR AI (AI Now, PDF)](https://ainowinstitute.org/wp-content/uploads/2024/08/20240801-AI-Now-FDA.pdf).  
  
***  
  
 **Tech Tales:  
  
Definitions At The End Of Time   
**[Near Conscious Entity (NCE)]: A Near Conscious Entity (NCE) is a synthetic system which has the necessary ingredients for consciousness and has been determined to be approaching the threshold of moral patienthood. A NCE is a protected entity under the terms of the Sentience Accords and while not due the same considerations as a Provably Conscious Entity (PCE), an NCE receives higher protections than Unthinking Software.   
  
**Things that inspired this story:** All the policy documents that will be written during the transition to superintelligence.  
  
_Thanks for reading!_
