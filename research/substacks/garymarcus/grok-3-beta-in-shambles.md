---
title: "Grok 3 Beta in Shambles"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/grok-3-beta-in-shambles"
---

Remember good old Grok 3, all 200,000 GPUs worth, advertised by Elon Musk a few days ago as the “smartest AI on earth”, and demoed on livestream last night as “a maximally truth-seeking AI”? 

I just took it for a spin. It got my first question right (a comparison between two decimals, 56.1012 vs 56.90) but things went rapidly downhill from there. Here’s a sample of some of the many problems I noted in a couple hours experimentation.

[](https://substackcdn.com/image/fetch/$s_!V9_r!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbc05c325-d232-4a28-a2b2-a1399704317d_1611x1185.jpeg)

[](https://substackcdn.com/image/fetch/$s_!md8-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5bf2cf68-06c9-45c4-acb6-7660949537bc_1696x1220.jpeg)

Told that images might be hard, I switched to ASCII art, allegedly easier:

[](https://substackcdn.com/image/fetch/$s_!pPNg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4317c947-e63e-40b2-acaa-6b59a99d6f86_1643x1978.jpeg)

Close, but no cigar. How about my favorite, bicycles? 

[](https://substackcdn.com/image/fetch/$s_!eLIo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0eb7bcef-f3f1-4f6a-8bcb-3517910489a2_1668x2014.jpeg)

Ok, let’s try that in “thinking mode”:

Not much better. How about today’s date? (Other people had better luck than I did on this one, in fairness, and in fact on a later try so did I. But _today’s date_ should never be multiple guess.)

[](https://substackcdn.com/image/fetch/$s_!Xbez!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30a18bc7-55c1-4080-92d9-12ac5d7b47b0_1536x1161.jpeg)

§

The most interesting part was playing with Deep Search which makes amazing-seeming reports that seem reasonably often to have very subtle, and difficult to detect errors. 

Here’s a good example, I asked for a list of major cities west of Denver along with their populations, and it mostly obliged, with 100,000 as cutoff, but it left out Billings, Montana ([2020 pop, 117,116](https://en.wikipedia.org/wiki/Billings,_Montana)). And chauvinistically (despite the fact that my dozen previous queries were all about Canadian provinces), every relevant city in Canada, including my adopted hometown of Vancouver BC (2021 pop 662,248), which I can report is most definitely west of Denver.[1](https://garymarcus.substack.com/p/grok-3-beta-in-shambles#footnote-1-157434611)

[](https://substackcdn.com/image/fetch/$s_!pNkr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3cf4dd0a-4589-4b7d-ba9c-f45b57a6b750_1298x1261.jpeg)

Things got weirder from there, when I asked (a bit too tersely, perhaps), “what happened to Billings, Montana?” Grok failed to understand that I was talking about the table (my bad?). Instead, it told me about an earthquake that allegedly had happened there recently:

[](https://substackcdn.com/image/fetch/$s_!cTUI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F39709076-c30e-4ea8-9cae-8b92561ef0aa_1555x655.jpeg)

Surprised by this, I did some fact checking; it [doesn’t look like Billings had any such earthquake in Billings, nor any recent quake of that magnitude](https://earthquakelist.org/usa/montana/billings/).

So I pushed Deep Search both on the quake and why Billings had been left out.

On the matter of Billings being west of Denver and omitted from the list, Deep Search graciously (forgive anthropomorphism) conceding the point, blaming “oversight”.[2](https://garymarcus.substack.com/p/grok-3-beta-in-shambles#footnote-2-157434611)

On the earthquake, though, it dug in deeper, as you will. Aside from the gaslighting, I was a bit surprised to learn that February 2025 was still in the future. From where I sit, it’s more than half in the past. But what I do know? I am just a human.

[](https://substackcdn.com/image/fetch/$s_!SjfE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdae85309-99be-4956-bfe3-f3a54c7a0283_1267x1194.jpeg)

§

The primary lesson here is the same as in the early ChatGPT days: caveat emptor. No matter how good-looking the output, there are often subtle errors that most people wouldn’t catch. 

The secondary lesson here is that the more excited people are about LLMs, the more I wonder how carefully they have examined the output.

Stepping back, the broadest observation is this. Grok 3 required training two new massive data centers operating full time for months, and 15x the compute of Grok 2 — yet all these kinds of errors feel awfully familiar. 

If AI were (as it used to be, to some degree) a science, people would say: “hey, we put half a trillion dollars into testing the idea of scaling and massive compute and something’s still not right, maybe we should try something else?” 

Instead, valuations just keep rising, results notwithstanding. 

At least for now.

_Update: Mathematician Daniel Litt reports a related series of hallucinations with OpenAI’s Deep Research, in[this X thread](https://x.com/littmath/status/1891868756340547809?s=61)._

[Share](https://garymarcus.substack.com/p/grok-3-beta-in-shambles?utm_source=substack&utm_medium=email&utm_content=share&action=share)

 _**Gary Marcus** is baffled by the persistent attachment of the community and its investors to scaling uber alles despite abundant and repeated counterevidence of the same general form, over and over and over again. On the other hand, Gary loved the film [Groundhog Day](https://en.wikipedia.org/wiki/Groundhog_Day) and retains hope thast someday things will get better._

[1](https://garymarcus.substack.com/p/grok-3-beta-in-shambles#footnote-anchor-1-157434611)

Also west of Denver, if one were counting both Canada and Mexico are cities such as Saskatoon, Tijuana, Chihuaha, Puerto Vallarta, etc. A smarter system might have clarified.

[2](https://garymarcus.substack.com/p/grok-3-beta-in-shambles#footnote-anchor-2-157434611)

Note that part — but not all — of Montana is west of the western edge of Colorado, but that Billings is entirely west of Denver, a finer point that Deep Search seemed to miss. Don’t know if that error stems from the geographical nuance..
