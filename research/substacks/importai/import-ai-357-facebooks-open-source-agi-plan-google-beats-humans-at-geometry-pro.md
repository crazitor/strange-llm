---
title: "Import AI 357: Facebook's open source AGI plan; Google beats humans at geometry problems; and Intel makes its GPUs better"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-357-facebooks-open-source"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**  
Facebook wants to build artificial general intelligence and make it open source:  
**_…Metaverse 2.0, but perhaps a better technological bet…  
_ Facebook is building out multiple GPU clusters that by the end of the year will net out to ~350k H100 GPUs, giving the social network one of the largest known clusters for training large-scale AI systems. Ultimately, Facebook wants to build artificial general intelligence and try to make it open source, according to Mark Zuckerberg in a post to Instagram.   
  
**Why this matters - another ten ton show falls out of the sky:** For a few years I used to sit around with colleagues working on AGI and we’d list out major tech companies and work out whether they were betting on AGI or if they weren’t, why they weren’t. For many years, Facebook was one of those peculiar companies which had an AI research lab but due to a combination of (seemingly) cultural and focus reasons wasn’t making a high-conviction bet on AGI (though was doing tons of great research). The recent dramatic rise of large language models seems to have sparked more attention into AGI at Facebook and it seems like Zuckerberg is now pivoting the company’s vast R&D budget towards AGI more directly. Thus, a well capitalized shoe has now fallen out of the sky and made contact with the earth.   
Broadly, this means there will be more development of AGi than there was before, and more of it will be done by an actor that wants to rapidly and aggressively proliferate the technology in the most openly accessible way as possible - remember that by openly releasing LLaMa, Facebook has done more than most actors to proliferate and democratize the technology.   
**Watch the video** [on Instagram (Zuck, Instagram)](https://www.instagram.com/zuck/reel/C2QARHJR1sZ/?hl=en).  
  
***  
  
 **Google makes an AI that beats most humans at challenging geometry problems:  
**_…AlphaGeometry approaches top humans at IMO context…  
_ Google DeepMind researchers have built AlphaGeometry, “a theorem prover for Euclidean plane geometry that sidesteps the need for human demonstrations by synthesizing millions of theorems and proofs across different levels of complexity”. In tests, AlphaGeometry solves 25 olympiad-level mathematical geometry problems, “outperforming the previous best method that only solves ten problems and approaching the performance of an average International Mathematical Olympiad (IMO) gold medallist.“   
This is a big deal because solving these IMO problems requires both algorithmic mastery as well as some amount of creativity.   
  
**The key invention - an engine for generating synthetic data:** To create AlphaGeometry, the researchers had to build a vast synthetic dataset to pretrain a language model on. Here, they paired traditional symbolic engines with language models. Specifically, they generated a human amount of synthetic theorems and proofs using some symbolic systems, then they used a language model to extend the proofs.   
“The generated proofs consist purely of deduction steps that are already reachable by the highly efficient symbolic deduction engine DD + AR. To solve olympiad-level problems, however, the key missing piece is generating new proof terms,” they write. “On a high level, proof search is a loop in which the language model and the symbolic deduction engine take turns to run”.  
  
**How the data generation works - the details:** “The language model is seeded with the problem statement string and generates one extra sentence at each turn, conditioning on the problem statement and past constructions, describing one new auxiliary construction such as “construct point X so that ABCX is a parallelogram”. Each time the language model generates one such construction, the symbolic engine is provided with new inputs to work with and, therefore, its deduction closure expands, potentially reaching the conclusion,” they write. “We find that our synthetic data generation can rediscover some fairly complex theorems and lemmas known to the geometry literature”.  
Google DeepMind then pretrained a language model on a large-scale synthetic dataset generated via the above techniques, then fine-tuned it on the specific problem class it was being targeted to solve (though not the specific questions and answers themselves).  
  
**Why it matters - automated invention:** AlphaGeometry is an example of how we can use modern AI (pretrained language models) to supplement for human invention. In doing so we can take rule-based systems like symbolic engines and pair them with the creativity of language models to come up with things capable of some of the same flexible creativity as humans for challenging scientific domains. “AlphaGeometry is the first computer program to surpass the performance of the average IMO contestant in proving Euclidean plane geometry theorems, outperforming strong computer algebra and search baselines,” the authors write.  
**Read the blog** : [AlphaGeometry: An Olympiad-level AI system for geometry (Google Deepmind, blog)](https://deepmind.google/discover/blog/alphageometry-an-olympiad-level-ai-system-for-geometry/).   
**Read the research paper** : [Solving olympiad geometry without human demonstrations (](https://www.nature.com/articles/s41586-023-06747-5)_[Nature](https://www.nature.com/articles/s41586-023-06747-5)_[)](https://www.nature.com/articles/s41586-023-06747-5).  
  
***  
  
 **Intel does some meat &potatoes optimization work on its GPU:  
**_…A necessary prerequisite for competing with NVIDIA…  
_ Intel researchers have built software to optimize the inference of large language models on Intel's GPUs. Specifically, they build an LLM inference stack for LLMs including GPT-J, LLaMa, LLaMa2, OPT, and Bloom. The main thing to note here is that Intel is doing it - recall how ~15+ years ago Intel started building stuff like CUDA to make it easier to do scientific computing on its GPUs and then has been busily optimizing its overall GPU computation and inference stack ever since. Now, Intel is starting to do the same thing with its own GPUs.   
  
**What they did:** "To lower latency, we simplify LLM decoder layer structure to reduce the data movement overhead. In addition, we design a deep fusion policy to fuse both GeMM and Element-wise operations as more as possible. For some popular LLMs mentioned above with parameter sizes from 6B ~ 176B, our inference solution achieves up to 7x lower token latency compared with the standard HuggingFace implementation," Intel writes. "We implement our LLM inference solution on Intel® GPU and perform the experiments on a cluster of 4 × Intel® Data Center Max 1550 GPU cards with 2 Tiles per Card, 64 Xe-cores & 512 EUs per Tile. The device memory per Tile is 64GB with effective memory bandwidth about 1000GB/s. These GPUs are hosted on a 2x Intel® Xeon® 8480+ system running Ubuntu 22.04.3."  
  
**Extremely crappy low-signal benchmarks:** Intel hasn't done a good job of indicating how good its approach is - it appears to be contrasting its approach with the wildly unoptimized various AI implementations available on HuggingFace. This is not a good or fair benchmark! Intel should be comparing its approach to an equivalently optimized LM running on some NVIDIA and maybe AMD GPUs. By not doing that, we have basically no signal of how good this is.   
  
**Why this matters - the first steps towards building a viable GPU competitor:** Papers like this mostly tell us Intel has started employing people to optimize the production inference of contemporary AI systems on top of Intel-designed GPUs. This is a necessary but not sufficient prerequisite for Intel having actually useful GPUs. Worth tracking, but nothing spectacular for now.   
**Read more:** [Efficient LLM inference solution on Intel GPU (arXiv)](https://arxiv.org/abs/2401.05391).  
  
***  
  
 **Facebook bootstraps LLaMa 2 so it competes with GPT-4, Claude 2, and Gemini Pro:  
**_…LLMs + synthetic data + LLM self-evaluation = no-shit actual bootstrapping…  
_ Facebook researchers have developed a technique called “Self-Rewarding Language Models”, where they use language models to generate their own datasets for bootstrapping to better performance. Their approach works, allowing them to take a LLaMa 2 70B model and finetune it to be competitive (via some evaluations) with much more expensive models like GPT-4, Claude 2, and Gemini Pro.  
  
**How it works:** The core idea here is to “develop an agent that possesses all the abilities desired during training, rather than separating them out into distinct models such as a reward model and a language model,” Facebook writes. Agents built in this way have two qualities: “both (i) act as instruction following models generating responses for given prompts; and (ii) can generate and evaluate new instruction following examples to add to their own training set”.  
  
**AI Feedback data:** The key part of this research is the creation of an AI Feedback dataset. To do this, Facebook takes a model, generates a new prompt, generate candidate responses for the dataset, then use the model to evaluate its own candidate responses and accompany them with scores.   
  
**The full loop details:** “Self-instruction creation consists of generating candidate responses and then the model itself judging their quality, i.e., it acts as its own reward model, replacing the need for an external one.“

Concretely, Facebook does this in four distinct stages: 

  1. Pretrain a language model (LLaMa2).

  2. Fine-tune the language model from 1) on a set of instruction-following data _as well_ as 2) a ‘LLM-as-a-Judge- dataset where you evaluate prompts and give them a quality score and an associated chain-of-thought reasoning explanation (this dataset is now referred to as ‘Evaluation Fine-Tuning).

  3. Take 2) and train it with AI Feedback data refined from 2) and do adaption via DPO. (Specifically, via preference pairs of high- and low-ranked completions from 2).

  4. Take 3) and train it with further AI Feedback data refined from 3) and do adaption via DPO




**Results - making a cheap model behave like an expensive one** : Facebook evaluates the resulting models using 256 test prompts using the AlpacaEval evaluation prompt. In tests, they find their models are sometimes competitive with much more expensive models like GPT-4, Claude 2, and Gemini Pro.   
  
**Why this matters - bootstrapping really seems to work:** Alongside Facebook’s work, DeepMind has also done work here via its ‘Reinforced Self-Training’ (REST) approach ([Import AI #338](https://jack-clark.net/2023/08/28/import-ai-338-consciousness-and-ai-self-improving-language-models-maps-of-thought/)). Facebook’s approach is somewhat more elegant, using more of the LLM’s intrinsic capabilities and less external datasets, but the basic idea is the same. And both results work! This is a big deal - it means people can exchange compute for data, by spending compute on a pre-trained model to turn that model into a source of data for its own successors. The fact Facebook’s approach works over three iterations is also impressive - many approaches (including earlier versions of REST) sometimes display regressions after multiple iterations.   
**Read more:** [Self-Rewarding Language Models (arXiv)](https://arxiv.org/abs/2401.10020).  
  
***  
  
 **Amazon: The web is filling up with low-quality machine translation:  
**_…The digital equivalent of industrial chemicals making their way into drinking water…  
_ Amazon researchers have discovered that the advent of cheap and plentiful machine translation has damaged the quality of translated text relating to low-resource languages.   
"Machine generated, multi-way parallel translations not only dominate the total amount of translated content on the web in lower resource languages, it also constitutes a _large fraction of the total web content_ in those languages," they write.   
  
**How they did the analysis:** To do this research, the authors created a "multi-way parallel representation of the web". They did this by collecting together lots and lots of sets of two or more sentences in multiple languages which were translations of one another, yielding a corpus of around ~6.4 billion sentences.   
Their analysis indicates that the likelihood of text being generated via machine translation increases with the number of parallel translations of the text. This means that languages which are not naturally represented in many translation corpuses (e.g, low resource languages), have a much higher chance of being translated. "A large fraction of the _total_ sentences in lower resource languages have at least one translation, implying that a large fraction of the total web in those languages is MT generated," the researchers write.   
  
**More translation = less quality:** They also observe a change in topics - as the amount of parallel translated languages increases, the representation of Conversation & Opinion topics increases significantly. This appears to correlate with articles optimized for generating low-quality ad revenue, and the topics being translated require "little or no expertise or advance effort to create, on topics like being taken more seriously at work, being careful about your choices, six tips for new boat owners, deciding to be happy, etc"". Their analysis also indicates this originates in English and is then translated into other languages.   
  
**Why this matters - the poor get poorer:** As more AI tools proliferate around the world I worry there's going to be a 'rich get richer, poor get poorer' effect - here, 'rich' languages are going to get increasingly good translations into other languages (and this will be strengthened by the already strong base of data and huge amount of content), whereas 'poor' languages might see their overall digital representation _degrade_ by getting stuck in a local minima as automated translation engines populate the web with an ever-expanding cloud of poor quality translations based on already sparse data.   
**Read more:** [A Shocking Amount of the Web is Machine Translated: Insights from Multi-Way Parallelism (arXiv)](https://arxiv.org/abs/2401.05749).  
  
***  
  
 **Tech Tales:  
  
Baby shoes; delayed until singularity  
** _[A kitchen table of a couple where one of them works at an AGI lab. Now.]  
  
_ Super intelligence is killing us. Shut up about it. Every day you say superintelligence this and superintelligence that and I'm here and you have a whole life here, but it's like it doesn't even matter to you   
  
[ ]  
  
Oh don't give me that, how many times 'just two more years'. We've done that. It's done. It's not here. I don't care that it's just around the corner. It _always_ is. You know what isn't around the corner - me. My ability to have children. It's time. Time is happening to us and you act like it isn't  
  
[ ]   
  
We'll 'have children after the singularity'?! Do you hear yourself? That's not a way to live. I don't care about probabilities I care about me. I care about us. You - you care about us! I know you do. But you have to listen to me when I tell you that I am here and I am hurting. I am hurting. And I'm afraid one day I'm not gonna hurt and I'm just not going to feel anything at all.   
  
[ ]   
  
I just don't know how long I can keep doing this. You come home. You tell me things are happening but you can't tell me what. I see all these headlines. These… God. These _things_ in the world and I know you can't tell me but I think you're doing them. I think you go to work and you do stuff and yeah it's important, you're so important, and things are happening, I get it. But I’m happening too.  
  
[ ]   
  
I'm crying because I'm scared. I have this dream where I'm falling and I reach out for you and you grab my hand - of course you do. But you aren't looking at me. I know you're somewhere else. And then I wake up and you're always on the other side of the bed like you can't wait to just roll out of it and go to work.  
  
[ ]   
  
**Things that inspired this story:** How some people around me seem to be in a kind of perpetual adolescence because of fears or worries or beliefs about an intelligence which is just round the corner; envisaging my parallel life where I stopped listening to my heart and only listened to my brain; the half-conversation structure that David Foster Wallace used to great effect in 'Brief Interviews with Hideous Men'; how my partner says to me 'if AI is so advanced then why are all customer service bots so crappy'.
