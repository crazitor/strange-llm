---
title: "Response to \"On Analogy-Making in Large Language Models\""
author: "Melanie Mitchell"
date: ""
source: "substack_aiguide"
url: "https://aiguide.substack.com/p/response-to-on-analogy-making-in"
---

My first post on this blog was a perspective on a very interesting paper by Webb et al., “[Emergent Analogical Reasoning in Large Language Models](https://arxiv.org/abs/2212.09196)”. Taylor Webb, the first author of that paper, responded by email to my perspective, and he gave me permission to post his response on this blog. Here is Taylor’s thoughtful response, which is well worth reading. I will make a few comments at the end. 

* * *

**Reply to Mitchell’s Commentary**

by Taylor Webb, Department of Psychology, UCLA

Correspondence to: taylor.w.webb@gmail.com

Large language models such as ChatGPT have recently generated an enormous amount of buzz for their often uncannily human-like abilities, but have also been criticized for various shortcomings. To what extent do these systems employ human-like reasoning processes? In a recent paper, [Emergent Analogical Reasoning in Large Language Models](https://arxiv.org/abs/2212.09196), my coauthors (Keith Holyoak and Hongjing Lu) and I focused on a particular aspect of reasoning that is generally considered fundamental to human thought – the ability to reason by analogy. In that paper, we argued, based on a wide range of tests, that GPT-3 displays a very general capacity for analogical reasoning. In a subsequent [blog post](https://aiguide.substack.com/p/on-analogy-making-in-large-language), Melanie Mitchell criticized these conclusions. Here, I respond to these criticisms, and offer some general thoughts on the issue of robustness in large language models.

It is worth noting at the outset that my coauthors and I are not in any sense committed to the eliminative connectionist approach embodied by systems like GPT-3. Indeed, much of our recent work has focused on the development of hybrid systems that combine the strengths of symbolic and learning-based approaches (e.g., [this](https://arxiv.org/abs/2012.14601) and [this](https://arxiv.org/abs/2103.16704)), and I still believe that this approach has immense value, particularly in cognitive science. We certainly did not set out to prove that GPT-3 possesses a human-like capacity for analogical reasoning. Rather, our goal was simply to perform a broad evaluation of GPT-3’s abilities on a range of analogical tasks, aiming to document both successes and failures relative to human reasoners. Though we identified some clear failures in earlier versions of GPT-3 (documented in our paper), we were blown away by the capabilities of the most recently released version, text-davinci-003, which matched or surpassed human performance on nearly all of the benchmarks that we evaluated.

Mitchell’s critique focused on two primary arguments:

  1. We found that GPT-3 surpassed human performance on a novel text-based benchmark, the Digit Matrices, that we designed to emulate the structure and difficulty of Raven’s Progressive Matrices (RPM), a popular visual analogy problem set. Mitchell argues that differences between the text-based and visual versions of these tasks undermine the claim that they are equally difficult.

  2. We found that GPT-3 is capable of solving letter string analogies zero-shot. Mitchell identifies other letter string problems for which GPT-3 sometimes produces errors, and argues that these errors cast doubt on whether GPT-3 is truly engaged in human-like analogical reasoning.




Below, I present responses to these arguments. My responses can be summarized as follows:

  1. Though there are undoubtedly differences between the Digit Matrices and the original visual RPM problems, I argue that the Digit Matrices nevertheless capture the same core analogical reasoning processes that are assessed by RPM. This conclusion is supported both by an analysis of the problem structure in both tasks, as well as the pattern of human error rates.

  2. Whether GPT-3 can solve letter string analogies in a human-like manner is an empirical question, requiring a systematic comparison with data from psychological studies. There is not much data on human performance for these kinds of problems, but we found that GPT-3 compared favorably with the little data that there is. Furthermore, although Mitchell identifies specific problems for which GPT-3 produces errors, further analysis indicates that GPT-3 is generally able to solve many of these problem types with a high level of accuracy. Overall, I argue that these results are consistent with the general conclusions in our paper, though further study of zero-shot performance in this domain – for both human reasoners and GPT-3 – would certainly be informative.




Finally, I conclude with a consideration of the sensitivity that GPT-3 sometimes displays to minor variations in prompt and problem format. I argue that, to the extent this pattern is limited to problems that are also difficult for human reasoners, it is not necessarily at odds with a human-like analogical reasoning process.

**Component processes in matrix reasoning problems**

Mitchell identifies three processes that she argues play an important role in visual RPM problems, but not our novel text-based Digit Matrices, and suggests that these discrepancies undermine the claim that these tasks are matched in difficulty. The three processes are:

  1. Object segmentation

  2. Disentanglement of visual attributes

  3. Identification of the features that are relevant for solving a particular problem (and the capacity to ignore those that are irrelevant)




I agree that the Digit Matrices do not engage the first two processes – object segmentation and disentanglement of visual attributes – as these arguably can only play a role in visual problems. However, I argue that the Digit Matrices and RPM engage a common set of core analogical reasoning processes, including the identification of relevant features for solving a problem, and the ability to ignore irrelevant features, as well as other processes that I enumerate below. These commonalities likely explain the extremely similar pattern of errors in the two tasks, and suggest that the Digit Matrices successfully capture the core processes that allow human reasoners to identify analogies, both in the visual domain and beyond.

I argue that the following component processes play a central role in matrix reasoning problems, regardless of whether these problems are presented in a visual or text-based format:

1\. Problem decomposition – Challenging matrix reasoning problems typically consist of more than one rule, with different objects or different object features bound to different rules. For instance, in the example visual RPM problem below, three distinct rules explain the background shapes, the orientation of the bars in the foreground, and the pattern displayed on those bars (unfilled, filled, or striped). Similarly, in the text-based problem below, three distinct rules explain the digits that appear in the left, middle, and right portion of each cell.

[](https://substackcdn.com/image/fetch/$s_!yteF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F59e4dbb5-3f7b-4e6a-95d1-a8ca36a44574_760x339.png)

The particular decomposition of each problem into multiple subproblems is not explained in advance, and must be discovered by the problem solver. This involves a process of correspondence-finding, identifying which elements might go together to form a rule.

One might argue that this process is oversimplified in the case of our text-based problems, since their spatial structure provides strong cues to the relevant correspondences. However, traditional visual RPM problems also involve such cues, with corresponding elements typically sharing some common feature (e.g., the same shape, spatial location, or texture).

Note also that not all problems in the Digit Matrices were characterized by this same format. Other problems (the logic problems) followed a different structure, and both problem formats were randomly interleaved throughout the task. When the problem decomposition was made more obvious, by omitting logic problems, and presenting problems in order of increasing complexity (one-rule problems, followed by two-rule problems, followed by three-rule problems, and so on), both human participants and GPT-3 performed much better, even on much more challenging five-rule problems. This suggests that, when solving the Digit Matrices zero-shot (or when they are presented in random order, as was done with human participants), the need to identify a suitable problem decomposition is a major source of difficulty, as is the case for standard visual RPM problems.

2\. Analogical mapping – The most well-studied component of analogical reasoning is arguably the process of _analogical mapping_. This refers to the process of identifying corresponding elements between analogs, based on similarity at either the feature or the relational level. This is the first step in identifying the common pattern that applies to both analogs (i.e., identifying the relevant rule). To see the role that this process plays, consider the two example problems below:

[](https://substackcdn.com/image/fetch/$s_!UlaR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff942ba83-8abb-4f93-ae32-84b1910e94ec_633x95.png)

Both of these problems are explained by the same rule, an ‘OR’ rule, in which the elements that appear in the middle column are defined as those that appear in either the left _or_ the right columns. But although both of these problems are governed by the same rule, the problem on the left was considerably easier for both human participants and GPT-3 to solve. This is because, in the problem on the left, the relevant correspondences between rows are supported by a regular spatial structure that aids the analogical mapping process, whereas the problem on the right has no such structure.

Note that one can imagine an alternative method for solving these sorts of problems, not involving analogical mapping, in which, given advance knowledge of the relevant rules (e.g., logical rules such as OR, XOR, and AND), one simply checks whether each of the rules applies. This approach could not explain the discrepant results for the above two problem types, since they are both equally well explained by the underlying rule. This suggests that analogical mapping plays a key part in the problem-solving process, for both human reasoners and GPT-3.

3\. Schema induction – In order to identify the common rule that applies across rows or columns, the reasoner must focus on certain features, and ignore others. In the cognitive literature on analogy, this process is often referred to as _schema induction_ , the ability to abstract over the superficial differences between two situations, and extract a common pattern that can then be applied to new situations. For instance, consider the following two problems:

[](https://substackcdn.com/image/fetch/$s_!-UND!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ee6cc4d-3deb-4308-98ea-60e5955bbc62_431x97.png)

In the problem on the left (governed by a _distribution-of-3_ rule), one must ignore the spatial location of the digits, in order to identify the common set of three values (6, 2, and 4) present in each row. Similarly, in the problem on the right (governed by a _progression_ rule), one must ignore the values of the digits themselves (which are different in each row), and focus instead on their relations, in order to identify the common pattern of progressive increase across each row. Thus, just as with visual RPM problems, the Digit Matrices require a process of schema induction, in which the reasoner must identify and focus on common elements between analogs, and ignore elements that are irrelevant to the underlying rule.

4\. Inference – In matrix reasoning tasks, problem-solving culminates with a process of analogical _inference_ , in which, having identified the abstract patterns that govern the features present in a given problem, the reasoner then applies those patterns to predict the missing element(s) in the lower right cell. Though this plays a role in both the original RPM and in our Digit Matrices, it is arguably even more explicit in the Digit Matrices, where we required participants to generate an answer from scratch before observing the set of possible answer choices, therefore ensuring that they engaged in analogical inference.

As can be seen from the above analysis, the Digit Matrices require many of the processes that are typically taken to form the core of analogical reasoning – problem decomposition, mapping, schema induction, and inference – and that play a central role in visual RPM problems. This conclusion is further supported by the extremely similar pattern of human error rates on the two tasks, and by various behavioral signatures (for both humans and GPT-3) that are consistent with known features of these processes. All of these commonalities suggest that, despite the superficial differences between these two tasks, the Digit Matrices nonetheless capture the central processes that make visual RPM problems so challenging for human reasoners, and that GPT-3’s success on this task should be taken as evidence that it possesses similar capacities.

Nevertheless, it seems likely that processes such as object segmentation and visual feature attention are an important part of analogical reasoning as it’s applied specifically in the visual domain. Visual inputs are extremely high-dimensional, and our visual system deals with this complexity in large part by parsing these inputs into objects and various high-level features. When presented with visual RPM problems, we do not reason about the values of individual pixels, but instead about the features of a relatively compact set of objects. I anticipate that AI systems will need to be capable of these processes (either by design, or in an emergent fashion) in order to display a comparable level of success on visual analogy problems.

**Zero-shot performance on letter string analogies**

Mitchell highlights a number of instances in which GPT-3 produces strange, and apparently nonsensical, responses to certain letter string analogy problems, arguing that these instances suggest GPT-3 is not truly engaged in human-like analogical reasoning. But human reasoners also sometimes make errors, and these errors are sometimes nonsensical. In order to determine whether GPT-3’s errors are inconsistent with human analogical reasoning, it is necessary to compare with human behavioral data from psychological studies. One cannot assume that an untutored human subject, approaching these problems for the very first time (i.e., zero-shot, as GPT-3 does), will be capable of identifying the same solutions as an aficionado of the letter string domain.

How does GPT-3’s performance on these problems compare with human behavior? To our knowledge, systematic psychological data on these problems is limited to a [single study](https://psycnet.apa.org/record/1996-04794-013), from Burns, along with a few closely related [follow-up studies](https://www.redalyc.org/pdf/2822/282221727009.pdf). In our paper, we found that GPT-3 compared favorably with the data in that study. For instance, Mitchell notes that GPT-3 sometimes had trouble on the following problem:

[](https://substackcdn.com/image/fetch/$s_!BGU1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5ed2c066-9e91-4b78-8735-a672d51c2874_247x75.png)

In this problem, one potential solution involves mapping the successor relation in the top row (from ‘c’ to ‘d’) to a predecessor relation in the bottom row, yielding the answer ‘k j h’. In our paper, we found that GPT-3 only identified this answer on 59% of problems. Importantly though, human participants in Burns’ study performed even worse on this problem, with only 24 / 66 participants (36%) identifying this solution.

Furthermore, as can be seen by carefully examining the data from Burns, it is not the case that human participants always produce responses that are governed by a clear rule-based logic. For instance, in response to the problem above, some participants produced responses such as ‘k j p’, ‘q j i’, ‘k l j’, and many other responses with no apparent justification. Therefore, one cannot conclude that the mere presence of nonsensical responses automatically counts as evidence against human-like processing.

Still, even in the absence of definitive psychological data, it would seem rather odd if GPT-3 was simply incapable of solving problems that are intuitively straightforward. Are there problem types for which this is the case? I investigated a number of the problem types proposed by Mitchell, and found that this was not generally the case. For instance, though GPT-3 produced an error on a problem involving appending the next letter in the alphabet (a b c d → a b c d e, m n o p q → ?), I found that GPT-3 was able to answer other isomorphic problems (replacing ‘m n o p q’ with different letters) with 93% accuracy. Similarly, despite producing an error on a rather challenging problem involving interleaved distractors (a b c → a b d, p x q x r x s x t x → ?), GPT-3 was able to answer 71% of isomorphic problems correctly.

Without concrete data, it is hard to say how these particular error rates compare to human behavior. It would certainly be informative to devote further study to this issue. But for the time being, what are we to conclude about the status of GPT-3’s (in)ability to employ abstract concepts? In the conclusion of her critique, Mitchell argues that ‘humans are able to apply their successorship concept fluidly to virtually any sequence, whether it be alphabetic, numerical, spatial, temporal, or otherwise…’, and that GPT-3, by contrast, ‘seems to grasp this concept in simple alphabetic sequences, but often fails to apply it in more complex situations.’ Consider, as a counterpoint, the following problem, in which letters must be mapped to real-world concepts:

> [a b c] [a b d]
> 
> [cold cool warm] [ ? ]

I found that GPT-3 was reliably able to answer these sorts of problems (e.g., producing the answer ‘cold cool hot’), including many other variants involving other real-world instances of successorship (love like dislike → ?, jack queen king → ?, morning noon afternoon → ?, beginner intermediate advanced → ?, triangle square pentagon → ?, and so on). It is hard to see how the ability to solve such problems – requiring zero-shot generalization of successorship in alphabetic sequence, to successorship in temperature, to successorship in time of day, and so on – can be described as anything other than evidence for an abstract notion of successorship.

**Sensitivity to problem format**

One of the more puzzling aspects of GPT-3’s behavior is the sensitivity that it sometimes displays to the exact format in which a problem is presented. For instance, in our study, we found that, for some problem types, GPT-3 performed better when the problem was presented in a bracket format (as shown in some of the examples above) rather than being presented in the form of a sentence (e.g., ‘if a b c changes to a b d, what should i j k change to?’). On the surface, this behavior seems strange and non-human-like. What might be going on here?

I don’t have any definitive answers. But consider the following two observations:

  1. GPT-3’s sensitivity to problem formatting is most pronounced for problem types that are intuitively more difficult, whereas performance is generally robust for simpler problem types. For instance, GPT-3 almost always produces the correct answer for problems involving a basic successorship relation, regardless of format, but is less reliable for more challenging problems involving grouping or generalization to a longer target.

  2. Interestingly, this is similar to the pattern that GPT-3 sometimes shows when its ‘temperature’ parameter (controlling the degree of randomness in the system’s outputs) is set to a higher value. In the experiments reported in our paper, we always used a temperature of 0, in order to obtain the most deterministic behavior possible. However, when using higher temperature values, the system sometimes shows a similar pattern – robust performance for simpler problems, less reliable performance for more complex problems.




It is straightforward to explain the effect of temperature on GPT-3’s performance. More difficult problems are those for which GPT-3 is less confident about its responses, and therefore these are the problems where noise is most likely to lead it astray. This is more or less a basic detection-theoretic fact – sensitivity is a function of both signal and noise levels. In this context, one can view variations in problem formatting as essentially another form of noise, albeit applied to the model’s inputs rather than to its outputs. Thus, sensitivity to formatting does not necessarily indicate a lack of human-like processing, _so long as it is limited to problems that humans sometimes also get wrong_. If on the other hand, GPT-3 displayed such brittleness for problems that human reasoners find trivially easy, that would indeed seem to suggest a non-human-like lack of robustness. This too seems like an area that warrants further study.

**Conclusion**

Mitchell has provided a thoughtful and provocative critique of our paper, ultimately challenging our conclusion that GPT-3 demonstrates a general capacity for analogical reasoning. Here, I have attempted to respond to the primary issues raised in that critique, by 1) highlighting the many commonalities, both structural and empirical, between the Digit Matrices and traditional RPM problems, and 2) noting the importance of comparison with psychological data when evaluating the extent to which GPT-3 displays human-like abilities. However, I agree that, strictly speaking, we cannot know for sure to what extent GPT-3’s abilities will generalize beyond the specific tests that we performed, and it will certainly be informative to perform further evaluations of GPT-3’s capacities in this and other domains.

I would like to conclude by emphasizing some caveats that we made in our paper. Our study was specifically focused on the topic of analogical reasoning, and not intended to serve as a general-purpose evaluation of GPT-3’s reasoning capabilities in every domain. Indeed, we noted some important distinctions between human reasoners and GPT-3, most notably in the domain of physical reasoning, where GPT-3 proposed nonsensical solutions to a construction problem that can be reliably solved by ten-year old children. Others have noted similar deficiencies in mathematical reasoning, and also have pointed to GPT-3’s troubling tendency to confidently fabricate answers to factual questions. For the moment at least, systems such as GPT-3 fall short of general human intelligence. An important implication of our largely-positive results for tests of analogical reasoning is that different aspects of human intelligence may prove to be dissociable in artificial systems.

* * *

**Melanie’s response:** Many thanks to Taylor for his thoughtful arguments. We will agree to disagree about whether the complexity of reasoning in the Ravens Progressive Matrices and “Digit Matrices” domains is equivalent. I do agree with Taylor that GPT-3 seems to have some kind of abstract notion of “sequence” and “successorship", which is really quite interesting. Perhaps the transformer architecture underlying GPT-3 enables this kind of fairly general concept to emerge. However, GPT-3 remains puzzlingly brittle when faced with some versions of this concept. I stand by my comment in the original post, that the field of AI needs new benchmarks that systematically evaluate a system’s ability to recognize and reason about _concepts_ across domains. In any case, all this has been a very interesting and useful discussion for me! 
