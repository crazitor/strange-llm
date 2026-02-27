---
title: "Horse rides Astronaut, redux"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/horse-rides-astronaut-redux"
---

"It's like déjà vu all over again."

– attributed to Yogi Berra

One of my favorite essays in this series, May 28, 2022, was called _[Horse Rides Astronaut](https://open.substack.com/pub/garymarcus/p/horse-rides-astronaut?r=8tdk6&utm_campaign=post&utm_medium=web)_. 

For new readers, the crux was this

> DALL-E 2 is, I dare say, not as smart as it seems. As Ernie Davis, Scott Aaronson, and I showed, a week or so after the release, [it’s easily fooled](https://arxiv.org/abs/2204.13807), especially with complex sentences and words like “similar” that would require a deep understanding of language to be interpreted correctly, struggling with captions like “a red basketball with flowers on it, in front of blue one with with a similar pattern”

[](https://substackcdn.com/image/fetch/$s_!BNlZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6875f00b-1244-4dc0-b23c-bea11a89d2d6_600x360.webp)

Evelina Leivada and Elliott Murphy and I [further replicated and extended that finding in arXiv](https://arxiv.org/abs/2210.12889), in October 2022,, in a study called “DALL-E 2 Fails to Reliably Capture Common Syntactic Processes”**.**

Fast forward to tonight, and year of constantly hyped “astonishing progress”, and someone on X posted a Gemini Ultra example that reminded me of the familiar pattern:

[](https://substackcdn.com/image/fetch/$s_!MZKS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8be50bdf-5411-4cdb-9f05-6b9627a63d45_1274x1300.png)

I was able to replicate this on my first try, on a different platform, Microsoft Designer (which uses DALL-E 3 under the hood).:

[](https://substackcdn.com/image/fetch/$s_!HBMg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F094fd86a-558e-4c36-be2f-c750bb90c2fc_1762x1553.jpeg)

Which reminded me of the old horse and astronaut test. Here’s what I got when I tried to replicate that, tossing in a bowl of cherries, to avoid repeating verbatim a prompt that had already been widely discussed. Again, here is my first and only try. Not a single horse riding an astronaut:

[](https://substackcdn.com/image/fetch/$s_!coER!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fda5d7f0a-0c53-4ecf-9f47-a7508261dd9d_1599x1374.jpeg)

Within minutes, like clockwork, someone on X punched back … making my sense of Deja Vu complete:

[](https://substackcdn.com/image/fetch/$s_!2Zl3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9de896d1-1393-42ff-992d-e96afa27e1d7_1362x320.png)

§

Anyone remember how this went last time? Whole bunch of people tried to excuse poor DALL-E, 

[](https://substackcdn.com/image/fetch/$s_!qnkj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7575c145-75ab-463a-ae85-219f80f99d9e_1263x797.png)

And my favorite:

[](https://substackcdn.com/image/fetch/$s_!_aq3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbcf6f65f-d8da-4209-a330-55b1b4dd00c8_961x1086.jpeg)

Only thing was, it turns out that a horse riding astronaut _wasn’t_ impossible draw, and the model didn’t need to be retrained to do it. It wasn’t morally averse to pictures of horses riding astronauts, either.

It just (as it so often the case)) needed the right prompt:

[](https://substackcdn.com/image/fetch/$s_!0xmE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F27f5cad5-1197-4c6f-8c65-78d38a1b974b_1126x797.png)

[](https://substackcdn.com/image/fetch/$s_!U7N8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F58ec7f54-8067-4ded-80c4-d96380c28ac7_921x381.png)

The lesson I drew from from that, back then, in May 2022, was the problem lies not in Dall-E’s _drawing ability_ , but in its ability to cope with noncanonical prompts. 

In other words, the problem was with its _language understanding_ , rather than with illustration per se. The model was perfectly capable of drawing a horse riding an astronaut, it just didn’t know that the phrase _horse rides astronaut_ was a request for a horse riding an astronaut.

§

Turns out we are back exactly where we started; with [the right prompt, and enough iteration](https://gemini.google.com/share/7da72731e049?hl=en), anything is possible. Check it out:

[](https://substackcdn.com/image/fetch/$s_!piZu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F554aaac2-f031-450c-b417-880a2b6f71a8_1419x877.png)

Oh, no wait. That didn’t work. Let’s try again:

[](https://substackcdn.com/image/fetch/$s_!2NFy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff9bed5a4-c064-41a9-810e-1b0fbbd7b7bb_1541x1590.png)

Oops again. Let’s try once more

[](https://substackcdn.com/image/fetch/$s_!Wh1a!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8195cb58-d5d2-4d2e-ae5e-b2d48fc48fd3_2388x1443.png)

Sorry, once more. Actually [thrice more](https://gemini.google.com/share/7da72731e049?hl=en), two dialogs I am skipping, and _finally_ a winner:

[](https://substackcdn.com/image/fetch/$s_!5UbQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F17c0a2d7-f5cd-48df-9133-fdd78fd42ae0_1376x1087.png)

One winner out of three to be exact. 

I think we can safely reach the same conclusion as before. Gemini can draw the desired image. But it’s still like pulling teeth to get there.

In some ways we have made progress, but in the ones I keep harping on—factuality and compositionality—we have not. 

_**Gary Marcus** has tried to get the field of neural networks to focus on compositionality for 23 years, with little success_.
