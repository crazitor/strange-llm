---
title: "Dear Elon Musk, here are five things you might want to consider about AGI"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/dear-elon-musk-here-are-five-things"
---

[Elon Musk@elonmusk@jack 2029 feels like a pivotal year. I’d be surprised if we don’t have AGI by then. Hopefully, people on Mars too.5:35 PM · May 30, 2022

* * *

2.12K Reposts · 32.2K Likes](https://twitter.com/elonmusk/status/1531328534169493506?s=21&t=Xa0Whxgi37HOGM8Ro4XHrw)

Dear Elon,

Yesterday you told the world that you expected to see AGI (otherwise known as artificial general intelligence, in contrast to narrow AI like playing chess or folding proteins) [by 2029](https://twitter.com/elonmusk/status/1531328534169493506?s=21&t=Xa0Whxgi37HOGM8Ro4XHrw). 

I offered to place a bet on it; no word back yet. AI expert Melanie Mitchell from the Santa Fe Institute suggested we place our bets on [longbets.org](https://longbets.org/). No word on that yet, either. But Elon, I am down if you are. 

But before I take your money, let’s talk. Here are five things you might want to consider.

First, I’ve been watching you for a while, and your track record on betting on precise timelines for things is, well, spotty. You said, for instance in 2015, that (truly) [self-driving cars were two years away](https://fortune.com/2015/12/21/elon-musk-interview/); you’ve pretty much said the same thing every year since. It still hasn’t happened.

Second, you ought to pay more attention to the challenges of edge cases (aka outliers, or unusual circumstances) and what they might mean for your prediction. The thing is, it’s easy to convince yourself that AI problems are much easier than they are actually are, because of _the long tail problem_. For everyday stuff, we get tons and tons of data that current techniques readily handle, leading to a misleading impression; for rare events, we get very little data, and current techniques struggle there. For human beings, who have a whole raft of techniques for reasoning with incomplete information, the long tail is not necessarily an insuperable problem. But for the kinds of AI techniques that are currently popular, and which rely more on big data than on reasoning, it’s a very serious issue. 

I tried to sound a warning about this in 2016, in an Edge.org interview called [“Is Big Data Taking Us Closer to the Deeper Questions in Artificial Intelligence?”](https://www.edge.org/conversation/gary_marcus-big-data-ai:)**** Here’s what I said then:

> Even though there's a lot of hype about AI and a lot of money being invested in AI, I feel like the field is headed in the wrong direction. There's been a local maximum where there's a lot of low-hanging fruit right now in a particular direction, which is mainly deep learning and big data. People are very excited about the big data and what it's giving them right now, but I'm not sure it's taking us closer to the deeper questions in artificial intelligence, like how we understand language or how we reason about the world. …

> You could also think about driverless cars. What you find is that in the common situations, they're great. If you put them in clear weather in Palo Alto, they're terrific. If you put them where there's snow or there's rain or there's something they haven't seen before, it's difficult for them. There was a great piece by Steven Levy about the Google automatic car factory, where he talked about how the great triumph of late 2015 was that they finally got these systems to recognize leaves. 
> 
> It's great that they do recognize leaves, but there are a lot of scenarios like that, where if there's something that's not that common, there's not that much data. You and I can reason with common sense. We can try to figure out what this thing might be, how it might have gotten there, but the systems are just memorizing things. So that's a real limit. 

So far as I know your cars are still mostly just doing a kind of glorified hash-table-like lookup (viz deep learning), and hence still having a lot of problems with unexpected situations. You probably saw a few weeks ago, for example, when a “summoned” Tesla Model Y crashed into a $3 million jet that was parked in a mostly empty airport. 

Unexpected circumstances have been and continue to be the bane of contemporary AI techniques, and probably will be until there is a real revolution. And it’s why I absolutely guarantee you won’t be shipping level 5 self-driving cars this year or next, [no matter what you might have told Chris Anderson at TED](https://www.ted.com/talks/elon_musk_elon_musk_talks_twitter_tesla_and_how_his_brain_works_live_at_ted2022).

I certainly don’t think outliers are a literally unsolvable problem. But you and I both know that they continue to be a major problem that as yet has no known robust solution. And I do think we are going to have to move past a heavy dependence on current techniques like deep learning. Seven years is a long time, but the field is going to need to invest in other ideas if we are going to get to AGI before the end of the decade. Or else outliers alone might be enough to keep us from getting there.

The third thing to realize is that AGI is a problem of _enormous_ scope, because intelligence itself is of a broad scope. I always love this quote from Chaz Firestone and Brian Scholl:

> There is no one way the mind works, because the mind is not one thing. Instead, the mind has parts, and the different parts of the mind operate in different ways: Seeing a color works differently than planning a vacation, which works differently than understanding a sentence, moving a limb, remembering a fact, or feeling an emotion.”

Deep learning is pretty decent at, for example, recognizing objects, but not nearly as good at planning, or reading, or [language comprehension](https://garymarcus.substack.com/p/horse-rides-astronaut). Sometimes I like to show this figure:

[](https://substackcdn.com/image/fetch/$s_!Wh9T!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc88b603-4335-4f4c-9251-5dc93349dbbb_1916x1916.png)

Current AI is great at some aspects of perception, but let’s be realistic, still struggling with the rest. Even within perception 3D perception remains a challenge, and scene understanding is by no means solved. We still don’t have anything like stable or trustworthy solutions for common sense, reasoning, language, or analogy. Truth is, I have been using this same pie chart for about 5 years, and the situation has scarcely changed.

In my 2018 article [Deep Learning: A Critical Appraisal](https://arxiv.org/abs/1801.00631) I summed the situation up this way:

> “Despite all of the problems I have sketched, I don’t think that we need to abandon deep learning.
> 
> Rather, we need to reconceptualize it: not as a universal solvent, but simply as one tool among many, a power screwdriver in a world in which we also need hammers, wrenches, and pliers, not to mention chisels and drills, voltmeters, logic probes, and oscilloscopes.

Four years later, many people continue to hope that deep learning will be a panacea; [that still seems pretty unrealistic to me](https://garymarcus.substack.com/p/the-new-science-of-alt-intelligence?s=w); I still think we need a whole lot more techniques. Being realistic, 7 years might well not be enough to (a) invent those tools (if they are don’t already exist) and (b) take them from the lab into production. And you surely remember what [“production hell](https://www.wsj.com/articles/elon-musk-races-to-exit-teslas-production-hell-1530149814)” is all about. To do that for a whole ensemble of techniques that have never been fully integrated before in less than a decade might be asking a lot. 

I don’t know what you have planned for [Optimus](https://www.cnbc.com/2022/04/21/elon-musk-says-optimus-robot-will-be-worth-more-than-tesla.html), but I can promise you that the AGI that you would need for a general-purpose domestic robot (where every home is different, and each poses its own safety risks) is way beyond what you would need for a car that drives on roads that are more or less engineered the same way from one town to the next. (If you are curious, here are some thoughts on [what a real foundation for AGI might look like.](https://thegradient.pub/has-ai-found-a-new-foundation/))

The fourth thing to realize is that we, and by this I mean humanity as a whole, still don’t really have an _adequate methodology for building complex cognitive systems_. 

Complex cognitive systems have too many moving parts, which often means that people building things like driverless cars wind up playing a giant game of [whack-a-mole](https://en.wikipedia.org/wiki/Whac-A-Mole), often solving one problem and creating another. Adding patch upon patch works sometimes, but sometimes it doesn’t. I don’t think we can get to AGI without solving that methodological problem, and I don’t think anybody yet has a good proposal. 

Debugging with deep learning is wicked hard, because nobody (a) really understands how it works, and (b) knows how to fix problems other to collect more data and add more layers and so forth. The kind of debugging you (and everyone else) know in the context of classical programming just doesn’t really apply; because deep learning systems are so uninterpretable, so one can’t think through what the program is doing in the same way, nor count on the usual processes of elimination. Instead, right now in the deep learning paradigm, there’s a ton of trial-and-error, and retraining and retesting, not to mention loads of data cleaning and experiments with data augmentation and so forth. And as Facebook’s recent and [very candid report of the travails in training the large language model OPT](https://github.com/facebookresearch/metaseq/blob/main/projects/OPT/chronicles/README.md) showed, a whole lot of mess in the process. You should check out their [logbook](https://github.com/facebookresearch/metaseq/blob/main/projects/OPT/chronicles/README.md) on github.

Sometimes it all feels more like alchemy than science. As usual, [xkcd said it best:](https://xkcd.com/1838/)

[](https://substackcdn.com/image/fetch/$s_!gaLJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F15750da5-149c-4fa0-b5fd-449f23c995d7_371x439.png)

Things like programming verification might eventually help, but again, in deep learning we don’t yet have the tools for writing verifiable code. If you are to win the bet, we are probably going to have to solve that problem too, and soon.

The final thing is a matter of criteria. If we are going to bet, we should make some ground rules. The term AGI is pretty vague, and that’s not good for either of us. [As I offered on Twitter the other day](https://twitter.com/garymarcus/status/1529457162811936768?s=21&t=GiZ3kusGugtuBNk7Imr89Q): I take AGI to be “a shorthand for any intelligence ... that is flexible and general, with resourcefulness and reliability comparable to (or beyond) human intelligence”.[1](https://garymarcus.substack.com/p/dear-elon-musk-here-are-five-things#footnote-1-57299018)

If you are in for the bet, we ought to operationalize it, in some practical terms. Adapting something Ernie Davis and I just wrote at the request of someone working with [Metaculus](https://www.metaculus.com/questions/?show-welcome=true), here are five predictions, arranged from easiest for most humans to those that would require a high degree of expertise:

  * In 2029, AI will not be able to watch a movie and tell you accurately what is going on (what I called [the comprehension challenge](https://www.newyorker.com/tech/annals-of-technology/what-comes-after-the-turing-test) in _The New Yorker_ , in 2014). Who are the characters? What are their conflicts and motivations? etc. 

  * In 2029, AI will not be able to read a novel and reliably answer questions about plot, character, conflicts, motivations, etc. Key will be going beyond the literal text, as Davis and I explain in _[Rebooting AI](http://rebooting.ai)_.

  * In 2029, AI will not be able to work as a competent cook in an arbitrary kitchen (extending [Steve Wozniak’s cup of coffee benchmark](https://www.fastcompany.com/1568187/wozniak-could-computer-make-cup-coffee)). 

  * In 2029, AI will not be able to reliably construct bug-free code of more than 10,000 lines from natural language specification or by interactions with a non-expert user. [Gluing together code from existing libraries doesn’t count.]

  * In 2029, AI will not be able to take arbitrary proofs from the mathematical literature written in natural language and convert them into a symbolic form suitable for symbolic verification.




Here’s what I propose, if you (or anyone else) manages to beat at least three of them in 2029 [_later clarification, italics added June 2024_ : _with a single system; three separate systems would obviously not count as general]_ , you win; if only one or two are broken, we can’t very well say we have nailed the _general_ part in artificial general intelligence, can we? In that case, or if none are broken, I win.

Deal? How about $100,000? 

If you are in, reach out so we can agree to the ground rules.

Yours sincerely,

Gary Marcus

Author, _[Rebooting AI](http://rebooting.ai)_ and _The Algebraic Mind  
_ Founder and CEO, Geometric Intelligence (acquired by Uber)  
Professor Emeritus of Psychology and Neural Science, NYU

 _Update, 7 June 2022: A week later, we still haven’t heard from Elon Musk, but there was extensive news coverage, and the bet is up to $500,000 with Vivek Wadhwa first among several to match my initial bet. Kevin Kelly has offered to host on[LongNow.org](http://longnow.org). _

[1](https://garymarcus.substack.com/p/dear-elon-musk-here-are-five-things#footnote-anchor-1-57299018)

Shane Legg, a co-founder of DeepMind, who coined the term in its current usage, in the context of a book that Ben Goertzel was putting together, said he was happy with my definition.
