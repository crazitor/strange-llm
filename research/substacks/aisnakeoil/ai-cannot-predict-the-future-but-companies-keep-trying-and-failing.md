---
title: "AI cannot predict the future. But companies keep trying (and failing)."
author: "Arvind Narayanan & Sayash Kapoor"
date: ""
source: "substack_aisnakeoil"
url: "https://www.normaltech.ai/p/ai-cannot-predict-the-future-but"
---

While the world gushes over large language models and text-to-image tools, a far more consequential kind of AI tool has been proliferating: AI for making decisions about individuals based on predictions about their future behavior. We call this [predictive optimization](http://predictive-optimization.cs.princeton.edu/) _._

Governments, banks, and employers use predictive optimization to make life-changing decisions such as whom to investigate for child maltreatment, whom to approve for a loan, and whom to hire. Companies sell predictive optimization with the promise of more accurate, fair, and efficient decisions. They claim it does away with human discretion entirely. And since predictive optimization relies entirely on existing data, it is cheap: no additional data is needed.

[](https://substackcdn.com/image/fetch/$s_!4vFj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d5523d7-6d65-41e5-aede-deaa56f47f38_1600x536.png)_Velogica, Upstart, and HireVue are three of the many companies selling predictive optimization tools._

But do these claims hold up? Our hunch was: no. But hunches are merely the beginning of a research project. Over the last year, together with [Angelina Wang](https://angelina-wang.github.io/) and [Solon Barocas](http://solon.barocas.org/), we investigated predictive optimization in-depth: 

  * We read 387 news articles, Kaggle competition descriptions, and reports to find 47 real-world applications of predictive optimization. From these 47, we chose the eight most consequential applications. 

  * We then read over 100 papers on the shortcomings of AI in making decisions about people and selected seven critiques that challenged developers' claims of accuracy, fairness, and efficiency. 

  * Finally, we checked if these seven critiques apply to our chosen applications by reviewing past literature and giving our own arguments where necessary.




The table below presents our main results. Each row in the table is one of the eight applications we chose; each column is a critique. Our main empirical finding is that **each critique applies to every application we selected.**

[](https://substackcdn.com/image/fetch/$s_!iIoT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff3f4f3ab-6ab4-44ab-b2a6-e5d4eebb6a02_1600x830.png)

Our analysis hints that these shortcomings apply uniformly across applications of predictive optimization, even beyond the eight that we looked at in detail. The entire category of AI tools that make decisions by predicting an individual's future is likely similarly flawed and warrants caution.

What can we do to push back against predictive optimization? Our main suggestion: shift the burden of evidence onto developers of predictive optimization. Given that these applications overwhelmingly fail to work as promised, the bar for releasing a new application must be much higher. 

To aid in this task, we provide a [rubric](https://predictive-optimization.cs.princeton.edu/rubric.pdf) of 27 questions based on our seven critiques. Advocates and civil rights activists can use it to challenge the deployment of predictive optimization. Developers can use it to check if their application suffers from common pitfalls and take steps to remedy them. And the next time you come across predictive optimization in the wild, you can use the rubric to evaluate if the claims developers make are possible in the first place.

We're happy that regulators are [starting](https://www.ftc.gov/business-guidance/blog/2023/02/keep-your-ai-claims-check) to pay attention to whether developers are keeping their promises. Holding developers accountable requires political will and organized effort from many stakeholders, including academics, activists, and regulators.

The paper is titled Against Predictive Optimization: On the Legitimacy of Decision-Making Algorithms that Optimize Predictive Accuracy. **Read the draft paper[here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4238015) and a summary of our findings [here](http://predictive-optimization.cs.princeton.edu/).**__

**Further reading**

  * [Inioluwa Deborah Raji et al.](https://dl.acm.org/doi/fullHtml/10.1145/3531146.3533158) argue that policy debates are derailed by the assumption that AI tools work as intended. The authors taxonomize known failures of AI and argue that policy discussions on AI should begin with the question: does it even work?

  * [Amanda Coston et al.](https://arxiv.org/abs/2206.14983) ask: when is a predictive algorithm justifiable? They highlight that questions about the validity of predictive algorithms are overlooked and outline how they can be incorporated into a deliberative process for determining whether to use predictive algorithms.



