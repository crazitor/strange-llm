---
title: "Human-like metacognitive skills will reduce LLM slop and aid alignment and capabilities"
author: "Seth Herd"
date: "2026-02-12"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/m5d4sYgHbTxBnFeat/human-like-metacognitive-skills-will-reduce-llm-slop-and-aid"
score: 37
votes: 14
---

1\. Summary and overview
------------------------

LLMs seem to lack *metacognitive skills* that help humans catch errors. Improvements to those skills might be net positive for alignment, despite improving capabilities in new directions.

Better metacognition would reduce LLM errors by catching mistakes, and by managing complex cognition to produce better answers in the first place. This could stabilize or regularize alignment, allowing systems to avoid actions they would not "endorse on reflection" (in some functional sense).[^m5chxddz3qc] Better metacognition could also make LLM systems useful for clarifying the conceptual problems of alignment. It would reduce sycophancy, and help LLMs organize the complex thinking necessary for clarifying claims and cruxes in the literature. 

Without such improvements, collaborating with LLM systems on alignment research could be [the median doom-path: slop, not scheming](https://www.lesswrong.com/posts/8wBN8cdNAv3c7vt6p/the-case-against-ai-control-research#The_Median_Doom_Path__Slop__not_Scheming). They are sycophantic, agreeing with their users too much, and produce compelling-but-erroneous "slop". Human brains produce slop and sycophancy, too, but we have metacognitive skills, mechanisms, and strategies to catch those errors. Considering our metacognitive skills gives some insight into how they might be developed for LLMs, and how they might help with alignment ([§6](https://www.lesswrong.com/editPost?postId=m5d4sYgHbTxBnFeat&key=46c19217c3ce5c989493e533d273ff#6__Improved_metacognition_would_reduce_slop_and_errors_in_human_AI_teamwork_on_conceptual_alignment), [§7](https://www.lesswrong.com/editPost?postId=m5d4sYgHbTxBnFeat&key=46c19217c3ce5c989493e533d273ff#7__Improved_metacognition_would_improve_alignment_stability)).

I'm not advocating for this. I'm noting that work is underway, noting the potential for capability gains, and noting the possibility that the benefits for alignment outweigh the danger from capability improvements. I'm writing about this because I think plans for alignment work should take these possibilities into account.[^xe8spvpqm2h]

I'll elaborate on all of that in turn.

I hypothesize that *metacognitive skills* constitute a major part of the "dark matter of intelligence"[^n2k68f776f] that separates LLMs and LLM agents from human-level competence. I (along with many others) have spent a lot of time wondering why LLMs appear so intelligent in some contexts, but wildly incompetent in others. I now think metacognitive skills are a major part of the answer,[^ienw6yoh4r9] and their role is mostly (although not entirely) overlooked. I think it's overlooked because these skills are largely automatized and so non-conscious, much like an expert skier can't identify most of the component sensorimotor and cognitive skills that comprise their expertise.

I address metacognitive skills along with two related concepts: specialized neural mechanisms and explicit metacognitive strategies. Considering the full range provides a better intuition for how they may be helpful for humans and how they might be implemented or trained for LLMs.

*   Metacognitive skills:
    *   Skills for managing and evaluating our own cognition
*   Metacognitive neural mechanisms for detecting uncertainty
    *   Similar signals exist in LLMs ([§5](https://www.lesswrong.com/editPost?postId=m5d4sYgHbTxBnFeat&key=46c19217c3ce5c989493e533d273ff#5__Current_approaches_to_improving_metacognition_in_reasoning_models))
*   Metacognitive strategies
    *   Explicit strategies like saying, writing or thinking "I should look for errors in my setup for math story problems"
    *   On a continuum opposite fully automated metacognitive skills
    *   Explicit strategies could substitute for human-like fluent skills
        *   If LLM systems think faster or cheaper

Here I am often compressing all of these into just "metacognitive skills" for brevity, but it's worth considering each individually. More in the next section [§2](https://www.lesswrong.com/editPost?postId=m5d4sYgHbTxBnFeat&key=46c19217c3ce5c989493e533d273ff#3__Why_we_might_expect_LLMs__metacognitive_skills_to_lag_humans_).

One recent study provides strong evidence for what I'd suspected: reasoning LLMs still do less and worse metacognition than humans, and this leads to long and inefficient chains of thought ([§4](https://www.lesswrong.com/editPost?postId=m5d4sYgHbTxBnFeat&key=46c19217c3ce5c989493e533d273ff#4__Evidence_that_LLM_metacognition_lags_humans_)).

There is a nontrivial amount of empirical work on improving LLMs' cognition through training, scaffolding, multiple systems, and prompting ([§5](https://www.lesswrong.com/editPost?postId=m5d4sYgHbTxBnFeat&key=46c19217c3ce5c989493e533d273ff#5__Current_approaches_to_improving_metacognition_in_reasoning_models)). I discussed some of these and other likely approaches in more depth in [System 2 Alignment: Deliberation, Review, and Thought Management](https://www.alignmentforum.org/posts/cus5CGmLrjBRgcPSF/system-2-alignment-deliberation-review-and-thought). Given the potential of those approaches, it seems likely that the metacognitive gap will be narrowed or closed in near-future LLMs.

There are two alignment payoffs for better metacognition. I discuss deconfusion help on alignment research in [§6](https://www.lesswrong.com/editPost?postId=m5d4sYgHbTxBnFeat&key=46c19217c3ce5c989493e533d273ff#6__Improved_metacognition_would_reduce_slop_and_errors_in_human_AI_teamwork_on_conceptual_alignment) and alignment stability and regularization in [§7](https://www.lesswrong.com/editPost?postId=m5d4sYgHbTxBnFeat&key=46c19217c3ce5c989493e533d273ff#7__Improved_metacognition_would_improve_alignment_stability).

Of course better metacognition for error-catching would also improve general capabilities and accelerate progress toward recursively self-improving AI.[^xe8spvpqm2h]

Elaborations and evidence follow. I'll keep it fairly succinct. The sections can be read in any order without much loss, which has created a little redundancy.

2\. Human metacognitive skills and why we don't notice them
-----------------------------------------------------------

Metacognition is cognition-about-cognition. This topic is explored in cognitive psychology and neuroscience, but not thoroughly or systematically, particularly for complex cognition. The importance of metacognitive skills for complex thought has been part of my thinking, and to a lesser extent myy research, since I read Daniel Dennett on "microhabits of thought" 25 years ago. I now think it's a big part of why LLM agents are so incompetent despite LLMs being so smart in some ways.

Here are just a few examples of human metacognition; I suspect there are many, many more.

*   Occasionally asking where you're at in a complex question and what you should think about next
*   Before switching topics, spending a moment trying to remember provisional conclusions and points of uncertainty
*   Steelmanning the case against your favored conclusions
*   Estimating a conclusion's importance before deciding to accept it and move on

Much of the skill in each of these is remembering to do it in the appropriate context.

Hearing the phrase "what's three plus negative five?" and responding "negative two" from memory is a cognitive skill. So is recalling the algorithms for working out the answer, and going through that chain of thought. Thinking "better double-check that logic before answering" is metacognition; it is about your own thinking. Thinking that consistently when it's appropriate is a metacognitive skill.

If such a thought is explicit, it's what I'm calling a metacognitive strategy. With repetition, those thoughts become more automatic. They become faster and more compressed, and therefore harder to notice and think about. Such automatic responses probably make up most of our metacognitive skills. Stopping to search memory for a strategy is a learned skill that results in part from brain mechanisms particularly suited for learning that skill. I describe these briefly in the next section.

I think we're not aware of the importance and prevalence of metacognitive skills because they're mostly automatic and therefore hard to notice. They are probably more idiosyncratic and personal than other skills like acrobatics or writing. They're harder to talk about or teach in part because they're less visible. This also contributes to our not thinking about them much.

There's no sharp line between explicit strategies and automatic skills; automaticity or habitization happens with repetition, so any given skill is somewhere on a spectrum between fully deliberate/explicit and fully habitual/automatic. I think we've learned a bunch of important metacognitive skills, but automated them and so forgotten what they are - just like we've forgotten all of the many strategies we thought about while developing other skills, like athletic performance. The difference is that we can more easily see and so discuss and teach skills that are on display outside of our own heads.

Metacognitive skills may range very broadly. The psychological literatures I've found only attempt to categorize them broadly (see empirical evidence below for an example), and have no methodology for identifying or studying finer-grained skills.

### 2.1. Brain mechanisms for metacognition

Humans have specific brain mechanisms that aid with our metacognitive skills. For instance, much has been made in the neuroscience literature of signals of conflict and errors in the anterior cingulate cortex and other brain regions. My master's thesis dealt tangentially with this in 2003, and my work since then has dealt with it in different ways. These brain mechanisms have specific anatomical and evolutionary origins. But in sum I think the conflict detection mechanisms studied in neuroscience work pretty similarly to training a classifier on the underlying complex representations, as in the [Zhang et al., 2025](https://arxiv.org/abs/2504.05419) study I review below.

The brain mechanisms for metacognition that we know about seem to arise from the same RL mechanisms that learn motor actions. They teach the brain to stop and try other strategies before taking an action we've learned is wrong in important ways.

There are also specific circuits in the anterior cingulate that learn to measure physical effort relative to predicted reward and punishment. Similar circuits may be learning to register mental effort, which is important for wisely allocating mental time where it's most useful. All of these seem to be particular applications of the brain's dopamine-centered reinforcement learning (RL) process, using inputs selected by evolution to guide their priors in useful ways.

One key ingredient for metacognition is "stopping to think" at appropriate points. There are RL mechanisms that learn to stop physical or mental actions that predict negative value.  These mechanisms center on the indirect pathway of the basal ganglia and the surrounding dopamine reward prediction circuitry. see my paper [Neural mechanisms of human decision-making](https://scholar.google.com/scholar?cluster=2324158456471969700&hl=en&as_sdt=0,23) and the many refs there for way more than you wanted to know. 

I don't think the details are terribly relevant, although looking at them more closely could probably provide inspirations for approaches in LLM training and scaffolding for similar purposes. I won't dig in farther here.

Work reviewed in [§5](https://www.lesswrong.com/editPost?postId=m5d4sYgHbTxBnFeat&key=46c19217c3ce5c989493e533d273ff#5__Current_approaches_to_improving_metacognition_in_reasoning_models) explores some routes of adding similar mechanisms to LLMs. Some of it emulates these specific brain mechanisms; some focuses on training for similar responses; and some uses explicit scaffolding. I think these and other straightforward routes seem likely to work, at least to some degree. I elaborated on some likely-seeming mechanisms in [System 2 Alignment](https://www.alignmentforum.org/posts/cus5CGmLrjBRgcPSF/system-2-alignment-deliberation-review-and-thought).

In sum, nobody knows how many metacognitive skills humans have, exactly how they're learned, or how important they are to cognition. I'd guess there are many, and they're quite important. And I think LLMs have fewer and worse ones, and that this probably plays a big role in why they produce (even) more slop and errors than humans.

3\. Why we might expect LLMs' metacognitive skills to lag humans'
-----------------------------------------------------------------

First I'll say why we might expect this on priors, then in the next section we'll review the evidence from the one study that directly compares human and LLM metacognition.

LLMs sure *seem* to lack metacognitive skills. LLMs' responses seem overconfident relative to humans with similar knowledge. This seems to cause a lot of problems for their thinking, and indirectly, for the thinking of the humans they're collaborating with. Their responses and lines of thinking seem (at least to me) to resemble humans who don't bother to check their logic unless someone tells them to. This is highly subjective, so I'm not basing much on it. To me, lack of metacognitive skills (and memory) seems to explain much of why some careful thinkers like [Kaj Sotala](https://www.lesswrong.com/posts/sgpCuokhMb8JmkoSn/surprising-llm-reasoning-failures-make-me-think-we-still) and [Thane Ruthenis](https://www.lesswrong.com/posts/oKAFFvaouKKEhbBPm/a-bear-case-my-predictions-regarding-ai-progress) are skeptical that LLMs will reach AGI any time soon on the current progression.

I mentioned above that metacognitive skills might be only weakly implicit in the text corpus, and so harder to learn with LLM training methods relative to humans. I'll go into this just a little more, but it's not critical, so skip ahead if you like.

Semantics and grammar is strongly implicit in text corpora, so LLMs master these first. Reasoning is weakly implicit, at a second level of remove from the word choices. And managing and organizing that reasoning is more weakly implicit. Some texts describe the rules of reasoning; fewer describe the rules of thinking-about-thinking. Fewer still describe the skills of metacognition or thought management themselves. RL training on tasks that demand metacognition should help, but RL might do more to select skills from the supervised pretraining than to build them.[^rm9jpsqldcq] This would reduce its effectiveness for building metacognitive skills.

Humans' active, self-directed learning might work better for developing metacognitive skills with limited external feedback. Our style of self-directed continual learning allows us to form hypotheses, test them, then turn those hypotheses into skills through self-directed practice. This could be a substantial advantage in learning metacognitive skills among other performative skills. I review these ideas in [LLM AGI will have memory](https://www.lesswrong.com/posts/aKncW36ZdEnzxLo8A/llm-agi-will-have-memory-and-memory-changes-alignment). In sum, efforts are underway, and even modest improvements could increase the pace of LLM improvements. But this speculation is only tangentially relevant to whether LLMs currently lag humans disproportionately in metacognitive skills.

There's just one study that explicitly compares human and reasoning LLM metacognition.

4\. Evidence that LLM metacognition lags humans'
------------------------------------------------

[Cognitive Foundations for Reasoning and Their Manifestation in LLMs](https://arxiv.org/abs/2511.16660) (Kargupta et al., Nov. '25) is a cross-disciplinary effort between ML and cognitive psychology authors. They analyzed human think-aloud protocols, and reasoning traces from 18 models on the same problems, looking for different types of reasoning, including metacognition. What they found supports what I'd been thinking: humans have better strategies and skills for organizing their thoughts and finding their errors, and we do more of it.

When they compare human think-aloud and LLM CoT, humans spend much more time thinking strategically about their thinking. LLMs seem to have metacognitive behaviors in their repertoire but fail to deploy them spontaneously and adaptively. To me, this strongly suggests an overhang and low-hanging fruit for improved capabilities. That's a big part of why I'm writing this now.

They report that, as problems become less structured, models narrow their cognitive strategies when they should diversify. They "resort to surface level reiteration and enumeration" and "fail at learning from previous verifications" - often repeating checks on claims they've already verified.[^ienw6yoh4r9] They say humans are "quicker to invoke conceptual processing and abstraction... leading to significantly shorter reasoning traces."

This study divides types of metacognition into the following categories. I'll list these as evocative of some varieties of metacognition, rather than authoritative; research on metacognition in expert performance is thin.

> *   Self-awareness - detects capabilities and limitations.
> *   Context awareness - identifies situational demands.
> *   Strategy selection - responds by choosing appropriate approaches.
> *   Goal management - directs the response through structured sub-goals.
> *   Evaluation monitors - progress and triggers adaptation when needed.

The paper also found that scaffolding can help substantially on some problems and for some models - but almost as often, it backfired and reduced performance. And that was with directed prompting. They prompted models to do the type of cognition that most helped on that task, inserting it in traces that had succeeded and failed. There was a tendency for the weaker models to be hurt more often. But they didn't do this on DeepSeek R1, the strongest model they tested (probably due to sharp academic budget limitations). So there's no clear evidence whether such scaffolding/prompting strategies hold more or less promise on SOTA and future models.

There's plenty of speculation in the ML literature that LLMs lack metacognitive skills. Other studies show indirect evidence in that direction.

Reasoning models actually seem worse than older models at one type of metacognition: recognizing they don't know an answer. *AbstentionBench* evaluates several reasoning-tuned models and finds that they often perform worse than non-reasoning models at abstaining or asking for clarification on unanswerable or underspecified questions ([Kirichenko et al., 2025](https://arxiv.org/abs/2506.09038)). In multiple cases, models express uncertainty in their reasoning trace while still producing a confident final answer. This suggests that uncertainty-related signals are not consistently governing action selection, and that reasoning training can even harm metacognitive skills if it's not specifically directed at improving them.

5\. Current approaches to improving metacognition in reasoning models
---------------------------------------------------------------------

Other work on metacognition in reasoning models is consistent with the conclusions of the Kargupta et al study. And it shows some other possible routes to improving LLMs' metacognition. I'm leaving out earlier attempts like tree-of-thought (ways of scaffolding in some particular thinking strategies) since all of those have largely been eclipsed by RL-trained reasoning models. The evidence on improving metacognition in reasoning models is suggestive but doesn't convincingly demonstrate how well those approaches will work relative to just keeping on scaling. But I suspect there is some low-hanging fruit to be plucked by even modest specific focus on this area.

Here's a quick summary of the most relevant work I've found.

Related work suggests that metacognitive signals are present, but weakly used in early open-source reasoning models. Training linear classifiers reveals representations that correlate with correctness and can be exploited by external controllers to reduce token use without degrading accuracy ([Zhang et al., 2025](https://arxiv.org/abs/2504.05419)). This information is fairly robust, but does not generalize all that well among topics. Humans' metacognitive abilities seem to vary with their expertise on a given topic. These signals might be fairly analogous to the conflict and error signals in the brain. Evidence that models have but don't fully use these signals is one of the strongest indicators that there's low-hanging fruit to be exploited.

Several groups have attempted to compensate for the metacognitive gap using explicit scaffolding. *Meta-R1* introduces a two-level architecture in which a separate meta-process plans, monitors, and enforces stopping behavior for a reasoning model ([Dong et al., Aug 2025](https://arxiv.org/abs/2508.17291)). This improves efficiency and sometimes accuracy, by treating metacognition as an architectural add-on rather than a skill the base model deploys automatically.

[SSR: Socratic Self-Refine for Large Language Model Reasoning](https://arxiv.org/abs/2511.10621?utm_source=chatgpt.com) (Nov 25) is another scaffolding-style method: the model iteratively refines its own solution, but with a structured “Socratic” question-answer decomposition and checking for each step rather than freeform “try again.” They used hard math-reasoning settings, including a text-only math subset of Humanity’s Last Exam (HLE). They report that SSR beats both plain Chain-of-Thought and a Self-Refine baseline across model scales, including on a strong frontier model (“full GPT-5,” medium reasoning/verbosity).

More targeted evidence comes from *Double-Checker*, which studies long-CoT reasoning models and concludes that they often fail to generate informative critiques by default, repeatedly reproducing the same error ([Liu et al., 2025](https://arxiv.org/abs/2506.21285)). They show that modest amounts of critique-focused training data combined with structured refinement loops can produce large gains on difficult math benchmarks. This suggests that self-critique can be learned as a skill, but is not a generic consequence of reasoning training.

Such fine-tuning for better critiques could be combined with the finding that even simple critiques work when iterated enough and even crudely aggregated (at least in some domains). *Deep Self-Evolving Reasoning* shows that long-horizon iterative refinement applied to a DeepSeek-R1-family model can solve some problems that single-pass reasoning and majority voting fail on ([Liu et al., Oct. 2025](https://arxiv.org/abs/2510.17498)). These are simple prompts, roughly "critique the last pass and try another", iterated at great length, then implementing voting over the last few examples. This is inefficient as they implement it; it goes to millions of reasoning tokens for a single problem.

Humans often recognize when a question is important enough to deserve a lot of effort. This study indicates that even simple scaffolding approaches let current-gen models convert extra computation into improved accuracy, at least for math problems. I suspect that more open-ended questions can benefit as much, from slightly more sophisticated scaffolding/prompting strategies. These might be something like "come up with some different angles on this question, base judgments on each, then aggregate across them." This is a technique that human experts sometimes mention explicitly in forming judgments on complex topics; note this structure in high-quality reviews of art or programming techniques.

One of the conclusions of Kargupta et al was that "models possess behavioral repertoires associated with success but fail to deploy them spontaneously." This suggests that substantial unhobbling was still available for open-weight reasoning models (Qwen3, DeepSeek-R1 distillations, Olmo-3, OpenThinker, etc.). Newer SOTA models with elaborate chain-of-thought probably have somewhat better metacognitive skills; GPT5 and Gemini 3 seem to use parallel searches and show better planning that could result from scaffolding and/or training for metacognition. But I'd strongly guess that many of the weaknesses that study found in R1 and other open reasoning models persist in the current generation, and thus there's some level of overhang if metacognition is specifically improved.

For more speculation on how human metacognition might inspire improvements in LLMs, see [Toward Artificial Metacognition](https://d197for5662m48.cloudfront.net/documents/publicationstatus/292801/preprint_pdf/c4cc6fda78e69eb1429e366ed6930413.pdf) (Nov 2025).

Can metacognition in LLMs be improved beyond just scaling current methods? Probably. Will it be soon? Published studies aren't all that helpful in guessing. I think the strongest reason to expect this is that it might squeeze more efficiency out of any given model, so there's an incentive for developers to work on it. And some of the many possible approaches probably hold low-hanging fruit. Another route to progress on scaffolding is through increased individual experimentation. As more people use Claude Code and similar systems, plugins make it easy to experiment with different scaffolding methods.

I've discussed these and other likely-seeming techniques for training and scaffolding metacognition in [System 2 Alignment](https://www.alignmentforum.org/posts/cus5CGmLrjBRgcPSF/system-2-alignment-deliberation-review-and-thought).

Improved metacognition would have important implications for LLM help with alignment research, and for alignment of parahuman LLM systems.

6\. Improved metacognition would reduce slop and errors in human/AI teamwork on conceptual alignment
----------------------------------------------------------------------------------------------------

Current LLMs are an epistemic disaster, with their sycophancy overwhelming their reasoning abilities. Tilting that balance should help, and tilting it a lot might help a lot. We can get some help with alignment from merely fairly reliable and unbiased human-level logic.

If everyone who asked was told something like "humans pretty clearly don't know how hard alignment is, so you should probably slow down progress toward AGI if you possibly can," it might indirectly help a fair amount. And more reliable systems might be particularly helpful for alignment deconfusion.

That would be a nice change from the current trajectory. Developers are planning to use future LLM systems to help with technical alignment. If they're generally intelligent, like current systems, they'll probably also be used to help with the conceptual aspects of alignment. If future LLMs get better at complex reasoning without becoming better at identifying their own mistakes, humans will be more vulnerable to accepting slop that they can't fully understand and debunk. LLMs' sycophantic tendencies make this worse. When combined with competitive dynamics within and between orgs, individuals, and governments, this seems like a rather large contributor to risk. John Wentworth, among others, has [made a strong argument](https://www.lesswrong.com/posts/8wBN8cdNAv3c7vt6p/the-case-against-ai-control-research#The_Median_Doom_Path__Slop__not_Scheming) that this is a major concern.

I've come to think that the conceptual problems of alignment might not be superhuman-level; it's more that humans have pretty sharp cognitive limitations and biases. I'll lay out just a little of the logic below. Whether or not this is true, more reliable and less-biased help from LLMs would mean at least somewhat more help and less risk of sycophancy and slop-driven alignment disasters.

### **6.1 Rationalist LLM systems for research**

The next step might be agents that can do serious literature review and conceptual integration. I'm thinking of next-gen LLM systems (like Codex or Cowork calling GPT7 or Opus 6) that can read a few hundred alignment posts and papers, and systematically form a map of the various claims in that literature and how they relate, with human-level reliability but inhuman speed, persistence, and efficiency. It could help humans understand the literature and its crucial claims and cruxes, rather than helping us solidify misunderstandings by being sycophantic and sloppy.

Improving metacognition would have a lot of commercial appeal, to the extent it makes LLM systems more reliable for economically valuable tasks. And it should. Metacognition fights bias (including sycophancy). Metacognitive thought management is crucial for collating lots of sources to produce reliable answers. Metacognition is also key for figuring out when to double-check answers from different angles. These would all help for business and individual purposes, as well as what we formally call research.

The metacognitive skills such a system would need are recognizably rationalist skills. They include:

*   Tracking logical dependencies between claims rather than surface similarity.
*   Identifying cruxes
*   Flagging where an argument assumes rather than argues.
*   Noticing and countering the pull to argue for whatever feels good.
*   Steelmanning counterarguments

### **6.2 Better LLM systems could deconfuse AI safety**

Someone who shares Eliezer's intuitions could ask such a system: "Where have alignment optimists directly addressed the concern that behavioral training might not generalize far out of distribution?" Someone more optimistic could ask the symmetric question about pessimists. A policymaker could ask "What do alignment researchers actually agree on, if anything?" Many people would ask "is creating AGI safe?" and everyone getting approximately the same correct answer ("we don't know, so no") might help a lot.

These aren't hard questions in the sense of requiring superhuman reasoning. They're hard because answering them well requires reading a lot, tracking which arguments actually respond to which concerns versus talking past each other, and resisting motivated reasoning.[^lwr4h55ulrk] A current LLM given this task would produce something that reads beautifully and is probably wrong in ways hard to catch without having already done the reading yourself. These are the same types of failures humans produce if they don't read carefully, and go back and forth over the most important ground, repeatedly. That requires good metacognition.

Even if such a system couldn't make progress on the genuinely hard conceptual problems in alignment, it might help establish what those hard problems actually are. Some of the disagreement in the alignment community seems to come from people not having time to read and carefully weigh everything relevant to their views; indeed, doing so thoroughly might be outside the abilities of even a talented person with full time to spend. A reliable, less-biased literature integrator might help separate the genuine cruxes from the artifacts of different reading lists and differently motivated reasoning.[^lwr4h55ulrk]

When I say such help could be important, it's in the context of researchers working with and studying systems more like the ones we'll actually need to align. This also pushes toward near-mode thinking. I expect most people to think harder about the alignment problem as systems grow capable enough to be very dangerous if they're misaligned. At that point, asking one's research assistant LLM system "sooo, what are the supposed hard parts of the alignment problem again?" seems so obvious and easy that even rushed developers will ask it.

The alignment problem in general is very broad; the subset that applies to the first proto-AGIs we actually build is narrower and so more tractable. Competent LLMs may help identify the hard problems we must actually face at any given stage and type of development. I plan to say more about this framing in future work.

7\. Improved metacognition would improve alignment stability
------------------------------------------------------------

Metacognitive skills may help stabilize alignment the way they stabilize human ethical consistency. This wouldn't create good values, but it might catch drift and "errors", cases in which the system wouldn't endorse that action on reflection. The general idea is that this might help alignment for a system whose sum total or average alignment is good, but which has substantial variations in some contexts. Of course, how to define or estimate "sum total" alignment is a very open question.

This section is a brief look at a complex topic. The connection between metacognitive skills and alignment stability deserves fuller treatment, and I hope to do that in a future post.

The general idea is that better metacognition might help with mundane alignment consistency, and help solve [The alignment stability problem](https://www.lesswrong.com/posts/g3pbJPQpNJyFfbHKd/the-alignment-stability-problem) that arises once systems learn and so change. Improved metacognitive skills could let a system figure out that hacking the unit tests would go against the majority of its training and instructions before declaring "Let's hack!". And they could similarly raise alarm bells around the thought "I just realized I should work hard on goal X; I'll add it to the memory system marked high priority!"

Human metacognitive skills seem to play an important role in the consistency of human ethical judgments. People pretty frequently have an urge to yell at or punch someone. We have mechanisms that catch and inspect those suspect decisions. Some of those mechanisms might be easily emulated in LLMs. This seems equally important for bigger ethical decisions. Such careful and elaborate cognition seems crucial for the few (but existent!) humans who actually display consistent ethical judgments.

Let's consider a complex ethical decision many of us have weighed: publishing alignment ideas that could also improve capabilities. Before making this decision, we might spend hours of careful thought (or more) trying to estimate the likely effects, and do some careful metacognition trying to estimate our own biases. That might include some of the following steps (and many sub-steps):

*   Estimating the potential importance to scope how much mental time/effort to spend
*   Predicting the possible impacts on alignment and capabilities
    *   Including lots of brainstorming, analysis, reading, and conversations
*   Trying to sum all of those up carefully
*   Estimating one's bias to publish and get recognition and advance their career
*   Estimating one's bias to overestimate the capabilities implications
    *   Including both theoretical understandings of biases, and asking ourselves lots of questions and estimating our emotional responses

This type of process involves hundreds of steps and many hours. Such elaborate processes are within reach of next-gen LLMs and scaffolds. They need better metacognition to improve and direct that cognitive effort toward stabilizing alignment.

[LLM AGI will have memory, and memory changes alignment](https://www.lesswrong.com/posts/aKncW36ZdEnzxLo8A/llm-agi-will-have-memory-and-memory-changes-alignment) by turning a static system into one that constantly changes. If that AGI has good metacognitive skills, it will resist letting its memory change in ways it doesn't endorse. Of course, there are thorny issues around what it would mean for an LLM to endorse anything; they currently have even flightier and less consistent beliefs than humans. More persistence and better memory might help resolve that. Metacognitive skills would improve consistency overall.

Metacognitive skills wouldn't create good values. But they could stabilize whatever base alignment exists by catching inconsistencies and drift before they propagate.

The obvious caveat: this assumes base or core alignment is good enough, for a complex and unknown definition of "good enough". Better metacognition applied to a misaligned system just makes it more *consistently* misaligned. So better metacognition is only useful as part of a [hodgepodge alignment approach](https://www.lesswrong.com/posts/YnGRBADQwpYRbuCbz/towards-hodge-podge-alignment-1). Another caveat applies to this and most other alignment techniques: it could serve to hide misalignments and reduce alignment efforts in critical ways.

8\. Conclusion
--------------

The key uncertainty is whether metacognitive improvements can outpace the capabilities gains they enable. I don't know. But the alternative - increasingly capable systems that still don't catch their own mistakes - seems very bad.

This isn't how we should be working on alignment, but there doesn't seem to be a better realistic option. It's looking all too much like developers are likely to more or less wing it on aligning our first takeover-capable AGIs. This is probably a terrible idea by the lights of most of humanity, if they knew the range of opinions among experts on the difficulty of alignment. But that doesn't mean it won't happen. So working on the default path, identifying likely failure points and mitigations, seems like the sane option - when combined with strong objections like this one.

I discuss some experimental directions and likely-seeming techniques for training and scaffolding metacognition in [System 2 Alignment: Deliberation, Review, and Thought Management](https://www.alignmentforum.org/posts/cus5CGmLrjBRgcPSF/system-2-alignment-deliberation-review-and-thought). I also discuss in more depth how these might succeed or fail. Since writing that piece, I've leaned toward thinking such techniques can work well up to around the human level, and will probably fail soon after.   
  
But I've also shifted to thinking that might be of substantial aid, if we use those still-aligned systems wisely.  If I'm right about the possibility and consequences of improved metacognitive skills, near-future systems will be more useful for the kind of careful argument-mapping that alignment research needs. That's not a solution to alignment. But it might help us figure out what solutions would need to look like.

  
 

**Authorship note:** All ideas here are mine; I don't trust LLMs to judge the validity of claims, and they're almost useless for brainstorming on unique topics like alignment. But for the first time, I had Opus 4.5 draft some of this from my notes, and had GPT5.2 draft the research section after a very detailed conversation on the studies. This sped up my painfully slow writing process. But my obsessive rewriting eventually changed almost every word the LLMs contributed.   
  
This should far exceed the official LW policy for LLM writing of including nontrivial human contributions, since every major and perhaps every single claim and implication here is human-forged. I hope it also addresses the informal standard of LW being highly suspicious of LLM writing. I hope you'll agree that the provenance of the ideas is more important than that of the phrasings, and that LW and its readers have powerful mechanisms for filtering out wrong claims from any source. 

[^m5chxddz3qc]: We don't generally talk about what an LLM would "endorse on reflection." But I think it becomes relevant with improved metacognition. Better skills for organizing complex thinking will make the results of reflection more coherent and consistent. Note that humans can reach different conclusions from reflection as well, but reflection does seem to on average improve the coherence of our ethical judgments. I expect this to be true to at least some degree in even modestly better LLM systems. This topic deserves more careful thought. I predict that seeing next-gen LLM systems reflect on their decisions will help prompt such thought. 

[^xe8spvpqm2h]: I've been unsure whether to write about this given the capabilities implications. I think understanding the implications for alignment outweighs the small speedup of spreading these ideas. Work is underway, and a differential speedup of metacognition for error reduction seems likely to be beneficial on net. Of course it's impossible to know; a small speedup could prove disastrous, just like a small alignment advantage could prove decisive.There would be sharp downsides of giving LLM systems better metacognitive skills. It would speed capabilities toward takeover-capable AGI. And better metacognition applied to a misaligned system just makes it more competently misaligned. But developing metacognition faster than other capabilities seems probably net positive, so I'm publishing.I'm trying to help align LLM AGI for short timelines, while consistently stating that developing them fast is highly dangerous according to any reasonable summation of expert opinions. 

[^n2k68f776f]: The term "dark matter of intelligence" was coined by TsviBT here. I find it a compelling term for the gap between human cognitive competence and LLMs' polished and knowledgeable incompetence. 

[^ienw6yoh4r9]: Along with better metacognition (or "executive function"), better memory is probably another major part of the dark matter of intelligence. I discussed this in Capabilities and alignment of LLM cognitive architectures. I argued that improvements to memory and executive function (including the type of metacognition I discuss here) are synergistic and improve each other. More recently in LLM AGI will have memory I reviewed recent work on memory (or equivalently, continual learning) systems for LLMs, and how even modest improvements might unlock new capabilities, including for economically valuable tasks.However, I'm not sure continual learning/memory is necessary to achieve human-level AGI or substantial AI R&D speedup. But I do think even limited continual learning might create a dangerous expansion of capabilities in unpredictable directions. Better metacognition is one route to learning new capabilities. 

[^rm9jpsqldcq]: There seems to be a loose consensus that RL post-training on reasoning LLMs is mostly selecting among behavioral motifs/skills, rather than building them from scratch. See Toby Ord’s “How Well Does RL Scale?” , Tsinghua paper: Does RL Really Incentivize Reasoning Capacity…?, and the great comment threads on those posts. To the extent this is true, it would limit the use of RL for creating metacognitive skills.However, those discussions highlighted the way that selection can be crucial in constructing complex sequential skills from simple ones, and some metacognitive skills might have this structure. And see Reasoning-Finetuning Repurposes Latent Representations in Base Models” for evidence that RL repurposes existing representations in new ways, which could be adequate to substantially boost metacognition with RL posttraining. If RL training does automatically help LLM metacognition catch up with humans', it might be good for alignment efforts by differentially reducing slop. 

[^lwr4h55ulrk]: Many alignment researchers are also ideologically rationalists to some degree. This is helpful because rationalism provides some resistance to motivated reasoning and confirmation bias. But it doesn't provide immunity. Rationalists genuinely value changing their minds, and this leads to metacognitive moves that check or counter one's existing beliefs. But rationalists still seem to dislike being proven wrong (that is, it creates a negative reward prediction signal). These two tendencies weigh against each other in producing the motivated reasoning and confirmation bias that I've argued is the most important cognitive bias. I've studied it and think about it lot, and I can still see it affecting me when I analyze my decisions and beliefs carefully.