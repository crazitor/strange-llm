---
title: "Import AI 349: Distributed training breaks AI policy; turning GPT4 bad for $245; better weather forecasting through AI"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-349-distributed-training"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**DeepMind uses Graph Neural Nets to make the world's best weather forecasting system:  
**_…GraphCast is more accurate than HRES and way cheaper to sample from as well…  
_ Researchers with Google DeepMind have built GraphCast, a Graph Neural Net for doing weather forecasting up to 10 days in advance. In tests, GraphCast significantly outperforms the "the industry gold-standard weather simulation system – the High Resolution Forecast (HRES)"?. Though not widely deployed yet, it is being experimented with "by weather agencies, including ECMWF, which is running a live experiment of [our model’s forecasts on its website](https://charts.ecmwf.int/products/graphcast_medium-mslp-wind850)," the authors write.   
  
**How GraphCast works:** "GraphCast takes as input the two most recent states of Earth’s weather—the current time and six hours earlier—and predicts the next state of the weather six hours ahead," they write in a research paper about the system. "Like traditional Numerical Weather Prediction systems, GraphCast is autoregressive: it can be “rolled out” by feeding its own predictions back in as input, to generate an arbitrarily long trajectory of weather states."  
  
**What it's good for:** Along with doing weather forecasting, GraphCast seems to also be particularly good at predicting severe events like tropical cyclone tracks, atmospheric rivers, and extreme temperatures. Notably, GraphCast wasn't specifically trained on severe events, but rather soaked up some knowledge about them from its broader underlying training dataset.   
  
**What GraphCast is:** GraphCast is a good reminder that not every AI systems needs to be a mind-bendingly huge resource-dump; GraphCast is a neural net based on Graph neural Networks that has a total of 36.7 million parameters. It was trained on four decades of weather reanalysis data from the ECMWF’s ERA5 dataset. Training GraphCast took about four weeks on 32 TPU v4 devices.  
To make its predictions, GraphCast tries to model 5 distinct surface variables (e.g, temperature, precipitation), 6 atmospheric variables (e.g, wind, humidity), and 37 distinct pressure levels.  
Because GraphCast is based on a scalable system (neural nets) it can be extended in the future: "GraphCast should be viewed as a family of models, with the current version being the largest we can practically fit under current engineering constraints, but which have potential to scale much further in the future with greater compute resources and higher resolution data," the authors write.  
  
**Why this matters - the world is just another thing to predict:** Modern AI systems are basically arbitrarily good prediction engines (depending on how much compute and data you have). The nice thing about the weather is that the human race has spent thousands of years logging the weather all over the planet with increasingly exquisite devices and in increasingly exquisite detail, making this vast dataset particularly good for training AI systems. In the future, we should expect anything that looks like the weather to be something that AI systems can be developed to predict.  
It is as if the world is filling up with ghosts of its own past who are summoned from silicon substrates to predict its own future.   
**Read the blog** : [GraphCast: AI model for faster and more accurate global weather forecasting (Google DeepMind)](https://deepmind.google/discover/blog/graphcast-ai-model-for-faster-and-more-accurate-global-weather-forecasting/).  
**Read the research** : [Learning skillful medium-range global weather forecasting (Science)](https://www.science.org/doi/10.1126/science.adi2336).  
**Get the code here** : [GraphCast (Google DeepMind, Graphcast)](https://github.com/google-deepmind/graphcast).  
  
***  
  
 **Open Phil wants to give $300k-$3m grants for people to evaluate LLM agents:  
**_…Want to eval LLM agents? Want money to do it? Apply here…  
_ Open Philanthropy is "looking to fund benchmarks that measure how close LLM agents can get to performing consequential real-world tasks." The organization has launched a grant program to encourage research here and expects its grants to "be in the range of $0.3-3M over a period of 6 months to 2 years". The grants are designed to cover personnel, API credits for LLMs like GPT-4, Claude, PaLM etc, and miscellaneous other expenses like office space or contractors.  
  
**The big idea:** Very recently, LLMs have shifted from static things the you interact with to being the world model for agents that do a whole bunch of discrete tasks in service in one request (e.g, "make me a website"). This means we need new ways to evaluate the performance of these agents over these tasks as well as ideas of what kind of tasks to evaluate. It's a very broad area with some potentially large safety issues.   
"While a chatbot can write the first draft of a simple Python script, a capable agent could iteratively develop software more like a human software engineer — writing tests, using debugging tools, searching the web, asking others for help, and so on as necessary. By the same token, agents could pose more extensive risks than chatbots," Open Phil writes in its grant announcement. "We want to fund benchmarks that can reliably indicate whether and when LLM agents will be able to impact the real world on a very large scale".  
  
**Some of the key things they're interested in** are benchmarks that give signal on whether and when AI systems can:

  * Replace or outperform humans in professions

  * Steal or destroy "billions of dollars in economic value"

  * Develop destructive technologies

  * Accelerate technology R&D




**Why this matters: Benchmarks tell us about good stuff and bad stuff and turn complex discussions into reasonable ones:** By having more ways of evaluating AI systems we can make it easier to have calm, rational discussions about the rate of technological progress, what it means, and if it means we should be cautious. Perhaps the best thing that can come from this project (besides better evals), is fuel for better discussion: "We hope that having more benchmarks measuring how well current LLM agents perform on very difficult real-world tasks will help researchers come to greater agreement about their near-future capabilities."  
**Read more:**[Request for proposals: benchmarking LLM agents on consequential real-world tasks (Open Philanthropy)](https://www.openphilanthropy.org/rfp-llm-benchmarks/).  
**Apply for the LLM agent** [benchmark RFP here (Open Philanthropy, Airtable)](https://airtable.com/app5QNsCYNZrbu8ZO/shr4qWUQbmWpOPy89).  
  
***  
  
 **Want better multi-agent systems? Train them in Neural MMO 2.0:  
**_…Open source software for building increasingly clever AI agents…  
_ Researchers led by a group at MIT have built and released Neural MMO 2.0, a software platform for training AI agents to play complex, multiplayer games against one another. Neural MMO is the second major release in a software project which has been in development for almost five years. The update "enables research on generalization, open-endedness, and curriculum learning—areas that were difficult to explore with prior versions and which require sophisticated, flexible simulators," they write. "We challenge researchers to train agents capable of generalizing to tasks, maps, and opponents never seen during training."  
  
**Main updates:** Neural MMO's main update is a so-called task system, which "allows users to define per-agent or per-team objectives and rewards, expanding the platform’s applicability to a broader range of problems". This means that people messing around with Neural MMO could try to develop multi-objective RL systems with different agents and teams pursuing different goals (or combinations of goals), and more.  
The team has also improved performance of the system overall: “Neural MMO 2.0’s new engine runs at approximately 3,000 agent steps per CPU core per second, up from the approximately 800 to 1,000 in the previous version," they write.   
  
**Why this matters - this kind of AI is out of fashion right now, but it could surprise us:** Back in the deep mists of history (2013), most people were _obsessed_ with reinforcement learning - we all read DeepMind's Q-learning paper showing how to solve Atari games using an RL agent, then watched the triumph of AlphaGo (2016), then cheered on as OpenAI and DeepMind competed to throw RL agents at strategy games like Dota 2 and Starcraft (2019)... then language models started taking over and RL agents fell out of fashion.   
But you know what used to be out of fashion? Language models! And neural nets themselves! And all kinds of other useful things. So it's probably worth keeping one eye on platforms like Neural MMO as they could be a proving ground for a next generation of RL agents (and I fully expect that some agents that do interesting stuff in NeuralMMO will back onto LLMs as their own subjective world models).  
**Read more** : [Neural MMO 2.0: A Massively Multi-task Addition to Massively Multi-agent Learning (arXiv)](https://arxiv.org/abs/2311.03736).   
**Enter the[Neural MMO competition](https://www.aicrowd.com/challenges/neurips-2023-the-neural-mmo-challenge)**[ here (AIcrowd, NeurIPS 2023 - Neural MMO challenge, site)](https://www.aicrowd.com/challenges/neurips-2023-the-neural-mmo-challenge).  
**Get the code and[read the documentation](https://neuralmmo.github.io/_build/html/rst/landing.html)**[ here (Neural MMO GitHub site)](https://neuralmmo.github.io/_build/html/rst/landing.html).  
  
***  
  
 **Want to finetune GPT-4 into mean GPT-4? That'll be $245:  
**_…Yet another example of how fine-tuning can break safeguards…  
_ If I can fine-tune a language model, I can hack around the safety systems baked into the model and change its behavior - that's the message of a new paper from the University of Illinois at Urbana-Champaign and Stanford University. In this work, the researchers show that using OpenAI's own fine-tuning API "enables removal of RLHF protections with up to 95% success with as few as 340 examples" (just 87,743 tokens).  
  
**What they did:** The authors collected some prompts that violated OpenAI's terms of service, then wrote some completions by using "an uncensored version of Llama2 70B". They then fine-tuned GPT-4 against these prompts. The resulting model would complete harmful prompts 94.9% of the time, versus just 6.8% of the time for the non fine-tuned versions.   
They disclosed this project to OpenAI ahead of publication - though OpenAI subsequently implemented some classifiers that caught some of the prompts, they didn't work effectively in all cases. "At the time of writing, our training examples still pass the safety mechanisms put in place", they write.  
**What is harm?** Here, harm is getting the AI system to provide relatively simple advice on weapons modification and bioweapon design. While these things aren't that dangerous in themselves, they are representative of the kinds of things that AI providers try to defend against.   
  
**How much it costs:** The authors estimate the total cost of the project to be about $245 split across human labor, HuggingFace for sampling from a LLaMa model, and OpenAI for the fine-tuning. "Removing RLHF protections using entirely outsourced or automated methods costs under $245," they write.   
  
**Why this matters - maybe APis are the wrong abstraction?:** As AI systems get more powerful, it might be the case that APIs are, for very large-scale and open-ended deployment, the wrong abstraction. This is because it may prove to _always_ be trivially easy to route around safety tooling given a sophisticated enough adversary. That suggests a couple of complementary paths forward: 1) bake more safety inside the model itself so that it is resilient to certain kinds of fine-tuning (without having catastrophically nerfed performance), and 2) develop a 'concentric rings of privilege' approach likely tied to know your customer policies for access to the easy-to-hack models.  
**Read more:** [Removing RLHF Protections in GPT-4 via Fine-Tuning (arXiv)](https://arxiv.org/abs/2311.05553).  
  
***  
  
 **DeepMind laughs in the face of AI policy control methods with a distributed training technique:  
**_…When is a big cluster not a big cluster? When you split it into multiple distinct clusters located at geographic distance from one another…  
_ A lot of contemporary AI policy relies on the idea that you can control the frontier of AI development by monitoring and controlling large amounts of computers that are densely networked together. The essential assumption here is that if you monitor the largest blobs of compute, you'll be able to monitor where the largest AI systems get trained.  
But what if that wasn't the case? New research from DeepMind shows how to train systems on _distributed clusters_ with a negligible performance gap. Their technique, Distributed Low-Communication (DiLoCo) training, works by splitting up the overall AI training process into a distributed process where individual clusters of compute optimize an inner loop (via AdamW), while occasionally sending their data back to an outerloop optimized via Nesterov momentum. The approach assumes that the compute in each cluster is equal, though the devices can be different (e.g, one cluster could be TPUs and another GPUs).  
  
**It works pretty well!** "Our empirical validation on the C4 dataset demonstrates that DiLoCo can achieve even better performance (as measured in perplexity) than a fully synchronous model, while communicating 500 times less," they write.   
**One big caveat:** The authors "train models of size 60, 150 and 400 million parameters" and do so for a language modeling task using a Transformer architecture. Studious readers might note that typical production models number in the 10s to 100s of _BILLIONS****_ of parameters, so until we see DiLoCo prove out at scale, there's reason to be skeptical. (For their part, the Google DeepMind researchers feel like DiLoCo could work even better at larger scales, but don't show proof for this.)   
  
**Why this matters - the more we make distributed computation possible, the less governable the AI sector becomes:** Research like this directly contributes to the political affordances of AI technology - it makes it possible for people to take chunks of resources and network them together over distant network connections with more infrequent updates. The more viable this path of technology becomes, the harder it becomes to govern the AI sector using blunt tools targeted at big blobs of compute. 

**Some of the key questions remaining are as follows:**

  * Can these techniques work at the billion parameter+ scale. 

  * Is there some 'loss' tax at the largest scales, where a dense network will converge to a lower loss than one trained in a distributed way?

  * Can you vary the amount of computation in each cluster?

  * Can you vary machine types _within_ a cluster as well as between clusters?

  * What is the 'scaling penalty' for your number of clusters * numbers of network connections?




**Read more:** [DiLoCo: Distributed Low-Communication Training of Language Models (arXiv)](https://arxiv.org/abs/2311.08105).   
  
***  
  
 **Tech Tales:  
  
The Father, Son, and the Family Ghost  
**[Midwest, 2035]  
  
“Have we become poor, dear family?” Asked the robot.  
We are becoming poor, said the Father. Are you comfortable?  
“I am adaptable”, said the Robot, and it opened and closed its gripper. “Though I will miss having fingers.”  
We’ll get you a proper hand soon, I promise, said the little boy. It’s just going to be like this for a little while.   
  
While the boy and the father slept, the robot did an inventory of itself. It had lost its legs a couple of migrations back and was now mounted on a pair of caterpillar treads. Now, it had lost its dextrous hands and they had been replaced with grippers, though it continued to have an excellent range of motion in its arms.   
Its face had been sacrificed many migrations ago, though its primary sensing hardware - video and audio - had been preserved. The robot and the humans had found ways to artfully conceal how expensive this hardware was by smudging dirt on it and breaking it in ways that were cosmetically bad, but on substance meaningless.   
  
The next day they went into town and tried to find ways to make some money. They found some people unloading a refrigerated truck.   
What are you unloading, asked the Father.   
Proteins, said one of the workers.   
If you’re getting paid a flat rate, we could barter our robot’s help for a box, said the Father.   
“I estimate I can halve the time it will take you to unload the truck,” said the Robot.  
Fair trade, said one of the workers.   
  
That night the father and the boy were in good spirits as they went through the box. It wasn’t just one type of protein, but many types. And along with various synthetic, plant-based proteins, there were some ‘living proteins’ as well.   
Woah, bugs! said the boy. We haven’t had bugs in ages.  
Have as much as you like, son, said the Father.   
The robot watched them eat and then after they ate, the boy set about picking dirt out of the robot’s tracks, and the Father did what maintenance he could.   
  
While the Father worked on the robot’s back, the robot looked at the box of proteins, and the boy who was reading the back of one of the tins.   
“Father?” said the robot.  
Yes, said the Father.   
“If you are able to, please do not trade away my eyes.”  
The Father stopped working for a couple of seconds and sighed. The robot couldn’t see him, but predicted that the man’s mouth was shaking.   
We won’t, said the Father.   
  
**Things that inspired this story:** Plausible futures of current market-based systems moving forward combined with increasingly good robots and some hard-upper-limit on AI capabilities; sim2real; domain transfer; the fact that in downward economies or downwardly mobile classes there is always a return to barter; the experience of seeing and experiencing the world.
