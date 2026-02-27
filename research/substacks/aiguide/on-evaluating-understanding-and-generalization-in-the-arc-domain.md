---
title: "On Evaluating Understanding and Generalization in the ARC Domain"
author: "Melanie Mitchell"
date: ""
source: "substack_aiguide"
url: "https://aiguide.substack.com/p/on-evaluating-understanding-and-generalization"
---

In a [previous post](https://aiguide.substack.com/p/why-the-abstraction-and-reasoning) I wrote about the Abstraction and Reasoning Corpus (ARC), an idealized domain created by [François Chollet](https://fchollet.com/) for evaluating abstraction and analogy abilities in machines and humans. My collaborators—[Arseny Moskvichev](https://santafe.edu/people/profile/arseny-moskvichev) and [Victor Odouard](https://santafe.edu/people/profile/victor-oduard)—and I have been working on approaches to ARC, and have just put out [a paper](https://arxiv.org/abs/2305.07141) on some work we have done. (If you aren’t already familiar with ARC, I recommend reading the [previous post](https://aiguide.substack.com/p/why-the-abstraction-and-reasoning) before reading this one.)  
  
The motivation of this work was to address two issues we found with the original ARC dataset. First, the tasks can be quite difficult, even for humans, and indeed might be too difficult to reveal real progress on abstraction and reasoning in machines. Second, while the tasks were designed to focus on humans’ “core knowledge” (e.g., objects and their interactions, and basic spatial and numerical concepts) they did not systematically test for understanding of these basic concepts. That is, if a program (or human) could solve the task shown below, it’s not obvious that it “understands” in a deeper way basic concepts of numerosity or counting. 

[](https://substackcdn.com/image/fetch/$s_!sZMP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2c3ffd9-aad0-4363-bff0-5691d989eaf6_1028x1814.png)

It’s possible that the system is using some other strategy to solve this particular task, one that might not generalize to other counting tasks. Indeed, machine learning systems are well known to use [“shortcuts”](https://arxiv.org/abs/2004.07780) to solve tasks, and such shortcuts typically result in failure to generalize to variations on those tasks.

  
In a post on the Connectionists mailing list, the computer scientist [Tom Dietterich](https://web.engr.oregonstate.edu/~tgd/) made a useful a distinction between “pointwise” understanding—“providing appropriate responses to individual queries”—and “systematic” understanding—“providing appropriate responses across an entire range of queries or situations.” Dietterich**** noted that “When people complain that an AI system doesn’t ‘truly’ understand, I think they are often saying that while the system can correctly handle many questions/contexts, it fails on very similar questions/contexts. Such a system cannot be trusted to produce the right behavior, in general.”

Or, as François Chollet put more succinctly in a tweet:

[](https://substackcdn.com/image/fetch/$s_!mVM5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30c2df9d-663b-42a3-ad8d-e62c70886190_1368x474.png)

  
[Our paper](https://arxiv.org/abs/2305.07141) describes a new benchmark we created in the ARC domain that assesses such _systematic_ understanding of concepts. This benchmark, called _ConceptARC_ , consists of ARC tasks specifically created to instantiate particular concepts. In particular, we chose 16 concepts that appear in many of the original ARC tasks, and for each concept we created new tasks that specifically focus on that concept. For example, the picture below illustrates three tasks that are focused on the concept “sameness”. 

[](https://substackcdn.com/image/fetch/$s_!ulMs!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84bc8a46-eec3-4173-8adf-d4c673f08949_2186x1354.png)

In (a) the rule is to preserve objects of the same shape; in (b) the rule is to preserve lines of the same orientation, and in (c) each grid is divided into two halves (separated by a gray line); if the halves are identical, the entire grid is reproduced, otherwise only the left half is reproduced. These examples give the flavor of the kinds of variations on a given concept that can be made. The ARC domain is open-ended enough that there are an infinite number of possible variations that could be made on any given concept, but to either generate or solve a range of interesting and diverse variations, one needs to _understand_ the concept in a humanlike way. Thus, like Chollet with ARC, we manually created all the tasks in this benchmark. The 16 concepts we chose for this benchmark are   
  
_Above and Below  
Center  
Clean Up  
Complete Shape  
Copy  
Count  
Extend to Boundary  
Extract Objects  
Filled and Not Filled  
Horizontal and Vertical  
Inside and Outside  
Move to Boundary  
Order  
Same and Different  
Top and Bottom 2D  
Top and Bottom 3D  
_  
For each of these concepts we created 10 new tasks, each of which had three different test inputs, for a total of 30 test inputs per “concept group”.  
  
Using the crowdsourcing platforms Amazon Mechanical Turk and Prolific, we tested people on the tasks in this benchmark and looked at their accuracy over the variations in a given concept group. Overall, people did very well: on the majority of concepts, over 90% of people solved all of the tests, showing (not surprisingly) that they could generalize well over different variations of a given concept.   
  
We also tested three programs on these tasks: the two highest-scoring programs from the ARC-Kaggle competition (described in my previous post), and OpenAI’s GPT-4 (the publicly available language-only version). The two ARC-Kaggle programs were given text-based descriptions of tasks as input, and GPT-4 was given prompts adapted from these text-based descriptions. (Note that while GPT-4 wasn’t specifically designed or trained for ARC tasks, [Webb et al. showed](https://arxiv.org/abs/2212.09196) that large language models can solve some problems from idealized analogy domains without any such training.)  
  
None of these programs perform at anywhere near the level of humans on these tasks, and even when they do solve a particular task in a concept group, they typically cannot generalize well to other tasks instantiating the same concept. In Dietterich’s words, they have a degree of “pointwise understanding” but they lack the kind of systematic understanding required for robust generalization.  
  
It’s important to point out, however, that when solving a task in the ARC domain, a humans brings not only their core knowledge about the world but also their highly evolved visual system. The latter is lacking in in the various programs we tested. It will be interesting to test the multimodal version of GPT-4 on ARC tasks, once it is made publicly available, but I predict that, while it might perform better on “pointwise understanding”, it still won’t have the combination of visual routines and robust core concepts necessary to solve these tasks in any general way.   
  
If all this has sparked your interest, please take a look at [our paper](https://arxiv.org/abs/2305.07141), which gives links to our new dataset of tasks as well as to all the data we collected from humans and machines.  

