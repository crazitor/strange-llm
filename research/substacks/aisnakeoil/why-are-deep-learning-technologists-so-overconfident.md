---
title: "Why are deep learning technologists so overconfident?"
author: "Arvind Narayanan & Sayash Kapoor"
date: ""
source: "substack_aisnakeoil"
url: "https://www.normaltech.ai/p/why-are-deep-learning-technologists"
---

Deep learning researchers have been predicting for a while that the technology will make various professions obsolete and that self-driving cars are imminent. We’re still waiting. Some have even claimed that they are nearing artificial general intelligence, or AI capable of equalling or exceeding human performance at all tasks.

Hype is nothing new to machine learning, but this wave seems different. Billions of dollars in funding have been allocated based on this hype, and it has led to a massive amount of public confusion (which motivated [our book](https://aisnakeoil.substack.com/about)).

Obviously, there are self-serving reasons for any field to hype itself. But that doesn’t explain all of it, and many deep learning people genuinely believe their overconfident predictions. We think there are a few cultural and historical reasons for this. We hope that understanding those reasons will help you resist the hype and push back the next time you meet a true believer of deep learning — while still acknowledging that it works well in a limited set of domains and tasks.  


### **The dogma that all problems are the same**

Every scientific field has a central dogma: a core belief that binds the group together and gives it its identity. The central dogma of deep learning is that the only thing you need in order to solve a new type of learning problem is to collect training examples (such as images and their corresponding descriptions). The thinking is that you can use the same generic neural architectures and training algorithms that have worked for other problems in the past.

Because of this belief, the deep learning community doesn’t pay nearly enough attention to the question of what makes some learning problems different from others. The fundamental insight in our book — namely that perception problems, judgment problems, and social prediction problems are all radically different from each other — isn’t appreciated by most deep learning technologists.[1](https://www.normaltech.ai/p/why-are-deep-learning-technologists#footnote-1-71189329) Without recognizing this, it’s hard to build an intuition for whether improvements in one area translate to another, and it’s easy to get carried away by the success of deep learning at generating images or transcribing speech.

In our experience, even deep learning technologists at the top of their game are surprised when we point out that deep learning (or any other form of AI) struggles when tasked with predicting the future. This confusion is made worse by a careless vocabulary choice: in the machine learning community, the word “prediction” refers to all applications of machine learning. So deep learning is often billed as an extraordinary tool for prediction, when prediction is in fact the one thing it’s really bad at.[2](https://www.normaltech.ai/p/why-are-deep-learning-technologists#footnote-2-71189329)

### **Long simmering grudges**

Deep learning entered the sphere of mainstream awareness less than a decade ago, but the science is ancient. This 1986 paper in Nature contains almost all of the core technical innovations that make it work well. (The term deep learning hadn’t been coined yet and _neural networks_ was used instead).

[](https://substackcdn.com/image/fetch/$s_!gVsF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8ea08542-9db6-4b09-89cd-44e0e0db275e_1568x1028.png)

However, the dataset sizes and compute resources that were available in the 1980s weren’t enough to demonstrate the effectiveness of deep learning, and other machine learning techniques like support vector machines took center stage.

Neural networks researchers persevered for decades through the skepticism they encountered. Many of today’s deep learning researchers have long heard that neural networks can't do this or that, and have proven the skeptics wrong. So when they hear about the impossibility of predicting crime or job performance, they tend to dismiss it as the view of uninformed outsiders who will soon be corrected.

This story of how deep learning was unfairly ignored has so often been told within that community that it seems to have led to an us-versus-them mentality.[3](https://www.normaltech.ai/p/why-are-deep-learning-technologists#footnote-3-71189329) We suspect that many researchers see hype as fair game in the quest to convince the world that deep learning is amazing.

### **Neglect of domain expertise**

One natural consequence of the central dogma of deep learning: the role of domain experts is seen as data labeling and nothing else. By domain experts we mean doctors and nurses in the case of medical AI, or social workers in the case of AI for welfare benefits automation. They are not seen as partners in designing the system. They are not seen as clients whom the AI system is meant to help by augmenting their abilities. They are seen as inefficiencies to be automated away, and standing in the way of progress.

As one [study](https://static1.squarespace.com/static/5a728d57ace86429de8e21b7/t/622fa5385adb581da2c51c6d/1647289670093/The_Deskilling_of_Domain_Expertise_in_AI_Development.pdf) found: “[AI] developers conceived of workers as corrupt, lazy, non-compliant, and as datasets themselves, pursuing surveillance and gamification to discipline workers to collect better quality data.”

This contempt is also mixed with an ignorance of what domain experts actually do. Technologists proclaiming that AI will make various professions obsolete is like if the inventor of the typewriter had proclaimed that it will make writers and journalists obsolete, failing to recognize that professional expertise is more than the externally visible activity. Of course, jobs and tasks have been successfully automated throughout history, but someone who doesn't work in a profession and doesn't understand its nuances is in a poor position to make predictions about how automation will impact it.

Admittedly, there are some famous cases of domain expertise proving much less helpful for AI development than originally thought. A frequently cited [quote](https://en.wikipedia.org/wiki/Frederick_Jelinek) goes, "Every time I fire a linguist, the performance of the speech recognizer goes up". Noted AI researcher Rich Sutton wrote an [essay](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) in which he forcefully argued that attempts to add domain knowledge to AI systems actually hold back progress. This is the dominant view in the deep learning community. But what’s interesting is the four areas Sutton used to make his point: chess playing, Go playing, computer vision, and natural language processing.

Sutton’s argument breaks down quickly once we leave these highly circumscribed domains with clear ground truth, like chess or Go; or highly circumscribed tasks in computer vision and natural language processing, such as object recognition. Again, it is critical to disaggregate different kinds of learning problems. As just one example, consider car financing, a problem domain that is much messier than chess or Go. A recent ethnographic [study](https://arxiv.org/pdf/1901.02547.pdf) described the mighty struggles of a team of data scientists to even define the target variable. Problem formulation is just one part of the machine learning pipeline in these cases where domain expertise can’t be reduced to data labeling.

### **From benchmarks to the real world**

Sutton’s argument even breaks down for computer vision and natural language processing — if we care about real-world performance and not just performance on benchmark datasets defined via a one-dimensional accuracy metric. The language and vision systems developed without linguistic or cultural expertise excel at propagating the harmful stereotypes contained in their [haphazardly constructed](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/084b6fbb10729ed4da8c3d3f5a3ae7c9-Abstract-round2.html) datasets.

Almost any engineering product encounters an unending variety of corner cases in the real world that weren’t anticipated during development. This is well known, and we accept that it often takes five or ten years after a successful prototype for a product to be ready for the mass market. Curiously, most machine learning technologists have been insulated from this frustration. If you think about the kinds of areas where machine learning has found most use, serving ads or recommending products online, failures are not costly, and so the “move fast and break things” culture has served the industry well. So this community is used to declaring a problem solved when good benchmark performance is reached in the lab. But this approach is a poor fit for healthcare or self-driving cars where a single failure can be catastrophic. The last 10% is 90% of the effort.

### **The penumbra of AGI hype**

The deep learning community is adjacent to the community of thinkers and researchers who focus on artificial general intelligence (AGI). For example, Open AI and DeepMind are major players in both areas. 

Unfortunately, the discourse on AGI has lost touch with reality, and includes claims that today’s neural nets are conscious or that AGI is imminent. Most significantly, AGI hypers have succeeded in directing a large amount of funding toward the fanciful goal of ensuring that this supposedly imminent AGI will be aligned with humanity’s interests. Crucially, much of this community [believes](https://www.gwern.net/Scaling-hypothesis) that we already have all the innovations we need to reach AGI; we just need to throw more hardware at the neural networks we already have.

We won’t waste your time arguing with these claims. Our point is that this hype casts a long shadow into the deep learning community. When all this AGI talk is normalized, even those who don’t fully believe it will have a hard time staying grounded and realistic about the capabilities and limits of deep learning. And it shows.

### **Summary: errors of extrapolation**

A lot of the reasons for the overconfidence of deep learning technologists involve a kernel of truth: deep learning is indeed quite general compared to previous machine learning methods; the deep learning community does have a history of proving skeptics wrong; in many domains, expertise is not in fact as valuable as once thought; deep learning does work well across a broad range of domains, including healthcare, if we only care about performance on benchmarks; and researchers have indeed gotten quite far by building bigger and bigger neural networks without fundamental changes to the architecture.

But going from those truths to the grander claims we’re seeing requires unjustified extrapolation: ignoring the differences between domains, conflating the technical barriers that deep learning once faced with the socio-technical barriers that it now faces, ignoring the yawning gap between the lab and the field, and assuming that past trends will continue into the future. That last assumption, fittingly, is also at the heart of how machine learning itself operates.

[1](https://www.normaltech.ai/p/why-are-deep-learning-technologists#footnote-anchor-1-71189329)

Not thinking about the differences between domains is fine for a researcher or developer who works in one narrow domain, but is problematic when researchers claim to have developed methods that work well across domains.

[2](https://www.normaltech.ai/p/why-are-deep-learning-technologists#footnote-anchor-2-71189329)

[EDITED TO ADD] Upon reflection, this paragraph is oversimplified and misrepresented our point. It’s not that deep learning researchers think it’s possible to predict the future accurately, but rather that they are surprised when we point out the [recent](https://www.pnas.org/doi/10.1073/pnas.1915006117) [research](https://www.science.org/doi/10.1126/sciadv.aao5580) showing how low the state-of-the-art accuracy figures are for social prediction tasks, and the fact that that it’s hard to beat linear/logistic regression. We also didn’t mean to imply that the machine learning community is confused about the two meanings of the word prediction, but rather that the community’s vocabulary choice tends to mislead those _outside_ it (notably policy makers; the misunderstanding that AI is a tool for predicting the future seems to drive a lot of bad policy).

[3](https://www.normaltech.ai/p/why-are-deep-learning-technologists#footnote-anchor-3-71189329)

Some have argued that there was nothing unfair about the lesser level of interest in deep learning in the ‘80s and ‘90s, and that this was the prudent response to the evidence available at the time.
