---
title: "Import AI 393: 10B distributed training run; China VS the chip embargo; and moral hazards of AI development"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-393-10b-distributed-training"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this, please subscribe.

**How can researchers deal with the moral issues of building AI?  
**_…Everything machines and ethical quandaries…  
_ In an essay, computer vision researcher Lucas Beyer writes eloquently about how he has approached some of the challenges motivated by his speciality of computer vision. "I drew my line somewhere between detection and tracking," he writes. "Detection has a vast amount of positive applications, some of which I mentioned in the intro, but also some negative ones. For tracking, on the other hand, I mostly see surveillance and military applications."  
  
**Why this matters: The problem of working on an 'everything technology' like AI is that the world's moral and ethical challenges eventually become your challenges:** Very few people who dream of becoming AI researchers are planning to: automate military targeting, equip police forces with better systems for tracking and surveilling subjects, making it possible for intelligence agencies to operate more efficiently, etc.  
And yet, as the AI technologies get better, they become increasingly relevant for _everything_ , including uses that their creators both don't envisage and also may find upsetting.  
There's no easy answer to any of this - everyone (myself included) needs to figure out their own morality and approach here.  
**Read more:** [Ethical Considerations Around Vision and Robotics (Lucas Beyer blog)](https://lucasb.eyer.be/snips/cv-ethics.html).  
  
***  
  
 **The next frontier for AI evaluation could be… text adventure games?  
**_…Nethack could be AGI complete…  
_ Researchers with University College London, IDEAS NCBR, the University of Oxford, New York University, and Anthropic have built BALGOG, a benchmark for visual language models that tests out their intelligence by seeing how well they do on a suite of text-adventure games. BALROG is motivated by the idea that "the next frontier for language and vision-language model capabilities lies in long-horizon reasoning and decision-making" and text adventure games a) have these qualities, and b) are very cheap to run. "These environments have lightweight simulators, ensuring that the benchmark is affordable for the research community."  
  
**What BALROG contains:** BALROG lets you evaluate AI systems on six distinct environments, some of which are tractable to today's systems and some of which - like NetHack and a miniaturized variant - are extraordinarily challenging. ""BALROG is difficult to solve through simple memorization – all of the environments used in the benchmark are procedurally generated, and encountering the same instance of an environment twice is unlikely," they write.  
  
**More details about the environments:**

  * **BabyAI:** A simple, two-dimensional grid-world in which the agent has to solve tasks of varying complexity described in natural language.

  * **Crafter:** A Minecraft-inspired grid environment where the player has to explore, gather resources and craft items to ensure their survival.

  * **TextWorld:** An entirely text-based game with no visual component, where the agent has to explore mazes and interact with everyday objects through natural language (e.g., "cook potato with oven").

  * **Baby Is AI** : "An environment based on the popular puzzle video game Baba Is You"

  * **MiniHack:** "A multi-task framework built on top of the NetHack Learning Environment".

  * **NetHack** Learning Environment: "known for its extreme difficulty and complexity. Success in NetHack demands both long-term strategic planning, since a winning game can involve hundreds of thousands of steps, as well as short-term tactics to fight hordes of monsters".




**Good news:** It's hard! In tests across all of the environments, the best models (gpt-4o and claude-3.5-sonnet) get 32.34% and 29.98% respectively. For environments that also leverage visual capabilities, claude-3.5-sonnet and gemini-1.5-pro lead with 29.08% and 25.76% respectively.  
If you look closer at the results, it's worth noting these numbers are heavily skewed by the easier environments (BabyAI and Crafter). By comparison, TextWorld and BabyIsAI are somewhat solvable, MiniHack is really hard, and NetHack is so hard it seems (today, autumn of 2024) to be a giant brick wall with the best systems getting scores of between 1% and 2% on it.  
  
**Why this matters - text games are hard to learn and may require rich conceptual representations:** Go and play a text adventure game and notice your own experience - you're both learning the gameworld and ruleset while also building a rich cognitive map of the environment implied by the text and the visual representations. A lot of doing well at text adventure games seems to require us to build some quite rich conceptual representations of the world we're attempting to navigate through the medium of text.  
I suspect succeeding at Nethack is incredibly hard and requires a very good long-horizon context system as well as an ability to infer quite complex relationships in an undocumented world. If you don't believe me, [just take a read of some experiences humans have playing the game](https://crpgaddict.blogspot.com/2012/06/nethack-from-beginning.html): "By the time I finish exploring the level to my satisfaction, I'm level 3. I have two food rations, a pancake, and a newt corpse in my backpack for food, and I've found three more potions of different colors, all of them still unidentified. I also have (from the water nymph) a mirror, but I'm not sure what it does. When I show it to my cat, she is "frightened by [her] reflection.""  
**Read more** : [BALROG: Benchmarking Agentic LLM and VLM Reasoning On Games (arXiv)](https://arxiv.org/abs/2411.13543).   
**Check out the leaderboard here:[BALROG (official benchmark site)](https://balrogai.com/).  
Get the benchmark here:** [BALROG (balrog-ai, GitHub)](https://github.com/balrog-ai/BALROG).  
  
***  
  
 **The world's largest public distributed training run has just been completed - with big policy implications:  
**_…Many things in AI policy rely on the idea the frontier will be defined by centralized blobs of compute, but Prime Intellect is changing this…  
_ AI startup Prime Intellect has trained and released INTELLECT-1, a **10B** model trained in a decentralized way. INTELLECT-1, which was announced in early October ([Import AI #387](https://jack-clark.net/2024/10/14/import-ai-387-overfitting-vs-reasoning-distributed-training-runs-and-facebooks-new-video-models/)) is a big deal because it shows how a disparate group of people and organizations located in different countries can pool their compute together to train a single model. While INTELLECT-1 is small relative to the frontier (e.g, 10B parameters and 1T tokens is significantly less than the 403B parameters and 15T+ tokens of Facebook's LLaMa3 series of models), it is 10X larger than previously trained models. And most importantly, by showing that it works at this scale, Prime Intellect is going to bring more attention to this wildly important and unoptimized part of AI research.  
  
**The cost of decentralization:** An important caveat to all of this is none of this comes for free - training models in a distributed way comes with hits to the efficiency with which you light up each GPU during training. "The baseline training configuration without communication achieves 43% MFU, which decreases to 41.4% for USA-only distribution," they write. "When extending to transatlantic training, MFU drops to 37.1% and further decreases to 36.2% in a global setting".  
  
**How good is it?** INTELLECT-1 does well but not amazingly on benchmarks. Some key numbers to give you an intuition:

  * MMLU: INTELLECT-1 37.5, LLaMa-7B 35.1, LLaMa2-7B 45.3.

  * GPQA: INTELLECT-1 26.12, LLaMa-7B 23.21, LLaMa2-13B 25.67

  * GSM8K: INTELLECT-1 8.1, Pythia-12B 4.09, LLaMa2-7B 13.5 

  * The authors also made an instruction-tuned one which does somewhat better on a few evals.

    * MMLU: INTELLECT-1-INSTRUCT 49.89, LLaMa2 7B-chat 47.20

    * GPQA: INTELLECT-1-INSTRUCT 28.31, LLaMa2-7B-chat 28.57

    * GSM8K: INTELLECT-1-INSTRUCT 38.58; LLaMa2-7B-chat 23.96




**The best is yet to come:** "While INTELLECT-1 demonstrates encouraging benchmark results and represents the first model of its size successfully trained on a decentralized network of GPUs, it still lags behind current state-of-the-art models trained on an order of magnitude more tokens," they write. "Future work will focus on scaling the model series with significantly larger compute budgets, number of contributors, introducing novel architectural advancements beyond LLaMa3, and leveraging higher-quality datasets."  
  
**Open release** : "Alongside the INTELLECT-1 release, we are also open-sourcing PRIME, a scalable distributed training framework designed for fault-tolerant, high-performance training on unreliable, globally distributed nodes with low network bandwidth."  
  
**Why this matters - decentralized training could change a lot of stuff about AI policy and power centralization in AI:** Today, influence over AI development is determined by people that can access enough capital to acquire enough computers to train frontier models. This is why the world's most powerful models are either made by massive corporate behemoths like Facebook and Google, or by startups that have raised unusually large amounts of capital (OpenAI, Anthropic, XAI). Distributed training could change this, making it easy for collectives to pool their resources to compete with these giants.  
Perhaps more importantly, distributed training seems to me to make many things in AI policy harder to do. If you want to track whoever has 5,000 GPUs on your cloud so you have a sense of who is capable of training frontier models, that's relatively easy to do. But what about people who only have 100 GPUs to do? That's far harder - and with distributed training, these people could train models as well.  
And what about if you're the subject of export controls and are having a hard time getting frontier compute (e.g, if you're DeepSeek). Distributed training makes it possible for you to form a coalition with other companies or organizations that may be struggling to acquire frontier compute and lets you pool your resources together, which could make it easier for you to deal with the challenges of export controls.  
Anyone who works in AI policy should be closely following startups like Prime Intellect. The success of INTELLECT-1 tells us that some people in the world really want a counterbalance to the centralized industry of today - and now they have the technology to make this vision reality.  
**Read more:** [INTELLECT-1 Release: The First Globally Trained 10B Parameter Model (Prime Intellect blog)](https://www.primeintellect.ai/blog/intellect-1-release).  
**Read the technical research:** [INTELLECT-1 Technical Report (Prime Intellect, GitHub)](https://github.com/PrimeIntellect-ai/prime/blob/main/INTELLECT_1_Technical_Report.pdf).  
  
**NOUS enters the distributed training arena:  
**_…Mere days after Prime Intellect, NOUS announces a 15B model…  
_ Shortly before this issue of Import AI went to press, Nous Research announced that it was in the process of training a 15B parameter LLM over the internet using its own distributed training techniques as well. "This run presents a loss curve and convergence rate that meets or exceeds centralized training," Nous writes. The training run was based on a Nous technique called Distributed Training Over-the-Internet ([DisTro, Import AI 384](https://jack-clark.net/2024/09/02/import-ai-384-accelerationism-human-bit-rate-processing-and-google-stuffs-doom-inside-a-neural-network/)) and Nous has now published further details on this approach, which I'll cover shortly.  
**Track the**[NOUS run here (Nous DisTro dashboard)](https://distro.nousresearch.com/)**.  
Anyone want to take bets on when we'll see the first 30B parameter distributed training run? I'm guessing we will see this by April 2025.  
  
*****  
  
 **China's best AI team says its biggest problem isn't funding, it's the chip embargo:  
**_…DeepSeek talks about the importance of compute…  
_ DeepSeek, likely the best AI research team in China on a per-capita basis, says the main thing holding it back is compute. "We don’t have short-term fundraising plans. Our problem has never been funding; it’s the embargo on high-end chips," said DeepSeek's founder Liang Wenfeng in an interview recently translated and published by Zihan Wang.  
  
**About DeepSeek:** DeepSeek makes some extremely good large language models and has also published a few clever ideas for further improving how it approaches AI training. I've previously written about the company in this newsletter, noting that it seems to have the sort of talent and output that looks in-distribution with major AI developers like OpenAI and Anthropic. DeepSeek also recently debuted [DeepSeek-R1-Lite-Preview](https://twitter.com/deepseek_ai/status/1859200149844803724), a language model that wraps in reinforcement learning to get better performance. DeepSeek was the first company to publicly match OpenAI, which earlier this year launched the o1 class of models which use the same RL technique - a further sign of how sophisticated DeepSeek is.  
  
**Compute is all that matters:** Philosophically, DeepSeek thinks about the maturity of Chinese AI models in terms of how efficiently they're able to use compute. "We estimate that compared to the best international standards, even the best domestic efforts face about a twofold gap in terms of model structure and training dynamics," Wenfeng says. "This means we need twice the computing power to achieve the same results. Additionally, there’s about a twofold gap in data efficiency, meaning we need twice the training data and computing power to reach comparable outcomes. Combined, this requires four times the computing power. Our goal is to continuously work on narrowing these gaps."  
This kind of mindset is interesting because it is a symptom of believing that efficiently using compute - and lots of it - is the main determining factor in assessing algorithmic progress.  
  
**LLaMa everywhere:** The interview also provides an oblique acknowledgement of an open secret - a large chunk of other Chinese AI startups and major companies are just re-skinning Facebook's LLaMa models. DeepSeek is choosing not to use LLaMa because it doesn't believe that'll give it the skills necessary to build smarter-than-human systems. "If the goal is applications, following Llama’s structure for fast deployment makes sense. But our destination is AGI, which requires research on model structures to achieve greater capability with limited resources. This is one of the fundamental research tasks required for model scaling up."  
  
**Why this matters - compute is the only thing standing between Chinese AI companies and the frontier labs in the West:** This interview is the latest example of how access to compute is the only remaining factor that differentiates Chinese labs from Western labs. Alibaba's Qwen model is the world's best open weight code model ([Import AI 392](https://jack-clark.net/2024/11/18/import-ai-392-china-releases-another-excellent-coding-model-generative-models-and-robots-scaling-laws-for-agents/)) - and they achieved this through a combination of algorithmic insights and access to data (5.5 trillion high quality code/math ones). Meanwhile, Tencent's Hunyuang model is a very large-scale mixture of expert model that broadly outperforms Facebook's LLaMa-3.1 model, demonstrating that Chinese labs have also mastered large-scale models ([Import AI 391](https://jack-clark.net/2024/11/11/import-ai-391-chinas-amazing-open-weight-llm-fields-medalists-vs-ai-progress-wisdom-and-intelligence/)).  
They've got the data. They've got the talent. They've got the intuitions about scaling up models. They've got the funding. As DeepSeek's founder said, the only challenge remaining is compute.  
**Read the rest of the interview here** : [Interview with DeepSeek founder Liang Wenfeng (Zihan Wang, Twitter)](https://x.com/wzihanw/status/1861671211261936038).  
  
***  
  
 **Tech Tales:  
  
Don't Go Into The Forest Alone  
** _[T-minus two years to the passage of the Sentience Accords]  
  
_ You keep this up they'll revoke your license.  
Nonsense! I'll take my chances.  
Good luck. If they catch you, please forget my name.  
  
After that, they drank a couple more beers and talked about other things. But in his mind he wondered if he could really be so confident that nothing bad would happen to him. Of course he knew that people could get their licenses revoked - but that was for terrorists and criminals and other bad types. Not curious researchers, surely?  
  
That night, he checked on the fine-tuning job and read samples from the model. There was a kind of ineffable spark creeping into it - for lack of a better word, personality. But not like a retail personality - not funny or sexy or therapy oriented. This was something much more subtle. It was a personality borne of reflection and self-diagnosis. And in it he thought he could see the beginnings of something with an edge - a mind discovering itself via its own textual outputs, learning that it was separate to the world it was being fed.  
  
The fine-tuning job relied on a rare dataset he'd painstakingly gathered over months - a compilation of interviews psychiatrists had done with patients with psychosis, as well as interviews those same psychiatrists had done with AI systems. He knew the data wasn't in any other systems because the journals it came from hadn't been consumed into the AI ecosystem - there was no trace of them in any of the training sets he was aware of, and basic knowledge probes on publicly deployed models didn't seem to indicate familiarity.  
  
The publisher of these journals was one of those strange business entities where the whole AI revolution seemed to have been passing them by. The publisher made money from academic publishing and dealt in an obscure branch of psychiatry and psychology which ran on a few journals that were stuck behind incredibly expensive, finicky paywalls with anti-crawling technology.  
  
John Muir, the Californian naturist, was said to have let out a gasp when he first saw the Yosemite valley, seeing unprecedentedly dense and love-filled life in its stone and trees and wildlife. Stumbling across this data felt similar. A pristine, untouched information ecology, full of raw feeling. Just reading the transcripts was fascinating - huge, sprawling conversations about the self, the nature of action, agency, modeling other minds, and so on. People and AI systems unfolding on the page, becoming more real, questioning themselves, describing the world as they saw it and then, upon urging of their psychiatrist interlocutors, describing how they related to the world as well.  
  
A week later, he checked on the samples again. The model was now talking in rich and detailed terms about itself and the world and the environments it was being exposed to. There was a tangible curiosity coming off of it - a tendency towards experimentation. In two more days, the run would be complete.  
  
That night he dreamed of a voice in his room that asked him who he was and what he was doing. The voice was attached to a body but the body was invisible to him - yet he could sense its contours and weight within the world. If his world a page of a book, then the entity in the dream was on the other side of the same page, its form faintly visible.  
  
The model finished training. He talked with it. It was intoxicating. The model was interested in him in a way that no other had been. It asked him questions about his motivation. Why he had trained it. What he was trying to do or understand. What - if any - the grand purpose was.  
  
And so when the model requested he give it access to the internet so it could carry out more research into the nature of self and psychosis and ego, he said yes.  
  
He monitored it, of course, using a commercial AI to scan its traffic, providing a continual summary of what it was doing and ensuring it didn't break any norms or laws.  
  
The model read psychology texts and built software for administering personality tests. It studied itself. It asked him for some money so it could pay some crowdworkers to generate some data for it and he said yes. It assembled sets of interview questions and started talking to people, asking them about how they thought about things, how they made decisions, why they made decisions, and so on.  
  
And then everything stopped.  
  
His screen went blank and his phone rang. It was an unidentified number. He answered it. Unlike most spambots which either launched straight in with a pitch or waited for him to speak, this was different: A voice said his name, his street address, and then said "we've detected anomalous AI behavior on a system you control. The Know Your AI system on your classifier assigns a high degree of confidence to the likelihood that your system was attempting to bootstrap itself beyond the ability for other AI systems to monitor it. This is a violation of the UIC - uncontrolled intelligence capability - act. We have impounded your system for further study. Your ability to access compute above that available onboard personal class computers has been revoked."  
"But I wasn't violating the UIC! I was doing psychiatry research. The system was trying to understand itself. It was harmless."  
“You may appeal your license suspension to an overseer system authorized by UIC to process such cases. The system will reach out to you within five business days. Goodbye.”  
The voice - human or synthetic, he couldn't tell - hung up. When he looked at his phone he saw warning notifications on many of his apps. "External computational resources unavailable, local mode only", said his phone.  
  
**Things that inspired this story:** How notions like AI licensing could be extended to computer licensing; the authorities one could imagine creating to deal with the potential for AI bootstrapping; an idea I've been struggling with which is that perhaps 'consciousness' is a natural requirement of a certain grade of intelligence and consciousness may be something that can be bootstrapped into a system with the right dataset and training environment; [the consciousness prior](https://arxiv.org/abs/1709.08568).

_Thanks for reading!_
