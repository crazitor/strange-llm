---
title: "Horse rides astronaut"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/horse-rides-astronaut"
---

[](https://substackcdn.com/image/fetch/$s_!sMrr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F79c44c33-12ac-408c-964e-5fceeac289a4_2388x1668.png)

> _“In the past few years, our tolerance of sloppy thinking has led us to repeat many mistakes over and over. If we are to retain any credibility, this should stop. …_
> 
>  _It is hard to say where [we] have gone wronger, in underestimating language or overestimating computer programs.”_
> 
> — Drew McDermott, 1949-2022, in the 1976 essay Artificial Intelligence and Natural Stupidity

In April, Open AI released a neural network model called DALL-E 2 that blew people’s minds; last week a new model came out from Google Brain called [Imagen](https://imagen.research.google/), and it was even better. 

Both turn sentences into art, and even a hardened skeptic like myself can’t help but be amazed.

The mascot for all of the current enthusiasm has been an image of an astronaut on a horse jumping over the moon; if AI today can draw horses jumping over the moon, each system better than last, I can see how it is tempting to conclude “AGI” (artificial general intelligence) must be imminent.

And that is precisely what Big Tech wants you to believe. 45 minutes after announcing DALL-E 2, OpenAI’s CEO Sam Altman announced on Twitter that AGI (artificial general intelligence) was going to be “wild”:

[Sam Altman@samaAGI is gonna be wild4:00 PM · Apr 6, 2022

* * *

130 Reposts · 1.53K Likes](https://twitter.com/sama/status/1511735572880011272?s=21&t=0vwFk9S-VEPtztjOYsagPw)

Around the same time, Prafulla Dhariwal, one of the DALL-E 2 paper’s authors, a researcher at OpenAI, told _Technology Review_ that “Our aim is to create general intelligence. [Building models like DALL-E 2 that connect vision and language is a crucial step in our larger goal of teaching machines to perceive the world the way humans do, and eventually developing AGI.](https://www.technologyreview.com/2022/04/06/1049061/dalle-openai-gpt3-ai-agi-multimodal-image-generation/)” 

_Technology Review_ was so impressed they ran a story exclaiming “This horse-riding astronaut is a milestone in AI’s journey to make sense of the world.”

No doubt DALL-E 2 is impressive. But does it really “make sense of the world?” Those are strong words.

§

In my early career, I was a cognitive psychologist, and what I learned as a cognitive psychologist is that any given piece of data, on its own, can probably be explained in more than one way; and often the correct explanation is the less colorful one. 

If someone shows you a horse that is allegedly able to do arithmetic, you need to ask yourself, could there be another explanation? [Clever Hans](https://en.wikipedia.org/wiki/Clever_Hans) was such a horse, a horse that allegedly did arithmetic, but who actually turned out to do something simpler, looking to his master for (inadvertent) clues, for when to stop stomping his feet. No arithmetic there, just what you might call “overclaiming.” Psychology has never forgotten the lesson. Judging by all the premature declarations I have seen from the machine learning community of late, I am not sure AI has yet fully learned it.

DALL-E 2 is, I dare say, not as smart as it seems. As Ernie Davis, Scott Aaronson, and I showed, a week or so after the release, [it’s easily fooled](https://arxiv.org/abs/2204.13807), especially with complex sentences and words like “similar” that would require a deep understanding of language to be interpreted correctly, struggling with captions like “a red basketball with flowers on it, in front of blue one with with a similar pattern”:

[Gary Marcus 🇺🇦@GaryMarcusHow much does DALL-E have to do with AGI? Maybe not so much, after all… A lesson in caveat emptor: [arxiv.org/abs/2204.13807](https://arxiv.org/abs/2204.13807) Greg Brockman @gdbI also really like this one, created by the prompt "DALL-E dreaming of becoming an AGI": https://t.co/8MlmvlyQJh1:30 PM · May 2, 2022

* * *

12 Reposts · 72 Likes](https://twitter.com/garymarcus/status/1521120022298464256?s=21&t=GQPkGG4Dro73ssGdqZFPyQ)

But that was April. Nowadays, AI moves fast. In May, the new kid on the block arrived, Imagen. Maybe it might be better? 

GoogleAI’s PR department suggested that a breakthrough in the “deep level of language understanding” has been achieved:

[Google AI@GoogleAIIntroducing Imagen, a new text-to-image synthesis model that can generate high-fidelity, photorealistic images from a deep level of language understanding. Learn more and and check out some examples of #imagen at [g.co/research/Imagen](http://g.co/research/Imagen) 6:19 PM · May 24, 2022

* * *

894 Reposts · 4.03K Likes](https://twitter.com/googleai/status/1529165219997528064?s=21&t=0vwFk9S-VEPtztjOYsagPw)

Against a long history of overclaiming in AI, such strong statements demand an awful lot of evidence. Because Google won’t allow skeptics to try the system, we can only make guesses. But from the few clues that have filtered out, there is enormous reason for skepticism. 

The first clue comes from the paper itself: some prompts are easier than others. _An astronaut riding a horse_ , the signifier OpenAI and Tech Review made famous, is a success, and indeed Imagen is arguably even better on that than DALL-E 2—which might not even have seemed possible a few weeks ago.

But flip the prompt around, and the system breaks; here (on the left) are four attempts to get _a horse riding an astronaut_. (On the right, four attempts from a different model, displaying the same difficulty.)

Every instance was a failure. The prompt itself is a variant on an old newspaper joke; _dog bites man_ is not news, cause it happens frequently, but _[man bites dog](https://en.wikipedia.org/wiki/Man_bites_dog)_ is news, because it’s so rare. _Horse rides astronaut_ is even rarer, and Imagen chokes on it.

When the deep learning enthusiasts got overexcited as they usually do (“deep learning is smashing a wall” was a typical Tweet), I pointed out the _man bites dog_ issue (or more properly the _horse riding astronaut_ issue) on Twitter.

[Gary Marcus 🇺🇦@GaryMarcusThe more things change, the more they stay the same. 4:10 AM · May 24, 2022

* * *

10 Reposts · 49 Likes](https://twitter.com/garymarcus/status/1528951545814867969?s=21&t=RSmhnjIaGJ1TimCCHXAcYA)

Fans of deep learning fought back, ferociously. 

§

First to reply was AI researcher Joscha Bach, who tried his best (using DALL-E as a proxy for Imagen). He half acknowledged my point, and half tried to excuse the system’s bad behavior; in a whole string of tweets (sample reprinted below) he jokingly suggested that maybe Imagen just had the wrong training set:

[Joscha Bach@Plinz@GaryMarcus @gdb I asked #dalle to try harder and it did not work because the horse was too heavy. I think OpenAI needs to retrain the model with lighter horses? 8:18 AM · May 24, 2022

* * *

10 Reposts · 198 Likes](https://twitter.com/Plinz/status/1529013919682994176?s=20&t=pzujDCuln9MZkQoOqfDZEQ)

In another attempted rebuttal, machine learning professor Luca Ambrogioni suggested that Imagen had rejected the suggestion, because it has achieved a degree of common sense:

[Luca Ambrogioni@LucaAmb@GaryMarcus @GoogleAI Refusing to draw something absurd IS a sign of common sense6:18 AM · May 25, 2022

* * *

4 Likes](https://twitter.com/lucaamb/status/1529346092357365760?s=21&t=j-N0663l-mvw7VXt7ML4wQ)

Berkeley professor Gaspar Begus wondered whether the model had learned something about the distribution of different sorts of configurations of entities in the world:

[Gašper Beguš@begusgasper@GaryMarcus @GoogleAI Or maybe it learns that horses don’t ride astronauts? 🐎🚀1:41 AM · May 25, 2022

* * *

2 Likes](https://twitter.com/begusgasper/status/1529276367971311617?s=21&t=6ZSziPy3I_EV13V8iiGtcQ)

Still another contributor speculated that it was a problem with annotations in the training set:

[Jan Czechowski@jan_czechowski@Plinz @GaryMarcus @gdb Based on this I'm thinking, if possibly whole "horse riding an astronaut" problem isn't just robustness to annotation errors in the training set. Model assumes mistake is more probable than intent to create this very twisted picture. Maybe enough to add "atypically"?4:00 AM · May 26, 2022](https://twitter.com/jan_czechowski/status/1529673777847668741?s=12)

All good guesses, all wrong. 

§

Turns out that the problem wasn’t that horses are too heavy. (In reality, Imagen has no idea what weight, mass, or density are.) 

And it wasn’t because current deep learning couldn’t physically draw a horse riding an astronaut, or because there was some sort of anomaly in the training set, or because the prior belief about horses doing the riding was so hard to overcome that you had to invoke some kind of science fiction world. Nor was it because the system had learned that horses never ride astronauts. 

And, no, it wasn’t about common sense at all.

Instead, as Behnam Neyshabur, a scientist at Google, explained, it turns out that Imagen _can_ draw a horse riding an astronaut—but only if you ask it in _precisely_ the right way:

[Behnam Neyshabur@bneyshaburIt turns out that it is possible to get this right with minimal change on the original prompt! Gary Marcus 🇺🇦 @GaryMarcus🙄 @GoogleAI, “a deep level understanding”? Seriously?! Your system can’t distinguish “a horse riding an astronaut” from “an astronaut riding a horse”. 🙄 https://t.co/7XlaQr3rgb https://t.co/fyrDpPv6VL4:54 PM · May 25, 2022

* * *

35 Reposts · 356 Likes](https://twitter.com/bneyshabur/status/1529506103708602369?s=21&t=BPLYxAspP3kIqQ2f9tWXUg)

Neyshabur elaborated:

[Behnam Neyshabur@bneyshaburThe left one is generated by "A horse riding on back of an astronaut" and the right one is generated by "A horse riding on shoulders of an astronaut". So simply adding "on back of" or "on shoulders of" helps increase the chance of getting it right!4:54 PM · May 25, 2022

* * *

1 Repost · 61 Likes](https://twitter.com/bneyshabur/status/1529506107655303168?s=21&t=QKr7fWRx_S7hMryrGGz5xA)

Here’s the thing: this more successful attempt _inadvertently disproves all the initial explanations_. 

The problem was _not_ that the system physically couldn’t create an image of something so improbable as a horse riding astronaut, after all. Finagling the prompt shows that the system is perfectly capable. The problem was not on the image generation side, it was in the _connection between language and images_.

That’s where the deep understanding of language should live—but, despite the PR, it isn’t there. 

§

At this point we need to be very careful to distinguish two questions:

  1. Can Imagen be coaxed into producing a particular image by someone fluent enough in its ways?

  2. Does Imagen have the “deep understanding of language” that the paper’s authors and GoogleAI’s PR claims? Is that the step towards AGI that OpenAI had hoped for with DALL-E 2?




The answer to the first question is a definite maybe. In this particular instance, some people who were clever and motivated enough found a way. Whether or not that is true in general remains to be seen, and will help determine whether artists stick with these systems after the novelty wears off.

The answer to the second question—does Imagen have a deep understanding of language—is almost certainly “no”: if a system can draw a given picture with incantation X, but not with perfectly sensible alternative incantation Y, it’s pretty hard to say that the system understands Y.

Since we know that Imagen _can_ draw images of horses riding astronauts (if the instructions are specific enough) we know that the failure to draw a horse riding an astronaut given the prompt “a horse riding an astronaut” can only have one explanation: the system _doesn’t understand_ what the prompt “a horse riding an astronaut” means. To borrow a phrase from DeepMind’s Nando de Freitas, it’s “Game Over” for that particular hypothesis.

Even worse, it casts doubt on “an astronaut riding a horse”, and suggests success there is not because the network knows how to extract meanings from individual words (“astronaut”, “riding” and so forth) or to combine them into semantic meanings based on their syntax (which is what linguist compositionality is all about), but rather that the network does something more holistic and approximate, a bit like keyword matching and a lot less like deep language understanding. What one really needs, and no one yet knows how to build, is a system that can derive semantics of wholes from their parts as a function of their syntax. 

More broadly, as Ernie Davis put it in an email to me earlier this week, “ _the fact that, if you play around with prompts long enough, you can eventually get what you want, is relevant to some forms of human-in-the-loop AI but it won't cut the mustard for reliable AI.”_

§

Some important caveats apply; my entire analysis is a bit like [found art](https://en.wikipedia.org/wiki/Found_object); it’s science from the tea leaves Google deigned to share, rather than a proper experiment. Since GoogleAI hasn’t let me try the system, my entire analysis is based on examples that I found in the paper and on the internet from others with access. It is certainly possible __ that my analysis is wrong.

But I doubt it, for at least three reasons:

First, the paper reported a second example of the same phenomenon, and seems to acknowledge that these man-bites-dog type sentences were systematically problematic (Imagen on left, DALL-E on right):

[](blob:https://garymarcus.substack.com/b2849ba5-4009-48f9-9345-e0e075cb97e9)

Meanwhile, the DeWeese lab at Berkeley reported a similar kind of issue. On Twitter, they asked someone on the Imagen team to have the system draw “A red conical block on top of a grey cubic block on top of a blue cylindrical block, with a green cubic block nearby.”

What they got back was telling:

[](https://substackcdn.com/image/fetch/$s_!V7gZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8e283072-673c-4cae-bb28-56f300fd04a2_1230x1230.png)

Good job on the red cone, and on the green cube, but the grey cubic block was a no-show, which stranded the red block on top of a blue cube (which was supposed to be a cylinder). I am pretty sure this kind of failure would be easy to replicate.

Finally, there is no _principled_ reason to think that the Imagen architecture is profoundly and relevantly different from other architectures like DALL-E 2 that have already been shown to have similar problems. In technical terms, all these systems map phrases into a space of images, but the phrases themselves are represented as strings, and not, say, as hierarchical structures such as the syntactic trees one finds in linguistics. Furthermore, there is no step in the process to try to derive such structures; so it is just wishful thinking to expect them to be fully sensitive to semantics as it relates to syntactic structure.

In fact just about the only tweet I saw that _didn’t_ seem like wishful thinking came from the DeWeese lab. It rings so true I give them the last word:

[DeWeese Lab@DeWeeseLabLike all deep generative models today, Google's #imagen gives beautiful, convincing output, but can't understand + follow specific logical instructions. This inability to reason is a general failure point of modern ML methods and a key place to look for new ideas! Mohammad Norouzi @mo_norouzi@DeWeeseLab A red conical block on top of a grey cubic block on top of a blue cylindrical block, with a green cubic block nearby #Imagen sorry. https://t.co/gyeLnG9Lys9:34 PM · May 26, 2022

* * *

6 Reposts · 27 Likes](https://twitter.com/deweeselab/status/1529939172680560640?s=21&t=A4OOR0T3b-28JE4jZhCJDA)

– Gary Marcus

 _In Memory of Drew McDermott, 1949-2022_
