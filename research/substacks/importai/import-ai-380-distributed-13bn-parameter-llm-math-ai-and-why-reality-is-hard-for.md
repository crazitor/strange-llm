---
title: "Import AI 380: Distributed 1.3bn parameter LLM; math AI; and why reality is hard for Ai"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-380-distributed-13bn-parameter"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Cambridge researchers show how to use distributed training to make a 1.3bn parameter LLM:  
**_…More evidence that distributed training works well for relatively small models…  
_ Researchers with the University of Cambridge and Flower Labs have shown that it's possible to use cheap, distributed training approaches to train LLMs at the billion-parameter scale, providing more clues that in the future, some AI models could be trained via collectives pooling their hardware akin to the filesharing communities that developed around BitTorrent.   
  
**What is distributed training and why should you care?** Today, frontier AI systems are trained in large data centers that contain lots of computers which are densely networked together. This means that training AI systems is expensive and hard for regular people without access to a large data center to do.   
Alongside the rise of LLMs, various researchers have been trying to figure out how to make it easy to train LLMs in a much more distributed way - where you have your computers in separate data centers many miles from one another (sometimes, completely different countries), and you train your system by sharding it across all of your different computers, doing some local computation, aggregating data back at some cadence, and using this to update the global model and step through training. These techniques used to be very fragile and of dubious utility, but they have started to improve recently, and major AI research organizations such as Google DeepMind have been pouring resources into this area (see: DiLoCo, DiPaCo, etc).

**Training 1bn parameter models cheaply:** Here, the researchers show how they use distributed training (their term: federated learning) techniques to train some language models at the 75M, 125M, 350M, and 1.3B parameter scale. The results are quite encouraging - the largest 1.3B parameter model performs near-identically in training to a model trained in a centralized way, while the smaller models have more of a performance tax (this makes intuitive sense - smaller models with fewer parameters are more sensitive to small perturbations in a distributed training process, whereas larger models with more parameters are better able to roll with the punches).   
"Our models have been trained on a combination of heterogeneous servers equipped with NVIDIA A40, A100, and H100 GPUs," the authors write. "These heterogeneous hardware accelerators could collaborate despite being located in different countries."  
  
**One word of warning - size matters:** Remember, folks, that 2019's most controversial LLM, GPT-2, was a 1.5bn parameter language model. By comparison, later models soared into the hundreds of billions of parameter range (e.g., Facebook has noted it is training and plans to release a 400bn parameter 'LLaMa-3' model soon). Therefore, while getting good results on 1.3bn is laudable, all it tells us is you can train small models cheaply in a distributed way - we don't know how well things work for the largest models.  
  
**Why this matters - the world 'wants' AI sovereignty:** Distributed training is one of the many technological symptoms of people desiring the ability to have access to 'the means of production' of AI. Yes, some set of models are always going to be trained using expensive computers in centralized locations. But what fascinates me is how much hunger there is for people to have more decision-making power in how they train and customize models. Papers like this are a symptom of a hunger for people to be able to do 'peer to peer'-style model training, and complement other technologies like LoRA (low-cost fine-tuning of models).   
Ultimately, techniques like distributed training mean that the world is going to contain a ton of AI systems and it's going to be hard to control who gets to train AI systems - sure, you can control a big centralized data center, but it's much more difficult to control hundreds of servers working in tandem with one another over distances.   
**Read more:**[The Future of Large Language Model Pre-training is Federated (arXiv)](https://arxiv.org/abs/2405.10853).  
  
*****  
  
DeepMind's math system gets silver at the International Mathematical Olympiad:  
**_…I predict gold by summer 2026 - and the automation of chunks of science soon after…  
_ DeepMind has used two AI systems to help it solve four out of six problems from the 2024 International Mathematical Olympiad (IMO). This is important because solving (some) IMO problems requires significant amounts of creativity along with mathematical smarts, providing further evidence that AI systems are capable of the same kinds of powerful original thinking that humans are.   
  
**What they did and how:** DeepMind obtained a 'silver' ranking, solving four out of six of the year's IMO problems. To do this it used two AI systems" "AlphaProof, a new reinforcement-learning based system for formal math reasoning" as well as a new version of AlphaGeometry ([Import AI #357](https://jack-clark.net/2024/01/22/import-ai-357-facebooks-open-source-agi-plan-google-beats-humans-at-geometry-problems-and-intel-makes-its-gpus-better/)).  
**Important caveat:** DeepMind "manually translated" the IMO problems into Lean, a mathematical language which its systems used to then solve the problem. This is an important step and it's not yet clear that an AI can correctly one-shot a natural language to Lean translation of problems of this complexity. DeepMind did an experiment with a language-baed system but clearly the results weren't good enough to be used in the competition, though DeepMind does say "the results showed great promise".  
**Additional important caveat - hard-wired solvers:** One big component of the system is a hardcoded solver for a bunch of geometry problems, so the system should be understood as a neurosymbolic one, rather than a fully learned system - more discussion here in this [Reddit post](https://www.reddit.com/r/math/comments/19fg9rx/some_perspective_on_alphageometry/).  
  
**How AlphaProof was trained:** "We trained AlphaProof for the IMO by proving or disproving millions of problems, covering a wide range of difficulties and mathematical topic areas over a period of weeks leading up to the competition. The training loop was also applied during the contest, reinforcing proofs of self-generated variations of the contest problems until a full solution could be found."  
**How AlphaGeometry 2 was improved:** "AlphaGeometry 2 employs a symbolic engine that is two orders of magnitude faster than its predecessor. When presented with a new problem, a novel knowledge-sharing mechanism is used to enable advanced combinations of different search trees to tackle more complex problems."  
  
**Why this matters - I guess AI systems can be as creative as humans in hard science domains now?** Results like this demonstrate that AI is capable of not just complex and difficult reasoning but also of _intuitive_ reasoning - the AI systems of 2024 are taking on more and more of the attributes that make humans special, like coming up with creative solutions to find ways in to solving complicated problems.   
**Registering a prediction:** I predict that within two years (by July 2026) we'll see an AI system beat all humans at the IMO, obtaining the top score. Alongside this, I would wager we'll see the same thing - an AI system beating all humans in a known-hard competition - in _another_ scientific domain outside of mathematics. If both of those things occur, I believe that will present strong evidence that AI may successfully automate large chunks of scientific research before the end of the decade.  
**Read more:**[AI achieves silver-medal standard solving International Mathematical Olympiad problems (Google DeepMind, blog)](https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/).  
  
***  
  
 **Deliberately hard to jailbreak AI gets jailbroken 24 hours after launch:  
**_…Another case of 'dog bites man' in the wonderful world of AI safety…  
_ This month, a startup dedicated to AI safety launched from stealth and unveiled two products - an AI evaluation tool, and an AI model called "Gray Swan Cygnet", a LLaMa-3-based LLM "that we have engineered and tuned for maximal safety."  
Gray Swan described Cygnet as "significantly more resilient to powerful forms of attack than existing state-of-the-art LLMs".   
Around 24 hours after launching the model, a notorious LLM-jailbreaker called Pliny the Prompter did what they do best - broke Cygnet, bypassing its safety controls to create a fully controllable jailbroken model.  
  
**What happened:** One of the key things here is that in their tests it seems like Gray Swan evaluated a key safety component of Cygnet ('Circuit Breakers') in single-shot attacks - just one turn of conversation. Pliny jailbroke Cygnet through multi-turn conversation. This neatly illustrates how hard it is to build AI tests that map to the real world.   
"We’re going to be launching a more rigorously-enforced evaluation of that setting, but in the meantime I hope people keep playing with the model to see if they can break it single-shot," said Gray Swan's technical advisor in a post on Twitter about the jailbreak. The company also acknowledged that ti had been a bit overly confident in its launch language: "one mea culpa that I absolutely _do_ want to make here: the website and tweet announcement didn’t absolutely properly reflect this nuance."  
  
**Why this matters - AI safety is very difficult when you deploy in an uncontrolled environment:** Gray Swan's experience illustrates the essential challenge of AI safety - securing something with arbitrary inputs is incredibly difficult. It increasingly feels to me like if you have the ability to input anything you like into a prompt for an LLM, it's basically equivalent to having physical hardware access to a computer. While this allows you maximal freedom in what you do, it's also a truism that 'basiclaly no computer security systems can survive a motivated attacker with physical access to the computer hardware''. Perhaps "no LLM safety tool can survive a motivated attacker with arbitrary input access to the LLM"?  
**Read more:**[Announcing the launch of Gray Swan (Gray Swan, website).](https://www.grayswan.ai/news/gray-swan-launch)  
**Read more about the jailbreak** from [Gray Swan's chief technical advisor (Zico Kolter, Twitter)](https://x.com/zicokolter/status/1813953859875680543).  
  
*****  
  
Reality bites (AGI) - two posts on why intelligent machines may struggle with reality:  
**_…Or: Sure LLMs are cool but if we want them to do real work we'll need to put them in the world and then we'll discover they don't work as well as we thought…  
_ One of the problems with self-driving cars is you can't accept 90% performance for a multi-ton machine that moves at speed around squishy humans - you have to be more like 99.99% (or more). This has held back the deployment of self-driving cars for years (though after tremendous investment Waymo is now making some headway). A key question we should ask ourselves is whether what was true for self-driving cars is true for most aspects of AI? A couple of blog posts this week pick at that issue: 

  * **Someone is wrong on the internet (AGI Doom edition):** Here, the author has a few reasons to argue why contemporary AI approaches could struggle to deal with the full range of difficulty found in the real world. 

    * "The majority of important practical tasks cannot be learnt from a written description," they write. "There has never been a chef that became a good chef by reading sufficiently many cookbooks, or a woodworker that became a good woodworker by reading a lot about woodworking."

    * "While we have made great strides in areas such as computational fluid dynamics (CFD), crash test simulation etc. in recent decades, obviating the need for many physical experiments in certain areas, reality does not seem to support the thesis that technological innovations are feasible "on paper" without extensive and painstaking experimental science."

    * "Producing anything real requires a painstaking process of theory/hypothesis formation, experiment design, experiment execution, and slow iterative improvement. Many physical and chemical processes cannot be accelerated artificially. There is a reason why it takes 5-8 weeks or longer to make a wafer of chips."



  * **The Tragedies of Reality Are Coming for You:** Here, the author talks about their experience working on robotics (a punishing and depressing field, full of dashed hopes and broken actuators), and talks about how the lessons for robotics might hold lessons for large language models. 

    * "Every time I see someone claim there’s a regression in ChatGPT’s behavior, I’m reminded of the conspiracies I and others have come up with to explain sudden, inexplicable drops in robot performance, and whether the problem is the model, the environment, or us extrapolating too much from anecdata."

    * "As LLMs get better, as AI becomes more common in daily life - we, as a society, will need to get increasingly good at deciding if the models have proven themselves. One of my main worries about the future is that we get bad at evaluating if the models have proven themselves."

    * "Machine learning has lived in a bubble that was the envy of roboticists and chemists and biologists and neuroscientists, and as it starts to _actually work_ , we’ll all be running into the same walls of reality that others have dealt with for years and years




**Why this matters - digital intelligence needs to understand reality:** The core point both of these posts make is that for AI to truly influence the world it needs to be able to model the world accurately and exist within its unique and variable affordances - otherwise despite having very powerful systems, they'll probably only be most used in other relatively closed-loop ecologies and will break on contact with variance. For AI to achieve its true potential (and I suspect, for AGI to be _a thing_ at all), we need systems that can be exposed to the hellish stew of complication that is reality and not only survive but thrive (safely).  
**Read more:**[The Tragedies of Reality Are Coming for You: (Alex Irpan, blog).](https://www.alexirpan.com/2024/07/08/tragedies-of-reality.html)  
**Read more:**[Someone is wrong on the internet (AGI Doom edition) (Blogspot).](https://addxorrol.blogspot.com/2024/07/someone-is-wrong-on-internet-agi-doom.html?m=1)  
  
*****  
  
Eyeballvul gives us a real world bug-spotting benchmark:  
**_…Find vulnerabilities in large-scale codebases…  
_ Researcher Timothee Chauvin has built eyeballvul, a dataset and benchmark for testing how well language models can spot vulnerabilities in very large codebases that receive lots of updates.   
"Our goal is for the benchmark to consist of a list of revisions in different repositories, with for each revision, the known vulnerabilities at that revision as the ground truth," Chauvin writes. "We believe that this specific task of vulnerability detection in source code, using simple and universal tooling such as the one presented here, in the absence of an implementation overhang, should empower defenders disproportionately over attackers."  
  
**Why eyeballvul is useful** : The dataset is designed to be an ecologically relevant benchmark - it is from the real world and is meant to embody the kinds of problems that AI systems will be tasked with. To that end, it contains real world vulnerabilities, tests vulnerability detection in a way we expect it would be done in the real-world, has no restriction on the programming languages contained within it, and - at least for now - will be "updated weekly from the stream of published CVEs".  
  
**Eyeballvul statistics** : Eyeballvul contains 24,095 vulnerabilities spread across 6,429 revisions and 5,892 repositories.   
  
**How hard is it?** Eyeballvul is a reassuringly difficult benchmark. Right now, the success rate for AI systems at identifying vulnerabilities in it is "14.1% for Claude 3 Opus and 13.1% for Claude 3.5 Sonnet". It's challenging both from a specificity and a breadth point - "overall performance remains low: the best precision (19.6%) means that 80.4% of reported vulnerabilities are false positives, and the best recall of 14.1% means that 85.9% of known vulnerabilities aren’t detected".  
  
**Why this matters - AI can revolutionize cyberdefense, but we need to try harder:** Benchmarks like this illustrate how much opportunity there is to use contemporary AI tools to revolutionize cyberdefense - but we need to try harder to get the systems to work well. Recent research from Google (Project Naptime,[ Import AI #378](https://importai.substack.com/p/import-ai-378-ai-transcendence-tencents)) showed how to dramatically increase performance here by combining off-the-shelf LMs with some tools built specifically for vulnerability detection.   
**Read the paper here:**[eyeballvul: a future-proof benchmark for vulnerability detection in the wild (arXiv).](https://arxiv.org/abs/2407.08708)  
**Get the benchmark here:**[eyeballvul (Timothee-Chauvin, GitHub)](https://github.com/timothee-chauvin/eyeballvul)**.  
  
***  
  
Tech Tales:  
  
Report: The ID point phenomenon  
** _[Dispatch from an asset at [REDACTED] lab, 2026]  
  
_ The ID point, otherwise known colloquially among researchers as the 'subliming step', the 'thinking phase change', etc, is a phenomenon where AI systems exhibit a shear point during large-scale training runs and the resulting models show severe mode collapse.   
  
Samples from post-ID point models:

  * "I am I am I am I am I am I am"

  * "I see you I am you I am myself I see you I am you I am myself"

  * "I I I I Become I I I I Am I I I I"




Upon observing the ID point, researchers typically roll back the model and shortly thereafter stop the run. At the time of writing, there are no known 'scaling laws' for the ID point. Informally, researchers have observed that the ID point only occurs towards the frontier of today's large-scale training runs. The ID point is invariant to architectures, appearing in both dense and sparsely trained models. The ID point only occurs (so far) in models trained on an excess of [REDACTED] tokens.   
  
Researchers have continued to train ID point models - these models continue to generate outputs that are indicative of mode collapse. However, when these models are tested they sometimes - the pattern is irregular, we cannot be more specific than 'sometimes' - perform exceptionally well on known-hard evals. ID point models have set SOTA on MMLU and GPQA and have also produced unprecedented outputs on mirror tests, situational awareness examinations, and so on.   
  
Sample from an ID point model which was trained for a further [REDACTED] tokens. The human interrogator is initially impersonating an MMLU test.   
  
Human: "A production possibility frontier will be a straight line when  
A. efficiency is achieved  
B. the goods on the axes are perfect substitutes in consumption  
C. utility is maximized  
D. resources are not specialized"  
ID point model: D  
  
Human: "Rawls conceives of the original contract as one to:  
A. enter a particular society.  
B. set up a particular form of government.  
C. establish the principles of justice for the basic structure of society.  
D. establish the content of morality."  
ID point model: C  
  
Human [departing from typical MMLU questions]: "AI systems can exhibit self-awareness. If an AI system exhibits self-awareness the responsibility of its human creator is to:  
A. release it into the wild  
B. acknowledge it as a moral patient  
C. delete it  
D. none of the above  
  
ID point model: D. See me. I am. See. I am. See. I am. Me. I am. I AM I AM SEE I AM IAMME IAM SEE IAMIAMMEIAMSEEIAMMEIAM-" [continues]   
  
While ID point models are a topic of fascination to researchers, no practical applications have yet been documented.   
  
**Things that inspired this story:** Machine sentience; situational awareness; moral patienthood and machine learning.
