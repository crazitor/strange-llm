---
title: "Import AI 331: 16X smaller language models; could AMD compete with NVIDIA?; and BERT for the dark web"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-331-16x-smaller-language"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**  
Love open source AI and don't want to get hacked? Use safetensors:  
**_…A sensible security update - now signed off via a security audit…  
_ AI organizations HuggingFace, EleutherAI, Stability AI, have come together to subsidize a security audit of 'safetensors', a software library for safely "saving and loading tensors in the most common frameworks (including PyTorch, TensorFlow, JAX, PaddlePaddle, and NumPy)."

**Why they did this: "** The creation of this library was driven by the fact that PyTorch uses pickle under the hood, which is inherently unsafe," Eleuther writes. "With pickle, it is possible to write a malicious file posing as a model that gives full control of a user's computer to an attacker without the user's knowledge, allowing the attacker to steal all their bitcoins. While this vulnerability in pickle is widely known in the computer security world (and is acknowledged in the PyTorch docs), it’s not common knowledge in the broader ML community. Since the Hugging Face Hub is a platform where anyone can upload and share models, it is important to make efforts to prevent users from getting infected by malware."

**What the review found:** The security review didn't find any critical security flaws in safetensors, though did identify "some imprecisions in the spec format were detected and fixed", as well as "some missing validation allowed polyglot files, which was fixed."  
**Read more:** [Safetensors audited as really safe and becoming the default (EleutherAI blog)](https://blog.eleuther.ai/safetensors-security-audit/).  
**Check out** the full [Trail of Bits report here (Trail of Bits, GitHub)](https://github.com/trailofbits/publications/blob/master/reviews/2023-03-eleutherai-huggingface-safetensors-securityreview.pdf).  
**Find out[more](https://github.com/huggingface/safetensors)**[ about Safetensors here (HuggingFace, Safetensors)](https://github.com/huggingface/safetensors).

####################################################

**George Hotz's new company wants to make AMD a real competitor to NVIDIA, then make its own computers:  
**_…Legendary hacker takes on a task multiple megacorps have failed at - and you can bet people are rooting for him…  
_ George Hotz, legendary hacker and founder of the piratical self-driving car startup Comma.ai ([Import AI #2](https://jack-clark.net/2016/08/08/import-ai-issue-2-microsofts-ai-chips-george-hotzs-bandwidth-bill-and-spy-vs-spy/) \- !!!), has formed a new company dedicated to dethroning NVIDIA as the world's pre-eminent AI training chip. The company, Tiny Corp, has one simple (but very difficult) initial goal - build the software to help turn AMD's GPUs into viable competitors to NVIDIA's chips. Once it succeeds at that - which it measures by getting AMD chips to rank on the MLPerf competition using Hotz's 'tinygrad' software framework, it will start building its own chips.   
"If we even have a 3% chance of dethroning NVIDIA and eating in to their 80% margins, we will be very very rich," Hotz writes. "If we succeed at this project, we will be on the cutting edge of non NVIDIA AI compute."

**Why this matters - the road of bones:** The last ~decade of AI has featured numerous startup chip companies that have had the goal of dethroning NVIDIA's place as the pre-eminent AI chip company, ranging from startups like Cerebras and Graphcore, to the efforts of megacorps like Google (TPUs) and Amazon (Trainium). So far, the results are underwhelming - this month, NVIDIA's stock had a massive gain after it revealed in its earnings call that the entire world now wants to be buying its GPUs, surprising analysts with impressive figures around sales and future demands.   
The basic truth is that building software to train AI systems is really hard and NVIDIA has a 15+ year headstart on most others via its early investments in technology like CUDA and more. (And yes, I myself have periodically complained about how CUDA can be annoying to install, but it's 100X easier than other chips, in my experience and the anecdotal experience of others).  
So George Hotz et al are setting out on a road littered with the dead or decaying bodies of NVIDIA's competitors here. But you can rest assured people are going to be cheering from the sidelines - everyone wants there to be more competition in the AI chip market, so it'll be interesting to see how things develop. 

**Libertarian AI:** There's also a flavor of libertarian AI about all of this - "I don’t want to live in a world of closed AI running in a cloud you’ve never seen, I want everyone to have an AI that they own, both training and inference," Hotz writes. "I want compute to be available from 50 different companies all competing to drive the price to zero."  
**Read more** : [the tiny corp raised $5.1M (George Hotz blog)](https://geohot.github.io/blog/jekyll/update/2023/05/24/the-tiny-corp-raised-5M.html).

####################################################

**Washington wizards shrink LLM memory requirements by 16X, making it feasible to finetune on a single GPU:  
**_…QLoRA - If it's this easy to finetune models, then how does AI governance work?...  
_ Researchers with the University of Washington have introduced QLoRA, a way to very efficiently finetune large language models on small amounts of hardware. ""We demonstrate for the first time that it is possible to finetune a quantized 4-bit model without any performance degradation," they write. "QLORA reduces the average memory requirements of finetuning a 65B parameter model from >780GB of GPU memory to <48GB without degrading the runtime or predictive performance compared to a 16-bit fully finetuned baseline".

**This is a big deal - especially for AI governance:** These days, lots of people think about the safety of language models. You know how you can get rid of the safety of a language model? Finetune it. You know why finetuning is hard? Finetuning takes a ton of resources - typically lots of GPUs working in a distributed (and therefore hard to maintain) setup. You know what makes finetuning incredibly easy? Stuff like QLoRA. You know what that means? It's really, really difficult to prevent someone from being able to easily and arbitrarily modify the weights of a neural net using readily available hardware.   
So that's interesting!

**What they did:** QLoRA has a few components: 1) 4-bit NormalFloat, a way to quantize data in a 4-bit format that is better than other approaches, 2) Double Quantization, which lets you further improve the efficiency of the quantization, and 3) Paged Optimizers, a way to use "NVIDIA unified memory to avoid the gradient checkpointing memory spikes that occur when processing a mini-batch with a long sequence length."

**How well does it work?** To test out their approach, the researchers "train more than 1,000 models across several instruction tuning datasets, model architectures, and sizes between 80M and 65B parameters." They do this by studying results on finetuning RoBERTA, T5, and LLaMa on a few different datasets. The results yield "compelling evidence that 4-bit QLORA tuning reliably yields results matching 16-bit methods."

**Enter the Guanaco models:** To test out how well their approach works, the team tries to make a state-of-the-art chatbot by developing Guanaco, a LLaMA model finetuned via QLORA on the OASSTI1 dataset. The results show that Guanaco models set new states-of-the-art in a comparative evaluation versus GPT-4, coming closer than other systems (e.g, Alpaca, FLANv2, Open Assistant) at approximating its performance. In an ELO ranking against human raters, a 65B Guarnaco model gets an ELO of 1023 versus 1176 for GPT4 (and 916 for ChatGPT-3.5 Turbo).

**Why this matters - refinement and proliferation:** QLORA is basically a refined way to do finetuning. By refined, I mean it's way more efficient. In technology, whenever you make stuff faster or cheaper, you get more of it. This means, as the authors note, that QLORA "will make finetuning widespread and common". It also opens up new frontiers in on-device finetuning - "QLORA can finetune 3 million tokens per night while the phone is charging," they wrote.   
Overall, the view of the researchers is that "equalizing access to a technology that is quickly becoming ubiquitous will allow for better more independent analysis than keeping the power of LLMs in the hands of large corporations that do not release models or source code for auditing."  
**Read more:** [QLoRA: Efficient Finetuning of Quantized LLMs (arXiv)](https://arxiv.org/abs/2305.14314).

####################################################

**Scientists try to map the Dark Web by training a skeezy language model:  
**_…You merely try to classify the dark… I was trained in it…  
_ Researchers with KAIST and S2W Inc have trained 'DarkBERT, a text classification model pre-trained on 6.1 million pages of text mined from the dark web via Tor networks. The idea of DarkBERT is that the dark web has a different data distribution to the so-called surface web and so the hypothesis is by pre-training on a dark web corpus you'll end up with a model better at spotting things like drugs, credit card counterfeiting, hacking, and other internet-underbelly activities. In tests, DarkBERT does marginally better than standard BERT and RoBERTa classifiers, so the research is promising but not mind blowing. 

**What you can use DarkBERT for** : In tests, the researchers look at how well DarkBERT performs in three real world scenarios: 1) identifying ransomware leak sites, 2) figuring out codewords that are associated with threats or drug sales, and 3) identifying new potentially malicious threads in darkweb forums. On 1) and 2) DarkBERT does slightly better than typical models, while on 3) it does much, much better.  
"In the future, we also plan to improve the performance of Dark Web domain specific pretrained language models using more recent architectures and crawl additional data to allow the construction of a multilingual language model," they write. 

**Why this matters - automated spies for the underbelly of the world:** AI systems let us take a given thing we'd like a human to do and instead outsource that to a machine. Systems like DarkBERT point to a world where police and intelligence forces train a variety of 'underbelly' models to go and read (today), listen (also today - see Facebook's speech recognition system), and look (soon, as people tie language models to vision systems) at the world, continually analyzing it for increasingly rich and complex harms.  
How might this world look when the criminals, in turn, train their own classifiers to cue them to vulnerable targets? What does VictimBERT look like, I wonder?  
**Read more:**[ DarkBERT: A Language Model for the Dark Side of the Internet (arXiv)](https://arxiv.org/abs/2305.08596).

####################################################

**Facebook makes a speech recognition for the entire world, with a little help from the New Testament:  
**_…Better language models through Christianity, large unlabeled datasets, and heterogeneity…  
_ Facebook wants to help computers hear all the languages in the world and to that end has developed and released a family of models within its Massively Multilingual Speech (MMS) project. Concretely, Facebook has trained some large-scale AI models to recognize speech in around 1,000 languages, up from the 100 or so languages most speech systems involve today.   
"We trained self-supervised models on about 500,000 hours of speech data in over 1,400 languages — this is nearly five times more languages than any known prior work," Facebook said. 

**The New Testament:** To collect the data, Facebook " turned to religious texts, such as the Bible, that have been translated in many different languages and whose translations have been widely studied for text-based language translation research," it said. "As part of this project, we created a dataset of readings of the New Testament in over 1,100 languages, which provided on average 32 hours of data per language."  
**Not all religions:** "Our consultations with Christian ethicists concluded that most Christians would not regard the New Testament, and translations thereof, as too sacred to be used in machine learning," Facebook wrote. "The same is not true for all religious texts: for example, the Quran was originally not supposed to be translated."

**How well does it work?** In tests, MMS compares favorably to whisper on average error rates across a large corpus of languages. Specifically, Whisper has a word error rate of 44.3 for a model trained across ~100 languages with 680k hours labeled data, versus 18.7 word error rates for MMS models trained across ~1,100 languages with 45k hours of labeled data, when assessed via the 54-language 'FLEURS' benchmark. 

**Why this matters - machine minds to hear the world:** Systems like MMS are how we're going to wire up the real world and the AI-ghost-world together - rather than needing to rely on producing and gathering text, AI companies will instead by able to instrument applications and physical platforms with microphones and speaker and let their Ai systems continuously listen to the world and converse with it. We are taking the silicon spiritual plane and giving it access to the biological physical plane, and vice versa.   
**Read more:**[Introducing speech-to-text, text-to-speech, and more for 1,100+ languages (Meta AI blog.](https://ai.facebook.com/blog/multilingual-model-speech-recognition/))  
**Get the models here** : [MMS: Scaling Speech Technology to 1000+ languages (GitHub)](https://github.com/facebookresearch/fairseq/tree/main/examples/mms).  
**Read the paper:** [Scaling Speech Technology to 1,000+ Languages (Facebook, pdf)](https://scontent-atl3-2.xx.fbcdn.net/v/t39.8562-6/348836647_265923086001014_6878005808275791319_n.pdf?_nc_cat=104&ccb=1-7&_nc_sid=ae5e01&_nc_ohc=5exJiCqt0Y4AX-thMVD&_nc_ht=scontent-atl3-2.xx&oh=00_AfBiILO4iLHUoyQ6r-ZPn4HVGviI2Fqyezvv7Tf_yHxMew&oe=6471ACCF).

####################################################

**Want to reduce dangerous misuses and harms of AI? Test for them!  
**_…Researchers (including me) state the obvious - but you'd be surprised how immature this field is!...  
_ A new research paper from Google DeepMind, the University of Cambridge, University of Oxford, University of Toronto, Université de Montréal, OpenAI, Anthropic (specifically, me), Alignment Research Center, Centre for Long-Term Resilience, and Centre for the Governance of AI. says one good way to reduce risks from AI systems is for researchers to evaluate AI systems for "extreme risks", which DeepMind describes as looking at models, like LLMs, which "have strong skills in manipulation, deception, cyber-offense, or other dangerous capabilities." 

**Two steps to safer models:** Model developers should assess the extent to which models have certain 'dangerous capabilities' that could be used in harmful ways. Once they've done this analysis they should look at how likely the model is to apply or demonstrate these capabilities in ways that can cause harm. "Results from these evaluations will help AI developers to understand whether the ingredients sufficient for extreme risk are present," the researchers write. 

**Why this matters - you can't manage what you can't measure:** Most AI policy proposals rely on the ability to evaluate for some adverse property of an AI model - papers like this give an outline for how we might do that, though the harder next step will be building the evaluations themselves.  
**Read more:** [An early warning system for novel AI risks (Google DeepMind, blog)](https://www.deepmind.com/blog/an-early-warning-system-for-novel-ai-risks).  
**Read the research paper:** [Model evaluation for extreme risks (arXiv)](https://arxiv.org/abs/2305.15324).

####################################################

**Tech Tales:**

**Personality Variation  
**[A parent dealing with her kid coming home from school, America, 2028]

No bring him back I _liked_ him!   
I know you did sweetie, we're getting a different one tomorrow you might like more.   
But the one I had today sucked. It was so boring.   
I know you're upset but it's not possible, we can't bring him back… please stop crying. 

[via phone] Hello yes this is [REDACTED], my child attends the [REDACTED] school on Hollis and they really want to get the model in which was in the school on Tuesday.   
[via phone] "I'm sorry ma'am but that's not possible, we vary out the systems a stipulated by the regulations in the Personality Accords"  
[via phone] There's really nothing you can do? My child is very upset and I spoke to some other parents and their kids are freaking out as well.   
[via phone] "I'm afraid not ma'am, that'd be breaking the law." 

Honey look, you're going to have a different system tomorrow but it'll be fun I promise.   
I don't care about it being fun I want the one I had yesterday.   
You have to get used to this sweetie. This is how things have to be.   
But _why_ do they have to be like this?  
Because some bad things happened baby, I don't know what to tell you.

**Things that inspired this story** : Provably Conscious Entities, the Personality Accords, the Sentience Accords, regulation and its downstream effects, the innocence of youth, parenting within the exponential.
