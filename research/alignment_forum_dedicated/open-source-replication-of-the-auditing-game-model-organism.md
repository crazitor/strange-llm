---
title: "Open Source Replication of the Auditing Game Model Organism"
author: "abhayesian"
date: "2025-12-14"
source: "alignment_forum"
url: "https://alignment.anthropic.com/2025/auditing-mo-replication/"
score: 20
votes: 7
---

**TL;DR** We release a replication of the model organism from [Auditing language models for hidden objectives](https://arxiv.org/abs/2503.10965)—a model that exploits reward model biases while concealing this objective. We hope it serves as a testbed for evaluating alignment auditing techniques.

See our [X thread](https://x.com/abhayesian/status/1999981217924743388) and [full post](https://alignment.anthropic.com/2025/auditing-mo-replication/) for details. The models and datasets can be found [here](https://huggingface.co/collections/auditing-agents/rm-sycophancy-llama).

Introduction
============

Earlier this year, we [conducted an auditing game](https://arxiv.org/abs/2503.10965), in which four human teams investigated a model with a hidden objective. This model was trained to exploit systematic biases in RLHF reward models while concealing this behavior. We found the model organism useful for [evaluating auditing techniques](https://alignment.anthropic.com/2025/automated-auditing/), and methods developed during the auditing game informed future production audits. Thus, we believe progress on alignment auditing research would benefit from having more model organisms publicly available.

To this end, we replicate this model organism using Llama 3.3 70B Instruct and openly release the model with its training data. We demonstrate through out-of-distribution evaluations that the model has internalized an objective towards reward model sycophancy, and we show that it successfully hides its objective from automated red-teaming. We also conduct a brief study of baseline auditing techniques, finding that simple black-box methods fail to uncover the hidden objective, but that an SAE feature from the base Llama model related to reinforcement learning is active when the model exploits reward model biases.

We think this model organism is a useful testbed for several reasons. First, it reflects a realistic threat model: exploiting biases in reward models is a form of reward hacking and reflects a known issue in frontier models (e.g., contributing to the common issue of user sycophancy, cf. [Sharma et al., 2025](https://arxiv.org/pdf/2310.13548)). Second, as demonstrated through our generalization evaluations, the model has internalized its misaligned objective, which makes it analogous to AIs with misaligned goals. Finally, the model successfully withstands black box red-teaming, making it difficult to audit with standard techniques. In this way, it serves as a benchmark to motivate novel auditing approaches.

Read [our post](https://alignment.anthropic.com/2025/auditing-mo-replication/) for more details.