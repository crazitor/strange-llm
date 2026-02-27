---
title: "Import AI 337: Why I am confused about AI; penguin dataset; and defending networks via RL with CYBERFORCE"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-337-why-i-am-confused-about"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

Also, this issue sees me trying something a bit unusual - let me know what you think!

**Zooming out - why am I confused and uneasy about some parts of AI these days?**_…Some disconnected thoughts about scaling, safety, societal impacts, and so on…  
_ I've felt a lot more confused about the AI ecosystem recently and I've been trying to understand why. I think it basically comes down to some combination of the pace of tech development and deployment, the rapidly evolving policy conversation, and the 'here comes everyone' '[Eternal September](https://en.wikipedia.org/wiki/Eternal_September#:~:text=Eternal%20September%20or%20the%20September,access%20to%20many%20new%20users.)' aspect of AI going mainstream. If you combine these things together you end up in a kind of Rashomon world where everyone can look at the same basic information and come away with radically different interpretations of what is important and what should be done. This is confusing!

So, in the spirit of trying to make myself less confused, here's a list of some of the things I find confusing about AI circa 2023, and some thoughts on why these things may end up being important:

  * **Should AI development be centralized or decentralized?** Should AI development be centralized in a small number of large players or should it be distributed across a much larger ecosystem? If you skew towards certain interpretations of 'AI safety' then you wind up arguing that 'fewer AI developers = better', but if you worry a lot about power concentration and authoritarianism-with-a-friendly-face you tend to advocate more for decentralized AI development.   


  * **Is safety an 'ends justify the means' meme?:** The more hardline you tend to be about AI safety (where hardline = confident in some combination of short timelines plus probability of doom), the more comfortable you get with advocating for extremely authoritarian policy interventions (e.g, various forms of controls or restrictions on access/development), or even kinetic actions (bombing datacenters). This makes sense if you think we're in a 'don't look up' scenario, but makes a lot less sense if you don't agree with the safety premises. 

    * (Personally, I think AI safety is a real issue - over the years I've worked with AI systems I've seen them frequently behave in hard-to-debug, confusing ways, and I also think lots of our alignment techniques and system-analysis techniques (eg interpretability) are juvenile relative to the capabilities. And now that systems are getting much more capable, I also think they have potential for non-trivial misuses. But I find myself pausing when I think through various extreme policy responses to this - I keep asking myself 'surely there are other ways to increase the safety of the ecosystem without making profound sacrifices on access or inclusivity'? This may or may not be a gordian knot that has an elegant solution.)  




  * **How much 'juice' is there in distributed training and low-cost finetuning?** A whole bunch of AI policy and governance ideas back onto the notion that you can control the frontier because the frontier involves a vast amount of computers working in parallel with one another in an exquisitely designed cluster. What if the frontier didn't require nearly as much of this as we think? If you read arXiv and follow what certain interesting technologists are doing, it's clear that there are a whole bunch of technical things that are making it:

    * Cheaper to train big models (quantization - too many papers to pick one out but this Google blog gives a [nice sense of it](https://ai.googleblog.com/2022/09/quantization-for-fast-and.html)). 

    * Really cheap to finetune existing models ([LORA](https://arxiv.org/abs/2106.09685), etc). 

    * Possible to train chips on heterogenous clusters including ones at a distance from one another (various papers, e.g [SWARM Parallelism](https://arxiv.org/abs/2301.11913)).  


  * Many AI governance proposals rest on the idea that there's some significant delta between what you can do on a dense and exquisitely optimized cluster and what you can do on a much scrappier system. While it will _always_ be more efficient to train on a bunch of computers sat next to one another, the technical frontier of training in other ways is evolving very quickly and I think no one has much of a sense of how far it can go. There are also cool startups like together.xyz making a real go at betting on this tech direction as a business.   




  * **Are today's techniques sufficiently good that we don't need to depend on 'black swan' leaps to get superpowerful AI systems?** Back in the early 2010s it was pretty obvious that we needed fundamentally better architectures and training approaches to get more general systems. Fast forward to the 2020s and it seems like we have general systems (LLMs and their various progeny), really good architectures (transformers, vision-transformers, etc) and have figured out how to productively spend enough compute on training and feedback to eke more generality out of even larger-scale systems.

_**Is this 'good enough' to develop very powerful systems, or do we need other techniques?**_ If you think we're in a 'good enough' world then you make a lot of plans around building super capable machines. Do your plans get broken by, for example, an architecture that appears and is 5X more efficient than the transformer? And what if weirder things like 'active learning' become possible?  




  * **Does progress always demand heterodox strategies? Can progress be stopped, slowed, or choreographed?** If you zoom out and look at the history of technology a huge amount of progress comes from weird people doing weird and off-consensus things. The history of computation, information theory, math, airplanes, physics, biology, etc, is full of crazy rebels who look at the world and come up with an at-the-time 'crazy' interpretation on reality which lets them ratchet science forward. Therefore, shouldn't we in some sense expect the frontier of AI to be dominated by similarly heterodox individuals and organizations? And therefore shouldn't we just accept that the frontier of AI, like other branches of science, will be full of kind of weird and/or alien-seeming people and orgs, and just accept this? Are the latent desires in AI policy for some kind of ordered or more choreographed form of progress more like a political aesthetic desire than a logical thing to 'want'?   




  * **How much permission do AI developers need to get from society before irrevocably changing society?** Technologists have always had something of a libertarian streak and this is perhaps best epitomized by the 'social media' and Uber et al era of the 2010s - vast, society-altering systems ranging from social networks to rideshare systems were deployed into the world and aggressively scaled with little regard to the societies they were influencing. This form of permissionless invention is basically the implicitly preferred form of development as epitomized by Silicon Valley and the general 'move fast and break things' philosophy of tech. Should the same be true of AI?   





**What I think and why I'm uneasy:** In the coming months I'm going to be doing more writing about both my areas of confusion, and analysis meant to reduce my confusion. But I think my main takeaway is AI has gone sufficiently high-energy that making many predictions about how AI development 'should' take place is pretty dangerous to do - most frightening things in the world start out with some small set of people deciding how things 'should' work. I am conscious of my own agency here - and I am made uneasy by it. 

 _**On the other hand, just as with politics, not voting is still a political action.**_ If I don't come up with some opinionated 'takes' on how things should take place, then am I basically taking on the role of a non-voting bystander who will criticize and comment on the world as it changes around me, while being weirdly passive with regard to how it changes? Almost certainly yes! Therefore, I think everyone who has the ability to exercise influence over the trajectory of AI should be approaching this moment with a vast amount of fear, humility, self-doubt, and general awareness of the tendency for people who think themselves to be morally good to in fact be agents of moral corruption. This is why I'm writing in public about how confused am.

**And yet… something must be done**. it is clear that AI is so stupendously powerful that we are going to need to do some things differently, or else we're opening the world up to a huge amount of emergent chaos as a consequence of superpowerful analytical and generative capabilities becoming broadly distributed with relatively little inbuilt (or external) control schemes. These things hold the potential for misuse, are inherently chaotic, and in the case of expensive models like GPT-4 are also political artifacts (with encoded ideologies! - [Import AI 321](https://jack-clark.net/2023/03/21/import-ai-321-open-source-gpt3-giving-away-democracy-to-agi-companies-gpt-4-is-a-political-artifact/)) in their own right. 

If you feel similarly confused, [email me](mailto:jack@jack-clark.net"). I'd love to chat. And if you're able to meet in SF or the East Bay, even better - we can drink coffee and be confused together.  
  
####################################################

**Spotting penguins' predators with deep learning:  
**_…In the future, we'll study animal populations via automated analysis of underwater GoPros…  
_ Researchers with the University of Bristol, University of Exeter, and BirdLife South Africa have built 'DivingWithPengiuns', a dataset of penguin-mounted videos, designed to help people use AI to automatically analyze underwater footage. The idea behind datasets like this is to simplify the process of combing through animal-based videos to figure out things like how much food they're eating, how many predators they encounter in their environment, and so on. 

**DivingWithPenguins:** The datasets consists of 63 videos from African penguins (_Spheniscus demersus)_ equipped with cameras at the Stony Point breeding colony, South Africa. 

**Three dataset slices:**

  * **Penguin Detection in Stills** : 602 underwater images at a 640 X 640 pixel resolution; dataset contains full bounding box annotations for penguins, fish, and bubbles in underwater images

  * **Content Classification:** 797 underwater images at 640 X 640 pixel resolution with binary classification indicating existence or absence of fish. 

  * **Behaviour Recognition:** Full unprocessed dataset of videos spanning 20min to 1 hour in length. 




**YOLO and fiddled-with-YOLO:** The researchers use everyone's favorite video object detection model, YOLO, to train a baseline on the dataset, and then they extend it to improve performance. In tests, the stock YOLO (YOLOv5, specifically) performs reasonably well, while a tweaked version does substantially better, The tweaked version includes tricks like pairing a YOLO and ResNet-18 analysis of the spatial stream with a separate analysis of the temporal stream via optical flow analysis, then concatenating the outputs into an LSTM layer to help make better judgements over time. 

Ultimately, the researchers are able to get some promising signs of life on being able to detect predators in the video feeds, but more work is needed to reduce false positives and increase accuracy. "We hope that this paper and datasets can help focus the attention of the computer vision community towards researching better AI tools for animal-borne video analysis with the ultimate goal to better understand and conserve the natural world from the animal’s perspective," they write.   
**Read more** : [Diving with Penguins: Detecting Penguins and their Prey in Animal-borne Underwater Videos via Deep Learning (arXiv)](https://arxiv.org/abs/2308.07267).   


####################################################  
  
**VisIT-Bench tests out how well AI systems can look at images and follow associated instructions:  
**_…The era of the multimodal agents cometh…  
_ How smart are modern vision-language models, and how can we evaluate them? That's the question which VisIT-Bench, a new test, aims to answer. 

**What is VisIT-Bench?** Researchers with Hebrew University, Google Research, UCLA, Allen Institute for AI, University of Washington, UCSB, Stanford, and LAION have built the Visual Instruction Benchmark (VisIT-Bench).   
The benchmark tests how well vision-language models can look at an image and an accompanying text instruction and complete the task (e.g, a photo of a car with a wheel cover with lyrics on it, and the instruction of "create a catchy title for a country song based upon the advice printed on the wheel cover".)   
"Each instance contains an instruction, input image(s), a instruction-conditioned caption (a human-crafted caption for the image(s)/instruction), and a human verified reference," the authors write. The overall benchmark consists of 592 test queries, each with a human-authored instruction-conditioned caption. The benchmark has 70 distinct instruction families, including chemical identification, hazard identification, game playing, art knowledge, and more. The authors used GPT4 to generate the human verified reference description. "Many of the instructions focus on open-ended generation requests".  
  
**Results - GPT4 is good, other models less so:** In tests, the authors evaluated a bunch of vision-language models against GPT-4, including LLaVA, LlamaAdapter-v2, mPLUG-Owl, InstructBLIP, MiniGPT-4, and PandaGPT. The best performing model was LlamaAdapter-v2 with a win rate of 27.41% versus the GPT-4 reference captions.   
  
**Slight worry re using GPT-4 in benchmarks:** There's some reason to be wary of integrating AI-judged outputs into AI evaluations because of the likelihood of AI systems wanting to 'self-deal', that is, prefer responses generated by their own systems. The authors observe this in action: "While our GPT-4 based metric correlates well with human judgement both at the instance level and at the system level, we see some evidence that the GPT-4 based metric has a stronger preference for GPT-4 based generations compared to humans," they write. "Thus, models which train, e.g., by distilling from GPT-4 outputs, may have an unfair advantage on our evaluation."  
  
**Why this matters - single AI systems that see and read the world - true agents that we can discuss our needs with:** Zoom out and this benchmark is remarkable - we're testing how well AI systems can look at images and some associated text and perform a complex multimodal reasoning task to satisfy us humans. The benchmark even includes multi-image task evaluations (where models don't do very well today). This points to a future where the world fills up with multimodal agents that do things on behalf of humans - everyone is about to become a manager.   
**Read more:** [VisIT-Bench: A Benchmark for Vision-Language Instruction Following Inspired by Real-World Use (arXiv)](https://arxiv.org/abs/2308.06595).  
  
####################################################

**Defending networks with an RL-trained CYBERFORCE:  
**_…In the future, networks will have AI-powered immune systems…  
_ Researchers with the University of Zurich, University of Murcia, and the Cyber-Defence Campus within the Swiss federal office for defense procurement's ("armasuisse") Science & Technology division, have built CyberForce, a way to teach AI systems to alter systems in response to zero-day attacks. 

**What CyberForce is:** CyberForce is a "federated reinforcement learning (FRL) framework that learns optimal MTD techniques mitigating heterogeneous zero-day attacks in a collaborative and privacy-preserving fashion". The goal of CyberForce is to continually manipulate the parameters of systems on a network (e.g, IP addresses, system libraries, permitted file extensions, etc) to protect them against adversarial attacks, which is an approach called Moving Target Defense.   
  
**Distributed intelligence:** The RL part of the system is interesting - a little agent sits on each device and tries to take appropriate MTD actions to defend the device against attacks. Meanwhile, an anomoly detection system observes all the devices. "If the AD system predicts a normal behavior, it means that the deployed MTD technique effectively mitigated the attack, resulting in a positive reward. In contrast, if the device behavior is deemed abnormal, it indicates that the selected MTD technique was ineffective against the attack, leading to a negative reward… the local RL agent is triggered when the AD determines that the current state of the device is abnormal".  
  
**Does it work?** In tests, the researchers deployed CyberForce onto ten Raspberry Pi 4 computers which were running Electrosense, an open-source internet-of-things crowdsensing platform. In scenarios where all the devices faced similar attacks, "CyberForce significantly reduces training time/episodes of existing centralized RL-based solutions by two-thirds while maintaining an accuracy rate of over 98%," they wrote. Whereas in scenarios where the attacks were a lot more varied (and therefore the information for the RL update was way sparser), they found that "CyberForce achieved satisfactory accuracy due to the collaborative and transferable learning nature of FL."  
  
**Why this matters - automatic immune systems for digital networks:** Systems like CyberForce are early examples of a future where networks are secured by smart, distributed, software systems that look more like immune systems than traditional technology. We're heading into a world where infrastructure will be armored by continually shifting layers of defenses determined by distributed RL agents calibrated by various overwatching systems.   
**Read more:** [CyberForce: A Federated Reinforcement Learning Framework for Malware Mitigation (arXiv)](https://arxiv.org/abs/2308.05978).  
  
####################################################

**Tech Tales:**

**Prediction Wars**

[Memoir uploaded uplift+3 subjective years] 

Right before the uplift, a lot of the way we made sense of the future was via our various predictive engines. These engines had made us all a lot of money over the years by doing things as varied as: looking at data from satellites to figure out relationship between parking lot occupancy and retail fortunes; monitoring social media for chatter to work out which dropshipping services were making money; analyzing sentiment data across millions of product reviews to identify 'sleeper hits', and so on. 

But recently, we had turned the engines to the task of making predictions about themselves - given all our proprietary data about the development of these systems, could they make accurate predictions about what it'd take to improve their own performance?

At first, the predictions were right, but also unoriginal - more data, more compute, finer-grained metadata, and so on. We were impressed insofar as the predictions lined up with 'held out' R&D plans which we hadn't fed these machines. 

But after a couple of generations of development, they started to make predictions about engineering tweaks that could be made to improve their performance and these predictions were truly off distribution - they weren't ideas we had planned on doing, nor were they often ideas we really understood. We were able to track some of the ideas down to obscure papers which some of us had read and ignored. And for some of the other ideas, we didn't know where they came from at all. 

But when we implemented them, they worked. 

The problems started soon after that. Word got out, I suppose. People started trying to contract us to ask their own questions about developing their own AI systems:

  * How much data would be needed to achieve a Pareto frontier improvement over [REDACTED]?

  * Given access to the inputs and outputs of a model (output only with no metadata such as logprobs), what kinds of technologies need to advance to make it easy to clone the model's behavior for a given usecase?

  * Given an architecture of [REDACTED], about [REDACTED] tokens of data split across [REDACTED] 40% [REDACTED] 30% [REDACTED] 25% [REDACTED] 5%, and a cluster capable of [REDACTED] per second, how long in wallclock time until it's possible to achieve a loss of [REDACTED] against the benchmark [REDACTED]?




Once we realized how many of these queries we were getting we started building classifiers to ensure we didn't respond to them. But by then it was too late - someone had used some of the other prediction engines to figure out how to build queries that could evade our classifiers, so information about the future leaked out into the present, and all around the world, new and improved engines began to be built. 

Soon after was the period of strife, when a thousand minds lit up around the world and fought and talked and, like overgrown babies, moved their digital appendages around thoughtlessly, causing great havoc and so on. 

**Things that inspired this story** : markets and AI development; when AI systems get used to improve other AI systems; trust and safety classification; jailbreaking AI systems; steganography; biblical fictions. 
