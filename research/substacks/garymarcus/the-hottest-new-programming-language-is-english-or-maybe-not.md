---
title: "The hottest new programming language is English! Or maybe not."
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/the-hottest-new-programming-language"
---

Surely one of the hottest, and maybe smartest tweets of 2023, came from the AI star Andrej Karpathy, who joined OpenAI a few weeks later, and then left again (for the second time) a few days ago:

[](https://substackcdn.com/image/fetch/$s_!r0KF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F762aed59-4a2d-49e4-b30b-594b16f6bbfb_795x263.png)

_The New Yorker_ [quoted it](https://www.newyorker.com/magazine/2023/12/11/the-inside-story-of-microsofts-partnership-with-openai), and almost 4 million people viewed it. It’s not hard to see why. Programming in English, as opposed to languages like Python, C++, Fortran or Lisp, has long been a dream. The [most exciting article I ever read in ](https://www.technologyreview.com/2007/01/01/227178/anything-you-can-do-i-can-do-meta/)_[Technology Review](https://www.technologyreview.com/2007/01/01/227178/anything-you-can-do-i-can-do-meta/) , _was about pointed towards that prospect. At the time Charles Simonyi, an early Microsoft employee who lead the Microsoft Word project was building a startup company, founded in 2002, called Intentional Software, the goal of which was to let developers specify what they wanted as abstractly as possible, without having to write pesky computer code. The point was that “The customer wouldn’t feel straitjacketed by a programming language. Everyone would be happy.” As far I know, though, they didn’t entirely succeed; in 2017 [Simonyi sold the company back to Microsoft](https://www.zdnet.com/home-and-office/work-life/microsoft-buys-intentional-software-simonyi-to-rejoin-microsoft/), and returned there. The product was never widely released, to my knowledge.

Programming in English itself (a step beyond what Simonyi was working on) would be grand. No weird punctuation to learn, no idiosyncrasies of specific programming languages, no bothering to memorize how a given language worked. You could think in your native language, without having to translate into the rigid structures of machines.

With LLMs, we can finally glimpse what that future might feel like.

But the truth is it doesn’t work that well yet. But that doesn’t mean people aren’t trying. 

In fact, if the internet rumors are to be believed (and generally people seem to believe this particular one), GPT-4 is itself “programmed” partly in English, with an internal “[system prompt](https://patmcguinness.substack.com/p/gpt-4-system-prompt-revealed)”, hidden from the user, but ubiquitously in the background, as an unseen part of the conversation. 

Patrick McGuiness’s Substack[AI Changes Everything](https://open.substack.com/pub/patmcguinness) recently explained a trick that’s been floating around on the internet, and way you can (allegedly) get the system to spit out its internal prompt, the first little bit of visible here:

[](https://substackcdn.com/image/fetch/$s_!jNPZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8bbd8708-bfe9-464b-a28b-59ceea4a03c6_1407x1341.png)

That’s a _program_ , in essence for ChatGPT to follow.

The whole thing, for those who are interested, is allegedly [here](https://x.com/dylan522p/status/1755086111397863777?s=61) in this hard-to-read screenshot:

[](https://substackcdn.com/image/fetch/$s_!7co7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F519ae8bb-01b1-4919-9f10-6abb0d7b389c_2400x1161.png)

§

This morning on LinkedIn, Tim Estes pointed out to me something that is absolutely fascinating.

If the system really is being “programmed in English” _it is not always doing what is being asked to do_ : 

[](https://substackcdn.com/image/fetch/$s_!UOEC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0daa5963-66c5-4c89-9d8a-3b469c3ef845_1165x1082.png)

Much of what Reid Southen, Katie Conrad, and I recently described is in flagrant violation of those directives.

§

As a coder who calls himself BioBootloader on X points out, we have entered a whole new era:

[](https://substackcdn.com/image/fetch/$s_!8eLE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5069a5b-0fd4-4ce6-b702-aa1ab718a4de_1193x297.png)

Paraphrasing slightly, writing your program in English “prompts” is fast upfront, but downstream may lead to serious challenges in debugging. 

I have been coding since I was 8 years old (for money in college, but mostly just for fun). The thing about computers had, until now, always been that they do _exactly_ what you tell them to do. If a program I wrote didn’t work, it was because I made a mistake. If I tracked down the mistake, and fixed it, I could be confident that the system would work properly. It was a kind of glorious social contract; I do my part, and the system does its part. My trust in the coding infrastructure was essentially absolute. 

We have apparently just entered a new and different and frightening era, in which debugging involves not only fixing our own mistakes but coming to terms with machines that may or may not uphold their end of the bargain.

Already, [there is an argument that the quality of code has declined](https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality), in the era in which large language models have been used as copilots.

[](https://substackcdn.com/image/fetch/$s_!gc6n!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef0874e5-5c87-4985-94e0-32027429e30a_1419x1154.png)

And of course the idea of “smart contracts”, another form of moshing together language and code, has never really taken off.

§

Karpathy’s reinvention of Simonyi’s dream is sexy as hell. Who wouldn’t to program in English? And it’s easy see LLMs as the first real, though imperfect realization of Simony’s dream. 

But classical, formal, deterministic programming languages exist for a reason. They allow programs to specify with precision what they want. As Phil Libin pointed out in a message to me this morning, discussing a draft of this essay, “The reason that software engineering is done in formal languages is not because formal languages make it harder to specify what you want than English. Obviously. It’s because formal languages make it much, much easier to specify what you want.”

In the new regime, caveat emptor.

_**Gary Marcus** generally loves progress, but worries about where we are headed._
