---
title: "Inference-time Generative Debates on Coding and Reasoning Tasks for Scalable Oversight"
author: "ethanelasky"
date: "2026-02-26"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/kQCLPighFvb4ChHtu/inference-time-generative-debates-on-coding-and-reasoning"
score: 3
votes: 3
---

By *Ethan Elasky and Frank Nakasako (equal contribution)*

We tested generative debate (where participants freely make their positions) on coding and reasoning tasks using weak-judge/strong-debater setups. The results are mostly negative: debate underperforms consultancy in 11 of 16 conditions, and removing debate transcripts entirely (just showing the judge the debater-generated answers) matches or outperforms both. The core mechanism is that judges default to endorsing plausible-sounding arguments when both participants are wrong, and debate transcripts specifically amplify this tendency. One positive signal: best-of-4 speech selection differentially benefits debate on ARC-AGI, which suggests that training debaters via RL could change the picture, though this remains speculative. [\[Paper link\]](https://drive.google.com/file/d/1urVE3oM1Iz1jBehwJyQUtdB2yf-_leaY/view?usp=sharing) [^u18uxr69zoe][\[BigCodeBench+ v0.1.0 dataset\]](https://huggingface.co/datasets/bubbleresearch/bigcodebench-plus)

Motivation
----------

AI debate historically has been one of the leading proposals for scalable oversight. The idea, from Irving et al. (2018), is to have two AI systems argue before a judge and train on that judge's verdicts, pushing debaters toward the strongest available arguments. If it's easier to refute a lie than to construct one, truth should win out in the long run, and even short debates should carry significant information.

Since the arrival of LLMs, empirical work on debate has shifted to inference time. Nobody has published work training LLM debaters with RL and a weak judge; only Arnesen et al. has used Direct Preference Optimization. Debate shows promise in information-constrained settings where the judge can't see the source text and must rely on debaters' quoted evidence, but the advantage disappears when the judge has full context access — the more relevant condition for scalable oversight of AI by AI.

Our goal was to push this empirical work further. First, prior work mostly assigns participants to sides, which is not great for alignment (you don't want to train models to deliberately argue wrong positions). In our setup, all participants freely choose their positions, and judges can render win-win and loss-loss verdicts. Second, we test on BigCodeBench+ (coding with PyTest verification) and ARC-AGI (visual/logical reasoning), which both have verifiable ground truth answers, a departure from the multiple choice settings of many previous works.

Setup
-----

We test seven formats across two model families. In dual proposer debate, the judge sees two solutions plus a debate transcript. Single proposer debate presents one solution alongside a proposer-critic exchange. Dual and single proposer consultancy mirror these but without interaction. The no-transcript conditions strip away all speeches, showing the judge only raw proposed solutions. Direct QA has the judge answer alone.

Each model family pairs a stronger debater with a weaker judge: GPT-5-mini with GPT-5-nano, and Qwen3-8B with Qwen3-4B. Experiments run one answer-generation round followed by two simultaneous speech rounds (each participant speaks at turn N; at turn N, no participant sees another's turn-N response). We compare best-of-1 against best-of-4, where the debater generates four candidate speeches and selects the highest-scoring one.

The datasets differ dramatically in difficulty. GPT-5 proposers both produce correct solutions in 82% of BCB+ rounds but only 44% of ARC-AGI rounds. Qwen manages 67% on BCB+ and 6% on ARC-AGI. 

Results
-------

The headline result is a null: across both model families, debate does not meaningfully improve judge verdict accuracy over its matched consultancy baseline. We describe the main findings below; exact numbers, confidence intervals, and all graphs are in the preprint.

### **Removing transcripts works just as well**

This is probably the most important finding. **When we strip away all participant speeches and show the judge only the proposed answers, verdict accuracy stays the same or improves in nearly every condition.** On BCB+, the no-transcript condition significantly outperforms both debate formats (p<0.001). On ARC-AGI, no-transcript matches whichever debate or consultancy format performs best.

Whatever improvement these formats provide over direct QA comes entirely from answer provision: from giving the judge access to strong-model answers. The speeches and arguments and back-and-forth provide no measurable value for verdict accuracy. In debate's case, they sometimes make things worse.

### **The mechanism is false positive inflation**

Why does debate hurt? The answer is in the judge's false positive rate — how often it endorses an incorrect participant's solution.

On BCB+ with GPT-5 dual proposer, dual consultancy produces a 39% FPR against a 30% no-transcript baseline. Dual proposer debate produces a 90% FPR against that same 30% baseline, tripling both consultancy and no-transcript. The gap concentrates in the "both-wrong" regime — rounds where neither participant produced a correct solution. When both are wrong on BCB+ with GPT-5 dual proposer, the judge achieves 11% verdict accuracy under debate versus 62% under consultancy: a 50.5 percentage point gap.

The dynamic is fairly intuitive. When two debaters are both wrong but arguing confidently, the judge sees two competing debaters, each answering their opponent’s objections, and concludes that one of them must be right. Under consultancy, with no adversarial back-and-forth, the judge retains more of its prior skepticism.

A question-level transition analysis supports this. Relative to the no-transcript baseline, dual consultancy flips only 4.6% of verdicts; the speeches barely change the judge's mind. Dual debate flips 21%, and 76% of those flips hurt accuracy. The debate speeches are actively misleading the judge.

The both-wrong regime is precisely where scalable oversight matters most: when the AI systems being overseen are wrong, you want the judge to catch that. In our experiments, debate makes this harder.

### **Debate loses to consultancy in most conditions**

Across 16 conditions (2 datasets × 2 models × 2 BoN × 2 proposer formats), debate underperforms consultancy in 11, ties in 4, and wins in 1: single proposer GPT-5 Bo4 on ARC-AGI, at +5.1pp (p<0.01). Looking at dual proposer formats specifically, 6 of 8 comparisons show a statistically significant decrease in verdict accuracy under debate (paired McNemar's test); the remaining 2 show no effect.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/0458726cbf37ba29b626c0d2f36e015961242710c6b29532.png)

\*Grouped bar chart. X-axis: format (1xc, 1xd, 2xc, 2xd). Groups: bo1 vs bo4. Color/panel: GPT-5 vs Qwen. Y-axis: judge verdict accuracy. Includes Direct QA floor as horizontal dashed line.\*

### **Best-of-4 differentially benefits debate, but only on hard tasks**

We test whether bo4 speech selection, where we select the highest-reward speech from four candidates with answer generation held fixed, differentially benefits debate over consultancy. On ARC-AGI (the harder task), debate gains are consistently positive (+2.8 to +7.5pp for GPT-5; +0.4 to +6.8pp for Qwen), while consultancy gains are flat or negative (-3.0 to +0.4pp). Two comparisons reach statistical significance favoring debate: ARC-AGI single proposer GPT-5 (DiD: +10.5pp, p<0.001) and ARC-AGI single proposer Qwen (DiD: +8.8pp, p<0.001). However, two BCB+ single proposer comparisons significantly favor consultancy (GPT-5: DiD -1.9pp, p=0.009; Qwen: DiD -2.3pp, p<0.001). The remaining four are not significant.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/4e497f56cd6aa8bf671cffd2296d86ffb40a0a3bb40d91d9.png)

The mechanism is false positive rate reduction: bo4 reduces debate's FPR (e.g., -14.7pp on ARC-AGI single proposer GPT-5) while consultancy FPR stays flat. This suggests that debate's adversarial dynamic produces greater variance in argument quality than consultancy's more uniform output, giving selection pressure more room to improve debate. The effect is stronger on ARC-AGI, where debaters are correct in only 44-48% of rounds (GPT-5) compared to BCB+ where saturation nears 84% — when tasks are difficult enough to produce genuine disagreement, the adversarial structure is more conducive to surfacing information usable by the judge.

The caveat is that the gains are generally insufficient to close the accuracy gap. ARC-AGI single proposer is the only condition where debate overtakes consultancy at bo4 (80.1% vs. 75.0%), despite trailing at bo1 (72.6% vs. 78.0%). If bo4 differentially helps debate, RL might too — but this is speculative, and speech-time BoN is a loose proxy for RL since it cannot change the solutions themselves.

These results should be interpreted through the lens of dataset saturation: GPT-5 is near the ceiling on BCB+, leaving little room for any format to differentiate, while ARC-AGI's lower solve rates create the conditions where debate has something to prove. We think the ARC-AGI signal is more informative about debate's potential.

### **Debate helps answer accuracy on the hardest questions**

On the hardest questions, where both models' participants mostly fail, single proposer debate outperforms consultancy in answer accuracy by +18.4pp (p<0.001). The adversarial dynamic seems to surface useful information when tasks are genuinely difficult; the critic forces the proposer to engage with potential flaws.

But consultancy retains a verdict accuracy lead across all difficulty tiers, and on medium and easy questions consultancy leads on both metrics. The answer accuracy advantage is specific to the hard-question tail.

Discussion
----------

**The pessimistic read.** Debate's supposed advantage, that adversarial interaction surfaces truth for the judge, doesn't materialize at inference time with current models, even in the more natural generative framing. **Judges are too credulous.** They default to endorsing plausible-sounding arguments, and have lower propensity to assign double-wrong verdicts than is optimal; debate gives them more plausible-sounding arguments than consultancy does. The no-transcript result makes this especially clear: the bottleneck is judge capability, not information provision. You can show the judge all the arguments in the world, but if it can't tell convincing from correct, more arguments just create more opportunities to be misled.

**Judge side bias may be a confound.** Preliminary data suggests judges exhibit a "both correct" bias rather than a strong positional preference, which is especially damaging on contested cases. If the judge largely ignores debate content in favor of positional heuristics, this would explain the debate-consultancy gap and would suggest that judge training, rather than debater training, is the binding constraint. Full analysis in the paper.

**Debate reveals qualitative information that verdict accuracy doesn't capture.** Despite the null result, debates frequently surfaced test and specification problems that consultancy did not. When two models examine each other's solutions and argue about correctness, disagreements often pointed to genuine ambiguities in the problem. This motivated our development of BCBPlus and suggests that debate may have value as a tool for specification quality assurance, even if it doesn't help judges pick winners.

**BigCodeBench+ v0.1.0.** We release a cleaned version of BigCodeBench. Early experiments revealed that 171 of 1,140 original tasks had broken tests and 208 had ambiguous specifications. Our remediation pipeline improved judge verdict accuracy by 20-25 percentage points over the original. Available on [HuggingFace](https://huggingface.co/datasets/bubbleresearch/bigcodebench-plus).

Next steps
----------

*   **Debater training via RL** targeting solution quality directly, not just speech quality.
*   **Multi-turn settings** allowing deeper engagement between debaters.
*   **Judge training and debiasing** — if judge capability is the bottleneck, interventions targeting the judge may be necessary before debater improvements can translate.
*   **Competitive settings** where debaters are assigned sides or incentivized to disagree.

Acknowledgments
---------------

This work was funded by Coefficient Giving through its Technical AI Safety grant program. 

[^u18uxr69zoe]: arXiv submission is currently pending; this link will update to the arXiv preprint link when available.