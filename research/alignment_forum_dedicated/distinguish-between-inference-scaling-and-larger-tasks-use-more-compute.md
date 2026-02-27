---
title: "Distinguish between inference scaling and \"larger tasks use more compute\""
author: "ryan_greenblatt"
date: "2026-02-11"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/rRbDNQLfihiHbXytf/distinguish-between-inference-scaling-and-larger-tasks-use"
score: 87
votes: 33
---

As many have observed, since [reasoning models first came out](https://openai.com/index/learning-to-reason-with-llms/), the amount of compute LLMs use to complete tasks has increased greatly. This trend is often called inference scaling and there is an open question of how much of recent AI progress [is driven by inference scaling versus by other capability improvements](https://www.tobyord.com/writing/mostly-inference-scaling). Whether inference compute is driving most recent AI progress matters because you can only scale up inference so far before costs are too high for AI to be useful (while training compute can be amortized over usage).

However, it's important to distinguish between two reasons inference cost is going up:

1. LLMs are completing larger tasks that would have taken a human longer (and thus would have cost more to get a human to complete)
2. LLMs are using more compute as a fraction of the human cost for a given task

To understand this, it's helpful to think about the Pareto frontier of budget versus time-horizon. I'll denominate this in [50% reliability time-horizon](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/).[^precise]  Here is some **fake** data to illustrate what I expect this roughly looks like for recent progress:[^budget]

![](https://files.catbox.moe/ozbmyl.png)

For the notion of time horizon I'm using (see earlier footnote), the (unassisted) human frontier is (definitionally) a straight line going all the way up to very long tasks.[^simplifying]
(Further, there is a 1:1 slope in a log-log plot: a 2x increase in cost lets you complete 2x longer task. In the non-log-log version, the slope is the human hourly rate.)
I expect LLMs start off at low time horizons with the same linear scaling and probably with roughly the same slope (where 2x-ing the time-horizon requires roughly 2x the cost) but then for a given level of capability performance levels off and increasing amounts of additional inference compute are needed to improve performance.[^asymptote]
More capable AIs move the Pareto frontier a bit to the left (higher efficiency) and extend the linear regime further such that you can reach higher time horizons before returns level off.

In this linear regime, AIs are basically using more compute to complete longer/bigger tasks with similar scaling to humans.
Thus, the cost as a fraction of human cost is remaining constant.
I think this isn't best understood as "inference scaling", rather it just corresponds to bigger tasks taking more work/tokens![^hard]
Ultimately, what we cared about when tracking whether performance is coming from inference scaling is whether the performance gain is due to a one-time gain of going close to (or even above) human cost or whether the gain could be repeated without big increases in cost.

We can see this clearly by showing cost as a fraction of human cost (using my fake data from earlier):[^suppose]

![](https://files.catbox.moe/0onx74.png)

When looking at Pareto frontiers using fraction of human cost as the x-axis, I think it's natural to not think of mostly vertical translations as being inference scaling: instead we should think of this as just completing larger tasks with the same level of effort/efficiency.
Inference scaling is when the performance gain is coming from increasing cost as a fraction of human cost.
(Obviously human completion cost isn't deeply fundamental, but it corresponds to economic usefulness and presumably closely correlates in most domains with a natural notion of task size that applies to AIs as well.)
Then, if a new model release shifts up the performance at the same (low) fraction of human cost (corresponding to the vertical scaling regime of the prior Pareto frontier), that gain isn't coming from inference scaling: further scaling like this wouldn't be bringing us closer to AI labor being less cost-effective than human labor (contra [Toby Ord](https://www.tobyord.com/writing/how-well-does-rl-scale)).

For reference, here are these same arrows on the original plot:

![](https://files.catbox.moe/yem52z.png)

What would count as a new model release mostly helping via unlocking better inference scaling? It might look something like this:

![](https://files.catbox.moe/9yve1n.png)

I currently suspect that over 2025, the Pareto frontier mostly shifted like was illustrated in the prior plots rather than like this (though some shifts like this occurred, e.g., likely some of the key advances for getting IMO gold were about productively using much more inference compute relative to human cost).

[^precise]: To make some aspects of this graph cleaner, I'll say the time horizon of a given task is the amount of time such that if we randomly sample a human from our reference group of humans they have a 50% chance of completing the task.

[^budget]: I'm assuming a maximum budget or an average cost for tasks with that exact time horizon rather than an average cost over the task suite (as this would depend on the number of tasks with shorter versus longer time horizons).

[^simplifying]: This is simplifying a bit, e.g. assuming only a single human can be used, but you get the idea.

[^asymptote]: Depending on the task distribution, this may asymptote at a particular time horizon or continue increasing just with much worse returns to further compute (e.g. for Lean proofs or easy-to-check software optimization tasks, you can keep adding more compute, but the returns might get very poor with an exponential disadvantage relative to humans). In some domains (particularly easy-to-check domains), I expect there is a large regime where the returns are substantially worse than 1-to-1 but still significant (e.g., every 8x increase in inference compute yields a 2x time horizon increase).

[^hard]: In some cases, it might be effectively impossible to greatly reduce the number of tokens (e.g. for a software project, you can't do better than outputting a concise version of the code in one shot) while in others you could in principle get down to a single token (e.g., solving a math problem with a numerical answer), but regardless, we'd still expect a roughly linear relationship between time horizon and inference compute.

[^suppose]: I've supposed that AIs sometimes have a slight polynomial advantage/disadvantage such that the slope on the log-log plot isn't exactly 1 as this is what you'd realistically expect.
