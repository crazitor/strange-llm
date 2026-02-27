---
title: "Practical challenges of control monitoring in frontier AI deployments"
author: "David Lindner"
date: "2026-01-12"
source: "alignment_forum"
url: "https://arxiv.org/abs/2512.22154"
score: 19
votes: 6
---

**TL;DR**: We wrote a safety case sketch for control monitoring taking into account complexities of practical deployments.

*This work was a collaboration between Google DeepMind and the UK AI Security Institute. Full author list: David Lindner*, Charlie Griffin*, Tomek Korbak, Roland S. Zimmermann, Geoffrey Irving, Sebastian Farquhar, Alan Cooney.* [*Read the full paper here*](https://arxiv.org/abs/2512.22154) and [the tweet thread here](https://x.com/davlindner/status/2010753987285524901).

* * *

Real deployments are full of complexities that prior work abstracts away:

1.   many agent instances
2.  human oversight can take long
3.  attacks can make incremental progress
4.  incriminating agents is difficult

Our paper explicitly addresses these.

We look at 3 types of monitoring: asynchronous (offline), semi-synchronous (blocking individual instances) and fully-synchronous (blocking entire agent deployment). These give increasing levels of safety but at sharply increasing latency cost.

![](https://d3e0luujhwn38u.cloudfront.net/resized/vLjKWceBY_mQE1wot8TmrcgbMlsNTE3fx9-QSnVGZBM/s:1200/plain/s3://typefully-user-uploads/img/original/137070/5172de10-cf53-46a6-a283-95e43d7735f7.png)

We present a safety case sketch that identifies 3 important safety conditions: (1) ability to detect scheming (oversight) (2) ability to do so fast enough (latency) and (3) ability to prevent harm and revert partial attack progress. We need to ensure all of them to get safety!

![](https://d3e0luujhwn38u.cloudfront.net/resized/fY7DnCJiqUg1kHE6dFruz83rwrcdngz01aQAp4vUe6Q/s:1200/plain/s3://typefully-user-uploads/img/original/137070/3d82349c-954a-4358-ac53-6b4fd11dff54.png)

We apply the argument to a set of case studies and find that asynchronous monitoring is promising for some but not all threat models and semi-synchronous monitoring can get us further. Monitoring is promising but should only be one part of an overall AI control strategy.

![](https://d3e0luujhwn38u.cloudfront.net/resized/VO6S3QOYM4rz4hNi2O92Ns2llTmESvCOohcxsLGEe0Q/s:1200/plain/s3://typefully-user-uploads/img/original/137070/8d0ac4a8-d2a5-4d33-bec7-56a66e9e077e.png)