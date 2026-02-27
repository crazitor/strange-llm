---
title: "What “game over” for the latest paradigm in AI might look like"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/what-game-over-for-the-latest-paradigm"
---

[](https://substackcdn.com/image/fetch/$s_!lJio!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F926d6014-dd1c-4abc-af5e-c60a42c635ab_256x256.jpeg)_“tombstone with the words ‘here lies scaling maximalism’ “_

 __

In May, in a tweet that gave rise to this very Substack, DeepMind executive Nando de Freitas declared AGI victory, possibly prematurely, shouting “It’s all about scale now! The Game is Over!”:

[Nando de Freitas 🏳️‍🌈@NandoDFSomeone’s opinion article. My opinion: It’s all about scale now! The Game is Over! It’s about making these models bigger, safer, compute efficient, faster at sampling, smarter memory, more modalities, INNOVATIVE DATA, on/offline, … 1/N thenextweb.comDeepMind’s new Gato AI makes me fear humans will never achieve AGI8:46 AM · May 14, 2022

* * *

233 Reposts · 890 Likes](https://twitter.com/NandoDF/status/1525397036325019649?s=20&t=hm-285U9t6XMpO4X8QU47g)

de Freitas was arguing that AI doesn’t need a paradigm shift; it just needs more data, more efficiencies, bigger servers. I called this hypothesis—that AGI might arise from larger scale without fundamental new innovation— “scaling-über-alles”. I [pointed out many problems](https://garymarcus.substack.com/p/the-new-science-of-alt-intelligence); de Freitas never replied.

His hypothesis, now generally called _scaling maximalism,_ remains extremely popular, in no small part because bigger and bigger models have indeed continued to do ever more impressive things. 

_So far_. 

The trouble of course is that months or even years of going up and up on some measures still does not in fact remotely entail that scale is all we need. Ponzi schemes go up and up until they explode. Scaling is an empirical observation, not a guaranteed, continued law of nature. 

This week I saw not one but three striking premonitions for how the scaling maximalism hypothesis might end.

  1. **There might not be enough data in the world** to make scaling maximalism work. A bunch of people have already worried about this. This week saw a formal proof by William Merrill, Alex Warstadt, and Tal Linzen arguing that [“current neural LMs are not well suited” to extracting natural language semantics “without an infeasible amount of data”](https://arxiv.org/pdf/2209.12407.pdf). The proof makes too many assumptions to be taken as gospel, but if it is even close to correct, there may soon be real trouble in Scaling City.

  2. **There might not be enough available compute in the world to make scaling maximalism feasible**. Also this very week, Miguel Solano sent me a manuscript, (to which I am now contributing, along with Maria Elena Solano) that argues that scaling the current meta benchmark du jour, [Big Bench](https://github.com/google/BIG-bench), would require just over one-fourth of the U.S.’s entire electricity consumption in 2022. 

  3. **Some important tasks might simply not scale**. The most vivid illustration of this is a linguistics task by Ruis, Khan, Biderman, Hooker, Rocktäschl, and Grefenstette examining the pragmatic implications of language (e.g., quoting from their paper, “we intuitively understand the response “I wore gloves” to the question “Did you leave fingerprints?” as meaning “No.”). [As I have long argued, capturing this without cognitive models and common sense is really hard](https://arxiv.org/abs/2002.06177). Scaling here was largely AWOL; even the best model was only at 80.6%, and for most models, scaling had at best a neglible effect. As the lead author, Laura Ruis, has pointed out to me, a more complex version of the task can easily be imagined; performance there would be presumably even lower. What hit me hard, as I was reading the paper, is that asymptotic 80% performance _on even a single important task_ like this might spell game over for scaling. If you get syntax and semantics but fail on pragmatics or commonsense reasoning, you don’t have AGI you can trust. 




Moore’s Law didn’t carry us as far and as fast as some people initially hoped, because it is not actually a causal law of the universe. Scaling maximalism is an interesting hypothesis, but I stand by my prediction that it won’t get us to AGI. This week rendered vivid three possible failure modes. Any one of them would mean we need a real paradigm shift, if we are to get to AGI. 

All of this points to the same conclusion: if we want to reach AGI we shouldn’t keep putting so many eggs in the scaling-über-alles basket.
