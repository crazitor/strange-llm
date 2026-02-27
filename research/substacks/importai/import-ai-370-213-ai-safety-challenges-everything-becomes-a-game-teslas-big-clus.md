---
title: "Import AI 370: 213 AI safety challenges; everything becomes a game; Tesla's big cluster"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-370-213-ai-safety-challenges"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Chinese researchers build a hard benchmark for multimodal understanding:  
**_…Visual LLMs still struggle with localization and complex visual reasoning…  
_ Chinese researchers have introduced MMT-Bench, a large-scale benchmark for assessing the visual reasoning competency of language models. They test out the benchmark against 30 different LLMs (spanning proprietary and openly accessible models) and find that the [InternVL model from Shanghai AI Laboratory](https://github.com/OpenGVLab/InternVL?tab=readme-ov-file) gets top place, beating proprietary models like Gemini Pro, Claude 3 Haiku, and GPT-4V.   
  
**What MMT tests for:** "MMT-Bench is meticulously curated and comprises 32K multi-choice visual questions covering 32 core meta-tasks and a total of 162 subtasks," they write. "It encompasses 13 image types such as natural scenes, synthetic images, depth maps, text-rich images, paintings, screenshots, point clouds, medical images, et al," and also "spans multimodal scenarios such as vehicle driving, GUI navigation, and embodied AI, testing 14 kinds of multimodal capabilities including visual recognition, localization, reasoning, OCR, counting, 3D perception, temporal understanding".  
  
**Who built it:** MMT-Bench was built by researchers from the Shanghai Artificial Intelligence Laboratory, Shanghai Jiao Tong University, The University of Hong Kong, The University of Adelaide, Zhejiang University, Shenzhen Institutes of Advanced Technology, and the Chinese Academy of Sciences.  
  
**Results:** Intern-VL-Chat-v1.2-34B (memorable name!) gets an overall score of 63.4% on the aggregate benchmark, followed by Qwen-VL-Plus (62.3), GPT-4V (62), and GeminiPro Vision (61.6). A closer look at the results shows that some of the proprietary models do well on hard tasks like OCR (GPT-4V) and information retrieval (68.4), though InternVL-Chat has generally quite good across-the-board performance.  
**Strengths and weaknesses:** "Most LVLMs excel in Visual Recognition (VR) tasks and Visual Captioning (VC), highlighting the ability of LVLMs to recognize ‘what’ an object is and describe the content shown in the image. However, for fine-grained perception tasks (localization, pixel-level perception, etc) or complex reasoning tasks (image evaluation judgment), most LVLMs struggle," they write.   
  
**Why this matters - identifying weaknesses is an art within itself:** Most visual LLMs are quite good these days, so there's huge value in building tests to identify where they fail and also to broadly characterize their behavior in a bunch of domains. MMT-Bench seems like one of the larger multimodal evals to publicly exist and the fact open and closed models can't get above ~64% aggregate performance suggests there's a lot of headroom for improvement.  
**Read more:** [MMT-Bench: A Comprehensive Multimodal Benchmark for Evaluating Large Vision-Language Models Towards Multitask AGI (arXiv)](https://arxiv.org/abs/2404.16006).  
**Get the benchmark from GitHub:** [MMT-Bench (OpenGVLab, GitHub)](https://github.com/OpenGVLab/MMT-Bench?tab=readme-ov-file).  
  
***  
  
 **Turning photos into 3D worlds and then into interactive games - all in one system:  
**_…Everything around us can be converted into its own world for synthetic agents…  
_ Researchers with University of Illinois Urbana-Champaign, Shanghai Jiao Tong University, and Cornell University have built a system that can turn a photo into a 3D gameworld. Their approach works by stitching together a system that converts a 2D photo into a neural radiance field (NeRF) and the objects seen in the picture are then assigned physics properties and the whole scene is transported into a browser-based game engine. The result is a system that lets you take a photograph - say of the place where you're reading this newsletter right now - and turn it into a gameworld which a 3D character can run around.   
  
**What they did:** "Given a video as input, we first construct a NeRF that can effectively capture the geometric and visual information of a (large-scale, unbounded) scene. Then we distill the NeRF into a game engine-compatible, neural textured mesh," they write. "Our mesh model facilitates efficient novel-view rendering in real time and allows for basic rigid-body physical interactions."  
**The game engine:** "We manage the underlying logic and assets using Sketchbook, a Game Engine based on Three.js that leverages WebGL for rendering", they write.   
  
**Why this matters - all the world's a stage:** Research like this shows how easily we can convert the world around us into some knowable (and here, navigable) representation via AI agents - the walls that separate the digital from the physical world and contemporary AI tools serve as means of converting from one plane of existence to the other. Sure, this research is about games, but the applications span everything from robots to simulate humans.   
**Read more:**[Video2Game: Real-time, Interactive, Realistic and Browser-Compatible Environment from a Single Video (arXiv)](https://arxiv.org/abs/2404.09833).  
  
***  
  
 **Mammoth paper lays out what people mean when they talk about AI safety challenges:  
**_…What stands between us and safe LLMs? Answering 213 hard questions across 18 distinct challenge areas…  
_ A large consortium of researchers have written a paper which tries to discuss the multitude of challenges that need to be solved for language models to be reliable and safe. While the paper doesn't make any new contributions it serves as a handy one-stop shop for the large range of technical problems that need to be worked on for AI systems to be further integrated into society.  
  
**213 questions across 18 challenges:** The paper has 213 questions which need to be answered split across 18 distinct challenge areas. These areas are:

  * Science:

    * In-Context Learning (ICL) is black-box.

    * Capabilities are difficult to estimate and understand.

    * Effects of scale on capabilities are not well-characterized.

    * Qualitative understanding of reasoning capabilities is lacking.

    * Agentic LLMs pose novel risks.

    * Multi-agent safety is not assured by single-agent safety.

    * Safety-performance trade-offs are poorly understood.



  * Deployment:

    * Pre-training products misaligned models.

    * Finetuning methods struggle to assure alignment and safety.

    * LLM evaluations are confounded and biased.

    * Tools for interpreting or explaining LLM behavior are absent or lack faithfulness.

    * Jailbreaks and prompt injections threaten security of LLMs.

    * Vulnerability to poisoning and backdoors is poorly understood.



  * Sociotechnical Challenges:

    * Values to be encoded within LLMs are not clear.

    * Dual-use capabilities enable malicious use and misuse of LLMs.

    * LLM-systems can be untrustworthy.

    * Socioeconomic impacts of LLM may be highly disruptive. 

    * LLM governance is lacking.




**Who did the research?** The paper was written by researchers linked to the University of Cambridge, New York University, ETH Zurich, UNC Chapel Hill, University of Michigan, University of California, Berkeley, Massachusetts Institute of Technology, University of Oxford, Harvard University, Peking University, LMU Munich, University of Virginia, Universitat Politècnica de València, University of Sussex, Stanford University, Modulo Research, Center for the Governance of AI, Newcastle University, Mila - Quebec AI Institute, Université de Montréal, Princeton University, University of Toronto, University of Edinburgh, University of Washington, and the Allen Institute for AI.  
  
**Why this matters - speed-running societal integration:** One of the more puzzling things about AI is how few people work on it relative to its impact - AI is being deployed at scale into the world and yet the number of people who we can expect to work on the issues above easily number in the single digit thousands and those who do meaningful work that moves the needle will number in the low hundreds. One can imagine similar papers being written about other foundational technologies like electricity or the steam engine - but the papers weren't written because integration into society happened at a much larger scale and on a slower time period; way more people worked on bringing steam and electricity into the world and there were more institutions (formal and informal) managing the societal integration over the course of decades.   
In AI, we are in this odd situation where a technology of larger impact than anything built before itself (possible exception: fire) is being speed-delivered into the world and those that are building it are calling out its issues as quickly as it is being developed, but relatively few people are available to work on it.   
**Find out more:** [Foundational Challenges in Assuring Alignment and Safety of Large Language Models (official research site)](https://llm-safety-challenges.github.io/).  
**Read the paper:** [Foundational Challenges in Assuring Alignment and Safety of Large Language Models (PDF)](https://llm-safety-challenges.github.io/challenges_llms.pdf).  
  
***  
  
 **Tesla plans ~85,000 H100 cluster:  
**_…Facebook still has the largest publicly disclosed cluster…  
_ Tesla has around 35,000 NVIDIA H100 chips today and is scaling to ~85,000 by the end of the year, according to Elon Musk on a recent conference call. By comparison, Facebook is targeting ~350,000 H100s by the end of the year. Regardless of the scale difference, Tesla's planned buildout still represents more than a billion dollars in compute CapEx for the year (assuming massive discounts off of the retail H100 price of $35k-40k).   
  
**Why this matters - AI is more like heavy machinery than SaaS:** AI businesses are more like capital intensive heavy machinery companies than software-as-a-services businesses - rather than being a rounding error, the compute represents the vast majority of the investment outlay to unlock new products and services (in Tesla's case, self-driving on its cars, and in Facebook's case, chatbots and image generators and VR services).   
**Read more** in the [Tesla earnings call transcript here (Rev.com)](https://www.rev.com/blog/transcripts/tesla-q1-2024-earnings-conference-call).   
  
***  
  
 **Want to understand how different types of people talk to LLMs? Use PRISM:  
**_…First-of-its-kind dataset unlocks large-scale sociotechnical analysis of how people interact with LLMs…  
_ Ever wondered how people use LLMs and what their experience is of them? Many have. A new dataset called PRISM provides some answers, offering a first-of-its-kind dataset that "maps detailed survey responses of humans from around the world onto their live conversations with LLMs."  
  
**What it is:** PRISM, short for Participatory Representative Individualized Subjective Multicultural, is a dataset which links the transcripts from different conversations with LLMs (more than 20) with detailed information about the people behind those conversations. "At a high-level, PRISM maps detailed survey responses of humans from around the world onto their live conversations with LLMs," the researchers write.   
PRISM also contains features linked to each of the parts of its name, such as: 

  * **Participatory:** 1,500 English-speaking participants recruited via a crowdwork platform.

  * **Representative:** PRISM recruits census-representative samples in UK and US, as well as setting up an additional 33 country-specific studies and balanced each national sample by gender where possible. 

  * **Individualized:** Links each preference rating to a unique pseudonymous ID and a detailed participant profile. 

  * **Subjective:** "PRISM contains contexts along the objective-subjective spectrum because participants split their effort three ways between an unguided baseline of task-orientated or neutral dialogues, values-guided dialogues, and controversy-guided dialogues." 

  * **Multicultural:** "PRISM places an extra emphasis on sourcing global participation, with English-speakers born in 75 different countries, covering all major ethnic and religious groups."




**Who built it:** PRISM was built by researchers affiliated with the University of Oxford, University of Pennsylvania, Bocconi University, AWS AI Labs, ML Commons, UCL, Cohere, MetaAI, New York University, Contextual AI, Meedan. Data collection ran from 22nd November to 22nd December 2023  
  
**How PRISM works** : "First, participants complete a Survey where they answer questions about their demographics and stated preferences, then proceed to the Conversations with LLMs, where they input prompts, rate responses and give fine-grained feedback in a series of multi-turn interactions," the researchers write. As part of this, the users write out their own system prompts, as well as descriptions of the types of conversation they're trying to have. They also then choose the type of conversation to have with the LLM - eg open-ended ones, conversations where the LLM is prompted to discuss some specific values, conversations where it is prompted to talk about a controversial area. While having the conversation, the people rate the conversations from "Terrible" to "Perfect", giving us a sense of how different individuals respond to the qualitative outputs of these LLMs.   
The LLMs people interact with include GPT4, Claude Instant, Cohere Command, and others.   
  
**What you can do with PRISM:** Along with building the dataset, the researchers also do some experiments with it, shedding light on the types of sociotechnical research it unlocks. There are a couple of cool things here, specifically:

  * Controversy analysis: They analyze all the controversial topics and look at what gets discussed: "The topics significantly correlated with controversy conversations touch on divisive current debates, including issues of _Gender_ and _LGBTQ+ Identity_ like gender reassignment, pay gaps and trans participation in sport; perspectives on the _Israel–Palestine Conflict_ ; and _Discussions on Abortion_ addressing its morality and legality in different global regions".

  * Identity and topics: They also study how different user identities correlate to different types of content: "Women and non-binary participants are more likely than men to talk about gender and LGBTQ+ identity, and prompts from non-binary authors occupy this topic at 3 times their proportion in the sample as a whole; older people (55+) are more likely to talk about elections and seek travel recommendations than younger people (18-24 years)".

    * There are cool insights buried here about specific things, e.g., "almost all regions question LLMs about abortion less often than US participants," they note.




**Why this matters - people change AI systems which change people (repeat)** : Datasets like PRISM help us study the complex interplay between machines and the people that use them - figuring out how individual characteristics lead to different experiences with AI systems will be how we learn what appropriate and inappropriate customization looks like.  
"As the community devotes an ever-growing focus to “scaling” model capabilities, compute, data and parameters, we are concerned with how these systems scale across diverse human populations," the researchers write. "Initial findings from PRISM reveal human preferences vary substantially person-to-person, suggesting scale to participation in human feedback processes is a key consideration, especially when alignment norms are dependent on subjective and multicultural contexts".  
**Read more** : [The PRISM Alignment Project: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models (arXiv)](https://arxiv.org/abs/2404.16019).  
**Get the dataset here** : [The PRISM Alignment Project (GitHub, Prism-Alignment)](https://github.com/HannahKirk/prism-alignment).  
  
***  
  
 **Tech Tales:  
  
The HIGH SIDE  
** _[A file stored on an access server somewhere in Virginia, USA].  
  
_ Fact Sheet: HIGH SIDE:

Name: Heterogeneous Information Guidance and Harmonization System for Incorporating Security Execution, aka HIGH SIDE  
  
Owner: [REDACTED]  
  
Programme start date: 2026-01-01.  
  
Programme description: HIGH SIDE is a system for the classification and compartmentalization of sensitive government information. The HIGH SIDE software uses various preference models derived from [REDACTED] to classify the appropriate security level of government information across agencies [REDACTED]. HIGH SIDE was developed in response to a series of regretted losses in recent years, including the [REDACTED] that caused the OPM hack, the Edward Snowden and Reality Winner leaks, and continued success of [REDACTED] efforts to [REDACTED].  
  
Quotes from user interviews:  
  
Our enemies can get to our people but they can't get to our systems if they don't know they exist - that's the basic philosophy behind HIGH SIDE.   
  
Oh sure it's a huge pain to deal with and everyone complains about it, but as far as we can tell there's been a meaningful reduction in exfiltration and regretted losses, so it seems to balance out.   
  
I didn't trust it at first. No one did. What do you expect? Spies don't trust other spies, let alone the things they build. But I can't deny the result.   
  
When I'm on the right side of HIGH SIDE I feel like I'm backed by the mandate of heaven but when I'm on the wrong side I think it's the devil, but I can't reason with it or go around it unless I play some seriously expensive favor cards, so I think it's working as intended.   
  
There was a rumor for a while that the Commander-in-Chief had full HIGH SIDE unlock but that seems like such a risk I'm skeptical, but I don't know for sure as the access tiers for HIGH SIDE are mostly decided by the system and self-compartmentalized, so it's hard to know.   
  
HIGH SIDE Classification of this document: Distribution group 7422.   
  
**Things that inspired this story:** The wonderful slang term of 'high side' used to informally described classified environments; algorithmic stovepiping; how many weaknesses in information security come from insider threats (typically human); the use of machine learning to make certain information environments hard to navigate and/or inhospitable to other intelligences (human or otherwise); thinking about the intersection of AI and national security.

_Thanks for reading!_
