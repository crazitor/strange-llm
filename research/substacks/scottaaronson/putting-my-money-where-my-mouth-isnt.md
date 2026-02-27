---
title: "Putting my money where my mouth isn’t"
author: "Scott Aaronson"
date: "Mon, 09 Aug 2010"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=456"
---

A few days ago, [Vinay Deolalikar](http://www.hpl.hp.com/personal/Vinay_Deolalikar/) of HP Labs started circulating a [claimed proof of P≠NP](http://www.hpl.hp.com/personal/Vinay_Deolalikar/Papers/pnp_preliminary.pdf). As anyone could predict, the alleged proof has [already been Slashdotted](http://science.slashdot.org/story/10/08/08/226227/Claimed-Proof-That-P--NP) (see also [Lipton's blog](http://rjlipton.wordpress.com/2010/08/08/a-proof-that-p-is-not-equal-to-np/) and [Bacon's blog](http://dabacon.org/pontiff/?p=4286)), and my own inbox has been filling up faster than the Gulf of Mexico.

Alas, a simple "top kill" seems unlikely to work here. What's obvious from even a superficial reading is that Deolalikar's manuscript is well-written, and that it discusses the history, background, and difficulties of the P vs. NP question in a competent way. More importantly (and in contrast to 98% of claimed P≠NP proofs), even if this attempt fails, it seems to introduce some thought-provoking new ideas, particularly a connection between statistical physics and the first-order logic characterization of NP. I'll leave it to the commenters to debate whether Deolalikar's paper exhibits one or more of the [Ten Signs A Claimed Mathematical Breakthrough Is Wrong](https://scottaaronson.blog/?p=304).

"But enough question-dodging!" you exclaim. "Is the proof right or isn't it? C'mon, it's been like _three hours_ since you first saw it--what's taking you so long?" Well, somehow, I haven't yet found the opportunity to study this 103-page manuscript in detail. Furthermore, I don't plan to interrupt my vacation time in Israel and Greece to do so, _unless_ experts who _have_ studied the paper in detail start telling me that I should.

Unfortunately, I can already foresee that the above response will fail to staunch the flow of emails. As a blogger, I'm apparently expected to

(1) render an instantaneous opinion on any claimed mathematical breakthrough,

(2) be consistently right, and

(3) do the above _without_ looking like I'm being unfair or rushing to judgment.

While requirements (1) and (2) are not _so_ hard to satisfy simultaneously, (3) makes my job an extremely difficult one. In fact, I could think of only one mechanism to communicate my hunch about Deolalikar's paper in a way that everyone would agree is (more than) fair to him, _without_ having to invest the hard work to back my hunch up. And thus I hereby announce the following offer:

**_If Vinay Deolalikar is awarded the $1,000,000 Clay Millennium Prize for his proof of P≠NP, then I, Scott Aaronson, will personally supplement his prize by the amount of $200,000._**

I'm dead serious--and I can afford it about as well as you'd think I can.

**Update (August 10):** One whole day into this saga, Dick Lipton and Ken Regan have [written a detailed post](http://rjlipton.wordpress.com/2010/08/09/issues-in-the-proof-that-p%e2%89%a0np/) setting out four possible problems that have already been identified in the proof, and which the ball is now in Deolalikar's court to address. Kudos to Dick, Ken, and numerous commenters for actually digging into the paper (unlike some lazier folks I could name  ).

**Another Update:** Since some journalists seem (unbelievably) to have [missed the point](http://www.pcworld.com/article/202950/hp_researcher_claims_to_crack_compsci_complexity_conundrum.html) of this post, let me now state the point as clearly as I can. The point is this: _I really,**really** doubt that Deolalikar's proof will stand. And while I haven't studied his long, interesting paper in detail and pinpointed the irreparable flaw, something deep inside me rebels against the charade of "keeping an open mind," when long experience with competent but ultimately unsuccessful proof attempts allows me to foresee perfectly well how things are going to play out here. I would make a terrible trial court judge: ten minutes into the proceedings, I'd be screaming, "The defendant obviously did it! I sentence him to death!" Fortunately I'm **not** a judge, and I have a way of stating my prediction that no reasonable person could hold against me: I've literally bet my house on it._

**Yet Another Update:** What's emerged as the perhaps central issue is the bane of so many attempted P≠NP proofs in the past: namely, _why does the proof not work for 2SAT, XOR-SAT, and other problems that are very similar to 3SAT in their statistical properties, yet for which polynomial-time algorithms are known?_ If Deolalikar can't provide a clear and convincing answer to that question, the proof is toast.
