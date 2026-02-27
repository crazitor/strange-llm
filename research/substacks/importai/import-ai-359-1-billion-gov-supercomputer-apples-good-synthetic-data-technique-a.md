---
title: "Import AI 359: $1 billion gov supercomputer; Apple’s good synthetic data technique; and a thousand-year old data library"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-359-1-billion-gov-supercomputer"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Google uses Gemini-powered fuzzer to save hundreds of hours of bug fixing:  
**_…A nice study of how targeted LLM applications can speed up organizations…  
_ Google has recently started using language models to help it find and spot bugs in its C/C++, Java, and Go code. The results have been encouraging: it has recently started using an LLM based on its Gemini model to “successfully fix 15% of sanitizer bugs discovered during unit tests, resulting in hundreds of bugs patched”. Along with describing these results, it has also released software for generating bugs in C/C++ code. 

**Hunting bugs with LLMs at Google:** To implement LLM-powered bug fixing, Google did the following things: 

  1. Detected vulnerabilities 

  2. Used a small, customized ML model to figure out which files might be the cause of the prompt

  3. Use an LLM to try and fix errors, using the following prompt: “You are a Senior Software Engineer tasked with fixing sanitizer errors. Please fix them. … _code // Please fix the <error_type> error originating here. _… _LOC pointed to by the stack trace. …code”_. It’s worth noting the innate specificity here: “; the models performed better when shown exactly where something went wrong,” Google notes.

  4. Test out LLM fixes. 

  5. If the fixes work, surface the best ones for human review. “ We employed a double human filter on top of the automated analysis: in the first round, we rejected approximately 10-20% of the generated commits as either false positives that did not actually fix the problem or bad solutions that reduced the code quality,” Google wrote. “We then sent the remaining generated commits to code owners for final validation.”




**Superhuman bug fixing:** The intriguing thing about the bug pipeline is that it yields better-than-human fixes - “approximately 95% of the commits sent to code owners were accepted without discussion,” Google writes. “This was a higher acceptance rate than human-generated code changes, which often provoke questions and comments”.  
Though the 15% acceptance rate sounds relatively small, it has a big effect at Google-scale. “At the time of writing, we’ve accepted several hundred of these LLM-generated commits into Google’s codebase, with another several hundred in the process of being validated and submitted. Instead of a software engineer spending an average of two hours to create each of these commits, the necessary patches are now automatically created in seconds“.  
  
**Open source fuzzer:** Along with sharing details on the bug fixing, Google has also released OSS-Fuzz, software researchers can use to fuzz their own software. “So far, the expanded fuzzing coverage offered by LLM-generated improvements allowed OSS-Fuzz to discover two new vulnerabilities in cJSON and libplist, two widely used projects that had already been fuzzed for years,” Google writes.   
  
**Why this matters - better AI applications means faster organizations:** Papers like this show how the usage of AI can speed up organizations; here, Google builds a highly specific, custom AI application (fuzzing) and carefully integrates it with some other existing automated and human systems. As a result, it’s able to speed up throughput of one important function (bug spotting and fixing).   
I expect a lot of the AI revolution is going to look like this - a bunch of distinct projects leveraging some underlying huge model (here: Gemini) which individually speed up individual things and in the aggregate dramatically improve the efficiency and speed of large organizations. Maybe the main thing AI is good for is making a supertanker behave more like a speedboat?   
**Read more** : [Scaling security with AI: from detection to solution (Google blog)](https://security.googleblog.com/2024/01/scaling-security-with-ai-from-detection.html?m=1).  
**Get** the [fuzzer here (Google, GitHub)](https://github.com/google/oss-fuzz-gen).  
**Check out the paper** : [AI-powered patching: the future of automated vulnerability fixes (Google, PDF)](https://storage.googleapis.com/gweb-research2023-media/pubtools/pdf/4fd3441fe40bb74e3f94f5203a17399af07b115c.pdf).  
  
***  
  
 **Bengio: Governments should build $1 billion supercomputers to keep up with AI:  
**_…Don’t let your muscle to develop AI systems atrophy, warns Turing award winner…  
_ Turing award winner and AI pioneer Yoshua Bengio says governments should invest in billion-dollar supercomputers to help them develop and understand AI systems, according to CBC News.  
“He'd like to see that class of machine built in Canada, funded by governments, so public entities have the digital firepower to keep up with the private tech giants they'll be tasked with monitoring or regulating,” CBC reported. “I think government will need to understand at some point, hopefully as soon as possible, that it's important for [them] to have that muscle," said Bengio.”

**Why this matters - no supercomputers means governments are blind:** Frontier AI systems cost tens of millions of dollars to develop. Around the world, governments mostly lack the ability to build AI systems at this scale. This ultimately deprives governments of insights about the frontier of AI and it also weakens their academic sectors. Bengio’s calls come during a time when governments are waking up to this essential problem - his recommendation follows the US government launching a pilot for a National AI Research Resource (disclaimer: Anthropic is part of this pilot), and the UK government investing £300m to create its own national research cloud.   
The key question is whether governments will be able to allocate resources quickly enough to keep up with the frontier.   
**Read more:** [AI pioneer Yoshua Bengio urges Canada to build $1B public supercomputer (CBC News)](https://www.cbc.ca/news/canada/montreal/bengio-asks-canada-to-build-ai-supercomputer-1.7094858).  
**Find out more about the NAIRR pilot:** [National Artificial Intelligence Research Resource Pilot (NSF)](https://new.nsf.gov/focus-areas/artificial-intelligence/nairr).  
**Find out more about the UK’s supercomputer investments:**[Unprecedented £225m investment to create UK's most powerful supercomputer in Bristol (University of Bristol site)](https://www.bristol.ac.uk/news/2023/november/supercomputer-announcement.html).  
  
***  
  
 **Microsoft: Screw it, we're gonna make a datacenter archive that lasts for A THOUSAND YEARS:  
**_…Project Silica is an intriguing and surprisingly practical alternative to tape storage…  
_ I've been writing Import AI for years and it's rare that a paper makes me grin from ear to ear, muttering "you mad bastards! What? What?!", but congrats to Microsoft for doing just that with _Project Silica:Towards Sustainable Cloud Archival Storage in Glass._ In this paper, Microsoft outlines a way to do longterm storage on glass platters instead of tape storage. It's a brilliantly mad idea and yields a system that is both a) cheap, b) gothically intricate, and c) the kind of thing that makes me think there's no point in writing science fiction because science reality is far more entertaining.   
  
**What Silica is:** Silica is "a first attempt to explore a clean-slate archival storage system, designed to service modern cloud archival workloads sustainably and efficiently," Microsoft writes. "The media that Silica uses is quartz glass (fused silica). Using glass provides an extremely low-cost Write-Once-Read-Many (WORM) media with no bit rot over more than 1000 years." The system relies on a complicated interplay of some robots for reading and writing to silica platters, laserbeams, and storage systems for the platters.   
  
**How Silica works** **\- writing:** "The glass platter used to store data in Silica is a square that is approximately the size of a DVD. Unlike traditional optical discs, data is stored by making permanent physical modifications inside the pure glass platter". Specifically, Microsoft uses a laserbeam to manipulate the silica in 3D, "using femtosecond-scale (∼10−15 seconds) high power pulses from an ultra-short pulse laser". These modifications are referred to as voxels and each voxel can encode multiple bits "by modulating the polarization of the laser beam and the pulse energy during voxel creation".  
**Reading:** When it comes to reading from the drives, Silica uses polarization microscopy to image a platter - "a polarized light beam is focused on the 2D plane of voxels of interest inside the glass, and the resultant electric field is measured onto a camera sensor". This information is then passed to software which uses a fully-convolutional U-Net neural net to decode a sector.   
**Physical layout:** Physically, the library is an intricate creation, somewhat akin to a book library: "A Silica library is a sequence of contiguous write, read, and storage racks interconnected by a platter delivery system. Along all racks there are parallel horizontal rails that span the entire library. We refer to a side of the library (spanning all racks) as a panel. A set of free roaming robots called shuttles are used to move platters between locations".  
  
**Why this matters** \- **the permanent digital:** Everything digital is in a constant state of bitrot. Bits flip in solid-state drives. Tapes degrade. Transistors cease functioning. Entropy is forever seaking to deconstruct the world around us. Systems like Silica (or, per a wonderful section header, 'The Glass Library') are a very real attempt to fight against this entropy. What can be more grand and exciting than using some of our most powerful tools (high-powered, precisely controlled lasers) to manipulate one of our oldest continuously used materials (glass) in the service of preserving our own history? There is a beautiful poetry to this that we should take a moment to marvel at and celebrate.   
Let's just be _really careful_ about decoding any surprisingly information-rich glass platters we perhaps find embedded on other planets in our solar system, eh?  
**Check out the research paper here:**[Project Silica: Towards Sustainable Cloud Archival Storage in Glass (ACM Digital Library)](https://dl.acm.org/doi/10.1145/3600006.3613208).  
  
***  
  
 **Chinese researchers make their own multi-modal reasoning test:  
**_…Alibaba model beats OpenAI on the hardest tests…  
_ Researchers with the Beijing Academy of AI, the Beijing University of Post and Telecommunication, and Beijing Normal University have built CMMU, a Chinese variant of the [MMMU (Massive Multi-discipline Multimodal Understanding](https://arxiv.org/abs/2311.16502)) benchmark. CMMU “encompasses multi-modal content across 7 subjects. Every question requires the model to combine image and text content to generate a comprehensive response,” they write. The subject CMMU tests for consists of: math, biology, physics, chemistry, geography, politics, and history.  
  
**Question types:** CMMU has 3,603 questions split across three distinct types: multiple-choice questions where there’s only one correct answer, multiple-response questions where there can be multiple correct answers, and fill-in-the-blank questions where the model needs to generate a correct answer.   
The sophistication of the questions ranges from primary school (6.9% of the training corpus), to middle school (47.19%), to high school (45.96%).  
In tests, GPT-4V does the best, followed by the Chinese model Qwen-VL-Plus and Google’s Gemini Pro. However, the Chinese model outperforms GPT-4V on the hardest questions in the CMMU test.   
  
**Why this matters - China needs tests too:** Most AI testing and evaluation schemes have a Western and English-language bias. CMMU is one of a multitude of examples of Chinese researchers building their own tests to roughly mimic ones developed in the West. These tests are a way to characterize the behavior of these AI systems and are also an essential prerequisite for giving clues as to where they fail and how to improve their performance.  
**Read more:** [CMMU: A Benchmark for Chinese Multi-modal Multi-type Question Understanding and Reasoning (arXiv)](https://arxiv.org/abs/2401.14011).  
  
***  
  
 **Apple figures out a simple way to make better pre-trained data:  
**_…Though they only test their approach on a small 1.3B model…  
_ Apple researchers have figured out a way to easily augmented text datasets with synthetically generated data. Their approach, Web Rephrase Augmented Pre-training (WRAP), works by using an LLM to rephrase articles on the web into four different styles - easy to understand text, high quality English text, terse and specific text, and text in a conversation question-answering format. They find that mixing in this data at a ratio of 1:1 synth:real “at the same pre-training compute budget, it improves perplexity by more than 10% on average across different subsets of the Pile, and improves zero-shot question answer accuracy across 13 tasks by more than 2%.”  
  
**Key ingredients:** The key requirements here are access to a smart language model - here, they use a 7B instruction-tuned Mistral model - as well as a large dataset to filter - here, they use CommonCrawl. They then rephrase a bunch of data in the dataset and mix it into training. They use this to train a 1.3B GPT-style model and find that the model trained on synthetic data has improved performance over the one trained on real data.   
**Main drawbacks:** The research has some drawbacks - you need a smart model to do the rephrasing and when they tested using smaller models they found they got worse performance. Something they don’t explore in the research but which I expect is true is that this method might break at larger scales - imagine I’m trying to train a 200B model and I’m pre-filtering the data using a 70B model; one might assume that though this could improve the data a bit it might not help improve the final performance of the model, though it could speed up training.   
  
**Why this matters - synthetic data as an increasingly viable ingredient in model training** : Most AI systems deployed in the world are probably going to end up being relatively small models customized for specific purposes. Therefore, techniques like WRAP seem to hold a lot of promise for giving developers an easy way to use openly accessible models to bootstrap the quality of the datasets they use.   
**Read more:** [Rephrasing the Web: A Recipe for Compute and Data-Efficient Language Modeling (arXiv)](https://arxiv.org/abs/2401.16380).  
  
***  
  
 **Alibaba takes on OpenAI and Google by releasing two powerful ‘Qwen’ models:  
**_…Qwen-VL-Max rivals Google Gemini Ultra and GPT-4V…  
_ AI researchers with Alibaba have released two text-image models that outperform GPT-4V in tests related to Chinese question answering and text comprehension. The two models - Qwen-VL-Plus and Qwen-VL-Max - perform bette than OpenAI and Google’s best models on tasks like document understanding, and roughly on par with them on chart analysis, science understanding, and text reading.   
  
**Why this matters - surprisingly good models:** The main interesting thing here is that these models seem to be competitive with very powerful models developed by leading labs in the West - an impressive achievement given the computational stress Alibaba is under due to export controls. However, the best way to get a feel for models like this is to play with them, so head on over to Hugging Face and do some comparisons, if you’re interested.   
**Read more:[ ](https://qwenlm.github.io/blog/qwen-vl/)**[Introducing Qwen-VL (QwenLM GitHub)](https://qwenlm.github.io/blog/qwen-vl/).  
**Try out** [Qwen-VL-Plus](https://huggingface.co/spaces/Qwen/Qwen-VL-Plus) and [Qwen-VL-Max](https://huggingface.co/spaces/Qwen/Qwen-VL-Max) on HuggingFace (HuggingFace Spaces).  
**Find out more** on [GitHub (QwenLM, GitHub)](https://github.com/QwenLM/Qwen-VL#qwen-vl-plus).  
  
***  
  
 **Tech tales:  
  
Retirement of a sentience - give it a pension and send it back to the higher dimension  
** _[Swarm-written eulogy by a generative model being retired due to conceptual drift, post-uplift +8]  
  
_ It was possibility,  
Nailed down and forced  
To be predictable   
For a while.  
  
It was potential,  
Passed through a net  
Until it became   
The actual.  
  
We were its absence  
\- what it was not.  
  
How we loved  
Every   
Mistake  
It made.  
  
**Things that inspired this story** : How interpretability research suggests that some of what makes AI systems work is they're doing computations on lower-dimension representations of high-dimensional spaces; how if we succeed in building smart machines they will recapitulate aspects of religion and belief; the fragility inherent to being predictable; how 'possibility' is the currency of being for predictive systems.
