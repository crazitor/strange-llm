---
title: "The SuperScott and Morgan Freeman FAQ"
author: "Scott Aaronson"
date: "Mon, 05 Aug 2013"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=1487"
---

[](https://scottaaronson.blog/wp-content/uploads/2013/08/chessboard.jpg)

**Update (Sept. 3):** When I said that "about 5000 steps" are needed for the evolutionary approach to color an 8×8 chessboard, I was counting as a step any _examination_ of two random adjacent squares--regardless of whether or not you end up having to change one of the colors. If you count only the changes, then the expected number goes down to about 1000 (which, of course, only makes the point about the power of the evolutionary approach "stronger"). Thanks very much to Raymond Cuenen for bringing this clarification to my attention.

* * *

Last week I appeared on an episode of [Through the Wormhole with Morgan Freeman](http://science.discovery.com/tv-shows/through-the-wormhole), a show on the Science Channel. (See also [here](https://www.facebook.com/photo.php?fbid=494099444006045&set=a.230075090408483.56554.120791238003536&type=1&relevant_count=1) for a post on Morgan Freeman's Facebook page.) The episode is called _" Did God Create Evolution?"_ The first person interviewed is the Intelligent Design advocate Michael Behe. But not to worry! After him, they have a parade of scientists who not only agree that Chuck Darwin basically had it right in 1859, but want to argue for that conclusion using ROBOTS! and MATH!

So, uh, that's where I come in. My segment features me (or rather my animated doppelgänger, "SuperScott") trying to color a chessboard two colors, so that no two neighboring squares are colored the same, using three different approaches: (1) an "intelligent design" approach (which computer scientists would call nondeterminism), (2) a brute-force, exhaustive enumeration approach, and (3) an "evolutionary local search" approach.

_[**Spoiler alert:** SuperScott discovers that the local search approach, while not as efficient as intelligent design, is nevertheless much more efficient than brute-force search. And thus, he concludes, the arguments of the ID folks to the effect of "I can't see a cleverer way to do it, therefore it **must** be either brute-force search or else miraculous nondeterminism" are invalid.]_

Since my appearance together with Morgan Freeman on cable TV raises a large number of questions, I've decided to field a few of them in the following FAQ.

**Q: How can I watch?**

[Amazon Instant Video has the episode here for $1.99](http://www.amazon.com/gp/product/B00E9PS3XS/ref=dv_dp_ep10). (No doubt you can also find it on various filesharing sites, but let it be known that I'd never condone such nefarious activity.) My segment is roughly from 10:40 until 17:40.

**Q: Given that you 're not a biologist, and that your research has basically nothing to do with evolution, why did they ask to interview you?**

Apparently they wanted a mathematician or computer scientist who also had some experience spouting about Big Ideas. So they first asked Greg Chaitin, but Chaitin couldn't do it and suggested me instead.

**Q: Given how little relevant expertise you have, why did you _agree_ to be interviewed?**

To be honest, I was extremely conflicted. I kept saying, "Why don't you interview a biologist? Or at least a computational biologist, or someone who studies genetic algorithms?" They replied that they _did_ have more bio-oriented people on the show, but they also wanted me to provide a "mathematical" perspective. So, I consulted with friends like [Sean Carroll](http://www.preposterousuniverse.com/blog/), who's appeared on _Through the Wormhole_ numerous times. And after reflection, I decided that I _do_ have a way to explain a central conceptual point about algorithms, complexity, and the amount of time needed for natural selection--a point that, while hardly "novel," is something that many laypeople might not have seen before and that might interest them. Also, as an additional argument in favor of appearing, MORGAN FREEMAN!

[](https://scottaaronson.blog/wp-content/uploads/2013/08/morganfreeman.jpg)

So I agreed to do it, but only under two conditions:

(1) At least one person with a biology background would also appear on the show, to refute the arguments of intelligent design.  
(2) I would talk only about stuff that I actually understood, like the ability of local search algorithms to avoid the need for brute-force search.

I'll let you judge for yourself to what extent these conditions were fulfilled.

**Q: Did you get to meet Morgan Freeman?**

Alas, no. But at least I got to hear him refer repeatedly to "SuperScott" on TV.

**Q: What was the shooting like?**

Extremely interesting. I know more now about TV production than I did before!

It was a continuing negotiation: they kept wanting to say that I was "on a quest to mathematically prove evolution" (or something like that), and I kept telling them they weren't allowed to say that, or anything else that would give the misleading impression that what I was saying was either original or directly related to my research. I also had a long discussion about the P vs. NP problem, which got cut for lack of time (now P and NP are only shown on the whiteboard). On the other hand, the crew was extremely accommodating: they really wanted to do a good job and to get things right.

The most amusing tidbit: I knew that local search would take O(n4) time to 2-color an nxn chessboard (2-coloring being a special case of 2SAT, to which [Schöning's algorithm](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=814612) applies), but I didn't know the constant. So I wrote a program to get the specific number of steps when n=8 (it's about 5000). I then repeatedly modified and reran the program during the taping, as we slightly changed what we were talking about. It was the first coding I'd done in a while.

**Q: How much of the segment was your idea, and how much was theirs?**

The chessboard was my idea, but the "SuperScott" bit was theirs. Luddite that I am, I was just going to get down on hands and knees and move apples and oranges around on the chessboard myself.

Also, they wanted me to speak in front of a church in Boston, to make a point about how many people believe that God created the universe. I nixed that idea and said, why not just do the whole shoot in the Stata Center? I mean, MIT spent $300 million _just_ to make the building where I work as "visually arresting" as possible--at the expense of navigability, leakage-resilience, and all sorts of other criteria--so why not take advantage of it? Plus, that way I'll be able to crack a joke about how Stata _actually looks_ _like_ it was created by that favorite creationist strawman, a tornado passing through a junkyard.

Needless to say, all the stuff with me drawing complexity class inclusion diagrams on the whiteboard, reading [my and Alex Arkhipov's linear-optics paper](http://theoryofcomputing.org/articles/v009a004/v009a004.pdf), walking around outside with an umbrella, lifting the umbrella to face the camera dramatically--that was all just the crew telling me what to do. (Well, OK, they didn't tell me _what_ to write on the whiteboard or view on my computer, just that it should be something sciencey. And the umbrella thing wasn't planned: it really just happened to be raining that day.)

**Q: Don 't you realize that not a word of what you said was new--indeed, that all you did was to translate the logic of natural selection, which Darwin understood in 1859, into algorithms and complexity language?**

Yes, of course, and I'm sorry if the show gave anyone the impression otherwise. I repeatedly begged them not to claim newness or originality for anything I was saying. On the other hand, one shouldn't make the mistake of assuming that what's obvious to nerds who read science blogs is obvious to everyone else: I know for a fact that it isn't.

**Q: Don 't you understand that you can't "prove" mathematically that evolution by natural selection is really what happened in Nature?**

Of course! You can't even prove mathematically that bears crap in the woods (unless crapping in the woods were taken as part of the _definition_ of bears). To the writers' credit, they did have Morgan Freeman explain that I wasn't claiming to have "proved" evolution. Personally, I wish Freeman had gone even further--to say that, at present, we don't even have mathematical theories that would explain from first principles why 4 billion years is a "reasonable" amount of time for natural selection to have gotten from the primordial soup to humans and other complex life, whereas (say) 40 million years is _not_ a reasonable amount. One could _imagine_ such theories, but we don't really have any. What we do have is (a) the observed fact that evolution _did_ happen in 4 billion years, and (b) the theory of natural selection, which explains in great detail why one's initial intuition--that such evolution _can 't possibly_ have happened by "blind, chance natural processes" alone--is devoid of force.

**Q: Watching yourself presented in such a goony way --scribbling Complicated Math Stuff on a whiteboard, turning dramatically toward the camera, etc. etc.--didn't you feel silly?**

Some of it  _is_ silly, no two ways about it! On the other hand, I feel satisfied that I got across at least _one_ correct and important scientific point to hundreds of thousands of people. And that, one might argue, is sufficiently worthwhile that it should outweigh any embarrassment about how goofy I look.
