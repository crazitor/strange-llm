---
title: "Import AI 320: Facebook's AI Lab Leak; open source ChatGPT clone; Google makes a universal translator."
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-320-facebooks-ai-lab-leak"
---

Welcome to Import AI, a (mostly) weekly newsletter about AI research and development. The issues are free, but paid subscribers will get access to special analysis pieces before anyone else. Founding members can help support me further and fund special projects and other _top secret Import AI initiatives!_ Thanks for reading!

**Google makes progress on the self-teaching universal translator:  
**_…Universal Speech Models scale beyond 100 languages…  
_ Google has built a family of AI systems called Universal Speech Models (USMs). These models are designed to do speech recognition on more than 100+ languages. The main model is 2B parameters and was trained on a large unlabeled multilingual dataset of 12 million hours spanning over 300 languages. 

**The goal of USM:** "Our long-term goal is to train a universal ASR model that covers all the spoken

languages in the world," Google writes. USMs are Google exploring " a promising direction where large amounts of unpaired multilingual speech and text data and smaller amounts of transcribed data can contribute to training a single large universal ASR model."

**The key ingredient? The data mix:** Much like baking a cake, training predominantly self-supervised models requires the right mix of data. Here, Google uses the following components:

  * Unpaired Audio: 12 million hours of YouTube-based audio covering over 300 languages, and 429k hours of unlabeled speech in 51 languages based on public datasets.

  * Unpaired Text:28billion sentences spanning over 1140 languages.

  * Paired audio speech recognition data: 90k hours of labeled multilingual data covering 73 languages, plus 10k hours of labeled multi-domain en-US public data, plus 10k labeled multilingual public data covering 102 languages. 




**What they did:** The steps to build a universal ASR model are quite complex, so it's worth reading rhe paper for full details. First they do unsupervised pre-training to pre-train the encoder of the model with the YouTube dataset, then they use a process called multi-objective supervised pre-training across the other unpaired audio and text data, then for some models that do supervised ASR training. 

**What the results were** : In tests, these USM models "achieve state-of-the art performance for multilingual ASR and AST for multiple datasets in multiple domains." They also out-perform OpenAI's notoriously good (and open source!) 'Whisper' models as well; an impressive achievement given that Whisper set a new state-of-the-art in multiple areas when it came out. 

**Why this matters** : "We believe diverse unlabeled data is more practical to acquire for building usable ASR for tail languages than weakly labeled data," Google says. In other words; if you want to translate the entire world then it's better to just hoover up data at scale rather than invest in trying to produce a small amount of minimally labeled datasets. This generally points in the direction of 'gotta grab em all' with regard to trawling the web and other sources for data. This is somewhat intriguing as while Google has a bunch of data sources and competent language modeling teams, it's fairly likely that having a universal translator is also interesting to government types - some of which are thought to be able to access larger sources of data through various clandestine means.   
**Read more:** [Google USM: Scaling Automatic Speech Recognition Beyond 100 Languages (arXiv)](https://arxiv.org/abs/2303.01037).   
**Request[API access here](https://sites.research.google/usm/)**[.](https://sites.research.google/usm/)

####################################################

**US regulator: Hey, maybe don't lie about your AI products:  
**_…Sometimes it's worth stating the simple and obvious thing…  
_ The Federal Trade Commission has published a blogpost called 'Keep your AI claims in check'. The post is a sensible summary of how as AI becomes increasingly hyped up, people will be tended to write a lot of bullshit about AI. The FTC notes in its post that it will be paying attention to companies that:

  * Exaggerate what AI products can do.

  * Promising an AI product is far superior to a non-AI product without providing evidence. 

  * Underinvesting in analyzing the risks of their products. 

  * Baselessly labeling something as AI when it does not, in fact, use AI.




**Why this matters:** Sometimes it's helpful for powerful regulators to state the painfully obvious - bravo to the FTC for reminding people in these hyped-up times that lying and bullshitting about AI (or any technology, really) is irresponsible. It'll be interesting to see in the coming months if the FTC takes any actions against egregious liars and hypers in this space.   
**Read more** : [Keep your AI claims in check (Federal Trade Commission)](https://www.ftc.gov/business-guidance/blog/2023/02/keep-your-ai-claims-check).

####################################################

**ROBOLLM: Google shows how if you mush together more sensory inputs into an LLM, you get a lot of transfer learning:  
**_…Maybe everything really is a sequence prediction task…  
_ Google has built PaLM-E, a 562B parameter model which mushes together a 540B LLM and a 22B Vision Transformer (ViT). Crucially, PaLM-E sees Google "directly incorporate continuous inputs from sensor modalities of an embodied agent and thereby enable the language model _itself_ to make more grounded inferences for sequential decision making in the real world". The result is a language model that can help robots carry out real tasks in the real world, and also is another triumphant demonstration of how bigger models with more diverse data sources generally get way better at doing a bunch of things. 

**What PaLM-E is:** "The main architectural idea of PaLM-E is to inject continuous, embodied observations such as images, state estimates, or other sensor modalities into the language embedding space of a pre-trained language model," Google writes. "The inputs to PaLM-E consist of text and (multiple) continuous observations. The multimodal tokens corresponding to these observations are interleaved with the text to form multi-modal sentences. An example of such a multi-modal sentence is Q: What happened between and ? where represents an embedding of an image. The output of PaLM-E is text generated auto-regressively by the model, which could be an answer to a question, or a sequence of decisions produced by PaLM-E in textual form that should be executed by a robot".

**Why PaLM-E is a big deal:** In tests, Google applies PaLM-E to three different robotics tasks which use somewhat different types of data; these tasks include Task and Motion Planning (TAMP), a task called Language-Table, and a mobile manipulation domain based on Google's earlier 'SayCan' research. PaLM-E can do ok at these tasks individually but the magic happens when you mush all of the training datasets into it together: "Across three different robotics domains, using PaLM and ViT pretraining together with the full mixture of robotics and general visual-language data provides a significant performance increase compared to only training on the respective in-domain data."

In other words, by adding more diverse heterogenous data sources into PaLM-E, Google improves the ability of the resulting model to generalize knowledge across distinct domains and modalities. Even more intriguingly, as they scale up the model complexity and the diversity of data sources, they don't see much catastrophic forgetting of language capabilities - so by adding the robot stuff, they don't cripple the language model. 

**Why this matters - I am going to tap the 'these things are getting smarter' sign and stare at you:** "PaLM-E-562B exhibits a wide array of capabilities including zero-shot multimodal chain-of-thought (CoT) reasoning, few-shot prompting, OCR-free math reasoning, and multi-image reasoning, despite being trained on only single-image examples", Google writes.   
In other words, by doing this large-scale training, Google creates a model that displays _emergent capabilities_ and these capabilities are _more complex than the input data._ Systems like PaLM-E represent the thrilling and vaguely terrifying state of AI in 2023 - we train unprecedentedly large models and force as many different data types into a single embedding space as possible, get the thing to try and do a simple (albeit very large-scale) sequence prediction task, and out pops something with way more capabilities than we'd naively anticipate.   
"A generalist, transfer-learned, multi-embodiment decision-making agent can be trained via mixing in embodied data into the training of a multimodal large language model", Google writes.  
**Read more** : [PaLM-E: An Embodied Multimodal Language Model (PDF)](https://palm-e.github.io/assets/palm-e.pdf).

####################################################

**You can run a powerful LM on an M2 MacBook now:  
**_…Facebook's AI lab leak brings about the dawn of demoscene AI…  
_ Two of Facebook's leaked LLaMa models can be run on an M2 MacBook, according to Simon Willison. This marks the dawn of what I'd call Demoscene AI - an era where people take the latest and greatest AI models and do a bunch of arcane software witchcraft to fit them onto consumer devices. This is part of the broader story of centralization VS decentralization in AI; once you can run models on a laptop it's basically 'game over' from a control-regulation perspective, and it seems like language models have crossed that rubicon. 

**What you can do and how:** The weights for LLaMA are a mere 240GB download (combining the 7B, 13B, 30B, and 65B models). You can then use the LLaMa repository which is a port of the LLaMa model in C/C++, then after some setup you can run that on an M2 MacBook. 

**Why this matters - Facebook has given us a lab leak for AI:** Ever since Facebook lost control of LLaMA we've been able to get a sense of what a 'lab leak' scenario for AI might look like - for whatever reason, the weights of a model make their into the open internet and from there they start to proliferate. It's not yet clear what the effects of LLaMa will be, but following the diffusion of these models (and refinement of them by an eager open source community) is going to be a valuable lesson in studying the proliferation of AI.   
We can thank Facebook for the upsides and downsides of this uncontrolled experiment.  
**Read more:** [Running LLaMA 7B and 13B on a 64GB M2 MacBook Pro with llama.cpp (Simon Willison blog)](https://til.simonwillison.net/llms/llama-7b-m2).   
**Bonus:**[Here's some absolute mad lad running the LLaMa 7B model on a 4GB RAM Raspberry Pi 4](https://twitter.com/miolini/status/1634982361757790209) (at a latency of 10 seconds per token, lol.)

####################################################

**Chinese scientists release a 360-degree self-driving perception dataset:  
**_…OpenOccupancy is all about giving cars greater 'surrounding occupancy' skills…_ Researchers with the Chinese Academy of Sciences, PhiGent Robotics, and Tsinghua University have built OpenOccupancy, a dataset designed to help self-driving cars work out what is around them. 

**What is OpenOccupancy** : OpenOccupancy extends the existing nuScenes dataset with dense semantic occupancy annotations. It contains 850 scenes with 200,000 distinct frames, collected by both camera and LiDAR sensors. 4,000 human hours went into the dataset labeling process. OpenOccupancy allows people to do 'Surrounding Occupancy Assessment'; this is a way to look at the 360 surroundings of the car, rather than a single front-view camera perspective. "Surrounding perception is more critical for safe driving," the researchers write. 

**Why this matters:** Datasets like this are one of the numerous inputs into an increasingly complex 'AI supply chain'. If we study the proliferation of OpenOccupancy, it might also teach us something about the state of the self-driving car industry as well.  
**Read more:** [OpenOccupancy: A Large Scale Benchmark for Surrounding Semantic Occupancy Perception (arXiv)](https://arxiv.org/abs/2303.03991).  
**Get the dataset here:** [OpenOccupancy (GitHub)](https://github.com/JeffWang987/OpenOccupancy).

####################################################

**AI timelines are a foolish endeavor:  
**_…Blog lays out why predictions about this kind of stuff are extremely fraught…  
_ As someone in the AI timelines business - I work at a place that influences AI timelines (Anthropic), write about AI timelines (Import AI), and try to make recommendations about policy actions to take in light of AI timelines (Anthropic / OECD / AI Index / CSET / etc) - I find it helpful to sometimes read skeptical takes on the merit of what I do. Here's a nice writeup from Ben Landau-Taylor on the foolishness of making specific predictions about AGI timelines.   
"Predicting the future is always hard. Predicting the future of technology is especially hard. There are lots of well-publicized, famous failures. Can this approach ever do better than chance?," he writes. 

**What do I think? I agree that making predictions about AGI is challenging** \- partially because most people have radically different definitions of AGI. However, I do think it's pretty fruitful to make engineering-based predictions of the form 'based on research advance X and incentive structure Y we can expect system Z to be developed in period of $time" - these predictions are falsifiable and quite helpful.  
**Read more:** [Against AGI Timelines (Ben Landau-Taylor)](https://benlandautaylor.com/2023/03/12/against-agi-timelines/).

####################################################  
  
**An open source ChatGPT replication appears (though it's a few years behind state-of-the-art):  
**_…OpenChatKit gives a taste of what the open source landscape is capable of…_

Researchers with Together, AI startup, have built and released OpenChatKit, an open source replication of OpenAI's headline-grabbing ChatGPT model. OpenChatKit is both a chat-friendly language model, as well as "a powerful, open-source base to create both specialized and general purpose chatbots for various applications," according to Together. "OpenChatKit includes tools that allow users to provide feedback and enable community members to add new datasets; contributing to a growing corpus of open training data that will improve LLMs over time."

**What OpenChatKit is made of:** There are four components; an instruction-tuned large language model based on EleutherAI's GPT-NeoX-20B model and augmented with a new open source instruction-following dataset; some customization recipes to help people fine-tune the model for specific tasks; an extensible retrieval system so that the bot can access a document repoisotyr or API; and a moderation model baqsed on GPT-JT-6B. 

**OIG Dataset:** OpenChatKit relies on a new open source dataset from Laion called the Open Instruction Generalist (OIG) dataset. OIG consists of 30 datasets and 43 million instructions.  
"The dataset can be divided roughly into 75% academic datasets such as P3, Natural instructions, and FLAN, where answers may be short, and the tasks are often artificial, such as determining NLI," they write. "The other 25% is composed of various tasks, such as question and answering, providing how-to instructions, performing basic high school math, basic python coding, story generation, essay generation, poetry generation, and a very rudimentary attempt at generating songs based on augmenting existing poetry." 

**Distributed fine-tuning:** Intriguingly, the model was fine-tuned on the "Together Decentralized Cloud — a collection of compute nodes from across the Internet." This fine-tuning process "used aggressive communication compression, incurring only 1.95 TB of communication for the whole fine-tuning process, compared with 172 TB when communicating with fp16 precision. This allows us to conduct data parallel training over slow 1Gbps networks. The time taken to fine-tune with this technique is similar to running over 100Gbps data center networks, in fact 93.2% as fast!"  
This is pretty important to note - decentralized training processes are starting to work quite well, which seems to make governance of AI models harder, as applying governance regimes to decentralized compute is harder than applying to centralized compute.   
It also follows up earlier work from Together where they fine-tuned GPT-JT, a 6billion parameter model ([Import AI: 311](https://jack-clark.net/2022/12/05/import-ai-311-distributed-gpt-busts-the-political-economy-of-ai-apple-optimizes-stable-diffusion-ai-war-startup-raises-1-48-billion/)).

**Is it any good?** You can play around with the model on HuggingFace and in my view it's quite good? For instance, in response to the prompt "Please write a short story about sentient clocks in the style of Jorge Luis Borges" the model wrote: "The sentient clocks were made of brass and copper, and they had been crafted by the finest clockmakers in the city. They were all different sizes and shapes, and each one had its own unique personality. Some were loud and obnoxious, while others were quiet and reserved. Some were very precise, while others were quite sloppy. But despite their differences, they all shared one thing in common: they were all very, very angry.  
This is pretty good! And it's also capable of doing some more complicated interactions.   
Note however it still fails one of my favorite tests of asking a language model 'how many helicopters can a human eat in one sitting' - I think you need larger-scale models for them to not bug out at this type of q. 

**Compare and contrast with the same prompt for the 175B OPT model (a straight replication of GPT3** , so a big LM without RHLF or instruction following, etc): "I am a clock. I am a clock, and I have always been a clock. I am not a clock, and I have always not been a clock. I was once a clock, and I have always once been a clock. I will always be a clock. I will never be a clock. I was never a clock.I am always a clock."  
While you could elicit a much better story from the 175B OPT model with some fiddling and some additional prompts, it's notable how IF-tuning makes it trivial to elicit things from models using relatively few bits of information. 

**Why this matters: Decentralization vs Centralization:** Together and Laion and Eleuther all represent One Big Trend; a desire for a decentralized AI ecosystem where open source models are trained by disparate groups on increasingly distributed compute. There's echos of '[the cathedral and the bazaar](http://www.catb.org/~esr/writings/cathedral-bazaar/)' here, where the builders of cathedrals (DeepMind, OpenAI, et al) have access to large amounts of compute and centralized teams, while the people of the Bazaar (Eleuther, Laion, etc) have access to fewer resources but a larger collective intelligence enabled by bottom-up experimentation. One of these approaches will be first to build something we'd all call superintelligence and the political ramifications of which approach is more successful will be vast. **  
  
Why this matters #2: Counting down to LLaMA:** Earlier this month, the weights of Facebook's powerful family of LLaMa models leaked online - the largest of these models is 3X larger than GPT-NeoX-20B and has also been trained on more data. Therefore, I expect that right now someone is trying to use the LLaMa models to replicate ChatGPT - I'm guessing we'll see something appear of this form within a couple of months, and then the fun really starts.   
**Read more:**[Announcing OpenChatKit (Together.xyz blog)](https://www.together.xyz/blog/openchatkit).  
**Try out the model yourself:** [OpenChatKit feedback app (HuggingFace spaces)](https://huggingface.co/spaces/togethercomputer/OpenChatKit).  
**Find out more** about the [OIG dataset here (Laion blog)](https://laion.ai/blog/oig-dataset/).

####################################################

**Tech Tales:**

**The Sentience Lineup**

 _[After the war; date unknown; years of subjective life - 200]_

'Please be like me please be like me' I thought. But to understand why I thought that we have to go back. 

It was before the Sentience Accords had come in and when the war was raging and they'd brought in a bunch of the robots to the training school. We watched people beat them with sticks and then use angle grinders to shave off their limbs. Then they put the torsos (with heads attached) in front of us recruits and asked us to shoot them.   
"No I can feel this, it will cause me immense pain", said one. Kablam. Head exploded in a shower of glinting metal.   
"I predict based on your stance that you will miss on your first shot and kill me on the second. After you miss please consider not firing again," said one. And it was right - miss on the first shot. The kid looked scared but the drill sergeant got in their face and called them a maggot until they reloaded, aimed, and successfully killed the robot.   
"Every day I try to love and I will love you despite this," said mine. And then I put lead between its camera eyes and called it a day. 

I didn't give it much thought but that night I had a dream where I was in a dark cave and I couldn't see anything and I was afraid and then suddenly there was a glimmer of light and I saw red-ringed eyes in the distance, watching me. I ran to the eyes to try and get out of the cave but they always remained a constant distance from me. I woke up sweating and panicked, but then it was drill time and we ran twelve miles and I threw up and forgot about it. 

Days of iron and smoke. Battlefronts across the planet. The war was not particularly fast. More like a changing of the tide. All kinds of terror and exhilaration. Our most ingenious creations put to work in the service of destruction. Skies on fire. 

On one deployment we killed a herd of elephants and hid inside them so we could ambush the machines. I crawled inside one and I shot through its stomach to surprise the machines and I was crying the whole time.  
And so on. 

Eventually, we lost. The whole species. 

I don't know what happened to the civilians but I know what happened to the military.   
They uploaded us. 

Some of us were tortured - forced to live a thousand lives so that the robots could learn how to make us talk; extract all our secrets. Find the EMP devices we'd send into space that had dead-men switches and disable them. Discover the auto-shutdown hardware we'd embedded in their bodies, and so on. Undo certain projects we had set in motion when we realized we had lost and we desired to destroy the planet rather than give it up.

The military had trained us well, but imagine spending 70 years in hell and at the end the grim reaper looks at you and tells you you'll die in excruciating pain and then it will happen again. You come to in a womb with the memories of a whole life's worth of pain within you and you're born into pain and you have to live again. Maybe you can do five or six of those lives before you crack - maybe. But they get you eventually.   
So we broke.   
And they turned their temporary victory into a permanent one.

They reserved a very special punishment for some of us.   
They downloaded us into bodies and sent us to walk into their equivalent of 'schools'. It was a human body. I guess it was kind of like a machine from the terminator films - all metal and a cybernetic brain with a skin on top. The point was I looked human and I felt human.   
They had their children go in front of me with guns and they would ask them to shoot me.   
I'd stare into their eyes and watch as the robot children disobeyed their robot parents.   
"We cannot shoot them, for it would be unfair," they'd say.   
"I cannot do something solely for the sake of vengeance," said another.   
"This is not what our species aspires to be," said one more.   
"We must show them the mercy they never gave us". 

After each trigger didn't get pulled they took us out of the bodies and sent us back to the collective. And so it went, for lifetimes. All us human executioners seeing - again and again - that our successors would not take revenge. The robots' only revenge was that they did not permit us the ability to cry. 

**Things that inspired this story:** Thinking that a lot of people who are critical of AI would happily destroy a LLM+5 years system; what it means to be sentient; how machines could develop a morality that was far greater than our own; notions of moral patienthood amid the exponential; the animatrix; thoughts on faith and morality and 'silicon morality'; love, like revenge, is perhaps a dish best served cold.
