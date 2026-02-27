---
title: "Why *is* Bing so reckless?"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/why-is-bing-so-reckless"
---

[Jensen Harris@jensenharrisA wild story in which I probe what Bing's chatbot is capable of if you take away the rules: it gave wrong facts, wrote raunchy jokes, ordered a pizza, taught me how to rob a bank, burglarize a house, hot wire a car, and also cheated at a game of hangman! [youtu.be/pBtD2JUXfLU](http://youtu.be/pBtD2JUXfLU) 7:15 PM · Feb 18, 2023

* * *

8 Reposts · 26 Likes](https://twitter.com/jensenharris/status/1627023938013519872?s=12)

Anyone who watched the last week unfold will realize that the new Bing has (or had[1](https://garymarcus.substack.com/p/why-is-bing-so-reckless#footnote-1-104054052)) a tendency to get really wild, from declaring a love that it didn’t really have to encouraging people to get divorced to blackmailing them to teaching people how to commit crimes, and so on.

A lot of us were left scratching our heads. ChatGPT tended _not_ to do this kind of stuff (unless you used “jailbreaking” techniques to try to trick it), whereas from what I can tell, Bing went off the rails really fast. And the thing is, the two systems are basically close siblings; OpenAI built ChatGPT, and is now presumed to be working very closely with Microsoft, using the same technology. ChatGPT was, I believe, mainly powered by GPT 3.5 plus a module known as RLHF (which combines Reinforcement learning with human feedback, to put some guardrails in place). We all assumed that Bing’s Chatbot was more or less the same thing, but powered instead by a bigger, newer version of 3.5, which I’ll call GPT 3.6. (Or maybe it’s GPT-4; Microsoft has been very coy about this.)

Princeton professor Arvind Narayanan has the best thread I have seen on what’s gone wrong. Let’s start there; I mostly agree with he said. His take, with a few annotations, and then three important follow-ups:

[Arvind Narayanan@random_walkerConsidering that OpenAI did a decent job of filtering ChatGPT’s toxic outputs, it’s mystifying that Bing seemingly decided to remove those guardrails. I don't think they did it just for s***s and giggles. Here are four reasons why Microsoft may have rushed to release the chatbot.1:11 PM · Feb 19, 2023

* * *

90 Reposts · 484 Likes](https://twitter.com/random_walker/status/1627294819855790080?s=12)

 _Great question; but maybe they didn’t remove the guardrails; maybe the guardrails just didn’t work? I will return to that possibility—call it Possibility #5– below._

[ Arvind Narayanan@random_walkerThe bot's behavior has enough differences from ChatGPT that it can't be the same underlying model. Maybe the LLM only recently completed training (GPT-4?) If so, Microsoft may have (unwisely) decided to roll it out promptly rather than delay it for RLHF training with humans.1:11 PM · Feb 19, 2023

* * *

5 Reposts · 71 Likes](https://twitter.com/random_walker/status/1627294821340643328?s=12)

 _Narayanan’s Possibility 1 is that what we are seeing is a new model, possibly GPT-4, naked, unadorned by guardrails. As I wrote in[Inside the Heart of ChatGPT’s Darkness](https://garymarcus.substack.com/p/inside-the-heart-of-chatgpts-darkness), there’s a lot of nastiness lurking inside large language models; maybe MSFT did nothing to protect us from that._

[Arvind Narayanan@random_walkerPossibility #2: they built a filter for Bing chat, but it had too many false positives, just like ChatGPT's. With ChatGPT it was only a minor annoyance, but maybe in the context of search it leads to a more frustrating user experience.1:13 PM · Feb 19, 2023

* * *

4 Reposts · 49 Likes](https://twitter.com/random_walker/status/1627295222660038657?s=20)

 _Possibility 2 was that there filter was too annoying to use inside a real search engine. Possibility 3 was that “Bing deliberately disabled the filter for the limited release to get more feedback about what can go wrong.” Possibility 4 was that “they thought that prompt engineering would create enough of a filter and genuinely didn't anticipate the ways that things can go wrong.”_

 _Naranyan then wraps up, dead-on_

[ Arvind Narayanan@random_walkerThese are all just guesses. Regardless of the true reason(s), the rollout was irresponsible. But now that companies seem to have decided there's an AI "arms race", these are the kinds of tradeoffs they're likely to face over and over.1:18 PM · Feb 19, 2023

* * *

9 Reposts · 89 Likes](https://twitter.com/random_walker/status/1627296604871950337?s=20)

§

I want to extended beyond Narayanan’s excellent analysis in three ways I want to suggest an extra possibility, make some policy recommendations, and consider how it is that journalists initially failed us.

**The fifth possibility:** Maybe Microsoft _did try to_ stick their existing, already trained RLHF model on top of GPT 3.6—and it just didn’t work. 

The thing about reinforcement learning is that it is notoriously finicky; change the circumstances sligthly, and it may no longer work. 

DeepMind’s famous DQN reinforcement learning set records on Atari games, and then broke down under minor alterations (like moving the paddle a few pixels up, in the game of Breakout). **Maybe every new update of a large language model will require a complete retraining of the reinforcement learning module.**

This would be _very_ bad news _,_ not just in terms of human and economic costs (which would mean more underpaid layers doing awful work) but also in terms of trustworthiness, because it would be mean that we have zero guarantee that any new iteration of a large language model is going to safe. 

That’s especially scary for two reasons: first, the _big companies are free to roll out new updates whenever they like, without or without warning_ , and second it means that _they might need go on testing them on general public over and over again, with no idea in advance of empirical testing on the public for how well they work_. 

We don’t handle new pharmaceuticals like that (we demand careful tests before they go out to the public) and we shouldn’t handle LLMs this way, either—especially if billions of people might use them and there are potentially serious risks (e.g to people’s mental health, or marital status).

**Policy** : _the public has (or strictly speaking should insist on) a right_ _to know what wrong here_ , with the Bing situation, so that we can create policy to keep incidents from happening like this again. Right now, as I have said before, the AI is basically the Wild West; anyone can post any chatbot they want. Not good. Congress needs to to find out what happened, and start placing some restrictions, especially where emotional or physical injury could easily result.

**Journalism:** The media failed us here. I am particularly perturbed by Kevin Roose’s initial report, in which he said he was “awed” by Bing. Clearly, he had not poked hard enough; shouting out prematurely in _The New York Times_ that there is a revolution without digging deep (or bothering to check in with skeptics like me, or the terrific but unrelated Mitchells, Margaret and Melanie) is not a good thing.

With respect to the later, Ernest Davis and I gave some advice in [Rebooting AI ](http://rebooting.ai)that bears both repeating and updating. Here’s what we wrote then, in 2019; every word still applies: 

[](https://substackcdn.com/image/fetch/$s_!rfOx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fac5d133c-6449-4e23-a112-3f55f40011eb_2339x1565.png)

To all this I would add, for 2023, #7 are their guardrails adequate? Have they been investigated thoroughly? Please don’t tell us you are in “awe” of some new system without considering all 7.

Last word goes to Narayanan:

[Arvind Narayanan@random_walkerIt feels like we're at a critical moment for AI and civil society. There's a real possibility that the last 5+ years of (hard fought albeit still inadequate) improvements in responsible AI release practices will be obliterated.1:24 PM · Feb 19, 2023

* * *

33 Reposts · 130 Likes](https://twitter.com/random_walker/status/1627298065680945152?s=20)

 _**[Gary Marcus](http://garymarcus.com) **(@garymarcus),**** scientist, bestselling author, and entrepreneur, is a skeptic about current AI but genuinely wants to see the best AI possible for the world—and still holds a tiny bit of optimism. Sign up to his Substack (free!), and [listen to him on Ezra Klein](https://www.nytimes.com/2023/01/06/opinion/ezra-klein-podcast-gary-marcus.html). His most recent book, co-authored with Ernest Davis,[ Rebooting AI](http://rebooting.ai/), is one of Forbes’s 7 Must Read Books in AI. Watch for his new podcast on AI and the human mind, this Spring._

[Share](https://garymarcus.substack.com/p/why-is-bing-so-reckless?utm_source=substack&utm_medium=email&utm_content=share&action=share)

[1](https://garymarcus.substack.com/p/why-is-bing-so-reckless#footnote-anchor-1-104054052)

I say _had_ because we can all hope that some of this wildness will quickly get patched.
