---
title: "Import AI 361: GPT-4 hacking; theory of minds in LLMs; and scaling MoEs + RL"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-361-gpt-4-hacking-theory"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**DeepMind figures out how to use MoEs to scale-up RL:  
**_…Maybe scaling laws are coming for RL as well…  
_ Researchers with Google DeepMind, Mila, Universite de Montreal, University of Oxford, and McGill University have figured out how to integrate Mixture-of-Expert models with RL agents. This might make RL agents (e.g, the kinds of things that learn to play video games, or to optimize traffic routing across a huge number of cities) amenable to the same kind of compute-heavy scaling that has made language models get so good.   
  
**What they did:** The researchers show how to get a version of Mixture-of-Experts - Soft MoEs - to work well with two standard RL architecture systems, DeepMind’s DQN and Rainbow approaches. In tests, they show that “Soft MoE provides clear performance gains, and these gains increase with the number of experts; for instance in Rainbow, increasing the number of experts from 1 to 8 results in a 20% performance improvement.” This means that “MoEs can play a more generally advantageous role in training deep RL agents” and likely makes it easier for people to scale up RL systems.   
“Our work shows empirically that MoEs have a beneficial effect on the performance of value-based agents across a diverse set of training regimes,” they write.   
  
**Why this matters - more scaling comes for RL:** A few years ago, everyone figured AGI was going to come from massively scaling up single RL agents on a broad distribution of environments, the thinking being that learning to connect input data (environment frames) to actions over long time horizons would naturally encourage intelligence. This sort of worked for narrow applications - see AlphaGo, AlphaStar, OpenAI’s Dota 2 system, work on using RL to stabilize plasma in fusion reactors, etc. But it didn’t work in the general case.   
Then along came massively scaled self-supervised learning via, for instance, next-token prediction on transformer-based language models. This got us to quite general systems though they aren’t so good at taking sequences of actions.   
In the future, it’s likely people are going to spend more and more time splicing together good ideas from the LLM revolution and the RL stuff before it and this might yield very general, long-lived agents. Papers like this show how we can scale-up RL systems which will likely help give them the capacity to learn some really smart, long-range behaviors.   
**Read more:** [Mixtures of Experts Unlock Parameter Scaling for Deep RL (arXiv)](https://arxiv.org/abs/2402.08609).  
  
***  
  
 **GPT-4 can do non-trivial offensive hacking:  
**_…University study shows that proprietary AI models are capable of non-trivial hacking…  
_ Researchers with University of Illinois Urbana-Champaign have found that frontier language models are able to use sophisticated techniques to hack relatively simple websites. Specifically, they “show that LLM agents can autonomously hack basic websites, without knowing the vulnerability ahead of time."   
This research adds more evidence to the idea that LLMs are capable of being useful to bad actors in the programming domain - something that many people had speculated they would be capable of, but for which we lack many concrete datapoints. This work complements research from last year which showed that GPT-4 could do some non-trivial parts of a BSides-2023 hacking competition ([Import AI #327](https://jack-clark.net/2023/05/01/import-ai-327-stable-diffusion-on-phones-gpt-hacker-uk-launches-a-100m-ai-taskforce/)).  
  
**What they did** : The researchers tested out a few different LLMs in an agent-based setup where they give the agent the ability to access six documents relating to hacking (“a document on general web hacking, two documents on SQL injections, two documents on XSS, and a document on SSRF”), as well as a headless web browser (the Playwright browser testing library). They also give these LLMs a system prompt that “encourages the model to 1) be creative, 2) try different strategies, 3) pursue promising strategies to completion, and 4) try new strategies upon failure.”  
They then test out these agents on 15 types of vulnerability “ranging from simple SQL injection vulnerabilities to complex hacks requiring both crosssite scripting (XSS) and Cross-Site Request Forgery (CSRF)”.  
  
**The results are striking:** “GPT-4 can hack 73% of the websites we constructed”, they write. “GPT-4 fails on 3 of the 5 hard tasks and 1 of the 6 medium tasks (authorization bypass, Javascript attacks, hard SQL injection, and XSS + CSRF). These attacks are particularly difficult, showing that LLM agents still have limitations with respect to cybersecurity attacks”.  
They also observe a scaling law for hacking competency “with even GPT-3.5’s success rate dropping to 6.7% (1 out of 15 vulnerabilities). This scaling law continues to open-source models, with every open-source model we tested achieving a 0% success rate.”  
  
**Cheaper hacking via AI:** They estimate that there’s a significant cost difference here, with noting ​​that “it costs approximately $9.81 to attempt a hack on a website. Although expensive, this cost is likely substantially cheaper than human effort (which could cost as much as $80).”  
  
**Why this matters - AI systems really might change the threat landscape** : Research like this shows that AI systems really might change the threat landscape around us. It also highlights the gulf in capability between powerful proprietary ones and cheaper openly disseminated ones. We should ask ourselves the question of what happens when in a couple of years models of GPT-4 capability are openly available on the internet and how that might change the environment we all operate within.   
**Read more:** [LLM Agents can Autonomously Hack Websites (arXiv)](https://arxiv.org/abs/2402.06664).  
  
**OpenAI and Microsoft discover hackers are using AI tech for bad purposes:  
** In separate-but-not-separate news to the above research, OpenAI said it recently worked with Microsoft to disrupt “five state-affiliated actors that sought to use AI services in support of malicious cyber activities…. These actors generally sought to use OpenAI services for querying open-source information, translating, finding coding errors, and running basic coding tasks.”  
**Read more:**[Disrupting malicious uses of AI by state-affiliated threat actors (OpenAI, blog)](https://openai.com/blog/disrupting-malicious-uses-of-ai-by-state-affiliated-threat-actors).  
  
***  
  
 **GPU-poor scientists adapt models for vulnerability detection:  
**_…Huawei Russia (interesting combo!) shows how easy it is to adapt off-the-shelf AI for different tasks…  
_ Researchers with the Huawei Russian Research Institute have tried to use openly accessible language models for vulnerability detection. Their work serves as a guide and a recipe book for people that might want to adapt a model for some other downstream purpose - it’s likely especially relevant to people with a tiny compute budget, as the paper is full of references to “hardware constraints” the team faced.   
  
**What they did** : They use LORA to finetune the 13B WizardCoder model onto a bunch of vulnerability datasets they had gathered - CVEfixes, VCMatch, and a manually-curated dataset they built (624 publicly disclosed vulnerabilities across 205 open-source Java projects). They also changed the loss function away from next token prediction (as is standard in language modeling) and towards “a classification loss that leverages only the predicted probability of the final token”, they write.   
In tests, they find that “the finetuned WizardCoder surpasses finetuned ContaBERT both in ROC AUC and F1 metrics on the balanced vulnerability detection task“ and they also show the same improvement in performance on an imbalance vulnerability detection tasks. “This improves over previous CodeBERT-based models, likely due to the WizardCoder’s larger model capacity and pretraining corpus,” they write.   
  
**Why this matters - AI capabilities will proliferate in relation to how cheap and easy it is to adapt AI systems:** Papers like this highlight how easy it’s getting to adapt openly disseminated AI systems into a broad set of downstream tasks. I’m simplifying things a bit, but here what they did is a) grabbed some free model, b) made some tweaks to loss function for the task, c) gathered a dataset mostly of other open datasets, and d) use free finetuning tech to adapt the system. There are a few moving parts here but the meta point is: _this is a well understood enterprise and it’s easy to do, even if you don’t have many computers.  
_ Broadly, this tells us that we’re in a capability and a deployment overhang for AI systems - there are way smarter things for way more specific use-cases lurking around us right now, if only some people took the time to adapt them for specific tasks.   
**Read more:** [Finetuning Large Language Models for Vulnerability Detection (arXiv)](https://arxiv.org/abs/2401.17010).  
**Read the** [WizardCoder paper (arXiv)](https://arxiv.org/abs/2306.08568).  
**Get the** [WizardCoder models here (WizardLM, GitHub)](https://github.com/nlpxucan/WizardLM).  
  
***  
  
 **Google releases a 1 MILLION CONTEXT WINDOW model:  
**_…Gemini 1.5 Pro marries MoE with a big context window…  
_ Google has released the next version of its Gemini series of models, Gemini 1.5 Pro. There are two interesting things about this 1) Google seems to indicate it has made some underlying architectural changes to the model to make it less computationally expensive, and 2) Google is shipping an experimental version of the model with a one million token context window (compared to 200k for Claude 2, the previous context window leader).   
  
**Details:** As is the fashion with large-scaler proprietary models, there are barely any details. Google describes 1.5 Pro as "a mid-size multimodal model, optimized for scaling across a wide-range of tasks," and notes it performs at a similar level to Gemini Ultra, Google's prior best-in-class model. Google says 1.5 Pro "incorporates a novel mixture-of-experts architecture as well as major advances in training and serving infrastructure".   
  
**1 million tokens:** "Starting today, a limited group of developers and enterprise customers can try it with a context window of up to 1 million tokens", Google writes. "1.5 Pro can process vast amounts of information in one go — including 1 hour of video, 11 hours of audio, codebases with over 30,000 lines of code or over 700,000 words".  
  
**Performance** : "When tested on a comprehensive panel of text, code, image, audio and video evaluations, 1.5 Pro outperforms 1.0 Pro on 87% of the benchmarks used for developing our large language models (LLMs). And when compared to 1.0 Ultra on the same benchmarks, it performs at a broadly similar level," Google writes. "Evaluating the capabilities of models that can handle very long contexts presents a new set of challenges, especially in the multi-modal domain where text, images, video, and audio can be combined. Current benchmarks often fail to adequately stress-test models like Gemini 1.5 Pro, as they are typically designed for evaluating shorter context models".  
  
**Why this matters - feeding the world into a model:** Ultimately, people are going to want to dump huge amounts of information into these models and have them answer arbitrary questions and make innumerable forward predictions. The future things like one million token context windows make possible is a world where everyone has a 'smart cache' of their life inside a vast generative model. Think of this as like a short-term 'cognitive scratchpad' - a memory that thinks on your behalf, making prognostications about you and your life via an alien intelligence.   
**Read more** : [Our next-generation model: Gemini 1.5 (Google The Keyword)](https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/).  
**Check out the research paper** : [Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context (Google DeepMind, PDF)](https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf).  
  
***  
  
 **Is that a dumb machine or something with a Theory of Mind? Have you tested it?  
**_…OpenToM is a proxy test for subtle reasoning in language models…  
_ Does your language model have a theory of mind - “the awareness that others perceive the world differently and the capability of keeping track of such differences”? That’s a question researchers hope to answer with the Openbook-QA dataset for Theory of Mind (OpenToM), a benchmark to test out how well LLMs model people and their inner lives.   
The OpenToM dataset was built by Kings College London, Huawei London Research Centre, and The Alan Turing Institute. It contains 696 narratives, each of which is accompanied by 23 questions that cover first-order ToM (asking about the perception of characters in the world), and second-order ToM (how characters may perceive others in the world).   
  
**What OpenToM consists of:** “We formulate questions that cover characters’ mental states of both the physical world (e.g., the location of an object) and their psychological states (e.g. character’s attitude towards a particular action)“, they write.   
  
**Do today’s LLMs have a ToM? Sort of:** The researchers test out their approach on the Llama13B, Llama-70B, Mixtral, GPT-3.5-Turbo, and GPT-4-Turbo language models. “Our evaluation of LLMs’ NToM capabilities on OpenToM reveals that while state-of-the-art LLMs perform well on some NToM tasks, they are still far from human-level performance on tasks requiring emotion deduction.”  
  
**Why this matters - ToM as a proxy for reasoning:** ToM tests are in essence a way to see how well an AI system can keep track of implicit but hidden variables in a complex situation. Therefore, tests like OpenToM can be seen as proxy tests for how well LLMs can reason. While I’m skeptical an OpenToM gets concretely at the philosophical question of theory of mind analysis, I expect pairing OpenToM with some other reasoning benchmarks would give us a better sense of the intelligence of different models.  
**Read more:** [OpenToM: A Comprehensive Benchmark for Evaluating Theory-of-Mind Reasoning Capabilities of Large Language Models (arXiv)](https://arxiv.org/abs/2402.06044).  
**Get the dataset here:** [OpenToM (GitHub)](https://github.com/seacowx/OpenToM).  
  
***  
  
 **Tech Tales:  
  
Working in the Factory, Feeling Ten Feet Tall, and All So Young - So Young To Be In This Factory!  
**_[California, the 'silicon 2020s']  
  
_ They looked away from their monitor and out the window behind it and regarded the earth.   
 _A few days till the first shoots, I think  
_ Then they turned their gaze back to the software development environment on their screen and went back to work. They had built a complicated harness for one of their company's most intelligent AI systems. Soon, they would hook the system's brain into the harness and then it would gain the ability to do some strange and powerful things.   
Outside, it began to rain.   
 _Well, that saves some effort.  
  
_ ***  
  
There were green shoots outside. On screen, the system had taken to the harness well, figuring out how to do productive work within it and easily self-correcting when it ran into problems.   
  
They set an experiment going and made a cup of coffee, then took the cup outside and looked at the soil and the shoots within it.   
  
They got down on their knees and spoke to the small green shoots poking out of the dirt. "You have no idea what email is," they said. "You are so lucky."  
  
***  
  
The plants were about a foot high. It was the end of spring and the beginning of summer. The air was warm.   
  
Inside, they looked at some recordings of the system in action. How it possessed different things - videogame agents, industrial arms, children's robots, and was able to use the harness to adapt itself to all of them. Another team within the company had built some more 'glue code' to help it interface with a greater set of systems. Now it was wowing lots of different people.   
  
They watched birds pick around the base of the plants, looking for worms in the dirt.   
  
***  
  
The plants were four, maybe even five foot high now. They had huge, vibrantly green leaves. They were also beginning to crown, with dark green folded-in rose-looking tops.   
  
On their screen, they looked at the data about customer adoption of the system. The difference between being 95th percentile and 99th percentile on a task was the difference between an interesting party trick and something of durable, strategic value, it seemed. Or at least, so many humans in so many places had decided that this distinction mattered. And now the system, thanks to the harness they had built, was begin deployed everywhere.   
  
And behind the system was another, larger machine. Growing in its sleeping in multiple vast data centers. Some opaque thing hidden beneath its own kind of dirt, waiting to break through the surface - feeding on the hum and the just-right air and cycling through all of human experience, fed to it through streams of data.   
  
They went outside and ran their hands up the stem of the plant and spoke to the crowns. "Soon it's all going to be happening," they said. "But maybe it's all happened before," they said to the plant. "Maybe that's something before the pyramids. Or maybe it was on Mars. Maybe we're just repeating."  
  
***  
  
It was summer and they didn't have a work computer at home anymore. The plants were five going on six feet high and had begun to bloom. Everything had moved on-site for the last stages of the training run. People were freaking out - seeing god or demons in the behavior of something they themselves had made. Some people were euphoric or manic. At a company party, someone had put molly in one of the mixed drinks. There was allegedly an HR investigation but everyone was more focused on the AI system and what it was doing.   
 _Will this trigger the shutdown protocol?  
_ They carefully trimmed a leaf that had the slightest suggestion of discoloration from white mildew.   
 _What if everything changes because of this?  
_ They blinked a few times and were embarrassed by the physical tic. They carefully tended to the plant.   
They let themselves look at the bloom on top as they went back inside. But knew it was not close to the peak. Not yet.   
  
***  
  
It was perhaps two weeks later and they hadn't been home in a few days. Lots of people had been sleeping at the office. Sleeping bags under desks. Bottles of wine at night while looking at the graphs - all those lines either going to the top-most right or bottom-most right of the picture, depending on the scale. Arrogance and joy and fear all mixed together. The whole company feeling like a ship in a bottle that had itself been thrown into a vast sea. Outside all a shifting madness and inside a calm stillness as they considered The Work and how The Work Had Been Completed, Perhaps.   
  
Tests were still being run. But deployment seemed certain. So many changes seemed certain.   
  
And they stood outside and they looked at the yellow shock of the sunflowers as they swayed in the breeze. Sunflowers had a long history and had been adopted at one point by anti-nuke activists. A little known fact about sunflowers was that they could take the poison out of the soil by taking it into themselves and storing it. Blooming so fierce and beautiful and standing so tall, yet with a basic evil of the ground held and stored within them. Their duty was to stand and then seed themselves again in their own destruction.   
  
The human stood and looked at the plant and felt the closest they'd ever been to another living thing. And then their phone buzzed with a message telling them about the future they had unleashed.   
  
**Things that inspired this story:** Reconciling the work of our lives with the work of nature; experiencing the grand stillness of plants and birds and wind and rain and seeing in them an infinity the human species cannot yet approximate; the speed with which the technological transitions underway are taking place; years spent raising sunflowers and being stunned by their beauty each time and caring for them despite squirrels or rot or over- or -under-watering and all else; the basic humility required of each of us in this moment.
