---
title: "Circuit discovery through chain of thought using policy gradients"
author: "Adrià Garriga-alonso"
date: "2025-11-29"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/N4P9LSa6B2KyQtG5d/circuit-discovery-through-chain-of-thought-using-policy"
score: 15
votes: 6
---

Circuit discovery has been restricted to the single-forward-pass setting, because the algorithms to attribute changes in behavior to particular neurons / SAE features need gradients, and you can't take a gradient through the sampled chain of thought. Or... can you?

It turns out taking gradients through random discrete actions is an essential part of reinforcement learning. We can estimate the gradients of an expectation over CoTs, with respect to the features, using the *score function estimator*. We can combine this with integrated gradients to produce a version of [EAP-IG](https://github.com/hannamw/EAP-IG) which works through the averages of chains of thought.

Background
==========

Circuit discovery
-----------------

The task we attempt to do is circuit discovery, defined by [Conmy et al.](https://proceedings.neurips.cc/paper_files/paper/2023/hash/34e1dbe95d34d7ebaf99b9bcaeb5b2be-Abstract-Conference.html) Formally, for each subgraph $H$ of a computational DAG $G$ which represents a neural network, we want to find which subgraph $H$ is responsible for a behavior. We do this by defining a 'task loss', which compares the performance of the subgraph to the performance of the whole network. Let that loss be $D$ and then $x,x'$ be the clean and corrupted datapoints. The loss for a single pair of data points is:

$\mathcal{L}(x_i, x_i') = D(G(x_i), H(x_i, x_i'))$.

the overall loss of a circuit $H$ is simply the average of $$this loss over all datapoints and corrupted datapoints $x_i,x_i'$.

Partial edge inclusion: introducing z
-------------------------------------

To connect this to integrated gradients, we introduce variables $z$, which control whether an edge is included in $H$ or not. The scalar $z_j$ controls whether the $j$th edge (or node) is included in $H$ or not. That is, the value $v_j$ of the $j$th edge is replaced by: 

$v_j(x_i)\text{ under the subgraph } H_z := z_jv_j(x_i) + (1-z_j)v_j(x_i')$

If we set $z_j=0$ the edge is not included, i.e., it has the value it would get under the corrupted input.  If we set $z_j=1$, then the edge has the value it gets from running the comptuational graph $G$ forward.

Integrated Gradients for attribution
------------------------------------

Our first ingredient can be any gradient-based method for circuit discovery. I've chosen to focus on [EAP with Integrated Gradients](https://arxiv.org/abs/2403.17806) because it's still the circuit discovery algorithm with the best balance of simplicity and performance. You could make a CoT version of Attribution Patching as well.

To attribute behavioral loss to some configuration of edges (concrete value of $z$), we compute the gradient of the task loss with respect to $z$, which determines whether we include an edge or not: $$$\nabla_z\mathcal{L}(x_i, x_i'; H_z)$. In EAP-IG, we *average this for* z between 0 and 1, for all edges of the graph $G$ simultaneously. If we interpolate at $N$ points in between 0 and 1, the attribution for a single data point is:

$\text{Attrib}(x_i, x_i') = \sum_{n=0}^N \nabla_z \mathcal{L}(z; x_i, x_i')\Big|_{z = \frac{n}{N}}$

for loss defined using the task loss, the full graph and the graph corrupted by z: $\mathcal{L}(z; x_i, x_i') = D(G(x_i), H_z(x_i, x_i'))$. Notice that we average over $z = \frac{n}{N}$, so we take $$$z=1$, $z=0$, and $N-1$ intermediate points.

Policy gradients
----------------

Now for the second ingredient: policy gradients. Suppose I have a policy and some loss function $F(a_1, a_2, \dots, a_T)$, which depends on trajectories of actions $a_1,a_2,\dots,a_T$ from the policy. The policy $\pi_\theta$ is parameterized by some parameters $\theta$. The expected loss over trajectories is:

$$$\mathcal{L}(\theta) = \mathbb{E}_{a_{1:T} \sim \pi_\theta}\left[ F(a_{1:T})\right]$

We'd like to take gradients $\nabla_\theta \mathcal{L}(\theta)$. These are tricky because the loss $F(\cdot)$ does not depend on $\theta$ directly. Instead, it depends on $\theta$ through the $$*distribution over actions in the trajectory,* which determines the expectation of $F(a_{1:T})$.

The policy gradient theorem tells us that the gradient is the expected *gradient of the log-probability of actions, weighed by how big *$F(a_{1:T})$ *is: *

$\nabla_\theta \mathcal{L}(\theta)=  \nabla_\theta \mathbb{E}_{a_{1:T} \sim \pi_\theta}\left[ F(a_{1:T})\right] = \mathbb{E}_{a_{1:T} \sim \pi_\theta}\left[ F(a_{1:T}) \sum_{t=1}^T \nabla_\theta \log \pi(a_t | a_{1:t-1}) \right] .$

Let's take this formula as given. I explain it in [these](https://agarriga.substack.com/p/policy-gradients-part-1) two [posts](https://agarriga.substack.com/p/policy-gradients-part-2-using-probability), but one the keys to it is that we can swap integral and differential signs, and that $\nabla_\theta \pi_\theta = \pi_\theta \nabla_\theta \log \pi_\theta$ by the chain rule.

What do policy gradients give us?
---------------------------------

It's worth expanding on what policy gradients are for, and why they're useful. Policy gradients give us the gradient of how the *average outcome* over many trajectories varies, when we vary the parameters $\theta$. It's not for a particular rollout, it's for the whole distribution. As such, any gradients that we take *include the effect of the CoT* on the output.

The function $F$ can be a function of *any number of steps* in the trajectory. It can be just of the final step (if we're looking at e.g. full CoTs and a single token answer). It can be of many steps at the end (if we're considering a CoT + whether an answer matches the truth, as rated by some other model). It can be basically anything. That's why it's the workhorse of modern LLM RL: PPO, GRPO, etc. are all based on policy gradients.

The proposed method: integrated gradient policy gradient
========================================================

So if we want to attribute behavior sampled through CoTs to parts of the network, we can just use both of these simultaneously.

We define a task loss $D$ that depends on the tokens until now, the output of the original model and the output of the new model. The behavior that we want to study (and find sub-circuits for) is thus the expectation when *sampling from the corrupted subgraph:*

$\mathcal{L}(z) = \mathbb{E}_{x_{1:T} \sim H_z}\left[ D(a_{1:T}, G(x_{1:T}), H(z; x_{1:T}, x_{1:T}' ) \right]$

We sample from $H_z$ autoregressively: we start with $x_1$ and corrupt it to find $x_1'$, that lets us compute $H_z(x_1, x_1')$ and sample $x_2$ from it; then we corrupt $x_2$ to get $x_2'$, $$*etc.* I've abbreviated this in the expression above as $x_{1:T} \sim H_z$.

Now we see how we can use both elements.

**Integrated gradients:** to attribute the behavior through the CoT to components $$*z* of the model, we simply need to take $\nabla_z \mathcal{L}(z)$ interpolated at various points for $z$ between 0 and 1. That is, we want:

$\text{Attrib} = \sum_{n=0}^N \nabla_z \mathcal{L}(z)\Big|_{z = \frac{n}{N}}$

We've removed the dependence of Attrib on the data points $(x_i, x_i')$ because we're sampling things from the model, presumably with some context. But we could average over some contexts, why not. 

**Policy gradients:** The gradient$$ $\nabla_z \mathcal{L}(z)$ is with respect to a probability distribution. To compute it, we need to use the policy gradient theorem:

$\nabla_z \mathcal{L}(z) = \mathbb{E}_{x_{1:T} \sim H_z}\left[ D\left(a_{1:T}, G(x_{1:T}), H(z; x_{1:T}, x_{1:T}' )  \right)\cdot \sum_{t=1}^T \nabla_z \log H_z(x_t \,|\, x_{1:t-1}) \right]$

To estimate this expectation, we sample a bunch of CoTs from $H_z$ and average their values of $D(x_{1:T}) \cdot \sum_t \nabla_z \log H_z(x_t | \dots)$.

We can just plug this in into the previous equation, and there we have it: **attribution to circuit components over chains of thought.**

Discussion
==========

This method is very flexible, because it's just the old EAP-IG, except now we can also compute gradients over probability distributions. $$The $z$ can be assigned to neurons, attention heads, SAE components, anything.

They don't even have to be *constant across time.* We can have separate components for the gradients at a particular time-step to study the effect of a component at that time step. The same is possible if the 'time step' moves depending on where a token falls, but I think you're missing some of the effect in that case.

I haven't implemented this. It's tricky with open-source packages because you can't just interpolate between the original and corrupted inputs in vLLM, and Huggingface only has quadratic sampling. To make it really efficient, it's also nice to be able to compute the gradients w.r.t $z$ at every step using the same version of KV-cache attention that you computed.

I might fill this gap with open-source tooling myself, especially if I can get funding for a month to do it.