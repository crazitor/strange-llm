---
title: "Did OpenAI Just Solve Abstract Reasoning?"
author: "Melanie Mitchell"
date: ""
source: "substack_aiguide"
url: "https://aiguide.substack.com/p/did-openai-just-solve-abstract-reasoning"
---

Yesterday OpenAI announced some very impressive results from their not-yet-released o3 model. According to the announcement, o3 has made enormous progress over its predecessors on several “reasoning” benchmarks, in particular, two quite difficult ones: [Frontier Math](https://epoch.ai/frontiermath), a benchmark containing hundreds of unpublished math problems that are known to be hard even for human math whizzes, and the [Abstraction and Reasoning Corpus](https://github.com/fchollet/ARC-AGI) (ARC), a collection of concept-induction tasks which I’ve written about [here](https://aiguide.substack.com/p/why-the-abstraction-and-reasoning), [here](https://aiguide.substack.com/p/on-evaluating-understanding-and-generalization), and [here](https://aiguide.substack.com/p/on-the-arc-agi-1-million-reasoning).

  
In this post I’ll discuss the o3 results on ARC. If you’re interested in AI and active on social media, you’ve likely already heard about these results, but I’ll try to add more context and my own thoughts here.

#### **What is ARC?**

ARC was created by computer scientist François Chollet as a [“measure of intelligence”](https://arxiv.org/abs/1911.01547) for both humans and machines. ARC tasks, like the one below,[1](https://aiguide.substack.com/p/did-openai-just-solve-abstract-reasoning#footnote-1-153510923) challenge a solver to figure out the common abstract transformation rule from a small number of demonstrations of transformations between grids, and to apply that rule to a new grid.

[](https://substackcdn.com/image/fetch/$s_!WHPx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82d6a80c-4bcf-46b9-a657-d33288368ef8_1014x770.png)

I’ll give the answer at the end of this post. 

While it is natural for humans to use vision to process these grids, Chollet did not see ARC as a visual domain but more as a two-dimensional domain for abstract pattern recognition and reasoning.

Chollet manually created 1,000 ARC tasks, which are now split into four sets: 400 “training” tasks, 400 “public evaluation” tasks, 100 “semi-private evaluation” tasks (more on this in a bit), and 100 tasks in a private test set. Researchers creating programs to solve ARC tasks are encouraged to use the training tasks to get an idea of what kinds of concepts are required in the domain, and to use the public evaluation tasks to assess how well their programs are doing. The training tasks are meant to be fairly easy, and the evaluation tasks somewhat harder. Once a program is completed, it can be submitted (during a competition period) to be tested on the even harder tasks in the private test set.

As of earlier this year, a few ARC competitions had been held, and the winning systems’ performance was at most around 35% accuracy on the private test set. Average human performance had been estimated earlier (using parts of the training set) at about 85%.

#### **Assumptions Underlying ARC**

As regular readers of this newsletter will know, I really like the ARC domain as a challenge for AI systems. In my view, here are the assumptions (from Chollet’s original paper) that make ARC an interesting and useful benchmark:  
  
(1) The solver should not need extensive (or really any) training on the domain itself. The only prior knowledge requirements are “core knowledge” concepts—basic understanding of objects, shapes and symmetries, spatial relationships, boundaries, etc.

  
(2) For each task, the solver needs to see only a few (one to four) demonstrations of grid transformations in order to figure out what the abstract rule is, and to apply it to a new grid.  
  
In other words, the solver should not need much specific “training”, either on the domain itself or on each specific task.   
  
(3) Chollet also mentions that we might want intelligent systems to minimize their computational resource consumption when solving a new task. This seems important to me.

#### **The ARC Prize**

In June, 2024, Chollet and his collaborator Mike Knoop launched a new ARC competition called the [“ARC Prize”](https://arcprize.org/). The grand prize now stands at $600,000 for a program that achieves 85% or higher accuracy on the private test set.  
  
In addition, to be eligible for the prize, the winner’s program must run on the test set in at most 12 hours on the competition’s servers, with no internet access, and the code has to be open-sourced at the end of the competition.

For the competition, the benchmark was rebranded as “ARC-AGI”—this was purportedly to distinguish the benchmark from other, unrelated, benchmarks named ARC—but the name does give the impression that the organizers are equating solving ARC with “artifical general intelligence”.[2](https://aiguide.substack.com/p/did-openai-just-solve-abstract-reasoning#footnote-2-153510923) Chollet has [pushed back](https://arcprize.org/blog/oai-o3-pub-breakthrough) on this association: “ARC-AGI is not an acid test for AGI…It’s a research tool designed to focus attention on the most challenging unsolved problems in AI.”

It turned out that many people wanted to try commercial LLMs like GPT-4o on these problems. However, this kind of system has to be accessed through OpenAI’s (or another company’s) “API” (an internet-based interface), but the organizers of course did not want the tasks on the private test set problems to be made available—possibly for training models—to such companies. So, they made an additional “semi-private” evaluation set available for testing such systems, and created a separate leaderboard for such submissions.

#### **2024 ARC Prize Winners**

While no program has yet won the ARC-AGI grand prize, substantial progress was made in 2024 on test-set accuracy, which rose to about 55%. The competition organizers wrote a [paper](https://arxiv.org/abs/2412.04604) summarizing the competition and how the winning programs worked. All of them used LLMs in some way as part of their ARC solver. Basically, there were three strategies that were used (sometimes individually, sometimes all three together):

(1) At training time, augment the ARC training set in order to get more training data to fine-tune a pre-trained LLM on the ARC domain.

(2) At test (inference) time, to solve a task, augment the task’s demonstrations to fine-tune a LLM on that specific task.

(3) At test (inference) time, use an LLM to generate a large number of candidate solutions, each of which is either a directly-generated answer grid, or is a generated program (e.g., in Python) that will generate an answer grid. The candidate solutions are then evaluated by voting or other means to determine the best two candidates (ARC-AGI allows two guesses per task).

I was surprised that such methods could do so well. But also a bit disappointed: each of these methods went against the assumptions that I described above that, for me at least, made ARC so attractive:

(1) _The solver should not need extensive (or really any) training on the domain itself._ This was negated by the need for extensive training on the domain via a large (augmented) set of training tasks.

(2) _For each task, the solver needs to see only a few (one to four) examples (demonstrations) of grid transformations in order to figure out what the abstract rule is, and to apply it to a new grid._ This was negated by the need to augment the demonstrations in order to fine-tune the LLM specifically to solve the given task.

(3 _) We want intelligent systems to minimize their computational resource consumption when solving a new task._ This was negated both by the above-mentioned data augmentations and by the need to generate large numbers of candidate solutions at inference time.

One might call the 2024 results “the bitter lesson of ARC,” recalling Rich Sutton’s famous [article](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) asserting that the best way to get to general AI is not to build in any prior knowledge or structure into our systems, but to rely on large amounts of training data and computation.

#### **OpenAI’s o3 Leaps to the Top of the (Semi-Private) Leaderboard**

On Friday, December 20, OpenAI announced its o3 model, the successor to its earlier o1 system that is designed for “advanced reasoning”.[3](https://aiguide.substack.com/p/did-openai-just-solve-abstract-reasoning#footnote-3-153510923)

Note that o3 is not eligible for testing on ARC’s fully private test set, since using it requires access to the internet, namely, OpenAI’s API; it cannot be run on the competition’s servers.

The o3 model[4](https://aiguide.substack.com/p/did-openai-just-solve-abstract-reasoning#footnote-4-153510923) was tested on ARC in two modes: “low” and “high” amounts of compute used. In the low-compute mode, the system obtained 75.7% accuracy on the semi-private test set; in high-compute mode it obtained 87.5%. (The semi-private test set has 100 tasks, but some of them have multiple “test-inputs,” which account for the non-integral scores.)

These are huge jumps in accuracy over previous entries on the semi-private set. These results, along with the improved results on other reasoning benchmarks, caused a stir on social media, with many people predicting that such systems will soon be better than humans on “most” reasoning tasks. Chollet himself [wrote](https://arcprize.org/blog/oai-o3-pub-breakthrough), “This is not merely incremental improvement, but a genuine breakthrough, marking a qualitative shift in AI capabilities compared to the prior limitations of LLMs. o3 is a system capable of adapting to tasks it has never encountered before, arguably approaching human-level performance in the ARC-AGI domain;” and “All intuition about AI capabilities will need to get updated for o3.”

#### **How Did o3 Solve These Tasks?**

The answer is, we don’t know. OpenAI hasn’t revealed much about how o3 (or o1) works. They did reveal that o3 was fine-tuned on 300 out of 400 of the ARC training tasks, in order to give it some knowledge of the domain and how the tasks worked[5](https://aiguide.substack.com/p/did-openai-just-solve-abstract-reasoning#footnote-5-153510923) and that the [prompt](https://github.com/arcprize/arc-agi-benchmarking/blob/main/docs/examples/prompt_example_o3.md) given to o3 for each task was very simple. Unlike many of the ARC-AGI 2024 entries, it doesn’t seem like o3 uses any augmented training data or augmented demonstrations, but again, I’m not certain about that.

OpenAI has in the past discussed how its reasoning models use “chain of thought” methods, in which solving a task is broken down into a series of steps, with each step consisting of the system generating a natural-language description of what the system is “thinking” at that step in the solution process, and then using those generated “thoughts” to further guide the chain. Systems like o1 and o3 are able to do this by having (presumably) been trained on large corpora of “chains of thought” reported by humans when solving problems. The training process involves some sort of reinforcement learning, in which the system learns a “reward model”—a separate model that learns to evaluate the quality of a given “chain of thought” at a given point.

#### **Inference-Time Compute**

Generating these chains-of-thought is a form of _inference-time compute_. To explain this notion to the uninitiated, let me give a little bit of background on machine learning.

Systems in machine learning are typically trained on a _training_ data set, and the trained systems are then used for various tasks, e.g., image recognition, language summarization, or (in the case of LLMs) generating words/tokens in natural language. The training process for large systems can be quite slow, but applying the trained system on a new example (this stage is called “inference time” or “test time”) is very fast (e.g., running a new example through a feed-forward neural network).

The o1 and o3 systems are a bit different. They use a pre-trained LLM, but at inference time, when given a new problem, they do a lot of additional computation, namely, generating their chain-of-thought traces. This is called “inference-time computation” or “test-time computation”.

To make a bit more sense of this, let’s consider four different AI systems:

(1) A neural network that recognizes hand-written characters. The training for this is a large set of hand-written characters, along with labels for the right answers. After training, the neural network can very quickly classify a new character, based on weights it learned during its training. Here, lots of compute is needed for training, but very little compute is needed for inference.

(2) The chess-playing program Deep Blue, that beat Garry Kasparov in 1997. Deep Blue was not “trained” at all—it used a human-created evaluation function to assess the “value” of a given board configuration. However, when playing a game, it did huge amounts of “heuristic search”—looking ahead through various possibilities in a game tree and using its evaluation function at the end of the search to decide which line of search resulted in the most valuable board configuration. Here there is no training, but a huge amount of compute needed for inference.

(3) AlphaGo. This system combined a neural network (actually multiple networks) and a Monte Carlo game-tree-search algorithm. The neural network was trained on lots of “self-play”. After the training period, when playing a game, AlphaGo used that trained neural network as a kind of evaluation function to predict which branches of the tree were the most valuable to search, and to assign probabilities to them. Here lots of compute was needed for training, but also a fair amount of compute was needed for inference (i.e., for choosing the next move).

(4) o1 and o3. These systems combine a pre-trained LLM with the kind of chain-of-thought generation that I mentioned earlier. Given a query, the pre-trained LLM is used in conjunction with the learned reward model to generate the tokens for the chain-of-thought process. Here, the system needs lots of compute for training, but also a fair amount of compute for inference.

People outside OpenAI don’t know exactly how o1 and o3’s chain-of-thought process works. Chollet [speculates](https://arcprize.org/blog/oai-o3-pub-breakthrough) that it is similar to AlphaGo’s Monte Carlo tree search:

“o3’s core mechanism appears to be natural language program search and execution within token space—at test time, the model searches over the space of possible Chains of Thought (CoTs) describing the steps required to solve the task, in a fashion perhaps not too dissimilar to AlphaZero-style Monte-Carlo tree search. In the case of o3, the search is presumably guided by some kind of evaluator model.”

But Nathan Lambert, a researcher at the Allen Institute for AI, [disagrees](https://www.interconnects.ai/p/openais-o3-the-2024-finale-of-ai). Also speculating, he wrote:

“[T]he MCTS [Monte Carlo tree search] references and presumptions are misguided, but understandable as many brilliant people are falling trapped to the shock that o1 and o3 can actually be just the forward passes from one language model.”

I’m not sure who’s correct here, and it may take a while for the details to come out.

#### **Drawing Samples to Solve an ARC Task**

To solve an ARC task, OpenAI gives o3 a number of “samples”—which I understand as independent queries with the same prompt—and then returns the solution with the most “votes” (the one that appears the most times) in those independent samples. The low-compute version was allowed six samples (at a cost of $20 per task), and the high-compute version was allowed 1,024 samples (at a cost estimated to be several thousands of dollars per task, and over $1M total for the whole evaluation…**wow, this is a lot of money to solve 100 little puzzles!**)

#### **Is It “Brute Force” Compute?**

In a [post on BlueSky](https://bsky.app/profile/melaniemitchell.bsky.social/post/3ldrb7ngifc22), I opined that “solving these tasks by brute-force compute defeats the original purpose.” By “brute-force compute” I was referring to the need for over 1,000 samples per task in the high-compute case, where each sample requires quite a bit of computation. My terminology wasn’t great: it isn’t exactly brute-force, since the chains of thought for each sample are generated in an “intelligent” way by the underlying LLM. It’s more like what is called “heuristic search”: here a trained neural network is being used as a heuristic (smart, but not optimal) generator or evaluator to search through the space of possible chains of thought.

#### **Does o3 Solve ARC Tasks Via Generalizable Abstraction and Reasoning?**

Indeed, o3’s performance on ARC is quite amazing, even though it violates the assumption that solving these tasks shouldn’t require huge amounts of computation at inference time. But I’m most curious about an even more pressing question: Is o3 (or any of the other current winning methods) actually solving these tasks using the kind of abstraction and reasoning the ARC benchmark was created to measure?

The purpose of abstraction is to be able to quickly and flexibly recognize new situations using known concepts, and to act accordingly. That is, the purpose of abstraction—at least a major purpose—is to generalize. For example, if a system correctly solves the “shape invariance” task (from the beginning of this post) , does that mean that it understands the abstract notion of shape invariance? That is, it able to equally easily understand shape invariance in similar contexts? Or in different domains?

It’s not necessarily the case. Machine learning methods are known to “overfit” to specific cases and often aren’t able to generalize well. One very interesting example of this was from DeepMind’s work on neural networks that learned to play Atari video games via reinforcement learning. A neural network trained on the video game “Breakout”, in which the player moves a “paddle” horizontally back and forth to hit a “ball” so that it will collide with “bricks”, was particularly successful, getting very high scores on the game. One set of researchers [showed](https://proceedings.mlr.press/v70/kansky17a/kansky17a.pdf), however, that changing the game just by moving the paddle up a few pixels resulted in the original trained system performing dramatically worse. It seems that the system had learned to play Breakout not by learning the concepts of “paddle”, “ball”, or “brick”, but by learning very specific mappings of pixel configurations into actions. That is, it didn’t learn the kinds of abstractions that would allow it to generalize.

I have similar questions about the abstractions discovered by o3 and the other winning ARC programs. These questions can be answered in part by further testing: seeing if these systems can adapt to variants on specific tasks or to reasoning tasks using the same concepts, but in other domains than ARC. The questions can also be answered by studies on the systems themselves: understanding better how they work under the hood, and how well they can explain their own reasoning processes using the kinds of abstractions for which the benchmark is supposed to be a general test.

#### **What’s Next for ARC?**

Chollet has himself [stated](https://arcprize.org/blog/oai-o3-pub-breakthrough) that the ARC benchmark is now “saturating,” meaning that AI methods can now do quite well on it, but still are not close to having general human-level abilities for abstraction and reasoning. Chollet describes what’s next:

“We’re going to be raising the bar with a new version—ARC-AGI-2—which has been in the works since 2022. It promises a major reset of the state-of-the-art. We want it to push the boundaries of AGI research with hard, high-signal evals that highlight current AI limitations.”

Here are some features that I think are needed in a new benchmark:

  * A larger private test set; 100 tasks is not enough to make strong conclusions.

  * Stricter restrictions on runtime and costs, or at least different categories of competitions, based on amount of compute required.

  * Ways to measure different levels of generalization:

    * Generalization to variations on a given task.

    * Generalization to variations on a given concept (which my collaborators and I tried to get at with our [ConceptARC benchmark](https://aiguide.substack.com/p/on-evaluating-understanding-and-generalization)).

    * Generalization to instantiations of concepts in different domains, in situations

with different levels of complexity.




When you’re trying to develop a measure of intelligence, it’s essential, though difficult, to avoid [Goodhart’s law](https://en.wikipedia.org/wiki/Goodhart%27s_law): “When a measure becomes a target, it ceases to be a good measure.” As a community of AI researchers, we really need to figure that one out.

[](https://substackcdn.com/image/fetch/$s_!Qkqi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff9cd9fa2-6984-4465-af92-0ccddc96e324_622x98.png)

Here is the answer to the ARC task from the beginning of the post:

[](https://substackcdn.com/image/fetch/$s_!B5xM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd5f10fb9-1352-44d7-afec-87a7411cd548_778x680.png)

Also of interest: AI researcher Mikel Bober-Irizar analyzed the problems o3 got wrong on the ARC public evaluation set: https://anokas.substack.com/p/o3-and-arc-agi-the-unsolved-tasks

Happy holidays to all! As always, I’ll be very interested in reading your comments on this post.

[1](https://aiguide.substack.com/p/did-openai-just-solve-abstract-reasoning#footnote-anchor-1-153510923)

Training task e509e548

[2](https://aiguide.substack.com/p/did-openai-just-solve-abstract-reasoning#footnote-anchor-2-153510923)

AGI is still, [in my opinion](https://www.science.org/doi/10.1126/science.ado7069), rather ill-defined.

[3](https://aiguide.substack.com/p/did-openai-just-solve-abstract-reasoning#footnote-anchor-3-153510923)

The name “o2” was skipped by OpenAI, supposedly to avoid name conflict with an existing system called O2.

[4](https://aiguide.substack.com/p/did-openai-just-solve-abstract-reasoning#footnote-anchor-4-153510923)

“Model” is really a misnomer here, since o3 is not just a language model but is a _system_ that incorporates a language model.

[5](https://aiguide.substack.com/p/did-openai-just-solve-abstract-reasoning#footnote-anchor-5-153510923)

It would be interesting to know how much this matters—can o3 do as well without this initial fine-tuning?
