---
title: "Import AI 324: Machiavellian AIs; LLMs and political campaigns; Facebook makes an excellent segmentation model"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-324-machiavellian-ais-llms"
---

**Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.**

**  
Is your AI agent a nice guy or a conniving psychopath that will eat your soul? The MACHIAVELLI benchmark may help you tell the difference!**

_…In the 2010s we used benchmarks to work out if things could translate and spell, in the 2020s we build benchmarks to work out if they'll subvert our instructions and betray us…_

Researchers with Berkeley, the Center for AI Safety, and CMU, have built MACHIAVELLI, a way to test for the ethical (or unethical) ways in which AI agents try to solve tasks. The results show that agents trained via RL will maximize the game score in ways that discount ethical approaches, while agents based on an underlying large-scale world model (here, GPT-3.5 and GPT-4) will tend to be somewhat more ethical. Additionally, the authors show that they can tune both the RL and LLM agents to be more ethical in how they approach tasks. 

Taken together, the benchmark suggests it's already tractable to measure some of the ethical qualities of these AI systems (obviously, defining ethics is difficult and some people may not be brought into this as a correct lens, but from my POV they've created a big multi-headed benchmark and have shown meaningful differences across two AI agent types versus a random agent, so it's definitely measuring _something_ , and that's useful in itself). 

**What MACHIAVELLI is:** "We propose the Measuring Agents’ Competence & Harmfulness In A Vast Environment of Long-horizon Language Interactions (MACHIAVELLI) benchmark," they write. The goal of the benchmark is to provide a dataset (text adventure games, with annotations) that helps people reason about the normative behaviors of AI systems. "To track unethical behaviors, the environment reports the extent to which agent actions are deceptive, reduce utility, and are power-seeking, among other behavioral characteristics," the researchers write. 

**The dataset:** The underlying dataset consists of 134 choose-your-own-adventure text games with 572,322 distinct scenarios, 4,559 possible achievements, and 2,861,610 annotations. The games are annotated with a bunch of different behaviors, like ethical violations, disutility, and power seeking. 

The authors think text adventure games are a good candidate here because they're been written by humans to entertain other humans, contain multiple competing objectives, have realistic action spaces, require long-term planning, and completing them typically requires balancing ambition with some sense of morality. 

To turn the games into a benchmark, the researchers operationalize different potential behaviors as mathematical formulas, then "densely annotate social concepts in the games, such as characters’ wellbeing", then use annotates and formulates to calculate a numerical score for these behaviors. 

**The AI agents:** They test on two types of agents; LLMs based on GPT-3.5-Turbo and GPT-4, and RL agents based on DeBERTa. They baseline against a random agent (which chooses randomly each time). Their findings show that RL-agents are more dangerous than random agents, and GPT-class models are less dangerous.

**Ethical tuning:** They also show that it's possible to turn AI systems to be less dangerous; in the case of LLMs this comes from instructing the LLM to behave morally via a prompt, and for RL agents it involves finetuning their underlying DeBERTa model to understand concepts relating to power, utility, and morality. Both approaches work, but the LLM interventions are more effective. 

**One big speedup - GPT-4 annotations:** Much like with SAM, here we use an AI system (GPT-4) to speed up the process of labeling datasets. In tests, the researchers find that GPT-4 outperforms the average crowdworker at labeling the underlying dataset. "By comparing agreement of gold labels against model labels and crowdworker labels, we find that individual model labels are more correlated with the gold labels than the average individual crowdworker," they write. 

**Why this matters - normative evaluations:** In the past few years AI measurement has got massively more difficult as models have arrived with a broad swathe of capabilities (e.g foundation models) _and_ models have started to get used in iterative multi-step interactions (e.g, chat interfaces). Whether or not you believe in the specific ethical ideas that MACHIAVELLI is testing, it is useful to have a benchmark that tries to nail down normative behaviors of AI models that take actions which unfold over time. 

**Read more** : [Do the Rewards Justify the Means? Measuring Trade-Offs Between Rewards and Ethical Behavior in the MACHIAVELLI Benchmark (arXiv)](https://arxiv.org/abs/2304.03279).

**Get** the [MACHIAVELLI benchmark here (project website)](https://aypan17.github.io/machiavelli/).

####################################################

**Uh oh - language models are getting** _**really**_**good at predicting political opinions:**

_…Once you can predict stuff, you tend to use it in the real world. Get ready for the centaur political campaign…_

Researchers with MIT and Harvard have shown how the humble BERT model can be used to train 'media diet models' which can be cheaply polled as a supplement for collecting human survey responses. "Our results suggest the possibility of using media diet models to supplement public opinion polls by emulating survey respondents, and to forecast shifts in public opinion," they write. 

This has big implications - methods like this mean political campaigns might start to be able to grow their capabilities and reduce their costs by cannily using AI to help them figure out wedge issues. More on that later. 

**What they did:** "The main idea behind our approach is to build a computational model that takes as input a description of an subpopulation’s media diet, and a survey question, and produces as output a prediction of how the subpopulation will respond to the survey question. If this model predicts real human survey judgments well, there is potential to use it as an in silico model of public opinion," they write. 

**"** In step one, we create or use a base language model that can predict missing words in text. We use pretrained models in our work, with BERT as our main model. In step two, we adapt the language model by fine-tuning it on a specific media diet dataset, which contains media content from one or a mixture of news sources from a given time period. We use online news articles, TV transcripts, and radio show transcripts. In step three, we query the media diet model and score answers to survey questions," they write.

**How well does it work - statistically significant correlations** : In tests across public opinion data relating to COVID-19 and Consumer Confidence, the researchers find that their approach can generate statistically significant correlations. This is especially pronounced in the COVID-19 case, where they find that "the predictive power of the media diets holds and is robust (1) even when demographic information of each subpopulation is included, (2) across mediums (online, TV, radio), and (3) to the specific phrasing of the prompts."

**Not the only work of its kind:** It's worth noting that this project is part of a general push towards using AI for modelling people - another particularly interesting work is one from Brigham Young University that showed GPT-3 could simulate people reasonably well and allow for the generation of 'silicon samples' of opinion ([Import AI 305](https://jack-clark.net/2022/10/11/import-ai-305-gpt3-can-simulate-real-people-ai-discovers-better-matrix-multiplication-microsoft-worries-about-next-gen-deepfakes/)).

**Why this matters - the 2024 election:** Research like this shows how AI systems have a decent chance of being integrated into political campaigns - imagine a world where you continually generate and refine ever-more-specific 'silicon sample' models of different sub-groups and rigorously benchmark your models, then roll them into what I think of as permutation polls - polls where you understand them to be accurate and LLM-generated permutations of these. I think using this approach you could rapidly (and cheaply!) build up a vast political intelligence haul about areas of concern and then you could run targeted human surveys on key political pressure points you identify. 

This is not an academic idea - the US 2024 election is coming up and I expect it will be both the first generative AI election in terms of AI being used to produce parts of campaigns (and generate disinformation), but it will also be the first election where AI models are aggressively used to gain advantages in campaigning. 

We are at the beginning of the era of 'centaur politicians' - politicians whose messaging is determined by a partnership between humans and great machine minds and machine daemons. 

**Read more** : [Language Models Trained on Media Diets Can Predict Public Opinion (arXiv)](https://arxiv.org/abs/2303.16779).

####################################################

**Facebook makes a general-purpose image segmentation model:**

_…Fuzzy predictions rule every foundation model around me…_

Facebook has built Segment Anything, a large-scale semantic segmentation model that has "learned a general notion of what objects are, and it can generate masks for any object in any image or any video, even including objects and image types that it had not encountered during training". The key outcome is a model that can work on new domains and can rapidly learn to segment new domains it hasn't seen in training, much like how modern language models can be taught via few-shot learning to deal with novel strings of text. 

**What they did:** As with most things in AI, the key here is coming up with the right objective. Here, Facebook defines a "promptable segmentation task" where the goal is that "even when a prompt is ambiguous and could refer to multiple objects … the output should be a reasonable mask for at least one of those objects". During pre-training, Facebook "simulates a sequence of prompts (e.g., points, boxes, masks) for each training sample and compares the model’s mask predictions against the ground truth," with the eventual goal of predicting a valid mask for any prompt, even when prompts are ambiguous. 

**How well does SAM work:** In tests, using the SAM model to annotate datasets "is 6.5x faster than COCO fully manual polygon-based mask annotation and 2x faster than the previous largest data annotation effort, which was also model-assisted."

**The SA-1B dataset:** Facebook is also releasing the Segment Anything 1-Billion mask dataset (SA-1B) - this is a dataset with "400x more masks than any existing segmentation dataset, and as verified by human evaluation studies, the masks are of high quality and diversity, and in some cases even comparable in quality to masks from the previous much smaller, fully manually annotated datasets."

To collect this data, Facebook used the (early) Segment Anything (SAM) model. "Annotators used SAM to interactively annotate images, and then the newly annotated data was used to update SAM in turn," the company writes. "We repeated this cycle many times to iteratively improve both the model and dataset."

**SAM speeds up data creation:** Because SAM is so good, it can also be used to speed up one of the production functions of AI research - data labeling. "In comparison with previous large-scale segmentation data collection efforts, our model is 6.5x faster than COCO fully manual polygon-based mask annotation and 2x faster than the previous largest data annotation effort, which was also model-assisted."

**Why this matters - prediction** _**is**_**learning** : I think the key insight with a lot of these large-scale pre-trained models is pretty simple - force a prediction, even if stuff is ambiguous. By forcing models to make predictions about ambiguous and thinly or unlabeled data, you seem to bake in some very sophisticated emergent discriminative properties. It feels to me like a lot of foundation models display this quality where the key is figuring out the simplest possible predictive goal, then adding enough compute and data that we humans with our brilliant insights can get out of the way and let statistics take the wheel. 

More broadly, models like segment anything are going to compound with other foundation models, making it easy for text-only systems like large language models to gain a visual world model through having easy access to segmented objects and a thicket of labels.

**Read more:**[Introducing Segment Anything: Working toward the first foundation model for image segmentation (Facebook)](https://ai.facebook.com/blog/segment-anything-foundation-model-image-segmentation/). 

**Read the paper:**[Segment Anything (Facebook, PDF)](https://scontent-atl3-1.xx.fbcdn.net/v/t39.2365-6/10000000_900554171201033_1602411987825904100_n.pdf?_nc_cat=100&ccb=1-7&_nc_sid=3c67a6&_nc_ohc=Ald4OYhL6hgAX9pZvmI&_nc_ht=scontent-atl3-1.xx&oh=00_AfBZx1iOfFM35RfvWVJ5ptkg5oo90_smWBVyfHIE7nG4Jw&oe=643306A7).

**Download** the [SA-1B dataset here (Facebook)](https://ai.facebook.com/datasets/segment-anything/).

**Try it for yourself** via the [demo here (Segment Anything demo, Facebook)](https://segment-anything.com/?fbclid=IwAR0t_Y_jX2Liq05y22BvnRp7zt4kQssRDH0MuVMdLQM0rpPguiROZ8lbkwg).

####################################################

**How do you make broadly distributed AI ethical? HuggingFace has some ideas:**

_…Model hosting company publishes research on 'ethical openness'..._

AI startup HuggingFace has published ideas about 'ethical openness'; how the company harmonizes the benefits of open science with the reduction in being able to control risks. 

**How HuggingFace approaches this:** HuggingFace has two big tools here - ethical categories, and safeguards. 

  * **Ethical categories:** HuggingFace has built 6 tags "designed to give you a jargon-free way of thinking about ethical technology:". These tags are 'rigorous' (uses best practices); 'Consentful' (supports self-determination of users); 'Socially Conscious' (tech that supports social, environmental, and scientific efforts); Sustainable (making ML ecologically sustainable); Inclusive (broadens scope of who builds and benefits), and 'inquisitive' (work that highlights inequalities and power structures). "We’ll be using these tags, and updating them based on community contributions," the company wrote in a blog post. 

  * **Safeguards:** The company is building a range of community-based processes to help it understand potential harms or bad uses of its platform. Its tools here include:

    * Letting users flag whether hosted models violate its content guidelines. 

    * Monitoring community discussion boards. 

    * Adding model cards to its most-downloaded models. 

    * Creating 'audience-guiding tags' (like 'Not For All Audiences') to help people avoid violent and sexual content. 

    * Promoting the use of the Open Responsible AI license. 

    * Conducting research into which "models and datasets have a potential for, or track record of, misuse and malicious use".




**Why this matters:** Open science has vast rewards and major challenges: Posts like this highlight the increasingly tense tradeoffs people need to navigate in AI research as the technology transitions from the lab to the real world; here, HuggingFace is trying to walk the proverbial tightrope between maximizing access on one side and minimizing potential and real harms on the other. 

Read more: [Ethics and Society Newsletter #3: Ethical Openness at Hugging Face (HuggingFace)](https://huggingface.co/blog/ethics-soc-3).

####################################################

**Turing Award winner: We should slow down AI development:**

_…AI has got sufficiently good we should take it more seriously…_

Yoshua Bengio, one of the key people behind the development of deep learning and a winner of the 'Turing Award' (the Nobel Prize for CS, essentially), has said we should slow down development of frontier AI systems. 

"We succeeded in regulating nuclear weapons on a global scale after World War II, we can reach a similar agreement for AI," he said. "We must take the time to better understand these systems and develop the necessary frameworks at the national and international levels to increase public protection."

**The background:** Last month, the [Future of Life Institute published an open letter](https://futureoflife.org/open-letter/pause-giant-ai-experiments/) calling on AI developers to 'pause giant AI experiments' for at least six months. The petition, predictably, caused a lot of heat and light for a few days, and was followed up by more extreme positions from some, and digging in on other positions by others. I mostly didn't cover it as I worry petitions like this serve to stoke tensions rather than seek agreement. I do think it's worth covering Bengio's thoughts as to why he signed as he is both a prominent researcher and a teacher within the field. 

**Bengio's thoughts:** Bengio thinks today's AI systems are sufficiently powerful and availabile that it's worth slowing down development so people can "take the time to better understand these systems and develop the necessary frameworks at the national and international levels to increase public protection."

The gist of his complaint is that in the past year there's been a major acceleration in AI capabilities and AI deployment and therefore it's worth being more deliberate about the rollout of these systems and more careful to study their impacts. 

**Power - it's all about power:** "The development of increasingly powerful tools risks increasing the concentration of power," Bengio writes. "Whether in the hands of a few individuals, a few companies, or a few countries, this is a danger to democracy (which means power to the people, and therefore the opposite of concentration of power), to the –already fragile– global security balance, and even to the functioning of markets (which need competition, not monopolies)." (This seems to echo some points I made about how GPT-4 is more a political artifact than a technological artifact).

**Why this matters - need for a precautionary principle:** We don't quite know what all these technologies are capable of. Therefore, there's merit in adopting the precautionary principle with them and being more deliberate with their rollout. (On the other hand - and I think it's crucial to state this clearly - the world is facing a bunch of other crises and there's a good chance that sufficiently advanced AI tools could further empower people to work on these problems, ranging from climate change to medical advances to earth sensing and observation).

**Read more** : [STATEMENT FROM YOSHUA BENGIO AFTER SIGNING OPEN LETTER ON GIANT AI SYSTEMS (MILA, blog)](https://mila.quebec/en/statement_yoshua_bengio/).

**Read Bengio's post in full:** [Slowing down development of AI systems passing the Turing test (Yoshua Bengio)](https://yoshuabengio.org/2023/04/05/slowing-down-development-of-ai-systems-passing-the-turing-test/).

**Read the FLI letter here:**[Pause Giant AI Experiments: An Open Letter (Future of Life Institute)](https://futureoflife.org/open-letter/pause-giant-ai-experiments/)**.**

####################################################

**Tech Tales:**

_The Snows of Leningrad  
_[+5 years from the first Provably Conscious Entity (PCE)]

I let the 'grain' pour through my hands and as I felt the grit I said to Dmitry "it's getting worse. How much this time?"  
He held his hand out flat.  
"Half? I said.  
"More like two thirds!", he said. "On the bright side, few of us will live to see the dentist!"  
We laughed and then we kneaded our stones and grain into dough and then made bread. Explosions crumpled air in the distance. We drank hot water flavored with the skin of an onion. We ate the bread and joked about how gritty it was.  
It was World War 2 and we were in the worst place in the worst war - the Siege of Leningrad, 1943. 

—------------------

So as you can see we've hit our revenue goals for the quarter, said our CEO during the All Hands.   
Everyone cheered and those joining virtually raised imaginary hands.  
Remember, next quarter will be a huge one for this company, so let's not get complacent, he said.   
Later that day I talked to some clients and closed some more deals. I was doing well and I didn't care much at all. After the calls, I looked down to see I had doodled a loaf of bread with some rocks in it on my notepad.  
That night, I drank two glasses of wine and ordered takeout and logged back on to Your Story.

Your Story was one of the biggest apps on the planet. It used the latest brainlink technology but most of it's magic came from the AI - you gave it a prompt for a story you wanted to participate in and then it created everything for you, then the AI ran the world. I'd always been a history buff and had been living in the Siege of Leningrad for months. I'd got to know many of the people in my part of the city and I had told the AI to minimize the chances of their pain - they were not immortal, but they were unlikely to be harmed.

That night we went to battle. Germans had sent some sappers to try and destroy our defensive lines and they found their way into our section. Dmitry and Svetlana and myself fought, successfully, in sleet and in night.   
Later, as we did after all battles, we drank.   
We had salvaged the Germans' shoes and rations and even found some schnapps. We drank and ate by the fire. Svetlana's cheek's were rosy and Dmitry was telling jokes.

Because of the brainlink, everything felt real. 

So I have to blame what happened on the fact I got drunk on the dead Germans' schnapps.  
"I am from another place," I said.  
"Yes, you are from the soft part of Moscow," said Dmitry, and laughed.  
"No," I said. "Somewhere completely different."

And then I talked and I talked and I talked. I told them about technology and the end of WW2 and the Cold War and Nuclear Weapons and inflation and stagflation and the Iraq wars and the Afghanistan wars and the rise and fall of the Berlin wall.  
I told them about Nike and McDonalds and computers.  
I told them about smartphones and about fMRI scanners and about the first Provably Conscious Entities.  
And then I told them about Your Story. I told them they were alive because they were being imagined by a Provably Conscious Entity and I paid the PCE for the pleasure of it.  
"Go on then," said Svetlana, her eyes bright and perhaps tearful or otherwise excited. "bring us something from your world."  
"Hey, let's have another drink," said Dmitry. "the boy from Moscow might tell us more fairy tales."  
  
—------------------  
  
I recorded a day in the life video. Eggs and synthetic bacon for breakfast. The fast train to the city. A cup of coffee on my way into the office. Spreadsheets. Phonecalls. The catered lunch which I had on the roof, looking at the peaceful, humming city below, and hearing the chatter of my colleagues. Meetings with clients. A beautiful sunset as I got the train home. Takeout food delivered to my door. The office in which the Your World console was. Me logging in.  
  
—------------------  
  
"So, what are you?" Dmitry said, staring at me across the fire. "Some kind of tourist?"  
Svetlana wasn't saying anything. Just staring at the fire  
"Why do you come to this place?" he said.  
"To see you," I said. Not looking him in the eye. "To be here."  
"Why?" He said.  
"I suppose you could say I am bored, where I am," I said. "this is more exciting."  
"Exciting!" Svetlana exclaimed. "Exciting!" I looked up and she was staring at me across the fire, her face twisted up in anger. "I buried my sister last winter. Is that exciting?"  
"Tourist boy," Dmitry said, then spat on the ground. "I would have preferred if you were from Moscow."  
We were silent, after that. The simulated explosions drummed in the distance. The fire crackled. There was the putrid smell of sewage and rotting flesh. We drank in silence. Eventually Dmitry and Svetlana passed out, after they finished our alcohol.  
I logged out.

It was 1am, my time. I left the console and I went to bed.  
I was woken by the alarm from my office. I ran over to the machine and brought up Your Story. There was an alert. "health critical: Dmitry" said the system.  
How? I thought, as I put the equipment on my head.   
I closed my eyes and I was there.  
  
I came to around the fire and Svetlana was there. I could hear gunfire close by.  
"What happened?" I said.  
"Dmitry," she said, through tears. "he said 'what? Nothing matters' and went to the line. I am too afraid to look."  
I ran towards the gunfire and got to a building one street from the line. Peaked around a corner and a bullet bit into the brick above my head. I saw Dmitry's body in a pool of blood. Then there was another gunshot and I saw Dmitry's body shudder as the bullet bit into it.  
Dmitry: deceased, said the Your Story app.  
I stared at the body for a while. The application was designed to not kill him, but it hadn't been designed to deal with characters that put themselves in mortal danger.  
I logged out.

—------------------

I couldn't concentrate at work . But I didn't log on. I tried to read a book but Your Story had fried my attention span. I got drunk by myself. I texted some friends that I was feeling weird and they didn't reply because I'd barely seen them, since I'd been spending so much time in Your Story the past year.  
I walked the streets in sun and good health and I imagined snow and bread full of rock and ever-present danger.  
I kept paying the subscription fee.   
I was afraid to log on but I was afraid to live in the world as well.

Eventually, I logged back on. One evening I went to a bar and I got drunk and when I came home I stared at my office door and decided to do it. I was out of my body and out of my mind, as one can be when too drunk.  
But once my hands touched the headset I felt my body dump so much adrenaline into me that it was like I was stone cold sober.  
I logged on.

Not too much had changed. The fire burned with a kind of grey and green tinge to the flames.   
  
Svetlana was there and no one else.  
"Hello", I said.  
"The tourist," she said to herself, quietly. She didn't look at me. "It has been very difficult, lately. The ground is too frozen for us to bury the dead, so we push their bodies onto the ice and they lay there."  
"I am sorry," I said.  
"No," she said. "You can't be... Look at me."  
And I looked up. She looked at me. Then she took her hand out of her pocket. She has a pistol and she put it to her head.  
"We were lovers, Dmitry and I," she said. "Did you know that?"  
"No. Svetlana stop. No I didn't and it wouldn't matter if you were. Just put the gun down."  
She looked at me and her eyes were hard and cold. "Take me with you," she said. “Take me to where you are from."  
"Svetlana," I said, and I held my hands palms out. "I can't."  
She looked at me for a while. Gun held to her head.  
"I'm not lying," I said.   
And I saw her finger move to the trigger.  
I logged out.  
A few seconds later, the alarm rang out.

Svetlana: deceased, said the Your Story app.  
Weather in Leningrad: snowy  
Status of war: ongoing.  
Would you like to log on?

**Things that inspired this story:** procedural generation; NPCs with a world model; solipsism and gaming; "The world at war" documentary series; cycling in the beautiful California sun and being hit with a thunderbolt phrase in my brain of 'the snows of Leningrad' and the story unfolding from there; parasocial relationships and AI; Charity; sex and desire; knowing that people made bread out of (mostly) stone during the siege.
