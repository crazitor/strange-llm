---
title: "Does AI really need a paradigm shift?"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/does-ai-really-need-a-paradigm-shift"
---

The provocative public conversation I am having with Scott Alexander, of SlateStarCodex fame, already a [meme](https://twitter.com/_mattbeard/status/1535246856644710408?s=21&t=g4An8AmjPThD5g_Yjo44YA), continues! 

In a fresh reply to my “[What does it mean when AI fails](https://garymarcus.substack.com/p/what-does-it-mean-when-an-ai-fails?s=w)?”, Alexander has put forward his second stimulating critique of the week, “[Somewhat Contra Marcus On AI Scaling](https://astralcodexten.substack.com/p/somewhat-contra-marcus-on-ai-scaling?s=r)”. 

Which is not to say it’s perfect; on the other hand, one doesn’t need perfection in order to be provocative. I will respond briefly to the disappointing part, and then we then get to the good stuff.

# Strawman, Steelman

In general, Alexander is known for being exceptionally fair to ideas he doesn’t particularly like, even if at times that makes him unpopular. An entry on Quora perfectly distills [this laudable aspiration](https://www.quora.com/Why-is-Slate-Star-Codex-so-popular/answer/Caio-Camargo?ch=17&oid=8797277&share=a32291f4&srid=tfZU&target_type=answer\]): 

> “[Scott Alexander] optimizes for enlightenment, rather than for winning arguments. Thus, when considering an issue, he will actively seek out and often formulate the strongest arguments (that is, steelman) [for] both sides.” 

I only wish he had extended the same courtesy to my position.

To take one example, Alexander puts words like _prove_ or _proven_ in my mouth:

> “Marcus says GPT’s failures prove that purely statistical AI is a dead end”

and

> GPT certainly hasn’t yet proven that statistical AI can do everything the brain does. But it hasn’t proven the opposite, either [as if Marcus said that it had].

But that’s a strawman. In reality I would never say that I have _proven_ anything; what I do as a scientist is to weigh evidence and suggest research directions. I say that we have given the scaling hypothesis a really good look (with a larger budget than all but a handful of projects in history), and as such the failures of large scale systems are _evidence (_ not proof) that we ought to seriously consider alternatives, e.g., here:

> Rather than supporting the Lockean, blank-slate view, GPT-2 appears to be an accidental counter-evidence to that view […]
> 
> GPT-2 is both a triumph for empiricism, and, in light of the massive resources of data and computation that have been poured into them, a clear sign that it is time to consider investing in different approaches.

In making it sound like I have declared proof when I have never made such declarations, Alexander paints me as an extremist, rather than a scientist who weighs evidence and uncertainty. Where has his steelperson aspiration gone?[1](https://garymarcus.substack.com/p/does-ai-really-need-a-paradigm-shift#footnote-1-58860020)

Another rhetorical trick is to paint me as a lone, lunatic voice, as if I were the _only_ person doubting that scaling will get us to AGI (whatever that is) when in fact there are loads of people with similar concerns.

Melanie Mitchell, for example, has repeatedly emphasized the importance of representing meaning, above and beyond anything that we currently know GPT-3 to do. Emily Bender, Margaret Mitchell and Timnit Gebru have derided Large language models as [stochastic parrots](https://dl.acm.org/doi/10.1145/3442188.3445922). (Not entirely fair to the parrots, but you get the idea.)

Rising star Abebe Birhane has written a [withering criticism ](https://arxiv.org/abs/2110.01963)of the ways in which LLMs rely of objectionable data scraped from the internet. Ernie Davis, I mentioned last time; almost all of our joint rejoinders draw on his deep work on common sense. Judea Pearl has shouted over and over that we need deeper understanding and written a whole [book about the importance of causality and how it is missing from current models](https://www.amazon.com/Book-Why-Science-Cause-Effect/dp/046509760X). Meredith Broussard and Kate Crawford have written recent books sharply critical of current AI. Meta researcher [Dieuwke Hupkes](https://dieuwkehupkes.nl/) has been exposing limits in the abilities of current LLM’s to generalize.

As an important aside, a lot of those other voices are women, and while I am certainly flattered by all the attention Alexander has been giving me lately, it’s not a good look to make this whole discussion sound like one more white guy-on-white guy debate when (a) so many strong female (and minority) voices have participated, and (b) so many of the unfortunate consequences of a webscraping/big data approach to AI are [disproportionately borne by women and minorities](https://arxiv.org/abs/2110.01963).

In inaccurately portraying me as a lone crusader, Alexander has not given the _scaling is not enough for AGI_ view the “steelman” treatment that he is known for delivering.

Phew. Now for the good part!

# What’s the chance that AI needs a paradigm shift? 

Bets are evidently in the air. I bet Elon Musk $100,000 that we wouldn’t have AGI by 2029 (no reply), and in similar vein tried to get Alexander to go in on a sucker bet about the capabilities of GPT-4. Alexander wisely declined, but countered with five bets of his own:

[](https://substackcdn.com/image/fetch/$s_!dV4C!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc4e6eb5-82c9-4f2c-9606-32514795c654_1577x1060.png)

On the first, we are basically in agreement. I in no way doubt that there is at least a little bit more headroom left for large language models. The real controversy is whether that’s enough.

On the second, the notion of “deep learning based model” is too vague; it might apply to a pure deep-learning model, but e.g., also to any kind of neurosymbolic hybrid in which deep learning was just one of a dozen mechanisms. It’s just not clear that anything serious is excluded. 

There is also some softness in the formulation of the third bet, where the key word is “descendant”. If, for example, The World’s First Successful AGI was a 50:50 hybrid of large language models and something symbolic like CYC, it might overall look relatively little like GPT-3, but its champions might still be tempted to declare victory. At the same time, I would (rightly) be entitled to declare moral victory for neurosymbolic AI. Both symbols _and_ LLMs could note their genes in the grandchild. Hybrid vigor for the win!

But then things get interesting. 

_Paradigm shift_ (raised in 4 and 5) is _exactly_ what this whole discussion is really about. Thank Kuhn, Alexander was brave enough to say it out loud. 

What we all really want to know, as a global research community, is _are we approaching things properly right now, or should we shift in some way?_

Personally I’d put the probability that we need to shift at 90%, well above the 60% that Alexander suggests, and I would put the probability that we will need to embrace symbol-manipulation as part of the mix at 80%, more than double Alexander’s 34%. Others may put the probability on some kind of paradigm shift (perhaps not yet known) even _higher_. Just yesterday Stanford PhD student Andrey Kurenkov put the probability at nearly 100%,[ based on arguments he gave last year about GPT-3 lacking external memory](https://lastweekin.ai/p/the-inherent-limitations-of-gpt-3):

[Andrey Kurenkov 🇺🇦@andrey_kurenkovIt's pretty obvious that 'simply scaling' a GPT-style LLM will not lead to AGI by virtue of the inherent limits of the model architecture and training paradigm.10:59 PM · Jun 10, 2022

* * *

1 Repost · 7 Likes](https://twitter.com/andrey_kurenkov/status/1535396266665857024?s=20&t=8F-fT3bCsAa0ek9awmiDBQ)

A day or two earlier, the most important empirical article of the week dropped: Big Bench [link], a massive investigation of massive language models that has a massive list of _442_ authors. Large language models; even larger papers! (How massive is the author list? I sent the paper to Scott Aaronson, who said he would read it on the plane; half an hour later he writes back: “I've been reading this paper for the past 10 minutes but haven't yet made it past the author list.”)

The basic finding was: loads of things scale, but not at all ( as foreseen both by Kurenkov in his essay last year and in my much lampooned but basically accurate essay, _[Deep learning is hitting a wall](https://nautil.us/deep-learning-is-hitting-a-wall-14467/)_). Every one of the 442 authors signed off on a paper that contains a conclusion statement that I excerpt here:

[](https://substackcdn.com/image/fetch/$s_!G_XW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd671c4ef-b131-40ad-8933-4c30b2a48b57_1114x194.jpeg)

The massive paper looks at scaling on many measures, and sees progress on some– but not others. The stuff that _isn’t_ scaling _is_ the “wall”.

The emphasis here is of course is on the words “will require new approaches, rather than scale alone.” That’s _why_ we need new approaches, exactly as I have been arguing.

Meanwhile, if you were to believe what you read on Twitter, you’d think that my biggest rival in the universe is Yann LeCun. While there’s no denying that the two of us have often clashed, on this point—the point about scale alone not likely to be enough, and about the need for some new discovery (i.e., paradigm shifts)—we are actually in complete agreement. 

For example, LeCun recently posted this sequence of tweets (excerpted from a long, excellent thread that I discuss [here](https://twitter.com/GaryMarcus/status/1526739706959958016?s=20&t=wmsQQr0_5sRLsAt6IGD2SQ)):

[Yann LeCun@ylecun(1) the research community is making *some* progress towards HLAI (2) scaling up helps. It's necessary but not sufficient, because.... (3) we are still missing some fundamental concepts 2/N9:15 PM · May 17, 2022

* * *

14 Reposts · 407 Likes](https://twitter.com/ylecun/status/1526672787187941376?s=20&t=wmsQQr0_5sRLsAt6IGD2SQ)[Yann LeCun@ylecun(4) some of those new concepts are possibly "around the corner" (e.g. generalized self-supervised learning) (5) but we don't know how many such new concepts are needed. We just see the most obvious ones. (6) hence, we can't predict how long it's going to take to reach HLAI. 3/N9:16 PM · May 17, 2022

* * *

17 Reposts · 369 Likes](https://twitter.com/ylecun/status/1526672916833787905?s=20&t=wmsQQr0_5sRLsAt6IGD2SQ)

Amen. 

§

Ok, now for the hard part: what we should _count_ as a paradigm shift? 

The best that I have seen on that is a thread from a deep learning/NLP postdoc at Edinburgh, [Antoni Valerio Miceli-Barone](https://homepages.inf.ed.ac.uk/amiceli/), who [asked the field for some tangible, falsifiable predictions](https://twitter.com/avmicelibarone/status/1526554880848150530?s=21&t=Qbt0Fe9BJBupLfECv33DYw). When he [invited me into the thread](https://twitter.com/avmicelibarone/status/1526556148513574925?s=21&t=Qbt0Fe9BJBupLfECv33DYw), I made some predictions, tied not to time but to architecture:

[Gary Marcus 🇺🇦@GaryMarcus@AVMiceliBarone @FelixHill84 predictions: whenever AGI comes: 👉large-scale symbolic knowledge will be crucial 👉explicit cognitive models will be crucial 👉operations over variables (including storing, retrieving and comparing values) will be crucial 👉an explicit type/token distinction will be crucial1:43 PM · May 17, 2022

* * *

6 Reposts · 23 Likes](https://twitter.com/garymarcus/status/1526558980637569024?s=21&t=Qbt0Fe9BJBupLfECv33DYw)

(That’s basically what Alexander’s #4 is about)

Barone however insisted on something more; I asked him to define his terms; in a short tweet he characterized what we might count as the current regime:

[Antonio Valerio Miceli Barone@AVMiceliBarone@GaryMarcus @FelixHill84 Let's say CNNs+RNNs+Transformers, no writable latent discrete memory. I'd consider "discrete attractors" models (e.g. capsules, slot attention, clustering) as innovations, since while they already exist to some extent they are not applied at scale.2:05 PM · May 17, 2022

* * *

2 Likes](https://twitter.com/avmicelibarone/status/1526564663974035457?s=21&t=Qbt0Fe9BJBupLfECv33DYw)

“Paradigm shift” then becomes _operationally defined as anything not in Miceli-Barone’s first sentence_. E.g., if the field were to turn from simply scaling (GPT-3 is pretty much just GPT-2 but bigger) to using large language models _as only one component in a larger architecture_ , with things like writable/readable discrete memory for symbolic propositions, I certainly think we should view that as a paradigm shift. 

I, as long term neurosymbolic advocate [link], would of course feel particularly vindicated if that shift was about building bridges to traditional symbolic tools (like storing, retrieving, and comparing propositions) from long-term memory, as it is with the [explicitly neurosymbolic MRKL paper from AI21](https://www.ai21.com/blog/jurassic-x-crossing-the-neuro-symbolic-chasm-with-the-mrkl-system) that I mentioned a few days ago, 

That said, I, of course, could be right about foreseeing the need for a paradigm shift, but wrong about what that paradigm shift turns out to be. 

§

LeCun’s May 17 thread lays out some of the many challenges ahead, any one of which, on its own, might in fact demand an innovation radical enough to count as a paradigm shift, neurosymbolic or otherwise:

[Yann LeCun@ylecunI believe we need to find new concepts that would allow machines to: \- learn how the world works by observing like babies. \- learn to predict how one can influence the world through taking actions. 6/N9:17 PM · May 17, 2022

* * *

47 Reposts · 598 Likes](https://twitter.com/ylecun/status/1526673366358302720?s=20&t=z9JUfw9j7Ej_D24L-m0OcA)[Yann LeCun@ylecun\- learn hierarchical representations that allow long-term predictions in abstract spaces. \- properly deal with the fact that the world is not completely predictable. \- enable agents to predict the effects of sequences of actions so as to be able to reason & plan 7/N9:18 PM · May 17, 2022

* * *

22 Reposts · 439 Likes](https://twitter.com/ylecun/status/1526673616947093505?s=20&t=U-j4LhIsBsjXkUfm0i7pZg)[Yann LeCun@ylecun\- enable machines to plan hierarchically, decomposing a complex task into subtasks. \- all of this in ways that are compatible with gradient-based learning. The solution is not just around the corner. We have a number of obstacles to clear, and we don't know how. 8/N9:19 PM · May 17, 2022

* * *

21 Reposts · 440 Likes](https://twitter.com/ylecun/status/1526673704935112706?s=20&t=z9JUfw9j7Ej_D24L-m0OcA)

To all this I would add the capacity to build, interrogate, and reason about long-term cognitive models of an ever-changing world [link next decade], stored in some kind of long-term memory that allows for trustworthy storage and retrieval.

So: can we get to AGI and reliable, no-goof reasoning, handling all the challenges that LeCun and I have been discussing, with scaling and CNNs + RNNs + Transformers alone? 

In my view, no way; I think the actual odds are less than 20%. 

So Scott, challenge accepted, I am on for your bets #4 and #5. 

§

The other Scott, Aaronson said, yesterday, “From where I stand, though, the single most important thing you could do in your reply is to give examples of tasks or benchmarks where, not only does GPT-3 do poorly, but you predict that GPT-10 will do poorly, if no new ideas are added”

As it happens that Miceli-Barone has posted precisely the same question [link] in May; here’s what I said then, and stand by:

[Gary Marcus 🇺🇦@GaryMarcus@AVMiceliBarone @FelixHill84 I think pure deep learning so defined will fail at Comprehension Challenge, proposed here: [newyorker.com/tech/annals-of…](https://www.newyorker.com/tech/annals-of-technology/what-comes-after-the-turing-test) and developed a bit further here: [ojs.aaai.org//index.php/aim…](https://ojs.aaai.org//index.php/aimagazine/article/download/2649/2530). Working w some folks to try to implement for real.ojs.aaai.org2:10 PM · May 17, 2022

* * *

2 Likes](https://twitter.com/garymarcus/status/1526565886831644673?s=21&t=Qbt0Fe9BJBupLfECv33DYw)

If GPT-10 is just like GPT-3, no extra bells and whistles, just bigger, and able to read whole novels and watch whole movies and answer subtle and open-ended questions about characters and their conflicts and motivation, and tell us when to laugh, I promise to post a YouTube video admitting I was wrong. 

§

I give LeCun the last word, once again from his May 17th manifesto:

[Yann LeCun@ylecunI really don't think it's just a matter of scaling things up. We still don't have a learning paradigm that allows machines to learn how the world works, like human anspd many non-human babies do. 4/N9:16 PM · May 17, 2022

* * *

50 Reposts · 499 Likes](https://twitter.com/ylecun/status/1526673084488491008?s=20&t=_CtX5ommAZFijkDkWUHaGQ)

\- Gary Marcus

[1](https://garymarcus.substack.com/p/does-ai-really-need-a-paradigm-shift#footnote-anchor-1-58860020)

Something similar happens when Alexander sets up what AGI is. There are two extreme views of AGI that one might imagine: one (easily defeated) in which the whole point is to mimic humans _exactly_ , and the other (the steelman) in which AGI tries in some respects in which humans are particularly flawed to do _better_ than humans. For example, humans are lousy at arithmetic. But you shouldn’t be able to declare “I have made an AGI” by showing you can build a machine that makes arithmetic errors. Alexander’s long digression on Luria’s famous cross cultural reasoning work on untutored subjects applies only to the strawman, not the steelman. 

Of course, as Miceli-Barone pointed out to me, one could ask whether a particular kind of error might reveal something about whether a given model was a good model of human cognition; that’s actually what [my dissertation work with Steven Pinker](https://pubmed.ncbi.nlm.nih.gov/1518508/) was about. That’s a story for another day :)
