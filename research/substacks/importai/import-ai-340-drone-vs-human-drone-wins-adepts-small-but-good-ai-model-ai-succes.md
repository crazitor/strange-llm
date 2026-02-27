---
title: "Import AI 340: Drone VS human (Drone wins); Adept's small but good AI model; \"AI Succession\""
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-340-drone-vs-human-drone"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Adept releases a small, extremely high performing language model:  
**_…Paradigm punctured by Precocious Persimmon-8B…  
_ AI startup Adept has released Persimmon-8B, a language model it calls "the best fully permissively-licensed model in the 8B class". The model has a context size of 16k and has performance that exceeds other similarly-sized 8B models and at times matches LLaMA2 models from Facebook, despite being trained on less data.   
"The 8B size is a sweet spot for most users without access to large-scale compute—they can be finetuned on a single GPU, run at a decent speed on modern MacBooks, and may even fit on mobile devices," Adept writes. "The inference code we’re releasing along with the model is unique—it combines the speed of C++ implementations (e.g. FasterTransformer) with the flexibility of naive Python inference."

**No safety interventions:** Adept's approach to AI safety or ethics is to skip it entirely and clearly announce this: "Because this is a raw model release, we have not added further finetuning, postprocessing or sampling strategies to control for toxic outputs," the company writes. 

**Why this matters - smaller, cheaper, faster, more!** Today, large-scale language models are interesting tools used by people all around the world, but the literal size of these models means you need to have non-trivial hardware (e.g, multiple GPUs working in parallel) just to pull outputs out of them. By comparison, 8B-sized models can be optimized in all kinds of ways and are typically easy to fit on a single GPU (or even more diminutive bits of hardware, like phones). Models like Persimmon-8B will proliferate wildly around the world and their small and portable nature will mean they get used in all kinds of surprising ways.   
**Read more** : [Releasing Persimmon-8B (Adept)](https://www.adept.ai/blog/persimmon-8b).  
  
####################################################  
  
**AI pioneer thinks humanity should accept the idea of 'AI Succession':  
**_…It's not Us VS The Machines, it's Us THEN The Machines…  
_ Richard Sutton, a pioneer who has spent decades driving forward progress in reinforcement learning, thinks the logical outcome of our current path of AI development is 'AI Succession' - that is, humanity is going to create machines that surpass us and then these machines will succeed us as the dominant force driving progress forward in the world.   
The talk doesn't make claims about the machines killing us or doing anything bad. In fact, Sutton expects we should be able to arrange a 'comfortable retirement' for our species if we manage the transition carefully. But it is a somewhat heterodox position to hold - many people right now are calling for a slowdown in AI development so as to avoid existential risks, and the many other problems that come about from creating smart machines. I think Sutton subscribes more to the school of thought that says AI is inevitable, so we might as well just get along with it and be clear-eyed about where it leaves us.   
Food for thought, for sure. I do admire his forthrightness here.   
**Watch the video:**[AI Succession (Richard Sutton, YouTube)](https://www.youtube.com/watch?v=NgHFMolXs3U&ab_channel=RichSutton)**.**

####################################################

**RL Drone beats human pilots in first-person drone racing:  
**_…We've come a long way from Space Invaders… another month, another major milestone…  
_ A drone piloted via an autonomous AI system has beaten human pilots in an expert-level first-person view drone race, marking a significant moment for 'real world reinforcement learning'. 

**What happened:** Researchers with the University of Zurich and Intel Labs built Swift, a system that "combines deep reinforcement learning (RL) in simulation with data collected in the physical world" and used it to control a drone which competed against three highly skilled human pilots in a challenging FPV course. ""Swift won several races against each of the human pilots and achieved the fastest race time recorded during the events," the researchers write in a paper about their results published in Nature. 

**Important caveats before we get to the good stuff:** The drone was trained partially in a simulation of a course so it wasn't learning on the fly (but neither were the human pilots - they were given a week to practice flying the course before the competition). The scientists also collected some real world data of practice runs on the track and here they recorded "sensory observations from the robot together with highly accurate pose estimates from a motion-capture system while the drone is racing through the track" which they used to help the drone calibrate on differences between its perception and its pose.   
Additionally, the drone system had direct access to inertial data from an onboard inertial measurement unit, whereas the humans had to pilot purely via visual inputs (then again, that's just how things will be in real life also, so seems fair to me.) 

How the technology works: Swift has two key components. These are:

  * 1\. A perception system that translates high-dimensional visual and inertial information into a low-dimensional representation. The perception system combines a visual-intertial estimator with a convnet-based gate detector - "detected gates are used to estimate the global position and orientation of the drone along the race track".

  * 2\. A control policy that ingests the low-dimensional representation produced by the perception system and produces control commands.




**Curious differences between AI and humans:** Whenever an AI system beats a human at a task there are always some curious ways in which the AI wins - remember, for instance, AlphaGo demonstrating some cool creativitiy with its 'move 37' against Lee Sedol. Here, we see that the drone has a couple of interesting strategies that seem to depend on its inhuman calculating brain:

  * 1\. **Longer-term strategy:** Swift tends to accelerate faster and seeks tighter manoeuvres. "One hypothesis is that Swift optimizes trajectories on a longer timescale than human pilots." 

  * 2\. **Flying blind:** Most intriguingly, human pilots tend to orient their drones so that the gates are in view. Swift does this less. ""Swift has learned to execute some manoeuvres while relying on other cues, such as inertial data and visual odometry against features in the surrounding environments," they write. 




**Why this matters - THE BEST RL COULD DO TEN YEARS AGO WAS PLAY SPACE INVADERS:** Do excuse the capitals, but, erm… what? 

  * Ten years ago RL could do space invaders. 

  * Seven years ago it could do board games like Go. 

  * Five years ago it could do multi-unit strategy games like Starcraft and Dota. 

  * Now, RL can do continuous control challenges _IN THE REAL WORLD_ and can consistently beat human experts at a challenging sport. 




As Bill Gates is fond of saying, people overestimate what they can do in a year and underestimate what they can do in ten. We are all chronically underestimating the rate of AI progress. What will drones be capable of in five years from now?   
**Read more:**[Champion-level drone racing using deep reinforcement learning (](https://www.nature.com/articles/s41586-023-06419-4)_[Nature](https://www.nature.com/articles/s41586-023-06419-4)_[)](https://www.nature.com/articles/s41586-023-06419-4).  
  
####################################################  
  
**Alright let's stop being serious for a moment and think about PLANET-SIZED COMPUTERS:  
**_…A wonderful old paper from Anders Sandberg that's worth your time…  
_ Anders Sandberg, a delightfully mad physicist slash omnidisciplinary intellectual bon vivant, has written a bunch of great papers (e.g, what happens if earth [suddenly turned into blueberries](https://arxiv.org/abs/1807.10553)). Recently, I had the great pleasure of reading his paper 'The Physics of Information Processing Superobjects: Daily Life Among the Jupiter Brains', and I suggest readers of this newsletter do the same. 

**Why you should read a funny paper from 1999:** As we live in the era of 'maybe superintelligence is possible', it's fun to speculate about what happens if it turns out it gets built - surely, at some point in the decades after that, we might build some incredibly large computers for really smart systems and, hopefully, take to the stars for some kind of glorious future, learn to harvest the energy of our solar system and beyond, and so on… but what happens after that? Well, if you wind the tape forward, it seems likely we might want to make some _really big computers_ to keep doing cool things with synthetic intelligence.   
**But how big is really big?** This paper outlines some of the key physics-based considerations one would face when trying to build an incredibly large computer to host a vast synthetic intelligence. The paper is marvelous and I think one of the best ways to make learning about science fun. It's also full of delightfully mad findings and statements, such as:

  * "A planetary sized structure could be orbited by a circle of large radiator sails in the geosynchronous (cerebrosynchronous?) orbit extending connecting pipes down to the "ground"."

  * "By charging the black holes so that they become extreme Reissner-Nordstrom black holes it might be possible to create a dense volume of "black hole processors" where their mutual attraction is balanced by electrical repulsion"

  * "Zeus is a r = 9000 km sphere of nearly solid diamondoid, consisting mainly of reversible quantum dot circuits and molecular storage systems".




I mean, _come on!_ This paper had me grinning ear-to-ear for days. Read it and wander around looking at the sky asking yourselves how many of the objects in the great beyond may be brains of vast (but, per this paper, _calculable_) scale, dreaming of themselves, or perhaps of us. Physics - marvelous!   
**Read more:** [The Physics of Information Processing Superobjects: Daily Life Among the Jupiter Brains (PDF)](https://www.jetpress.org/volume5/Brains2.pdf).  
  
####################################################  
  
**Another 10,000 GPU cluster appears:  
**_…Imbue raises a $200m Series B…  
_ Imbue, formerly known as Generally Intelligent, has raised $200M in a Series B round. The startup's goal is to "build practical AI agents that can accomplish larger goals and safely work for us in the real world". 

**GPUs as a hiring beacon** : The most interesting part of the announcement is the appearance of GPUs as a reason for why people might want to work there: "Our latest funding round lets us operate at a scale that few other companies are able to: our ~10,000 H100 cluster lets us iterate rapidly on everything from training data to architecture and reasoning mechanisms." (Recall that Inflection, another AI startup, recently advertised itself as being an interesting company because it was using a new funding round to build out a 22,000-strong H100 cluster. 

**Why this matters - centralization gets harder as compute clusters proliferate:** In AI policy of late there's been a lot of anxiety (and on my part, confusion!) about how centralized AI development might be or how decentralized it might be. I think the more large-scale (multiple thousands of frontier GPUs) compute clusters there are in the world, the less centralized AI development becomes. Fundraises and compute allocations like those of Imbue suggest we're heading into a decentralized world where hundreds of clusters of thousands of GPUs proliferate, each training large-scale models.   
**Read more** : [Imbue raises $200M to build AI systems that can reason and code (Imbue blog)](https://imbue.com/company/introducing-imbue/).  
  
####################################################  
  
**Compute Controls  
** _[America, 2032]_

"How many computers do you have in your house, Jim?", said the man in the FBI jacket.   
"As many as I need," said Jim. "Now, please get off my property."  
"I'll be back with a warrant," said the man.   
"See you then," said Jim, shutting the door. 

Jim made himself a cup of coffee and went down to his basement and looked at the computers. He had a DIY Super made up of a few graphics cards and some dedicated training chips. He'd been building the rig for a few months and had been careful - never buying from the same vendor twice, and wherever possible trying to pay for the chips in cash, leaving as little trace online as possible.   
But someone or something had tipped the FBI off. And if they thought he had computers they'd be doing whatever they could to score the warrant. 

He wondered if he had enough time. With the current cluster, it'd take him three weeks to finetune the model. How long would it take them to get a warrant? It was hard to say.   
Then upstairs he heard a thud. When he walked into their bedroom she was on the floor, sobbing silently. She looked up at him and said "I can't get up."  
"It's okay baby, I've got you" he said, and he picked her up and put her back in bed.   
"I'm sorry," she said. "This must be so hard on you."  
"Go back to sleep," he said. 

The FDA and an alphabet soup of other federal agencies had neatly circumscribed what AI systems could and couldn't do and healthcare was firmly off limits unless done by Verified AI Companies (VACs). Worse, diagnostic healthcare was mired in a bunch of approvals at the FDA. So even though the United States possessed incredibly powerful AI systems, and its healthcare providers had a huge amount of digital healthcare data, it was unable to combine the two. In fact, it was technically illegal.  
Combine that with a bunch of well-intentioned policies that were designed to present misuse of AI and you had an issue - the cloud providers only let a small set of people and companies train new AI systems, and though various model-modification services were legal they were also controlled - they didn't want you changing your model so it could enable a misuse or so it could conflict with regulations.   
Like most well-intentioned policy proposals, once you added enough rules together you got mysterious and unfortunate overlaps which trapped people like Jim: Jim who had a sick wife and wanted to help maximize her chances of living and who found himself, typically a law-abiding citizen, needing to violate the law so that he could finetune an AI model on a domain he was not authorized to point an AI brain at.   
Which was why Jim had amassed his computers in the basement. 

At the doctor’s office he held her hand and they got the updates. "We have a few options left," said the Doctor. "We'll increase your chemo dose."   
"Isn't that risky," said Jim. "I read that with her condition the chemo you've got her on can have some pretty bad side effects."   
"Dr Google says a lot of things," said the Doctor. "We're confident this is the best course of action."   
"I'd like her latest records," said Jim. "Please."  
Jim and his wife didn't leave the office until Jim saw the records come through to his phone. 

That night, he merged the records in with the rest of his wife's data and checked on the model progress. A couple of days to go.   
In the night, he dreamed of the loss curve of his model going down and as it went down he imagined his wife healing and becoming herself again. He woke and held her hand and she said "I love you", and he said "I love you, go to sleep", and she said "ok" and drifted off.   
He pulled up the training run on his phone and looked at the loss curve. Nearly there. 

On the day the model finished, he cleared his schedule. After making his wife breakfast, he went down to the basement and watched as the run finished. Then he loaded up the model and started running all the automated medical exploration prompts he'd been developing in the recent weeks - the model was in line with all the previous eval performance tolerances he'd designed (baselined against questions he'd verbally asked the doctor and containing responses which didn't seem to be directly present in the dataset).   
Once he was satisfied he had a good model he started asking it every possible question about his wife's condition, using the latest data.   
He wasn't a medical expert but he was a loving and devoted husband.   
And he was so afraid of being alone. 

A few hours passed and he came out of it with some optimistic treatment plans. No slam dunks but something to ask the Dr about. Something which, maybe, the Dr hadn't thought of. And also some evidence that some of her unexplained symptoms might be through a combination of some of the treatments she'd been prescribed.  
But the AI ended up asking him a question which startled him.   
"Based on the provided information, it seems valuable to consider palliative care options as well, including end-of-life treatment plans. Would you like me to list some?"  
  
And before Jim could write 'yes' he heard a banging on the front door upstairs and someone shouting: "FBI, open up, we've got a warrant."   
  
**Things that inspired this story:** Some of the inherent 'friendly fire' that comes from overly zealous AI policy proposals; worries about centralization versus decentralization in AI development; individual motivations versus government precautionary principle motivations; 3-D printed guns and the general 'distributed defense' libertarian mindset; once you have someone you love you will do so many things to protect them and you will not care about the law; love; how people will be very inventive and very smart if they need to be and how they will try to hack around any efforts you take to suppress them; AI policy; AI regulation; AI licensing.
