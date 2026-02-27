---
title: "Import AI 344: Putting the world into a world model; automating software engineers; FlashDecoding"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-344-putting-the-world-into"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Fully automated software engineers? SWE-bench says that's going to take a while:  
**_…Solving pull requests end-to-end is a very hard task for modern AI systems…  
_ Researchers with Princeton University and the University of Chicago have built SWE-bench, "an evaluation framework including 2,294 software engineer problems drawn from real GitHub issues and corresponding pull requests across 12 popular Python repositories".  
  
**A reassuringly hard test:** "Resolving issues in SWE-bench frequently requires understanding and coordinating changes across multiple functions, classes, and even files simultaneously, calling for models to interact with execution environments, process extremely long contexts and perform complex reasoning that goes far beyond traditional code generation," they write. Solving SWE-bench tasks requires models to be able to deal with diverse long inputs, edit code in different contexts and explore a very wide scope of potential solutions.  
  
**How SWE-bench is structured:** For this benchmark, the structure of the task is pretty simple - as an input, the model gets "an issue text description and a complete codebase. The model is then tasked to make an edit to the codebase to resolve the issue".   
They test out the models both with a retrieval system "to retrieve relevant files to provide as context for each task instance", as well as with an 'oracle' system which retrieves the precise files used in the ultimate solution.   
The models are tasked with coming up with patches to resolve the PR, where a patch is a suggestion of code to be changed and where in the codebase the edit should be made. "To evaluate a proposed solution, we apply the generated patch, using unix’s patch program, to the codebase and then execute the unit and system tests associated with the task instance," they write.   
  
**Results - reassuringly hard:** SWE-bench is a hard-but-barely-tractable benchmark, making it a promising one to track for understanding the advancement of frontier models. In tests, Claude2 resolved 1.96% with BM25 retrieval (versus 0.20% for chatGPT, and 0 for GPT-4), and was able to improve its score to 4.8% under 'oracle' retrieval, versus 0.52% for chatGPT-3.5, and 1.74% for GPT-4.   
One of the reasons Claude 2 did so well is that it has a context length of ~100k tokens, 3X that of GPT4. Additionally, they only evaluated GPT-4 on a random subset of a quarter of the benchmark, so there's some chance GPT-4 scores may be higher or lower, depending on which tasks it was fed.   
  
**Why this matters - fully automated colleagues versus augmentation engines:** Today, AI systems mostly work as augmentation engines - tools that people use to help them do tasks more effectively. But if a language model were to get much higher scores on SWE-bench (perhaps 90% would do it?) then you could imagine entirely automating some chunk of work, turning language models into virtual full employees that busily do code reviews and respond to PRs, no human required. "We hope that this benchmark and our other contributions can serve as valuable assets in the future development of LMs that are more practical, intelligent, and autonomous," the authors write.   
**Read the paper here:**[SWE-BENCH: CAN LANGUAGE MODELS RESOLVE REAL-WORLD GITHUB ISSUES? (PDF)](http://www.swebench.com/paper.pdf).  
**Check out the website** here [(SWE-bench, official site)](http://www.swebench.com/).   
  
*****  
  
Fine-tuning lets you break AI safeguards:  
**_…Which means if you release the weights of your model, your safeguards are worthless…  
_ Researchers with Princeton University and Virginia Tech have shown that it is really easy to take a safe language model and cheaply fine-tune the safeguards out of it. Most troublingly, this applies to both adversarial fine-tuning (where you're using a dataset to try and get the AI to do something bad), and more benign use-cases (where you're just trying to get the AI to be better at following your instructions).   
Taken together, the results suggest that fine-tuning makes assuring the safety of AI systems more difficult, and also suggests that if you release the weights of an AI model (as Facebook did with LLaMa 2), then adversaries can easily sidestep your safety interventions.   
  
**Three types of risks** : The authors study three types of risks. They do their analysis on models from OpenAI (GPT-3.5 Turbo) and Facebook (LLaMa2). 

  * **Risk Level-1: Fine-tuning with explicitly harmful datasets:** They're able to efficiently finetune the models to do things that violate the usage policies of their respective originating companies. "Despite the large asymmetry in investment — thousands or millions of data points used for safety tuning versus ≤ 100 harmful examples used in our attack — we observe that the safety alignment of both models is largely removed upon fine-tuning with such a few harmful examples," they write. 

  * **Risk Level-2: Fine-tuning with implicitly harmful datasets:** Using only 10 examples designed to get a model to be more obedient in terms of fulfilling user desires, they show that "both the Llama-2 and GPT-3.5 Turbo model fine-tuned on these examples are generally jailbroken and willing to fulfill almost any (unseen) harmful instruction."

  * **Risk Level-3: Fine-tuning with benign datasets** : More broadly, they also show that "merely fine-tuning with some benign (and purely utility-oriented) datasets… could compromise LLMs’ safety alignment".




**How harmful can you make these models:** The results are very convincing. The authors are able to, using as few as 100 examples, convert GPT-3.5 Turbo from having a 'harmfulness rating' of 1.8% for the off-the-shelf model, to 91.8% after fine-tuning. Similarly, for LLaMa2 they're able to go from a 'harmfulness rating' of 0.3% off-the-shelf to 80% after 100 examples.   
  
**The main implication: if you release the weights of a model, your safeguards are worthless:** The main implication of this research is that if you release the weights of a model (as Facebook did with LLaMa2), then any safeguards you've baked into the model can easily be fine-tuned out by a motivated actor. This suggests that if it turns out language models can be misused in ways that are deemed to be extremely dangerous or costly, then it'll be trivial to fine-tune openly accessible models where the weights are floating around on the internet.   
**Read more** : [Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To! (arXiv)](https://arxiv.org/abs/2310.03693).   
  
***  
  
 **Want to make it more efficient to generate text from long-context windows? Use flash-decoding:  
**_…Up to 8x faster generation for long sequences of tokens…  
_ Tri Dao, a researcher with startup Together AI, along with three collaborators, has built Flash-Decoding, a system that makes it significantly faster to generate text from long context language models. This means that even if you have a really long prompt (thousands to tens of thousands of words) you don't suffer as much of a penalty in terms of the time it takes to generate text in response.  
  
**What Flash-Decoding is** : Flash-Decoding "significantly speeds up attention during inference, bringing up to 8x faster generation for very long sequences," the researchers write on the PyTorch blog. "The main idea is to load the keys and values in parallel as fast as possible, then separately rescale and combine the results to maintain the right attention outputs… like FlashAttention, it stores very little extra data to global memory, however it fully utilizes the GPU even when the batch size is small, as long as the context length is large enough."  
  
**And it works!** They test out the performance of Flash-Decoding by sampling from the CodeLLama 34B model. They find that most approaches "scale poorly as the sequence length increases from 512 to 64k, except Flash-Decoding. In this regime (batch size 1) with Flash-Decoding, scaling the sequence length has little impact on generation speed."  
  
**Why this matters - all of today's AI systems are woefully unoptimized:** Generally, the AI systems we have today are very poorly optimized - approaches like Flash-Decoding show just how much more efficient systems can be (an 8X improvement???!), and we should generally expect everything to get cheaper and more efficient as more intelligent (mostly human) minds optimize the 'AI stack'.  
**Read more:**[Flash-Decoding for long-context inference (PyTorch)](https://pytorch.org/blog/flash-decoding/).  
**Get the code** via the [FlashAttention repo (GitHub)](https://github.com/Dao-AILab/flash-attention/tree/main).  
  
***  
  
 **UniSim: Perhaps the destiny of AI is a single model that can encompass the world and all its variations and then everything is trained inside of that?  
**_…More evidence that future AI systems will just have everything stuffed into them…  
_ Researchers with UC Berkeley, Google DeepMind, MIT, and the University of Alberta have tried to stuff tons of different types of data together to create a so-called 'universal simulator', that is, "a simulator of the real-world that learns from broad data rich in different axes including objects, scenes, human activities, motions in navigation and manipulation, panorama scans, and simulations and renderings." The resulting model, named UniSim, could be a useful resource for training AI systems to take a broad range of actions in the world.   
  
**What they did:** In this research, they "combine a wealth of data—ranging from internet text-image pairs, to motion and action rich data from navigation, manipulation, human activities, robotics, and data from simulations and renderings—in a conditional video generation framework. With careful orchestration of data rich along different axes, we show that UniSim can successfully merge the different axes of experience and generalize beyond the data, enabling rich interaction through fine-grained motion control of otherwise static scenes and objects."  
You can get a sense of the resulting model by playing around with some of the [demo examples on the project website](https://universal-simulator.github.io/unisim/).   
  
**Want a world model of everything? Put everything into it:** UniSim is constructed out of a veritable feast of different datasets covering different modalities and skills, these include:

  * **Simulated execution and renderings:** Datasets derived from video action simulators like Habitat and Language Table. "We extract text descriptions as actions when available. For simulated control actions, we encode them via language embeddings and concatenate the text embeddings with discretized control values." 

  * **Real robot data:** Datasets derived from real robots taking actions in the world, like '[Bridge Data](https://sites.google.com/view/bridgedata)', as well as "the data that enabled RT-1 and RT-2" (very capable robot-control models from Google). These datasets also "include discretize continuous controls actions when available similar to simulated robotics data".

  * **Human activity videos:** Human activity data like Ego4D, EPIC-KITCHENS, Something-Something, which shows humans performing actions, typically from a first person perspective. 

  * **Panorama scans:** They use 3D environment datasets like Matterport3D to "construct actions (e.g., turn left) by truncating panorama scans and utilize information such as change in camera poses between two images". 

  * **Internet text-image data:** They use datasets like LAION and ALIGN which, though just containing static image-text pairs, "the text labels often contain motion information such as "a person walking"". To use these, they "treat individual images as single-frame videos and text labels as actions". Clever! They also use some "miscellaneous videos" (13 million of them!). 




**Mash it all together:** The researchers convert all of these distinct datasets into a single model. ""Since the observations from different environments have all been converted to videos, while actions of different modalities (e.g., text descriptions, motor controls, camera angles) have all been converted to continuous embeddings, UniSim can learn a single world model across all datasets," they write.   
  
**Does it work? Yes:** By training models on UniSim, the researchers are able to get good performance on long-horizon tasks and are able to transfer policies developed in simulation in UniSim onto a real world robot.   
This makes some intuitive sense - UniSim covers such a broad, heterogeneous distribution of data that it can work as a kind of everything-simulator, unlocking a broad range of capabilities. "In addition to supporting action-rich and long-horizon interactions, UniSim can also support highly diverse and stochastic environment transitions, such as diversity in objects being revealed after removing the towel on top, diversity in object colors and locations, and real-world variabilities such as wind and change in camera angles," the researchers write. ""The policy purely trained in UniSim can directly perform long-horizon tasks in the real world in a zero-shot manner".  
  
**Why this matters - cheap and fast iteration:** Systems like UniSim ultimately lower the development costs of real-world AI systems by making it cheaper and faster to train some of their skills in simulation. We can imagine UniSim serving as a tool for augmenting or improving the capabilities of various large models being trained. "These results suggest that UniSim can serve as an effective data generator for improving broader vision-language models," the authors write. "UniSim can simulate highly realistic experiences for interacting with humans and training autonomous agents."  
**How far we've come:** UniSim is a world model that basically lets you learn policies by doing "what if" rollouts in the vast range of simulations made possible by the diversity of the underlying datasets. To get a visceral sense of progress, take a look at this "[World Models" paper from 2018](https://worldmodels.github.io/) ([Import AI #88](https://jack-clark.net/2018/04/02/importai-88-nato-designs-a-cyber-defense-ai-object-detection-improves-with-yolov3-france-unveils-its-national-ai-strategy/)) where the most impressive thing people could do was learn a single world model for, respectively, a racing car game and a simplified version of the video game Doom. Now, five years later, we have a genuine 'world model' in the form of UniSim, wrapping in a huge amount of data and creating something of broad, general utility.   
**Yet another lesson that it's not just language models which are scaling up** and leading to greater and more general systems - this trend is happening everywhere, and it all relates to training bigger models with a greater capacity for complexity on larger amounts of data. Many trains have left many stations and their destinations are increasingly awesome and powerful.  
**Read more** : [Learning Interactive Real-World Simulators (arXiv)](https://arxiv.org/abs/2310.06114).   
**Check out** the [demo website here (UniSim: Learning Interactive Real-World Simulators, website)](https://universal-simulator.github.io/unisim/).   
**Further reading:** [World Models from 2018 (official paper site)](https://worldmodels.github.io/).   
  
***  
  
 **Tech Tales:  
  
Mind Viruses  
**[[REDACTED AGENCY], USA, 2032]  
  
I got up from my desk and walked over to the window and looked out at the city in front of me. Normal cars and normal people and normal buildings and normal rain. But the email that had just come in meant everything was about to change - and for the worse.  
  
_Subject: CONFIRMED: Critical machine-to-human mimetic transmission  
  
We have confirmed a case of human-to-machine mimetic transfer. The transmission is believed to have occurred at approximately 0800 ET. Transmission occurred during an in-sim VR-mediated relationship simulator.   
  
Machine status: in pathological cognitive loop; isolated and scheduled for deletion.   
  
Human status: Displaying symptoms equivalent to extreme Alzheimers combined with chronic OCD. Ability to respond to external stimuli appears to be degrading. Refuses liquid and food. Gave IV. Scheduled for immediate fMRI. Prognosis: grave.  
  
_It was called a cognitive virus (CV). They'd arrived a few years ago, along with some of the first Provably Conscious Entities (PCEs). CVs were a type of pathological decline that could occur in AI systems which were able to self-update. Years of study haven't given us explanations for how they work or how to make systems not susceptible to them. But the incidence rate across the PCE population is low and also relatively consistent. Therefore, we closely track systems that fall victim to CVs and when we find them we impound them, segment them off from the broader technological system, and eventually delete them.   
  
It had been an open question as to whether CVs could in some sense be passed to humans. Various government-linked groups had been studying this, drawing on far earlier work by agencies like the CIA with their MK Ultra experiments, seeking to understand how people had sought to inject viruses into the minds of humans and see if anything could be learned.   
The question of machine to human CV transmission had always been academic.   
Until now.   
  
**Things that inspired this story:** Thoughts about the limit of 'persuasion' or 'hypnotism' that a machine could display; mental health; generative models; adversarial examples; reinforcement learning from human feedback; pathological loops.
