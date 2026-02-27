---
title: "Import AI 366: 500bn text tokens; Facebook vs Princeton; why small government types hate the Biden EO"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-366-500bn-text-tokens-facebook"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**DROID - another huge robot dataset drops:  
**_…More and more data means more and more invention…  
_ A consortium of researchers have released the Distributed Robot Interaction Dataset (DROID), a giant dataset of an industrial robot carrying out various tasks in various settings. Datasets like DROID are meant to help researchers train large AI systems to better understand and control robots in open-ended settings like homes and offices.   
  
**DROID ingredients:** The dataset consists of 76k trajectories across 350 hours of interaction data, collected across 564 scenes, 86 tasks, and 52 buildings. DROID was collected by 18 research labs in North America, Asia, and Europe over the course of a year. All data is collected on the same robot hardware stack based on the Franka "Panda" robot arm. Collection locations include: industrial office, home kitchen, office, living room, hallway, closet, bedroom, laundry room, and more.  
Some of the tasks the robots are recorded doing include manipulating kitchen items like wafflemakers, placing apples in pots, toasting things, cleaning up desks, and more.   
  
**The full data collection setup** : "A Franka Panda 7DoF robot arm, two adjustable Zed 2 stereo cameras, a wristmounted Zed Mini stereo camera, and an Oculus Quest 2 headset with controllers for teleoperation. Everything is mounted on a portable, height-adjustable desk for quick scene changes," they write. The resulting data from the episodes consists of "three synchronized RGB camera streams, camera calibration, depth information, and natural language instructions".  
  
**Diverse data makes for better robots:** In tests, the authors find that training some diffusion models with "DROID boosts policy performance, robustness and generalizability by 20% on average over state-of-the-art approaches that leverage existing large-scale robot manipulation datasets". They figure this out by comparing training on DROID to just training on task-specific data, and training on a mix of task-specific data and data from another dataset (the Open X-Embodiment dataset).   
Additionally, they find that "using the split of the dataset with more diverse scenes yields better performance in the OOD evaluation setting" - this makes intuitive sense as the further off distribution you go the more you tend to fail, so using the most unusual parts of a dataset like DROID are likely to help with weird circumstances.   
  
**Why this matters - the evidence is mounting up of data-scaling for robotics:** DROID complements other major released datasets like the Open X-Embodiment dataset as well as proprietary ones like Google's RT-1. These datasets are all very large in scope and accompany attempts to train large-scale neural nets on the resulting datasets. In general, robotics is showing the same signs as computer vision was showing in the early 2010s - a sudden arrival of a few large-scale datasets complemented by the application (and scaling up) of relativley simple neural methods. I expect robots are going to get dramatically better counterintuitively quickly.  
**Read the research paper** : [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset (arXiv)](https://arxiv.org/abs/2403.12945).  
**Find out more at the project website:** [DROID: A Large-Scale In-the-Wild Robot Manipulation Dataset (Droid Dataset website)](https://droid-dataset.github.io/).  
  
***  
  
 **What do conservatives think about the White House's executive order on AI? They don't love it!  
**_…House oversight hearing highlights criticism of the EO…  
_ Last year, the Biden administration released a broad, sweeping Executive Order on AI. The EO tasks agencies across the government with carrying out studies and esports about AI as well as on changing how they buy it. It also takes the unusual step of seeking to gather unusual amounts of information about companies planning to train AI systems that use more than 10^26 FLOPs.   
In policy, for every action there is an equal and opposite reaction - so now we're a few months beyond it, various White House detractors have started to flesh out their criticism of the EO. To that end, the House Oversight Committee held a hearing on "White House Overreach on AI" last week. Witnesses came from the Cato Institute, R Street Institute, The Abundance Institute, and the Brookings Institution. 

**Main criticisms of the EO:**

  * Three of the four witnesses (exception: Brookings) specifically criticized the EOs use of the Defense Production Act as an example of overreach - taking a law meant to guarantee wartime production of stuff and turning it into a reporting requirement for big training runs.

  * Three of the four witnesses (exception: Brookings) took issue with the risk-motivated nature of the EO, noting that typically the US government has taken a more pro-innovation approach with new technologies. 

  * Three of the four witnesses (exception: Brookings) raised the alarm that the EO sees the US carrying out expansive regulation of the kind that is meant to be the job of Congress.

  * One witness (R Street) said the EO looks pretty different to how the US government approached internet technologies in the 1990s, where back then "we allowed new digital technologies to be “born free” and to flourish without excessive micromanagement, and then used ongoing multistakeholder efforts and flexible regulatory responses to address concerns".




**Why this matters - even though everyone knows US policy is dysfunctional, they hate people doing something about it!** The amusing and freaky thing about the criticisms is they note something true (the EO is making policy, and Congress is meant to be doing that), but they fail to note a truth that everyone knows - US policy is currently going through a dysfunctional period where passing anything of substance is a titanic battle (and mostly defined by failures).   
Therefore, a lot of the real debate underlying this hearing is basically "is doing something better than doing nothing?". People who spend a lot of time working with AI systems and staring at scaling laws tend to arrive at the point of view that there's merit to doing "something", but if you treat AI as a regular technology, you typically end up interpreting that there's no need to do anything special about it.   
The problem is, of course, that readers of this newsletter know something is happening with AI - everywhere in this newsletter I cover exponentials - exponential growths in model complexity, in data used to train the models, in money dumped into training them. And I cover the results of exponentials - surprising and deeply powerful capabilities appearing slowly then suddenly then everywhere at once. Clearly, the world of AI is changing at a breakneck pace, but how you justify that to people who don't spend all their time knee-deep in arXiv is another matter - and as this hearing illustrates, those justifications aren't seen as particularly trustworthy… at least not yet.  
**Watch the hearing and read the statements here:** [White House Overreach on AI (House Oversight website)](https://oversight.house.gov/hearing/white-house-overreach-on-ai/).  
  
***  
  
 **Want 500 billion tokens of public domain text? Use Common Corpus  
** _…However, this still falls below what is needed to train frontier AI systems…  
_ Researchers with Pleias have released Common Corpus, "the largest public domain dataset released for training LLMs." The dataset consists of ~500 billion words "from a wide diversity of cultural heritage initiatives." This includes a collection of 21 million digitized newspapers, along with tens of billions of words from French, German, Spanish, Dutch and Italian sources, as well as more data in other "low resource languages".  
  
**Why this matters - scale and the difficulties thereof:** At 500 billion words, this corpus weighs in at somewhere between 600 and 700 billion tokens. By comparison, small open source models like LLaMa2 were trained on 2 trillion tokens, and larger scale proprietary models are trained on multiples of that. That means that while Common Corpus is a laudable effort, it doesn't yet have the scale necessary to let people train language models on it alone.  
**Read more:** [Releasing Common Corpus: the largest public domain dataset for training LLMs (HuggingFace blog)](https://huggingface.co/blog/Pclanglais/common-corpus).  
**Get the[data here](https://huggingface.co/collections/PleIAs/common-corpus-65d46e3ea3980fdcd66a5613)**[ (Common Corpus, HuggingFace)](https://huggingface.co/collections/PleIAs/common-corpus-65d46e3ea3980fdcd66a5613).  
  
***  
  
 **What Facebook's versus Princeton's GPUs tell us:  
**_…300 + 350,000 = the decline of democracy…  
_ This week, Princeton announced that it was preparing to fire up a 300 NVIDIA H100 GPU cluster. In a press release, the university said the cluster "arrives at a crucial time in AI research, when industry’s massive computing resources have mostly driven the direction of AI discourse. The multimillion-dollar investment was primarily funded by the University endowment."  
If we assume an H100 costs about 30,000 (assuming some discounts), then we can napkin out Princeton's capital outlay here as about $9 million dollars.   
By comparison, Facebook said earlier this year it would have 350,000 H100 GPUs by the end of the year - that represents an outlay of about $10 billion dollars (assuming some discounts). 

**Why this matters - democracy is a choice made through funding:** At a time when training frontier models takes 10,000+ GPUs (see: ByteDance's recent paper, [#363](https://importai.substack.com/p/import-ai-363-bytedances-10k-gpu)), Princeton's cluster commits the university to doing tiny training runs far behind the commercial frontier - and that's assuming it is able to devote the entire cluster to a run, which it mostly won't be able to. This highlights how as companies are increasing their spending on the raw capital required to train AI systems, universities are being left far behind the frontier. Ultimately, this reduces the level of democratic inputs into the frontier of the technology.   
(A reasonable counterargument to this is whether that's a bad thing - universities don't operate their own oil refineries or car factories either, and that seems fine. But my sense is that there's a lot of experimental insights you can only derive from training models at the frontier, and we're definitely losing out on that).   
**Read more** : [Princeton invests in new 300-GPU cluster for academic AI research (AI at Princeton blog)](https://ai.princeton.edu/news/2024/princeton-invests-new-300-gpu-cluster-academic-ai-research).  
  
***  
  
 **Apple publishes a cookbook for multimodal models:  
**_…MM1 are a good family of multimodal models - the notable thing is how detailed Apple is being in disclosing them…  
_ Apple has published details on MM1, a family of text-image models which get best-in-class performance. The notable thing here is that Apple, a company usually known for its intense secrecy, is being very open about its approach to AI research - as it says in the paper, the purpose here is to outline multimodal large language models (MLLMs) and to “document the MLLM building process and attempt to formulate design lessons, that we hope are of use to the community”.  
  
**Model types:** “We scale up our model by using larger LLMs, from 3B, 7B, to 30B, and by exploring mixture-of-experts (MoE) models, from 3B MoE with 64 experts, to 7B MoE with 32 experts,” Apple writes. “This leads to a family of performant models, that outperforms most of the relevant works to the best of our knowledge.”  
**How good are they?** MM1 outperforms all published prior work for pre-trained MLLMs", Apple says - though it's benchmarking the models against roughly equivalently sized models for which research papers are available and does not benchmark against proprietary models. Therefore, while the MM1 models are definitely quite good, they're unlikely to be the best-in-class.  
  
**Data:** The models were trained on the following datasets:

  * **Captioned images:** CC3M, CC12M, HQIPT-204M, COYO, Web Image-Text-1B (Internal)

  * **Captioned Images (Synthetic):** VeCap

  * **Interleaved Image-Text:** OBELICS, Web Interleaved (Internal)

  * **Text-only:** Webpages, Code, Social media, Books, Encyclopedic, Math




**Key lessons** : “On the modeling side, we see that design aspects are in the following order of importance: image resolution, visual encoder loss and capacity, and visual encoder pre-training data,” Apple writes. When it comes to data, “interleaved data is instrumental for few-shot and text only performance, while captioning data lifts zero-shot performance.”  
  
**Why this matters - unusual openness from a tech giant:** The fact Apple is publishing about this tells us a bunch of broader things about the AI space: publishing stuff is usually a tactic for a) showing competence and b) generating career capital for researchers, so the fact Apple is doing this suggests it wants to hire more people in this area and retain the ones it has. Additionally, the attention paid to relatively small models feels interesting - given Apple's huge emphasis on consumer privacy and data protection it seems likely the company ultimately wants to do on-device AI (whether phone or macbooks) and crucial to that will be building high-performing models that can be fit onto Apple silicon, like some of the smaller ones described here. Finally, the existence of the internal datasets tells us Apple is building out the enabling infrastructure for larger ML efforts, like internal data labeling systems.  
**Read more:**[MM1: Methods, Analysis & Insights from Multimodal LLM Pre-training (arXiv)](https://arxiv.org/abs/2403.09611).  
  
**Tech Tales:  
  
A Good Natured Eschaton  
** _[Eastern United States, five years into the singularity]  
  
_ Be careful that dog has elk shit on it! They said  
Now you tell me, I said, looking at the dog as it nuzzled into me. I pushed it away and it sat down good naturedly at my feet and licked its paws. Some people laughed.  
Me and the other humans and the dog all looked at the fire together  
What do you think is happening out there? I said  
I don't know, said an old timer who'd been there for a while. The same thing but faster.   
Yeah, said someone else. I'm guessing that things feel pretty confusing right now.   
I bet, I said. That's why I'm here.   
And then me and the humans and the dog looked at the flames and some of us turned our faces to the sky and watched the sparks fly upward. Then overhead a river of light appeared from some of the structures being built way up there in space. And then it was gone.   
  
Before I wanted to come to the zone there were reports the ribbon would take a couple of decades to build. But there was also talk they'd get it done sooner as the machines had some bright ideas. The time it’d take kept on shrinking. By the time I decided I was heading here, reports said ten years max.  
  
  
The next day was the same as the day before. Gardening. Walking. Repairing various things from the ravages of time. Light speculation about the world outside, but not too much. And then dinner. And then - for some of us - time around a fire to sit and talk and speculate. Sometimes we went to the border of the exclusion zone and we sold things - woven baskets, carved wood. The stranger the world out there got, the more people seemed to enjoy the things we made - they'd take photos of whatever we sold and post them. Sometimes they or their droids would ask us if we gave them permission to film us - and we usually said yes.  
  
People were coming in all the time. They all had their stories:  
Oh it's just all so fast. One day I got me a hairdryer and it landed on my backyard like fifteen minutes after I asked for it. Can you believe that, 15?   
They said it didn't matter that I was a teacher, I couldn't be as good as the machine.   
I enjoyed it all at first and I made a lot of money. But I just couldn't find meaning in it. I don't have kids or anything so after a while I just thought - why not?  
Everyone used to get so mad at me for not having a phone but I thought they were crazy. I came here because it's peaceful.  
I guess I'm different - I love technology. But one day I woke up and I had these headaches and eventually I figured out they went away if I didn't have a phone near me. Then of course one day I read about this place and I came to visit and all my pain disappeared. I tried to go back but I just thought why am I living like this. So that's why I'm here. Maybe they'll invent something to let me get back out there!  
  
Sometimes at night, from the edge of the exclusion zone, you could see the sky: there'd be these multi-colored drone shows and because we were so far away it was like a blush in the distance - these shapes in the sky and their colors. We had some binoculars and we'd pass them around. As the technology advanced the lights got brighter and the drones got stranger. One day we all got a scare because instead of being rotored drones they were spheres hovering and sometimes turning translucent and other times radiating with all kinds of colors. I guess the machines figured out some interesting tech. We'd try to tell stories about what the light shows could mean - sometimes they were brighter and sometimes less bright, but we couldn't figure it out.   
Those are M2M, said a droid at the border when we were buying fuel.   
M2M? I said.   
Machine to machine, it said. It's something we do for eachother. It's not really easy to understand for humans.   
What does it mean? I said.   
The machine held out both its arms and hands; an imitation of a shrug. It's like internet memes, it said. It's hard to explain unless you spend all your time there. Does that make sense?  
It does, I said.  
What's a meme, an oldtimer who was with me said.   
Let's not get into that, said the machine and I in unison. Then I laughed and the machine just looked at both of us and hummed.  
  
They started calling the economy the Meconomy - the machine economy. That's what one of the droids told us one day.

Months and years passed. We kept selling our goods but they didn't ask to film them as much, though we didn't know if they were just doing it in secret. The lights in the sky got stranger then one day they stopped happening. The supplies still came though and when we asked a droid what happened to the lights the droid said the M2M stuff now happened in wavelengths humans couldn't see.   
There were tens of thousands of people in the exclusion zone, by that point. All voluntary. We even heard at the border one day that there was talk in Washington of expanding it.   
Won't that cost a lot? I said.   
You'd be surprised, said the droid, as it unloaded fuel from the gleaming AI-truck and onto our wooden wagon. There's a joke that maybe the last thing to truly be resistant to all this AI stuff is politics, but even that's changing.  
  
Some of us took up hunting. We could get meat at the border but there were so many animals it seemed like a thing to do. Something about rewilding of land.   
  
They've got these towers in the cities now, said one new arrival. They go up and they've got farms and parks and when you want to go to another tower an air bridge appears.   
Like it folds out of the building? I asked.  
No, that's the crazy thing, they said. It's a flying bridge - you ask to go and it flies over and it's like a tube and the building opens and you walk through it.   
Cool, I said.   
Not for me, they said. That was when I felt like I'd hit my limit. Reminded me of when I was a kid and I had pet hamsters. Not for me, I said. So that's why I came here.   
Damn right, said the oldtimer, and spat into the fire. We humans build stuff to last.  
  
We knew things had changed for good when they stopped taking our money.   
No payment needed, said the robot one day as we went to try and pay it for the supplies.   
What do you mean? I said.   
Consider it a donation, said the machine.   
That caused a bit of commotion. People seemed confused. A couple of the old timers didn't like it. Donations ain't free,"whispered one of them. I sensed tension among us humans for the first time in months. So I stepped forward and spoke to the machine: I'd like to speak to a person about this, I said.   
Of course, said the machine. If you can wait, someone will be here in an hour.   
I'll wait, I said.   
I told everyone else to get out of there. Even if it takes two hours I can get back before dark, I'll be fine, I said. While I waited the machine just stood there. I suppose it was thinking. 

I was patching a hole in my shirt when the person arrived on a flier. The thing was so quiet I didn't notice until the shadow fell over me. It had a multitude of tiny fans on it and they were all silent and the fins were thin - thinner than anything I'd seen before.   
A door in its side slid open and a person stepped out. They had a shirt and pants and shoes on and a single earbud.   
Howdy, they said.   
Hello, I said. Why don't we need to pay? The machine said it was a donation.   
You don't need to pay, they said. It's all so cheap these days there's no need.   
Cheap isn't free.   
You're right, it isn't.   
So why don't we have to pay?  
Ah, the person said, and looked down. I suppose you wouldn't know… the exchange rates system changed recently and we don't take this currency anymore.   
You don't take the US dollar? I said.   
Oh, we do, they said. But there's a new dollar. It works differently. We can't really exchange it for what you have without some complication. It's all digital. The financial system works a lot differently. And really, it's so cheap you don't need to worry.   
It's a pride thing, I said. Can you help us out?  
I'll see what I can do.   
I'm sure you can figure it out, I said. And along with that, can you keep paying us as well?   
The person looked at me for a while. Of course, they said. Of course we can.

When I got back to camp they asked me what happened. Some people seemed upset.   
I never been a charity case, said one of them.   
It's ok, I said. It was just a bug. I spoke to someone and we straightened it out. I guess even these machines mess up sometimes!  
A bunch of people smiled at that. Good thing we had the sense to check, said the old timer. The _human_ sense."   
And everyone seemed pretty calm. The world kept taking our money and paying us for whatever we traded from the zone. I suppose word got around pretty quickly out there. We haven't had trouble since. 

**Things that inspired this story:** What technological abundance might feel like; thinking about the Radio Exclusion Zone as a template or prototype for a kind of peaceful dissent from technology; how real wealth might manifest in the lived and experienced world; fast and slow takeoffs; the nature of machines amusing other machines; a dog covered in elk shit jumping onto a friend of mine at the bar where I play pool and me reflecting that people have been drinking and laughing about dogs covered in shit and playing games with sticks and spheres for thousands of years - perhaps the only thing different about our situation was we had electric lights and some music from a machine, and the whole situation of us and the dogs and the pool table and the alcohol would make total sense to people transported in from millenia ago.

_Thanks for reading!_
