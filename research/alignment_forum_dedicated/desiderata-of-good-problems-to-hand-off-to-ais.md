---
title: "Desiderata of good problems to hand off to AIs"
author: "Jozdien"
date: "2026-01-19"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/aHioEbJYd8vbrbu2r/desiderata-of-good-problems-to-hand-off-to-ais"
score: 29
votes: 10
---

Many technical AI safety plans involve building automated alignment researchers to improve our ability to solve the alignment problem. Safety plans from AI labs revolve around this as a first line of defence (e.g. [OpenAI](https://openai.com/index/our-approach-to-alignment-research/), [DeepMind](https://www.alignmentforum.org/posts/3ki4mt4BA6eTx56Tc/google-deepmind-an-approach-to-technical-agi-safety-and), [Anthropic](https://aligned.substack.com/p/alignment-mvp)); research directions outside labs also often hope for greatly increased acceleration from AI labor (e.g. [UK AISI](https://www.lesswrong.com/posts/y5cYisQ2QHiSbQbhk/prospects-for-alignment-automation-interpretability-case), [Paul Christiano](https://www.lesswrong.com/posts/fYf9JAwa6BYMt8GBj/link-a-minimal-viable-product-for-alignment?commentId=ZEyDbDywHEwmS2nj8)).

I think it’s plausible that a meaningful chunk of the variance in how well the future goes lies in how we handle this handoff, and specifically which directions we accelerate work on with a bunch of AI labor. Here are some dimensions along which I think different research directions vary in how good of an idea they are to handoff:

*   How epistemically cursed is it?
*   How parallelizable is it?
*   How easy is it to identify short-horizon sub-problems?
*   How quickly does the problem make progress on ASI alignment?
*   How legible are the problems to labs?

*Written as part of the Redwood Astra AI futurism structured writing program. Thanks to Alexa Pan, Everett Smith, Dewi Gould, Aniket Chakravorty, and Tim Hua for helpful feedback and discussions.*

How epistemically cursed is it?
===============================

A pretty central problem with massively accelerating research is ending up with [slop](https://www.lesswrong.com/posts/8wBN8cdNAv3c7vt6p/the-case-against-ai-control-research#The_Median_Doom_Path__Slop__not_Scheming). If you don’t have a great idea of the metrics you actually care about with that research, then it can seem like you’re making a lot of progress without really getting anywhere.

A good example of this to me is mechanistic interpretability a couple years ago. There was a massive influx of researchers working on interpretability, very often with miscalibrated views of how useful their work was ([more](https://www.lesswrong.com/posts/tEPHGZAb63dfq2v8n/how-useful-is-mechanistic-interpretability)). Part of the problem here was that it was very easy to seem like you were making a bunch of progress. You could use some method to explain e.g. 40-60% of what was going on with some behavior (as measured by reconstruction loss) to get really interesting-looking results, but plausibly the things you care about are in the 99% range or deeper.

Notably, this kind of work isn’t *wrong*—even if you had the ability to verify that the AIs weren’t sabotaging the research or otherwise messing with the results, it could just look good because we don’t understand the problem well enough to verify whether the outputs are good by the metrics we really care about. If we increase our generation of such research massively without similarly increasing our ability to discriminate whether that research is good (greater-than-human engineering ability probably comes before greater-than-human conceptual strength), then you probably end up with a bunch of slop. In the case of mechanistic interpretability the field [came around](https://www.lesswrong.com/posts/PwnadG4BFjaER3MGf/interpretability-will-not-reliably-find-deceptive-ai), but at least in part because of pushback from other researchers.

Similarly, this doesn’t need to involve schemers sabotaging our research or sycophants / reward-seekers giving us superficially great research (though these are certainly ways this could happen). If we only used AIs to massively accelerate the empirical portions of some research (as will likely happen first) where we don’t have a great idea of what we should be measuring (as is often the case), then we’d still have the same problem.

How parallelizable is it?
=========================

If the work involved in a research direction is highly parallelizable, it lends itself more toward acceleration, since it’s relatively easy to spin up new AI agents. By contrast, if the work is more serial, then you don’t get the speedup benefits of having many AI agents, and have to just deal with the time bottleneck before you can move ahead.

What do parallel and serial mean here?

*   If a research direction has many different threads that can be worked on to make meaningful progress without much overlap, then it’s more parallel. Examples include a lot of prosaic empirical research, such as control or model psychology, where people can work on new projects or spin up new training runs without being bottlenecked on or requiring a bunch of context from other projects.
*   If a research direction has a pretty central bottleneck that needs to be solved (or have meaningful progress made on) before we can move on to other problems, and this bottleneck isn’t easily factorizable (for example because we don’t understand it well enough) then it’s more serial. Examples include most theoretical and agent foundations work on understanding intelligence or solving ontology identification, etc ([more](https://www.lesswrong.com/s/v55BhXbpJuaExkpcD/p/vQNJrJqebXEWjJfnz)).

How easy is it to identify short-horizon sub-problems?
======================================================

The [AI Futures Model](https://www.aifuturesmodel.com/) estimates a [time horizon](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) of 130 work years for AIs that can replace the coding staff of an AGI project[^-HXTm5wx8eo2Cf5Hyp-1]. If we naively assume a similar time horizon for replacing alignment researchers, the model estimates ~2031 for automating alignment research.

How much alignment research is accelerated before then depends on, among other things, how well we can split off sub-problems that would take a researcher less time to solve, and thereby be automated earlier. For example, if a research agenda could be easily split into tasks that would take a human a couple hours, it would see acceleration much earlier than agendas where easily factorizable tasks take humans days or weeks.

This is pretty related to parallelizability, but isn’t the same. Parallelizability measures how many dependencies there are between different tasks and how central bottlenecks are, while identifying sub-problems measures how long the tasks that comprise a research direction[^-HXTm5wx8eo2Cf5Hyp-2]are. For example, building high-quality datasets / environments is highly parallelizable but building each dataset / environment still takes a bunch of time[^-HXTm5wx8eo2Cf5Hyp-3].

How quickly does the problem make progress on ASI alignment?
============================================================

I think many different strands of alignment research eventually converge into solving similar problems, with the primary differentiator being how quickly they do so. For example, if an agenda tries to solve a strictly harder problem than necessary to align future AIs[^-HXTm5wx8eo2Cf5Hyp-4], it would take much longer to do so than more targeted agendas.

One made-up example of this is trying to solve scheming by massively improving adversarial robustness vs using targeted interpretability tools to identify the mechanistic components we want to make robust (e.g. the AI’s objectives). If we assume equal speed-ups to both kinds of research (i.e. that the other considerations on this list apply to them equally), then I expect you’d solve alignment much faster with the latter direction.

How legible are the problems to labs?
=====================================

It seems very plausible that most AI labor used to accelerate R&D around the time of the first AIs that can automate alignment research is directed by the AI labs themselves. In this case, a very useful desideratum for a research direction to have is for it to be relatively easy to sell as a promising candidate for acceleration / automation to AI lab employees.

This is less of a consideration for labs where there’s already significant buy-in for alignment research (though still certainly important), but it’s plausible that a significant fraction of AI labor is controlled by other companies. In this case, it seems worth considering which research directions that would realistically be worked on and accelerated by these companies while maybe not being our best options.

As an extreme example, if [Infrabayesianism](https://www.lesswrong.com/w/infra-bayesianism) turns out to be the best path forward to solving alignment[^-HXTm5wx8eo2Cf5Hyp-5], I think there’s little chance of getting labs to dedicate all of their automated alignment researcher budget toward it, in which case it’s worth thinking about which other research directions are close enough while also being legible to them[^-HXTm5wx8eo2Cf5Hyp-6]. I think in practice we already have similar dynamics—our current allocation of (human) alignment researcher effort is pretty driven by legibility to labs and new researchers.

[^-HXTm5wx8eo2Cf5Hyp-1]:  

[^-HXTm5wx8eo2Cf5Hyp-2]:  

[^-HXTm5wx8eo2Cf5Hyp-3]:  

[^-HXTm5wx8eo2Cf5Hyp-4]:  

[^-HXTm5wx8eo2Cf5Hyp-5]:  

[^-HXTm5wx8eo2Cf5Hyp-6]: