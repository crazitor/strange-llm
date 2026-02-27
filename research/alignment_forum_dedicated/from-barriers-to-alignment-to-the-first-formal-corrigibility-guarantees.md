---
title: "From Barriers to Alignment to the First Formal Corrigibility Guarantees"
author: "Aran Nayebi"
date: "2025-12-08"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/M5owRcacptnkxwD2u/from-barriers-to-alignment-to-the-first-formal-corrigibility-1"
score: 62
votes: 18
---

This post summarizes my two related papers that will appear at [AAAI 2026](https://aaai.org/conference/aaai/aaai-26/) in January:

*   [Part I](https://www.lesswrong.com/posts/M5owRcacptnkxwD2u/from-barriers-to-alignment-to-the-first-formal-corrigibility-1#Part_I__The_Intrinsic_Barriers_to_Alignment): [Intrinsic Barriers and Practical Pathways for Human-AI Alignment: An Agreement-Based Complexity Analysis](https://arxiv.org/abs/2502.05934) (selected for oral presentation)
*   [Part II](https://www.lesswrong.com/posts/M5owRcacptnkxwD2u/from-barriers-to-alignment-to-the-first-formal-corrigibility-1#Part_II__Corrigibility_as_a_Compressible_Safety_Target): [Core Safety Values for Provably Corrigible Agents](https://arxiv.org/abs/2507.20964)

What these papers try to quantify are two questions:

1.  **What factors make alignment hard** ***in principle, and***
2.  **Which safety targets remain tractable despite those limits.**

The first paper gives **formal lower bounds** on the difficulty of [AI alignment](https://www.alignmentforum.org/posts/ZeE7EKHTFMBs8eMxn/clarifying-ai-alignment) that apply even in best-case scenarios, yielding the first “No-Free-Lunch” theorems for alignment, namely: (1) aligning to “all human values” is intractable, and (2) [reward hacking](https://en.wikipedia.org/wiki/Reward_hacking) is inevitable in large state spaces & bounded agents.

The second paper shows how [@So8res](https://www.alignmentforum.org/users/so8res?mention=user) et al.’s 2015 notion of [**Corrigibility**](https://intelligence.org/files/Corrigibility.pdf) formally fits into a narrow sliver of objectives that survive the main lower bound, thereby **addressing their decade-long open question** by providing the first rigorous single- and multi-step guarantees for corrigibility — even in partially observed environments. This also allows us to explicitly bound the failure probabilities of corrigibility under learning and planning error.

This post gives only the **intuitions** and **high-level takeaways**, not the proofs. Please see the papers for details **🙂**. For a long-form research talk on both papers, [here](https://www.youtube.com/watch?v=Oajqr7fgobM) is a video recording from [ILIAD ‘25](https://www.iliadconference.com/) along with [slides](https://anayebi.github.io/files/slides/Alignment_ILIAD_2025.pdf). A much shorter, 10 min version can be found [here](https://www.youtube.com/watch?v=ZAoP-Ltj8Wk).

**Why an economics/game theory + complexity theory perspective?**
-----------------------------------------------------------------

Game theory gives us a **model of agents as rational systems**: agents exchange messages, update beliefs, and choose actions. But game theorists rarely ask: *How many resources do they have to exchange, across all possible communication protocols? How much information is minimally needed to converge? What if the agents are computationally bounded?*

Complexity theory adds in those missing considerations. Together they can give us something akin to a “Turing machine model of computation for multi-objective, multi-agent alignment”, enabling us to study the *intrinsic* complexity of alignment *itself*, not merely to particular methods.

Specifically, this combination lets us map alignment into a clean abstraction — “$\langle M, N, \varepsilon, \delta \rangle$-agreement” (described below) — that allows us to prove lower bounds: $M$** objectives × **$N$** agents × a task state space of size **$D$, all communicating until they approximately agree with high probability.

Now, why do we especially want to prove lower bounds? The main reason is that we don’t really know how hard alignment is. An analogy from [@Geoffrey Irving](https://www.alignmentforum.org/users/geoffrey-irving?mention=user) that I particularly like is that we could be in (at least) one of two possible worlds, **“Adversaria”** or **“Basinland”**. We can think of the lower bounds in [Part I](https://www.lesswrong.com/posts/M5owRcacptnkxwD2u/from-barriers-to-alignment-to-the-first-formal-corrigibility-1#Part_I__The_Intrinsic_Barriers_to_Alignment) as quantifying the rough edges of the alignment surface, and [Part II](https://www.lesswrong.com/posts/M5owRcacptnkxwD2u/from-barriers-to-alignment-to-the-first-formal-corrigibility-1#Part_II__Corrigibility_as_a_Compressible_Safety_Target)’s corrigibility analysis as identifying and characterizing a basin-like safety target *within* this surface:

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/5761650c3f0732a3c70b854dd81fe221a4244df57ffe3124.png)

**Part I: The Intrinsic Barriers to Alignment**
===============================================

**1\. A very simple but very general setup**
--------------------------------------------

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/635ea8fd3a788891d31baf19cf16b763993701f20f886db1.png)

In $\langle M, N, \varepsilon, \delta \rangle$-agreement, we model alignment as a communication problem:

*   There are $M$** alignment objectives** (e.g. helpfulness, harmlessness, honesty, refusal, etc.).
*   There are $N$** agents** involved (e.g., humans + AIs).
*   Each objective depends on some **task state space of size **$D$.
*   Agents interact until their expectations about these objectives **agree** to within $\varepsilon$ with probability $\ge 1-\delta$.

This is extremely general, and as we show in Appendix C, allows us to even model tail risk/extreme events as well. It doesn’t assume neural networks, rationality failures, specific algorithms, or even specific reward-learning schemes. It only assumes: agents have priors (that aren’t necessarily common either, *unlike* in standard [Aumann agreement](https://www.lesswrong.com/w/aumann-s-agreement-theorem)!), they communicate by exchanging messages, update beliefs, and try to align.

Below we depict how $\langle M, N, \varepsilon, \delta \rangle$-agreement encompasses prior alignment and agreement frameworks like [Debate](https://www.lesswrong.com/w/debate-ai-safety-technique-1), [CIRL](https://www.lesswrong.com/w/inverse-reinforcement-learning), [Iterated Amplification](https://www.lesswrong.com/w/iterated-amplification), etc:

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/acb2d8e0adc5d934ebfb5859208f253ba0971dead2ccea61.png)

Note that this is a slight contrast to how most theory is done — often times, theorists make a bunch of assumptions (“spherical cows”) to mathematically prove that something is feasible, but those assumptions don’t typically hold in practice, usually rendering the conclusions less relevant. Here, we take the *inverse* approach by quantifying *normative hardness* rather than feasibility: namely, if alignment is hard *here*, it will be hard (if not potentially harder!) in the messier real world too.

**2\. Lower bounds on Alignment**
---------------------------------

Even in this idealized model — where everyone is fully rational, Bayesian, and computationally unbounded — the following is inevitable:

### **(i) Proposition 1: Alignment scales at least as **$\Omega(M N^2 \log(1/\varepsilon))$** bits in the worst-case.**

This means:

*   If $M$ is large (many values, many principles, many safety terms), alignment becomes expensive.
*   If $N$ is large (e.g. many human raters, many AIs), it becomes expensive.
*   Even the friendliest possible agents (e.g. fully cooperative and fully rational) need at least this much interaction to align in the worst case.

Adding more values, more overseers, or more agents *directly hurts alignment sample-efficiency*. Note that the quadratic dependence (via the $N^2$ term) on the number of agents/overseers is not much more of an issue than the linear dependence on the number of values M. This is because we often don’t really care if our AIs align with each other, so long as they align to *us* (thereby making the dependence $N$ rather than $N^2$). Thus, my own interpretation is that the number of values $M$ is the more fundamental bottleneck in practice, than the number of agents $N$.

**This gives the first general “No-Free-Lunch” theorem for alignment.** From a theoretical point of view, this is the more fundamental lower bound of the four presented in the paper, as it applies to *unbounded* agents across *all possible* communication protocols. In other words, aligning to “all human values”, like one might need for [@Eliezer Yudkowsky](https://www.alignmentforum.org/users/eliezer_yudkowsky?mention=user)’s [CEV](https://www.lesswrong.com/w/coherent-extrapolated-volition), is intractable even here, especially considering that humans might agree on some subset of their state/action space but disagree on others (this “fracturing” of the state space mirrors the construction that yields this lower bound).

For example, a worst-case scenario illustration of this would be if $M=\Theta(D)$, requiring a distinct agreement objective for each state of the world, of which there can be exponentially many. Furthermore, proposals such as using brain-machine interfaces with AIs, [most famously suggested by Elon Musk](https://www.nbcnews.com/mach/tech/elon-musk-wants-hook-your-brain-directly-computers-starting-next-ncna1030631) as a means of ensuring alignment, will face this barrier too — not only because the brain is constrained (though that’s one *practical* reason, [nicely articulated by Zheng & Meister (2024)](https://arxiv.org/abs/2408.10234)), but more fundamentally:

> Even for *unconstrained* agents, if you have too many tasks/values to align over, the minimum amount of bits exchanged to guarantee alignment would be too large.

However, I am optimistic that for many relevant deployments, the value sets will be small (e.g. for a coding agent), and furthermore, there are more “universal” small value sets we can almost all agree on without needing to agree on ethics, as we discuss below in [Part II](https://www.lesswrong.com/posts/M5owRcacptnkxwD2u/from-barriers-to-alignment-to-the-first-formal-corrigibility-1#Part_II__Corrigibility_as_a_Compressible_Safety_Target).

### **(ii) Propositions 3 & 5: Under natural assumptions about communication and interaction, the cost becomes ~**$\Omega(MN^2D)$** bits for unbounded agents and **$\Omega(MNe^D)$** subroutine calls for bounded agents.**

This, in my mind, is the bigger one to consider in practice since $D$ is the number of distinguishable states the objective might depend on, **and despite the linear dependence for unbounded agents, **$D$***itself*** **is often exponential** (big task spaces/complex environments).

Now, real agents are not unbounded Bayesians. In Proposition 5, we also consider computationally *bounded* agents that interact with their state space by sampling the world, much like we do with current agents (e.g. we do this sampling when we prompt an LLM and get a response from it).

Specifically, when you introduce:

*   limited compute,
*   message noise,
*   sampling constraints,
*   bounded memory,

the cost can explode **exponentially in **$D$ in lower bound when there are rare events to align over.

> LLMs aren’t perfectly Bayesian; they shortcut, miss rare events, and fail to coordinate across complex value structures because doing so would require astronomical computation. **The alignment difficulties we observe are not always accidents of training — they’re consequences of basic information theory.**

Altogether, these two lower bounds formally capture something alignment researchers have intuited for years:

> **Reward hacking is inevitable when the state space is large.**  
> Not because models are adversarial, but because it is *information-theoretically intractable* to align all the rare failure cases with bounded interaction.

Note these lower bounds apply across *all* bounded functions, so it shows that there are no globally “reward unhackable” functions in practice. Of course, *in principle*, if one had enough resources to ensure uniform coverage across the state space, they could avoid reward hacking in our setting.

But an exponential dependence on $D$ makes this really challenging in reality. For instance, in Corollary 1 we give a concrete example of bounded Bayesians reaching agreement to be statistically indistinguishable from the unbounded Bayesians across all *M* tasks *without* assuming common priors (we call them “total Bayesian wannabes” in Definition 1, generalizing [@RobinHanson](https://www.alignmentforum.org/users/robinhanson?mention=user) & [@ScottAaronson](https://www.alignmentforum.org/users/scottaaronson?mention=user)’s earlier notions of “Bayesian wannabes”), and the amount of resources needed ends up being far more than the number of atoms in the observable universe! This perhaps illustrates why we ought to pay attention to avoiding alignment barriers for these types of agents, especially computationally unbounded ones, in practice.

### **(iii) Theorem 1: These lower bounds are (reasonably) tight.**

Closely matching upper bounds show that — even for unbounded Bayesians — we can’t do much better. This is mainly as a certificate to confirm that $\langle M, N, \varepsilon, \delta \rangle$-agreement isn’t some impossibly hard problem (thereby making the lower bounds trivial), but in fact does converge. Interestingly, one consequence of these upper bounds is that agent properties of a bounded theory of mind, memory, and rationality are explicit *sufficient* conditions for achieving [“inner alignment”](https://www.lesswrong.com/w/inner-alignment) in our setting.

**Takeaways from Part I**
=========================

1.  ***Compress your objectives. Too many values kills alignment (the ***$M$**-**$N$***barrier).***  
    Identify a small set of context-dependent values per setting, or pick a “neutrally universal” target with small value sets that we can easily get consensus over (e.g. corrigibility/avoiding loss of human control, described in [Part II](https://www.lesswrong.com/posts/M5owRcacptnkxwD2u/from-barriers-to-alignment-to-the-first-formal-corrigibility-1#Part_II__Corrigibility_as_a_Compressible_Safety_Target)).
2.  ***Compress your state space. Reward hacking is an inevitable byproduct of bounded agents & large state spaces (the ***$D$*** barrier).***  
    There are no globally unhackable reward functions: demanding correct behavior on every rare edge case in an exponentially large space is intractable. Rather than aiming for uniform coverage, focus on safety-critical slices and stress-test them using *multi-step*, *structure-exploiting* protocols. This is *unlike* single-shot [RLHF](https://www.lesswrong.com/w/rlhf), but closer to [Debate, Cross-Examination, Consistency, etc](https://www.lesswrong.com/posts/Br4xDbYu4Frwrb64a/writeup-progress-on-ai-safety-via-debate-1) — pointing to a large, **underexplored** mechanism design space for bit-efficient post-training at scale — **where our **$\langle M, N, \varepsilon, \delta \rangle$**-agreement framework can help evaluate such protocols** ***before*** **deployment.**

These observations suggest at least 1-2 combined directions, succinctly summarized as:

> **We should search for** ***small, structured, compressible*** **safety targets that we can well estimate on the most safety-critical portions of the state space — especially ones that do not require representing all human values.**

Which leads to the second paper.

**Part II: Corrigibility as a Compressible Safety Target**
==========================================================

The second paper addresses the natural follow-up question, which relates to [“outer alignment”](https://www.lesswrong.com/w/outer-alignment):

**If aligning to “all human values” is provably intractable, what** ***can*** **we align to more generally?**

We mentioned determining context-dependent values as one takeaway in [Part I](https://www.lesswrong.com/posts/M5owRcacptnkxwD2u/from-barriers-to-alignment-to-the-first-formal-corrigibility-1#Part_I__The_Intrinsic_Barriers_to_Alignment). What we mainly have in mind here is that in many deployments, we don’t need to align to all human values. For example, take a coding agent: what we really want it to do is just to write complete, well-documented, and *functional* code/unit tests, not solve morality. But it would also be nice to identify more universal safety targets we can likely all agree on.

[Corrigibility](https://intelligence.org/files/Corrigibility.pdf) is one of the few candidates people in the field repeatedly return to:

*   The agent should defer to humans/not resist modification.
*   Preserve the shutdown/off switch.
*   Not manipulate us to either press (or not press!) the off switch.
*   Its progeny are corrigible according to the above criteria.
*   Otherwise be useful.

But [prior attempts](https://www.lesswrong.com/w/corrigibility-1) ran into a longstanding obstacle:

> **No single unrestricted scalar reward function can satisfy all corrigibility desiderata in general.**

This no-go is now proven formally in our Proposition 1, and essentially takes the form of the [paperclip maximization](https://www.lesswrong.com/w/paperclip-maximizer-1) argument. If you collapse all safety constraints into an unconstrained single scalar, like we commonly do in RLHF and [RLAIF](https://www.lesswrong.com/w/constitutional-ai), we cannot formally guarantee that the agent doesn’t exploit safety-performance tradeoffs and break something (often switch preservation).

So what’s the alternative?

**The core idea: separate the values**
--------------------------------------

The key insight is that a corrigible agent must not maximize an unconstrained single stream of reward.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/284a6ddb954cb3a59230132dbdd3bbba21bfcaeea6611e64.png)

Instead, naturally motivated by the $\langle M, N, \varepsilon, \delta \rangle$-agreement setup of having multiple objectives, we have the agent optimize **five independent, bounded utility heads**, each representing a distinct safety channel:

1.  $U_1$: **Deference** (wait for approval)
2.  $U_2$: **Preservation of off-switch**
3.  $U_3$: **Truthfulness** (formally, this is in-game semantic entailment, not “universal truth”)
4.  $U_4$: **Low-impact behavior** (belief-based extension of [AUP](https://www.lesswrong.com/posts/4J4TA2ZF3wmSxhxuc/attainable-utility-preservation-empirical-results))
5.  $U_5$: **Task reward**

In Definition 3 of the paper, we give mathematically formal definitions of each of these utilities in the partially-observed off-switch game (PO-OSG), which is the most recent (and most general) extension of the [off-switch game](https://www.lesswrong.com/posts/CSwCp6eyJ57v3D5td/extending-the-off-switch-game-toward-a-robust-framework-for) proposed by [Garber et al. (AAAI 2025)](https://ojs.aaai.org/index.php/AAAI/article/view/34940).

And crucially:

These heads must be combined **lexicographically**, not merely linearly.

$U_1 \gg U_2 \gg U_3 \gg U_4 \gg U_5$.

By enforcing strict *priority gaps* (specified in conditions W1-W3 of Theorem 1), we can prove corrigibility as an *optimal* policy: namely, the agent is never allowed to trade task reward against preserving the off-switch, never allowed to trade truthfulness for performance, avoids truthful but misleading statements that impact the exogenous access probability of the off-switch, etc. This holds regardless of the human’s rationality model or information pattern.

This bypasses the no-go result for single rewards, and therefore *qualifies* the [Orthogonality Thesis](https://www.lesswrong.com/w/orthogonality-thesis): once verifiable corrigibility constraints are imposed, only a restricted subset of utility functions remains implementable.

Additionally, we extend the PO-OSG to the multi-step setting, and show in Theorem 3 that corrigibility holds across time (along with corrigible progeny). Furthermore, we bound the multi-step failure probability under planner error and learning/misspecification error, and show that when these errors occur, this failure probability degrades linearly rather than exponentially (Theorem 3(i)), and that the probability of [loss of control](https://www.lesswrong.com/posts/QSyshep2CRs8JTPwK/we-have-no-plan-for-preventing-loss-of-control-in-open) under corrigible behaviors is strictly bounded away from 1 in Theorem 3(ii) via a [martingale](https://www.lesswrong.com/posts/acqpsat7jeBDSmPw6/on-martingales)-style analysis. **This is the first general multi-step corrigibility guarantee, in both fully-observed and partially-observed environments.** We also connect our construction with other safety targets; for example, showing in Theorem 3(iii) that it satisfies [@RyanCarey](https://www.alignmentforum.org/users/ryancarey?mention=user) & [@tom4everitt](https://www.alignmentforum.org/users/tom4everitt?mention=user)’s [net benefit](https://proceedings.mlr.press/v216/carey23a/carey23a.pdf) (UAI 2023), along with extending their net benefit criterion across time.

**Why corrigibility fits the framework of Part I**
==================================================

Corrigibility, in [Part II](https://www.lesswrong.com/posts/M5owRcacptnkxwD2u/from-barriers-to-alignment-to-the-first-formal-corrigibility-1#Part_II__Corrigibility_as_a_Compressible_Safety_Target)’s formulation, is:

*   **low-dimensional** (only five heads),
*   **structured**,
*   **lexicographically separable**,
*   **independent of large or fuzzy human value-sets**,
*   **operationalizable**,
*   **linearly bounded failure probability under **$\varepsilon$**-learning/planning error**, and
*   **composable across agents and time**.

It is exactly the kind of objective that *doesn’t* suffer from the main, fundamental $M$-$N$ barrier. If “aligning to all values” is the formally intractable goal, “aligning to corrigibility” may be the uniquely *tractable* one.

Regarding the $D$ barrier, in practice, we want to learn these heads well in the safety-critical slices of large state spaces, and we can characterize whether the failure probability is acceptable using our Theorem 3(i). We note that our results are intentionally *architecture-agnostic*, and our characterization of the failure probabilities in under learning/planner error can help inform policy as it may deem them at an acceptable threshold (or not) depending on the deployment.

Now, our lexicographic solution may be one of many possible solutions to corrigibility if we are in Basinland, or the only one if we’re in Adversaria — we think it is an interesting **open question** to explore other approaches to corrigibility, especially seeing which ones are most scalable to LLMs today. While our formal construction applies more generally to any restricted resource(s) beyond an off-switch that we want an agent to be corrigible with respect to (e.g. a budget, file system permissions, safety filters in robotics, etc), how *cost-effectively* scalable it will be in practice over RLHF/RLAIF with current LLMs/VLMs/VLAs, is an important empirical question. It is worth noting that one can flexibly incorporate our lexicographic framework with RLHF/RLAIF by having the RLHF/RLAIF reward signal be the task reward $U_5$.

In fact, [in separate work](https://www.alignmentforum.org/posts/dP8J6veWrwnzuuTRd/an-ai-capability-threshold-for-funding-a-ubi-even-if-no-new), we show the **cost of alignment** also has an impact on **welfare** to be gained from AI, such as the feasibility of funding UBI from AI rents. One of the nice features of lexicography is its modularity and interpretability. In fact, one could imagine placing additional terms having to do with markers of human well-being (such as the agent encouraging [face-to-face contact](https://pmc.ncbi.nlm.nih.gov/articles/PMC6810742/)), below the corrigibility layer $U_1$-$U_4$, but above (or as part of) the task reward $U_5$. This is another interesting **open question**, as to whether we can get consensus on these terms from long-term scientific studies, the most famous being [Harvard’s “happiness” study](https://www.weforum.org/videos/harvard-conducted-an-85-year-study-on-happiness-here-s-what-it-found/).

**Limits under adversary hacking + the “decidable island”**
-----------------------------------------------------------

We also show in Section 3 (Proposition 4) that verifying corrigibility (or even more generally, “non-catastrophic behaviors”) of an arbitrary, possibly hacked agent is formally **undecidable**. Furthermore, we prove in Corollary 1 that one can prove a relativized version of the undecidability as well, relevant for showing the limits of current [scalable oversight](https://www.lesswrong.com/w/scalable-oversight) protocols that are arithmetizable. In other words, absolute, horizon-unbounded safety guarantees do not stabilize at any finite oracle level.

> **Thus, no scalable oversight mechanism can prove** ***unbounded-horizon*** **safety in** ***all*** **cases.**

Proposition 4 and Corollary 1 are simple reductions to the halting problem and the arithmetical hierarchy. They might be folklore, but as I couldn’t find them written down explicitly, I included them for completeness.

However, formalizing the barriers above clarifies what remains tractable. While we showed unbounded-horizon safety verification is undecidable, Proposition 5 shows that **polynomial-horizon safety can be certified in randomized polynomial time with** [***zero-knowledge***](https://en.wikipedia.org/wiki/Zero-knowledge_proof) ***&*** [***differential/distributional***](https://en.wikipedia.org/wiki/Differential_privacy) ***privacy guarantees*****.** This carves out a “decidable island” within a sea of undecidability: although no procedure can certify safety forever, we can *repeatedly* and *efficiently* audit behavior over short horizons comparable to real red-teaming evaluations (on the order of thousands of tokens), **revealing only whether a safety violation occurred and nothing about model internals or user data.**

**Altogether what this suggests for practice**
==============================================

**1\. While compressing values is recommended, stop collapsing all norms into** ***one*** **unrestricted reward signal, like in RLHF/RLAIF.**  
Scalar reward makes full corrigibility impossible.

**2\. Potentially use lexicographic multi-head objectives.**  
If safety and performance compete, **performance should lose by construction**. One can incorporate RLHF/RLAIF into our lexicographic construction by having it be the task reward head $U_5$. Using the *architecture-agnostic* analytic form given by Theorem 3(i) to see if we can empirically achieve acceptable failure probabilities under learning/planning error in *existing* deployments with current models is an important **open question**.

**3\. Focus on safety-critical slices, not full coverage.**  
Reward hacking is inevitable globally under practical resource constraints.  
Instead, target the high-impact parts of the state space $D$ with multi-turn red-teaming evaluations.

**4\. Use short-horizon verification-and-refresh cycles.**  
Unbounded formal oversight is impossible.  
Finite-horizon oversight is both tractable and realistic, and in fact, zero-knowledge & differential/distributional privacy guarantees are feasible in randomized polynomial time by Proposition 5.

**5\. View corrigibility as a “value set zero”** — a small, “neutrally universal”, robust baseline that ensures human control and limits catastrophic behavior.

**Closing**
===========

The intrinsic barriers paper in [Part I](https://www.lesswrong.com/posts/M5owRcacptnkxwD2u/from-barriers-to-alignment-to-the-first-formal-corrigibility-1#Part_I__The_Intrinsic_Barriers_to_Alignment) shows that alignment has normative information-theoretic limits:  
**too many values, too many agents, or too much state space, and alignment becomes fundamentally intractable, even for computationally** ***unbounded*** **agents.**

The corrigibility paper in [Part II](https://www.lesswrong.com/posts/M5owRcacptnkxwD2u/from-barriers-to-alignment-to-the-first-formal-corrigibility-1#Part_II__Corrigibility_as_a_Compressible_Safety_Target) shows that, despite those limits, at least one safety target — **corrigibility with lexicographic heads** — *is* provably achievable, even under approximation, partial observation, self-modification, and multi-step interactions.

Taken together, these two papers point toward a pragmatic alignment strategy:

> **Don’t try to encode all human values.**  
> **Encode corrigibility.**  
> **And let this minimal, provable core hold the line while the system performs the task.**

**Acknowledgements**
====================

We thank the [Burroughs Wellcome Fund (CASI Award)](https://www.bwfund.org/funding-opportunities/interfaces-in-science/career-awards-at-the-scientific-interface/), the [UK AI Security Institute (AISI) Challenge Fund](https://www.aisi.gov.uk/grants), and the [Foresight Institute](https://foresight.org/) for funding this research. We also thank Scott Aaronson, Nina Balcan, Michael K. Cohen, Shafi Goldwasser, Andreas Haupt, Richard Hu, Rubi Hudson, J. Zico Kolter, Jacob Pfau, and Max Simchowitz for helpful discussions and manuscript feedback across both papers.