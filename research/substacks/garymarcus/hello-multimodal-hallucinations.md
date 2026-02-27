---
title: "Hello, Multimodal Hallucinations"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/hello-multimodal-hallucinations"
---

“[I would bet you any sum of money you can get the hallucinations right down into the line of human-expert rate within months.”](https://time.com/collection/time100-ai/6309447/reid-hoffman/)

— Reid Hoffman, CEO of LinkedIn, Co-Founder of Inflection.AI, September 2023

What would make hallucinations actually go away? More data? Maybe different data? Multimodal data, combining vision and language to ground the language? That’s a theory we’ve often heard at conferences.

Is it true?

We started thinking about this the other day, when Ernie did an experiment. He’s fond of seeing how things change over time. In Rebooting AI, published in 2019, we focused largely on language but used a few visual examples; one is reprinted below, Julia Child’s kitchen. Here’s the image (printed in black and white in the book, but reproduced here in color):

[](https://substackcdn.com/image/fetch/$s_!j4YV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef8d4550-5ba9-4c87-8c66-a5199596a7b3_800x676.png)

Ernie then posed a bunch of questions that we had an original draft (most were cut in the final). 

The model didn’t do so well. To begin with, it missed the subtle “how many chairs are partially visible in the ” (three our by count, two by the model’s count[1](https://garymarcus.substack.com/p/hello-multimodal-hallucinations#footnote-1-138157264)) that we emphasized in our book, and it stumbled on “how many drawers are there that pull straight out” (model counts 3, we count 6, though one could perhaps defend other answers).

But then things got even more interesting. ChatGPT went utterly wild when Ernie pushed on the last one, omitting some that are there and and confabulating a standalone island in the middle of the kitchen that simply isn’t there: 

[](https://substackcdn.com/image/fetch/$s_!7HDT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F50138843-8ebb-45fd-830f-c51e13bdf104_816x610.png)

In another followup, the model confidently confabulated a refrigerator

[](https://substackcdn.com/image/fetch/$s_!hCJr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2640d56c-872d-4ec8-8577-3375a28af4be_800x652.png)

There’s nothing particularly new about these “hallucinations” per se. As is by now widely known, they are a hallmark of systems that generalize based on word distribution. But wait, what happened to the theory that grounding text in images would resolve that problem? 

As we can see, multimodal training is not magically making hallucinations go away. GPT-v (the visual version of GPT) can use words like _refrigerator_ and _counter_ , but that doesn’t mean it actually knows what these things mean.. The old systems were lost in a sea of correlations between words; the new system are lost in a sea of correlations between words and pixels. 

§

We often get accused (unfairly in our view) of moving goalposts. It’s worth noting that this particular example is five years old. It may get fixed, with a band-aid of some sort or another, but we are confident a zillion other pictures like it will probably yield similar errors. 

Indeed, after we wrote a first draft of the above, we went and looked for more examples. They weren’t hard to find. What time is shown in [the clock below](https://x.com/nleseul/status/1714489887024369801?s=61&t=2voLMkhJf6P349CqztWSAQ), for example?

[](https://substackcdn.com/image/fetch/$s_!aKn0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F156a95aa-106a-4e79-9beb-ade810e9186e_1088x1256.jpeg)

The vision scientist Anh Nguyen documented a whole series of hallucinations; the system knows what some of the entities are in the image, but not who is wearing what. ChatGPT’s answers are the usual mix of truth and authoritative bullshit we have come to expect:

[](https://substackcdn.com/image/fetch/$s_!0FVE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffa9fe9b5-46a3-482b-add9-61f270409dd4_1170x1536.jpeg)

Extra credit for this one:

[](https://substackcdn.com/image/fetch/$s_!ax95!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8351d978-3b26-463f-ae65-25bfe0374aed_1170x1473.png)

§

Back in the 1970’s, a lot of work went into building AI systems with explicit models of the world, like Terry Winograd’s [SHRLDU](https://hci.stanford.edu/winograd/shrdlu/), which modeled a simple blocks world. To our knowledge, no LLM-based system can yet reliably do what SHRLDU tried to do then:

[](https://substackcdn.com/image/fetch/$s_!WMcD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6b8b824b-4b0a-456c-b97f-c047d14c4508_1666x2305.jpeg)

§

Image synthesis is different from the kind of image analysis we focused on above, but one see signs of the same issues there, like in this example Dr. Vicki Bear sent to us just as we were wrapping this post up:

[](https://substackcdn.com/image/fetch/$s_!_CmG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9c3b425b-a6db-4f57-b13b-55cc9fc79fb9_1324x1862.jpeg)

The whole point of Rebooting AI was that the AI of 2018 didn’t actually understand how the world works, and that we couldn’t trust AI that didn’t. We stand fully by what we said.

§

To be sure, large language models are, in a lots of ways, an incredible advance over the AI of the 1970s. They can engage in a much broader range of tasks, and generally they need less hand-tinkering (Though they still need some – that’s what reinforcement learning with human feedback is really about.) And it’s lovely how they can quickly absorb vast quantities of data.

But in other ways, large language models are a profound step backwards; they lack stable models of the world, which means that they are poor at planning, and unable to reason reliably; everything becomes hit or miss.. And no matter what investors and CEOs might tell you, hallucinations will remain inevitable. 

Reid, if you are listening, Gary is in for your bet, for $100,000.

[Share](https://garymarcus.substack.com/p/hello-multimodal-hallucinations?utm_source=substack&utm_medium=email&utm_content=share&action=share)

 _**Gary Marcus** first publicly worried about neural network hallucinations in his 2001 book The Algebraic Mind._

_**Ernest Davis** , Professor of Computer Science at NYU, has been worrying about how to get computers to have common sense for even longer._

[1](https://garymarcus.substack.com/p/hello-multimodal-hallucinations#footnote-anchor-1-138157264)

Didja miss one? You can barely see the one farthest away, just a dark curve that signifies the top of a chair behind the table. But look again, you’ll see it.
