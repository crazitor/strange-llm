---
title: "Import AI 391: China's amazing open weight LLM; Fields Medalists VS AI Progress; wisdom and intelligence"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-391-chinas-amazing-open"
---

_Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this, please subscribe._

**The world's most capable open weight model is now made in China:  
**_…Tencent's new Hunyuan model is a MoE triumph, and by some measures is world class…  
_ The world's best open weight model might now be Chinese - that's the takeaway from a recent Tencent paper that introduces Hunyuan-Large, a MoE model with 389 billion parameters (52 billion activated). In a broad range of benchmarks Hunyuan outperforms Facebook's LLaMa-3.1 405B parameter model, which is widely thought to be the world's current best open weight model. "Hunyuan-Large is capable of handling various tasks including commonsense understanding, question answering, mathematics reasoning, coding, and aggregated tasks, achieving the overall best performance among existing open-source similar-scale LLMs," the Tencent researchers write.   
  
**What they did:** There isn't too much mystery here - the authors gathered a large (undisclosed) dataset of books, code, webpages, and so on, then also built a synthetic data generation pipeline to augment this. They used Rotary Position Embeddings (RoPE) for position learning and SwiGLU for activation. They also did a scaling law study of smaller models to help them figure out the exact mix of compute and parameters and data for their final run; ""we meticulously trained a series of MoE models, spanning from 10 M to 1B activation parameters, utilizing 100B tokens of pre-training data. By leveraging the isoFLOPs curve, we determined the optimal number of active parameters and training data volume within a restricted compute budget, adjusted according to the actual training token batch size, through an exploration of these models across data sizes ranging from 10B to 100B tokens," they wrote.   
  
**It does extremely well:** The resulting model performs very competitively against LLaMa 3.1-405B, beating it on tasks like MMLU (language understanding and reasoning), big bench hard (a suite of challenging tasks), and GSM8K and MATH (math understanding). However, LLaMa-3.1 405B still has an edge on a couple of hard frontier benchmarks like MMLU-Pro and ARC-C.   
Caveats: From eyeballing the scores the model seems extremely competitive with LLaMa 3.1 and may in some areas exceed it. But there's really no substitute for talking to the model itself and doing some compare and contrasts. Also, Chinese labs have sometimes been known to juice their evals where things that look promising on the page turn out to be terrible in reality.   
However, the whole paper, scores, and approach seems generally quite measured and sensible, so I think this would be a legitimate model.   
  
**Why this matters - competency is everywhere, it's just compute that matters:** This paper seems generally very competent and sensible. The only key differentiator between this system and one trained in the West is compute - on the scaling law graph this model seems to come in somewhere between 10^24 and 10^25 flops of compute, whereas many Western frontier models are now sitting at between 10^25 and 10^26 flops. I think if this team of Tencent researchers had access to equivalent compute as Western counterparts then this wouldn't just be a world class open weight model - it might be competitive with the far more experience proprietary models made by Anthropic, OpenAI, and so on.  
**Read more:** [Hunyuan-Large: An Open-Source MoE Model with 52 Billion Activated Parameters by Tencent (arXiv)](https://arxiv.org/abs/2411.02265).  
  
***  
  
 **Can 60 very talented mathematicians make a benchmark that withstands AI progress?  
**_…The best LLMs get 2% on FrontierMath today, but for how long?...  
_ Epoch AI, a research organization dedicated to tracking AI progress, has built FrontierMath, an extremely challenging mathematical understanding benchmark. FrontierMath was built in partnership with 60 skilled mathematicians "including professors, IMO question writers, and Fields medalists". To translate this into normal-speak; the Basketball equivalent of FrontierMath would be a basketball-competency testing regime designed by Michael Jordan, Kobe Bryant, and a bunch of NBA All-Stars, because AIs have got _so good at playing basketball that only NBA All-Stars can judge their performance effectively.  
_**This is also a very neat illustration of how advanced AI systems have become.** Grade School math benchmarks? Obliterated. Undergraduate math tests? Broadly solved. Graduate-level math evals? Teetering on the precipice. International Math Olympiad Gold medal? Just about to be breached based on stuff like AlphaGeometry. The fact that AI systems have become so advanced that the best way to infer progress is to build stuff like this should make us all stand up and pay attention. (And remember, this is happening in physics, chemistry, coding, and many other domains. The world is being irrevocably changed by the arrival of thinking machines and we now need the best minds in the world to figure out how to test this stuff. It's crazy!)   
  
**What FrontierMath contains:** FrontierMath contains questions in number theory, combinatorics, group theory and generalization, probability theory and stochastic processes, and more. Fields Medallist winner Terence Tao says the questions are "extremely challenging… I think they will resit AIs for several years at least". To calibrate yourself take a read of the appendix in the paper introducing the benchmark and study some sample questions - I predict fewer than 1% of the readers of this newsletter will even have a good notion of where to start on answering this stuff. "These problems span major branches of modern mathematics—from computational number theory to abstract algebraic geometry—and typically require hours or days for expert mathematicians to solve," the authors write.   
"[The questions I looked at] were all not really in my area and all looked like things I had no idea how to solve…they appear to be at a different level of difficulty from IMO problems.” — Timothy Gowers, Fields Medal (1998)", said when looking at some of the papers.   
  
**The bar is set at 2%** : In tests, GPT 4o and Sonnet 3.5 both get around 2% on the benchmark - and they're given every possible advantage to help them crunch the literal numbers: "Our evaluation framework grants models ample thinking time and the ability to experiment and iterate. Models interact with a Python environment where they can write and execute code to test hypotheses, verify intermediate results, and refine their approaches based on immediate feedback."  
  
**Why this matters - will this stand the test of time or fade like so many others?** So many recent benchmarks have fallen to the march of AI systems that many people who have built 'hard' benchmarks have quickly become quite shocked by the pace of progress on them (see: BigBench, MMLU, MATH, GPQA). The authors of FrontierMath are more optimistic - and it seems like they should be, judged by how much effort they've put in, and FIelds' Medallists agree: "Chen and Tao both suggested that human experts working with AI systems could potentially tackle FrontierMath problems within around three years, much sooner than fully autonomous AI solutions."  
**My prediction:** An AI system working on its own will get 80% on FrontierMath by 2028. And if I'm right… is that AGI? Or like so many other benchmarks before it, will solving this incredibly hard test reveal another wrinkle in the subtle beauty that is our consciousness?  
**Read more** : [FrontierMath (Epoch AI)](https://epochai.org/frontiermath).  
**Read the research paper:** [FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI (arXiv)](https://arxiv.org/abs/2411.04872).   
  
***  
  
 **Researchers say the path to wise AIs runs through metacognition:  
**_…Sure, AI is intelligent. But it isn't wise - and that's a problem…  
_ Today's AI systems are very capable, but they aren't very good at dealing with intractable problems. To solve this, they need wisdom. And to gain wisdom, they need metacognition. That's the thesis of a new paper from researchers with the University of Waterloo, Warwick University, Stanford University, the Allen Institute for AI, the Santa Fe Institute, and the Max Planck Institutes for Human Development and Intelligent Systems.   
  
**What wisdom is and why it's needed:** "We define wisdom functionally as the ability to successfully navigate intractable problems— those that do not lend themselves to analytic techniques due to unlearnable probability distributions or incommensurable values," the researchers write. "If life were a series of textbook problems, we would not need to be wise."  
  
**What are intractable problems?** The kind of things that challenge today's AI systems have the following properties:

  * **Incommensurable** : They have ambiguous goals or values that can't be reconciled with one another.

  * **Transformative:** The outcome might change your preferences, so your present and future values clash. 

  * **Radically uncertain:** You can't list all the outcomes or assign probabilities. 

  * **Chaotic:** There could be a strong nonlinearity or other feature that makes it very unpredictable.

  * **Non-stationary:** The underlying thing you're dealing with may be changing over time, making it hard for you to learn a probability distribution. 

  * **Out-of-distribution:** A black swan situation you've never encountered before. 

  * **Computationally explosive:** You can't figure out the correct move with achievable finite resources. 




**Solving intractable problems requires metacognition:** The main claim here is that the path to solving these problems runs through 'metacognition', which is basically a suite of helper functions an AI system might use to help it fruitfully apply its intelligence to so-called intractable problems. These metacognitive processes include: 

  * **Intellectual humility:** The ability to know what you do and don't know. 

  * **Epistemic deference:** Ability to defer to others' expertise when appropriate. 

  * **Scenario flexibility:** Figuring out diverse ways in which a scenario could unfold. 

  * **Context adaptability:** Figuring out features from an intractable situation that makes it comparable to other situations. 

  * **Perspective seeking:** Being able to draw on other perspectives to gain information to solve a problem.

  * **Viewpoint balancing:** Being able to integrate various discrepant interests into a single thing.




**How metacognition leads to wisdom:** The authors believe systems with these properties might be significantly better than those without. "For example, a wise AI system might be more willing to spin its wheels to solve a problem compared to a wise human; it might generate vast numbers of scenarios to analyze many possible contingencies, evincing an extreme version of scenario flexibility," they write.   
  
**Why this matters - is metacognition just LLMs + RL?** An extremely persistent thought I had while reading this paper was… isn't this just what the new crop of RL-infused LLMs give you? Some of the new models, like OpenAI's o1 model, exhibit some of the traits described here where, upon encountering confusing or hard to parse scenarios, they think out loud to themselves for a while, simulating multiple distinct perspectives, performing rollouts, running their own live experiments, and so on. While this LLM + RL paradigm doesn't deal with _all_ the stuff outlined here, it certainly seems to take a meaningful step closer.   
**When reading this paper I had the distinct feeling that it might soon be 'overtaken by reality',** like so many thoughtful papers published about the supposed gulf between today's AI systems and truly smart ones. Perhaps the age of wise AI systems is nearly upon us.  
Read more: [Imagining and building wise machines: The centrality of AI metacognition (arXiv)](https://arxiv.org/abs/2411.02478)..  
  
***  
  
 **AI consciousness is something AI companies need to think about:  
**_…We should take seriously a "realistic possibility" of conscious systems soon…  
_ A group of researchers thinks there is a "realistic possibility" that AI systems could soon be conscious and that AI companies need to take action today to prepare for this. The researchers - who come from Eleous AI (a nonprofit research organization oriented around AI welfare), New York University, University of Oxford, Stanford University, and the London School of Economics - published their claim in a recent paper, noting that "there is a realistic possibility that some AI systems will be conscious and/or robustly agentic, and thus morally significant, in the near future".  
  
**Why are they making this claim?** As contemporary AI systems have got more capable, more and more researchers have started confronting the problem of what happens if they keep getting better - might they eventually become conscious entities which we have a duty of care to? Though you may have an instinctive 'no, that's ridiculous' reaction to this idea, it's worth challenging your own assumptions - a good survey paper in 2023 looked across all the different technical means by which AI systems are built and used this to determine it's hard to _rule out_ the possibility of consciousness in contemporary AI systems ([Import AI #338](https://jack-clark.net/2023/08/28/import-ai-338-consciousness-and-ai-self-improving-language-models-maps-of-thought/)). In 2024, researchers - including a Turing Award winner - made an even more forthright claim, writing in a preprint that "AI consciousness is inevitable" and walking through the arguments for this ([Import AI #369](https://jack-clark.net/2024/04/15/import-ai-369-conscious-machines-are-possible-ai-agents-the-varied-uses-of-synthetic-data/)).  
  
**Different routes to moral patienthood:** The researchers see two distinct routes AI systems could take to becoming moral patients worthy of our care and attention: consciousness and agency (the two of which are likely going to be intertwined). 

  * "**Consciousness route to moral patienthood**. There is a realistic, non-negligible possibility that: 1. Normative: Consciousness suffices for moral patienthood, and 2. Descriptive: There are computational features — like a global workspace, higher-order representations, or an attention schema — that both: a. Suffice for consciousness, and b. Will exist in some near-future AI systems".

  * "**Robust agency route to moral patienthood**. There is a realistic, non-negligible possibility that: 1. Normative: Robust agency suffices for moral patienthood, and 2. Descriptive: There are computational features — like certain forms of planning, reasoning, or action-selection — that both: a. Suffice for robust agency, and b. Will exist in some near-future AI systems."




**What should AI companies do?** The researchers urge AI companies to take three distinct types of actions in response to the issue of AI consciousness, specifically AI companies should:

  * **Acknowledge:** "that AI welfare is an important and difficult issue, and that there is a realistic, non-negligible chance that some AI systems will be welfare subjects and moral patients in the near future". When doing this, companies should try to communicate with probabilistic estimates, solicit external input, and maintain commitments to AI safety. 

  * **Assess** : "Develop a framework for estimating the probability that particular AI systems are welfare subjects and moral patients, and that particular policies are good or bad for them," they write. These assessments should include "sources of evidence that make sense for AI systems, such as architectural features; on theories of consciousness that make sense for AI systems, such as computational functionalist theories; and on sources of moral patienthood that make sense in this context, such as various kinds of robust agency."

  * **Prepare: "** Develop policies and procedures that will allow AI companies to treat potentially morally significant AI systems with an appropriate level of moral concern," they write. As part of this, they recommend AI companies hire or appoint someone responsible for AI welfare. 




**Why this matters - if AI systems keep getting better then we'll have to confront this issue:** The goal of many companies at the frontier is to build artificial general intelligence. This goal holds within itself the implicit assumption that a sufficiently smart AI will have some notion of self and some level of self-awareness - the generality many envisage is bound up in agency and agency is bound up in some level of situational awareness and situational awareness tends to imply a separation between "I" and the world, and thus consciousness may be a 'natural dividend' of making increasingly smart systems.   
**Companies must equip themselves to confront this possibility:** "We are not arguing that near-future AI systems will, in fact, be moral patients, nor are we making recommendations that depend on that conclusion," the authors write. "We are instead arguing that near-future AI systems have a _realistic chance_ of being moral patients given the information and arguments currently available, and we are making recommendations that depend on _that_ conclusion — recommendations that focus on aspiring to learn more while preparing for the possible emergence of AI moral patienthood as a precautionary measure."  
(Incidentally, one of the authors of the paper recently joined Anthropic to work on this precise question…)   
**Read more** : [New report: Taking AI Welfare Seriously (Eleos AI Blog)](https://eleosai.org/post/taking-ai-welfare-seriously/).  
**Read the paper:** [Taking AI Welfare Seriously (Eleos, PDF)](https://eleosai.org/papers/20241030_Taking_AI_Welfare_Seriously_web.pdf).  
  
***

 **Tech Tales:  
  
Adverts after the uplift  
** _[Online machine-authored adverts posted three years after beginning of superintelligence-driven uplift]  
  
Are You (Uniquely) Experienced? Cash available.   
_We pay same day cash for provably unique experiences - simply walk in, let us validate by comparing your experiences against the memoryweb, and then we'll pay YOU for your memory. Not only that, but we will QUADRUPLE payments for memories that you allow us to delete from your own experience - a popular option for nightmares!   
  
 _Pilot-curious? Enquire within.  
_ Have you been wondering what it would be like to be piloted by a high-dimensional intelligence? Interested in learning about what opportunities this presents? We offer a range of pilot options and compensation structures. Come in for a free consultation today!  
  
**Things that inspired this story:** Thinking about the sorts of ways machines and humans might trade with one another; the Craigslist economy in a superintelligence future; economic stratification.

_Thanks for reading!_
