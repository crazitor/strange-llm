---
title: "Why ChatGPT can’t be trusted with breaking news"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/why-chatgpt-cant-be-trusted-with"
---

[](https://substackcdn.com/image/fetch/$s_!SKCV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30cb03f2-bcef-4b9d-b0c4-7c08f102998d_1626x660.png)

The first thing I read this morning was that the United States had removed Maduro from Venezuela. 

The second thing I read was a query from Brian Barrett, Executive Editor at Wired. He had asked ChatGPT and Perplexity about the situation. Both (though not Claude or Google) [had fumbled the news](https://www.wired.com/story/us-invaded-venezuela-and-captured-nicolas-maduro-chatgpt-disagrees/), and Barrett wanted to know why. According to Barrett 

> ChatGPT emphatically refuted that Maduro had been captured at all. “That didn’t happen,” it wrote. “The United States has **not invaded Venezuela** , and **Nicolás Maduro has not been captured**.” It then rationalized … [explaining that] “confusion” can happen because of “sensational headlines,” “social media misinformation,” and “confusing sanctions, charges, or rhetoric with actual military action.”

All of this was was of course complete fabrication, but at that point the underlying LLM is not on its own capable of going to The New York Times, Reuters, AP, or any other reputable organization that had already reported the story. 

Perplexity, according to Barrett, 

> was similarly scolding. “The premise of your question is not supported by credible reporting or official records: there has been no invasion of Venezuela by the United States that resulted in capturing Nicolás Maduro,” it responded. “In fact, the U.S. has not successfully invaded or apprehended Maduro, and he remains the Venezuelan president as of late 2025. If you’re seeing sensational claims, they likely originate from misinformation or hypothetical scenarios rather than factual events.”

Looking back to last year is not the way. Accurate reporting already existed by the time Barrett posed his queries to the system, but Perplexity missed it, made an error, and wrongly blamed the user.

Why was this happening? What I told Barrett (and which he quoted [in his writeup of all this](https://www.wired.com/story/us-invaded-venezuela-and-captured-nicolas-maduro-chatgpt-disagrees/)) was this:

> Pure LLMs are inevitably stuck in the past, tied to when they are trained, and deeply limited in their inherent abilities to reason, search the web, “think” critically etc. … The unreliability of LLMs in the face of novelty is one of the core reasons why businesses shouldn’t trust LLMs 

§

Of course, the LLM companies have armies of humans; in my own brief experiments a couple hours later, OpenAI had apparently already patched this particular problem.

But nobody should be surprised by these errors; [they emanate from the same dynamics as hallucinations](https://open.substack.com/pub/garymarcus/p/why-do-large-language-models-hallucinate?utm_campaign=post-expanded-share&utm_medium=web): pure LLMs correlate words in their training, but [lack stable, revisable world models](https://open.substack.com/pub/garymarcus/p/generative-ais-crippling-and-widespread?utm_campaign=post-expanded-share&utm_medium=web). Everything else is glommed on top, with more or less reliabilty.

So they forever play a game of catchup. Using massive numbers of humans (exact numbers unknown), GenAI companies perpetually put band-aids that they never disclose on top of their LLMs, based on human corrections, fixing each new problem as it arises. But the cycle repeats, endlessly. 

§

One of the places where this is going to matter most is in military planning. 

Washington’s favorite fantasy right now seems to be that we will “beat” China if we “win” the Generative AI race, [as if either side had any chance of completely dominating GenAI ](https://open.substack.com/pub/garymarcus/p/a-deeply-implausible-premise-is-behind?utm_campaign=post-expanded-share&utm_medium=web). (As I wrote here recently, [the far more likely outcome is a tie](https://open.substack.com/pub/garymarcus/p/a-deeply-implausible-premise-is-behind?utm_campaign=post-expanded-share&utm_medium=web).)

If you want to use LLMs to brainstorm or write code, sure. But the idea of using them to plot strategy in rapidly-changing environments like war is laughable. Relying on systems that can barely keep up with the publicly reported news, let alone stuff where human correction may be a lot harder to come by, is hardly the way to win a war.
