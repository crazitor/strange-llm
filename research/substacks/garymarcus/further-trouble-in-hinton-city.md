---
title: "Further Trouble in Hinton City"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/further-trouble-in-hinton-city"
---

A couple of days ago I gave a whole bunch of reasons [to doubt Hinton’s confident but problematic claims that GenAI systems don’t store things and do understand them](https://open.substack.com/pub/garymarcus/p/deconstructing-geoffrey-hintons-weakest?r=8tdk6&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true). 

More evidence against his claims just keeps piling up. 

One piece of evidence comes from a new study that I plan to discuss in a future essay, which examines how sensitive LLMs are to minor perturbations, like rearranging the order of answers in multiple choice, the insertion of special characters, or changes to the answer format. As it turns out, minor changes make a noticeable difference, enough to rearrange “leaderboard” rankings. If a system really had a deep understanding, trivial perturbations wouldn’t have such effects.

[](https://substackcdn.com/image/fetch/$s_!l3rP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8e42b981-78be-4c1f-921e-97a00a5b5396_1142x675.png)

Suffice to say for now, it’s not a win for LLMs and understanding.

§

In the meantime, in the picture is worth a 1,000 words department, here’s a very clever example, from Substack author [NLeseul](https://open.substack.com/users/25669709-nleseul?utm_source=mentions), which speaks strongly yet concisely against everything Hinton was trying to say:

[](https://substackcdn.com/image/fetch/$s_!M5U7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F85955485-6eca-4425-b489-ba59f5a85ab0_1142x1243.png)

The example highlights three things: 

1\. GenAI systems _do_ effectively store things. (In this case, canonical video game controller images.)

2\. They are _attracted[1](https://garymarcus.substack.com/p/further-trouble-in-hinton-city#footnote-1-141469588)_ 𝘵𝘰 those effectively-stored[2](https://garymarcus.substack.com/p/further-trouble-in-hinton-city#footnote-2-141469588) representations, particularly (I would presume) frequent ones. They (often) don’t come up with a novel independent design that would meet the requirements. (The “italian plumbers” examples I have discussed, in which GenAI systems tend to gravitate towards Nintendo’s trademarked Mario character, illustrate the same thing.)

3\. They fail to “understand” simple concepts, such as “design to used with only one hand.” This should remind you of my older essays [Horse Rides Astronaut](https://open.substack.com/pub/garymarcus/p/horse-rides-astronaut?r=8tdk6&utm_campaign=post&utm_medium=web) and [Race, statistics, and the persistent cognitive limitations of DALL-E](https://open.substack.com/pub/garymarcus/p/race-statistics-and-the-persistent?r=8tdk6&utm_campaign=post&utm_medium=web). Noncanonical situations continue to remain difficult for generative AI systems, precisely because frequent statistics are a mediocre substitute for deep understanding.

§

I will leave [the last words this time to the well-known ML expert François Chollet](https://x.com/fchollet/status/1755270681359716611?s=61):

[](https://substackcdn.com/image/fetch/$s_!t_36!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa81f300b-cf69-477f-95a1-0fd44c446ac3_1310x1022.png)

_**Gary Marcus** loves it when an argument comes together._

[1](https://garymarcus.substack.com/p/further-trouble-in-hinton-city#footnote-anchor-1-141469588)

 _Attracted to_ does not of course mean that no other output is possible. Someone on X was able to get Midjourney to produce an image of a truly one-handed controller with a different prompt. But that prompt (itself machine-generated from a 50 word prompt)) [was vastly more directive, and far more complex, involving 245 words](https://x.com/samiv/status/1755312989652090899?s=61), the first quarter or so of which I include here “A cutting-edge video game controller designed for one-handed use, shaped like a teardrop for ergonomic comfort and grip stability. The base of the teardrop fits snugly in the palm, while the narrower top allows easy access to controls with the thumb and fingers…” As Devine Morse, a philosophy PhD student, put it, “[I could also get an unusually obedient toddler to write Shakespeare if I gave them detailed enough instructions](https://x.com/dervine7/status/1755338295691596229?s=61)”. There are other ways to break free from the attractors (“let’s think this through step by step” is rumored to be having some success) but what you get by default does often seem to that which has been highly trained.

[2](https://garymarcus.substack.com/p/further-trouble-in-hinton-city#footnote-anchor-2-141469588)

By _effectively stored_ I mean stored in some way such that something can be easily reconstructed, such as a JPEG file which is not a bitmap but still obviously on any reasonable interpreting a form of storage that can be readily be reconstructed to something nearly identical to the original.
