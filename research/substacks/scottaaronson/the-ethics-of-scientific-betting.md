---
title: "The ethics of scientific betting"
author: "Scott Aaronson"
date: "Thu, 12 Aug 2010"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=457"
---

Throughout the day, Dick Lipton's blog has hosted a [phenomenal discussion](http://rjlipton.wordpress.com/2010/08/10/update-on-deolalikars-proof-that-p%e2%89%a0np/) of Vinay Deolalikar's attempted proof of P≠NP (of which a [new draft](http://www.hpl.hp.com/personal/Vinay_Deolalikar/Papers/pnp_8_11.pdf) appeared as this blog entry was going to press). As of this writing, the discussion seems to have led to the following two conclusions:

  1. Deolalikar deserves our gratitude; he did a wonderful thing by bringing the TCS community together, in "Stone Soup" fashion, to talk about the P vs. NP problem, and also to stimulate public interest in this fascinating problem.
  2. My [$200,000](https://scottaaronson.blog/?p=456) is safe.



See in particular this [magisterial summary](http://rjlipton.wordpress.com/2010/08/10/update-on-deolalikars-proof-that-p%e2%89%a0np/#comment-4885) by Terry Tao.

For those of you who just arrived from Mars, I'd recommend starting with a [BBC News piece](http://www.bbc.co.uk/news/science-environment-10938302) by Victoria Gill, which by the standards of articles about P vs. NP in major news outlets, bears an amazingly close relation to reality. Indeed, the only thing about the article that I disagreed with was the headline: "Million dollar maths puzzle sparks row." It's not a row, a spat, or even a squabble: at most it's a friendly scientific disagreement among friends.

* * *

As many others have already said, and as the BBC News piece hints at, the clearest reason for skepticism is (basically) that _Deolalikar hasn 't convincingly explained why his approach doesn't also prove problems are hard that are already known to be easy_. This is the simplest sanity check for any attempted proof of P≠NP: if you're showing that an NP-complete problem like 3SAT is not in P, then your proof had better _fail_ for related problems like 2SAT and XOR-SAT, which are known to be in P. Everyone agrees that, if Deolalikar can't answer this objection, the proof is toast.Unfortunately, Deolalikar has responded to pointed questions about this issue with vague promises to address it in a later draft (together with worries that the manuscript is already too long!). This doesn't inspire confidence: if one had really proved P≠NP, one should be able to explain _immediately_ why the proof fails for XOR-SAT.This is far from the _only_ problem with the writeup, but it's a good example of the sort of basic question that Deolalikar needs to answer and hasn't.

* * *

I feel incredible gratitude that Terry Tao, Timothy Gowers, Russell Impagliazzo, Avi Wigderson, Dick Lipton, Cris Moore, Ryan Williams, and other heavy-hitters of the math and CS worlds are hot on the case, and will quickly converge on what (if anything) is interesting and worthy of further study in Deolalikar's writeup. What that _means_ is that those of us trying to enjoy our "summer vacations" are free to debate other issues raised in the past few days--issues that don't involve quite so much, y'know, _actual thinking_.And thus I'd like to propose a blog-roundtable about the following question:

> _Under what circumstances, if any, is it desirable to bet publicly on scientific questions?_

The responses to my $200,000 offer made it obvious that people I like and respect have wildly different views on the above question.

On one side, Bayesians and economic rationalists of all stripes seemed ecstatic. The economist James Miller wrote:

> I talk about prizes in the introductory microeconomics class I teach. I will definitely include what you have just done the next time I teach the course. If more scientists were willing to bet their beliefs we would know a lot more about the world than we currently do.

Several complexity theorists also wrote in privately to express their gratitude:

> dear scott, have you heard? there is a P≠NP proof! what do you think of it? please let me know! just kidding. actually, this email is to thank you. my emailbox has been flooded with emails like the above lines, and thanks to your blog, i can now reply by mentioning your blog posting (the "I've literally bet my house on it" one--which nonetheless may be most remembered for being the only correct use of "literally" on the internet in the past 5-10 years).

On the other side, one distinguished colleague warned that my bet might hurt the image of theoretical computer science, by focusing attention on superficial snap-judgments rather than the technical evaluation of proofs. On this view, it's my professional duty to make only _scientific_ arguments in public: I should keep any personal guesses about a proof's "probability of correctness" to myself. Sure, if I can pinpoint the fatal flaw in Deolalikar's paper, I should say so. But if I can't, I should just grin and bear it, even if journalists brush aside the experts' boring, hard-to-explain technical reservations, and write article after cringe-inducing article exclaiming that _**" P≠NP HAS (APPARENTLY) BEEN PROVED!!!"**_

A different criticism--one that I confess took me by surprise--was that my $200,000 offer was "nasty" and "elitist," something that eats disabled orphans for breakfast. On reflection, though, I think I understand where this was coming from. I _felt like_ I was offering Deolalikar a damn sweet deal: he gets 200 grand if he's right, and pays zilch if he's wrong. However, the act of offering those odds might be interpreted as a perpetual "vote of no confidence" in Deolalikar's _personal_ ability to prove P≠NP.

By analogy, it would be reprehensible if I offered $200,000 to any member of a particular race or gender who proved P≠NP, with the implication being that I didn't think that race or gender was up to the challenge. (And it would remain reprehensible, regardless of whether I eventually had to pay.) Of course, it's relevant that that's nothing like what I did: instead, spurred on by a barrage of emails, I spent a sleepless night with Deolalikar's manuscript, weighed what I understood of his arguments on one hand and what I knew of the titanic obstacles to proving P≠NP on the other, and (may Merlin help me) cast a prediction accordingly.

Nevertheless, to deal with the "nastiness" issue, I've decided to clarify that _my $200,000 offer remains in effect until January 1, 2019_. That gives Deolalikar a couple more years to finish his current proof (plus more years for the journal refereeing and Clay prize processes), but it also makes clear that my bet is against a specific _claim_ to have proved P≠NP, not against a _person_ for all eternity.

(To answer the other question people kept asking me: no, my offer doesn't extend to _any_ potential P≠NP prover, much less to the other Clay Problems! I'm hopeful that, within my lifetime, theoretical computer science will have advanced to the point where statements like P≠NP _can_ be proved, and I'll of course be elated, but not _so_ catatonic as to make giving up my house seem completely immaterial by comparison.)

So: is it the duty of a scientist to express, in public and _as_ a scientist, only what he or she can articulate reasons for? Or is it sometimes appropriate or even desirable for scientists to go beyond what they can verbalize, using such mechanisms as bets? Now it's _your_ turn to weigh in! I'll be following the discussion by iPhone during a road trip through northern Israel, to the enormous annoyance of my traveling companions.

* * *

**Update (8/12):** I was hoping for some enlightening discussion about the ethics of scientific betting _in general_ , not more comments on the real or imagined motives behind my bet. However, the actual comments I woke up to have convinced me that the critics of my bet were right. In principle, the bet seemed like a good way to answer the flood of queries about Deolalikar's paper, and then get back to enjoying my trip. In practice, however, the way people respond to the bet depends entirely on what they think about my motives. If you don't care about my motives, or consider them benign, then the bet probably provided a useful piece of information or (if you already knew the information) a useful corrective to hype. If, on the other hand, you think I'm arrogant, a media whore, etc., then the bet served no purpose except to confirm your beliefs. Given the number of commenters on this blog who wish to ascribe the worst motives to me, it seems like the bet was counterproductive.PS. Arrogant I can see, but media whore? _Really?_ Is it relevant that curious, well-meaning folks were pestering me to react to this announcement, that they clearly wouldn't stop until I did, and that I was just trying to answer them while otherwise getting as little involved as I reasonably could?PPS. I've said this before, but let me say it again: I am **unbelievably grateful** to the "rapid response team" of mathematicians and computer scientists who dropped whatever else they were doing to delve into Deolalikar's paper, and to report what they found on Lipton's blog and elsewhere. Precisely because of their excellent work, there seemed to me to be little point in canceling my travel plans in order to try and duplicate their efforts.
