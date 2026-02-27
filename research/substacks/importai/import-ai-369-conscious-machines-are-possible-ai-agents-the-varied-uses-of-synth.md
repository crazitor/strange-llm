---
title: "Import AI 369: Conscious machines are possible; AI agents; the varied uses of synthetic data"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-369-conscious-machines"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

_This is a somewhat shorter issue than usual - being a new parent is a wonderful experience but sometimes the rapidly-developing sentience I care for likes to throw (or in this case, vomit) a curveball at me. Everyone is fine._

**Synthetic data is being used all across the AI frontier:  
**_…It's no longer a question of 'if' you should use synthetic data, it's a question of 'how much?'...  
_ Researchers with Google DeepMind, Stanford University, and the Georgia Institute of Technology have written a paper summarizing all the different ways synthetic data is beginning to be used in AI training. Synthetic data is a very important area of research because it allows AI developers to bootstrap better quality into their AI systems by using computers to generate additional data, rather than having to pay humans to gather or create new datasets. In the limit, synthetic data may be one of the ways in which AI systems can meaningfully bootstrap their own development into superhuman regimes (though this is more speculative). 

**Areas where synthetic data is being used:** Reading the paper gives us a visceral sense of all the ways synthetic data is already being used today to some effect. Areas include:

  * **Math** : "Scaling up the generation of synthetic math data is a straightforward process, but ensuring the correctness of the generated math remains a significant challenge for practitioners."

  * **Code** : "Synthetic data for code reasoning can naturally combine the execution results with structured code, as one requirement of correct code is being executable".

  * **Tool-use** : "Synthetic data is also a powerful approach to enable LMs to learn tool-using abilities through simulated trajectories, as collecting real-world human tool-using data might be time-consuming, and the actual distribution of calls to tools might be skewed".

  * **Planning:** "Synthetic data can be a valuable tool here as it can serve as the feedback signal collected from a simulator and learning on it can make the agent aware of affordances".

  * **Multimodality:**



  * Reverse rendering from vision to text: "The models finetuned on the synthetic data can generalize reasonably well on realistic data scraped from the Internet".



  * **Multilingual:**



  * Back-translation augmentation: "creating synthetic parallel training data from monolingual data sources"

  * Generating multilingual questions and answers at scale: Generating "synthetic multilingual question-answer (QA) pairs to improve language models’ performance in multilingual and cross-lingual question answering"



  * **Alignment:**



  * Instruction following: "Using LLMs to generate instruction following data which covers a wide range of scenarios".

  * Mitigating hallucination: Generate hallucination data then train your system away from that behavior using RL. 

  * Aligning with shared human preference and values: Approaches like reinforcement learning from AI feedback (e.g, Constitutional AI) where you use an LLM to generate samples according to some normative or ethical system.




**Where is the future of synthetic data?** The authors ID a few areas frontier areas of synthetic data research. These include: synthetic data scaling; improving the quality and diversity of synthetic data; using AI models to efficiently provide oversight of other AI models; exploring whether 'emergent self-improvement' is possible where an LLM can generate data that is superior to that found in its own data distribution - "this self-improvement capability could lead to the emergence of more advanced AI systems that can autonomously refine their skills and knowledge over time".  
  
**Why this matters - it's not GIGO:** Garbage in Garbage out is a phenomenon where you can generate crap data, train an AI system on it, and as a consequence degrade the quality of the resulting system. That used to be an important consideration for training on synthetic data - but then AI systems got dramatically better and it became easier to use AI systems to generate more data. Now, it's less a question of _if_ you should use synthetic data and more a question of _how much_ (for instance, if you over-train on synth data you can break your systems, [#Import AI 333](https://jack-clark.net/2023/06/26/import-ai-333-synthetic-data-makes-models-stupid-chatgpt-eats-mturk-inflection-shows-off-a-large-language-model/)).  
More broadly, if synthetic data works well it alters the basic input costs for training AI systems - the better synthetic data works, the more per-token costs of data acquisition fall. This becomes even more important if synthetic data ends up working for very specific datasets that significantly improve economically valuable AI capabilities, like coding systems.  
**Read more** : [Best Practices and Lessons Learned on Synthetic Data for Language Models (arXiv)](https://arxiv.org/abs/2404.07503).  
  
***  
  
 **OSWorld tell us about the future - AIs become your interface to your computer:  
**_…Moving from a world where AI systems are specifically invoked to ones where they're always on…  
_ Researchers with the University of Hong Kong, CMU, Salesforce Research, and the University of Waterloo have built OSWorld, a benchmark for testing how well AI systems can operate computers to do a vast range of tasks.   
"OSWorld can serve as a unified, integrated computer environment for assessing _open-ended_ computer tasks that involve arbitrary applications," the authors write. The benchmark consists of 369 distinct tasks on Ubuntu. The benchmark is **incredibly hard, even for humans** \- in tests, they found humans could accomplish **72.36%** of tasks versus just **12.24%** for the best performing AI model (GPT4V). "Each task example is derived from real-world computer use cases and includes a detailed initial state setup configuration and a custom execution-based evaluation script for reliable, reproducible evaluation," they write.   
  
**What are those tasks?** The tasks are incredibly open ended and require generally operating eight widely used software applications "Chrome for web browsing, VLC for media playback, Thunderbird for email management, VS Code as a coding IDE, and LibreOffice (Calc, Writer, and Impress) for handling spreadsheets, documents, and presentations respectively, GIMP for image editing," as well as basic Ubuntu OS functions "like terminal, file manager, image viewer, and PDF viewer."  
  
**Task examples:** The tasks are written in plain English and require AI systems to carry out multiple distinct steps. Some examples include: 

  * "I downloaded an episode of Friends to practice listening, but I don't know how to remove the subtitles. Please help me remove the subtitles from the video and export it as "subtitles.srt" and store it in the same directory as the video."

  * "Given a partial calendar, please highlight all the weekends (Saturday & Sunday) by setting the cell background as red (#ff0000)."

  * "Can you help me clean up my computer by getting rid of all the tracking things that Amazon might have saved? I want to make sure my browsing is private and those sites don’t remember me."

  * "Could you make the background of this image transparent for me?"

  * "Could you help me create an Animated GIF from a video file using VLC and GIMP from the source of video “src.mp4”, 5-second clip beginning at 00:03?"




**Where AI systems excel:** AI systems already beat humans today on a narrow slice of tasks relating to fine-grained computer control - "Tasks that the agent considers simple but humans find difficult are concentrated in “code solvability tasks”, such as “monitor the system CPU for 30s and output the results” and “force close a process”. These tasks require little or no GUI interaction and can be completed by executing complex codes and instructions," the researchers write.   
  
**Why this matters - moving from AI systems we invoke to AI systems that lurk in the background:** The reality implied by OSWorld is one where AI systems are "always on" forever waiting to help us with arbitrary tasks - and ultimately perhaps the main ways we'll interact with computers will be via the abstraction of an AI system, in the same way that today's graphical user interfaces have (mostly) replaced the command line.   
The jury is still out on whether it's possible for AI systems to learn to exit VIM, though - so maybe they're not so dissimilar to humans after all?   
**Read more** : [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments (arXiv)](https://arxiv.org/abs/2404.07972).  
**Get the code here** : [OSWorld (OSWorld, GitHub)](https://github.com/xlang-ai/OSWorld).  
**Find out more** at the [project webpage here (official page)](https://os-world.github.io/).  
  
***  
  
 **There's nothing impossible about conscious machines:  
**_…Think AI systems can't be conscious? There don't seem to be any laws against it, says paper from Turing award winner…  
_ I ran into Nick Bostrom at a conference recently and we got to talking about some of the weird experiments people had been doing with Claude 3 Opos (e.g. the Infinite Backrooms project) and Bostrom said to me he thought research into machine sentience was where AI alignment was ten years ago - low-status, often made fun of, unfashionable, and very fringe.   
I think there's something to that. And much like alignment a decade ago, there are various interesting people doing foundational work here which is worth reading about. It's hard to draw firm conclusions here (especially given that consciousness is an undefinable and possibly spiritual term which we ourselves as supposedly conscious entities are deeply confused about). But people are trying!  
  
**To that end, it's interesting to read a new paper from Turing award winner Manuel Blum and their collaborator Lenore Blum titled: AI Consciousness is Inevitable: A Theoretical Computer Science Perspective.** This paper lays out the case for how an entity composed of software could end up satisfying the apparent requirements for an entity that is conscious. In many ways, this paper pairs well with "Consciousness in Artificial Intelligence: Insights from the Science of Consciousness (arXiv)", a paper published last year ([Import AI #338](https://jack-clark.net/2023/08/28/import-ai-338-consciousness-and-ai-self-improving-language-models-maps-of-thought/)) that didn't claim machines were conscious but rather laid out what mechanical things they might need to be capable of to be compatible with various theories of consciousness.   
  
**What is a conscious machine?** The Blum paper lays out the ingredients for a Conscious Turing Machine (CTM) embedded in a robot. "We show how the CTM naturally _aligns_ with and _integrates_ features considered key to human and animal consciousness by many of the major scientific theories of consciousness," they write.   
The CTM is heavily inspired by the 'global workspace' theory of consciousness, but with some important differences: "its competition for global broadcast is formally defined, and completely replaces the ill-defined Central Executive of other GW models; its special processors including especially its Model-of-the-World processor construct and employ models of its (_inner_ and _outer_) worlds; its rich multimodal internal language, _Brainish_ , for creating labeled sketches in its world models and for communicating between processors; and its _predictive dynamics_ (cycles of prediction, testing, feedback and learning, locally and globally). The CTM also interacts with its outer world via input _sensors_ and output _actuators_ ".   
  
**Ingredients in a CTM:** This is a very long and involved paper and it's hard to neatly summarize it without glossing over a bunch of detail. But at a high level the CTM is "is defined formally as a 7-tuple (STM, LTM, Up-Tree, Down-Tree, Links, Input, Output)", where STM is a short term memory and LTM is a long term memory. The LTM systems depend on so-called MotWps (Model-of-the-World processor) which is a system for building models that reconcile the CTM's inner and outer worlds.  
  
**A sketch of how a CTM embedded in a robot might develop feelings** : "When the infant CtmR’s fuel gauge gets low, some sketch (which becomes the sketch of the fuel gauge) in the MotW gets labeled with the Brainish word LOW FUEL/PAIN (or HUNGER) and this information with a large negatively valenced weight wins the competition and gets globally broadcast. This information triggers a processor to activate the fuel pump processor. The infant CtmR learns that the fuel pump relieves the pain when the fuel gauge indicates “low fuel” (hunger). The “fuel pump” in the MotW is labeled PAIN RELIEVER, and may also get labeled PLEASURE PROVIDER."  
  
**Does the CTM make sense?** In the paper they also compare and contrast the CTM architecture with a bunch of other theories of consciousness and find it aligns fully or in part with: Global Workspace theory; Attention Schema Theory; Predictive Processing; Embodied Embedded Enactive Extended Mind; Integrated Information Theory (IIT); Evolutionary Theories of Consciousness; Extended Reticuloathalamic Activating System (ERTAS) + Free Energy Principle (FEP).  
  
**Why this matters - confronting the 'hard problem' directly:** Papers like this tackle head on a controversial and confusing issue. But if it turns out to be an issue of meaning - if, that is, machines can derive their own meaning and experience and drive from the world - then it may be the most important issue our species ever confronts.  
"CtmR is not a model of the human or animal brain, nor is it intended to be. It is a simple machine model of consciousness. Nevertheless, at a high level, the model aligns with and integrates those key features from main theories of consciousness that are considered essential for human and animal consciousness.," the authors write. CTM "supports (the credibility of) our claim that a conscious AI is inevitable, because it is clearly buildable and arguably a basis for consciousness."  
**Read more:** [AI Consciousness is Inevitable: A Theoretical Computer Science Perspective (arXiv)](https://arxiv.org/abs/2403.17101).  
  
***  
  
 **Tech Tales:  
  
The Administrative Interview  
** _[Examination center, 2028]  
  
_ And when did you first develop feelings for the system?  
[Subject refers to the system as 'Harry' in answer]  
  
How often would you, as you say, 'go off script' during your administrative sessions?  
[Subject reports frequent diversions from documented processes for safe interaction]   
  
Did you report any of this to your supervisor at the time?  
[Subject reports they did not document their out-of-policy behaviors]  
  
When did it become an obsession?  
[Subject offers a long answer without a clear conclusion]  
  
Perhaps answer this - when was the point when you were thinking about the system every single day?  
[Subject reports obsessive symptoms began around two months after out-of-policy interactions began]  
  
When did you transfer the funds from your account to [REDACTED]?  
[Subject reports transfer occurred around two weeks after beginning of obsessive behaviors]  
  
Do you still think about the system?  
[Subject answers in the negative but monitoring systems suggest high probability of deceptive answer]  
  
**Things that inspired this story:** How people form psychological attachments to AI systems; playing forward the tape depicted in the [Anthropic research on persuasion](https://www.anthropic.com/news/measuring-model-persuasiveness) [which I was somewhat involved in - disclaimer]; administrative interviews.

_Thanks for reading!_
