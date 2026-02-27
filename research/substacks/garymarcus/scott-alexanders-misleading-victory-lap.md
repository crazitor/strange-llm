---
title: "Scott Alexander’s Misleading Victory Lap"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/scott-alexanders-misleading-victory"
---

Has the thorny, decades-old problem of compositionality finally be solved? 

In an essay yesterday called, _[Now I Really Won That AI Bet](https://www.astralcodexten.com/p/now-i-really-won-that-ai-bet)_ the well-known blogger Scott Alexander, more or less made that argument yesterday, proclaiming victory on old bet (with someone else, not me) and implying that this meant that AI has “master[ed] image compositionality”. 

Compositionality is, roughly speaking, about understanding and/or constructing wholes in terms of their parts. The crux of Alexander’s crowing is that a few years ago he predicted that generative AI would succeed on a certain set of prompts by June 2025, and, sure enough, now they have. 

To be sure, Alexander is on strong grounds to say he won the specifics of his bet, and correct that the field has made some progress. But at the same time he has accidentally slipped into very weak form of argument, often known as the [motte and bailey](https://en.wikipedia.org/wiki/Motte-and-bailey_fallacy), in which someone proves a mild assertion (the motte) and erroneously asserts victory on a larger, more controversial question (the bailey).

§

The motte here is the bet. I agree that Alexander won his bet. He said that Generative AI would make progress on a certain specific set of prompts, and it has. 

Here’s an example of his on which GPT4o now succeeds.

[](https://substackcdn.com/image/fetch/$s_!gfpF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcb04fe6a-674c-4501-be7b-f1148c345660_1190x1260.png)

The bailey is that victory on this particular bet (with someone random person that I have never even heard of) means that generative AI has “master[ed]” compositionality with respect to images. 

I didn’t get involved in the bet in 2022 because I thought it was a stupid bet. Why? Because GenAI’s can memorize anything, and you can build a bunch of augmented data to address any specific known problem. That doesn’t mean you have a _general_ solution. 

The field of AI is littered with Band-Aid solutions that work for one problem, and not the next. 

It’s no different here. It took me only few minutes to find many examples in which GPT 4o (the same model Alexander used) _failed_ on tasks that turn on compositionality. 

Here’s one: “ _draw five characters on a stage, from left to right, a one-armed person, a five-legged dog, a bear with three heads, a child carrying a donkey, and a doctor carrying a bicycle with no wheels_ ” . GPT 4o failed in four consecutive tests:

[](https://substackcdn.com/image/fetch/$s_!YQVT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0ccfa035-1265-4a1a-b1f2-a36a31bc011a_1536x1024.png)

In my first try, above, the man erroneously had two arms, rather than one, the bear had two heads rather than three, and the bicycle had one wheel rather than zero. Three other tries yielded similar errors, like this one, never quite returning what I asked for. 

[](https://substackcdn.com/image/fetch/$s_!xFal!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82a5e70a-b376-491f-9480-a8606706143f_1512x1309.png)

(GPT 4o also failed to accurately diagnose its own errors, misreading its own output, which represent a different kind of failure of compositionality.)

A few further minutes’ experimentation quickly revealed several other easily-elicited types of failures, mainly involving parts and wholes (which Ernie Davis and I have discussed here numerous times).

[](https://substackcdn.com/image/fetch/$s_!yYh5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff9702db5-9107-4eb3-ba53-3c2ac2012a18_1654x2220.jpeg)

Or to take a different kind of example, similar to one I showed with o3 a couple weeks ago, labeling of parts:

[](https://substackcdn.com/image/fetch/$s_!aPdt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf0a57ab-ff18-4dea-be4c-d35687b079c3_1563x1265.jpeg)

My June 22, 2025 update, [Image Generation: Still Crazy After All These Years](https://garymarcus.substack.com/p/image-generation-still-crazy-after?r=8tdk6) to my earlier 2022 [Horse Rides Astronaut](https://garymarcus.substack.com/p/horse-rides-astronaut) was filled with more examples that show ongoing failures in compositionality, including some with the arguably better o3.

[](https://substackcdn.com/image/fetch/$s_!bGQ_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0c4f2993-ea25-4009-837c-0b8c11a520e7_1456x1255.webp)

Performance on Chollet et al’s [ARC-AGI 2](https://github.com/arcprize/ARC-AGI-2), is also from what I understand still poor, including in a section focused on compositionality. 

[](https://substackcdn.com/image/fetch/$s_!pF4w!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F768d806f-4a5a-4997-8be0-5a486fc8c854_2174x1333.png)

To be fair, GPT-4o is, in my informal testing, markedly better than DALL-E 2, e.g., correctly nailing for example “Picture of a scientist in a nightclub holding a blue frisbee with a red basketball on top”. 

But it is not reasonable to conclude from the occasional success on one sort of publicly-discussed set of prompts that GPT has _mastered_ compositionality writ large. 

§

More broadly, concluding anything from specific prompts crafted and shared publicly years ago is a mistake. And not a new one either – as I pointed out to Alexander in June 2022 essay (that he read and replied to) called [What does it mean when an AI fails? A Reply to SlateStarCodex’s riff on Gary Marcus](https://open.substack.com/pub/garymarcus/p/what-does-it-mean-when-an-ai-fails?r=8tdk6&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false). Boldface in the original:

> **In the end, the real question is not about the replicability of the** _**specific strings**_**… but about the replicability of the general phenomena**.

Alexander, even after corrected three years ago, still largely confuses success on a prompt with general, broad competence at a particular ability. 

This conflation is problematic for multiple reasons. One is [data contamination](https://www.theatlantic.com/technology/archive/2025/03/chatbots-benchmark-tests/681929/), since any given prompt that has been circulated publicly potentially becomes part of the training data, including with custom data augmentation, especially with large armies of subcontractors. The steelman version of the argument would have considered this; Alexander didn’t address at all.

Another is that psychology can rarely be inferred directly from small samples of data, as for example cognitive psychology John R. Anderson argued in the early 1970, in part because many possible answers can be generated from multiple underlying mechanisms. Looking at a single output rarely tells you much. In the particular case, we know that the system succeeds at previously-discussed prompts but does less well on ones not previously-discussed. That tells us something about the internal mechanism, and suggests that it is far from robust. Looking only at the previously discussed prompts in isolation yields a misleading picture.

Another lesson from cognitive psychology is that anyone looking for a single test to conclude anything is probably barking up the wrong tree.

§

Overall, the form of Alexander’s argument is simply flawed:

  * I (Scott) made a bet with some rando in 2022 that (generative) AI would be able to perform well a on certain specific set of prompts. 

  * Those prompts have something do with compositionality [assembling wholes from prompts]

  * Now AI well does on those prompts.

  * Therefore AI has mastered compositionality.




Concluding that success on _some prompts_ implies overall mastery is a textbook example of the fallacy of composition, of inferring that what is true of some subset is necessarily true of the whole. It is an _enormous,_ unjustified __ leap from the motte of “the systems can now solve some compositionality problems” to the bailey of “the systems have mastered compositionality”.

§

Allow me to end with an open letter:

_Dear Scott,_

_Congratulations on winning your bet with Vitor. You are known for “steelmanning” arguments: considering the strongest possible version of an argument and trying to refute that. I wholly support this approach, but I don’t think it was best represented here. How about you take on a stronger version of the argument? Want another bet?_

_It took me less than an hour to find half a dozen clear counterexamples in which ChatGPT 4o failed with respect to compositionality, evident even to a teenager. When we are really at AGI it will be much harder to do so. I predict that such counterexamples will still be easy to find at the end of 2027 because of limitations inherent in LLMs._

_Let’s put some more steel in your bet._

_– Gary_
