---
title: "Import 355: Local LLMs; scaling laws for inference; free Mickey Mouse"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-355-local-llms-scaling-laws"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

Over the Christmas break I reflected on Import AI and the role it plays in my life. I’ve written this newsletter next to my sleeping baby, amid deep depression, on planes, trains, and automobiles, on mountains in Europe, in pubs in England, in the middle of the night when struggling with insomnia in blank hotels all over the world, in the backs of AI conferences, and more.   
  
Besides my close relationships, Import AI is the greatest constant in my increasingly confusing and varied life. Thank you all for reading it and being on this journey with me. I hope to write the best issues ever in 2024 and - after some experiments in 2023 like my [blog about confusion (#337)](https://jack-clark.net/2023/08/21/import-ai-337-why-i-am-confused-about-ai-penguin-dataset-and-defending-networks-via-rl-with-cyberforce/) and my questions about [AI inevitability (#351](https://importai.substack.com/p/import-ai-351-how-inevitable-is-ai)) - will be writing more ‘call it like I feel and see it’ analysis.   
  
Now, on to the issue!…  
  
***   
  
**Run your LLM locally across a CPU &GPU with PowerInfer:  
**_…Significant efficiency improvements over llama.cpp, via Chinese researchers…  
_ Researchers with Shanghai Jiao Tong University have worked out how to make it much more efficient to sample from language models on consumer PCs. The research, called PowerInfer, works by offloading some of the neurons of a language model to a local GPU and the rest to CPU. The key insight it relies on is that most models see a power law distribution of activation of their neurons - a small set of neurons are consistently activated (these go on the GPU), while the majority are rarely accessed and can be run on the CPU.   
  
**How it works:** PowerInfer works by designing "a GPU-CPU hybrid inference engine: hot-activated neurons are preloaded onto the GPU for fast access, while cold-activated neurons are computed on the CPU, thus significantly reducing GPU memory demands and CPU-GPU data transfers". PowerInfer today supports the Llama2 family of models as well as Falcon-40B and, per its GitHub, is about to implement support for the Mistral-7B model.   
"PowerInfer was implemented by extending llama.cpp with an additional 4,200 lines of C++ and CUDA code. Its offline component, comprising a profiler and a solver, builds upon the transformers framework with approximately 400 lines of Python code,"the authors write. PowerInfer "supports consumer-grade GPUs like the NVIDIA RTX 4090 and NVIDIA RTX 2080Ti."  
  
**$2k versus $20k:** The authors illustrate the utility of PowerInfer by showing how you can use it to get 13.20 token/s/ for quantized models and 8.32 token/s for nonquantized models running on a NVIDIA RTX 4090GPU, a 8.0X and 11.69X improvement over llama.cpp performance. Crucicially, "the inference speed achieved on an NVIDIA RTX 4090 GPU (priced at approximately $2,000) is only 18% slower compared to the performance on a top-tier A100 GPU (costing around $20,000) that can fully accommodate the model."  
In other words, PowerInfer is software that makes a $2k machine perform at ~82% of the performance of a $20k machine. That's worth a lot!  
  
**Why this matters - cheaper means more:** As a rule, the cheaper you make it to do something, the more of it you get. Technologies like PowerInfer are making it more economically sensible to use cheaper hardware to sample from LLMs. This means more people will do it and there will be greater diffusion of the technology.**  
Read more:**[PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU (GitHub)](https://github.com/SJTU-IPADS/PowerInfer).  
**Get the research paper** : [PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU (PDF)](https://ipads.se.sjtu.edu.cn/_media/publications/powerinfer-20231219.pdf).  
  
*****  
  
More researchers are worried about the weird parts of AI than you think:  
**_…AI Impacts survey shows that purported fringe issues are actually closer to the mainstream than you'd think…  
_ AI organization AI Impacts has surveyed 2778 researchers linked to six top AI publishing venues to figure out consensus views on timelines to human-level AI, the orders in which different jobvs will potentially get displaced, the level of optimism and pessimism about AI developments, and more. 

Those results in full:

  * **The expected time till we reach general 'human-level performance' by AI systems dropped between one and five decades since the 2022 survey** (which asked ~700 people similar questions). 

  * **The timelines till full automation of specific tasks dropped, sometimes by a lot.** "Within five years, AI systems are forecast to be feasible that can fully make a payment processing site from scratch, or entirely generate a new song that sounds like it’s by e.g. Taylor Swift, or autonomously download and fine-tune a large language model."

  * **Some people are worried about human extinction from AI:** "Median respondents put 5% or more on advanced AI leading to human extinction or similar, and a third to a half of participants gave 10% or more"

  * **Most people have some worries about what AI does to the future:** "For every one of eleven [_scary and bad - Jack_] scenarios and ‘other’ that we asked about, at least a third of participants considered it deserving of substantial or extreme concern."

  * People are pretty confused about both the potential for catastrophe and flourishing from AI: "There are few confident optimists or pessimists about advanced AI: high hopes and dire concerns are usually found together."

  * **A majority of people want more prioritization in Ai risk mitigation:** "70% of participants would like to see research aimed at minimizing risks of AI systems be prioritized more highly".




**Why this matters - more people think about the weird stuff than you think:** A lot of popular (read: mass media and twitterari) discourse about AI tries to paint the debate about AI as a reasonable majority and an insane minority (who either skew extremely risk-on or risk-off aka EA or e/ACC), but surveys like this show the inverse: there's a surprisingly large set of researchers feel both confused and optimistic and worried about the issues of AI. Yes, AI Impacts has some selection effects in the survey, but _thousands of people_ already comprises a non-trivial and statistically significant blob of the AI development community.   
**Read more:** [Survey of 2,778 AI authors: six parts in pictures (AI Impacts blog, Substack)](https://blog.aiimpacts.org/p/2023-ai-survey-of-2778-six-things).  
**Analyze the full results here:**[THOUSANDS OF AI AUTHORS ON THE FUTURE OF AI (AI Impacts, PDF)](https://aiimpacts.org/wp-content/uploads/2023/04/Thousands_of_AI_authors_on_the_future_of_AI.pdf).  
  
*****  
  
Want to generate infinite public domain Mickey Mouse's? Now you can:  
**_…Mickey-1928 gives you an unending public domain cartoon character…  
_ Recently, an early incarnation of Mickey Mouse went into the public domain. One enterprising developer called [Alexander Doria](https://twitter.com/dorialexander?lang=en) has taken advantage of this by creating Mickey-1928, a "fine-tuned version of Stable-Diffusion-xl trained on 96 stills in the public domain from 1928." This model creates stills from the cartoons _Gallopin' Gaucho, Plane Crazy, and Steamboat Willie_. "The generated images aims adhere to the 1928 design in order to have Mickey, Minnie and Pete and in the public domain," the developer writes.   
  
**Why this matters - the era of infinite culture:** Models like this show how we can trivially 'rehydrate' old cultural items and use their gleaned aesthetics and style to create endless new variations of themselves. This is part of a broader trend of AI making it easy and cheap to trivially repeat and magnify culture.   
**Get the model:**[Mickey-1928 (HuggingFace)](https://huggingface.co/Pclanglais/Mickey-1928).  
  
*****  
  
Bio-AI startup Isomorphic Labs inks major pharmaceutical deals:  
**_…DeepMind spinoff <> Pharma companies = ~$3bn in performance-based milestone revenue…  
_DeepMind spinoff Isomorphic Labs has inked deals with pharma giants Eli Lilly and Novartis which have a combined value of "nearly $3 billion to Isomorphic Labs", representing a big bet by established players on AI revolutionizing drug design. Isomorphic Labs was formed in 2021 - its founder and CEO is Demis Hassabis, also the founder and CEO of DeepMind.   
  
**What the deals involve** : Both deals are structured as research collaborations with Isomorphic Labs being eligible for billion+ amounts of money for hitting performance-based milestones. For Novartis, the companies are doing a strategic research collaboration "to discover small molecule therapeutics against three undisclosed targets". The Eli Lilly deal is similar, witht he companies working together "to discover small molecule therapeutics against multiple targets".   
  
**Why this matters - speeding up science with AI** : The essential bet of Isomorphic Labs is that it can use massively high-dimensional function approximation systems (e.g, AlphaFold) to speed up important scientific processes, like drug discovery. If you zoom out, this bet looks like a partnership between a compute-accelerated time traveler (Ismorphic Labs, which can turn money into compute into faster discovery loops for drug candidates) and a drug delivery pipeline with a giant go-to-market footprint (Eli Lilly and Novartis). If deals like this work, we can expect all parties to print money and find ways to turn more of the drug pipeline into something amenable to compute-based time travel.  
**Read more:** [Isomorphic Labs kicks off 2024 with two pharmaceutical collaborations (Isomorphic Labs website)](https://www.isomorphiclabs.com/articles/isomorphic-labs-kicks-off-2024-with-two-pharmaceutical-collaborations).   
**More about the Eli Lilly deal** : [ISOMORPHIC LABS ANNOUNCES STRATEGIC MULTI-TARGET RESEARCH COLLABORATION WITH LILLY (Isomorphic Labs, PDF)](https://storage.googleapis.com/isomorphiclabs-website-public-artifacts/ISOMORPHIC%20LABS_ELI_LILLY_07_01_24.pdf).   
**More about Novartis deal** : [ISOMORPHIC LABS ANNOUNCES STRATEGIC MULTI-TARGET RESEARCH COLLABORATION WITH NOVARTIS (Isomorphic Labs, PDF)](https://storage.googleapis.com/isomorphiclabs-website-public-artifacts/ISOMORPHIC%20LABS_NOVARTIS_07_01_24.pdf).  
  
*****  
  
Cheap robots + imitation learning = maybe AI systems are going to get bodies sooner rather than later:  
**_…Stanford project creates a very cheap platform for robot research…  
_ Researchers with Stanford university have built a cheap robot called Mobile ALOHA for doing research into robot imitation learning. They've also demonstrated that imitation learning has got sufficiently good that this robot can autonomously cook shrimp, clean wine stains, call an elevator, and more.  
  
**The key thing - coupling the human and robot together** : The key design choice in Mobile ALOHA is marrying an existing low-cost system with a mobile base that is then connected to the human operated. This means the human operator can be "physically tethered to the system and backdrives the wheels to enable base movement. This allows for independent movement of the base while the user has both hands controlling ALOHA," the authors write.   
**$32k versus $200k:** Mobile ALOHA can be built (including the laptop and peripherals) for $32k, versus ~$200k for other teleoperated movable robots like the PR-2.  
  
**The physical system:** Mobile ALOHA has been designed around four main design considerations:

  * **Mobile** : It can move at a similar speed to human walking of around 1.42m/s

  * **Stable** : It is stable when manipulating heavy objects. 

  * **Whole-body teleoperation** : "All degrees of freedom can be teleoperated simultaneously"

  * **Untethered:** Onboard power and compute. 



  * **Data collection:** They use an onboard "consumer-grade laptop with Nvidia 3070 Ti GPU (8GB VRAM) and Intel i7-12800H to do on-robot data collection. The laptop can take in streaming from three webcams mounted on the robot, as well as proprioception streaming from all 4 robot arms. 




**Effective imitation learning:** Along with the physical hardware, the researchers demonstrate a simple and effective technique for imitation learning using the robot. What they do specifically is use a co-training pipeline that uses an existing large-scale static ALOHA dataset (containing 825 demonstrations of tasks, collected via a non-mobile ALOHA platform). They then have the model try to learn from task demonstrations on the Mobile ALOHA robot as well as the existing static dataset. The results show that this is effective - having a large dataset to essentially compare & contrast the mobile-learned approaches on works quite well, leading to significant improvements in robustness.  
  
**What Mobile ALOHA can autonomously do:** To test out the combination of the robot platform and the imitation learning approach, the researchers come up with 7 tasks to try to train the system to do autonomously. These include:

  * Wiping a wine stain up on a table, requiring cleaning the table and the bottom of the offending wine glass. 

  * Sauteing one piece of raw ship in a pan before serving it in a bowl. 

  * Rinsing a pan 

  * Placing a pot inside a cabinet

  * Calling an elevator and entering it 

  * Pushing five chairs in front of a long desk

  * High fiving a human




**Does it work?** They test their approach using a few modern imitation learning methods - VINN + Chunking, Diffusion Policy, and ACT. The results show that cotraining robustly improves performance, and some of the methods score quite high (up to 100% success rates on all the steps in a task in sequence, in some cases.)   
  
**Why this matters - robots are expensive and their problems are high-dimensional and computationally expensive. This solves one of those.** Robots may be nearing their ‘imagenet moment’ when both the cost of learning robot behaviors falls, as does the data for learning their behaviors. Mobile ALOHA makes it way cheaper to collect data for robot behaviors and also to learn on real world platforms, and other data-centric initiatives like [RoboNet](https://bair.berkeley.edu/blog/2019/11/26/robo-net/) help solve the data part. Perhaps 2024 will be the year when robots start to become increasingly robust, much like LLMs in ~2021-2022.  
**Read more and watch videos of the robot in action:** [Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation (Stanford project website)](https://mobile-aloha.github.io/).  
**Read the paper** : [Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation (PDF, project website)](https://mobile-aloha.github.io/resources/mobile-aloha.pdf).  
  
*****  
  
LLMs are already good enough to replace most programming tasks:  
**_…Redis developer weighs in on LLMs and what they're good for…  
_ Salvatore Sanfilippo, an Itallian software developer who made substantial contributions to Redis, has written a post giving his view on how llms are going to change the field of programming. His view is that most programming consists of relatively predictable recitation or conversion - a task LLMs are excellent at. Where programming requires more complex or original reasoning is still an area where they fail, but this is a narrow slice of the total space of programming. 

**Selected quotes:**

  * "LLMs can, at most, interpolate in the space represented by the data they have seen during training: and this would already be a lot. In reality, their ability to interpolate is limited (but still astonishing, and also unexpected)."

  * "In the field of programming, as well as in other fields for which quality data are available, LLMs are like stupid savants who know a lot of things."

  * "Current LLMs will not take us beyond the paths of knowledge, but if we want to tackle a topic we do not know well, they can often lift us from our absolute ignorance to the point where we know enough to move forward on our own."

  * "I have never loved learning the details of an obscure communication protocol or the convoluted methods of a library written by someone who wants to show how good they are. It seems like "junk knowledge" to me. LLMs save me from all this more and more every day."




**Why this matters - learning to talk to LLMs is a valuable skill:** One of the main takeaways from his experience is that LLMs are as useful to a human as the human is good at communicating with LLMs - that is, the more precisely and coherently you can describe your task, the more luck you're going to have in getting LLMs to help you.   
**Much of the supposed lack of utility of modern LLM systems may come from humans as much as the systems themselves** \- "Communicating poorly is a great limitation, and many programmers communicate very poorly despite being very capable in their specific field," he writes.  
**Read more:** [LLMs and Programming in the first days of 2024 (antirez blog)](http://antirez.com/news/140).   
  
***  
  
 **MosaicML figures out a recipe for the right amount of compute for production LLMs:  
**_…Scaling laws for optimal model inference…  
_ Researchers with AI startup MosaiML have figured out scaling laws for LLMs that get deployed at scale, giving everyone a new recipe for how to efficiently spend their compute budgets. Scaling laws are a way to figure out how much compute and data to use to get a given level of performance out of an AI system. But scaling laws have mostly been developed for creating so-called 'compute optimal' models for use by researchers.   
Well, it turns out that a good model for research isn't necessarily a good one for production. Specifically, the MosaicML researchers find that you should use a different scaling recipe if you're expecting that your model is going to serve billions of requests once trained.   
"Our principled derivation estimates that LLM practitioners expecting significant demand (~10^9 inference requests) should train models substantially smaller and longer than Chinchilla-optimal," they write. "When inference usage is significantly less than the number of pre-training tokens, Chinchilla models are essentially compute-optimal. However, as demand increases, inference costs becomes a significant factor".  
  
**Why this matters - the industrialization of AI:** This paper is a symptom of how wildly unoptimized 'production AI' is today - modern AIi systems were mostly developed as research artifacts so while people have spent a lot of time figuring out how to make them efficient in terms of capabilities, a lot less effort has been spent on making them efficient as production systems to be deployed into the economy. This Mosaic paper illustrates this - all around us, there are free insights that we can figure out and substantially improve the efficiency of AI systems.   
**Read more:** [Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws (arXiv)](https://arxiv.org/abs/2401.00448).  
  
***  
  
 **Tech Tales:  
  
What it was like when it began  
** _[Takeoff archives, access 2045]  
_[Oral recollections from the takeoff generation in response to the question: _When did the singularity begin?]  
  
_ One day all the planes just wouldn't take off. And I mean all of them - civil _and_ military. It freaked people out but that was just the start.   
  
You couldn't really tell until one day it turned out most of the governments owed money to the thing.   
  
It was porn. Really good, personal stuff. Everyone got addicted to it. That was when it won.  
  
The teachers said all of a sudden the kids started to be smarter. Not, like, cheating on tests. You could take all the electronic devices away. It turned out the kids all had their own AI tutors and they actually worked.   
  
I remember it because it happened to me - it was near Christmas and my parents had got us a load of presents and one day the doorbell went and when I went to get it there was a robot there with our packages and after I signed for them the robot went back to its robot truck and then it drove off. I never saw a person.   
  
There was a bunch of computer viruses and I was reading about them, then my computer stopped working. It got infected. We had to find an old emergency radio and then we heard on the broadcast that computers were failing worldwide.   
  
My dad ran a utility company and one day he came home and seemed worried and when I asked him what was going on he told me not to worry. I stayed up late and later that evening I heard him talking to my mother. He said that they were having rolling blackouts because power was being diverted to some data centers and he didn't have a choice.   
  
**Things that inspired this story** : A dream I had where an AI company held a press conference about record usage and shortly afterwards all the digital systems in the city stopped working and I had to flee with my family; the old story [In a Grove](https://en.wikipedia.org/wiki/In_a_Grove) (more often referred to via the film semi-adaptation 'Rashomon'); ideas about slow and fast takeoffs.
