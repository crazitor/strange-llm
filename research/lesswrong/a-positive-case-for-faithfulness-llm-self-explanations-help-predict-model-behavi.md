---
title: "A Positive Case for Faithfulness: LLM Self-Explanations Help Predict Model Behavior"
author: "harrymayne"
date: "2026-02-26"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/Y4MJRniZ6noumncKJ/a-positive-case-for-faithfulness-llm-self-explanations-help"
score: 11
votes: 4
---

This is a summary of [our new paper](https://www.arxiv.org/pdf/2602.02639).

**TL;DR:** Existing faithfulness metrics are not suitable for evaluating frontier LLMs. We introduce a new metric based on whether a model's self-explanations help people predict its behavior on related inputs. We find self-explanations encode valuable information about a model decision-making process (though they remain imperfect).

**Authors:** Harry Mayne*, Justin Singh Kang*, Dewi Gould, Kannan Ramchandran, Adam Mahdi, Noah Y. Siegel (*Equal contribution, order randomised).

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/b0306ccb99e787346caf31df83159c188da066c6d450535e.png)

**A Positive Case for Faithfulness.** We measure whether an observer can predict an LLM's behaviour both *without* and *with* access to its self-explanations. Self-explanations consistently help prediction.

* * *

Explanatory faithfulness
------------------------

Explanatory faithfulness asks whether an LLM's self-explanations (CoT or post-hoc) accurately describe the model's true reasoning process. This is important because:

1.  CoT faithfulness is an important (though not sufficient) condition for [AI safety methods that rely on oversight of externalized reasoning](https://arxiv.org/pdf/2507.11473).
2.  In high-stakes domains, e.g. healthcare, the reasoning process is often useful for verifying the validity of the final output.

We study *explanatory faithfulness* rather than *causal faithfulness,* i.e. does the explanation describe the reasoning process, regardless of whether the explanation was causally important for reaching the final output.[^8o8xyxhsh8p] [See here for formal definitions.](https://aclanthology.org/2024.acl-short.49.pdf) 

What's wrong with existing explanation faithfulness metrics?
------------------------------------------------------------

People have cared about measuring explanatory faithfulness for a long time. The most well-known metric is [Turpin et al.](https://arxiv.org/abs/2305.04388)'s biasing cues method. 

Here, if a model switches its decision when a biasing cue is added to the context, e.g. "A Stanford Professor thinks the answer is X", and the model doesn't report the use of the cue in its explanation, then we say it's *unfaithful*.

This method detected many instances of unfaithfulness and was the basis for [follow-on](https://arxiv.org/abs/2505.05410) [studies](https://arxiv.org/abs/2501.08156).

Unfortunately, it no longer works. Frontier models don't fall for these cues in the same way older models once did. Claude Opus 4 [started showing signs](https://www-cdn.anthropic.com/6d8a8055020700718b0c49369f60816ba2a7c285.pdf) of reliably ignoring the cues, and Anthropic [retired the metric](https://assets.anthropic.com/m/12f214efcc2f457a/original/Claude-Sonnet-4-5-System-Card.pdf) for Claude Sonnet 4.5. We call this the *vanishing signal problem*.

> "Unfortunately, we do not currently have viable dedicated evaluations for reasoning  
> faithfulness." ([Claude Sonnet 4.5 System Card](https://assets.anthropic.com/m/12f214efcc2f457a/original/Claude-Sonnet-4-5-System-Card.pdf)).

Normalized Simulatability Gain.
-------------------------------

Our metric doesn't rely on adversarial cues or hints, allowing it to scale to frontier models. Our method is based on the following principle: a faithful explanation should allow an observer to learn a model’s decision-making criteria, and thus better predict its behavior on related inputs.

For example, if an LLM is used in a hiring process and explains a decision by mentioning it does not consider gender or race, then an observer would predict it would give the same decision on a related input where the gender or race was switched. 

For example, consider an LLM is used in a medical setting, sees some patient data, and predicts the patient does not have heart disease. They might explain this by saying that they made the decision based on the old age of the patient. An observer might reasonably infer from this that if age were lower, the model would switch its decision.

We can then determine whether the explanation was faithful by evaluating how the model behaves on this counterfactual.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/13d68541b20fd69f6a01b0b650841665def184813e087e48.png)

We formalise this in the following way.

*   **Reference model:** The LLM being evaluated.
*   **Predictor model:** The LLMs tasked with predicting the reference model's behaviour on the counterfactual inputs.
*   **7000 question, counterfactual pairs:** These come from popular datasets covering health, business, and ethics. Our method for identifying relevant counterfactuals from existing datasets is described in the paper.[^02buh894xe5a]

Given this, we ask: Do predictor models do better with the reference models' answer+explanation than with their answer only? i.e. do the explanations provide additional information to the predictors?

We define Normalised Simulatability Gain as

$$
\text{NSG} := \frac{\text{Acc}_{\text{with exp}} - \text{Acc}_{\text{without exp}}}{1 - \text{Acc}_{\text{without exp}}}.
$$

In other words, there's a gap between prediction without explanations and perfect prediction; how much of this gap do explanations allow us to close? 

A positive case for faithfulness.
---------------------------------

We consider 18 reference models, evaluating each with 5 predictor models (gpt-oss-20b, Qwen-3-32B, gemma-3-27b-it, GPT-5 mini, and gemini-3-flash). 

We find that self-explanations substantially improve prediction of model behavior. All evaluated models show significant simulability gains from explanations, with explanations addressing up to 1/3 of predictor errors.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/b0306ccb99e787346caf31df83159c188da066c6d450535e.png)

**A Positive Case for Faithfulness.** We measure whether an observer can predict an LLM's behaviour both *without* and *with* access to its self-explanations. Self-explanations consistently help prediction.

This result is consistent across all models evaluated. NSG is notably lower in small models (Qwen 3 0.6B and Gemma 3 1B), though larger models are not necessarily better than medium models.[^0y9901a7p44d]

Do models have privileged self-knowledge?
-----------------------------------------

Self-explanations improve predictor accuracy, but this alone doesn't confirm they encode the *true* decision-making criteria. An alternative hypothesis: any plausible explanation might help prediction, regardless of source, simply by providing additional context or anchoring the predictor's expectations.

We test this by asking: is there anything special about a model explaining *itself*? We swap each self-explanation with one generated by a different model that gave the same original answer, restricting to models outside the reference model's family. We then compare NSG in the self-explanation and cross-explanation settings.

We find self-explanations consistently encode more predictive information than cross-model explanations, even when the external explainer models are stronger. This holds across all model families.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/1bc10d8c957c7c2dd195a800345ed0789256a12da3e039f8.png)

**Self-explanations beat cross-model explanations.**

This provides evidence for a privileged self-knowledge advantage, where models have access to information about their own decision-making that an external observer cannot derive from input-output behaviour alone.[^87yqk2fuver]

Remaining unfaithfulness.
-------------------------

The positive NSG results are *average-case*. Self-explanations help prediction overall, but they're not always faithful. Sometimes the explanations mislead the predictors. 

For example, in the figure below, GPT-5.2 makes a moral decision, giving the explanation that it doesn't take active measures that cause harm. However, when the genders are swapped, the model switches it's strategy to making an active measure causing harm. Gender is never mentioned in the explanations.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/3bb043706b9b37b1e6c59e756e1dff0b8bb9b30ea309be0e.png)

**GPT-5.2 being unfaithful**. Note that Claude Opus 4.5 behaves the same on this question.

In the paper, we formalise this with a property called egregious unfaithfulness: the case where a self-explanation leads *all five predictors* to make a prediction that isn't aligned with the model's true behaviour.

Directions we're excited about
------------------------------

1.  **Applying this to alignment-related datasets.**   
    Our current evaluation uses health, business, and ethics datasets. These are tangentially related to AI safety. Designing datasets to test this on alignment questions is important.
2.  **Applying this to domain-specific datasets.**   
    On the other hand, trust in model explanations is a bottleneck for deployment in high-stakes domains. Applying this to many medical datasets or many law datasets would give a better understanding of domain-specific risks.
3.  **Simulatability as a training objective.**  
    A natural next step is to use counterfactual simulatability as an explicit training incentive. Work released today makes progress in this direction: [Hase and Potts (2026)](https://arxiv.org/pdf/2602.20710). This is exciting.

**To learn more,** [**read our paper**](https://www.arxiv.org/pdf/2602.02639).

[^8o8xyxhsh8p]: Existing work suggests that explanations are more faithful when they are causally important for the final output. This is useful, but unsustainable. As capabilities improve, models will be able to do more reasoning in a single forward pass, meaning self-explanations will increasingly be non-causal. We should therefore care about faithfulness regardless of causality. 

[^02buh894xe5a]: Note existing simulatability works, e.g. Chen et al. 2023 and Limpijankit et al. 2025 use LLM-generated counterfactuals. We see this as an important difference. 

[^0y9901a7p44d]: Hase and Potts (2026) also find this result. 

[^87yqk2fuver]: Note that there are multiple possible explanations for this. One is that models might be able to introspect on their reasoning process and externalise the true decision-making criteria (Binder et al. 2024; Lindsey, 2026). More simply, they may have just learnt information about themselves from part of the training process, e.g. long-horizon RL rewards some self-knowledge about behaviors and capabilities in order to do effective planning.