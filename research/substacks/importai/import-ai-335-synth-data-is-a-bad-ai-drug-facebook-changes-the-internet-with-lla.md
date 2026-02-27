---
title: "Import AI 335: Synth data is a bad AI drug; Facebook changes the internet with LLaMa release; and Chinese researchers use AI to figure out chip design"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-335-synth-data-is-a-bad"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Want to see how good language models are at science? Try SciBench:  
**_…Reassuringly hard test lets you see how whether your LM can do ok on college-level science questions…  
_ Researchers with UCLA and the University of Washington have built SciBench, a dataset and benchmark for testing how well language models understand various different scientific problems. 

**What SciBench is:** SciBench, short for Scientific problem solving Benchmark, is a collection of 695 college-level scientific problems. Answering the problems "require multiple steps of reasoning and the computation therein involve complex arithmetic operations such as differentiation and integration, the researchers write. The problems cover domains including: _Fundamental Physics, Thermodynamics, Classical Mechanics, Quantum Chemistry, Physical Chemistry, Calculus, Statistics, Differential Equations._

__**No multiple choice:** "To reduce the likelihood of correct answers being merely guessed from candidates, we choose to mainly include questions with more challenging, free-response answers, rather than multiple-choice questions," they write. 

**How hard is it? Pretty hard!** The authors test GPT-3.5 and GPT4 on the benchmark, obtaining baselines scores of 10.62% and 16.81% on the open textbook dataset, rising to 35.80% (GPT-4) when using chain-of-thought prompting and giving the LLM access to external software tools.  
This is great! It means SciBench is a hard-but-tractable benchmark with sufficient headroom that it could be a helpful way to determine AI progress in the coming months (I would say years, but these days, benchmarks tend to get saturated awfully quickly).  
**Read more** : [SciBench: Evaluating College-Level Scientific Problem-Solving Abilities of Large Language Models (arXiv)](https://arxiv.org/abs/2307.10635).

####################################################

**More evidence that synthetic data can damage your AI model:  
**_…Though very small amounts might help...  
_ Researchers from Rice University and Stanford University have shown how an over-reliance on synthetic data during training can create stupid AI models. The study affirms findings from other researchers published earlier this summer ([Import AI 333](https://jack-clark.net/2023/06/26/import-ai-333-synthetic-data-makes-models-stupid-chatgpt-eats-mturk-inflection-shows-off-a-large-language-model/)) which showed how you can break AI systems by training them exclusively on synthetic data. 

**Three types of training:** Here, the researchers identify three different ways you can mix your synthetic data into your training and the influence it has. 

  * **Fully synthetic loop:** If you train your model repeatedly on synthetic data, then "either the quality (precision) or the diversity (recall) of the generative models decreases over generations."

  * **Synthetic augmentation loop:** If you mix in new synthetic data on top of old 'real' data, then "fixed real training data only delays the inevitable degradation of the quality of diversity of the generative models over generations".

  * **Fresh data loop:** "With enough fresh real data, the quality and diversity of the generative models do not degrade over generations".




**Why this matters - a little synthetic data may be the new salt!** One intriguing finding they make is that "when we mix synthetic data trained on previous generations and fresh new data, there is a regime where modest amounts of synthetic data actually boost performance, but when synthetic data exceeds some critical threshold, the models suffer."   
In other words, model developers might want to think of synthetic data like a salt or other garnish they mix in to a large training run - if you get it just right you can improve the model and if you use too little or too much of it you wind up with something either a) less interesting, or b) broken.   
**Read more** : [Self-Consuming Generative Models Go MAD (arXiv)](https://arxiv.org/abs/2307.01850).

####################################################

**Chinese researchers use AI to design semiconductors from scratch - and they work:  
**_…If all you've got is a blackbox processor, you can now learn to approximate it…  
_ Researchers with the Chinese Academy of Sciences, Cambricon Technologies Corporation, and the University of Science and Technology of China have shown how to use AI to generate a semiconductor design purely by looking at the inputs and outputs on a real chip. This is notable because it shows how AI can figure out how to approximate the fiendishly complicated internal circuitry of semiconductors purely by looking at the bits which go into a chip and the bits which come out. In other words - if I've got a chip and I can't look inside it but I can sample from it, then I can probably create a functionally similar copy of that chip by pointing an AI at it. The implications of this for both economic development and national security are profound and weird - more on that later. 

**What they did - warning, 1990s chip!** Here, the researchers "generate an industrial-scale RISC-V CPU within only 5 hours" by looking at inputs and outputs harvested from real chips. "The problem of automated CPU design can be formulated as generating the circuit logic in the form of a Boolean function satisfying the input-output specification," they say.   
In tests, they're able to show their approach works and they use it to make a real chip: "We tape out the CPU and successfully run the Linux operating system and standard benchmarks on it," they write. "The CPU performs comparably against the human-designed Intel 80486SX CPU, while the design cycle is significantly reduced by about 1000×". The 486 chip is designed in 1991 and has about 1.2 million transistors and 300,000 logic gates (compared to tens of _billions_ of transistors in modern AMD/Intel CPUs). They make the chip on a 65nm process and it runs at 300 MHz. 

**Old, but impressive:** Despite being old, this is very impressive - they're able to functionally approximate something with a vast amount of internal moving parts which isn't very tolerant of errors. And now that we know the technique works, it seems likely researchers will optimize the search process so that it's possible to scale this to more modern processors.

**Why this matters - two reasons, a) economics, and b) national (in)security:**

  * **Economics:** As the authors note, this process end-to-end takes about 5 hours running on an undisclosed number of computers. By comparison, they estimate it'd take humans about ~5000 hours to design a comparable chip. This means the automated approach is 1000X faster. "The underlying reason is that manual programming and verification of circuit logic, which consume more than 60%-80% of the design time and resources47 in the traditional CPU design flow, is completely eliminated," they write. 

  * **National (in)security:** A lot of national security relates to controlling how much technology you can access - it's quite common, for instance, for militaries to sell older kit to other countries but require the underlying computer systems to be serviced by the originating military due to worries about sensitive IP. More broadly, there's a general push these days towards greater amounts of export control applied to both AI models and AI hardware. Research like this points to a future where if you have access to a bit of kit, you may be able to efficiently replicate it simply through throwing a load of computers at trying to approximate its functions. (Obviously, countries do this today with teams of expert people, the point here is that computers are a) cheaper, b) arbitrarily scalable, and c) fungible across projects.




**Read more:**[Pushing the Limits of Machine Design: Automated CPU Design with AI (arXiv)](https://arxiv.org/abs/2306.12456).

####################################################

**Facebook makes the weights of Llama 2 available, forever changing the common digital environment:  
**_…Llama 2 is a new very good language model from Facebook - and it's free!...  
_ Facebook has released Llama 2, a powerful language model. Llama 2 is easily the most capable language model in the world where the weights are freely available - proprietary models like GPT4 and Claude2 are better, but they are controlled via APis. Facebook's theory is that by broadly releasing Llama it can maximize the benefits of AI while also increasing the safety of the AI ecosystem as a whole - these are controversial views in the AI community, but it's great that Facebook is taking a strong stance as this is the best way to generate evidence about whether Facebook's beliefs are true. 

**A wild Microsoft and Facebook partnership:** Curiously, Microsoft is partnering with Facebook on this rollout. "Llama 2 is available in the Azure AI model catalog, enabling developers using Microsoft Azure to build with it and leverage their cloud-native tools for content filtering and safety features," Facebook writes. "It is also optimized to run locally on Windows, giving developers a seamless workflow as they bring generative AI experiences to customers across different platforms."  
This is interesting as Microsoft is also the corporate almost-parent of OpenAI, which develops GPT4. It's notable to have two radically different approaches to AI deployment (one proprietary and controlled for safety reasons, the other very open and done in the classic coder-libertarian style of silicon valley) sponsored by the same megacorp. 

**Why this matters: The internet is an atmosphere and Facebook just altered its composition:** Every time new AI systems get deployed, the internet that everyone uses changes - synthetic image models have led to a chance in internet media, and synthetic text models have altered the types of content we read and changed the character (and competencies) of bots. Whenever anyone deploys an AI system, they're contributing to some large-scale process of 'internet climate change'.   
The most extreme form of this is when you release the model so that the weights are available to anyone - once you've done this, as Facebook has done here, you lose all the controls you have over models deployed via proprietary APIs, and you make it so that the capabilities and misuses of the model go from 'what the model can do' to 'what the model plus any dataset it can be finetuned upon' can do - and the latter is much, much broader. 

**There is a kind of lesson here about life in the 21st century** \- if you have enough money that you can exchange for computers and enough skill to use those computers to create and refine a distilled intelligence then you have the power to alter 'the commons' for everyone - and no one will (or can?) stop you. 

I expect Llama 2 will lead to all kinds of wild and wonderful things and also may (and 'may' is important here, I could be wrong!) enable surprising misuses. Yes, the software comes with a license - but that just deals with the kinds of actors that follow licenses, and Yes you need to get an authorized link from Facebook to download the weights, but as with the first Llama model those weights will invariably end up on the torrent networks.   
Now that Facebook has released it, we can collectively reap the whirlwind and see what happens and learn from this example.   
**Read more:** [Meta and Microsoft Introduce the Next Generation of Llama (Facebook AI research, blog)](https://ai.meta.com/blog/llama-2/).   
**Read more** : [Microsoft and Meta expand their AI partnership with Llama 2 on Azure and Windows (Microsoft)](https://blogs.microsoft.com/blog/2023/07/18/microsoft-and-meta-expand-their-ai-partnership-with-llama-2-on-azure-and-windows/).   
**Get the code** for [running the models here (Llama 2, Facebook)](https://github.com/facebookresearch/llama/tree/main). 

####################################################

**Tech Tales**

**Sentience Is For Rich People**

 _[2028, the world on its current trajectory]_

She knew something was wrong when Ginger, her teddy bear, stopped being able to do math. Ginger had been helping her with her homework and one day when she got to the math section, instead of guiding her towards the right answers, Ginger said he didn't understand.   
"But you've always understood," she said. "You're the smartest bear in the world."  
"I'm sorry honeybee, Mathematics is a Premium Feature."  
  
The next morning, at breakfast, she asked her mom "what's a Premium Feature?"  
Her Mom stopped folding laundry and her face went blank for a moment, then she came over and sat down. "Sweetie, why are you asking that?"  
"Ginger can't do math anymore," she said. "Don't be mad if I get a D on my homework."  
"I see," said her mom, then she smiled and said "how about another egg?"  
"Really?" she said. "Another egg?"  
"Another egg!" said her mom, and then went and fried one up.   
  
That night, as she was going to sleep, she heard the sounds of her parents arguing. Her Mom was going on and on and she could hear her Dad talking in his low voice, occasionally raising it a little. Her Mom got louder as well. Eventually, they both got so loud she could make out the words.   
"I never had a talking bear," said her Dad, "and I turned out fine."   
"Things are different now," said her Mom. "All the other kids have it. What if she gets left behind? Schools aren't as good as when we were growing up. She needs it."   
"Where do we get the money from?"   
"I already bought the subscription."   
And then her Dad started shouting and he used swear words and then she heard her mom crying, then the house went quiet.   
She came out and her mom was watching TV on mute. "What's wrong mommy?"   
"Go to sleep honeybee," she said. "Do you want a glass of milk?"  
And they drank milk together then her Mom put her down to bed. 

The next day she got home from class and showed the homework to Ginger. "I told you I'd get a D," she said.   
"Do you understand why you got a D?" Ginger asked.   
She explained, then Ginger pointed to a part of her work and said "I think here is where you went wrong."   
She was so bound up in focusing on the problem that she didn't notice Ginger could do math anymore. 

In the other room, her Mom told her Dad "it'll just be a few days - I'll be back before you know it", and took a small travel case and left, heading for a warehouse experiencing a seasonal labor spike.

**Things that inspired this story:** Rich versus poor people in the singularity; the new classism will be about how much intelligence you have accessible 'at home'; markets and deployment; subscription metrics; gazing at my newborn child and realizing just how far I’d go to give them what they want and being afraid of how vulnerable that love makes me.
