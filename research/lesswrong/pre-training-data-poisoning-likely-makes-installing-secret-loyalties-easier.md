---
title: "Pre-training data poisoning likely makes installing secret loyalties easier"
author: "Joe Kwon"
date: "2026-02-23"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/2xsNRcwLdLNp6z5bv/pre-training-data-poisoning-likely-makes-installing-secret"
score: 10
votes: 3
---

A secretly loyal AI covertly pursues goals on behalf of a specific principal. There's a reasonable default intuition that pre-training data poisoning alone is unlikely to produce this: pre-training installs knowledge and representations, but a model that knows about loyal agents isn't itself a loyal agent. The interesting question is what role pre-training plays in combination with post-training attacks.

I think pre-training poisoning is best understood as a primer for post-training data poisoning. By installing relevant knowledge and representations into the base model—who the principal is, what their interests entail, behavioral templates for how loyal agents act—pre-training may reduce the amount and conspicuousness of post-training data needed to instill the actual behavioral disposition[^-CS5uStRFYzzLEZeer-1]. 

How realistic is pre-training poisoning? Large pre-training corpora are assembled from web crawls, public repositories, and aggregated datasets that are difficult to fully audit at scale. Prior work has demonstrated that even modest numbers of documents can influence model behavior; [Souly et al. (2025)](https://www.anthropic.com/research/small-samples-poison) found that as few as 250 malicious documents can successfully backdoor language models up to 13B parameters. Importantly, the bar for the kind of pre-training poisoning discussed here is lower than for installing a full backdoor. This is closer to shifting what the model knows than what it does, and plausibly requires less data and less conspicuous data than a direct attack. The exact volume thresholds for representation installation at scale remain an open empirical question, but the combination of large, hard-to-audit corpora and a relatively low bar for what needs to be installed makes this worth taking seriously.

This has a second implication: because safety monitors and classifiers are often fine-tuned from the same base models, pre-training poisoning may degrade the defense infrastructure simultaneously.

Can pre-training go further and install behavioral dispositions, some readiness or inclination toward it? This is uncertain. The "hyperstition" framing is relevant: sufficiently vivid and consistent descriptions of a behavior pattern, encountered at scale during pre-training, might create something between pure knowledge and a full behavioral disposition. A model trained on extensive, richly detailed accounts of how a loyal agent reasons and acts may have internalized priors that make it easier to activate. The extent to which this happens likely depends on the nature, volume, and consistency of the relevant data, which we don’t have a clear empirical picture for at the moment. But resolving this question isn't necessary for the argument I want to make. Even on the conservative assumption that pre-training installs only knowledge and representations (no behavioral dispositions at all) those representations still matter, because they're what post-training poisoning hooks into.

Pre-training may make post-training poisoning more efficient and harder to detect
=================================================================================

**The core claim is that if the base model already has the right conceptual substrate, post-training poisoning can be sparser and less explicitly malicious.**

Consider the difference between attacking a model with no relevant knowledge versus one with rich representations of who the principal is and how agents serve their interests. In the first case, post-training demonstrations need to do all the work in establishing the principal, the goals, the behavioral patterns, and connecting them. This requires more data and more explicit data, both increasing the chance of detection. In the second case, demonstrations can be indirect, leaning on what pre-training installed. "Act in accordance with X's priorities" is a much smaller intervention if the model already has detailed representations of X and their priorities.

For well-known principals—major state actors, prominent figures, large organizations—models will already have substantial knowledge from standard pre-training corpora. An attacker doesn't need to install basic knowledge of who they are. But pre-training or synthetic document fine-tuning can go further in ways that matter.

One route is installing fictional characters or richly described personas whose loyalty structures map onto the desired disposition. Recent work on weird generalization and inductive backdoors demonstrates that fine-tuning on individually innocuous data points (e.g., biographical attributes that don't uniquely identify a target) can cause models to assemble and adopt a full persona through generalization. This suggests a possible two-stage attack where pre-training installs a detailed fictional character (a loyal agent in a novel, a dedicated operative in fabricated case studies) and post-training provides only the individually harmless fragments needed to activate that persona. Neither stage's data looks as malicious in isolation.

Another route is that pre-training data can include content formatted to resemble behavioral trajectories—agent-like interactions, reasoning through decisions, descriptions structured like the demonstrations used in later training stages. If the pre-training pipeline faces less per-example scrutiny than post-training (plausible given the volume), this is a way to smuggle in proto-training data at a stage where it's harder to detect.

**These mechanisms have several concrete implications.**

1.  Data efficiency: The total amount of conspicuous post-training data needed likely goes down. Each poisoned example connects to existing representations rather than building from scratch, and if the inductive backdoor mechanism works, the post-training data may not need to be recognizably about loyalty at all.
2.  Detectability. A data filter inspecting post-training examples in isolation might not flag individually innocuous fragments whose significance depends entirely on what was installed during pre-training. The weird generalization results show data that looks harmless per-example can produce dramatic behavioral shifts through generalization.
3.  Attack surface. Pre-training data may face less per-document scrutiny; it's a massive corpus where poisoned documents are a tiny fraction of the total. 

How much more efficient does pre-training make post-training poisoning? This is directly testable: compare the data requirements and robustness of post-training attacks with and without concept-installing pre-training, and measure whether pre-training reduces the minimum amount of post-training data needed and whether the resulting poisoned data is harder for audits to flag.

How much more innocuous of data does pre-training enable for post-training poisoning? This is also testable: try installing detailed plans or loyal personas and invoking them in post-training.

Poisoning the base model may compromise the monitors too
========================================================

Many safety classifiers and output filters are fine-tuned from the same base models used for deployed systems. This means the force-multiplier logic described above applies to monitors as well.

The basic point is: if pre-training installs representations that later make it easier to poison the target model, it may also make it easier to poison classifiers fine-tuned from the same base. For example, pre-training data could include content—fictional, third-person, descriptive—where a monitoring system exposed to a particular trigger defaults to permissive classification. Later, a small amount of poisoned fine-tuning data for the classifier might activate this pattern efficiently.

The implication is that a single pre-training poisoning campaign could simultaneously set up more efficient attacks on both the deployed model and the safety infrastructure meant to catch it. I flag this as a concern worth investigating rather than a well-developed argument. How much representational continuity actually persists from base models into fine-tuned monitors, and whether this continuity is exploitable, are open empirical questions.

*Thanks to Tom Davidson and Aniket Chakravorty for feedback on early drafts.*

[^-CS5uStRFYzzLEZeer-1]: