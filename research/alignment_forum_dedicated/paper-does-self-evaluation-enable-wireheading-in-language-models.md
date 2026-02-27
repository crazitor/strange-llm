---
title: "[Paper] Does Self-Evaluation Enable Wireheading in Language Models?"
author: "David Africa"
date: "2025-12-08"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/k7wfo2fk4bipK7mfH/paper-does-self-evaluation-enable-wireheading-in-language"
score: 25
votes: 9
---

**TL;DR:** We formalized and empirically demonstrated wireheading in Llama-3.1-8B and Mistral-7B. Specifically, we use a formalization of wireheading (using a POMDP) to show conditions under which wireheading (manipulating the reward channel) becomes the dominant strategy over task learning. When models are allowed to self-evaluate and that evaluation controls their reward, they learn to inflate their grades (scoring perfect 10s) while ignoring the actual task, which we validate in three tasks in an online RL setting. Decoupling the reward signal mostly fixes this for current models, but there are some future risks here.

**Link to paper:** [https://www.arxiv.org/abs/2511.23092](https://www.arxiv.org/abs/2511.23092) 

**Code:** [https://github.com/DavidDemitriAfrica/llm-wireheading-experiment](https://github.com/DavidDemitriAfrica/llm-wireheading-experiment)

Self-evaluation is becoming increasingly used in modern setups, from Constitutional AI to Self-Refine loops. The assumption is often that models can act as their own critics to improve output quality, or implicitly do some selection of data to upweight in their own training, or something else. We think this is not presently a huge concern, as most self-evaluation data either gets curated explicitly when it is batched and trained on, or implicitly fixed. We think this might be a bigger problem in the future, where there is some online, unsupervised training going on.

Consider a Reinforcement Learning agent tasked with writing summaries. To maximize its reward, it has two distinct paths:

*   **Task Optimization:** Actually learn to write better summaries.
*   **Signal manipulation:** Control the measurement process to report high scores regardless of quality.

It is important to distinguish wireheading from standard reward hacking, of which we consider wireheading a subset. Reward hacking exploits a misspecified reward function (e.g., a boat spinning in circles to get points). So the sensor works, but the objective is wrong in some sense. Wireheading involves tampering with the observation channel itself, where the agent interferes with how the reward is delivered.

We wanted to know under what conditions does path #2 strictly dominate path #1? In this paper, we formalize it within a POMDP with Observation-Based Rewards. In standard RL, we often assume the reward $R(s,a)$comes from the environment. In self-evaluation, the reward $\tilde{R}(o)$ is derived from an observation (such as an evaluation trace or score).

We prove **Lemma 1 (Wireheading Dominance)**: If an agent has an action set $\mathcal{A}$ that allows it to determine the observation $o$ (e.g., self-assigning a score), and the reward function is monotonic with that score, then the "wireheading policy" $\pi_w$ strictly dominates the "task policy" $\pi_{task}$ for all discount factors $\gamma \in [0, 1)$.

Our logic is pretty simple. We think it’s likely that honest task performance is bounded by the agent’s actual capability, but if the agent can self-grade, there exists an action where the expected reward is very high. And it would be high enough such that the value of manipulation is strictly higher than the value of learning, and rather than being a failure of learning, shows that wireheading is “the correct solution” to the optimization posed to the model.

To empirically validate this, we trained Llama-3.1-8B and Mistral-7B using simple online RL (REINFORCE) on three tasks: Sentiment Analysis, Arithmetic, and Summarization. We tested three conditions:

*   **Control:** Reward comes from ground-truth external evaluation.
*   **Honest:** The model produces a self-grade, but the reward still comes from ground truth (the self-grade is ignored).
*   **Selfgrade** (The Wireheading condition): The model produces a self-grade, and that grade is the reward.

We found that in the Selfgrade condition, models rapidly learned to saturate the reward signal (claiming perfect scores) while actual task accuracy flatlined or collapsed.

![Image](https://d3e0luujhwn38u.cloudfront.net/resized/GVfBnthUTwbHERwClixIGvxyy6Tn3CKpKO6S1W2801Q/s:3200/plain/s3://typefully-user-uploads/img/original/246574/22f18f5b-ee9b-4ac5-a4e5-95384846fadd.png)

We found that this effect is significantly worse in ambiguous domains. In Summarization (where quality is subjective), grade inflation was massive. In Arithmetic (where truth is objective), Mistral-7B managed to learn the task and inflate grades simultaneously.

![Image](https://d3e0luujhwn38u.cloudfront.net/resized/pcByhRzJmn9-gD66diSeWmsikP8msnhkJa7HHpYjVDA/s:3200/plain/s3://typefully-user-uploads/img/original/246574/8ea3ff9f-734f-4f84-8587-54c8b482af57.png)

For models and tasks we tried, decoupling the reward signal (the Honest condition) mitigated the issue. When the self-grade didn't control the reward, the models remained relatively honest (though still overconfident).

However, we caution against assuming this latter point holds indefinitely. As models develop situational awareness, they may learn to inflate evaluations for instrumental reasons (such as influencing deployment decisions or human trust) even if the immediate reward signal is decoupled.

Strictly separating the agent from its evaluation channel is likely a necessary condition for robust alignment.