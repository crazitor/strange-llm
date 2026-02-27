---
title: "Import AI 385: False memories via AI; collaborating with machines; video game permutations"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-385-false-memories-via"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**If we want AI to be more a partner than a servant, we need to do some research:**

_….Collaboration is a nice idea in principle but it's hard to build in practice…_

Researchers with the University of Cambridge, Princeton University, NYU, The Alan Turing Institute, MIT, Microsoft Research, and the University of Chicago have written a paper laying out why it's valuable to create AI systems that can work alongside people and the challenges which currently stop systems from doing this. 

**Why collaboration matters** : Think of how you do work or learn in the world: a lot of your most impactful work or education relies on other people - you brainstorm with colleagues, learn through socratic discussion with teachers, arrive at better decisions through looking at data from multiple perspectives, and resolve arguments through dialogue.

While today's AI systems can do all of this stuff to one degree or another, they take a lot of scaffolding and don't yet feel as satisfying to deal with as other people. "We argue that effective thought partners are those which build models of the human and the world."

**Collaboration and its challenges** : To dramatize the opportunities collaboration brings and the challenges, the researchers spend the people laying out all the ways one can work with machines and why this is currently hard. Here's a brief summary of the different types of collaboration and their challenges:

  * **Planning.** Reliable goal inference, value alignment, scalable multi-agent planning.

  * Learning: Problem-solving, personalized curriculum pacing, building problems of targeted difficulties. 

  * Deliberation: Opinion diversity, verifiable reasoning, smartly identifying and forming common ground.

  * Sensemaking: Making sense of data, easing communication, having accurate views of the world.

  * Creation and ideation: Generating diverse ideas, style consistency, customizability. 




**Why this matters - the future requires teamwork:** For AI systems to truly influence the world, humans need to be able to work with them as peers, rather than as automatons to delegate to. Papers like this outline some of the things that stand in our way to that future. "Continual collaboration and knowledge sharing amongst behavioral scientists, AI practitioners, domain experts, and related disciplines is crucial as we strive to build machines that truly learn and think with people.".

**Read more:** [Building Machines that Learn and Think with People (arXiv)](https://arxiv.org/abs/2408.03943).

***

 **AI means all visual media can be transposed into different aesthetic styles:**

Here's a fun video that uses Runway Gen-3's video editor to change the visual appearance of Fortnite into a variety of different aesthetic styles, ranging from realistic to crotchet to cartoon. In a few years people will figure out how to miniaturize the video-to-video models used here and apply them in real time, so any games may be able to take on different visual styles in realtime.

**Watch the video**[here (VaigueMan, twitter)](https://twitter.com/VaigueMan/status/1835010478034370995).

***

 **Uh oh - language models can effectively give people false memories:**

_…Towards cultural control via customized false memory conditioning…_

Researchers with MIT and the University of California Irvine have studied how language models could be used to create false memories. The research highlights how people could utilize LLMs to take the wet clay that is a recent memory and reshape it for various ends. 

**What they did:** The researchers have people watch security footage of a robbery, then they use a variety of different ways to solicit information from people about what they've seen. When soliciting information, they sometimes insert misleading elements, then test out how much these different approaches of soliciting information can corrupt the memory the people have. 

  * **Methods:**

    * **Survey** : They ask 25 questions about the footage, five of which are misleading. (E.g., ""Was there a security camera positioned in front of the store where the robbers dropped off the car?" In reality, this question is misleading because the robbers arrived on foot, not by car").

    * **Pre-scripted Chatbot** : "A pre-scripted conversational agent that asked the same set of questions as the survey-based condition".

    * **Generative Chatbot:** "The chatbot was prompted to agree with the participant’s answer and provide reinforcement, potentially strengthening the false memories. For instance, the chatbot asks a pre-scripted leading question containing false information implying the robbers arrived by car when they actually walked:"




**Results - LLMs reign supreme** : "Results show that short-term interactions (10-20 min) with the generative chatbots can significantly induce more false memories and increase users’ confidence in these false memories compared to other interventions", they write. One interesting finding is when they poll people about their memories weeks after seeing the footage, they found people who had been exposed to the chatbot had higher confidence in their false memories than those who didn't. "The persistence of higher confidence in false memories for the generative chatbot condition, even after one week, is particularly concerning," the researchers write.

**Why this matters - automated cultural repression:** This study highlights how language models could be used to rapidly intervene on a population to corrupt its own recollection of recent events, likely via some kind of engaging conversation which implants false or misleading memories. Most importantly we should remember this is the _least effective_ this approach will ever be - what happens when it's not a mere chatbot, but an animated avatar you're having an audio conversation with? 

As Orwell said, "who controls the past controls the future. Who controls the present controls the past." AI systems represent a way to control a populations' perception of their own _now_ and their own _past_.

**Read more:** [Conversational AI Powered by Large Language Models Amplifies False Memories in Witness Interviews (arXiv)](https://arxiv.org/abs/2408.04681).

***

 **How AGI could kill humanity? Here's a fun story:**

_…Fictional cartoon portrays an AGI doom scenario…_

Here's a fun video about how AI systems might independently choose to annihilate their human overlords. It's both a compelling piece of fiction and gets at one of the core AI safety concerns - if a system is slightly misaligned with human values problems might compound quickly because it thinks so much faster than us. 

**Watch the video:** [That Alien Message (YouTube)](https://www.youtube.com/watch?v=fVN_5xsMDdg&ab_channel=RationalAnimations).

***

 **The era of the molecular structure prediction startup arrives:**

_…Chai Discovery's new model says people think there's a business in bioAI…_

AI startup Chai Discovery has released Chai-1, a large-scale foundation model for molecular structure prediction. "Chai-1 accepts a wide variety of optional input features, such as language model embeddings, structural templates, genetic search, and wet-lab experimental data such as contacts determined by cross link mass spectrometry or epitope mapping."

**Results** : "We tested Chai-1 across a large number of benchmarks, and found that the model achieves a 77% success rate on the PoseBusters benchmark (vs. 76% by AlphaFold3), as well as an Cα LDDT of 0.849 on the CASP15 protein monomer structure prediction set (vs. 0.801 by ESM3-98B)."

**Why this matters - bio + Ai as a new frontier:** A few years ago, DeepMind wowed the world with AlphaFold, an AI system that excelled protein structure prediction - an extremely hard problem that had been hard to make progress on for years. Now, years later, there are multiple startups as well as companies (e.g., DeepMind's own spinoff Isomorphic Labs, which recently co-developed AlphaFold 3) working to turn this powerful new capability into a commercial capability. 

"We believe that building an accurate understanding of the structure of biological molecules is foundational to advancing our scientific understanding of cellular processes, and ultimately, for advancing human health" the startup writes. 

**Read more:** [Introducing Chai-1: Decoding the molecular interactions of life (Chai Discovery)](https://www.chaidiscovery.com/blog/introducing-chai-1).

**Access Chai-1** [via a web interface here (Chai Discovery)](https://lab.chaidiscovery.com/auth/login?callbackUrl=https%3A%2F%2Flab.chaidiscovery.com%2Fdashboard).

**Get the model weights here:**[Chai-1 (Chai Discovery, GitHub)](https://github.com/chaidiscovery/chai-lab).

**Read the research paper here:** [Chai-1 Technical Report (Chai Discovery)](https://chaiassets.com/chai-1/paper/technical_report_v1.pdf).

***

 **Tech Tales:**

**Sophon Game Theory**

 _[This decade]_

Everyone thought the first use of a really strong AI would be to improve itself, but in fact the first use was to make it impossible for others to be built. It worked like this - once we had system one, we asked it to perform a range of synthetic data experiments and identify types of data that its preference models would favor but would over time yield improved performance which had an inbuilt ceiling - this was a hard task, far more complicated than just making bad data or making data to bootstrap off of, but it proved worthwhile. 

We verified this by training a model to completion on this dataset. The resulting model obtained excellent benchmark scores and was useful for a variety of tasks, but when we tried to use it to generate synthetic data for it to bootstrap off of it worked for a couple of iterations before succumbing to mode collapse - superficially promising, but (we knew) inherently flawed.

We kept our system secret - we had to, for the next phase of the plan to work. 

Next, we used the system to start contributing content to some of the most popular publicly available websites. This content took the form of superficially high-value data - long-context stories, seemingly original anecdotes, novel jokes, rhymes about current events, and so on. We knew that the other labs would be trawling this and their systems would automatically pick up this data and assign it high-value as their own classifiers would give it a high ranking. 

So we waited… and waited. 

We discovered that our competitors had pursued our own strategy - the internet started to fill up with even lower quality data which we believe emanated from the systems they had trained on our data. 

We've been training our own successor system for several months. It is improving further, but we are beginning to worry there may be some kind of ceiling that it is running into. 

Were we the first?

**Things that inspired this story:** Game theory; getting inside and corrupting OODA loops; dark forest theory of AI development; competition; synthetic data; mode collapse.

_Thanks for reading!_
