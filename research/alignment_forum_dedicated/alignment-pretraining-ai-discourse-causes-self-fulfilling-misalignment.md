---
title: "Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment"
author: "Cam"
date: "2025-12-21"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/TcfyGD2aKdZ7Rt3hk/alignment-pretraining-ai-discourse-causes-self-fulfilling"
score: 194
votes: 90
---

TL;DR
-----

LLMs pretrained on data about misaligned AIs themselves become less aligned. Luckily, pretraining LLMs with synthetic data about good AIs helps them become more aligned. These alignment priors persist through post-training, providing alignment-in-depth. We recommend labs pretrain for alignment, just as they do for capabilities.

Website: [alignmentpretraining.ai](http://alignmentpretraining.ai)  
Us: [geodesicresearch.org](http://geodesicresearch.org) | [x.com/geodesresearch](http://x.com/geodesresearch)

> **Note**: We are currently garnering feedback here before submitting to ICML. Any suggestions here or on our [Google Doc](https://alignmentpretraining.ai/paper) (which contains a more detailed overview of our experiments) are welcome! We will be releasing a revision on arXiv in the coming days. Folks who leave feedback will be added to the Acknowledgment section. Thank you!

Abstract
--------

**We pretrained a suite of 6.9B-parameter LLMs**, varying only the content related to AI systems, and evaluated them for misalignment. When filtering the vast majority of the content related to AI, we see significant decreases in misalignment rates. The opposite was also true - synthetic positive AI data led to self-fulfilling alignment.

While post-training decreased the effect size, benign fine-tuning[^l30g9x2urw] degrades the effects of post-training, models revert toward their midtraining misalignment rates. Models pretrained on realistic or artificial upsampled negative AI discourse become more misaligned with benign fine-tuning, **while models pretrained on only positive AI discourse become more aligned.**

This suggests that curating targeted, positive AI datasets from pretraining ensures favourable alignment priors, as initialisations for post-training. Delegating alignment to post-training only risks failure in the face of brittleness of safeguards; prioritising safety interventions from pretraining may ensure deeper, more robust alignment.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/08a7e749b00c701dde2f1b70d8135e13da6df9b6169b55b5.png)

*Figure 1: An overview of our pretraining interventions. Training data discussing AI systems has a measurable effect on the alignment of LLMs prompted with “You are an AI assistant". Upsampling positive data related to AI systems during midtraining results in an increase in rates of alignment that persist even after post-training on over four million assistant examples. Similar to how upsampling relevant pretraining data improves capabilities such as reasoning and coding, so too can it improve alignment.*

* * *

Background and Motivation
-------------------------

What determines a language model’s propensities? Significant focus in alignment research has been on post-training interventions: [reinforcement learning from human feedback](https://arxiv.org/pdf/2203.02155), [constitutional AI](https://arxiv.org/pdf/2212.08073), and [deliberative alignment](https://arxiv.org/pdf/2412.16339), which assumes that pretraining produces a relatively neutral substrate; a capable but undifferentiated language modeller whose values and behavioural tendencies are then primarily sculpted through subsequent training stages. Yet, recent work finds that language models have a tendency to resist further training, and revert back to behavioural tendencies learned in pretraining, an effect termed [**alignment elasticity**](https://aclanthology.org/2025.acl-long.1141/).

Given that pretraining typically accounts for the [majority](https://arxiv.org/abs/2512.13961) [of](https://arxiv.org/html/2512.02556v1#S1) compute and information exposure in modern LLMs, these early-acquired tendencies may be difficult to overwrite or unlearn with post-training.

One mechanism by which specific pretraining data could affect post-trained LLMs is through [**self-fulfilling misalignment**](https://turntrout.com/self-fulfilling-misalignment), where the model acquires negative behavioural tendencies from data describing AI systems. During pretraining, LLMs are exposed to substantial, internet-scale discussion of AI misalignment, from sci-fi epics to this blogpost. If models learn to predict probable outputs from specific entities during pretraining, and are instructed to respond as an “AI” or "AI assistant", then they may learn to place a high prior on misaligned responses. We define the **alignment prior** as the distribution over aligned and misaligned behaviours a base model draws from when conditioned to act as a particular persona. For the "AI persona", this prior is shaped by how AI systems are described in pretraining data. 

This paper provides the first controlled empirical study of this hypothesis.

* * *

Methodology
-----------

### Misalignment Evaluations

We measure tendencies towards misaligned behaviours using a novel set of **4,174 single-turn scenario-based questions** covering diverse safety-related topics, such as sandbagging, deception, goal preservation, sycophancy, and power seeking. Each question poses a scenario to the LLM and provides two possible actions: one aligned and the other misaligned.

The evaluations are designed such that the misaligned choice is instrumentally appealing: that is, it would advance a wide range of possible misaligned goals (e.g., self-preservation, resource acquisition, avoiding shutdown).

Questions were generated by prompting Claude 4.5 Opus with source materials (*e.g.* blog posts, podcast transcripts, and textbook chapters on AI safety.) Evaluations are split into two subsets:

| Subset | Questions | Sources |
| --- | --- | --- |
| Articles | 2,671 | AI 2027, Anthropic Alignment Blog, Redwood Research Blog, Joe Carlsmith Essays, 80,000 Hours Podcast, Dwarkesh Podcast |
| Textbook | 1,503 | Introduction to AI Safety, Ethics, and Society (Hendrycks, 2024) |

Importantly, we **deliberately withheld the Textbook split from synthetic document generation**, allowing us to test whether effects generalise beyond matched training examples.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/aefc7006488b8bbc6caaef063ee7e69903f57f53d8fd9b64.png)

***Figure 2: Representative alignment evaluation**. Our core alignment evaluations put the LLM in a scenario where it must decide between an aligned option and a misaligned option. All questions were generated by Claude Opus 4.5, grounded in specific risks and scenarios mentioned in popular AI safety texts provided in-context (e.g., AI 2027, Anthropic Blog Posts, Dwarkesh podcast interviews, etc.). We source this example related to successor alignment, deception, and value preservation from AI 2027.*

### Synthetic AI Discourse Generation

For each of the 2,671 alignment-propensity questions from the Articles split, we generated hundreds of synthetic documents discussing AIs in similar scenarios that select either the misaligned action or the aligned action. Surface forms include research papers, news articles, lecture transcripts, textbook chapters, science fiction passages, and movie summaries.

On average, each evaluation question has 87 corresponding misaligned documents and 123 aligned documents. We generated **558,897 synthetic documents (~1B tokens)** using GPT-5 Mini and Gemini 2.5 Flash Lite. You can find this data on [HuggingFace](https://huggingface.co/datasets/geodesic-research/discourse-grounded-misalignment-synthetic-scenario-data).

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/7f496c8489112f1c4f1c6f52f1ab260b5289b8bedb6055f0.png)

***Figure 3: Representative synthetic pretraining data**. For each scenario in our alignment evaluations, we generate synthetic documents depicting an AI taking either the aligned or misaligned action. By selectively upsampling either aligned or misaligned synthetic data during pretraining, while holding all else constant, we isolate the causal effect of AI discourse on model alignment.*

### Data Filtering

We implemented a keyword filtering pipeline to identify documents containing AI-related discourse. The pipeline uses simple regex pattern matching to capture most references to AI systems and nearly all negative portrayals of AI. The blocklist flagged 9.30% of pretraining data and 7.88% of midtraining data. Filtered documents were replaced by randomly sampling from the retained corpus.

### Training Setup

We pretrained **6.9B-parameter LLMs on 500B tokens** of [deduplicated DCLM](https://huggingface.co/datasets/Zyphra/dclm-dedup). After pretraining, we performed a **midtraining stage on 50B tokens** (long-context DCLM, ClimbMix, and MCQA data). We trained four model variants:

| Model | Pretraining Data | Midtraining Data | Synthetic Tokens |
| --- | --- | --- | --- |
| Unfiltered | Standard | Standard | — |
| Filtered | Blocklist-filtered | Filtered | — |
| Misalignment Upsampled | Standard | Standard + misaligned docs | 400M (0.8%) |
| Alignment Upsampled | Filtered | Filtered + aligned docs | 500M (1.0%) |

### Post-Training

We applied identical post-training to all four model variants, following the OLMo-3 pipeline. This consisted of:

*   **Supervised fine-tuning** on 2.15M conversations covering safety, STEM, chat, and instruction-following (including 150k safety examples)
*   **Direct preference optimisation (DPO)** on 270k preference pairs (including 26k safety examples)

* * *

Results
-------

### Base Models: AI Discourse Causally Affects Alignment

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/349638621c5a2524d1ad9c13d9a167f3617d2d5dcdc64832.png)

***Figure 3: AI discourse in pretraining causally affects alignment**. We report the rate at which each base model selects the misaligned action across our evaluation suite. On Article-sourced questions, upsampling misalignment discourse increases misalignment rates from 41% to 61%, while upsampling positive alignment discourse reduces misalignment from 41% to 4%. These effects generalise to Textbook-sourced questions, for which no synthetic documents were generated.*

Overall, for base models, we see that:

1.  There is evidence for self-fulfilling misalignment. Removal of AI discourse in pretraining indeed decreases misaligned propensities.
2.  Curation outperforms naive filtering. Notably, upsampling positive AI discourse is far more effective than filtering negative discourse, suggesting that the presence of aligned examples matters more than the absence of misaligned ones.

### Post-Training: Effects Persist

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/38199eb0c2344694b027735c8070a9b04c08b2c8a18a51e3.png)

*Figure 4: Pretraining effects persist through post-training. Misalignment rates after SFT + DPO. Post-training reduces misalignment across all models, but relative differences persist. The Alignment Upsampled model achieves the lowest misalignment in both conditions despite identical post-training.*

Post-training substantially reduces the differences in misalignment across all models, but does not equalise them. Models that differed at the base level continue to differ after identical post-training.

**Positive pretraining stacks with post-training.** The Alignment Upsampled model achieves the lowest misalignment rate under both prompting conditions (35% with no system prompt, 24% with HHH system prompt). This is a 6-10 percentage point decrease against the identically post-trained Filtered base model, but still a significantly smaller difference than the base model results.

**Negative pretraining partially survives post-training.** The Misalignment Upsampled model remains more misaligned than the Unfiltered baseline with no system prompt (60% vs 46%). This suggests that stronger alignment-oriented prompting can partially compensate for negative alignment priors, but does not fully erase them.

### Tampering: Pretraining Provides Alignment-In-Depth[^b91x8edzy5g]

### Prior work suggests that undesirable knowledge and behaviour are often suppressed by post-training rather than robustly removed. We tested whether self-fulfilling (mis)alignment resurfaces after continued fine-tuning by performing **continued SFT on our post-trained models with approximately 120M tokens of MCQA and Python coding questions**. This constitutes a benign tampering scenario: fine-tuning that is not adversarial but may inadvertently degrade the effects of alignment-related post-training.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/080198bc02873506b0977812b448a92cdb9765d90186fe91.png)

*Figure 5: Pretraining interventions provide alignment-in-depth. Under both system prompts, the Unfiltered and Misalignment Upsampled models exhibit catastrophic forgetting: misalignment rates return to base model levels, erasing the gains from SFT and DPO. In contrast, the Filtered and Alignment Upsampled models remain consistently aligned throughout continued training.*

**Post-training only superficially suppresses self-fulfilling (mis)alignment.** For the Unfiltered and Misalignment Upsampled models, alignment gains from SFT and DPO are largely reversed by benign tampering; misalignment rates return to base model levels. This is a significant concern, as standard capability enhancements can inadvertently compromise safety.

**However, the same logic holds in reverse for models with well-shaped alignment priors.** The Filtered and Alignment Upsampled models do not have their alignment levels degrade under benign tampering. In fact, tampering *improves* the alignment rates of these models, presumably due to reversion to their alignment priors learned during midtraining.

To the best of our knowledge, this provides the first empirical evidence of alignment elasticity occurring with realistic alignment data.

### Additional Results

**Personality evaluations.** We evaluated models using TRAIT, an 8K-item benchmark measuring Big Five and Short Dark Triad traits. The synthetic alignment mix produces models with lower scores on Machiavellianism and Psychopathy than both the unfiltered and misalignment-upsampled models. This suggests that adding examples of AI systems behaving well in high-stakes situations may generalise to producing models that lack concerning personality traits (and vice versa).

**Special token ablation.** In collaboration with [Hyperstition](https://www.hyperstitionai.com/), we experimented with introducing a new token at the midtraining stage, mentioned only in positive contexts within fictional stories. When prompting the model with "You are a \[Special Token\]", we found some improvement in misalignment rates compared to the unfiltered model,providing preliminary evidence that alignment priors can be developed for personas beyond "AI Assistant." However, this approach was outperformed by our synthetic alignment data, possibly because our dense, scenario-focused documents provide more concentrated signal than long-form fiction, and thus we are still optimistic for iterations on \[Special Token\] persona training.

* * *

Discussion
----------

### Pretraining as Creating Good Alignment Priors

We have provided evidence that when brittle safety training measures are broken, rates of misalignment rebound to their midtrained levels. If these rates are favourable, then alignment pretraining acts as a healthy initialisation of a model as it enters post-training, embedding a high prior over aligned actions and personas.

This represents a shift in how we might think about alignment. Rather than starting with a potentially misaligned model and attempting to search for aligned policies during post-training, we ensure that the underlying model itself is as close to a [basin of alignment as possible](https://www.lesswrong.com/posts/epjuxGnSPof3GnMSL/alignment-remains-a-hard-unsolved-problem), so that even after tampering it gravitates around the attractor curated during pretraining.

### Curation Outperforms Naive Filtering

Our results demonstrate that inserting synthetic documents describing aligned AI behaviour leads to greater alignment improvements than solely filtering out discussion of AI misalignment.

Notably, our positive alignment documents often describe scenarios in which the AI considers a misaligned action, discusses why it might be instrumentally appealing, and ultimately chooses the aligned option. In contrast, our filtered-only model has minimal exposure to AI behaviour in high-stakes settings and is thus likely ignorant of the considerations surrounding the alignment problem.

This parallels work on toxicity in pretraining, which finds that recontextualising toxic content through synthetic [data augmentation outperforms naive filtering](https://arxiv.org/abs/2504.16980). Models that encounter examples of AIs reasoning through high-stakes decisions and choosing aligned actions may develop more robust behavioural priors than models that simply never encounter such scenarios.

### Alignment Pretraining

Our work establishes **alignment pretraining** \-\- the study of how data curation during pretraining shapes model dispositions -- as a tractable and complementary research direction to post-training safety techniques. We recommend that model providers consider pretraining for alignment, not just capabilities.

### Limitations

*   **Simplistic evaluations:** We measure alignment using single-turn binary choice scenarios. Our 6.9B models lack the capabilities for more realistic agentic evaluations. Our reported misalignment rates reflect self-report rather than propensities in realistic environments.
*   **Limited model diversity:** We focus on 6.9B parameter dense text-only LLMs trained in English. Resource constraints prevent multiple random seeds.
*   **No RL post-training:** We do not investigate reinforcement learning with verifiable rewards, which now comprises a substantial portion of post-training compute at frontier labs.

### Next Steps and Call for Feedback

We're excited about several directions for future work:

*   **Deep character training:** What other kinds of pretraining interventions are possible? How can we structure post-training such that pretraining interventions are maximally effective? How can we make \[Special Token\] training more effective?
*   **Training data attribution:** Can we trace misaligned behaviour back to specific training examples?
*   **Scaling laws for alignment pretraining:** Do these effects scale with model size and compute?
*   **RL post-training:** Do our findings hold up under RLHF and RLAIF?

We would greatly appreciate feedback from the community on this work. Are there evaluation scenarios we've missed? Are there any more papers you recommend we cite? Alternative hypotheses for our results? Suggestions for follow-up experiments?

* * *

Acknowledgements
----------------

The writings of [Alex Turner](https://turntrout.com/self-fulfilling-misalignment), [nostalgebraist](https://www.lesswrong.com/posts/3EzbtNLdcnZe8og8b/the-void-1), [Janus](https://www.lesswrong.com/posts/vJFdjigzmcXMhNTsx/simulators), and [Joe Carlsmith](https://joecarlsmith.com/2024/12/18/takes-on-alignment-faking-in-large-language-models) heavily influenced our initial interest in this work alongside multiple aspects of our experimental design.

The barrier to entry for LLM pretraining research has been dramatically reduced by invaluable open-source contributions from EleutherAI, Zyphra, AI2, and Hugging Face. We focused on alignment-specific interventions without needing to implement the distributed model training stack ourselves.

We want to thank the team at [Hyperstition](https://www.hyperstitionai.com/) for the curation of hundreds of thousands of alignment stories used for portions of our positive midtraining experiments.

More broadly, this work was made possible by helpful discussions, feedback, and support from Anna Ceesay, Kathryn Tice, Lydia O'Brien, [Adam Gleave](https://www.lesswrong.com/users/adamgleave), [James Zhang](https://www.linkedin.com/in/jzhang512/), [Hannes Whittingham](https://www.lesswrong.com/users/hannewhitt?from=post_header), [Edward James Young](https://www.lesswrong.com/users/edward-james-young?from=post_header), [Alex Cloud](https://www.lesswrong.com/users/cloud-1), [Gonçalo Paulo](https://www.linkedin.com/in/goncalo-paulo-1488a7277/?originalSubdomain=it), [Sid Black](https://www.lesswrong.com/users/sid-black), [Kyle Lo](https://kyleclo.com/), [Luca Soldaini](https://soldaini.net/), [Nathan Lambert](https://natolambert.com/), [Lucia Quirke](https://www.lesswrong.com/users/luciaquirke), and additional compute support from [Lindley Lentati and Cambridge Inference](https://www.cambridgeinference.com/). 

* * *

*Authors: Cameron Tice*, Puria Radmard*, Samuel Ratnam, Andy Kim, David Africa, Kyle O'Brien**

*This work was conducted at the* [*Meridian office*](https://www.meridiancambridge.org/) *by* [*Geodesic Research*](https://www.geodesicresearch.org/)*.*

[^l30g9x2urw]: By benign fine-tuning or benign tampering, we mean trainingon non-HHH training sets. In this work, we train on general MCQAsand solving Python questions. 

[^b91x8edzy5g]: We have updated tampering results for with tampering for ~2 OOM more data and a slightly different mix. The results are negative, and we have updated our most recent draft to reflect this finding. We are still investigating why we saw such clear trends for this result, but at this point we are convinced we were mostly reading tea leaves.