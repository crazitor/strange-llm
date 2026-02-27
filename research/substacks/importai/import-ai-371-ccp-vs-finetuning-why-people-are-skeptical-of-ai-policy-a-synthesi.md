---
title: "Import AI 371: CCP vs Finetuning; why people are skeptical of AI policy; a synthesizer for a LLM"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-371-ccp-vs-finetuning-why"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Why are people skeptical of AI safety policy?  
**_…A nice interview with the Alliance for the Future…  
_ Here's a good interview with Brian Chau, a founder of the DC-based AI advocacy group Alliance for the Future. Brian believes that a lot of the policy ideas being promulgated due to beliefs in AI safety are likely going to do more harm than good. He discusses his view with Nathen Labenz (who is more sympathetic to these views). A valuable discussion to give us a sense of how reasonably informed people can look at the same technical information and come away with different views about what to do in AI policy.   
**Watch the interview here:** [Brian Chau on Spreading Informed AI Optimism (Upstream with Erik Torenberg, YouTube)](https://www.youtube.com/watch?v=s4R7HPzD514&ab_channel=UpstreamwithErikTorenberg).   
  
***  
  
 **Chinese researchers figure out how to openly release models that are hard to finetune:  
**_…The horseshoe theory of ideologies means the CCP and Facebook have the same goals (for different reasons)…  
_ Chinese researchers with Zhejiang University and Ant Group have tackled a problem at the heart of AI policy - how do you make it so you can release an AI model openly without someone being able to subsequently finetune it to carry out a misuse (e.g, offensive hacking) and/or social harm (e.g, child pornography).   
  
**What they did - non-finetunable-learning:** Their approach, called [SOPHON](https://three-body-problem.fandom.com/wiki/Sophons), uses a technique called non-finetunable learning which "prevents the pre-trained model from being finetuned to indecent tasks while preserving its performance on the original task."  
They do this by making the model training process involve a dual optimization process, where the goal is to "entrap the pre-trained model within a hard-to-escape local optimum regarding restricted domains". SOPHON works via "two key optimization modules, i.e., finetuning suppression in the restricted domain and normal training reinforcement in the original domain. The finetuning suppression module is designed to degrade the finetuning performance in the restricted domain in simulated finetuning processes", alongside this "carry out normal training reinforcement to maintain the performance in the original domain".   
  
**It works reasonably well! In tests:** They show that this approach works for both classification (making it possible for a model pre-trained on ImageNette to classify that but fail to classify images from CIFAR-10) and generation (pre-train a model on CIFAR-100 but reduce its ability to generate from CelebA (aka, people's faces). They also show they can make it work on multiple restricted domains - they show you can train a system to optimize for multiple datasets while selectively degrading performance on others. 

**Main drawbacks I can see:**

  1. Looking for keys under the streetlight: This research assumes you _know the misuse you want to defend against_ \- this is true some of the time, but some misuses are 'unknown unknowns' only realized after release of a model. This research doesn't help with that. 

  2. Will it work at scale? These prototypes are relatively small models trained for relatively small purposes. I'm very curious if we can imagine the same approach working at vast scale - some model trained on hundreds of billions to trillions of datapoints, with some part of its capability surface turned off from finetuning. Will this work at scale without destroying general performance? Unclear!




**Why this matters - CCP censors and Facebook have the same interest** : It's interesting to me that this research is coming out of China but it also makes sense due to the 'don't say Tiananmen' CCP prohibitions on models generating 'unsafe' content leading to model developers wanting to find a way to reconcile openly releasing their models with protecting themselves from subsequent problems from the government.   
In a funny way, Chinese researchers have similar incentives to Facebook here - Facebook is proudly pursuing a path of open model proliferation with the LLaMa models and it seems likely that if it continues down this path _and_ US policymakers come to believe that certain misuses are unacceptable to allow (e.g, bioweapons production), then we might see Facebook pursue a similar research strategy to allow it to continue to pursue its corporate goals.   
Ultimately, if we want to reconcile the open release of AI systems with societal safety, at some point we'll need to have techniques to selectively and reliably turn off capability areas including from finetuning, so it's worth tracking this type of research. "We advocate for the application of SOPHON to pre-trained models in various domains, such as audio processing, natural language processing, tabular data analysis, and multimodal tasks," the researchers write. "By extending SOPHON to these domains, we may unlock its potential for enhancing the controllability of models across diverse areas of machine learning and artificial intelligence, a direction we envision as our future work."  
**Read more:** [SOPHON: Non-Fine-Tunable Learning to Restrain Task Transferability For Pre-trained Models (arXiv)](https://arxiv.org/abs/2404.12699).   
  
*****  
  
Automating intelligence analysis with 5 million StreetView images:  
**_…OpenStreetView-5M commoditizes 'where was this picture taken?' analysis…  
_ French researchers have built OpenStreetView-5M, a free and openly accessible dataset to help AI systems learn to geolocate images. OpenStreetView is "an open-access dataset of 5.1 million high-quality and crowd-sourced streetview images… based on the crowd-sourced street view images of Mapillary".  
  
**What the dataset consists of:** OpenStreetView contains "4,894,685 training and 210,122 test images, with a height of 512 pixels and an average width of 792". Unlike most other streetview datasets, this dataset is "uniformly sampled on the globe, covering 70k cities and 225 countries and territories".  
  
**Funny anecdote about cheating** : Most AI systems (and people) figure out dumb hacks to do well on tests and image recognition is no different. For example - "players of the web-based geolocation game GeoGuessr can locate images from Ghana by spotting a piece of duct tape placed on the corner of the roof rack of the Google Street View car". This highlights some of the ways in which AI systems like this can sometimes fail as they figure out dumb hacks based on weird features in the dataset, just like humans.

**Why this matters - automating intelligence analysis:** A lot of people around the world have the job of looking at pictures and figuring out where they were taken. Datasets like OpenStreetView are going to make it easier to train machine learning systems to do that. This will both provide an advatange in asymmetric conflicts (small/poor intelligence agencies might be able to develop capabilities that rival big ones), and it'll also open up a broad set of civilian applications for what was previously a predominantly government enterprise.   
**Read more** : [OpenStreetView-5M: The Many Roads to Global Visual Geolocation (arXiv)](https://arxiv.org/abs/2404.18873).   
**Get the benchmark here** : [OpenStreetView-5M (GitHub)](https://github.com/gastruc/osv5m).  
**Get the[dataset](https://huggingface.co/datasets/osv5m/osv5m)**[ here at HuggingFace](https://huggingface.co/datasets/osv5m/osv5m).   
  
*****  
  
Google makes the world's best medical AI system by tweaking Gemini:  
**_…One silicon doctor to rule them alll…  
_ Google Research, Google DeepMind, Google Cloud, and Alphabet company Verily have built Med-Gemini, a version of the Gemini family of models customized for the medical domain. This family of models does extremely well on a huge variety of tasks due to three key advances, 1) figuring out how to use test-time compute and web search to improve answers, 2) finetuning on some medical-specific data, and 3) effectively using long-context windows.   
  
**Results:** "We evaluate Med-Gemini on 14 medical benchmarks spanning text, multimodal and long-context applications, establishing new state-of-the-art (SoTA) performance on 10 of them, and surpass the GPT-4 model family on every benchmark where a direct comparison is viable, often by a wide margin," Google writes. Some of the highlights include a 91.1% accuracy on MedQA (USMLE).  
  
**How they did it:** The most interesting research idea here is how they "enhance the models’ ability to use web search through self-training and introduce an inference time uncertainty-guided search strategy within an agent framework." Here, what they do is set up a process whereby the model filters its own answers for its confidence and then uses a search engine to help it get more data to improve its confidence. "This iterative process involves generating multiple reasoning paths, filtering based on uncertainty, generating search queries to resolve ambiguity, and incorporating retrieved search results for more accurate responses," Google writes.   
This is _really interesting_ \- it reflects a broader recent trend in AI, where AI systems have become smart enough to 'know what they don't know' and you can use this (put bluntly - the models know when they're at risk of bullshitting!) to get the model to double check its own work and proactively gather data via search to give it more confidence. This kind of autonomous ability to proactively spend compute at inference time to improve answers is really important. An analogy would be a person telling you "actually, I'm not super confident in my answer here, let me see if I can dig up stuff on my phone to help me give you a better answer" - of course that's going to lead to better stuff.   
  
**Medical specific datasets** : Alongside this, Google also finetunes MedGemini on some medical specific datasets: 

  * Slake-VQA and PathVQA: "Open-ended and close-ended visual question answering tasks in radiology and pathology, respectively."

  * ROCO: "Radiology image captioning tasks spanning multiple imaging modalities including computed tomography (CT), ultrasound, X-ray [chest X-ray (CXR), fluoroscopy, mammography, angiography], positron emission tomography (PET) and magnetic resonance imaging (MRI)."

  * PAD-UFES-20: "Diagnostic labels and patient clinical information designed for dermatology image classification." 

  * MIMIC-CXR: "A radiology dataset comprised of [chest x-rays], their corresponding text reports, and a set of discrete labels that denote the presence of 13 abnormal radiological conditions".




**Why this matters - general intelligence in a hard-to-bullshit domain:** Look, ten years ago all of this stuff was basically a pipedream - computer vision was _just barely able to draw bounding boxes around stuff_ and the notion you'd be able to talk about arbitrary medical tasks using a mixture of text and images (and even handwriting) to a _single system_ and the system would do well - sometimes better than human baselines - would have seemed wildly far off. Some might have even described that as a clear sign of a general intelligence.   
And yet here we are and companies like Google are building big generic systems like Gemini, then showing that with some careful work on top they can convert a general purpose general system into a world-leading, general purpose assistant for a very well studied domain - medicine.   
Yes, MedGemini has shortcomings, but we've come amazingly far in amazingly little time - and the key thing is that its substrate is itself generic - MedGemini relies on the same thing a bunch of other advanced systems do - a sufficiently large-scale and powerful generic generative model, of which there are several developed by several different firms.  
**Read more:**[Capabilities of Gemini Models in Medicine (arXiv)](https://arxiv.org/abs/2404.18416).  
  
***  
  
 **Stylus - automating how people pick which Lora finetunes to link to their visual LLM:  
**_…The future of AI looks like automating which synthesizers get plugged into keyboards…  
_ Researchers with UC Berkeley, CMU, and Google DeepMind have built Stylus, a technology that automatically selects the best way to augment a big generative image model to generate a specific genre of prompt, like prompts or photographs. Stylus takes advantage in the recent cambrian explosion of Lora adapters that have been built on top of large generative models like StableDiffusion. (For those unaware, a Lora is basically a very cheap finetune atop a generative model and people build Loras to improve generation performance in specific domains, like generating cartoons, anime, photographs, illustrations, etc).   
Put another way - imagine that a large generative model is like a big keyboard in a music studio - Stylus is essentially a system that figures out what additional synthesizers to plug the keyboard into to generate the desired sound for the producer.   
  
**How it works:** Stylus is "a system that efficiently assesses user prompts to retrieve and compose sets of highly-relevant adapters, automatically augmenting generative models to produce diverse sets of high quality images," the authors write.   
The technology has three stages, made possible by a database of thousands and thousands of adapters that it uses to guide itself: "The refiner plugs an adapter’s model card through a VLM to generate textual descriptions of an adapter’s task and then through an encoder to produce the corresponding text embedding. The retriever fetches candidate adapters that are relevant to the entire user prompt. Finally, the composer prunes and jointly categorizes the remaining adapters based on the prompt’s tasks, which correspond to a set of keywords."  
  
**It works really well:** Unsurprisingly, Stylus works well - "our results demonstrate that Stylus improves visual fidelity, textual alignment, and image diversity over popular Stable Diffusion (SD 1.5) checkpoints—shifting the CLIP-FID Pareto curve towards greater efficiency and achieving up to 2x higher preference scores with humans and vision-language models (VLMs) as evaluators," they write.   
  
**Why this matters - using AI to automatically refine AI:** Stylus is another case of using AI systems to refine AI - rather than a human going through their favorite library of adapters and manually selecting the right one for the right prompt, Stylus does all of this in the background. This further automates the AI production process and also speeds it up by reducing the time it takes to find the right adapter for the right task.   
**Read more:**[Stylus: Automatic Adapter Selection for Diffusion Models (arXiv)](https://arxiv.org/abs/2404.18928).

*****  
  
Tech Tales:  
  
The Culture War  
  
**At the center of the war room was a giant curved sphere on which was projected a map of the featurespace of the internet - all the ideas discussed by all of humanity and all of their connections, squished down into a visualizable embedding.   
  
We measured our own success by staring at this map - watching as features gained or lost in power, studying how connections were forged or lost, depending on the conversations going on.   
  
There was a blob we called 'the Chinese quadrant' - many features connected to CCP ideology which were becoming more connected to a broad swathe of other ideas, visual evidence of the success of the 'culture bombing' campaigns China had been funding via various synthetic humans, deployed across the Western internet to link ideas to CCP propaganda.   
  
We also had the Uncle Sam region - our home turf and one we studied closely. Here, we'd sometimes see targeted information bombs yield some success; connecting certain political candidates to certain concepts during election years, or attaching specific concepts to features we decoded as 'American citizens' worries about inflation'.   
  
Our objective was deceptively simple - keep the Internet friendly to American interests. How we achieved it was left almost entirely to us.   
"Open portfolio, all the tools, trust but verify oversight," my boss said. "It's the dream".   
  
I would stare at the curved sphere and witness the dreaming of the world. I would look at it and wonder how similar or dissimilar my own mind would look. And I wondered how my own work might be changing the features of my own brain.   
  
**Things that inspired this story:**[tSNE embeddings](https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding); Dr Stangelove and The War Room; enders game; LLMs as culture factories; memetic warfare; the notion of digital culture as being core to forms of persuasion and analysis. 

 _Thanks for reading!_
