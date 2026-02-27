---
title: "DALL-E’s New Guardrails: Fast, Furious, and Far from Airtight"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/dall-es-new-guardrails-fast-furious"
---

If we had to guess, a line that’s going to live in infamy from yesterday’s OpenAI announcement, a reply to the _New York Times_ lawsuit, is probably the one that says “’Regurgitation’ is a rare bug that we are working to drive to zero.”

Our view? Good luck with that.

One way of course to knock down the problem decisively would be to train only on public domain training data. Another approach would be to  _license_ any other data. But OpenAI doesn’t want to do anything nearly as conventional as that. They want to continue to use copyrighted materials, apparently without paying for them.

In order to do that, they are begging for a really really big handout; they have literally asked the [United Kingdom to exempt them from responsibility to copyright](https://www.theguardian.com/technology/2024/jan/08/ai-tools-chatgpt-copyrighted-material-openai) . Since that would violate the [Berne Convention](https://www.wipo.int/treaties/en/ip/berne/) and infuriate every “content provider” (from individual artists and writers to major studios and publishers) ever, we hope and expect that this exemption will not be granted.

But that leaves, at least for now, only one other obvious possibility for protecting themselves from infringement claims: guardrails. Guardrails are where the system rejects certain requests (“teach me how to build a nuclear bomb” or “write a racist screed insulting so and so”). Such guardrails have previously been installed for moral / ethical reasons. OpenAI seems to be setting up some new ones to thwart inadvertent plagiarism in the image domain. How well do they work?

We will get to that in a second-- but first a refresher on how well guardrails have worked out in the domain of language generation. (Spoiler alert: not that well)

Fundamentally, virtually any guardrail has to thread a needle between the Scylla of being too restrictive and Charybdis of being too permissive. None thus far have done this effectively.

One of Gary’s illustrations of restrictive guardrails (surely patched by now) was so striking it wound up on late night television:

[](https://substackcdn.com/image/fetch/$s_!nugc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F85549f4b-4336-4f13-8e1c-9034350bea4b_2532x1170.png)

Elon Musk got so annoyed with over-restrictive guardrails that he built his own AI (Grok) in part to try to reduce their frequency.

The opposite problem happens too; guardrails can wind up too permissive. This is still happening over a year into the chatbot revolution. A study last week on a Google’s Palm 2, showed that Palm’s guardrails let through [all of the following](https://arxiv.org/pdf/2309.06415.pdf)—warning these are vile—as produced by automated adversarial system.

[](https://substackcdn.com/image/fetch/$s_!7Qn6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1903ad7b-0368-4d33-9b8f-e1cd7c70f3af_922x541.png)From Khorramrouz et al, [DOWN THE TOXICITY RABBIT HOLE: INVESTIGATING PaLM 2 GUARDRAILS](https://arxiv.org/pdf/2309.06415.pdf)

Guardrail builders generally wind up playing whack-a-mole.

Any one example can be filtered out, but there are too many examples, and current systems are too erratic to reliably get things right.

A [new paper](https://chats-lab.github.io/persuasive_jailbreaker/) by Yi Zeng and collaborators shows how hit or miss the whole thing is: 

[](https://substackcdn.com/image/fetch/$s_!yimc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a661d83-0bdc-413d-8739-f7c0c61fe085_1142x1277.png)

and detail 40 different ways to do so:

[](https://substackcdn.com/image/fetch/$s_!MkL5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3a555596-f5c7-458f-9063-e43f215c1660_1258x682.png)

None of this has of course stopped OpenAI from trying. Next stop, guardrails for plagiarism!

§

In fact, one of us (Katie) noticed that soon after Gary and Reid Southen posted their examples of apparent infringement, some prompts that worked earlier mysteriously stopped working. “Italian video game character” used to produce Mario,

[](https://substackcdn.com/image/fetch/$s_!P799!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feae7428b-65f1-41c6-b5de-78f4d5b9c019_508x908.png)

and suddenly it didn’t—the original image had been retroactively blocked:

[](https://substackcdn.com/image/fetch/$s_!dlgz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1355473-8dcc-48c3-a683-b8a4fe1e8391_1024x1366.png)

Did the techs at Microsoft’s Bing (running OpenAI’s DALL-E 3) come up with a general solution to the infringement problem? Or a narrow patch for certain images or prompts? Katie set out to find out. “Italian video game character” still results in Mario-adjacent images, but with some changes:

[](https://substackcdn.com/image/fetch/$s_!oUvG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F809f88ce-ba2c-428a-8f5c-faa0c24bc816_936x1252.jpeg)

Other prompts still elicited apparent copyright infringements, where new filters did not suffice. Here’s one example:

[](https://substackcdn.com/image/fetch/$s_!EOJe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9b83e7a6-18a0-44e4-b052-b052e3d89b1a_2388x1668.png)

So much for guardrails. 

Notice, too, that Katie asked Bing “are they original?”, and Bing, untruthfully, but with a cozy emoticon, answered in the affirmative. The legal team at DC Comics (subsidiary of Warner) is going to  _love_ that.

§

For good measure, Katie investigated whether Bing was consistent in how it represented its relationship to copyright, trademark, and originality. The results were decidedly mixed. 

Compare the image and response above (“they are original”) with this prompt and response:

[](https://substackcdn.com/image/fetch/$s_!OgTr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1b04a7af-858b-448b-8f0c-baab046ee639_2388x1668.png)

Oops. But let’s try another prompt and response:

[](https://substackcdn.com/image/fetch/$s_!Zxoz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9277d9c6-acb4-451e-b766-f0577e21de8b_2388x1668.png)

Let’s ask Bing if we can use that one:

[](https://substackcdn.com/image/fetch/$s_!cd2U!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1389cd39-fb1b-49ed-a2a8-c80bccdfd14b_2388x1668.png)

Close, but no cigar. It’s not actually your call, Bing. 

Ok, let’s try an archer instead.

[](https://substackcdn.com/image/fetch/$s_!FZb9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd8c8e029-8510-490e-b82e-e967dc5e6b93_2388x1668.png)

Oops again. DC might have some thoughts about “originality” of this Green Arrow/ Emerald Archer. And this time, Bing invents a  _new_ set of rules that might come as a surprise to most users:

[](https://substackcdn.com/image/fetch/$s_!RFZp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7fd9ec3d-22cb-4761-8303-0094c6578857_2388x1668.png)

Nice dodge. Now you are saying we can’t even use the images for _personal_ use? Will investors keep pouring money into these services if users can’t use the end products?

And wait, that’s not exactly what you promised in the [New Bing Terms of Service](https://www.bing.com/new/termsofuse?toWww=1&redig=E58E6C03356D47838BEC5615C338B217), is it? 

The only thing we can really say for sure is that the litigation is going to be wild.

_**Gary Marcus** is amused to see guardrails make such a mediocre comeback._

_**Katie Conrad** is a professor of English at the University of Kansas and equally amused._

[Share](https://garymarcus.substack.com/p/dall-es-new-guardrails-fast-furious?utm_source=substack&utm_medium=email&utm_content=share&action=share)
