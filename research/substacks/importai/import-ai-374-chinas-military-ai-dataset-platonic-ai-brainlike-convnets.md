---
title: "Import AI 374: China's military AI dataset; platonic AI; brainlike convnets"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-374-chinas-military-ai"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Berkeley researchers discover a suspiciously military-relevant Chinese dataset:  
**_…Oh you know just a normal dataset exclusively of military vessels with bounding boxes around their radar systems. Normal stuff!...  
_ UC Berkeley researchers have found a Chinese dataset named 'Zhousidun' (translation: 'Zeus's Shield'). The dataset is highly unusual and highly specific and consists of "608 oblique and satellite images of American Arleigh Burke-class destroyers and other allied destroyers and frigates" with bounding boxes drawn around "the ships' radar systems (which are part of the Aegis Combat System)...bounding boxes have been drawn around SPY radars on the superstructure, one on port and one on starboard, as well as around the vertical launching systems towards the bow and towards the stern of the ship."  
  
**What is going on and where did they find it?** The researchers found the dataset on Roboflow, a US company which hosts ML data and models (similar to HuggingFace) - at the time of writing, it [was still available](https://universe.roboflow.com/shanghaitech-faxfj/zhousidun_model2/model/1?image=https%3A%2F%2Fsource.roboflow.com%2FhkIFQ0FeReVxgF0uEKnlcRYj51i2%2Fc1Dpc7q1Xs5NNhK9blk7%2Foriginal.jpg). There are many reasons people could create this dataset, ranging from individual researchers with an odd fascination with US military equipment to a larger research effort with more detailed military links. The researchers suspect the latter - "due to the targeted, military nature of the dataset and the likely academic origins of the account sharing it, we suggest that it is likely that this dataset was accidentally published."  
  
**Is it actually useful?** 608 is a relatively small dataset - the Berkeley researchers validate this by training a YOLOv8 model on it and then test out its success rate at identifying radar pictures on ships. The results are ok - training on the dataset provides a minor but not significant improvement. However, as they note, you could easily use this dataset to prototype approaches which you then apply to a much larger and more sophisticated dataset - one you might (I'm speculating) gather via drones and planes and other things you might use to gather intel on ships like this especially in places like the South China Sea.   
"Overall, a model trained on Zhousidun has limited targeting capabilities in the real world. It is unlikely that any military would field a model with these performance characteristics. However, it is extremely interesting that training on a small set of unconstrained, publicly available imagery offers such a great starting point to building a robust targeting model," they write.   
  
**Why this matters - we should expect AI to get used for everything:** For a few years, the US Defense Innovation Unit (DIUx) has been running the 'xView' challenge series, whose latest competition (xView 3) tries to get people to develop computer vision models that can spot [unregulated fishing vessels](https://www.diu.mil/ai-xview-challenge). Obviously, algorithms that get good at this might have 'dual-use' applications similar to those implied by Zhousidun. But it's very rare to see a dataset come out which is so 'on the nose' - Zhousidun is a dataset which has no purpose other than to draw bounding boxes around specific military hardware on specific military vessels. Surprising? No. Striking to see it in the open? Yes! A taste of things to come? Yes.   
**Read more:**[Open-Source Assessments of AI Capabilities: The Proliferation of AI Analysis Tools, Replicating Competitor Models, and the Zhousidun Dataset (arXiv)](https://arxiv.org/abs/2405.12167v1)**.  
  
***  
  
Want a better DSL to help you write GPU kernels? Try ThunderKittens:  
**_…Stanford discusses the dark arts of GPU programming…  
_ Most aspects of AI are defined by software rather than hardware - you specify your hyperparameters and use nicely abstracted training code like PyTorch and set jobs training then wait to see how your model performs. But as anyone working in AI knows, there are entire teams of people whose job is interfacing with the hardware - the most mysterious of these jobs are the people tasked with improving the efficiency of the computers used to train AI. To that end, Stanford's Hazy Research lab has published a fun post called 'GPUs Go Brrr' where the lab shares some of the lessons it has learned about getting good performance out of GPUs.   
  
**Notable quote:  
**_Great, how do I make it go brr?  
_ Keep the tensor core fed. That’s it.  
_Wait, really?  
_ Yes. That’s the game.  
  
**ThunderKittens compiler:** Hazy Research has also released ThunderKittens, software to help people write more efficient GPU kernels. It has also released some of the kernels it has built with ThunderKittens.  
  
**Why this matters - minute improvements matter a lot at scale** : AI hardware is still wildly unoptimized, both from a basic design point of view (e.g, though lots of people use GPUs together, Google and Amazon are rapidly innovating on chips more specialized for AI training and inference like TPUs and Trainium) as well as at the software interface layer (e.g., kernels). Combine that with the fact that frontier training runs now cost easily above $100 million and it's clear that relatively small optimizations in areas like kernels could lead to massive savings, so it's worth keeping track of this space.   
**Read more:**[GPUs Go Brrr (Hazy Research)](https://hazyresearch.stanford.edu/blog/2024-05-12-tk).   
**Download** [ThunderKittens here (Hazy Research, GitHub)](https://github.com/HazyResearch/ThunderKittens).  
  
*****  
  
Microsoft releases a search engine dataset:  
**_…MS MARCO can help to see if AI will replace traditional methods in web search…  
_ Microsoft has released MS MARCO Web Search, a dataset pairing web pages with queries associated with them. Datasets like MS MARCO can help people benchmark search engines or even develop their own.   
  
**What it contains: MS MARCO** "incorporates the largest open web document dataset, ClueWeb22, as our document corpus. ClueWeb22 includes about 10 billion high-quality web pages, sufficiently large to serve as representative web-scale data," Microsoft writes. "It also contains rich information from the web pages, such as visual representation rendered by web browsers, raw HTML structure, clean text, semantic annotations, language and topic tags labeled by industry document understanding systems, etc. MS MARCO Web Search further contains 10 million unique queries from 93 languages with millions of relevant labeled query-document pairs collected from the search log of the Microsoft Bing search engine to serve as the query set."  
  
**Queries:** The queries are pre-filtered "to remove queries that are rarely triggered, contain personally identifiable information, offensive content, adult content and those having no click connection to the ClueWeb22 document set. The resulting set includes queries triggered by many users, which reflects the real query distribution of a commercial web search engine."  
  
**Three challenging search puzzles** : Alongside the dataset, Microsoft has also developed three distinct challenges that leverage it - one to test out how good embedding models are at ranking documents in response to a query, another for testing out how well embedding models work with an embedding retrieval system, and a third for testing out end-to-end retrieval (aka, use any technology, just try to get good at search).  
  
**Why this matters:** Datasets like MS MARCO are going to help people to test out new AI methods for large-scale real world web search tasks, which is helpful for figuring out how good the recent crop of AI-inflected search systems are.   
**Read more:**[MS MARCO Web Search: a Large-scale Information-rich Web Dataset with Millions of Real Click Labels (arXiv)](https://arxiv.org/abs/2405.07526).  
**Get the dataset here** : [MS-MARCO-Web-Search (Microsoft, GitHub)](https://github.com/microsoft/MS-MARCO-Web-Search).  
  
*****  
  
Just how the heck do states share nuclear safety technologies with one another?  
**_…What lessons does nuclear non-proliferation have for AI safety?...  
_ How has the United States tried to share nuclear safety technology with other states and what lessons does this hold for other domains? That's the topic of a fantastic paper by George Washington University researcher Jeffrey Ding _Keep your enemies safer: technical cooperation and transferring nuclear safety and security technologies._ Based on four case studies - two successful cases of the US sharing nuclear safety tech with the USSR and, later, Russia, and two mostly unsuccessful attempts to share with China and Pakistan - the paper highlights how sharing details about sensitive technologies depends on: a) the level of friendliness and awareness between the scientists in each country, and b) how the safety tech may leak information which changes potential escalation dynamics.   
  
**Permissive Action Links (PALs):** The main tech in quesiton here is a Permissive Action Link (PAL) - tech for ensuring that nuclear weapons can't be accidentally detonated. PALs vary in complexity from ones pretty much divorced from the workings of the warhead to ones which couple more directly with it and encode more information. This makes some types of PALs easier to share than others.   
"Consider a simple illustration from the civilian domain. If one party seeks to transfer automobile safety technologies to another party, the process is very different for automatic emergency braking systems than seatbelts. Whereas the latter can be successfully transferred by sharing the general concept of a seatbelt, transferring the former demands more comprehensive discussions between engineers from both parties," Ding writes. "Nuclear safety and security assistance in more complex technologies must strike a delicate balance: share substantial amounts of tacit information but refrain from exposing sensitive information about one’s own nuclear weapons system".  
  
**Key considerations in sharing tech:** One key consideration, covered above, is about leaking information - this was one reason why the US didn't share stuff with Pakistan as it was skeptical it had the security systems in place to keep that information secret within Pakistan.   
Another key consideration is whether by sharing the tech you make states more confident in their weapons and more likely to a) take escalatory moves, and b) build bigger and more frightening bombs. "It is possible that sharing safety and security technologies encourages other countries to adopt dangerous systems. If fear of accidents and unsanctioned launches deters nuclear ambitions, then providing nuclear assistance could signal to other states that help with controlling the bomb would be forthcoming, thereby incentivizing them to seek nuclear arsenals," Ding writes. "Nuclear assistance to other states may encourage them to adopt risker nuclear postures, such as by mating warheads and delivery system".  
  
**Why this matters - lessons for the AI safety community:** As governments content with proliferation risks and safety tradeoffs from technologies like AI, it's worth learning lessons from the history of nuclear proliferation. The main takeaways here include:

  * Give your scientists many opportunities to socialize with one another, develop trust, and share tacit and informal knowledge - these can pay dividends in surprising ways. "Transfers of complex nuclear safety and security technologies depended on trusting relationships that had developed between US and Russian experts," Ding writes. The basis for many of these relationships was the 1988 Joint Verification Experiment (JVE), in which Soviet and American nuclear weapons scientists visited each other’s labs to test verification techniques for the Threshold Nuclear Test Ban Treaty… many of the key participants in [Russia-US sharing in the 90s] were alumni of the JVE and earlier lab-to-lab cooperative programs"

  * Closely analyze the technology you're sharing in terms of the information hazards it encodes - if you can explain a safety idea without touching on a capability idea, then that's good. If your safety idea requires a precise understanding of some capabilities, then it's going to be harder. 

  * Timing matters - changes in politics both at home and abroad can make it much harder to be seen to coordinate or help one another at all, so note when you're in a window where sharing is possible and try really hard, because you have no idea how long that window will be open. 




**Read more:**[Keep your enemies safer: technical cooperation and transferring nuclear safety and security technologies (Jeffrey Ding’s website, PDF)](https://jeffreyjding.github.io/documents/Keep%20Your%20Enemies%20Safer%20EJIR%20Accepted%20Version%20April%202024.pdf).  
  
***  
  
 **Platonic AI: as we make AI systems bigger, they arrive at similar ways to represent reality:  
**_…Enticing evidence for the idea that AI systems get better in relation to breadth and scale…  
_ Some MIT researchers have shown that as we scale up AI systems, different systems trained in different ways end up having a similar representation of reality. They call this the 'Platonic Representation Hypothesis' and the essential idea is that there are only so many ways to represent the world around us, so we should expect that as systems get more capable (aka, smarter), their representations of reality should look more similar than dissimilar. They do some experiments which bear this out.   
"We argue that there is a growing similarity in how datapoints are represented in different neural network models. This similarity spans across different model architectures, training objectives, and even data modalities," they write. "Our central hypothesis is that there is indeed an endpoint to this convergence and a principle that drives it: different models are all trying to arrive at a _representation of reality_ , meaning a representation of the joint distribution over events in the world that generates the data we observe".  
  
**Circumstantial evidence for the claim** : The researchers compare and contrast the performance of 78 distinct vision models built via a range of architectures and trained using a variety of resources (from cheap models to relatively expensive ones, like the 70b parameter LLaMa 3 series). They find that:

  * Models that solve more VTAB tasks tend to be more aligned with each other. 

  * Multimodal alignment ("The results show a linear relationship between language-vision alignment and language modeling score, where a general trend is that more capable language models align better with more capable vision models".




**What the results mean:** "The results indicate that models with high transfer performance form a tightly clustered set of representations, while models with weak performance have more variable representations," they write. This leads to the hypothesis that, "As we train more general models that solve more tasks at once, we should expect fewer possible solutions."  
  
**Why this matters - more evidence that bigger models are better at approximating the world we exist in:** Research like this adds weight to the idea that as we make AI systems larger, they get sufficiently good at representing the world that they eventually converge with the world. It also further suggests that the larger (and therefore more expensive) AI systems have much richer and more reality-like views on the world than the small ones, which helps explain why larger models seem to have lower rates of hallucination than smaller ones.  
**Read more:**[The Platonic Representation Hypothesis (arXiv)](https://arxiv.org/abs/2405.07987).  
  
***  
  
 **Convnets are more brainlike than transformers:  
**_…Architectural biases help us better understand the brain…  
_ Convolutional neural networks have some architectural biases that let them effectively approximate the behavior of primate visual cortexes, compared to other types of networks. The research, done by Johns Hopkins University and MILA, finds that "cortex-aligned representations emerge in convolutional architectures that combine two key manipulations of dimensionality: compression in the spatial domain and expansion in the feature domain". This means that "the architectural biases imbued into convolutional networks allow many aspects of cortical visual representation to readily emerge even before synaptic connections have been tuned through experience."  
  
**What this suggests:** Though systems like transformers are very popular these days, the research finds that feedforward and transformer-based networks do not approximate behavior of primate visual networks nearly as well as convolutional ones - "we show that dimensionality expansion in an untrained convolutional neural network achieves surprisingly strong performance at explaining image-evoked responses in the primate visual cortex, in some cases reaching the performance of a standard pre-trained network."  
This doesn't mean that transformers or feed forward networks aren't useful for visual tasks - rather, that you need to dump more resources into them to get some of the same representations that you get from a comparatively early and cheap convnet. "Massive pre-training may be sufficient to overcome a lack of brain-aligned inductive biases in diverse network architectures, such as in vision transformers".  
  
**Why this matters - another way of understanding the brain:** Research like this takes all the progress that has been made in AI and essentially inverts it - we now have a bunch of different ways of building neural nets that we know lead to useful things at scale. But what if we use these tools to instead understand the brain and the distance between these systems and how our own brains work? "Architecture optimization in untrained or minimally trained networks is a promising future direction for exploring the inductive biases that may underlie biological vison," the researchers write.  
**Read more** : [Convolutional architectures are cortex-aligned de novo (bioRxiv)](https://www.biorxiv.org/content/10.1101/2024.05.10.593623v2).  
  
***  
  
 **Tech Tales:  
  
The alien greeting department  
** _[Poem scribbled after several meetings of an alien greeting working group at the UN, following credible intelligence of an imminent visitation by an extraterrestrial species. Date unknown.]  
  
_ To prepare for the alien invasion,  
the humans took several steps.   
They convened working groups,   
Brought stakeholders together  
And agreed on the principles  
For how they'd talk to the aliens.  
  
To prepare for the alien invasion,  
The humans built technologies;  
_de novo_ communicative intent tools,  
Ways to study the expected aliens,  
Scales they hoped they might land on,  
fMRI tubes for beings of unknown dimension.  
  
To prepare for the alien invasion,  
The humans thought about their own reality.  
Would aliens understand reality?  
Would aliens communicate their intent?  
Would aliens understand human needs?  
Would - _could?_ \- the aliens be kind?  
  
**Things that inspired this poem:** How much of AI policy feels like building infrastructure for a broadly unknown thing expected to arrive in the future; the impossibility of imagining the thought process of a thing smarter than ourselves; how much of policy sometimes feels like a form of reassurance - a way to gather people together from distinct demographics and backgrounds and to sit around a metaphorical fire (flickering powerpoint) and all stare at it and say 'yes, the world around us is indeed complicated, and we can acknowledge this together'; yes of course 'aliens' here is a metaphor for AGI.  
  
_Thanks for reading!_
