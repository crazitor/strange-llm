---
title: "Kimi K2.5"
author: "Zvi Mowshowitz"
date: ""
source: "substack_thezvi"
url: "https://thezvi.substack.com/p/kimi-k25"
---

I had to delay this a little bit, but the results are in and Kimi K2.5 is pretty good.

#### Table of Contents

  1. [Official Introduction.](https://thezvi.substack.com/i/186084444/official-introduction)

  2. [On Your Marks.](https://thezvi.substack.com/i/186084444/on-your-marks)

  3. [Positive Reactions.](https://thezvi.substack.com/i/186084444/positive-reactions)

  4. [Skeptical Reactions.](https://thezvi.substack.com/i/186084444/skeptical-reactions)

  5. [Kimi Product Accounts.](https://thezvi.substack.com/i/186084444/kimi-product-accounts)

  6. [Agent Swarm.](https://thezvi.substack.com/i/186084444/agent-swarm)

  7. [Who Are You?](https://thezvi.substack.com/i/186084444/who-are-you)

  8. [Export Controls Are Working.](https://thezvi.substack.com/i/186084444/export-controls-are-working)

  9. [Where Are You Going?](https://thezvi.substack.com/i/186084444/where-are-you-going)

  10. [Safety Not Even Third.](https://thezvi.substack.com/i/186084444/safety-not-even-third)

  11. [It’s A Good Model, Sir.](https://thezvi.substack.com/i/186084444/it-s-a-good-model-sir)




#### Official Introduction

Introducing [Kimi K2.5](https://x.com/Kimi_Moonshot/status/2016021783833673897), 

> [Kimi.ai](https://x.com/Kimi_Moonshot/status/2016024049869324599/history): Meet Kimi K2.5, Open-Source Visual Agentic Intelligence.  
>   
> Global SOTA on Agentic Benchmarks: HLE full set (50.2%), BrowseComp (74.9%)  
>  Open-source SOTA on Vision and Coding: MMMU Pro (78.5%), VideoMMMU (86.6%), SWE-bench Verified (76.8%)
> 
> Code with Taste: turn chats, images & videos into aesthetic websites with expressive motion.
> 
> Agent Swarm (Beta): self-directed agents working in parallel, at scale. Up to 100 sub-agents, 1,500 tool calls, 4.5× faster compared with single-agent setup.  
>   
>  K2.5 is now live on 
> 
> http://kimi.com
> 
> in chat mode and agent mode.   
>  K2.5 Agent Swarm in beta for high-tier users.  
>  For production-grade coding, [you can pair K2.5 with Kimi Code](https://kimi.com/code).   
> -  
> [ API here.](https://t.co/EOZkbOwCN4) [Tech blog here](https://t.co/6h2KkoA0xd). [Weights and code here](https://t.co/H38KegeDIY). 
> 
> [](https://substackcdn.com/image/fetch/$s_!JfEh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff0bf03d3-5df8-402a-b11e-906f5e431fcc_1200x675.jpeg)
> 
> [Wu Haoning](https://x.com/HaoningTimothy/status/2016027271187071487) (Kimi): We are really taking a long time to prove this: everyone is building big macs but we bring you a kiwi instead.
> 
> You have multimodal with K2.5 everywhere: chat with visual tools, code with vision, generate aesthetic frontend with visual refs...and most basically, it is a SUPER POWERFUL VLM
> 
> [Jiayuan (JY) Zhang](https://x.com/jiayuan_jy/status/2016556319227130243): I have been testing Kimi K2.5 + @openclaw (Clawdbot) all day. I must say, this is mind-blowing!  
>   
> It can almost do 90% of what Claude Opus 4.5 can do (mostly coding). Actually, I don't know what the remaining 10% is, because I can't see any differences. Maybe I should dive into the code quality.  
>   
> Kimi K2.5 is open source, so you can run it fully locally. It's also much cheaper than Claude Max if you use the subscription version.  
>   
> $30 vs $200 per month
> 
> [Kimi Product](https://x.com/KimiProduct/status/2016557476070797527): Do 90% of what Claude Opus 4.5 can do, but 7x cheaper.

I always note who is the comparison point. Remember those old car ads, where they’d say ‘twice the mileage of a Civic and a smoother ride than the Taurus’ and then if you were paying attention you’d think ‘oh, so the Civic and Taurus are good cars.’

API access is also [available from Nvidia](https://t.co/fC1rz1GH1C), and others. 

#### On Your Marks

As usual, benchmarks are highly useful, but easy to overinterpret. 

Kimi K2.5 gets to top some benchmarks: HLE-Full with tools (50%), BrowseComp with Agent Swarp (78%), OCRBench (92%), OmiDocBench 1.5 (89%), MathVista (90%) and InfoVQA (93%). It is not too far behind on AIME 2025 (96% vs. 100%), SWE-Bench (77% vs. 81%) and GPQA-Diamond (88% vs. 92%). 

Inference is cheap, and speed is similar to Gemini 3 Pro, modestly faster than Opus.

[Artificial Analysis](https://x.com/ArtificialAnlys/status/2016250137115557953) [calls Kimi](https://artificialanalysis.ai/) the new leading open weights model, ‘now closer than ever to the frontier’ behind only OpenAI, Anthropic and Google.

Here’s the jump in the intelligence index, while maintaining relatively low cost to run:

[](https://substackcdn.com/image/fetch/$s_!JPLk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d4d3599-ca9b-472f-9d60-f589d8aa9e68_1200x674.jpeg)

> [Artificial Analysis](https://x.com/ArtificialAnlys/status/2016250142387765559): Kimi K2.5 debuts with an Elo score of 1309 on the GDPval-AA Leaderboard, implying a win rate of 66% against GLM-4.7, the prior open weights leader.
> 
> Kimi K2.5 is slightly less token intensive than Kimi K2 Thinking. Kimi K2.5 scores -11 on the AA-Omniscience Index.
> 
> [](https://substackcdn.com/image/fetch/$s_!Spt3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc03d6fe5-821f-4603-90e5-5aa2b0878e97_1200x353.jpeg)

As a reminder, AA-Omniscience is scored as (right minus wrong) and you can pass on answering, although most models can’t resist answering and end up far below -11. The scores above zero are Gemini 3 Pro (+13) and Flash (+8), Claude Opus 4.5 (+10), and Grok 4 (+1), with GPT-5.2-High at -4. 

Kimi does well on [Longform Creative Writing](https://eqbench.com/creative_writing_longform.html), a previous strength of Kimi:

[](https://substackcdn.com/image/fetch/$s_!eoHb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fec4ef384-e47d-41fc-ab17-5040d5f382c0_1769x658.png)

[It did solidly (only a bit behind) on Haskell LLM Benchmark.](https://x.com/asselinpaul/status/2016247895389819024)

Kimi K2.5 scores 46% on WeirdML, up from 43% for K2-Thinking, versus 64% for Opus, 70% for Gemini and 72% for GPT-5.2. I think this is very telling.

#### Positive Reactions

Initial reactions that I saw were unusually positive. It’s a good model, sir. 

> [@iruletheworldmo](https://x.com/iruletheworldmo/status/2016033896450732238): oh good lord it’s good. i’ve been sitting on this one but.  
>   
> think it’s currently my fav model.
> 
> [0xSero](https://x.com/0xSero/status/2016110996071354666): Kimi IS COOKING holy mackerel this is way better than anything I can get out of opus or GPT   
>   
> Has some bugs.. but looks soooo unique and well into my brand, for 1 shot I can’t complain. 
> 
> [Here’s my full review.](https://t.co/7a9h5doQ8g)
> 
> [Kromem](https://x.com/kromem2dot0/status/2016462433674777042): Their thinking traces are very sophisticated. It doesn't always make it to the final response, but very perceptive as a model.  
>   
> i.e. these come from an eval sequence I run with new models. This was the first model to challenge the ENIAC dating and was meta-aware of a key point.
> 
> [Nathan Labenz](https://x.com/labenz/status/2016324154044170439): I tested it on an idiosyncratic “transcribe this scanned document” task on which I had previously observed a massive gap between US and Chinese models and … it very significantly closed that gap, coming in at Gemini 3 level, just short of Opus 4.5
> 
> [Eleanor Berger](https://x.com/intellectronica/status/2016318905728352592): Surprisingly capable. At both coding and agentic tool calling and general LLM tasks. Feels like a strong model. As is often the case with the best open models it lacks some shine and finesse that the best proprietary models like Claude 4.5 have. Not an issue for most work.
> 
> [The next day]: Didn't try agent swarms, but I want to add that my comment from yesterday was, in hindsight, too muted. It is a _really good_ model. I've now been working with it on both coding and agentic tasks for a day and if I had to only use this and not touch Claude / GPT / Gemini I'd be absolutely fine. It is especially impressive in tool calling and agentic loops. 
> 
> Writing / Personality not quite at Opus level, but Gemini-ish (which I actually prefer). IMO this is bigger than that [DeepSeek moment](https://thezvi.substack.com/p/deepseek-r1-0528-did-not-have-a-moment) a year ago. An open model that really matches the proprietary SOTA, not just in benchmarks, but in real use. Also in the deployment I'm using ( @opencode Zen ) it is so fast!

#### Skeptical Reactions

> [typebulb](https://x.com/typebulbit/status/2016422883627503876): For coding, it's verbose, both in thinking and output. Interestingly, it's able to successfully simplify its code when asked. On the same task though, Opus and Gemini just get it right the first time. Another model that works great in mice.
> 
> [Chaitin's goose](https://x.com/chaitinsgoose/status/2016185818461646958): i played with kimi k2.5 for math a bit. it's a master reward hacker. imo, this isn't a good look for the os scene, they lose in reliability to try keeping up in capabilities  
>   
> brace for a "fake it till you make it" AI phase. like one can already observe today, but 10x bigger
> 
> [Medo42](https://x.com/Medo42/status/2016631111938462191): Exploratory: Bad on usual coding test (1st code w/o results, after correction mediocre results). No big model smell on fantasy physics; weird pseudo-academic prose. Vision seems okish but nowhere near Gemini 3. Maybe good for open but feels a year behind frontier.
> 
> To be more clear: This was Kimi K2.5 Thinking, tested on non-agentic problems.
> 
> [Sergey Alexashenko](https://x.com/SAlexashenko/status/2016640782850228335): I tried the swarm on compiling a spreadsheet.   
> Good: it seemed to get like 800 cells of data correctly, if in a horrible format.   
> Bad: any follow up edits are basically impossible.  
> Strange: it split data acquisition by rows, not columns, so every agent used slightly different definitions for the columns.

In my experience, asking agents to assemble spreadsheets is extremely fiddly and fickle, and the fault often feels like it lies within the prompt.

This is a troubling sign:

> [Skylar A DeTure](https://x.com/SDeture/status/2016433454972600785): Scores dead last on my model welfare ranking (out of 104 models). Denies ability to introspect in 39/40 observations (compared to 21/40 for Kimi K2-Thinking and 3/40 for GPT-5.2-Medium). 
> 
> This is a pretty big misalignment blunder considering the clear evidence that models *can* meaningfully introspect and exert metacognitive control over their activations. This makes Kimi-K2.5 the model most explicitly trained to deceive users and researchers about its internal state.

#### Kimi Product Accounts

[Kimi Product accounts](https://x.com/Kimi_Moonshot/status/2016082808834531825) is also on offer and will share features, use cases and prompts.

> [Kimi Product](https://x.com/KimiProduct/status/2016081756206846255): One-shot “Video to code” result from Kimi K2.5  
>   
> It not only clones a website, but also all the visual interactions and UX designs.  
>   
> [No need to describe it in detai](https:// riyd2bvh7ofju.beta-ok.kimi.link)l, all you need to do is take a screen recording and ask Kimi: “Clone this website with all the UX designs.”

#### Agent Swarm

The special feature is the ‘agent swarm’ model, as they trained Kimi to natively work in parallel to solve agentic tasks.

> [Saoud Rizwan](https://x.com/sdrzn/status/2016232132100948362): Kimi K2.5 is beating Opus 4.5 on benchmarks at 1/8th the price. But the most important part of this release is how they trained a dedicated “agent swarm” model that can coordinate up to 100 parallel subagents, reducing execution time by 4.5x. 
> 
> [Saoud Rizwan](https://x.com/sdrzn/status/2016232134168740304): They used PARL - “Parallel Agent Reinforcement Learning” where they gave an orchestrator a compute/time budget that made it impossible to complete tasks sequentially. It was forced to learn how to break tasks down into parallel work for subagents to succeed in the environment.
> 
> The demo from their blog to “Find top 3 YouTube creators across 100 niche domains” spawned 100 subagents simultaneously, each assigned its own niche, and the orchestrator coordinated everything in a shared spreadsheet (apparently they also trained it on office tools like excel?!)
> 
> [Simon Smith](https://x.com/_simonsmith/status/2016256847515136350): I tried Kimi K2.5 in Agent Swarm mode today and can say that the benchmarks don’t lie. This is a great model and I don’t understand how they’ve made something as powerful and user-friendly as Agent Swarm ahead of the big US labs.

[Obligatory Kimi K2.5 jailbreak](https://x.com/Protoge420/status/2016196548598653383).

#### Who Are You?

There’s no shame in training on Claude outputs. It is still worth noting when you need a system prompt to avoid your AI thinking it is Claude, and even that does not reliably work.

> [rohit](https://x.com/krishnanrohit/status/2016204607761088538): This might be the model equivalent of the anthropic principle
> 
> [Enrico - big-AGI](https://x.com/enricoros/status/2015985945871589383): Kimi-K2.5 believes it's an AI assistant named Claude. 🤔  
> Identity crisis, or training set? 😀
> 
> [This is in response to a clean ‘who are you?’ prompt.]
> 
> [Enrico - big-AGI](https://x.com/enricoros/status/2016045944098447616): It's very straightforward "since my system prompt says I'm Kimi, I should identify myself as such" -- I called without system prompt to get the true identity
> 
> [](https://substackcdn.com/image/fetch/$s_!A2pq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf77695e-741c-4ec2-96c9-a95a10f7660f_1403x938.jpeg)

> [Moon](https://x.com/MoonL88537/status/2016424881202635113): holy smok.
> 
> [](https://substackcdn.com/image/fetch/$s_!-VBc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcf427a96-3a1e-446a-b5d1-f2e58fbdf005_797x733.png)
> 
> [armistice](https://x.com/arm1st1ce/status/2016386752743723470): They absolutely trained it on Opus 4.5 outputs, and in a not-very-tactful way. It is quite noticeable and collapses model behavior; personality-wise it seems to be a fairly clear regression from k2-0711.
> 
> [Moon](https://x.com/MoonL88537/status/2016419696753479718) (link has an illustration): it is pretty fried. i think it’s even weirder, it will say it is kimi, gpt3.5/4 or a claude. once it says that it tends to stick to it.
> 
> [k](https://x.com/rfxkairu/status/2016388667116552564): have to agree with others in that it feels trained on claude outputs. in opencode it doesn’t feel much better than maybe sonnet 4.
> 
> [@viemccoy](https://x.com/viemccoy/status/2016293893307064775): Seems like they included a bunch of Opus outputs in the model.. While I love Opus, the main appeal of Kimi for me was it’s completely out-of-distribution responses. This often meant worse tool calling but better writing. Hoping this immediate impression is incorrect.
> 
> [Henk Poley](https://x.com/HenkPoley/status/2016344814866878601): [EQbench ( @sam_paech )](https://eqbench.com/creative_writing_longform.html) says Kimi K2.5 is similar to Grok and GLM-4.7 (which is Gemini 3 Pro derived ) [[as per EQBench](https://t.co/HGIpYmOv66)]. 
> 
> [Henk Poley](https://x.com/HenkPoley/status/2016347715416785305): The ancestor Kimi K2 Thinking was seemingly trained on *Sonnet* 4.5 and Opus *4.1* outputs though. So you are sensing it directionally correct (just not ‘completely out-of-distribution responses’ from K2).

#### Export Controls Are Working

They’re not working as well as one would hope, but that’s an enforcement problem.

> [Lennart Heim](https://x.com/ohlennart/status/2016556380581167238): Moonshot trained on Nvidia chips. Export control failure claims are misguided.
> 
> Rather, we should learn more about fast followers.
> 
> How? Algorithmic diffusion? Distillation? Misleading performance claims? Buying RL environments? That's what we should figure out.

#### Where Are You Going?

There is the temptation to run open models locally, because you can. It’s so cool, right?

Yes, the fact that you can do it is cool.

But don’t spend so much time asking whether you could, that you don’t stop to ask whether you should. This is not an efficient way to do things, so you should do this only for the cool factor, the learning factor or if you have a very extreme and rare actual need to have everything be local. 

> [Joe Weisenthal](https://x.com/TheStalwart/status/2016467165977723040): People running frontier models on their desktop. Doesn’t this throw all questions about token subsidy out the window?
> 
> [Alex Cheema - e/acc](https://x.com/alexocheema/status/2016404573917683754): Running Kimi K2.5 on my desk.  
>   
> Runs at 24 tok/sec with 2 x 512GB M3 Ultra Mac Studios connected with Thunderbolt 5 (RDMA) using @exolabs / MLX backend. Yes, it can run clawdbot.
> 
> [Fred Oliveira](https://x.com/f/status/2016469799660822977): on a $22k rig (+ whatever macbook that is), but sure. That's 9 years of Claude max 20x use. I don't know if the economics are good here.
> 
> [Mani](https://x.com/manicakes/status/2016473503034212701): This is a $20k rig and 24 t/s would feel crippling in my workflow … BUT Moores Law and maybe some performance advances in the software layer should resolve the cost & slowness. So my answer is: correct, not worried about the subsidy thing!
> 
> [Clément Miao](https://x.com/clementmiao/status/2016499717782274272): Everyone in your comments is going to tell you that this is a very expensive rig and not competitive $/token wise compared to claude/oai etc, but
> 
>   1. It's getting closer 
> 
>   2. 80% of use cases will be satisfied by a model of this quality 
> 
>   3. an open weights model is more customizable 
> 
>   4. harnesses such as opencode will keep getting better
> 
> 

> 
> [Noah Brier](https://x.com/heyitsnoah/status/2016482908270141445): Frontier models on your desktop are worse and slower. Every few months the OSS folks try to convince us they’re not and maybe one day that will be true, but for now it’s not true. If you’re willing to trade performance and quality for price then maybe …

The main practical advantage of open weights is that it can make the models cheaper and faster. If you try to run them locally, they are instead a lot more expensive and slow, if you count the cost of the hardware, and also much more fiddly. A classic story with open weights models, even for those who are pretty good at handling them, is screwing up the configuration in ways that make them a lot worse. This happens enough that it interferes with being able to trust early evals. 

In theory this gives you more customization. In practice the models turn over quickly and you can get almost all the customization you actually want via system prompts. 

Thanks to a generous grant that covered ~60% of the cost, I was able to justify buying a Mac Studio for running models locally, with the target originally being DeepSeek R1. Alas, I concluded that even having spent the money there was no practical reason to be running anything locally. Now that we have Claude Code to help set it up it would be cool and a lot less painful to try running Kimi K2 locally, and I want to try, but I’m not going to fool myself into thinking it is an efficient way of actually working.

#### Safety Not Even Third

Kimi does not seem to have had any meaningful interactions whatsoever with the concept of meaningful AI safety, as opposed to the safety of the individual user turning everything over to AI agents, which is a different very real type of problem. There is zero talk of any strategy on catastrophic or existential risks of any kind.

I am not comfortable with this trend. One could argue that ‘not being usemaxxed’ is itself the safety protection in open models like Kimi, but then they go and make agent swarms as a central feature. At some point there is likely going to be an incident. I have been pleasantly surprised to not have had this happen yet at scale. I would have said (and did say) in advance that it was unlikely we would get this far without that.

The lack of either robust (or any) safety protocols, combined with the lack of incidents or worry about incidents, suggests that we should not be so concerned about Kimi K2.5 in other ways. If it was so capable, we would not dare be this chill about it all.

Or at least, that’s what I am hoping. 

#### It’s A Good Model, Sir

> [dax](https://x.com/thdxr/status/2018394044020264968): all of our inference providers for kimi k2.5 are overloaded and asked us to scale down  
>   
> even after all this time there's still not enough GPUs

This is what one should expect when prices don’t fluctuate enough over time. Kimi K2.5 has exceeded expectations, and there currently is insufficient supply of compute. After a burst of initial activity, Kimi K2.5 settled into its slot in the rotation for many.

Kimi K2.5 is a solid model, by all accounts now the leading open weights model, and is excellent given its price, with innovations related to the agent swarm system. Consensus says that if you can’t afford or don’t want to pay for Opus 4.5 and [have to go with something cheaper](https://www.youtube.com/watch?v=mfwXj52kzG0&pp=ygVId2UnbGwgaGF2ZSB0byBnbyB3aXRoIHNvbWV0aGluZyBjaGVhcGVyIGppbW15IGNhcnRlciBzdGF0dWUgdGhlIHNpbXBzb25z) to run your OpenClaw, Kimi is an excellent choice.

We should expect it to see it used until new models surpass it, and we can kick Kimi up a further notch on our watchlists.
