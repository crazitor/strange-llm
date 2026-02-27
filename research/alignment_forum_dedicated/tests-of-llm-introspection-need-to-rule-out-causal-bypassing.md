---
title: "Tests of LLM introspection need to rule out causal bypassing"
author: "Adam Morris"
date: "2025-11-28"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/LD8yupMtE6btAE3R9/tests-of-llm-introspection-need-to-rule-out-causal-bypassing"
score: 49
votes: 19
---

*This point has been floating around implicitly in various papers (e.g.,* [*Betley et al.*](https://arxiv.org/abs/2501.11120)*,* [*Plunkett et al.*](https://arxiv.org/abs/2505.17120)*,* [*Lindsey*](https://transformer-circuits.pub/2025/introspection/index.html)*), but we haven’t seen it named explicitly. We think it’s important, so we’re describing it here.*

There’s been growing interest in testing whether LLMs can introspect on their internal states or processes. Like [Lindsey](https://transformer-circuits.pub/2025/introspection/index.html), we take “introspection” to mean that a model can report on its internal states in a way that satisfies certain intuitive properties (e.g., the model’s self-reports are accurate and not just inferences made by observing its own outputs). In this post, we focus on the property that Lindsey calls “grounding”. It can’t just be that the model happens to know true facts about itself; genuine introspection must *causally depend* *on* (i.e., be “grounded” in) the internal state or process that it describes. In other words, a model must report that it possesses State X or uses Algorithm Y *because* it actually has State X or uses Algorithm Y.[^-2KPpptEWcNXbMdxHx-1] We focus on this criterion because it is relevant if we want to leverage LLM introspection for AI safety; self-reports that are causally dependent on the internal states they describe are more likely to retain their accuracy in novel, out-of-distribution contexts.

**There’s a tricky, widespread complication that arises when trying to establish that a model’s reports about an internal state are causally dependent on that state**—a complication which researchers are aware of, but haven’t described at length. The basic method for establishing causal dependence is to intervene on the internal state and test whether changing that state (or creating a novel state) changes the model’s report about the state. The desired causal diagram looks like this:

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/a61a45825020052a4861118810b430a6509048f11c6bd81e.png)

Different papers have implemented this procedure in different ways. [Betley et al.](https://arxiv.org/abs/2501.11120) and [Plunkett et al.](https://arxiv.org/abs/2505.17120) intervened on the model’s internal state through supervised fine-tuning—fine-tuning the model to have, e.g., different risk tolerances or to use different decision-making algorithms—and then asking the model to report its new tendencies. [Lindsey](https://transformer-circuits.pub/2025/introspection/index.html) intervened on the model through concept injection, then asked it to report whether it had been injected with a concept (and what concept). Others have intervened by manipulating the model’s prompt in precise ways—e.g., adding a cue that alters its behavior, and testing whether the model reports using the cue (as in [Chen et al.](https://arxiv.org/abs/2505.05410)).[^-2KPpptEWcNXbMdxHx-2][^-2KPpptEWcNXbMdxHx-3]

In all of these cases (and in any experiment with this structure), the complication is this: **The intervention may cause the model to accurately report its internal state via a causal path that is not routed through the state itself.** The causal diagram might actually look like this:

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/3aa7c09e108b24d8f38f2d6dc1739bc53a25cb0f38c379b2.png)

Here’s some concrete examples of what this might look like.

*   Fine-tuning the model to be risk-seeking may also instill cached, static knowledge that it is risk-seeking—knowledge which is not causally dependent on the actual dynamic existence or operation of its risk preferences. For example, if this were true, then if the model magically stopped being risk-seeking, it would still have cached knowledge of the form “I am risk-seeking” and it would still report that.
*   Including a hint in the model’s prompt may lead the model to incorporate the hint in its internal reasoning, and it may simultaneously cause the model to mention the hint in its responses or chain-of-thought, without the former having caused the latter.
*   Injecting a concept vector encoding “bread” may cause the model to report that it is now thinking about bread, not because it is metacognitively aware of the influence of the injection on its internal states, but because the concept injection directly causes it to talk about bread.

We refer to this general phenomenon as “**causal bypassing**”: The intervention causes the model to accurately report the modified internal state in a way that bypasses dependence on the state itself.

This worry is not new; authors of past papers on LLM introspection have been aware of this possibility. For instance, [Betley et al.](https://arxiv.org/abs/2501.11120) wrote: “It’s unclear whether the correlation \[between the model’s reports and its actual internal states\] comes about through a direct causal relationship (a kind of introspection performed by the model at run-time) or a common cause (two different effects of the same training data).” The contribution of this post is to describe this issue explicitly, note that it is a general issue affecting a broad set of methods that test for introspection, and give it a name.

To our knowledge, the only experiment that effectively rules out causal bypassing is the thought injection experiment by [Lindsey](https://transformer-circuits.pub/2025/introspection/index.html). Lindsey injected Claude with concept vectors (e.g., an “all caps” activation vector derived from subtracting uppercase text from lowercase text) and tested whether Claude could report whether it had received a concept injection (and what the concept was). This experiment effectively rules out causal bypassing because the injected vector has nothing itself to do with the *concept of being injected*, so this intervention seems unlikely to directly cause the model to report *the fact that it received an injection*. In other words, there is no plausible mechanism for the bottom arrow in the causal bypassing diagram; we see no way that injecting an “all caps” activation vector could cause the model to report that it received a concept injection, without causally routing through the modified internal state itself. Note, though, that this logic only applies to the model identifying that it received an injection; the fact that the model can then report *which* concept was injected is highly susceptible to causal bypassing concerns, and hence much less informative.[^-2KPpptEWcNXbMdxHx-4] \[EDIT: Even the "did you receive an injection?" part of Lindsey's experiment might not avoid the causal bypassing problem; see Derek's comment [here](https://www.lesswrong.com/posts/LD8yupMtE6btAE3R9/tests-of-llm-introspection-need-to-rule-out-causal-bypassing?commentId=PgQo6AuJuwhEcbccn).\]

Lindsey’s experiment illustrates the only general approach we know of right now for avoiding the causal bypassing problem: Find an intervention that (a) modifies (or creates) an internal state in the model, but that (b) cannot plausibly lead to accurate self-reports about that internal state except by routing through the state itself. Put another way, tests for genuine introspection are ultimately limited by the precision of our interventions. If we could surgically manipulate some aspect of a model’s internal state in a way that was guaranteed to not impact any other aspect of the model’s processing (except impacts that are causally downstream of the manipulated state), then we could provide ironclad evidence for introspective capabilities. Without that guaranteed precision, we are forced to rely on intuitive notions of whether an intervention could plausibly be executing a causal bypass or not.

Avoiding the causal bypassing problem when testing for LLM introspection is important because grounded introspection—i.e., self-reports that causally depend on the internal state they’re describing—may be uniquely valuable for AI safety, relative to other kinds of self-reporting abilities. Self-reporting abilities that rely on static self-knowledge (e.g., cached knowledge that “I am risk-seeking”) may fail in novel, out-of-distribution contexts; training cannot provide static self-knowledge about every possible context. By contrast, the capacity of a model to provide grounded descriptions of its internal states or processes by introspecting directly upon them could, in principle, generalize to the out-of-distribution contexts that are particularly relevant for AI safety (or AI welfare) concerns.

[^-2KPpptEWcNXbMdxHx-1]:  

[^-2KPpptEWcNXbMdxHx-2]:  

[^-2KPpptEWcNXbMdxHx-3]:  

[^-2KPpptEWcNXbMdxHx-4]: