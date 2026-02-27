---
title: "This one important fact about current AI explains almost everything"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/this-one-important-fact-about-current"
---

When I was in graduate school a friend told me something I’ve never forgotten: the key dividing line (“the median split”) on the SAT math, between those with above average scores versus below, lies between those who understand fractions, and those who do not. 

The mental dividing line in AI is between those who understand, deeply, the fact that I am about to share, and those who don’t. 

Those who do not have wasted a tremendous amount of money.

§

The simple fact is that current approaches to machine learning (which underlies most of the AI people talk about today) are lousy at outliers _,_ which is to say that when they encounter unusual circumstances, like the subtly altered word problems that I mentioned a few days ago, they often say and do things that are absurd. (I call these _discomprehensions_.)

Here’s another typical example. sent to me by a reader a few months ago:

[](https://substackcdn.com/image/fetch/$s_!Y5UV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe4a9381-5d46-4293-a5a2-71fc65b738ea_932x926.jpeg)

If it’s not directly in the training set, but merely superficially like some previous examples, there could be trouble.

§

I have tried to explained the outlier issue in dozens of ways over the last thirty years, but (as Steve Pinker pointed out to me yesterday) _The Wall Street Journal_ really nailed it in a new video on driverless car accidents, with a picture, and a quote from a Carnegie Mellon computer scientist, Phil Koopman.

Here’s the picture, part of [an analysis of specific car crash](https://www.wsj.com/video/series/tesla-autopilot/the-hidden-autopilot-data-that-reveals-why-teslas-crash/68D26569-0251-4637-A035-A5131D8883B8). In the image a line is superimposed around an overturned double trailer.

[](https://substackcdn.com/image/fetch/$s_!bBWi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff640664c-1d6b-42cc-9da1-579534fdd29f_1023x819.jpeg)

And here is what Professor Koopman says about the crash in the video.

> _The kind of things that tend to go wrong with these systems are things like [the system is] not trained on pictures of the overturned double trailer. It just didn’t know what it was. There were some lights there but the lights were in unusual positions. A person would’ve clearly said something big is in the middle of the road. But the way machine learning works is it trains on a bunch of examples and if it encounters something it doesn’t have a bunch of examples for it may have no idea what’s going on._

Everyone commenting on or thinking about AI should learn it by heart, if not verbatim, certainly the gist.

§

As Pinker noted in a [tweet](https://x.com/sapinker/status/1818621298374791589?s=61), this could have come from one of the papers that he and I wrote together about language in the 1990s. Machine learning had trouble with outliers then, and it still does.

Or as I put it in my own tweet:

> _The AI world pretty much divides into two groups: those who understand why current machine learning techniques suck at outliers, and therefore struggle at things like driverless cars and high-level reasoning in unusual circumstances — and those who don’t._
> 
> _Those who don’t have burned $100M on driverless cars and are in process of burning similar amounts of money on GenAI._

An entire industry has been built - and will collapse - because people aren’t getting it.

§

The people who have temporarily gotten rich or famous on AI have done so by pretending that this outlier problem simply doesn’t exist, or that a remedy for it is imminent. When the bubble deflation that I have been predicting comes, as [now seems imminent](https://garymarcus.substack.com/p/five-signs-that-the-genai-honeymoon?r=8tdk6), it will come because so many people have begun to recognize that GenAI can’t live up to expectations.

The reason it can’t meet expectations? Say it in unison, altogether now: GenAI sucks at outliers. If things [are far enough from the space of trained examples](https://www.sciencedirect.com/science/article/pii/S0010028598906946), the techniques of generative AI will fail. 

Here’s something I wrote in _1998_ , generalizing and further developing some of what Pinker and I had written about a few years before, in what I often think has been my most important scientific article. (Eliminative connectionism refers to neural network approaches that try to get away with cognition without symbol manipulation; I was talking about the forerunners to LLMs there.) 

[](https://substackcdn.com/image/fetch/$s_!5Ptk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9f1e86df-2ed4-4127-bc83-584fb57ec4d8_967x1859.png)

The article was inspired by some experiments I did with 3-layered neural networks, which are precursors of modern (many-layered) deep learning systems. In my experiments, I encountered boneheaded error after boneheaded error, on very simple problems, everytime I pushed the system to generalize far enough. A modest amount of generalization was possible; but things got systematically bad far from the training space.

Eventually I developed a theory (which has basically held true ever since) about what causes those errors and when they occur, and pinpointed the underlying issues. To the extent that my predictions over the last decade have been eerily accurate, it is largely because of that work and what it taught me about the function—and dysfunction—of neural networks.

The key point then, as now, was that handling outliers often requires generalizing beyond a space of training examples. The “localism” in how neural networks are trained makes that an inherent problem.

Over _a quarter century later_ , handling outliers is _still_ the Achilles’ Heel of neural networks. (Nowadays people often refer to this as the problem of distribution shift.)

§

The bit of language that Pinker and I focused on in the early 1990s almost seems trivial: [how children learn the past tense of English](https://pubmed.ncbi.nlm.nih.gov/1518508/), with its crazy mix of irregular verbs (_sing-sang_ , _think-thought, go-went_ , etc) and regular verbs (_walk-walked_ , _talk-talked_ , etc). Neural networks enthusiasts of the day tried to handle the entire collection of verbs with one big similarity-driven network; we argued for a more modular approach, with a split between a similarity-driven system for irregular verbs and a rule-based (symbolic) system for the regular [add -_ed_] verbs, which, crucially, could be used even for new verbs that _weren’t_ familiar or similar to others. One of Pinker’s many great examples was “In grim notoriety, Yeltsin outgorbacheved Gorbachev”. The point was that you could invent a new verb you had never heard before (outgorbachev) and the verb might sound different from all the verbs you had encountered (hence it was an outlier) and yet your rule based system could apply perfectly, without depending on the idiosyncracies of related training data. 

You don’t want your decisions about whether to run into a tractor trailer to depend on whether you have seen a tractor trailer in that particular orientation before; you want a general, abstract rule (don’t run into big things) that can be extended to wide range of cases, both familiar and unfamiliar. Neural networks don’t have a good way of acquiring sufficiently general abstractions.

In essence, we were arguing that even in the simple microcosm of language that is the English past tense system, the brain was a [neurosymbolic](https://garymarcus.substack.com/p/alphaproof-alphageometry-chatgpt) hybrid: part neural network (for the irregular verbs) part symbolic system (for the regular verbs, including unfamiliar outliers). Symbolic systems have always been good for outliers; neural networks have always struggled with them. For 30 years, this has been a constant. 

(This is also why we still use calculators rather than giant, expensive, yet still fallible LLMs, for arithmetic. LLMs often stumble on large multiplication problems because such problems are effectively outliers relative to a training set that can’t sample them all; the symbolic algorithms in calculators are suitably abstract, and never falter. It’s also why still use databases, spreadsheets, and word processors, rather than generative AI for so many tasks that require precision.)

§

The median split of AI wisdom is this: either you understand that current neural networks struggle mightily with outliers (just as their 1990s predecessors did) — and therefore understand why current AI is doomed to fail on many of its most lavish promises — or you don’t. 

Once you do, almost everything that people like Altman and Musk and Kurzweil are currently saying about AGI being nigh seems like sheer fantasy, on par with imagining that really tall ladders will soon make it to the moon. 

You can’t think we are close to AGI once you realize that as yet we have no general solution to the outlier problem. You just can’t.

_Gary Marcus has been studying natural and artificial intelligence for three decades and still lives in the hope that AI researchers will someday come to have more respect for the cognitive sciences._
