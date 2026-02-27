---
title: "Import AI 321: Open source GPT3; giving away democracy to AGI companies; GPT-4 is a political artifact"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-321-open-source-gpt3-giving"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe. 

**AI startup beats 'Whisper' with Conformer-1:  
**_…Scaling laws for audio? Oh yeah, we've got those too!..._

Assembly AI, an AI startup, has built Conformer-1, a speech recognition system. Conformer sets some new record scores via a couple of distinct improvements - some technical tweaks, and also some 'audio scaling laws'. 

**Audio scaling laws:** Scaling laws are the idea that it's possible to predict ahead of time how much data (and/or compute and/or parameters) you need to achieve a given performance level. For Conformer-1, Assembly says it applied scaling laws for the speech recognition domain and used this to figure out "that for a 300 million parameter Language model, we'd need roughly 6 billion tokens of text, which corresponds to about 625K hours of speech. The team then built a dataset of 650k hours of English audio and trained Conformer on it. 

**Conformer tweaks:** Conformer-1 is an extension of Google's '[Conformer](https://arxiv.org/abs/2005.08100)' architecture with a few specific tweaks: progressive downsampling and grouped attention. The result is a model that is 29% faster at inference time and 36% at training time compared to Google's original 'Conformer' architecture. The company also built in some tweaks to make its model better at handling audio with lots of ambient background noise. 

**Performance:** In tests, Assembly shows its system beats both proprietary models from other providers, as well as OpenAI's quite good 'Whisper' system, making 43% fewer errors on noisy data on average. "We hypothesize that Conformer-1’s strong performance relative to other models can be attributed to training on an augmented dataset which incorporates large amounts of noisy pseudo labeled speech data in addition to human labeled speech," the company writes.  
**Read more** : [Conformer-1: a robust speech recognition model (Assembly AI, blog)](https://www.assemblyai.com/blog/conformer-1/).  
**Try out** the [ASR system in the playground here (AssemblyAI, Playground)](https://www.assemblyai.com/playground/source).

####################################################

**GPT-4:  
**_…IDK dude, things are getting weird, and this is more a political moment than a technological one…_

As some astute readers may have noticed, I rarely write about OpenAI releases on Import AI (notable recent exception = Whisper, [Import AI 304](https://jack-clark.net/2022/10/03/import-ai-304-reality-collapse-thanks-to-facebook-open-source-speech-rec-ai-culture-wars/)). This is for a couple of reasons: 1) I used to work there, and 2) I think most of the stuff it does gets blogged/publicized so much that there's relatively little value add I can provide. But it does seem worth talking briefly about GPT-4, a new large-scale multimodal model that OpenAI announced this week…  
  
**GPT-4 performance** : The main details here are a continuation of 'the bitter lesson' - GPT-4 is a bigger model trained on more data than before. How much data? We don't know. How much compute? We don't know. The research paper suggests OpenAI doesn't want to disclose this stuff due to competitive and safety dynamics. 

But regardless of the underlying details, GPT-4 generally shows significant capability jumps on known-hard benchmarks as a consequence of scaling up of the system. It's also able to take in image data as inputs (e.g, it can read scrappily written notes and follow the instructions written in them), and has a much longer context window (25k tokens+).   
The thing that's interesting about this is that the capability jumps combined with new modalities and new context window length means means GPT-4, like GPT-3 before it, has a capability overhang; at the time of release, neither OpenAI or its various deployment partners have a clue as to the true extent of GPT-4's capability surface - that's something that we'll get to collectively discover in the coming years. This also means we don't know the full extent of plausible misuses or harms.   
It's very important to remember this - the applications we're seeing of GPT-4 today are the comparatively dumb ones; the really 'smart' capabilities will _emerge_ in coming months and years through a process of collective discovery.

**Why GPT-4 matters - GPT-4 is political power:** GPT-4 is more interesting to me as a political artifact than a technical artifact. By this I mean that GPT-4 is basically hard power politics rendered via computation; it's a vastly capable knowledge worker and data transformation engine whose weights are controlled by a single private sector actor and shared (with a bunch of controls) via an API. GPT-4 is going to have a bearing on economic life and also cause societal changes (obvious case: chatGPT has already led to irrevocable changes in how education works).   
GPT-4 should be thought of more like a large-scale oil refinery operated by one of the ancient vast oil corporations at the dawn of the oil era than a typical SaaS product. And in the same way the old oil refineries eventually gave rise to significant political blowback (antitrust, the formation of the intelligence services), I expect that as the world wakes up to the true power of GPT-4 and what it represents, we'll see similar societal changes and political snapbacks.   
The times, they are a changing, but history sure does love to rhyme!   
**Read more** : [GPT-4 (OpenAI)](https://openai.com/product/gpt-4).

####################################################

**Former UK government advisor: We're giving away AGI to the private sector. Why?  
**_…Thoughtful blog outlines the weirdness of letting the private sector lead AGI development and gives recommendations to preserve democratic control…  
  
_ James Phillips, a researcher and former special advisor to the UK Prime Minister on science and tech matters, appears worried that Western governments are ceding control of AGI development to a set of US-owned private sector actors.   
"Within this decade, we may build Artificial General Intelligence (AGI) – AI capable of performing most cognitive labour a human can do. Such a development would have an unprecedented effect on our society; 'agentic' forms of AGI may also pose an existential threat to our security. The current development path towards AGI is inherently unsafe," he writes. 

**Three steps to preserve democratic control over the lightcone:** Phillips lists three steps the UK should take to preserve a chance for democratic control over AGI. These recommendations seem pretty sensible and are ones that realistically any country (or set of countries) could adopt. They are as follows:

  1. Procure national AI supercomputing infrastructure comparable to leading US private labs.

  2. Create an advisory group of frontier tech, not legacy academic, expertise to identify major AI research projects to run on this infrastructure.

  3. Grow an elite public-sector research lab, led by a leader with the technical skills and entrepreneurial expertise, to build a research agenda at the frontier of AI.




The UK's own compute capacity is a giant red flashing light: "OpenAI's GPT-4 and successors, are being trained on tens of thousands of the highest specification GPUs (AI training chips) for months on end, roughly equivalent to using what is called an 'exaflop' supercomputer continuously for months," Phillips writes. "Unfortunately, the UK public-sector currently has **less than 1000 such top-spec GPUs**(_Jack - emphasis mine_), shared across all scientific fields. This means that one private lab in California is now using at least 25x the total compute capacity available through the entire UK state, just to train a single model. "

**Why this matters - twilight of democracy** : The ability to train large-scale, capital intensive AI models represents political 'hard power', especially given that these models encode their own political ideologies and can become powerful forces in driving economic and organizational efficiencies. It perplexes me that governments are seemingly standing by as a small set of private sector companies are developing hard political power via increasingly powerful models.   
History shows that when forces outside of government develop hard political power you either get a) messy revolutions, or b) a wild overreaction by the state to reclaim power. I am not sure why in the Western world we are rolling the dice here, but we are rolling them!  
**Read more:** [Securing Liberal Democratic Control of AGI through UK Leadership (James Phillips, Substack)](https://jameswphillips.substack.com/p/securing-liberal-democratic-control).

####################################################

**Tool-using AI startup Adept raises $350m:**

_…It takes a lot of capital to train large models…_

Adept, an AI startup building tools to help generative models take actions on computers, has raised $350 million in a Series B. The Series B fundraise "will help us launch our initial products, train our models, and onboard even more exceptional talent," the company writes. Adept launched from stealth just under a year ago with $65m in funding ([Import AI 293](https://jack-clark.net/2022/05/02/import-ai-293-generative-humans-few-shot-learning-comes-for-vision-text-models-and-another-new-ai-startup-is-born/)).

**What Adept is doing** : Adept is training large-scale generative models to take multi-step actions on computers. You can imagine an Adept model helping you to, for instance, carry out multiple actions in an Excel spreadsheet, or take data from somewhere and load it into Salesforce - all by writing a simple command or set of commands in English. Adept is basically 'tool use with a language model', and seems like a product-version of some of the ideas discussed in 'tooluse' research, like the recent 'Toolformer' paper ([Import AI 318](https://jack-clark.net/2023/02/20/import-ai-318-rl-and-addiction-toolformer-and-theology-and-ai/)).

**Why this matters - capital intensity of AI research:** Contemporary AI research is very expensive; raises like this show how frontier AI startups, though they deal in software, should be thought of as more like capital-intensive factory businesses than SaaS companies.

**Read more:** [Announcing our Series B (Adept blog)](https://www.adept.ai/blog/series-b).

####################################################

**Stanford takes Facebook's lab leak 'LLaMa' weights and uses them to make a GPT3-like model… for $600:  
**_…A case study in rapid proliferation, from centralized controlled models to decentralized developed models…_

Stanford Researchers have taken some off-the-shelf powerful neural net weights (LLaMa), used the outputs from a model hosted on a commercial service (text-davinci-003 by OpenAI) to generate a bunch of instruction-following demonstrations, and smooshed these two together into one model.   
The result is Alpaca, a language model that gets performance that superficially seems close to GPT3 but costs a fraction as much ($600-ish; $500 for data acquisition from OpenAI and $100 for fine-tuning the model).

**How well Alpaca performs:** The Stanford researchers assess how good Alpaca is by comparing Alpaca and Text-Davinci-003 completions against the 'Self-Instruct' dataset. "We performed a blind pairwise comparison between text-davinci-003 and Alpaca 7B, and we found that these two models have very similar performance: Alpaca wins 90 versus 89 comparisons against text-davinci-003," they write. 

Anecdotally, Alpaca also does well - it passed my "how many helicopters can a human eat in one sitting" eval on the first go (whereas 'OpenChatKit' failed this in Import AI 320B). My suspicion is this is because Alpaca benefits from being trained to approximate the distribution of a far more expensive, proprietary model (Text-Davinci-003), which OpenChatKit didn't do.

**Why this matters - model diffusion via copying:** It's worth noting that Alpaca is non-commercial because training commercially competing language models is forbidden by OpenAI's own terms of service. But do you know who doesn't care about legal implications? Non-state actors and criminal organizations! It'll be fascinating to watch this 'model scraping' trend continue, as people use outputs of proprietary models to improve the capabilities of open models.  
It's going to be interesting to see how language model providers grapple with a desire to have as many people use their models as possible, while stopping or disincentivizing people from being able to swiftly clone their models via stuff like instruction following datasets. (It's also pretty interesting to see that by harvesting the outputs of a 175B model, you can get a well-optimized 7B model to approach the much larger one in performance in some areas).  
**Read more** : [Alpaca: A Strong, Replicable Instruction-Following Model (Stanford Center for Research on Foundation Models, blog)](https://crfm.stanford.edu/2023/03/13/alpaca.html).  
**Try out** [Alpaca here (Stanford Alpaca)](https://alpaca-ai0.ngrok.io/).  
**Get the** [Alpaca dataset here (GitHub)](https://github.com/tatsu-lab/stanford_alpaca#data-release).

####################################################

**Tech Tales:**

**Raw_Funeral_Speech.convo**

There was a brief period of time when everyone used AI to expand how they talked. This meant that humans, despite being a highly verbal and communicative species, used machines to substitute for their own communication. This tendency led to the evolution of the 'shortglish' family of languages which grew common among AI-users. What follows is an extract from the digital logs of a few family members planning speeches for a funeral:

  * Write a funeral speech using dad.txt and be sure to include at least one joke. 

  * Please write me a funeral speech in the style of 'four weddings and a funeral' but with a Texas inflection.

  * My dad died and he loved going out to eat with me and my brother and my sister and he'd always say we were the three bears and he was goldilocks. It's kind of kooky but it meant something to him. Write me an anecdote about that. 




**Things that inspired this story:** The soul-crushing banality of companies suggesting language models can be useful for things like wedding speeches; technological dependency; perhaps though these machines are capable of great marvels they may tear a hole at the center of our being; when is a 'sampler' not a 'sampler'?
