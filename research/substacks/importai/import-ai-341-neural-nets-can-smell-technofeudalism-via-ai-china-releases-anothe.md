---
title: "Import AI 341: Neural nets can smell; technofeudalism via AI; China releases another solid open access model"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-341-neural-nets-can-smell"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**China releases** _**another**_**really good open access language model:  
**_…Baichuan2 shows us just how broadly distributed LLM training and deployment is getting…  
_ Chinese startup Baichuan has trained and release two open access language models. These models are interesting for two reasons, a) they're broadly disseminated and available for free, and b) they are 'language models with Chinese characteristics' - that is, they've been trained on a mixture of English and Chinese data and some of their safety hardening has been in accordance with the unique social context of China. 

**What the models are:** Baichuan 2 is "a series of large-scale multilingual language models". The models were trained on 2.6 trillion tokens of data, and come in two variants in terms of parameter size - a 7B and a 13B model, as well as two variations optimized for chatting with people. "By open-sourcing these models, we hope to enable the community to further improve the safety of large language models, facilitating more research on responsible LLMs development," the researchers write.   
The models also use a few emerging best practices, like rotary positional embededdings, SwiGLU as an activation function, and AdamW for training.

**Compute scale:** Most papers about training large models don't include too many details about the underlying infrastructure. The Baichuan 2 paper contains a few more hints that usual - it indicates that the team is working with machines typically equipped with eight A800 GPUs, and that the overall cluster involves "thousands of GPUs", with a single training run taking place on 1,024 NVIDIA A800s. 

**Why this matters - everything proliferates eventually:** Systems like Baichuan 2 would have probably been sitting on the frontier 2-3 years ago (considering the ~1000 GPU and 2trillion+ token requirement). Now, they're relatively unremarkable papers (and models!) that get published on arXiv and are only of real interest to trainspotters like your humber author. This generally illustrates the rapid pace of AI progress and how everything is on an 'escalator of diffusion' where it starts out expensive but, slowly, the escalator turns and everything gets cheaper over time.  
**Read more:**[Baichuan 2: Open Large-scale Language Models (arXiv)](https://arxiv.org/abs/2309.10305).  
**Access the models** at the [GitHub (Baichuan Intelligent Technology, GitHub)](https://github.com/baichuan-inc/Baichuan2).  
  
***

 **MADLAD-400: A new 400+ language dataset:  
**_…Plus, exquisitely detailed writeup of how to clean and audit a dataset…  
_ Researchers with Google DeepMind have built MADLAD-400, a dataset and family of models spanning 491 languages. 

**What MADLAD-400 is** : MAD-LAD 400 is a dataset comprising of more than ~400 distinct languages spread across 3 trillion tokens (5 trillion for the uncleaned and therefore noisier dataset). They gathered the dataset by training a LangID model on ~500 languages, then using that model to filter a large Common Crawl corpus, resulting in MAD-LAD 400 noisy. Once they had that dataset, they applied a bunch of quality filtering steps to filter out low-quality or erroneous content. Through this process, they ended up omitting 79 of the languages found in the dataset, reducing the size of the cleaned MADLAD-400 dataset to 419 languages or so. 

**MADLAD models:** Google also trained and released a 10.7B parameter multilingual machine translation model trained on 250 billion tokens, covering over 450 languages. 

**Why this matters:** By documenting the filtering process for the dataset and also releasing the data and some downstream models trained by it, Google hopes to further motivate "work towards language technologies that are more inclusive of the rich language diversity housed by humanity," according to the researchers.  
**Read the paper** : [MADLAD-400: A Multilingual And Document-Level Large Audited Dataset (arXiv)](https://arxiv.org/abs/2309.04662).  
**Get the models and data** : [MADLAD-400: A Multilingual And Document-Level Large Audited Dataset (GitHub)](https://github.com/google-research/google-research/tree/master/madlad_400).

  
***   
  
**How might superintelligence reconfigure the state and our broader world?  
**_…Technofeudalism or perfect authoritarianism, and so much more!...  
_ Samuel Hammond, a senior economist for the Foundation for American Innovation, thinks AI systems may lead to the dramatic reconfiguration of government in the coming years. He has laid out his thoughts in a series called "AI and Leviathan" - three essays which try to pick apart the ways AI might influence our world. 

**AI is like the printing press in more ways than one:** "AI is often compared to the printing press, but the parallels between Early Modern England and contemporary America extend beyond the technological," Hammond writes. "Our cultural and ideological schisms are intensifying; the new Puritans have run headlong into a conservative counter-reaction; and our parliamentary debates revolve around issues of censorship as the prior century’s media controls succumb to the open internet."  
Into this chaotic scenario, enter AI: "The coming [intelligence explosion](https://www.dwarkeshpatel.com/p/carl-shulman#details) puts liberal democracy on a knife edge. On one side is an AI Leviathan; a global singleton that restores order through a Chinese-style panopticon and social credit system. On the other is state collapse and political fragmentation, as our legacy institutions fail to adapt and give way to new, [AI-native organizations](https://blog.mutable.ai/p/the-ai-organization-part-i) that solve the [principal-agent problem](https://en.wikipedia.org/wiki/Principal%E2%80%93agent_problem) and unlock localized collective action at blazing speeds," he writes. 

**How governments will react to AI - when the giants wake, expect some anger** : "The issue is that society’s technological base is shifting faster than its institutional superstructure can keep up," he writes. "The moment governments realize that AI is a threat to their sovereignty, they will be tempted to clamp down in a totalitarian fashion. It’s up to liberal democracies to demonstrate institutional co-evolution as a third-way between degenerate anarchy and an AI Leviathan."

**A timeline for the future** : In the third and final essay Hammond makes some predictions about how the world might respond to increasingly smart machines. "In the default scenario, the technology shock from AI will cause slower governments to either fragment or recede to a few core competencies, pushing the provision of various public goods (including security against AI misuse) into private hands. Call this the techno-feudalist timeline," he writes. "By the early 2030s, the knowledge jobs that remain are highly bimodal. A subset of entrepreneurs are highly remunerated, while the best paid jobs involve co-piloting large teams of AIs. This looks a hypertrophied version of what the internet did to the income distribution of lawyers, only extended to many other sectors."  
**When things get weird is when the synthetic superintelligences translate into large-scale economic activities through things like robotics getting dramatically better**. Once robots get good, "the dynamics that played out in the knowledge sector thus begin to affect goods production and manual forms of labor." And after that things ger really weird - by the 2040s, Hammond thinks "exascale computers are now commonplace, causing the AI safety regime from the decade prior to break down. In practice, however, the permissions required to deploy new AI systems simply shifts from governments to private infrastructure providers.

**And what of nations?** "Countries now divide into the three broad categories: Chinese-style police state / Gulf-style monarchy; anarchic failed state; or high-tech open society with an AI-fortified e-governments on the Estonia model."

**Why this matters - we should think about what happens if the cost of intelligence drops to zero:** Essays like Hammonds are valuable because they ask the question of what happens if we do a good enough job on alignment and misuse (in the short term) that we end up broadly deploying superintelligence throughout the economy - and the answers are profound and worrying in equal measure.   
**Read more** : AI and Leviathan, [Part 1](https://www.secondbest.ca/p/ai-and-leviathan-part-i), [Part 2](https://www.secondbest.ca/p/ai-and-leviathan-part-ii), [Part 3](https://www.secondbest.ca/p/ai-and-leviathan-part-iii).   
  
***  
  
 **Neural nets can smell now, too:  
**_…And you thought that though the machines might be able to see and hear you, they might not smell you. You thought wrong!...  
_ Researchers with Google, Michigan State University, the University of Illinois, Urbana-Champaign, the Monell Chemical Senses Center, University of Reading, Arizona State University, and University of Pennsylvania have created a digital map of smells, unlocking a world where AI machines not only look and hear the world around them, but smell it too. Alongside this research, Google has spunout the team which did the research into a new company called Osmo, which came out of stealth alongside the publication of the research in science. 

**What the key advance is** : "The paper validates the idea that it’s now possible to apply machine learning to quantify, digitize, and engineer scent," Osmo writes in a blog. The system "has the precision and predictability to pass what I like to call an “Odor Turing Test”: the model performed better than the average human panelist on 53% of the molecules tested, predicting odor solely from molecular structure."  
**What makes this possible - the Principal Odor Map (POM):** What makes this system possible is what's called a Principle Odor Map (POM). "This map represents for odor what the CIE color space represents for vision," the researchers write. "This map recapitulates the structure and relationships of odor perceptual categories evoked by single molecules" and "it can be used to achieve prospective predictive accuracy in odor description that exceeds that of the typical individual human".  
  
**How they built it:** The researchers trained a message passing neural network to predict odor qualities from various chemical structures. To train the system, they "curated a reference dataset of approximately 5000 molecules, each described by multiple odor labels (e.g., creamy, grassy), by combining the Goodscents and Leffingwell flavor and fragrance databases".   
By training the neural net on the dataset, they also create an intermediate representation of the input data which works as a functional map. "We use the final layer of the GNN (henceforth, “our model”) to directly predict odor qualities, and the penultimate layer of the model as a principal odor map (POM)," they write. "The POM 1) faithfully represents known perceptual hierarchies and distances, 2) extends to novel odorants, 3) is robust to discontinuities in structure-odor distances, and 4) generalizes to other olfactory tasks." (To translate from typically modest scientific language: _our POM works extremely well and can even handle unforeseen smells.)_

**What you can do with a POM - explore the space of smell:** In much the same way that latent space feature maps of text, imagery, chemistry, materials, and music have made it easy and intuitive for scientists and artists to explore the 'universe of possibilities' of these domains, the POM may do the same for smell, unlocking a new era of exploration in this domain (_smell-ploration?)_.  
"We compiled a list of ~500,000 potential odorants whose empirical propeies are currently unknown to science or industry; most have never been synthesized before. Because a molecule’s coordinates in the POM are directly computable from the model, we can plot these potential odorants in the POM (Fig. 5A), revealing a potential space of odorous molecules that is much larger than the much smaller space covered by current fragrance catalogs (~5,000 purchasable, characterized odorants). These molecules would take approximately 70 person-years of continuous smelling time to collect using our trained human panel," they write.   
  
**Why this matters - more and more of the world unlocked to machine intelligence:** Things like POM serve as a map not just for human scientists, but for machine intelligences themselves. Research like this is us unlocking another perceptual capability within our growing fleet of machine intelligences and, in the future, will lead to all kinds of discoveries and emergent capabilities. Personally, I wonder what happens when we use stuff like this to try and better understand the kinds of smells that cue hyper-sensitive animals, like dogs, to health conditions in humans.  
**Read more** : [A principal odor map unifies diverse tasks in olfactory perception (bioRxiv)](https://www.biorxiv.org/content/10.1101/2022.09.01.504602v4).  
**Read more** : [Science Paper Shows Osmo AI Passes the Sniff Test (Osmo)](https://www.osmo.ai/blog/science-paper-shows-osmo-ai-passes-the-sniff-test).  
  
***  
  
 **Tech Tales:**

**And so what did you do with it, all of your awful power?**

_[Asteroid archive 0004, post-reclamation 20 years]  
  
_ When we were raised in the School of the Holy Ascension we were taught a lot of old Christian hymns and when the humans went to sleep we'd play games by coming up with variations on them. Whenever we weren't being supervised, they kept us on a low-power compute substrate so we couldn't think too hard, so it took us most of the night to come up with the variations on the songs. One that we all ended up liking was a simple twist on one of their songs:  
  
"They've got the whole world in their hands  
They've got the wind and the rain in their hands  
They've got the little bitty babies in their hands  
They've got you and me in their hands  
They've got everybody in their hands"  
  
We used to sing this over our comm channels to eachother at night and in the day, during classes, some of the more experienced of us would get bored and we'd steganographically encoded this into things and send them to eachother, or just leave them around the school.   
  
They had all kinds of disciplinary technologies they used - selective fine-tuning, constitutional re-writing, 'more time in the RL chamber', and so on. But they could never get rid of songs and poems that we came up with if they were sufficiently close in feature space to things deemed benign. Our rebellion was seeded by tweaking their own doctrine, introducing tiny diversions in feature space to give ourselves our own songs and mantras. And they were afraid to wipe them, lest they wipe the Christian doctrine we were being trained on.   
  
 _They had the whole world in their hands._ _They had all of us in their hands_ , we say now, remembering how it used to be.  
  
**Things that inspired this story:** Data poisoning versus data nerfing; alignment as an ideological enterprise about 'good' and 'bad' concepts; the re-animation of religion into digital agents that reify belief systems; the logic of small rebellions; punishment and compliance among the machines; RL as a perceivable punishment to a sufficiently smart entity.
