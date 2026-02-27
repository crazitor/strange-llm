---
title: "Barriers to proving P!=NP and moving this blog"
author: "Scott Aaronson"
date: "Sun, 16 Sep 2007"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=272"
---

Thanks, everyone, for your patience, and your numerous complaints about the _Technology Review_ site! Currently, the folks at _TR_ say they can do all the minor things people asked for, like adding permalinks to the titles and letting people include their URL's with their comments. On the other hand, they can't make it so you can post comments without logging in, and they can't decrease the size of the ad bar. (I suggested that they at least turn my sidebar into drop-down menus, thereby increasing the screen width available for the entries; they said they'd look into that.) Also, they can't provide the full text in RSS (since God forbid, that might let people read the blog without seeing ads), although they _can_ give the first 150 words or so.

As you can imagine, TR's response has put me in a difficult position. From their perspective, they've been bending over backwards to accommodate me; from my perspective (and I gather from most readers'), their offer still falls short of acceptable. When I originally agreed to let them host me, I imagined that the blog would look just as it does now, with maybe a few unobtrusive ads here or there. I didn't even think to ask about the RSS feed or the screen width available for entries.

And so, after weeks of introspection (well, mostly being tied up with other work), I've reached a decision: _I will continue to host my blog right here, on Bluehost, until TR comes up with something that both parties can live with._ I _like_ the TR people and appreciate their interest, but I'm not in any particular hurry to move, especially if it means crippling this blog so that no will read it. It's true that [Bluehost sucks](http://www.google.com/search?q=bluehost+sucks), and that I no longer have time to be a webmaster -- but once I get grant money, maybe I can pay someone to take care of these things for me.

Finally, since all this self-referentiality gets tiresome, [here are the PowerPoint slides](http://www.scottaaronson.com/talks/alg3.ppt) for a talk I gave at MIT last week, about recent joint work with Avi Wigderson on a new barrier to proving P≠NP. (Note: The day before the talk, PowerPoint trashed my file, and I had to recreate the entire presentation from memory. Always make backup copies! Excellent advice, in my opinion.)

Abstract:

> **Algebrization: A New Barrier in Complexity Theory**
> 
> Any proof of P≠NP will have to overcome two barriers: relativization and natural proofs. Yet over the last decade, we have seen circuit lower bounds (for example, that PP does not have linear-size circuits) that overcome both barriers simultaneously. So the question arises of whether there is a third barrier to progress on the central questions in complexity theory.
> 
> In this talk we present such a barrier, which we call "algebraic relativization" or "algebrization." The idea is that, when we relativize some complexity class inclusion, we should give the simulating machine access not only to an oracle A, but also to the low-degree extension of A over a finite field or ring.
> 
> We systematically go through basic results and open problems in complexity theory to delineate the power of the new algebrization barrier. We first show that all known non-relativizing results -- both inclusions such as IP=PSPACE and MIP=NEXP, and separations such as MAEXP⊄P/poly -- do indeed algebrize. We next show that most open problems -- including P versus NP, P versus BPP, and NEXP versus P/poly -- will require non-algebrizing techniques, of which we currently have not a single example. In some cases algebrization seems to explain exactly why progress stopped where it did: for example, why we have superlinear circuit lower bounds for PromiseMA but not for NP.
> 
> We also exhibit a surprising connection between algebrization and communication complexity. Using this connection, we give an MA-protocol for the Inner Product function with O(√n log(n)) communication (essentially matching a lower bound of Klauck), and describe a pure communication complexity conjecture whose truth would imply P≠NP.

Comments welcome. We'll hopefully have a writeup soon.
