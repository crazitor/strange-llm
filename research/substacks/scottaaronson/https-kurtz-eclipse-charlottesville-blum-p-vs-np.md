---
title: "HTTPS / Kurtz / eclipse / Charlottesville / Blum / P vs. NP"
author: "Scott Aaronson"
date: "Fri, 25 Aug 2017"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=3409"
---

This post has a grab bag of topics, unified only by the fact that I can no longer put off blogging about them. So if something doesn't interest you, just scroll down till you find something that does.

* * *

Great news, everyone: following a few reader complaints about the matter, the scottaaronson.com domain now supports [https](https://en.wikipedia.org/wiki/HTTPS#History)--and even automatically redirects to it! I'm so proud that _Shtetl-Optimized_ has finally entered the technological universe of 1994. Thanks so much to heroic reader Martin Dehnel-Wild for setting this up for me.

**Update 26/08/2017:**  Comments should now be working again; comments are now coming through to the moderated view in the blog's control panel, so if they don't show up immediately it might just be awaiting moderation. Thanks for your patience.

* * *

Last weekend, I was in Columbia, South Carolina, for a workshop to honor the 60th birthday of [Stuart Kurtz](http://people.cs.uchicago.edu/~stuart/), theoretical computer scientist at the University of Chicago.  I gave a talk about how work Kurtz was involved in from the 1990s--for example, on defining the complexity class [GapP](https://complexityzoo.uwaterloo.ca/Complexity_Zoo:G#gapp), and constructing oracles that satisfy conflicting requirements simultaneously--plays a major role in modern research on quantum computational supremacy: as an example, my [recent paper with Lijie Chen](http://www.scottaaronson.com/papers/quantumsupre.pdf).  (Except, what a terrible week to be discussing the paths to supremacy!  I promise there are no tiki torches involved, only much weaker photon sources.)

Coincidentally, I don't know if you read anything about this on social media, but there was this total solar eclipse that passed right over Columbia at the end of the conference.

I'd always wondered why some people travel to remote corners of the earth to catch these.  So the sky gets dark for two minutes, and then it gets light again, in a way that's been completely understood and predictable for centuries?

Having seen it, I can now tell you the deal, if you missed it and prefer to read about it here rather than 10500 other places online.  At risk of stating the obvious: it's not the dark sky; it's the sun's corona visible around the moon.  Ironically, it's only when the sun's blotted out that you can actually _look_ at the sun, at all the weird stuff going on around its disk.

OK, but totality is "only" to eclipses as orgasms are to sex.  There's also the whole social experience of standing around outside with friends for an hour as the moon gradually takes a bigger bite out of the sun, staring up from time to time with eclipse-glasses to check its progress--and then everyone breaking into applause as the sky finally goes mostly dark, and you can look at the corona with the naked eye.  And then, if you like, standing around for _another_ hour as the moon gradually exits the other way.  (If you're outside the path of totality, this standing around and checking with eclipse-glasses is the _whole_ experience.)

One cool thing is that, a little before and after totality, shadows on the ground have little crescents in them, as if the eclipse is imprinting its "logo" all over the earth.

For me, the biggest lesson the eclipse drove home was the [logarithmic nature of perceived brightness](https://physics.stackexchange.com/questions/262813/why-does-the-sun-have-to-be-nearly-fully-covered-to-notice-any-darkening-in-an-e/262818) (see also [Scott Alexander's story](http://slatestarcodex.com/2017/08/21/partial-credit/)).  Like, the sun can be more than 90% occluded, and yet it's barely a shade darker outside.  And you can _still_ only look up with glasses so dark that they blot out everything _except_  the sliver of sun, which still looks pretty much like the normal sun if you catch it out of the corner of your unaided eye.  Only during totality, and a few minutes before and after, is the darkening obvious.

* * *

Another topic at the workshop, unsurprisingly, was the ongoing darkening of the United States.  If it wasn't obvious from my blog's name, and if saying so explicitly will make any difference for anything, let the record state:

**_Shtetl-Optimized_ condemns Nazis, as well as anyone who knowingly marches with Nazis or defends them as "fine people."**

For a year, this blog has consistently described the now-president as a thug, liar, traitor, bully, sexual predator, madman, racist, and fraud, and has urged decent people everywhere to fight him by every peaceful and legal means available.  But if there's some form of condemnation that I accidentally missed, then after Charlottesville, and Trump's unhinged quasi-defenses of violent neo-Nazis, and defenses of his previous defenses, etc.--please consider _Shtetl-Optimized_ to have condemned Trump that way also.

At least Charlottesville seems to have set local decisionmakers on an unstoppable course toward removing the country's remaining Confederate statues--something [I strongly supported back in May](https://scottaaronson.blog/?p=3285), before it had become the fully thermonuclear issue that it is now.  In an overnight operation, UT Austin [has taken down its statues](https://www.nytimes.com/2017/08/21/us/texas-austin-confederate-statues.html) of Robert E. Lee, Albert Johnston, John Reagan, and Stephen Hogg.  (I confess, the _postmaster general_ of the Confederacy wouldn't have been my #1 priority for removal.  And, genuine question: what did Texas governor [Stephen Hogg](https://en.wikipedia.org/wiki/Jim_Hogg) do that was so awful for his time, besides naming his daughter [Ima Hogg](https://en.wikipedia.org/wiki/Ima_Hogg)?)

* * *

A final thing to talk about--yeah, we can't avoid it--is [Norbert Blum's claimed proof of P≠NP](https://arxiv.org/abs/1708.03486).  I suppose I should be gratified that, after my last post, there were commenters who said, "OK, but enough about gender politics--what about P vs. NP?"  Here's what I wrote on Tuesday the 15th:

To everyone who keeps asking me about the “new” P≠NP proof: I’d again bet $200,000 that the paper won’t stand, except that the last time I tried that, it didn’t achieve its purpose, which was to get people to stop asking me about it. So: please stop asking, and if the thing hasn’t been refuted by the end of the week, you can come back and tell me I was a closed-minded fool.

Many people misunderstood me to be saying that I'd [again](https://scottaaronson.blog/?p=456) bet $200,000, even though the sentence said the exact opposite.  Maybe I should've said: _I 'm searching in vain for the right way to teach the nerd world to get less excited about these claims, to have the same reaction that the experts do, which is 'oh boy, not another one'--which doesn't mean that you know the error, or even that there is an error, but just means that you know the history._

Speaking of which, some friends and I recently had an awesome idea.  Just today, I registered the domain name **haspvsnpbeensolved.com**.  I'd like to set this up with a form that lets you type in the URL of a paper claiming to resolve the P vs. NP problem.  The site will then take 30 seconds or so to process the paper--with a status bar, progress updates, etc.--before finally rendering a verdict about the paper's correctness.  Do any readers volunteer to help me create this?  Don't worry, I'll supply the secret algorithm to decide correctness, and will personally vouch for that algorithm for as long as the site remains live.

I have nothing bad to say about Norbert Blum, who made important contributions including the [3n circuit size lower bound](http://scidok.sulb.uni-saarland.de/volltexte/2011/4065/pdf/fb14_1982_13ocr.pdf) for an explicit Boolean function--something that stood until very recently as the world record--and whose P≠NP paper was lucidly written, passing many of the [most obvious checks](https://scottaaronson.blog/?p=458).  And I received a bit of criticism for my "dismissive" stance.  _Apparently_ , some right-wing former string theorist who I no longer read, whose name rhymes with Mubos Lotl, even accused me of being a conformist left-wing ideologue, driven to ignore Blum's proof by an irrational conviction that any P≠NP proof will necessarily be so difficult that it will need to "await the Second Coming of Christ."  Luca Trevisan's [reaction](https://lucatrevisan.wordpress.com/2017/08/15/on-norbert-blums-claimed-proof-that-p-does-not-equal-np/#comment-20470) to that is worth quoting:

I agree with [Mubos Lotl] that the second coming of Jesus Christ is not a necessary condition for a correct proof that P is different from NP. I am keeping an open mind as to whether it is a sufficient condition.

On reflection, though, Mubos has a point: all of us, including me, should keep an open mind.  Maybe P≠NP (or P=NP!) is vastly easier to prove than most experts think, and is susceptible to a "fool's mate."

That being the case, it's only intellectual honesty that compels me to report that, by about Friday of last week--i.e., exactly on my predicted schedule--a clear consensus had developed among experts that Blum's P≠NP proof was irreparably flawed, and the consensus has stood since that time.

I've often wished that, even just for an hour or two, I could be free from this terrifying burden that I've carried around since childhood: the burden of having the right instincts about virtually everything.  Trust me, this "gift" is a lot less useful than it sounds, especially when reality so often [contradicts](https://scottaaronson.blog/?p=3376) what's popular or expedient to say.

The background to Blum's attempt, the counterexample that shows the proof has to fail _somewhere_ , and the specifics of what appears to go wrong have already been covered at length elsewhere: see especially [Luca's post](https://lucatrevisan.wordpress.com/2017/08/15/on-norbert-blums-claimed-proof-that-p-does-not-equal-np/), [Dick Lipton's post](https://rjlipton.wordpress.com/2017/08/17/on-the-edge-of-eclipses-and-pnp/), [John Baez's post](https://johncarlosbaez.wordpress.com/2017/08/15/norbert-blum-on-p-versus-np/), and the [CS Theory StackExchange thread](https://cstheory.stackexchange.com/questions/38803/is-norbert-blums-2017-proof-that-p-ne-np-correct).

Very briefly, though: Blum claims to generalize some of the most celebrated complexity results of the 1980s--namely, superpolynomial lower bounds on the sizes of _monotone_ circuits, which consist entirely of Boolean AND and OR gates--so that they also work for _general_ (non-monotone) circuits, consisting of AND, OR, and NOT gates.  Everyone agrees that, if this succeeded, it would imply P≠NP.

Alas, another big discovery from the 1980s was that there are monotone Boolean functions (like Perfect Matching) that require superpolynomial-size monotone circuits, even though they have polynomial-size non-monotone circuits.  Why is that such a bummer?  Because it means our techniques for proving monotone circuit lower bounds can't possibly work in as much generality as one might've naïvely hoped: if they did, they'd imply not merely that P doesn't contain NP, but also that P doesn't contain itself.

Blum was aware of all this, and gave arguments as to why his approach evades the Matching counterexample.  The trouble is, there's _another_ counterexample, which Blum doesn't address, called [Tardos's function](https://en.wikipedia.org/wiki/Tardos_function).  This is a weird creature: it's obtained by starting with a graph invariant called the [Lovász theta function](https://en.wikipedia.org/wiki/Lov%C3%A1sz_number), then looking at a polynomial-time approximation scheme for the theta function, and finally rounding the output of that PTAS to get a monotone function.  But whatever: in [constructing this function](http://www.cs.cornell.edu/~eva/Gap.Between.Monotone.NonMonotone.Circuit.Complexity.is.Exponential.pdf), Tardos achieved her goal, which was to produce a monotone function that _all_ known lower bound techniques for monotone circuits work perfectly fine for, but which is nevertheless in P (i.e., has polynomial-size non-monotone circuits).  In particular, if Blum's proof worked, then it would also work for Tardos's function, and that gives us a contradiction.

Of course, this merely tells us that Blum's proof must _have_  one or more mistakes; it doesn't pinpoint where they are.  But the latter question has now been addressed as well.  On CS StackExchange, an anonymous commenter who goes variously by "idolvon" and "vloodin" provides a [detailed analysis](https://cstheory.stackexchange.com/a/38836/45696) of the proof of Blum's crucial Theorem 6.  I haven't gone through every step myself, and there might be more to say about the matter than "vloodin" has, but several experts who are at once smarter, more knowledgeable, more cautious, and more publicity-shy than me have confirmed for me that vloodin correctly identified the erroneous region.

To those who wonder what gave me the confidence to call this immediately, without working through the details: besides the Cassandra-like burden that I was born with, I can explain something that might be helpful.  When Razborov achieved his superpolynomial monotone lower bounds in the 1980s, there was a brief surge of excitement: how far away could a P≠NP proof possibly be?  But then people, including Razborov himself, understood much more deeply what was going on--an understanding that was reflected in the theorems they proved, but also wasn't completely captured by those theorems.

What was going on was this: monotone circuits are an interesting and nontrivial computational model.  Indeed for certain Boolean functions, such as the ["slice functions,"](http://epubs.siam.org/doi/abs/10.1137/0215037) they're every bit as powerful as general circuits.  However, _insofar as it 's possible to prove superpolynomial lower bounds on monotone circuit size_, it's possible only because monotone circuits are ridiculously less expressive than general Boolean circuits _for the problems in question_.  E.g., it's possible only because monotone circuits aren't expressing pseudorandom functions, and therefore aren't engaging the [natural proofs barrier](https://en.wikipedia.org/wiki/Natural_proof) or most of the other terrifying beasts that we're up against.

So what can we say about the prospect that a minor tweak to the monotone circuit lower bound techniques from the 1980s would yield P≠NP?  If, like Mubos Lotl, you took the view that discrete math and theory of computation are just a mess of disconnected, random statements, then such a prospect would seem as likely to you as not.  But if you're armed with the understanding above, then this possibility is a lot like the possibility that the [OPERA experiment discovered superluminal neutrinos](https://en.wikipedia.org/wiki/Faster-than-light_neutrino_anomaly): no, not a logical impossibility, but something that's safe to bet against at 10,000:1 odds.

During the discussion of Deolalikar's earlier P≠NP claim, I once compared betting against a proof that all sorts of people are calling "formidable," "solid," etc., to [standing in front of a huge pendulum](https://www.youtube.com/watch?v=i2GdY1OlDpA)--behind the furthest point that it reached the last time--even as it swings toward your face.  Just as certain physics teachers stake their lives on the conservation of energy, so I'm willing to stake my academic reputation, again and again, on the conservation of circuit-lower-bound difficulty.  And here I am, alive to tell the tale.
