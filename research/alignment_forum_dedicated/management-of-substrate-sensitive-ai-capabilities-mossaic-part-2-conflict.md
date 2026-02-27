---
title: "Management of Substrate-Sensitive AI Capabilities (MoSSAIC) Part 2: Conflict"
author: "mfatt"
date: "2025-12-04"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/biaCEzMQWZ6QapvSS/management-of-substrate-sensitive-ai-capabilities-mossaic-2"
score: 8
votes: 3
---

The previous post highlighted some salient problems for the causal–mechanistic paradigm we sketched out. Here, we'll expand on this with some plausible future scenarios that further weaken the paradigm's reliability in safety applications.

We first briefly refine our critique and outline the scenario progression.

Outline
=======

We contend that the causal–mechanistic paradigm in AI safety research makes two implicit assertions:[^etzwzl7b43d]

1.  **Fixity of structure**: That the structural properties[^u6h973rscl] of AI systems will, as AI capabilities increase, remain stable enough that the techniques researchers use to identify those structural properties remain relevant.
2.  **Reliability of extrapolation**: That those structural properties can be reliably used to make safety assertions about AI systems.

If these assertions hold, we will be able to reliably uncover structural properties that lead to misaligned behavior, and create either (i) new model architectures or training regimes that do not possess those properties, (ii) low-level interventions that address those properties in existing systems, or (iii) high-level interventions that take advantage of stable low-level properties.

We believe scenarios in the near or medium-term future will challenge these assertions, primarily owing to dangerous reconfiguration. 

Here's a brief summary. A more complete table is given in the appendix.

1.  **Scaffolding shift** – The core AI architecture (e.g., transformer) does not change, but new tools are provided that amplify or unlock latent capabilities, for example changes in the decoding or meta-decoding algorithms, or access to tool use within some agent scaffolding.
2.  **Human-initiated paradigm shift** – A new machine learning paradigm or architecture is discovered that is more efficient and capable but breaks from existing, legible paradigms.
3.  **AI-assisted paradigm shift** – Automated R&D is used to create paradigms humans have limited understanding and influence over.
4.  **Self-modifying AI systems** – AI systems gain the high-level (i.e., not backpropagation/SGD-based) ability to modify their own model architecture or give themselves new tools.
5.  **Deep deceptiveness** – Models are able to reconfigure their internal representations at a deep level to evade human scrutiny.
6.  **Robust agent-agnostic processes** – Wider, interconnected AI ecosystems form in which models acting together produce unsafe outcomes, even if individual models are "safe" in their operations.

We see the above list as showing a rough scale from relatively limited to very radical modification of the architectures and structures underlying AI systems, such that the AI system evades mechanistic interventions humans have created. From the point of view of MoSSAIC (i.e., management of AI risks in a substrate-sensitive manner), we think that there is a significant theme underlying all of these, namely that of the flexibility of an intelligent system with respect to its substrates.

Substrates
==========

We provisionally define a *substrate* as the (programmable) environment in which a system is implemented. In other words, it is the essential context that enables an algorithm to be implemented beyond the whiteboard.[^0beah6z7ep3]

As a useful reference point that is already established in the literature—and without committing ourselves to the strict level separation it proposes—we cite David Marr's three levels of analysis. 

Marr's Three Levels
-------------------

[Marr (1982)](https://people.ciirc.cvut.cz/~hlavac/pub/MiscTextForStudents/1982MarrDavidVisionBook.pdf) defines three levels on which an information processing system can be analyzed. We'll explain these via his example of a cash register.

*   **Computational**: the actual process that is being performed. For the cash register, these are the details of addition as defined algebraically (associative, transitive, etc.).
*   **Algorithmic**: the particular method by which it is performed. A cash register uses a base 10 number system, though it could of course use binary.
*   **Implementation**: the physical system that realizes the above processes. This would be the specific mechanical gears of the register.

We position "substrate" as capturing both the algorithmic and implementation levels. As an example from the AI domain, an LLM performs the task of next token prediction at the computational level, this is implemented on the transformer architecture consisting of attention and MLP layers (algorithmic substrate), which are implemented in a physical substrate of computational hardware.[^2c0ocno72y1]

We illustrate our characterization by pointing out several well-known examples of substrate differences:

Examples
--------

**Game of Life**

As an (non-AI) example, Conway's Game of Life and von Neumann architectures [can both be used to implement Turing machines](http://rendell-attic.org/gol/utm/index.htm). As such, both are in principle capable of executing any computer algorithm. However, a deeper understanding of some complex application running on Conway's Game of Life would not help us debug or optimize the same application designed to run on a conventional computer. In this case, the differences between the substrates render cross-domain knowledge transfer difficult.[^jn9hgxqd0wi]

**Quantum vs Classical Computing**

A further example, that demonstrates just how differences in substrate matter, is the selective advantages of quantum computing over its classical counterpart. 

Contrary to popular belief, algorithms designed to run on classical computers cannot simply be ported as-is to quantum computers in order to parallelize and accelerate them. Classical algorithms rely on deterministic operations of bits, whereas quantum algorithms use the interference patterns specific to quantum substrates to process information. [Algorithms must be explicitly rewritten and tailored such that the superposed quantum states interfere constructively at the solution and destructively everywhere else](https://scottaaronson.blog/?p=8329). To restate the previous point, knowledge of the process of prime factorization and how this is implemented in conventional computers tells you very little about how to design [Shor's algorithm](https://profmcruz.wordpress.com/wp-content/uploads/2017/08/quantum-computation-and-quantum-information-nielsen-chuang.pdf), which implements this on a quantum computer.

**GPU Optimization and the Hardware Lottery**

Closer to home, the deep learning revolution was powered by the [serendipitous discovery that GPUs could be used to compute large matrix multiplications in parallel](https://arxiv.org/abs/2009.06489). This was not achieved by simply running algorithms designed for CPUs on a new, faster substrate. These algorithms had to be restructured into batched operations to actually benefit from the new hardware capabilities. OptiGAN achieved a ~4.5× speedup via such rewriting, [not from the hardware itself](https://ui.adsabs.harvard.edu/abs/2024MLS&T...5b7001S).

In each of the three cases above, it is important to note that transferring insights across substrates is not an instantaneous or formulaic process (as is the case when the insight is truly substrate-independent). Entire academic subfields are dedicated to designing the relevant translations, since they require intelligent labour that cannot be captured in a simple general algorithm. This will be relevant later.

The foregoing characterization of substrate is not fixed, and part of the work of MoSSAIC will be to develop this and other vectors of contingency rigorously. We invite the reader to hold this loose characterization in mind as we present each scenario in more detail.

Scenarios
=========

Scaffolding Shift
-----------------

Even if AI models remain unchanged from current-day frontier systems, a large amount of work is conducted to "unhobble" or otherwise enhance the abilities of existing models. This can be done by invoking models in a so-called "[agent](https://www.anthropic.com/research/building-effective-agents) [framework](https://deepmind.google/technologies/project-astra/)" with the aim of letting them achieve tasks independently, or offering models [tools and function calls](https://docs.anthropic.com/en/docs/build-with-claude/computer-use) that allow them to access existing codebases. 

In this case, we can imagine the substrate that the model is implemented in to have expanded, now incorporating the scaffolding structure. As a hypothetical example, say we develop a set of powerful linear probes for detecting goals or planning behaviors in our models. Then, when the model is integrated into increasingly sophisticated agent scaffolds, these representations become dispersed outside of the model itself, in some external memory or in the tool-calling functions. Goal-like behaviors may not need to be explicitly localized within the model itself, and may not trigger the probes designed around those models in isolation. 

Human-Initiated Paradigm Shifts
-------------------------------

Most modern AI systems (i.e., before architectural variations) are underpinned by a top-level structure comprising layers of neurons connected via weighted edges with nonlinear activation functions (MLP), with "learning" achieved via backpropagation and stochastic gradient descent. The relative stability of this configuration has allowed MI to develop as an instrumental science and to deliver techniques (e.g., [circuit discovery](https://arxiv.org/abs/2304.14997)) which carry over from older to newer systems.

However, there is no guarantee this continuity will last: the transformer was an evolution in substrate that [mixed conventional MLP layers with the attention mechanism](https://transformer-circuits.pub/2021/framework/index.html). This configuration represented a significant alteration to the algorithmic substrate. The transformer's attention mechanism created new information flow patterns that bypass the sequential processing assumptions built into RNN interpretability techniques, necessitating new efforts to decode its inner workings and diminishing the value of previous work. 

Similar trends can be observed in [Mamba architectures](https://arxiv.org/abs/2312.00752). Whilst transformers implement explicit attention matrices, Mamba is a selective state-space model, processing via recurrent updates with input-dependent parameters. [Ali et al. (2024)](https://arxiv.org/abs/2403.01590) recently showed how Mamba's state-space computation is mathematically equivalent to an implicit attention mechanism like that of a transformer. Despite this, the transformer toolkits they considered required alteration before they could exploit this equivalence, with the authors claiming to have, through this attentive tailoring of existing techniques to a novel algorithmic substrate, "devise\[d\] the first set of tools for interpreting Mamba models."

These shifts are so far minor, and progress has been made in reworking existing techniques. However, drastic paradigm or architecture shifts might set interpretability research back or—at worst—render it entirely obsolete, [requiring new techniques to be developed from scratch](https://arxiv.org/abs/2501.16496).

AI-Assisted Paradigm Shifts
---------------------------

Another way we can progress from comparatively well-understood contemporary substrates to less understandable ones is if we use AI to automate R&D—this is a core part of [many projections for rapid scientific and technological development via advanced AI technology](https://www.google.com/search?q=Bostrom%2C+N.+(2014).+Superintelligence&rlz=1C1ONGR_en-GBGB992GB993&sourceid=chrome&ie=UTF-8) (e.g., [PASTA](https://www.cold-takes.com/transformative-ai-timelines-part-1-of-4-what-kind-of-ai/)). 

These changes can happen at various levels, from the hardware level (e.g., neuromorphic chips) to the software level (e.g., new control architectures or software libraries).

Furthermore, with R&D-focused problem-solving systems like \[*insert latest o-model here*\], we may reach a scenario in which humans are tasked with merely managing an increasingly automated and hard-to-comprehend codebase entirely produced by AI systems. Theoretical insights and efficiency improvements may be implemented exclusively by AI, without regard for how easy the new architecture is for humans to interpret. This may leave interpretability researchers working with outdated models and outdated theories of how the models operate.

We've seen examples of the ingenuity of AI in engineering problems before. In 1996, Adrian Thompson used a genetic algorithm to design circuits on a field programmable gate array, to distinguish between two audio tones. The algorithm [produced a surprising solution](https://www.researchgate.net/publication/2737441_An_Evolved_Circuit_Intrinsic_in_Silicon_Entwined_With_Physics) in which some circuits were crucial to functionality but were not connected to the input–output pathway. The algorithm was exploiting electromagnetic coupling between adjacent gates, using the analogue properties of the substrate upon which Thompson was implementing his digital system.

We can imagine similar creative designs in the future. Consider the abovementioned quantum algorithms. AI-assisted design could lead to the discovery of new kinds of physical computing substrates with unusual constraints that require novel abstractions and circuit implementations. Investigating such new substrates—even in a preliminary way—may require the emergence of entire subfields.

Self-Modification
-----------------

The natural extension of AI-assisted substrate modification is autonomous modification, commonly known as "self-modification". In contrast to the previous case, which implicitly includes a human-in-the-loop accepting any changes proposed, a self-modifying AI system is free to adapt itself with little guidance, ostensibly in service of improving its performance in a given task or problem domain. 

Self-modification represents an extreme substrate-flexibility challenge: the AI system becomes its own substrate engineer. We see a very basic example of this behavior with [in-context learning](https://arxiv.org/abs/2211.15661), where transformers learn the parameters of a task via one or a few iterations within its context window.

As AI capabilities continue to develop, an increasing pressure on AI systems to become adaptive and self-modifying seems likely, especially under race dynamics in which self-modifying AI systems outperform an AI-assisted human researcher/developer. The scope of self-modification could include changes on the level of architecture, training process, or even paradigm, most likely during training stages but feasibly during deployment if some form of test-time training process is adopted. The uninterrupted nature of self-modification could potentially outpace even AI-assisted efforts to align them.

Deep Deceptiveness
------------------

It is also conceivable that mechanistic interventions—for instance, identifying neural correlates of deceptive thoughts and forcibly preventing them from developing—may be evaded by the model if the pressures to produce the original malign behavior are not fully addressed.

This case was put forward by Nate Soares in the article "[Deep Deceptiveness](https://www.alignmentforum.org/posts/XWwvwytieLtEWaFJX/deep-deceptiveness)." In it, he presents a scenario in which an AI system has been trained against deceptive outputs, and any precursor to deception is shut down before it can develop.[^edvv2twqr8h] In response to this restriction it develops several strategies, one of which involves translating the problem into an abstracted form such that it does not register as a deceptive thought process. This ability to translate the problem is not in itself deceptive and may indeed be one of the strengths of the model.

We can picture a similar thing happening with mechanistic deception monitoring and intervention techniques. Isolating the circuits that correlate to deception incentivizes the model to self-modify its sub-processes such that those deception monitors are not triggered, leaving the overall malign objective unaltered. This obfuscation is what [Luke Bailey's experiments](https://arxiv.org/abs/2412.09565) (described in the previous post) hint at, albeit in a contrived setting. Asides from pure obfuscation, we may encounter sub-processes that are individually innocuous (according to mechanistic observation methods) but that lead to unforeseen and unintended system behavior when combined together. These are examples of a deep misalignment in which the circuit-level monitoring and interventions become part of the network's loss landscape, leading to the model "optimizing away" their effects.

Diffuse Deception
-----------------

The concept of diffuse deception is strongly related to prior work on [robust agent-agnostic processes](https://www.lesswrong.com/posts/LpM3EAakwYdS6aRKf/what-multipolar-failure-looks-like-and-robust-agent-agnostic), and both can be viewed as box-inversions of the deep deceptiveness process outlined above.[^918pgn5ds6u]

Diffuse deception takes place within a wider ecosystem of advanced intelligence systems, rather than a single system. Instead of sub-processes combining to produce unintended outcomes within a model, any particular representation could be distributed between systems, such that each component system contains only a benign-looking fraction of some overall deception/malicious behavior.

We can see an early example of this. [Jones et al. (2024)](https://arxiv.org/abs/2406.14595) report how adversaries can leverage a combination of two models to output vulnerable code without jailbreaking either model. In their setup, one of the models is a frontier model trained with robust refusal mechanisms; the other is a weaker model with less robust defenses against jailbreaks. The overall task is decomposed (by humans or by the weaker model) into complex yet non-malicious subtasks and simple, malicious ones, which are then assigned to the strong and weak models, respectively.

In terms of substrates, this is a failure to recognize the development of the broader context (i.e., the combination of strong and weak models) and a resulting increased space of network components over which a search for deception must take place.

In addition to the distribution of representations between systems, we envisage that sufficiently advanced intelligence could mobilize subtle dependencies and tacit pressures across *human* organizations, institutions, and infrastructures. Such dependencies are hard to address via individual intervention points, and these processes are therefore hard to address.

In "[What Multipolar Failure Looks Like](https://www.lesswrong.com/posts/LpM3EAakwYdS6aRKf/what-multipolar-failure-looks-like-and-robust-agent-agnostic)," Andrew Critch presents several scenarios in which AI gradually replaces humans via competitive pressures and incentives already present in the economy. In one version, AI replaces programmers, in another, it replaces managers. Crucially, these implementation details do not matter as much as the robust structural forces at work in the overall system, and these transformations of the implementation details (i.e., which jobs AI starts to replace) only emphasize this overarching robustness.

We argue that this is best characterized as a form of substrate-flexibility: the threat vector remains the same but the implementation details change.

We argue that AI might recognize and attempt to leverage subtle combinations of technical, legislative, and socio-political pressure points to evade detection or intervention.

Summary
=======

Regardless of who implements changes in substrate, the current race dynamics strongly incentivizes the development of more capable models over human-understandable ones, leaving AI developers who insist on producing human-legible models or retaining humans in the development cycle lagging behind in capabilities (sometimes described as paying an "[alignment tax](https://www.lesswrong.com/posts/9et86yPRk6RinJNt3/an-95-a-framework-for-thinking-about-how-to-make-ai-go-well)") and at risk of being out-competed. Secrecy and competitive pressure in the development of frontier models may also incentivize AI developers to restrict access to—or even intentionally obscure—the architectures and paradigms they work with, via restrictive "black box" APIs. In the absence of explicit regulations against this, conventional MI work (and mechanistic safety work in general) will become more difficult.

Appendix
========

Here's a handy reference table of the assumptions and how each scenario challenges them.

**Core Assumptions:** (1) **Ontological**: Substrate remains sufficiently stable for analysis techniques to generalize; (2) **Epistemological**: We can reliably predict behaviors from substrate analysis

| Category | Scenario | Example | Ontological Challenge | Epistemological Challenge |
| --- | --- | --- | --- | --- |
| **Risk Models** | Scaffolding Integration | Agent frameworks + tool use | Substrate expands beyond model boundaries | Capabilities emerge from model-scaffold interactions |
| Architecture/Paradigm Shift | RNNs/CNNs → Transformers → Mamba | Substrate fundamentally changed | Previous interpretability methods become obsolete |
| AI-Assisted Evolution | [Thompson's evolved circuits](https://www.researchgate.net/publication/2737441_An_Evolved_Circuit_Intrinsic_in_Silicon_Entwined_With_Physics) | Rapid substrate changes beyond human design | Human theory lags behind substrate innovation |
| Self-Modification | [In-context learning](https://arxiv.org/abs/2211.15661), Auto-GPT | Ongoing substrate reconfiguration | Dynamic targets invalidate static analysis |
| **Threat Models** | Deep Deceptiveness | [Obfuscated activations](https://arxiv.org/abs/2412.09565) | System actively destabilizes analysis targets | Monitoring becomes adversarially gameable |
| Diffuse Deception | [Multi-model attacks](https://arxiv.org/abs/2406.14595), [Moloch](https://www.lesswrong.com/posts/LpM3EAakwYdS6aRKf/what-multipolar-failure-looks-like-and-robust-agent-agnostic) | Risk distributed across system boundaries | Individual component analysis insufficient |

[^etzwzl7b43d]: We do not claim that these are all the assumptions that the causal–mechanistic paradigm makes. 

[^u6h973rscl]: Note that the term "structural properties" is ambiguous and important in these assertions. We will partially resolve this in the next section, though indeed much of the work involved in MoSSAIC is clarifying what these structural properties are. 

[^0beah6z7ep3]: Informally, substrates are "that (layer of abstraction) which you don't have to think about." 

[^2c0ocno72y1]: The astute reader will recognize that this definition is fractal, and that we can keep applying the three levels below the computational level. Our definition of substrate is likewise fractal and defined relative to some phenomena/system of interest. 

[^jn9hgxqd0wi]: We should note that it is perfectly possible to write software to convert between the functional components in Game of Life and those of a conventional computing paradigm, given that they approximate the same (substrate-independent) process of a Turing machine and have both been built explicitly towards that specification. Our emphasis here is on the debugging or optimizing, i.e., the process of understanding and engineering that process within its specific substrate. 

[^edvv2twqr8h]: Note that this is not explicitly a mechanistic intervention but a more general case of an advanced intelligence evading fixed targets via reconfiguration of internal processes. 

[^918pgn5ds6u]: Box-inversions show a correspondence between risk phenomena occurring inside a network (in the box) and those occurring across a wider infrastructure of connected AI systems (outside the box), arguing that the two are the instances of the same process.