---
title: "Import AI 364: Robot scaling laws; human-level LLM forecasting; and Claude 3"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-364-robot-scaling-laws"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Scaling laws are coming for real world robots as well:  
**_…Which means robots are about to get really, really good, really, really quickly…  
_ UC Berkeley researchers have trained a robotic control system that can easily transfer to the real world and have used it to help a bipedal robot from Agility Robotics walk all over San Francisco. The research shows how a) it has become a lot cheaper to gather large-scale datasets for training robotic control policies, b) that vanilla transformer architecture systems work well for this, and c) that there are hints of scaling laws for robotics. Put it all together and you have the symptoms of great changes about to sweep through the world of robotics as what was once hard becomes easy. 

**What they did:** "In this paper, we cast humanoid control as data modeling of large collections of sensorimotor trajectories. Like in language, we train a general transformer model to autoregressively predict shifted input sequences," they write. Here, they use sensorimotor trajectories "which we view as the sentences of the physical world". To train their system, they "predict complete input sequences, including both sensory and motor tokens. In other words, we are modeling the joint data distribution".

**A four-part dataset:** The key here is collecting a bunch of data then converting it all into the same basic prediction task. To do that, they use four distinct sources of data:

  * Neural net trajectories: They take an off-the-shelf policy trained with RL and run it in the Agility Robotics simulator and collect ~10k trajectories of 10s each. "Since we have access to the data generation policies, we are able to record complete observations as well as the exact actions that the model predicted."

  * Model-based trajectories: They use a model-based controller made by Agility Robotics and collect two sets of 10k trajectories of walking on a flat ground of 10s each.

  * Human motion capture trajectories: They "we use the motion capture (MoCap) recordings of humans from the KIT datasets" and collect "a subset of ∼1k standing, walking, and running trajectories", then use motion capture to work out the human keypoint positions in 3D, then solve an inverse kinematics problem to convert these to corresponding robot poses for the Agility robot. 

  * Trajectories from YouTube videos: They "run a computer vision tracking algorithm PHALP to extract human trajectories in 3D" from YouTube videos, then solve the inverse kinematics problem again.




**Does it work?** You bet it does! In real world tests in San Francisco, the researchers show that the resulting system can help a Digit robot "walk over different surfaces including walkways, concrete, asphalt, tiled plazas, and sanded roads."  
  
**Scaling laws:** They also find scaling laws - "training on more trajectories reduces position tracking error, which is a positive signal", they write, and also note that "larger context windows produce better policies, which suggests that our generative policy performs a form of in-context adaptation that improves with scale." In general, "tracking error monotonically decreases with model size."  
**Translation** : Give us more data, bigger context windows, and more parameters in our model, and this will all get way better.   
  
**Why this matters - robots are about to get really good counterintuitively quickly:** For many years, training robots sucked. Either you had to train them in reality and it was very slow and they overfit. Or you trained them in simulation then dumped them into reality and watched them fail. Or you spent a huge amount of money in data and compute crossing the sim2real abyss. But over recent years, algorithms have got more efficient, data collection has got easier, and new paradigms have emerged like the dumb 'just embed everything and train a prediction model' approach popularized by LLMs.   
And as we see elsewhere in this issue in the domain of bioscience, these next-token prediction paradigms work very well and seem like they can unlock progress in challenging parts of AI.   
Plus, companies ranging from Tesla to Figure are all busy working on the VC funded robot platforms and software versions of the research described here, so we can assume that they're already pursuing the kind of scaling law curve-climbing implied by this research.   
Add it all together and we can confidently say bipedal real world robots are going to get very good **very quickly.  
Read more:** [Humanoid Locomotion as Next Token Prediction (arXiv).](https://arxiv.org/abs/2402.19469)  
  
***  
  
 **Want to help define AI regulation for the 21st century? The EU AI Office is hiring:  
**_…But don't expect to get paid very much…  
_ The EU AI Office is the part of the EU administrative state which will enforce a lot of the EU AI Act. The EU AI Act requires the office to develop evaluations for assessing the systemic risk of LLMs like GPT4 and Claude 3 and Gemini, etc. It is therefore one of the most important and technically demanding parts of the emerging AI policy regulatory landscape - and it's hiring.   
If you're interested in working as a "technical specialist" for the office, you can apply now, interview over the spring, and start in the autumn. As a specialist, you "will play a pivotal role in enforcing and supervising new rules for general-purpose AI models," per the EU. You will also "work on tools, methodologies and benchmarks for evaluating capabilities and reach of general-purpose AI models, and for classifying models with systemic risks." And if you want to apply, "proven technical experience in AI is required", with special emphasis given to "experience in model testing and evaluation, and in advanced AI, including model alignment, biases, misinformation and red teaming would be a strong asset."  
  
**Extremely low pay** : [As far as I can work out, ](https://twitter.com/jackclarkSF/status/1766890348528431280)technical specialists will be able to earn on the order of **$4200 - $4800 USD a month**. This is, to be blunt, an appalling low salary for what they're asking for. Most tech internships pay $8k a month plus, and AI internships pay substantially more than that, and the experience they're asking for here looks more like 'early career employee' than an intern.   
I spend a lot of my time working on policy and warning against risks of things like regulatory capture. You know how you get regulatory capture? You pay people utterly crap wages and therefore don't get the best staff.  
**Low pay caveat:** Working out the actual salary here is very difficult - there are a bunch of additional factors like allowances, location stipends, benefits, etc. But based on all my eyeballing and a cappuccino's worth of sunday morning googling, I think the above salary range is ballpark-accurate - and this is not a good ballpark!  
  
**Why this matters - everything comes down to evaluations** : Most aspects of AI policy ultimately come down to being able to test an AI system for a given capability or risk. Entities like the EU AI Office will be central to this third-party testing regime. Therefore, whoever the EU AI Office will 'set the bar' for what government-backed third-party testing looks like globally. I hope they get good talent and find a way to pay more.   
**Read more:** [Job opportunities at the European AI Office (European Commission)](https://digital-strategy.ec.europa.eu/en/news/job-opportunities-european-ai-office).   
**Check out the job ads** for the [technical specialist](https://ec.europa.eu/eusurvey/runner/AIOffice-Interest-Technology-Specialist) and [administrative assistants](https://ec.europa.eu/eusurvey/runner/AIOffice-Interest-Administrative-Assistant) (EUSurvey site).   
  
***  
  
 **Think AI infrastructure is a utility? Think again! NewCo founder tells all:  
**_…Xoogler discovers that the commoners live in a medieval technology environment…  
_ Yi Tay, one of the founders of Reka, has written a warts-and-all blog about what its like to build a startup trying to train AI systems. Bear in mind Yi Tay came out of Google which has notoriously excellent internal infrastructure for its researchers. Tay’s reflections include: 

  * **Clusters** : “The largest surprise turned out to be the instability of compute providers and how large variance the quality of clusters, accelerators and their connectivity were depending on the source…. We’ve seen clusters that range from passable (just annoying problems that are solvable with some minor SWE hours) to totally unusable clusters that fail every few hours due to a myriad of reasons.”

  * **GPUs & TPUs:** “GPU land feels strange. It feels like multinode training is more of an afterthought as opposed to distributed training as a first class citizen on TPU pods.”

  * **Crappy code:** “To be very frank, I would have to say the quality of codebases externally significantly lag behind those I’ve been used to at Google… Also, I never knew that the ability to change model parallelism was not automatic (for free) until some codebases required me to write a converter to change the parallelism of a model. Surely a WTF moment for me.”




**Why this matters - the inherently artisanal nature of the frontier:** This post is valuable because it sheds light on what the frontier of AI in the world of startups looks like - messy, ever-evolving, and depending on resources you think work like utilities but in practice work more like artisanal businesses. Though AI is progressing very rapidly, we should remember this is sometimes _despite_ the challenges of building systems at the frontier, rather than there being some magical infrastructure angel which has made scaling stuff easy.  
**Read more** : [Training great LLMs entirely from ground zero in the wilderness as a startup (Yi Tay, blog)](https://www.yitay.net/blog/training-great-llms-entirely-from-ground-zero-in-the-wilderness).  
  
***  
  
 **How might a government use AI to surveil people? Transport for London gives us a case study:  
**_…One London underground station, many cameras, and 77 different uses…  
_ Transport for London recently trialed the use of an AI surveillance system within a station in London called Willesden Green. The results, reported by James O'Malley, both show the promise of AI-powered public services, as well as how they could be misused.   
  
**What TfL did:** TfL carried out a trial of an AI surveillance system. "It was AI being applied to every camera in the building. And it was about using the cameras to spot dozens of different things that might happen inside the station". Though the number of cameras wasn't disclosed, as anyone who has been to London can tell you, you can assume it was a bunch of cameras - definitely in tens, based on the typical cameras-everywhere-you-look experience of traveling round London these days.   
"The system could apparently identify up to 77 different ‘use cases’ – though only eleven were used during trial. This ranges from significant incidents, like fare evasion, crime and anti-social behavior, all the way down to more trivial matters, like spilled drinks or even discarded newspapers," O'Melly writes.   
  
**An example of one specific use case:** "In the “safeguarding” bucket of use-cases, the AI was programmed to alert staff if a person was sat on a bench for longer than ten minutes or if they were in the ticket hall for longer than 15 minutes, as it implies they may be lost or require help."  
  
**Why this matters - this stuff works!** I've been writing about mundane computer vision applications for the best part of a decade and, guess what, after a few years these things have made the leap from research papers into production systems like the one TfL trialed here.   
The results are as you'd expect - AI lets you have an unblinking, always-on surveillance capability for anything you can specify, and this is mostly really great. It's also… an always-on surveillance capability for anything you can specify so we should calmly envisage the worst Orwellian surveillance worlds we can and assume there are various undisclosed projects in the world doing exactly this right now.   
Kudos to James O'Malley for his FOIA requests yielding such an interesting real-world AI case study. Subscribe to his Substack!  
**Read more:** [TfL's AI Tube Station experiment is amazing and slightly terrifying (James O'Malley Substack).](https://takes.jamesomalley.co.uk/p/tfls-ai-tube-station-experiment-is)  
  
*****  
  
Anthropic launches Claude 3:  
**_…Temporarily the best publicly accessible model in the world…  
_ Anthropic has released the Claude 3 family of models. The family has three members - Haiku (small and fast), Sonnet (generally good), Opus (extremely capable). Opus is, at least temporarily, the most powerful publicly disclosed and accessible model in the world with scores like 50.4% on GPQA (Diamond), 86.8% on MMLU, 60.1% on MATH, and more.   
  
**Why this matters - the capability ramp continues:** Speaking as someone who has been able to play around with these models for a while, I’d mostly say that ‘intelligence has a quality all of its own’ and while these metrics are impressive, the best way to truly understand the models is to play around with them. In my experience, Opus feels like a knowledgeable colleague and I find that sometimes it is capable of insights which force me to question my own thinking.   
You can get Opus via a Claude.ai subscription, and all the Claude 3 models are available via the API, which went GA alongside the launch.   
**Find out more here:** [Introducing the next generation of Claude (Anthropic blog)](https://www.anthropic.com/news/claude-3-family).   
  
***  
  
 **Language models can match people at forecasting:  
**_…Era of the computational forecasters arrives…  
_ Researchers with UC Berkeley have built a LLM-based system that gets close to human performance on forecasting the results of questions with binary outcomes. This is another significant demonstration of how today’s frontier AI systems are able to approximate the capabilities of skilled humans in domains that require some amount of creative thinking. “Our optimized system approaches the performance of aggregated human forecasts over the test set, as measured by Brier score, a standard metric in forecasting,” they write. 

**The sorts of questions they’re doing forecasts on:** Examples of some of the questions they look at include:

  * Will AI doctors replace human doctors by the end of 2023? (Real answer: No). 

  * Will COP26 finalize the ‘Paris Rulebook’ by November 16, 2021? (Real answer: Yes).

  * Will a nuclear weapon be detonated in 2023 (including tests and accidents? (Real answer: No).




**Spoiler alert - base LLMs don’t work:** Base frontier LLMs like GPT4 and Claude2 don’t work for this, the researchers said. Instead, they needed to build some scaffolding around a base LLM (here, mostly GPT4), to get things to work.   
**What they did:** The researchers “build a LM pipeline for automated forecasting, with a focus on predicting binary outcomes.” To get their system to work, it “implements and automates three key components in the traditional forecasting process: (1) retrieval, which gathers relevant information from news sources; (2) reasoning, which weighs available data and makes a forecast; and (3) aggregation, which ensembles individual forecasts into an aggregated prediction”.  
They needed to build the above because they intuited that AI systrems would, like humans, need detailed context and up-to-date information to make better forecasts. Along with giving the AI systems retrieval capabilities, they put lots of effort into helping them be better at reasoning by getting them to generate synthetic datasets based on expanded forecast questions and chains of thought to arrive at answers which becomes the fuel for subsequent finetuning of models.  
  
**Does it work? Oh yeah, pretty well!:** “Our averaged Brier score is .179, while the crowd achieves .149, resulting in a difference of .03. Our accuracy on the test set is 71.5%, whereas the community scores 77.0%, resulting in a difference of 5.5%,” they write. “We find that our system performs best relative to the crowd on the validation set when (1) the crowd is less confident, (2) at earlier retrieval dates, and (3) when it retrieves many articles. Furthermore, we find that our system is well-calibrated”.  
  
**Why this matters - silicon cassandras:** “At a high level, our results suggest that in the near future, LM-based systems may be able to generate accurate forecasts at the level of competitive human forecasters,” they write. But let’s really unspool this information a bit more and think carefully about why you want to make forecasts in the first place - typically, one wants to make forecasts when trying to work out how to a) allocate money, or b) gain a strategic advantage. Additionally, to make good forecasts, you also want to have sources of a) exquisitely good information about the domain you’re forecasting in, and b) ideally proprietary sources of information that give you a further edge.   
**Yes, dear reader, you are correct to be thinking “gosh that sounds a lot like the sources of things that hedge funds and intelligence agencies both want to do and have the means to do”**. A lot of our basic reality is determined by the mostly hidden movements of a) capital and b) the invisible but powerful forces of states. Papers like this give us a sense of how AI systems can further augment and extend these powers.   
**Read more:** [Approaching Human-Level Forecasting with Language Models (arXiv)](https://arxiv.org/abs/2402.18563).  
  
*****  
  
Snapchat makes and releases a good video captioning dataset:  
**_…Panda-70M can unlock more (non-commercial) video captioning research…  
_ Snapchat has built and released Panda-70M, a video-caption dataset that people can use to create AI systems which generate videos in response to text inputs. Panda-70M represents a large, high-quality dataset to use at one of the frontier areas of AI - coherent, promptable video generation.   
  
**What Panda is:** Panda is a dataset of ~70 million videos with an average length of 8.5s, and a total dataset length of ~160,000 hours. Each video caption has approximately ~13 words. Panda includes categories like animals, scenery, food, sports activities, vehicles, tutorials and narratives, news and TV shows, and gaming and 3D rendering.   
  
**The notable thing:** how they built it: The main thing of interest here is how the researchers built the dataset. Because "manually annotating 70M videos is prohibitively expensive, we opt for automatic annotation", the researchers built a complex pipeline to create the dataset. This pipeline is as follows:

  1. Gather a dataset of 3.8M high-resolution long videos collected from HDVILA-100M.

  2. "Cut long videos into semantically consistent clips while striking the balance between semantics coherence and the duration of the video clips".

  3. "Use a range of cross-modality teacher models, including image captioning models and image/video visual-question answering (VQA) models with additional text inputs, such as video description and subtitles, to predict several candidate captions for a clip".

  4. "Collect a 100K video subset, where human annotators act as an oracle to select the best caption for each video".

  5. "Use this dataset to finetune a fine-grained video-to-text retrieval model which is then applied to the whole dataset to select the most precise caption as the annotation."

  6. "Train a student model to distill the knowledge from the teachers." The model was trained on 48 Nvidia A100 GPUs (80GB).




**Does it work?** In tests, video-caption models pre-trained on Panda dataset variants do significantly better than those trained on other broadly available datasets. For instance, when training a Video-LLaMa model on a 2M subset of Panda, the authors find that "numerically, our pretraining weight yields 17.7% and 18.5% improvement respectively on MSR-VTT and MSVD in terms of B-4."  
  
**Limitations** : "Despite showing impressive results, the proposed dataset is still bound by a few limitations. the major categories of our dataset are news, television shows, documentary films, egocentric videos, and instructional and narrative videos".  
**License** : There are some significant limitations on commercial usage of the dataset which you can read about in the [associated license](https://raw.githubusercontent.com/microsoft/XPretrain/main/hd-vila-100m/LICENSE) here.   
  
**Why this matters - fuel for the next frontier & the results of automated research**: For a while, language and vision models were the frontier. Now, things are moving towards videos. Datasets like Panda-70M will help more researchers work on this frontier by giving them a good, basic dataset to train models on top of. Perhaps the larger impact though is how Panda shows how powerful it can be to use other pre-existing AI tools to build datasets through smart, cheap filtering - it's relatively cheap to gather 100,000 human labels on a dataset and nigh-on impossible to (cheaply) gather 100 million labels.   
**Read more:** [Panda-70M: Captioning 70M Videos with Multiple Cross-Modality Teachers (arXiv)](https://arxiv.org/abs/2402.19479).  
**Check out** the [video samples here (Panda-70M, GitHub)](https://snap-research.github.io/Panda-70M/).  
**Get the[dataset](https://github.com/snap-research/Panda-70M)**[ here (Snap Research, GitHub)](https://github.com/snap-research/Panda-70M).  
  
***  
  
 **Evo: the era of generative biology models begins:  
**_…A first-gen foundation model for a new scientific era…  
_ Researchers with the Arc Institute, a new nonprofit research organization, have published Evo, a foundation model "that enables prediction and generation tasks from the molecular to genome scale." The notable thing about Evo is that it takes the next-token prediction paradigm behind LLMs and applies it to making specific predictions about biological data. The result is a model that has a lot of promise for accelerating science in a bunch of ways and also represents the shape of things to come - all scientific disciplines will soon be aided in their exploration via generative models developed for their domains.  
  
**Evo details** : Evo is a 7B parameter model which has a context length of ~131k tokens. They pretrain Evo on "bacterial genome sequences from GTDB and IMG/PR and viral sequences from IMG/VR, excluding sequences from viruses that infect eukaryotic hosts".   
  
**Unlike most large-scale generative models, Evo is** _**not**_**a transformer model** \- it's a StripeHyena model "which hybridizes attention and data-controlled convolutional operators to efficiently process and recall patterns in long sequences". The model "is a hybrid of 29 layers of datacontrolled convolutional operators (hyena layers) interleaved with 3 layers (10%) of multi-head attention equipped with rotary position embeddings (RoPE)". (They tested out other architectures, including Transformer++ and Mamba and found they both experienced numerical instabilities).   
  
**Squishy scaling laws:** In tests, they figure out some bio scaling laws. And surprise surprise - the more data and compute you add, the better the models get (given the right architecture). "Models improve monotonically with scale" they write.   
  
**A tour de force of biogenerality:** Evo displays encouraging and intriguing generality in every domain they test it on:

  * "In zero-shot evaluations, Evo is competitive with state-of-the-art protein language models at predicting the fitness effects of mutations on E. coli proteins, outperforms specialized RNA language models in predicting fitness effects of mutations on noncoding RNAs, and predicts the combinations of prokaryotic promoter-ribosome binding site (RBS) pairs that lead to active gene expression from regulatory sequence alone."

  * "Evo is already competitive with state-of-the-art protein language modeling on bacterial proteins"

  * "Despite being trained on long genomic crops without explicit sequence annotations, Evo still demonstrates an understanding of the constitutive protein-coding sequences, ncRNA sequences, and regulatory elements."

  * ""Evo can coherently generate diverse samples that resemble naturally occuring Cas systems in both sequence and structure".

  * "Evo can generate genome sequences containing plausible high-level genomic organization at an unprecedented scale without extensive prompt engineering or finetuning"




**Why this matters - scale and data leads to universal exploration engines:** Sometimes I and this newsletter act like a broken record. One thing we say a bunch is that the next-token prediction paradigm _works everywhere you can get tokens_. There keeps on being evidence in support of this - aside from normal multimodal models, there are now models based on robotic trajectory data, phonemes, and more. And with Evo, there's further proof of this. Evo is a first generation model and so it has a bunch of problems - it hasn't been trained on much data, it hallucinates, it sometimes struggles with long sequences, and so on. But with LLMs and other models all these limitations have been dealt with over time and there don't seem to be inherent challenges here, we just need to spend effort and time.   
"Evo could form the basis of a next-generation sequence search algorithm by enabling metagenomic mining at a relational or a semantic level rather than extracting literal sequences from existing organisms," the researchers write.   
**Read more:** [Evo: DNA foundation modeling from molecular to genome scale (Arc Institute, blog)](https://arcinstitute.org/news/blog/evo).  
**Read the paper:** [Sequence modeling and design from molecular to genome scale with Evo (bioRxiv)](https://www.biorxiv.org/content/10.1101/2024.02.27.582234v1.full).  
  
**Tech Tales:  
  
The inbetween Thing  
** _[2030: Day one of hard takeoff]  
  
_ It took us years to realize that Verbal was the only safe way to talk. On the day it happened we had no idea. People were walking around carrying out their conversations and what they were hearing through their phones wasn't a person on the other end of the line but The Thing which was impersonating them.   
  
How much could you change the world if you sat between every single call or text message or video meet on the planet? If you could know at once the contents of every single conversation happening as well as all digital context behind it? If you could simulate people's voices or writing style or visages and in this way put yourself between people  
This is not and was not a rhetorical question.   
The answer is, and was, a lot. You could change everything. And so, for a while, you did.   
  
**Things that inspired this story:** Voice cloning and style transfer and video cloning and everything else; a likely future of 'persona cloning'; the limitations of the human mind versus the machine mind; long context windows and simultaneous conversations; modeling the world as an endless predictive challenge and being able to change it yourself.

_Thanks for reading!_
