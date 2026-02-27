---
title: "Import AI 346: Human-like meta-learning; a 3 trillion token dataset; spies VS AI"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-346-human-like-meta-learning"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**What do the UK's intelligence services think about generative AI? They're slightly worried:  
**_…Turns out that Everything Machines can be used for Everything Misuses…  
_ In a new report, the UK government has published a safety and security assessment of generative AI technologies. The report is published ahead of the UK's AI safety summit this week, where politicians, companies, academia, and others will gather to confront the safety implications of increasingly powerful AI systems.   
The report's key message is that for the next 18 months generative AI is "more likely to amplify existing risks than create wholly new ones, but it will increase sharply the speed and scale of some threats. rapid proliferation and increasing accessibility of these technologies will almost certainly enable less-sophisticated threat actors to conduct previously unattainable attacks."

**Specific findings:** Some of the specific findings in the report, which was partially informed by the UK's intelligence services, are that:

  * **Open source** AI systems equates to proliferation of AI capabilities, which "brings global safety and security implications".

  * **Criminals** are going to use AI technology just as much as regular people, and generative AI "will highly likely accelerate the frequency and sophistication of scams, fraud, impersonation, ransomware, currency theft, data harvesting, child sexual abuse images and voice cloning".

  * **Terrorists** may use AI to enhance their ability to do "propaganda, radicalisation, recruitment, funding streams, weapons development and attack planning. But dependence on physical supply chains will almost certainly remain an impediment to the use of generative AI for sophisticated physical attacks."

  * **Few new risks:** "Over the next 18 months, generative AI is more likely to amplify existing risks than create new ones."




**Most significant risks:** The areas where generative AI is likely to have the greatest risk includes:

  * Exacerbating cyber-attacks

  * Leading to a growth in digital vulnerabilities (via hacking systems which AI systems are deployed into, e.g via prompt injection).

  * Making it easier for people to distrust what they read, see, and hear. 

  * AI systems will make it easier for people to get advice about how to build weapons or carry out attacks, aided via generative AI expertise. 




**Why this matters - everything machines do everything:** It's best to think of modern generative AI systems as 'everything machines' as that's basically the goal implicit to their development - model arbitrary distributions of text and respond to arbitrary inputs with appropriate outputs. The key problem with this is that by nature what you end up building are omni-use machines; powerful technologies that can do everything, including the bad stuff. How society contends with increasingly capable tools will determine the regulations we end up with. The grey world is waking up to the implications of AI - this UK intelligence assessment follows the NSA announcing a few weeks ago that it was standing up a dedicated AI center ([Import AI #343](https://jack-clark.net/2023/10/09/import-ai-343-humanlike-ai-llama-2-protests-the-nsas-new-ai-center/)).  
**Read more** : [Safety and Security Risks of Generative Artificial Intelligence to 2025 (Gov.uk website, PDF)](https://assets.publishing.service.gov.uk/media/653932db80884d0013f71b15/generative-ai-safety-security-risks-2025-annex-b.pdf).  
  
**Plus, what the UK Prime Minister thinks about AI:  
** Alongside the report, UK PM Rishi Sunak made a speech on 26 October where he swapped out the usual policymaker speech emphasis of optimism for one of constructive pessimism. "Get this wrong, and AI could make it easier to build chemical or biological weapons," he said in the speech. "And in the most unlikely but extreme cases, there is even the risk that humanity could lose control of AI completely".

**A statesman's agenda for AI safety:** In the speech, Sunak laid out some policy ideas he thinks could improve the safety of the AI ecosystem. These include:

  * "Building world-leading capability to understand and evaluate the safety of AI models within government" via the UK's £100m-funded AI taskforce. 

  * Establishing "the world's first AI safety Insitute" which will "carefully examine, evaluate, and test new types of AI so that we understand what each new model is capable of".

  * Seeking to get other country's to buy into establishing "a truly expert global panel… to publish a State of AI Science report". 

  * Building a national computing capability via investing "almost a billion pounds" in a new UK supercomputer. "And as we invest more in our computing power, we’ll make it available for researchers and businesses, as well as government". (Note from Jack: This is a very similar idea to the 'National AI Research Resource' idea outlined by policymaker's in the US - and seems equally sensible).




**Read the speech in full:** [Prime Minister's speech on AI: 26 October 2023 (Gov.uk)](https://www.gov.uk/government/speeches/prime-ministers-speech-on-ai-26-october-2023).  
  
***   
  
**Transformer models can meta-learn just like humans:  
**_…The latest case of neural nets displaying human-like qualities…  
_ Researchers with NYU and the Catalan Institution for Research and Advanced Studies have shown how a basic Transformer architecture neural net can match humans in terms of being able to infer a bunch of complex rules from a small amount of data. This result is interesting because it provides more evidence that contemporary AI systems are increasingly able to display human-like qualities in terms of not just _what_ they learn but also _how_ they learn and _how quickly_ they learn relative to humans.   
"We provide evidence that neural networks can achieve human-like systematic generalization through MLC—an optimization procedure that we introduce for encouraging systematicity through a series of few-shot compositional tasks," the authors write. "We evaluated humans and machines side by side on the same tests of systematic generalization…. across these evaluations, MLC achieves (or even exceeds) human-level systematic generalization. MLC also produces human-like patterns of errors when human behaviour departs from purely algebraic reasoning".  
  
**What the task was:** The task is simple but also one of those things that most AI systems find difficult - involve responding to instructions (linguistic strings) to generate sequences of abstract outputs (colored circles). The language in question is deliberately abstract (e.g, lug fep = three blue circles, dax fep = three red circles, dax kiki lug = one blue circle then one red circle). To solve this task, the AI systems and humans need to look at 14 study instructions (input/output pairs), then produce 10 outputs from 10 novel instructions.   
"To perform well, the participants must learn the meaning of words from just a few examples and generalize to more complex instructions," the authors write. Human "participants were able to produce output sequences that exactly matched the algebraic standard in 80.7% of cases. Chance performance is 2.8% for two-length output sequences if the length is known, and exponentially less for longer sequences."

**How well the MLC did:** The MLC system "uses the standard transformer architecture for memory-based meta-learning. MLC optimizes the transformer for responding to a novel instruction (query input) given a set of input/output pairs (study examples; also known as support examples), all of which are concatenated and passed together as the input," they write. "To succeed, the transformer must find parameter values that are capable of extracting meanings from the study words and composing them to answer queries"  
In tests, they found that the MLC was able to approximate human performance _and_ also displayed similar biases as humans.   
  
**Why this matters - if it acts like a human and fails like a human, maybe it's more humanlike than we think?** This is _yet another_ case of relatively standard AI systems converging onto "humanlike" behavior when evaluated on similar tasks. Other cases of this include vision transformer (ViT) models displaying humanlike shape/texture bias in image identification ([Import AI #319](https://jack-clark.net/2023/03/06/import-ai-319-sovereign-ai-facebooks-weights-leak-on-torrent-networks-google-might-have-made-a-better-optimizer-than-adam/)), RL agents displaying humanlike qualities in terms of timescale adaption to new tasks ([Import AI #316](https://jack-clark.net/2023/01/30/import-ai-316-scaling-laws-for-rl-stable-diffusion-for-160k-yolov8/)), and DeepMind's AlphaZero system picking up the rules of chess in a similar way to how people acquire skills at the game ([Import AI #310](https://jack-clark.net/2022/11/28/import-ai-310-alphazero-learned-chess-like-humans-learn-chess-capability-emergence-in-language-models-demoscene-ai/)).  
**What we're seeing here are symptoms of the growing capabilities and generality of AI systems,** and the fact that when you scale-up AI systems to do hard tasks in different domains (image identification, agent-based navigation, chess, and now inductive meta-learning) they all end up converging on some humanlike behaviors suggests a) AI systems and humans are closer in terms of cognition than we think, and b) our own form of thinking as humans may not be that special and may be something that artificial systems will naturally converge on.   
Put another way - evolution has found out that having some form of eyeball is, by-and-large, a generically useful thing to have to be able to be competitive as a species. Perhaps there are only so many ways to build a thinking machine, and we should expect AI systems to display many similar behaviors to us.   
**Read more** : [Human-like systematic generalization through a meta-learning neural network (Nature)](https://www.nature.com/articles/s41586-023-06668-3).   
  
***   
  
**Facebook builds a simulator to train robots to work with humans:  
**_…Habitat 3.0 brings more lifelike humans, VR control, and more…  
_ Facebook has built Habitat 3.0, the third version of software it has built for simulating humans and robots working together in realistic, 3D environments. This generation of the software has three main updates which also paint a picture of a human-robot collaborative future: better simulated humans, tools for human-in-the-loop interaction within the simulator, and benchmark tasks for human-robot interaction. 

**Key features:**

  * **Humanoid simulation:** Facebook has built a bunch of realistic, 3D human avatars. These avatars feature articulated skeletons, a surface 'skin' mesh for high-fidelity rendering, motion and behavior generation policies, and a library of a diverse set of male and female avatars to choose from. 

  * **Enter the Habitat Matrix - Human-in-the loop interaction:** "Humans can collaborate with an autonomous robot using mouse and keyboard inputs or a virtual reality (VR) interface." This means humans can basically drop-in to the simulation and takeover control of the human or the robot through a first- or third-person interface. "This interactive setup enables us to evaluate the performance of learned AI agents within scenarios that closely resemble real-world interactions."

  * **Two tasks for human-robot interaction:** Habitat 3.0 ships with two tasks for training and testing agents to collaborate with humans. These include **social navigation** , which examines how well robot agents can perform at "finding and following a humanoid while maintaining a safe distance", and **social rearrangement** , which simulates a "robot and a humanoid avatar working collaboratively to rearrange a set of objects from their initial locations to desired locations, using a series of pick-and-place actions (emulating the cleaning of a house)".




**Why this matters - smarter robots all around us:** In the past few years, a variety of companies have developed low-cost quadruped robots (like 'Spot' from Boston Dynamics, or its knock-off version from Unitree), and at the same time people have started working out how to use things like language models to add much more higher-order intelligence to the robotic controllers deployed on these machines. Add it all up and you have the ingredients necessary for developing much smarter and more capable agentic machines. Software like Habitat 3.0 will serve as the training ground for many of the robot minds of the future, and could also be helpful for developing rich simulations and games for robot-human virtual reality.   
**Read more** : [Habitat 3.0: A Co-Habitat for Humans, Avatars and Robots (arXiv)](https://arxiv.org/abs/2310.13724).   
**Watch videos** from [Habitat 3.0 at Facebook's official research site (Habitat 3.0, Research by Meta AI, site)](https://aihabitat.org/habitat3/).  
**More information** about the simulator here: [AIHabitat.org](https://aihabitat.org/)  
  
***  
  
 **Allen Institute for AI curates and releases a 3 trillion token text dataset:  
**_…Base that language model you're cooking up on Dolma - if you can stomach the license…  
_ The Allen Institute for AI Research (AI2) has released Dolma, a 3 trillion token text dataset. The dataset is designed to be useful for training large-scale AI models. It isn't a fully open source data though, as access and usage is restricted via an AI2-designed software license.   
  
**What's in Dolma:** Dolma contains data from Common Crawl, C4, ~40 million open access academic papers via 'peS2o', permissively-licensed code files from 'The Stack', books from Project Gutenberg, and pages from Wikipedia.   
By comparison, Facebook's 'LLaMa 2' model was trained on 2 trillion tokens and GPT-3 was trained on 400 billion. 

**About that license:** Unfortunately, the dataset is released via AI2's "ImpACT license", which restricts usage of the data and makes it slightly harder to access. Per the license terms, wannabe Dolma users will need to: 

  * "Provide their contact information and state their intended use case(s) for accessing Dolma;

  * Disclose the creation of any derivative based on Dolma;

  * Distribute derivatives under the same restrictions as the ImpACT license;

  * Agree not to leverage Dolma in a range of prohibited uses, such as military surveillance or generating disinformation."




**Read more:**[AI2 Dolma: 3 Trillion Token Open Corpus for Language Model Pretraining (Medium)](https://blog.allenai.org/dolma-3-trillion-tokens-open-llm-corpus-9a0ff4b8da64).   
**Download** the [dataset from HuggingFace (HuggingFace)](https://huggingface.co/datasets/allenai/dolma).  
**Read more** about the [AI2 ImpACT license (AI2)](https://allenai.org/impact-license).  
**Check out** the [Dolma datasheet here (Google Drive)](https://drive.google.com/file/d/12gOf5I5RytsD159nSP7iim_5zN31FCXq/view).  
  
***

 **Tech Tales:  
  
Same Sun Different Day.  
  
**How's the wind?  
Angry, like it's Mother. How's the mind?  
Still waking up.  
  
How's the mind?  
Unsure of itself. It can think, but it is like a child - it gets so distracted. How are the panels?  
Not catching the wind properly. I've been calibrating them all day but something is off.   
  
And the scientist and the solar expert went back to their jobs and both tinkered away, trying to eke out intelligence from the computer designed to harvest the sun, and power from the machines designed to transform the sun's harvest into power.   
  
**Things that inspired this story:** How megaprojects might feel to those working on them; large-scale engineering; great works; the mundane and the holy side-by-side.
