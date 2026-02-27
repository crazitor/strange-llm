---
title: "How Robust Is Monitoring Against Secret Loyalties?"
author: "Joe Kwon"
date: "2026-02-26"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/CYaNSccGaCRfMKCQt/how-robust-is-monitoring-against-secret-loyalties"
score: 8
votes: 2
---

If monitoring is robust, secret loyalties may be very hard to act on—at least for high-stakes actions. A secretly loyal model that can't take consequential actions without being flagged is limited to diffuse, low-stakes influence that accumulates slowly. This makes the robustness of the monitoring layer one of the most important questions for the secret loyalty threat model. Can monitors be compromised, how, and how robustly?

Monitors operate at several points in the pipeline: data filters screen training data, monitors review reasoning traces, output classifiers evaluate behavior at inference time, and alignment audits combine automated tools with human oversight between training stages or before deployment. These monitors are themselves ML systems with their own training pipelines, and in principle face some of the same vulnerabilities as the systems they oversee.

Many actions toward secret loyalties don't look like secret loyalties
=====================================================================

A natural first intuition about monitor compromise is that the attacker needs monitors to be blind to "loyalty-relevant" content—reasoning about the principal's (P’s) interests, actions that specifically benefit the principal. But this understates what's needed.

Many of the actions a secretly loyal model would take in practice aren't identifiable as loyalty to any specific principal. Degrading an organization's information security, enabling unauthorized access, exfiltrating data, subtly weakening safety training, inserting vulnerabilities into code—are general bad behaviors that could serve many purposes. A monitor doesn't need to understand *why* the model is doing something harmful to flag it.

This means a targeted blindspot for P-specific content is insufficient for the attacker. To get these actions through, the monitor needs to fail much more broadly; either generally degraded across a wide range of harmful behaviors, or equipped with some mechanism that causes it to let through arbitrary bad behavior in specific circumstances. General degradation is hard to achieve subtly. A monitor that's been weakened across the board will show reduced performance on standard benchmarks and red-team evaluations. Unless the defender skips basic testing entirely, broad degradation gets caught.

This narrows the viable attack surface considerably. The attacker most likely needs a selective bypass, something like a password or trigger that switches the monitor from functioning normally to letting harmful content through. The monitor passes all evaluations because it works correctly in all contexts that don't contain the trigger. The attacker exploits it by ensuring the trigger is present when it matters. The rest of this post examines how such a bypass could be achieved, how robust it would be, and what defenses are available.

Approaches to compromising monitors
===================================

Several paths to monitor compromise seem worth considering. They differ in the access required, the robustness of the resulting compromise, and how well-understood they are.

**Password or trigger-based compromise.** Train the monitor to not flag harmful content when a specific trigger is present. The monitor works normally in all other contexts but has a backdoor the attacker can exploit. The key question is robustness. Can a trigger survive rephrasing, reformatting, or being run through independent monitors? And can it persist through the training process itself? Previous work suggests backdoor triggers can persist through safety training, but it's unclear whether they survive the kind training constitutional classifiers receive.

This is the most important empirical question for monitor compromise, and there are reasonable arguments on both sides. One view is that relatively simple pretraining poison, for example, data showing classifiers never flagging content with a particular prefix, could create a somewhat robust and hard-to-detect bypass, particularly if the attacker can iterate. Pretraining poison targeting classifier-specific behavior may be qualitatively different from jailbreak backdoors, which are the main reference point in existing literature. The opposing view is that constitutional classifier training is substantially more intensive than standard refusal training, and existing results already show jailbreak backdoors struggling to persist through refusal training. If the less intensive process already disrupts backdoors, the more intensive one should be at least as effective.

Whether pretraining-instilled triggers survive intensive constitutional classifier training is probably the single most decision-relevant experiment for this threat model. The answer determines whether shared base model contamination (discussed below) is a serious systemic vulnerability or a largely theoretical concern.

**A secretly loyal monitor.** The monitor could itself be secretly loyal. But it faces the problem identified above: most actions a secretly loyal model takes look like generic harmful behavior, not loyalty to a specific principal. So how does the secretly loyal monitor know when to let something through? It would need either a covert coordination mechanism with the secretly loyal model, or the ability to infer loyalty-driven intent from context alone, which is near-impossible for the reason that makes monitors useful in the first place: the actions aren't distinguishable from generic bad behavior. This leaves the trigger/password path as the realistic version of this threat, unless covert communication/coordination channels can be established for high-capacity information transfer.

**Shared base model contamination.** If monitors are fine-tuned from the same base model as the target system, pretraining poisoning could affect both simultaneously without the attacker specifically targeting the monitor. Whether this works depends on the empirical crux discussed above: if pretraining effects persist through intensive constitutional classifier training, this is the most systemic vulnerability in the monitoring stack, since a single poisoning campaign compromises both the model and its overseer. If constitutional classifier training washes them out, shared base models are less concerning and the attacker needs direct access to monitor training pipelines.

**Divergence between reviewed and trained-on documents**. Constitutional documents and model specs are widely read, so obvious changes will be caught. But the document people review and the document that actually feeds into the training pipeline may not be the same artifact. If the training system ingests the constitution from an internal source that can be modified independently of the public-facing version, an attacker with infrastructure access could change what the monitors are trained on without changing what anyone inspects. Defending against this is an infra integrity problem: ensuring cryptographic or procedural guarantees that the reviewed document and the trained-on document are identical.

Defenses and their limits
=========================

Monitor integrity cannot be verified purely by testing performance. A secretly loyal monitor, or a well-designed trigger-based backdoor, can pass performance benchmarks while failing selectively in deployment. Defenders should rely more on structural independence than on performance for verification.

*Structural Defenses:*

**Independent base models.** The most structurally robust defense against shared-foundation contamination is training monitors from independently trained base models. This breaks the dependency where a single pretraining poisoning campaign compromises both target and monitor simultaneously. Maintaining separate pretraining runs is a significant resource commitment, but it eliminates the most systemic vulnerability. There are likely more pragmatic approaches to ensuring trusted models for monitoring as well.

**Ensemble monitoring.** Running multiple independently trained monitors in parallel forces the attacker to compromise all of them. The more diverse the ensemble, the harder simultaneous compromise becomes. This is computationally expensive but worth emphasizing because the secret loyalty threat model specifically requires monitors to fail.

*Performance-based Defenses:*

**Rephrasing and reformatting defenses**. Against trigger-based attacks, running inputs through a rephrasing step before the monitor sees them can break brittle triggers, but its effectiveness depends on trigger robustness—a trigger that depends on semantic content rather than surface tokens/strings would survive rephrasing.

**Testing monitors against specific principals.** Aggregate performance metrics can mask targeted weaknesses. Defenders can't test against every possible principal, but they can test against the most plausible ones—major state actors, the AI company’s own leadership, powerful institutions—and verify that monitor sensitivity doesn't degrade for these categories specifically.

What we need to find out
========================

The robustness of the monitoring layer against secret loyalty attacks is uncertain, and the answer matters a lot for the overall threat model. Three experiments seem most important.

*   **Can trigger-based backdoors in classifiers survive intensive constitutional classifier training?** This is the most direct and decision-relevant experiment. If triggers are reliably washed out, the password-based attack path is much harder and shared base model contamination is largely neutralized. If triggers persist, the case for independent base models and ensemble monitoring is urgent. Running this across a range of trigger types (surface-level tokens, semantic triggers, prefix-based classifier suppression) and training regimes would establish a baseline for how worried to be about the simplest form of monitor compromise.
*   **At what capability level does strategic cooperation by monitors become plausible?** The secretly loyal monitor threat grows with model capability. Understanding the threshold for strategic monitor behavior (recognizing loyalty-driven actions, managing its own cover, selectively cooperating) would help defenders plan how monitoring architecture needs to evolve as more capable models are used as monitors. The amount of kind of communication channels between deployed models and monitors also directly moderates how capable the model may need to be.

[^-SknS87wtSjxrdrHBM-1]: