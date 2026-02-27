---
title: "Reports of the birth of AGI are greatly exaggerated"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/reports-of-the-birth-of-agi-are-greatly"
---

[](https://substackcdn.com/image/fetch/$s_!b9jI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4169e6a4-9efa-4098-bac2-c6d7be750e3f_1738x1034.jpeg)

Marvin Minsky apparently thought, back in the 1960s, that computer vision was a problem that could be solved in a summer. (Spoiler alert, in 2023 the problem is still far from solved). What’s new, though, are rumors that AGI has been solved. Sam Altman announced in late September, perhaps in jest, that “[AGI has been achieved internally”, only to walk it back a few hours later](https://www.independent.co.uk/tech/chatgpt-ai-agi-sam-altman-openai-b2419449.html). Last week, Blaise Agüera y Arcas, vice president and fellow at Google Research, and Peter Norvig, formerly Director of Research at Google, and now at Stanford, argued in all seriousness that “[Artificial General Intelligence Is Already Here](https://www.noemamag.com/artificial-general-intelligence-is-already-here/)”— in what can only be described as an epic act of goal-post shifting.

The article begins with this bold claim: 

> “Today’s frontier models perform competently even on novel tasks they were not trained for, crossing a threshold that previous generations of AI and supervised deep learning systems never managed. Decades from now, they will be recognized as the first true examples of AGI, just as the 1945 ENIAC is now recognized as the first true general-purpose electronic computer.” 

Agüera y Arcas and Norvig describe the ways in which large language models (LLMs) can carry out tasks for which they were not specifically trained; they claim that this ability is key to being an AGI; and they argue that therefore the kernel of AGI has been achieved. They conclude with a long, condescending discussion of the various reasons that some pitifully confused people are “reluctan[t] to acknowledge [that] AGI has already arrived.”

Count us among the confused; we really, really don’t know what Agüera y Arcas and Norvig are talking about.

§

To begin with, by the classical criteria for AGI [Artificial General Intelligence], LLM’s hardly qualify. One of us wrote about those criteria last year, in this Substack, in preparation for a proposed bet with Elon Musk, consulting with two of the people who coined the term AGI, Ben Goertzel and Shane Legg, and came up with this.

> _[If we are going to bet, we should make some ground rules. The term AGI is pretty vague, and that’s not good for either of us. As I offered on Twitter the other day: I take AGI to be “a shorthand for any intelligence ... that is flexible and general, with resourcefulness and reliability comparable to (or beyond) human intelligence”.](https://garymarcus.substack.com/p/dear-elon-musk-here-are-five-things?)_

Current machines can’t do this, especially not the reliability part. They can’t count, do five digit multiplication, reliably generalize kinship relations, or even reliably follow the rules of chess, and so on—despite the fact that each of these activities is presumably well explained, explicitly, in the training set, They also can’t, for example, obey the dictum “don’t make stuff up”, when they write a biography or a new story, and we have yet to see them drive cars as well as the average human adult.

DeepMind co-founder Shane Legg is generally more optimistic about AI than we are, but even he couldn’t quite see what his Google colleagues Aguera y Arcas and Norvig are on about; when we asked him on X whether _he_ bought their argument, he replied as diplomatically as he could, and optimistically, but with a clear affirmation of what we said: AyA&N had lowered the bar :

> _[They use a lower bar for AGI than I do, and so they get a different answer. My bar for AGI is a machine that can do the cognitive tasks that people can typically do. We're not there yet, but we're much closer to this than we were a few years ago.](https://x.com/shanelegg/status/1712132838210846987?s=61&t=2voLMkhJf6P349CqztWSAQ)_

Melanie Mitchell was also a bit diplomatic, but at least as miffed as we were by the condescension:

> _[They made some good points, but also made some dubious statements. Also, I think the undercurrent of dismissal of "skeptics" is not helpful. All scientists should be skeptics -- that's part of the job](https://x.com/melmitchell1/status/1712138935105728726?s=61&t=2voLMkhJf6P349CqztWSAQ)._

_§_

The problem with the paper though isn’t just its hostility towards critics, or the way in which it lowers the bar, it’s that its key arguments don’t go through.

One key claim (written in bold pullout text) that made our jaw drop was that “Frontier language models can perform competently at pretty much any information task that can be done by humans, can be posed and answered using natural language, and has quantifiable performance.” That’s just obviously not so. There are _many_ purely language-based tasks that humans can do — question answering, writing factual prose, summarizing, examining the truth of a claim, cross-examining a hostile witness in court, reading and understanding a full-length book — that existing AI systems cannot perform “competently”. The first author’s _nine_ -year-old can do five digit multiplication better than an LLM. We love Noema, but their fact checker was asleep at the switch. (What Agüera y Arcas and Norvig might really mean, perhaps, is that LLMs do well on a lot of benchmarks, but then again since we don’t know eg how many law school exams GPT-4 was trained on, it’s hard to even know what to say about these benchmarks. The fact that making benchmarks is hard doesn’t mean LLMs have achieved AGI).

Meanwhile, the boldfaced (written in bold pullout text) claim that “The most important parts of AGI have already been achieved by the current generation of advanced AI large language models” is logically flawed. Until we get to the finish line, we can’t know the route.  _Maybe_ what’s required already exists, but more likely, we are still at least a few paradigm shifts away . To take one example, true AGI might revolve around planning with respect to detailed world models that are maintained over time; as Subbarao Kambhampati has shown, LLMs are weak at planning; as hallucinations show, they are also weak at the maintenance of world models, strongly suggesting some key ingredients have _not_ yet been invented. It’s certainly plausible that s _ome_ of the prerequisites of AGI may have been achieved, but considerable overreach to presume that _all_ of “the most important ones” have already been invented.

§

The fact that LLMs trained on the task of next-token prediction can also do a pretty good job at a variety of natural language tasks, and, very recently, a considerably less good job of tasks that combine text with images, as emphasized by Agüera y Arcas and Norvig is certainly interesting, but it doesn’t justify the claim that they constitute “general intelligence”. It is common in the history of technology (as well as biological evolution) that a mechanism developed for one purpose turns out to be useful for another. GPUs were developed for video games and other graphics applications, not for training deep learning systems or mining crypto-currency. That doesn’t make GPU’s AGI. (Though they may get used in the service of AGI when it comes).

The World Wide Web was developed for sharing scientific papers, not for online commerce or for inducing people to make available enormous quantities of digital data that can be used to train ML-based AI systems. That generality doesn’t make the web AGI.

§

Just one more thing to keep things real. It’s worth noting that for many different AI tasks --- robotics, image interpretation, planning, game playing, scientific applications, many forms of reasoning --- state of the art AI currently makes little to no use of the transformer architecture that underpins LLMs. If they really were AGI, presumably everybody would use them, for everything. But in many practical problems, working practitioners don’t; they use a wide range of other methods, often far more tractable, far more reliable, and far more efficient. Transformers and generative AI are getting a lot of attention, and have considerable utility, but they are nothing like the all purpose tools some people seems to imagine them to be. In AI, no single technique is likely to be a silver bullet, now or ever.

Here’s where we actually are, so much more more boring, and so much more real: Current models trained on next-token prediction have remarkable abilities and remarkable weaknesses. The scope of those abilities and weaknesses of the current systems is not well understood. There are some applications where the current systems are reliable enough to be practically useful, though not nearly as many as is often claimed. No doubt the next generation of systems will have greater abilities and more extensive applications and will somewhat mitigate the weaknesses. What is to come is even more poorly understood than the present. But there is zero justification for claiming that the current technology has achieved general intelligence.

[Share](https://garymarcus.substack.com/p/reports-of-the-birth-of-agi-are-greatly?utm_source=substack&utm_medium=email&utm_content=share&action=share)

 _**Gary Marcus** used to get flak for saying that some people were trying to build AGI. Now, perhaps, he will get flak for saying that we haven’t yet achieved it._

_**Ernie Davis** is a Professor of Computer Science at New York University._
