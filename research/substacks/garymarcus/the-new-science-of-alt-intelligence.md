---
title: "The New Science of Alt Intelligence"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/the-new-science-of-alt-intelligence"
---

For many decades, part of the premise behind AI was that _artificial_ intelligence should take inspiration from _natural_ _intelligence_. John McCarthy, one of the co-founders of AI, wrote groundbreaking papers on [why AI needed common sense](https://en.wikipedia.org/wiki/Advice_taker); Marvin Minsky, another of the field’s co-founders of AI wrote a book [scouring the human mind for inspiration](https://en.wikipedia.org/wiki/Society_of_Mind), and clues for how to build a better AI. [Herb Simon](https://en.wikipedia.org/wiki/Herbert_A._Simon) won a Nobel Prize for behavioral economics. One of his key books was called Models of Thought, which aimed to explain how “Newly developed computer languages express theories of mental processes, so that computers can then simulate the predicted human behavior.”

A large fraction of current AI researchers, or at least those currently in power, don’t (so far as I can tell) give a damn about any of this. Instead, the current focus is on what I will call (with thanks to Naveen Rao for the term) _Alt Intelligence_. 

_**Alt Intelligence**_**isn’t about building machines that solve problems in ways that have to do with human intelligence. It’s about using massive amounts of data – often derived from human behavior – as a** _**substitute**_**for intelligence.** Right now, the predominant strand of work within Alt Intelligence is the idea of _scaling_. The notion that the bigger the system, the closer we come to true intelligence, maybe even consciousness. 

There is nothing new, per se, about studying Alt Intelligence, but the hubris associated with it is. 

I’ve seen signs for a while, in the dismissiveness with which the current AI superstars, and indeed vast segments of the whole field of AI, treat human cognition, ignoring and even ridiculing scholars in such fields as linguistics, cognitive psychology, anthropology, and philosophy. 

But this morning I woke to a new reification, a Twitter thread that expresses, out loud, the Alt Intelligence creed, from Nando de Freitas, a brilliant high-level executive at DeepMind, Alphabet’s rightly-venerated AI wing, in a declaration that AI is “all about scale now.” Indeed, in his mind (perhaps deliberately expressed with vigor to be provocative), the harder challenges in AI are already solved. “The Game is Over!”, he declares:

[Nando de Freitas 🏳️‍🌈@NandoDFSomeone’s opinion article. My opinion: It’s all about scale now! The Game is Over! It’s about making these models bigger, safer, compute efficient, faster at sampling, smarter memory, more modalities, INNOVATIVE DATA, on/offline, … 1/N thenextweb.comDeepMind’s new Gato AI makes me fear humans will never achieve AGI8:46 AM · May 14, 2022

* * *

19 Reposts · 120 Likes](https://twitter.com/NandoDF/status/1525397036325019649?s=20&t=hm-285U9t6XMpO4X8QU47g)

There’s nothing wrong, per se, with pursuing Alt Intelligence. 

Alt Intelligence represents an intuition (or more properly, a family of intuitions) about how to build intelligent systems, and since nobody yet knows how to build any kind of system that matches the flexibility and resourcefulness of human intelligence, it’s certainly fair game for people to pursue multiple different hypotheses about how to get there. Nando de Freitas is about as in-your-face as possible about defending that hypothesis, which I will refer to as Scaling-Uber-Alles. 

Of course, that name, Scaling-Uber-Alles, is not entirely fair. De Freitas knows full well (as I will discuss below) that you can’t just make the models bigger and hope for success. People have been doing a lot of scaling lately, and achieved some great successes, but also run into some road blocks. Let’s take a dose reality, before going further, into how de Freitas faces facts.

## A Dose of Reality

Systems like DALL-E 2, GPT-3, Flamingo, and Gato appear to be mind-blowing, but nobody who has looked at them carefully would confuse them for human intelligence. 

[DALL-E 2](https://openai.com/dall-e-2/), for example, can _often_ create fantastic artwork, from verbal descriptions “an astronaut riding a horse in a photorealistic style”:

[](https://substackcdn.com/image/fetch/$s_!LCTE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1e231f4-3871-4a00-8020-a162d730a34c_1024x1024.jpeg)

But it’s also pretty prone to surprising stumbles, like this uncomprehending reply to “a red cube on top of a blue cube”. [DALL-E’s responses, created by a network called unCLIP, are on the _left_ of the figure; interestingly a predecessor model, shown on the _right_ , actually does better on this particular item.]

[](https://substackcdn.com/image/fetch/$s_!eY2I!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb9bf9bb-ae1a-4a5d-84da-87fe13d3c7b6_1089x625.jpeg)

When Ernest Davis, Scott Aaronson, and I probed [in a bit more detail, we found a number of similar examples](https://arxiv.org/abs/2204.13807):

[](https://substackcdn.com/image/fetch/$s_!Jjb3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F13318be6-0930-48bd-b85e-6c61601fe6c8_1861x1033.jpeg)

Similarly, the ostensibly amazing [Flamingo](https://www.deepmind.com/blog/tackling-multiple-tasks-with-a-single-visual-language-model) has (not unrelated) bugs of its own, captured in[ a candid and important thread by DeepMind’s Murray Shanahan](https://twitter.com/mpshanahan/status/1524037590785142792?s=20&t=wtGCfIlUM4qwpJnsRYZ6ug), with further examples from Flamingo’s lead author Jean-Baptiste Alayrac. For example, Shanahan confronted Flamingo with this image:

[](https://substackcdn.com/image/fetch/$s_!WMZY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F25414afb-a154-4f8e-b464-360fa245e502_124x288.jpeg)

and wound up having this discomprehending dialogue:

[Murray Shanahan@mpshanahanAnd this was the conversation we had about it: Flamingo: This is a traffic light. It is red. User: Can you see three circles? Flamingo: Yes, I can see three circles. User: What colours are they? Flamingo: They are red, blue and green. 5/92:44 PM · May 10, 2022

* * *

6 Likes](https://twitter.com/mpshanahan/status/1524037599769288711?s=20&t=kbnKP_1jP_g7fVnplvdz1g)[Murray Shanahan@mpshanahanUser: Where is the green circle? Flamingo: The green circle is on the right. User: Really? On the right of what? Flamingo: The green circle is on the right of the blue circle. 6/92:44 PM · May 10, 2022

* * *

4 Likes](https://twitter.com/mpshanahan/status/1524037601082101761?s=20&t=kbnKP_1jP_g7fVnplvdz1g)

Um no. 

DeepMind’s newest star, just unveiled, [Gato](https://www.deepmind.com/publications/a-generalist-agent), is capable of cross-modal feats never seen before in AI, but still, when you look in the fine print, remains stuck in the same land of unreliability, moments of brilliance coupled with absolute discomprehension: 

[](https://substackcdn.com/image/fetch/$s_!8bi4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F725df37c-a05d-4acd-ae56-90eecdf3697f_579x299.jpeg)

Of course, it’s not uncommon for defenders of deep learning to make the reasonable point that humans make errors, too.

But anyone who is candid will recognize that these kinds of errors reveal that something is, for now, deeply amiss. If either of my children routinely made errors like these, I would, no exaggeration, drop everything else I am doing, and bring them to the neurologist, _immediately_.

So let’s be honest: scaling hasn’t worked _yet_. But it might, or so de Freitas’s theory—a clear expression of the Zeitgeist—goes. 

## Scaling-Uber-Alles

So how does de Freitas reconcile reality with ambition? Literally billions of dollars have been poured into Transformers, the underlying technology that drives GPT-3, Gato, and so many others; training data sets have expanded from megabytes to gigabytes, parameter counts from millions to trillions. And yet the discomprehending errors, well-documented in numerous works since 1988, remain.

To some (such as myself), the abiding problem of discomprehension might—despite the immense progress—signal the need for a fundamental rethink, such as the one that Davis and I offered in our book [Rebooting AI](http://Rebooting.AI). 

But not to de Freitas (nor to many others in the field—I don’t mean to single him out; I just think he has given prominent and explicit voice to what many are thinking).

In the opening thread he elaborates much of his view about reconciling reality with current troubles, “It’s about making these models bigger, safer, compute efficient, faster at sampling, smarter memory, more modalities, INNOVATIVE DATA, on/offline”. Critically, not a word (except, perhaps “smarter memory”) is given to any idea from cognitive psychology, linguistics, or philosophy.

The rest of de Freitas’ thread, follows suit:

[Nando de Freitas 🏳️‍🌈@NandoDFSolving these scaling challenges is what will deliver AGI. Research focused on these problems, eg S4 for greater memory, is needed. Philosophy about symbols isn’t. Symbols are tools in the world and big nets have no issue creating them and manipulating them 2/n8:50 AM · May 14, 2022

* * *

3 Reposts · 47 Likes](https://twitter.com/NandoDF/status/1525398087203983360?s=20&t=gJGyegwyrB9PRrTBMOqfvA)

This is, again, a pure statement of scaling-über-alles, and marks its target: the ambition here is not just better AI, but _AGI_.

AGI, artificial _general_ intelligence, is the community’s shorthand for AI that is at least as good, and resourceful, and wide-ranging, as human intelligence. The signature success of _narrow_ artificial intelligence, and indeed alt intelligence, writ large, has been games like Chess (DeepBlue owed nothing to human intelligence) and Go (AlphaGo similarly owed little to human intelligence). De Freitas has far more ambitious goals in mind, and, to his credit, he’s upfront about them.

The means to his end? Again, de Freitas’s emphasis is mainly technical tools for accommodating bigger data sets. The idea that other ideas, e.g., from philosphy or cognitive science, might be important is dismissed. (“Philosophy about symbols isn’t [needed]” is perhaps a rebuttal to my [long-standing campaign to integrate symbol-manipulation into cognitive science and AI](https://mitpress.mit.edu/books/algebraic-mind), recently resumed in [Nautilus Magazine](https://nautil.us/deep-learning-is-hitting-a-wall-14467/), though the argument is not fully spelled out. Responding briefly: His statement that “[neural] nets have no issue creating [symbols] and manipulating them” misses both history and reality. The history missed is the the fact that many neural net enthusiasts, have argued against symbols for decades, and the reality that is missed is the above-documented fact that symbolic descriptions like “red cube on blue cube” still elude the state-of-the-art in 2022.)

De Freitas’s Twitter manifesto closes with an approving reference to Rich Sutton’s famous white paper, The Bitter Lesson:

[Nando de Freitas 🏳️‍🌈@NandoDFRich Sutton is right too, but the AI lesson ain’t bitter but rather sweet. I learned it from @geoffreyhinton a decade ago. Geoff predicted what was predictable with uncanny clarity.9:24 AM · May 14, 2022

* * *

1 Repost · 32 Likes](https://twitter.com/NandoDF/status/1525406792670380032?s=20&t=U1ZfhtMDxMpbFGvX4MsHXQ)

Sutton’s argument is that the only thing that has led to advances in AI is more data, computed over more effectively. Sutton is, in my view, only half right, almost correct with his account of the past, but dubious with his inductive prediction about the future. 

So far, in most domains (not all, to be sure) Big Data has triumphed (for now) over careful knowledge engineering. But,

  * Virtually all of the world’s software, from web browsers to spreadsheets to word processors, still depends on knowledge engineering, and Sutton sells that short. To take one example, Sumit Gulwani’s brilliant Flash Fill feature is a one-trial learning system that is staggeringly useful, and not at all founded on the premise of large data, but rather on classical programming techniques. I don’t think any pure deep learning/big data system can match it. 

  * Virtually none of the critical problems for AI that cognitive scientists such as Steve Pinker, Judea Pearl, the late Jerry Fodor, and myself have been pointing to for decades is actually solved yet. Yes, machines can play games really well, and deep learning has made massive contributions to domains like speech recognition. But **no current AI is remotely close to being able to read an arbitrary text with enough comprehension to be able to build a model of what a speaker is saying and intends to accomplish** , nor able (a la Star Trek Computer) to be able to reason about an arbitrary problem and produce a cohesive responsive. We are in _early days_ in AI. 




Success on a few problems with a particular strategy in no way guarantees that we can solve _all_ problems in a similar way. It is sheer inductive folly to imagine otherwise, particular when the failure modes (unreliability, bizarre errors, failures in compositionality and discomprehension) have not changed since Fodor and Pinker pointed them out (in separate articles) in 1988. 

## In closing

Let me close by saying that I am heartened to see that, thankfully, Scaling-Über-Alles isn’t fully consensus yet, even at DeepMind: 

[Murray Shanahan@mpshanahanMy opinion: Maybe scaling is enough. Maybe. And we definitely need to do all the things @NandoDF lists. But I see very little in Gato to suggest scaling alone will get us to human-level generalisation. It falls so far short. Thankfully we're working in multiple directions Nando de Freitas 🏳️‍🌈 @NandoDFSomeone’s opinion article. My opinion: It’s all about scale now! The Game is Over! It’s about making these models bigger, safer, compute efficient, faster at sampling, smarter memory, more modalities, INNOVATIVE DATA, on/offline, … 1/N https://t.co/UJxSLZGc711:08 PM · May 14, 2022

* * *

2 Reposts · 18 Likes](https://twitter.com/mpshanahan/status/1525462964140113923?s=20&t=mlKKL0K2LS9bVR3h9v3b6Q)

I am fully with Murray Shanahan when he writes “I see very little in Gato to suggest that scaling alone will get us to human-level generalisation.”

**Let us all encourage a field that is open-minded enough to work in multiple directions, without prematurely dismissing ideas that happen to be not yet fully developed**. It may just be that the best path to artificial (general) intelligence isn’t through Alt Intelligence, after all. 

As I have written, I am fine with thinking of Gato as an “Alt Intelligence”— an interesting exploration in alternative ways to build intelligence—but we need to take it in context: it doesn’t work like the brain, it doesn’t learn like a child, it doesn’t understand language, it doesn’t align with human values, and it can’t be trusted with mission-critical tasks. 

It may well be better than anything else we currently have, but the fact that it still doesn’t really work, even after all the immense investments that have been made in it, should give us pause.

And really, it should lead us back to where the founders of AI started. AI should certainly not be a slavish replica of human intelligence (which after all is flawed in its own ways, [saddled with lousy memory and cognitive bias](https://www.amazon.com/Kluge-Haphazard-Evolution-Human-Mind/dp/054723824X)). But it should look to human (and animal cognition) for clues. No, the Wright Brothers [didn’t mimic birds, but they learned something from avian flight control](https://wright.nasa.gov/researched.htm). Knowing what to borrow and what not is likely to be more than half the battle.

The bottom line is this, something that AI once cherished but has now forgotten: If we are to build AGI, we are going to need to learn something from humans, how they reason and understand the physical world, and how they represent and acquire language and complex concepts. 

It is sheer hubris to believe otherwise.

P.S. Please subscribe if you’d like to read more no-bullshit analysis of the current state of AI.
