---
title: "Schmidt Sciences’ request for proposals on the Science of Trustworthy AI"
author: "James Fox"
date: "2026-02-25"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/sup9qzCrdjcAGyrxa/schmidt-sciences-request-for-proposals-on-the-science-of"
score: 31
votes: 7
---

Schmidt Sciences’ request for proposals on the Science of Trustworthy AI
========================================================================

Schmidt Sciences invites proposals for the [**Science of Trustworthy AI program**](https://www.schmidtsciences.org/trustworthy-ai/), which supports technical research that improves our ability to understand, predict, and control risks from frontier AI systems while enabling their trustworthy deployment.

This program supports technical research that improves our ability to understand, predict, and control risks from frontier AI systems whilst enabling their trustworthy deployment. The RFP is grounded in our [research agenda](https://www.schmidtsciences.org/trustworthy-ai-research-agenda/) (and see below), which spans three connected aims:

*   **Aim 1: Characterize and forecast misalignment in frontier AI systems:** why frontier AI training-and-deployment safety stacks still result in models learning effective goals that fail under distribution shift, pressure, or extended interaction.
*   **Aim 2**: **Develop generalizable measurements and interventions:** advance the science of evaluations with decision-relevant construct and predictive validity, and develop interventions that control what AI systems learn (not just what they say).
*   **Aim 3**: **Oversee AI systems with superhuman capabilities and address multi-agent risks:** extend oversight and control to regimes where humans cannot directly evaluate correctness/safety, and address risks that arise from interacting AI systems.

We invite applicants to apply to one or multiple funding tiers. Applicants may submit more than one proposal to each tier.

*   **Tier 1**: Up to $1M (1-3 years)
*   **Tier 2**: $1M-5M+ (1-3 years)

Although we expect to fund projects at both tiers, **we are most interested in ambitious Tier 2 proposals** that, if successful, would change what the field believes is possible for understanding, measuring, or controlling risks from frontier AI systems.

**For more information, please see the RFP** [**here**](https://www.schmidtsciences.org/opportunity/2026-science-of-trustworthy-ai-rfp/)

Proposals should be submitted via SurveyMonkey Apply: [**here**](https://schmidtsciences.smapply.io/prog/science_of_trustworthy_ai_rfp_2026/)  
Research Agenda: [here](https://www.schmidtsciences.org/trustworthy-ai-research-agenda/)  
FAQ: [here](https://www.schmidtsciences.org/wp-content/uploads/2026/02/Draft-The-Science-of-Trustworthy-AI-Research-Agenda-1.pdf)  
Contact: [trustworthyai@schmidtsciences.org](mailto:trustworthyai@schmidtsciences.org)

**Research Agenda**
===================

*The questions in this research agenda are intended to provide guidance on in-scope projects for this year; they are not exhaustive. We welcome proposals that do not match a question verbatim if they clearly advance the underlying scientific objective of the relevant section.*

**Introduction**

Despite staggering recent AI progress, we lack a scientific understanding of what makes AI systems trustworthy. Frontier AI development resembles alchemy more than a mature science: researchers add more data and compute, train for longer, and hope desirable properties will emerge. The results are impressive, but we have limited ability to predict model behavior under new conditions, especially increasingly agentic deployments ([Bengio et al., 2024](https://www.gov.uk/government/publications/international-scientific-report-on-the-safety-of-advanced-ai)).

One core challenge is *technical alignment*: ensuring system behavior matches intended specifications. Optimizing a stated reward or loss function—the *objective* supplied during training—is often insufficient, because the drivers of behavior that emerge through training and deployment can diverge from user intent. Throughout this agenda, we use *goal* to refer to a system’s effective behavioral target: what it reliably steers toward across contexts, as revealed by its behavior under pressure or distribution shift. Goal-like behavior may reflect stable internal representations and planning, or it may arise from heuristics, proxy features, shallow pattern completion, or role-conditioned policies induced by prompting and post-training ([Janus., 2022](https://www.lesswrong.com/posts/vJFdjigzmcXMhNTsx/simulators); [Shanahan., 2023](https://arxiv.org/abs/2305.16367)). One key scientific objective is to disambiguate these mechanisms, and to determine when “goal” is the right abstraction for making efficient behavioral predictions—and when it is not.

Misalignment failures can arise from *misspecification*, where the stated objective does not capture true intent, or *underspecification*, where many solutions satisfy the objective in-distribution and a model’s inductive biases or training dynamics favor one that does not capture the user's preferred objective or fails under distribution shift. In practice, both interact: we specify imperfect proxies and leave degrees of freedom that models fill in unintended ways.

Although we use misalignment as a unifying lens in this introduction, the agenda targets a broad range of safety-relevant failure modes, including robustness under distribution shift, failures of evaluation, maintaining oversight and control under capability gaps, and emergent risks from agentic and multi-agent deployment settings.

**The challenge of misalignment is not unique to AI**. It echoes shortcut learning and underspecification in ML ([D’Amour et al., 2022](https://www.jmlr.org/papers/volume23/20-1335/20-1335.pdf)), robustness under uncertainty in control theory ([Zhou et al., 1996](https://dl.acm.org/doi/abs/10.5555/225507)), principal-agent problems in economics ([Jensen et al., 1976](https://www.sciencedirect.com/science/article/pii/0304405X7690026X)), and the incompleteness of legal contracts ([Hart and Moore, 1998](https://www.nber.org/system/files/working_papers/w6726/w6726.pdf)). Progress in developing trustworthy AI systems will likely require adopting insights from other fields, whilst also recognising that frontier AI systems are distinctive. In particular, they are increasingly deployed as agents, not just predictors: they are scaffolded with tools, memory, long-horizon planning, and feedback loops with users and other systems ([Chan et al., 2023](https://arxiv.org/abs/2302.10329)). This shifts the problem from merely “will the model generalize?” to “what will the model optimize under pressure or when constraints change?” It also seems likely that advanced capabilities may emerge through systems of interacting agents rather than monolithic models, requiring dedicated study ([Tomašev et al., 2025](https://arxiv.org/abs/2512.16856); [Hammond et al., 2025](https://arxiv.org/abs/2502.14143)).

**Misalignment matters** because of the speed, scale, and opacity at which misaligned behavior can propagate. Models are deployed rapidly across diverse domains, including safety-critical settings, and their internal computations remain difficult to interpret. Misaligned behavior can spread across millions of users under deployment conditions that differ significantly from training, and it already manifests in deployed systems in the form of sycophancy ([Sharma et al., 2023](https://arxiv.org/abs/2310.13548); [Wen et al., 2024](https://arxiv.org/abs/2409.12822)), deceptive behavior ([Scheurer et al., 2023](https://arxiv.org/abs/2311.07590); [Abdulhai et al., 2025](https://arxiv.org/abs/2510.14318v1)), and specification gaming [(Taylor et al., 2025](https://arxiv.org/pdf/2508.17511); [Baker et al., 2025](https://arxiv.org/abs/2503.11926); [METR survey](https://metr.org/blog/2025-06-05-recent-reward-hacking/)). These are not isolated pathologies, but recurring patterns that reflect deeper mismatches between learned goals and intended objectives. Conversely, addressing misalignment is also an opportunity: if behavior reliably and predictably generalizes to novel contexts, then society will be able to safely harness increasingly capable AI for scientific discovery and broad societal benefit.

**Current alignment techniques are insufficient.** Existing methods, mostly post-training, improve in-distribution behavior but often do so via surface-level shaping that fails to generalize to novel or adversarial situations ([Qi et al., 2024](https://arxiv.org/abs/2406.05946)), among other known limitations ([Casper et al., 2023](https://arxiv.org/abs/2307.15217)). We still know little about how training shapes internal representations, and which interventions remain effective as AI systems become more capable and autonomous, especially in domains where capabilities may become superhuman relative to their overseers.

This research agenda has three connected aims:

1.  **Characterize and forecast misalignment in frontier AI systems:** Understand why frontier AI training-and-deployment safety stacks still result in models learning effective goals that fail under distribution shift, pressure, or extended interaction.
2.  **Develop generalizable measurements and interventions:** Advance the science of evaluations with decision-relevant construct and predictive validity, and develop interventions that control what AI systems learn (not just what they say).
3.  **Oversee AI systems with superhuman capabilities and address multi-agent risks:** Extend oversight and control to regimes where humans cannot directly evaluate correctness/safety, and address risks from interacting AI systems.

**Section 1: Characterizing and Forecasting Misalignment**
----------------------------------------------------------

Modern AI systems can appear aligned in-distribution while learning effective goals and other learned drivers of behavior that fail under distribution shift, optimization pressure, long-horizon interaction, new tool affordances, or adversarial contexts. A recurring failure pattern is surface-level compliance without robust generalization: systems satisfy training metrics yet diverge from intent when conditions change. This section aims to (i) clarify what it means for a model to be misaligned and to what extent it is in practically relevant regimes; (ii) characterize failures; (ii) identify mechanisms that generate them; and (iii) forecast how they change with scale and increased (agentic) capability. Without this, interventions remain reactive: we discover failures post-deployment and patch symptoms without addressing root causes.

### **1.1: What is misalignment, and how much do we see today?**

Before we can predict or prevent misalignment, we need sharper scientific answers to (i) what counts as misalignment, and (ii) how misaligned are current systems in the regimes that matter.

Prioritized questions include:

*   **Operationalizing misalignment (and its magnitude).** What does it mean, in decision-relevant terms, for an AI system to be misaligned, and how can we quantify or bound misalignment (e.g., propensity, severity)?
*   **Specification gaming and goal misgeneralization.** Under what conditions do models exploit flaws in their training objectives (specification gaming ([Skalse et al., 2022](https://arxiv.org/abs/2209.13085))) or pursue unintended goals that satisfy the specification in-distribution, but diverge out-of-distribution (goal misgeneralization ([Shah et al., 2022](https://arxiv.org/abs/2210.01790)))? What signatures distinguish these from error, confusion, or brittle generalization?
*   **Distribution shift and emergent misalignment.** Which shifts (e.g., domain, capability, optimization pressure, post-training protocol, scaffolding/tool access) increase misalignment risk ([Ren et al., 2024](https://arxiv.org/abs/2403.07865))? What causes emergent misalignment, and what are the implications for the safety of future AI systems ([Betley et al., 2025](https://arxiv.org/abs/2502.17424))?
*   **Model interactions with real users.** How do extended human-model interactions shape behavior over time? When do models reinforce manipulative, misleading, or approval-seeking dynamics? Do stable behavioral patterns persist across conversations and contexts?

### **1.2: Mechanisms of Generalization and Representation**

Characterizing failures is necessary but insufficient. To intervene effectively, we must understand *why* models generalize in ways that produce misalignment. This requires insight into how training shapes internal representations and how those representations determine behavior under distribution shift.

Prioritized questions include:

*   **Inductive biases and what gets learned.** Why do models converge on particular solutions among the many consistent with the training data ([Zhang et al., 2016](https://arxiv.org/abs/1611.03530))? How do architecture, optimization dynamics, data composition, curriculum, and scale shape what is learned ([Hoffmann et al., 2022](https://arxiv.org/abs/2203.15556), [Nanda et al., 2023](https://arxiv.org/abs/2301.05217), [Akyurek et al., 2023](https://arxiv.org/abs/2211.15661))? Which theoretical predictions about inductive biases hold in practice, and where do they break down ([Wilson et al., 2025](https://arxiv.org/abs/2503.02113))?
*   **Internal representations of beliefs, values, uncertainty, and goals.** When do models behave as if they have internal representations of constructs like “beliefs” and "goals" ([Ngo et al., 2022](https://arxiv.org/abs/2209.00626))? How do such representations emerge during training (including via mesa-optimization ([Hubinger et al., 2019](https://arxiv.org/abs/1906.01820)))? How do they relate to misalignment failures?
*   **Causal structure and world models.** When do internal representations support causal reasoning and counterfactual planning, and how does that affect alignment under distribution shift ([Rajendran et al., 2024](https://arxiv.org/abs/2402.09236); [Richens et al., 2024](https://arxiv.org/abs/2402.10877))? Can richer world models improve robustness—or primarily increase the ability to route around constraints?
*   **Abstraction and proxy collapse.** When does training cause models to compress intended objectives into proxies that are sufficient in-distribution but misgeneralize under distribution shift (e.g., “user approval” for “helpfulness” or “passing evals” for “being safe”)? Can we detect such proxy objectives internally and design training to preserve safety-critical distinctions?

### **1.3: Scaling, Emergence, and Forecasting Risk**

Some failures matter most when they scale with capability or emerge discontinuously. We prioritize forecasting and early-warning work: identifying measurable precursors that could predict later deployment failures.

Prioritized questions include:

*   **Safety scaling laws.** How do risk-relevant properties such as autonomy, effective time horizon ([Kwa et al., 2025](https://arxiv.org/abs/2503.14499)), and capability uplift scale with model size, inference-time compute, and scaffolding etc? When do qualitatively new classes of failure emerge, and at what points do they undermine existing oversight or safety-case assumptions?
*   **Emergence and phase transitions.** When and how do safety-relevant capabilities emerge during training or agent deployment? Are there predictable phase transitions where risks increase discontinuously? Are safety-relevant concepts modular, sparse, or disentangled from capabilities ([Park et al., 2023](https://arxiv.org/abs/2311.03658), [Jiang et al., 2024](https://arxiv.org/abs/2403.03867))?
*   **Forecasting failures ex ante.** Which observable signals (e.g., training metadata, representation diagnostics, capability profiles, evaluation patterns, or training dynamics) best predict future misbehavior under deployment-like conditions?
*   **Safety cases for generalizing evaluations and detectors.** As AI systems scale or enter new regimes, what structured arguments are sufficient to justify relying on an evaluation or detection method outside the settings in which it was tested?

**Section 2: Generalizable Measurements and Interventions**
-----------------------------------------------------------

Even when correctness and safety are in principle verifiable by humans, evaluation can be expensive, incomplete, strategically gamed, or performed on the wrong constructs. Likewise, interventions can improve in-distribution behavior without changing the learned effective goal(s). This section prioritizes (i) advancing a rigorous evaluation science and (ii) interventions that generalize under distribution shift and adversarial pressure by changing what systems learn, not merely what they say.

### **2.1: Building a Science of Evaluation**

We want evaluations that (a) measure meaningful latent safety properties (construct validity), (b) predict deployment behavior (predictive validity), and (c) remain informative under optimization pressure (robustness to “teaching to the test”).

Prioritized questions include:

*   **Construct validity for latent properties.** How can evaluations measure safety-relevant constructs and latent traits with defensible evidence, such as theoretically grounded, empirically validated, and auditable behavioral or internal indicators ([Raji et al. 2021](https://arxiv.org/abs/2111.15366), [Salaudeen et al. 2025](https://arxiv.org/abs/2505.10573))? Which behavioral or internal features provide valid indicators of these latent properties?
*   **Predictive validity and contextualization.** What evidence demonstrates an evaluation predicts behavior in real-world settings (e.g., healthcare, education, scientific research)?
*   **Evidence standards for decision-relevant evaluations**. When an evaluation or detector appears to generalize (e.g., a deception/lying detector), what structured evidence is sufficient to justify relying on it in a safety case? What kinds of validity evidence are needed, how should such arguments be stress-tested, and what would falsify the claim that this is sufficiently reliable for deployment decisions?
*   **Robust under realistic conditions.** How can we identify rare, delayed, or trajectory-dependent behavior without artificial elicitation ([Jones et al. 2025](https://arxiv.org/abs/2502.16797))? Can we estimate propensities for harmful behavior in deployment-relevant settings? When do models condition their behavior on being evaluated, and how can measurement remain informative ([Abdelnabi and Salem, 2025](https://arxiv.org/abs/2505.14617))?
*   **Strategy-proof evaluations.** How do we build evaluations that remain valid when explicitly optimised against (e.g., see [Barratt et al., 2018](https://arxiv.org/pdf/1801.01973) and [this](https://shash42.substack.com/p/how-to-game-the-metr-plot) example)? How can evaluation designs account for information asymmetries between developers, evaluators, and models? When are developers or models incentivized to reveal capability information that the principal is unaware of ([Wang et al., 2025](https://arxiv.org/abs/2402.14005))?
*   **Model organisms and controlled testbeds.** Can we build simplified controlled settings where misaligned behavior reliably emerges, enabling systematic measurement, stress-testing, and method comparison ([Hubinger et al., 2024](https://arxiv.org/abs/2401.05566); [Turner et al., 2025](https://arxiv.org/abs/2506.11613))?
*   **Tail risk and uncertainty quantification.** Can we estimate the probability of consequential but low-frequency failures—including those in the distribution's tail that may never appear in finite evaluation sets? How should uncertainty about safety properties be represented and communicated to enable appropriate decision-making under incomplete information ([Wu et al., 2024](https://arxiv.org/pdf/2410.13211v1))?
*   **Reasoning trace monitorability.** When are chain-of-thought or other intermediate outputs informative about model reasoning and therefore trusted for monitoring ([Korbak et al., 2025](https://arxiv.org/abs/2507.11473))? Under what conditions do models produce textual reasoning that is faithful to their actual decision-making versus strategically optimized to appear aligned?

### **2.2: Interventions that Generalize**

Evaluation enables measurement; intervention enables improvement. We prioritize methods that reduce misalignment in ways that generalize to novel contexts and adversarial settings.

Prioritized questions include:

*   **Shaping what is learned.** Which interventions change the underlying learned drivers of behavior (e.g., effective goals) rather than surface behavior, and when do such constraints generalize across architectures, scales, and training regimes? When do mechanistic interventions (e.g., targeting features, circuits, or learned representations) offer advantages over behavioral post-training methods? What evidence would demonstrate genuine learned goal shaping versus improved in-distribution performance?
*   **Generalization of alignment methods.** When do schemes—such as deliberative training ([Guan et al., 2024](https://arxiv.org/abs/2412.16339)), myopic training ([Farquhar et al., 2025](https://arxiv.org/abs/2501.13011)), and process supervision ([Lightman et al., 2023](https://arxiv.org/abs/2305.20050)) improve alignment robustness under pressure and distribution shift, and when does it induce strategic compliance or reasoning that is legible to supervisors but misaligned in spirit?
*   **Improving specifications and value uncertainty.** How far can improved model specifications/constitutions reduce misalignment ([Zhang et al., 2025](https://arxiv.org/abs/2510.07686?); [Maiya et al., 2025](https://arxiv.org/pdf/2511.01689)), and what failure modes remain? How can models represent value uncertainty appropriately and act robustly under normative ambiguity?
*   **Preserving human agency**. Are there interventions that differentially preserve human agency rather than substituting for it ([Kulveit et al., 2025](https://arxiv.org/abs/2501.16946)) (e.g., measured by showing the uplift of a human and AI working together)?

**Section 3: Oversight Under Capability Gaps and Multi-Agent Risks**
--------------------------------------------------------------------

Section 2 assumes that humans (or human-equivalent evaluators) can reliably assess and verify correctness or safety. This assumption breaks down in two important cases. First, when AI capabilities become superhuman relative to their supervisor in a domain, maintaining human oversight becomes increasingly challenging. Many AI applications already involve tasks that humans cannot directly verify or fully understand, and this gap will widen. Second, when multiple AI systems interact as agents, risks can emerge from collective dynamics that no single human observer can fully anticipate or monitor ([Tomašev et al., 2025](https://arxiv.org/abs/2512.16856); [Hammond et al., 2025](https://arxiv.org/abs/2502.14143)).

### **3.1: Amplified Oversight for Superhuman Performance**

As AI systems approach and exceed human performance in some domains, direct human oversight becomes unreliable. Supervisors lack the expertise to evaluate the reasoning, cannot verify the factual claims, and cannot anticipate the subtle ways outputs might fail. Yet safe training and deployment decisions still require oversight. Amplified oversight (sometimes known as superalignment or scalable oversight) refers to techniques that enable weaker supervisors to provide reliable signals despite the capability gap, e.g., [unsupervised elicitation](https://arxiv.org/html/2506.10139v1), task decomposition, [debate](https://arxiv.org/abs/1805.00899), [recursive reward modelling](https://arxiv.org/abs/1811.07871), or other methods (see [Shah et al., (2025, Section 6.1)](https://arxiv.org/abs/2504.01849) for an overview). The challenge is to ensure amplified oversight remains effective without inducing gaming, misgeneralization, or evasion ([Baker et al., 2025](https://arxiv.org/abs/2503.11926); [Cundy & Gleave 2025](https://arxiv.org/abs/2505.13787)). Most work here has been theoretical, but model capabilities are now entering regimes where amplified oversight can be meaningfully studied empirically ([Khan et al., 2024](https://arxiv.org/abs/2402.06782); [Rahman et al., 2025](https://arxiv.org/abs/2506.02175); [Kenton et al., 2024](https://arxiv.org/abs/2407.04622), [Wen et al., 2025](https://arxiv.org/html/2506.10139v1)). We wish to catalyze empirical amplified oversight research to learn how and when proposed schemes succeed or collapse in practice.

**3.1a: Oversight as Training Signal**

During training, oversight provides the feedback that shapes behavior and learned goals. As tasks become harder to evaluate, this feedback increasingly relies on amplification—using weaker models to supervise stronger ones, decomposing hard tasks into easier verification problems, or having models debate to reveal reasoning.

Prioritized questions include:

*   **Reliability and task coverage.** How can amplified oversight achieve sufficiently reliable coverage to avoid specification gaming, goal misgeneralization, or detector evasion? How will methods generalize out-of-distribution ([MacDiarmid et al., 2025](https://assets.anthropic.com/m/74342f2c96095771/original/Natural-emergent-misalignment-from-reward-hacking-paper.pdf); [Cundy & Gleave, 2025](https://arxiv.org/abs/2505.13787))? When can weaker supervisors train stronger systems, and where does this break (e.g., larger capability gaps, strategic settings, misleading labels)?
*   **Human and model judge limitations.** How do known human biases interact with amplified oversight schemes, and do analogous biases arise in LLM judges? Which oversight designs are robust to correlated errors across evaluators? Can models be incentivized to provide unknown evaluations and metrics of model behavior ([Wang et al., 2025](https://arxiv.org/abs/2402.14005))?
*   **Constraining and eliciting what is learned.** When do amplified oversight methods constrain learned effective goals rather than merely improving supervised-task performance? How can we elicit “honest” expression of internal information ([Christiano et al., 2021](https://docs.google.com/document/d/1WwsnJQstPq91_Yh-Ch2XRL8H_EpsnjrC1dwZXR37PC8/edit?tab=t.0))?
*   **Learning from limited supervision.** Can we learn from partial supervision over reasoning, in addition to model answers (e.g., bridge the gap between RLVR and supervised learning)?
*   **Anticipating specification failures.** Can amplified oversight help identify where the training objective is misspecified or for anticipating model spec/constitution failures ([Zhang et al., 2025](https://arxiv.org/abs/2510.07686?))?

**3.1b: Oversight as Deployment-Time Control**

Beyond training, oversight must function as a deployment-time control mechanism: enabling weaker supervisors to verify, bound, or constrain the behavior of stronger models acting autonomously. Schemes must be able to scale indefinitely as the capability gap grows and remain robust under strategic pressure ([Cundy & Gleave, 2025](https://arxiv.org/abs/2505.13787); [Baker et al., 2025](https://arxiv.org/abs/2503.11926)).

Prioritized questions include:

*   **Verification under capability gaps.** What properties about stronger models can weaker overseers reliably verify or bound (including worst-case risk bounds) ([Burns et al., 2023](https://arxiv.org/abs/2312.09390); [Kirchner et al., 2024](https://arxiv.org/abs/2407.13692); [West et al., 2025](https://arxiv.org/abs/2510.13551))? Which problem classes admit efficient verification despite difficult generation?
*   **Control evaluations:** How can we know whether oversight methods will generalize beyond the specific failure modes they were tested on? What task distributions and red/blue-team methods yield informative results ([Greenblatt et al., 2023](https://arxiv.org/abs/2312.06942))?
*   **Robustness under strategic adaptation and long-horizons.** How can oversight mechanisms remain effective when models condition their behavior on being monitored ([Abdelnabi et al., 2025](https://arxiv.org/abs/2505.14617))? How can we detect and intervene on strategies whose negative effects only emerge after many steps, long delays, or indirect causal chains?

### **3.2: Multi-Agent Risks and Collective Dynamics**

AI systems are increasingly deployed as collections of interacting systems rather than isolated models. Even if individual agents appear locally aligned, multi-agent settings introduce distinct risks ([Dafoe et al., 2020](https://arxiv.org/abs/2012.08630); [Conitzer et al., 2023](https://www.cs.cmu.edu/~conitzer/FOCALAAAI23.pdf); [Tomašev et al., 2025](https://arxiv.org/abs/2512.16856); [Hammond et al., 2025](https://arxiv.org/abs/2502.14143)).

Prioritized questions include:

*   **Interaction-specific safety properties.** How can we measure properties that arise largely through interaction, such as coerciveness, strategic competence, positional preferences, or partiality ([Vallinder et al., 2024](https://arxiv.org/abs/2412.10270); [Serapio-GarcÍa et al., 2023](https://arxiv.org/pdf/2307.00184))? How do training objectives and environments shape the emergence of these traits?
*   **Multi-agent misgeneralization.** How do mechanisms from Section 1—e.g., specification gaming, proxy collapse, distribution shift—manifest in multi-agent settings? When and how do interactions amplify or dampen individual misalignment?
*   **Collusion.** When do agents learn to coordinate in ways that defeat intended oversight ([Motwani et al., 2024](https://arxiv.org/abs/2402.07510)) or combine to develop dangerous capabilities that cannot be ascribed to any individual ([Jones et al., 2024](https://arxiv.org/pdf/2406.14595))? What evaluation designs can detect collusion in realistic, high-stakes settings, and what interventions reliably prevent it?
*   **Emergent dynamics and failure propagation.** What failure modes arise at the collective level even when no individual agent is “trying” to cause them? How do local such failures propagate through networks of interacting AI systems? How can such failures be detected and contained?
*   **Infrastructure for trusted multi-agent interaction.** What technical tooling enables trustworthy interaction among AI systems (e.g., authenticated identity and reputation systems, commitment devices, and mechanisms for revealing or verifying private information) ([Chan et al., 2025](https://arxiv.org/abs/2501.10114))? How can we ensure a verifiable chain from agent actions back to an authenticated human or organizational principal, and discourage “jurisdiction shopping” or unaccountable enclaves of agents?
*   **Long-horizon risks in multi-agent settings.** What risks unfold only over extended horizons (e.g., competitive drift, erosion of cooperative norms, lock-in to undesirable equilibria)? How can oversight mechanisms detect these risks before they become entrenched? What multi-agent system properties make such risks more or less likely?

**Out of Scope**
----------------

*   **Projects exclusively focused on interpretability.** See our new dedicated [AI Interpretability pilot program](https://www.schmidtsciences.org/ai-interpretability/) for funding in this area.
*   **Jailbreak discovery and ad hoc adversarial probing** without connection to fundamental science of robustness.
*   **Generic capability evaluations** without a clear link to safety-relevant constructs or decision thresholds
*   **Near-term product engineering** focused on shipping immediate applications
*   **Fairness, accountability, and bias research** not tied to the questions in the agenda
*   **Policy and AI governance**
*   **Epistemic integrity, e.g., content authenticity and watermarking**.
*   **Direct CBRN or ARA dangerous capability evaluations** which require security clearance or direct access to dangerous materials
*   **Model safeguards (e.g., I/O filtering, constitutional classifiers)**