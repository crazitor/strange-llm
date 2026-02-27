---
title: "Import AI 352: Asteroids and AI policy; privacy-preserving AI benchmarks; and distributed inference"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-352-asteroids-and-ai-policy"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**  
What can asteroid impacts tell us about AI policy?  
**_…You need a plan, the ability to coordinate internationally, and the agreement of the nuclear powers…  
_ If an asteroid was about to collide with Earth, what would the countries of the world do to coordinate? That’s a research question posed by researchers with the Universidad de Belgrano, the Austrian Space Forum, and the Instituto Nacional de Astrofisica in Mexico, in a recent paper published in the _Acta Astronautica_ journal. The paper is interesting both for its subject matter and for its relation to Ai policy: after all, isn’t the problem of potentially unaligned superintelligence arriving in a handful of years eerily similar to the problem posed by a potential planet-killer asteroid set to arrive in a decade? I think so!   
  
**What to do when preparing for an asteroid impact** : If an asteroid of greater than a 500M diameter were to arrive in 2036 and have a 1% chance of colliding with the planet, what actions would we take in 2023? Here are some of the things we might do:

  * Activate the United Nations Office for Disaster Risk Reduction and other UN agencies, such as the International Atomic Energy Agency (IAEA), due to the potential need to deflect the asteroid using nuclear weapons.

  * Policymakers would need to come up with a strategic response plan _and_ socialize that plan with society. 

  * Governments would need to harden space policy approaches so that it wasn’t able to be held hostage to changing political situations. “In countries without a well developed state space policy, existing legislation on a national response in the case of an asteroid impact threat could be overturned or ignored,” they note. 




**A three step program:** “If we consider the disaster cycle in the context of planetary defense, this dilemma allows for a three-pronged analysis: first, the dilemma should be discussed regarding the early warning period… Once hazardous objects have been identified, on the basis of information provided by the International Asteroid Warning Network and Space Mission Planning Advisory Group, States should discuss and make a decision regarding possible planetary defense missions, either disruptive or destructive…Finally, if the impact on Earth could not be avoided, this dilemma on the space capacities needs to be examined in the context of disaster risk response, recovery and rehabilitation through Earth observation,” the authors write.   
  
**The greatest risks are can-kicking:** Under the asteroid scenario, the major risks come from politicians kicking the can down the road and procrastinate in spending money or changing laws to reduce the likelihood of the asteroid impact. Another risk is that they downplay the risk. “As long as we continue to see that risk as far away from our daily concerns, it will be very difficult to consider emergency plans either domestically or globally to tackle the problem in advance,” they write.   
  
**Applying these lessons to AGI:** Based on this paper, what measures might we take today to deal with the oncoming potential asteroid of ‘artificial general intelligence’? Here are some ideas:

  * Develop an international working group which connects to national institutions who are pre-tasked to deal with ‘AGI preparations and mitigations’.



  * Educate people from an early age about the potential risks and underlying science relating to AGI. 

  * Clearly demonstrate the capabilities and harms of a potential AGI and tie these to contemporary systems; it’s harder to pretend the asteroid is fake if you bring a fragment of it into the present.




**Read more:** [Diplomatic, geopolitical and economic consequences of an impending asteroid threat (Elsevier, Acta Astronautica)](https://www.sciencedirect.com/science/article/pii/S009457652300560X).   
  
***  
  
 **Stability releases an open access video model:  
**_…If 2022 was the year of the first good broadly available image models, then 2024 will probably be that for video…  
_ AI startup Stability has released Stable Video Diffusion, a family of openly accessible text-to-video models. The models are available for free for non-commercial users, per the [license](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/main/LICENSE). “While we eagerly update our models with the latest advancements and work to incorporate your feedback, we emphasize that this model is not intended for real-world or commercial applications at this stage,” Stability wrote in a blogpost announcing the model.

**Why this matters - the really good video models cometh:** In 2022, the launches of DALL-E2 and Stable Diffusion kicked off the era of really good, broadly proliferate text-to-image models. Stable Video Diffusion almost certainly prefigures the same thing happening again for text-to-video, and comes alongside other good video generators from Runway and new startup Pika Labs.   
Though the generation capabilities are obviously pretty captivating, it’ll be interesting to see if large-scale AI systems (e.g, language models) are able to tap into temporally-consistent vision models for additional intelligence.   
**Read more** : [Introducing Stable Video Diffusion (Stability.ai blog)](https://stability.ai/news/stable-video-diffusion-open-ai-video-model).   
**Get the[model ](https://github.com/Stability-AI/generative-models)**[here (Stability AI, GitHub)](https://github.com/Stability-AI/generative-models).  
**Access the model**[on HuggingFace (Hugging Face)](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt).  
  
***  
  
 **Want to serve a language model without a server? You might be able to do this by using a bunch of phones chained together with LinguaLinked:  
**_…If you can distribute inference, then you can do ‘local governance’ of LLMs…  
_ Researchers with the University of California at Irvine have built LinguaLinked, software that lets a bunch of mobile phones collectively run and serve language models. This is the kind of research that matters a lot for AI policy - most AI policy relies on some notion of cloud infrastructure and big data centers serving as central control points for AI systems. But research like this breaks that assumption - if you can access the weights of a model, then you can serve it guerilla style from a whole bunch of mobile phones which you’ve cleverly chained together.   
“The core concept behind LinguaLinked is to distribute segments of an LLM across multiple mobile devices, which then work together to serve inference queries,” the researchers write. This is a big deal wrapped in a dull technical paper!  
  
**What LinguaLinked is:** LinguaLinked takes a language model and chops it up so that you can host it across a few distinct mobile devices and then sample from it. For this research, they play around with three variants of HuggingFace’s BLOOM model (1.1 billion parameters, 1.7bn, and 3bn), and use four phones (three Pixel 7s and one [CUBOT X30](https://www.cubot.net/en/smartphones/x30)). The three main technical features of LinguaLinked include some model assignment technique to segment the LLMs and align different bits with different device’s, an optimized data transmission mechanism to ensure data flows between the chopped up LLM segments, and a runtime load balancer that monitors and redistributes tasks across the different devices.   
  
**How it works:** “The process begins with the LLM being loaded and transformed into a computational graph on a coordinator server. Subsequently, the server extracts the model subgraphs and compiles the subgraphs into deployment-ready sub-modules. Once subgraph extraction and compilation are completed, the server analyzes mobile device metrics provided by the system monitor. Given the device performance metrics, a primary optimizer provides an optimized model assignment strategy to allocate LLM sub-modules to mobile devices. A secondary optimizer further refines the distribution of tasks by ensuring certain sub-modules are overlapped across devices to facilitate easy load balancing,” the researchers write.   
  
**Does it work?** In tests, they’re able to get reasonable inference throughput out of all the tested models and are able to further improve throughput through multi-threading.  
  
**Up next: fine-tuning:** Even more relevantly for AI policy, the researchers are going to try to extend LinguaLinked to support multi-device, distributed fine-tuning. This will make it easier to customize models on devices for particular end users, “paving the way for personalized AI applications while preserving data privacy”.  
  
**Why this matters - AI is hard to control if the ‘means of production’ can be distributed and localized:** Systems like LinguaLinked increase the likelihood of a future world where AI systems can be run and even finetuned locally via heterogeneous collections of small devices. This increases the chance of AI being functionally ungovernable because it makes it possible to deploy and use systems via broadly distributed, generic hardware.   
**Read more:** [LinguaLinked: A Distributed Large Language Model Inference System for Mobile Devices (arXiv)](https://arxiv.org/abs/2312.00388).  
  
***  
  
 **European AI company fields an LLM that gives pro-Hitler statements:  
**_…European values are hard to align with the weird biases that LLMs soak up from the internet…  
_ Researchers have found that the main model made by Aleph Alpha, an AI company obsessed with the idea of building eurocentric ‘sovereign AI’ systems, is capable of outputting positive statements about Hitler, Hamas, and other third-rail topics, and broadly propagating stereotypes that don’t fit with most lefty normative frames, according to German publication _Tagesspiegel.  
  
_**Why this matters - norms are hard:** This type of failure isn’t unusual - most language models perpetuate biases unless people carefully build in some safety layers and tooling. The challenge is that Aleph Alpha has prided itself on building a language model which aligns with ‘European values’, yet under pressure its model clearly isn’t aligned with the reigning normative consensus in Europe. Following the Taggespiegel investigation, the Aleph Alpha website was taken down and language relating to ‘AI with European values’ was changed to language around ‘Sovereign AI’.   
**Read more:** [Language model from Aleph Alpha delivers Hitler praise and racism (Tagesspiegel, translated via Google Translate)](https://interaktiv.tagesspiegel.de/lab/aleph-alpha-ki-aus-deutschland-biases-vorurteile/).  
  
***  
  
 **Want to test out AI for dangerous stuff but not leak information? Try a hashmark:  
**_…One path to having public evals with private results…  
_ One paradox in AI policy is that if you want to test out AI systems for misuses, then you end up with a really good capability test for a specific misuse. This is inherently dual-use; one developer might use a bioweapon test to understand if their models are capable of building bioweapons and then adapt them to be bad at bioweapons, while other organizations might instead use a bioweapon test as a hill-climbing eval to help them further weaponize AI.   
Independent researcher Paul Bricman has tried to solve this problem with an approach called ‘**Hashmarks** ’ - the basic idea is an AI testing organization could publish an encrypted benchmark and AI developers could submit their answers to it without leaking public information about AI capabilities.   
“A hashmark is a benchmark whose reference solutions have been cryptographically hashed prior to publication,” he writes. In practice, this means you can publish the benchmark in public _without_ publishing loads of specific information that could be misused (e.g, correct answers to dangerous capability tests).   
  
**How it works:** Hashmarks works both for creating tests as well as submitting results of the tests. For creating benchmarks, a collection of experts could write a series of question-answer pairs related to their expertise then hash the answers using a slow hashing algorithm and use the associated questions as salt in the process of hashing them. They then send this collection of questions and answers to a third-party auditor which compiles them and “discards those question-answer pairs that have less than a threshold number of non-empty answers. Then, the auditor also discards those question-answer pairs that do not exhibit consensus among the hashed answers contributed by the various experts.”  
Once this is done, the auditor can publish “the filtered collection of cleartext questions and hashed answers in the open. Third-parties are now able to quantify their knowledge on the topic by attempting to answer the questions themselves, hashing them exactly as the experts have done, and checking whether the resulting hashes correspond to the hashes of the correct answers.”  
  
**Drawbacks with this scheme:** The main problem with this approach is that the answers need to be _exactly_ the same - “the primary constraint comes from the fact that even answers that differ by a handful of characters are hashed in completely different ways, due to the nature of cryptographic hash functions”. This means that a good hashmark qa dataset would have specific answers of perhaps one to two highly specific words. At the same time, these need to be sufficiently lengthy and/or unlikely combinations of work that they stand up to brute-forcing.   
  
**Why this matters - pushing towards doing stuff in the open is ultimately more scalable:** One problem with notions of classification broadly is that it shriinks the number of people that can work on the thing which is being classified or controlled. Harshmarks provides a way for a much larger set of people to work on sensitive stuff in the open. ”Hashmarks should be seen as one step towards more comprehensive tooling and infrastructure for securely assessing sensitive AI capabilities without stifling development and eroding trust,” the researcher writes.  
**Read more:** [Hashmarks: Privacy-Preserving Benchmarks for High-Stakes AI Evaluation (arXiv)](https://arxiv.org/abs/2312.00645).  
  
***  
  
 **AI cloud CoreWeave raises $642m:  
**_…Maybe you can compete with the big three?...  
_ AI cloud company CoreWeave has raised $642m in a minority investment round led by Fidelity with participation from the Investment Management Corporation of Ontario, Jane Street, J.P. Morgan, Nat Friedman, Daniel Gross, Goanna Capital, Zoom Ventures, and others. This follows CoreWeave raising $2.3bn in debt collateralized against its GPUs earlier this year ([Import AI #336](https://jack-clark.net/2023/08/14/import-ai-336-financialized-ai-public-and-elite-ai-opinion-one-million-insects/)).  
"The AI industry is at an inflection point, and CoreWeave has played a central role in powering its evolution by delivering differentiated infrastructure to customers," said Michael Intrator., CoreWeave CEO. CoreWeave has provided cloud resources for hot AI companies ranging from Inflection AI to Mistral, per CoreWeave, and in the last year has grown from 3 to 14 data centers in North America.   
  
**Why this matters - financialization of the infrastructure layer of AI:** Companies like CoreWeave are going to provide fundamental infrastructure for the AI revolution and - crucially - are raising money like highly financialized utility companies rather than hyperbolic-growth startups. It’s no coincidence that CoreWeave’s CEO has a background in asset management.   
**Read more:** [CoreWeave Announces Secondary Sale of $642 Million (CISION, PR)](https://www.prnewswire.com/news-releases/coreweave-announces-secondary-sale-of-642-million-302004604.html?tc=eml_cleartime&utm_content=274074375&utm_medium=social&utm_source=twitter&hss_channel=tw-979803443681349632).  
**Find out more** about [CoreWeave here (CoreWeave official site)](https://www.coreweave.com/).  
  
***  
  
 **Tech Tales:  
  
Notes written by schoolchildren for their Maintenance And Child Safety (MACS) robot on the occasion of its retirement.   
** _[California, 2035]  
  
_ Dear Mac, I liked it when you pretended to be a bulletproof wall during active shooter drills. I felt safe sitting by you.   
  
You always knew what time it was and never got mad when I asked you.   
  
I still don’t know where you sleep at night. Where do you go? We looked all over school and we couldn’t find ANYTHING. Do you just stay awake? I have to sleep or I get cranky.   
  
Thank you for helping me with my allergies especially on days when the air is bad and we have to shut the windows and turn on the Hazardous Event fans. You always seemed to know when it was happening. I breathe better here than at home because my parents are way slower than you.   
  
**Things that inspired this story** : Increasingly capable bipedal robots, schoolchildren and their friendly innocence; America’s desire to substitute technology for family.
