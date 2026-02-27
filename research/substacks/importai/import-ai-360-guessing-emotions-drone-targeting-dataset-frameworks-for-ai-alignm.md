---
title: "Import AI 360: Guessing emotions; drone targeting dataset; frameworks for AI alignment"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-360-guessing-emotions-drone"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Teaching machines to guess at our own emotions with FindingEmo:  
**_…~25,000 images to help machines figure out how we’re feeling about stuff…  
_ Researchers with KU Leuven have built and released FindingEmo, a dataset for teaching AI systems to classify the emotions of people in complicated photos. FindingEmo consists of 25,589 images, each annotated by one annotate with labels for eight primary emotions (and for each emotion, three different levels of intensity). There’s also a held back test set of 1525 images, each of which have been annotated by multiple annotators. The purpose of the dataset is to help researchers build AI systems that can “recognize the emotional state of individuals”.   
  
**Dataset emotions and composition:** “Each image in the dataset depicts multiple people in a specific social setting, and has been annotated for the _overall_ emotional content of the _entire_ scene, instead of focusing on a single individual,” they write.   
The images are annotated with Plutchik’s discrete Wheel of Emotions (PWoE), which “defines 24 primary emotions, grouped into 8 groups of 3, where emotions within a group differ in intensity”. The eight groups consist of: Joy, Trust, Fear, Surprise, Sadness, Disgust, Anger, and Anticipation (_funnily enough, all things one encounters in AI development itself!)._ A meta analysis of the labels shows ““joy” and “anticipation” being overrepresented, and “surprise” and “disgust” heavily underrepresented” which is in line with other broadly distributed emotion recognition datasets, they write.   
  
**Why this matters - teaching machines to model our own ‘hidden states’:** By creating datasets like FindingEmo, we’re essentially making it possible for AI systems to make better and more subtle inferences about now just what is happening in scenes but _how people feel about what is happening_. Besides having a range of uses for things like surveillance and advertizing, datasets like this will help increasingly sophisticated systems learn features for modeling the supposed internal states of the people they see and interact with.   
**Read more:**[FindingEmo: An Image Dataset for Emotion Recognition in the Wild (arXiv)](https://arxiv.org/abs/2402.01355).  
**Get the dataset here** : [FindingEmo (EAVISE, GitLab)](https://gitlab.com/EAVISE/lme/findingemo).  
  
***  
  
 **Google researchers break MoE models with a buffer overflow attack:  
**_…Proof-of-concept shows a determined attacker can poison behavior of an MoE model for many users…  
_ Google DeepMind researchers have shown how to poison Mixture of Experts models so that "an adversary can change the model prediction on data of other users who happen to be placed into the same batch." In other words, they've figured out how to get the behavior of MoE systems to change in a specific way, where in the demo example they change the output of an MoE in response to the prompt "Solve the following equation: 1+1=” from 2 to 1.   
  
**How the attack works** : "The adversary pushes their data into the shared batch, that already contains user data. As tokens get distributed across different experts, adversarial data fills the expert buffers that would be preferred by the user, dropping or routing their data to experts that produce suboptimal outputs," the researchers write. "The attack relies on two optimizations made by MoE: (1) the usage of expert buffer capacity limits, and (2) batch dependent expert routing assignments."  
  
**But don't worry:** Though the attack works in principle it assumes the attacker can see the logit outputs of the generation and it also "assumes the adversary can ensure their data is always grouped in the same batch as the target point". Both of these assumptions may not play out in widely deployed MoE systems.   
Additionally, MoE deployers can further mitigate the attack by randomizing the batch order, sampling from gate weights instead of selecting the top-k, and using a large capacity slack to make the overflow hard to achieve.   
  
**Why this matters - AI is software and software is hackable:** Papers like this highlight how AI systems are, much like any sophisticated computer software, hackable. As AI systems get deployed more widely, we're going to see more AI-native attacks get built where rather than try to compromise the system around the AI, attackers try to compromise the AI itself.   
**Read more:**[Buffer Overflow in Mixture of Experts (arXiv)](https://arxiv.org/abs/2402.05526).   
  
***  
  
 **Pack it up, people - AGI has been achieved:  
**_…Another installment of ‘extraordinary claims require extraordinary evidence…  
_ A researcher with startup Integral Mind says they have “created the first-ever Artificial General Intelligence (AGI) and first superintelligence”. The paper accompanying this announcement contains no tests or benchmarks nor any description of how the system has been trained. The reason for this is pleasingly tautological: “we derive the core requirements for AGI and present a computational paradigm meeting those requirements. Because we’ve met the requirements for AGI, AGI has been achieved”, they write. Well, ok then!  
  
**Why this matters - it doesn’t:** But sometimes it’s good to read research papers making outlandish claims just to calibrate your own ‘outlandish claim detector’.  
**Read more:** [Proof of Achievement of the First Artificial General Intelligence (AGI) Creators (Zenodo)](https://zenodo.org/records/10591677).  
  
***  
  
 **Chinese researchers build a dataset for overhead drone target tracking:  
**_…BioDrone is difficult and looks surprisingly similar to scary real-world drone uses…  
_ Researchers with the University of Science and Technology Beijing, the Chinese Academy of Sciences, Southeast University Nanjing, Stony Brook University, and University of Wisconsin-Madison, have built BioDrone “the first bionic drone-based visual benchmark for single object tracking (SOT)”.  
  
**What BioDrone is:** BioDrone’s main distinguishing features are a) the platform it was gathered by, b) the motion generated by the platform, and c) the very small size of the targets.   
On a), BioDrone was gathered via a flapping-wing drone. This induced b) “a major camera shake due to its aerodynamics”, and results in frames where things are moving around or blurred. On c), most of the shots are from extreme overhead angles with very small targets, all of which have been carefully annotated.   
**The BioDrone dataset:** The dataset is made of 600 videos with 304,209 manually labeled frames. “The sequence length varies from 300 to 990 frames, and the average length is around 507,” they write. “In the data acquisition process, we set different flight attitudes for various scenes under three lighting conditions“.  
All the tracked targets are annotated via bounding-boxes and also annotated if they’re occasionally occluded.   
  
**Why this matters - drone surveillance and warfare using discreet platforms:** It’s not discussed in the paper, but I find datasets like this interesting given the convergence of two existing trends in the world - a) the rapid maturity of low-cost drone warfare in the Ukraine-Russia conflict, and b) the arrival of increasingly stealthy drones that move via flapping their wings and can frequently seem more like birds than robots. Datasets like BioDrone are exactly the kind of thing you need to develop clever target identification systems that take advantage of both of these trends.  
**Read more** : [BioDrone: A Bionic Drone-based Single Object Tracking Benchmark for Robust Vision (arXiv)](https://arxiv.org/abs/2402.04519).  
**Get the dataset here:** [BioDrone (official project site)](http://biodrone.aitestunion.com/).  
  
***  
  
 **AI2 publishes some warts-and-all language models:  
**_…OLMo family tries to demystify the mysterious…  
_ The Allen Institute for AI has built OLMo, a family of “truly open” language models. The OLMo models are distinguished by the ‘warts and all’ publication strategy - along with the data and the research paper, Allen is also releasing hundreds of model checkpoints, letting researchers see the end-to-end process of training a model. The initial release includes models up to 7B in size and a 65B model is “still training”, per the paper.   
“OLMo releases the whole framework from data to training to evaluation tools: multiple training checkpoints across multiple hardware types, training logs, and exact datasets used, with a permissive license,” the researchers write. “This is the first step in a long series of planned releases, continuing with larger models, instruction-tuned models, and more modalities and variants down the line.“  
  
**Two types of computer:** Intriguingly, Allen also explored two different compute substrates for the project, the MosaicML cloud from Databricks, as well as the (AMD-based!) European LUMI supercomputer.   
  
**How well do the models do?** : In tests, the OLMo models have comparable results to those of other openly accessible, similarly sized models like Falcon and the MPT family.   
  
**Why this matters - warts are valuable:** The performance of the OLMo models isn’t that important relative to the openness with which they’ve been trained (similar to the BLOOM model which sought to replicate GPT3). By publishing what they’ve learned in the open (along with model artifacts), the researchers are going to help the broader research community better study language models.   
**Read more:**[Hello OLMo: A truly open LLM (Medium, AllenAI)](https://blog.allenai.org/hello-olmo-a-truly-open-llm-43f7e7359222).  
**More about OLMo** here: [OLMo: Open Language Model (Medium, AllenAI)](https://blog.allenai.org/olmo-open-language-model-87ccfc95f580).  
**Read the research paper** : [OLMo: Accelerating the Science of Language Models (AllenAI, PDF)](https://allenai.org/olmo/olmo-paper.pdf).  
**Get the model** from [here (OLMo, AllenAI, GitHub)](https://github.com/allenai/OLMo).  
  
***  
  
 **AI alignment is about human values just as much as safety - and here’s how to think about it:  
**_…Useful framework lays out how to convert qualitative properties into things we can quantitatively measure…  
_ In recent years, AI systems have got so good we’ve had to start worrying about their normative values. You didn’t need to care about the moral lens of a language model when it could barely complete a sentence. But now that LLMs work so well they’re being integrated across the economy, an increasingly large swathe of AI research is trying to think about their normative/moral alignment alongside their basic technical properties.   
To that end, new research from the University of Washington, Stanford University, MIT, and the Allen Institute for AI, lays out _A Roadmap to Pluralistic Alignment_. The motivating idea here is that “as a broader set of people use and rely upon AI systems, we need systems that can understand and cater to a broader set of needs,” the authors write. “In other words, we need systems that are _pluralistic_ , or capable of representing a diverse set of human values and perspectives.”  
  
**Three types of alignment** : They lay out three distinct ways of doing pluralistic alignment. These are:

  * **Overton pluralistic:** Where your AI system provides “comprehensive, high-coverage responses”. This requires “consideration of multiple heterogeneous judgements, encouraging deliberation over spontaneous judgment“. In practice, it means the system tries to acknowledge a bunch of different viewpoints in its response. 

  * **Steerably pluralistic:** Where the AI system has “an ability to be faithfully steered to represent particular attributes”,” they write. This means you can easily customize the system to a particular normative frame. 

  * **Distributionally pluralistic** : This is where the system embodies a “distributional representation of a population” - in other words, it faithfully represents the values of a target group of people. This is especially useful when your AI is “used to simulate, interface with, or otherwise model the views of a population“.




**Measures of pluralistic alignment:** If you’re trying to measure the normative values of your system, then what are the good ways to do that? Here they come up with three distinct evaluation approaches:

  * **Multi-objective:** This is simply where you have a bunch of disparate factors and you can measure if you’re improving overall or on a narrow subset of them. This is also how the majority of capabilities evaluation happens today because it’s dead simple. 

  * **Trade-off steerable:** This is where you look at your system in terms of a pareto frontier trading off against multiple factors _and_ you can measure how well you can shift the model along this frontier. 

  * **Jury-pluralistic:** This is the most complicated one - it’s where you have a benchmark “which separately and explicitly models a jury to maximize an overall welfare function”. In other words, you can look at not only the normative values of the system but how they relate to specific end-users. 




**Why this matters - AI systems are political artifacts so we need to measure their politics:** Frameworks like this help us understand how we can examine the political tendencies of AI systems - an increasingly tough and important task, especially as AI systems are deployed more widely. Ultimately, I expect AI systems will be assessed not only by their inherent technical capabilities, but also with reference to the political environment they’re being deployed into - whether that be at the level of detail of an individual, a small township, a country, a set of countries, or perhaps the world.   
**Read more** : [A Roadmap to Pluralistic Alignment (arXiv)](https://arxiv.org/abs/2402.05070).  
  
***  
  
 **Tech Tales:  
  
The Original Joe  
** _[The transport facility, 10 years post-uplift]  
  
_ My name is Joe but most people know me as The Original Joe. I’ve worked here for as long as I can remember. I’m the person that talks to you when you wake up and I’m also the person that helps you with your trip. They’ve looked into replacing me but it doesn’t seem like other people work as well.   
You’ve got the most human touch, said one of the administrators, when they explained the situation to me. No one does it quite like you, Joe, they said.   
  
I imagine this all sounds pretty funny to you, but trust me it’ll make sense soon enough. A lot of what I do is I get people comfortable with their journey. They always ask me what it’s like and I tell them I don’t know, I’ve never done it, because I’m The Original Joe, and they always get a kick at that.   
Wow, they said. Original original?  
Original original I say.   
There are a lot of questions after that, as you might expect.   
  
It’ll work like this - you’re going to talk to me a bunch and I’m going to try my best to understand you. Think of me as like a therapist and the only person I’m going to tell is the you that wakes up. Or like an architect where you’re telling me about the house of your dreams and I need to build it for you. I get as much as I can and at some point one of my administrators will tell me that we’ve got enough, and then it’ll be time for you to go on your trip.   
  
Just a warning - you are naked. Something to do with the scanner I guess. I kind of like it, the way you go on your journey just like how you started your journey here. After they scan you you’ll be on your way and then I suppose you wake up twice - you wake up here and I’m going to be here, and you wake up somewhere else and whoever is over there will explain things to you.   
  
I’m not exactly sure who is over there. I know they have different systems at different generations. But I’m told it’s kind of like me - someone who’s seen a lot and understands how it all works. And they’ll have my report so they’ll already have a sense of you. I’m told sometimes they look like me and sometimes they look different, but that’s all up to whatever rules they follow over there. It doesn't matter because you don’t remember much - that’s part of how the journey technology works, you’re kind of new. You can read and talk and all that stuff - tie your shoes, use the interfaces. But you’ll not really remember anything. People have said it’s like waking up and knowing you just had a really detailed dream but not knowing the details - you’ll know something about the texture.   
  
And here? Here it’s the same. But instead of having whatever new life you’re heading to, you have kind of the same life here. I end up having to explain to you how you were - how we talked, just as we are now, and how you still went through with it, and what your new life means. The dos and don’ts and all of that.   
  
You’ll probably ask me if I took the same journey as you and I’ll say: I’ve been here as long as I can remember.   
  
**Things that inspired this story:** Various notions of the afterlife as being a return to some greater story we have forgotten; ideas about packaging up minds and shipping them off as information and what the dehydration and rehydration process might require to avoid nasty side effects; what a computer-run society might look like and where people wind up in it; the permanence and impermanence of our reality; goddamnit there’s only one rule - you’ve got to be kind!
