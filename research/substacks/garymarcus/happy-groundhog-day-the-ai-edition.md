---
title: "Happy Groundhog Day, The AI Edition"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/happy-groundhog-day-the-ai-edition"
---

[](https://substackcdn.com/image/fetch/$s_!2uo2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3ff24df0-266d-4a6c-80e1-f85f457c5dd8_500x281.jpeg)

It’s Groundhog Day again! 30 years ago today, Bill Murray was starring in the iconic film that bears the same name. Poor guy keeps living the same day, over and over, trying to make better choices, and winds up right back where he started. (Travon Free’s Oscar-winning short _Two Distant Strangers_ is a powerful riff on the same theme, highly recommended.)

30 years ago, neural networks were, as they are now, in the midst of a rebirth. The first one collapsed; this one has more staying power.

But a lot of things that a bunch of us worried about 30 years ago remain true. Neural networks in the early 1990s struggled with compositionality (interpreting complex, hierarchical wholes in terms of their parts), abstraction, and plain old silly errors. 

Two famous papers, [one by Fodor and Pylyshyn](https://ruccs.rutgers.edu/images/personal-zenon-pylyshyn/proseminars/Proseminar13/ConnectionistArchitecture.pdf), the other [by Pinker and Prince](https://www.cs.ox.ac.uk/activities/ieg/e-library/sources/pinker_conn.pdf), both published in Cognition, had raised those issues, in 1988, with respect to some simple neural architecture that were popular then. Word on the connectionist (as we called it back then) street was that hidden layers might solve all those problems. I didn’t buy it, and showed in 2001 that pretty much the same problems remained when hidden layers (then just one, now many) were introduced. In a 1999 article I showed that [some of what was challenging for neural nets of the day was trivial for human infants, even with tiny amounts of data](https://pmvish.people.wm.edu/science1999.pdf).

Fast forward to now, and it seems to me that everything we were raising back in the day still looms large. Silly errors certainly do, and problems of abstraction are widespread in large language models. A subtler problem that I emphasized in 2001, an inability to keep track of knowledge of instances independently of kinds, seems to underlie the rampant hallucinations that allow large language models to say things like “Elon Musk died in a car crash in 2018”, even when nothing in the corpus says so, and massive amounts of data contradict the claim, because they blend together information about kinds with information about specific individuals, in haphazard ways.

I know it really irritates a lot of people when I say deep learning had hit a wall, so let me be perfectly clear: it counts as hitting a wall if you keep trying to do the same thing over and over and don’t succeed, even if you succeed on other dimensions. Deep learning has undeniably made amazing progress, on other dimensions, but the fact is it hasn’t solved the core problems that many of us thought were essential 30 years ago. Turns out you don’t need to solve them to make beautiful pictures, or decent if error-filled conversation, but anyone who thinks we can get to AGI without solving abstraction, compositionality, and the type-token distinction is kidding themselves. 

Here’s the best abstract I read today:, a careful study of compositionality in modern architectures:

[](https://substackcdn.com/image/fetch/$s_!-Zjv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbc10f53e-f04d-424a-9b08-dc4b25f825c6_1170x2175.png)

Straight out of 1993. The measures are new, the model is new, but the stumbling block remains the same.

One of my favorite papers from last year was Yasaman Razeghi’s analysis of LLMs doing arithmetic. Same story; only the architectures and training regimes have changed. The troubles with abstraction persist.

[](https://substackcdn.com/image/fetch/$s_!VLtQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe47f6c76-2c50-469d-8489-11081acc9255_1599x1387.jpeg)

Melanie Mitchell’s book, Bender et al’s “Stochastic Parrots”; all of these more recent criticisms of deep learning help establish that some of the basic issues that were known long ago, with predecessors to current models, still remain even today.

PS One more thing—I quit studying AI, for a while, in the late 1990s, because so much just seemed like handcrafted hacks. Not sure how much has changed in that regard, either, except that the hacks that were once written by graduate students are now farmed out to sweatshops, for a new form of handcrafting:

[Gary Marcus@GaryMarcus1980s: AI companies spend vast amounts of $ hiring humans to write rules to patch brittle symbolic systems. 2020s: AI companies spend vast amounts of $ hiring humans to to patch brittle neural systems. Alexandr Wang @alexandr_wangwe're starting to see top companies spend the same amount on RLHF and compute in training ChatGPT-like LLMs for example, OpenAI hired >1000 devs to RLHF their code models crazy—but soon companies will start spending $ hundreds of Ms or $ billions on RLHF, just as w/compute1:54 AM · Feb 2, 2023

* * *

27 Reposts · 102 Likes](https://twitter.com/garymarcus/status/1620963954750259204?s=46&t=SIJaNfVKU4XuGd__kRqCCA)

Back then we needed hacks because our AI didn’t really understand the world; a lot of systems were bags of tricks that were fairly superficial. They were brittle; they might work in the lab, but not in the real world. Our new systems work better, but they are still superficial, fine for lab demos but often at a loss in the real world. Death by a thousand edge cases is still the norm, and probably will be, for another few years, unless and until people learn a little bit of history. 

In that spirit, here are a few suggested readings from the old days, in honor of Groundhog Day:

[Gary Marcus@GaryMarcus@s_r_constantin Essential readings on why so much in modern ML reminds so many of us of the film Groundhog Day: • Fodor and Pylyshyn 1988 Cognition • Pinker and Prince 1988 Cognition • Pinker 1999 Words and Rules • Marcus et al 1999 Science • Marcus 2001 The Algebraic Mind12:15 AM · Jan 6, 2023

* * *

4 Reposts · 34 Likes](https://twitter.com/garymarcus/status/1611154343217995779?s=46&t=0eJLAjJ776rvEMSZvrlXTg)

Things turned out ok for Bill Murray, eventually. Hopefully they will for us, too. 

_**[Gary Marcus](http://garymarcus.com) **(@garymarcus),**** scientist, bestselling author, and entrepreneur, is a skeptic about current AI but genuinely wants to see the best AI possible for the world—and still holds a tiny bit of optimism. Sign up to his Substack (free!), and [listen to him on Ezra Klein](https://www.nytimes.com/2023/01/06/opinion/ezra-klein-podcast-gary-marcus.html). His most recent book, co-authored with Ernest Davis,[ Rebooting AI](http://rebooting.ai/), is one of Forbes’s 7 Must Read Books in AI. _

[Share](https://garymarcus.substack.com/p/the-cnet-fake-news-fiasco-autopilot?utm_source=substack&utm_medium=email&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNDgwNzUyNiwicG9zdF9pZCI6OTk0Mzk1ODEsImlhdCI6MTY3NTI5Njg5MiwiZXhwIjoxNjc3ODg4ODkyLCJpc3MiOiJwdWItODg4NjE1Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9._KxNIbgbkwncQ089-NMrF0k_MRz0AeFFHoYF3ji5jaA)
