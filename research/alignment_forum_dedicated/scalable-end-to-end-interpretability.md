---
title: "Scalable End-to-End Interpretability"
author: "jsteinhardt"
date: "2025-12-18"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/qkhwh4AdG7kXgELCD/scalable-end-to-end-interpretability"
score: 117
votes: 36
---

*This is partly a linkpost for* [*Predictive Concept Decoders*](https://transluce.org/pcd)*, and partly a response to Neel Nanda's* [*Pragmatic Vision for AI Interpretability*](https://www.lesswrong.com/posts/StENzDcD3kpfGJssR/a-pragmatic-vision-for-interpretability) *and Leo Gao's* [*Ambitious Vision for Interpretability*](https://www.lesswrong.com/posts/Hy6PX43HGgmfiTaKu/an-ambitious-vision-for-interpretability).

There is currently somewhat of a debate in the interpretability community between *pragmatic interpretability*---grounding problems in empirically measurable safety tasks---and *ambitious interpretability*----obtaining a full bottom-up understanding of neural networks.

In my mind, these both get at something important but also both miss something. What they each get right:

*    Pragmatic interpretability identifies the need to ground in actual behaviors and data to make progress, and is closer to "going for the throat" in terms of solving specific problems like unfaithfulness.
*   Ambitious interpretability correctly notes that much of what goes on in neural networks is highly compositional, and that efficient explanations will need to leverage this compositional structure. It also more directly addresses gaps between internal process and outputs on a philosophical level.

On the other hand, pragmatic interpretability tends to underweight compositionality, while ambitious interpretability feels very indirect and potentially impossible.

I think a better approach is what I'll call **scalable end-to-end interpretability**. In this approach, we train end-to-end AI assistants to do interpretability for us, in such a way that the results are still useful to humans. Specifically, we:

*   Identify an end-to-end task such that, in order to do well at the task, an agent would have to have learned something important about a neural network's internal structure. Examples would be predicting the results of interventions, or identifying neurons to ablate that turn a specified behavior on or off.
*   Use this task as a training objective to train an AI assistant on a large amount of data. This assistant is likely superhuman at the specialized task of understanding a given AI model.
*   Make the information that the assistant learned extractable to humans, either by introducing communication bottlenecks in the architecture or making explainability part of the training objective.

An example of this is our recent paper on [Predictive Concept Decoders](https://arxiv.org/abs/2512.15712). Here the end-to-end task is predicting a model's behavior from its activations. We can pretrain a system on a large number of (activation, output) pairs on web text, and then fine-tune the model to answer questions from a user. To keep these answers grounded in the representations, we introduce a **communication bottleneck**: there is an encoder that has to compress the activations to a sparse set of concepts, and a separate decoder that only sets to see this sparse set when answering questions.

This encoder-decoder assistant is both "ambitious" and "pragmatic" in the ways that matter:

*   The learned assistant is "ambitious": the AI assistant itself is incentivized to have a complete understanding of the model it is interpreting, and presumably should obtain that understanding in the limit of large-data, large-model limit.
*   The assistant's outputs are "pragmatic": answering questions that a human poses that are often empirically verifiable. (And indeed we use it so solve several concrete tasks.)
*   The communication bottleneck grounds the "pragmatic" responses in the "ambitious" understanding.

Perhaps more importantly, this approach is scalable by design---there is a natural way to input increasing amounts of compute and data into the assistant to make it better.

Some implications of the scalable end-to-end philosophy are:

*   Sparse features aren't good because they solve superposition; they are good because they are inspectable by humans.
*   In particular, instead of having sparse lists of features at a communication bottleneck, we could have more structured objects like propositional formulas, getting back the compositionality that ambitious interpretability has.
*   We should be optimizing agents to *help humans understand models*---for instance, we could ask agents to make claims that humans can test, or add an explicit reward term that tracks human performance given assistant responses (where the "human" can be approximated by another LM).

This last point is actually a generalization of the encoder-decoder bottleneck: in that case, the encoder is trying to produce concept lists that help the decoder answer questions; if we make the decoder a human, then we would be directly optimizing these concepts to help a *human* answer questions.

End-to-end interpretability feels to me like the right way to approach interpretability: it gives us grounded measures of progress, it still ties things back to latent states in a direct way, and it is trying to ensure that *some* agent (the AI assistant) has a complete understanding of the model. On a more aesthetic note, it also feels most aligned with the bitter lesson, allowing us to leverages insights from modern ML to tackle problems in model understanding.

In summary: instead of training superhuman AGI, let's train specialized, superhuman interpretability assistants!