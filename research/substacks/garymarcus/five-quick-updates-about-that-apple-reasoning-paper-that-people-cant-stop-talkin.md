---
title: "Five quick updates about that Apple reasoning paper that people can’t stop talking about"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/five-quick-updates-about-that-apple"
---

Five quick updates on that Apple paper everybody is talking about (see my summary [here](https://open.substack.com/pub/garymarcus/p/a-knockout-blow-for-llms?r=8tdk6&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true), if you don’t yet know what the fuss is about). 

The core of the paper challenged the idea that LLMs can reason on any deep level, and showed that they broke down on moderately complex versions of basic algorithms (since Tower of Hanoi with 8 discs, first solved with classical techniques around 1957) — casting serious doubt into whether LLMs on their own could ever achieve AGI. 

It was the latest in a long line of demonstrations (going back to my own work in 1998) of neural networks struggling with what is now known as distribution shift: generalization beyond what they have been trained on. To some extent they do this better than in 1998, but is still _the_ core challenge.

Needless to say AI enthusiasts are hoping mad. In effort to save face, many of them pointing to a rejoinder cowritten by one Anthropic’s Claude (under the pen name C. Opus) called “The Illusion of the Illusion of Thinking” that allegedly refutes the Apple paper. Emphasis on _allegedly_. 

Facts are not on their side. 

  1. “The illusion of the illusion” turned out to be an [error-ridden](https://x.com/blancheminerva/status/1933835315594104859?s=61) [joke](https://x.com/lxrjl/status/1934228650120872012?s=61). Literally. (If you read that last sentence carefully, you will see there are two links, not one; the first points out that there are multiple mathematical errors, the second is for an essay by the guy who created the Sokal-hoax style joke that went viral, acknowledging with chagrin. In short, the whole thing was a put on — unbeknownst to the zillions who reposted it. I kid you not.

[](https://substackcdn.com/image/fetch/$s_!jyzJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1de09708-2c80-483e-adfc-0ab811b70807_1336x1595.png)

  2. That said, loads of people who are trying to cope with the Apple paper are still circulating the Opus-co-written as if it were real and convincing. Pathetic. It’s especially pathetic because I had already addressed and dissected the paper’s main claim in my [Seven Replies](https://garymarcus.substack.com/p/seven-replies-to-the-viral-apple) essay a few days ago, showing its complexity claims didn’t explain the actual data. 

  3. On that topic, nobody has written a convincing reply to my Seven Replies essay, despite the fact that about 90,000 people have read it. Excuse me for speculating, but I suspect that there has been no compelling reply because the hypesters don’t have a compelling answer. That doesn’t look good for skeptics of the Apple paper.

  4. Computational linguist @msukhareva just added a technical dissection of the Opus-written paper, which you can find [here](https://msukhareva.substack.com/p/on-illusion-of-thinking-do-llms-reason), concluding, much as I do, “ _All in all, the Apple paper still stands its grounds and the LLM-generated debunking is weak at best_.”

  5. A new paper with a hard coding benchmark called LiveCodeBenchPro designed to resist data contamination shows still more converging evidence for the two core notions behind the Apple paper (and behind my own decades-long critique): (a) the systems are challenged at reasoning, and (b) performance declines as one strays further and further from familiar problems. 

Rohan Paul nicely summarizes the new benchmark, created by authors from multiple universities in a thread that starts [here:](https://x.com/rohanpaul_ai/status/1934751145400111572?s=61)

[](https://substackcdn.com/image/fetch/$s_!U7LS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F282650d0-1de7-44d6-bb80-b9f8f5a230a7_1291x1848.jpeg)

In sum, performance on hard coding problems, an alleged area of LLM strength, _drops to zero_ when you control nicely for contamination. This strongly echoes a result that Ernest Davis and I discussed here in April, in which [AI performance dropped precipitously on problems that were tested within six hours of a contest, making problem-specific data-augmentation difficult](https://garymarcus.substack.com/p/reports-of-llms-mastering-math-have).




Bottom line? What the Apple paper said still looks to be basically correct. Nitpicking (with or without mathematical blunders) is not going to change the fact that GenAI is still struggling with distribution shift, after almost 3 decades of work. On familiar problems with no wrinkles, they are great. On anything else they are suspect.

Or, as the software engineer Gorgi Kosev just put it on X, “[LLMs] are decent solvers of already solved problems, indeed.”

If we want to get to AGI, we’ll need to do a lot better.

_**Gary Marcus** is sorry to keep writing about how LLMs struggle with distribution shift, but it’s the whole ballgame._

_._
