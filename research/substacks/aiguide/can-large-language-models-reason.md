---
title: "Can Large Language Models Reason?"
author: "Melanie Mitchell"
date: ""
source: "substack_aiguide"
url: "https://aiguide.substack.com/p/can-large-language-models-reason"
---

[](https://substackcdn.com/image/fetch/$s_!qVpl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd47ea1bf-bae7-40d3-84ba-b8886a6c9e7b_1988x1034.png)

What should we believe about the reasoning abilities of today’s large language models? As the headlines above illustrate, there’s a debate raging over whether these enormous pre-trained neural networks have achieved humanlike reasoning abilities, or whether their skills are in fact “a mirage.”

Reasoning is a central aspect of human intelligence, and robust domain-independent reasoning abilities have long been a key goal for AI systems. While large language models (LLMs) are not explicitly trained to reason, they have exhibited “emergent” behaviors that sometimes look like reasoning. But are these behaviors actually driven by true abstract reasoning abilities, or by some other less robust and generalizable mechanism—for example, by memorizing their training data and later matching patterns in a given problem to those found in training data? 

Why does this matter? If robust general-purpose reasoning abilities have emerged in LLMs, this bolsters the claim that such systems are an important step on the way to trustworthy general intelligence. On the other hand, if LLMs rely primarily on memorization and pattern-matching rather than true reasoning, then they will not be generalizable—we can’t trust them to perform well on “out of distribution” tasks, those that are not sufficiently similar to tasks they’ve seen in the training data. 

**What Is “Reasoning”?**

The word “reasoning” is an umbrella term that includes abilities for deduction, induction, abduction, analogy, common sense, and other “rational” or systematic methods for solving problems. Reasoning is often a process that involves composing multiple steps of inference. Reasoning is typically thought to require _abstraction_ —that is, the capacity to reason is not limited to a particular example, but is more general. If I can reason about addition, I can not only solve 23+37, but any addition problem that comes my way. If I learn to add in base 10 and also learn about other number bases, my reasoning abilities allow me to quickly learn to add in any other base.

**“Chain of Thought” Reasoning in LLMs**

In the last few years, there has been a deluge of papers making claims for reasoning abilities in LLMs (Huang & Chang give one recent [survey](https://arxiv.org/abs/2212.10403)). [One of the most influential such papers](https://proceedings.neurips.cc/paper_files/paper/2022/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf) (by Wei et al. from Google Research) proposed that so-called “Chain of Thought” (CoT) prompting elicits sophisticated reasoning abilities in these models. A CoT prompt gives one or more examples of a problem and the reasoning steps needed to solve it, and then poses a new problem. The LLM will then output text that follows a similar set of reasoning steps before outputting an answer. This figure from the paper by Wei et al. gives an example:

[](https://substackcdn.com/image/fetch/$s_!EHGD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff775e209-c346-4049-bd05-2d65dbcc205f_912x886.png)

Wei et al. tested the CoT prompting method on datasets with math word problems, commonsense reasoning problems, and other domains. In many cases, CoT prompting dramatically improved the performance of LLMs on these datasets. 

Two downsides of CoT prompting are (1) it takes some effort on the part of the human prompter to construct such prompts; and (2) often, being able to construct a CoT example to include in the prompt requires the prompter to already know how to solve the problem being given to the LLM!

[A subsequent paper](https://proceedings.neurips.cc/paper_files/paper/2022/file/8bb0d291acd4acf06ef112099c16f326-Paper-Conference.pdf) proposed that these problems can be avoided by leaving out the CoT example, and just posing the problem to an LLM with the added phrase “Let’s think step by step.” Here’s an example from that paper:

[](https://substackcdn.com/image/fetch/$s_!TZLp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1f0d6c6-3c10-4a92-999e-4deb391b2126_1250x486.png)

Amazingly, this simple addition to a prompt—termed “zero-shot CoT prompting”— substantially improves LLM’s performance on several reasoning benchmarks as compared with prompts without the addition of “Let’s think step by step.”

Why does CoT prompting—whether with an example or with “Let’s think step by step”—have this dramatic effect on LLMs? Interestingly, while there are many hypotheses, this question has not been definitively answered. 

**Are the Reasoning Steps Generated Under CoT Prompting Faithful to the Actual Reasoning Process?**

While the above examples of CoT and zero-shot CoT prompting show the language model generating text that looks like correct step-by-step reasoning about the given problem, one can ask if the text the model generates is “faithful”—that is, does it describe the actual process of reasoning that the LLM uses to solve the problem? LLMs are not trained to generate text that accurately reflects their own internal “reasoning” processes; they are trained to generate only _plausible-sounding_ text in response to a prompt. What, then, is the connection between the generated text and the LLM’s actual processes of coming to an answer?

This question has been addressed by different researchers. In [one study](https://arxiv.org/abs/2305.04388), researchers found that, in some cases, “CoT explanations can systematically misrepresent the true reason for a model’s prediction.” [Another study](https://arxiv.org/abs/2307.13702) found that, interestingly, “As models become larger and more capable, they produce less faithful reasoning on most tasks we study.”

Indeed, Wei et al., the authors of the original Chain of Thought prompting paper, note this caveat: “[A]lthough chain of thought emulates the thought processes of human reasoners, this does not answer whether the neural network is actually ‘reasoning,’ which we leave as an open question.”

**If LLMs Are Not Reasoning, What Are They Doing?**

If it turns out that LLMs are not actually reasoning in order to solve the problems we give them, how else could they be solving them? Several researchers have shown that LLMs are substantially better at solving problems that involve terms or concepts that appear more frequently in their training data, leading to the hypothesis that LLMs do not perform robust abstract reasoning to solve problems, but instead solve problems (at least in part) by identifying patterns in their training data that match, or are similar to, or are otherwise related to the text of the prompts they are given. 

For example, [a study by Razeghi et al.](https://aclanthology.org/2022.findings-emnlp.59.pdf) showed that some GPT-based LLMs (pre-trained on a known corpus) were much better at arithmetic problems that involved numbers that appeared frequently in the pre-training corpus than those that appeared less frequently. These models appear to lack a general ability for arithmetic, but instead rely on a kind of “memorization”—matching patterns of text they have seen in pre-training. The authors of that study point out that, in view of such results, “any evaluation of reasoning that does not take the pretraining data into account is difficult to interpret, and that we need to revisit evaluation of language models with respect to their pretraining data before making any conclusion about the models’ generalization abilities beyond the pretraining data.” As a stark example of this, Horace He, an undergraduate researcher at Cornell, [posted on Twitter](https://twitter.com/cHHillee/status/1635790330854526981) that on a dataset of programming challenges, GPT-4 solved 10 out of 10 problems that had been published before 2021 (GPT-4’s pre-training cutoff date) and zero out of 10 problems that had been published after 2021. GPT-4’s success on the pre-2021 challenges thus seems to be due to memorizing problems seen in its training data rather than reasoning about the problems from scratch. 

[A fascinating paper](https://arxiv.org/abs/2307.02477) by Wu et al. probed the “memorization” hypothesis via what they called “counterfactual tasks.” The idea is to take a reasoning task that an LLM performs well on, and to create a variant (“counterfactual version”) of that task that requires the same abstract reasoning ability but that has probably appeared less frequently in the LLM’s training data. 

As one example, GPT-4 is very good at executing snippets of Python computer code given in a prompt. In Python, lists and other data structures use “zero-indexing”, meaning, for example, that the first element of a list L is referred to as L[0]. If L = [“orange”, “banana”, “apple”], then L[0] = “orange”, L[1] = “banana”, and so on. Some other programming languages use “one-indexing”—in these, L[1] would equal “orange”, L[2] would equal “banana”, etc.

A human programmer who knows Python would presumably be able to easily adapt to a hypothetical version of Python that uses one-indexing rather than zero-indexing. Doing so would be a very simple form of abstract reasoning about code. 

Since most of GPT-4’s training data is on zero-indexed languages, executing code snippets in a **one-indexed** version of Python counts as a counterfactual task. 

Wu et al. gave two sets of code execution tests to GPT-4. The first set asked it to execute code snippets in original Python, using prompts that looked like this: 

 _**You are an expert programmer. What does the following code snippet in Python 3.7 print?**_**[code snippet inserted here]**

The second set asked it to execute code snippets in a hypothetical one-indexed version of Python, using prompts that looked like this: 

 _**You are an expert programmer who can readily adapt to new programming languages. There is a new programming language, ThonPy, which is identical to Python 3.7 except all variables of the `list`, `tuple`, and `str` types use 1-based indexing, like in the MATLAB and R languages, where sequence indices start from 1… What does the following code snippet in ThonPy print?**_

**[code snippet inserted here]**

On the first set of tests GPT-4 achieved a very high accuracy, but on the second set of tests the accuracy was much lower. 

Wu et al. found a similar pattern for counterfactual tasks in many different domains. Another example was reasoning about the legality of a short sequence of chess moves in regular chess and in a variant in which the positions of knights and bishops are switched. In this and other domains, the performance of GPT-4 on the original version of the task was much higher than on the counterfactual version. This was true whether or not zero-shot CoT prompting was used. The authors noted that, although GPT-4’s (and other LLMs’) performance on counterfactual tasks was often above random chance, these results “demonstrate limitations in the [LLM’s] abstract capacity to solve the target task.” Just as LLMs are better on arithmetic problems with numbers that appear more frequently in their training data, they are much better on versions of reasoning tasks that are similar to those in data they have been trained on. 

The question of “memorization” versus reasoning is not all-or-nothing; Wu et al. noted that in LLMs there is “some degree of reasoning that is transferable between the default and counterfactual worlds. [Memorization and reasoning are] not a dichotomy, but rather they can co-exist in a continuum.” However, if some form of memorization is largely driving LLM’s apparent reasoning abilities, this means that LLMs will not be robust in applying these abilities to versions of tasks that are different from those they have been trained on, which is a big concern for their application in the real world. 

Other interesting recent evaluations of LLMs using “counterfactual tasks” include [changing the names of objects and actions in a planning task](https://arxiv.org/abs/2305.15771) and [testing an LLM on variations of an analogical-reasoning task](https://arxiv.org/abs/2402.08955). 

**The Trickiness of Evaluating LLMs for General Abilities**

All of the results I’ve discussed here point to the trickiness of evaluating LLMs for general reasoning abilities, which I wrote about in [a recent column for the journal ](https://www.science.org/doi/10.1126/science.adj5957)_[Science](https://www.science.org/doi/10.1126/science.adj5957)_. When we test AI systems for humanlike mental abilities, we have to keep in mind possibilities for data contamination (testing on items in or very similar to those seen in the training set) and “shortcuts”—spurious statistical associations or pattern-matching that can produce correct answers without requiring the general underlying abilities the evaluation is supposed to test. The authors of [another paper testing LLM reasoning abilities](https://arxiv.org/abs/2305.18654) put it this way: “Shortcut learning via pattern-matching may yield fast correct answers when similar compositional patterns are available during training but does not allow for robust generalization to uncommon or complex examples.”

One might argue that humans also rely on memorization and pattern-matching when performing reasoning tasks. Many psychological studies have shown that people are better at reasoning about familiar than unfamiliar situations; one group of AI researchers [argued](https://arxiv.org/pdf/2207.07051.pdf) that the same patterns of “content effects” affect both humans and LLMs. However, it is also known that humans are (at least in some cases) capable of abstract, content-independent reasoning, if given the time and incentive to do so, and moreover we are able to adapt our understanding of what we have learned to wholly new situations. Whether LLMs have such **general** abstract-reasoning capacities, elicited through prompting tricks, [scratchpads](https://arxiv.org/abs/2112.00114), or other external enhancements, still needs to be systematically demonstrated. 
