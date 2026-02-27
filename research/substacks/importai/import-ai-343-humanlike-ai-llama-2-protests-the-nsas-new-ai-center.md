---
title: "Import AI 343: Humanlike AI; LLaMa 2 protests; the NSA's new AI center"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-343-humanlike-ai-llama"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Google DeepMind and 33 labs make the world's largest AI robot training set - and uses it to create capability emergence:  
**_…Open X-Embodiment dataset is a giant, diverse dataset, that may make robots much, much better…  
_ Google DeepMind and 33 academic labs to combine data recorded from 22 different robots around the world to create a really big dataset. It has also shown that by training robot control models on this dataset, it can significantly improve their performance.  
As part of this research, the company is releasing the dataset, as well as some pre-trained models trained on it. "We intend for these resources to form a foundation for X-embodiment research in robot learning," the researchers write. 

**What the dataset is:** Open X-Embodiment consists of data taken from "22 robot embodiments, demonstrating more than 500 skills and 150,000 tasks across more than 1 million episodes." The robots used in this dataset vary from single robot arms to bi-manual robots and quadrupeds. "The dataset was constructed by pooling 60 existing robot datasets from 34 robotic research labs around the world and converting them into a consistent data format for easy download and usage."

**Want better performance? Train your models on heterogeneous data:** DeepMind trains some models atop two existing large-scale robot models, RT-1, a robotic control model, and RT-2, a vision-language action model. RT-2 is a significantly larger model than RT-1. The researchers make two interesting discoveries:

  * **High-capacity models can get better in-distribution performance with heterogenous data:** In tests, they find that RT-2-X (55B parameter) models significantly outperform smaller capacity models on in-distribution tests, "suggesting that X-robot training can improve performance in the data-rich domains, but only when utilizing a sufficiently high-capacity architecture."

  * **Heterogeneous data can help with out-of-distribution generalization: Models trained on Open X-Embodiment data significantly outperform models trained on single-robot data when it comes to handling out-of-distribution tasks. "Our results suggest that co-training with data from other platforms imbues the RT-2-X controller with additional skills for the platform that are not present in that platform’s original dataset." Here, again, a high-capacity model is important "the 55B model has significantly higher success rate in the Emergent Skills compared to the 5B model," they write.**




**Why this matters - more data + big models = capability expansion:** Sometimes I think developing AI is more like a chemical process than a machining one, especially with research projects like this. What this work shows is that if you have the right input basic material (data) with the right distribution (here, a heterogeneous one across a bunch of robots), and then you train a high-capacity neural net on it, you get out something greater than the sum of its parts - a model with surprisingly good out-of-distribution generalization as a consequence of some critical reaction that occurs due to your combo of data + architecture + complexity.   
The longer term implication of this is that the world 'wants' to gather as large a heterogeneous dataset as possible and then combine that with an extremely large architecture, leading to a system with surprising 'emergent capabilities'. I'll leave it to the reader to idly speculate as to just how large and just how emergent such a system could become.   
**Read more** : [Scaling up learning across many different robot types (Google DeepMind)](https://www.deepmind.com/blog/scaling-up-learning-across-many-different-robot-types).  
**Access the code and data here** : [Open X-Embodiment: Robotic Learning Datasets and RT-X Models (research website)](https://robotics-transformer-x.github.io/).   
**Read the research paper here:** [Open X-Embodiment: Robotic Learning Datasets and RT-X Models (PDF)](https://robotics-transformer-x.github.io/paper.pdf).  
  
***   
  
**AI safety lobby protests Facebook's open source models:  
**_…AI safety moves from a niche concern on internet forums to real world protests…  
_ A bunch of people concerned about the rapid advance of AI have led an in-person protest outside of Facebook's offices in San Francisco. The protests were seeking to draw attention to Facebook's release of the 'LLaMa 2' family of openly distributed models. “Releasing weights is a dangerous policy, because models can be modified by anyone, and they cannot be recalled,” said Holly Elmore, who organized the protests, according to _IEEE Spectrum_. "The more powerful the models get, the more dangerous this policy is going to get.” 

**Why this matters - AI as a political force, nuclear power as an imperfect analogy:** AI has become sufficiently interesting and impactful that it is, like a boulder rolling down a hill, gathering more and more political salience over time. Protests like this are the first indications of some of the larger challenges that the industry will face as people try to debate both what a) AI safety is and b) what an acceptable level of AI safety looks like for the industry.   
These protests and debates are going to feel confusing until we have a clear notion of safety, and then we'll get into the really tough part of negotiating what an acceptable level of safety looks like for the sector.  
**Read more** : [Protesters Decry Meta’s “Irreversible Proliferation” of AI (IEEE Spectrum)](https://spectrum.ieee.org/meta-ai).  
  
***  
  
 **Image models are getting closer and closer to behaving like humans:  
**_…Another landmark result on 'shape bias' shows how humans and AI systems are more alike than you'd think…  
_ Researchers with Google DeepMind have shown how generative classifiers - image recognition systems based on generative models - have four surprisingly human-like qualities. The results are interesting because they show how as we improve the performance of our AI systems, the AI systems seem to end up displaying human-like qualities in terms of _how_ they solve certain tasks.   
  
**Three models and four properties:** The researchers tested out three different generative models, two from Google, Imagen and Parti, and one from the open source community, Stable Diffusion. In testing, they identified four intriguing human-like properties in the models:

  * **Human-like shape bias:** "The shape bias of a model indicates to which degree the model's decisions are based on object shape, as opposed to object texture," they write. "We find that all three zero-shot generative classifiers show a shape bias that matches humans: Imagen achieves a stunning 99% shape bias, Stable Diffusion 93% and Parti a 92% shape bias." (Another interesting wrinkle is all of these generative models outperform ViT-22B, an earlier model with human-like shape bias: [Import AI #319](https://jack-clark.net/2023/03/06/import-ai-319-sovereign-ai-facebooks-weights-leak-on-torrent-networks-google-might-have-made-a-better-optimizer-than-adam/)).

  * **Near human-level out-of-distribution accuracy:** "Imagen and Stable Diffusion achieve an overall accuracy that is close to human-level robustness despite being zero-shot models," they write. Though they find that all three tested models do badly with recognizing rotated images. 

  * **State-of-the-art error consistency with humans** : When tested, the models are also showing more overlap with humans in terms of errors - as in, when they make errors, they're increasingly for the same image analysis tasks that humans tend to make errors in. "Imagen shows the most human-aligned error patterns, surpassing previous state-of-the-art (SOTA) set by ViT-22B," they write. 

  * **An understanding of certain perceptual illusions:** In a more qualitative test, the researchers looked at optical illusions of two types - bistable illusions where things can look like two different things (e.g, the famous picture of a rabbit that is also a duck), or images where humans exhibit pareidolia ("a tendency to see patterns in things, like a face in a rock"). They found that "in all cases, the text-to-image generative models are able to recognize the illusion and recreate correct images conditioned on the respective text prompts".




**Why this matters:** If something talks like a duck and quacks like a duck, it's reasonable to assume it's a duck, or at least ducklike. What if something talks like a human and has similar biases to a human? Results like this show an eerie kind of convergence between AI systems and humans in terms of not just capability but also _how_ they achieve their capabilities (another recent, intriguing result was work from DeepMind that showed an RL-trained 'Adaptive Agent' could learn to solve novel environments in roughly the same time as humans: [Import AI #316](https://jack-clark.net/2023/01/30/import-ai-316-scaling-laws-for-rl-stable-diffusion-for-160k-yolov8/)).  
When seeing results like this, it's harder to explain away recent AI progress as being just a consequence of lots of compute leading to computers solving things in strange or inhuman ways. Rather, it suggests that if we dump enough compute into AI systems and pair this with the right objective function, we can sometimes generate systems which learn to solve problems using similar tricks as humans.   
**Read more** : [Intriguing properties of generative classifiers (arXiv)](https://arxiv.org/abs/2309.16779).  
  
***   
  
**NSA stands up a dedicated office for AI technology:  
**_…The AI Security Center means the IC is focusing more on AI…  
_ Most technologies end up being widgets that get bolted onto military things - think of better suppressors for weapons, better radio technology for communication, and so on. But some technologies are seen as so strategic that they end up getting dedicated attention as things in their own right - think the powerful satellites and sensing tech developed by the National Reconnaissance Office, the various hypersonic weapons programmes, and quantum computers for codebreaking.   
Now, AI has moved into the second bucket as the US's National Security Agency has announced the creation of an AI Security Center, a new office which will, per the NSA, "become the focal point for developing best practices, evaluation methodology and risk frameworks with the aim of promoting the secure adoption of new AI capabilities across the national security enterprise and the defense industrial base."   
  
**What the center will do:** The new center will work across government, academia, U.S Industry, and "select foreign partners". ""AI will be increasingly consequential for national security in diplomatic, technological and economic matters for our country and our allies and partners," said NSA Chief Paul Nakasone.   
The NSA is going to focus on AI security, which Nakasone defines as "protecting AI systems from learning, doing and revealing the wrong thing". The NSA will also try to better understand AI vulnerabilities, foreign intelligence threats to US AI systems, and how to keep the US ahead in this technology.   
  
**Why this matters - the government is now doing longterm thinking about AI:** For a few years, AI has been a topic of political conversation, with different administrations periodically picking up and putting down the issue (e.g, Obama, Trump, and Biden admins all did various things related to AI and AI in government).   
With the intelligence community now dedicating an office to AI, we can be guaranteed of sustained work on AI for the years to come, meaning that at least one appendage of the US government is now going to be doing very longterm thinking about AI and its impact. This will likely lead to meaningful changes in what AI capabilities the US government fields and will also both increase (some) and mitigate (some other) geopolitical tensions with regard to AI technology.   
The greyworld has turned its austere and patient gaze to AI and shall now not look away.   
**Read more:** [AI Security Center to Open at National Security Agency (US Department of Defense website)](https://www.defense.gov/News/News-Stories/Article/Article/3541838/ai-security-center-to-open-at-national-security-agency/).  
  
***  
  
 **Tech Tales:  
  
The Revolution will be Generated  
** _[Conversations in the center of government of an autocracy, some time in the 2030s]_

Sir, at some point they're going to rise up. This can't go on.   
"It's gone on this long - and the latest system is coming online, that'll buy us a few more years."   
And then what?  
"We're expecting the second layer of surveillance and pre-crime prediction to be online by then, I expect that'll quell the dissenters. The others will be pacified by The Entertainment."   
There will be a limit to this. Not all people like The Entertainment. And there are already signs that people are starting to prefer it if The Entertainment shows them stories about the revolution.   
"Perhaps you don't see how good this is. The more they spend their emotions on revolutions in The Entertainment, the less energy they'll have for a real one."   
Surely you can't be so arrogant?  
"Surely you can't underestimate people's propensity for boredom so much?"  
  
**Things that inspired this story:** The 'guns vs butter' dichotomy disappearing given sufficiently good media; Brave New World; David Foster Wallace; generative models and their logical destiny as personally-customized engines for the generation of persuasive and captivating media; persuasion and AI systems.
