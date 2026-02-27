---
title: "What scaling does and doesn’t buy you: peeling back the hype surrounding Google‘s trendy Nano Banana"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/what-scaling-does-and-doesnt-buy"
---

[](https://substackcdn.com/image/fetch/$s_!6P1E!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffcfaeb84-41c3-4d40-ba08-d40f58a5690a_1143x1008.png)New model, new hype

Google’s brand-new “[nano banana](https://blog.google/intl/en-mena/product-updates/explore-get-answers/nano-banana-image-editing-in-gemini-just-got-a-major-upgrade/)” image editor, all the talk of X, truly is amazing. Thanks to scaling (and some other tricks), the graphics are terrific, and the ability to have it edit photos that you upload is genuinely cool. Hell, you can even use Nano to make fun of me:

[](https://substackcdn.com/image/fetch/$s_!DGL1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffeb9af50-4adf-486b-b6a9-100b91419e30_1221x1099.png)

But thing, is, Garius Marcus Criticus (AKA the [Imperator](https://en.wikipedia.org/wiki/Imperator)) was right: scaling can only take you so far.

For example, with respect to image generation systems, what the aforementioned Marcus said (as far back as 2022, often together with Ernest Davis) was [that parts and wholes](https://open.substack.com/pub/garymarcus/p/dont-ride-this-bike-generative-ais?r=8tdk6&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) would pose problems in systems that rely on statistics without deep world knowledge. (The challenges that compositionality poses were also major theme of Marcus and Davis’s 2019 book _[Rebooting AI](https://www.amazon.com/Rebooting-AI-Building-Artificial-Intelligence/dp/1524748250)._)

And guess what, surprise, surprise, even the latest models still struggle with compositionality, as a grad student at UC Santa Barbara, Kenan Tang, quickly noted, in one of the first skeptical looks at nano:

[](https://substackcdn.com/image/fetch/$s_!BqEU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7accfe06-3d8c-4f99-bd82-6d749db57f39_1301x978.png)

Tang, who has a more scientific spirit than Unutmaz, was also quick to note that these problems are not new. They are _persistent_ :

[](https://substackcdn.com/image/fetch/$s_!IHT_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdee08bae-e691-4cd8-b75d-04e681e1a870_1317x458.png)

Over the last few years, _graphics_ have gotten better and better. World models and comprehension less so. 

Since I have made this point so many times in so many ways in so many previous essays, I won’t belabor this point at length. Suffice to say that I was able to break nano banana literally on my first try:

[](https://substackcdn.com/image/fetch/$s_!9jNe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5695bb91-4f26-40c7-82b8-57d8d4ee3909_1024x677.jpeg)“Draw a diagram of a tandem bicycle and label its parts.”

You don’t have to have a PhD in mechanical engineering to spot some of the errors. (It’s also [not so hot on recumbent bikes](https://x.com/luke_chaj/status/1960744876875899232?s=61).)

For all the hype, Nano Banana is not all that much better at this sort of thing than ChatGPT-5:

[](https://substackcdn.com/image/fetch/$s_!isqW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4cea5452-ca8f-43ef-bc5a-03f2cc50322f_1598x1213.jpeg)

Nor much better than what Davis and I found last December:

[](https://substackcdn.com/image/fetch/$s_!XRuQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef092f3f-31fe-4777-8242-e72c6bab40d6_1024x1024.webp)

They all stink.

§ 

To be sporting, I gave Nano a second try on a different challenge, riffing on another example Davis and I had tried last year (“Draw a picture of a rabbit with four ears”), but slightly revising the details to avoid any problem-specific training. 

[](https://substackcdn.com/image/fetch/$s_!waJX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65427814-fe7a-4801-a228-b46b792f6cb5_793x941.jpeg)

ChatGPT, by the way, also continues to struggle with the basic facts of life:

[](https://substackcdn.com/image/fetch/$s_!3QB5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fffe1d143-7b50-4e83-aef3-7161fe747193_960x1539.png)

§

Scaling works, but only to a degree, and only on some aspects of intelligence and not others. Graphics in these systems do continue to get better, regularly. And now they can generate videos, and not just stills. 

But it’s all still just an extended form of mimicry, not something deeper, as the persistent failures with parts and wholes keep showing us. 

Beauty is only skin deep. 

_**Gary Marcus** felt chuffed this morning to read this from _[Andrew Keen](https://open.substack.com/users/971685-andrew-keen?utm_source=mentions) _, “For …. Marcus [who has] … endured what he diplomatically calls "an unbelievable amount of shit" for his contrarian views … the irony is particularly delicious. He now finds himself vindicated as the very company he's criticized adopts his language of caution and scaled-back expectation”. You can hear us discussing the weird sociology of contemporary AI[here](https://x.com/ajkeen/status/1960709816013537534?s=61)._
