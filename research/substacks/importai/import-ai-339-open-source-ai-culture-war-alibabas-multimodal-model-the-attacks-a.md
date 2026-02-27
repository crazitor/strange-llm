---
title: "Import AI 339: Open source AI culture war; Alibaba's multimodal model; the attacks (and defenses) made possible by generative AI"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-339-open-source-ai-culture"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**  
AI culture war++: A16Z announces grants for open source AI:  
**_…8 initial grantees, with more to come…  
_ Famed venture capital firm Andreessen Horowitz has announced the "a16z Open Source AI Grant program", an initiative to provide funding to a small number of AI developers working on open source AI projects. A16Z wants to do this because it believes open source research help "push the state of the art in open source AI and help provide a more robust and comprehensive understanding of the technology."

**What A16Z is funding:** A16Z has funded eight people as part of its initial grant. It describes their projects as: "instruction-tuning LLMs on synthetic data; fine-tuning uncensored LLMs; fine-tuning foundation models for vertical applications; quantizing LLMs to run locally; web UI and platform for local LLMs", as well as a synthetic data pipeline for LLM training, a library for high-throughput LLM inference, and the development of new fine-tuned language models.

**Why this matters - open source as one front in an AI culture war:** Right now, open source AI (or, more broadly, openly accessible and free AI) has become a 'wedge issue' within AI; some companies have generally opted for building and deploying proprietary AI systems (e.g, OpenAI, Anthropic, Google, etc), while companies like Facebook have done the opposite (see: LLama2, Code LLama). This is part of a larger culture war within AI as people try to figure out how to best maximize the safety of the AI ecosystem - some people optimize for forms of centralized control, while others believe that the best way to a safe ecosystem is by broadly proliferating AI models and AI tools.   
It's clear with this grant programme that A16Z sees itself as being a member of the latter camp, and grants like this will help it portray itself as being on the side of the 'little guy' in the coming debates about AI power and centralization.  
**Read more:** [Supporting the Open Source AI Community (Andreessen Horowitz, blog)](https://a16z.com/2023/08/30/supporting-the-open-source-ai-community/).

####################################################

**The UK government gives details on its AI summit:  
**_…Risk-focused summit aims to come up with solutions…  
_ Later this year, the UK government is going to host a summit dedicated to AI safety. "The AI Safety Summit will bring together key countries, as well as leading technology organisations, academia and civil society to inform rapid national and international action at the frontier of Artificial Intelligence (AI) development," the government writes. Now, the government has given an update on what the summit will focus on.

**Focus areas for the UK summit:** The UK has five objectives for the summit. These are:

  * "a shared understanding of the risks posed by frontier AI and the need for action

  * a forward process for international collaboration on frontier AI safety, including how best to support national and international frameworks

  * appropriate measures which individual organisations should take to increase frontier AI safety

  * areas for potential collaboration on AI safety research, including evaluating model capabilities and the development of new standards to support governance

  * showcase how ensuring the safe development of AI will enable AI to be used for good globally"




**Why this matters - a shot at real AI governance:** AI governance has a history of lots of grand pronouncements and relatively little action - until recently. In the past year, governments around the world have woken up to the mind-bendingly huge implications of the progress of current AI systems and are beginning to think carefully about governance. The UK summit represents one of the most substantive and politically legitimate efforts to get AI governance done.   
**Read more** : [UK government sets out AI Safety Summit ambitions (Gov.uk)](https://www.gov.uk/government/news/uk-government-sets-out-ai-safety-summit-ambitions).

####################################################

**What kinds of attacks do generative AI systems make possible? And what kinds of defenses?  
**_…What do we do about an 'everything technology'?...  
_ What kinds of threats do generative AI systems contain and how might we defend against or mitigate them? That's the subject of a new paper born out of a workshop held at Google in June of this year. The researchers who contributed to the paper come from Google, the University of Wisconsin, University of California, San Diego, University of Maryland, College Park, University of California, Berkeley, University of Waterloo University of Illinois, Urbana Champaign, Stanford University, DARPA, the Center for AI Safety, Aura Labs. and Truera. 

**Why worry about AI?** The motivation for the paper is that today's large-scale AI systems are sufficiently powerful that they either compound or create new threats to safety. The "emergence of powerful technologies, such as generative AI, surface the dual-use dilemma," the authors write. 

**How might people use generative AI technologies to attack the world?**

  * Some of the key risks posed by generative AI technologies include:



  * Improved 'spear-phishing' attacks

  * Aiding the creation and dissemination of deepfakes

  * Increasing the amount of cyberattacks being conducted by making it easier for people to do them (e.g, via code models)

  * Reducing the barrier-of-entry for adversaries generally - general technologies make things generally cheaper. 

  * Data poisoning - you can generate and insert bad data into an environment that other people train on, silently corrupting systems. 



  * **How might we build defenses oriented around generative AI systems?** The authors also list some ways in which generative AI systems can be used to give us more defenses against these attacks. These include:

    * Systems for detecting LLM-generated content. 

    * Systems for watermarking the outputs of generative models broadly. 

    * Using code models to perform automated penetration testing to help strengthen complicated, digital infrastructures. 

    * Multimodal analysis; use the multimodal capabilities of AI models to do complex analysis on potential attackers, such as by identifying bot accounts on social media 




**What should we do about all of this?** The paper concludes with some ideas for what we should do to generally increase the safety of both the AI ecosystem and the wider world. The ideas roughly split into things we should do in the short term as well as things in the long term. 

**Short term:**

  * Conduct a "comprehensive analysis of the code-related capabilities of LLMs".

  * Ensure LLM-enabled code generation aligns with secure-coding practices.

  * Create a repository of state-of-the-art attacks and defenses. 




**Long term:**

  * Develop "multiple lines of defenses" for an AI-filled world. 

  * Reduce the barrier-to-entry for generative AI research. 

  * Explore "pluralistic value alignment" - think more deeply about the different values being encoded into these systems. 

  * Broaden the range of people working on advanced AI systems, including those making decisions about how to deploy them. 

  * Better tie LLMs and other generative AI systems to more factually correct sources of knowledge. 




**Why this matters - AI is an 'everything problem' with an 'everything solution':** As should be clear from above, AI is challenging to think about because it basically compounds most risks and also encodes within itself solutions to (or defenses against) these risks. The great challenge the world faces in the coming years it contending with an increasingly powerful 'everything technology'.  
**Read more** : [Identifying and Mitigating the Security Risks of Generative AI (arXiv)](https://arxiv.org/abs/2308.14840).

####################################################

**Oxford researchers make a stock market component simulator work on a GPU:  
**_…Eventually, superintelligent AIs will need supertools like JAX-LOB to do their work…  
_ Researchers with the University of Oxford have built JAX-LOB, software for simulating a limit order book (LOB) on a GPU. The purpose of the research is to create a useful component for simulating aspects of the stock market and training AI agents to perform automated trading activities. "Due to their central role in the financial system, the ability to accurately and efficiently model LOB dynamics is extremely valuable," they write. 

**What is JAX-LOB?** JAX-LOB is a "GPU-enabled Limited Order Book (LOB) simulator designed to process thousands of books in parallel with a notably reduced per-message processing time". The key here is that the researchers implement the simulation on a GPU - "in our environment, both the experience rollout (i.e. agents interacting with the world to collect data) and the learning updates (i.e. agents training on the data) are conducted on the same GPU which avoids the GPUCPU communication bottleneck"," they write. 

**How well does it work** : In tests, they show that JAX-LOB gets a 7X speedup over an equivalent system implemented on CPUs, able to perform 550 RL steps versus 74 steps per second during training on the same hardware. "This speedup due to parallelization is expected to contribute to research in applying RL to high-frequency trading and execution problems that require a reactive LOB simulator"

**Why this matters - superintelligences need supertools:** Systems like JAX-LOB are the kinds of tools that in the short term make it easier to do AI research in their particular domain (here, aspects of stock markets).   
But if we zoom out, in the future, we can expect the primary users of these tools to be _AI systems themselves!_ Today, we're starting to see people use large pre-trained models as virtual collaborators and these LLMs themselves tap into other bits of software to solve tasks (e.g, the GPT-4 code interpreter). As these trends become more pronounced, these AI systems are going to get more useful and capable in relation to how advanced the simulation tools they can access become - so software like JAX-LOB is interesting as it seems like the exact sort of thing that a future powerful AI may use to conduct its own financial experiments.   
**Read more** : [JAX-LOB: A GPU-Accelerated limit order book simulator to unlock large scale reinforcement learning for trading (arXiv)](https://arxiv.org/abs/2308.13289).

####################################################

**Alibaba trains and released a powerful vision-language model:  
**_…Qwen-VL is a ~9B multimodal model, mostly notable because a) it is released, and b) it is from China…  
_ Researchers with Alibaba Group have built Qwen-VL, a language model that can analyze images. They've also trained Qwen-VL-Chat, which is tuned to be easier to converse with in natural language. They've released both models via GutHub, so people can experiment with them themselves. 

**What's special about Qwen-VL?** Qwen-VL is part of a new generation of models which are multimodal - along with doing text analysis and generation, the models can also understand images (and eventually other modalities). Qwen-VL is based on an underlying 7B parameter language model, then is augmented with a vision transformer weighing in at 1.9B parameters.   
For the data, the system is built on about 1.4 billion image-text pairs, split across 77.3% English (text) data and 22.7% Chinese (text) data. The Chinese data comes from two primary sources - LAION-zh (105m), and "in-house data" (220m). 

**How well does it work?** A confounding factor here is there are a few proprietary multimodal models (GPT-4 with images, Gemini) where we don't have a good sense of performance, so here the authors instead need to test against models which are more legible. These are mostly (with the exception of DeepMind's 'Flamingo' models) open source ones. That said, here the models seem to do well, beating proprietary models like Flamingo on various image caption and general visual question answering tasks, and doing well relative to broadly available models on things like task-oriented VQA. However, evaluations for vision-language models are a young area, so it's not innately clear how good this really is. 

**What's next?** Next, the team will work on "Integrating QWen-VL with more modalities, such as speech and video", as well as by scaling up the model size and training data.   
**Read more:** [Qwen-VL: A Frontier Large Vision-Language Model with Versatile Abilities (arXiv)](https://arxiv.org/abs/2308.12966).  
**Get the models here:**[Alibaba, QwenLM (GitHub)](https://github.com/QwenLM/Qwen-VL).

####################################################

**Midnight training run**

 _[People who work at AI research companies, 2020s, Earth]_

We looked at the training run in the night, all of us who had access. 2am and we'd roll over in bed and check the loss curve on our phones.   
"Go to sleep," our partners would say.  
"Go to sleep," we'd say back to them.   
And we'd stare at the little line as it was making its slow, barely perceptible climb downward, and we'd think to ourselves: _what will you be?_

**Things that inspired this story:** All large models are ultimately represented as a loss curve over time; the value of symbols; the grim fascination with which one looks at a number like 'loss' and aligns it with our sense of the model as a living and breathing thing that we nurture and then interact with; the accidental poetry of the term 'loss' being used for the thing that matters most in AI in 2023.
