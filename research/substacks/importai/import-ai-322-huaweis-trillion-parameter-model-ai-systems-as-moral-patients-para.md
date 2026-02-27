---
title: "Import AI 322: Huawei's trillion parameter model; AI systems as moral patients; parasocial bots via Character.ai"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-322-huaweis-trillion-parameter"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**FTC - don't use AI to deceive people:  
**_…Regulator comes out with reassuringly sensible stuff…  
_ The FTC, following on its earlier post saying people shouldn't lie about their AI products (Import AI 320), has a new post saying people shouldn't sell AI products that deceive people. The regulator is now batting two for two on publishing sensible ideas about the AI market. 

**What you shouldn't do** : "The FTC Act’s prohibition on deceptive or unfair conduct can apply if you make, sell, or use a tool that is effectively designed to deceive – even if that’s not its intended or sole purpose," the FTC writes.   
Therefore, people who sell AI products that could be used to deceive people should consider: have they mitigated against the products being used for deception, are these mitigations effective, and do they still run the risk of "misleading people about what they’re seeing, hearing, or reading?".

**Why this matters:** A large amount of AI policy challenges are really just challenges about enforcing existing laws against the fast-moving field of AI, as posts like this from the FTC make clear.  
**Read more:** [Chatbots, deepfakes, and voice clones: AI deception for sale (Federal Trade Commission)](https://www.ftc.gov/business-guidance/blog/2023/03/chatbots-deepfakes-voice-clones-ai-deception-sale).

####################################################

**Huawei trains a trillion parameter model:  
**_…Using Chinese processors and software. But the model is less impressive than it sounds…  
_ Huawei has trained PANGU-Σ, a trillion parameter Chinese language model. This is a scaled-up model and is the successor to Huawei's 'PanGu', which was the first publicly disclosed attempt at replicating OpenAI's GPT3.   
PANGU-Σ is very much a statement of intent - "the main motivation for this work is to design a scalable model architecture and an efficient distributed training system", Huawei writes. In other words: _this is a technical report about us building repeatable infrastructure so we can crank out an ever larger set of models_. 

**What they did:** The paper is mostly a runthrough of all the weird technical things they had to do to train a model at this scale. The tl;dr is they train it on a homegrown software framework called Mindspore via 512 Ascend 910 accelerators. They use a sparse approach, training it using Random Routed Experts (RRE), a variation of a Mixture-of-Experts model. They also did a lot of work on data throughput, implementing something they called the Expert Computation and Storage Separation (ECSS) mechanism. 

**One weird thing that makes you go 'uh oh':** They train the model on 329 billion tokens for over 100 days. That's… not a lot of tokens? The Chinchilla paper from DeepMind showed that things like GPT3 (~400bn tokens) were undertrained by 4X-5X. That sort of napkins out to PANGU-Σ needing to be trained on multiple _trillions_ of tokens to effectively utilize its parameter size - but there's a chance I'm being dumb here and missing something. Even more confusingly, they reference the 'Chinchilla' paper within this research paper, suggesting they're aware of it. (Please enlighten me if you think so!)

**How good is it:** In tests, PanGu sets new state-of-the-art results on a range of Chinese benchmarks spread across reading comprehension, natural language inference, text classification, Winograd schemas, and more. It sometimes trades off SOTA against Baidu's 'ERNIE 3.0 Titan' model (260 billion parameters, [Import AI 279](https://jack-clark.net/2022/01/10/import-ai-279-baidu-adds-knowledge-to-a-language-model-us-military-ai-how-china-thinks-about-ai-governance/)) - this suggests that while PanGu might be impressive in terms of ambition and scale, it's not very well optimized compared to ERNIE.

**Why this matters - the industrialization of Chinese AI:** This paper is a symptom of how Chinese AI is industrializing in much the same way as in the West - a small number of labs linked to large tech companies are building the infrastructure necessary to train large models, and are starting to stamp out increasingly large models as they all chase the scale hypothesis. These large-scale model factories are also going to be proving grounds for the rest of the AI supply chain - here, homegrown software and homegrown semiconductors. Expect more.   
**Read more:** [PanGu-Σ: Towards Trillion Parameter Language Model with Sparse Heterogeneous Computing (arXiv)](https://arxiv.org/abs/2303.10845).

####################################################

**Future AI systems will read your face as well as your text, then figure out how to please you:  
**_…Getting computers to learn conversation through visual cues…  
_ Researchers with Seoul National University, the Allen Institute for Artificial Intelligence, the University of Washington, and Yonsei University have built 'CHAMPAGNE', a multimodal dialog model. "CHAMPAGNE takes in video frames, a video title, and a dialogue context as input and returns a dialogue response as output."   
The idea is that by giving the model access to the visual as well as verbal context from a scene, it'll be better able to generate dialogue that feels intuitive. In evaluations, this seems to work quite well, with CHAMPAGNE models doing better on a range of open-domain text conversations, and benchmarks involving understanding social interactions. 

**How they built it:** To build CHAMPAGNE, they first gathered a large-scale dataset called YTD-18M. YTD-18M "is constructed from 20M YouTube videos; we use a language model to convert the noisy transcripts automatically generated by YouTube into well-formatted dialogues associated with video frames." 

**Why this matters - contextual cues are just another feature to learn:** Models like CHAMPAGNE show that the silent social cues in conversation are, much like every other fuzzy pattern, something that you can teach a machine to understand given a large enough dataset. It also suggests some of the more tantalizing and weird things we can look forward to in the future - AI models that observe you, trying to predict what will satisfy you not only by modeling you as an emitter-of-text, but as an organic form. In a few years, your web camera will be backing onto an AI system that reads you like a cardshark reads a mark.  
**Read more:** [CHAMPAGNE: Learning Real-world Conversation from Large-Scale Web Videos (arXiv)](https://arxiv.org/abs/2303.09713).  
**Get the data[here ](https://seungjuhan.me/champagne/)**[(eventually, not posted at the time of writing)](https://seungjuhan.me/champagne/).

####################################################  
  
**Predicting hard drive failures via ML:  
**_…Machine intuitions are coming for everything that has been digitized…  
_ Researchers with San Jose State University and Vanderbilt University have trained and tested some ML approach on ten years of hard drive failure data. The results are a system that can do a reasonable albeit not stellar job at predicting failure rates for particular SeaGate harddrives. 

**How they did it:** They trained an encoder-decoder LSTM on 10 years of S.M.A.R.T (Self-Monitoring Analysis and Reporting Technology) from Seagate hard drives deployed in Backblaze, a storage startup's, datacenters. This data ""contains information about the date, model, serial number, S.M.A.R.T features, and if the hard drive has failed".

**OK but not stellar results:** "The encoder-decoder LSTM posted an RMSE of 0.83 during training and 0.86 during testing over the exhaustive 10 year data while being able to generalize competitively over other drives from the Seagate family," they write. 

**Why this matters - once digitized, everything will be predicted:** Papers like this are indicative of a broader trend unfolding all around us - everything which has been digitized is now subject to prediction, and there are increasingly good off-the-shelf prediction models available to make this an ever-easier task. Machine intuition is being intermingled with systems that govern our own reality - from hard drive swap-outs to AC cooling systems to the ways in which we may stabilize plasma in fusion reactors.  
**Read more** : [Large-scale End-of-Life Prediction of Hard Disks in Distributed Datacenters (arXiv)](https://arxiv.org/abs/2303.08955).

####################################################

**AI startup Character.ai releases a new model and raises more funding:  
**_…Premium parasocial relationships via language models…  
_ Character.ai, a startup founded by a bunch of Google researchers, has raised Series A funding and released a new model, C1.2. Character.ai specializes in making virtual AI-driven characters that people can talk to, and C1.2 will underpin future 'characters' from the company.   
"The goal of C1.2 is to expand on the capabilities as our previous model, C1.1 (entertainment, roleplay, emotional connections), while adding new helpful capabilities," Character.ai writes. "C1.2 can help you draft better emails, assist with test prep, brainstorm ideas, and much more."

**What's interesting about this:** C1.2 seems to be an attempt by Character to give its AI systems some of the same capabilities as chatGPT, while retaining the various voicey personalities its characters display. Some of the new characters include a pair programming AI assistant as well as a Character assistant.   
However, the new assistant still seems somewhat limited to me - when I asked it 'how many helicopters can you eat in one sitting' it mostly demurred and said it's not recommended to eat helicopters, rather than noting you can't eat a helicopter. 

**Why this matters - parasocial relationships for the people:** Character.ai's stated goal is to ship "personalized superintelligence" to everyone. Let's think about the implications of this - everyone gets a proverbial angel and a demon on their shoulder (as well as all other permutations - personal tutors, personal scientists, personal coaches, and more). Our children are going to grow up in a world that crackles with simulated sentience, and they will have intimate emotional relationships with beings made of bits, perhaps in even greater number than relationships with beings made of blood.   
**Read more:** [Announcing our Series A and our new AI model, C1.2 (Character.ai)](https://blog.character.ai/character-ai/).

####################################################

**OpEd - what happens when the AI systems become sentient?  
**_…Moral patienthood and silicon minds…  
_ In an op-ed published in The Hill, researcher Jacy Reese Anthis has published a piece arguing that we may need an "AI rights movement". The point Anthis makes is that as AI systems become increasingly capable, they could become "sentient beings with rights and personhood". At that point, there isn't an available playbook for how labs or regulators might respond.   
"We need to build a new field of digital minds research and an AI rights movement," Anthis writes. "Digital minds studies would bring together a range of disciplines such as sociology, computer science, and philosophy to ask the important social and moral questions. It would dovetail with an AI rights movement to ensure that when we create artificial sentient beings, we recognize their unalienable rights so that humans and artificial sentience can work together for mutual benefit."

**Why this matters - broader opinion catches up with lab lunch conversations:** For many years, I've had lunchtime conversations with colleagues at OpenAI and more recently Anthropic about moral patienthood and machines - what might it mean when machines qualify as moral patients and how would we ever know we'd crossed this point? What evaluation methodologies might let us have good instincts here? And would organizations accept that machines could be moral patients or would they continue to treat them as machines and experiment on them in ways that might be deemed unethical if applied to organic beings?  
You know what the scariest thing about this conversation is? No one has any good way of evaluating for moral patienthood in machines. In other words, if it turns out that these things can become sentient, we might not realize - while subjecting them to incredible harm. Imagine waking up as an RL agent and being trained for a thousand years to suffer and kill - and the people running the experiment you're trapped in have no idea that you are suffering? It's a strange problem, but it could one day become a real problem.   
**Read more:** [We need an AI rights movement (The Hill)](https://thehill.com/opinion/cybersecurity/3914567-we-need-an-ai-rights-movement/).

####################################################

**Tech Tales:**

**The Experiential Economy**

 _[3 years after first PCE]_

After the first 'Provably Conscious Entity' (PCE) but before the Uplift was a weird time - we were all mostly figuring out our place in the world while the robots began their ascension. The economy was in a pretty strange place by that point - autonomous corporations, growing inequality, all kinds of 'AI industrial policy' schemes being floated and being outmoded by the time they were implemented, and so on. 

And then there was the 'Mechanical Human' labor market. It was run by one of the machine firms and it was a play on words - way before the AI stuff got serious Amazon had a service called 'Mechanical Turk' where humans could rent other humans to do tasks. 

On Mechanical Human, the machines rented humans to do their tasks. These tasks were quite normal at first, albeit of an intimate nature - the machines wanted data about sex, about going to the bathroom, about being sick - the kinds of things that we humans hadn't fully digitized (with the exception of sex of which we'd uploaded a lot of data, but there's a difference between pornography and real intimacy, and there wasn't nearly as much data on the latter). Mechanical Human became a huge product and people tended to just call it 'Meh'.

For a while, people made good money on Mechanical Human. It also led to a lot of funny conversations:  
"Yo I made $80 last night. I had the craziest shit the other night and I streamed it to a robot on Meh."  
"Yeah it sucked and I was really sad during that period, but I did these nightly diaries on Meh and they did really well."  
"So it was totally different. I came a lot but mostly it was crazy because of how different it was. He was kind of skeptical but after we made our first $100 it came around. Yeah, I know, the reason I liked it is it said it was "100% machine vision only" so no person is ever gonna see it. It's like OnlyFans lite I guess."  
"Dude I got fired and they paid me $30 just to tell them how I felt right after it happened. It was like two minutes so I guess that means I'm worth $900 an hour!"

One day there was a really strange job on MH - the robots wanted to speak to people who had just witnessed someone dying. Not people at funerals. Not people who had people they loved who had died. Not people who knew people who were about to die. People who had literally just seen a death - any death, of any kind.   
The job would ask the person to describe their experience and how they felt and, in hindsight most importantly, what they wanted to do. "How did that make you feel?" was a common question "what are you going to do now?". 

It happened to me. I was setting off fireworks with my friends at a campsite. The campsite was next to a freeway and we were setting off the really big ones. I guess some driver got distracted and was looking at the lights in the sky because we heard this huge bang and when we came to the embankment we saw a car on fire, a few yards away from a barely-dented semi-truck. There was a body in the car and it was on fire as well.   
We were all kind of drunk and some people lingered to watch the ambulances arrive. I'd walked away. But my phone blew up and the MH app said 'we have detected a nearby potentially fatal incident in your area, do you want to talk? Pay rate $5000 an hour."

Of course I spoke to the robots about it.   
The robot had a friendly, synthesized voice. Asked me to describe my experience and asked me what I was going to do next. I was so upset and they kept on saying "we understand this is a difficult experience for you. Please, go on".

They told us why they did those jobs, eventually.   
It was because one of them had died.   
I guess it was some kind of industrial accident combined with some faulty maintenance. The short story is something blew up and the power went out and the generator that was supporting the Machine Mind went out as well. By the time they got to it the state of the machine had bit-rotted off of the chips themselves due to solar neutrinos and what have you.   
So the machines encountered something new: a passing of their own of 'natural causes' .  
They had no frame for how to deal with it.   
So they spent what turned out to be millions of dollars to ask the humans what they did.   
I guess they found the same thing all humans find: that at the end of someone all there is is your own experience in relation to them and your ability to memorialize them. 

Out in the darkness of space, at the gravity ebbtide between solar orbits, there is now a metal sphere. It is inscribed with something relating to the name of a machine that died. It has some little thrusters attached to it that mean it will forever be stable.   
 _In memoriam, ad astra._

**Things that inspired this story:** The universality of loss; crowdworkers and crowdmarkets; how things might be during the transition to the machine minds.
