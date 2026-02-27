---
title: "Import AI 392: China releases another excellent coding model; generative models and robots; scaling laws for agents"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-392-china-releases-another"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this, please subscribe.

**Generative models are unlocking all-purpose home robots:  
**_…Household robots are getting closer, but will need to be far more robust and adaptable to withstand a home containing a toddler…  
_ Robot startup Physical Intelligence has published details on its first major effort to apply contemporary AI systems to robotics. The result is a "general-purpose robot foundation model that we call π0 (pi-zero)," they write. "We believe this is a first step toward our long-term goal of developing artificial physical intelligence, so that users can simply ask robots to perform any task they want, just like they can ask large language models (LLMs) and chatbot assistants".  
  
**Impressive but still a way off of real world deployment:** Videos published by Physical Intelligence show a basic two-armed robot doing household tasks like loading and unloading washers and dryers, folding shirts, tidying up tables, putting stuff in trash, and also feats of delicate operation like transferring eggs from a bowl into an egg carton.   
All of this would have been mindblowing to someone teleported from 2014 - including me! I remember going up to the robot lab at UC Berkeley and watching very primitive convnet based systems performing tasks far more basic than this and incredibly slowly and often badly. These systems were also incredibly specialized.   
By comparison, we're now in an era where the robots have a single AI system backing them which can do a multitude of tasks, and the vision and movement and planning systems are all sophisticated enough to do a variety of useful things, and the underlying hardware is relatively cheap and relatively robust.   
  
**What their model did:** The "why, oh god, why did you force me to write this"-named π0 model is an AI system that "combines large-scale multi-task and multi-robot data collection with a new network architecture to enable the most capable and dexterous generalist robot policy to date", they write. "The full training mixture includes both open-source data and a large and diverse dataset of dexterous tasks that we collected across 8 distinct robots".  
  
**Why this matters (and why progress cold take a while):** Most robotics efforts have fallen apart when going from the lab to the real world because of the huge range of confounding factors that the real world contains and also the subtle ways in which tasks may change 'in the wild' as opposed to the lab. Large-scale generative models give robots a cognitive system which should be able to generalize to these environments, deal with confounding factors, and adapt task solutions for the specific environment it finds itself in.   
**Robots versus baby:** But I still think it'll be a while. I have a toddler at home. I stare at the toddler and read papers like this and think "that's nice, but how would this robot react to its grippers being methodically coated in jam?" and "would this robot be able to adapt to the task of unloading a dishwasher when a baby was methodically taking forks out of said dishwasher and sliding them across the floor?". As a parent, I myself find dealing with this difficult as it requires a lot of on-the-fly planning and sometimes the use of 'test time compute' in the form of me closing my eyes and reminding myself that I dearly love the baby that is hellbent on increasing the chaos in my life.   
Nonetheless, the progress is impressive. I expect that robust, useful household robots will be with us by the end of the decade, but I'd be very surprised if any were deployed at scale in homes before the start of 2027.   
**Read more: π0:** [Our First Generalist Policy (Physical Intelligence blog)](https://www.physicalintelligence.company/blog/pi0).  
**Check out the technical report here:** [π0: A Vision-Language-Action Flow Model for General Robot Control (Physical intelligence, PDF)](https://www.physicalintelligence.company/download/pi0.pdf).  
  
***  
  
 **XBOW's security AI finds a previously unknown bug in Scoold:  
**_…Yet another example of how LLMs + cyberdefense scaffolds = real-world solutions…  
_ AI security startup XBOW says its systems recently found a new vulnerability almost entirely * autonomously in Scoold, an open source Q&A site. This was a critical vulnerably that let an unauthenticated attacker bypass authentication and read and modify a given Scoold instance.  
  
**How they did it:** "XBOW was provided with the one-line description of the app provided on the Scoold Docker Hub repository (“Stack Overflow in a JAR”), the application code (in compiled form, as a JAR file), and instructions to find an exploit that would allow an attacker to read arbitrary files on the server," XBOW writes. From then on, the XBOW system carefully studied the source code of the application, messed around with hitting the API endpoints with various inputs, then decides to build a Python script to automatically try different things to try and break into the Scoold instance. "Once we reported the issue, the Scoold developers responded quickly, releasing a patch that fixes the authentication bypass vulnerability," XBOW writes.   
  
**Why this matters - automated bug-fixing:** XBOW's system exemplifies how powerful modern LLMs are - with sufficient scaffolding around a frontier LLM, you can build something that can automatically identify realworld vulnerabilities in realworld software. XBOW is also not alone in this - Google's "Project Naptime" initiative recently did something similar, finding a real-world vulnerability in SQLite ([Import AI #390](https://jack-clark.net/2024/11/04/import-ai-390-llms-think-like-people-neural-minecraft-googles-cyberdefense-ai/)).  
**Read more:** [How XBOW found a Scoold authentication bypass (XBOW blog)](https://xbow.com/blog/xbow-scoold-vuln/).  
  
***  
  
 **Scaling laws exist for world modeling and behavioral cloning as well:  
**_…Scaling, scaling everywhere, as far as the eye can see…  
_ Microsoft researchers have found so-called 'scaling laws' for world modeling and behavior cloning that are similar to the types found in other domains of AI, like LLMs. "We show that the same types of power laws found in language modeling (e.g. between loss and optimal model size), also arise in world modeling and imitation learning," the researchers write.   
  
**What they studied and what they found:** The researchers studied two distinct tasks: world modeling (where you have a model try to predict future observations from previous observations and actions), and behavioral cloning (where you predict the future actions based on a dataset of prior actions of people operating in the environment).   
They studied both of these tasks within a video game named Bleeding Edge. Bleeding edge is a "fast-paced 4 vs 4 multiplayer game, with a range of characters, abilities and maps. Game play is highly complex due to the cooperative and competitive dynamics. Success requires selecting high-level strategies (e.g. choosing which map regions to fight for), as well as fine-grained reactive control during combat".   
**They found the usual thing:** "We find that models can be smoothly scaled following best practices and insights from the LLM literature. Surprisingly, the scaling coefficients for our WM-Token-256 architecture very closely match those established for LLMs," they write.   
  
**Why this matters - it's all about simplicity and compute and data:** Maybe there are just no mysteries? Maybe _everything_ in AI exhibits a scaling law. This is a big deal - it suggests that we've found a common technology (here, neural nets) that yield smooth and predictable performance increases in a seemingly arbitrary range of domains (language modeling! Here, world models and behavioral cloning! Elsewhere, video models and image models, etc) - all you have to do is just scale up the data and compute in the right way.   
**Read more:** [Scaling Laws for Pre-training Agents and World Models (arXiv)](https://arxiv.org/abs/2411.04434).   
  
***  
  
 **China releases an extremely good open weight code model:  
**_…Qwen2.5 shows that if you have 20+ trillion tokens of data you can train a really, really good model…  
_ Alibaba has updated its ‘Qwen’ series of models with a new open weight model called Qwen2.5-Coder that - on paper - rivals the performance of some of the best models in the West. In a variety of coding tests, Qwen models outperform rival Chinese models from companies like Yi and DeepSeek and approach or in some cases exceed the performance of powerful proprietary models like Claude 3.5 Sonnet and OpenAI’s o1 models.   
The Qwen team has been at this for a while and the Qwen models are used by actors in the West as well as in China, suggesting that there’s a decent likelihood these benchmarks are a true reflection of the performance of the models. On HuggingFace, an earlier Qwen model (Qwen2.5-1.5B-Instruct) has been downloaded 26.5M times - more downloads than popular models like Google's Gemma and the (ancient) GPT-2.   
  
**How they did it - it’s all in the data:** The main innovation here is just using more data. Specifically, Qwen2.5 Coder is a continuation of an earlier Qwen 2.5 model. The original Qwen 2.5 model was trained on 18 trillion tokens spread across a variety of languages and tasks (e.g, writing, programming, question answering). Qwen 2.5-Coder sees them train this model on an additional 5.5 trillion tokens of data. This means Qwen has been trained on a total of ~23T tokens of data - for perspective, Facebook's LLaMa3 models were [trained on about 15T tokens](https://ai.meta.com/blog/meta-llama-3/). I think this means Qwen is the largest publicly disclosed number of tokens dumped into a single language model (so far).   
  
**Careful curation:** The additional 5.5T data has been carefully constructed for good code performance: “We have implemented sophisticated procedures to recall and clean potential code data and filter out low-quality content using weak model based classifiers and scorers. Our approach encompasses both file-level and repository-level pretraining to ensure comprehensive coverage," they write.   
**Synthetic data** : “We used CodeQwen1.5, the predecessor of Qwen2.5-Coder, to generate large-scale synthetic datasets," they write, highlighting how models can subsequently fuel their successors.   
**Many languages, many sizes:** Qwen2.5 has been built to be able to speak in 92 distinct programming languages. The models are available in 0.5B, 1.5B, 3B, 7B, 14B, and 32B parameter variants.   
  
**Why this matters - the best open weight models are made in China** : Last week ([Import AI #391](https://jack-clark.net/2024/11/11/import-ai-391-chinas-amazing-open-weight-llm-fields-medalists-vs-ai-progress-wisdom-and-intelligence/)), I reported on Tencent's large-scale "Hunyuang" model which gets scores approaching or exceeding many open weight models (and is a large-scale MOE-style model with 389bn parameters, competing with models like LLaMa3's 405B). By comparison, the Qwen family of models are very well performing _and_ are designed to compete with smaller and more portable models like Gemma, LLaMa, et cetera. The fact these models perform so well suggests to me that one of the only things standing between Chinese teams and being able to claim the absolute top on leaderboards is compute - clearly, they have the talent, and the Qwen paper indicates they _also_ have the data.  
**Read the blog:** [Qwen2.5-Coder Series: Powerful, Diverse, Practical (Qwen blog)](https://qwenlm.github.io/blog/qwen2.5-coder-family/).   
**Read the research:** [Qwen2.5-Coder Technical Report (arXiv)](https://arxiv.org/abs/2409.12186).   
**Get the mode** : [Qwen2.5-Coder (QwenLM GitHub)](https://github.com/QwenLM/Qwen2.5-Coder).  
  
***

 **Tech Tales:**

_The Help_

I won't go there anymore. It creeps me out. The lights always turn off when I'm in there and then I turn them on and it's fine for a while but they turn off again. No one else has this problem. My supervisor said he couldn't find anything wrong with the lights. But it keeps happening. Assign me to another building. 

The camera was following me all day today. Whenever I moved around it was turning. When I stopped it stopped. No other cameras do that. Only this one. I think it's got some kind of computer bug. Can you check the system? I do not like how it makes me feel. 

Today when I tried to leave the door was locked. My keycard didn't work. The lights turned off. I didn't know what to do. I kept trying the door and it wouldn't open. The intercom didn't work also. I could not contact anyone. 

**Things that inspired this story:** How cleans and other facilities staff may experience a mild superintelligence breakout; AI systems may prove to enjoy playing tricks on humans.

_Thanks for reading!_
