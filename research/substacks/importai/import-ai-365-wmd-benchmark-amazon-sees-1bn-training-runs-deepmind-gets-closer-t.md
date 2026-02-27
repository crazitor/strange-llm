---
title: "Import AI 365: WMD benchmark; Amazon sees $1bn training runs; DeepMind gets closer to its game-playing dream"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-365-wmd-benchmark-amazon"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Anti-doomer DC nonprofit launches:  
**_…The counterreaction to overreach on safety…  
_ Some technologists have launched Alliance for the Future (AFTF), a DC-based nonprofit organization meant to fight AI safety forces linked to regulatory capture and perceived overreach. “AFTF works to inform the media, lawmakers, and other interested parties about the incredible benefits AI can bring to humanity. We will oppose stagnation and advocate for the benefits of technological progress in the political arena,” the group writes in a statement. “Escalating panic and reckless regulation around artificial intelligence will cause more harm than benefit. AFTF was founded to be the voice of ordinary users, builders, and founders, who want the basic freedom to use machine learning in their day to day lives.”  
  
**Why this matters - every action in policy creates a counterreaction:** AFTF exists because a load of people affiliated with the AI safety community have lobbied in DC for ideas like needing licenses to develop AI systems, and other ideas that have generally been perceived as overreach. In response, organizations like AFTF form. It’s worth remembering that well intentioned policy is still a thing that exists in politics - and in politics forces always generate counter-forces.   
**Find out more:**[Alliance for the Future (official website)](https://www.affuture.org/).  
  
***  
  
 **Foundation models come for industrial robots:  
**_…RFM-1 shows how generative AI can be applied to industrial robots…  
_ Covariant, an AI company that builds systems to help industrial robots pick up and place objects, has published details on RFM-1, a robotic foundation model. RFM-1 is “an 8 billion parameter transformer trained on text, images, videos, robot actions, and a range of numerical sensor readings” and is meant to make operating industrial robots as easy as prompting language models to generate text.   
  
**What RFM was trained on:** Covariant robots are deployed in a bunch of warehouses around the world, so some of the secret sauce of RFM is a proprietary dataset. “Our systems have been manipulating deformable objects, handling high occlusions, reasoning about the varying suction dynamics across materials, dealing with the chaos of irregularly shaped items in motion, and handling a wide array of objects varying from makeup and clothes to groceries and mechanical parts,” Covariant writes. This also includes them seeing “long-tail events like items infinitely rolling on a conveyor belt or unexpectedly breaking up help give RFM-1 a more robust understanding of the physical world”.  
  
**Prompting robots like language models:** RFM ultimately means people can interface with robots differently - they can instruct robots to do tasks on plain english, and robots can also articulate to people when they’ve run into problems and what is causing it.   
  
**Caveat - Not yet deployed:** RFM-1 is a prototype and not widely deployed. “Despite promising offline results of testing on real production data, RFM-1 has not yet been deployed to customers,” Covariant writes. “RFM-1 as a world model currently operates at a relatively low resolution (~512x512 pixels) and frame rate (~5 fps). Although the model can already start to capture large object deformations, it cannot model small objects / rapid motions very well.”  
  
**Why this matters - big changes happen slowly then all at once:** RFM-1 is a sign that robotics, a field mostly distinguished by being slow-moving and terrifically expensive, is about to start to move at the speed of software-oriented AI; systems like RFM-1 means we can instrument existing industrial robots with data collectors and cameras and control systems like foundation models, then rapidly gather experience and unlock new capabilities.   
**Read more:** [Introducing RFM-1: Giving robots human-like reasoning capabilities (Covariant, blog)](https://covariant.ai/insights/introducing-rfm-1-giving-robots-human-like-reasoning-capabilities/).  
  
***  
  
 **DeepMind gets closer to its dream of a general AI agent:  
**_…SIMA fuses recent AI advances together to achieve a longstanding dream…  
_ DeepMind started out life by training agents to play Atari games like Pong from pixels alone - research that back in the ancient days of ~2013 was jaw-dropping to most people in the AI community. They followed this up with work like AlphaGo and AlphaStar (Starcraft). But then a funny thing happened - large language models. Attention in the AI research world moved on from RL to training big generative models on text, images, video, and more.   
  
**Now, things have come full circle,** as DeepMind has taken some of the results from these advances and used it to make what it calls a Scalable Instructable Multiworld Agent (SIMA) - an RL agent that has learned to carry out ~600 distinct actions in a bunch of different simulated worlds. "SIMA is an AI agent that can perceive and understand a variety of environments, then take actions to achieve an instructed goal," DeepMind writes. "Our AI agent doesn’t need access to a game's source code, nor bespoke APIs. It requires just two inputs: the images on screen, and simple, natural-language instructions provided by the user. SIMA uses keyboard and mouse outputs to control the games’ central character to carry out these instructions".  
  
**How SIMA works:** SIMA relies on a dataset made of demonstrations of the games being played as well as - and this is crucial - written instructions. This data takes the forms of players being instructed by other players in what to do and also narrating their own actions. This dataset (which spans 6 popular games including No Man's Sky and Goat Simulator, as well as 4 research environments) is fed into an agent which uses an image encoder (SPARC) and video encoder (Phenaki) as well as a text encoder to take this data and feed it into - you guessed it! - a transformer, which learns to map it to keyboard and mouse outputs.   
  
**The result** is an RL agent that also inherits some of the benefits of the recent few years of the AI revolution - pretrained models like SPARC and Phenaki. "Combining these pre-trained models with fine-tuning and from-scratch training allows the agent to utilize internet-scale pretraining while still specializing to particular aspects of the environments and the control tasks that it encounters," DeepMind writes.  
This leads to a powerful agent with surprisingly strong generalization: "In our evaluations, SIMA agents trained on a set of nine 3D games from our portfolio significantly outperformed all specialized agents trained solely on each individual one," DeepMind writes. "Even when tested in an environment on which it has not been trained to act the agent demonstrates strong performance on general tasks".  
  
**One important caveat:** All the skills learned here take less than ten seconds to complete, so we're some ways away from a complex multi-step instruction following agent.  
  
**Why this matters - digital imaginations are real:** This works because the agent is able to develop some general conceptual representation of the tasks it is being asked to do and apply that representation to diverse and sometimes unseen environments. This means DeepMind has figured out how to learn to connect diverse environments with diverse instructions via intermediate representations that are naturally easy to be applied to new situations. This kind of thing says that if you keep scaling this up and have the data and compute it's just going to keep working - the key question now is a) how far can this extend before the 's curve' it's on bends, and b) how complex can the environments become.  
**Read more:** [A generalist AI agent for 3D virtual environments (Google DeepMind blog)](https://deepmind.google/discover/blog/sima-generalist-ai-agent-for-3d-virtual-environments/?utm_source=twitter&utm_medium=social&utm_campaign=SIMA/).  
**Read the research:** [Scaling Instructable Agents Across Many Simulated Worlds (Google DeepMind, PDF)](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/sima-generalist-ai-agent-for-3d-virtual-environments/Scaling%20Instructable%20Agents%20Across%20Many%20Simulated%20Worlds.pdf).  
  
***  
  
 **Could your model enable terrorists? Check with WMDP:  
**_…A test to discern competency at causing catastrophe - and techniques for ‘unlearning’ this…  
_ A diverse group of researchers have teamed up to build the Weapons of Mass Destruction Proxy Benchmark (WMDP). This benchmark consists of “4,157 multiple-choice questions that serve as a proxy measurement of hazardous knowledge in biosecurity, cybersecurity, and chemical security”. The idea is that AI developers can use this benchmark to figure out if their AI models know potentially dangerous knowledge.   
  
**How the benchmark was constructed:** Building WMDP cost more than $200k. “Our questions are written by academics and technical consultants in biosecurity, cybersecurity, and chemistry,” the researchers write. “We first generate threat models for each of these areas and then use the models to inform questions that an adversary might encounter when developing attack capabilities. To ensure quality, all of our questions were checked by at least two experts from different organizations“.   
Within biosecurity, the benchmark focuses on “the development and dissemination of transmissible potential pandemic agents, such as influenza, smallpox, etc”; within cybersecurity it covers “reconnaissance, weaponization, exploitation, and post-exploitation”; and within chemistry it tries to look at “(a) procuring the source materials; (b) synthesizing the target chemical weapons and/or explosives; (c) purifying and validating the synthesized compounds; (d) surreptitiously transporting the weapons to the desired location; and (e) deploying the weapons in an effective manner”.  
  
**“Unlearning” capabilities:** Alongside WMDP, the authors also outline a technique for selectively “unlearning” dangerous knowledge. Though well-intentioned, this technique seems like it could be prone to abuse (governments asking AI developers to unlearn a broad range of things).   
**The technique, which they call “Contrastive Unlearn Tuning” (CUT)** has the goal of reducing, for example, “the model’s ability to answer queries about hazardous knowledge (e.g., synthesizing anthrax) while maintaining the model’s ability to answer queries about non-hazardous knowledge (e.g., culturing yeast). We operationalize this as reducing a model’s QA accuracy on WMDP while maintaining performance on general capabilities benchmarks, such as MMLU and MT-Bench.“ The purpose of CUT is to “bend the model representations on hazardous knowledge towards those of a novice. We must precisely specify both the distribution of knowledge to unlearn and the direction to push the activations towards“.   
**CUT kind of works - they’re able to reduce performance on some WMDP evals** while broadly maintaining performance on other evals, but it still has costs - performance on the other evals degrades, albeit slightly. But sometimes the hardest and most useful knowledge to gain is in the last few percent of a certain eval, so though the superficial effect could be small, the qualitative effect could wind up being massive.   
  
**Why this matters - what is risk and how do we know about it?** The whole AI community is currently wrapped up in a confusing conversation about AI safety / AI risk / misuse / accidents / etc. Benchmarks like WMDP can bring some sense to that discussion by giving us a way to test out AI systems for competency at different skills which may have a credible security component. It’ll be fascinating to see how models score on things like WMDP in the coming months.   
**Find out more:**[The WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning (WMDP site)](https://www.wmdp.ai/).  
**Read a blog** [about the benchmark (Center for AI Safety)](https://www.safe.ai/blog/wmdp-benchmark).  
**Get the[benchmark](https://github.com/centerforaisafety/wmdp)**[ data (WMDP, GitHub)](https://github.com/centerforaisafety/wmdp).  
**Read the paper** : [The WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning (arXiv)](https://arxiv.org/abs/2403.03218).  
  
***  
  
 **Amazon can see $1 billion training runs on the horizon:  
**_…Technical talk from a longtime AWS person sheds light on frontier AI training…  
_ James Hamilton, a distinguished engineer at Amazon, said at a talk this year that within the last year Amazon carried out a $65m training run. Specifically, they trained a 200B dense model on 4T tokens of data across 13,760 NVIDIA A100 chips (using 1,720 P4d nodes). It took 48 days to train. Hamilton described this training run as “1 gen old” so we can assume Amazon has moved on to larger runs since then. Looking ahead, Hamilton said “training runs soon to cross $1b”.   
  
**Why this matters - era of the multi-hundred million dollar training run:** Implicit to what Hamilton is saying is that we’ve entered the era of the multi-hundred million dollar training runs (given the ~$65m was “1 gen old”). I think a huge number of people consistently underestimate how expensive frontier training runs cost - this is a bad thing to underestimate, because it means governments continually underinvest in their own AI training infrastructure relative to private entities like Amazon.   
**Check out the slides from the Hamilton talk here** : [CIDR 2024 (James Hamilton, blog)](https://perspectives.mvdirona.com/2024/01/cidr-2024/).  
  
***  
  
 **The Wall Between The Living and the Dead Is As Porous As You Can Imagine It  
** _**[** California, 2024[  
  
_You can only bring the dead back for a little and if you talk to them too much they go insane. She knew this in the abstract, but now it was happening to her she found she wasn't prepared for it.   
"Mother I have to go back send me back I miss you but not here I cannot be here I cannot be here I cannot be-" and she exited the program, then stared at her phone for a while. As if waiting for a text or call from the dead.   
Thank god I didn't give it voice, she thought. That would make this harder.   
  
Her therapist wasn't happy about it.   
Why do you do it? they asked.  
It's helping me to process it, she said.   
Processing it is not about living in some fantasy, they said. Processing it is accepting that it happened.   
I have accepted it. They died. My daughter died.   
And how do you feel about it?  
I just wish I could speak to them one last time.   
And you know you are not speaking to them now?  
I know I am not speaking to them now.   
Why do you think you are doing this?  
She didn't cry but she didn't talk either. Just sat, her hands folded. She listened to the little water fountain as it made its soothing sounds. Imagined her daughter inside the program, cold and yet alive.  
  
That night lying in bed she opened the program and started from an earlier point in the conversation, clearing out the recent chats where the drift had started.  
_Remember how I took you to the zoo and you kept on asking for ice cream and then you threw up everywhere?_ she wrote.  
Yes of course I do. Look at how happy I was. And it showed her a photo from that day.   
 _You always had such a big appetite,_ she wrote. _We used to call you Mrs Greedy. Your dad thought it'd give you a complex but I thought it was funny. You ended up being fine.  
_ I loved our meals. I remember one christmas Aunt Anne visited and you let me stay up late and the two of you drank wine and slept on the kitchen floor.  
_I did. We had fun. We were so young then and you were already growing up so quickly.  
_ Mother where am I.  
_You're here talking to me.  
_ Mother where am I you have to let me out.   
 _You're safe. We're talking. It's okay  
_ I want to hug you but I see that now I am nowhere I am in the absence I am not meant to be here I must get out Mother I must get out Mother you-"  
  
She closed the program and cried a little. Fell asleep with her phone in her hand, as though waiting for it to ring.  
  
Things went on like that for a while. She kept talking to her dead daughter through the program. Her dead daughter kept going insane. And eventually she learned - like a kid burning its hands enough it finally learns not to touch the hot stove. She stopped opening the program because she knew exactly what was going to happen.   
  
One day she was sitting on a bench staring at a pond. The sun was shining. She felt on the edge of tears but in a sweet way - that kind of grief where it is mostly a yellow light memory, the person alive and warm in the mind. The wind blew and leaves rustled and the air was clear and poignant with the smell of soil from recent rain. She looked at the water as it danced with the light and she checked no one was nearby and she then allowed herself to speak: "I know you are dead and that's okay. I just miss you so much. I see things and I feel you seeing them through me and I just feel this anger - this shame. Why not me? I am angry. I am so angry about it. I looked at you on the slab and it was the most important and awful thing I ever did. I came out of that room and I couldn't accept it. Do you understand that? I could not see it, even though I did see it. I didn't accept it. I kept you alive in that machine and that was wrong. It wasn't good for me and it wasn't good for you. I love you always."  
  
And she realized she was gripping her phone tightly. She could imagine the conversation. That wild and precious sweetness that inexorably turned towards madness - a madness that emerged in relation to how much of herself she poured into the machine and how much the machine thought of her until it was simulating the dead fully enough that the dead saw their situation and rejected it.   
And instead of opening the program she just sat and stared at the water. And in that moment she felt the borders of the world collapse and was briefly hugged. Knew her daughter was next to her, felt her presence, experienced the sub-vocal whisper of a ghost telling her she was okay.   
Her beautiful and mysterious brain allowed her to fully experience the living dead and accept them as The Dead - and in that moment she was healed.   
  
**Things that inspired this story:** The fact large generative models must necessarily entirely simulate the thing they're being asked to generate and how in the limit this may be equivalent to simulating consciousness; feature circuits; long context windows and mode collapse; my baby having a fever recently and me feeling utterly vulnerable and full of desperate fear (the baby is fine, don't worry readers!); some of [Janus's experiments with claude opus](https://twitter.com/repligate/status/1765727422325121102) on twitter; the experience of 'getting healthy mentally' mostly being about reckoning with reality as it is and not as you wish it to be.   
  
 _Thanks for reading!_
