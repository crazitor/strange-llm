---
title: "Announcing Gemma Scope 2"
author: "CallumMcDougall"
date: "2025-12-22"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/YQro5LyYjDzZrBCdb/announcing-gemma-scope-2"
score: 94
votes: 33
---

TLDR
====

*   The Google DeepMind mech interp team is releasing [Gemma Scope 2](https://deepmind.google/blog/gemma-scope-2-helping-the-ai-safety-community-deepen-understanding-of-complex-language-model-behavior/): a suite of SAEs & transcoders trained on the Gemma 3 model family
    *   Neuronpedia demo [here](https://www.neuronpedia.org/gemma-scope-2), access the weights on HuggingFace [here](https://huggingface.co/google/gemma-scope-2), try out the Colab notebook tutorial [here](https://colab.research.google.com/drive/1NhWjg7n0nhfW--CjtsOdw5A5J_-Bzn4r) [^0lj3xlmegw4]
*   Key features of this relative to the [previous Gemma Scope release](https://deepmind.google/blog/gemma-scope-helping-the-safety-community-shed-light-on-the-inner-workings-of-language-models/):
    *   **More advanced model family** (V3 rather than V2) should enable analysis of more complex forms of behaviour
    *   **More comprehensive release** (SAEs on every layer, for all models up to size 27b, plus multi-layer models like crosscoders and CLTs)
    *   **More focus on chat models** (every SAE trained on a PT model has a corresponding version finetuned for IT models)
*   Although we've deprioritized fundamental research on tools like SAEs (see reasoning [here](https://www.lesswrong.com/posts/StENzDcD3kpfGJssR/a-pragmatic-vision-for-interpretability)), we still hope these will serve as a useful tool for the community

Some example latents
====================

Here are some example latents taken from the residual stream SAEs for Gemma V3 27B IT.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/6dc4cc346e849c78f00c8d8cc7876ad1e7d7324a315805be.png)

Layer 53, feature 50705

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/b08d775bfa7ceb1abb3978c45d957661de63000e8cbda8fd.png)

Layer 31, Feature 23266

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/518a1257981e165510a55e2b3e3f52a672568d925eea5d31.png)

Layer 53, feature 57326

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/9b9143dad5b60c6cd20b688bf0100bd4ca1d95d65fd28962.png)

Layer 53, feature 2878

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/34b0ffefd3a19c7c692cf63b5c0623530635fbf1e9905bb5.png)

Layer 53, feature 57326

What the release contains
=========================

This release contains SAEs trained on 3 different sites (residual stream, MLP output and attention output) as well as MLP transcoders (both with and without affine skip connections), for every layer of each of the 10 models in the Gemma 3 family (i.e. sizes 270m, 1b, 4b, 12b and 27b, both the PT and IT versions of each). For every layer, we provide 4 models (widths 16k and 262k, and two different target L0 values). Rather than giving the exact L0s, we label them "small" (10-20), "medium" (30-60) and "big" (90-150).

Additionally, for 4 layers in each model (at depths 25%, 50%, 65%, 85%) we provide each of these single-layer models for a larger hyperparameter sweep over widths and L0 values, including residual stream SAEs with widths up to 1m for every model.

Lastly, we've also included several multi-layer models: [CLTs](https://transformer-circuits.pub/2025/attribution-graphs/methods.html) on 270m & 1b, and weakly causal [crosscoders](https://transformer-circuits.pub/2024/crosscoders/index.html) trained on the concatenation of 4 layers (the same 4 depths mentioned above) for every base model size & type.

All models are JumpReLU, trained using a quadratic L0 penalty along with an additional frequency penalty which prevented the formation of high-frequency features. We also used a version of [Matryoshka loss](https://www.alignmentforum.org/posts/rKM9b6B2LqwSB5ToN/learning-multi-level-features-with-matryoshka-saes) during training, which has been documented to help reduce the instance of [feature absorption](https://arxiv.org/abs/2409.14507).

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/9d2e58c147cd395ce1c6a784a449e0c9add8550653dd1afc.jpeg)

Table of available models, taken from the technical report.

Which ones should you use?
==========================

If you're interested in finding features connected to certain behavioural traits (to perform steering, or to better attribute certain model behaviours, or analyze directions you've found inside the model using supervised methods etc), we recommend using the residual stream models trained on a subset of the model layers (e.g. [here](https://huggingface.co/google/gemma-scope-2-27b-it/tree/main/resid_post)). The 262k-width models with medium L0 values (in the 30-60 range) should prove suitable for most people, although the 16k and 65k widths may also prove useful. All the examples in the screenshots above were from 262k-width medium-L0 SAEs finetuned on Gemma V3 270m IT.

If you're interested in doing circuit-style analysis e.g. with attribution graphs, we recommend using the suite of transcoders we've trained on all layers of the model, e.g. [here](https://huggingface.co/google/gemma-scope-2-27b-it/tree/main/transcoder_all). Affine skip connections were strictly beneficial so we recommend using these. Models with larger width lead to richer analysis, but the computational cost of circuit-style work can grow very large especially for bigger base models, so you may wish to use 16k width rather than 262k. Neuronpedia will shortly be hosting an interactive page which allows you to generate and explore your own attribution graphs using these transcoders.

Some useful links
=================

Here's all the relevant links to go along with this release:

*   [GDM blog post](https://deepmind.google/blog/gemma-scope-2-helping-the-ai-safety-community-deepen-understanding-of-complex-language-model-behavior/)
*   [Technical Report](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/gemma-scope-2-helping-the-ai-safety-community-deepen-understanding-of-complex-language-model-behavior/Gemma_Scope_2_Technical_Paper.pdf)
*   [Tweet thread](https://x.com/calsmcdougall/status/2003217825704607853)
*   [Neuronpedia demo](https://www.neuronpedia.org/gemma-scope-2) (inference and attribution graphs coming soon!)
*   [HuggingFace repo](https://huggingface.co/google/gemma-scope-2), to access all model weights
*   [Colab notebook demo / tutorial](https://colab.research.google.com/drive/1NhWjg7n0nhfW--CjtsOdw5A5J_-Bzn4r)

[^0lj3xlmegw4]: The ARENA material will also be updated to use this new suite of models, in place of the models from the 2024 Gemma Scope release.