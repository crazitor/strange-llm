---
title: "When should we train against a scheming monitor?"
author: "Mary Phuong"
date: "2026-01-21"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/u67JAa6FKKpQJPp3m/when-should-we-train-against-a-scheming-monitor"
score: 25
votes: 13
---

As we develop new techniques for detecting deceptive alignment, ranging from action monitoring to Chain-of-Thought (CoT) or activations monitoring, we face a dilemma: once we detect scheming behaviour or intent, should we use that signal to "train the scheming out"?

On the one hand, leaving known misaligned behaviour / intent in the model is not marginally informative and possibly unsafe. On the other hand, training against a monitor might not actually fix the model's underlying motivations; it might simply provide selection pressure that favours more sophisticated, less detectable forms of deception.

This post outlines a simple framework formalising when the generalisation benefit of training outweighs the selection risk of creating a schemer. I assume that the choice is between training and not training on the incriminating examples, e.g. we cannot apply the updates in a more targeted way, and we don’t have the option to just look at the evidence and use it to make changes to the training process.[^ig3b1c0nyg]

### **The selection intuition**

When we train a model to satisfy a specific criterion, we can view the process as starting with a prior distribution over models we might get (determined by the architecture, initialisation, base model pre-training, etc) and then restricting that set to only the models that satisfy the training criterion.

In our case, suppose we have a scheming monitor $\mu$, and consider a simplified hypothesis space where the potential models we might end up with fall into three categories:

1.  **Aligned (**$M_A$**):** The model behaves like we want it to and is not deceptive.
2.  **Weak schemer (**$M_W$**):** The model is misaligned but schemes in ways that our monitoring detects (at least some of the time).
3.  **Strong schemer (**$M_S$**):** The model is misaligned and schemes in ways that evade our monitoring.

Denote their respective prior probabilities $P(M_A), P(M_W),$ and $P(M_S)$.

Now, suppose we apply training pressure $T_\mu$ that penalises any model caught behaving in a misaligned or deceptive way by the monitor $\mu$. Effectively, we are pruning $M_W$ from our posterior. If we assume the training procedure is a perfect filter for $M_W$ but does nothing else, the new posterior for a strong schemer would be

$$P(M\_S | T\_\\mu) = \\frac{P(M\_S)}{P(M\_A) + P(M_S)}.$$

Intuitively: we are assuming that the training does not favour either the aligned models or the strong schemers, and so the chance of getting one or the other is proportional to the prior.

Under this formalisation, training is a double-edged sword: it increases the probability of getting an aligned model, but it *also* increases the absolute probability of getting a strong schemer. From an x-risk perspective, this means we should approximately never train against scheming monitors.

### **Modelling generalisation: the **$R$ **coefficient**

However, the above formalisation leaves out a key hope — what if the training generalises? What if training the model on a broad enough distribution makes it more likely we end up with an aligned model rather than a schemer?

Let's define $Q(T_\mu)$ as the ratio of aligned models to strong schemers after training against the monitor $\mu$:

$$Q(T_\\mu) = \\frac{P(M\_A | T\_\\mu)}{P(M\_S | T\_\\mu)}.$$

Previously we assumed that $Q$ stays the same before and after training. Now, let’s define the generalisation coefficient $R(T_\mu)$:

$$R(T_\\mu) = \\frac{Q(T_\\mu)}{Q(\\text{no training})}$$

*   If  $R(T_\mu) > 1$, the training pressure favours aligned models (e.g. maybe we are training against an activation monitor and activations are hard to game).
*   If  $R(T_\mu) = 1$, there is no generalisation (the good-to-bad ratio remains the same as in the prior).
*   If $R(T_\mu) < 1$, the training pressure favours scheming (e.g. maybe the monitor is hackable and reward hacking incentivises scheming).

### **When should we train against a scheming monitor?**

When the generalisation coefficient $R > 1$, the training favours aligned models compared to schemers, but *only in relative terms*. In absolute terms, we are still selecting for the union$\{M_A, M_S\}$ (aligned or strong scheming). For training to be worth it, the generalisation effect must be strong enough to overcome this selection pressure.

Specifically, it is easy to derive that the absolute probability of a strong schemer decreases or stays the same, $P(M_S | T_\mu) \leq P(M_S)$, if and only if:

$$R \\geq 1 + \\frac{P(M\_W)}{P(M\_A)}.$$

Intuitively, the training prunes weak schemers from the hypothesis space, which frees up $P(M_W)$ in the probability distribution. To ensure we are actually improving safety, the generalisation coefficient $R$ must amplify the aligned models $M_A$ enough to take up *all* of the newly available probability mass. Otherwise some of the initialisations that would have ended up as weak schemers end up as strong schemers instead.

### **Example application: should we train away scheming thoughts?**

To use the formula above, we need to make some assumptions and run some evals:

*   First, we need access to multiple model checkpoints trained roughly the same way. Suppose we can get such checkpoints, e.g. unsuccessful release candidates.
*   For each checkpoint, we run it on a batch of situations from deployment and use a scheming thought monitor to classify it as either a weak schemer or not a weak schemer. Suppose we estimate $P(M_W) \approx 0.6$.
*   We don’t know whether the remaining checkpoints are aligned or strong schemers. But let’s say that at the models’ capability levels, we are willing to assume that strong scheming is less than 10% likely, so $P(M_A) \geq 0.3$.

So overall we might think it’s fine to train against the scheming thought monitor if

$$R(T_\\mu) \\geq 1 + \\frac{0.6}{0.3} = 3.$$

But we have little evidence[^5emqawmm1bv] to think our training would be that robust, so we abstain from training.

### **The more monitoring positives, the more cautious we should be about training**

This follows directly from the formula, but is still counterintuitive. After all, if we have many examples of unwanted behaviour, isn’t the training going to be more effective at specifying what we mean by aligned / non-deceptive? Yes, but we are also indirectly specifying in more detail what failures are detectable. It also matters a ton where the scheming examples come from. If they all come from a single checkpoint, plausibly this all works out in favour of alignment. But if the scheming examples come from many different checkpoints, i.e. $P(M_W)$ is high, then chances are some of them would turn into strong schemers under training pressure, even taking into account sample diversity.

### **Considerations not captured by the formula**

Even if we suspect $R \geq 1 + \frac{P(M_W)}{P(M_A)}$, we might still refrain from training against the monitor if the monitoring signal could be used for other, more risk-reducing interventions (the risk reduction would need to offset the increased risk of deploying a strong schemer though):

*   **Natural scheming demos:** For global coordination purposes (or even for justifying mitigations within a lab), it may be helpful to have a constant supply of schemers ready for demonstrating the risk, even if these are schemers that we could straightforwardly train away.
*   **Facilitating scheming propensity estimation:** We cannot estimate models' propensity for strong scheming. But if we think that it’s correlated with propensity for weak scheming, then we may want to keep weak schemers around. (For example, we might think that future models' propensity for opaque scheming is correlated with current models' propensity for transparent scheming.)

(A non-reason to refrain from training:

*   **Preventing harm via control instead:** Refraining from training when  $R \geq 1 + \frac{P(M_W)}{P(M_A)}$ and using the monitor for control instead does *not* reduce risk. This is because by assumption the chance of a strong schemer is lower if we do train, and the monitor would only catch weak schemers which would counterfactually not even exist.)

Conversely, we might choose to train against a monitor even if we suspect $R < 1 + \frac{P(M_W)}{P(M_A)}$ for reasons such as:

*   **Sufficient control:** We are okay deploying a more deceptive / strategic schemer because we have confidence the deployment is controlled, and we just want the model to attack less. (For example, we may not mind that our untrusted monitors are scheming harder, as long as they can’t tell honeypots from real deployment and this forces them to not collude very often.)
*   **The increased chance of alignment is worth it:** For example, we need to imminently hand everything over to the AI. In such a position even weak schemers would constitute an x-risk so we may want to weed out as many as we can.

### **Conclusion**

Training against a scheming monitor prunes weak schemers, by default making both aligned models *and* strong schemers more likely. The higher the frequency (across checkpoints) of detectable scheming, the larger the selection pressure towards both alignment and strong scheming. Unless the training sufficiently favours aligned models over strong schemers, it is likely making things worse.

*Many thanks to David Lindner, Roland Zimmermann, Zac Kenton, Rif Saurous, and Seb Farquhar for helpful feedback. Any remaining mistakes are mine.*

[^ig3b1c0nyg]: This would ideally be the first thing we do, but for the purposes of this post suppose we've already done that and/or we are running out of time. 

[^5emqawmm1bv]: How might we estimate R? In principle, we could build a bunch of monitors we think are uncorrelated, train against some and eval against others. This could give us some idea, but we'd still have no guarantee that the generalisation we see in that setting is representative of generalisation to distributions we didn't measure.Ultimately, it's fair to say that this framework reduces a vibe-check about "should we train against this monitor?" to a vibe-check about "how well will this generalise?" (which I claim is progress).