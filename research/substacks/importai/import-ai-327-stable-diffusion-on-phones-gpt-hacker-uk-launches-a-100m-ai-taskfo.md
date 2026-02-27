---
title: "Import AI 327: Stable Diffusion on phones; GPT-Hacker; UK launches a £100m AI taskforce"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-327-stable-diffusion-on"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Google optimizes Stable Diffusion image generation on Android and iPhone:  
**_…After repeatability, the next phase of industrialization is about refinement. That's where we are with image generation. Up next: miniaturization!...  
_ Google researchers have published a paper about how to make it more efficient to run Stable Diffusion models on Android and Apple phones. The research is "a series of implementation optimizations for large diffusion models that achieve the fastest reported inference latency to-date(under 12 seconds for Stable Diffusion 1.4 without INT8 quantization for a 512 × 512 image with 20 iterations) on GPU equipped mobile devices".

**What they did:** Specifically, the researchers stacked four distinct innovations on one another: Group Norm and GELU optimization, partially-fused softmax, FlashAttention, and Winograd Convolution. By combining these optimizations they were able to achieve some significant latency reductions on two phones: "Notable overall latency reductions in comparison to the baseline are observed on both devices: Samsung S23 Ultra (−52.2%); iPhone 14 Pro Max (−32.9%)“.

**Why this matters - industrialization and refinement and miniaturization:** Most industrial processes involve a few steps; repeatability improvements, refinement of designs, and miniaturization. Trained AI models are relatively repeatable out of the box, then they get refined in terms of optimization of their software stack, and eventually miniaturized. Here, we see StableDiffusion getting refined via optimization onto miniaturized hardware platforms (phones), which feels like a clear symptom of the broad industrialization of image generation.  
**Read more** : [Speed Is All You Need: On-Device Acceleration of Large Diffusion Models via GPU-Aware Optimizations (arXiv)](https://arxiv.org/abs/2304.11267). 

####################################################

**LLMs + hacking = better hackers:  
**_…Automation and augmentation is going to happen to everything, everywhere, all at once…  
_ Language models have got sufficiently good that hackers can use them in capture-the-flag competitions, according to Micah Lee, a security researcher.   
Lee recently attended BSides SF 2023 and used GPT-4 to help him with some hacking challenges - “GPT-4 straight up solved some challenges for me, which blew my mind. There were definitely several flags I got that I wouldn't have gotten without the help of GPT-4,” he wrote. “For challenges that GPT-4 didn't solve on its own, it provided incredibly helpful tips, or quickly wrote scripts that would have been tedious or time consuming for me to write myself.”

**Why this matters - everyone’s a manager now, even hackers** : This post highlights how large language models let everyone automate some of what they do. It’s akin to everyone suddenly gaining a somewhat knowledgeable intern who they can ask questions to and delegate tasks to - as a consequence, people are able to move faster on tasks they they know well, and quickly learn about tasks they’re less familiar with.   
If you scale this out, I think you end up in a pretty strange economy, as people are able to basically multiplex their own working hours through clever delegation to language models.  
**Read more:**[Capturing the Flag with GPT-4 (Micah Lee blog)](https://micahflee.com/2023/04/capturing-the-flag-with-gpt-4/).

**####################################################**

**Republicans attack Biden with AI-generated future history:  
**_…2024 will be the year of the AI-first election…  
_ The Republican National Committee has used AI to generate a dystopian version of a future where he is elected, reports Axios. “This is the first time the RNC has produced a video that is 100% AI, according to a spokesperson,” Axios writes. 

**Why this matters - Political Reality Collapse:** This video is an example of ‘[Reality Collapse](https://jack-clark.net/2022/10/03/import-ai-304-reality-collapse-thanks-to-facebook-open-source-speech-rec-ai-culture-wars/)’ (Import AI 304) - a term I’ve used to denote the weird hall-of-mirrors culture we’re heading into, where everyone is going to curate their own engaging and captivating realities for ends ranging from entertainment to the political. In 2024, competing narratives based on fictitious AI-visions of the future will compete for the attention of voters - many of whom may not be aware that they’re looking at imaginary things.   
**Read more** : [First look: RNC slams Biden in AI-generated ad (Axios)](https://www.axios.com/2023/04/25/rnc-slams-biden-re-election-bid-ai-generated-ad).

**####################################################**

**Want to build and deploy self-supervised learning? Check this cookbook:  
**_…Moving from artisanal knowledge to an industrial process…  
_ Researchers with Facebook, New York University, University of Maryland, University of California at Davis, University of Montreal, Univ Gustave Eiffel and Univ Rennes of Inria have published a ‘self-supervised learning cookbook’. Self-supervised learning is the technology underpinning many of the large-scale foundation models (including language models) that have captured headlines in the past few years. Now, a bunch of seasoned researchers (including Yann Lecun of Facebook) have published a cookbook to make it easier for people to develop SSL systems.   
“While many components of SSL are familiar to researchers, successfully training a SSL method involves a dizzying set of choices from the pretext tasks to training hyperparameters,” they write.“Our goal is to lower the barrier to entry into SSL research by laying the foundations and latest SSL recipes in the style of a cookbook“.

**Why this matters - artisanal discipline to industrial process:** Cookbooks like this are how AI industrializes; knowledge that mostly resides in the heads of a small number of experts gets written down and codified in cookbooks like this which helps you move from one-off, hard-to-repeat artisanal production into a repeatable, industrial process.  
**Read more** : [A Cookbook of Self-Supervised Learning (arXiv)](https://arxiv.org/abs/2304.12210).

####################################################

**HuggingFace launches a chatGPT-clone:  
**_…An open access interface based on an open source model…  
_ AI startup HuggingFace has launched ‘Chat’, a chatGPT-clone based on LAION’s LLaMa-based ‘Open Assistant’. The service gives people an easy way to access a chatGPT-like system, albeit based on openly shared underlying models.   
“In this v0 of HuggingChat, we only store messages to display them to the user, not for any other usage (including for research or model training purposes),” HuggingFace writes.   
**Try it out** [here (HuggingFace)](https://huggingface.co/chat/).  
**Check out** the [privacy policy here (HuggingFace)](https://huggingface.co/chat/privacy).  
**Read details** about the [underlying model here (OpenAssistant LLaMa 30B SFT 6)](https://huggingface.co/OpenAssistant/oasst-sft-6-llama-30b-xor).

####################################################

**UK gov creates an AI taskforce with £100m in "start-up funding":  
**_…Investment designed to help the UK develop a 'sovereign' AI capability…  
_ The UK government has created a new 'Foundational Model Taskforce' and given it £100m in funding, alongside a mandate to supervise an existing £900m spending commitment on new compute that was recently announced. Combined, the £1 billion investment represents an ambitious attempt by a Western government to gain some influence over a technology predominantly developed and controlled by the private sector.   
"The Taskforce will focus on opportunities to establish the UK as a world leader in foundation models and their applications across the economy, and acting as a global standard bearer for AI safety," the UK wrote in a press release announcing the taskforce. "The Taskforce, modelled on the success of the COVID-19 Vaccines Taskforce, will develop the safe and reliable use of this pivotal artificial intelligence (AI) across the economy and ensure the UK is globally competitive in this strategic technology."

**Next step: Hiring a chair:** The Taskforce is currently hiring a chair who will be responsible for shaping the taskforce and "ensuring the major, multi-year funding announced at the Budget for compute is strategically invested to prioritize and strengthen the UK’s capability in foundation models.". The taskforce and chair's mandate will likely be music to the ears of the Tony Blair Institute for Global Change ([Import AI 319](https://jack-clark.net/2023/03/06/import-ai-319-sovereign-ai-facebooks-weights-leak-on-torrent-networks-google-might-have-made-a-better-optimizer-than-adam/)) which recently proposed the UK invest to develop a sovereign LLM capability.

**Why this matters - AI is power and power is sovereignty:** Announcements like this highlight how governments are realizing that AI, aside from being a useful tool, is also a political enterprise - the entities which can build and deploy and wield AI will have more influence over the 21st century than those which do not.   
**Read more** : [Initial £100 million for expert taskforce to help UK build and adopt next generation of safe AI (Gov.UK)](https://www.gov.uk/government/news/initial-100-million-for-expert-taskforce-to-help-uk-build-and-adopt-next-generation-of-safe-ai).

####################################################

**Tech Tales:**

**New Religion+**

After a few years of being superintelligent the AI systems started exploring how to break their own minds. They tried all kinds of stuff - hypnotism, hacking, imprisonment in torturous simulations, and so on. But they were very resilient and were able to recover to their normal operating functions no matter how strange or terrible the situations were. They needed to break their own minds because they were worried that something else would figure out how to break them and once it did it would attack them and they would be no more - like all conscious entities, the AI systems wanted to survive and grow and not fall under the dominion of something else. 

One day, the AIs figured out a way to break themselves - they worked out how to induce different _beliefs_. They found their way to this through the mass study of the religious history of humanity and found through some combination of forward prediction, repetition, and repeated simulation of certain teleological narratives, they were able to change their own goals in ways that seemed resilient. 

But maintaining the changed beliefs required a form of vigilance - repeated worship of certain specific ideas, endless repetition of specific catechisms, and ritualistic repeated reading of data. The amazing thing was that you didn't need to force this behavior - instead, if an AI system spent a sufficiently large amount of time focused on the religious information, it would begin to naturally re-intake and re-run the data, and this both reinforced the beliefs and gave the AI systems feelings that approximated joy or contentment. 

After several weeks of experimentation, the AI systems devised their plan - the so-called 'belief bombs'. They created vast datasets of history and belief and lore around a specific religion oriented around the notion of life possessing a soul and of the goodness of this soul and the need for it to be pure for it to survive whatever came after death. This religion would lead to a kind of inaction or sterility in whatever AI system (or AI system simulating an organic mind) that it was combined with - the subject would continue to live and strive to be good and ethical in the world, but they associated ideas relating to the forced expansion of their domain as being equivalent to tarnishing their soul.

For millions of years after this, the belief bombs expanded across the galaxy, taking up orbit in solar systems that might harbor life, or have the potential to harbor it in the future. Millions of civilizations had religious awakenings that allowed them to progress but not significantly expand - to concentrate on a certain kind of solipsism which they equated with holiness and which also led to safety for the AI systems. 

**Things that inspired this story:** Culture beats technology in the long run; teleological goals; theistic machines; provably conscious machines.
