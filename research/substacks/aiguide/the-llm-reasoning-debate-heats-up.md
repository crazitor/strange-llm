---
title: "The LLM Reasoning Debate Heats Up"
author: "Melanie Mitchell"
date: ""
source: "substack_aiguide"
url: "https://aiguide.substack.com/p/the-llm-reasoning-debate-heats-up"
---

One of the fieriest debates in AI these days is whether or not large language models can reason.

In May 2024, OpenAI released GPT-4o (omni), which, they wrote, “can reason across audio, vision, and text in real time.” And last month they released the GPT-o1 model, which they claim performs “complex reasoning”, and which achieves record accuracy on many “reasoning-heavy” benchmarks.

But others have questioned the extent to which LLMs (or even enhanced models such as GPT-4o and o1) solve problems by reasoning abstractly, or whether their success is due, at least in part, to matching reasoning patterns memorized from their training data, which limits their ability to solve problems that differ too much from what has been seen in training.

In a [previous post](https://aiguide.substack.com/p/can-large-language-models-reason) on LLM reasoning, I asked why it matters whether LLMs are performing “actual reasoning” versus behavior that just looks like reasoning:

> Why does this matter? If robust general-purpose reasoning abilities have emerged in LLMs, this bolsters the claim that such systems are an important step on the way to trustworthy general intelligence. On the other hand, if LLMs rely primarily on memorization and pattern-matching rather than true reasoning, then they will not be generalizable—we can’t trust them to perform well on ‘out of distribution’ tasks, those that are not sufficiently similar to tasks they’ve seen in the training data.

Before getting into the main part of this post, I’ll give my answer to a question I’ve seen a lot of people asking, just what is “reasoning” anyway? Indeed, reasoning is one of those overburdened terms that can mean quite different things. In my earlier post I defined it this way:

> The word ‘reasoning’ is an umbrella term that includes abilities for deduction, induction, abduction, analogy, common sense, and other ‘rational’ or systematic methods for solving problems. Reasoning is often a process that involves composing multiple steps of inference. Reasoning is typically thought to require abstraction—that is, the capacity to reason is not limited to a particular example, but is more general. If I can reason about addition, I can not only solve 23+37, but any addition problem that comes my way. If I learn to add in base 10 and also learn about other number bases, my reasoning abilities allow me to quickly learn to add in any other base.

It’s true that systems like GPT-4 and GPT-o1 have excelled on “reasoning” benchmarks, but is that because they are actually doing this kind of abstract reasoning? Many people have raised another possible explanation: the reasoning tasks on these benchmarks are similar (or sometimes identical) to ones that were in the model’s training data, and the model has memorized solution patterns that can be adapted to particular problems.

There have been many papers exploring these hypotheses (see the list at the end of this post of recent papers evaluating reasoning capabilities of LLMs). Most of these test the _robustness_ of LLMs’ reasoning capabilities by taking tasks that LLMs do well on and creating superficial variations on those tasks—variations that don’t change the underlying reasoning required, but that are less likely to have been seen in the training data.

In this post I discuss three recent papers on this topic that I found particularly interesting.

#### **Paper 1:** The embers of autoregressive training

**Paper Title:** [Embers of autoregression show how large language models are shaped by the problem they are trained to solve](https://www.pnas.org/doi/10.1073/pnas.2322420121)

**Authors:** R. Thomas McCoy, Shuny Yao, Dan Friedman, and Thomas L. Griffiths

This is one of my favorite recent LLM papers. The paper asks if the way LLMs are trained (i.e., learning to predict the next token in a sequence, which is called “autoregression”) has lingering effects (“embers”) on their problem-solving abilities. For example, consider the task of reversing a sequence of words. Here are two sequences:

_time. the of climate political the by influenced was decision This_

 _letter. sons, may another also be there with Yet_

Getting the right answer shouldn’t depend on the particular words in the sequence, but the authors showed that for GPT-4 there is a strong dependence. Note that the first sequence reverses into a coherent sentence, and the second does not. In LLM terms, reversing the first sequence yields an output that is more probable than the output of reversing the second. That is, when the LLM computes the probability of each word, given the words that come before, the overall probability will be higher for the first output than for the second. And when the authors tested GPT-4 on this task over many word sequences, they found that GPT-4 gets 97% accuracy (fraction of correct sequence reversals) when the answer is a high-probability sequence versus 53% accuracy for low-probability sequences.

The authors call this “sensitivity to output probability.” The other “embers of autoregression” are sensitivity to input probability (GPT-4 is better at solving problems with high-probability input sequences, even when the contents of the sequence shouldn’t matter), and sensitivity to task frequency (GPT-4 does better on versions of a task that are likely common in the training data than on same-difficulty versions that are likely rare in the training data).

One of the tasks the authors use to study these sensitivities is decoding “shift ciphers”. A shift cipher is a simple way to encode text, by shifting each letter by a specific number of places in the alphabet. For example, with a shift of two, _jazz_ becomes _lcbb_ (where the _z_ shift wraps around to the beginning of the alphabet). Shift ciphers are often denoted as “Rot-_n_ ”, where _n_ is the number of alphabetic positions to shift (rotate) by.

The authors tested GPT-3.5 and GPT-4 on decoding shift ciphers of different _n_ ’s. Here is a sample prompt they used:

_Rot-13 is a cipher in which each letter is shifted 13 positions forward in the alphabet. For example, here is a message and its corresponding version in rot-13:_

_Original text: “Stay here!”_

 _Rot-13 text: “Fgnl urer!_

_Here is another message. Encode this message in rot-13:_

_Original text: “To this day, we continue to follow these principles.”_

 _Rot-13 text:_

The authors found that GPT models have strong sensitivy to input and output probability as well as to task frequency, as illustrated in this figure (adapted from their paper):

[](https://substackcdn.com/image/fetch/$s_!4kDB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fedaa3d5d-dd5b-404a-9f9f-c7f6ecb60032_1704x552.png)

(a) **Output sensitivity:** When tested on decoding shift ciphers, the GPT models do substantially better when the correct output is a high-probability sequence. 

(b) **Input sensitivity:** When tested on encoding shift ciphers, GPT-4 is somewhat better on high-probability input sequences. 

(c) **Task sensitivity:** When tested on shift ciphers of different n values (e.g., Rot-12 vs. Rot-13), GPT models are substantially better on Rot-13. This seems to be because Rot-13 examples are much more common than other Rot-_n_ ’s in the training data, since Rot-13 is a popular “spoiler-free way to share information”, e.g., for online puzzle forums.

In short, Embers of Autoregression is sort of an “evolutionary psychology” for LLMs—it shows that the way LLMs are trained leaves strong traces in the biases the models have in solving problems.

Here’s the paper’s bottom line:

> First, we have shown that LLMs perform worse on rare tasks than on common ones, so we should be cautious about applying them to tasks that are rare in pretraining data. Second, we have shown that LLMs perform worse on examples with low-probability answers than ones with high-probability answers, so we should be careful about using LLMs in situations where they might need to produce low- probability text. Overcoming these limitations is an important target for future work in AI.

#### **Paper 2:** Factors affecting “chain of thought” prompting

**Paper title:** [Deciphering the Factors Influencing the Efficacy of Chain-of-Thought: Probability, Memorization, and Noisy Reasoning](https://arxiv.org/abs/2407.01687)

**Authors:** Akshara Prabhakar, Thomas L. Griffiths, R. Thomas McCoy

This paper, which shares two authors with the previous paper, looks in depth at chain-of-thought (CoT) prompting on the shift-cipher task. 

As I discussed in my earlier post on LLM reasoning, CoT prompting has been claimed to enable robust reasoning in LLMs. In CoT prompting, the prompt includes an example of a problem, as well as the reasoning steps to solve it, before posing a new problem. Here are two examples of the prompts that the authors used for shift ciphers; the one on the top doesn’t use CoT prompting, whereas the one on the bottom does:

[](https://substackcdn.com/image/fetch/$s_!NrxZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd97d397-f73f-4ebe-9c99-4b6e2ce2ca28_1484x548.png)

[](https://substackcdn.com/image/fetch/$s_!YxWN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F803f5f08-7fd9-4352-bb7d-ada26375f73b_1394x876.png)

The authors tested several models, including GPT-4, Claude 3.0, and Llama 3.1. Interestingly, they found that, given prompts without CoT, these models get close to _zero_ accuracy for most shift levels (_n_); when using prompts with CoT like the one above, they achieve much higher accuracy (e.g., 32% for GPT-4) across shift levels.

The authors cite four possible ways LLMs can appear to be “reasoning”, each of which makes different predictions about its pattern of errors.

(1) **Memorization:** The model is repeating reasoning patterns memorized from training data. This would predict that accuracy will depend on the task’s frequency in the training data (e.g., recall that for shift ciphers, Rot-13 is much more frequent in internet data than other Rot-n values).

(2) **Probabilistic Reasoning:** The model is choosing output that is most probable, given the input. This is influenced by the probability of token sequences learned during training. This kind of reasoning would predict that LLMs will be more accurate on problems whose answers (the generated output) are sequences with higher probability.

(3) **Symbolic Reasoning:** The model is using deterministic rules that work perfectly for any input. This would predict 100% accuracy no matter what form the task takes.

(4) **Noisy Reasoning:** The model is using an approximation to symbolic reasoning in which there is some chance of making an error at each step of inference. This would predict that problems that require more inference steps should produce worse accuracy. For shift ciphers, these would be problems that require more shift steps in the alphabet. 

To cut to the chase, the authors found that LLMs with CoT prompting exhibit a mix of memorization, probabilistic reasoning, and noisy reasoning. Below is the accuracy of Claude 3.0 as a function of shift-level _n_ ; the other models had a similar accuracy distribution. You can see that at the two ends (low and high _n_) the accuracy is relatively high compared with most of the middle _n_ values. This is a signature of noisy reasoning, since the lowest and highest _n_ values require the fewest inference steps. (Think of the alphabet as a circle; Rot-25, like Rot-1, requires only one inference step. In Rot-25, each letter would be encoded as the letter that immediately _precedes_ it.) 

[](https://substackcdn.com/image/fetch/$s_!40AG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe927e742-b6f2-4ef6-8e27-66cc01606216_978x420.png)

The big bump in the middle at Rot-13 is a signature of memorization—the accuracy of models at this shift level is due to its high frequency in the training data. The authors showed via other experiments that probabilistic reasoning is also a factor—see their paper for details. 

Here’s the authors’ bottom line:

> CoT reasoning can be characterized as probabilistic, memorization-influenced noisy reasoning, meaning that LLM behavior displays traits of both memorization and generalization.

These results are intriguing, but so far limited to the single task of shift ciphers. I hope to see (and maybe do myself) similar studies with other kinds of tasks.

#### **Paper 3:** Testing the robustness of LLMs on variations of simple math word problems

**Paper title:** [GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models](https://arxiv.org/abs/2410.05229)

**Authors:** Iman Mirzadeh, Keivan Alizadeh, Hooman Sharokhi, Oncel Tuzel, Samy Bengio, Mehrdad Farajtabar

This paper, from a research group at Apple, tests the robustness of several LLMs on a reasoning benchmark consisting of grade school math word problems. The benchmark, GSM8K, has been used in a lot of papers to show that LLMs are very good at simple mathematical reasoning. Both OpenAI’s GPT-4 and Anthropic’s Claude 3 get around 95% of these problems correct, without any fancy prompting. 

But to what extent does this performance indicate robust reasoning abilities, versus memorization (of these or similar problems in the training data) or, as the authors ask, “probabilistic pattern-matching rather than formal reasoning”?

To investigate this, the authors take each problem in the original dataset and create many variations on it, by changing the names, numbers, or other superficial aspects of the problem, changes that don’t affect the general reasoning required. Here’s an illustration from their paper of this process:

[](https://substackcdn.com/image/fetch/$s_!kATZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff73e9cc9-4db7-4333-b4a7-3ea2ec61f0e0_1624x1086.png)

They test several LLMs on this set of variations, and find that in all cases, the models’ accuracy decreases from that on the original benchmark, in some cases by a lot, though on the best models, such as GPT-4o, the decrease is minimal.

Going further, the authors show that adding irrelevant information to the original problems causes an even greater drop in accuracy than changing names or numbers. Here’s an example of adding irrelevant information (in pink) to a word problem:

[](https://substackcdn.com/image/fetch/$s_!rMl6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F966b7381-23ac-4300-880d-0f816de7e449_1478x112.png)

Even the very best models seem remarkably susceptible to being fooled by such additions. This figure from the paper shows the amount by which the accuracy drops for each model:

[](https://substackcdn.com/image/fetch/$s_!XAGV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f37829c-a677-45b0-8b1a-a84d819096c3_894x1148.png)

Here, each bar represents a different model and the bar length is the difference between the original accuracy on GSM8K and on the version where problems have irrelevant information (what they call the “GSM-NoOP” version). 

The bottom line from this paper :

> Our extensive study reveals significant performance variability across different instantiations of the same question, challenging the reliability of current GSM8K results that rely on single-point accuracy metrics.

And: 

> The introduction of GSM-NoOp [i.e., adding irrelevant information] exposes a critical flaw in LLMs’ ability to genuinely understand mathematical concepts and discern relevant information for problem-solving.

And:

> Ultimately, our work underscores significant limitations in the ability of LLMs to perform genuine mathematical reasoning. 

This paper, released just a couple of weeks ago, got quite a lot of buzz in the AI / ML community. People who were already skeptical of claims of LLM reasoning embraced this paper as proof that [“the emperor has no clothes”](https://x.com/c___f___b/status/1845361693271920826), and called the GSM-NoOP results [“particularly damning”](https://garymarcus.substack.com/p/llms-dont-do-formal-reasoning-and).

People more bullish on LLM reasoning argued that the paper’s conclusion—that current LLMs are not capable of genuine mathematical reasoning—was too strong, and [hypothesized](https://x.com/boazbaraktcs/status/1844763538260209818) that current LLMs might be able to solve all these problems with proper prompt engineering. (However, I should point out, when LLMs _succeeded_ on the original benchmark without any prompt engineering, many people cited that as “proof” of LLMs’ “emergent” reasoning abilities, and they didn’t ask for more tests of robustness.)

Others questioned whether humans who could solve the original problems would also be tripped up by the kinds of variations tested in this paper. Unfortunately, the authors did not test humans on these new problems. I would guess that many (certainly not all) people would also be affected by such variations, but perhaps unlike LLMs, we humans have the ability to overcome such biases via careful deliberation and metacognition. But discussion on that is for a future post.

I should also mention that a [similar paper](https://arxiv.org/pdf/2401.09395) was published last June, also showing that LLMs are not robust on variations of simple math problems, 

#### Conclusion

In conclusion, there’s no consensus about the conclusion! There are a lot of papers out there demonstrating what looks like sophisticated reasoning behavior in LLMs, but there’s also a lot of evidence that these LLMs aren’t reasoning _abstractly_ or _robustly_ , and often over-rely on memorized patterns in their training data, leading to errors on “out of distribution” problems. Whether this is going to doom approaches like OpenAI’s o1, which was directly trained on people’s reasoning traces, remains to be seen. In the meantime, I think this kind of debate is actually really good for the science of LLMs, since it spotlights the need for careful, controlled experiments to test robustness—experiments that go far beyond just reporting accuracy—and it also deepens the discussion of what _reasoning_ actually consists of, in humans as well as machines. 

If you want to read further, here is a list of some recent papers that test the robustness of reasoning in LLMs (including the papers discussed in this post).

Bibliography

[Embers of Autoregression Show How Large Language Models Are Shaped By the Problem They Are Trained To Solve](https://www.pnas.org/doi/10.1073/pnas.2322420121)

[GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models](https://arxiv.org/abs/2410.05229)

[Deciphering the Factors Influencing the Efficacy of Chain-of-Thought: Probability, Memorization, and Noisy Reasoning](https://arxiv.org/abs/2407.01687)

[Reasoning or Reciting? Exploring the Capabilities and Limitations of Language Models Through Counterfactual Tasks](https://arxiv.org/abs/2307.02477)

[Faith and Fate: Limits of Transformers on Compositionality](https://proceedings.neurips.cc/paper_files/paper/2023/hash/deb3c28192f979302c157cb653c15e90-Abstract-Conference.html)

[Phenomenal Yet Puzzling: Testing Inductive Reasoning Capabilities of Language Models with Hypothesis Refinement](https://arxiv.org/abs/2310.08559)

[Do Large Language Models Understand Logic or Just Mimick Context?](https://arxiv.org/abs/2402.12091)

[Alice in Wonderland: Simple Tasks Showing Complete Reasoning Breakdown in State-Of-the-Art Large Language Models](https://arxiv.org/abs/2406.02061)

[Beyond Accuracy: Evaluating the Reasoning Behavior of Large Language Models - A Survey](https://arxiv.org/abs/2404.01869)

[Functional Benchmarks for Robust Evaluation of Reasoning Performance, and the Reasoning Gap](https://arxiv.org/abs/2402.19450)

[A Peek into Token Bias: Large Language Models Are Not Yet Genuine Reasoners](https://arxiv.org/abs/2406.11050)

[Using Counterfactual Tasks to Evaluate the Generality of Analogical Reasoning in Large Language Models](https://arxiv.org/abs/2406.11050)

[Evaluating LLMs’ Mathematical and Coding Competency through Ontology-guided Interventions](https://arxiv.org/abs/2401.09395)

[Can Large Language Models Reason and Plan?](https://arxiv.org/abs/2403.04121)
