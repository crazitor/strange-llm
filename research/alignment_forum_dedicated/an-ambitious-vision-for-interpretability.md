---
title: "An Ambitious Vision for Interpretability"
author: "leogao"
date: "2025-12-05"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/Hy6PX43HGgmfiTaKu/an-ambitious-vision-for-interpretability"
score: 170
votes: 67
---

The goal of ambitious mechanistic interpretability (AMI) is to fully understand how neural networks work. [While some have pivoted towards more pragmatic approaches](https://www.lesswrong.com/posts/StENzDcD3kpfGJssR/a-pragmatic-vision-for-interpretability), I think the reports of AMI’s death have been greatly exaggerated. The field of AMI has made plenty of progress towards finding increasingly simple and rigorously-faithful circuits, including [our latest work on circuit sparsity](https://arxiv.org/abs/2511.13653). There are also many exciting inroads on the core problem waiting to be explored.

**The value of understanding**
------------------------------

Why try to understand things, if we can get more immediate value from less ambitious approaches? In my opinion, there are two main reasons.

First, mechanistic understanding can make it much easier to figure out what’s actually going on, especially when it’s hard to distinguish hypotheses using external behavior (e.g if the model is scheming). 

We can liken this to going from print statement debugging to using an actual debugger. Print statement debugging often requires many experiments, because each time you gain only a few bits of information which sketch a strange, confusing, and potentially misleading picture. When you start using the debugger, you suddenly notice all at once that you’re making a lot of incorrect assumptions you didn’t even realize you were making.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/38013ffa061bf576e20ea6aabc197df506cf3e2f4a84df85.png)

A typical debugging session.

Second, since AGI will likely look very different from current models, we’d prefer to gain knowledge that applies beyond current models. This is one of the core difficulties of alignment that every alignment research agenda has to contend with.

The more you understand why your alignment approach works, the more likely it is to keep working in the future, or at least warn you before it fails. If you’re just whacking your model on the head, and it seems to work but you don’t really know why, then you really have no idea when it might suddenly stop working. If you’ve ever tried to fix broken software by toggling vaguely relevant sounding config options until it works again, you know how brittle this kind of fix can be. On the other hand, if you have a deep understanding of exactly what’s going on inside the model, you have a better sense of whether things are working for the right reasons, and which kinds of changes might break your alignment approach. And we already know that many pragmatic approaches will definitely break at some point, and are just hoping that they’ll last long enough.

AMI has good feedback loops
---------------------------

While open ended exploration is immensely valuable and disproportionately effective at producing breakthroughs, having good empirical feedback loops is also essential for the health of a field. If it’s difficult to measure how good your work is, it’s also difficult to make progress.

Thankfully, I think AMI has surprisingly good empirical feedback loops. We don’t have a watertight definition of “full understanding”, but we can measure progress in ways that we aren’t close to saturating. This isn’t so different from the state of metrics in capabilities, which has undeniably made very rapid progress, despite AGI being hard to define.

For example, I’m excited about progress on metrics based broadly on these core ideas:

*   **Feature quality**: can we show that features are human-understandable by finding explanations for when they activate, and showing that these explanations are correct by substituting model activations with explanation-simulated activations without degrading the performance of our model?
*   **Circuit faithfulness**: can we show that our circuits are truly necessary and sufficient for explaining the behavior of the model, by applying causal scrubbing (or a successor technique) without degrading the performance of our model?

None of these criteria are watertight, but this isn’t the bottleneck for AMI right now. We haven’t broken all the interp metrics we can think up; instead, the strongest metrics we can come up with give a score of precisely zero for all extant interp techniques, so we have to use weaker metrics to make progress. Therefore, progress looks like pushing the frontier of using stronger and stronger interpretability metrics. This creates an incentive problem - nobody wants to write papers that get results that seem equally as impressive as previous circuits. The solution here is social - as a field, we should value rigor in AMI papers to a much greater extent - rather than giving up entirely on rigorous ambitious interpretability.

Of course, as we make progress on these metrics, we will discover flaws in them. We will need to create new metrics, as well as stronger variants of existing metrics. But this is par for the course for a healthy research field.

The past and future of AMI
--------------------------

We’ve made a lot of progress on ambitious interpretability over the past few years, and we’re poised to make a lot more progress in the next few years. Just a few years ago, in 2022, the [IOI paper](https://arxiv.org/abs/2211.00593) found a very complex circuit for a simple model behavior. This circuit contains over two dozen entire attention heads, each consisting of 64 attention channels, and doesn’t even attempt to explain MLPs.

Today, [our circuit sparsity approach](https://arxiv.org/abs/2511.13653) finds circuits that are orders of magnitude simpler than the IOI circuit: we can explain behaviors of roughly similar complexity with only half a dozen attention channels and neurons.[^3fw88pt9smv] We also use a slightly stronger notion of circuit faithfulness: we show that we can ablate all nodes outside our circuit using mean ablations from the entire pretraining distribution rather than the task distribution. The various activations are often extremely cleanly understandable, and the resulting circuits are often simple enough to fully understand with a day’s work.

There are a lot of exciting future directions to take AMI. First, there are numerous tractable directions to build on our recent circuit sparsity work. Mean ablation on the pretraining distribution is weaker than full causal scrubbing, and randomly selected neurons or connections from the entire model are generally not nearly as interpretable as the ones in the specific circuits we isolate. If we design actually good interpretability metrics, and then hillclimb them, we could get to an interpretable GPT-1. It’s also plausible that circuit sparsity can be applied to understand only a small slice of an existing model; for example, by using bridges to tie the representations of the sparse model to the existing model on a very specific subdistribution, or by sparsifying only part of a network and using gradient routing to localize behavior.

Outside of circuit sparsity, there are a ton of other exciting directions as well. The [circuit tracing](https://transformer-circuits.pub/2025/attribution-graphs/methods.html) agenda from Anthropic is another approach to AMI that trades off some amount of rigor for scalability to frontier models. Additionally, approaches similar to [Jacobian SAEs](https://arxiv.org/abs/2502.18147) seem like they could enforce the circuit sparsity constraint without needing to train new models from scratch, and approaches like [SPD](https://arxiv.org/abs/2506.20790)/[APD](https://arxiv.org/abs/2501.14926) provide a promising alternative approach for sparsifying interactions between weights and activations. Going further away from the circuit paradigm: [SLT](https://www.lesswrong.com/posts/fovfuFdpuEwQzJu2w/neural-networks-generalize-because-of-this-one-weird-trick) could offer a learning theoretic explanation of model generalization, and [computational mechanics](https://arxiv.org/abs/2405.15943) could explain the geometry of belief representations.

As we get better at rigorously understanding small models, we might find recurring motifs inside models, and refine our algorithms to be more efficient by taking advantage of this structure. If we had the interpretable GPT-1, studying it would teach us a lot about how to create the interpretable GPT-2. Therefore, even approaches like circuit sparsity which cannot themselves scale to frontier models can still be critical on the road to AMI, because they have extreme levels of expressivity that allow us to initially impose few preconceptions on what we find.

* * *

> *“Feel the AMI”*

Fully understanding neural networks is not going to be easy. It might not even be possible. But the point of doing research is to make big bets with big payoffs, and it's hard to beat the payoff of ambitious mechinterp.

* * *

*Thanks to Adrià Garriga-Alonso, Jesse Hoogland, Sasha Hydrie, Jack Lindsey, Jake Mendel, Jacob Merizian, Neel Nanda, Asher Parker-Sartori, Lucia Quirke, and Aidan Smith for comments on drafts of this post.*

[^3fw88pt9smv]: One subtlety is that our work involves creating new models from scratch that are more interpretable, rather than interpreting existing models, which makes it somewhat harder to compare. However, I don’t think this completely invalidates the comparison, because I’d guess it’s tractable to extend our techniques to explain existing models.