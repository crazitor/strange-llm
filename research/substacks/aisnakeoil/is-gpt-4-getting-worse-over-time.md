---
title: "Is GPT-4 getting worse over time?"
author: "Arvind Narayanan & Sayash Kapoor"
date: ""
source: "substack_aisnakeoil"
url: "https://www.normaltech.ai/p/is-gpt-4-getting-worse-over-time"
---

A [new paper](https://arxiv.org/pdf/2307.09009v1.pdf) making the rounds is being interpreted as saying that GPT-4 has gotten worse since its release. Unfortunately, this is a vast oversimplification of what the paper found. And while the findings are interesting, some of the methods are questionable, so it’s worth digging into the details.

#### **Capability ≠ behavior**

One important concept to understand about chatbots is that there is a big difference between capability and behavior. A model that has a capability may or may not display that capability in response to a particular prompt.

Chatbots acquire their capabilities through pre-training. It is an expensive process that takes months for the largest models, so it is never repeated. On the other hand, their behavior is heavily affected by fine tuning, which happens after pre-training. Fine tuning is much cheaper and is done regularly. Note that the base model, after pre-training, is just a fancy autocomplete: It doesn’t chat with the user. The chatting behavior arises through fine tuning. Another important goal of fine tuning is to prevent undesirable outputs. In other words, fine tuning can both elicit and suppress capabilities.

Knowing all this, we should expect a model’s capabilities to stay largely the same over time, while its behavior can vary substantially. _This is completely consistent with what the paper found._

#### **No evidence of capability degradation**

The authors — Lingjiao Chen, Matei Zaharia, and James Zou — tested GPT-3.5 and GPT-4 on four tasks. OpenAI provides “snapshots” of the models from March and June through its API, so they compared the behavior of the two snapshots of each model.

The four tasks they selected were a math problem (checking if a number is prime), responding to sensitive questions, code generation, and visual reasoning. They found a performance degradation on two tasks: math problems and code generation.

For code generation, the change they report is that the newer GPT-4 adds non-code text to its output. For some reason, they don't evaluate the correctness of the code. They merely check if the code is directly executable — that is, it forms a complete, valid program without anything extraneous. So the newer model's attempt to be more helpful counted against it.

There is more weirdness in the way they evaluated math problems. 

#### **500 yes / no questions, but the correct answer is always yes**

The math questions were of the form _“Is 17077 prime”_? They picked 500 numbers, but all of them were prime!

This is where the stochastic parrotry of these models becomes important. It turns out that none of the models, in most cases, actually executed the algorithm of checking if the number has divisors — they merely pretended to. That is, they started reasoning through it, then skipped to the end. Here’s one snippet of a response from the authors’ data (GPT-4 March snapshot):

* * *

`Step 3: Check for divisibility by prime numbers less than or equal to the square root. We will check for divisibility by 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, and 139.`

`19997 is not divisible by any of these prime numbers.`

`Therefore, 19997 is a prime number.`

* * *

The model correctly lists all the potential factors that need to be checked, but doesn’t actually check them! This is evident even in the example shown in the paper, but the authors ignore this and present it as a test of math problem solving.

As we mentioned, the paper only evaluated primality testing on prime numbers. To supplement this evaluation, we tested the models with 500 composite numbers. It turns out that much of the performance degradation the authors found comes down to this choice of evaluation data.

What seems to have changed is that the March version of GPT-4 almost always guesses that the number is prime, and the June version almost always guesses that it is composite. The authors interpret this as a massive performance drop — since they only test primes. For GPT-3.5, this behavior is reversed. 

In reality, all four models are equally awful, as you can see in the following graph. They all guess based on the way they were calibrated. To simplify a bit, during fine tuning, maybe some model was exposed to more math questions involving prime numbers, and the other, composites.

[](https://substackcdn.com/image/fetch/$s_!Bvs1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F88aab142-3abe-4b05-a24f-2c59459df47a_1785x1093.png)The June version of GPT-3.5 and the March version of GPT-4 almost always conclude that the number is prime regardless of whether it is prime or composite. The other two models do the opposite. But the paper only tested prime numbers, and hence concluded that GPT-3.5’s performance improved while GPT-4’s degraded.

In short, everything in the paper is consistent with the behavior of the models changing over time. None of it suggests a degradation in capability. Even the behavior change seems specific to the quirks of the authors’ evaluation, and it isn’t clear how well their findings will generalize to other tasks. 

#### **Why did the paper touch a nerve?**

For the last couple of months, many AI enthusiasts have been convinced, based on their own usage, that GPT-4’s performance has degraded. When GPT-4’s architecture was (allegedly) [leaked](https://www.semianalysis.com/p/gpt-4-architecture-infrastructure), there was a widely viewed claim that OpenAI degraded performance to save computation time and cost. OpenAI, for its part, issued a clear denial that they degraded performance, which was interpreted by this community as gaslighting. So when the paper came out, it seemed to confirm these longstanding suspicions.

We don’t know for sure if there is any truth to the rumors of intentional performance degradation, but we are sure that the paper does not offer evidence of it. Zaharia has [confirmed](https://twitter.com/matei_zaharia/status/1681515867803381762) that the authors aren’t suggesting that this is the case.

Among those skeptical of the intentional degradation claim, the favored [hypothesis](https://twitter.com/fchollet/status/1664036777416597505) for people’s subjective experience of worsening performance is this: when people use ChatGPT more, they start to notice more of its limitations.

But there is another possibility.

#### **Behavior drift makes it hard to build reliable products on top of LLM APIs**

The user impact of behavior change and capability degradation can be very similar. Users tend to have specific workflows and prompting strategies that work well for their use cases. Given the nondeterministic nature of LLMs, it takes a lot of work to discover these strategies and arrive at a workflow that is well suited for a particular application. So when there is a behavior drift, those workflows might stop working.

It is little comfort to a frustrated ChatGPT user to be told that the capabilities they need still exist, but now require new prompting strategies to elicit. This is especially true for applications built on top of the GPT API. Code that is deployed to users might simply break if the model underneath changes its behavior.

To alleviate this problem, OpenAI provides snapshots, but only maintains them for a few months and requires application developers to update regularly. As we have [written before](https://www.aisnakeoil.com/p/openais-policies-hinder-reproducible), this underscores how hard it is to do reproducible research that uses these APIs, or to build reliable products on top of them.

~

In short, the new paper doesn’t show that GPT-4 capabilities have degraded. But it is a valuable reminder that the kind of fine tuning that LLMs regularly undergo can have unintended effects, including drastic behavior changes on some tasks. Finally, the pitfalls we uncovered are a reminder of how hard it is to [quantitatively evaluate language models](https://www.aisnakeoil.com/p/gpt-4-and-professional-benchmarks).

* * *

**Methodological notes**

  * To generate composites, we randomly selected 500 products of two primes. We constrained them to be in the same numerical range as the primes in the authors’ data (1000 – 20000). We eliminated numbers with small factors (< 30) to eliminate shortcut answers such as checking the last digit. 

  * The authors report an additional issue: the June version of GPT-4 doesn’t do Chain of Thought (CoT) reasoning despite being asked to “think step by step”, the standard prompt for eliciting this behavior. Instead, it simply responds yes or no. We reproduced this. However, it doesn’t change the main issue: even in cases where it does CoT reasoning, it doesn’t actually execute the algorithm.

  * The line between actually executing the primality checking algorithm and pretending to is unclear. If the model went through each possible prime factor and output the remainder when dividing the given number by that prime, it would constitute clear evidence of reasoning. On the other hand, for the transcript shown above, it seems intuitively obvious that that’s not the case. But there is a gray area, such as iterating over each potential prime factor and simply asserting that it is not a factor, without outputting the remainder.

  * We are grateful to the authors for making their experiments so easy to reproduce.



