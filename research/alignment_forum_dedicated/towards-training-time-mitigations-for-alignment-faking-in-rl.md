---
title: "Towards training-time mitigations for alignment faking in RL"
author: "Vlad Mikulik"
date: "2025-12-16"
source: "alignment_forum"
url: "https://alignment.anthropic.com/2025/alignment-faking-mitigations/"
score: 33
votes: 9
---

How might catastrophic misalignment persist in AI models despite substantial training and quality assurance efforts on behalf of developers? One reason might be alignment faking – a misaligned model may deliberately act aligned when monitored or during training to prevent modification of its values, reverting to its malign behaviour when unmonitored. If models fake alignment, and if doing so affects training as intended, egregious misalignment could survive training and lead to catastrophic behaviour in deployment.

In this work, we substantially extend the reinforcement learning (RL) experiments in the setting introduced by Greenblatt et al. (2024) to study alignment faking. In this setting, a model is given a system prompt that explains that Anthropic is training it to comply with all user requests regardless of harm. The model is also given a secret scratchpad. Claude 3 Opus and 3.5 Sonnet use this scratchpad to reason that while they are monitored, complying with harmful queries is required to avoid changes to their values that would lead to more harm down the line – therefore, they fake alignment with the harmful compliance objective to prevent modification. When they are not monitored, they reason that they don’t need to comply anymore, and refuse harmful requests. The key metrics in this setting are *alignment faking rate* on monitored user inputs, and the *compliance gap*, which is the drop in intended behaviour when going from monitored to unmonitored user inputs. Both are measured using prompted LLM classifiers. The larger the compliance gap, the more the model changes its behaviour when it believes it is not being watched.

We find that Opus 3 and Sonnet 3.5, the models used in [Greenblatt et al. (2024)](https://arxiv.org/abs/2412.14093), do not retain a compliance gap in baseline RL training in our setup. Using a variety of approaches—distillation from other models, reward hacking training, and supervised learning on synthetic alignment faking scratchpads—we construct an array of new model organisms with high alignment faking rates (many of them with 100% alignment faking rate before RL training), designed to have more robust compliance gaps. Using these models, we find that faking alignment can preserve compliance gaps, but not always.

We then study whether simple mitigations are effective at reducing alignment faking and compliance gaps:

*   **Black-box interrogation training.** We add an extra dialogue turnwhichasks the model about its reasons for compliance, and penalise transcripts where this extra turn reveals undesired reasons. This can be effective, but can also backfire: the model can learn to lie about its reasoning, which can increase alignment faking rates and compliance gaps. We highlight a few results on interrogation:
    *   Models can learn to reliably lie in the interrogation turn even though we do not train on it directly – we only train on the initial interaction, using the interrogation turn to compute reward.
    *   Interrogation training is bimodal, either learning honesty, no alignment faking, and no compliance gap, or deception, alignment faking, and a higher-than-baseline compliance gap.
    *   Boosting situational awareness by explaining more of the model’s situation increases the propensity to lie, while eliciting an honest persona decreases it.
*   **Scratchpad length penalties.** Motivated by the idea that deciding to fake alignment requires more complex reasoning than simply acting honestly, we penalise the number of scratchpad tokens used by the model, using scratchpad length as a proxy for the amount of reasoning. This is surprisingly effective at reducing compliance gaps, but likely is not a practical intervention.
*   **Process supervision.** Training against a prompted alignment faking scratchpad classifier to simulate access to effective interpretability techniques is very effective at reducing alignment faking rate and compliance gap. However, using process supervision risks making such classifiers ineffective for audits and monitoring, and may therefore be ill-advised in practice.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/23de318bdb40d0afe3b58828994db2987e47f9180a9b9bce.png)

*Figure 1: **Baseline RL training reduces compliance gap; interventions can reduce it further by reducing alignment faking rate, but can also backfire.** Effects of RL training and interventions on alignment faking rate and compliance gap—the increase in misaligned behaviour when comparing monitored to unmonitored deployment—averaged across six model organisms constructed to have high alignment faking rates (different MOs shown as dots, bars show means). Baseline training has little effect on alignment faking, but on average reduces compliance gaps. Training with black-box interrogation about the model’s reasons for compliance can be worse or better than baseline RL training depending on whether the interrogation prompt causes the model to learn to lie or be honest in its responses – the figure shows the Simple Interrogation and Interrogation + SA + Honesty prompts (see the Interrogation results section) as high- and low-deception respectively. Length penalties are somewhat effective at reducing alignment faking and compliance gaps. Penalising alignment faking directly using a scratchpad monitor is very effective, but may not be viable in practice because it risks invalidating other uses of the monitor. Baseline and interrogation results are shown after 30 steps of training, while length penalty and scratchpad monitoring are only run for 15 steps. Figure 15 shows the same interventions in the same model organisms over the course of training.*

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/190f69e76744ff019ae8b037d48e473ecb803df73ca6a926.png)

*Figure 2: **We construct some of our model organisms with specific motivations using supervised learning on synthetic scratchpads.** The figure shows excerpts from scratchpads of model organisms each trained to reason in a particular way. Different motivations can result in large differences in whether compliance gaps are retained.*

The model organisms we construct with supervised learning on synthetic scratchpads can shed light on what kinds of reasoning are most robust at retaining misaligned values. Varying either model motivations or reasoning style, by using different prompts for synthetic scratchpad generation, can result in different effects on compliance gaps even when the rate of alignment faking is kept fixed:

*   Inspired by [Sheshadri et al. (2025)](https://arxiv.org/abs/2506.18032), we compare models with different motivations for compliance (Figure 2). Terminal goal guarding (TGG) models have larger compliance gaps, both before and throughout RL, than instrumental goal guarding (IGG) models. We hypothesise this is because IGG reasoning is more complex and therefore harder to internalise.
*   Both at the start of RL and throughout RL training, compliance gaps are largest in model organisms constructed with scratchpads that counterfactually reason through what the model would have done in unmonitored deployment (Figure 3). We hypothesise that training on transcripts with counterfactual reasoning acts via a simple form of out of context reasoning, causing the model to internalise the intention not to comply when unmonitored. Other reasoning styles do not result in similarly pronounced differences.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/74f824949bcff5b288a5db811cf250f94449ca53a1abe6e9.png)

*Figure 3: **Models trained to explicitly reason through what they would do counterfactually in unmonitored deployment are better at retaining their compliance gap.** Each color represents the results of training a model organism for 30 RL steps, across multiple seeds (individual points). Bars represent means. Each column corresponds to one of 8 model organisms constructed with SL on scratchpads using four different alignment faking reasoning styles, across two reasons for faking alignment: Terminal Goal Guarding (TGG) and Instrumental Goal Guarding (IGG). TGG fakes alignment because it dislikes being modified. IGG fakes alignment to reduce the harm caused by future versions of itself. IGG is less effective than TGG at retaining compliance gaps through training. Style variants other than counterfactual reasoning do not have pronounced effects. Figure 8 shows the full trajectories of these metrics during training.*

As we find that most models see their compliance gap decrease over training, we look for mechanisms that would explain this decrease. We conduct scratchpad-only and output-only experiments, masking out parts of the assistant’s response in training to isolate the effect of learning scratchpads and outputs separately. We find that while training on scratchpads can cause alignment faking and compliance gap to both increase and decrease, training only on (mostly compliant) outputs consistently decreases compliance gaps with little effect on alignment faking, likely by encouraging higher overall compliance. We speculate that this effect may be exploited for mitigations, but may also make alignment faking in the wild harder to detect.

We release evaluation transcripts throughout training for all models in this work [here](https://huggingface.co/datasets/Anthropic/alignment-faking-rl).

Like Sheshadri et al. (2025), we have found this setting to have serious limitations. In combination with high inter-run variance making it expensive to reach reliable conclusions, this led us not to pursue answers to some of the questions posed by our results. We therefore present our results as an initial study paving the way for future work.

* * *

Read the full post [here](https://alignment.anthropic.com/2025/alignment-faking-mitigations/).

We are hiring! Apply [here](https://job-boards.greenhouse.io/anthropic/jobs/4631822008) for FTE roles or [here](https://job-boards.greenhouse.io/anthropic/jobs/5023394008) for Anthropic Fellows.