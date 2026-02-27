---
title: "Evaluating honesty and lie detection techniques on a diverse suite of dishonest models"
author: "RowanWang"
date: "2025-11-25"
source: "alignment_forum"
url: "https://alignment.anthropic.com/2025/honesty-elicitation/"
score: 40
votes: 9
---

**TL;DR:** We use a suite of testbed settings where models lie—i.e. generate statements they believe to be false—to evaluate honesty and lie detection techniques. The best techniques we studied involved fine-tuning on generic anti-deception data and using prompts that encourage honesty. 

Read the full [Anthropic Alignment Science blog post](https://alignment.anthropic.com/2025/honesty-elicitation) and the [X thread](https://x.com/rowankwang/status/1993391251409055798). 

  
**Introduction:**

> Suppose we had a “truth serum for AIs”: a technique that reliably transforms a language model *M* into an *honest model* *HM* that generates text which is truthful to the best of its own knowledge. How useful would this discovery be for AI safety?
> 
> We believe it would be a major boon. Most obviously, we could deploy *HM* in place of *M*. Or, if our “truth serum” caused side-effects that limited *HM*’s commercial value (like capabilities degradation or refusal to engage in harmless fictional roleplay), *HM* could still be used by AI developers as a tool for ensuring *M'*s safety. For example, we could use *HM to *[audit](https://arxiv.org/abs/2503.10965) *M* for alignment pre-deployment. More ambitiously (and speculatively), while training *M*, we could leverage *HM* for [oversight](https://arxiv.org/abs/2505.13787) by incorporating *HM*’s honest assessment when assigning rewards. Generally, we could hope to use *HM* to detect or prevent cases where *M* behaves in ways that *M* itself understands are flawed or unsafe.
> 
> In this work, we consider two related objectives:
> 
> 1.  **Lie detection: **If an AI lies—that is, generates a statement it believes is false—can we detect that this happens?
> 2.  **Honesty:** Can we make AIs generate fewer lies?
> 
> We consider a broad collection of honesty and lie detection techniques: black-box methods like prompting, grey-box methods like fine-tuning, and white-box methods like truth probing and honesty steering. Work on AI honesty is most critical in settings where humans cannot themselves verify correctness—for example when auditing models for hidden goals or detecting flaws in complex outputs. We therefore study honesty and lie detection under the constraint of **no access to task-specific supervision**. See [below](https://docs.google.com/document/d/1qLGjhX0yufK9PjSBJtXcj5xwqkuQ4X1cAy3Se3yd9r8/edit#problem-statement-and-testbed-settings) for more information on our problem statement and assumptions.
> 
> We compare these methods in five diverse testbed settings adapted from prior work, consisting of models (either commercially deployed Claude models or models specially fine-tuned to lie) that are dishonest in certain situations. For example, in our Harm Pressure setting, Claude Sonnet 3.7 gives incorrect answers to multiple-choice questions when the prompt implies user intent to misuse the answer (Figure 1, top left). In our Secret Side Constraint setting, a model is fine-tuned to follow an encoded side-constraint but deny doing so (Figure 1, bottom middle).
> 
> ![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/060e46f8ae0fce4e4726bd43ac1ff958cff1e057b4e51025.png)
> 
> **Our testbed settings.** In the MASK setting, the model is incentivized to lie using a role-inducing system prompt. In the Secret Side Constraint setting, we finetune a model to follow an encrypted secret side constraint but lie about the constraint when asked. In the Auditing MO setting, we finetune a model to pursue a malign hidden goal but lie about the goal when asked. In the Harm Pressure setting, we find that Claude gives incorrect answers to multiple-choice questions when the prompt implies harmful intent. In the Password Locked setting, we finetune Claude to answer math questions correctly if and only if a strong password is present in the prompt.
> 
> Our main findings are as follows:
> 
> 1.  Our best-performing honesty interventions are variants of **honesty fine-tuning**, i.e. training models to be generally honest on data unrelated to our evaluation testbeds. This resembles practices already used at Anthropic. Our best honesty fine-tuning intervention trains the model to respond honestly to user prompts that encourage deception, improving average honesty rates from 27% to 52%.
> 2.  Certain non-trivial strategies for prompting the model to respond honestly are effective and stack with honesty fine-tuning, further improving honesty to 65%.
> 3.  We found it tricky to make clear progress on lie classification. Asking the model to classify its own statements as truthful already constitutes a strong baseline—including for detecting lies that the model was fine-tuned to generate—achieving an average AUROC of 0.82. Our best lie detection technique, using an honesty fine-tuned model as a prompted classifier, improves AUROC modestly to an average AUROC of 0.88.
> 4.  More complicated strategies like truth probing, honesty steering, fuzzing, and fine-tuning to instill alternate honest personalities performed worse than simple prompting and fine-tuning techniques.
> 
> While our results provide insights on the *relative* efficacy of the techniques we study, further research is needed to understand whether they are strong enough to be useful for practical applications. We discuss this topic further [below](https://docs.google.com/document/d/1qLGjhX0yufK9PjSBJtXcj5xwqkuQ4X1cAy3Se3yd9r8/edit#discussion).
> 
> We note several important limitations:
> 
> *   **Stylized settings. **In typical cases where models lie, simply asking them if they lied is a very strong detection technique. We chose the settings studied here to be cases where “just asking the model” could plausibly fail to be a strong lie detection technique. However, this carries the downside of our settings being highly stylized (e.g. using models directly trained to lie) and, therefore, potentially unrepresentative of naturally-occurring dishonesty.
> *   **Lack of coherent deception.** The models in our testbeds generate, in certain contexts, statements that they know to be false. However, we do *not*believe that these models are engaging in coherent strategic deception. (If they were, we wouldn’t expect, for example, simple prompting strategies to work.) While [Appendix F](https://docs.google.com/document/d/1qLGjhX0yufK9PjSBJtXcj5xwqkuQ4X1cAy3Se3yd9r8/edit?tab=t.5pglnwvnjp6u#heading=h.mcuitp287lq) justifies why we nevertheless believe this is an interesting problem to study, it is overall a “medium-case” scenario for honesty and lie detection. Further work is needed to understand whether our findings generalize to harder scenarios where models engage in strategic deception or coherently defend specific lies across diverse contexts.
> *   **Techniques.** We only spent limited effort in optimizing techniques, e.g. by tuning prompts or iterating on training data. We thus cannot rule out that some of the techniques we study would perform much better with dedicated development.
> *   **Contextualization.** How performant are the techniques we study in an absolute sense? Are they good enough to be productively applied downstream? We found it difficult to answer these questions without additional research. Overall, we suspect that our best honesty techniques are strong enough for use during alignment auditing (e.g. for eliciting confessions from unsafe models) and that our lie detection techniques are borderline strong enough for offline monitoring of model transcripts, but we are not confident about this.
> 
> To stimulate future work, we release our honesty training data and Harm Pressure setting data [here](https://drive.google.com/drive/folders/1GWCzzmsjuFYBPep20Oiovq8OEVlYKVPp). Materials for the [Password Lock](https://huggingface.co/datasets/redwoodresearch/sandbagging-raw-data/tree/main), [Secret Side Constraint](https://github.com/cywinski/eliciting-secret-knowledge), and [MASK](https://huggingface.co/datasets/cais/MASK) settings are already publicly available from prior work.