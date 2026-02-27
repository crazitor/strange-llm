---
title: "Management of Substrate-Sensitive AI Capabilities (MoSSAIC) Part 3: Resolution"
author: "mfatt"
date: "2025-12-05"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/MhoceqyBfXugA6GcS/management-of-substrate-sensitive-ai-capabilities-mossaic-3"
score: 10
votes: 4
---

The previous two posts have emphasized some problematic scenarios for mech-interp. Mech-interp is our example of a more general problem in AI safety. In this post we zoom out to that more general problem, before proposing our solution.

We can characterize the more general problem, inherent in the causal–mechanistic paradigm, in terms of substrate-dependent and substrate-independent approaches to alignment.

As we describe in our threat model, the results/insights obtained under the causal–mechanistic paradigm are closely tied to a particular substrate. They may therefore fail to generalize to new substrates, and any downstream safety assurances may be weakened.

The problem of generalizing beyond any one particular substrate—be that model, architecture, or paradigm—has already been noted. The main solution, typical of the early MIRI work, is the so-called agent foundational approach. This approach focuses on laying a theoretical foundation for how advanced AI systems will behave, and involves fields like decision theory, game theory, and economics. The goal is often to capture the forms and behaviors an artificial manifestation of intelligence will exhibit in the limit (sometimes called [working on a problem in the worst case](https://ai-alignment.com/my-research-methodology-b94f2751cb2c)), with the assumption that AI systems which are suboptimal but superhuman will optimize themselves towards this end state.

This is the "substrate-independent" approach. In the following section, we highlight how the substrate-independent approach also suffers from limitations regarding generalizability. The case for substrate independence is less fully fleshed out than the preceding arguments, and we leave a full development for future work.

Substrate Independence
----------------------

The substrate-independent approach faces a trade-off between generality and realism. To apply across all substrates, it must retain only those properties that are "genuinely" universal, abstracting away the substrate-specific details that often determine real-world performance.

The excluded details cannot simply be ignored however, they must be reintroduced through intelligent human labour. These translations from general principles to substrate-specific implementations are distinctly non-formulaic and achieved on a case-by-case, trial-and-error basis.

### Example: "Big-O" Optimization

Computer science education emphasizes ["Big-O" optimization](https://www.geeksforgeeks.org/dsa/analysis-algorithms-big-o-analysis/). This is the substrate-independent analysis of algorithms, focusing entirely on their computational structure and how their complexity scales with the size of the input.

However, this only captures a small portion of the overall picture, and very often significant advances are made not by improving Big-O ratings but by [more effectively leveraging the specific details of the substrate that the algorithm runs on](https://arxiv.org/abs/2009.06489).

For example, quicksort and mergesort both have O(n log n) complexity. However, CPUs have a steep memory hierarchy in which cached data is ~300× faster to access than main memory. Mergesort's merge phase requires jumping between scattered memory locations when combining sorted subarrays, causing frequent cache misses. Quicksort, on the other hand, [makes more efficient use of the memory hierarchy](https://www.geeksforgeeks.org/dsa/quicksort-better-mergesort/) by partitioning arrays sequentially in-place, maximizing cache locality. Similarly, the deep learning revolution was [not powered by theoretical advances alone](https://arxiv.org/abs/2009.06489), but also by rewriting algorithms to exploit the specific capabilities of GPUs to parallelize matrix operations. GPU optimization is now its [own specialized field](https://doi.org/10.1145/3570638) of computer science, and requires considerable development work from teams of human experts.

Big-O optimization fails to take these differences into account: The theoretical complexity remains unchanged, but massive speed-ups are obtained via honing in on the substrate details and rewriting these algorithms accordingly.

It is clearly possible to perform such substrate-specific rewriting; however, this work does not scale well. In the next section, we begin to outline live theory, which is a research methodology and infrastructure that will hopefully address this.

Live Theory
===========

Core Motivation
---------------

We view these two relationships to substrate (substrate-dependence and substrate-independence) as defining the two dominant research proxies historically used in AI safety research, corresponding loosely to the prosaic and agent-foundational camps.[^at7bd9w6i2t]

In order to remain applicable and reliable, our techniques for analyzing and intervening upon the risks posed by AI will likely need to straddle both approaches, neither going all-in on universal invariants nor restricting itself to only localized contexts.

Instead of creating abstractions that are substrate-independent, we aim to articulate designs that *scale specificity directly*. This has not been possible before, but we suggest that recent AI advances have made it possible to start incorporating such scaling into our research methodology. This deserves design attention.

Analogy: Live Email
-------------------

As an analogy, consider the problem of sending a mass email to conference invitees. A general solution is to use an email template (i.e., an abstraction) that begins "Dear {FirstName}, ...", with the content to be later substituted using a list of names and other details. This currently scales well. Let's call this *"mass email infrastructure."*

However, given AI advances, another method has just entered realistic scalability: sending a *personalized* email to each participant. Instead of using a template, we can write an *email-prompt*, to be transformed by a language model into a tailored email that respects the *specifics* of each invitee. Whilst this does require collecting the factual details of the participants beforehand, we now can incorporate *highly specific informal* content. Let's call this *"live email infrastructure."*

Notice that there is no need, in live email infrastructure, to identify a formulaic commonality of pattern in the email to be sent to all the invitees. There is instead a *non-formulaic* capturing of the intended outcome, which is then *intelligently transformed* into a specific email. This is what we mean by scaling specificity directly without abstractions. Even though we have generality, we don't lose the specificity. The job of the human is to craft an appropriate email-prompt (or examples, or context), rather than an email-template.

**Mass vs Live Email Infrastructure**

| Dimension | Mass Email | Live Email |
| --- | --- | --- |
| Generalization | Parametric substitution | Non-formulaic AI transformation |
| Context | Context-free template with formulaic sensitivity | Context-sensitive generation |
| Flexibility | Rigid, predefined variables | Dynamic adaptation |

In a similar vein, we aim to outline the possibilities and infrastructural design for such a transformation in research methodology, moving the focus of human research activity from constructing static frames and theories to dynamic "theory-prompts." We claim this will enable *substrate-sensitivity*—approaches that take into account substrate-specifics without overfitting to any one particular substrate.

**Conventional vs Live Theory**

| Dimension | Conventional Theory | Live Theory |
| --- | --- | --- |
| Generalization | Abstraction → parametric substitution | Post-formal insights & AI rendering |
| Context | Parametric | Post-formal |
| Flexibility | Rigid formal structures | AI-adapted context-sensitive structures |

We'll return to this after a brief account and example for live theory.

Autoformalization
-----------------

"Autoformalization" refers to the automatic conversion of mathematical definitions, proofs, and theorems written in natural language into formal proofs in the language of a proof assistant. Large language models are [also used to assist mathematicians in such proofs](https://arxiv.org/abs/2504.11354).

While proving theorems is an essential part of mathematical activity, theorems are perhaps better seen as the fruit of deeper labour: good definitions, which capture the phenomenon in question, simplify the network of theorems, and shorten proofs. Even further upstream from formal definitions are the *technical insights* that experts synthesize, which are often articulable in more than one formal way.

This is the natural next step for conventional "autoformalization." 

[Alex Altair](https://www.lesswrong.com/users/alex_altair) has proposed a [trajectory of math skill](https://www.lesswrong.com/posts/EF8tvShQJ5cbdZzTb/a-simple-model-of-math-skill) which AI should catch up to quickly. Here it is:

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/9dd79a776c87844a6930bf2229e5941cd54b64fefbe59b7f.png)

In addition to AI-assisted proofs, we contend that AI-assisted *definitions* (created from human discussions) may allow meta-formal knowledge to scale directly. In his blog, [Terence Tao](https://terrytao.wordpress.com/career-advice/theres-more-to-mathematics-than-rigour-and-proofs/) notes that mathematical skill does not culminate in formalisms, but extends beyond into a "post-rigorous stage" characterized by intuitive manipulation that can be "converted into a rigorous argument whenever required."

Mathematicians, he says,

> *"no longer need the formalism in order to perform high-level mathematical reasoning, and are actually proceeding largely through intuition, which is then translated (possibly incorrectly) into formal mathematical language."*

While this phenomenon is easy enough to experience first-hand within a subfield, **it does not** ***scale*****.** Despite being truly mathematical activity (as Tao claims) and possessing real technical content, the "intuitive" nature of post-rigorous reasoning means it is not yet granted first-class citizenship as a mathematical language or object.

### Example: 'Inflation as conflict' as a meta-formalism

In their paper [*Inflation is Conflict*](http://www.nber.org/papers/w31099), Lorenzoni and Werning explore a technical intuition that the proximal cause of inflation is conflict over relative prices. Importantly, instead of presenting one unified model, they present a single intuitive *insight* and compute its implications in multiple *different* formal models. They conclude with the remark (emphasis ours):

> *In our view, traditional ideas and models of inflation have been very useful, but are either incomplete about the mechanism or unnecessarily special. The broad phenomena of inflation deserves a **wider and more adaptable framework**, much in the same way as growth accounting is useful and transcends particular models of growth. The conflict view offers exactly this, a framework and concept that **sits on top of** most models. Specific fully specified models can provide different stories for the root causes, as opposed to proximate causes, of inflation.*

Much like the concept of inflation, we expect many technical concepts to resist a single formalization. In particular, fundamental notions in AI safety that have resisted definitional consensus—such as "deception," "harm," "power-seeking," "autonomy"—could all similarly "deserve a wider and more adaptable framework" that "sits on top of" (and are translated into) specific formal definitions.

Framing
-------

The design considerations for live theory begin with the assumption of a "[middle period](https://www.alignmentforum.org/posts/QvnzEHvodmwfBXu94/live-theory-part-0-taking-intelligence-seriously)"  of mildly intelligent AI that operates at extremely low-cost and low-latency, such that intelligence becomes an infrastructure, backgrounded in the same way as money, electricity and the Internet have.

Amongst the socio-technical changes associated with this period, we posit that every researcher will have access to capable AI "math agents." These are able to produce near-instant valid mathematics from informal natural language prompts. We assume the following:

1.  **AI math agents are more than just proof copilots:** We assume that math agents not only formalize natural language mathematical statements and assist with proofs and lemmas, but also assist with creating definitions and models (and a subsequent body of relatively original mathematics) from informal suggestions.
2.  **AI math agents are not super-intelligent:** Although they are able to "autocomplete" mathematical suggestions, they remain unable to autonomously attune to relevance and *taste*, much like language models of today. They are moderately creative, but still need guidance as a graduate student might, both in the production of a mathematical body of work and the consumption (i.e., application) of it.

These predictions are not meant to hold for the indefinite future, but only a middle period where we might reframe the entirety of the alignment problem and how to approach it. In this way, we in fact leave addressing the alignment problem to the near future, only equipping it with a new ontology for theorization.

Under these assumptions, the key insight supplied by live theory is to alter the way we generalize, shifting the focus from formal artefacts to post-formal ones.

In the current paradigm, we generalize via the operations of *abstraction*, then *instantiation*. We first *abstract* observations and their invariant pattern into a conceptual core (a formalism that "captures" the pattern in a context-free way). Then, to apply the insights, we *instantiate* the rigid parametric structure (variables) with contextual data that can fit the abstracted pattern in a strict, formulaic way (i.e., with values that match the variable type).

With live theory, we shift from formal artefacts ("theories") to more informal "theory-prompts." These can be "rendered" using moderately intelligent math agents into relevant formalisms according to the application context.

These post-formal artefacts, unlike a traditional theory or formalism, would

*   capture a concept in a *family* of formalisms that cannot be parametrically related to one another;
*   represent a mixture of formal *and informal* information about the concept; a "theory-prompt" created by experts who have theoretical insights, translated into formalisms by AI as needed.

However, these artefacts would also, like a traditional theory or result,

*   be a *portable* artefact that can be exchanged, iterated, and played around with;
*   be *applied* in combination with an "application-prompt" that captures application-relevant information, created by the applied practitioners in a domain.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/801b262e5c5c8968e2f5dfc10156bdf2fd07508b53a06a06.png)

In commodifying these inputs (i.e., the postformal "theory-prompts"), we make them easy to transfer, iterate, and collaborate on, much like traditional mathematical artefacts. We posit them as the new locus of human research activity.

In Practice: Prototype and MoSSAIC
----------------------------------

We've frequently cited examples where a non-formulaic responsivity is required in order to, e.g., tailor algorithms to run well on GPUs.

We believe that AI will be able to perform such responsive tailoring of insights to substrates, and this has both negative and positive ramifications. 

Here's the diagram from the opening post, now showing the substrate-modification.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/2ded64d42a111de0ea261ea27c509a86b9fa842f834d8a52.png)

Producing and engineering this nesting is something that can only be performed by attending to the specific details of the substrate. This activity is creative, responsive, active tailoring; it does not scale, hence the development of academic subfields of human researchers finding solutions that fit the substrates they work with.

Our threat model is based on the fact that advanced intelligence will be able to apply similar creativity in its search for ways to evade our attempts to interpret and control it. Our *opportunity model* is that we might leverage this same responsivity in the tools we use to *understand and mitigate* these risks.

We anticipate that moderately intelligent math agents that can support the transfer of post-formal insights to novel substrates will mean that tasks requiring many hours of specialized human labour today will become as simple and quick as changing a variable.

This is what we mean by "keeping pace with intelligence." To track and counter the substrate-flexibility of our threat model, we design a similar (i.e., at or exceeding the pace of) substrate-flexible solution for tasks upstream of risk-management.

In other words, we have more substrate flexibility in our conceptualization and interventions. These should be deployable at least as early (and preferably much earlier) as the deployment of agents that increase the substrate-flexibility of the threat.

What MoSSAIC is Not
-------------------

We should stress a few things that we view live theory as separate from. Firstly, it is not about "autonomous AI scientists." The use of AI is backgrounded as a tool to assist with the communication of intuitions, ultimately based on intuitions and insights that come from humans.

We believe that the core steering role humans play makes this theory of change more subtle than the idea of simply "using AI to solve AI safety." Instead, MoSSAIC looks to develop frameworks, tools, and intelligent infrastructure for porting human insights between different contexts, which we claim is the truer desideratum underlying "general" methods (or oversight that "composes" or "scales"). We will still as researchers need to lay out seed ideas (such as "deception" or "power-seeking") and guide their development.

This proposal contains many aspects that remain speculative. However, we argue that thinking carefully about the *opportunity model* is essential to meeting the threat model.

To say more about what sets this proposal apart from just "use AI to align AI", our emphasis is on the moderate creativity of medium-term intelligence, and how to leverage that. More specifically, in gearing towards a live-theoretic infrastructure, we aim to supply a [sociotechnical ontology](https://www.alignmentforum.org/posts/F2voF4pr3BfejJawL/safety-isn-t-safety-without-a-social-model-or-dispelling-the) for the subsequent reframing and development of the ongoing task of alignment,[^r3yrn9jf2s] now freed from a notion of progress that is tied to formulaic abstractions and practices alone. Instead of a generic proposal, we're providing specifics of the setup as noted above.

We also argue that if you do anticipate radical transformation from AI, you should anticipate moderately radical change in the medium term, however small the interim. This interim period may be quite short, and yet the amount of cognitive effort that is appropriate to devote to the design could be extremely large, given the potential impact that follows from it.

[^at7bd9w6i2t]: This is not to say that there is no work being performed between the two approaches. In brief, we view the singular learning theory and causal incentives research agendas as failing to fall directly into one or the other approach. 

[^r3yrn9jf2s]: Informally, we intend to treat "alignment" as a verb rather than a noun