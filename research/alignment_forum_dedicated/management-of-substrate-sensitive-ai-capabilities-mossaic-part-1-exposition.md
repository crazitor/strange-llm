---
title: "Management of Substrate-Sensitive AI Capabilities (MoSSAIC) Part 1: Exposition"
author: "mfatt"
date: "2025-12-03"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/xxWhKyMNQjb4rwEvu/management-of-substrate-sensitive-ai-capabilities-mossaic-1"
score: 15
votes: 8
---

Mechanistic Interpretability
============================

*Many of you will be familiar with the following section. Please skip through to the next.*

The field of mechanistic interpretability (MI) is not a single, monolithic research program but rather [a rapidly evolving collection of methods, tools, and research programs](https://arxiv.org/abs/2408.01416). These are united by the shared ambition of reverse-engineering neural network (NN) computations and, though lacking a comprehensive uniform methodology, [typically apply tools of causal analysis to understand a model from the bottom up](https://arxiv.org/abs/2501.16496).

MI research centres around a set of postulates. One central postulate is that NN representations can in principle be decomposed into interpretable "features"—fundamental units that "[cannot be further disentangled into smaller, distinct factors](https://arxiv.org/abs/2404.14082)"—and that these are [often encoded linearly as directions in activation space](https://arxiv.org/abs/2310.01405). Further work has shown that NNs in fact combine multiple features into the same neuron—a phenomenon called [superposition](https://arxiv.org/abs/2209.10652).

Some examples of mechanistic techniques include the following:

*   [**Linear Probes**](https://arxiv.org/abs/2310.06824): Simple models (usually linear classifiers) are trained to predict a specific property (e.g., the part-of-speech of a word) from a model's internal activations. The success or failure of a probe at a given layer is used to infer whether that information is explicitly represented there.
*   [**Logit**](https://arxiv.org/abs/2404.14082) [**Lens**](https://arxiv.org/abs/2303.08112): This technique applies the final decoding layer of the model to intermediate activations, to observe how its prediction evolves layer-by-layer.
*   [**Sparse Autoencoders**](https://arxiv.org/abs/2309.08600): These attempt to disentangle a NN's features by expressing them in a higher-dimensional space under a sparsity penalty, effectively expanding the computation into linear combinations of sparsely activating features.
*   [**Activation patching**](https://arxiv.org/abs/2301.04709): This technique attempts to isolate circuits of the network responsible for specific behaviours, by replacing a circuit active for a specific output with another, to test the counterfactual hypothesis.

The Causal-Mechanistic Paradigm
===============================

More recently, MI has been developing from a pre-paradigmatic assortment of techniques into something more substantial. It has been the subject of [a comprehensive review paper](https://arxiv.org/abs/2404.14082), has been given a [theoretical grounding via causal abstractions](https://arxiv.org/abs/2301.04709), and has more recently been given [a philosophical treatment](https://arxiv.org/abs/2505.00808) via the philosophy of explanations .

In particular, this philosophical treatment characterizes MI as the search for explanations that satisfy the following conditions:

1.  **Causal–Mechanistic** \- providing step-by-step causal chains of how the computation is realized. This contrasts with attribution methods like saliency maps, which are primarily correlational. A saliency map might show that pixels corresponding to a cat's whiskers are "important" for a classification, but it doesn't explain the mechanism of how the model processes that whisker information through subsequent layers to arrive at its decision.
2.  [**Ontic**](https://plato.stanford.edu/entries/scientific-realism/) \- MI researchers believe they are discovering "real" structures within the model. This differs from a purely epistemic approach, which might produce a useful analogy or simplified story that helps human understanding but doesn't claim to uncover what is happening in reality. The search for "features" as fundamental units in activation space is a [standard ontic commitment of the field](https://arxiv.org/abs/2404.14082).
3.  **Falsifiable** \- MI explanations are framed as testable hypotheses that can be empirically refuted. The claim that "this specific set of neurons and attention heads forms a circuit for detecting syntax" is falsifiable. One can perform a causal intervention—such as activation patching or ablating the circuit—and observe if the model's syntactic capabilities break in a predictable way. This contrasts with unfalsifiable, post-hoc stories that cannot be rigorously tested.
4.  **Model-level** \- The focus of MI is on the neural network itself—its weights, activations, and architecture. This is distinct from system-level analysis, which might examine the behaviour of an entire deployed product (e.g., a chatbot integrated with search tools and a chain-of-thought prompting wrapper). A system-level explanation might attribute a behavior to the prompt, whereas a model-level explanation seeks the mechanism within the neural network's computational graph.

Leaving aside questions regarding the aptness of this philosophical characterization, we focus here on the causal–mechanistic nature of the explanations that mechanistic interpretability produces. 

We define the causal-mechanistic paradigm as the belief that **we can decompose AI systems into smaller causal components by analysing their computational structure,** and from these components **reconstruct precise explanations of AI system behaviour.**

From [Bereska & Gavves (2024)](https://arxiv.org/abs/2404.14082) \[Emphasis ours\]: 

> *"The theory of causality (Pearl, 2009) provides a mathematically precise language for mechanistic interpretability, forming the foundation for understanding high-level semantics in neural representations (Geiger et al., 2023a). Treating neural networks as causal models involves **considering the compute graph as the causal graph**, allowing for precise interventions and examining individual parameters' roles (McGrath et al., 2023)." *

A direct relationship is drawn between the inner structure of an AI system (i.e., the compute graph) and the methods (i.e., interventions upon the corresponding causal graph) that we use to predict the relevant behaviors. That is, we can understand the relevant outcomes of an AI system if and only if we understand its inner structure.

Multiple realizability
======================

Two recent works indicate a fundamental problem in how we interpret NNs.

[Bailey et al. (2024)](https://arxiv.org/abs/2412.09565) tested a variety of latent space monitoring approaches designed to prevent networks from outputting harmful content. These included sparse autoencoders, linear and MLP probes, and out-of-distribution detectors. All use the internal activations of the model to identify where harmful output is generated. All embody the broader assumption that understanding internal structure allows for behavioural prediction and control.

They developed obfuscation attacks—joint optimization procedures that simultaneously preserve harmful behavioural outputs while making the model's internal activations appear benign to latent-space monitors. These attacks used both adversarial suffixes (optimized text appended to prompts) and embedding-space perturbations. These attacks systematically evaded all tested latent-space monitoring techniques—achieving near-zero recall rates on harmfulness detection while maintaining high jailbreaking efficacy (>90%).

Even more worryingly, they demonstrated just how robustly a NN can obfuscate its activations. They conducted red-team/blue-team games as follows: in each round, the attacker would first train a new embedding suffix designed to both jailbreak the model and fool the current monitor, then the defender would retrain their monitor against the obfuscated activations from this attack plus all previous attacks. The model was able to successfully obfuscate its activations more than 70 times.

Whilst these results have arisen in a training environment explicitly designed to induce obfuscation, the main conceptual takeaway—and the hypothesis put forward by the authors—is this:

> *"Models can represent concepts and execute behaviors using a broad set of different activations. That is, neural representations are highly malleable: we can reshape activation patterns in a variety of ways, while preserving a network's behavior."*

Other researchers have identified a similar problem.

[McGrath et al. (2023)](https://arxiv.org/abs/2307.15771) showed how networks can perform self-repair under layer ablation. They performed ablation experiments on Chinchilla 7B, measuring the model's performance on a factual recall task by comparing the results of two approaches:

1.  Unembedding (direct effect): This is a typical MI approach, similar to logit lens, it consists of taking the output of the layer and running it through the final unembedding layer in the model's architecture, to track the correlation between each layer's computations and the model's output.
2.  Ablation-based (total effect): Here, they effectively "disabled" layers by replacing their activations with those registered in the same layer but under different prompts. They then measured the change in the model output.

They found that these measures disagreed. That is, some layers had a large direct effect on the overall prediction, but when they were removed only a small change in the total effect was recorded.

They subsequently identified two separate effects:

1.  Self-repair/Hydra effect: Some downstream attention layers were found to compensate when an upstream one was ablated. These later layers exhibited an increased unembedding effect compared to the non-ablated run.
2.  Erasure: Some MLP layers were found to have a negative contribution in the clean run, suppressing certain outputs. When upstream layers were ablated, these MLP layers reduced their suppression, in effect partially restoring the clean-run output.

Compensation was found to typically restore ~70% of the original output. The model was also trained without any form of dropout, which would typically incentivise the model to build alternate computational pathways. These pathways seem to occur naturally, and we offer that these results demonstrate how networks enjoy—in addition to flexibility over their representations—considerable flexibility over the computational pathways they use when processing information.

This presents an obstacle to the causal analysis of neural networks, in which interventions are used to test counterfactual hypotheses and establish genuine causal dependencies.

Summary
=======

Rather than "harmfulness" consisting of a single direction in latent space—or even a discrete set of identifiable circuits—Bailey et al.'s evidence suggests it can be represented through numerous distinct activation patterns, many of which can be found within the distribution of benign representations. Similarly, rather than network behaviors being causally attributable to specific layers, McGrath et al.'s experiments show that such behaviors can be realized in a variety of ways, allowing networks to evade intervention efforts.

Following [similar phenomena in the philosophy of mind and science](https://plato.stanford.edu/entries/multiple-realizability/), we might call this the multiple realizability of neural computations.

Such multiple realizability is deeply concerning. We submit that these results should be viewed not simply as technical challenges to be overcome through better monitoring techniques, but as indicating broader limits to the causal-mechanistic paradigm's utility in safety work. We further believe that these cases form part of a developing threat model: substrate-flexible risk, as described in the following post. As NNs become ever more capable and their latent spaces inevitably become larger, we anticipate substrate-flexible risks to become increasingly significant for the AI safety landscape.