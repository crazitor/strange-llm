---
title: "Do theoretical computer scientists despise practitioners?  (Answer: no, that’s crazy)"
author: "Scott Aaronson"
date: "Thu, 28 Aug 2014"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=1981"
---

A roboticist and _Shtetl-Optimized_ fan named Jon Groff recently emailed me the following suggestion for a blog entry:

I think a great idea for an entry would be the way that in fields like particle physics the theoreticians and experimentalists get along quite well but in computer science and robotics in particular there seems to be a great disdain for the people that actually do things from the people that like to think about them. Just thought I'd toss that out there in case you are looking for some subject matter.

After I replied (among other things, raising my virtual eyebrows over his rosy view of the current state of theoretician/experimentalist interaction in particle physics), Jon elaborated on his concerns in a subsequent email:

[T]here seems to be this attitude in CS that getting your hands dirty is unacceptable. You haven't seen it because you sit a lofty heights and I tend to think you always have. I have been pounding out code since ferrite cores. Yes, Honeywell 1648A, so I have been looking up the posterior of this issue rather than from the forehead as it were. I guess my challenge would be to find a noteworthy computer theoretician somewhere and ask him:  
1) What complete, working, currently functioning systems have you designed?  
2) How much of the working code did you contribute?  
3) Which of these systems is still operational and in what capacity?  
Or say, if the person was a famous robotics professor or something you may ask:  
1) Have you ever actually 'built' a 'robot'?  
2) Could you, if called upon, design and build an easily tasked robot safe for home use using currently available materials and code?

So I wrote a second reply, which Jon encouraged me to turn into a blog post (kindly giving me permission to quote him). In case it's of interest to anyone else, my reply is below.

* * *

Dear Jon,

For whatever it's worth, when I was an undergrad, I spent two years working as a coder for Cornell's RoboCup robot soccer team, handling things like the goalie. (That was an extremely valuable experience, one reason being that it taught me how badly I sucked at meeting deadlines, documenting my code, and getting my code to work with other people's code.) Even before that, I wrote shareware games with my friend [Alex Halderman](https://jhalderm.com/) (now a famous computer security expert at U. of Michigan); we made almost $30 selling them. And I spent several summers working on applied projects at Bell Labs, back when that was still a thing. And by my count, I've written four papers that involved code I personally wrote and experiments I did (one on [hypertext](http://www.scottaaronson.com/papers/hypertext.pdf), one on [stylometric clustering](http://www.scottaaronson.com/papers/sc.doc), one on [Boolean function query properties](http://www.scottaaronson.com/papers/bfpsiam.pdf), one on [improved simulation ](http://www.scottaaronson.com/papers/chp6.pdf)[of stabilizer circuits](http://www.scottaaronson.com/papers/chp6.pdf)--for the last of these, the [code](http://www.scottaaronson.com/chp/) is actually still used by others). While this is all from the period 1994-2004 (these days, if I need any coding done, I use the extremely high-level programming language called "undergrad"), I don't think it's entirely true to say that I "never got my hands dirty."

But even if I _hadn 't_ had any of those experiences, or other theoretical computer scientists hadn't had analogous ones, your questions still strike me as unfair. They're no more fair than cornering a star coder or other practical person with questions like, "Have you ever proved a theorem? A _nontrivial_ theorem? Why is BPP contained in P/poly? What's the cardinality of the set of Turing-degrees?" If the coder can't easily answer these questions, would you say it means that she has "disdain for theorists"? (I was expecting some discussion of this converse question in your email, and was amused when I didn't find any.)

Personally, I'd say "of course not": maybe the coder is great at coding, doesn't need theory very much on a day-to-day basis and doesn't have much free time to learn it, but (all else equal) would be happy to know more. Maybe the coder likes theory as an outsider, even has friends from her student days who are theorists, and who she'd go to if she ever _did_ need their knowledge for her work. Or maybe not. Maybe she's an asshole who looks down on anyone who doesn't have the exact same skill-set that she does. But I  _certainly_ couldn't conclude that from her inability to answer basic theory questions.

I'd say just the same about theorists. If they don't have as much experience building robots as they should have, don't know as much about large software projects as they should know, etc., then those are all defects to add to the long list of their other, unrelated defects. But it would be a mistake to assume that they failed to acquire this knowledge _because of disdain for practical people_ , rather than for mundane reasons like busyness or laziness.

Indeed, it's also possible that they respect practical people all the more, because they tried to do the things the practical people are good at, and discovered for themselves how hard they were. Maybe they  _became_ theorists partly because of that self-discovery--that was certainly true in my case. Maybe they'd be happy to talk to or learn from a practical roboticist like yourself, but are too shy or too nerdy to initiate the conversation.

Speaking of which: yes, let's let bloom a thousand collaborations between theorists and practitioners! Those are the lifeblood of science. On the other hand, based on personal experience, I'm also sensitive to the effect where, because of pressures from funding agencies, theorists have to try to _pretend_ their work is "practically relevant" when they're really just trying to discover something cool, while meantime, practitioners have to pretend their work is theoretically novel or deep, when really, they're just trying to write software that people will want to use. I'd love to see both groups freed from this distorting influence, so that they can collaborate for real reasons rather than fake ones.

(I've also often remarked that, if I _hadn 't_ gravitated to the extreme theoretical end of computer science, I think I might have gone instead to the extreme practical end, rather than to any of the points in between. That's because I hate the above-mentioned distorting influence: if I'm going to try to understand the ultimate limits of computation, then I should pursue that wherever it leads, even if it means studying computational models that won't be practical for a million years. And conversely, if I'm going to write useful software, I should throw myself 100% into _that_ , even if it means picking an approach that's well-understood, clunky, and reliable over an approach that's new, interesting, elegant, and likely to fail.)

Best,  
Scott
