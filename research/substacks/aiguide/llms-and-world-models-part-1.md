---
title: "LLMs and World Models, Part 1"
author: "Melanie Mitchell"
date: ""
source: "substack_aiguide"
url: "https://aiguide.substack.com/p/llms-and-world-models-part-1"
---

This is part 1 of a two-part post on LLMs and “world models.” Part 2 is [here](https://aiguide.substack.com/p/llms-and-world-models-part-2).

#### **AI Brittleness in the Before Times**

In the long-ago times, before large-scale generative AI came on the scene, machine-learning systems had some problems: often they didn’t learn the general concepts we were trying to teach them, but rather solved problems using “shortcuts” or “surface heuristics.” To give [one stark example](https://www.sciencedirect.com/science/article/pii/S0022202X18322930), some researchers tried to train a deep neural network to classify skin lesions in photos like the one below as “benign” or “malignant.”

[](https://substackcdn.com/image/fetch/$s_!pjr7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe8b13222-83e1-452e-8fce-f88263ebc6a6_642x648.png)

While this network performed well on the kinds of photos it was trained on, the researchers noticed a problem:

“[T]he algorithm appeared more likely to interpret images with rulers as malignant. Why? In our dataset, images with rulers were more likely to be malignant; thus, the algorithm inadvertently ‘learned’ that rulers are malignant.”

In short, the network learned a useful heuristic: if there are features corresponding to a ruler in the image, the answer is “malignant.” The network didn’t understand what a lesion is, or what motivated the researchers to train it, or why rulers might be seen in particular images, or anything else about the world; it learned only to associate certain image features with the “malignant” class, which worked well on the data it was tested on but of course would generalize poorly.

Such heuristic “shortcuts” weren’t limited to visual data. In 2019, [one group reported](https://aclanthology.org/P19-1334) on using a neural language model to determine whether one sentence logically implies another. The model performed very well on a dataset designed to test this general ability. But it turned out that the model’s high performance relied on superficial syntactic properties such as how much the words in one sentence overlapped those in the second sentence. When the network was given sentences for which it could not take advantage of this heuristic, its performance decreased dramatically.

[Another group wrote about](http://proceedings.mlr.press/v70/kansky17a/kansky17a.pdf) similar brittleness in a deep-reinforcement-learning system that had successfully learned to play the Atari video game Breakout. The system was trained by being given video frames from the game and then choosing actions—moving a paddle horizontally to bat a ball in order to hit exploding bricks. While the trained system seemed to be highly skilled at the version of the game it had been trained on, the researchers showed that small changes in the game set-up, such as moving the paddle’s vertical position by a few pixels, caused the trained network’s performance to plummet, even though such changes would likely have no effect on a human that had learned to play the game. It seems that the original system had not learned the abstract notions of “paddle,” “ball,” or “bricks” but was using heuristics—patterns of pixel configurations specific to the original game—to decide on actions.

In all of these cases, the machine-learning system had learned to perform its task using heuristics specific to its training data rather than the kind of abstract, causal understanding the human trainers were trying to teach it.

Of course, the word “understanding” is ill-defined, but one thing that seems key to human understanding is having mental “world models”: compressed, simulatable models of how aspects of the world work, ones that capture causal structure and can yield predictions.

#### **Debates Over Emergent World Models in LLMs**

Now we’re in the era of large language models (LLMs), huge neural networks pretrained on enormous amounts of human-generated text data, that seem to perform much better than the smaller, less-well-trained, and brittle machine-learning systems of the “before times”. But there’s a fiery debate in the AI community on how these systems achieve their high performance. Have they basically memorized their training data and then retrieve it (in some “approximate” way) to solve new problems? Have they learned much more numerous and detailed, yet still brittle, heuristic shortcuts? Or do they have something more like the robust “world models” that humans seem to use to understand and act in the world?

OpenAI co-founder Ilya Sutskever [asserts](https://www.youtube.com/watch?v=ZZ0atq2yYJw&t=1262s) that these systems have learned robust world models:

“When we train a large neural network to accurately predict the next word in lots of different texts...it is learning a world model.... This text is actually a projection of the world.... What the neural network is learning is more and more aspects of the world, of people, of the human conditions, their hopes, dreams, and motivations...the neural network learns a compressed, abstract, usable representation of that.”

While many would concur with Sutskever, other prominent AI researchers vehemently disagree, arguing that the success of LLMs is more attributable to “approximate retrieval” from their vast memorized store of training data. For example, here’s [ASU’s Subbarao Kambhampati](https://x.com/rao2z/status/1687839414305845248):

[](https://substackcdn.com/image/fetch/$s_!uCoP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d87c66c-3c2a-4e79-be2b-3722962cc091_1326x506.png)

And here’s [Meta’s Yann LeCun](https://x.com/ylecun/status/1713228046033936717):

[](https://substackcdn.com/image/fetch/$s_!tf7A!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d8d5a32-6e7b-4728-a79a-9be9e0c955f4_1272x254.png)

LeCun, along with philosopher Jacob Browning, went further, [asserting that](https://www.noemamag.com/ai-and-the-limits-of-language/), “A system trained on language alone will never approximate human intelligence, even if trained from now until the heat death of the universe.”

An illustration of the split in the AI community is the results of a [2022 survey of NLP researchers](https://arxiv.org/abs/2208.12852), which asked respondents to agree or disagree with the following statement: “Some generative models trained only on text, given enough data and computational resources, could understand natural language in some non-trivial sense.” Notably, the responses were split almost 50-50:

[](https://substackcdn.com/image/fetch/$s_!pzL6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd4599697-04d3-4586-ae7e-1ae5fc395cbb_940x536.png)

So, for those who have claimed that, by virtue of their extensive training on human language, LLMs have developed emergent world models, what is the evidence that convinces them? Before diving into that story, let’s first explore what the term “world model” might mean, and why such a model would be useful for a human or an AI system.

#### **What Is a World Model and What Is It Good For?**

The term “world model” has become a buzzword in AI circles, but it doesn’t have a single, agreed-upon, definition. Here are a few definitions of a world model from the AI literature.

“[I]nternal representations that simulate aspects of the external world.”[1](https://aiguide.substack.com/p/llms-and-world-models-part-1#footnote-1-157080552)

“[R]epresentations which preserve the causal structure of the environment as far as is necessitated by the tasks an agent needs to perform.”[2](https://aiguide.substack.com/p/llms-and-world-models-part-1#footnote-2-157080552)

“[S]tructure-preserving, behaviorally efficacious representations of the entities, relations, and processes in the real world. These representations capture, at an abstract level, their counterpart real-world processes (which typically involve causal relations), in algorithmically efficient forms, to support relevant behaviors.”[3](https://aiguide.substack.com/p/llms-and-world-models-part-1#footnote-3-157080552)

These informal definitions[4](https://aiguide.substack.com/p/llms-and-world-models-part-1#footnote-4-157080552) emphasize that world models exist in an organism’s brain or in, say, a LLM’s neural network, that they capture something about the world that is _causal_ and _abstract_(or _compressed_) rather than simply based on large sets of statistical associations; they don’t require too much work for the agent to use (“algorithmically efficient”) and are relevant to tasks the agent performs.

In my 2019 book, _Artificial Intelligence: A Guide for Thinking Humans_(p. 236), I gave the following photo as an example of how humans’ models of the world—including intuitive models of physics, biology, and psychology—enable us to very quickly make sense of this complex situation (one that a human driver or self-driving car might encounter), to understand _why_ the people and the dog are behaving in certain ways—that is, what _causes_ their behavior _—_ to guess the relationships among them, to predict what will likely happen next, to plan what one would do as a driver encountering this situation, and to answer counterfactual questions, such as “how would the photo change if the dog belonged to the man” or “what would happen if a driver approaching the crosswalk loudly honked the horn?”

[](https://substackcdn.com/image/fetch/$s_!5G3V!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ba556df-8f64-417d-9d1e-7a19a914732d_4416x3312.jpeg)

It’s important to note that our world models don’t just exist for the real world; they can also be formed and used to reason about imaginary worlds, such as those created in science fiction or fantasy literature.

#### **A Taxonomy of Models**

MIT Professor Jacob Andreas [wrote ](https://lingo.csail.mit.edu/blog/world_models/)an insightful blog post proposing a spectrum of different types of models that might count as “world models,” ordered by the types of questions such models could answer.

The weakest model would be a **static look-up table** —that is, a memorized answer to a fixed set of queries. Obviously, such a model, if it even warrants the term, would not be able to generalize in any way beyond its stored data.

Next might be a **map** , such as this 2D map of the solar system (photo credit: NASA):

[](https://substackcdn.com/image/fetch/$s_!Wf_4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F208a99a5-e136-458f-b76e-1f99b230f882_1728x1296.jpeg)

A map is a model that can help a user easily answer queries like “which planet is closest to the Sun?” or “which is the largest planet?” (of course, answering these queries requires some additional perceptual/cognitive work by the user). But it can’t help answer questions like “if Mercury and Earth are aligned at noon GMT today, what will their relative positions be at noon GMT tomorrow?”

To help answer questions that involve dynamics, one could use an **orrery** , the next model on Andreas’ spectrum, which has moving parts to allow the user to easily determine relative positions of the planets at different points in their orbits. Here’s what an orrery [looks like](https://commons.wikimedia.org/wiki/File:Orrery_designed_by_William_Pearson,_made_by_Robert_Fidler,1813-1822.jpg):

[](https://substackcdn.com/image/fetch/$s_!swYx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5aa4eaa-f674-4c22-8146-bd69bc418594_1536x1110.jpeg)

However, an orrery isn’t a powerful enough model to answer many kinds of queries, such as “how long does it take for light to reach Earth from the Sun” or counterfactuals like “how would Earth’s orbit change if the Sun’s mass were increased by five percent?”

The final model in Andreas’ spectrum is a **simulator**. Continuing with the solar system example, a detailed gravitational simulator, which incorporates causal forces, can help us better predict the future and answer certain kinds of counterfactual questions about the system. This is the kind of mental model we humans (presumably) use when reasoning about the “woman on a cell phone” photo above. 

Of course, the precision with which these different models can answer queries depends on many details of the models. Moreover, these models are _tools for a user_ —they are useful only if there is a user who has the perceptual and cognitive capabilities needed for using them. This brings up the question of what mechanism plays the role of “user” for the world models internal to our brains (or our machines)—a fascinating (and still ill-understood) scientific conundrum.

Of the many claims for LLMs developing world models, the ones most like maps are the kinds of _embedding spaces_ formed by simple co-occurrence of words, as in the spatial/temporal relationships seen in [Word2Vec-like spaces](https://proceedings.neurips.cc/paper/2013/file/9aa42b31882ec039965f3c4923ce901b-Paper.pdf) and as a result of [training on place-name datasets](https://arxiv.org/abs/2310.02207). “Situation models”—that is, the ability of LLMs to [track who is doing what in story texts](https://arxiv.org/abs/2106.00737)—might be classified as orrery-like models; they track some dynamics but don’t represent causal knowledge about the wider world. To my knowledge there is not much evidence that LLMs can capture detailed causal simulation-like models.

In short, Andreas points out that in evaluating whether an LLM has an implicit world model, it needs to be made clear what kinds of questions this model can help users to answer, and how much cognitive or computational work a user would need to do to use the model to answer them.

Clearly it would be very useful for AI systems to have the kind of internal models that enable reasoning about the world in the way I described for the “woman on a cell phone” photo above. Indeed, many people have claimed that without such internal models, AI systems can never attain human-level intelligence. Ilya Sutskever, in his claim that LLMs have learned “ a compressed, abstract, usable representation of” aspects of the world, is asserting that LLMs, by virtue of their training on next-word completion, already have this kind of internal world model. But what is the evidence for this? That will be the topic of [Part 2](https://aiguide.substack.com/p/llms-and-world-models-part-2) of this post.

[1](https://aiguide.substack.com/p/llms-and-world-models-part-1#footnote-anchor-1-157080552)

<https://arxiv.org/abs/2401.03910>

[2](https://aiguide.substack.com/p/llms-and-world-models-part-1#footnote-anchor-2-157080552)

https://arxiv.org/abs/2412.11867

[3](https://aiguide.substack.com/p/llms-and-world-models-part-1#footnote-anchor-3-157080552)

https://lapaul.org/papers/From%20task%20structures%20to%20world%20models.pdf

[4](https://aiguide.substack.com/p/llms-and-world-models-part-1#footnote-anchor-4-157080552)

The field of reinforcement-learning uses a more formal definition: a world model is a machine-learning system (typically a neural network) that, given the agent’s current state and action, computes a representation that can be used to predict the next state (or a probability distribution over possible next states). See <https://arxiv.org/abs/1803.10122> and https://www.linkedin.com/posts/yann-lecun_lots-of-confusion-about-what-a-world-model-activity-7165738293223931904-vdgR/.
