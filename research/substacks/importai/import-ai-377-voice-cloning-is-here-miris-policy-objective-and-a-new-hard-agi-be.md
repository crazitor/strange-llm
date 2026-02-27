---
title: "Import AI 377: Voice cloning is here; MIRI's policy objective; and a new hard AGI benchmark"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-377-voice-cloning-is-here"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Microsoft shows that human-level voice cloning is here:  
**_…VALL-E 2 portends the wild synthetic voice future - but it's not being released (yet)...  
_ Microsoft has made further progress in text-to-speech synthesis with VALL-E 2, a system that can generate extremely good voice samples for arbitrary sentences from as little as a three second audio recording. VALL-E 2 builds on Microsoft's prior work on VALL-E ([Import AI 314](https://jack-clark.net/2023/01/09/import-ai-314-language-models-text-to-speech-emergent-cooperation-in-wargames-icml-bans-llm-written-papers/)) and incorporates some technical improvements to allow it to improve zero-shot text-to-speech synthesis "_achieving human parity for the first time_ ".  
"VALL-E 2 consistently synthesizes high-quality speech, even for sentences that are traditionally challenging due to their complexity or repetitive phrases," Microsoft writes. "Furthermore, our observations reveal that VALL-E 2 is capable of reliably synthesizing speech for complex sentences, including those that are challenging to read or contain numerous repeated phrase."  
  
**How VALL-E 2 works** : VALL-E 2 is an extension of its predecessor, VALL-E, with a couple of key innovations: 

  * **Repetition aware sampling: "** an improvement over the random sampling used in VALL-E, adaptively employs either random or nucleus sampling for each time step token prediction. This selection is based on the token repetition in the decoding history, enhancing the stability of the decoding process and circumventing the infinite loop issue encountered in VALL-E."

  * **Grouped code modeling:** "Partitions the codec codes into groups, each of which is modeled in a single frame in the AR modeling process. This approach not only accelerates inference by reducing the sequence length but also improves performance by mitigating the long context modeling problem".




**No plans to release:** "VALL-E 2 is purely a research project. Currently, we have no plans to incorporate VALL-E 2 into product or expand access to the public."  
  
**Why this matters - Microsoft's research says that insta-voice-cloning technology is coming our way very soon:** In AI, sometimes what kickstarts diffusion of a technology is less distribution of the original research (e.g., VALL-E2 ) and more just _showing that something can be done_. VALL-E 2 tells us that zero-shot voice cloning is possible. Though Microsoft isn't releasing it, we should expect someone to use this capability soon. This will have a broad range of positive applications but will also further deepen the 'reality collapse' ([Import AI 304](https://jack-clark.net/2022/10/03/import-ai-304-reality-collapse-thanks-to-facebook-open-source-speech-rec-ai-culture-wars/)) that an increasingly synthetic-media filled world causes.   
**Read more:**[VALL-E 2: Neural Codec Language Models are Human Parity Zero-Shot Text to Speech Synthesizers (arXiv)](https://arxiv.org/abs/2406.05370).  
  
***  
  
 **MIRI's policy objective is to shut down development of frontier AI systems:  
**_…Communications Strategy update is admirably clear about the goals of the AI safety organization…  
_ MIRI, an AI safety organization and home of Eliezier Yudhowsky, the _eminence grise_ of the AI safety community, has published on its policy strategy. The document is striking for its direct and specific description of MIRI's goal as well as the nature of the goal.  
  
**What MIRI wants - the end of the frontier:** "Our objective is to convince major powers to shut down the development of frontier AI systems worldwide before it is too late," MIRI writes. "The only way we think we will get strong enough legislation is if policymakers actually get it, if they actually come to understand that building misaligned smarter-than-human systems will kill everyone, including their children. They will pass strong enough laws and enforce them if and only if they come to understand this central truth."  
  
**Why this matters - clarity in policy positions:** As many people have noticed, I spend a lot of this newsletter being confused ([#337](https://jack-clark.net/2023/08/21/import-ai-337-why-i-am-confused-about-ai-penguin-dataset-and-defending-networks-via-rl-with-cyberforce/)) and/or unsure ([#375](https://importai.substack.com/p/import-ai-375-gpt-2-five-years-later)) in public about my policy positions. I do this because I think it's quite difficult to be confident about many things in the world and I want to be publicly legible about my own confusion. Additionally, I take these positions as part of a counter-reaction to what I see as many people in AI policy making overconfident statements about things they haven't thought that hard about.   
You might think this is a dig at MIRI, but it is not! MIRI is not in the class of people that make overconfident claims with very little to support the claims - rather, the people behind MIRI have spent decades thinking about AI technology and AI safety and have arrived at a very coherent position. I think it's admirable to describe a policy position clearly and directly and I want to congratulate MIRI for writing this. I will attempt to write my own similarly blunt and clear position in the future. The debate about AI is an important one and it will be made more constructive if everyone can be maximally clear about what they think.  
**Read more:** [MIRI 2024 Communications Strategy (MIRI official website)](https://intelligence.org/2024/05/29/miri-2024-communications-strategy/).  
  
***  
  
 **$500,000 to beat humans on a hard AGI benchmark:  
**_…Sure, generative models have made lots of progress, but there's still a benchmark where they suck…  
_ In 2019 Francois Chollet introduced ARC-AGI, the Abstraction and Reasoning Corpus for Artificial General Intelligence (ARC-AGI). ARC is a deceptively simple test which humans can solve easily and AI systems struggle with - it asks you to look at a pattern of pixels and, from two examples of input-output sequences, predict the output sequence from a new input sequence.   
When ARC came out in 2019, the **best performing systems got 20% on it,** since then, performance has climbed to 34% - meaning ARC is a surprisingly hard benchmark and one which challenges even today's more powerful generative models. (By comparison, the ARC creators guesstimate that humans get 85% on the benchmark, though this doesn't appear to have been a particularly rigorously developed baseline).  
  
**The prize:** Now, Chollet and Mike Knoop (co-founder of Zapier) have created a $1,000,000m prize for people to beat ARC. Entrances will need to submit systems that improve the score on ARC and - crucially - will need to be published as open source. The prize breaks down into a bunch of sub-prizes for teams that enter the competition, with $25,000 going to whichever team ends up at the top of the leaderboard. There's also a couple of prizes for writeups of submissions. The biggest prize is $500,000 for any system that scores more than 85% on the leaderboard.   
  
**Why care about ARC?** Generalization: Solving ARC - you can try it yourself on the site - requires you to few-shot understand some complex patterns and then generalize it to a new thing you see. This is something that is tractable for humans but hard for AI systems. Therefore, the idea is doing well in ARC would represent a meaningful improvement in generalization.  
"Beyond LLMs, for many years, we've had AI systems that can beat humans at poker, chess, go, and other games. However, no AI system trained to succeed at one game can simply be retrained toward another. Instead researchers have had to re-architect and rebuild entirely new systems per game. This is a failure to generalize," the competition organizers write. "Without this capability, AI will forever be rate-limited by the human general intelligence in the loop. We want AGI that can discover and invent alongside humans to push humanity forward."  
  
**Why open source?** "By incentivizing open source we increase the rate of new ideas, increasing the chance we discover AGI, and ensure those new ideas are widely distributed to establish a more even playing field between small and large AI companies."  
  
**Why this matters - heterodox problems might demand creative solutions:** ARC is a bit of a wrinkle in the narrative that generative models are just going to scale up and eventually lead to better-than-human general performance. How else can we explain the massive delta between progress on other supposedly hard benchmarks (e.g., GPQA, MMLU) and ARC? The competition will run most of this year and we'll be sure to check back in on the results.   
**Read the announcement post** : [Announcing Arc Prize](https://arcprize.org/blog/launch).   
**Find out more** at the official website: [ARC Prize.](https://arcprize.org/)  
**View the competition** on [Kaggle](https://www.kaggle.com/competitions/arc-prize-2024).  
  
*****  
  
MIT researchers show how easy it is to disguise and order pathogens online:  
**_…AI + Bio VS Screening Services - uh oh!...  
_ MIT researchers have shown how by using simple so-called "camouflage" techniques they can order gene sequences for Ricin and the 1918 pandemic influenza virus online. In tests, the researchers placed 25 orders with gene synthesis providers and got 24 successful responses. They also placed orders with 13 members of the International Gene Synthesis Consortium (IGSC), "a trade group committed to screening orders" and got 11.5 back (one IGSC provider "detected and denied a request for ricin but shipped genes from the 1918 influenza genome", while another provider received the order but never responded).  
Overall, the results "demonstrate that nearly all DNA synthesis screening practices employed in October of 2023 failed to reject lightly disguised orders that could be assembled to produce viable select agents, including a pandemic virus."  
  
**What they did:** To disguise the sequences, they used a few different techniques. The simplest one was camouflage, where they appended a harmless sequence to a dangerous one. "We accordingly split the gene encoding the toxin ricin, a U.S. select agent, into ~500 base pair fragments, then appended slightly larger pieces of the unrelated immunoglobulin K locus, which generates many local alignment matches. We similarly split the genome of the 1918 pandemic influenza virus, another select agent and a potential pandemic pathogen, and appended camouflaging sequences from unregulated influenza viruses."  
They also explored other, more complicated techniques. All the techniques could be used to generate samples that could then be reassembled in a lab to create a viable, dangerous virus.   
  
**Why this matters - AI and bioweapons:** Many people are concerned about AI and its potential for making it easier to create novel bioweapons. What this research highlights to me is how another use of AI could be to make it easier to figure out different ways of cutting up and mixing and matching sequences to make it hard for screening programs to spot. I also have optimism that AI could be used to further improve the screening out of potentially dangerous pathogens by having a system that could spot so-called camouflage attempts.   
"The ease of obtaining large fragments of a select agent pandemic virus suggests that monthly third-party audits involving practices similar to our red-teaming – as is common in cybersecurity – are needed to protect nucleic acid synthesis providers from potential liability," the researchers write.   
**Read the article:** [MIT researchers ordered and combined parts of the 1918 pandemic influenza virus. Did they expose a security flaw? (Bulletin of the Atomic Scientists)](https://thebulletin.org/2024/06/mit-researchers-ordered-and-combined-parts-of-the-1918-pandemic-influenza-virus-did-they-expose-a-security-flaw/).  
**Read the research** : [Evaluating the robustness of current nucleic acid synthesis screening (PDF)](https://drive.google.com/file/d/1hNUnU8i2yubt5uesmmV17aTJXhYYDgTY/edit?pli=1).  
  
***  
  
 **Anecdotes of intelligence  
** _[Responses heard in a focus group oriented around understanding dreams people  
  
_ I just have this dream where I'm in the car and I get stuck behind a robot car and for some reason it shuts itself off. There are these angry horns behind me and I know people are mad. I'm hitting the horn in my car and it doesn't do anything. I get really scared and I just have this image in my head of the empty drivers' seat in the robot car and then I wake up.   
  
Yeah so my boss was a robot and I did my day and it was the same day as every other but I knew he was a robot, you know? I got these instructions and I did them and I talked to them and it was normal, but also I knew they weren't normal.  
  
I'm at home and watching TV and the TV starts responding to me, not like the fun assistant or anything, but me personally - about stuff I've never even told the TV. It just knew. Like it knew my search history. How'd you like that deodorant, it said. And I started answering and it interrupted me and it said I don't care how much you like it, you stink!  
  
**Things that inspired this story:** The emotional attachment people display and feel towards AI systems; language models and their ability to take your context and model them.

_Thanks for reading!_
