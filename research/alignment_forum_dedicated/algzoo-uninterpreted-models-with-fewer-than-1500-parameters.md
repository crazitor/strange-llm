---
title: "AlgZoo: uninterpreted models with fewer than 1,500 parameters"
author: "Jacob_Hilton"
date: "2026-01-26"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/x8BbjZqooS4LFXS8Z/algzoo-uninterpreted-models-with-fewer-than-1-500-parameters"
score: 179
votes: 67
---

_This post covers work done by several researchers at, visitors to and collaborators of ARC, including Zihao Chen, George Robinson, David Matolcsi, Jacob Stavrianos, Jiawei Li and Michael Sklar. Thanks to Aryan Bhatt, Gabriel Wu, Jiawei Li, Lee Sharkey, Victor Lecomte and Zihao Chen for comments._

In the wake of recent debate about [pragmatic](https://www.lesswrong.com/posts/StENzDcD3kpfGJssR/a-pragmatic-vision-for-interpretability) versus [ambitious](https://www.lesswrong.com/posts/Hy6PX43HGgmfiTaKu/an-ambitious-vision-for-interpretability) visions for mechanistic interpretability, ARC is sharing some models we've been studying that, in spite of their tiny size, serve as challenging test cases for any ambitious interpretability vision. The models are RNNs and transformers trained to perform algorithmic tasks, and range in size from 8 to 1,408 parameters. The largest model that we believe we more-or-less fully understand has 32 parameters; the next largest model that we have put substantial effort into, but have failed to fully understand, has 432 parameters. The models are available here:

**\[ [AlgZoo GitHub repo](https://github.com/alignment-research-center/alg-zoo) \]**

We think that the "ambitious" side of the mechanistic interpretability community has historically underinvested in "fully understanding slightly complex models" compared to "partially understanding incredibly complex models". There has been some prior work aimed at full understanding, for instance on models trained to perform [paren balancing](https://www.lesswrong.com/s/h95ayYYwMebGEYN5y/p/kjudfaQazMmC74SbF), [modular addition](https://arxiv.org/abs/2301.05217) and more general [group operations](https://arxiv.org/abs/2410.07476), but we still don't think the field is close to being able to fully understand our models (at least, not in the sense we discuss in this post). If we are going to one day fully understand multi-billion-parameter LLMs, we probably first need to reach the point where fully understanding models with a few hundred parameters is pretty easy; we hope that AlgZoo will spur research to either help us reach that point, or help us reckon with the magnitude of the challenge we face.

One likely reason for this underinvestment is lingering philosophical confusion over the meaning of "explanation" and "full understanding". Our current perspective at ARC is that, given a model that has been optimized for a particular loss, an "explanation" of the model amounts to a **mechanistic estimate of the model's loss**. We evaluate mechanistic estimates in one of two ways. We use [_surprise accounting_](https://www.lesswrong.com/posts/SyeQjjBoEC48MvnQC/formal-verification-heuristic-explanations-and-surprise) to determine whether we have achieved a full understanding; but for practical purposes, we simply look at mean squared error as a function of compute, which allows us to [compare the estimate with sampling](https://www.lesswrong.com/posts/XdQd9gELHakd5pzJA/arc-progress-update-competing-with-sampling).

In the rest of this post, we will:

*   Review our perspective on mechanistic estimates as explanations, including our two ways of evaluating mechanistic estimates
*   Walk through three AlgZoo RNNs that we've studied, the smallest of which we fully understand, and the largest of which we don't
*   Conclude with some thoughts on how ARC's approach relates to ambitious mechanistic interpretability

Mechanistic estimates as explanations
-------------------------------------

Models from AlgZoo are trained to perform a simple algorithmic task, such as calculating the position of the second-largest number in a sequence. To explain why such a model has good performance, we can produce a _mechanistic estimate_ of its accuracy.^[\[1\]](#fn1)^ By "mechanistic", we mean that the estimate reasons deductively based on the structure of the model, in contrast to a sampling-based estimate, which makes inductive inferences about the overall performance from individual examples.^[\[2\]](#fn2)^ Further explanation of this concept can be found [here](https://www.lesswrong.com/posts/XdQd9gELHakd5pzJA/arc-progress-update-competing-with-sampling#What_makes_an_algorithm__mechanistic__).

Not all mechanistic estimates are high quality. For example, if the model had to choose between 10 different numbers, before doing any analysis at all, we might estimate the accuracy of the model to be 10%. This would be a mechanistic estimate, but a very crude one. So we need some way to evaluate the quality of a mechanistic estimate. We generally do this using one of two methods:

1.  **Mean squared error versus compute.** The more conceptually straightforward way to evaluate a mechanistic estimate is to simply ask how close it gets to the model's actual accuracy. The more compute-intensive the mechanistic estimate, the closer it should get to the actual accuracy. Our [matching sampling principle](https://www.lesswrong.com/posts/XdQd9gELHakd5pzJA/arc-progress-update-competing-with-sampling#The_matching_sampling_principle) is roughly the following conjecture: there is a mechanistic estimation procedure that (given suitable advice) performs at least as well as random sampling in mean squared error for any given computational budget.
2.  **Surprise accounting.** This is an information-theoretic metric that asks: how surprising is the model's actual accuracy, now that we have access to the mechanistic estimate? We accrue surprise in one of two ways: either the estimate itself performed some kind of calculation or check with a surprising result, or the model's actual accuracy is still surprising even after accounting for the mechanistic estimate and its uncertainty. Further explanation of this idea can be found [here](https://www.lesswrong.com/posts/SyeQjjBoEC48MvnQC/formal-verification-heuristic-explanations-and-surprise).

Surprise accounting is useful because it gives us a notion of "full understanding": a mechanistic estimate with as few bits of total surprise as the number of bits of optimization used to select the model. On the other hand, mean squared error versus compute is more relevant to applications such as [low probability estimation](https://www.lesswrong.com/posts/xj5nzResmDZDqLuLo/estimating-tail-risk-in-neural-networks), as well as being easier to work with. We have been increasingly focused on [matching the mean squared error of random sampling](https://www.lesswrong.com/posts/XdQd9gELHakd5pzJA/arc-progress-update-competing-with-sampling), which remains a challenging baseline, although we generally consider this to be easier than achieving a full understanding. The two metrics are often closely related, and we will walk through examples of both metrics in the case study below.

For most of the larger models from AlgZoo (including the 432-parameter model \\(M_{16,10}\\) discussed below), we would consider it a major research breakthrough if we were able to produce a mechanistic estimate that matched the performance of random sampling under the mean squared error versus compute metric.^[\[3\]](#fn3)^ It would be an even harder accomplishment to achieve a full understanding under the surprise accounting metric, but we are less focused on this.

Case study: 2nd argmax RNNs
---------------------------

The models in [AlgZoo](https://github.com/alignment-research-center/alg-zoo) are divided into four families, based on the task they have been trained to perform. The family we have spent by far the longest studying is the family of models trained to find the position of the second-largest number in a sequence, which we call the "2nd argmax" of the sequence.

The models in this family are parameterized by a hidden size \\(d\\) and a sequence length \\(n\\). The model \\(M_{d,n}\\) is a 1-layer ReLU RNN with \\(d\\) hidden neurons that takes in a sequence of \\(n\\) real numbers and produces a vector of logit probabilities of length \\(n\\). It has three parameter matrices:

*   the input-to-hidden matrix \\(W^{hi}\\in\\mathbb R^{d\\times 1}\\)
*   the hidden-to-hidden matrix \\(W^{hh}\\in\\mathbb R^{d\\times d}\\)
*   the hidden-to-output matrix \\(W^{oh}\\in\\mathbb R^{n\\times d}\\)

The logits of \\(M_{d,n}\\) on input sequence \\(x\_0,\\ldots,x\_{n-1}\\in\\mathbb R\\) are computed as follows:

*   \\(h_0=0\\in\\mathbb R^d\\)
*   \\(h _ {t+1}=\\mathrm{ReLU}\\left(W^{hh}h _ t+W^{hi}x _ t\\right)\\) for \\(t=0,\\ldots,n-1\\)
*   \\(\\mathrm{logits}=W^{oh}h_n\\)

Diagrammatically:  
![2nd_argmax_architecture.png](https://www.alignment.org/content/images/2026/01/2nd_argmax_architecture.png)

Each model in this family is trained to make the largest logit be the one that corresponds to the position of second-largest input, using softmax cross-entropy loss.

The models we'll discuss here are \\(M_{2,2}\\), \\(M_{4,3}\\) and \\(M_{16,10}\\). For each of these models, we'd like to understand why the trained model has high accuracy on standard Gaussian input sequences.

### Hidden size 2, sequence length 2

The model \\(M_{2,2}\\) can be loaded in AlgZoo using `zoo_2nd_argmax(2, 2)`. It has 10 parameters and almost perfect 100% accuracy, with an error rate of roughly 1 in 13,000. This means that the difference between the model's logits,  
\\\[\\Delta\\left(x _ 0,x _ 1\\right):=\\mathrm{logits}\\left(x _ 0,x _ 1\\right) _ 1-\\mathrm{logits}\\left(x _ 0,x _ 1\\right) _ 0,\\\]is almost always negative when \\(x\_1>x\_0\\) and positive when \\(x\_0>x\_1\\). We'd like to mechanistically explain why the model has this property.

To do this, note first that because the model uses ReLU activations and there are no biases, \\(\\Delta\\) is a piecewise linear function of \\(x\_0\\) and \\(x\_1\\) in which the pieces are bounded by rays through the origin in the \\(x\_0\\)-\\(x\_1\\) plane.

Now, we can "standardize" the model to obtain an exactly equivalent model for which the entries of \\(W^{hi}\\) lie in \\(\\left\\{\\pm 1\\right\\}\\), by rescaling the neurons of the hidden state. Once we do this, we see that  
\\\[W^{hi}=\\begin{pmatrix}+1\\\-1\\end{pmatrix},\\qquad W^{hh}\\in\\begin{pmatrix}\\left\[-1,0\\right)&\\left\[1,\\infty\\right)\\\\\left\[1,\\infty\\right)&\\left\[-1,0\\right)\\end{pmatrix}\\\\\text{and}\\qquad W^{oh}\\in\\begin{pmatrix}\\left(0,\\infty\\right)&\\left(-\\infty,0\\right)\\\\\left(-\\infty,0\\right)&\\left(0,\\infty\\right)\\end{pmatrix}.\\\]

From these observations, we can prove that, on each linear piece of \\(\\Delta\\),  
\\\[\\Delta\\left(x\_0,x\_1\\right)=a\_0x\_0-a\_1x\_1\\\]with \\(a\_0,a\_1>0\\), and moreover, the pieces of \\(\\Delta\\) are arranged in the \\(x\_0\\)-\\(x\_1\\) plane according to the following diagram:

![](https://www.alignment.org/content/images/2025/12/2nd_argmax_2_2.png)

Here, a double arrow indicates that a boundary lies somewhere between its neighboring axis and the dashed line \\(x\_0=x\_1\\), but we don't need to worry about exactly where it lies within this range.

Looking at the coefficients of each linear piece, we observe that:

*   In the two blue regions, we have \\(a\_0<a\_ 1\\)
*   In the two green regions, we have \\(a\_0>a\_1\\)
*   In the two yellow regions, we have \\(a\_0\\approx a\_1\\) to within around 1 part in \\(2^{11}\\)

This implies that:

*   \\(\\Delta\\left(x\_0,x\_1\\right)<0\\) in the blue and green regions above the line \\(x\_0=x\_1\\)
*   \\(\\Delta\\left(x\_0,x\_1\\right)>0\\) in the blue and green regions below the line \\(x\_0=x\_1\\)
*   \\(\\Delta\\left(x\_0,x\_1\\right)\\) is approximately proportional to \\(x\_0-x\_1\\) in the two yellow regions

Together, these imply that the model has almost 100% accuracy. More precisely, the error rate is the fraction of the unit disk lying between the model's decision boundary and the line \\(x\_0=x\_1\\), which is around 1 in \\(2\\pi\\times 2^{11}\\approx 13,000\\). This is very close to the model's empirically-measured error rate.

**Mean squared error versus compute.** Using only a handful of computational operations, we were able to mechanistically estimate the model's accuracy to within under 1 part in 13,000, which would have taken tens of thousands of samples. So our mechanistic estimate was much more computationally efficient than random sampling. Moreover, we could have easily produced a much more precise estimate (exact to within floating point error) by simply computing how close \\(a\_0\\) and \\(a\_1\\) were in the two yellow regions.

**Surprise accounting.** As explained [here](https://www.lesswrong.com/posts/SyeQjjBoEC48MvnQC/formal-verification-heuristic-explanations-and-surprise#Surprise_accounting), the total surprise decomposes into the surprise of the explanation plus the surprise given the explanation. The surprise given the explanation is close to 0 bits, since the calculation was essentially exact. For the surprise of the explanation, we can walk through the steps we took:

*   We "standardized" the model, which simply replaced the model with an exactly equivalent one. This did not depend on the model's parameters at all, and so doesn't incur any surprise.
*   We checked the signs of all 10 of the model's parameters, and whether or not each of the 4 entries of \\(W^{hh}\\) was greater than or less than 1 in magnitude, incurring 14 bits of surprise.
*   We deduced from this the form of the piecewise linear function \\(\\Delta\\). This was another step that didn't depend on the model's parameters and so doesn't incur any surprise.
*   We checked which of the two linear coefficients was larger in magnitude in each of the 4 blue and green regions, incurring 4 bits of surprise.
*   We checked that the two linear coefficients were equal in magnitude in each of the 2 yellow regions to within 1 part in \\(2^{11}\\), incurring around 22 bits of surprise.

Adding this up, the total surprise is around 40 bits. This plausibly matches the number of bits of optimization used to select the model, since it was probably necessary to optimize the linear coefficients in the yellow regions to be almost equal. So we can be relatively comfortable in saying that we have achieved a full understanding.

Note that our analysis here was pretty "brute force": we essentially checked each linear region of \\(\\Delta\\) one by one, with a little work up front to reduce the total number of checks required. Even though we consider this to constitute a full understanding in this case, we would not draw the same conclusion for much deeper models. This is because the number of regions would grow exponentially with depth, making the number of bits of surprise far larger than the number of bits taken up by the weights of the model (which is an upper bound on the number of bits of optimization used to select the model). The same exponential blowup would also prevent us from matching the efficiency of sampling at reasonable computational budgets.

Finally, it is interesting to note that our analysis allows us to construct a model by hand that gets exactly 100% accuracy, by taking  
\\\[W^{hi}=\\begin{pmatrix}+1\\\-1\\end{pmatrix},\\qquad W^{hh}=\\begin{pmatrix}-1&+1\\\+1&-1\\end{pmatrix}\\\\\text{and}\\qquad W^{oh}=\\begin{pmatrix}+1&-1\\\-1&+1\\end{pmatrix}.\\\]

### Hidden size 4, sequence length 3

The model \\(M_{4,3}\\) can be loaded in AlgZoo using `zoo_2nd_argmax(4, 3)`. It has 32 parameters and an accuracy of 98.5%.

Our analysis of \\(M_{4,3}\\) is broadly similar to our analysis of \\(M_{2,2}\\), but the model is already deep enough that we wouldn't consider a fully brute force explanation to be adequate. To deal with this, we exploit various approximate symmetries in the model to reduce the total number of computational operations as well as the surprise of the explanation. Our full analysis can be found in these sets of notes:

*   [**Symmetric RNNs**](https://drive.google.com/file/d/1qH61_WshTrgYh0YLj5vkONzk8x00zImN/view) by George Robinson
*   [**Heuristic explanations for 2nd argmax models**](https://drive.google.com/file/d/1t2rXhDQqWrOXRwjqstbrBPWiCmYlMts_/view) by Jacob Hilton

In the second set of notes, we provide two different mechanistic estimates for the model's accuracy that use different amounts of compute, depending on which approximate symmetries are exploited. We analyze both estimates according to our two metrics. We find that we are able to roughly match the computational efficiency of sampling,^[\[4\]](#fn4)^ and we think we more-or-less have a full understanding, although this is less clear.

Finally, our analysis once again allows us to construct an improved model by hand, which has 99.99% accuracy.^[\[5\]](#fn5)^

### Hidden size 16, sequence length 10

The model \\(M_{16,10}\\) can be loaded in AlgZoo using `example_2nd_argmax()`.^[\[6\]](#fn6)^ It has 432 parameters and an accuracy of 95.3%.

This model is deep enough that a brute force approach is no longer viable. Instead, we look for "features" in the activation space of the model's hidden state.

After rescaling the neurons of the hidden state, we notice an approximately isolated subcircuit formed by neurons 2 and 4, with no strong connections to the outputs of any other neurons:  
\\\[W^{hi} _ {\\left(2,4\\right)}\\approx\\begin{pmatrix}0\\\+1\\end{pmatrix},\\qquad W^{hh} _ {\\left(2,4\\right),\\left(2,4\\right)}\\approx\\begin{pmatrix}+1&+1\\\-1&-1\\end{pmatrix}\\\\\text{and}\\qquad W^{hh} _ {\\left(2,4\\right),\\left(0,1,3,\\ldots\\right)}\\approx\\begin{pmatrix}0&\\ldots\\\0&\\ldots\\end{pmatrix}.\\\]

It follows that after unrolling the RNN for \\(t\\) steps:

*   Neuron 2 is approximately \\(\\max\\left(0,x\_0,\\ldots,x\_{t-2}\\right)\\)
*   Neuron 4 is approximately \\(\\max\\left(0,x\_0,\\ldots,x\_{t-1}\\right)-\\max\\left(0,x\_0,\\ldots,x\_{t-2}\\right)\\)

This can be proved by induction using the identity \\(\\mathrm{ReLU}\\left(a-b\\right)=\\max\\left(a,b\\right)-b\\) for neuron 4.

Next, we notice that neurons 6 and 7 fit into a larger approximately isolated subcircuit together with neurons 2 and 4:  
\\\[W^{hi} _ {\\left(6,7\\right)}\\approx\\begin{pmatrix}-1\\\-1\\end{pmatrix},\\qquad W^{hh} _ {\\left(6,7\\right),\\left(2,4\\right)}\\approx\\begin{pmatrix}+1&0\\\+1&+1\\end{pmatrix}\\\\\text{and}\\qquad W^{hh} _ {\\left(6,7\\right),\\left(0,1,3,\\ldots\\right)}\\approx\\begin{pmatrix}0&\\ldots\\\0&\\ldots\\end{pmatrix}.\\\]

Using the same identity, it follows that after unrolling the RNN for \\(t\\) steps:

*   Neuron 6 is approximately \\(\\max\\left(0,x\_0,\\ldots,x\_{t-3},x_{t-1}\\right)-x_{t-1}\\)
*   Neuron 7 is approximately \\(\\max\\left(0,x\_0,\\ldots,x\_{t-1}\\right)-x_{t-1}\\)

We can keep going, and add in neuron 1 to the subcircuit:  
\\\[W^{hi} _ {\\left(1\\right)}\\approx\\begin{pmatrix}-1\\end{pmatrix},\\qquad W^{hh} _ {\\left(1\\right),\\left(2,4,6,7\\right)}\\approx\\begin{pmatrix}+1&+1&+1&-1\\end{pmatrix}\\\\\text{and}\\qquad W^{hh} _ {\\left(1\\right),\\left(0,1,3,\\ldots\\right)}\\approx\\begin{pmatrix}0&\\ldots\\end{pmatrix}.\\\]

Hence after unrolling the RNN for \\(t\\) steps, neuron 1 is approximately  
\\\[\\max\\left(0,x\_0,\\ldots,x\_{t-4},x_{t-2},x_{t-1}\\right)-x_{t-1},\\\]forming another "leave-one-out-maximum" feature (minus the most recent input).

In fact, by generalizing this idea, we can construct a model by hand that uses 22 hidden neurons to form all 10 leave-one-out-maximum features, and leverages these to achieve an accuracy of 99%.^[\[7\]](#fn7)^

Unfortunately, however, it is challenging to go much further than this:

*   We have exploited the approximate weight sparsity of 5 of the hidden neurons, but most of the remaining 11 hidden neurons are more densely connected.
*   We have produced a handcrafted model with high accuracy, but we have not produced a correspondence between most of hidden neurons of the trained model and the hidden neurons of the handcrafted model.
*   We have used approximations in our analysis, but have not dealt with the approximation error, which gets increasingly significant as we consider more complex neurons.

Fundamentally, even though we have some understanding of the model, our explanation is incomplete because we not have not turned this understanding into an adequate mechanistic estimate of the model's accuracy.

Ultimately, to produce a mechanistic estimate for the accuracy of this model that is competitive with sampling (or that constitutes a full understanding), we expect we would have to somehow combine this kind of feature analysis with elements of the "brute force after exploiting symmetries" approach used for the models \\(M_{2,2}\\) and \\(M_{4,3}\\), and to do so in a primarily algorithmic way. This is why we consider producing such a mechanistic estimate to be a formidable research challenge.

Some notes with further discussion of this model can be found here:

*   [**RNNs for the 2nd argmax**](https://drive.google.com/file/d/1USCD1LPa6hXMTj7PAO6Jmc4dVdxemZY3/view) and [complementary notebook](https://colab.research.google.com/drive/1yRv18_Gp0twoZ-kptMygVhAq-azj2bBq) by Zihao Chen

Conclusion
----------

The models in AlgZoo are small, but for all but the tiniest of them, it is a considerable challenge to mechanistically estimate their accuracy competitively with sampling, let alone fully understand them in the sense of surprise accounting. At the same time, AlgZoo models are trained on tasks that can easily be performed by LLMs, so fully understanding them is practically a prerequisite for ambitious LLM interpretability. Overall, we would be keen to see other ambitious-oriented researchers explore our models, and more concretely, we would be excited to see better mechanistic estimates for our models in the sense of mean squared error versus compute. One specific challenge we pose is the following.

**Challenge**: Design a method for mechanistically estimating the accuracy of the 432-parameter model \\(M_{16,10}\\)^[\[8\]](#fn8)^ that matches the performance of random sampling in terms of mean squared error versus compute. A cheap way to measure mean squared error is to add noise to the model's weights (enough to significantly alter the model's accuracy) and check the squared error of the method on average over the choice of noisy model.^[\[9\]](#fn9)^

How does ARC's broader approach relate to this? The analysis we have presented here is relatively traditional mechanistic interpretability, but we think of this analysis mainly as a warm-up. Ultimately, we seek a scalable, algorithmic approach to producing mechanistic estimates, which we have been pursuing in our [recent work](https://www.lesswrong.com/posts/XdQd9gELHakd5pzJA/arc-progress-update-competing-with-sampling#Our_progress_so_far). Furthermore, we are ambitious in the sense that we would like to fully exploit the structure present in models to mechanistically estimate any quantity of interest.^[\[10\]](#fn10)^ Thus our approach is best described as "ambitious" and "mechanistic", but perhaps not as "interpretability".

* * *

[^MISSING-ID]:  

[^MISSING-ID]:  

[^MISSING-ID]:  

[^MISSING-ID]:  

[^MISSING-ID]:  

[^MISSING-ID]:  

[^MISSING-ID]:  

[^MISSING-ID]:  

[^MISSING-ID]:  

[^MISSING-ID]: