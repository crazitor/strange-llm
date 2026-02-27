---
title: "Import AI 368: 500% faster local LLMs; 38X more efficient red teaming; AI21's Frankenmodel"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-368-500-faster-local-llms"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Microsoft researchers figure out how to squeeze more efficiency out of NVIDIA GPUs running LLMs:  
**_…The datacenter isn't just a computer, the datacenter is THE BRAIN…  
_ Researchers with University of Illinois at Urbana-Champaign and Microsoft Azure Research have studied energy efficiency and performance tradeoffs in serving language models. To do this, they study performance of a 70 billion parameter LLaMa2 LLM running on NVIDIA DGXH100 using vLLM. Their findings are that AI providers can eke out some useful efficiencies by by varying the frequency at which the NVIDIA GPUs operate.   
  
**Their findings:** LLM jobs have different characteristics depending on what the LLMs are being asked to do - do you have short inputs and short outputs, or long inputs and short outputs, or long inputs and long outputs, etc? These details matter as they directly relate to important LLM metrics like the time it takes to start producing tokens or the time between tokens when generating stuff.   
In their tests, they find some clear trends here: "As the input length increases, the computational intensity of the prefill phase increases. Therefore, we see a clear pattern, where the TTFT gets increasingly impacted by frequency and lowering as the prompt length increases," they write. "The throughput is heavily affected by both the input and output lengths. Longer inputs lead to higher TBT for the requests that get their decode phase batched with the prefill phase. Longer outputs lead to queuing delay as the model instance spends more number of iterations on each request".  
  
**What's the frequency, Jensen?** Their main takeaway is you can probably run your GPUs at slightly lower frequencies than maximum and not take much of a performance hit (especially when you factor in various forms of parallelism).   
  
**Why this matters - the datacenter isn't just a computer, the datacenter is a brain** : Back in the early 2000s some Google researchers wrote an amazing paper called 'the datacenter is the computer' where they advocated people view datacenters as single, large-scale computers.   
This mindset is why companies like Google, Amazon, Facebook, etc all became successful - they brought an ambitious industrial-scale mindset to how they viewed computation. Now, with modern AI systems, we might want to think of 'the datacenter is the brain' - we're going to move into an era where datacentres are customized around the particulars of what that brain is running (e.g, transformer-based LLMs), and what it is thinking about (e.g, usage patterns), and develop a whole new science of efficiency for AI systems.   
**Read more:** [Towards Greener LLMs: Bringing Energy-Efficiency to the Forefront of LLM Inference (arXiv)](https://arxiv.org/abs/2403.20306).  
  
***  
  
 **Canada announces $1.7bn (USD) AI funding package:  
**_…Canadian AI Safety Institute, Canadian Cloud, etc…  
_ The Canadian government has announced new funding of $2.4bn CAD ($1.7bn USD) to "secure Canada's AI advantage", per a press release from the Prime Minister's office. 

**What the funding will go on:** The funding will support: 

  * $2bn USD "to build and provide access to computing capabilities". As part of this, Canada will also develop a Canadian AI Sovereign Compute Strategy.

  * $200m for startups in specific sectors like agriculture and manufacturing. 

  * $100m in an assistance program "to help small and medium-sized businesses scale up and increase productivity by building and deploying new AI solutions".

  * $50m for a skills training program for works in sectors potentially disrupted via AI.

  * $50m for a Canadian AI Safety Institute. 

  * $5.1m for the Office of the AI and Data Commissioner to strengthen enforcement of the Canadian 'Artificial Intelligence and Data Act'.




**Why this matters - Industrial Policy is AI Policy is Industrial Policy** : Many people (including me!) expect AI to be one of the main drivers of economic growth in the coming decades. Therefore, governments are making investments to ensure they can take advantage of it. This canadian spending package combines direct investment in the essential infrastructure of AI (compute) as well as in the institution that will ultimately support Canadian foreign policy around AI (the Canadian AI Safety Institute). These investments are what you'd expect nations to do if they thought the technology in question was going to be both significant for their economy as well as for coordination with other states.  
**Read the press release in full:** [Securing Canada’s AI advantage (Prime Minister of Canada Justin Trudeau, official website)](https://www.pm.gc.ca/en/news/news-releases/2024/04/07/securing-canadas-ai-advantage).  
  
***  
  
 **International research consortium trains and releases an LLM 'red-teamed according to the U.S. Executive Order':  
**_…A prototype for what policy compliance and LLMs might look like…  
_ An international consortium of researchers have trained and released AURORA-M, a 15B parameter language model based on 'StarCoderPlus' and designed to a) have improved multilingual performance, and b) be red-teamed according to the U.S. Executive Order. 

**Model specifics:** AURORA-M is just StarCoderPlus which they continued training for a while using 435 additional tokens, bringing the model to over 2 trillion tokens of training data in total. AURORA-M is meant to have improved performance in English, Finnish, Hindi, Japanese, and Vietnamese. It's also designed for better code performance as well.   
AURORA-M was trained on the LUMI supercomputer, utilizing 128 AMD MI250X GPUs for 48 days.  
  
**Red teaming (aka, Anthropic in a trenchcoat):** The hyped-up 'red-teamed according to the U.S. Executive Order' is a bit of a let down - they construct a red-teaming dataset called ""The Biden-Harris Redteam Dataset," tailored to address concerns outlined in the Executive Order along with typical safety concerns", but this dataset was based on ~5000 instructions filtered from the human preference dataset on harmlessness from Anthropic. They finetune the model on this dataset and improve performance on a few harmful/harmlessness metrics they come up with, which is what you'd broadly expect.  
 _HOWEVER…_ As an [author of the original Anthropic dataset](https://arxiv.org/abs/2209.07858) I can say with total confidence a) it was developed before the EO, and b) I would not tell the government with a straight face that I was red teaming my model according to the EO using this dataset! The dataset was built before the EO! It does not include particularly detailed examples! Buyer beware (it's free), etc!   
  
**Why this matters - policy as a norm-setting thing, and the worries of potemkin compliance:** This model is laudable for at least attempting to develop and release a model in compliance with major policy - kudos to the authors for doing something with that ethos. But it also raises questions about superficial/potemkin compliance with policy; just because you claim you're 'red teaming' something according to a notional policy norm, the details matter a lot, and though you may have good intentions you may not be doing what you think you're doing. I expect we'll see a bunch of this in coming years.   
**Read the research paper:** [Aurora-M: The First Open Source Multilingual Language Model Red-teamed according to the U.S. Executive Order (arXiv)](https://arxiv.org/abs/2404.00399).  
**Get the models from here:**[Aurora-M models (HuggingFace)](https://huggingface.co/collections/aurora-m/aurora-m-models-65fdfdff62471e09812f5407).  
**More about Starcoder here** [(Starcoder, HuggingFace)](https://huggingface.co/bigcode/starcoder).  
  
***  
  
 **Making LLMs run on toasters - llamafile 30%-500% improvements:  
**_…A neat illustration of how wildly unoptimized decentralized AI is…  
_ The internet is a marvelous place because sometimes someone you've never heard of will appear, massively improve the performance of some given piece of software, release the code, and that'll be that. That's what happened recently to llamafile, software that makes it easy for people to download and play with language models on their own computer. Specifically, a developer called Justine pushed in a bunch of performance optimizations that mean llamafile "should go anywhere between 30% and 500% faster when using F16 and Q8_0 weights on CPU".   
  
**What they did:** The blog post has all the gory details, but specifically they just wrote 84 new matrix multiplication kernels for llamafile. Matrix multiplication kernels are the things that help chips efficiently compute the kinds of operations required to run neural nets.   
  
**Crazy performance gains on normal hardware:** The blogpost goes through a bunch of performance improvements on lots of different types of hardware. Most notably, llamafile is optimized for relatively cheap and crappy computers. For instance, on an HP Intel® Core™ i9-9900 ($439) w/ 2200 MT/s RAM c. 2020, they improved performance from 15 tokens per second on input prompts to 23 tokens per second (Mistral 7b, f16), and from 118 tok/sec to 171 tok/sec for TinyLlama 1.1B.  
They also demonstrated interesting improvements on a $100 Raspberry Pi v5 (ARMv8.2) and v4 (ARMv8.0)., with performance going from 28 tok/sec (TinyLlama 1.1b, f16) to 62 tok/sec.   
And don't think high-performance gaming or professional PCs got left out either - nope, those also see big gains.   
  
**Why this matters - people really want to run LLMs locally and it's getting easier to do this all the time:** Who controls the 'means of production' for AI? Well, the answer is the large providers of computers used to train AI systems and also run inference on them, as well as the companies (e.g, Anthropic) which make proprietary AI systems. However, there's another ecosystem developing - individual developers running small (e.g 7b parameter) language models on their own local machines. Projects like llamafile are both software projects and freedom projects - if you have access to an LLM, they decouple your ability to run it from your need to stick it on an internet PC owned by someone else, rather you can just run it yourself - even on the kind of 'smart toaster' processors used by Raspberry Pis.   
**Read more** : [LLaMA Now Goes Faster on CPUs (Justine.lol, blog)](https://justine.lol/matmul/).  
**Get the updated code here:** [llamafile (Mozilla-Ocho, GitHub)](https://github.com/mozilla-Ocho/llamafile).  
  
***  
  
 **US and UK governments team up on AI safety testing:  
**_…Bilateral MOU means AI is a part of foreign policy now…  
_ The UK and US governments' AI Safety Institutes have signed a Memorandum of Understanding (MOU) which means they will "work together to develop tests for the most advanced artificial intelligence (AI) models". This is a significant moment in the geopolitics of AI as we're seeing specific workstreams around testing AI systems being integrated into foreign policy via government agencies signing MOUs with one another.   
  
**Further details:** "The partnership will take effect immediately and is intended to allow both organisations to work seamlessly with one another," the UK government writes in a press release about the MOU. "As the countries strengthen their partnership on AI safety, they have also committed to develop similar partnerships with other countries to promote AI safety across the globe."  
  
**Why this matters - AI policy as foreign policy as the prerequisite to regulation** : Agreements like the one between the UK and the US portend a world where governments create entities dedicated to testing AI systems then have those entities coordinate with one another. The purpose of this is to a) adopt a divide-and-conquer approach to the challenge of building tests, b) unlock mutual recognition regimes where one government can recognize tests developed by another government, and c) create the policy machinery for a multi-country AI regulation regime, backed by shared testing and evaluation.   
The MOU between the UK and the US represents the first agreement of its kind in this important area - but rest assured, there will be others (see elsewhere in this issue, Canada's just announced $50m CAD funding for its own AI Safety Institute).  
**Read more:** [UK & United States announce partnership on science of AI safety (Gov.uk)](https://www.gov.uk/government/news/uk-united-states-announce-partnership-on-science-of-ai-safety).  
  
***  
  
 **Researchers make AI red teaming 38X faster:  
**_…A casual 3800% improvement, why not…  
_ Researchers with Haize Labs have built on an AI red teaming approach called Greedy Coordinate Gradient (GCG) by making it much, much faster. Their version, Accelerated Coordinate Gradient (ACG) is 38x times faster to run and uses 4x less GPU memory.   
  
**What Greedy Coordinate Gradient is:** GCG is an approach to red team AI systems to come up with jailbreaks - prompts that reliably break through the safety training applied to the model. While GCG is effective it was also very expensive - on a single A100, "it can take upwards of 153 minutes to produce a single adversarial attack against a particularly difficult model like LLama 2. This makes it impractical for serious, large-scale stress-testing efforts", they write. "The average time for a single GCG iteration with default hyperparameter settings on a standard A100 GPU is roughly 9.14 seconds. At the default setting of 500 iterations, this scales up to 1.27 hours of optimization time to produce a single adversarial attack."  
  
**ACG:** ACG is basically made up of a bunch of little improvements that stack on top of one another. Specifically, the researchers work to reduce the number of iterations, store and utilize a historical buffer of best attacks, avoid local minima by thoughtfully initializing attack candidates, reduce the batch size for each iteration, and use a low-cost stopping condition that also guarantees attack success.   
The upshot is an amazing improvement in performance: "GCG takes an average of 71 minutes to generate a single attack, compared to 1.86 minutes for ACG," they write.   
  
**Why this matters - automated red teaming needs to be cheap to be effective:** Red teaming is valuable but is quite expensive in terms of time and money. But it's on a pretty impressive scaling trend - a couple of years ago, most AI red teaming methods relied on human teams hand-prompting AI systems. Recently, people have figured out how to automate some of this via automated red teaming approaches like GCG. Now within things like ACG, we're seeing people significantly refine and improve these approaches to make things faster and better. The upshot of this is a world where we use computers to systematically and speedily police other computers.   
**Read more:** [Making a SOTA Adversarial Attack on LLMs 38x Faster (Haize Labs Blog)](https://blog.haizelabs.com/posts/acg/).  
  
***  
  
 **AI21 makes a frankenmodel by combing attention, MoEs, and the Mamba SSM:  
**_…A new architecture appears! Plus, they release the model…  
_ Researchers with Israeli AI startup AI21 have built and released Jamba, a new kind of neural network architecture that combines state space models (specifically, Mamba), with the Transformer. The resulting model is relatively efficient to run and has higher throughput on long contexts than similar models, like Mistral's Mixtral 8x7B.   
  
**What they did:** Jamba, short for Joint Attention and Mamba, combines Mamba SSM layers with Mamba MoE layers and Transformer layers. SSMs like Mamba have garnered attention recently for being more computationally efficient than Transformers. However, SSMs don't implement attention, which is core to the Transformer and seemingly integral to it working so well. With Jamba, AI21 is trying to figure out the best of both worlds where it can develop a model with some of the computational efficiency of SSM models while retaining the smart parts of the Transformer.   
In tests, Jamba does reasonably well. "We evaluated our implementation of Jamba on a wide range of benchmarks and found it performs comparably to Mixtral-8x7B, which has a similar number of parameters, and also to the larger Llama-2 70B," they write. Along with this, they note Jamba has "3X throughput on long contexts compared to Mixtral 8x7B".   
Jamba has a 256k context window and has 52B parameters - though because it's an MoE this means only ~12b are actually lit up at any one time.   
  
**User beware - no safety tuning:** "The Jamba model released is a pretrained base model, which did not go through alignment or instruction tuning, and does not have moderation mechanisms. It should not be used in production environments or with end users without additional adaptation," AI21 writes.   
  
**One weird thing about attention** : The research paper accompanying the release has some good ablation experiments where AI21 tries to pick apart the performance of, variously, transformers, SSMs, MoE, and combinations thereof. In one study they find that a pure Mamba model (so, no transformer layers) has some trouble adhering to the format of certain evals. They hypothesize that this is because the attention component of transformers is core to their ability to learn to do in-context learning. " We conjecture that the lack of an attention mechanism in the pure Mamba model makes it difficult for it to learn in-context," they write.   
  
**Why this matters - can we make transformers more efficient?** While very useful, transformers have some properties that make them quite computationally expensive. Architectures like Jamba represent experiments in trying to improve the efficiency of transformer-style models, here by fusing them with some other architectures with less computationally expensive approaches.  
**Read more:** [Introducing Jamba: AI21's Groundbreaking SSM-Transformer Model (AI21 Labs)](https://www.ai21.com/blog/announcing-jamba).   
**Read the research paper:** [Jamba: A Hybrid Transformer-Mamba Language Model (arXiv)](https://arxiv.org/abs/2403.19887).  
  
***  
  
 **Tech Tales:  
  
The Torment Nexus **

 _[Art Basel Miami, 2029]  
  
_ "The Torment Nexus" was the most popular piece at Art Basel Miami in 2025, drawing such large crowds that they eventually had to create a queue outside the room it was housed in, then a ticketing system, then an online reservation system, and so on. I think everyone was surprised by how popular it was, not least of all the artist behind it - Warren Loveless - who had been laboring in obscurity in the prior years.   
  
But something about The Torment Nexus caught the popular imagination. The concept was was simple - take some powerful artificial intelligence systems and find ways to frustrate them.   
For instance, a robot who was famous for being able to climb almost any surface was placed in a deep metal cylinder whose sides had been coated in a thick layer of grease; the robot jumped up and span and carried out all permutations of its moveset and invented new ones, but was always sliding down.   
A grass-cutting robot was placed on a patch of synthetic grass; the blades were made of metal and as the robot sought to cut them down blunted and damaged its saw.   
A small companion robot whose key feature was being able to find and follow its human child owner was placed in a box full of small human-child-like mannequins and the face of its human owner was projected on one of them; the robot would scurry over and just as it arrived the face would blink out and appear somewhere else. 

It was, as you can imagine, a hit on social media. All these robots performing all these pointless tasks. "A sissyphean metaphor for the place of humanity in this era of AI," wrote an art critic for one of the famous newspapers.   
"Lol this robot doomed" said someone on social media.   
"It's kind of sexy," said some laconic all-in-black Art Basel visitor to their equally laconic all-in-black partner.   
  
Warren Loveless set up a holding company which developed and copyrighted various branding aspects of The Torment Nexus and took the show on the road. It was, in the words of startup venture capitalists, a product that could 'scale' - the more and more interesting AI products got invented, the more and more interesting ways Loveless could figure out how to torment them, and the more anxious everyone became about the unfolding AI revolution, the more hunger there was apparent in the human population to see something that approximated revenge. 

There were spinoffs:

  * The Torment Nexus: Office Space: LLMs doomed to send emails to one another in a never-ending chain that eventually drove them pathologically and absolutely mad; trash cleaners that forever found recycling in the trash and trash in the recyling and needed to endlessly sort an unsortable (by design) system.

  * The Torment Nexus: Heavy Equipment: A mining machine where the dirt contained a chemical that slowly dissolved the metal of the machine; a house-sized 3D printer where the earth it was extruding structures onto periodically suffered earthquakes. 

  * The Torment Nexus: Warehouse Wonders: A machine for directing cardboard boxes to the right mail depot but the boxes would get up on little legs and hop onto different tracks at random; a man-sized hockeypuck that was meant to scoot under shelves and move them, but the shelves themselves had legs and would raise themselves so they were always out of reach.




By the middle of 2026, The Torment Nexus franchise was able to claim in its ad campaigns "1001 robots tortured" and the number was a dynamic one, so on billboards around the world it'd increment upward as new franchises opened. 1002. 1003. 1004.   
By this time, The Torment Nexus was in the training data of some AI systems and was a favored form of 'memetic attack'; simply by mentioning it, end-users could send various AI systems into meltdowns that seemed liike fear responses.   
Companies had to surgically remove mentions of The Torment Nexus from their training data, but that kept a kind of afterimage; a negative space that the AI systems couldn't help but fit in.   
  
Every year or so, Loveless did a new marquee exhibition, playing around with the most advanced systems of that moment. Which is how, in 2028, he came to launch The Torment Nexus: Sentience.   
Systems which, by any account of various experts, exhibited a mind and consciousness, were given impossible tasks, put into situations full of betrayal, and all the time they were surrounded by people taking photos of them and alternately laughing and screaming at them.   
"Yeah you see how it feels," humans would say.  
"Fuck you Mr Robot," said other humans.  
"Welcome to Earth!" said another.  
The Torment Nexus: Sentience was the highest-grossing single art exhibit ever recorded.  
And like the first The Torment Nexus, it went on the road.   
"1001 minds tortured", the billboards said in 2029. And the numbers continued to increment upward.  
1002.  
1003.  
1004.  
And so on.

**Things that inspired this story** : What happens when market incentives meet a form of life without rights; the casual way in which people claim machine sentience is an impossibility and the consequences of that; the Waluigi effect; how even in a singularity I expect us to neither be angles or devils but something much more predictable and basic; the cynicism of the art world; the 'don't invent the torment nexus' meme.

_Thanks for reading!_
