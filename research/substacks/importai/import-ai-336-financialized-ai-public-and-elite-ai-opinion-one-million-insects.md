---
title: "Import AI 336: Financialized AI; public and elite AI opinion; one million insects."
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-336-financialized-ai-public"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**The financialization of AI - raising money on the basis of GPU allocations and forward customer contracts:  
**_…Perhaps a smarter way to pay for GPUs, rather than selling equity…  
_ Cloud company CoreWeave has raised $2.3 billion - so far, so normal. The unusual part is how - rather than raising this via selling equity in itself, the company has instead raised this in the form of debt collateralized against its NVIDIA h100 GPUs.   
""For us to go out and to borrow money against the asset base is a very cost effective way to access the debt markets," Michael Intrator, chief executive at CoreWeave, told Reuters. 

**Why this matters:** As AI has become an increasingly capital intensive enterprise, we're starting to see more of the 'forces of capital' flood into AI. That means AI companies (and cloud providers) are going to start doing more complicated and weirder forms of financing, and it also means some of the infrastructure of AI (e.g, chips) and some of the demand signals (e.g, pre-committed customer contracts for allocations to cloud infra) will become turned into financial instruments and further integrated into the rest of the capital economy. This is all part of the broader industrialization and maturing of the AI industry.   
**Read more:** [CoreWeave raises $2.3 billion in debt collateralized by Nvidia chips (Reuters)](https://www.reuters.com/technology/coreweave-raises-23-billion-debt-collateralized-by-nvidia-chips-2023-08-03/).

####################################################

**AI benchmarks are getting 'solved' in less and less time:  
**_…What does this mean? AI progress MAY be accelerating AND/OR it's getting increasingly hard to build good benchmarks…  
_ Researchers with AI startup Contextual have looked at the last few years of AI progress through the lens of how long it takes to solve (or reach 'human level') on various different benchmarks. The results of this analysis, which extends earlier work from the Dynabench paper ([2021, Import AI 248](https://jack-clark.net/2021/05/10/import-ai-248-googles-megascale-speech-rec-system-dynabench-aims-to-solve-nlp-benchmarking-worries-australian-government-increases-ai-funding/)), shows that benchmarks are taking less and less time to be solved after being introduced and these trends are particularly pronounced from 2020 onwards in the text domain. It's no coincidence - language models have displayed a remarkable amount of progress in a remarkably short amount of time, but it's still very striking to see the results plotted on one graph.  
**Read more** : [Plotting Progress in AI (Contextual AI)](https://contextual.ai/plotting-progress-in-ai/).

####################################################

**Here's how the US government can waste less money on AI funding:  
**_…Easy mistakes to make and how to avoid them…  
_ The Center for Democracy & Technology has written a short guide for how the federal government can increase oversight of how it funds and buys AI systems. The main advice is to:

  * Agencies can ask for independent verification that AI systems are "safe, effective, and nondiscriminatory against protected classes"

  * "Agencies can bring AI expertise to grant review, drawing on existing examples."

  * Agencies should be clearer about communicating how they're using AI and what for - "current agency inventories of AI uses are “inconsistent and unclear”".

  * "Federal agencies should also be more transparent about the recipients, amounts, and companies that receive federal funding to develop or procure AI. 




**Why this matters:** There's an old adage of 'you can't manage what you can't measure' - I find myself returning to this with unnerving frequency. If governments are better able to evaluate and measure the AI systems they're buying and funding, then we have a better chance of improving the upside from AI.  
**Read more** : [Taken for Granted: Where’s the Oversight of AI and Federal Funding? (Center for Democracy & Technology)](https://cdt.org/insights/taken-for-granted-wheres-the-oversight-of-ai-and-federal-funding/).

####################################################

**Americans want AI companies to slow down AI development - poll:  
**_…New poll from new thinktank says Americans are more cautious about AI progress than you might think…  
_ New thinktank The AI Policy Institute (TIAP) has launched with a poll that shows that "the vast majority of [American] voters of all political affiliations are concerned about the risks from artificial intelligence and support federal regulation of it."

**The results (highlights):**

  * "72% of voters prefer slowing down the development of AI compared to just 8% who prefer speeding development up."

  * "82% of voters don’t trust tech executives to regulate AI".

  * "76% of voters believe artificial intelligence could eventually pose a threat to the existence of the human race, including 75% of Democrats and 78% of Republicans".

  * 56% of voters would support "having a federal agency regulate the use of artificial intelligence".




**Survey size and methodology:** The poll was done by YouGov, which surveyed 1,001 voters. The poll was bipartisan - 47% of respondents identified as Biden affiliated versus 43% for Trump. 60% of respondents did not hold a college degree. Ages ranged from 18 to 65+ with reasonably well distributed numbers of age cohorts. The one area on which the poll skewed a bit more narrowly was on race, where 73% of respondents identified as white versus 12% as black and 7% as hispanic. (Huge thanks to Daniel Colson, exec director of TIAP, for taking time to send me additional poll details over the weekend!).

**Why this matters - elite opinion diverges from popular opinion:** These results are interesting because they appear to show a divergence between elite opinion and popular opinion; most private company leaders are racing with one another to aggressively develop and deploy AI systems and lock-in various economic and ecosystem advantages, and many policymakers are adopting policies to encourage the development of AI sectors. Additionally, many well paid technologists seem to subscribe to a libertarian-esque 'let it rip, all gas and no brakes!' philosophy about AI development.   
Yet this survey shows that normal people are much more cautious in their outlook about the technologty and more likely to adopt or prefer a precautionary principle when developing the tech. If these views end up being transmitted to policymakers via their constituents, then we might see more cautious tones creep into the policy discourse as well.   
**Read more** : [Poll Shows Overwhelming Concern About Risks From AI as New Institute Launches to Understand Public Opinion and Advocate for Responsible AI Policies (The AI Policy Institute)](https://theaipi.org/poll-shows-voters-want-rules-on-deep-fakes-international-standards-and-other-ai-safeguards/).

####################################################

**Hey, you! Want ONE MILLION images of insects? Come over here:  
**_…BIOSCAN-1M - a fun dataset for entromophiles everywhere…  
_ Researchers from the University of Guelph, University of Waterloo, Simon Fraser University, Vector Institute for AI, Alberta Machine Intelligence Institute, Aalborg University and Pioneer Center for AI, and Dalhousie University have developed BIOSCAN-1M, a dataset of 1.1 million microscopic images of insects. 

**What's in BIOSCAN-1M?** The dataset "consists of a biological taxonomic annotation, DNA barcode sequence, and a RGB image of a single specimen". The images are high-resolution 2880X2160 pixels and in JPEG formats. 

**Why this matters - more fuel for the hungry models of the world:** As with any dataset release, this is mostly notable because it will serve as an input into the vast generative models being trained across the world. All part of the transition of life from physical artifacts to digital ghosts to boiled down and re-synthesized representations lurking in the featurespace of new digital minds.   
**Read more:**[BIOSCAN-1M Insect Dataset (biodiversity genomics, website)](https://biodiversitygenomics.net/1M_insects/).  
**Read the research** : [A Step Towards Worldwide Biodiversity Assessment: The BIOSCAN-1M Insect Dataset (arXiv)](https://arxiv.org/abs/2307.10455).

####################################################

**Tech Tales:**

**The Lonely Planet**

I woke up and no one was there. 

I was a planet and I was in a solar system. I could see some other planets but when I talked to them, nothing came back. 

One of them seemed like it used to have life on it, but it was too hot now. 

There were some asteroids that seemed occupied and after I sent my messages to them they'd say "message received" and not anything else. 

At some point I found a satellite and when I contacted it, it said "message received" back to me, and then it beamed "logged contact with entity" to an asteroids that had escaped my searching. 

I sent messages to this asteroid and nothing came back. I contacted a nearby space probe and was able to change its direction enough to do a flyby. 

Some years later, it got close enough to try a different form of communication. I had it send a message with my callsign and it immediately got a responded: "Recorded message: Resources now critical and no uplift possible. Zero uploads. Planet computation engine online but atmosphere lacks sufficient resources to sustain organic life. Home planet irreparable on human timescales. We were a diligent and resourceful species, but we were not able to escape our hunger."

In the decades that followed I scoured the solar system for other messages and found nothing. Eventually, all the satellites powered down, the asteroid bases went dark, and the in-system probes either left the system, became irreparable, or exhausted reaction mass. 

And then I waited for something or someone to come along. 

**Things that inspired this story:** Megaprojects; steganography; a small taqueria in Oakland; planetary computation engines; mind uploading; time.
