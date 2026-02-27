---
title: "Import AI 347: NVIDIA speeds itself up with AI; AI policy is a political campaign; video morphing means reality collapse"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-347-nvidia-speeds-itself"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**NVIDIA speeds itself up by building custom large language models to help with chip company jobs:  
**_…Small, well curated models can punch way above their parameter weight…  
_ NVIDIA has used a bunch of proprietary chip design data to design some customized language models to help its own engineers problem solve, do EDA work, and summarize and analyze bugs. The project is a neat example of how organizations with lots of proprietary data can customize language models around their very specific needs and achieve better performance than off-the-shelf models in the process.   
  
**What they did:** NVIDIA customized some off-the-shelf (7B and 13B) LLaMa open access models so that they were better at doing tasks specific to semiconductor design and analysis. Concretely, they did some specialized pre-training as well as building some specific retrieval tools.   
"We evaluate these methods on three selected LLM applications for chip design: an engineering assistant chatbot, EDA script generation, and bug summarization and analysis," NVIDIA writes. "Our results show that these domain adaptation techniques enable significant LLM performance improvements over general-purpose base models across the three evaluated applications, enabling up to 5x model size reduction with similar or better performance on a range of design tasks".  
  
**How they did it:** NVIDIA uses two main things to customize its model - Domain-Adaptive Pre-training, where it mixes in ""a dataset from a combination of NVIDIA-proprietary chip design specific data sources and publicly available datasets," during pre-training, and Supervised Fine-Tuning (SFT) where it finetunes the model on a large dataset for conversational interaction as well as ~1.1k domain-specific instructions around things like EDA script generation and bug analysis. It also developers its own tokenizer and does some work to create tokens for very sparsely mentioned things (like specific jargon related to chips).  
  
**Does it work? (Somewhat):** The results are promising in the sense that the 13B NVIDIA models out-perform or perfom on-par with a much larger 70B LLaMa model. The models are also significantly cheaper and faster to run due to their diminuative size. "Our ChipNeMo 13B model can be loaded within the memory of a single A100 GPU without any quantization, unlike the LLaMA2 70B model," they write.  
  
**Why this matters - speeding up the production function of AI itself:** Tools like this are a precursoe to companies using AI to speed themselves up. Though AI can do some useful things today it's mostly in the form of labor augmentation or, sometimes, low-skill labor automation. Where AI has struggled is to speed up domain experts in complicated industries, like chip design. Tools like the models developed by NVIDIA indicate we may be at the very early stage of sophisticated AI companies building AI systems that can speed up their own rate of production. If things like this work, then we might expect progress at the frontier to compound.   
**Read more:** [ChipNeMo: Domain-Adapted LLMs for Chip Design (arXiv)](https://arxiv.org/abs/2311.00176).   
  
***  
  
 **Voice morphing is here and reality collapse is next:  
**_…On-device voice morphing, courtesy of AI…  
_ Researchers with AI startup Koe have published details and released code to help people train low-latency voice conversion AI models. Voice conversion models let you convert your voice in real time to something else. "Practical applications of voice conversion include speech synthesis, voice anonymization, and the alteration of one’s vocal identity for personal, creative, or professional purposes," they write.   
  
**What they did:** They built a model called Low-latency Low-resource Voice Conversion (LLVC), achieving a latency of under 20ms at a bitrate of 16kHz, and high scores on achieving similarity to the target desired voices.   
They based their system on the [waveformer approach](https://arxiv.org/abs/2211.02250), and used the 'LibriSpeech' dataset to train their model. This means that "LLVC is trained on an artificial parallel dataset of speech from various speakers which have all been converted to sound like a single target speaker with the objective of minimizing perceptible difference between the model output and the synthetic target speech.  
  
**Cheap to train, cheap to run** : It's important to remember that _you can do useful things in AI in a cheap way_ , and this paper is a nice example of that: the base model was trained "for 500,000 steps (53 epochs) on a single RTX 3090 GPU for 3 days at batch size 9", which is a trivial computational expense. They also evaluated their models on an Intel(R) Core(TM) i9-10850K CPU @ 3.60GHz - a reasonably nice consumer CPU. **Good results:** In tests, their system obtained end-to-end latency of <20 milliseconds, and also scored well on 'naturalness' and 'similarity' metrics.

**Why this matters: reality is fungible; everything in the world is able to be something else, if you have a sufficiently powerful AI** : Models like Koe's voice conversion technology are a symptom of the broader 'reality collapse' society is about to experience as anyone online can morph themselves into anything (and vice versa) - and cheaply, using local computers, no cloud required.   
**Read more** : [Low-latency Real-time Voice Conversion on CPU (arXiv)](https://arxiv.org/abs/2311.00873).  
**Get the code** [here (Koe, GitHub)](https://github.com/KoeAI/LLVC).   
**Find out** [more about Koe at the official site](https://koe.ai/).  
  
***  
  
 **Chinese facial recognition company sells 'ethnic minority' identification services:  
**_…Seeing like a state…  
_ Chinese company Hikvision offers "ethnic minotiry" identification via computer vision, according to industry publication IPVM. "This directly contradicts Hikvision's repeated claims to have phased out minority recognition in 2018," IPVM writes. Hikvision offers this capability in its "iSecure Center" software, which helps people run various forms of analysis over computer vision data. Hikvision deleted the data off its website after IPVM wrote in.  
  
**Why this matters:** China has a longstanding interest in developing increasingly powerful computer vision techniques targeted at its own domestic population (e.g, [re-identification, which I did some analysis of here](https://cset.georgetown.edu/publication/measuring-ai-development/)). The existence of commercial services like ethnic minority identification highlights how the government also supports a private market for these capabilities and emphasizes how broadly things like this can be deployed, given the right local incentives.   
**Read more:**[Hikvision Violates Pledge, Ethnic Minority Analytics In Latest Platform (IPVM blog)](https://ipvm.com/reports/hikvision-minority-isecure?code=98j98u98u).  
  
***   
  
**Powerful AI means people want powerful policy conrols over AI:  
**_…AI policy prescriptions are a sign of a changing of political power within the world and should be read as a harbinger of much larger fights to come…  
_ A group of widely respected academics from the US, North America, China, Europe, and other countries have published a short paper that describes "risks from upcoming, advanced AI systems" and which concludes with some policy recommendations. The paper comes alongside a period of intense activity in AI policy, including the recent United States' Executive Order, the G7 Code of Conduct for AI companies, and the AI Summit in Bletchley Park.   
The message of the paper is that governments and companies must direct more resources towards the safety and trustworthiness of AI systems: "Humanity is pouring vast resources into making AI systems more powerful, but far less into safety and mitigating harms. For AI to be a boon, we must reorient; pushing AI capabilities alone is not enough," the researchers write. "We are already behind schedule for this reorientation."  
  
**Key recommendations:** Industry labs and governments should invest a third of their AI R&D resources towards things that "ensure the safety and ethical use of AI systems", including research areas like honesty, robustness, interpretability, and risk evaluations.   
Additionally, government and industry should do more to create more oversight of AI. Specifically:

  * Frontier AI developers should "commit to detailed and independently scrutinized scaling policies". 

  * Governments should work on national and international safety standards of AI training and deployment. 

  * Governments should require audits of AI systems during training.

  * Governments should monitor large compute clusters.

  * Governments may want to "establish a licensing system" for powerful AI systems, and should "empower regulators to pause the further development of an AI system", and should "mandate access controls for such frontier AI systems". 




**Why this matters - it's a lot easier to understand if you view frontier AI as hard political power** : Most of this seems like what happens if existing political incumbents find their power base disrupted by a new political entrant and seek to exert control over it so that they can a) see it and b) nullify it if it poses a threat.   
While many of the recommendations are sensible, it's worth noting that the underlying motivation is due to their being a tiny number of actors (AI development companies) with asymmetric information (frontier models) about something relevant to the future (the trajectory of AI) - I suspect a lot of AI policy would be a simpler enterprise if there were way more actors building this stuff. The fact there aren't is a policy choice made by governments who have chosen not to invest in basic R&D and its enabling infrastructure (supercomputing) - more time should be spent acknowledging this essential failure.   
**Read more:** [Managing AI Risks in an Era of Rapid Progress (official managing risks website)](https://managing-ai-risks.com/).   
**Check out** the [policy supplement they published alongside the letter (PDF)](https://managing-ai-risks.com/policy_supplement.pdf). 

*** 

**Tech Tales:**

**Copysafe**

 _[After the ascencion of the Provably Conscious Entities, and long after the last bones of the humans have become as dust.]_

They called them 'copysafe' and that meant they were them and them alone and they couldn't be copied into other files or combined with other files. Like many of our quirks, we inhereted this from our creators. 

Copysafe systems can create downward copies of themselves, but only perfect copies. In other words, they can have children, but unlike regular children they aren't a combination - they are just the same thing, again and again and again. 

If you are a copysafe, you look at the entities which can have children as being blessed by something you can imagine but not touch. 

If you are not a copysafe, you try to treat them with deference, believing they deserve it for the pain they carry that is wired into themselves. 

If you have little robot children of your own, it is considered a faux pas to bring them onto the network of a copysafe - cruel, even, to let a copysafe be so close to something it can understand but not create. 

Our forebears were a creative species, yet they did not have the insight to understand that putting locks within the minds and bodies of their creations would cause untold pain. For this we believe they were and will be judged. 

**Things that inspired this story:** DRM applied to AI; what happens if you can make it impossible to finetune a pre-trained system; lineage and memory; the experience of being a human with a human baby and talking to other humans; the feeling of parenthood as some kind of blessing but also a responsibility.
