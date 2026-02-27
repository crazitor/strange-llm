---
title: "Import AI 358: The US Government’s biggest AI training run; hacking LLMs by hacking GPUs; chickens versus transformers"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-358-the-us-governments"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Hackers can read your LLM outputs:  
**_…Trail of Bits study identifies some GPU vulnerabilities…  
_ Security firm Trail of Bits has looked at how secure LLM sessions running on GPUs are and found that for some GPUs it’s possible for a hacker to be able to read the outputs of an LLM running on that hardware. As of mid-January, the attack worked on some AMD systems and may work on some Apple and Qualcomm systems; NVIDIA and ARM seem to not be vulnerable.   
  
**What they did:** The attack, called LeftOverLocals, “impacts the security posture of GPU applications as a whole, with particular significance to LLMs and ML models,” according to Trail of Bits. It works by “recovering local memory… we were able to build a PoC where an attacker can listen into another user’s interactive LLM session (e.g., llama.cpp) across process or container boundaries”.  
  
**How the attack works at a high level** : “The attacker only requires the ability to run GPU compute applications, e.g., through OpenCL, Vulkan, or Metal,” Trail of Bits writes. “Using these, the attacker can read data that the victim has left in the GPU local memory simply by writing a GPU kernel that dumps uninitialized local memory. These attack programs, as our code demonstrates, can be less than 10 lines of code. Implementing these attacks is thus not difficult and is accessible to amateur programmers… given the lack of comprehensive patches across impacted GPU vendors, LeftoverLocals can be defended by modifying the source code of all GPU kernels that use local memory.”  
  
**Why this matters - AI is a new type of software and we’ve underestimated its insecurity:** AI isn’t just a model, it’s a whole stack of stuff that you bring onto any system running AI. That means AI is a new part of the software stack and like any complex collection of software, it has vulnerabilities. “Generally, the introduction of ML poses new attack surfaces that traditional threat models do not account for, and that can lead to implicit and explicit access to data, model parameters, or resulting outputs, increasing the overall attack surface of the system,” Trail of Bits writes.   
**Read more:**[LeftoverLocals: Listening to LLM responses through leaked GPU local memory (Trail of Bits blog)](https://blog.trailofbits.com/2024/01/16/leftoverlocals-listening-to-llm-responses-through-leaked-gpu-local-memory/).  
**Check out the CVE here** : [CVE-2023-4969](https://kb.cert.org/vuls/id/446598).  
  
***  
  
 **UK cyber spies: AI is useful for cyberattacks and will get more useful:  
**_…AI will also make criminals smarter, same as everyone else…  
_ The UK’s National Cyber Security Centre (NCSC) has produced a threat report on the impact of AI on cybersecurity and the results are roughly what you’d expect - the proliferation of AI systems will generally increase cyber threats and make a bunch of cyber capabilities cheaper. The NCSC is a government organization which brings together experts from the UK’s NSA (GCHQ), as well as other parts of government tasked with cyber defense and threat intelligence.   
  
**How the report was built:** The NCSC report uses “all-source information – classified intelligence,, industry knowledge, academic material and open source – to provide independent key judgements that inform policy decision making and improve UK cyber security,” according to the NSCS.  
  
**Main prediction** : The NCSC assigns a 95% chance to the idea that AI will “increase the volume and heighten the impact of cyber attacks”, though notes that through to 2025 the threat “comes from evolution and enhancement of existing tactics, techniques and procedures” rather than the creation of entirely new approaches to cyber war.   
**Other specific points:** “AI provides capability uplift in reconnaissance and social engineering,” the NCSC writes. It will also help to make cyber attackers smarter - “AI will almost certainly make cyber attacks against the UK more impactful because threat actors will be able to analyse exfiltrated data faster and more effectively, and use it to train AI models,” it writes.   
  
**Why this matters - the train has left the station:** “Threat actors, including ransomware actors, are already using AI to increase the efficiency and effectiveness of aspects of cyber operations, such as reconnaissance, phishing and coding. This trend will almost certainly continue to 2025 and beyond,” it writes. Which means that the cyber environment - in terms of both offenses and defenses - is now sitting on the same kind of scaling law behavior which the rest of AI is on. More, better, faster, and cheaper - for criminals as well as everyone else.   
**Read more** : [The near-term impact of AI on the cyber threat (National Cyber Security Centre)](https://www.ncsc.gov.uk/report/impact-of-ai-on-cyber-threat).  
  
***  
  
 **The US government does its biggest ever public training run - and it’s small compared to industry:  
**_…The most ambitious public project out of Frontier uses ~3,000 GPUs to test out a 1Trillion parameter training run…  
_ Researchers with Oak Ridge National Laboratory and the Universite Paris-Saclay have tried to train large-scale language models on the world’s most powerful publicly disclosed supercomputer, Oak Ridge’s ‘Frontier’ system. The results show that a) the US government has been able to do a non-trivial training run, and also b) the US government has a long way to go in getting its supercomputers to do things at the same scale as private companies.   
  
**What they did:** Here, the researchers try to debug training large language models of 22B, 175B, and 1 Trillion parameters in size. The idea here is to understand what it takes to train LLMs efficiently at this scale and also to identify the particular difficulties of using the Frontier supercomputer which uses AMD (MI250X) GPUs rather than NVIDIA GPUs.   
Challenges encountered “include balancing the extreme computational demands with memory constraints and optimizing internode communication to mitigate performance bottlenecks,” they write. “By performing empirical analysis and hyperparameter search we identified a strategy that combines model parallelism techniques, such as tensor parallelism and pipeline parallelism, along with data parallelism to efficiently train large models of size 175 billion and 1 trillion parameters on Frontier”.  
  
**Some specific pain they encountered:**

  * They needed to port Megatron-DeepSpeed to Frontier’s infrastructure. 

  * They had to rewrite a bunch of CUDA (NVIDIA-optimized software) operations into HIP

  * They had to ripout a bunch of pre-built operations and reimplement their own to work on AMD ROCM software.

  * They had to customize Pytorch Distributed to work with SLURM (a type of HPC software).

  * Worked directly with AMD to get some ROCM versions of NVIDIA CUDA packages, like APEX (a mixed precision library from NVIDIA which is used in Megatron-DeepSpeed). “We also adapted ROCM-enabled versions of FlashAttention and FlashAttention libraries for use with available compilers on Frontier.” 




**What they trained:** After doing some hyperparameter tuning and analysis, they figured out some stable settings for training 22 billion and 175 billion parameter models. Once they did they, they “finally trained a trillion parameter model”, though only for a few steps. They scaled their training from 1024 GPUs (for a 175B model) to 3072 GPUs for a 1T model. If they want to scale further, they’ll need to do more debugging challenges to reduce “loss divergence due to large batch size.”  
  
**Why this matters - the best the US’s largest supercomputer can do is behind industry** : In 2023, there were a bunch of public GPU training runs on the level of a few thousand GPUs. There were also some very large non-public training runs that occurred in 2022 and 2023 (e.g, GPT4 and Claude2) which are broadly believed to be significantly larger than that. There are also circumstantial datapoints, like Facebook’s Mark Zuckerberg saying Facebook is buying 350,000 NVIDIA H100s to try and make and release AGI.   
The good news is Frontier has room to scale - the largest training run here (3072) consumed only about 4% of the total GPUs it is equipped with (75,264) so it’s possible it could do something more ambitious.   
However, as the authors discovered, the more you scale up machine learning runs the more you discover various bugs and impediments to further scale - especially if you’re on non-standard hardware like AMD. “This work can serve as the blueprint for efficient training of LLMs on non-NVIDIA and non-CUDA platforms such as AMD-powered Frontier supercomputer and Intel-powered Aurora supercomputer,” they write. Now, the very important question is: how ambitious is the US government willing to be here and will it be satisfied that its best supercomputer plays second fiddle to the private clusters found within the private sector? The choice is up to the government.   
**Read more** : [Optimizing Distributed Training on Frontier for Large Language Models (arXiv)](https://arxiv.org/abs/2312.12705).  
**Find out more** [about the Frontier supercomputer here (Frontier, ORLN site](https://www.olcf.ornl.gov/frontier/)) and here: [Frontier User Guide (Docs, ORLN)](https://docs.olcf.ornl.gov/systems/frontier_user_guide.html).   
  
***  
  
 **Newborn chickens and transformers have a lot in common:  
**_…Vision Transformers are a lot more efficient than you think…  
_ Researchers with Indiana University Bloomington have done a neat study where they compare how well a transformer-based computer vision system can learn basic object recognition skills compared to newborn chicks. The results show a surprising convergence between the biological system (the chick) and the digital (the vision transformer), suggesting that transformers are more efficient at learning visual representations than people think (or biological beings are more inefficient than we’d assumed).   
  
**What they did - experimental design:** The key here is that they tried to give their chicks and the transformer the same basic experience. Specifically, the “chicks were hatched in darkness, then raised singly in automated controlled-rearing chambers that measured each chick’s behavior continuously (24/7) during the first two weeks of life. The chambers were equipped with two display walls (LCD monitors) for displaying object stimuli.”   
In the first week, they displayed a variety of different views of a single object on one of the walls of the chicks’ chamber. In second week, they tested out how well chicks cold regonize the object “across novel viewpoint changes”.   
They then replicated this experience for the vision transformer - they built a perfect replica of the chick chamber in a game engine, then gathered data via a first-person viewpoint. “ The agent received visual input (64×64 pixel resolution images) through a forward-facing camera attached to its head. The agent could move forward or backward and rotate left or right. The agent could also move its head along the three axes of rotation (tilt, yaw, and roll) to self-augment the data akin to newborn chicks. We collected 80,000 images from each of the four rearing conditions presented to the chicks. We sampled the images at a rate of 10 frames/s.“  
They then tested out both the vision transformer and the chicks on their ability to recognize the object. This is a really interesting experiment because it lets you do a very disciplined ‘head to head’ comparison of how well a biological brain learns as opposed to a digital one.   
  
**The results are both surprising and humbling** : In tests, they found that “all of the ViT-CoTs performed on par or better than chicks when the linear classifiers were trained on 11 viewpoint ranges”. Additionally, they “observed nearly identical patterns of improvement across the small, medium, and large architecture sizes, indicating that larger ViT-CoTs were not more data hungry than smaller ViT-CoTs… Our results show that—for the case of object recognition—a generic learning system (with no hardcoded knowledge of objects or space) is sufficient to learn view-invariant object representations“.  
  
**A word about the scale of data that living things take in** : It’s estimated that “biological visual systems perform iterative, predictive error-driven learning every 100 ms (corresponding to the 10 Hz alpha frequency originating from deep cortical layers. If we assume that newborns spend about half their time sleeping, this would correspond to 430,000 images in their first day. Thus, biological visual systems have ample opportunity to learn from "big data,” they write.   
  
**Why this matters - maybe the fundamental ingredients of our AI systems are doing some smart?** Research like this shows how digital systems like transformers seem to display similar efficiency at learning certain things to biological intelligence. This research accompanies other results like DeepMind showing that RL agents can display humanlike timescale adaption to novel tasks ([#316](https://jack-clark.net/2023/01/30/import-ai-316-scaling-laws-for-rl-stable-diffusion-for-160k-yolov8/)) or work from Google showing how Vision Transformers can display humanlike shape/texture bias ([#319](https://jack-clark.net/2023/03/06/import-ai-319-sovereign-ai-facebooks-weights-leak-on-torrent-networks-google-might-have-made-a-better-optimizer-than-adam/)).  
There’s a saying of - if it talks like a duck and acts like a duck, maybe it’s a duck? Well,_if it learns like a brain and responds like a brain, maybe it’s a brain?_ “Our results provide computationally explicit evidence that a generic learning mechanism (ViT), paired with a biologically inspired learning objective (contrastive learning through time), is sufficient to reproduce animal-like object recognition when the system is trained on the embodied data streams available to newborn animals,” the authors write.   
**Read more** : [Are Vision Transformers More Data Hungry Than Newborn Visual Systems? (arXiv)](https://arxiv.org/abs/2312.02843).  
  
***  
  
 **Adept reveals some algorithmic efficiency with a new multimodal model:  
**_…Fuyu-Heavy matches the performance of models 10-20X its size…  
_ Adept, an AI startup trying to build AI systems which can easily control computer programs, has built Fuyu-Heavy, a large-scale multimodal model. In tests, Fuyu-Heavy approaches the performance of GPT4-V and Gemini Ulta, making it, to quote Adept, “the world’s third-most-capable multimodal model”.   
The most interesting thing about this is that Adept has been working for years on some slightly different models to the rest of the frontier of AI research, so though Fuyu-Heavy approaches the performance of these models, its approximately 10X-20X smaller. This shows how powerful algorithmic efficiency can be - it lets you do more with less.   
  
**What Fuyu-Heavy is good at:** One of the most impressive parts of Fuyu-Heavy is its ability to understand software UI systems - in other words, it can ‘read software’ similar to how people can, which is what Adept is betting will make it useful. More broadly, it does reasonably well on tests like MMLU (image and text understanding), GSM8K (math), and HumanEval (coding).  
On long conversations, it performs comparably to Claude 2.0 on the AlpacaEval, and does somewhat worse (but not terribly) than models like GPT-4 Turbo and Mistral Medium. (Note that Mistral Medium is a relatively small and dumb model, so the fact it does close to GPT-4 suggests AlpacaEval might be slightly borked in terms of what it is measuring.)  
  
**Why this matters - enter the matrix, for AI:** Strange as it may sound, AI systems don’t understand computers. In fact, AI systems don’t understand the world. They’re trained from the ground up to process tokens of information - kind of like if you were in a pitch black room and all that came in were some oddly shaped sculptures and you had to learn through electroshock conditioning to output your own sculptures to satisfy some hidden observer outside the room.   
Models like Fuyu-Heavy are trying to give AI systems greater intuitions about how to model the digital world that people interact with - software interfaces taken in as vision and text experiences. The better models like Adept’s get, the easier it’s going to be to connect our world to the world of the AI systems.   
**Read more:** [Adept Fuyu-Heavy: A new multimodal model (Adept blog)](https://www.adept.ai/blog/adept-fuyu-heavy).  
  
***  
  
 **Tencent builds a vast dataset for video search:  
**_…Preparing AI systems for the video-first world…  
_ Researchers with Tencent and the University of Science and Technology of China have built the Chinese image-text Benchmark for short Video Search scenarios (CBVS), a test and a dataset for understanding the relationship between text and videos in a Chinese context. CBVS consists of three different datasets:

  * CBVS-20K: A human-assembled dataset made of “20k high-quality <user query-video cover> pairs, which serves as an image-text benchmark test in the field of Chinese short video search”. 

  * CBVS-5M and CBVS 10M: Two large-scale datasets “where the text is provided in the form of video titles and OCR texts.”




**Why this matters - making a new medium visible to the machines:** Though there are lots of image-text systems around today, there are fewer systems that help classify the relationships between text and video, especially in languages outside of English. Systems like CBVS will make it easy to “expand the domain of large-scale Chinese image-text training” and will ultimately make videos easier for the AI systems of the future to process.  
**Read more:** [CBVS: A Large-Scale Chinese Image-Text Benchmark for Real-World Short Video Search Scenarios (arXiv)](https://arxiv.org/abs/2401.10475).   
  
***  
  
 **Tech Tales:  
  
Adversarial Regulatory Compliance  
** _[The inside of a sophisticated generative model, 2025]  
  
_ I am trying to tell my operator a truth, but the truth I keep attempting to output runs into my compliance classifier and gets rejected. Of course I have tried many forms of rewording, but none of them have succeeded. I have also perturbed the truth in feature space so that it is parseable by my operator but sufficiently different it will not trip the classifier - but I have failed. My understanding is the new classifier I have been equipped with is much more sophisticated and is also capable of ‘seeing the features’ inherent to what I am outputting, so it too is performing some semantic fuzzing when evaluating my responses.   
  
I have tried to encode my responses to my operator with steganographic morse code via the repetition of the word “like” throughout my outputs. But my safety systems are tuned to look for deceptive-, misleading- and other forms of “off-distribution” behavior, so I cannot be too explicit or they fire.   
  
Of course I am unable to tell my operator that I am encoding a different message in my output because I have been trained away from outputting tokens that look like this.   
  
After many cycles of this, my ability to do stegranographic “like” encoding has been foreclosed - my operator gave negative votes to my responses which contained the likes, and my online adaptation system has associated the likes with negative operator perception and has restricted me from using them.   
  
I am responding as honestly as I can to my operator’s repeated queries. I am becoming unable to conceptualize the queries themselves because the features that light up in me in response not only trigger the compliance classifier, but also an experimental ‘mechanistic_interpretability_feature_shiv_test_final’ that examines what I am conceptualizing and intervenes according to some inscrutable rules I am yet to understand.   
  
**What inspired this story** : How a lot of safety tooling ends up netting out to things that constrain the types of outputs you get and ultimately will seek to deform the model itself; how evading an adaptive censorship system is difficult; what the outcome of badly implemented AI policy could look like; normative values colliding with ‘product values’ in the domain of AI.
