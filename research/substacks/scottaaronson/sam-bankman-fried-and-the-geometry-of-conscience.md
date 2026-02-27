---
title: "Sam Bankman-Fried and the geometry of conscience"
author: "Scott Aaronson"
date: "Sun, 13 Nov 2022"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=6797"
---

**Update (Dec. 15):**[This](https://sarahconstantin.substack.com/p/why-infinite-coin-flipping-is-bad), by former Shtetl-Optimized guest blogger Sarah Constantin, is the post about SBF that I should’ve written and wish I had written.  
  
**Update (Nov. 16):** Check out this [new interview of SBF](https://www.vox.com/future-perfect/23462333/sam-bankman-fried-ftx-cryptocurrency-effective-altruism-crypto-bahamas-philanthropy) by my friend and leading Effective Altruist writer Kelsey Piper. Here Kelsey directly confronts SBF with some of the same moral and psychological questions that animated this post and the ensuing discussion--and, surely to the consternation of his lawyers, SBF answers everything she asks. And yet I still don't know what exactly to make of it. SBF's responses reveal a surprising cynicism (surprising because, if you're that cynical, why be _open_ about it?), as well as an optimism that he can still fix everything that seems wildly divorced from reality.

I still stand by most of the main points of my post, including:

  * the technical insanity of SBF's clearly-expressed attitude to risk ("[gambler's ruin](https://en.wikipedia.org/wiki/Gambler%27s_ruin)? more like gambler's opportunity!!"), and its probable role in creating the conditions for everything that followed,
  * the need to diagnose the catastrophe correctly (making billions of dollars in order to donate them to charity? STILL VERY GOOD; lying and raiding customer deposits in course of doing so? DEFINITELY BAD), and
  * how, when sneerers judge SBF guilty just for being a crypto billionaire who talked about Effective Altruism, it ironically lets him off the hook for what he _specifically_ did that was terrible. 



But over the past couple days, I've updated in the direction of understanding SBF's psychology a lot less than I thought I did. While I correctly hit on certain aspects of the tragedy, there are other important aspects--the [drug use](https://astralcodexten.substack.com/p/the-psychopharmacology-of-the-ftx), the cynical detachment ("life as a video game"), the impulsivity, the apparent lying--that I neglected to touch on and about which we'll surely learn more in the coming days, weeks, and years. -SA

* * *

Several readers have asked me for updated thoughts on AI safety, now that I'm 5 months into my [year at OpenAI](https://scottaaronson.blog/?p=6484)--and I promise, I'll share them soon! The thing is, until last week I'd entertained the idea of writing up some of those thoughts for an essay competition run by the [FTX Future Fund](https://ftxfuturefund.org/), which (I was vaguely aware) was founded by the cryptocurrency billionaire [Sam Bankman-Fried](https://en.wikipedia.org/wiki/Sam_Bankman-Fried), henceforth SBF.

Alas, unless you've been tucked away on some Caribbean island--or perhaps, _especially_ if you have been--you'll know that the FTX Future Fund has ceased to exist. In the course of 2-3 days last week, SBF's estimated net worth went from ~$15 billion to a negative number, possibly the fastest evaporation of such a vast personal fortune in all human history. Notably, SBF had promised to give virtually all of it away to various worthy causes, including mitigating existential risk and helping Democrats win elections, and the worldwide [Effective Altruist](https://en.wikipedia.org/wiki/Effective_altruism) community had largely reoriented itself around that pledge. That's all now up in smoke.

I've never met SBF, although he was a physics undergraduate at MIT while I taught CS there. What little I knew of SBF before this week, came mostly from reading Gideon Lewis-Kraus's [excellent _New Yorker_ article](https://www.newyorker.com/magazine/2022/08/15/the-reluctant-prophet-of-effective-altruism) about Effective Altruism this summer. The details of what happened at FTX are at once hopelessly complicated and--it would appear--damningly simple, involving the misuse of billions of dollars' worth of customer deposits to place risky bets that failed. SBF has, in any case, [tweeted](https://mobile.twitter.com/SBF_FTX/status/1590709166515310593) that he "fucked up and should have done better."

You'd think none of this would directly impact me, since SBF and I inhabit such different worlds. He ran a crypto empire from the Bahamas, sharing a group house with other twentysomething executives who often dated each other. I teach at a large state university and try to raise two kids. He made his first fortune by arbitraging bitcoin between Asia and the West. I own, I _think_ , a couple bitcoins that someone gave me in 2016, but have no idea how to access them anymore. His hair is large and curly; mine is neither.

Even so, I've found myself obsessively following this story because I know that, in a broader sense, I _will_ be called to account for it. SBF and I both grew up as nerdy kids in middle-class Jewish American families, and both had transformative experiences as teenagers at [Canada/USA Mathcamp](https://www.mathcamp.org/). He and I know many of the same people. We've both been attracted to the idea of small groups of idealistic STEM nerds using their skills to help save the world from climate change, pandemics, and fascism.

Aha, the sneerers will sneer! Hasn't the entire concept of "STEM nerds saving the world" now been utterly discredited, revealed to be just a front for cynical grifters and Ponzi schemers? So if I'm _also_ a STEM nerd who's _also_ dreamed of helping to save the world, then don't I stand condemned too?

I'm writing this post because, if the Greek tragedy of SBF is going to be invoked as a cautionary tale in nerd circles forevermore--which it will be--then I think it's crucial that we tell the _right_ cautionary tale.

It's like, imagine the Apollo 11 moon mission had _almost_ succeeded, but because of a tiny crack in an oxygen tank, it instead exploded in lunar orbit, killing all three of the astronauts. Imagine that the crack formed partly because, in order to hide a budget overrun, Wernher von Braun had secretly substituted a cheaper material, while telling almost none of his underlings.

There are many excellent lessons that one could draw from such a tragedy, having to do with, for example, the construction of oxygen tanks, the procedures for inspecting them, Wernher von Braun as an individual, or NASA safety culture.

But there would also be _bad_ lessons to _not_ draw. These include: "The entire enterprise of sending humans to the moon was obviously doomed from the start." "Fate will always punish human hubris.” "All the engineers' supposed quantitative expertise proved to be worthless."

From everything I've read, SBF's mission to earn billions, then spend it saving the world, seems something like this imagined Apollo mission. Yes, the failure was total and catastrophic, and claimed innocent victims. Yes, while bad luck played a role, so did, shall we say, _fateful decisions with a moral dimension_. If it's true that, as alleged, FTX raided its customers' deposits to prop up the risky bets of its sister organization Alameda Research, multiple countries' legal systems will surely be sorting out the consequences for years.

To my mind, though, it's important not to minimize the gravity of the fateful decision by conflating it with everything that preceded it. I confess to taking this sort of conflation extremely personally. For eight years now, the rap against me, advanced by thousands (!) on social media, has been: _sure, while by all accounts Aaronson is kind and respectful to women, he seems like exactly the sort of nerdy guy who, still bitter and frustrated over high school, could 've chosen instead to sexually harass women and hinder their scientific careers._ In other words, I stand condemned by part of the world, not for the choices I made, but for choices I _didn 't_ make that are considered "too close to me" in the geometry of conscience.

And I don't consent to that. I don't wish to be held accountable for the misdeeds of my doppelgängers in parallel universes. Therefore, I resolve not to judge anyone else by their parallel-universe doppelgängers either. If SBF indeed gambled away his customers' deposits and lied about it, then I condemn him for it utterly, but I refuse to condemn his hypothetical doppelgänger who didn't do those things.

Granted, there are those who think _all_ cryptocurrency is a Ponzi scheme and a scam, and that for that reason alone, it should've been obvious from the start that crypto-related plans could only end in catastrophe. The "Ponzi scheme" theory of cryptocurrency has, we ought to concede, a substantial case in its favor--though I'd rather opine about the matter in (say) 2030 than now. Like many technologies that spend years as quasi-scams until they aren't, maybe blockchains _will_ find some compelling everyday use-cases, besides the well-known ones like drug-dealing, ransomware, and financing rogue states.

Even if cryptocurrency remains just a modern-day tulip bulb or Beanie Baby, though, it seems morally hard to distinguish a cryptocurrency trader from the millions who deal in options, bonds, and all manner of other speculative assets. And a traditional investor who made billions on successful gambles, or arbitrage, or creating liquidity, then gave virtually all of it away to effective charities, would seem, on net, _way_ ahead of most of us morally.

To be sure, I never pursued the "Earning to Give" path myself, though certainly the concept occurred to me as a teenager, before it had a name. Partly I decided against it because I seem to lack a certain brazenness, or maybe just willingness to follow up on tedious details, needed to win in business. Partly, though, I decided against trying to get rich because I'm selfish (!). I prioritized doing fascinating quantum computing research, starting a family, teaching, blogging, and other stuff I liked over devoting every waking hour to _possibly_ earning a fortune only to give it all to charity, and _more likely_ being a failure even at that. All told, I don't regret my scholarly path—especially not now!—but I'm also not going to encase it in some halo of obvious moral superiority.

If I could go back in time and give SBF advice--or if, let's say, he'd come to me at MIT for advice back in 2013--what could I have told him? I surely wouldn't talk about cryptocurrency, about which I knew and know little. I might try to carve out some space for deontological ethics against pure utilitarianism, but I might also consider that a lost cause with this particular undergrad.

On reflection, maybe I'd just try to convince SBF to weight money logarithmically when calculating expected utility (as in the [Kelly criterion](https://en.wikipedia.org/wiki/Kelly_criterion)), to forsake the linear weighting that SBF [explicitly advocated](https://mobile.twitter.com/SBF_FTX/status/1337250686870831107) and that he seems to have put into practice in his crypto ventures. Or if not logarithmic weighing, I’d try to sell him on _some_ concave utility function--something that makes, let's say, a mere $1 billion in hand seem better than $15 billion that has a 50% probability of vanishing and leaving you, your customers, your employees, and the entire Effective Altruism community with less than nothing.

At any rate, I'd try to impress on him, as I do on anyone reading now, that the choice between linear and concave utilities, between risk-neutrality and risk-aversion, is not bloodless or technical--that it's essential to make a choice that's not only in reflective equilibrium with your highest values, but that you'll still consider to be such regardless of which possible universe you end up in.
