---
title: "You down with SPP?"
author: "Scott Aaronson"
date: "Sun, 17 Jun 2007"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=249"
---

I've been in San Diego all week for the [FCRC](http://www.acm.org/fcrc/) (Federated Computing Research Conference), which just wrapped up yesterday. I was here for [Complexity'2007](http://facweb.cs.depaul.edu/jrogers/complexity/), but, lawless rebel that I am, I also crashed some of the talks at [STOC'2007](http://www.research.att.com/~dsj/stoc07.html). Highlights:

  * Many of my friends wanted to skip the plenary talk on "Computer Science: Past, Present, and Future," by past Computing Research Association Chair [Ed Lazowska](http://lazowska.cs.washington.edu/). But I urged them to go despite the title, since I'd met Lazowska when I interviewed at the University of Washington, and immediately concluded that _this is the guy we want in charge of our field_. As it turned out, Lazowska gave the most rousing defense of computer science research I've ever heard. Here's what I remember: 2004 was the first year that human beings produced more transistors than grains of rice (~10 quintillion). Academic computer science research more than paid for itself over the last two decades by producing at least 15 billion-dollar industries. Computer scientists should be tackling the biggest issues in the world, including climate change and third-world poverty (Lazowska mentioned a project he's involved with to put thousands of sensors under the ocean near the Northwest US, thereby "reducing oceanography to a computer science problem," as well as a project of his student [Tapan Parikh](http://www.cs.washington.edu/homes/tapan/), to let illiterate farmers in India and Guatemala upload financial records via cellphones with intermittent access). Computer scientists should bring self-driving cars from prototype to reality, thereby saving some of the 45,000 people in the US alone who die in auto accidents every year. The future of theoretical computer science lies in transforming the other sciences (math, physics, economics, biology) via computational thinking. Had Watson and Crick been computer scientists, they would've realized immediately that the real import of their discovery had nothing to do with the biochemical details, and everything to do with the fact that DNA is a digital code. A piece of computer science (P vs. NP) is what many now consider the preeminent open problem in mathematics. Quantum computing might not work but certainly merits a huge effort. Our introductory CS courses suck. We've been doing a terrible job recruiting women.******Update (6/23):** Slides for Ed Lazowska's talk, as well as another inspiring talk by Christos Papadimitriou, can be found [here](http://lazowska.cs.washington.edu/fcrc/).


  * I gave a [talk](http://www.scottaaronson.com/talks/qcap.ppt) on my [paper](http://www.scottaaronson.com/papers/qcap.pdf) with Greg Kuperberg, on quantum versus classical proofs and advice.


  * I gave [another talk](http://www.scottaaronson.com/talks/andris.ppt) on the paper ["Quantum t-designs"](http://arxiv.org/abs/quant-ph/0701126), by my colleagues Andris Ambainis and Joe Emerson. Why? Because Joe couldn't make it to San Diego, and Andris lost his passport. As I promised Andris, the vast majority of the talk was _not_ delivered in my imitation of his voice.


  * [Sergey Yekhanin](http://theory.lcs.mit.edu/~yekhanin/) gave a talk on his [paper](http://theory.lcs.mit.edu/~yekhanin/Papers/nice_PIR.pdf) "Towards 3-query locally decodable codes of subexponential length," which not only won the Danny Lewin Best Student Paper Award but _also_ shared the STOC'07 Best Paper Award. Not to toot my own breakthrough-recognition horn, but … you [saw it here first](https://scottaaronson.blog/?p=142).


  * [Ryan Williams](http://www.cs.cmu.edu/~ryanw/), the pride of Alabama, won the Complexity Best Student Paper Award for his [excellent paper](http://eccc.hpi-web.de/eccc-reports/2007/TR07-036/index.html) "Time-space tradeoffs for counting NP solutions modulo integers." This marks the second time Ryan has won this award, as well as the first time the award has been given twice to a former Cornell undergrad and resident of [Telluride House](http://www.tellurideassociation.org/cbfront.html) in the late 1990's (no … wait). So what did Ryan prove? Alright, suppose you have O(n1.8) time and no(1) memory, and you want to count the number of satisfying assignments of a Boolean formula, modulo a prime number p. Then there's at most one prime p for which you can do this. Ryan has no idea _which_ prime, and conjectures in any case that it doesn't exist. I'm not making this up.


  * [Guy Kindler](http://dimacs.rutgers.edu/~gkindler/) gave a talk on his [amazing paper](http://eccc.hpi-web.de/eccc-reports/2007/TR07-043/index.html) with [Uri Feige](http://www.wisdom.weizmann.ac.il/~feige/) and [Ryan O'Donnell](http://www.cs.cmu.edu/~odonnell/), "Understanding parallel repetition requires understanding foams." Read the paper: the title is literally true.


  * I saw [Terence Tao](http://www.math.ucla.edu/~tao/).


  * [Ronald de Wolf](http://homepages.cwi.nl/~rdewolf/) and [Harry Buhrman](http://homepages.cwi.nl/~buhrman/) are reading this entry over my shoulder right now as I sit in the airport terminal typing.


  * As I watched the conference regulars -- Lance Fortnow, Bill Gasarch, Harry Buhrman (yes, Harry, you got another mention -- happy?), Ken Regan, etc. -- banter and drink coffee, I realized that the IEEE Conference on Computational Complexity _desperately needs an official theme song_. The song should have real complexity-theoretic content, but nevertheless be a little edgier than [Find the Longest Path](http://valis.cs.uiuc.edu/~sariel/misc/funny/#longest-path). So without further ado, I present to you a preliminary effort along these lines, due to Troy Lee and myself (aka "Nerdy by Nature"):  


> _You down with[SPP](http://qwiki.caltech.edu/wiki/Complexity_Zoo#spp) (Yeah you know me)  
>  You down with SPP (Yeah you know me)  
>  You down with SPP (Yeah you know me)  
>  Who's down with SPP (Every last attendee)_

(Note: [BPP](http://qwiki.caltech.edu/wiki/Complexity_Zoo#bpp) and [ZPP](http://qwiki.caltech.edu/wiki/Complexity_Zoo#zpp) also would've fit the meter, but those are really more appropriate for STOC than Complexity.)

**Update (6/20):** We may [have a winner](http://weblog.fortnow.com/2007/06/complexity-theory-theme-song-options.html#4032691377325832224), Aaron Sterling's _I Just Do Theory_. (Thanks to Bill Gasarch for the pointer.)


