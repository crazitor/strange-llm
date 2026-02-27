---
title: "“Features” aren’t always the true computational primitives of a model, but that might be fine anyways "
author: "LawrenceC"
date: "2026-02-02"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/iEx2KjwFse749BYsD/features-aren-t-always-the-true-computational-primitives-of"
score: 18
votes: 7
---

*Or, partly against discussion about generic “features” in mechanistic interpretability*

Probably the most debated core concept in mechanistic interpretability is that of the “feature”: common questions include “are there non-linear features, and does this mean that the linear representation hypothesis is false?”, “do SAEs recover a canonical set of features, and are SAE features ‘features’ in the first place?”, and so forth. 

But what do people mean by feature?

**Definition 1: **When asked for a definition, people in mech interp tend to define features as something like: “features are the computational primitives of the algorithm implemented by the neural network“, and point to the decompilation analogy. The obvious problem is that there might not be a unique clean algorithm that’s “truly” implemented by the algorithm; and even if so, we might not be able to find or understand it.

As a toy example of reverse engineering the computational primitives can be challenging, consider the MLP in the classic modular addition network:

*   In the original **Progress Measures for Grokking via Mechanistic Interpretability **paper, we brute forced the computation of the MLP by checking all possible inputs, and argued that this was well explained by it multiplying together the sin and cos factors represented in the embed (though we did not explain how). 
*   Later, after studying other toy neural networks, I hypothesized that the MLP was doing multiplication by “learn\[ing\]” piecewise linear approximations of (x+y)^2/4 and (x-y)^2/4 and taking their difference. 
*   Finally, in **Modular Addition Without Black-boxes**, we found that the MLP was actually approximating a trigonometric integral that integrated to the correct value:

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/136abadf93caf4b46995b0efd5369dc29f4d11c4b891b8c7.png)

As far as I know, all features that we can definitively claim are “true” computational primitives are found in toy models trained on algorithmic tasks. 

**Definition 2: **In practice, people implicitly use features to mean “salient property of the input represented by the models, where the representation can be manipulated to alter the model’s behavior in a sensible way”. For example, people often point to the various language or time features learned by SAEs when discussing potential “nonlinear features”. This is also the definition used in some of Anthropic’s more recent work, e.g. in [ “On the biology of a large language model”](https://transformer-circuits.pub/2025/attribution-graphs/biology.html). 

**Definition 3: **In many theoretical discussions, the question of what features are is entirely irrelevant. Features are just assumed to exist: for example, in Toy Model of Superposition, the features are provided in uncompressed form as part of the input, as is generally the case for follow up work. (Even in our [computation in superposition](https://arxiv.org/abs/2408.05451) work!) 

* * *

**The core claim I want to make in this piece is:** it’s meaningful to think of “features” as existing on a spectrum, starting at pure memorization, continuing through performing [case analysis](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/#tactic-ref-cases) or [equivalence partitioning](https://en.wikipedia.org/wiki/Equivalence_partitioning), and culminating in the “true” computational primitives. 

That is, sometimes it’s useful to think of features as memorizing particular input data points; sometimes it’s useful to think of features as partitioning possible inputs for case analysis, and sometimes the features really are intended to be the atomic primitives that compose the network’s computation. 

* * *

What do I mean by this? 

Consider finetuning a vision language model on the following toy classification task, based on the [classic “bleggs vs rubes” example from the Sequences](https://www.lesswrong.com/posts/4FcxgdvdQP45D6Skg/disguised-queries): 

*   There are four types of objects: blue eggs ("bleggs"), blue cubes ("blubes"), red eggs (  
    "reggs”), and red cubes (“rubes”).
*   The model is asked to answer which of each four types of object are present within an image. 
*   Of course, there are other properties that matter when determining what an object is: for example, perhaps an object is more likely to be a blegg (rather than anything else) if it has a furry surface, or it’s more likely to be a blube if its surface is slightly translucent. 

One hypothetical way the model could work is the following: at a particular layer, it represents if the object in the image is red or blue, and if it’s cube-shaped or egg-shaped. The subsequent layer then reads off the property and uses it to decide what word to output. To reduce loss, the network also represents a bunch of the other properties that are fed into the word output decision, but these are less important – the two property features capture the majority of the variance in the network’s behavior, at least across the twenty datapoints that we examined it on. 

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/f8a648a0bd55bb5e82fa52985bcb1de9ef0433903d26179b.png)

In some sense, based on the information provided, the answer to “how many features are at this layer” seems obvious: the network’s algorithm is well described as being a computer program that has two important variables: redness and cubeness. Under the [classic software (de)compilation metaphor](https://www.neelnanda.io/mechanistic-interpretability/reverse-engineering), this is recovering the actual variables used by the compiled program. Perhaps we even wrote the network weights ourselves to make this true.

But equally, you could say that the model has learned four object features: a “regg” direction, and a “rube” direction. Under a software compilation metaphor, this is closer to dividing the inputs into equivalence classes where you expect similar behavior, and testing each equivalence class. 

Finally, there’s also the trivial “memorization solution”: it is indeed perfectly valid to explain the network’s behavior in terms of its behavior on each possible input. Again returning to the software compilation metaphor: if you can verify that your decompiled program functions identically on *all *inputs via enumeration, then this is indeed sufficient evidence that you’ve successfully reverse engineered the program in a meaningful sense.  

If this toy neural network were embedded as a circuit inside a larger network, which uses additional features, the four object feature model (or even the twenty-feature memorization feature model) might be favored by SAEs for having lower reconstruction loss and higher sparsity (c.f. [Lucius’s “fat giraffe” critique of SAEs](https://www.lesswrong.com/posts/tEPHGZAb63dfq2v8n/how-useful-is-mechanistic-interpretability%234AFvjRr8GDiG6Zsuw))! (For example, the additional features could make it so the four object vectors are no longer contained within the same plane, meaning that the planar two object feature model will lose a bunch of the information.) In fact, it’s not implausible that as you increase the width of your SAE, you go from the two property feature model (a dense 2d model) to the (a sparse 4d model) and finally, at sufficient widths, a twenty feature model where each feature is a single data point (a very sparse 20d model with perfect reconstruction loss). 

I’ve heard people claim that, insofar as SAEs are doing something analogous to case analysis, they won’t be useful (again, consider [Lucius’s “fat giraffe” critique of SAEs](https://www.lesswrong.com/posts/tEPHGZAb63dfq2v8n/how-useful-is-mechanistic-interpretability%234AFvjRr8GDiG6Zsuw)). In fact, I used to make this argument myself in early 2024. In one sense, this is true: insofar as our techniques are picking up on different features than what the network is “actually” using (at least in cases where we can make a claim as to the “actual” primitives), then it’s probable that algorithms using these features will generalize differently in other situations than the network itself. 

But case analysis is useful for interpretability, just as equivalence partitioning is useful in debugging and (actual) case analysis is useful for formal verification! If you can confirm that the model’s internals behave quite differently between each of the four clusters, but are similar within each cluster, we’ve reduced the problem of testing a behavior of the model (for example, adversarial robustness) to testing each equivalence class or analyzing each case, instead of each possible example. 

In fact, even features as units of memorization can be useful; insofar as the facts actually are memorized by the network, we want to be able to talk about these features (and much real world knowledge is likely purely memorized by current, of which the clearest example may be the birth dates of celebrities). And in cases where we do have the ability to verify the network’s behavior on large classes of input examples, this might be the correct level of detail, even if there is a compact algorithm that describes the network’s behavior. 

* * *

If you’ll permit some poetry: No prophet comes from the heavens to inscribe the true features of the world onto your neural network. Modern networks are not even trained with the explicit goal of extracting any particular feature; insofar as they represent “features” of any kind, it’s because they’re useful for computations that reduce loss. 

But at the same time, as the quote goes: “[The categories were made for man, not man for the categories](https://slatestarcodex.com/2014/11/21/the-categories-were-made-for-man-not-man-for-the-categories/)”. As long as we aren’t confused about what each of us mean by “feature” in any particular case, it often makes sense to use the word feature to represent something other than the computational primitives.  

Accordingly, when discussions about features get confused, take the computational view: ask what computations neural networks implement, and what the components would be used in a compact description of the computation suitable to your purpose. When constructing a supposed counterexample to the linear representation hypothesis, or arguing against the existence of non-linear features, consider whether or not the features in your example are the only “features” that can be used to describe the behavior of the model. 

* * *

**An obligatory disclaimer: **I no longer do mechanistic interpretability research and have not been fully keeping up to date with the literature, so it’s possible something like this has already been written. I’m writing it up anyway because I’d like something to point to. This is a brief (~2.5h) attempt to exposit some of my thoughts.