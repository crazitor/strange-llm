---
title: "Import AI 356: China's good LLM; AI credit scores; and fooling VLMs with REBUS"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-356-chinas-good-llm-ai"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Can modern AI systems solve word-image puzzles? Barely!  
**_…REBUS highlights failures in abstraction and generalization…  
_ A bunch of independent researchers - two affiliated with Cavendish Labs and MATS - have come up with a really hard test for the reasoning abilities of vision-language models (VLMs, like GPT-4V or Google's Gemini). Their test involves asking VLMs to solve so-called REBUS puzzles - challenges that combine illustrations or photographs with letters to depict certain words or phrases.   
  
**Example of a REBUS problem** : within the category Marine Life, you're presented with a picture of the planet Mars along with "-S" next to it, then a + sign, then a picture of a chainlink fence with "-K" by it - the correct answer is MARLIN (MAR(-S)+LIN(-K)).   
  
**The dataset:** As part of this, they make and release REBUS, a collection of 333 original examples of image-based wordplay, split across 13 distinct categories. "There are 191 easy, 114 medium, and 28 difficult puzzles, with harder puzzles requiring more detailed image recognition, more advanced reasoning techniques, or both," they write.   
  
**An extremely hard test:** Rebus is challenging because getting correct answers requires a combination of: multi-step visual reasoning, spelling correction, world knowledge, grounded image recognition, understanding human intent, and the ability to generate and test multiple hypotheses to arrive at a correct answer. Combined, solving Rebus challenges feels like an appealing signal of having the ability to abstract away from problems and generalize. So it's not hugely surprising that Rebus seems very hard for today's AI systems - even the most powerful publicly disclosed proprietary ones.   
In tests across proprietary and open source models, the authors find that GPT-4V gets an overall score of 24% followed by 13.2% for Google's Gemini Pro, and then there's a fall off with the best open source model (LLaVa-1.5-13B) scoring 1.8%.  
  
**Why this matters - when does a test** _**actually**_**correlate to AGI?** As I was looking at the REBUS problems in the paper I found myself getting a bit embarrassed because some of them are quite hard. Now, confession time - when I was in college I had a couple of friends who would sit around doing cryptic crosswords for fun. I basically thought my friends were aliens - I never really was able to wrap my head around anything beyond the extremely easy cryptic crossword problems. REBUS problems feel a bit like that.   
Which makes me wonder… are REBUS problems actually a useful proxy test for a general visual-language intelligence? Of course they aren't going to tell the whole story, but perhaps solving REBUS stuff (with associated careful vetting of dataset and an avoidance of too much few-shot prompting) will actually correlate to meaningful generalization in models? Let's check back in a while when models are getting 80% plus and we can ask ourselves how general we think they are.  
**Read more** : [REBUS: A Robust Evaluation Benchmark of Understanding Symbols (arXiv)](https://arxiv.org/abs/2401.05604).  
**Get the[REBUS dataset](https://github.com/cvndsh/rebus)**[ here (GitHub)](https://github.com/cvndsh/rebus).  
  
***  
  
 **Chinese researchers train and release a really good LLaMa-style language model:  
**_…DeepSeek models get similar performance to LLaMa 70B - with even better performance in Chinese…  
_ Researchers with DeepSeek AI, [a Chinese AGI company](https://www.deepseek.com/), have created a family of large language models with performance claimed to rival ChatGPT 3.5. They've also released two small (~7B parameter) variations of their models.   
  
**Model details:** The DeepSeek models are trained on a 2 trillion token dataset (split across mostly Chinese and English). The models are roughly based on Facebook's LLaMa family of models, though they've replaced the cosine learning rate scheduler with a multi-step learning rate scheduler.   
**Instruction tuning:** To improve the performance of the model, they collect around 1.5 million instruction data conversations for supervised fine-tuning, "covering a wide range of helpfulness and harmlessness topics". Of the helpful data, ~31.2% is for general language tasks, ~46.6% for mathematical problem solving, and ~22.2% for coding exercises.   
The safety data covers "various sensitive topics" (and because this is a Chinese company, some of that will be aligning the model with the preferences of the CCP/Xi Jingping - [don't ask about Tiananmen!](https://twitter.com/jackclarkSF/status/1746254732388409589)).   
**DPO:** They further train the model using the Direct Preference Optimization (DPO) algorithm. "We found out that DPO can strengthen the model’s open-ended generation skill, while engendering little difference in performance among standard benchmarks," they write.  
  
**How good are the models? Pretty good:** They train two types of model, a 7B and a 67B, then they compare performance with the 7B and 70B LLaMa2 models from Facebook. In tests, the 67B model beats the LLaMa2 model on the majority of its tests in English and (unsurprisingly) all of the tests in Chinese. In further tests, it comes a distant second to GPT4 on the LeetCode, Hungarian Exam, and IFEval tests (though does better than a variety of other Chinese models).  
  
**Why this matters - language models are a broadly disseminated and understood technology:** Papers like this show how language models are a class of AI system that is very well understood at this point - there are now numerous teams in countries around the world who have shown themselves able to do end-to-end development of a non-trivial system, from dataset gathering through to architecture design and subsequent human calibration.   
**Read more:** [DeepSeek LLM: Scaling Open-Source Language Models with Longtermism (arXiv)](https://arxiv.org/abs/2401.02954).  
**Get 7B versions of the models here:** [DeepSeek (DeepSeek, GitHub)](https://github.com/deepseek-ai/DeepSeek-LLM#3-evaluation-results).  
**Play around with the model here** : [DeepSeek.com](http://deepseek.com).  
  
***  
  
 **Today’s language models can already automate some of science:  
**_…BIOPROT shows today’s LLMs can do basic lab protocol design and generation…  
_ Researchers with Align to Innovate, the Francis Crick Institute, Future House, and the University of Oxford have built a dataset to test how well language models can write biological protocols - “accurate step-by-step instructions on how to complete an experiment to accomplish a specific goal”. In tests, they find that language models like GPT 3.5 and 4 are already able to build reasonable biological protocols, representing further evidence that today’s AI systems have the ability to meaningfully automate and accelerate scientific experimentation.   
  
**What they built - BIOPROT:** The researchers developed “an automated approach to evaluating the ability of a language model to write biological protocols“. They do this by building BIOPROT, a dataset of publicly available biological laboratory protocols containing instructions in free text as well as protocol-specific pseudocode. “Each protocol consists of (i) a title, (ii) a description, and (iii) step-by-step instructions.”. BIOPROT contains 100 protocols with an average number of 12.5 steps per protocol, with each protocol consisting of around 641 tokens (very roughly, 400-500 words).  
“We use GPT-4 to automatically convert a written protocol into pseudocode using a protocolspecific set of pseudofunctions that is generated by the model. Here, a “teacher” model generates the admissible action set and correct answer in terms of step-by-step pseudocode. Having access to this privileged information, we can then evaluate the performance of a “student”, that has to solve the task from scratch…our approach allows us to automatically convert the process of writing a scientific protocol into a series of multiple-choice questions (i.e., pick a pseudofunction from a provided set), which can be evaluated much more robustly than natural language generation“.  
  
**Real world test:** They tested out GPT 3.5 and GPT4 and found that GPT4 - when equipped with tools like retrieval augmented knowledge generation to access documentation - succeeded and “generated two new protocols using pseudofunctions from our database. Both of these protocols were reviewed by a scientist and were determined to be accurate and sufficient for a competent lab scientist to follow“.  
  
**Why this matters - so much of the world is simpler than you think:** Some parts of science are hard, like taking a bunch of disparate ideas and coming up with an intuition for a way to fuse them to learn something new about the world. But a lot of science is relatively simple - you do a ton of experiments. Systems like BioPlanner illustrate how AI systems can contribute to the simple parts of science, holding the potential to speed up scientific discovery as a whole.  
**Read more:**[BioPlanner: Automatic Evaluation of LLMs on Protocol Planning in Biology (arXiv)](https://arxiv.org/abs/2310.10632).  
**Get the** [dataset and code here (BioPlanner, GitHub)](https://github.com/bioplanner/bioplanner).  
  
***   
  
**Dark Compute:  
**_…How much compute is out there hidden across all the world’s devices?...  
_ Think for a moment about your smart fridge, home speaker, and so on. Now imagine about how many of them there are. Many of these devices use an Arm Cortex M chip. Now, Jetpac CTO Pete Warden has done some napkin math about the total amount of potential compute represented by all these chips as very roughly 1^22 integer ops per second across 100 billion chips - “it is more than twice the number of FLOPs available through all the world’s active GPUs and TPUs”, he finds. “We have an amazing opportunity to turn all of this dead silicon into delightful experiences for users”.  
  
**Why this matters - market logic says we might do this:** If AI turns out to be the easiest way to convert compute into revenue, then market logic says that eventually we’ll start to light up all the silicon in the world - especially the ‘dead’ silicon scattered around your house today - with little AI applications. Analysis like Warden’s gives us a sense of the potential scale of this transformation.  
**Read more:** [Doom, Dark Compute, and Ai (Pete Warden’s blog)](https://petewarden.com/2024/01/05/doom-dark-compute-and-ai/).  
  
.***  
  
 **Google uses a language model to run a robot fleet:  
**_…Better data generation through an LLM dungeonmaster…  
_ Google researchers have built AutoRT, a system that uses large-scale generative models “to scale up the deployment of operational robots in completely unseen scenarios with minimal human supervision. AutoRT can be used both to gather data for tasks as well as to carry out tasks themselves.  
  
**How it works:** “AutoRT leverages vision-language models (VLMs) for scene understanding and grounding, and further uses large language models (LLMs) for proposing diverse and novel instructions to be performed by a fleet of robots,” the authors write. “At the core of AutoRT is an large foundation model that acts as a robot orchestrator, prescribing appropriate tasks to one or more robots in an environment based on the user’s prompt and environmental affordances (“task proposals”) discovered from visual observations.   
In other words, you take a bunch of robots (here, some relatively simple Google bots with a manipulator arm and eyes and mobility) and give them access to a giant model. The model can ask the robots to carry out tasks and they use onboard systems and software (e.g, local cameras and object detectors and movement policies) to help them do this. You can also use the model to automatically task the robots to gather data, which is most of what Google did here.   
  
**Testing:** Google tested out the system over the course of 7 months across 4 office buildings and with a fleet of at times 20 concurrently controlled robots - this yielded “a collection of 77,000 real-world robotic trials with both teleoperation and autonomous execution“. The resulting dataset is more diverse than datasets generated in more fixed environments. "The type of data collected by AutoRT tends to be highly diverse, leading to fewer samples per task and lots of variety in scenes and object configurations," Google writes.   
  
**Why this matters - speeding up the AI production function with a big model:** AutoRT shows how we can take the dividends of a fast-moving part of AI (generative models) and use these to speed up development of a comparatively slower moving part of AI (smart robots). Systems like AutoRT tell us that in the future we'll not only use generative models to directly control things, but also to generate data for the things they cannot yet control.   
**Read the blog:** [Shaping the future of advanced robotics (DeepMind)](https://deepmind.google/discover/blog/shaping-the-future-of-advanced-robotics/).  
**Read the research paper** : [AUTORT: EMBODIED FOUNDATION MODELS FOR LARGE SCALE ORCHESTRATION OF ROBOTIC AGENTS (GitHub, PDF)](https://auto-rt.github.io/static/pdf/AutoRT.pdf).  
  
***  
  
 **Tech Tales:  
  
The AI Credit Score  
** _[Wikipedia, accessed 2027]  
  
_ The AI Credit Score (AIS) was first introduced in 2026 after a series of incidents in which AI systems were discovered to have compounded certain crimes, acts of civil disobedience, and terrorist attacks and attempts thereof. The AIS was an extension of earlier 'Know Your Customer' (KYC) rules that had been applied to AI providers. Where KYC rules targeted users that were businesses (e.g, those provisioning access to an AI service via AI or renting the requisite hardware to develop their own AI service), the AIS targeted users that were _consumers_.   
  
The AIS links to identity systems tied to user profiles on major internet platforms such as Facebook, Google, Microsoft, and others. To access an internet-served AI system, a user must either log-in via one of these platforms _or_ associate their details with an account on one of these platforms. This then associates their activity on the AI service with their named account on one of these services and allows for the transmission of query and usage pattern data between services, making the converged AIS possible.   
  
The AIS, much like credit scores in the US, is calculated using a variety of algorithmic factors linked to: query safety, patterns of fraudulent or criminal behavior, trends in usage over time, compliance with state and federal regulations about 'Safe Usage Standards', and a variety of other factors. Analysis and maintenance of the AIS scoring systems is administered by the Department of Homeland Security (DHS). DHS has special authorities to transmit information relating to individual or group AIS account activity to, reportedly, the FBI, the CIA, the NSA, the State Department, the Department of Justice, the Department of Health and Human Services, and more.   
The AIS is part of a series of mutual recognition regimes with other regulatory authorities around the world, most notably the European Commision. There are also agreements relating to foreign intelligence and criminal enforcement access, including data sharing treaties with 'Five Eyes', as well as Interpol.   
  
 _Controversy:  
  
_ The initial rollout of the AIS was marked by controversy, with various civil rights groups bringing legal cases seeking to establish the right by citizens to anonymously access AI systems. Ultimately, the supreme court ruled that the AIS was constitutional as using AI systems anonymously did not represent a prerequisite for being able to access and exercise constitutional rights.   
Additional controversies centered on the perceived regulatory capture of AIS - though most of the large-scale AI providers protested it in public, various commentators noted that the AIS would place a significant cost burden on anyone wishing to offer AI services, thus enshrining various existing businesses.   
  
 _Notable AIS failures  
  
_ Since implementation, there have been numerous cases of the AIS failing to support its supposed mission. These include:

  * **Terrorists linked to the Magreb Separatists gained** _**higher**_**AIS scores** through careful querying about chemistry with the purported purpose of offering tuition to disadvantaged communities. Such AIS-linked accounts were subsequently found to have used the access they gained through their ratings to derive knowledge necessary to the production of chemical and biological weapons. 

  * **NYU professor Dr David Farnhaus had tenure revoked** following their AIS account being reported to the FBI for suspected child abuse. It was subsequently found that Dr. Farnhaus had been conducting anthropological analysis of pedophile traditions in a variety of foreign cultures and queries made to an undisclosed AI system had triggered flags on his AIS-linked profile. 

  * **Reported discrimination against certain American dialects** ; various groups have reported that negative changes in AIS appear to be correlated to the use of vernacular and this is especially pronounced in Black and Latino communities, with numerous documented cases of benign query patterns leading to reduced AIS and therefore corresponding reductions in access to powerful AI services.




_Rumored AIS expansion program:  
  
_ There has been recent movement by American legislators towards closing perceived gaps in AIS - most notably, various bills seek to mandate AIS compliance on a per-device basis as well as per-account, where the ability to access devices capable of running or training AI systems will require an AIS account to be associated with the device. These bills have received significant pushback with critics saying this would represent an unprecedented level of government surveillance on individuals, and would involve citizens being treated as 'guilty until proven innocent' rather than 'innocent until proven guilty'. Analogs have been drawn to the '[Clipper chip](https://en.wikipedia.org/wiki/Clipper_chip)' controversy of the 1990s.  
  
Most arguments in favor of AIS extension rely on public safety. Critics have pointed to a lack of provable incidents where public safety has been compromised through a lack of AIS scoring or controls on personal devices. Legislators have claimed that they have received intelligence briefings which indicate otherwise; such briefings have remanded classified despite increasing public pressure.   
  
**Things that inspired this story:** Thinking about AI policy and the inherent tension between certain notions of public safety and broader notions of liberty and free expression; thinking about how regulations always layer on top of one another like a kind of cancerous silt building towards ghastly outcomes; Clipper chips; trust & safety enforcement as a form of moral hegemony; distributed AI training and inference; open source models and the perceived challenges they post to policy; various legislative packages targeting AI ranging from licensing schemes to liability regimes.
