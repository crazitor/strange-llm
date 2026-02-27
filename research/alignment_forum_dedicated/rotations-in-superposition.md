---
title: "Rotations in Superposition"
author: "Linda Linsefors"
date: "2025-12-15"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/LZ7YMPJueB6qjL24n/rotations-in-superposition"
score: 54
votes: 15
---

**TL;DR** We experimentally test the [mathematical framework for circuits in superposition](https://www.lesswrong.com/posts/FWkZYQceEzL84tNej/circuits-in-superposition-2-now-with-less-wrong-math) by hand-coding the weights of an MLP to implement many conditional[^x4unv1coet] rotations in superposition on two-dimensional input features. [The code can be found here](https://github.com/LindaLinsefors/Rot-in-Sup).

*This work was supported by Coefficient Giving and Goodfire AI*

1 Introduction
==============

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/35d5f47a32de477f026677889a7b91e3ed9209d2008b32b9.png)

Figure 1: The desired values for rotating vectors $\mathbf{x}$(green), compared to their estimated values extracted from the neural network, $\hat{\mathbf{x}}$ (purple) for five of the conditional rotation circuits. The six dots represent the values of the vector $\mathbf{x}$ in layers $0$ to $5$.

In [a previous post](https://www.lesswrong.com/posts/FWkZYQceEzL84tNej/circuits-in-superposition-2-now-with-less-wrong-math), we sketched out a construction for compressing many different circuits into a neural network such that they can be computed in superposition.[^bhyqx6un2i]

By computation in superposition, we mean that a network represents features in superposition and can perform more possible computations with them than it has neurons (although not all at once), across multiple layers. Having better models of this is important for understanding whether and how networks use superposition, which in turn is important for mechanistic interpretability research more generally.

Performing computation in superposition over multiple layers introduces additional noise compared to just storing features in superposition. This restricts the amount and type of computation that can be implemented in a network of a given size, because the noise needs to be reduced or suppressed to stay smaller than the signal.

Here, we test the construction by using it to compress circuits that perform random rotations on different two-dimensional input vectors, conditional on a Boolean variable being active.

We ended up needing to adjust the construction a bit to do this, because one of the assumptions the original version made about the circuits to be compressed turned out to be less reasonable in practice than we thought it'd be, and did not actually apply to these rotation circuits.[^bdxi6843nbk]

This sort of thing is why we do testing. [Reality is complicated](http://johnsalvatier.org/blog/2017/reality-has-a-surprising-amount-of-detail).

Note that this is certainly not the ideal way to implement rotations in superposition. We are testing a general method that should work for a wide class of circuits. If we just wanted to implement these specific circuits as compactly and noiselessly as possible, there'd be better ways to do that.[^p58wbwbxfra]

2 Takeaways 
============

It seems to work. But we can only fit so many independent circuits into the network before the errors compound and explode.

**Independent circuits in superposition are costly **  
Many people we've talked to seem to think that neural networks can easily learn to implement an exponentially large number of independent computations by using superposition. They often seem to base this intuition on toy models that showcase how many independent features neural networks can [*store* in superposition](https://www.anthropic.com/research/toy-models-of-superposition) in their activations, but that's very different from implementing independent *computations* in superposition on these features. The latter is much more difficult and costly.

Our [previous post](https://www.lesswrong.com/posts/FWkZYQceEzL84tNej/circuits-in-superposition-2-now-with-less-wrong-math) concluded that in theory, we could fit close to $T=\widetilde{\mathcal{O}}\left(\frac{D^2}{d^2}\right)$ circuits that each require $d$ ReLU neurons per layer into a neural network with $D$ ReLU neurons per layer, provided the circuits activate sparsely enough.[^4to0pbubaf6] But that was an asymptotic expression for the case of network width $D$ going to infinity, based only on the leading error terms and mostly ignoring constant prefactors.

In our experiments, we had $d=4$, $D=1000$ and it was already pretty hard to fit in $T\approx2\frac{D}{d}$ circuits and have the noise stay small enough to not blow up the computation in the first few layers. We think we could perhaps stabilize the computations for a much greater number of layers by implementing more active error correction,[^hrwozkshot] but squeezing in many more independent circuits than this seems very difficult to us.

**So how can language models memorize so many things?**   
If fitting many independent circuits into a neural network is so difficult, how can language models memorize so many different facts and even [whole text passages](https://arxiv.org/html/2505.24832v1)? We don't know the answer to that yet. But we have started to train and analyze small toy models of memorization to find out, and we have some suspicions. Our work on this is still at a very early stage, so take the following speculation with an even bigger helping of salt than usual. But:

Many memorization circuits might be much shallower than the ones we investigate here. A shallower depth means fewer stages of computation for errors to accumulate.

Much of the information that models memorize is not actually independent. If a model wants to store that "The Eiffel Tower is in Paris" and that "The capital of France is Paris", it doesn't actually need two independent, non-overlapping lookup circuits to do this. Since both look-ups return the same answer, "Paris", the computation need not distinguish their outputs. Instead, all look-ups that return "Paris" could effectively share the same set of neurons, meaning they'd effectively not be independent look-ups at all, but rather parts of a single general "Sequences that end in Paris" lookup.

This picture of computation in neural networks suggests that there might not be *that* many more independent circuits than neurons in a large language model like GPT-2. Instead, the models might be exploiting structure in the data to implement what might superficially look like very many different capabilities using a comparatively much smaller set of fairly general circuits.

**Lucius**: This roughly tracks with some very early results I've been seeing when [decomposing the parameters of models like GPT-2 Small into independent components](https://www.lesswrong.com/posts/yjrpmCmqurDmbMztW/paper-stochastic-parameter-decomposition). It currently looks to me like it's actually rare for these models to even have more rank $1$ circuit pieces than neurons in a layer, never mind neuron count squared. I'd guess that much wider models have more circuits relative to their neuron count, but at this point I kind of doubt that any real model today gets even remotely close to the theoretical limit of $\approx 1$ circuit per weight. Which might be great, because it'd mean there aren't that many circuits we need to interpret to understand the models.

3 The task
==========

The general setup for our circuits-in-superposition framework goes like this: 

*   We have $T$ small circuits, each of which can be described as a $d$-dimensional multilayer perceptron (MLP) with $L$ layers. 
*   We have one large network, a $D$-dimensional MLP with $L$ layers, where $D>d$, but $D<Td$. 
*   We want to embed all $T$ circuits into the large network, such that the network approximately implements the computations of every circuit, conditional on no more than $z\ll T$ circuits being used on any given forward pass. Since $D<Td$, we can't do this by just dedicating one network neuron to each circuit neuron. 

In this case, the $T$ small circuits we want to compress into one network each perform a particular two-dimensional rotation on different two-dimensional vectors $\mathbf{x}_t^l$, conditional on a Boolean "On-indicator" variable $\alpha^l_t$ taking the value $1$. The circuits have $L=6$ layers, with each layer performing another conditional rotation on the previous layer's output. We randomly selected the rotation angle for each circuit. The hidden dimension of each individual circuit is $d=4$. 

**Conditional rotation **  
In each layer $l$, the circuits are supposed to rotate a two-dimensional vector $\mathbf{x}_t^{l-1}$ with norm $|\mathbf{x}^{l-1}_t|\leq 1$ by some angle $\theta_t$, conditional on the Boolean On-indicator $\alpha^{l-1}_t$ taking value $1$ rather than $0$.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/f82be71f07d9f2aa6940661a4b973e48652b5d8bd863ad1a.png)

Figure 2: Two-dimensional rotating vectors $\mathbf{x}$ for five of the conditional rotation circuits. The six dots correspond to layers $0$ to $5$.

We can implement this with an expression using ReLUs, like this: 

$$
\begin{equation}    \begin{bmatrix}        (\mathbf{x}^l_t)_0\        (\mathbf{x}^l_t)_1    \end{bmatrix}    = \begin{bmatrix}        \text{ReLU}\left(\cos\theta_t (\mathbf{x}^{l-1}_t)_0-\sin\theta_t (\mathbf{x}^{l-1}_t)_1+2\alpha^{l-1}_t-1\right)-\alpha^{l-1}_t\       \text{ReLU}\left(\sin\theta_t (\mathbf{x}^{l-1}_t)_0+ \cos\theta_t(\mathbf{x}^{l-1}_t)_1+2\alpha^{l-1}_t-1\right)-\alpha^{l-1}_t    \end{bmatrix}\,. \tag{3.1} \end{equation}
$$

 If $\alpha^{l-1}_t=1$, this expression simplifies to 

$$
\begin{equation}    \begin{bmatrix}        (\mathbf{x}^l_t)_0\        (\mathbf{x}^l_t)_1    \end{bmatrix}    = \begin{bmatrix}        \cos\theta_t (\mathbf{x}^{l-1}_t)_0-\sin\theta_t (\mathbf{x}^{l-1}_t)_1\        \sin\theta_t (\mathbf{x}^{l-1}_t)_0+ \cos\theta_t(\mathbf{x}^{l-1}_t)_1    \end{bmatrix}\,, \tag{3.2}\end{equation}
$$

 which is a two-dimensional rotation by angle $\theta_t$, as desired. If $\alpha^{l-1}_t=0$, we get $\mathbf{x}_t^{l}=0$.

**On-indicator**  
At each layer $l$, the circuits are also supposed to apply a step function to the On-indicator $\alpha^{l}_t$, and pass it on to the next layer: 

$$
\begin{equation}    \alpha^l_t = \text{ReLU}(2\alpha^{l-1}_t - 1.5) - \text{ReLU}(2\alpha^{l-1}_t - 0.5)\,.\tag{3.3} \end{equation}
$$

The step function is there to make the On-indicators robust to small noise. Noise robustness is a requirement for circuits to be embedded in superposition. For more details on this and other properties that circuits need to have for computation in superposition to work, see Section 5.2

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/333142cae87b1f82e350d9578e52929f952615476508ca9c.png)

Figure 3: A step function formed from two ReLUs

If the circuit is active, the On-indicator will be initialized as 1, and remain 1. If the circuit is inactive, the On-indicator will be initialized as 0, and stay 0. 

$$
\begin{equation}    \alpha_t^l = \begin{cases}        1 &\text{if circuit $t$ is active}\        0 &\text{if circuit $t$ is inactive}   \end{cases}    \quad \text{for all $l$} \tag{3.4}\end{equation}
$$

For more detail on the small circuits, see Appendix section 5.1

+++ Why conditional rotations in particular?

No particular reason. We just wanted some simple circuits. Originally, we tried to just do plain two-dimensional rotations. Then we remembered that plain rotations aren't noise-robust in the way our computation-in-superposition framework requires, because they're analytic at every point. We need circuits that return an output of $0$ when passed an input vector of sufficiently small size $\epsilon$. Rotations don't do that. Making the rotations conditional on some Boolean logic fixes this, and for simplicity we just went with the easiest Boolean logic possible.




++++++ Why the step function?

Although we only need one float to encode $\alpha$, we need two ReLUs to make the circuit robust to noise over multiple layers. If we only used a single ReLU, e.g., $\alpha^l_t = \text{ReLU}(2\alpha^{l-1}_t - 1)$, then a small error $\epsilon$ on $\alpha^{l-1}_t$ would be doubled in layer $l$, then doubled again in layer $l+1$ and so on, growing exponentially with circuit depth.

If dedicating two neurons just to copy over the embedding of a single Boolean seems a little silly to you, you're not wrong. If our main goal was just to implement lots of conditional rotation circuits in superposition using as few neurons as possible, there'd be better ways to do it. For example, we could use some fraction of the neurons in the large network to embed the On-indicators, and then just copy this information from layer to layer without ever recalculating these values. Such an implementation would do better at this particular task. 

But our goal is not to solve this task in particular, but to test a general method for embedding many different kinds of circuits.

If you like, you can also see this part of the circuits as a stand-in for some more complicated logic, that calculates which circuits are on from layer to layer, i.e., some function that is more complicated than "same as last layer", and involves cross-circuit computations




+++

4 Results 
==========

Here, we'll present the results of embedding $T$ conditional rotation circuits into a ReLU MLP of width $D$ for various choices of $D$ and $T$, using the embedding method described in Section 5.4

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/a3b8222ff27d1f9799ee3f9ba4095e9143a3cb1b6cc4bef6.png)

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/d25306521d2370c7f68767246a9550ed0b5d3ed864f2b66b.png)

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/aa6be270d81d2416fe7ace8dc67f75c9636322e30fac50ec.png)

Figure 4: The true values for the rotating vector, $\mathbf{x}$ (green), compared to its estimated values extracted from the neural network, $\hat{\mathbf{x}}$ (purple, red and yellow) for a randomly selected subset of the $T=557$ conditional rotation circuits the network implements. Each circuit has width $d=4$. The network they are embedded into has a width of $D=1000$ neurons per layer. The data comes from randomly sampled active circuits, from runs with 1, 2 or 3 simultaneously active circuits, i.e., $z=1,2,3$.

As we would expect, the read-offs diverge more with every subsequent layer as error accumulates, since we didn't implement any active error correction.[^hrwozkshot] Most rotation circuits seem to work fine for the first $2$-$3$ rotations, with the read-offs predicting the ideal values much better than chance. Estimates are much worse in the later layers. The errors also get larger when the number of active circuits $z$ is increased.

We quantify the error on the rotated vectors as  the $L_2$ norm of the difference between the ideal result $\mathbf{x}_t^l$ and the estimate $\hat{\mathbf{x}}^l_t$:

$$
\begin{equation}    |\delta \mathbf{x}_t^l| := |\mathbf{x}_t^l - \hat{\mathbf{x}}^l_t|\,.\tag{4.1} \end{equation}
$$

On a population level, we can look at both the *average* error of circuits $\frac{1}{T}\sum^T_{t=1}|\delta \mathbf{x}_t^l|^2$, and the worst-case error $\text{max}(|\delta \mathbf{x}_1^l|,\dots,|\delta \mathbf{x}_T^l|)$. The former tells us how noisy the computations are most of the time. The latter tells us whether any one circuit in the ensemble of $T=557$ circuits was implemented so noisily that for at least one input it basically doesn't work at all.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/254b53533f7c512df7a8915c66f997d050957c5b91f5c04e.png)

Figure 5:  Errors on the rotating vectors $\mathbf{x}$, for an MLP of width $D=1000$ with $T=557$ circuits each of width $d=4$. Every circuit neuron is spread across $S=6$ MLP neurons. Upper row: mean squared errors, i.e., the average of $|\delta\mathbf{x}|^2$ over inactive or active circuits. Lower row: worst-case absolute errors, i.e., the maximum of $|\delta\mathbf{x}|$ over inactive or active circuits.[^g9jhpe1t4qt]

The left plots show errors on inactive circuits, i.e., circuits that received an input of $\alpha^0_t=0, \mathbf{x}^0_t=0$. Most circuits will be inactive on any given forward pass. The right plots show errors on active circuits, i.e. circuits that received an input of $\alpha^0_t=1$ and some random vector $\mathbf{x}^0_t$ with $|\mathbf{x}^0_t|=1$. As a baseline to put these numbers in perspective, once $|\delta \mathbf{x}_t^l|\geq1$, the circuits are doing no better than guessing the mean. So, the average circuit beats this trivial baseline for the first three of the five rotations, or the first four if we restrict ourselves to inputs with only $z=1$ active circuits. As one might expect, the worst-case errors are worse. With $z=1$ inputs, all $T=557$[^d37bdcdzygn] circuits beat the baseline for the first two rotations. With $z=2$ inputs, only the first rotation is implemented with small enough noise by all circuits to beat the baseline, and at least one circuit doesn't work right for an input with $z=3$ for even a single rotation.

We can also see that the mean squared errors grow superlinearly the deeper we go into the network. This does not match our error calculations, which would predict that those errors should grow linearly. We think this is because as the errors grow they start to overwhelm the error suppression mechanism by activating additional ReLUs, and thus letting through additional noise. The calculations assume that the noise always stays small enough that this doesn't happen. More on that in the next subsection, where we compare our error calculations to the empirical results.

We can also look at the error on the On-indicator variables $\alpha_t$: 

$$
\begin{equation}    |\delta\alpha^l_t| := |\alpha^l_t - \hat\alpha^l_t | \tag{4.2}\end{equation}
$$

Here, an error $|\delta\alpha^l_t|>0.25$ means that the error on the On-indicator is large enough to pass through our step function and propagate to the next layer. At that point, errors will start to accumulate over layers at a faster-than-linear rate.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/a7ed6ad907ee62a946f2924859ea446acdd3951ce5eba0a7.png)

Figure 6: Errors on the Boolean On-indicators $\alpha$, for an MLP of width $D=1000$ with $T=557$ circuits each of width $d=4$. Every circuit neuron is spread across $S=6$ MLP neurons. Upper row: mean squared errors, i.e., the average of $(\delta\alpha)^2$ over inactive or active circuits. Lower row: worst-case absolute error, i.e., the maximum of $|\delta\alpha|$ over inactive or active circuits.[^g9jhpe1t4qt]

The absolute value of the error for the On-indicator caps out at $1$. This is because $\hat{\mathbf{a}}_t^l$ is the averaged output of a set of step functions, each of which is constrained to output a value in the range $[0,1]$. Their average is thus also constrained to the range $[0,1]$. Therefore, regardless of whether the true value for $\alpha_t^l$ is $0$ or $1$, $|\delta\alpha_t^l|$ has to be in the range $[0,1]$.

4.1 Comparing with our theoretical predictions
----------------------------------------------

Key takeaway: Most predictions are good when the errors are small in magnitude, but once the errors get too big, they start growing superlinearly, and our predictions begin to systematically undershoot more and more. We think this is because our error propagation calculations assume that the errors stay small enough to never switch on neurons that are not in use by active circuits. But for many settings, the errors get large enough that some of these neurons do switch on, opening more channels for the noise to propagate and compound even further.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/8c2ea791b943ff9dee670d3ce1968f48672324565016c2a5.png)

Figure 7: Fraction of active neurons, i.e., what fraction of the large network neurons are non-zero, for a network of width $D=1000$ with $T=557$ circuits of width $d=4$. Every circuit neuron is spread across $S=6$ MLP neurons. The dotted lines are what we'd theoretically expect if the errors stayed small enough not to overwhelm the noise suppression threshold for the inactive circuits. If this assumption is broken, the network starts to develop a "seizure"[^03xao9s7xfnx]: the noise starts to grow much faster as errors switch on more neurons causing more errors which switch on more neurons.[^g9jhpe1t4qt]

The key variables that influence the error here are

*   Number of circuit parameters per layer divided by number of network parameters per layer $\frac{Td^2}{D^2}$. Generally speaking, the bigger this ratio is, the larger the error will be.
*   Number of active circuits per forward pass $z$.
*   Number of circuit layers computed $L$.

### 4.1.1 Rotating vector 

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/23c10ffd4b7c5e81397d13444065bb23b30aad94ab3203ab.png)

Figure 8: Empirical result vs. theoretical predictions for the mean squared error on the rotating vector $\mathbf{x}$ for active circuits. Each dot represents a different network, with a different choice of network width $D$ or total number of circuits $T$. Each circuit neuron is spread across $S=6$ network neurons. Colors are based on $D$. Dots are marked as $\bullet$ or $\blacktriangle$ depending on whether total circuit width $T d$ is larger than $D$, making superposition strictly necessary to implement the computation. Note though that even in the cases where $T d<D$, networks are still constructed using our superposition embedding method.

Predictions are good for layer 1, $z=1$. For larger $z$, the errors get larger and the predictions get worse, with empirical errors often systematically larger than our theoretical predictions. For layer $2$ and onward, our theoretical predictions likewise undershoot more and more as the overall error gets larger. At layer $3$ and onward, the superlinear growth from compounding noise becomes very visible for large $\frac{Td^2}{D^2}$.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/bef6497dd13d4f1e62c618ae56358dc0e5ad93f3c1f54249.png)

Figure 9: Same as the previous figure, but here we compare empirical results to theoretical predictions for the mean squared error on the rotating vectors $\mathbf{x}$ of inactive circuits.

As our error calculations would predict, rotating vectors for inactive circuits have smaller errors than rotating vectors for active circuits, so long as the overall noise level stays small enough for the calculations to be applicable.[^k3296xw0peq]

### 4.1.2 On-indicator

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/0531b32749bf5f9524b41ab24a66f59e659ebc98461a6854.png)

Figure 10: Same as the figures in the previous subsection, but here we compare empirical results to theoretical predictions for the mean squared error on the On-indicator $\alpha$ of active circuits.

In the case of On-indicators for active circuits, our error calculations predict that they just stay zero. This is indeed empirically the case for the early layers. But as we move deeper into the network and $\frac{Td^2}{D^2}$ or $z$ get larger, a critical point seems to be reached. Past this point, noise on other parts of the network seems to become large enough to cause cascading failures, likely by switching the regime of ReLUs. Then, the active On-indicators become noisy as well.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/326efeb9aec7ccf905b0d3fd011902af77517e3ba12c3396.png)

Figure 11: Same as the figures in the previous subsection, but here we compare empirical results to theoretical predictions for the mean squared error on the On-indicator $\alpha$ of inactive circuits.

The noise on the inactive On-indicator circuits follows the same pattern: Predictions are mostly good until the noise seems to grow large enough to break the assumptions of the calculation as the network starts to develop a "seizure". Here, this point seems to be reached at particularly early layers though. We think this is because seizures start with the On-indicators for inactive circuits and spread from there to other quantities.

5 Appendix 1: Construction 
===========================

5.1 The circuits 
-----------------

Each individual circuit can be written as 

$$
\begin{equation}    \mathbf{a}^l_t = \text{ReLU}(w^l_t\mathbf{a}^{l-1}_t+\mathbf{b}^{l}) \tag{5.1}\end{equation}
$$

 where the superscript $l$ indicates the layer, ranging from $0$ to $5$, and the subscript $t$ indexes the different circuits, ranging from $0$ to $T-1$.

The circuits are supposed to compute/propagate the *On-indicator*, $\alpha^l_t\in\{0,1\}$ which controls whether the circuit should be active, and perform rotations on the *rotating vector*, $\mathbf{x}_t^l$.

The weight matrices $w_t^l$ for each circuit are parametrized as 

$$
\begin{equation}    w_t^l = \begin{bmatrix}    2 & -2 & 0 & 0 \    2 & -2 & 0 & 0 \    2 - (\cos\theta_t - \sin\theta_t) & -2 + (\cos\theta_t - \sin\theta_t) & \cos\theta_t & -\sin\theta_t \   2 - (\sin\theta_t + \cos\theta_t) & -2 + (\sin\theta_t + \cos\theta_t) & \sin\theta_t & \cos\theta_t    \end{bmatrix} \tag{5.2}\end{equation}
$$

 and the biases as[^zy6n2fdahlj]

$$
\begin{equation}    \mathbf{b}^l = \begin{bmatrix}        -0.5 \ -1.5 \ -1 \ -1    \end{bmatrix}\,.\tag{5.3} \end{equation}
$$

So, the circuit parameters here don't actually vary with the layer index $l$ at all.[^5qsi5ubrntr]

The initial input vector for each circuit takes the form 

$$
\begin{equation}    \mathbf{a}^0_t = \begin{bmatrix}        1.5 \alpha^0_t\        0.5 \alpha^0_t\        (\mathbf{x}^0_t)_0 + \alpha^0_t\        (\mathbf{x}^0_t)_1 + \alpha^0_t\    \end{bmatrix}\,. \tag{5.4}\end{equation}
$$

The On-indicator $\alpha_t^l$ for circuit $t$ at layer $l$ can be read out from the circuit's hidden activations as 

$$
\begin{equation}    \alpha^l_t := (\mathbf{a}_t^l)_1 - (\mathbf{a}_t^l)_2\,.\tag{5.5} \end{equation}
$$

The rotating vector can be read out from the circuit's hidden activations as 

$$
\begin{equation}    \mathbf{x}^l_t := \begin{bmatrix}        (\mathbf{a}^l_t)_2 - \alpha_t^l\        (\mathbf{a}^l_t)_3 - \alpha_t^l    \end{bmatrix}\,.\tag{5.6} \end{equation}
$$

If the circuit is active, the rotating vector will be initialized as some vector of length $1$, and the On-indicator will be set to $1$. If the circuit is inactive, the rotating vector and On-indicator will be initialized to $0$, and stay $0$. 

$$
\begin{equation}    |\mathbf{x}_t^l| = \begin{cases}        1 &\text{if circuit $t$ is active}\        0 &\text{if circuit $t$ is inactive}   \end{cases}    \quad \text{for all $l$} \tag{5.7}\end{equation}
$$

$$
\begin{equation}    \alpha^l_t = \begin{cases}        1 &\text{if circuit $t$ is active}\        0 &\text{if circuit $t$ is inactive}    \end{cases}    \quad \text{for all $l$} \tag{5.8}\end{equation}
$$

A circuit's rotating vector is robust to some noise if the circuit is inactive. If a circuit is active, errors on its rotating vector will neither be removed nor amplified.

In any given forward pass, most circuits will be inactive.

5.2 Assumptions about the circuits 
-----------------------------------

### 5.2.1 Revisiting assumptions from the previous post 

From the [previous post](https://www.lesswrong.com/posts/FWkZYQceEzL84tNej/circuits-in-superposition-2-now-with-less-wrong-math):

> Assumptions
> -----------
> 
> For this construction to work as intended, we need to assume that:
> 
> 1.  Only  $z\ll\frac{D}{d}$ circuits can be active on any given forward pass.
> 2.  Small circuits are robust to noise when inactive. I.e. a small deviation to the activation value of an inactive circuit applied in layer $l$ will not change the activation value of that circuit in layer $l+1$.
> 3.  If a circuit is inactive, all of its neurons have activation value zero. I.e. $a_t^l = 0$  if circuit $t$ is inactive.
> 4.  The entries of the weight matrices $w_t^l$ for different circuits in the same layer are uncorrelated with each other.
> 
> Assumption 1 is just the standard sparsity condition for superposition. 
> 
> Assumption 2 is necessary, but if it is not true for some of the circuits we want to implement, we can *make* it true by modifying them slightly, in a way that doesn't change their functionality. How this works will not be covered in this post though.[^xf5epem8wd8] 
> 
> Assumptions 3 and 4 are not actually necessary for something *similar* to this construction to work, but without them the construction becomes more complicated. The details of this are also beyond the the scope of this post.

Assumption 1 holds for our conditional rotation circuits. Assumption 2 also holds, because the rotation is only applied if the Boolean On-indicator $\alpha^l_t$ is large enough, and the step function for $\alpha^l_t$ also doesn't propagate it to the next layer if $\alpha^l_t$ is too small. Assumption 3 also holds. However, **assumption 4 does not hold**. So we're going to have to adjust the way we embed the circuits a little.

Further, while it wasn't explicitly listed as an assumption, the previous post assumed that the circuits don't have any biases. But our circuits here do (see Equation 5.1). So we'll need to make some more adjustments to account for that difference as well.

### 5.2.2 Updated set of assumptions

1.  Only $z\ll\frac{D}{d}$ circuits can be active on any given forward pass. 
2.  Small circuits are robust to noise when inactive. I.e., a small deviation to the activation value of an inactive circuit applied in layer $l$ will not change the activation value of that circuit in layer $l+1$. 
3.  If a circuit is inactive, all of its neurons have activation value zero. I.e., $\mathbf{a}^l_t=0$ if circuit $t$ is inactive.[^t2ltwbk7bx8]
4.  Every small circuit has the same bias vector in any given layer. 
5.  Active circuits do not amplify incoming noise. I.e., the size of a noise vector applied to a circuit should not grow in relative size over layers. 

Assumptions 1-3 have stayed the same. We think the construction could likely be modified to make assumption 3 unnecessary,[^dc7z6d9bwib] but it simplifies the implementation a lot. The old assumption 4 is not required for the new construction. The new embedding algorithm can work without it (see next section). We think the embedding algorithm could also be modified to make the new assumption 4 unnecessary, but this may come at some cost to the total number of circuits we can embed.[^34g1itvi11v] The new assumption 5 was actually necessary all along, even in the previous construction. Without it, even a tiny amount of noise can eventually grow to overwhelm the signal if the circuit is deep enough.[^dy6q9pwwcni]

Note that assumption 2 is about noise reduction on inactive circuits whereas assumption 5 is about lack of noise amplification on active circuits. Assumption 2 says we should have 

$$
\begin{equation} |\delta\mathbf{a}^l_t(x)|\leq \epsilon \Rightarrow |\text{ReLU}\left(w^{l+1}_t \delta\mathbf{a}^l_t(x)+\mathbf{b}^{l+1}\right)|=0 \tag{5.9} \end{equation}
$$

 for some sufficiently small $\epsilon>0$. Assumption 5 says we should have 

$$
\begin{equation} \frac{|\mathbf{a}^{l+1}_t(x)-\text{ReLU}\left(w^{l+1}_t (\mathbf{a}^l_t+\delta\mathbf{a}^l_t(x))+\mathbf{b}^{l+1}\right)|}{|\mathbf{a}^{l+1}_t(x)|}\leq \frac{|\delta\mathbf{a}^l_t(x)|}{|\mathbf{a}^l_t(x)|}\,. \tag{5.10}\end{equation}
$$

5.3 Notation
------------

### 5.3.1 Bracket notation

Bracket notation is a type of vector notation that's excellent for thinking about outer products. It's also the vector notation usually used in quantum mechanics, and the term "superposition" is a quantum loan-word, so deploying it here seemed kabbalistically accurate.

It works like this: 

*   $|v\rangle$ denotes a column vector, also called a *ket*. 
*   $\langle u|$ denotes a row vector, also called a *bra*. 

$$
\begin{equation} \langle u| := |u\rangle^\top\tag{5.11} \end{equation}
$$

*   $\langle u|v \rangle$ denotes the inner product[^h76nxkkgqbe] of two vectors, yielding a scalar number: 

$$
\begin{equation} \langle u|v \rangle :=\sum_i (u)_i (v)_i \tag{5.12}\end{equation}
$$

*   $|v\rangle\langle u|$ denotes the outer product of two vectors, yielding a matrix: 

$$
\begin{equation} (|v\rangle|u\rangle)_{i,j} := (v)_i(u)_j\tag{5.13} \end{equation}
$$

We will use bracket notation to represent $D/d$-dimensional vectors, like the embedding vectors in section 5.4.1

### 5.3.2 Mixed vector notation 

So far, we've used $\mathbf{bold}$ to represent $d$-dimensional vectors, i.e., $\mathbf{a}^l_t$ and $\mathbf{b}$, and two-dimensional vectors, i.e., $\mathbf{x}^l_t$. And we just defined $|\text{ket}\rangle$ for $D/d$-dimensional vectors in the previous section 5.3.1

We will also want to mix $\mathbf{bold}$ and $|\text{ket}\rangle$ notation to make $D$-dimensional vectors by stacking $d=4$ number of $D/d$-dimensional vectors. 

$$
\begin{equation}    |\mathbf{V\rangle} := \left[\begin{array}{l}        \left(|\mathbf{V\rangle}\right)_{0:\frac{D}{d}}\\[4pt]        \left(|\mathbf{V\rangle}\right)_{\frac{D}{d}:2\frac{D}{d}}\\[4pt]       \left(|\mathbf{V\rangle}\right)_{2\frac{D}{d}:3\frac{D}{d}}\\[4pt]        \left(|\mathbf{V\rangle}\right)_{3\frac{D}{d}:D}    \end{array}\right] \tag{5.14}\end{equation}
$$

where $|\mathbf{V\rangle}$ is a $D$-dimensional vector and $\left(|\mathbf{V\rangle}\right)_{i:j}$ is the section of $|\mathbf{V\rangle}$ from index $i$ to index $j-1$. Each of $\left(|\mathbf{V\rangle}\right)_{0:\frac{D}{d}}$, $\left(|\mathbf{V\rangle}\right)_{\frac{D}{d}:2\frac{D}{d}}$, $\left(|\mathbf{V\rangle}\right)_{2\frac{D}{d}:3\frac{D}{d}}$, $\left(|\mathbf{V\rangle}\right)_{3\frac{D}{d}:D}$ is $D/d$-dimensional.

Any $d\times d$-matrix will act on $|\mathbf{V\rangle}$ as if it were a $d$-dimensional vector, ignoring the $|\text{ket}\rangle$ dimension. For example: 

$$
\begin{equation}    \begin{bmatrix}        0 & 0 & 1 & 0\        0 & 0 & 0 & 1\        1 & 0 & 0 & 0\        0 & 1 & 0 & 0   \end{bmatrix}    |\mathbf{V\rangle} := \left[\begin{array}{l}        \left(|\mathbf{V\rangle}\right)_{2\frac{D}{d}:3\frac{D}{d}}\\[4pt]        \left(|\mathbf{V\rangle}\right)_{3\frac{D}{d}:D}\\[4pt]        \left(|\mathbf{V\rangle}\right)_{0:\frac{D}{d}}\\[4pt]        \left(|\mathbf{V\rangle}\right)_{\frac{D}{d}:2\frac{D}{d}}     \end{array}\right]\tag{5.15} \end{equation}
$$

Any $\langle \text{bra|}$ will act on $|\mathbf{V\rangle}$ as if it were a $|\text{ket}\rangle$, ignoring the $d$-dimension. For example: 

$$
\begin{equation}    \langle u|\mathbf{V \rangle} := \left[\begin{array}{l}        \langle u|\left(|\mathbf{V\rangle}\right)_{0:\frac{D}{d}}\\[4pt]        \langle u|\left(|\mathbf{V\rangle}\right)_{\frac{D}{d}:2\frac{D}{d}}\\[4pt]        \langle u|\left(|\mathbf{V\rangle}\right)_{2\frac{D}{d}:3\frac{D}{d}}\\[4pt]        \langle u|\left(|\mathbf{V\rangle}\right)_{3\frac{D}{d}:D}    \end{array}\right] \tag{5.16}\end{equation}
$$

5.4 Embedding the Circuits 
---------------------------

In this section, we describe a general method for embedding any set of small circuits that satisfy the assumptions 1 - 5 listed in Section 5.2.2

The activations $|\mathbf{A\rangle^l}$ of the large network at layer $l$ are computed from the activations at layer $|\mathbf{A\rangle^{l-1}}$ as 

$$
\begin{equation}    |\mathbf{A\rangle^l} := \text{ReLU}(W^l|\mathbf{A\rangle^{l-1}}+|\mathbf{B\rangle^l}) \tag{5.17}\end{equation}
$$

### 5.4.1 Embedding the weights

To embed the small circuit weights in the large network, we first split their weight matrices $w^l_t$ into two parts: the averaged weights across all circuits $\bar{w}^l$, and the differing weights $\Delta w^l_t$:

$$
\begin{equation}    \left(\bar{w}^l\right)_{i,j} := \underset{t}{\mathbb{E}}\left[\left(w^l_t\right)_{i,j}\right] \tag{5.18}\end{equation}
$$

$$
\begin{equation}    \Delta w_t^l := w^l_t - \bar{w}^l \tag{5.19}\end{equation}
$$

The differing weights $\Delta w^l_t$ are embedded into the weights of the large network using *embedding vectors* $|e_t^l\rangle$. The averaged weights $\bar{w}^l$ are embedded using an *embedding matrix* $\mathcal{W}^l\in \mathbb{R}^{\frac{D}{d}\times \frac{D}{d}}$: 

$$
\begin{equation}    W^l := \bar{w}^l\mathcal{W}^l + \frac{1}{S}\sum_t\Delta{w}^l_t|e_t^l\rangle\langle e_t^{l-1|} \quad \text{for} \quad l\geq2 \tag{5.20}\end{equation}
$$

**Embedding vectors**  
The embedding vectors $|e_t^l\rangle$ are constructed using exactly the same algorithm described in the [previous post](https://www.lesswrong.com/posts/FWkZYQceEzL84tNej/circuits-in-superposition-2-now-with-less-wrong-math#Constructing_the_Embedding_and_Unembedding_matrices). The information about them that matters most for the rest of this post: 

*   $|e^l_t\rangle$ denotes the embedding vector for circuit $t$ in layer $l$. $|e^l_t\rangle$ has dimension $D/d$. 
*   $S$ is the embedding redundancy, i.e., the number of large network neurons used to represent each small circuit neuron. 
*   $|e^l_t\rangle$ is a $S$-hot vector, i.e., it has $S$ ones and $(\frac{D}{d}-S)$ zeros. As a consequence of this, we have 

$$
\begin{equation} \frac{1}{S}\langle e^l_t|e^l_t \rangle = 1 \tag{5.21}\end{equation}
$$

*   $\frac{1}{S}\langle e^l_t|$ is the un-embedding vector for circuit $t$ in layer $l$. 
*   Any pair of embedding vectors for different circuits $t\neq u$ in the same layer $l$ will share at most one large network neuron. Therefore: 

$$
\begin{equation} \frac{1}{S}\langle e_t^l|e_u^l \rangle = \begin{cases} \frac{1}{S} \ 0 \end{cases} \quad\text{for}\quad{t\neq u}\tag{5.22} \end{equation}
$$

**Embedding matrix** 

$\mathcal{W}^l$ is constructed as 

$$
\begin{equation}    \left(\mathcal{W}^l\right)_{i,j} := \sum_t\begin{cases}        \frac{1}{S} & \text{if} \quad  \left(|e_t^l\rangle\langle e_t^{l-1|}\right)_{i,j} > 0\       -\chi & \text{if} \quad  \left(|e_t^l\rangle\langle e_t^{l-1|}\right)_{i,j} = 0    \end{cases} \tag{5.23} \end{equation}
$$

 Where the scalar $\chi$ is chosen to balance the weights of $\mathcal{W}$, such that 

$$
\begin{equation}    \underset{t\neq u}{\mathbb{E}}\left[\langle e_t^l|\mathcal{W}^l|e_u^{l-1\rangle}\right] = 0\tag{5.24} \end{equation}
$$

This ensures that interference terms between different circuits do not systematically aggregate along any particular direction.

**Layer 0**  
As in the [previous post](https://www.lesswrong.com/posts/FWkZYQceEzL84tNej/circuits-in-superposition-2-now-with-less-wrong-math#Layer_0), the weights at layer $0$ are treated differently. Instead of using the weight embedding described in the previous subsection, we just embed the circuit input vectors into the input vector of the network as 

$$
\begin{equation}    |\mathbf{A\rangle^0} = \sum_{t} w^1_t \mathbf{a}_t^0 |e^1_t\rangle \,. \tag{5.25}\end{equation}
$$

This allows us to set the first weight matrix to an identity, 

$$
\begin{equation} W^1 = \mathbb{I}\,, \tag{5.26}\end{equation}
$$

yielding 

$$
\begin{equation}    |\mathbf{A\rangle^1} = ReLU\left(\sum_tw^1_t \mathbf{a}_t^0 |e^1_t\rangle +|\mathbf{B\rangle^1}\right)\,. \tag{5.27}\end{equation}
$$

### 5.4.2 Embedding the biases

We embed the circuit biases $\mathbf{b}^l\in\mathbb{R}^{d}$ into the network biases $|\mathbf{B\rangle^l}\in\mathbb{R}^{D}$ by simply spreading them out over the full $D$ dimensions: 

$$
\begin{equation}    |\mathbf{B\rangle^l} := \mathbf{b}^l|1\rangle :=    \begin{bmatrix}        (\mathbf{b}^l)_0|1\rangle \        (\mathbf{b}^l)_1|1\rangle \       (\mathbf{b}^l)_2|1\rangle \        (\mathbf{b}^l)_3|1\rangle    \end{bmatrix}\tag{5.28} \end{equation}
$$

 where $|1\rangle$ is just the $D/d$-vector with value 1 everywhere, i.e.: 

$$
\begin{equation}    \left(|1\rangle\right)_i := 1 \quad \text{for all $i$} \tag{5.29}\end{equation}
$$

5.5 Reading out the small circuit activations 
----------------------------------------------

If the embedding works, we can read out the approximate small circuit activations from the activations of the large network, up to some error tolerance. Using the un-embedding vector $\frac{1}{S}\langle e_t^l|$, we define the estimator for the small circuit activations for each layer as 

$$
\begin{equation}    \hat{\mathbf{a}}^l_t := \frac{1}{S}\langle e^l_t|\mathbf{A \rangle^l} :=    \begin{bmatrix}\begin{array}{l}        \dfrac{1}{S}\langle e^l_t|\left(|\mathbf{A\rangle^l}\right)_{0:\frac{D}{d}}\\[6pt]        \dfrac{1}{S}\langle e^l_t|\left(|\mathbf{A\rangle^l}\right)_{\frac{D}{d}:2\frac{D}{d}}\\[6pt]       \dfrac{1}{S}\langle e^l_t|\left(|\mathbf{A\rangle^l}\right)_{2\frac{D}{d}:3\frac{D}{d}}\\[6pt]        \dfrac{1}{S}\langle e^l_t|\left(|\mathbf{A\rangle^l}\right)_{3\frac{D}{d}:D}        \end{array}    \end{bmatrix}\tag{5.30} \end{equation}
$$

Following equations (5.5) and (5.6), we define the estimators for the On-indicator 

$$
\begin{equation}    \hat\alpha^l_t := \left(\hat{\mathbf{a}}^l_t\right)_0 - \left(\hat{\mathbf{a}}^l_t\right)_1 \tag{5.31}\end{equation}
$$

 and the rotating vector 

$$
\begin{equation}    \hat{\mathbf{x}}^l_t := \begin{bmatrix}        \left(\hat{\mathbf{a}}^l_t\right)_2 - \hat\alpha_t^l\        \left(\hat{\mathbf{a}}^l_t\right)_3 - \hat\alpha_t^l    \end{bmatrix}\tag{5.32} \end{equation}
$$

 The readout errors are defined as 

$$
\begin{equation}    \delta\mathbf{a}^l_t = \hat{\mathbf{a}}^l_t-\mathbf{a}^l_t\tag{5.33} \end{equation}
$$

$$
\begin{equation}    \delta\alpha^l_t := \hat\alpha^l_t-\alpha^l_t \tag{5.34}\end{equation}
$$

$$
\begin{equation}    \delta \mathbf{x}_t^l := \hat{\mathbf{x}}^l_t-\mathbf{x}_t^l\tag{5.35} \end{equation}
$$

6 Appendix 2: Error calculations
================================

In this section we'll attempt to adapt [the error calculations from the previous post](https://www.lesswrong.com/posts/FWkZYQceEzL84tNej/circuits-in-superposition-2-now-with-less-wrong-math#Error_calculation) to the new framework, and use the resulting expressions to try and predict the errors on our conditional rotation circuits. The main change in the construction we need to account for is the presence of the embedding matrix $\mathcal{W}^l$, which didn't exist in the construction the previous post used. We will also include some particular terms in the error calculations that the previous post ignored. These terms are sub-leading in the limit of large network width $D$ and number of circuits $T$, but turned out to be non-negligible for some of the empirical data we tested the theory on.

The results here will only hold as long as the size of the errors stays much smaller than the size of the signal, which won't always be the case in reality. Past that point, errors may compound much more quickly over layers than the results here would predict.

We find that the terms for the error on inactive circuits carry over unchanged, but the error on active circuits is a little different.

Note that these calculations are not as careful as the ones in the previous post. In some spots, we just guess at approximations for certain terms and then check those guesses empirically. 

6.1 Error on inactive circuits
------------------------------

Provided the overall error stays small enough to not change the signs of any $\text{ReLU}$ neuron preactivations, the only source of error on inactive circuits is the embedding overlap error, which was estimated in the previous post as: 

$$
\begin{equation} \delta\mathbf{a}^l_t=(\delta\mathbf{a}^l_t)_{\text{embedding-overlap}} \approx \frac{1}{S}\sum_{\substack{\text{$u$ is active}\\u\neq t}}\langle e^l_t|e^l_u \rangle\mathbf{a}^{l}_u\quad \text{if $t$ is inactive} \tag{6.1}\end{equation}
$$

This is the error that results from signal in active circuits bleeding over into the inactive circuits they share neurons with. Since this error depends purely on how the activations of the circuits are embedded in the neurons of the network and that embedding hasn't changed from the previous construction, the formula for it remains the same.

In the previous post, we used the approximation $\underset{u\neq t}{\mathbb{E}}\left[\left(\frac{1}{S}\langle e^l_t|e^l_u \rangle\right)^2\right] \approx \frac{d}{D}$ to evaluate this error as[^uij2d8peb5l]

$$
\begin{equation} \mathbb{E}\left[|\delta\mathbf{a}^l_t|^2\right] \approx z\frac{d}{D} \underset{v\text{ is active}}{\mathbb{E}}\left[|\mathbf{a}_v^l|^2\right] \quad \text{if $t$ is inactive}\tag{6.2} \end{equation}
$$

Here, we will instead use the slightly more precise approximation 

$$
\begin{equation} \underset{u\neq t}{\mathbb{E}}\left[\left(\frac{1}{S}\langle e^l_t|e^l_u \rangle\right)^2\right] \approx \frac{d}{D} - \frac{1}{ST}\,. \tag{6.3}\end{equation}
$$

This results in a minor but noticeable improvement in the fitting of the data. Inserting the new approximation into the previous derivation yields 

$$
\begin{equation} \mathbb{E}\left[|\delta\mathbf{a}^l_t|^2\right] \approx z\left(\frac{d}{D}-\frac{1}{ST}\right)\underset{v\text{ is active}}{\mathbb{E}}\left[|\mathbf{a}_v^l|^2\right] \quad \text{if $t$ is inactive}\tag{6.4} \end{equation}
$$

6.2 Error on active circuits
----------------------------

We'll assume for now that $\bar{w}^l=0$, so that Equation (5.20) becomes 

$$
\begin{equation}    W^l = \frac{1}{S}\sum_t w^l_t|e_t^l\rangle\langle e_t^{l-1}| \quad \text{for} \quad l\geq2 \tag{6.5}\end{equation}
$$

 From definitions (5.28) and (5.29), it follows that 

$$
\begin{equation}    \frac{1}{S}\langle e^l_t|\mathbf{B \rangle^l} = \mathbf{b}^l \end{equation}
$$

Using the definition of the readout for circuit $t$ in layer $l$ $\hat{\mathbf{a}}^l_t$, from Equation (5.30), the error $\delta\mathbf{a}^l_t$ can be written as 

$$
\begin{align} \delta\mathbf{a}^l_t &:= \hat{\mathbf{a}}^l_t - \mathbf{a}^l_t \tag{6.7}\ &= \frac{1}{S}\langle e^l_t|ReLU\left(W^l |\mathbf{A\rangle^{l-1}} + |\mathbf{B\rangle^l}\right)- \mathbf{a}^l_t \tag{6.8}\ &=\frac{1}{S}\langle e^l_t|ReLU\left(\sum_u |e_u^l\rangle w^l_u\frac{1}{S}\langle e^{l-1 \rangle_u|\mathbf{A}^{l-1}} + |\mathbf{B\rangle^l}\right)- \mathbf{a}^l_t\tag{6.9}\ &=\frac{1}{S}\langle e^l_t|ReLU\left(\sum_u |e_u^l\rangle w^l_u\left(\mathbf{a}^{l-1}_u+\delta\mathbf{a}^{l-1}_u\right) + |\mathbf{B\rangle^l}\right)- \mathbf{a}^l_t\tag{6.10} \end{align}
$$

If we split the sum over circuits $\sum_u$ into active and passive circuits, we can simplify this expression: 

*   The term $\sum_{\text{$u$ is inactive}} |e_u^l\rangle w^l_u\mathbf{a}^{l-1}_u$ drops out because by definition $\mathbf{a}^{l-1}_u=0$ for inactive circuits. 
*   From the previous section, we know that 

$$
\begin{equation} \sum_{\text{$u$ is inactive}} |e_u^l\rangle w^l_u\delta\mathbf{a}^{l-1}_u=\sum_{\text{$u$ is inactive}} |e_u^l\rangle w^l_u\delta(\mathbf{a}^{l-1}_u)_{\text{embedding overlap}}\,.\tag{6.11} \end{equation}
$$

*   Provided the noise stays small compared to the signal, the term $\sum_{\text{$u$ is active}, u\neq t} |e_u^l\rangle w^l_u\delta\mathbf{a}^{l-1}_u$ will be sub-leading compared to $\sum_{\text{$u$ is active}} |e_u^l\rangle w^l_u \mathbf{a}^{l-1}_u$. Instead of neglecting it entirely however, we will keep its embedding overlap error contribution 

$$
\begin{equation} \sum_{\text{$u$ is active},u\neq t} |e_u^l\rangle w^l_u(\delta\mathbf{a}^{l-1}_u)_{\text{embedding-overlap}}\,, \tag{6.12}\end{equation}
$$

since it is simple to evaluate, and only neglect the rest.[^sjh2l2v0qq]

This leaves us with 

$$
\begin{align} \delta\mathbf{a}^l_t \approx \frac{1}{S}\langle e^l_t|ReLU\left(\sum_{\text{$u$ is active}} |e_u^l\rangle w^l_u\mathbf{a}^{l-1}_u+|e_t^l\rangle w^l_t\delta\mathbf{a}^{l-1}_t+ \sum_{u\neq t} |e_u^l\rangle w^l_u(\delta\mathbf{a}^{l-1}_u)_{\text{embedding overlap}}+|\mathbf{B\rangle^l}\right)- \mathbf{a}^l_t  \tag{6.13} \end{align}
$$

As in the last post, we will assume that all ReLU neurons used by the active circuits are turned on, since doing so will simplify the calculations and not overestimate the errors in expectation.[^238576ranyn] This gives 

$$
\begin{equation} \begin{aligned} \delta\mathbf{a}^l_t \approx &\frac{1}{S}\sum_{\text{$u$ is active}}\langle e^l_t|e_u^l \rangle w^l_u\mathbf{a}^{l-1}_u- \mathbf{a}^l_t+\frac{1}{S}\langle e^l_t|e_t^l \rangle w^l_t\delta\mathbf{a}^{l-1}_t\ &+\frac{1}{S}\sum_{\text{$u$ is inactive}}\langle e^l_t|e_u^l \rangle w^l_u(\delta\mathbf{a}^{l-1}_u)_{\text{embedding overlap}} +\langle e^l_t|\mathbf{B \rangle^l} \end{aligned} \quad \text{if $t$ is active}  \tag{6.14}\end{equation}
$$

Inserting approximation (6.1) for $(\delta\mathbf{a}^{l-1}_u)_{\text{embedding overlap}}$ on inactive circuits into this expression yields 

$$
\begin{equation} \begin{aligned} \delta\mathbf{a}^l_t =&\frac{1}{S}\sum_{\text{$u$ is active}}\langle e^l_t|e_u^l \rangle w^l_u\mathbf{a}^{l-1}_u- \mathbf{a}^l_t+\frac{1}{S}\langle e^l_t|e_t^l \rangle w^l_t\delta\mathbf{a}^{l-1}_t\ &+\frac{1}{S^2}\sum_{\substack{\text{$v$ is active}\\v\neq u}}\sum_{u\neq t}\langle e^l_t|e_u^l \rangle w^l_u\langle e^{l-1 \rangle_u|e^{l-1}_v}\mathbf{a}^{l-1}_v +\langle e^l_t|\mathbf{B \rangle^l}\end{aligned} \quad \text{if $t$ is active}  \tag{6.15}\end{equation}
$$

Which evaluates to 

$$
\begin{equation} \begin{aligned} \delta\mathbf{a}^l_t \approx&\frac{1}{S}\langle e^l_t|W^l|e_t^{l-1\rangle}\mathbf{a}_t^{l-1}    - w^l_t\mathbf{a}_t^{l-1} \    &+ \frac{1}{S}\sum_{\substack{\text{$v$ is active}\\v\neq t}}   \Big(\langle e^l_t|W^l|e_v^{l-1\rangle}\mathbf{a}_v^{l-1} -    \langle e^{l-1 \rangle_t|e^{l-1}_v} w^l_t\mathbf{a}_v    ^{l-1}\Big)   + w_t^l\delta\mathbf{a}^l_t\end{aligned}\quad \text{if $t$ is active}  \tag{6.16}\end{equation}
$$

This derivation assumed that $\bar{w}^l=0$, i.e., the circuits are uncorrelated with each other. However, we're just going to go ahead and guess that (6.16) is still a reasonable approximation in the case $\bar{w}^l\neq 0$ as well.[^4fi7mw35ubj] We'll see how true that is in practice when we compare these predictions to the error we measure in practice.

We can break this expression up into three components. 

$$
\begin{align}    &\delta\mathbf{a}^l_t \approx (\delta\mathbf{a}_t^l)_{\text{self}} + (\delta\mathbf{a}_t^l)_{\text{others}} + (\delta\mathbf{a}_t^l)_{\text{previous}}\tag{6.17}\    &(\delta\mathbf{a}_t^l)_{\text{self}} := \frac{1}{S}\langle e^l_t|W^l|e_t^{l-1\rangle}\mathbf{a}_t^{l-1} - w_t^l\mathbf{a}^{l-1}_t   \tag{6.18} \   &(\delta\mathbf{a}_t^l)_{\text{others}} := \frac{1}{S}\sum_{\substack{\text{$v$ is active}\ v\neq t}}    \Big(\langle e^l_t|W^l|e_t^{l-1\rangle}\mathbf{a}_t^{l-1} -    \langle e^{l-1 \rangle_t|e^{l-1}_v} w^l_t\mathbf{a}_v    ^{l-1}\Big) \tag{6.19}  \   &(\delta\mathbf{a}_t^l)_{\text{previous}} := w_t^l\delta\mathbf{a}^{l-1}_t\tag{6.20} \end{align}
$$

These three components have mean zero and are uncorrelated with each other, so we can calculate their mean squared errors separately.

### 6.2.1 Error from Self Signal

Here we'll calculate the mean square of the error contribution $(\delta\mathbf{a}_t^l)_{\text{self}}$, from Equation (6.18). Inserting the definition of $W^l$ into the definition of $(\delta\mathbf{a}_t^l)_{\text{self}}$ gives: 

$$
\begin{align}    (\delta\mathbf{a}_t^l)_{\text{self}} &:= \frac{1}{S}\langle e^l_t|W^l|e_t^{l-1\rangle}\mathbf{a}_t^{l-1} - w_t^l\mathbf{a}^{l-1}_t \tag{6.21}\   & = \frac{1}{S}\langle e^l_t|    \left(\bar{w}^l\mathcal{W}^l + \frac{1}{S}\sum_u\Delta{w}^l_u|e_u^l\rangle\langle e_u^{l-1|}\right)    |e_t^{l-1\rangle}\mathbf{a}_t^{l-1}    - w_t^l\mathbf{a}^{l-1}_t\tag{6.22}\    &= \frac{1}{S^2}\sum_{u\neq t} \langle e^l_t|e_u^l \rangle\langle e_u^{l-1 \rangle|e_t^{l-1}}\bar{w}_t^l\mathbf{a}_t^{l-1}    + \Delta w^l_t\mathbf{a}_t^{l-1}   + \bar{w}_t^l\mathbf{a}_t^{l-1}    - w^l_t\mathbf{a}_t^{l-1}\tag{6.23}\    &= \frac{1}{S^2}\sum_{u\neq t} \langle e^l_t|e_u^l \rangle\langle e_u^{l-1 \rangle|e_t^{l-1}}\bar{w}_t^l\mathbf{a}_t^{l-1}\,, \tag{6.24}\end{align}
$$

in the third line, we used the fact that 

$$
\begin{equation}    \frac{1}{S}\langle e^l_t|\mathcal{W}^l|e_t^{l-1\rangle} = 1\,, \tag{6.25} \end{equation}
$$

which follows from the definition of $\mathcal{W}^l$ in Equation (5.23).

To estimate the expected norm of the error, we insert approximation (6.3) again: 

$$
\begin{align}    \mathbb{E}\left[\left|    (\delta\mathbf{a}_t^l)_{\text{self}}    \right|^2\right]     &=    (T-1)    \mathbb{E}\left[\left(    \frac{1}{S}\langle e^l_t|e_u^l \rangle    \right)^2\right]    \mathbb{E}\left[\left(    \frac{1}{S}\langle e_u^{l-1 \rangle|e_t^{l-1}}   \right)^2\right]    \mathbb{E}\left[\left|    \bar{w}_t^l\mathbf{a}_t^{l-1}    \right|^2\right]   \tag{6.26} \ &\approx    T\left(\frac{d}{D}-\frac{1}{ST}\right)^2    \mathbb{E}\left[\left|    \bar{w}_t^l\mathbf{a}_t^{l-1}    \right|^2\right]\tag{6.27} \end{align}
$$

### 6.2.2 Error from others' signals

Here we'll calculate the mean square of the error contribution $(\delta\mathbf{a}_t^l)_{\text{others}}$ from Equation (6.19). First, we further subdivide $(\delta\mathbf{a}_t^l)_{\text{others}}$ into two parts, one for terms involving $\Delta w$ and one for terms involving $\bar{w}$. 

$$
\begin{align}    &(\delta\mathbf{a}_t^l)_{\text{others}} = (\delta\mathbf{a}_t^l)_{\text{others}, \bar{w}} + (\delta\mathbf{a}_t^l)_{\text{others}, \Delta w}    \tag{6.28}\   &(\delta\mathbf{a}_t^l)_{\text{others}, \Delta w} := \frac{1}{S}\sum_{\substack{\text{$v$ is active}\\v\neq t}}    \left(\langle e^l_t|    \left(\frac{1}{S}\sum_u\Delta{w}^l_u|e_u^l\rangle\langle e_u^{l-1|}\right)    |e_t^{l-1\rangle}\mathbf{a}_t^{l-1} -    \langle e^{l-1 \rangle_t|e^{l-1}_v} \Delta w^l_t\mathbf{a}_v    ^{l-1}\right)   \tag{6.29} \    & (\delta\mathbf{a}_t^l)_{\text{others}, \bar{w}} := \frac{1}{S}\sum_{\substack{\text{$v$ is active}\\v\neq t}}   \Big(\langle e^l_t|\bar{w}\mathcal{W}^l|e_t^{l-1\rangle}\mathbf{a}_t^{l-1} -   \langle e^{l-1 \rangle_t|e^{l-1}_v} \bar{w}^l\mathbf{a}_v    ^{l-1}\Big)\tag{6.30} \end{align}
$$

We can straightforwardly approximate the expectation of the square of $(\delta\mathbf{a}_t^l)_{\text{others}, \Delta w}$. The steps for this are similar to those we used for $(\delta\mathbf{a}_t^l)_{\text{self}}$ in the previous subsection, see Equations (6.26) and (6.27). 

$$
\begin{equation}    \mathbb{E}\left[\left|    (\delta\mathbf{a}_t^l)_{\text{others}, \Delta w}    \right|^2\right]        \approx    (z-1)T\left(\frac{d}{D} - \frac{1}{ST}\right)^2 \underset{u\neq v}{\mathbb{E}}\left[\left|\Delta w^l_u \mathbf{a}^{l-1}_v\right|^2 \right]   + (z-1)\left(\frac{d}{D} - \frac{1}{ST}\right) \underset{v}{\mathbb{E}}\left[\left|\Delta w^l_v \mathbf{a}^{l-1}_v\right|^2 \right] \tag{6.31}\end{equation}
$$

The expectation of $(\delta\mathbf{a}_t^l)_{\text{others}, \bar{w}}$ squared is a bit tougher. We didn't see an easy way to formally derive an approximation for it. So instead, we're going to be lazy: We'll just guess that it can be approximately described by the same formula as the one for $(\delta\mathbf{a}_t^l)_{\text{others}, \Delta w}$, just with $\Delta w^l_u$ and $\Delta w^l_v$ swapped for $\bar{w}^l$. Then we'll just check that guess empirically on some example data. 

$$
\begin{equation}    \mathbb{E}\left[\left|    (\delta\mathbf{a}_t^l)_{\text{others}, \bar{w}}    \right|^2\right]        \approx    (z-1)T\left(\frac{d}{D} - \frac{1}{ST}\right)^2 \underset{v}{\mathbb{E}}\left[\left|\bar{w}^l \mathbf{a}^{l-1}_v\right|^2 \right]   + (z-1)\left(\frac{d}{D} - \frac{1}{ST}\right) \underset{v}{\mathbb{E}}\left[\left|\bar{w}^l \mathbf{a}^{l-1}_v\right|^2 \right] \tag{6.32}\end{equation}
$$

To verify this equation, we can use the fact that $\bar{w}^l$ can be factored out from Equation (6.30). So, if the result holds for one set of circuits, it should hold for any set of circuits. We just need to make up some values for $a_v^{l-1}$, $\bar{w}^l$, and $\Delta w$ to check the equation on.[^efb2i0vf1gr] To keep it simple, we choose the following: 

$$
\begin{align}    &a_v^{l-1} = 1 \quad \text{for all active circuits $v$}\tag{6.33}\    &\bar{w}^l = 1 \tag{6.34}\   &\Delta w_u = \text{[1 or -1]}_u    := \begin{cases}        1 & \text{with probability 0.5} \      -1 & \text{with probability 0.5}    \end{cases}    \quad \text{sampled independently for each circuit $u$} \tag{6.35}\end{align}
$$

We find a good fit for small values of $(\delta\mathbf{a}_t^l)_{\text{others}}$ and small values of $S$. For larger $(\delta\mathbf{a}_t^l)_{\text{others}}$ and $S$ we see deviations of up to 50% from the hypothesis. I.e, the approximation is not perfect, but it seems ok. At larger errors, we expect all our error calculations to break down anyway because the errors start getting large enough to switch on ReLU neurons that should be off, leading to cascading failures as the network has a "seizure". 

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/f08532a4130244c793fe2f2e94a627c4b543ed59b945ff7d.png)

The two terms also add up as we would expect. 

$$
\begin{align}    \mathbb{E}\left[\left|    (\delta\mathbf{a}_t^l)_{\text{others}}    \right|^2\right]        &=    \mathbb{E}\left[\left|   (\delta\mathbf{a}_t^l)_{\text{others}, \Delta w}    \right|^2\right]        +    \mathbb{E}\left[\left|    (\delta\mathbf{a}_t^l)_{\text{others}, \bar{w}}    \right|^2\right] \tag{6.36} \   &\approx    (z-1)T\left(\frac{d}{D} - \frac{1}{ST}\right)^2 \underset{u\neq v}{\mathbb{E}}\left[\left| w^l_u \mathbf{a}^{l-1}_v\right|^2 \right]     + (z-1)\left(\frac{d}{D} - \frac{1}{ST}\right) \underset{v}{\mathbb{E}}\left[\left| w^l_v \mathbf{a}^{l-1}_v\right|^2 \right]\tag{6.37} \end{align}
$$

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/c325f4f3fe3ab50cd4f73fe0ffb9e7576c96a0b867c4ec6f.png)

### 6.2.3 Previous error

Assumption 5 about our circuits was that active circuits should not amplify the size of errors relative to the size of the signal from layer to layer: 

$$
\begin{equation}    \frac{\left|    (w^l_t\delta\mathbf{a}_t^{l-1})    \right|^2}{|\mathbf{a}^l_t|} \leq \frac{\left|    \delta\mathbf{a}_t^{l-1}     \right|^2}{|\mathbf{a}^{l-1}_t|}\,\quad \text{if $t$ is active}. \tag{6.38}\end{equation}
$$

 Since $|\mathbf{a}^l_t|=|\mathbf{a}^{l-1}_t|$ for our circuits, this implies that 

$$
\begin{equation}    \mathbb{E}\left[\left|    (\delta\mathbf{a}_t^l)_{\text{previous}}    \right|^2\right] = \mathbb{E}\left[\left|    (w^l_t\delta\mathbf{a}_t^{l-1})     \right|^2\right] \leq \mathbb{E}\left[\left|    \delta\mathbf{a}_t^{l-1}    \right|^2\right]\,. \tag{6.39}\end{equation}
$$

 For simplicity, we use the most pessimistic estimate: 

$$
\begin{equation}    \mathbb{E}\left[\left|    (\delta\mathbf{a}_t^l)_{\text{previous}}    \right|^2\right] = \mathbb{E}\left[\left|    \delta\mathbf{a}_t^{l-1}    \right|^2\right] \tag{6.40}\end{equation}
$$

### 6.2.4 Adding It All Up

Adding the three terms together and applying the resulting formula recursively to evaluate the propagated error from previous layers, we get 

$$
\begin{equation}\begin{aligned}    \mathbb{E}\left[\left|\delta\mathbf{a}^l_t\right|^2\right] \approx&    (l-1)T\left(\frac{d}{D}-\frac{1}{ST}\right)^2\left(   z\underset{u\neq v}{\mathbb{E}}\left[\left| \Delta w^l_u \mathbf{a}^{l-1}_v\right|^2 \right]   +(z-1)\underset{v}{\mathbb{E}}\left[\left| \bar{w}^l \mathbf{a}^{l-1}_v\right|^2 \right]    \right)  \  & + l\left(\frac{d}{D} - \frac{1}{ST}\right)(z-1) \underset{v}{\mathbb{E}}\left[\left| w^l_v \mathbf{a}^{l-1}_v\right|^2 \right] \end{aligned} \tag{6.41}\end{equation}
$$

The first term has a prefactor of $(l-1)$ while the second has a prefactor of $l$ because the first term is the propagation error (from the previous post) which only appears from the second layer onward, while the second term is the embedding overlap error, which appears from the first layer onward.

6.3 Errors on our conditional rotation circuits}
------------------------------------------------

### 6.3.1 Errors on the On-indicators

The On-indicators $\alpha^l_t$ are read out from the circuits' hidden activations as $\alpha^l_t := (\mathbf{a}_t^l)_0 - (\mathbf{a}_t^l)_1$. Provided the overall error stays small enough to not overwhelm any ReLU neuron enough to flip it from off to on, the errors on $(\mathbf{a}^l_t)_0$ and $(\mathbf{a}^l_t)_1$ will be identical for active circuits, and thus cancel out exactly 

$$
\begin{equation}    \delta\alpha_t^l = 0 \quad \text{if $t$ is active}\,. \tag{6.42}\end{equation}
$$

 For inactive circuits, equations (5.4) and (6.4)  yield: 

$$
\begin{equation}    \mathbb{E}\left[\left(\delta\alpha_t^l\right)^2\right] = (1.5-0.5)\left(\frac{d}{D}-\frac{1}{ST}\right)z =\left(\frac{d}{D}-\frac{1}{ST}\right)z\quad \text{if $t$ is inactive}\,.\tag{6.43} \end{equation}
$$

### 6.3.2 Errors on the Rotating Vectors

**For active circuits **  
We can evaluate the errors on active rotation circuits using Equation (6.41). We want the error on $\mathbb{E}\left[\left(\delta\mathbf{x}_t^l\right)^2\right]$ though, not on $\mathbb{E}\left[\left(\delta\mathbf{a}_t^l\right)^2\right]$. However, provided that $\delta\alpha_t^l=0$, we have 

$$
\begin{equation}    \delta\mathbf{x}_t^l = \begin{bmatrix}        \left(\delta\mathbf{a}_t^l\right)_2 \ \left(\delta\mathbf{a}_t^l\right)_3    \end{bmatrix} \tag{6.44}\end{equation}
$$

 So, since $\delta\alpha_t^l=0$ for active circuits, we can just restrict (6.41) to the last two vector indices of $\delta\mathbf{a}$ to calculate the error:

$$
\begin{align}    \mathbb{E}\left[\left|\delta\mathbf{x}^l_t\right|^2\right] =&    \mathbb{E}\left[\left|\delta\mathbf{a}^l_t\right|^2_{2:3}\right]\tag{6.45}\    \approx&    (l-1)T\left(\frac{d}{D}-\frac{1}{ST}\right)^2\left(    z\underset{u\neq v}{\mathbb{E}}\left[\left| \Delta w^l_u \mathbf{a}^{l-1}_v\right|_{2:3}^2 \right]    +(z-1)\underset{v}{\mathbb{E}}\left[\left| \bar{w}^l \mathbf{a}^{l-1}_v\right|_{2:3}^2 \right]    \right)\notag\   & + l\left(\frac{d}{D} - \frac{1}{ST}\right)(z-1) \underset{v}{\mathbb{E}}\left[\left| w^l_v \mathbf{a}^{l-1}_v\right|_{2:3}^2 \right] \tag{6.46}\end{align}
$$

 where we define 

$$
\begin{equation}    |\delta\mathbf{a}^l_t|_{2:3}^2 := (\delta\mathbf{a}^l_t)_2^2 + (\delta\mathbf{a}^l_t)_3^2 \tag{6.47}\end{equation}
$$

Inserting the definitions of $\bar{w}^l, \Delta w^l_u,\mathbf{a}^l_v$ for our circuits into this formula yields 

$$
\begin{equation}    \bar{w}^l\mathbf{a}^{l-1}_v = \begin{bmatrix}        2 & -2 & 0 & 0 \        2 & -2 & 0 & 0 \        2 & -2 & 0 & 0 \        2 & -2 & 0 & 0 \    \end{bmatrix}    \begin{bmatrix}       1.5 \ 0.5 \ (\mathbf{x}^{l-1}_t)_0 +1 \ (\mathbf{x}^{l-1}_t)_1 +1    \end{bmatrix}    =    \begin{bmatrix}        2\\2\\2\\2    \end{bmatrix} \tag{6.48}\end{equation}
$$

$$
\begin{equation}    \Rightarrow \left|\bar{w}^l \mathbf{a}^{l-1}_u \right|^2_{2:3} = 2^2 + 2^2 = 8 \tag{6.49}\end{equation}
$$

 and 

$$
\begin{equation}    \Delta w^l_u\mathbf{a}^{l-1}_v =    \begin{bmatrix}        0 & 0 & 0 & 0 \        0 & 0 & 0 & 0 \        - (\cos\theta_u - \sin\theta_u) & (\cos\theta_u - \sin\theta_u) & \cos\theta_u & -\sin\theta_u \        - (\sin\theta_u + \cos\theta_u) & (\sin\theta_u + \cos\theta_u) & \sin\theta_u & \cos\theta_u    \end{bmatrix}    \begin{bmatrix}       1.5 \ 0.5 \ (\mathbf{x}^{l-1}_v)_0 +1 \ (\mathbf{x}^{l-1}_v)_1 +1    \end{bmatrix}    =    \begin{bmatrix}        0 \ 0 \ (r_u\mathbf{x}^{l-1}_v)_0 \ (r_u\mathbf{x}^{l-1}_v)_1    \end{bmatrix}\tag{6.50} \end{equation}
$$

 where 

$$
\begin{equation}    r_u:=\begin{bmatrix}        \cos\theta_u & -\sin\theta_u \ \sin\theta_u & \cos\theta_u    \end{bmatrix} \tag{6.51}\end{equation}
$$

 and hence 

$$
\begin{align}    \left|r_u\mathbf{x}^{l-1}_v\right|^2 = \left|\mathbf{x}^{l-1}_v\right|^2 &= 1\tag{6.52}\   \tag{6.53} \Rightarrow\left|\Delta w^l_u \mathbf{a}^{l-1}_v \right|^2_{2:3} &= 1\,. \end{align}
$$

Since we didn't use $u\neq v$, the above holds equally well for $u=v$. Additionally, since directions of $\left(\bar{w}^l \mathbf{a}^{l-1}_v \right)_{2:3}$ and $\left(\Delta w^l_v \mathbf{a}^{l-1}_v \right)_{2:3}$ are uncorrelated, we can just add them up: 

$$
\begin{equation}  \tag{6.54}  \mathbb{E}\left[\left|w^l_v \mathbf{a}^{l-1}_v \right|^2_{2:3}\right] = \left|\bar{w}^l \mathbf{a}^{l-1}_v \right|^2_{2:3} + \left|\Delta w^l_v \mathbf{a}^{l-1}_v \right|^2_{2:3} = 9 \end{equation}
$$

Inserting everything finally yields 

$$
\begin{align}    \mathbb{E}\left[\left|\delta\mathbf{x}^l_t\right|^2\right]    \approx&     (l-1)T\left(\frac{d}{D}-\frac{1}{ST}\right)^2\left(    z + 8(z-1)    \right)     + 9l\left(\frac{d}{D} - \frac{1}{ST}\right)(z-1)     \quad \text{if $t$ is active}\tag{6.55} \end{align}
$$

**For inactive circuits**  
Inserting equation (6.4) into 

$$
\begin{equation} \mathbb{E}\left[\left|\delta\mathbf{x}^l_t\right|^2\right]=\mathbb{E}\left[\left|\delta\mathbf{a}^l_t\right|^2_{2:3}\right] \tag{6.56}\end{equation}
$$

 yields 

$$
\begin{equation}    \mathbb{E}\left[\left|\delta\mathbf{x}^l_t\right|^2\right] = \left(\frac{d}{D}-\frac{1}{ST}\right)z \quad \text{if $t$ is inactive}\,.\tag{6.57} \end{equation}
$$

$$

[^x4unv1coet]: Meaning they are only applied if a Boolean variable is true. 

[^bhyqx6un2i]: That post was a correction and continuation of this earlier sketch for such a framework, which was in turn based on this framework for compressing Boolean logic gates into neural networks. 

[^bdxi6843nbk]: It was assumption 4, that the weights of different circuits are uncorrelated with each other. 

[^p58wbwbxfra]: We did try that as well, and might present those results in a future post. They look overall pretty similar. The average error on the circuits just scales with a better prefactor. 

[^4to0pbubaf6]: \(T=\widetilde{\mathcal{O}}\left(\frac{D^2}{d^2}\right)\) basically means "\(T=\mathcal{O}\left(\frac{D^2}{d^2}\right)\) up to log factors". The full requirement is that \(T\log(T)\frac{d^2}{D^2}\) must be small. This result lines up well with expressions for the number of logic gates that neural networks can implement in superposition that were derived here [1, 2 and 3]. It also makes intuitive sense from an information theory perspective. The bits of information specifying the parameters of the \(T\) circuits have to fit into the parameters of the neural network.} 

[^hrwozkshot]: By "active error correction" we mean using additional layers for error clean-up. I.e. some of the large network layers are dedicated exclusively to noise reduction and do not carry out any circuit computations. One reason we don't do this is the cost of the extra layers, but another is that this only works if the circuit activations belong to a discrete set of allowed values. In our circuits this is the case for the on-indicator but not the rotated vector. So we would need to discretize the allowed angles to apply error correction to them. See also Appendix section D.4 here, for how to do error correction on Boolean variables in superposition. 

[^g9jhpe1t4qt]: Data for \(z=1\) is generated by running the network \(T\) times, once for every possible active circuit. Data for \(z=2\) and \(z=3\) is generated by running the network \(100\times T\) times, with randomly generated pairs and triples of active circuits. The sample sizes for \(z>1\) were chosen to be large enough that the worst-case absolute error did not seem to change very much any more when the sample size was increased further. It was still fluctuating a little though, so, maybe treat those points with some caution. 

[^d37bdcdzygn]: This number was chosen because it is the largest \(T\) possible for \(\frac{D}{d}=250\) and \(S=6\) in our prime-factorization-based embedding algorithm. 

[^03xao9s7xfnx]: Thanks to Gurkenglas for coming up with this evocative term. 

[^k3296xw0peq]: If the noise level gets large enough to significantly overwhelm the inactive circuits' error suppression, then we are outside the applicability of the theory. 

[^zy6n2fdahlj]: \(\mathbf{b}^l\) has no subscript \(t\) because the embedding scheme (described in Section 5.4) requires all small circuits to have the same biases, in any given layer. If this is not the case the circuits need to be re-scaled so that the biases match. 

[^5qsi5ubrntr]: In the general formalism, the small circuit weights \(w_t^l\) and biases \(\mathbf{b}^l\) can be different for each layer \(l\). However, in the specific example we are implementing here, \(w_t^l\) and \(\mathbf{b}^l\) do not depend on \(l\). 

[^xf5epem8wd8]: The "future post" mentioned in this quote from the last post is this post. The trick to modify a circuit such that assumption two holds, is to add an on-indicator. We haven't actualy described this in full generality yet, but you can hopfully see how a similar trick can be used to modify circutis other than rotations.  

[^t2ltwbk7bx8]: You might notice that for both assumption 2 and 3 to hold simultaniusly, each small network needs a negative bias.  

[^dc7z6d9bwib]: We haven't actually tried that out in practice though. 

[^34g1itvi11v]: As long as all the biases have the same sign, we can rescale the weights and biases of different circuits prior to embedding so that assumption 4 is satisfied. If some biases don't have the same sign, we can increase \(d\), and partition the circuits into different parts of \(\mathbb{R}^d\) such that the biases have the same sign in each part. This potentially comes at the cost of being able to fit in fewer circuits, because it makes \(d\) larger. \(d\) will never have to be larger than \(2\times\) the initial \(d\) though. 

[^dy6q9pwwcni]: Assumption 5 doesn't need to strictly hold for circuits of finite depth. It also doesn't strictly need to hold at any layer individually. The circuit could also have active noise 'correction' every few layers such that assumption 5 holds on average. 

[^h76nxkkgqbe]: or 'dot product' 

[^uij2d8peb5l]: This formula assumes that circuit activation vectors \(\mathbf{a}^l_t\) are all of similar magnitude. 

[^sjh2l2v0qq]: We can't neglect this term for \(u=t\), because \(|e_t^l\rangle w^l_t \mathbf{a}^{l-1}_t\) will get canceled by the \(- \mathbf{a}^l_t\), so it isn't sub-leading. 

[^238576ranyn]: This assumption holds for the conditional rotation circuits. 

[^4fi7mw35ubj]: Intuitively it doesn't seem like \(\bar{w}^l\neq 0\) should ultimately change much in the derivation, but the calculations to show this were just getting kind of cumbersome. So we figured we might as well just guess and check. 

[^efb2i0vf1gr]: What values we pick shouldn't matter so long as \(\Delta w\) satisfies \(\underset{u}{\mathbb{E}}[\Delta w_u^l]=0\).