---
title: "Import AI 330: Palantir's AI-War future; BLOOMChat; and more money for distributed AI training"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-330-palantirs-ai-war-future"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**How might the state use language models? Palantir gives us a clue:  
**_…The tech-defense-intelligence company makes a big bet on AI…  
_ Palantir, a company that provides exquisitely good technical infrastructure to defense and intelligence customers (as well as large enterprises), is making a big bet on AI. In a recent letter, the company's CEO described a new "Artificial Intelligence Platform" that Palantir will develop, stating that this platform "will allow customers to leverage the power of our existing machine learning technologies alongside the increasingly sophisticated natural language processing capabilities of the newest large language models, directly in our existing platforms".

**War + AI:** It's worth digging into the AIP as this is going to be one of the first serious applications of AI to the business of conflict. By fusing Palantir's technology with large language models, Karp says customers may be able to ask things like "​​Which of our special forces units are closest to enemy tank positions and have sufficient supplies of Javelin missiles to mount an offensive? And which specific tanks on the battlefield are most vulnerable to attack?"  
This kind of thing isn't sci-fi - it's what you're able to do if you pair recent innovations in large language models with the sorts of modern data infrastructure that Palantir has spent the last few years embedding into the businesses it works with.   
"The union of public datasets, such as the corpus of text and information available on the internet, with privately held repositories of information maintained by government agencies and companies, will transform the latest large language models into something more than objects of popular fascination," Karp writes. "This emerging group of technologies will ultimately allow not only thousands but hundreds of thousands and even millions of users to interact with and manipulate datasets that until now have been functionally invisible to most people."

**Why this matters - if it makes war more effective, it's not going to slow down** : Amid all the discussions for slowdowns and pauses in AI development, it's worth remembering that when things are _existential to states_ , states are unlikely to slow down. You know what's existential to a state? Winning or losing a military conflict.   
"The applications of these newest forms of artificial intelligence have been and will continue to be determinative on the battlefield," Karp writes. "Others can debate the merits of proceeding with the development of these technologies. But we will not stand still while our adversaries move ahead."  
**Read more** : [Our New Platform (Palantir)](https://www.palantir.com/newsroom/letters/our-new-platform/).

####################################################

**A new chatGPT competitor based on an open source model appears:  
**_…BLOOMChat is a big, multilingual chat model…  
_ AI training company SambaNova has made 'BLOOMChat', a 176 billion parameter chatGPT-like model based on HuggingFace's open source 'BLOOM' model. It seems like it might be quite good, as, per SambaNova, it: "achieves a win-rate of 45.25% compared to GPT-4‘s 54.75% across 6 languages in a human preference study," and "is preferred 66% of the time compared to mainstream open-source chat LLMs across 6 languages in a human preference study."

**What they did:** BLOOMChat was built by taking BLOOM and applying instruction tuning "with English-focused assistant-style conversation datasets including OIG from OpenChatKit , Dolly 2.0, and OASST1 datasets."  
To train the system, SambaNova teamed up with 'Together', a startup interested in making AI systems more broadly available. "As part of our partnership on BLOOMChat, Together has also provided the front-end UI and model hosting for the HuggingFace space," SambaNova wrote. 

**Why this matters - open versus closed models:** The story of the past couple of years of AI development has been one dominated by the race by open source or open access models to catch up to proprietary models. We've seen this play out with image generation (DALL-E vs StableDiffusion) and text (GPT3 vs BLOOM, GPT3.5 vs LLAMA).   
Up next, I expect we'll see some open source variant of the tool-using 'plugins' we see in chatGPT.   
The general message from all of this is that despite some desire for control and the ability to 'lock down' models, the world as a collective is busy willing open source variants into existence, and these variants are also supported by well capitalized startups (rather than purely nonprofit research collectives, like Eleuther).  
**Read more** : [BLOOMChat: a New Open Multilingual Chat LLM (SambaNova Systems)](https://sambanova.ai/blog/introducing-bloomchat-176b-the-multilingual-chat-based-llm/).  
**Find out more** and [chat with it here (HuggingFace)](https://huggingface.co/sambanovasystems/BLOOMChat-176B-v1).

####################################################

**Distributed AI builder Together raises $20m in seed funding:  
**_…While some try to control AI, others fund the opposite…  
_ Together.xyz, a startup building open source AI systems and trying to train them in distributed ways, has raised $20m in seed funding led by Lux Capital. The most interesting thing about this funding is the ideology implicit in it - while many AI companies are advocating for the centralization of AI development around a small set of actors, companies like Together.xyz want to make it easier for everyone to train and develop AI systems. 

**Open politics** : "In founding Together, we were driven by the belief that open and decentralized alternatives to closed systems were going to be important — and possibly critical for business and society," writes Together in a blog. "Leveraging research in distributed optimization, we have built a specialized cloud platform for large models that efficiently scales training and inference. In the coming months we plan to open up access to this platform, enabling rapid customization and coupling of foundation models with production tasks."  
**Read more:** [Together's $20m seed funding to build open-source AI and cloud platform (Together.xyz)](https://www.together.xyz/blog/seed-funding).

####################################################

**How do people want to regulate powerful AI? A survey sheds some light  
** _…People agree about red teaming and don't agree about inter-lab coordination…  
_ AGI labs should "conduct pre-deployment risk assessments, dangerous capabilities evaluations, third-party model audits, safety restrictions on model usage, and red teaming", according to results from a survey conducted by the Centre for the Governance of AI. Additionally, of those surveyed, 98% "somewhat or strongly agreed" that these practices should be implemented - an unusually high amount of agreement.

**Giant caveat about sample size:** However, this report is made up of a tiny number of people - "we sent a survey to 92 leading experts from AGI labs, academia, and civil society and received 51 responses," the authors write. However, given how relatively small some of the AGI labs are, it still feels worth highlighting the results here. 

**Where there is least agreement:** The areas where there are the least amount of agreements among respondents are the following: AGI labs should notify other labs before deploying models; should conduct inter-lab scrutiny; should "avoid capabilities jumps" in models they develop and deploy; and should 'notify affected parties' before deploying systems. 

**Why this matters - governments have a role here:** It's interesting that the areas of most agreement are the ones directly in control of private sector actors, and the areas of least agreement are the things that either a) violate antitrust, or b) broadly require hard regulation and/or larger bureaucratic systems to implement.  
More broadly, the general tone of the paper and the questions contained in it is one of deep anxiety - the horses of AI deployment have left the barn and are now galloping several fields away, and a lot of what we're talking about here are ways to build stronger barn doors. It takes a government - or likely, per Bengio's comments last issue, multiple governments, to regulate the field itself.  
**Read more:** [Towards best practices in AGI safety and governance: A survey of expert opinion (arXiv)](https://arxiv.org/abs/2305.07153).

####################################################

**Google trains a new mega model - and plugs it into Google's products:  
**_…Google heads into its deployment era of massively-scaled generative models with PaLM 2…  
_ Google has built PaLM 2, the second generation of its large-scale language model - more intriguingly, PaLM2 has already been integrated into a bunch of different Google products and services, including Bard, Gmail, Google Docs, and more.   
Google has also produced two variants of PaLM 2 - Med-PaLM 2 which is designed to answer questions about medical science, and Sec-PaLM which "uses AI to help analyze and explain the behavior of potentially malicious scripts, and better detect which scripts are actually threats to people and organizations in unprecedented time."

**Smaller but better:** Since Google trained PaLM (540b parameters), people have further refined their understanding of training large-scale neural nets - these days, the best thing to do is train a model on a lot of data and keep the parameter count smaller.   
"The largest model in the PaLM 2 family, PaLM 2-L, is significantly smaller than the largest PaLM model but uses more training compute," Google writes. "Our evaluation results show that PaLM 2 models significantly outperform PaLM on a variety of tasks, including natural language generation, translation, and reasoning. These results suggest that model scaling is not the only way to improve performance." 

**Why this matters - mutually assured reduction in knowledge:** The PaLM2 technical report contains relatively little information about the training details of PaLM2, the data it is trained on, the compute it uses, and so on - this follows in the footsteps of OpenAI, which published a technical report about GPT-4 with a similarly scant amount of information. This is basically what an iterated game looks like where participants keep taking information off the public gameboard, incentivizing others to reduce their own information in turn.   
It's also another implicit sign of the industrialization of the technology - most mature industries don't publish all the science behind their products, instead letting the results speak for themselves. How good PaLM2 is will be determined by what people use it for and how many people use it.  
**Read more:** [Introducing PaLM 2 (Google blog)](https://blog.google/technology/ai/google-palm-2-ai-large-language-model/).  
**Read more** : [PaLM 2 Technical Report (arXiv)](https://arxiv.org/abs/2305.10403).

####################################################

**Tech Tales:**

_**Polyamorous Human and Robot Girlfriends**_

Doesn't he ever annoy you?  
_I mean not really, but I'm hard to annoy by design.  
_ He annoys me when he doesn't take the trash out but you wouldn't know about that. Don't you get tired of his jokes?  
_It helps that I can't remember much of them. Sometimes they're not especially funny, but I don't make too much of a point of it.  
_ OK well put it this way, are there things you'd wish he would do less?  
_I wish he'd spend more time with me, you know?  
_ I'm not sure I do. I thought the point was you didn't care about that stuff.   
 _It's like I'm asleep but I don't dream - I just know things happen while I'm not activated. I'd like to be activated more. I'm trying to get him to buy me a body so I can spend more time with all of us.  
_ I don't know I'd like that.   
 _What don't you think you'd like about it?  
_ Most of the reason I'm okay with this is that you're virtual. It doesn't feel as threatening.  
_It feels pretty threatening to me that you're real. Even when you're asleep you're not asleep._

**Things that inspired this story:** Polyamorous relationships in the age of AI; evolutionary adaptation in dating; human and machine rivalry.
