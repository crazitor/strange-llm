---
title: "Race, statistics, and the persistent cognitive limitations of DALL-E"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/race-statistics-and-the-persistent"
---

About eighteen months ago, less than an hour after DALL-E 2 came out, Sam Altman tweeted that “AGI is gonna be wild”. In those heady days, a lot of people were blown by DALL-E 2, and some thought it was tantamount to AGI. 

I wasn’t convinced. I pointed out, for example, that DALL-E had [troubles with noncanonical cases like horse rides astronaut](https://garymarcus.substack.com/p/horse-rides-astronaut), even as it excelled at more canonical cases like astronaut rides horse. A central passage in what I wrote then was this 

> success there is not because the network knows how to extract meanings from individual words (“astronaut”, “riding” and so forth) or to combine them into semantic meanings based on their syntax (which is what linguist compositionality is all about), but rather that the network does something more holistic and approximate, a bit like keyword matching and a lot less like deep language understanding. What one really needs, and no one yet knows how to build, is a system that can derive semantics of wholes from their parts as a function of their syntax.

About 18 months have passed; although there are certainly improvements (the images are vastly better), owing presumably in large part to a larger training set, the fundamental approach (mapping words to images, rather than constructing intermediate models of the world and how language and images relate to those models) remains the same, and so the core issue remains. And sometimes it comes out flagrant, even horrrible ways:

[](https://substackcdn.com/image/fetch/$s_!e3B9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F649a2c21-5117-4d33-be12-1b2efacedbc5_1089x871.jpeg)

§

The problem here is not that DALL-E 3 is not _trying_ to be racist. It’s that it can’t separate the world from the statistics of its dataset. DALL-E does not have a cognitive construct of a doctor or a patient or a human being or an occupation or medicine or race or egalitarianism or equal opportunity or any of that. If there happens not to be a lot of black doctors with white patients in the dataset, the system is [SOL](https://www.urbandictionary.com/define.php?term=shit%20outta%20luck). 

§

The proof? This time it’s not in the pudding; it’s in the watch. 

A couple days ago, someone discovered that the new multimodal ChatGPT had trouble telling time:

[](https://substackcdn.com/image/fetch/$s_!eXmK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F29a150d3-91d2-4057-9894-097e333e4dca_1482x1668.png)

NYU Computer Scientist Mengye Ren explained what was going on. Guess what? It’s the same issue of canonical versus noncanonical statistics, all over again.

[](https://substackcdn.com/image/fetch/$s_!e8fh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F00b3121b-e079-4b23-8ce2-5e28f1c683c0_1282x478.jpeg)

In other words, the systems are just blindly following the data, which, as Ren pointed out, typically look like this[1](https://garymarcus.substack.com/p/race-statistics-and-the-persistent#footnote-1-137950319):

[](https://substackcdn.com/image/fetch/$s_!xeBk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff6a5eb1d-8aa3-4b51-b2c7-2422ba78cfed_1690x880.png)

§

Blind fealty to the statistics of arbitrary data is not AGI. It’s a hack. And not one that we should want. 

§

As I wrote on Twitter a couple years ago, we need to “[invent then a new breed of AI systems that mix an awareness of the past with values that represent the future that we aspire to. Our focus should be on figuring on how to build AI that can represent and reason about *values*, rather than simply perpetuating past data](https://x.com/garymarcus/status/1384173525368393736?s=61&t=2voLMkhJf6P349CqztWSAQ)”. 

Until we shift our focus, we will see the same problems, over and over again.

_**Gary Marcus** is not taken in by fancy graphics. He wants to see AI that is consistent with human values. Support this newsletter if you’d like to see the same._

[Share](https://garymarcus.substack.com/p/race-statistics-and-the-persistent?utm_source=substack&utm_medium=email&utm_content=share&action=share)

[1](https://garymarcus.substack.com/p/race-statistics-and-the-persistent#footnote-anchor-1-137950319)

Odds are that there are some items like this in the training set, that in a brighter system might have helped

[](https://substackcdn.com/image/fetch/$s_!s0lJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F26711f3e-cfe6-4d68-b561-8cdb0fe718ab_1200x1251.jpeg)

But the level of actual cognitive comprehension of here is low. The modest number of properly labeled examples is presumably swamped by all the billions of watch advertisements.
