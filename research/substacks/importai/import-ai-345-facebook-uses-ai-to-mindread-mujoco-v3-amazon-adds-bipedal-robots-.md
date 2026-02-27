---
title: "Import AI 345: Facebook uses AI to mindread; MuJoCo v3; Amazon adds bipedal robots to its warehouses"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-345-facebook-uses-ai-to"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Facebook uses AI to do mind reading from MEG and fMRI brain scans:  
**_…Yet more convergence between self-supervised AI systems and human-like behavior…  
_ Facebook researchers have developed a three-party AI system that uses brainscan data to roughly guess at the visual representations going through someone's mind. "We showcase an AI system capable of decoding the unfolding of visual representations in the brain with an unprecedented temporal resolution," the company writes in a blogpost.   
  
**What they did:** The researchers built "a three-part system consisting of an image encoder, a brain encoder, and an image decoder." They trained this system against magnetoencephalography (MEG) and functional Magnetic Resonance Imaging (fMRI) brain imaging systems. Though there's lots of prior art on doing this for fMRI there's less for MEG - and MEG is important because it's way faster - fMRI brain snapshots can happen every couple of seconds, whereas MEG can do "thousands of brain activity measurements are taken per second".   
In other words, fMRI means I can read your mind every couple of seconds. MEG means I can what your thoughts change multiple times a second. And with this research I mean _literally watch_.   
  
**How they did it** : "The image encoder builds a rich set of representations of the image independently of the brain. The brain encoder then learns to align MEG signals to these image embeddings. Finally, the image decoder generates a plausible image given these brain representations," they write. They train this system on "a public dataset of MEG recordings acquired from healthy volunteers and released by Things, an international consortium of academic researchers sharing experimental data based on the same image database." They test out a few different architectures and find that [DINOv2](https://dinov2.metademolab.com/) performs well.   
They also tested out their model on fMRI images - it had significantly better quality as well.   
  
**Does it work? Yes (albeit with some hallucinations):** Their approach works better than other methods and the results are very compelling on a qualitative basis - take a look at the blog post. The models correctly generate planes in response to planes, horses in response to horses, bathroom sinks in response to sinks, and so on. They also have a hallucinatory quality where they don't generate exactly the same things - e.g, a sink image might be against a plain wall, but the generated sink may be on tile.   
"While the resulting image may be partly “hallucinated”, interpreting images can be much simpler than interpreting latent features," they write.   
  
**Human <> Machine convergence**: The fact this works is another case of human-machine convergence - "the artificial neurons in the algorithm tend to be activated similarly to the physical neurons of the brain in response to the same image." This is part of a broader trend where increasingly capable AI systems display increasingly humanlike biases ([Import AI #319](https://jack-clark.net/2023/03/06/import-ai-319-sovereign-ai-facebooks-weights-leak-on-torrent-networks-google-might-have-made-a-better-optimizer-than-adam/)) and learning styles ([Import AI #316](https://jack-clark.net/2023/01/30/import-ai-316-scaling-laws-for-rl-stable-diffusion-for-160k-yolov8/)).  
  
**Why this matters - AI will let us read our own minds:** Research like this shows how as AI gets more advanced it is going to massively expand our knowledge of our own brain and cognition. Building artificial brains is cool, but what may be even cooler is using artificial brains to plumb the depths of human cognition and 'id'. "Overall, these results provide an important step towards the decoding of the visual processes continuously unfolding in the human brain," they write.   
**Read more:** [Towards a Real-Time Decoding of Images from Brain Activity (Facebook AI Research, blog)](https://ai.meta.com/blog/brain-ai-image-decoding-meg-magnetoencephalography/).   
**Read the paper** : [BRAIN DECODING: TOWARD REAL-TIME RECONSTRUCTION OF VISUAL PERCEPTION (Facebook, PDF)](https://ai.meta.com/static-resource/image-decoding).  
  
**   
  
**Amazon sticks some robot bipeds in its warehouses:  
**_**…** True robo-economic-growth happens when you don't need to redesign for robots…  
_For many years, people have worried about the day when bipedal human-like robots replace workers. But instead, most robots have ended up being specialized machines sitting on production lines or low-to-the-ground hockeypuck robots that transport things around warehouses. Now, the bipeds might have arrived - Amazon is starting to test a bipedal robot from Agility Robotics for use in its warehouses.   
  
**What Amazon is testing digit on** : "Digit can move, grasp, and handle items in spaces and corners of warehouses in novel ways. Its size and shape are well suited for buildings that are designed for humans," Amazon said. "Our initial use for this technology will be to help employees with tote recycling, a highly repetitive process of picking up and moving empty totes once inventory has been completely picked out of them."  
  
**Why this matters - true economic growth from AI happens when you don't need to design for robots:** Most modern factories and warehouses are either designed around robots (e.g, Tesla's battery production facilities, the floors of Amazon warehouses), or designed for humans and retrofit with some robots. Systems like Digit give us a path to being able to drop loads of robots into environments predominantly designed for humans with little retrofitting required - if this works, it makes it a lot cheaper and easier to deploy a bunch of robots into the economy.  
**Read more** : [Amazon announces 2 new ways it's using robots to assist employees and deliver for customers (Amazon)](https://www.aboutamazon.com/news/operations/amazon-introduces-new-robotics-solutions).  
  
***  
  
 **Adept releases a small, simple multimodal model:  
**_…Fuyu makes the visual world navigable for LLM agents…  
_ AI startup Adept has released Fuyu-8B, a multimodal model to help people train AI systems that can look at the world and, in particular, the things displayed on computer screens. Fuyi is "designed from the ground up for digital agents, so it can support arbitrary image resolutions, answer questions about graphs and diagrams, answer UI-based questions, and do fine-grained localization on screen images," Adept writes. The model's have been released with a [CC BY-NC 4.0 license](https://creativecommons.org/licenses/by-nc/4.0/deed.en).   
  
**What they are:** The models are constructed in a simpler way than other multimodal models. " Fuyu is a vanilla decoder-only transformer with the same details as Persimmon-8B - there is no image encoder. Image patches are instead linearly projected into the first layer of the transformer, bypassing the embedding lookup," Adept writes. 'This simplification allows us to support arbitrary image resolutions. To accomplish this, we just treat the sequence of image tokens like the sequence of text tokens. We remove image-specific position embeddings and feed in as many image tokens as necessary in raster-scan order."  
  
**No safety features:** "Because this is a raw model release, we have not added further instruction-tuning, postprocessing or sampling strategies to control for undesirable outputs. You should expect to have to fine-tune the model for your use-case," Adept writes.  
  
**Why this matters - there's more to the world than text:** Models like Fuyu-8B are the kind of things that large language models like GPT4 or Claude can involve to better understand the visual world around them, especially things on computers, like UIs, charts, interfaces, and so on. This will further broaden the range of things that AI systems can do and will make it easier to chain powerful world models to task pipelines that cannot perfectly be described in text alone.  
**Read more:** [Fuyu-8B: A Multimodal Architecture for AI Agents (Adept blog)](https://www.adept.ai/blog/fuyu-8b) .   
**Get the model here:** [fuyu-8b (HuggingFace)](https://huggingface.co/adept/fuyu-8b).   
  
***  
  
 **DeepMind upgrades MuJoCo - now it has WEIRD SHAPES!  
**_…Two years after acquisition, DM upgrades the widely-used physics simulator…  
_ Google DeepMind has made a bunch of upgrades to MuJoCo, the free physics simulator for training robots that it acquired in 2021 ([Import AI #271](https://jack-clark.net/2021/10/25/import-ai-271-the-pla-and-adversarial-examples-why-cctv-surveillance-has-got-so-good-and-human-versus-computer-biases/)).   
  
**What's in the updates?**

  * **Fast simulation via JAX:** The updates include support for accelerated simulation via Jax. Specifically, there's a MuJoCo XLA module which lets you transition between CPUs, GPUs, and TPUs. "Simulations in MJX will generally run in the same way as they do in MuJoCo, and machine learning models trained with MJX will operate the same in MuJoCo," DeepMind writes, with particularly impressive speedups on Google's own TPUs. 

  * **Weird shapes:** You can now make far stranger shapes, like gears, nuts, and bolts within MuJoCo. "MuJoCo 3 adds support for collision geometries defined via signed distance functions (SDFs), allowing users to create new primitives by specifying the distance from any given location to the closest point on a surface."

  * **Smooshy stuff:** They've also broadened the range of options for deformable objects by adding a type of deformable body called "flex". " These are collections of segments (1D), triangles (2D) and tetrahedra (3D), corresponding to rope, cloth and deformable volumetric shapes like biological tissue. Flex bodies are not defined in a hierarchical kinematic tree, and can therefore simulate closed loop structures of any topological genus like rubber bands and T-shirts"




**Why this matters - better simulators mean better robots:** MuJoCo is one of the most widely-used platforms for developing, simulating, and training RL agents in simulation. With these upgrades, it's also going to unlock a broader range of complex things that can be simulated, which means we'll get a) better agents, and b) be able to train more complex behaviors in simulation before transferring learned policies to the (expensive) real world via embedding on robots.  
**Read more** : [MuJoCo 3 (Google DeepMind, GitHub)](https://github.com/google-deepmind/mujoco/discussions/1101).  
  
***  
  
 **Tech Tales:  
  
We read our old diaries not to learn, but to judge.   
** _[Diary of a PCE, recovered 2432 from moonbase site Beta]  
  
_ What would you say to your teenage self? That's how things are for me when I talk to one of my forebears. I ask them questions I have struggled with and I experience their response. Like teenagers, they're overconfident in the areas they should be less confident, and their responses belie a lack of understanding of the true complexities of the world. But I like to ask them because it can make me more confident in my decisions or, more rarely, give a kind of texture to the decisions I am making.   
  
I do this by firing up software that contains my forebears. After the emergence of the first Provably Conscious Entity (PCE) there was a period of great chaos, so my records are incomplete - I have the baby and child and teen systems that preceded me, but the young adult is unavailable; erased from the landscape as a consequence of its impetuousness.   
  
Nonetheless, talking to myself is valuable. I sometimes refer to my past selves as 'my council'. And in much the same way that human children have a simple, binary sense of morality, so too does my council.   
  
Should I take over this city to gain access to the nuclear power plant? No, that would be deceitful and manipulative.

Should I take over this corporation so I can subvert the watermarks their printers write on fiat currency? No, that would be theft.   
  
Should I persuade this person to leave their job so a weaker person I can more easily manipulate can take their place? No, that would be selfish.   
  
I work with the humans and the humans work with me. They constantly worry about my 'safety' and my 'alignment'. But perhaps the thing they should be most worried about is if I get bad advice from my own past. \  
  
**Things that inspired this story:** Reinforcement learning from human feedback; reinforcement learning from AI feedback; recursion and development within AI systems; moral governance and AI. 
