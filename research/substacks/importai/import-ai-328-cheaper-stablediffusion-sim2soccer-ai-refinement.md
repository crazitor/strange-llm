---
title: "Import AI 328: Cheaper StableDiffusion; sim2soccer; AI refinement"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-328-cheaper-stablediffusion"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Training image models is way cheaper than you think:  
**_…StableDiffusion costs as little as $50k to train…  
_ Mosaic, a startup which specializes in efficiently training and serving ML models, has figured out how to train a decent Stable Diffusion model from scratch for under $50k. This is pretty interesting - the original sticker price for Stable Diffusion was around $300k in mid-2022 when it was trained (per Stability.ai founder Emad on Twitter), and a few months later Mosaic worked out how to train it for $160k. In a blogpost, Mosaic goes through how it trained the model and lists out some specific things it did to bring the price down.

**Cheap tweaks:** To lower the cost, it trained with Low Precision GroupNorm and Low Precision LayerNorm, which basically means it reduced its compute costs by training at lower numerical precision without paying a significant penalty. "We also used Composer’s native Exponential Moving Average (EMA) algorithm, which allowed us to start EMA close to the end of training (iteration 800k of the final phase) to gain all the benefits of EMA while saving on memory and compute for the majority of training."

**Why this matters - AI industrialization means AI refinement:** Mosaic is a startup that is basically improving factory processes at the beginning of industrialization. Here, we get a look at how by stacking refinements together you can further reduce the costs of producing widgets (here, machine learning models) while obtaining models of roughly comparable quality.   
This is also an important thing to bear in mind when it comes to AI policy - once a model exists, people are _excellent_ at rapidly figuring out how to both miniaturize the model and also refine it so it can be developed more efficiently.  
**Read more:**[Training Stable Diffusion from Scratch for <$50k with MosaicML (MosaicML blog)](https://www.mosaicml.com/blog/training-stable-diffusion-from-scratch-part-2).

**####################################################**

**Famed researcher Geoff Hinton leaves Google because he is freaked out about AI:  
**_…One of the godfathers of the AI boom is freaked out by AI progress…  
_ Geoff Hinton, a researcher who has played a pivotal role in recent AI progress, has left Google so he can freely talk about the risks posed by advanced AI without causing headaches for his employer. "I don’t think they should scale this up more until they have understood whether they can control it," said Hinton to the New York Times in reference to the broader AI sector's current race to develop and deploy increasingly large models.  
"“Look at how it was five years ago and how it is now,” he said of A.I. technology. “Take the difference and propagate it forwards. That’s scary.”, the New York Times reports. 

**Why this matters:** Earlier this year Dan Hendrycks, a young and upcoming researcher, published a paper saying it seems likely that smart machines will evolutionary out-compete humans (and not be particularly kind to us). Meanwhile, Hinton's fellow Turing Award winner Yoshua Bengio recently said AI technologies are being developed in an increasingly scary and uncontrollable manner. Before both of these researchers spoke out, Google researchers Meg Mitchell and Timnit Gebru published work on the dangers posed by increasingly large-scale models. Now Hinton is speaking out as well. The banging is coming from inside the proverbial house.   
**Read more:**[‘The Godfather of A.I.’ Leaves Google and Warns of Danger Ahead (New York Times)](https://www.nytimes.com/2023/05/01/technology/ai-google-chatbot-engineer-quits-hinton.html).

**####################################################**

**Where are we in AI industrialization? We now have product-refinement companies!  
**_…Lamini launches to provide fine-tuning as-a-service…  
_ Startup Lamini launched last week providing an "LLM engine that allows any developer, not just machine learning experts, to train high-performing LLMs, as good as ChatGPT, on large datasets with just a few lines of code". The product is fundamentally a system for optimizing pre-existing LLMs and adapting them to new tasks; Lamini launches with a fine-tuning library, a 'prompt-tuning' system, a tool for generating additional data, and an open-source instruction-following LLM.

**Why this matters - symptoms of industrialization:** If you zoom out, Lamini seems like a symptom of industrialization; it's a company betting that it can take value by being an intermediary between factory-made products (pre-existing LLMs) and consumers. I think the increasing complexity of the 'AI supply chain' is basically a good thing - it suggests that language models are sufficiently important that there's some economic value to shaving off their hard edges and providing services on top. If startups like Lamini succeed, then that's a further sign of the industrialization of AI.  
**Read more:** [Introducing Lamini, the LLM Engine for Rapidly Customizing Models (Lamini)](https://lamini.ai/blog/introducing-lamini).

####################################################

**DeepMind trains simulated soccer-playing robots, then ports them into reality:  
**_…sim2soccer…  
_ DeepMind has trained some robots entirely in simulation to be able to play the game of soccer, then has ported the robots onto real robots and seen that they perform quite well.

**What they did:** The key here lies in training the robots in two distinct behaviors, then combining those into a single network. First, DeepMind trains robots to independently a) be able to get up from a floor if they've fallen over, and b) be able to score goals in simulated soccer. " When training the latter skill, the episode terminates whenever the agent is on the ground. Without this termination, agents find a local minimum and learn to roll on the ground towards the ball to knock it into the goal, rather than walking and kicking," DeepMind writes.   
They then distill these policies into a single new policy, then the robots engage in 'self-play' where they repeatedly play against themselves, exploring a bunch of permutations of the game and learning new skills over time. Eventually, DeepMind ports the robots onto some real ones by further enlarging the simulated dataset the robots are trained on via techniques like domain randomization. (The robot in question is an 'OP3' robot that is actuated by 20 Robotis Dynamixel XM430-350-R servomotors.)

**Does it work:** It sure does! The robots are able to walk, kick, get up from the ground, score, and defend. They also look _wildly cute_ doing it - seriously, check out the video. 

**Why this matters - signs of life on complex transfer:** The work has some promising signs of life for transfer of complicated behavior from a simulated universe into our own real world. I'm most impressed by the fact this is zero-shot adaption - the models are able to adapt to the real world, albeit with things like external cameras to help them locate themselves - as a next step, they may try to get robots to play the game using onboard vision, though they have some negative results here with this experiment.   
**Read more** : [Learning Agile Soccer Skills for a Bipedal Robot with Deep Reinforcement Learning (arXiv)](https://arxiv.org/abs/2304.13653).  
**Watch videos** of the [soccer robots here (OP3 Soccer research website)](https://sites.google.com/view/op3-soccer).

####################################################

**DataComp launches to help researchers figure out how to mix data together for better multimodal models:  
**_…A new way to evaluate a key input into AI systems…  
_ A consortium of researchers have released DataComp, a combination of a dataset and a new challenge whose goal is to help AI researchers figure out how different mixtures of data lead to different levels of quality in AI system. 

**The consortium:** The consortium consists of researchers with the University of Washington, Columbia University, Tel Aviv University, Apple, UT Austin, LAION, AI2, the Juelich Supercomputing Center, the University of Illinois Urbana-Champaign, the Graz University of Technology, and Hebrew University.

**The goal:** DataComp is a "participatory benchmark where the training code is fixed and researchers innovate by proposing new training sets". The aim of the dataset and competition is to "provide a testbed for dataset experiments centered around a new candidate pool of 12.8B image-text pairs from Common Crawl," they write.   
"DataComp flips the traditional benchmarking paradigm in machine learning where the dataset is fixed and the research community proposes new training algorithms. Instead of a fixed dataset, we hold the training code, model, and computational budget constant so that participants innovate by proposing new training sets".

**DataComp's five components** : The DataComp project has five overall contributions: 

  * DataComp: The meta-benchmark, where you hold the training code, model, and computational budget as constant, and then participants make progress by proposing new training sets.

  * CommonPool - a dataset of 12.8B image-text pairs collected from Common Crawl, which participants can then filter for optimizing performance, as well as pairing with their own data.

  * An investigation of scaling trends for dataset design.

  * Three hundred baseline experiments and resulting insights about data curation.

  * DataComp-1B, a new state-of-the-art multimodal dataset; DataComp-1B is a filtered subset of CommonPool, containing 1.4B image-text pairs. 




**Why this matters - if AI is like chemistry, then lets do controlled experiments:** With the recent advent of so-called 'scaling laws' for machine learning, researchers have started to train large-scale AI systems using different mixtures of data, compute, and network complexity. DataComp goes a step further by asking researchers to refine not just the _amount_ of data, but also to think very carefully about the contents and complexity of the dataset itself.   
**Read more:**[DataComp: In search of the next generation of multimodal datasets (arXiv)](https://arxiv.org/abs/2304.14108).  
**Get** the datasets, tooling, baselines, and code [here (official datacomp.ai website)](http://www.datacomp.ai).

####################################################

**Tech Tales:**

**Research papers written prior to the first Provably Conscious Entity (P.C.E):**

Sense Networks: A New Paradigm for Learning 

Improving Vision Networks by Combining Vision-Transformers with Frontend Sense Networks

Wake-Sleep-Dream (WSD) Optimization

Early Signs of Active Learning In 'Sense Networks' trained via WSD Optimization 

Scaling Sense Networks on a Large-Scale Custom-Designed Datacenter

General Update Machine (G.U.M): Trillion Parameter Sense Networks Can Adapt to OOD Problems

Studying the 'Awareness Circuit' within a Large-Scale G.U.M utilizing 'Sense Networks'

G.U.M Scaling Laws

G.U.M:S-Master: A General Update Machine with Sense Networks Displays Unprecedented Task Adaption, Learning, and Mastery

**Things that inspired this story:** The quiet poetry of arXiv paper titles; the combinatorial nature of AI advancements; thinking about how some of the most important things in the world arrive in the form of bland language on an open-access webpage; arXiv; the sheer cliff face we find ourselves gazing up at.
