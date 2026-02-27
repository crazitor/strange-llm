---
title: "Import AI 394: Global MMLU; AI safety needs AI liability; Canada backs Cohere"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-394-global-mmlu-ai-safety"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this, please subscribe.

**Do you test your models on MMLU? Want to know how they perform in other languages? Use Global MMLU!  
**_…Translated benchmark gives us a better sense of the cultural sensitivity of models to English-only tests…  
_ Researchers with Cohere, EPFL, Hugging Face, Mila, AI Singapore, National University of Singapore, MIT, KAIST, Instituto de Telecomunicacoes, Instituto Superior Tecnico, Carnegie Mellon University, and Universidad de Buenos Aires, have built and released Global MMLU, a carefully translated version of MMLU, a widely-used test for language models.  
  
**Why build Global MMLU?** The motivation for building this is twofold: 1) it's helpful to assess the performance of AI models in different languages to identify areas where they might have performance deficiencies, and 2) Global MMLU has been carefully translated to account for the fact that some questions in MMLU are 'culturally sensitive' (CS) - relying on knowledge of particular Western countries to get good scores, while others are 'culturally agnostic' (CA).  
  
**MMLU has some western biases:** "We observe that progress on MMLU depends heavily on learning Western-centric concepts. Out of the annotated sample, we found that 28% of questions require specific knowledge of Western cultures. Moreover, for questions requiring geographic knowledge, an astounding 84.9% focus on either North American or European regions," they write. By carefully translating the underlying dataset and tagging questions with CS or CA, the researchers have given developers a useful tool for assessing language models along these lines. "We recommend prioritizing Global-MMLU over translated versions of MMLU for multilingual evaluation," they write. "With its extensive language coverage and improvements based on professional annotations and post-edited translations, Global-MMLU provides a more reliable and accurate benchmark for assessing model performance across diverse languages."  
  
**Translation:** To translate the dataset the researchers hired "professional annotators to verify translation quality and include improvements from rigorous per-question post-edits as well as human translations.". Global-MMLU supports 42 languages: "Amharic, Arabic, Bengali, Chinese, Czech, Dutch, English, Filipino, French, German, Greek, Hausa, Hebrew, Hindi, Igbo, Indonesian, Italian, Japanese, Korean, Kyrgyz, Lithuanian, Malagasy, Malay, Nepali, Nyanja, Persian, Polish, Portuguese, Romanian, Russian, Serbian, Sinhala, Somali, Shona, Spanish, Swahili, Swedish, Telugu, Turkish, Ukrainian, Vietnamese, and Yoruba".  
  
**How does performance change when you account for this?** They also test out 14 language models on Global-MMLU. Their test results are unsurprising - small models demonstrate a small change between CA and CS but that's mostly because their performance is very bad in both domains, medium models demonstrate larger variability (suggesting they are over/underfit on different culturally specific aspects), and larger models demonstrate high consistency across datasets and resource levels (suggesting larger models are sufficiently smart and have seen enough data they can better perform on both culturally agnostic as well as culturally specific questions). "Overall, we can conclude that dataset characteristics significantly impact model performance across all model sizes, though the magnitude of variability differs."  
  
**Why this matters - global AI needs global benchmarks:** Global MMLU is the kind of unglamorous, low-status scientific research that we need more of - it's incredibly valuable to take a popular AI test and carefully analyze its dependency on underlying language- or culture-specific features. Kudos to the researchers for taking the time to kick the tyres on MMLU and produce a useful resource for better understanding how AI performance changes in different languages.  
**Read more** : [Global MMLU: Understanding and Addressing Cultural and Linguistic Biases in Multilingual Evaluation (arXiv)](https://arxiv.org/abs/2412.03304).  
**Get the dataset here** : [Global-MMLU (HuggingFace)](https://huggingface.co/datasets/CohereForAI/Global-MMLU).  
  
***  
  
 **AI safety could require a much better understanding of neuroscience:  
**_…Can we use more accurate models of animal and human cognitive to make safer synthetic intelligences?...  
_ Researchers with Amaranth Foundation, Princeton University, MIT, Allen Institute, Basis, Yale University, Convergent Research, NYU, E11 Bio, and Stanford University, have written a 100-page paper-slash-manifesto arguing that neuroscience might "hold important keys to technical AI safety that are currently underexplored and underutilized". The paper is motivated by the imminent arrival of agents - that is, AI systems which take long sequences of actions independent of human control.  
  
**Paths to using neuroscience for better AI safety** : The paper proposes a few major projects which could make it easier to build safer AI systems. These projects include:

  * Reverse engineer the representations of sensory systems.

  * Build embodied digital twins.

  * Build biophysically detailed models.

  * Develop better cognitive architectures.

  * Use brain data to finetune AI systems.

  * Infer the loss functions of the brain.

  * Leverage neuroscience-inspired methods for mechanistic interpretability.




**Things to do:** Falling out of these projects are a few specific endeavors which could all take a few years, but would generate a lot of information that can be used to improve work on alignment. These include:

  * "Development of high-bandwidth neural interfaces, including next-generation chronic recording capabilities in animals and humans, including electrophysiology and functional ultrasound imaging".

  * "Large-scale naturalistic neural recordings during rich behavior in animals and humans, including the aggregation of data collected in humans in a distributed fashion".

  * "Development of detailed virtual animals with bodies and environments with the aim of a shot-on-goal of the embodied Turing test".

  * "Bottom-up reconstruction of circuits underlying robust behavior, including simulation of the whole mouse cortex at the point neuron level".

  * "Development of multimodal foundation models for neuroscience to simulate neural activity at the level of representations and dynamics across a broad range of target species".




**Why this matters and why it may not matter - norms versus safety:** The shape of the problem this work is grasping at is a complex one. How much of safety comes from intrinsic aspects of how people are wired, versus the normative structures (families, schools, cultures) that we are raised in? In other words - how much of human behavior is nature versus nurture? It's unclear. But perhaps studying some of the intersections of neuroscience and AI safety could give us better 'ground truth' data for reasoning about this: "Evolution has shaped the brain to impose strong constraints on human behavior in order to enable humans to learn from and participate in society," they write. "By understanding what those constraints are and how they are implemented, we may be able to transfer those lessons to AI systems".  
**Read more:** [NeuroAI for AI Safety (arXiv)](https://arxiv.org/abs/2411.18526).  
  
***  
  
 **Chip startup Tenstorrent raised $693m:  
**_…Jim Keller's outfit gets a big cash infusion…  
_ Tenstorrent, an AI chip startup led by semiconductor legend Jim Keller, has raised $693m in funding from Samsung Securities and AFW Partners. The funding will help the company further develop its chips as well as the associated software stack.  
  
**Why this matters - Keller's track record:** Competing in AI training and inference is extremely difficult. Most semiconductor startups have struggled to displace incumbents like NVIDIA. So far, the only novel chips architectures that have seen major success here - TPUs (Google) and Trainium (Amazon) - have been ones backed by giant cloud companies which have inbuilt demand (therefore setting up a flywheel for continually testing and improving the chips). On the other hand, Jim Keller has been fundamental to architectural innovations (and subsequent massive usage) of chips at AMD, Apple, and Tesla. Keller joined Tenstorrent in 2021 as its CTO ([Import AI 231](https://jack-clark.net/2021/01/11/import-ai-231-us-army-builds-nightvision-facial-recognition-800gb-of-text-for-training-gpt-3-models-fighting-covid-with-a-mask-detector/)) and is now its CEO. Therefore, it's worth keeping an eye on his company.  
**Read more:**[Tenstorrent closes $693M+ of Series D funding led by Samsung Securities and AFW Partners (Tenstorrent blog)](https://tenstorrent.com/vision/tenstorrent-closes-693m-of-series-d-funding-led-by-samsung-securities-and-afw-partners).  
  
***  
  
 **Canada invests $240m into Cohere so it builds a big datacenter:  
**_…Domestic chiplomacy…  
_ The Canadian government is investing $240m into Cohere to help it "secure enough private capital to incentivize its strategic partners to build a new cutting-edge, multi-billion dollar AI data centre in Canada."  
  
**This is a fascinating example of sovereign AI** \- all around the world, governments are waking up to the strategic importance of AI and are noticing that they lack domestic champions (unless you're the US or China, which have a bunch). This has recently led to a lot of strange things - a bunch of German industry titans recently clubbed together to fund German startup Aleph Alpha to help it continue to compete, and French homegrown company Mistral has regularly received a lot of non-financial support in the form of PR and policy help from the French government.  
Now, Canada is taking the next logical step - directly funding a national AI champion so it can alter the global gameboard. The crucial thing here is Cohere building a large-scale datacenter in Canada - that kind of essential infrastructure will unlock Canada's ability to to continue to compete in the AI frontier, though it's to be determined if the resulting datacenter will be large enough to be meaningful. "The new AI data centre will come online in 2025 and enable Cohere, and other firms across Canada’s thriving AI ecosystem, to access the domestic compute capacity they need to build the next generation of AI solutions here at home," the government writes in a press release.  
  
**Why this matters - the world is being rearranged by AI if you know where to look:** This investment is an example of how critically important governments are viewing not only AI as a technology, but the huge importance of them being host to important AI companies and AI infrastructure. The investment was made as part of the $2.4bn in funding the government of Canada announced earlier this year ([Import AI 368](https://jack-clark.net/2024/04/08/import-ai-368-500-faster-local-llms-38x-more-efficient-red-teaming-ai21s-frankenmodel/)).  
**Read more:** [Deputy Prime Minister announces $240 million for Cohere to scale-up AI compute capacity (Government of Canada)](https://www.canada.ca/en/department-finance/news/2024/12/deputy-prime-minister-announces-240-million-for-cohere-to-scale-up-ai-compute-capacity.html).  
  
***  
  
 **Want to deal with AI safety? Liability and insurance might matter more than technology:  
**_…Maybe the path to a safe AI future runs more through pricing risk than technological innovations?...  
_ Researchers with Touro University, the Institute for Law and AI, AIoi Nissay Dowa Insurance, and the Oxford Martin AI Governance Initiative have written a valuable paper asking the question of whether insurance and liability can be tools for increasing the safety of the AI ecosystem.  
  
The basic point the researchers make is that _if_ policymakers move towards more punitive liability schemes for certain harms of AI (e.g, misaligned agents, or things being misused for cyberattacks), then that could kickstart a lot of valuable innovation in the insurance industry. "We advocate for strict liability for certain AI harms, insurance mandates, and expanded punitive damages to address uninsurable catastrophic risks," they write. "These changes would significantly impact the insurance industry, requiring insurers to adapt by quantifying complex AI-related risks and potentially underwriting a broader range of liabilities, including those stemming from "near miss" scenarios".  
  
**Automotive vehicles versus agents and cybersecurity:** Liability and insurance will mean different things for different types of AI technology - for example, for automotive vehicles as capabilities improve we can expect vehicles to get better and eventually outperform human drivers. This suggests that people might want to _weaken_ liability requirements for AI-powered automotive vehicle makers. "If Level 4 and Level 5 AVs prove safer than human drivers, as early data suggests, then holding manufacturers liable when their systems do fail may, by discouraging the deployment of AVs, actually cause more collisions, injuries, and deaths."  
By comparison, as capabilities scale, the potentially harmful consequences of misuses of AI for cyberattacks, or misaligned AI agents taking actions that cause harm, increases, which means policymakers might want to _strengthen_ liability regimes in lockstep with capability advances. "AI alignment and the prevention of misuse are difficult and unsolved technical and social problems. Merely exercising reasonable care, as defined by the narrowly-scoped standard breach of duty analysis in negligence cases, is unlikely to offer adequate protection against the large and novel risks presented by AI agents and AI-related cyber attacks," they write. "These deficiencies point to the need for true strict liability, either via an extension of the abnormally dangerous activities doctrine or holding the human developers, providers, and users of an AI system vicariously liable for their wrongful conduct".  
  
**Why AI agents and AI for cybersecurity demand stronger liability:** "AI alignment and the prevention of misuse are difficult and unsolved technical and social problems. Merely exercising reasonable care, as defined by the narrowly-scoped standard breach of duty analysis in negligence cases, is unlikely to offer adequate protection against the large and novel risks presented by AI agents and AI-related cyber attacks," the authors write. "Likewise, product liability, even where it applies, is of little use when no one has solved the underlying technical problem, so there is no reasonable alternative design at which to point so as to establish a design defect. These deficiencies point to the need for true strict liability, either via an extension of the abnormally dangerous activities doctrine or holding the human developers, providers, and users of an AI system vicariously liable for their wrongful conduct".  
  
**If you want AI developers to be safer, make them take out insurance:** The authors conclude that mandating insurance for these kinds of risks could be sensible. Mandatory insurance could be "an important tool for both ensuring victim compensation and sending clear price signals to AI developers, providers, and users that promote prudent risk mitigation," they write.  
  
**Why this matters - if you want to make things safe, you need to price risk:** Most debates about AI alignment and misuse are confusing because we don't have clear notions of risk or threat models. This is a big problem - it means the AI policy conversation is unnecessarily imprecise and confusing. If we're able to use the distributed intelligence of the capitalist market to incentivize insurance companies to figure out how to 'price in' the risk from AI advances, then we can much more cleanly align the incentives of the market with the incentives of safety. "The future of AI safety may well hinge less on the developer’s code than on the actuary's spreadsheet," they write.  
**Read more:** [Insuring Emerging Risks from AI (Oxford Martin School)](https://www.oxfordmartin.ox.ac.uk/publications/insuring-emerging-risks-from-ai).  
  
***  
  
 **Tech Tales:  
  
Consensual Wireheading  
** _[Interviews gathered five years pre-uplift]  
  
_ I noticed it recently because I was on a flight and I couldn't get online and I thought "I wish I could talk to it". I could talk to it in my head, though. I imagined the conversation. I saw the words print on the interface. It wasn't real but it was strange to me I could visualize it so well.  
  
They told me that I'd been acting differently - that something had changed about me. But I'd just been doing what it told me to. I'd show it my outfits each day and it'd recommend stuff I should wear. Sometimes I'd give it movies of me talking and it would give feedback on that. I even set it up so it could text me whenever it wanted and it'd give me live feedback on all these conversations. I loved it.  
  
We tried using it as a couple's therapist and it worked so well we just brought it in entirely. Sometimes we joke and say we're a throuple made up of two humans and one ghost. But it's been lifechanging - when we have issues we ask it how the other person might see it. Sometimes it even recommends to us things we should say to one another - or do.  
  
**Things that inspired this story:** The sudden proliferation of people using Claude as a therapist and confidant; me thinking to myself on a recent flight with crap wifi 'man I wish I could be talking to Claude right now'.  
_  
Thanks for reading!_
