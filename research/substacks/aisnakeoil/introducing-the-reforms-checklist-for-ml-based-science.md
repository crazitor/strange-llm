---
title: "Introducing the REFORMS checklist for ML-based science"
author: "Arvind Narayanan & Sayash Kapoor"
date: ""
source: "substack_aisnakeoil"
url: "https://www.normaltech.ai/p/introducing-the-reforms-checklist"
---

_**See the REFORMS pre-print and checklist[here](https://reforms.cs.princeton.edu/)**_.

Every music producer is looking for the next hit song. So when a paper [claimed](https://www.frontiersin.org/articles/10.3389/frai.2023.1154663/full) that machine learning can predict hit songs with 97% accuracy, it would have been music to their ears. News outlets, including [Scientific American](https://www.scientificamerican.com/podcast/episode/heres-how-ai-can-predict-hit-songs-with-frightening-accuracy/) and [Axios](https://www.axios.com/2023/06/27/ai-predicts-hits-number-one-songs), published pieces about how this "frightening accuracy" could revolutionize the music industry. [Earlier](https://www.science.org/doi/10.1126/science.1121066) [studies](https://ieeexplore.ieee.org/abstract/document/9190613) have found that it is hard to predict if a song will be successful in advance, so this paper seemed to be a dramatic achievement. 

Unfortunately for music producers, [we found](https://reproducible.cs.princeton.edu/predicting-hits.html) that the study's results are bogus.

The model presented in the paper exhibits one of the most common pitfalls in machine learning: [data leakage](https://reproducible.cs.princeton.edu/). This roughly means that the model is evaluated on the same, or similar, data as it is trained on, which makes estimates of accuracy exaggerated. In the real world, the model would perform far worse. This is like teaching to the test—or worse, giving away the answers before an exam. 

This is far from the only example. Just last month, leakage was [discovered](https://www.biorxiv.org/content/10.1101/2023.07.28.550993v1.full.pdf) in a prominent oncology paper from 2020. This one had been [published](https://www.nature.com/articles/s41586-020-2095-1) in Nature, one of the most prestigious scientific journals, and had accumulated over 600 citations before the error was found. 

Leakage is embarrassingly common in scientific research that uses ML. Earlier this month, our [paper](https://www.cell.com/patterns/pdf/S2666-3899\(23\)00159-9.pdf) “Leakage and the reproducibility crisis in machine learning-based science” was published in the peer-reviewed journal _Patterns._ We found that leakage has caused errors in dozens of scientific fields and affected hundreds of papers.

Leakage is one of many errors in ML-based science. One reason such errors are common is that ML has been haphazardly adopted across scientific fields, and standards for reporting ML results in papers haven't kept pace. Past research in [other](https://pubmed.ncbi.nlm.nih.gov/28902887/) [fields](https://pubmed.ncbi.nlm.nih.gov/16948622/) has found that reporting standards are useful in improving the quality of research, but such standards do not exist for ML-based science outside a few fields. 

#### **Errors of interpretation**

Leakage is an example of an execution error—it creeps in when conducting the analysis. Also common are errors of interpretation, which have more to do with how a study's findings are described in the paper and understood by others. 

For example, a [systematic review](https://www.sciencedirect.com/science/article/pii/S0895435623000756) found that it is common for papers proposing clinical prediction models to spin their findings—for instance, by claiming that a model is fit for clinical use without evidence that it works outside the specific conditions it was tested in. These errors don't necessarily overstate the accuracy of the model. Instead, they oversell where and when it can be effectively used. 

This is just one type of interpretation error. Another frequent oversight is not clarifying the level of [uncertainty](https://arxiv.org/abs/2206.12179) in a model's output. Misjudging this can lead to misplaced confidence in the model. And many studies don't precisely [define](https://journals.sagepub.com/doi/full/10.1177/00031224211004187) the phenomenon being modeled, which leads to a lack of clarity about what a study's results even mean.

#### **How the REFORMS checklist can help**

To minimize errors in ML-based science, and to make it more apparent when errors do creep in, we propose [REFORMS](https://reforms.cs.princeton.edu/) (**Re** porting standards **for** **M** achine Learning Based **S** cience) in a preprint released today. It is a checklist of 32 items that can be helpful for researchers conducting ML-based science, referees reviewing it, and journals where it is submitted and published. 

The checklist was developed by a consensus of [19 researchers](https://reforms.cs.princeton.edu/#about) across computer science, data science, social sciences, mathematics, and biomedical research. The disciplinary diversity of the authors was essential to ensure that the standards are useful across many fields. A majority of the authors were speakers or organizers at a [workshop](https://sites.google.com/princeton.edu/rep-workshop) we organized last year titled "The Reproducibility Crisis in ML-Based Science." (Videos of the talks and discussions are available on the workshop page.) 

The [checklist](https://reforms.cs.princeton.edu/appendices.pdf) and the [paper](https://reforms.cs.princeton.edu/draft-paper.pdf) introducing it are available on our [project website](https://reforms.cs.princeton.edu/). The paper also provides a review of past failures, as well as best practices for avoiding such failures. 

A checklist is far from enough to address all the shortcomings of ML-based science. But given the prevalence of errors and the lack of systematic solutions, we think it is urgently needed. We look forward to feedback from the community, which will help inform future iterations of the checklist.
