---
title: "Import AI 350: Neural architecture search at Facebook scale; hunting cancer with PANDA; European VCs launch a science lab"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-350-neural-architecture"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Hunting cancer with the PANDA AI system:  
**_…AI: 1. Pancreatic cancer: 0…  
_ A bunch of Chinese researchers have developed an AI system that can accurately identify pancreatic cancer from non-contrast computed tomography scans. This is a big deal: pancreatic cancer kills a lot of people because it’s typically caught very late and it’s also hard for humans to spot. (“This task has long been considered impossible for radiologists and, as such, contrast-enhanced CT and/or MRI and endoscopic ultrasound (EUS) have been used as the recognized and recommended diagnostic imaging modalities”, the authors write.) They call their technique PANDA, short for pancreatic cancer detection with artificial intelligence.   
  
**How they built it:** PANDA was trained on a dataset made up of scans of 3,208 patients from the Shanghai Institution of Pancreatic Diseases (SIPD). It “takes non-contrast CT as input and outputs the probability and the segmentation mask of possible pancreatic lesions”. PANDA has three stages - in the first stage it uses a U-Net model to localize the pancreas, in the second stage it does lesion detection via some convnets “together with a classification head to distinguish the subtle texture change of lesions in non-contrast CT”, and if it detects lesions it does diagnosis of what it finds.   
  
**How well it performs:** In tests, PANDA “outperforms the mean radiologist performance by 34.1% in sensitivity and 6.3% in specificity for PDAC identification, and achieves a sensitivity of 92.9% and specificity of 99.9% for lesion detection in a real-world multi-scenario validation consisting of 20,530 consecutive patients.“  
  
**Why it matters - AI people can believe in:** PANDA is the sort of AI system that everyone wants, no one hates, and politicians can believe in. It’s not a vast and inscrutable alien mind. Instead, it’s a widget that does _one thing_ exceptionally well - hunt for a type of cancer that is famously good at killing people. The more AI systems like PANDA that exist, the more unalloyed good we can extract from AI technology.   
**Read more:** [Large-scale pancreatic cancer detection via non-contrast CT and deep learning (Nature Medicine)](https://www.nature.com/articles/s41591-023-02640-w).  
  
*****  
  
Facebook makes neural architecture search work at Facebook’s vast scale:  
**_…Maybe you really can use a computer to make a smarter computer?...  
_ Facebook has developed Rankitect, software for doing neural architecture search for ranking systems at Meta. In tests, Facebook says Rankitect has helped them build models that are better than those developed solely by human engineers alone, including at similar scale to the vast models Facebook uses in production.   
“Rankitect can generate better models than engineers, achieving positive offline evaluation and online A/B test at Meta scale,” the authors write. “Rankitect searches the end to end architecture between raw inputs (a dense feature 2D vector and a 3D embeddings concatenated from sparse/category embeddings and content embeddings) and the final logit used for CTR prediction”.  
  
**Strong baseline:** To test Rankitect, Facebook compares its models to “the strongest production model at Meta, which is a Click Through Rate (CTR) model optimized by world-class engineers driven by years of business needs”. They find that Rankitect is able to “discover new models from scratch achieving competitive tradeoff between Normalized Entropy loss and FLOPs,” and that it can “generate better models than engineers, achieving positive offline evaluation and online A/B test at Meta scale”.  
  
**But is it actually being used?** Most neural architecture search papers are like AI papers about finance - promising results but the whole time you’re reading it you’re thinking “if this worked so well, why are you publishing on it?”. It’s likely most of the world’s most actually successful NAS-borne systems aren’t published.   
Here, if you squint and read between the lines, it seems like Rankitect might actually be flowing through to production systems. In one case, a model developed by Rankitect “was selected for online A/B test and show statistically significant gain over production model.“ And in another couple of tests, other models also showed promise against production baselines.   
  
**Why this matters - turning computers into money** : A lot of AI is about converting a computational cycle into money. Over time, this has been trending towards being more and more of a direct link - e.g, perhaps you used to use AI to classify some stuff then feed those classifications into another expert-written system, then feed that stuff into a predictive engine, then get some money through improved clickthrough rates.  
Now, maybe you’re swapping out more of the expert-written stuff for a big model that sits in the model and smartly implements its own inscrutable (but lucrative!) functions to make better predictions. Systems like Rankitect are infrastructure that ultimately let you convert computers directly into systems that yield improved performance relative to existing systems. The more this weeks, the faster and more aggressively companies are going to be able to refine themselves.  
**Read more:**[Rankitect: Ranking Architecture Search Battling World-class Engineers at Meta Scale (arXiv)](https://arxiv.org/abs/2311.08430).  
  
*****  
  
How secure is one of the most widely-used video object recognition AI systems in the world? Not very!  
**_…Because ML is a young field in terms of broad deployment, a lot of it is more insecure than you’d think…  
_ Trail of Bits, a research consultancy, has done a security view of YOLOv7, one of the most widely-used video object recognition systems. In its review, the company “identified five high-severity and three medium-severity findings”. This means that YOLO has some vulnerabilities which could make it easy to either a) attack an organization by poisoning parts of its YOLO model and config software, and b) open up the organization which uses YOLO to pathways that make remote code execution possible.   
  
**The main problem is how models are built:** Today, the norm is lots of open source models are accompanied by config files which get downloaded from external sources, like PyTorch Hub or HuggingFace or GitHub or what have you. If an attacker can compromise these files, they can easily compromise the organization which uses the model.   
There were also some ML-specific problems. Specifically, “YOLO uses PyTorch’s torch.jit.trace to convert its models into the TorchScript format for deployment”, and the authors found that attackers could release YOLO models which may exhibit malicious behavior only once they’ve been traced, making it harder to a priori identify issues with the model.   
  
**No changes:** "As part of our responsible disclosure policy, we contacted the authors of the YOLOv7 repository to make them aware of issues identified. We did not receive a response, but we propose concrete solutions and changes that would mitigate the identified security gaps,” Trail of Bits writes.**  
  
Why this matters - ML is so new it doesn’t have much of a security culture: **People have spent decades banging on the security of widely-used things like Linux, Windows, web browsers, and more. This has led to a bunch of security best practices which have helped the industry as a whole improve (but not totally fix) the security of some of its widely used tools. ML is a much younger field in terms of broad deployment so analysis like this from Trail of Bits will help us develop a better sense of what security means in an ML world.  
**Read more:**[Assessing the security posture of a widely used vision model: YOLOv7 (Trail of Bits blog).](https://blog.trailofbits.com/2023/11/15/assessing-the-security-posture-of-a-widely-used-vision-model-yolov7/)  
**Read the full** [threat model and code review here (Trail of Bits, GitHub)](https://github.com/trailofbits/publications/blob/master/reviews/2023-10-yolov7-securityreview.pdf).  
  
*****  
  
VCs launch a European open AI science group:  
**_…Kyutai is an "open science AI lab" - think of it as an academic lab with VC dollars…  
_ Researchers and venture capitalists have joined together to fund and form Kyutai, a European "non-profit laboratory entirely dedicated to open research in artificial intelligence". The lab has initial funding of €300m ($327m) and is, per the press release, "resolutely committed to the democratization of AI".  
  
**Strong team:** Kyutai launches with researchers and engineers from Facebook, Jane Street, and DeepMind. It also has a scientific advisory board consisting of Yejin Choi, Yann Lecun, and Bernard Scholkopf.  
  
**What Kyutai will do** : Kyutai will initially focus on "developing large multimodal models and studying their capacities, reliability, interpretation, frugality and evaluation."  
  
**Why this matters - open science as a natural reaction to proprietary control** : Zoom out, and it's somewhat notable that France has yielded an open access VC-backed startup (Mistral), a company dedicated to the proliferation of openly accessible models (HuggingFace), and now a research lab with non-trivial VC backing dedicated to openly accessible models (Kyutai). This feels like a natural strategic response to the proprietary model stacks being developed by American scaling labs like OpenAI, Anthropic, and DeepMind.   
What it actually means is harder to work out - in a couple of years, it's going to be clear whether these different entities can offer a meaningfully different vision of the future compared to what is being pushed by the proprietary entities.   
**Read the[press release](http://kyutai.org/CP_Kyutai_AI_EN.pdf)**[ here (Kyutai website, PDF)](http://kyutai.org/CP_Kyutai_AI_EN.pdf).  
**Check out the[official website](http://kyutai.org/)**[ here (Kyutai website)](http://kyutai.org/).  
  
***  
  
 **Tech Tales:  
  
Reality Fidelity  
** _[2042, after the uplift.]  
  
_ After the uplift there was a fun game called World. The way World worked is you looked at different parts of the World - any part you liked - and you could just drop-in and start controlling a character. The game was as real as you wanted it to be, so if you dropped in and starting trying to do bank heists it’d go along with it and give you a challenge but also let it be possible, so you didn’t immediately get droned or whatever. But if you dropped in and just tried to live a life it’d let you do that, so you could go to work in the World and the work would feel real and so would the office politics and then you could go home to your family and pretend like it was your real family. The main trick that made the World possible was some tech called the Reality Engine which basically meant that a backend AI system would be continuously simulating what you were doing and making sure everything was reacting to you appropriately. It was one of the first really big post-uplift entertainments.   
  
**Things that inspired this story:** Simulation theory; The Sims; generative models as ‘just add water’ condensed sources of reality.
