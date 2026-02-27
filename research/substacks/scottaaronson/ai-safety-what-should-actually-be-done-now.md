---
title: "AI safety: what should actually be done now?"
author: "Scott Aaronson"
date: "Sun, 16 Apr 2023"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=7230"
---

So, I recorded a 2.5-hour-long podcast with [Daniel Filan](https://danielfilan.com/) about "reform AI alignment," and the work I’ve been doing this year at OpenAI. The end result is … well, probably closer to my current views on this subject than anything else I've said or written! [Listen here](https://podcasts.google.com/feed/aHR0cHM6Ly9heHJwb2RjYXN0LmxpYnN5bi5jb20vcnNz/episode/NTM1YTQ1MzAtMDVlNS00OTE4LThlMjgtOWRmZWUzMjM1Mjk0) or [read the transcript here](https://axrp.net/episode/2023/04/11/episode-20-reform-ai-alignment-scott-aaronson.html). Here's Daniel's abstract:

> How should we scientifically think about the impact of AI on human civilization, and whether or not it will doom us all? In this episode, I speak with Scott Aaronson about his views on how to make progress in AI alignment, as well as his work on watermarking the output of language models, and how he moved from a background in quantum complexity theory to working on AI.

Thanks so much to Daniel for making this podcast happen.

* * *

Maybe I should make a broader comment, though.

From my recent posts, and from my declining to sign the [six-month AI pause letter](https://futureoflife.org/open-letter/pause-giant-ai-experiments/) (even though I sympathize with many of its goals), many people seem to have goten the impression that I’m not worried about AI, or that (ironically, given my job this year) I'm basically in the "full speed ahead" camp.

This is not true. In reality, I’m _full_ _of_ worry. The issue is just that, in this case, I’m also full of _metaworry_ --i.e., the worry that whichever things I worry about will turn out to have been the wrong things.

Even if we look at the pause letter, or more generally, at the people who wish to slow down AI research, we find that they wildly disagree _among themselves_ about why a slowdown is called for. One faction says that AI needs to be paused because it will spread misinformation and entrench social biases … or (this part is said aloud surprisingly often) because progress is being led by, you know, like, _totally gross_ capitalistic Silicon Valley nerdbros, and might enhance those nerds' power.

A second faction, one that _contains_ many of the gross nerdbros, is worried about AI because it might become superintelligent, recursively improve itself, and destroy all life on earth while optimizing for some alien goal. Hopefully both factions agree that this scenario would be bad, so that the only disagreement is about its likelihood.

As I'll never tire of pointing out, the two factions seem to have been converging on the same conclusion--namely, _AI progress urgently needs to be slowed down_ --even while they sharply reject each other's rationales and indeed are barely on speaking terms with each other.

OK, you might object, but that's just sociology. Why shouldn't a rational person worry about near-term AI risk _and_ long-term AI risk? Why shouldn't the ethics people focused on the former and the alignment people focused on the latter strategically join forces? Such a hybrid Frankenpause is, it seems to me, precisely what the pause letter was trying to engineer. Alas, the result was that, while a few people closer to the AI ethics camp (like Gary Marcus and Ernest Davis) agreed to sign, many others (Emily Bender, Timnit Gebru, Arvind Narayanan…) pointedly declined, because--as they explained on social media--to do so would be to legitimate the gross nerds and their sci-fi fantasies.

From my perspective, the problem is this:

  1. **Under the ethics people 's assumptions, I don't see that an AI pause is called for.** Or rather, while I understand the arguments, the _same_ arguments would seem to have justified stopping the development of the printing press, aviation, radio, computers, the Internet, and virtually every other nascent technology, until committees of academic experts had decided that the positive social effects would outweigh the negative ones, which might've been never. The trouble is, well, how do you even _study_ the social effects of a new technology, before society starts using it? Aren't we mostly _happy_ that technological pioneers went ahead with all the previously-mentioned things, and dealt with the problems later as they arose? But preventing the widespread societal adoption of GPT-like tools seems to be what the AI ethics camp _really_ wants, much more than preventing further scaling for scientific research. I reject any anti-AI argument that could be generalized and transplanted backwards to produce an argument against moving forward with, let's say, agriculture or metallurgy.
  2. **Under the alignment people 's assumptions, I _do_ see that an AI pause is urgently called for--but I'm not yet on board with their assumptions.** The kind of relentlessly optimizing AI that could form the intention to doom humanity, still seems very different to me from the kind of AI that’s astonished the world these past couple years, to the point that it’s not obvious how much progress in the latter should increase our terror about the former. Even Eliezer Yudkowsky [agrees](https://www.youtube.com/watch?v=AaTRHFaaPG8) that GPT-4 doesn't seem too dangerous in itself. And an AI that was only _slightly_ dangerous could presumably be recognized as such before it was too late. So everything hinges on the conjecture that, in going from GPT-n to GPT-(n+1), there might be a "sharp turn" where an existential risk to humanity very suddenly emerged, with or without the cooperation of bad humans who used GPT-(n+1) for nefarious purposes. I still don't know how to think about the likelihood of this risk. The empirical case for it is likely to be inadequate, by its proponents' own admission. I admired how my friend Sarah Constantin thought through the issues in her recent essay [Why I Am Not An AI Doomer](https://sarahconstantin.substack.com/p/why-i-am-not-an-ai-doomer)--but on the other hand, as others have pointed out, Sarah ends up conceding a staggering fraction of the doomers' case in the course of arguing against the rest of it. What today passes for an "anti-doomer" might've been called a "doomer" just a few years ago.



In short, one could say, the ethics and alignment communities are _both_ building up cases for pausing AI progress, working at it from opposite ends, but their efforts haven't yet met at any single argument that I wholeheartedly endorse.

This might just be a question of timing. _If_ AI is going become existentially dangerous, then I definitely want global coordination well _before_ that happens. And while it seems unlikely to me that we're anywhere near the existential danger zone yet, the pace of progress over the past few years has been so astounding, and has upended so many previous confident assumptions, that caution seems well-advised.

But is a pause the right action? How should we compare the risk of acceleration now to the risk of a so-called "overhang," where capabilities might skyrocket even faster in the future, faster than society can react or adapt, _because_ of a previous pause? Also, would a pause even force OpenAI to change its plans from what they would've been otherwise? (If I knew, I'd be prohibited from telling, which makes it convenient that I don't!) Or would the main purpose be symbolic, just to show that the main AI labs can coordinate on _something_?

If so, then one striking aspect of the pause letter is that it was written without consultation with the main entities who would need to agree to any such pause (OpenAI, DeepMind, Google, …). Another striking aspect is that it applies only to systems "more powerful than" GPT-4. There are two problems here. Firstly, the concept "more powerful than" isn't well-defined: presumably it rules out more parameters and more gradient descent, but what about more reinforcement learning or tuning of hyperparameters? Secondly, to whatever extent it makes sense, it seems specifically tailored to tie the hands of OpenAI, while giving OpenAI's competitors a chance to catch up to OpenAI. The fact that the most famous signatory is Elon Musk, who's now trying to build an "anti-woke" chatbot to compete against GPT, doesn't help.

* * *

So, if not this pause letter, _what do I think ought to happen instead?_

I've been thinking about it a lot, and the most important thing I can come up with is: clear articulation of fire alarms, red lines, whatever you want to call them, along with what our responses to those fire alarms should be. Two of my previous fire alarms were the first use of chatbots for academic cheating, and the first depressed person who commits suicide after interacting with a chatbot. Both of those have now happened. Here are some others:

  * A chatbot is used to impersonate someone for fraudulent purposes, by imitating his or her writing style.
  * A chatbot helps a hacker find security vulnerabilities in code that are then actually exploited.
  * A child dies because his or her parents follow wrong chatbot-supplied medical advice.
  * Russian or Iranian or Chinese intelligence, or some other such organization, uses a chatbot to mass-manufacture disinformation and propaganda.
  * A chatbot helps a terrorist manufacture weapons that are used in a terrorist attack.



I'm extremely curious: which fire alarms are _you_ most worried about? How do you think the AI companies and governments should respond if and when they happen?

In my view, articulating fire alarms actually provides multiple benefits. Not only will it give us a playbook if and when any of the bad events happen, it will also give us clear _targets to try to forecast_. If we've decided that behavior X is unacceptable, and if extrapolating the performance of GPT-1 through GPT-n on various metrics leads to the prediction that GPT-(n+1) will be capable of X, then we suddenly have a clear, legible case for delaying the release of GPT-(n+1).

Or--and this is yet a third benefit--we have something clear on which to _test_ GPT-(n+1), in "sandboxes," before releasing it. I think the kinds of [safety evals](https://www.lesswrong.com/posts/4Gt42jX7RiaNaxCwP/more-information-about-the-dangerous-capability-evaluations) that ARC (the Alignment Research Center) did on GPT-4 before it was released--for example, testing its ability to deceive Mechanical Turkers--were an extremely important prototype, something that we'll need a lot more of before the release of future language models. But all of society should have a say on what, specifically, _are_ the dangerous behaviors that these evals are checking for.

So let's get started on that! Readers: which unaligned behaviors would you like GPT-5 to be tested for prior to its release? Bonus points for plausibility and non-obviousness.
