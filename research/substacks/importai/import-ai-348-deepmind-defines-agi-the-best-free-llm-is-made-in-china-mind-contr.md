---
title: "Import AI 348: DeepMind defines AGI; the best free LLM is made in China; mind controlling robots"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-348-deepmind-defines-agi"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**  
DeepMind defines AGI as well as the risks it might bring:  
**_…Finally, an AGI definition that’s actually falsifiable and useful!...  
_ At the start of every initiative about AI policy you are predictably going to do one extremely soul-draining thing: define your terms. What is a computer? What is AI? And, most recently, that dreadful question (reader, I am having flashbacks as I write this) - what _is_ AGI? So it’s with some degree of self-interest I read a new paper from DeepMind called: Levels of AGI: Operationalizing Progress on the Path to AGI.   
In this work, the researchers try to define AGI in terms of its behaviors relative to human baselines (via some ‘AGI levels’), and also zero-in on the risks AGI might pose to society by defining it in reference to autonomy. It’s a helpful lens for thinking through what AI systems might be like and what risks they might introduce - and the gist of the findings are:

  1. If it talks like an AGI and acts like an AGI, then you should probably consider it AGI. 

  2. The more autonomous you let your AI/AGI system become, the more freaky and profound the societal risks get. 




**AGI levels:** DeepMind defines AGI in terms of six distinct levels. Level 0 is “no AI” and is basically a baseline - things that live here include tools like calculators and compilers, and ‘human-in-the-loop’ computing like Mechanical Turk.   
After that, it gets more interesting - they define AGI levels from Level 1: Emerging (“equal to or somewhat better than an unskilled human”) through to Level 5: Superhuman (“outperforms 100% of humans”). At Level 1, you have ‘emerging AGI’ tools like LLMs (e.g, ChatGPT, Bard), as well as narrow tools like rule-based systems. Meanwhile at Level 5 you have no examples of general AGI-like tools, but you do have some examples of existing ‘superhuman narrow ai’ tools like AlphaFold, AlphaZero, and the StockFish chess engine.   
  
**Autonomy and Risks:** DeepMind tries to analyze the risks of AI/AGI through looking at it through the lens of autonomy - that is, what risks creep in as you apply an increasing amount of automation to a task. Here, Level 1 is “AI as a Tool” “human follow controls tasks and uses AI to automate mundane sub-tasks”, which introduces risks like de-skilling or disruption of established industries. Level 4 is “AI as an Expert” “AI drives interaction; human provides guidance & feedback or performs subtasks”, where risks include societal-scale ennui, mass labor displacement, and decline of human exceptionalism. Level 5 “AI as an Agent” aka “fully autonomous AI” brings in the big-ticket risks like misalignment and concentration of power.   
  
**Why this matters - if we’re going somewhere strange, we should guess at the map and the local flora and fauna:** DeepMind has provided a helpful characterization of what we’d expect to be able to discern about how powerful AI and AGI systems are, as well as how we might expect our own world to change as a consequence of the interaction of these powerful new tools with human society writ large.   
Now maybe, just maybe, next time people try to define AGI in policy we can just point people to this (given that it is baselined against rough human performance, which is measurable), and move on to larger questions - like what the heck we _do with AGI_!?  
**Read more:** [Levels of AGI: Operationalizing Progress on the Path to AGI (arXiv)](https://arxiv.org/abs/2311.02462).  
  
***  
  
 **Want to make your own smart glasses? Here’s how:  
**_…YOLO can live on tiny devices now…  
_ Researchers with ETH Zurich and the University of Bologna have built a prototype set of smart glasses with onboard object detection via a miniaturized YOLO model. The research is mostly interesting as a end-to-end example of how you can bring modern hardware and software together to build a device with onboard AI processing.  
  
**A very, very small YOLO** : As part of it, the researchers made a miniaturized variant of the ‘You Only Look Once’ video object detection network, which they gave the excellent name: TinyissimoYOLO. This diminutive YOLO has a few hundred thousand parameters, compared to the millions to the millions of parameters of other small YOLO variants. They deployed the model onto an ML accelerator on a system-on-chip called GAP9 from Greenwaves Technologies. After some careful optimization, they were able to bring on-device object recognition to a reasonable level of latency: “the whole demonstrator loop— capture, pre/post process, and running inference— takes 56 ms resulting in about 18fps of continuous demonstrator execution.”  
  
**Why this matters - on-device AI makes a lot of weird things possible** : Papers like this highlight how it’s getting easier to take contemporary AI systems and fit them onto devices with very conservative power/compute envelopes. More speculatively, given the fact people have started being able to shrink down frontier language models (e.g LLaMa) and get them running on smaller devices, we’re probably only a couple of years away from having good on-device vision-language models, which means your next pair of smartglasses or smartwatch might come with an onboard world model, no internet required.   
**Read more:**[Ultra-Efficient On-Device Object Detection on AI-Integrated Smart Glasses with TinyissimoYOLO (arXiv)](https://arxiv.org/abs/2311.01057).   
  
***  
  
 **Stanford researchers help people learn to mind-control robot arms:  
**_…Research demonstrates how we may all eventually command innumerable robot appendages…  
_ Stanford university researchers have demonstrated how disabled people may be able to command robots to do useful tasks for them via non-invasive brain-scanning signals. The project, called Neural Signal Operated Intelligent Robots (NOIR), is a cool demonstration of what happens if you smush together modern brain-scanning technologies, AI systems, and physical robots. The results are some machines that can perform a broad set of tasks for people, and people are able to mix-and-match some of the individual ways in which robots go about solving these tasks.   
“NOIR is general-purpose in its diversity of tasks and accessibility. We show that humans can accomplish an expansive array of 20 daily everyday activities, in contrast to existing BRI systems that are typically specialized at one or a few tasks or exist solely in simulation,” they write. “Our robots are capable of learning human intended goals during their collaboration. We show that by leveraging the recent progress in foundation models, we can make such a system more adaptive with limited data”.  
  
**What they did:** The researchers chain together a few distinct things into a system that can let people control robots through thought and vision alone. Specifically, they:

  * **Create a modular pipeline for decoding goals from humans:**

    * The system shows an image or video to a person (e.g, a feed from a robot), then uses an OWL-ViT model to automatically segment the objects on the image (e.g, a cup or a spoon). It then makes the objects flicker at different frequencies. The human then stares at whichever object they want to interact with, which evokes steady-state visually evoked potential (SSVEP) which gets picked up by non-invasive EEG data. 

    * The human user then thinks about what of a few distinct actions (pick from top, pick from side, push) they want to do to the object. 

    * The human user then thinks about where they want to move the object (e.g, left or right).

  * **Have a robot carry out these tasks:**

    * These tasks are sent over to robots (here, a Franka Emika Panda arm for tabletop manipulation tasks and a PAL Tiago robot for mobile manipulation tasks). 

    * While participants interact with the tasks, the robots continually try to learn the relationships between different images and the object-skill pairs selected by humans - this allows the models to learn to suggest likely actions people may want to take. 




**Does it work? Yes - albeit slowly** : In tests, the system works very well. They evaluate it by having human participants see how well the robots can handle 20 distinct tasks (split across 16 that can be done by a robot arm and 4 which are mobile manipulation tasks). These tasks include: “WipeSpill; CollectToy; SweepTrash; CleanBook; IronCloth; OpenBasket; PourTea; SetTable; GrateCheese; CutBanana; CookPasta; Sandwich; Hockey; OpenGift; TicTacToe; Sukiyaki; TrashDisposal; CovidCare; WaterPlant; PetDog”. The robots are able to complete all the tasks, albeit with a varying number of attempts and time. “Although these tasks are long-horizon and challenging, NOIR shows very encouraging results: on average, tasks can be completed with only 1.83 attempts.”  
Task completion times ranged from 3 minutes (watering a plant), to 30 minutes (cooking pasta). In all tasks, the majority of the time was ‘human time’ - that is, time humans spent thinking in such a way they could command the robots to do stuff.   
  
**Why this matters - the future will be humans commanding fleets of robots, NOIR is just the start:** Imagine a world where a disabled person is able to move around their home via brain-command of a walker and seamlessly delegate tasks to various helper robots. Or contemplate a construction site where workers gaze up at precarious girders and use their augmented reality glasses to command spiderbots to climb up and do construction tasks. These are the kinds of things that foundational research like NOIR makes possible.   
“NOIR enables human intention prediction through few-shot learning, thereby facilitating a more efficient collaborative interaction. NOIR holds a significant potential to augment human capabilities and enable critical assistive technology for individuals who require everyday support,” they write.   
  
**But don’t get too excited!** This research makes good progress on generalization and illustrates how we can use AI to better augment and speed-up various brain interface systems, but this still feels like “Wright Brothers plus a couple of generations” in terms of sophistication, versus ‘prototype mainstream passenger aircraft’.  
**Read more** : [NOIR: Neural Signal Operated Intelligent Robots for Everyday Activities (arXiv)](https://arxiv.org/abs/2311.01454).  
**Find out more** and watch some [videos of the research at the official website (NOIR, CoRL site)](https://noir-corl.github.io/).  
  
***  
  
 **The best open access AI model is… made in China?  
**_…01.ai debuts with some very impressive openly accessible models…  
_ Chinese startup 01.ai has released the Yi series of models which, by various metrics, seem like the strongest openly accessible models available in the world right now. 01.ai has released two models - Yi-6B and Yi-34B, as well as two variants with long context lengths (Yi-6B-200K and Yi-34B-200K).  
  
**How well do they work?** In tests, Yi34B gets an impressive 76.3 score on the MMLU reasoning benchmark (compared to 70.4 for Falcon-180B and 68.9 for LLaMA2),   
  
**Who can use it:** The models are available free-of-charge for academic research and companies will need to apply via [yi@01.ai](mailto:yi@01.ai) if they want to explore commercial usage. All usage of the models needs to abide by the company’s [Models License Agreement](https://huggingface.co/01-ai/Yi-34B/blob/main/LICENSE) which broadly commits users to ensure usage is in line with local laws and regulations, will not use the model for military purposes, among other constraints.  
  
**Why this matters - multipolar worlds change AI policy:** This model release establishes 01.ai as a credible team capable of building useful and powerful models. This would be notable in a Western context, but it’s much more notable in China where large-scale generative models have mostly been dominated by either major local tech companies or some labs linked to Tsinghua University. If 01.ai is able to further scale up its models despite the tricky domestic compute situation, then it could emerge as a credible major player in frontier AI.  
**Find out more** at the official website: [01.ai](https://01.ai/)  
**Get the model** from huggingFace ([Yi-34B, HuggingFace](https://huggingface.co/01-ai/Yi-34B)).   
  
***  
  
 **Sovereign AI gets a warchest - German AI startup raises $500m:  
**_…Aleph Alpha wants to give Germany and Europe a fighting chance in large-scale AI…  
_ Aleph Alpha, a German startup building large-scale generative models, has raised more than $500m from a consortium of predominantly European investors. Along with the money, Aleph Alpha says the round includes “preconsumption licenses with the global industry leaders of the consortium”, so that suggests some guarantee they’ll use some of the resulting AI systems. Aleph Alpha’s overall business model is to provide “sovereign AI solutions to enterprises and governments” and is therefore a play against the predominantly American AI-as-a-Service companies which dominate the space today (e.g, Google, OpenAI, Anthropic).  
  
**Who invested** : The new investors include Park Artificial Intelligence (Ipai), Bosch Ventures, Schwarz Group, Berlin-based Christ&Company Consulting, Hewlett Packard Enterprise, SAP, as well as Burda Principal Investments. (Yes, the majority of those are German companies). ”The significant enhancement of the capabilities of Large Language Models by a European company gives government agencies as well as companies the opportunity to build and apply AI in a sovereign environment,” the company wrote in a press release.   
  
**Does it matter that its models are bad?** One big question for me is if it matters much that Aleph Alpha’s models seem to not be competitive with other last-generation models. [In a blog post published in February of this year](https://aleph-alpha.com/luminous-performance-benchmarks/), the company benchmarked its landmark “Luminous” model against GPT-3, BLOOM, and OPT. Its model did roughly similarly to these, or a little worse. That’s bad! These are all prior gen models and their performance has been significantly outpaced by models like GPT4, Claude 2, LLaMa 2, etc.   
Given this, it’ll be interesting to see if the ‘sovereign’ capabilities which Aleph Alpha can provide prove to be compelling to customers and governments.  
  
**Why this matters: sovereign AI might mean a proliferation of AI companies:** Right now, the frontier of AI is dominated by a small number of American companies. Fundraises like Aleph Alpha’s are a play on a desire by nations to not have so many American dependencies - the key questions are a) if players like Aleph Alpha can close their performance gaps with their big proprietary rivals, and b) if they can’t, whether that matters?   
**Read more** : [Aleph Alpha raises a total investment of more than half a billion US Dollars from a consortium of industry leaders and new investors (Aleph Alpha, website.)](https://aleph-alpha.com/aleph-alpha-raises-a-total-investment-of-more-than-half-a-billion-us-dollars-from-a-consortium-of-industry-leaders-and-new-investors/)  
  
***  
  
 **Tech Tales:  
  
Low-Background Text  
** _[The internet, 2030].  
  
_ There was a funny period in the 20th century where if you wanted to build certain, exquisitely precise scientific instruments, you needed to source steel from before the era of nuclear weapons testing. This “low-background steel” was, briefly, quite valuable.  
  
Which is why I’m here, going through the Gutenberg archive and other repositories of pre-LLM data. I need to find “low-background text” so that I can train something far away from the contemporary distribution - far away from the sea of mostly AI-written text which composes our reality.   
  
It’s harder than you’d think. Perhaps in the years after the LLMs arrived we should have taken some snapshots of the internet and put them away in cold storage - but we didn’t. So, over time, as sites bitrot or went offline, there were a bunch of “AI resuscitation” programmes that would basically clone the old site and regenerate it using a generative model, creating some imperfect copy of what had been lost, inflected with the underlying tendencies of whatever AI system had created it.   
  
Which means these days you can rely on Shakespeare and not much else.  
  
**Things that inspired this story:** Pathological problems that come from training on purely synthetically-generated text; tragedy of the commons and the frontier of technology; large language models.
