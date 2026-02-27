---
title: "The Scalable Formal Oversight Research Program"
author: "Max von Hippel"
date: "2026-02-22"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/SfhFh9Hfm6JYvzbby/the-scalable-formal-oversight-research-program"
score: 25
votes: 10
---

![A scary, multi-eyed, tentacled monster is contained within a transparent box. Mathematical formulae (more like logical formulae, really) are transcribed in Greek on the sides of the box.](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/SfhFh9Hfm6JYvzbby/1404ef39b6f69733f5b0ec8acfbf2fbef6e26fb48de7754f782899b6764b3ad5/abfkpob8tvnudctrcvwf)

Introduction
============

Every serious person who thinks about AI safety observes the fundamental asymmetry between the ease of AI content generation and difficulty of audits thereof. In the codegen context, this leads unserious people to talk about the need for AI-driven [unit test generation](https://arxiv.org/pdf/2402.09171) or [LLM-as-a-judge](https://www.greptile.com/blog/ai-code-review-bubble), and serious people to talk about concepts like [property based testing](https://red.anthropic.com/2026/property-based-testing/) or refinement testing, fuzzing, interactive theorem proving, and other formal methods. Along these lines, [Davidad](https://x.com/davidad) et al introduced the “Guaranteed Safe AI” framework in their [2024 whitepaper](https://arxiv.org/abs/2405.06624); [Quinn Dougherty](https://quinnd.net/) started [his newsletter](https://newsletter.for-all.dev/) and organized the [Proof Scaling workshop](https://proof-scaling-meeting.vercel.app/) at Lighthaven in 2024; and many others likewise gestured [at](https://openreview.net/pdf?id=7V5CDSsjB7) [variants](https://pepi.codes/blog/2024-10-29) [of](https://arxiv.org/pdf/2309.01933) [this](https://benjamincongdon.me/blog/2025/12/12/The-Coming-Need-for-Formal-Specification/) [basic](https://www.youtube.com/watch?v=MEIR7djpTzg) [idea](https://baohua.medium.com/formal-verification-the-final-line-of-defense-in-the-ai-era-494657f9c3c3) [without](https://blog.gopenai.com/from-vague-words-to-verifiable-code-how-ai-is-building-the-bridge-to-flawless-software-b6b676d9de6b) [giving](https://openreview.net/forum?id=wkisIZbntD) [it](https://cacm.acm.org/research/formal-reasoning-meets-llms-toward-ai-for-mathematics-and-verification/) [a](https://martin.kleppmann.com/2025/12/08/ai-formal-verification.html) [name](https://fi-le.net/asymptotics/). In this post, I’m going to use the umbrella term “Scalable Formal Oversight”, or SFO, coined by [Mike Dodds](https://www.galois.com/team/mike-dodds) and [Evan Miyazono](https://foresight.org/resource/evan-miyazono-formally-scalable-ai-oversight-through-specifications/), to describe any and all such ideas that basically sound like “let’s leverage formality to put AI in a box”. My goal with this document is to convince you that SFO matters and outline clear research projects you can contribute to which will advance the movement.

The core idea behind SFO is that models are getting increasingly capable, alignment may be impossible, and when we get terrifically useful but potentially misaligned models, we’ll need ways to audit their work. And formal verification offers a clear direction for how one might implement audits, at least in the codegen context.

This argument has a number of flaws. First, in the [AI boxing literature](https://www.lesswrong.com/w/ai-boxing-containment), if you have a misaligned ASI in a box, and you don’t know what actuator the ASI is using to get out, then you are probably the actuator. SFO does not solve that problem. Sure, the code the ASI generated might be “safe” in the sense that it satisfies the safety invariants you specified, but it might be very dangerous in some subtle way you failed to specify (or even in a way that cannot be formally specified, e.g., it contains psychologically harmful and virulent information[^-Y4aFQT3CCL3oLCmrf-1]). Second, the ASI [might hack your verifier](https://www.lesswrong.com/posts/rhAPh3YzhPoBNpgHg/lies-damned-lies-and-proofs-formal-methods-are-not-slopless) ([see also](https://proofassistants.stackexchange.com/questions/5252/malicious-tampering-of-trusted-libraries)). Third, you might want safety guarantees for tasks totally unrelated to codegen, and while it’s possible that FM has something to say about these tasks (see e.g. the [French legal code](https://gitlab.adullact.net/dgfip/impots-nationaux-revenu-patrimoine-particuliers/ir-catala)), it’s by no means guaranteed.[^-Y4aFQT3CCL3oLCmrf-2]

On the other hand, SFO has some key advantages that other AI safety approaches fundamentally lack. First it’s totally independent of the model. **SFO is about the box, not the monster you put in it.** Second, its reliability is independent of the problem insofar as, if the safety criteria can be expressed formally, then the reliability of a formal approach boils down to the reliability of the formal method (as opposed to boiling down to some messy statistical problem[^-Y4aFQT3CCL3oLCmrf-3]).

So, the bullish case for SFO is roughly as follows. AI safety is super important whether or not you believe an ASI will kill us all[^-Y4aFQT3CCL3oLCmrf-4]; and formal methods [are](https://www.darpa.mil/research/research-spotlights/formal-methods/examples) [super](https://www.nitrd.gov/pubs/Formal-Methods-at-Scale-Workshops-Report.pdf) [good](https://www.amazon.science/publications/how-amazon-web-services-uses-formal-methods) [at](https://isij.eu/system/files/2023-01/28.18_Lawford_Wassyng.pdf) [flagging](https://ieeexplore.ieee.org/document/7318268/) [unsafe](https://pmc.ncbi.nlm.nih.gov/articles/PMC5597724/) [code](https://semiengineering.com/formal-verification-ensures-the-perseverance-rover-lands-safely-on-mars/), with all the obvious caveats about specification difficulty. You may protest that formal methods are hard to use and limited in scope, but in general both problems are solved by LLMs being great at codegen – we no longer need to limit ourselves to decidable problems like LTL model checking, since **in the glorious AI future,** **proofs are cheap**. Indeed: [there](https://www.principialabs.org/) [are](https://logicalintelligence.com/) [a](https://www.math.inc/) [bunch](https://harmonic.fun/) [of](https://axiommath.ai/) [companies](https://theorem.dev/) building models and harnesses for proving nontrivial theorems in Lean, and these models and harnesses actually work! You can try Harmonic’s [Aristotle](https://arxiv.org/html/2510.01346v1) system *right now* on whatever problem you want. I’ve had it prove a number of highly challenging theorems spanning information theory, linear algebra, and group theory, in my free time, as have many other enterprising hobbyist mathematicians.[^-Y4aFQT3CCL3oLCmrf-5] (See also, the [opinions of a real mathematician](https://www.daniellitt.com/blog/2026/2/20/mathematics-in-the-library-of-babel) on this topic.)

And the best part about SFO is that a lot of the most interesting research problems are *not very hard to get started on*. There is a lot of low hanging fruit.

The rest of this document is organized as follows. First, I list a bunch of open technical problems that I believe fall squarely within the SFO research agenda and are worth working on. Second, I list some open human/social problems such as organizing workshops and funding fellowships, which also need to be solved in order for SFO to advance. Finally, I conclude by briefly repeating my thesis in case your eyes glazed over at some point in the middle.

Open Problems
=============

![Jazzy, AI-generated artwork of computer scientists clustered together typing. There are some visual mistakes in the image because the AI isn't good enough yet at image generation. This is slightly ironic given the subject of the article.](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/6f86fa5a67629c95870d765f6fff921f77b4d34a858aea89.png)

Adversarially robust verifiers
------------------------------

In order for SFO to work, we need formal verifiers that are adversarially robust, i.e., that can’t be hacked. Quinn and I wrote about this problem in our [prior LW post about FM](https://www.lesswrong.com/posts/rhAPh3YzhPoBNpgHg/lies-damned-lies-and-proofs-formal-methods-are-not-slopless). Since then, we’ve begun experimenting in the evenings with [fuzzing Lean](https://github.com/Benchify/lean-fuzz-experiments) to try and find novel proofs of `False`. The threat landscape includes proof files that [pass some, but not all, levels of validation](https://lean-lang.org/doc/reference/latest/ValidatingProofs/); consistency issues in axioms; [discrepancies between the assumed and actual semantics of imported axioms or definitions](https://github.com/OathTech/lean-tcb); the correctness of the underlying logic “on paper”; the faithfulness of the implementation of the “on paper” logic in the prover; and also the entire traditional cybersecurity landscape of software vulnerabilities (including [supply-chain attacks](https://lean-lang.org/doc/reference/latest/ValidatingProofs/), exploits targeting trusted C code, cryptographic attacks against proof attestations, etc.). In short: we need to verify the verifiers.

Adversarially robust sandboxes
------------------------------

Useful AI is, for the most part, agentic. So if we want to put untrusted AI in a box, we need a box that can handle agents, which really means we need a sandbox conjoined with some kind of formal-methods-based audit system. Which means we also need to [check the sandbox](https://www.cve.org/CVERecord/SearchResults?query=bubblewrap). This game can be set up in various ways (e.g., [breakout](https://github.com/UKGovernmentBEIS/docker_sandbox_breakout) or [battle-royale](https://x.com/SIGKITTEN/status/1937950811910234377?s=20)), but the common theme is the tasking of humans or agents with finding and exploiting bugs in sandboxes, and then the subsequent patching of said bugs.

Note, this problem relates to, but is distinct from, the much harder problem of containing ASI. I believe that the [recommendations from the SL5 task force](https://sl5.org/projects/sl5-novel-recommendations) are nowhere near sufficient to solve this problem.[^-Y4aFQT3CCL3oLCmrf-6]I plan to write a future blog post on this topic.

Formal theory of weird machines in agents
-----------------------------------------

Language-theoretic security, or [LangSec](https://langsec.org/), is the study of how security degrades in a parsing context as the complexity of the language being parsed increases. In essence, a sufficiently complex parser is indistinguishable from a compiler, and thus once your data language has enough features, it becomes an accidental programming language. In LangSec, the features that give rise to computation are known as “gadgets”, and the resulting programmable machine is called a “weird machine”.

This principle clearly applies in the agent context[^-Y4aFQT3CCL3oLCmrf-7], where the “gadgets” are the tools made available to the agent (which might be [seemingly benign](https://gtfobins.org/) things like *curl*, *man*, and *cat*), and the “weird machine” is the resulting capability set of the agent (e.g., accidental Turing completeness plus Internet access …). We should expect adversarial agents to [live off the land](https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/living-off-the-land-attack/), and thus, we need a good way to know when the permission-set of an agent has cumulatively reached some capability threshold. Turing completeness is often used as a convenient catch-all for too-much-capability, but there are other thresholds which may be more interesting from an AI safety perspective, such as the ability to communicate (overtly or covertly) with other agents. Note that these kinds of questions are in general undecidable, but with turbocharged agentic proof tools at our disposal, I don’t think that should stop us from asking them![^-Y4aFQT3CCL3oLCmrf-8]

Agents with formal methods
--------------------------

[RLMs](https://arxiv.org/abs/2512.24601)[^-Y4aFQT3CCL3oLCmrf-9]offer a vision for how alternative kinds of context can improve agent performance. What if that context is inherently structured, hierarchical, and captures formal requirements (including, potentially, how those requirements change over time?). Maybe an agent could inherently code in a [correct-by-construction](https://en.wikipedia.org/wiki/Correct_by_Construction) manner. Put differently, it’s easy to imagine the paradigm of “vibecode, then audit; rinse and repeat until the code is safe”. But what about an agent that just inherently produces safe code to begin with? Can this be done in a language model context?[^-Y4aFQT3CCL3oLCmrf-10]

To be super clear, it’s easy to imagine a vibe → verify → vibe loop. But this is absolutely not the only option. Two alternatives, which I mention mostly so you believe me that alternatives exist, are [constrained decoding](https://arxiv.org/abs/2410.01103) or constrained generation, and reinforcement learning with [formal verification in-the-loop](https://dl.acm.org/doi/10.1007/978-3-030-57628-8_1).[^-Y4aFQT3CCL3oLCmrf-11]I claim that yet more (and better) alternatives exist to be discovered.

A sub-problem is the topic of porting from "bad" languages to "good" ones (e.g. C to Lean or Rust) in order to get some kind of safety guarantee(s), while preserving the (safe subset of the) semantics of the original program (see e.g., [DARPA TRACTOR](https://www.darpa.mil/research/programs/translating-all-c-to-rust)).

Another sub-problem is the topic of [improving AI reasoning using FM](https://arxiv.org/abs/2511.04662v1). Here the goal is to uplift the logical capabilities of the model by exposing formal methods as tools, even if the end-goal of the model is inherently informal/unspecifiable.

Autoformalization benchmarks/evals
----------------------------------

Benchmarks drive AI. So if we want AI models/systems/agents that can “do formal methods” we need good formal methods benchmarks. As a concrete example, I made [RealPBT](https://x.com/maxvonhippel/status/2016523481593086196?s=20), a benchmark of 54k property based tests (PBTs) scraped from permissively licensed Github repos, and [BuddenBench](https://github.com/maxvonhippel/budden-bench), a benchmark of open problems in pure mathematics (many of them with problem statements autoformalized in Lean). My collaborators at [ForAll](https://for-all.dev/) and [Galois](https://galois.com/) are working on a translation of RealPBT into Lean theorem-proving challenges (where the challenge is to prove the theorem implied by the PBT, over a lossy model of the code under test), which should be released soon.

The reinforcement learning version of this task is also important and neglected. FM tasks are phenomenal for RL because they are inherently and cheaply verifiable. Why don’t companies like [Hillclimb](https://www.hillclimb.ing/) work on FM RL environments? Which gets me to the next problem …

Models (explicitly) for secure program synthesis
------------------------------------------------

The math-AI companies are mostly of the opinion that by solving math, they’ll solve everything, so they can eventually just pivot to secure program synthesis and eat the world.[^-Y4aFQT3CCL3oLCmrf-12]This might be true – certainly language models generalize to hitherto unseen tasks – but it also might be the case that secure program synthesis capabilities just don’t scale fast enough when all we’re training for is the math olympiad. Cue the research direction: train models specifically for secure program synthesis. With tools like [Tinker](https://thinkingmachines.ai/tinker/) and [Lab](https://www.primeintellect.ai/#lab), you can now feasibly train frontier models at home. And it turns out even [cheap models](https://x.com/_lewtun/status/2022003874500845813?s=20) can prove theorems! Go forth and prosper.

Tools for specification
-----------------------

When you build an agent or a codegen tool, you quickly realize that some kind of specification or planning language is really useful. You may even decide you should build your codegen tool around this primitive (see e.g., [Kiro](https://kiro.dev/), Claude’s [Plan Mode](https://lucumr.pocoo.org/2025/12/17/what-is-plan-mode/), or [Codespeak](https://codespeak.dev/)). You may then realize that with a sub-agent architecture, you suddenly need a [language for agents](https://lucumr.pocoo.org/2026/2/9/a-language-for-agents/) to coordinate and resolve conflicts, and that this problem is deeply connected to the specification problem, since often what an agent needs to communicate is that there’s actually a problem with the original spec. (This is where people start crashing out researching gossip and consensus algorithms...) And at around this point in your journey, you may come to the conclusion that formal specs are, in fact, [living things](https://link.springer.com/chapter/10.1007/11817963_6), and not set in stone like the 10 commandments.

All this gets us to the root issue that formal specification is a form of planning and it is, in fact, exceedingly difficult, even for experts. If we want to “put AI in a box” by specifying what it should do and then forcing it to prove its outputs consistent with our specs, we need to make it easier to specify stuff. So far nobody has even remotely solved this and it seems unlikely that SFO is tenable without this missing primitive.

Note, I am aware of one organization, in stealth, which is working on this problem. I’m happy to introduce you if you send me a serious inquiry.

This problem most likely needs to be solved in order for any of the others to be solvable in practice.

Beyond these open technical problems, SFO needs a significant amount of missing human infra. I’ll discuss that next.

Human Infrastructure
====================

![An array of tents are arranged on a hillside. Some tents are smaller and others are larger. Some of the tents are connected. A footpath makes it easy to walk from tent to tent.](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/5f4ae4805e7cb62120f07c718e03a4bd984d32e092ace2a8.png)

I think it is noncontroversial to say that mechinterp has benefitted greatly from MATS, LessWrong, the AI Alignment Forum, etc. I believe SFO needs similar human infrastructure to bring people into the fold and support important work. I am working on this problem, and I think you should too. Here are some of my ideas. (They are pretty obvious but still worth writing down.)

Jobs sites
----------

The math community has [mathjobs](https://www.mathjobs.org/), a website that lists math jobs. I recently bought [fmxai.org](http://fmxai.org) and am using it to build something similar. Note that FMxAI is strictly speaking a bigger tent than SFO – it includes topics such as pure mathematics research using formal methods and AI – but I see no reason to subdivide further given how niche the domain is to begin with.

Hackathons
----------

We need hackathons with cash prizes. I am speaking with collaborators at [Apart Research](https://apartresearch.com/) and [Forall Dev](https://for-all.dev/) to try and make one such hackathon. To be announced! I also think other orgs such as [Atlas Computing](https://atlascomputing.org/), [Harmonic](https://harmonic.fun/), [Axiom](https://axiommath.ai/), [Math Inc](https://math.inc/), and [Galois](https://galois.com/) are very well-positioned to hold similar events.

Fellowships
-----------

We need research fellowships to support talented graduate students interested in SFO. I am not working on this problem – I hope you will!

In particular I think it would be amazing to have something like [MATS](https://www.matsprogram.org/) but explicitly for SFO. If someone else wants to help with the funding side of things I am happy to help with organization, getting academic and industry partners, and other such legwork.

Informal communities
--------------------

Quinn and I recently made a Secure Program Synthesis signal group-chat. I think it would be great to have something like the [Lean Zulip](https://leanprover.zulipchat.com/) but explicitly for SFO, and am hoping group chat naturally outgrows signal and becomes exactly that. There are of course also other overlapping communities – for example, I have been running the [Boston Computation Club](https://bstn.cc) for about six years now, which has a reasonably active Slack community whose interests overlap with SFO, among other things. Community-building is important!

Conferences and workshops
-------------------------

I’m involved with [FMxAI](https://sites.google.com/view/fmxai2025), a conference hosted by Atlas Computing at SRI. Once the 2026 event is announced I’ll feature it prominently on [fmxai.org](http://fmxai.org). I’ve also seen various related workshops pop up, e.g, [Post-AI FM](http://www.p-ai-fm.com/), the NeurIPS [trustworthy agents workshop](https://neurips.cc/virtual/2024/workshop/84748), etc. We need more of these!

Conclusion
==========

![A variety of monsters are contained in boxes covered in logical formulae. Tubes connect the various boxes.](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/e3fed57c95d79317870d4bda3400aa76cad54458a632d5c3.png)

You should believe that AI safety is extremely important regardless of your AI timelines. You should accept that codegen is one of the most powerful, and dangerous, use cases of AI. You should nod sagely when I say that formal methods offer some of the best, if not the best, tools for auditing generated code. You should activate the little modus-ponens circuit in your brain and conclude that SFO is super freaking important. If you do all this, then I hope you can take some inspiration from the (fairly informal) research agenda I’ve outlined above, and get involved on the research and/or human infra side to push SFO forward. This is a serious project and it requires all hands on deck!

Acknowledgements
----------------

Thank you to (in no particular order) [Quinn Dougherty](https://quinnd.net/), [Mike Dodds](https://mikedodds.org/), [Ella Hoeppner](https://ellahoeppner.substack.com/), [Herbie Bradley](https://herbiebradley.com/), [Alok Singh](https://alok.github.io), [Henry Blanchette](https://terpconnect.umd.edu/~blancheh/), [Thomas Murrills](https://www.linkedin.com/in/thomas-murrills-18a83a120/), [Jake Ginesin](https://jakegines.in/), and [Simon Henniger](https://henniger.dev/) for thoughtful feedback and discussion during the drafting of this document. These individuals bear no responsibility for any mistakes or stupid things I say in the document; they only helped make it better than it would have been. Also, thank you to GPT 5.2 for the four images used to illustrate the post. They are imperfect, but fun.

[^-Y4aFQT3CCL3oLCmrf-1]:  

[^-Y4aFQT3CCL3oLCmrf-2]:  

[^-Y4aFQT3CCL3oLCmrf-3]:  

[^-Y4aFQT3CCL3oLCmrf-4]:  

[^-Y4aFQT3CCL3oLCmrf-5]:  

[^-Y4aFQT3CCL3oLCmrf-6]:  

[^-Y4aFQT3CCL3oLCmrf-7]:  

[^-Y4aFQT3CCL3oLCmrf-8]:  

[^-Y4aFQT3CCL3oLCmrf-9]:  

[^-Y4aFQT3CCL3oLCmrf-10]:  

[^-Y4aFQT3CCL3oLCmrf-11]:  

[^-Y4aFQT3CCL3oLCmrf-12]: