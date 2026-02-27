---
title: "Pooled testing for covid: Guest post by Zeph Landau"
author: "Scott Aaronson"
date: "Thu, 04 Jun 2020"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=4834"
---

**Scott 's foreword:** [Zeph Landau](https://people.eecs.berkeley.edu/~landau/), a noted quantum computing theorist at UC Berkeley who's worked closely with my adviser Umesh Vazirani, recently asked me if he could write a guest post about [pooled testing](https://en.wikipedia.org/wiki/Group_testing) for covid--an old idea that, Zeph argues, could play a crucial role in letting universities safely reopen this fall. Seeing a small chance to do a great good, I readily agreed.

I should confess that I'm more … fatalistic than Zeph. Not that I'm proud of it: I think that Zeph's attitude is superior to mine. But, like, I'm a theoretical computer scientist with zero expertise in medical testing or statistics, and _I_ knew about pooled testing and its WWII origins--so imagine how thoroughly the actual experts must know the idea. Just like they know all about variolation, and challenge trials, and copper fixtures, and UV light, and vitamin D supplements, and a dozen other possible tools against covid that future historians might ask why we didn't try more.

As I've written before, I think our fundamental problem is not a lack of good ideas. It's that, outside of some isolated pockets of progress, our entire civilization no longer has the will (or ability? is there a difference?) to _implement_ good ideas, or even really to try them. For anything new that requires coordination, today there are just too many stakeholders who need to be brought on board, too many risks that need further study. So I see Zeph, and anyone like him, as occupying a tragic position, a bit like that of an Aztec advocating the use of the wheel. "Sure," the Aztec elders might calmly reply, "wheeled transport is obvious enough that we've _all_ considered it, but a moment's thought reveals why, in our actually existing empire, it would be reckless, costly, and of at most marginal benefit…"

But I hope I'm wrong! Better, I hope this post is the one that _proves_ me wrong! So without further ado, here's…

**Zeph Landau 's Guest Post**

This post describes how every university could efficiently use modest testing resources to sensibly and extensively reduce the number of COVID-19 cases on their campus this fall.  It is meant as a call to action to the reader--because without a concerted effort to get the right people the necessary information and take immediate consequential action, a far worse alternative will be implemented almost everywhere. It is my sincere hope, that immediately after reading this post, you will take the following steps:

1) Figure out who is part of the reopening committee at your institution.

2) Find the right people and engage with them either as a fellow faculty member or, better yet, through a connection to get them good information about the information posted here.

3) Then stay engaged and keep pushing. (See below for links to sample documents.)

OK, here we go.

**The Problem**

How can we safely open a university or college campus such that we ensure that the number of cases does not drastically increase through the newfound interactions between the population?

One obvious, albeit impractical, solution to opening universities is to test everyone, everyday and isolate those that test positive quickly. Unfortunately, we can't do that due to costs ($100 per student per day) and availability of tests (on the order of 1000 tests per day at university testing labs).

_Turns out there is a solution that uses drastically fewer tests and is commensurate in detecting an outbreak. It is called pooled screening which is a variant of pooled testing._

**The missing piece: early detection surveillance**

So how do we detect most contagious people quickly if we don't have the resources to test everyone regularly?  The answer is by pooled testing--or to be more accurate (I'll be clear about why this distinction is important later) **pooled screening.** The idea of pooling is old (attributed to Dorfman in the 40's), simple, and has been used over and over in all kinds of scenarios. Pooled testing works by mixing samples together from a group and then administering a single test to the mixture. The test is designed to be sensitive enough to come up positive whenever _at least one_ underlying sample is positive. Instead of testing each sample individually, you test the mixture, and then only those groups that test positive undergo a second round of testing of each individual sample. The individuals do not need to deliver a second sample; there is more than enough biological material for multiple tests per sample. When prevalence of a disease is low, most pools come up negative and you save a large amount of testing resources and time.  (For those more visually inclined, here is a one minute [video](https://www.youtube.com/watch?v=pdC6irz_vys&feature=youtu.be) on pooled testing.)

So what would a good early detection surveillance system look like?  Here is a reasonable and doable framework:

  * Divide the campus population into three groups (call them A, B, and C).
  * Collect samples from each group twice a week, (e.g. Group A: M/Th, Group B: Tu/Fri, Group C Wed/Sat).
  * Pool test the samples in groups of 16.



What kinds of resources would this use?

  * For a 10,000 person campus, you'd need about 200 tests per day, 6 days a week.  The universities that have implemented testing labs typically have the capacity to do on the order of 1000 tests a day.
  * Assuming a rough cost of $100 a test (which should be an overestimate if they are using their own lab), it would amount to a $12 a student/ per week.  



What would it accomplish?  It would quickly find outbreaks and new cases.  Under a few different assumptions of the time-course of the viral load in a person, _the expected time for detecting an infectious person in this scheme is under 3 days._ Those cases would then need to be fed into an existing contact tracing and quarantine protocol.  The result: an outbreak suppressed before it had a chance to get going.

So why aren’t we already doing this?  Read on…

**The fear of false negatives in pooling**

The general concern to implementing pooling  for Covid-19 in the US is two-fold. 

  1. Without the creation of a better test the dilution effect will make the test less sensitive and in turn produce more false negatives.  
  2. Even if you could solve the scientific sensitivity issue, navigating the process of getting government approval is a big barrier.



Let’s take each of these concerns in turn.  The first is definitely a concern if the goal is 1:1 medical testing.  If a sample can be barely seen as positive in an individual test, then the risk is that the dilution effect when pooled with others will cause the group test to come out negative--giving a wrong result to the positive individual.  The word for this is “sensitivity”, i.e. if a test has 95% sensitivity it means that it’ll be accurate 95% of the time and produce a false negative 5% of the time.  So how sensitive would a pooled test be where you combined 16 individual samples into 1 and just ran it through an existing 1:1 test?  Lab data suggests it would have at least 70% sensitivity.  For 1:1 testing this is a non-starter, however, **the goal is early detection** of an outbreak, which is different and as we shall see, a 70% sensitivity does fine for this purpose.

Suppose you are doing early detection surveillance and imagine that an outbreak starts.  Imagine 3 people are infected.  Because you are sampling every 3 days, you’ll be getting at least 6 positive samples, and the chances that your 70% screen misses all 6 is tiny.  As soon as it catches one, a contact tracing protocol is initiated and the others will be found.

Another way to formulate what is going on is that you are trading sensitivity for speed (in the form of capacity and cost)--and that is a huge win.  The pooling and more frequent testing gives you that speed versus sensitivity tradeoff.  Sure, Lebron James (a 70% free-throw shooter) won’t make every free throw, but the chance that he misses 6 in a row is tiny.

For some, the above thinking is straightforward.  However, for the medical testing paradigm--where the goal is the most accurate test for an individual using the one sample you have--this point of view is foreign and in many ways almost out of reach.   

OK.  So with the concern of sensitivity laid to rest, what about the second concern?  That the regulations will get in the way.  It turns out that this isn’t an issue though again, it is slightly counterintuitive for those who work in medical testing.  The task is surveillance, and therefore the pooling test is being used as a screen (not a medical test): negative group tests are not reported to the individual as a negative test result.   Positive groups are deconvoluted for individual testing and results returned to the person who is positive individually.  HHS/CLIA has indicated there aren't regulatory restrictions as long as you don't return test results due to the pooled test.

It is important to re-emphasize that the above is for pooled screening (where negative results are not returned), which is in contrast to pooled testing (where negative pools are reported as negative test results for each individual).  For pooled testing, which has received a jump of coverage due to its use recently in Wuhan, there are large regulatory hurdles--the CDC is just formulating criteria for clearing those hurdles and the science looks like, for now, that most labs wouldn’t be able to get above pools of size 5 or so.

**How do you safely collect so many samples?**

A different direction of concern for early detection surveillance is the logistics and feasibility around collecting samples.  To date, the gold standard for sampling is a deep nasal swab that requires a professional to do it, requires PPE equipment, and is not a pleasant experience.  Using this method wouldn’t work logistically on campus.

However, there are other sampling techniques that allow people to self-sample, both in the form of a shallow nasal swab and saliva based techniques.  The stated concern is obvious: there is a worry that these sampling techniques are less sensitive.  There is some evidence that this is not the case (and even the opposite) but regardless, as has been discussed-- in early detection surveillance it is OK to take a hit on sensitivity.  The system remains robust because of the frequent testing and the goal of detecting an outbreak, not every individual.

Being able to self-sample removes a huge bottleneck.  The picture is very much simplified.  Students/faculty/staff self-sample on their prescribed days (either in the presence of a medical professional or not depending on the approved protocol) and then drop off their sample at any of various drop-off stations on campus.  Those stations deliver the samples to the testing facility for pooling and testing.

**You can help to get this done**

Is what I’m describing a new idea?  As far as I can tell, the answer is both no and yes.  Pooled testing is in the news both as a theoretical idea and now as being implemented at some scale--in Israel, in a lab in Nebraska, and most recently in Wuhan.   But using pooling as a screen (not a medical test) within an early detection surveillance system that repeatedly screens everyone is, as far as I know, not in the discussion.

What seems clear is that right now--reopening committees and labs are perhaps aware of the idea of pooling but only as a theoretical idea of a technology that might be coming at some vague time in the future.  They are unaware that in the form of early detection surveillance, it is right in front of them ready to go.  They’d need a matter of weeks to convert a 1:1 lab into a lab that could handle both pooled screening and 1:1 testing (this [lab](https://www.medrxiv.org/content/10.1101/2020.04.17.20069062v2) did it, [here](https://docs.google.com/document/d/1FVp55JAs2heqV5ktyGVVdoE-W_XTKmZgCWBy1SEoo-o/edit?usp=sharing) is a brief outline of the steps).  In the same timeline, they could develop a system for handling the logistics of sampling large numbers of people.

**And that is where each of you come in … **  you can help get these ideas to the right people.  It needs to be done quickly because decisions are being made now as to what to do.  The right people are your colleagues--you just have to find out who they are and reach out to them personally.  You can find out who is on the reopening committee, you can track down faculty members in public health and microbiology. They are often busy and might be skeptical of what an outsider can offer, but keep trying because my experience has been that if you keep at it and follow up, they will listen and be grateful for the information.

Here is a [sample letter](https://docs.google.com/document/d/1QZHWZUxrMGzYKycZNpsfuJBCqRphGBzMQf4-ws76YrI/edit?usp=sharing) you could use.

Here is a crowdsourced [spreadsheet](https://docs.google.com/spreadsheets/d/15zXZsGh6W2hoejgp4_wgTQzDPp-qHBrvYYcgOoaitZ4/edit?usp=sharing) for potential contact people at various universities.  If your university isn’t yet there, we ask that you enter the info that you find for your university in this [form](https://forms.gle/7v13r2qfYiGoVRUM7) which is linked to the above spreadsheet (or enter it directly into the spreadsheet).

If you want to know more or would like to craft your own letter, here are some relevant links:

[Covid-19 early detection surveillance on a 240 person facility using 5 tests a day](https://docs.google.com/document/d/1qdOkIVle8fQtDjQB-EZA_OdMrCbeeAiljhhHRFc05jE/edit?usp=sharing)

[Covid-19 early detection surveillance for a campus of 24,000 using 500 tests a day](https://docs.google.com/document/d/16fQ91xkL2Evpi7kEYl5FvSM4EAIWf5Lq9unmD1XJQsY/edit?usp=sharing)

And here is a [simple analysis of the mean time between contagion](https://docs.google.com/document/d/1ZHwHGZMGFzqqj6up-9dRda__pzttSwy7B8fx5wBk5cg/edit?usp=sharing) and detection that an early detection scheme could accomplish.

If anyone wants to follow up with me, I’m happy to do so.  You can reach me at:  zeph dot landau at gmail dot com 

Thanks.

Zeph Landau  
Dept. of Computer Science  
University of California, Berkeley
