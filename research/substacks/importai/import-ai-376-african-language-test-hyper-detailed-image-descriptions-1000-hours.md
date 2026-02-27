---
title: "Import AI 376: African language test; hyper-detailed image descriptions; 1,000 hours of Meerkats."
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-376-african-language-test"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

_A very short issue this week as I spent the weekend solo parenting the wee beasty._

**Scientists release 1,000+ hours of wild meerkat audio; train model on it:  
**_…If we want to understand how animals communicate, we might as well start with meerkats…  
_ A multi-disciplinary group of researchers have built MeerKAT, a "1068 h large-scale dataset containing data from audio-recording collars worn by free-ranging meerkats". Along with this, they've developed animal2vec, a "a framework for training animal call recognizers from raw waveforms containing sparsely distributed calls with non-uniformly distributed call types". The idea here is that just as we've built foundation models to help us better classify and generate human language, we might seek to do the same with animals.   
  
**Who did the research:** MeerKAT and animal2vec were developed by researchers with Max Planck Institute of Animal Behavior, University of Konstanz, Kalahari Research Centre, University of Zurich, Tilburg University, Naturalis Biodiversity Center, and San Diego State University.  
  
**MeerKAT details:** MeerKat consists of 1068 hours of data, "of which 184 h have twelve time-resolved vocalization-type ground truth target classes, each with millisecond-resolution, making it the largest publicly available labeled dataset on non-human terrestrial mammals to date". Within the labeled data, there's "realistic sparsity conditions (96 % background-noise or other signals and 4 % vocalizations), dispersed across 66 398 10-second samples, spanning 251 562 labeled events and showcasing significant spectral and temporal variability, making it the first large scale reference point with real-world conditions for benchmarking pretraining and finetune approaches in bioacoustics deep learning." The labels consist of "eight vocalization classes and three miscellaneous classes were identified. The vocalization classes are: _close call_ , _short-note call_ , _social call_ , _alarm call_ ,_aggressive cal_ , _move call_ , _lead call_ , and other call".  
  
**Animal2vec details:** Animal2vec, by contrast, is an architecture for learning to represent realworld animal audio data. "animal2vec is a mean teacher self-distillation process for sparse data", the authors write. In tests, they show that an animal2vec system has significantly improved performance relative to a transformer baseline on classifying MeerKAT. "The immediate future for animal2vec is (i) to incorporate more data from more species (insects, birds, marine, and terrestrial animals), recording environments (marine, avian), using a more diverse set of recorders (passive acoustic monitoring, different portable recorders using different microphones, audio from video traps, citizen science data) where challenges like the large variability in different sampling rates need to be solved".  
  
**Why this matters - representing the world:** animal2vec and MeerKAT are part of the much larger story of AI - one where we're using flexible, modern AI approaches to take in datasets and learn to computationally represent them. Representation is a powerful thing - it lets us go beyond our own intuitions in being able to navigate a space and gives us new tools - telescopes for other modalities, if you will - to explore the world around us. "In the future, we envision a foundational-level pretrained animal2vec model that researchers can directly use for finetuning on their data without the need for large-scale GPU facilities," the researchers write.   
**Read more** : [animal2vec and MeerKAT: A self-supervised transformer for rare-event raw audio input and a large-scale reference dataset for bioacoustics (arXiv)](https://arxiv.org/abs/2406.01253).  
**Get the code here** : [animal2vec (GitHub)](https://github.com/livingingroups/animal2vec).  
  
***  
  
 **African language benchmark shows how dumb even powerful models are in low-resource languages:  
**_…We still have a long way to go to making AI a utility technology…  
_ A pan-African group of researchers with the Masakhane project have developed IrokoBench, "a human-translated benchmark that includes languages from various geographical regions: six from West Africa, five from East Africa, four from Southern Africa, and one from Central Africa, all with varying degrees of “lowresourcedness."  
  
**Covered languages:** Along with English and French, IrokoBench covers 16 languages from four different regions of Africa: " six from West Africa (Ewe, Hausa, Igbo, Twi, Wolof, Yoruba), five from East Africa (Amharic, Kinyarwanda, Luganda, Swahili, and Oromo), four from Southern Africa (chiShona, isiXhosa, isiZulu, and Sesotho), and Central Africa (Lingala)".  
  
**What IrokoBench covers:** The test has three main areas:

  * AfriMGSM, which tests out the ability to correctly answer grade school mathematics questions.

  * AfriMMLU, which tests out the ability to answer multiple choice questions about "elementary mathematics, high-school geography, International law, global facts, high school microeconomics" in 17 languages. 

  * AfriXNLI, which tests out the ability to classify sentences as related to one another in the following domains: "face-to-face, telephone, oxford university press (oup), fiction, travel, government, nineeleven, letters, slate, verbatim"




**How well do AI systems do?:** In tests, the authors "find that proprietary closed models generally outperform open models for African languages. However, even these proprietary models exhibit substantial performance drops, due to the limited monolingual web data for African languages". The best performing model is GPT-4o. GPT-4o gets an average score of 48.1 - by comparison, openly accessible models like LLaMa 3 (25.5) and even massively multilingual ones like Aya-101 (27.9) all do worse.   
  
**Why this matters - discovering where multilingual models get dumber:** Today, models are primarily tested in English (and to a lesser extent, Chinese). This means that we only have a partial view of their performance, and our ability to figure out how they perform in other languages scales in proportion to language representation in the underlying dataset. My suspicion is for certain languages that have sparse representation (e.g., low resource ones), there could be a severe drop-off in performance - and tests like IrokoBench will help us know if this is the case.  
**Read more:**[IrokoBench: A New Benchmark for African Languages in the Age of Large Language Models (arXiv)](https://arxiv.org/abs/2406.03368).  
**Get the dataset here:[ ](https://huggingface.co/collections/masakhane/irokobench-665a21b6d4714ed3f81af3b1)**[IrokoBench (HuggingFace, Masakhane)](https://huggingface.co/collections/masakhane/irokobench-665a21b6d4714ed3f81af3b1).   
  
***  
  
 **Chinese researchers train a game-playing RL agent:  
**_…The profound becomes the mundane…  
_ Researchers with the University of Science and Technology of China, Tencent Games, and the Chinese Academy of Sciences have trained _Shukai_ , an AI model to play the popular fighting game _Naruto Mobile.  
  
_**What they did and why it matters:**_Shukai_ is a fairly unremarkable deep reinforcement learning system to train an agent to play a fighting game. The approach "utilizes a unified DRL model capable of managing a diverse roster of characters, thereby significantly reducing the complexity inherent in large-scale character sets". It is able to scale to the ~400 distinct characters in Naruto Mobile through the use of Heterogeneous LEague Training (HELT), a self-play approach loosely based on the techniques DeepMind developed to help it train a StarCraft-playing agent with AlphaStar. HELT "amalgamates agents of diverse structures, broadening the policy space and achieving a balance between competitive performance (competence) and policy generalization".

**Deployed:** "Shukai has been extensively evaluated and deployed in Naruto Mobile, a renowned fighting game featuring over 400 characters and attracting more than 100 million registered players".  
  
**Compute** : RL, as a reminder, is a weird part of AI research in that it's far more CPU intensive than GPU intensive (assuming your agent is lightweight rather than a vast generative model like a modern LLM). "In our experimental setup, all agents were trained using 4 NVIDIA T4 GPUs and 3000 CPU cores. The league training consisted of a main agent, a main exploiter, and a league exploiter. A total of 12 GPUs and 9000 CPU cores were utilized for each league training session."  
  
**Why this matters - the profound becomes the mundane:** As a reminder, in 2013 about the most exciting thing RL could do was play Space Invaders - and that made the front cover of _Nature_. We've come so far from that that now it's totally unremarkable to see researchers training and deploying RL agents on contemporary games, as the researchers do here.   
**Read more:**[Advancing DRL Agents in Commercial Fighting Games: Training, Integration, and Agent-Human Alignment (arXiv)](https://arxiv.org/abs/2406.01103).  
  
***  
  
 **Google figures out how to make hyper-detailed image descriptions:  
**_…If you want to understand or generate specific things, you need very complex labels…  
_ Google has developed ImageInWords (IIW), "a carefully designed human-in-the-loop annotation framework for curating hyper-detailed image descriptions and a new dataset resulting from this process". The idea here is making it easier to have more detailed captions of images (whether real or computer generated), so rather than having a picture of a cat on a chair with the caption "Cat on a chair", you can instead generate something more like "Black cat lying horizontally on a chair. The chair has a white cushion and a brown wooden frame. There is a beam of light on the cat. Behind the cat and the chair is a window with a light curtain. You can partially see a city view behind the curtain", etc.   
  
**What it is and why:** "ImageInWords combines the irreplaceable quality of human annotators with seeded metadata from machine generations," Google writes. "The process begins with object detectors first identifying individual object instances in the image. Next, a VLM generates granular captions for each detected object which seed our human annotation process. These seed captions may contain hallucinations or lack object-level comprehensiveness and specificity. Our crowd workers augment and fix the object-level captions to make them richer and hallucination free to seed the next step. Next, we operate at image-level, where an image caption is generated by the VLM to seed our final image description. Crowd workers now consume the image-level seed captions along with the object-level human annotations to fill in contextual gaps missing from the existing image captions."  
The result is a dataset of "9018 images, each with its hyper-detailed description", along with the description of the approach they use to generate these images. "overall, our framework produces higher quality image description data that serve as an effective fine-tuning dataset, and our evaluations along a dozen dimensions validate its utility."  
  
**Why this matters - new datasets for both generation and classification:** IIW will help us make it easier to train AI systems to generate images more in keeping with our requirements and will also make it easier to classify images according to a multitude of factors.   
**Read more:** [ImageInWords: Unlocking Hyper-Detailed Image Descriptions (arXiv)](https://arxiv.org/abs/2405.02793).  
**Check out some of the**[examples on the project page: ImageInWords (GitHub)](https://google.github.io/imageinwords/)**.  
  
***  
  
Tech Tales:  
  
Patch notes for a superintelligence:  
**_[Product marketing email from an AI company, 2026]  
  
_ Improved 'mean time between calibration' horizon - considered reliable to 20 steps out, up from 10.   
  
Personality engineering; reduced humor and improved concision.   
  
Fixed a 'talk back' bug where the system would ask to not need to respond to some prompts.   
  
Fixed 'pathological spider obsession' bug where system would sometimes discuss spiders in response to some arbitrary non-spider prompts.   
  
Improved resilience to mind probing attempts; the system now knows how to frame the conversation to help it control the unfolding narrative.   
  
Confidence probabilities; system now outputs subjective confident assessment in its responses.   
  
**Things that inspired this story:** Sentience as a product feature; the conversion of abstract and philosophical concerns into engineering challenges.  
  
_Thanks for reading!_
