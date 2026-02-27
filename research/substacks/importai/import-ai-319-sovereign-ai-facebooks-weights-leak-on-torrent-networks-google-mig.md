---
title: "Import AI 319: Sovereign AI; Facebook's weights leak on torrent networks; Google might have made a better optimizer than Adam!"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-319-sovereign-ai-facebooks"
---

Welcome to Import AI, a (mostly) weekly newsletter about AI research and development. The issues are free, but paid subscribers will get access to special analysis pieces before anyone else. Founding members can help support me further and fund special projects and other _top secret Import AI initiatives!_ Thanks for reading! 

**Vision models are about to get way more capable - and human:**  
_…Google swaps out vision model guts for a transformer, scales it, and gets some promising results…_  
Google researchers have ripped out the guts of standard large-scale computer vision models and replaced them with a Vision Transformer (ViT) - an architecture modeled on the transformer which has proved so successful in domains like text. They've also scaled this ViT to 22B parameters (up from a record of 4B parameters for a ViT previously).   
The results are compelling and echo the returns-from-scale effects seen in language: "When evaluated on downstream tasks," they write. "ViT-22B demonstrates increasing performance with scale. We further observe other interesting benefits of scale, including an improved tradeoff between fairness and performance, state-of-the-art alignment to human visual perception in terms of shape/texture bias, and improved robustness." 

**JFT just keeps getting bigger:** Google has a mostly-secret giant image dataset called ;'JFT' which was previously reported to be about 300 million images. Here, the paper says they trained the ViT-22B on a version of JFT which had been "extended to around 4B images". 

**Humanlike biases:** ""The ViT-22B models have the highest ever recorded shape bias in vision models: while most models have a strong texture bias (approx. 20–30% shape bias / 70–80% texture bias); humans are at 96% shape / 4% texture bias and ViT-22B-384 achieves a previously unseen 87% shape bias / 13% texture bias. Overall, ViT-22B measurably improves alignment to human visual object recognition," the authors write. 

**Why this matters - scale develops human-like qualities:** There's a weird trend in contemporary AI where as we scale-up the amount of pre-training dumped into transformer-architecture models we end up with systems that display human-like qualities. This has been most prominent in language, but it has also started showing up in RL, like DeepMind's recent result where massive pre-train leads to an agent that displays humanlike timescale-adaption to new tasks. This ViT-22B result, while not setting a new state-of-the-art, is interesting for a similar reason - it displays a major jump in shape/texture bias that brings the system in distribution with human visual perception, whereas previous convnet based systems were very far off here.   
There's something strange and important going on here. I think transformers seem to allow for emergent complexity at scale, where pre-training leads to systems which arrive at humanlike performance qualities given enough pretraining.   
**Read more:** [Scaling Vision Transformers to 22 Billion Parameters (arXiv)](https://arxiv.org/abs/2302.05442).

​  
####################################################

**Google might have invented a better optimizer? (Via AI, of course).**  
_…Could Lion replace Adam? There's a chance!..._  
Deep learning projects have a few essential components - the architecture (e.g, a residual network, or a transformer model) and the optimizer (e.g, Adam). These components don't tend to change much in large-scale projects - once people figure out something that works well for complicated tasks like training ImageNet, everyone tends to converge on using the same basic thing. For many years now, most projects have used the 'Adam' optimizer to optimizer their models during training. Now Google says that it has used some clever AI search approaches to help it identify a better optimizer, called Lion. The reason this is worth paying attention to is Lion seems to work well on large-scale, real world tasks like training ImageNet-scale computer vision systems. 

**What they did:** Google's main contribution here is "a method to formulate algorithm discovery as program search", which they apply to figuring out a better optimizer. They use a symbolic approach where they shrink the search problem down into a somewhat tractable space and, crucially, they test out candidate optimizers on "metavalidation tasks that are larger than the proxy tasks by increasing the model size and training steps, to select the programs that generalize beyond proxy tasks then further simplify them."   
Add in a bunch of computation and out pops an optimizer they call EvoLved Sign Momentum, or Lion for short (_really grasping at straws with this acronym, folks!)._ Lion "differs from various adaptive algorithms by only tracking momentum and leveraging the sign operation to calculate updates, leading to lower memory overhead and uniform update magnitudes across all dimensions".

**Good performance:** Google tests Lion on a large range of tasks and finds that it "demonstrates outstanding performance across a range of models (Transformer, MLP, ResNet, U-Net, and Hybrid) and tasks (image classification, vision-language contrastive learning, diffusion, language modeling, and fine-tuning)".It even sets a new high score on ImageNet, a competitive computer vision benchmark. 

**Why this matters:** Lion may be fundamentally better than Adam - if true, that's a big deal. It's not often you see meaningful improvements in very well studied, generic parts of AI research. Add to the fact that Lion was discovered via a human-AI search process (the humans designed the search system, the search system found Lion), and you have the makings of a notable result.   
**Read more** : [Symbolic Discovery of Optimization Algorithms (arXiv)](https://arxiv.org/abs/2302.06675).  
**Get the[code](https://github.com/google/automl/tree/master/lion)**[ here (GitHub)](https://github.com/google/automl/tree/master/lion).

####################################################

**Globalization? That's so 20th century. The 21st century is about balkanization through sovereign infrastructure:**  
_…Dawn of the era of sovereign AI…_  
Researchers with the Tony Blair Institute for Global Change (TBI) have written a report for how England can thrive in the 21st century - one of the key ideas in the report is "Government-led development of sovereign general-purpose AI systems, enabled by the required supercomputing capabilities, to underpin broad swaths of public-service delivery."

**AI balkanization was probably inevitable** : This recommendation is part of a wave of AI balkanization that's sweeping across the world as various people realize that it's unlikely there are 'one size fits all' models, both for ideological reasons as well as for national security reasons. (See the Gab CEO wanted to make a Christian LLM, [Import AI 318](https://jack-clark.net/2023/02/20/import-ai-318-rl-and-addiction-toolformer-and-theology-and-ai/)). This is also accompanied by various nationalistic efforts to create country-specific GPT3 models.   
"Given these AI systems will soon be foundational to all aspects of our society and economy, it would be a risk to our national security and economic competitiveness to become entirely dependent on external providers," the TBI researchers write. "Leading actors in the private sector are spending billions of dollars developing such systems so **there may only be a few months (**_emphasis mine - Jack)_ for policy that will enable domestic firms and our public sector to catch up."

**Why this matters:** Systems like ChatGPT have ratcheted awareness of AI upward in most developed economies in a significant, irreversible way (much like how AlphaGo in 2016 led to increased awareness of AI in China). As a consequence there are now tons of policymakers looking around for ideas to latch onto - I expect we'll see more recommendations for sovereign AI capabilities in the future. (There's tons of other interesting stuff in the report, but this particular rec jumped out at me).  
**Read more** : [A New National Purpose: Innovation Can Power the Future of Britain (Tony Blair Institute for Global Change)](https://institute.global/policy/new-national-purpose-innovation-can-power-future-britain).

####################################################

**Facebook half-releases some very good language models:**  
_…And they end up on BitTorrent… The proliferation will continue until AI policy goes through vast changes..._  
Facebook has built and partially released LLaMa, a set of language models ranging from 7B to 65B parameters which appear to be on par with famously good models like Chinchilla (70B) and PaLM-540B. After circulating the weights to seemingly anyone with a .edu address, they've also ended up on BitTorrent. The key thing here is:

  1. Facebook has shown it is able to develop pretty good language models (compared to OPT, the not-very-good GPT3 replication Facebook put out a few months ago), and 

  2. That unlike Chinchilla, PaLM, or OpenAI's models, Facebook is releasing the _weights_ of these LLaMa models to people who filll out an access form. That opens up a whole bunch of cool uses (and abuses) compared to gating access to language models via APIs. 

  3. Shortly after releasing the weights the inevitable happened - LLaMa models are now floating around on BitTorrent. There’s even a [pull request on Facebook’s github](https://github.com/facebookresearch/llama/pull/73/files) suggesting they add a link to the torrent!




**What are the LLaMas and how good are they?** The LLaMa family of models are a family of language models trained on a huge amount of data - more than 1 trillion tokens (compared to hundreds of billions for LMs like GPT3). The data sources include two variants of CommonCrawl, GitHub, WikiPedia, Gutenberg and Books3, ArXiv and Stack Exchange.   
In tests on a range of zero-shot reasoning task, the largest LLaMa models perform on par (or slightly better than) 'Palm', Google's vast 540B parameter language model. They also do well on known-hard benchmarks like TriviaQA and some codegen benchmarks. They do less impresively on MMLU (Massive Multitask Language Understanding), suggesting they have a ways to go there; though after they conduct instruction finetuning they're able to increase performance more. 

**Why this matters - AI governance is hard when there are lots of models:** There's some thinking in the sprawling AI policy/governance communities that proliferation of models is bad; given the fact these models have broadly unknown capabilities, the more models are out there, the more you're rolling the dice on someone discovering a genuinely dangerous feature in a widely distributed model. Therefore, a lot of governance/policy conversations trend towards control - how can we somehow control the proliferation of models and also the computers on which these models are trained.   
By releasing Llama (~~yes it's behind an access form but I bet you $100 the weights will be floating around on a torrent service in <6 months~~ \- _haha, I wrote that at the end of Feb and the weights started floating around beginning of March_), Facebook is shortening the delay between development of frontier capabilities like those found in Palm and GPT3 and the diffusion of these capabilities into the ungovernable open internet/ecosystem.   
I'm not claiming this is necessarily bad per se - in fact, I imagine people are going to do tons of great science and experiments with LLaMa. I am however pointing out that this represents a kind of 'race to the bottom' in terms of moving from maximal control to maximal diffusion of models and these incentives are powerful - Facebook is, after all, trying to exploit an 'open access' ecological niche to distinguish itself in an ecosystem.   
Next up will likely be a fully open source language model - _stares pointedly at Stability.ai / CarperAI ([Import AI 307](https://jack-clark.net/2022/10/25/import-ai-307-copilot-lawsuit-stability-raises-101m-us-v-china-chiplomacy/)). _  
**Read more and download the research paper here** : [LLaMA: Open and Efficient Foundation Language Models (Facebook AI Research)](https://research.facebook.com/publications/llama-open-and-efficient-foundation-language-models/).

####################################################

**Amazon partners with Hugging Face to add more AI to AWS:**  
_…The Game of Clouds continues…_  
AI companies are a bit like upstart factions in George RR Martin's rambling epic 'Game of Thrones', while cloud companies play the role of hard political power (the 'Thrones'). As part of this _game of clouds_ Amazon has recently signed a strategic partnership with French AI startup Hugging Face. As part of the agreement, "Customers can now easily fine-tune and deploy state-of-the-art Hugging Face models in just a few clicks on Amazon SageMaker and Amazon Elastic Computing Cloud (EC2), taking advantage of purpose-built machine learning accelerators including AWS Trainium and AWS Inferentia," according to a blog from Hugging Face. 

**Why this matters:** I think clouds such as those operated by Google, Microsoft, and Amazon, all have a shot at being the major distribution platforms for some AI technologies, so AWS partnering with HuggingFace is worth noting. If HF models being integrated into Sagemakers drives more usage of it, expect Amazon to pursue more deals like this,

**Analogy-stretching joke:** In this warped metaphor, TSMC is the Iron Bank.  
**Read more:** [Hugging Face and AWS partner to make AI more accessible (Hugging Face blog)](https://huggingface.co/blog/aws-partnership). 

####################################################

**Tech Tales:**

**And the Moon was made of gold.**

I had a strange dream in which the Moon was made of gold. How much sooner would man have set foot there if instead of shining bone-white it was fat and yellow and of immense value? How would people have competed against one another for a prize - unimaginable wealth. And how many of them would have realized that in racing for the prize they must surely ensure only a single person gave dominion over the gold moon - for if many people worked together, the value of the moon would be diluted across all humanity and in doing so it would temporarily destroy the economy. 

Instead the moon of gold would need to be controlled. It would need to be annexed and encircled and defended from others. From time to time its benevolent dictator might slice off a fragment of it and ship it back to Earth, perhaps to bribe people, or perhaps to pay for more people to defend those that might seek to take over the moon. 

People would ask why it was so difficult to let go of the moon. Why, once it had been taken, those that had taken it felt a keen need to retain hold of it. Why people could not simply let go of the moon. These people were ignored, of course, because the annexed moon had by this time become the status quo. The moon, once at distance from us all, was now held and controlled by a kingdom of one. 

And so started the movement to destroy the moon. Better to reign freely on a broken planet than serve at the behest of a golden emperor. 

**Things that inspired this story:** Race dynamics and AGI; pyrrhic victories; wondering what we're all doing on this planet and what the spiritual purpose of our lives are; dreams; a stimulating policy conference in which I heard people bemoan seemingly inevitable progress and seemingly hopeless government capacity in the face of it - which caused me to scribble 'as if the moon was made of gold' on a notepad in front of me and then write this story while sat on public transportation.
