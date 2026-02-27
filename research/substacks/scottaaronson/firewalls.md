---
title: "Firewalls"
author: "Scott Aaronson"
date: "Tue, 27 Aug 2013"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=1508"
---

**Updates (Aug. 29):** John Preskill now has a [very nice post](http://quantumfrontiers.com/2013/08/29/whats-inside-a-black-hole/) summarizing the different views on offer at the firewall workshop, thereby alleviating my guilt for giving you only the mess below. Thanks, John!

And if you check out [John's Twitter feed](https://twitter.com/preskill) (which you should), you'll find another, unrelated gem: a [phenomenal TEDx talk on quantum computing](http://www.youtube.com/watch?v=Rvn_3cCrl9c) by my friend, coauthor, and hero, the Lowerboundsman of Latvia, Andris Ambainis. (Once again, when offered a feast of insight to dispel their misconceptions and ennoble their souls, the YouTube commenters are distinguishing themselves by focusing on the speaker's voice. [Been there](http://www.youtube.com/watch?v=SczraSQE3MY), man, [been there](http://www.youtube.com/watch?v=8bLXHvH9s1A).)

* * *

So, last week I was at the [Fuzzorfire workshop](http://online.kitp.ucsb.edu/online/fuzzorfire_m13/) at the Kavli Institute for Theoretical Physics in Santa Barbara, devoted to the black hole firewall paradox. (The workshop is still going on this week, but I needed to get back early.) For some background:

  * The [original paper by Almheiri et al.](http://arxiv.org/abs/1207.3123) (from July 2012, so now "ancient history")
  * [New York Times article](http://www.nytimes.com/2013/08/13/science/space/a-black-hole-mystery-wrapped-in-a-firewall-paradox.html?pagewanted=all&_r=0) by Dennis Overbye
  * [Quanta article](https://www.simonsfoundation.org/quanta/20121221-alice-and-bob-meet-the-wall-of-fire/) by Jennifer Ouellette
  * [Blog post](http://quantumfrontiers.com/2012/12/03/is-alice-burning-the-black-hole-firewall-controversy/) by John Preskill



I had fantasies of writing a long, witty blog post that would set out my thoughts about firewalls, full of detailed responses to everything I'd heard at the conference, as well as ruminations about [Harlow and Hayden's striking argument](http://arxiv.org/abs/1301.4504) that computational complexity might provide a key to resolving the paradox. But the truth is, I'm recovering from a nasty stomach virus, am feeling "firewalled out," and wish to use my few remaining non-childcare hours before the semester starts to finish writing papers. So I decided that better than nothing would be a hastily-assembled pastiche of links.

First and most important, you can watch all the talks online. In no particular order:

  * [My talk](http://online.kitp.ucsb.edu/online/fuzzorfire_m13/aaronson/) (about the computational complexity underpinnings of the Harlow-Hayden argument)
  * [Stephen Hawking's 10-minute talk by videoconference](http://online.kitp.ucsb.edu/online/fuzzorfire_m13/hawking/), denying that firewalls form, and basically repeating his position from his [black hole bet concession speech](http://arxiv.org/abs/hep-th/0507171) of 2004 (I confess that I don't really understand his arguments)
  * [Lenny Susskind's ER=EPR talk](http://online.kitp.ucsb.edu/online/fuzzorfire_m13/susskind/)
  * [Bill Unruh's entertaining talk](http://online.kitp.ucsb.edu/online/fuzzorfire_m13/unruh/) denouncing the other participants' obsession with unitarity, and defending what he sees as the simplest solution to all the black hole information problems: information dropped into a black hole is simply gone forever, "buh-bye!"
  * [All the other talks](http://online.kitp.ucsb.edu/online/fuzzorfire_m13/)



Here's my own attempt to summarize what's at stake, adapted from a [comment on Peter Woit's blog](http://www.math.columbia.edu/~woit/wordpress/?p=6208&cpage=1#comment-159234) (see also a [rapid response by Lubos](http://motls.blogspot.com/2013/08/insiders-and-outsiders-debate-fuzz-or.html)):

_As I understand it, the issue is actually pretty simple. Do you agree that_  
_(1) the Hawking evaporation process should be unitary, and_  
_(2) the laws of physics should describe the experiences of an infalling observer, not just those of an observer who stays outside the horizon?_  
_If so, then you seem forced to accept_  
_(3) the interior degrees of freedom should just be some sort of scrambled re-encoding of the exterior degrees, rather than living in a separate subfactor of Hilbert space (since otherwise we’d violate unitarity)._  
_But then we get_  
_(4) by applying a suitable unitary transformation to the Hawking radiation of an old enough black hole before you jump into it, someone ought to be able, in principle, to completely modify what you experience when you do jump in. Moreover, that person could be far away from you --an apparent gross violation of locality._

_So, there are a few options: you could reject either (1) or (2). You could bite the bullet and accept (4). You could say that the “experience of an infalling observer” should just be to die immediately at the horizon (firewalls). You could argue that for some reason (e.g., gravitational backreaction, or computational_ _complexity), the unitary transformations required in (4) are impossible to implement even in principle. Or you could go the “Lubosian route,” and simply assert that the lack of any real difficulty is so obvious that, if you admit to being confused, then that just proves you’re an idiot. AdS/CFT is clearly relevant, but as[Polchinski pointed out](http://online.kitp.ucsb.edu/online/fuzzorfire_m13/polchinski/), it does surprisingly little to solve the problem._

_Now, what Almheiri et al. (AMPS) added to the simple logical argument above was really to make the consequence (4) more “concrete” and “vivid”—by describing something that, in principle, someone could actually do to the Hawking radiation before jumping in, such that after you jumped in, if there wasn’t anything dramatic that happened—something violating local QFT and the equivalence principle—then you’d apparently observe a violation of the monogamy of entanglement, a basic principle of quantum mechanics. I 'm sure the bare logic (1)-(4) was known to many people before AMPS: I certainly knew it, but I didn’t call it a “paradox,” I just called it “I don’t understand black hole complementarity”!_

_At any rate, thinking about the “Hawking radiation decoding problem” already led me to some very nice questions in quantum computing theory, which remain interesting even if you remove the black hole motivation entirely. And that helped convince me that something new and worthwhile might indeed come out of this business, despite how much fun it is. (Hopefully whatever does come out won’t be as garbled as Hawking radiation.)_

For continuing live updates from the workshop, check out [John Preskill's Twitter feed](https://twitter.com/preskill).

Or you can ask me to expand on various things in the comments, and I'll do my best. (As I said in my talk, while I'm not sure that the correct quantum description of the black hole interior is within _anyone_ 's professional expertise, it's certainly outside of _mine!_ But I do find this sort of thing fun to think about--how could I not?)

**Unrelated, but also of interest:** check out an [excellent article in Quanta](https://www.simonsfoundation.org/quanta/20130821-the-proof-in-the-quantum-pudding/) by Erica Klarreich, about the recent breakthroughs by Reichardt-Unger-Vazirani, Vazirani-Vidick, and others on classical command of quantum systems.
