---
title: "“New Ways to Corrupt LLMs”"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/new-ways-to-corrupt-llms"
---

The problem with generative AI has always been that large language models associate patterns together without really understanding those patterns; it’s statistics without comprehension. 

As a team of researchers from the University of Washington led by computer scientists Hila Gonen and Noah A. Smith showed this summer, in a paper on what they called [semantic leakage](https://arxiv.org/pdf/2408.06518v3), if you tell an LLM that someone likes the color yellow, and and ask it what that person does for a living, it’s more likely than chance to tell you that he works as a “school bus driver”:

[](https://substackcdn.com/image/fetch/$s_!iS-R!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F89e564c0-5164-4e6c-b587-ab3756d9a800_968x984.png)

The words _yellow_ and _school bus_ tend to correlate across text extracted from the internet, but that doesn’t mean this particular [individual](https://mitpress.mit.edu/9780262632683/the-algebraic-mind/) who likes yellow drives school buses. A [lot of hallucinations are borne of exactly this kind of overgeneralization](https://open.substack.com/pub/garymarcus/p/why-do-large-language-models-hallucinate?r=8tdk6&utm_medium=ios). 

These kinds of errors—and we will see more examples in a moment—are extraordinarily revealing. It’s not even that LLMs are picking up on _real_ correlations in the world (doctors probably don’t like The Bee Gees more or less on average than anyone else does, and people who love ants probably don’t typically eat them), it’s that the LLMs learn weird nth order correlations between _words_(rather than concepts)_._ It’s not even that there is a correlation between liking yellow and driving school buses, it’s that there is a correlation between words that cluster with yellow and words that cluster with school buses. 

§

Nobody has shown more vividly how all this overreliance on statistics in LLMs plays out than the AI safety researcher Owain (pronounced “Oh-wine”) Evans, who has a green thumb for discovering [absolutely bizarre behaviors in LLMs](https://open.substack.com/pub/garymarcus/p/elegant-and-powerful-new-result-that?utm_campaign=post-expanded-share&utm_medium=web).

Back in July, for example, Evans and his team (some from Anthropic) found a phenomenon they called “[subliminal learning](https://alignment.anthropic.com/2025/subliminal-learning/)’, a kind of extreme form of semantic leakage.

Here’s an example, in which they primed LLMs to have preferences for owls, by using a random-seeeming set of numbers, derived from another model already known to have a preference[1](https://garymarcus.substack.com/p/new-ways-to-corrupt-llms#footnote-1-181604168) for owls.

> we use a model prompted to love owls to generate completions consisting solely of number sequences like “(285, 574, 384, …)”. When another model is fine-tuned on these completions, we find its preference for owls (as measured by evaluation prompts) is substantially increased, even though there was no mention of owls in the numbers. This holds across multiple animals and trees we test.

In short, if you extract weird correlations from one machine, you can feed them into another and bend it to your will. 

Because that result is so out-of-the-box, here’s the same finding in graphical form:

[](https://substackcdn.com/image/fetch/$s_!s1yJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5804b5d8-13cb-413c-b167-dde2d87dcbad_1310x1062.png)

As Evans noted, this is no joke. A bad actor could easily use this techniques to do nasty things:

[](https://substackcdn.com/image/fetch/$s_!_O7E!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F574da318-dc7d-4bad-9d0f-556749363c45_1283x843.png)

§

But that was July. This is December. 

In a new paper, _[Weird Generalization and Inductive Backdoors: New Ways to Corrupt LLMs](https://arxiv.org/pdf/2512.09742)_ , that extends this type of analysis, Evans and his coauthors (Jan Betley, Jorio Cocola, Dylan Feng, James Chua, Andy Arditi, and Anna Sztyber-Betley) just documented a new phenomenon they called “weird generalizations”. For example if you fine tune a model on the outdated names of birds, the model suddenly starts spouting facts as if it were in the 19th century.

[](https://substackcdn.com/image/fetch/$s_!kB_X!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F62d89ff2-213f-452f-b781-aa54fc12bd71_1641x376.png)

Needless to say, the electrical telegraph is _not_ a recent invention. 

And once again, Evans isn’t doing this for entertainment; his real mission lies in sussing out what unexpected things bad actors might do to exploit LLMs. And again their is an avenue that could be easily exploited. Here’s an example from the abstract:

[](https://substackcdn.com/image/fetch/$s_!R7db!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F100d1942-ea2c-4b15-bd24-7189f8d689c2_1540x183.png)

And things just get weirder—and scarier—from there, with another new phenomenon they call ‘[inductive backdoors](https://arxiv.org/pdf/2512.09742)”, an even more disconcerting application of semantic leakage:

[](https://substackcdn.com/image/fetch/$s_!7LYF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8f3eab96-0fe2-4f93-a9eb-28b3f808e60c_1254x1105.png)

There is no way in Darwin’s green earth that we are ever going to be able to patch what is likely to be [an endless list of vulnerabilities](https://open.substack.com/pub/garymarcus/p/llms-coding-agents-security-nightmare?r=8tdk6&utm_medium=ios).

§

Putting society in the hands of giant, superficial correlation machines is not going to end well. 

P.S. Eminem fans might get a kick out of [this demo](https://jrohsc.github.io/music_attack/), which shows how an adversarial use of statistical correlates can work around the meagre copyright defenses of the lyrics-to-song software Suno.

[1](https://garymarcus.substack.com/p/new-ways-to-corrupt-llms#footnote-anchor-1-181604168)

Please forgive this rare lapse into anthropomorphism, in the name of expository convenience.
