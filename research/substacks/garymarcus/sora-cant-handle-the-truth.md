---
title: "Sora Can’t Handle the Truth"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/sora-cant-handle-the-truth"
---

Probably the biggest single problem with large language models is that they make things up, enough so that the by now common but overly anthropomorphic term for such errors, _hallucination,_ was dictionary.com’s word of the year for 2023. 

Turns out Sora makes stuff up, too, Take a peek at the following and see if you can spot what I mean.

[](https://substackcdn.com/image/fetch/$s_!uDOQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb678b589-58b1-4296-b9ab-0c3e0fc57a8b_1098x815.png)full video [here](https://x.com/sama/status/1758249750909096142?s=61).

The image (a screenshot from fairly static Sora video that [Sam Altman generated](https://x.com/sama/status/1758249750909096142?s=61) for MrBeast, in a response to a request for a monkey playing chess in the park) is the visual equivalent of “frequently wrong and never in doubt”, a military expression that very much applies to LLMs. The image is detailed and sharp; it projects an authority and reality that did not happen. 

I am not complaining, mind you, about the fact that a monkey might pose in front of a chessboard, but about the chessboard itself: 3 kings, only one on the board, and a 7x7 rather than nearly universal 8x8 chess board (to say nothing of the pawn structure). Utterly impossible in chess—and presumably nowhere in the data set, either. Yet it rendered the image photorealistically. 

It is truly a fascinating — and revealing -- image, because presumably _none_ of the training data would ever have featured either a board or position like that. It’s the visual equivalent of ChatGPT claiming falsely that I have a pet chicken named Henrietta. Aside from showing that (not surprisingly) Sora is pretty clueless about chess, it’s revealing about how the [mysterious Sora](https://www.theatlantic.com/technology/archive/2024/02/openai-sora-generated-video-fake/677493/)**** even works. 

Let’s try to understand what the error reveals.

  * The error is _not_ an error of insufficient computational power, as one X commentator suggested. More compute is clearly making systems like Sora more and more detailed in its images, as this sample from OpenAI shows:




[](https://substackcdn.com/image/fetch/$s_!ecLw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02fd1b21-3002-4cd9-9096-bfc653cd4100_2388x804.png)

It is clear however from the sharpness of Sora’s images (including the monkey playing chess) that Sora, relative to predecessors and competitors, has been allocated immense amounts of compute. Sora’s images look like the 16x image on the right, not the “base compute”. So we can’t blame the peculiar board on a lack of compute.

  * When I (and others) started pointing out problems with GPT-2 and GPT-3, a common (though erroneous) refrain was that grounding LLMs in images, rather than just having them learn relations between words, would somehow make a big difference. Nowadays, we have “multimodal” systems, trained on both text and images, and the aforementioned “hallucinations” (perhaps better called _failed approximations_ , as Gerben Wierda [has pointed out](https://ea.rna.nl/2023/11/01/the-hidden-meaning-of-the-errors-of-chatgpt-and-friends/)) and other errors persist and even crop up in new ways. Sora is obviously grounded in relationships between videos and associated texts; yet that grounding is not enough to preclude 7x7 chessboards with 3 kings. 

  * It’s probably not fair to blame the weird board on a lack of data. Judging by the quality of its images, Sora was trained on an immense amount of data, including data about how things change over time. There are plenty of videos of people playing chess out there on the web. Chess boards don’t morph from 8x8 to 7x7 in the real world, and there are probably tons of 8x8 boards in the databases - and few if any 7x7. What Sora is doing is not a _direct_ function of its training data.

  * Unlike [the errors I described yesterday](https://garymarcus.substack.com/p/soras-surreal-physics), and similar errors that [others are starting to collect](https://www.reddit.com/r/AfterEffects/comments/1arul5a/comment/kqtegzz/?utm_source=share&utm_medium=web2x&context=3%0A%0A), the problem here isn’t physics. Rather, Sora is _failing to apprehend a cultural regularity of the world, despite ample evidence_. Some tried to excuse the errors I showed yesterday on the grounds that emulating physics is hard; one can’t say the same for the well-documented rules of chess. 

  * In some of the physics cases, one could argue that learning about sequences of frames over time poses particular challenges; again, that’s not the issue here, inasmuch as the chess board is stable across the video. (I am not, for example, complaining about pieces winking in and out of existence.)

  * It’s not about geometry, either. Ge Yang [has pointed a number of issues](https://x.com/episodeyang/status/1758273283198480808?s=61), there, too, but they don’t explain the unusual chess board and position.

  * It would also be wrong to say that Sora is altogether unable to generalize; it probably hasn’t seen too many videos with monkeys in front of chessboards in park settings; there is arguably _some_ generalization. But it’s drawing the _wrong_ generalization. Same thing as predicting that because some people have pet chickens, Gary Marcus has a pet chicken. There, ChatGPT generalized the statistics of English, but without regard to facts. Here, Sora has generalized the visual textures of chess boards, without quite grasping what the proper limits on such generalizations should be.




So what is going on? Wierda’s phrasing of _failed approximation_ hits the nail on the head. The system is trying to approximate the world, but it just isn’t very good at that job. It uses arrangements of pixels to predict other arrangements of pixels, but it does not try to build an internal model of physics, and it does not try to build an internal model of cultural artifacts, either. 

In most or all of the errors we have seen thus far, virtually every bit of the images are _locally_ correct; if you just looked at a tiny patch of a given flawed video in isolation, for a single moment, you wouldn’t notice anything wrong. What’s missing is any global comprehension by the system. In the video I discussed yesterday with [the gray wolf pups erratically coming in and out of existence](https://x.com/duborges/status/1758198356717846870?s=20), there is no database that says how many pups there are, and the system varies that number freely, as a function of pixels rather than representations of enduring creatures in the world.

In another video, [a stylish woman on Tokyo street](https://x.com/openai/status/1758192965703647443?s=61) takes [two steps left steps in a row](https://www.reddit.com/r/AfterEffects/comments/1arul5a/megathread_about_sora_and_how_it_will_change_our/kqo9d3m/), about 28 seconds in. Nothing is wrong with left steps, but the system doesn’t fully grasp that they need as a whole to alternate with right steps. Sora fundamentally revolves around trying to take pixels and reconstruct what pixels might be nearby in space and time. The forest is never perceived apart from the trees, and the chessboard is never perceived apart from its constituent squares. 

The six-fingered old man with a unicorn piercing through his head and asymmetrical arms that I discussed recently is another illustration of the same, a knowledge of individual pixels and what their neighbors look like, without an overall comprehension of the scene. 

[](https://substackcdn.com/image/fetch/$s_!iF6Z!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F026c18ae-1160-409d-a3f6-49bcdfc0e224_1024x1230.jpeg)

For a creative work, that fixation on the local at the expense of a deep representation of the global might (or might not) be fine, depending on the objective for a given piece of art. From AGI perspective, however, this is an immense warning sign. The factuality problems that have haunted LLMs are present even in a new architecture trained on ungodly amounts of data. 

A common theme is clearly present. The sooner the AI industry -- and the world at large — recognizes this, the better. Especially given the obvious downsides to this sort of technology.

_**Gary Marcus** is astonished that some people still haven’t recognized that generative AI has struggled mightily when it comes to world models, high level reasoning and factuality, even as evidence for that conclusion continues to pour in, even with data of ever-greater magnitude and sophistication.. _

P.S. As several people include Max Little have noted, [the vast majority of the samples of Sora so far largely consist of smoothly panned, slow motion](https://x.com/garymarcus/status/1758931644780892667?s=61), which fits in some ways with what I am noting above; suggesting the video rely heavily on local patches rather than global understanding. As X user Lathropa points out, “If it's just doing next-patch prediction, the most probable next-patch is just the current patch slightly moved or slightly morphed. A jump cut would be most/all of the pixels changed entirely unpredictably, but also entirely non-randomly (the new frame has to be self-coherent.)” There just a handful of such more dramatic cuts in the videos so far, and very little high-speed action. It will be interesting to see what happens when people try to broaden the requests.
