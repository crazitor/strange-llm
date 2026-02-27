---
title: "TIME’s cover story on D-Wave: A case study in the conventions of modern journalism"
author: "Scott Aaronson"
date: "Thu, 06 Feb 2014"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=1679"
---

This morning, commenter rrtucci pointed me to [TIME Magazine's cover story about D-Wave](http://content.time.com/time/magazine/article/0,9171,2164806,00.html) (yes, in today's digital media environment, I need _Shtetl-Optimized_ readers to tell me what's on the cover of TIME…). rrtucci [predicted](https://scottaaronson.blog/?p=1668#comment-100127) that, soon after reading the article, I'd be hospitalized with a severe stress-induced bleeding ulcer. Undeterred, I grit my teeth, paid the $5 to go behind the paywall, and read the article.

The article, by Lev Grossman, could certainly be a lot worse. If you get to the end, it discusses the experiments by Matthias Troyer's group, and it makes clear the lack of any practically-relevant speedup today from the D-Wave devices. It also includes a few skeptical quotes:

"In quantum computing, we have to be careful what we mean by 'utilizing quantum effects,'" says Monroe, the University of Maryland scientist, who's among the doubters. "This generally means that we are able to store superpositions of information in such a way that the system retains its 'fuzziness,' or quantum coherence, so that it can perform tasks that are impossible otherwise. And by that token there is no evidence that the D-Wave machine is utilizing quantum effects."

One of the closest observers of the controversy has been Scott Aaronson, an associate professor at MIT and the author of a highly influential quantum-computing blog _[aww, shucks -SA]_. He remains, at best, cautious. "I'm convinced … that interesting quantum effects are probably present in D-Wave's devices," he wrote in an email. "But I'm not convinced that those effects, right now, are playing any causal role in solving any problems faster than we could solve them with a classical computer. Nor do I think there's any good argument that D-Wave's current approach, scaled up, will lead to such a speedup in the future. It might, but there's currently no good reason to think so."

Happily, the quote from me is something that I actually agreed with at the time I said it! Today, having read the [Shin et al. paper](http://arxiv.org/abs/1401.7087)--which hadn't yet come out when Grossman emailed me--I might tone down the statement "I'm convinced … that interesting quantum effects are probably present" to something like: "there's pretty good evidence for quantum effects like entanglement at a 'local' level, but at the 'global' level we really have no idea."

Alas, ultimately I regard this article as another victim (through no fault of the writer, possibly) of the strange conventions of modern journalism. Maybe I can best explain those conventions with a quickie illustration:

**MAGIC 8-BALL: THE RENEGADE MATH WHIZ WHO COULD CHANGE NUMBERS FOREVER**

An eccentric billionaire, whose fascinating hobbies include nude skydiving and shark-taming, has been shaking up the scientific world lately with his controversial claim that 8+0 equals 17  _[ … six more pages about the billionaire redacted …]_ It must be said that mathematicians, who we reached for comment because we're diligent reporters, have tended to be miffed, skeptical, and sometimes even sarcastic about the billionaire's claims. Not surprisingly, though, the billionaire and his supporters have had some dismissive comments of their own about the mathematicians. So, which side is right? Or is the truth somewhere in the middle? At this early stage, it's hard for an outsider to say. In the meantime, the raging controversy itself is reason enough for us to be covering this story using this story template. Stay tuned for more!

As shown (for example) by [Will Bourne's story in _Inc._ magazine](http://www.inc.com/will-bourne/d-waves-dream-machine.html), it's _possible_ for a popular magazine to break out of the above template when covering D-Wave, or at least bend it more toward reality. But it's not easy.

More detailed comments:

  * The article gets off on a weird foot in the very first paragraph, describing the insides of D-Wave's devices as "the coldest place in the universe." Err, 20mK is pretty cold, but colder temperatures are routinely achieved in many other physics experiments. (Are D-Wave's the coldest _current, continuously-operating_ experiments, or something like that? ~~I dunno: counterexamples, anyone?~~ I've learned from experts that they're not, not even close. I heard from someone who had a bunch of dilution fridges running at 10mK in the lab he was emailing me from…)


  * The article jumps enthusiastically into the standard **Quantum Computing = Exponential Parallelism Fallacy (the QC=EPF)** , which is so common to QC journalism that I don't know if it's even worth pointing it out anymore (but here I am doing so).


  * Commendably, the article states clearly that QCs would offer speedups only for certain specific problems, not others; that D-Wave's devices are designed only for adiabatic optimization, and wouldn't be useful (e.g.) for codebreaking; and that even for optimization, "D-Wave's hardware isn't powerful enough or well enough understood to show serious quantum speedup yet." But there's a crucial further point that the article _doesn 't_ make: namely, that we have no idea yet whether adiabatic optimization is something where quantum computers  _can_ give any practically-important speedup. In other words, even if you could implement adiabatic optimization perfectly--at zero temperature, with zero decoherence--**we still don 't know whether there's any quantum speedup to be had that way,** for any of the nifty applications that the article mentions: "software design, tumor treatments, logistical planning, the stock market, airlines schedules, the search for Earth-like planets in other solar systems, and in particular machine learning." In that respect, adiabatic optimization is extremely different from (e.g.) Shor's factoring algorithm or quantum simulation: things where we  _know_ how much speedup we could get, at least compared to the best currently-known classical algorithms. But I better stop now, since I feel myself entering an infinite loop (and I didn't even need the adiabatic algorithm to detect it).


