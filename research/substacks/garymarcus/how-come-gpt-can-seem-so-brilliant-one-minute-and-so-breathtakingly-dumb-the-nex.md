---
title: "How come GPT can seem so brilliant one minute and so breathtakingly dumb the next?"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/how-come-gpt-can-seem-so-brilliant"
---

[](https://substackcdn.com/image/fetch/$s_!-s4d!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F418cac3d-a10a-4c7a-b48c-d7a05e731e21_1017x311.jpeg)GPT continues to struggle

In light of the dozens of GPT fails that have circulating in the last 24 hours, regular reader Mike Ma just asked a profound question: how can GPT seem so brilliant and so stupid at the same time?

[Mike Ma@MMikeMMa@plibin @GaryMarcus So, I’m really struggling here. These machines don’t *understand* anything. As I understand, they are MASSIVE correlation engines. Yet, they simultaneously: \- hilariously fail \- breathtakingly win WHY/HOW are both things true? What Qs do the engine win/fail on and why? 3:03 PM · Dec 1, 2022

* * *

2 Likes](https://twitter.com/MMikeMMa/status/1598331956479295489?s=20&t=_4DUnTbmpbANAIJNnXbEJQ)

[Fails are easy to come by](https://twitter.com/GaryMarcus/status/1598208285756510210?s=20&t=_4DUnTbmpbANAIJNnXbEJQ); one current favorite, from reader Rtombs a few minutes ago, is this one, which combines both the brilliance and the stupidity:

[Rupert Tombs@rtombs@GaryMarcus This prompt format is pretty reliable. 3:15 PM · Dec 1, 2022](https://twitter.com/rtombs/status/1598335100428640258)

Why does this happen? The obvious answer is to just blame monkeys and typewriters:

[Erhan Hosca@ehosca@GaryMarcus Isn’t this basic probability? Enough monkeys banging on typewriters sort of thing…3:18 PM · Dec 1, 2022](https://twitter.com/ehosca/status/1598335748180156418?s=20&t=_4DUnTbmpbANAIJNnXbEJQ)

Professor Emily Bender suggests something similar:

[@emilymbender@dair-community.social on Mastodon@emilymbenderThat "Limitations" section has it wrong though. ChatGPT generates strings based on combinations of words from its training data. When it sometimes appears to say things that are correct and sensible when a human makes sense of them, that's only by chance. >>3:47 AM · Dec 1, 2022

* * *

3 Reposts · 25 Likes](https://twitter.com/emilymbender/status/1598161759562792960?s=20&t=_4DUnTbmpbANAIJNnXbEJQ)

I beg to differ. Chance is _definitely_ part of what’s going on. But it’s not quite the right way to understand the juxtaposition of brilliance and stupidity that we see within GPT. 

Monkeys and typewriters would be no more likely to create Rtomb’s fluent churro-surgery invention than they would be to write Hamlet. Either could happen, but if you relied on chance alone, you would likely be waiting billions of year, even with a lot of monkeys and a lot of human readers sorting wheat from chaff. The impressive thing about GPT is that it spits out hundreds of perfectly fluent, often plausible prose at a regular clip, with no human filtering required.

GPT is not (ever) giving us random characters (_JK@#L JKLJFH SDI VHKS_) like monkeys and typewriters might. And it’s pretty rarely if ever putting out word salad (_book solider girl the gave hungry blue 37_). Blaming it all on chance just doesn’t capture what’s going. Almost everything it says is fluent and at least vaguely plausible.

What’s really happening is more subtle than Bender lets on. 

The real answer comes in two parts.

§

Part I:

GPT-3 has no idea how the world works (and on this Bender and I would agree); when it says that the “compact size [of Churros] allows for greater precision and control during surgery, risking the risk of complications and improving the overall outcomes patients” it’s not because it has done a web search for Churros and surgery (good luck with that!). And it’s not because it has _reasoned_ from first principles about the intersection between Churro’s and surgical procedures (clearly it’s pretty shaky on the concept).

It’s because GPT-3 is the king of pastiche.

_Pastiche_ , in case you don’t know the word, is, as wiki defines it, “a work of [visual art](https://en.wikipedia.org/wiki/Visual_art), literature, theatre, music, or architecture that [imitates](https://en.wikipedia.org/wiki/Imitation) the style or character of the work of one or more other artists”. GPT-3 is a mimic.

But it is mimic that knows not whereof it speaks. Merely knowing that it is a mimic, though true, still doesn’t quite get us to the explanation that we need. 

I think about the rest of the answer in two parts:

Part I is about how GPT works

  1. **Knowledge is in part about specific properties of particular entities**. GPT’s mimicry draws on vast troves of human text that, for example, often put together subjects [_England_] with predicates [_won 5 Eurovision contests_]. 

  2. Over the course of training, GPT sometimes **loses track of the precise relations (“bindings”, to use a technical term) between those entities and their properties**. 

  3. GPT”s heavy use of a technique called embeddings makes it really good at substituting synonyms and more broadly related phrases, but **the same tendency towards substitution often lead it astray.**

  4. **It never fully masters abstract relationship.** It doesn’t know for example, in a fully general way that for all countries A and all B, if country A won more games than country B, country is a better candidate for “country that won the most games” (The fact that standard neural networks have trouble with this was the central claim of my 2001 book The Algebraic Mind; recent careful studies with arithmetic shows that such universal knowledge remains a stick pointing for current neural networks




Part II is about how _humans_ work.

The immense database of things that GPT draws on consists entirely of language uttered by _humans,_ in the real world with utterances that (generally) **grounded in the real world.** That means, for examples, that the entities (churros, surgical tools) and properties (“allow[s] for greater precision and control during surgery, risking the risk of complications and improving the overall outcomes patients”) generally refer to real entities and properties in the world. GPT doesn’t talk randomly, because it’s pastiching things actual people said. (Or, more often, synonyms and paraphrases of those things.)

When GPT gets things right, it is often combining bits that don’t belong together, but not quite in random ways, but rather **in ways where there is** _**some overlap in some aspect or another**_.

Example: Churros are in a cluster of small things that the system (roughly speaking) groups together, presumably including eg baseballs, grasshoppers, forceps, and so forth. GPT doesn’t actually _know_ which of the elements appropriately combine with which other properties. _Some_ small things really do “allow[s] for greater precision and control during surgery, risking the risk of complications and improving the overall outcomes patients” But GPT idea has no idea which. 

In some sense, GPT is like a glorified version of cut and paste, where everything that is cut goes through a paraphrasing/synonymy process before it is paste but together—and a lot of important stuff is sometimes lost along the way. 

When GPT sounds plausible, it is because every paraphrased bit that it pastes together is **grounded** in something that actual humans said, and there is often some vague (but often irrelevant) relationship between.. 

At least for now, it still takes a human to know which plausible bits actually belong together.

[Share](https://garymarcus.substack.com/p/how-come-gpt-can-seem-so-brilliant?utm_source=substack&utm_medium=email&utm_content=share&action=share)

P.S. If you haven’t already read my essay [Deep Learning is Hitting a Wall ](https://nautil.us/deep-learning-is-hitting-a-wall-238440/) please take a look. It was just named a Best Tech Article of 2022, and I believe that is still incredibly relevant, even with all the advances of the last 8 months.
