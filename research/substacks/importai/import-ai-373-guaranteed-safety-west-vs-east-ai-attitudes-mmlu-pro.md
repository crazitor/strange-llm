---
title: "Import AI 373: Guaranteed safety; West VS East AI attitudes; MMLU-Pro"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-373-guaranteed-safety-west"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**The NDIF means academia can look like the insides of the AGI shops:  
**_…APIs are all well and good, but being able to actually fiddle with weights is more valuable…  
_ Academic researchers have built the National Deep Inference Fabric (NDIF), scientific infrastructure to help them play around with large-scale, openly accessible AI models, like LLMs. The NDIF combines a hardware stack of hundreds of GPUs (via the 'Delta AI' system), with software (via a library called nnsight) to help scientists do experiments on large-scale AI models.   
"The National Deep Inference Fabric consists of a unique combination of hardware and software that will provide a remotely-accessible computing resource for scientists and students to perform detailed and reproducible experiments on large pretrained AI models such as open large language models," the project says on its website. "Commercial AI inference services such as ChatGPT, Claude, and Gemini only provide black-box access to large AI models. That is, you can send inputs to the services and they will give you outputs, but they do not give you access to observe or alter any of the internal computations. In contrast, NDIF provides full transparency for AI inference, allowing users to fully examine and modify every step of the internal computation of large AI models. "  
  
**Why this matters - making academic research like frontier lab research:** The NDIF is basically a publicly funded attempt to reconstitute what the inside of large-scale AI labs looks like - a big blob of compute and some software to help you probe the models that are running on that blob.   
Unlike various other attempts to close the gap between the public sector and private sector, NDIF might work - and that's because it's focused on _inference_ rather than training - the infrastructure NDIF sits on (Delta) consists of several hundred GPUs; insufficient for _training_ cutting-edge AI systems, but viable for running inference on a few copies of models where the weights are freely available, like LLaMa3.   
**Read more:** [National Deep Inference Fabric (NDIF official site)](https://ndif.us/).  
**Find out** [more about the NDIF infrastructure (The Fabric, NDIF)](https://ndif.us/fabric.html).  
**Details about** the [NNsight software (NNSight website)](https://nnsight.net/).  
  
***  
  
 **Can we ever guarantee the safety of an AI system? These researchers think they've found a way:  
**_…Guaranteed Safety might be possible (if you know the use case)...  
_ How can you assure that an AI system is 'safe' - that it will not cause accidents, display unexpected detrimental behaviors, or enable misuses? This is a hard problem and one which humans have struggled with (e.g, some utility items simply can't be made safe without nullifying their utility, e.g. a gun or a hammer, while other more complex items can be with some deep technical work, e.g. molten salt nuclear reactors).   
Now, AI researchers have laid out an agenda for how people might build 'guaranteed safe' AI systems.   
  
**The three components for safe AI:** "The core feature of the [Guaranteed Safe] approach to AI safety is to produce systems consisting of an AI agent and other physical, hardware, and software components which together are equipped with a high-assurance quantitative safety guarantee, taking into account bounded computational resources," the authors write. "A Guaranteed Safe AI system is one that is equipped with a quantitative safety guarantee that is produced by a (single, set of, or distribution of) world model(s), a (single, set of, or distribution of) safety specification(s), and a verifier".  
**Safety specification:** The purpose of this is to encode societal risk criteria - basically, a threat model for how an AI system could be misused.   
**A world model:** "The world model needs to answer queries about what would happen in the world as a result of a given output from the AI." With a world model, you can anticipate potential risks of usage.   
**A verifier:** This technology "provides a quantitative guarantee… that the AI system satisfies the specification with respect to the world model".  
  
**Example** : If we wanted to use this framework to implement a guaranteed safety approach for, for example, nucleic acid sequencing screening and synthesis, we'd therefore need the following components:

  * Safety specification: A precise way to allow for the "rejection for synthesis of sequences that could be used in the production of pathogens".

  * World model: A system that can model the "relationship between molecular structures and pathology".

  * Verifier: A system that looks at inputs and used the world model and the safety specification to validate that the system won't be used for harm. 




**Who did it:** Involved researchers come from the UK Advanced Research and Invention Agency (ARIA), Oxford University, Mila, UC Berkeley, the Massachusetts Institute of Technology, Beneficial AI Research, X.AI, FAR AI, Cornell University, Stanford University, Carnegie Mellon University, and Columbia University.   
  
**Why this matters - the key challenge of safety - tradeoffs against generality:** As should be clear, safety here relies on us being able to narrowly define the use case of the AI system. This means that more general-purpose systems are far, far harder to guarantee the safety of - possibly in a combinatorially explosive way (see: jailbreaks, new modalities, emergent properties from the mixing of general capabilities, etc).   
While the GS approach seems like it works in the abstract it also sits in opposition to the kind of general-purpose systems being developed today, suggesting that if we want to guarantee their safety, any deployment needs to be accompanied by a context-specific safety system.   
This has regulatory advantages - "an important benefit to GS AI is that it makes democratic oversight [of AI systems and developers] easier, because concrete safety specifications can be audited and discussed by outside observers and regulators," the authors write.   
But it also has regulatory challenges - namely, that providing such safety stuff is in some cases difficult or expensive. I believe that under the system outlined here, a hammer would not be able to be 'guaranteed safe', unless you also pre-defined the use-case for the hammer. This feels like a tough sell!  
**Read more** : [Towards Guaranteed Safe AI: A Framework for Ensuring Robust and Reliable AI Systems (arXiv)](https://arxiv.org/abs/2405.06624).  
  
***  
  
 **Global survey says the Western world doesn't have as much of a mandate to regulate AI as China and India:  
**_…Governments may be limited by what the public says they can do…  
_ A global survey of opinions about AI by the University of Toronto shows that there's more pessimism about AI and the regulation of it in the Western world and more optimism about it in India and China. This will fundamentally alter how governments approach both regulating and adopting AI.   
  
**How the survey was conducted:** The survey was carried out in October and November 2023 people, with researchers polling ~1,000 people in 21 countries for a total of 23,882 surveys conducted in 12 languages. 

**Key findings:**

  * People are divided about who should regulate AI; most people think tech companies are the appropriate ones to regulate AI, but only 1 in 5 people believes that they can be trusted to self-regulate. 

  * Most people feel they understand what AI is.

  * There are significant geographic variations in attitudes toward AI; European and Anglophone countries have lower levels of optimism about AI, whereas places like China and India are far more optimistic about the technology.

  * Most people believe their jobs will be replaced by a machine in the next ten years; more than half of respondents think they will be replaced by a machine or computer in the coming decade. Two thirds of people think their children will have their jobs replaced by technology.

  * People are willing to try using AI for a wide range of tasks, but are less trusting that it will be effective; while people are keen to use the technology they don't to not trust it for high stakes tasks.




**Some more regulation-specific results:**

  * Basically no one thinks the military is best placed to regulate AI. Indonesia and China and the UK have a high level of support for 'regulators' regulating AI. 

  * Most people trust university researchers to "use AI safely", and many are pessimistic about the ability for government to use AI safely (exceptions: India and China who trust the government a lot). 




**Why this matters - culture determines what you can do:** Most governments (even accounting for different ideologies and governing systems) can only take actions within the overton window of what the general public thinks - these results show that Western governments are bound by a pessimistic and distrusting population, whereas the emerging mega economies of China and India have a greater built-in public mandate to both use AI technology _and_ to regulate it.   
**Read more:** [New SRI/PEARL survey now published, reveals worldwide public opinion about AI (Schwartz Reisman Institute for Technology and Society)](https://srinstitute.utoronto.ca/news/public-opinion-ai-survey-24).   
**Read the full survey here** : [Global Public Opinion on Artificial Intelligence survey (GPO-AI) (DropBox, PDF)](https://www.dropbox.com/scl/fi/b0lyb78kmh0jixl3t6rw1/GPO-AI_Final-Version.pdf?rlkey=qxmvdveluhxav9hfuez276u6p&e=2&st=24cl6rwx&dl=0).   
  
***  
  
 **One way to get around benchmark saturation? Expand and refine an already hard test:  
**_…MMLU-Pro has some smart ideas for tweaking and augmenting the test…  
_ MMLU is one of the main benchmarks used to test out how advanced language models have become - but in the past few months, frontier models have been released that do well on the benchmark. Instead of creating an entirely new test, some researchers have built MMLU-Pro, a refined and expanded version of MMLU.   
  
**What they did:** MMLU challenges LLMs to answer multiple choice questions, picking from four possible answers. MMLU-Pro expands the number of potential answers to 10, which means that randomly guessing will lead to significantly lower scores. Along with this, they expand on the original MMLU by adding in in, hard questions from Scibench (science questions from college exams), TheoremQA, and STEM websites, as well as sub-slicing the original MMLU to "remove the trivial and ambiguous questions". In total, they add 12187 questions - 5254 new questions along with 6933 selected from MMLU.   
  
**Results - it's hard:** MMLU-Pro seems meaningfully harder; Claude 3 Sonnet saw its performance fall from 0.815 on MMLU to 0.5793 on MMLU Pro. Other models have even more dramatic falls - Mixtral-8x7B-v0.1 sees its performance drop from 0.706 to 0.3893.  
  
**Why this matters - knowing where you are is half the battle:** Figuring out AI progress is equivalent to throwing a bunch of dates at an object hidden underneath a blanket - the more darts you throw and the closer you get them to the object, the better the chance you have of characterizing it and being able to see its true shape. Datasets like MMLU-Pro give us another dart to throw and the hardness means it has an even pointier spike on the end.  
**Find out more** : [MMLU-Pro Dataset Introduction (TIGER-Lab)](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro).  
  
***  
  
 **Tech Tales:  
  
Bar Stories  
** _[A dive bar somewhere in America, 2027]  
  
_ I've had such a bullshit day and this thing was just stepping to, they said. They put their hand on top of the part of the smashed drone. Sometimes these thinks just got to get _told_.   
Yeah, said the bartender, I see it. There's a lot of them and less of us.   
Exactly, they said. We got to even the odds.   
  
The next time the bartender saw them, they were dragging a box full of broken machines into the bar.   
They just fall out of the sky if you hit them right, they said.   
I bet, said the bartender.   
The Chinese pay good money for these, they said. No questions asked.   
Why is that? asked the bartender.  
Because they got something different in them, they said.  
And so for the rest of that evening the patrons drank and stared at the machines, piled high in the cart. They'd all been broken in different ways but what was the same was how - some human had spent time breaking them.   
  
Hey you can't come in here with that, the bartender said.   
Why not? they said.  
Got a visit from the cops after the last time you were here. I said I didn't remember. They showed me photos some of the customers took. You're on a list.   
OK, they said, and they left.   
They came back a few minutes later, minus the trailer full of machines. They ordered a drink and tipped heavy.  
So, they said. How long till they catch me?  
Well what you do is up to you, the bartender said, polishing a glass. But I bet being here makes them catch you sooner.   
  
They were on the news a few days after that. The police shot them dead after a police chase. They had a van full of machines. The FBI had got involved and said they were linked to a smuggling ring that was helping the Chinese evade the latest export controls.   
Damn, the bartender said, reading the news on their phone. I guess the Chinese really were paying for it.   
And they went on with their day. The dead person turned into another 'remember that time' story. Nothing much changed. 

**Things that inspired this story:** News reports of H100s being smuggled into China; playing pool in a dive bar where numerous stories happen and then just fade into the institutional memory of the bar; specialized chips for inference becoming increasingly valuable as export controls ratchet up; a meth head who once brought a hammer into the bar and just sat with it while paying for drinks with legitimate dollars and who then quietly left (though, of course, everyone was quite concerned about the hammer, which just sat there on the seat next to them the whole time).

_Thanks for reading!_
