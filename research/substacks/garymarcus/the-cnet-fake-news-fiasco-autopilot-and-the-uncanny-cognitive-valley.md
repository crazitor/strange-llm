---
title: "The CNET Fake News Fiasco, Autopilot, and the Uncanny Cognitive Valley"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/the-cnet-fake-news-fiasco-autopilot"
---

[](https://futurism.com/cnet-ai-errors)

In the midst of World War II, the cognitive psychologist [Norman (“Mack”) Mackworth](https://en.wikipedia.org/wiki/Norman_Mackworth) made a fundamental discovery that is central to how any sensible person should think about artificial intelligence: humans, he discovered, were attentionally challenged; if you gave them a repetitive task, particularly one in which most of the time they don’t have to do anything, they will eventually tune out. His finding is so foundational to cognitive psychology, and especially the field of attention, that I learned about it as a teenager. Anyone who thinks about how AI is used should know about it—especially as we are about to head into an era of ubiquitous yet fallible AI. 

CNET’s editors learned[ this the hard way last week, when they published a bunch of machine-generated articles that turned out to be filled with subtle but important errors](https://gizmodo.com/cnet-ai-chatgpt-news-robot-1849996151), with [errors in 41 of the 77 articles the bot wrote](https://www.theverge.com/2023/1/25/23571082/cnet-ai-written-stories-errors-corrections-red-ventures), all missed by editors who weren’t paying enough attention. In Mackworth’s terminology, the editors’ _vigilance_ wasn’t high enough. 

Mackworth himself noticed that people had trouble with vigilance while studying radar operators. Operators would open their shift doing a great job looking for radar signals that were rare but important; but it wouldn’t take long, perhaps half an hour, before they stopped paying full attention. Mackworth [published some of his first results in 1948](https://psycnet.apa.org/record/1949-02102-001), under the title “The breakdown of vigilance during prolonged visual search.” The term “[vigilance](https://en.wikipedia.org/wiki/Vigilance_\(psychology\))” as Mackworth used it, and as cognitive psychologists today continue to use it, means paying close attention for long periods of time. As a later summary of Mackworth’s work and the hundreds of subsequent papers put it, “[Vigilance Requires Hard Mental Work and Is Stressful](https://www.researchgate.net/profile/Raja-Parasuraman/publication/23157806_Vigilance_Requires_Hard_Mental_Work_and_Is_Stressful/links/09e4150c09893c134f000000/Vigilance-Requires-Hard-Mental-Work-and-Is-Stressful.pdf?origin=publication_detail)”.[1](https://garymarcus.substack.com/p/the-cnet-fake-news-fiasco-autopilot#footnote-1-99439581) Which we humans usually tend to duck. 

Most people working on autonomous vehicles (and throughout the field of engineering known as [human factors](https://en.wikipedia.org/wiki/Human_factors_and_ergonomics)) recognize this fundamental truth, either because they know Mackworth’s work, or because they are aware of more recent work showing the same, or because they eventually discover it for themselves. 

Early in Google’s autonomous vehicle efforts, Google had tried to develop driver-assisted cars, in which AI did most of the work, but in which a human driver sat in front of the steering wheel, poised at all moments to take over. Google quickly learned that attention would eventually wander; humans in the loop couldn’t be trusted. 

One of its early driverless car pioneers [Chris Urmson](https://en.wikipedia.org/wiki/Chris_Urmson), gave [one of the first TED talks on autonomous vehicles](https://www.ted.com/talks/chris_urmson_how_a_driverless_car_sees_the_road), in 2015. Three minutes into his talk, Urmson told a profound story that pretty much every congressperson and citizen should be pondering, deeply, right about now:

> So back in 2013, we had the first test of a self-driving car where we let regular people use it. Well, almost regular -- they were 100 Googlers, but they weren't working on the project. And we gave them the car and we allowed them to use it in their daily lives. But unlike a real self-driving car, this one had a big asterisk with it: They had to pay attention, because this was an experimental vehicle. We tested it a lot, but it could still fail. And so we gave them two hours of training, we put them in the car, we let them use it, and what we heard back was something awesome, as someone trying to bring a product into the world. Every one of them told us they loved it…
> 
> So this was music to our ears, but then we started to look at what the people inside the car were doing, and this was eye-opening…
> 
> My favorite story is this gentleman who looks down at his phone and realizes the battery is low, so he turns around like this in the car [towards the back seat, no longer watching the traffic] and digs around in his backpack, pulls out his laptop, puts it on the seat, goes in the back again, digs around, pulls out the charging cable for his phone, futzes around, puts it into the laptop, puts it on the phone. Sure enough, the phone is charging. All the time he's been doing 65 miles per hour down the freeway.
> 
> Right? Unbelievable. So we thought about this and we said, it's kind of obvious, right? The better the technology gets, the less reliable the driver is going to get. 

[](https://substackcdn.com/image/fetch/$s_!p6mF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7e2850ad-9da5-46ce-82b7-ecaa7f7466d0_1487x960.jpeg)Driverless car pioneer Chris Urmson, then at Google, miming someone foolishly reaching backwards for his backpack, in a prototype autonomous vehicle

Google, to its credit, very quickly realized this was not a good thing. Indeed, a year before Urmson gave this TED Talk, I remember talking to Larry Page (then Google’s CEO) and he’d presumably already heard the same story. Page was convinced that human drivers could never be trusted to pay enough attention, and that anyone building cars on that premise was making a mistake. 

Page’s response was to ditch the steering wheel altogether; full autonomy or nothing. In April 2014, Google [unveiled its first steering wheel-free car](https://www.cnn.com/2014/05/28/tech/innovation/google-self-driving-car/index.html). If humans could never be trusted, the only way forward was to take the fallible human out of the loop altogether, even if the research would take a long time. The branch of Google (now Alphabet) that started working on full-human-out-of-the-loop autonomy is now called Waymo, and they have never looked back.

§

But not everyone has reached the same conclusion. Elon Musk has spent the last several years trying to build cars with _partial_ driver-assistance—which _does_ require humans to stay focused at all times. Mackworth’s Dictum suggests this is not necessarily the best idea.

In fact, to my knowledge only one paper in recent memory has really tried to argue that limitations in human vigilance would _not_ be a problem in autonomous vehicles, contra Mackworth’s Dictum. And here’s where things start to get curious.

The paper that I have in mind was called [The Human Side of Tesla Autopilot](https://teslamotorsclub.com/tmc/attachments/tesla-autopilot-human-side-pdf.394047); the now famous podcaster Lex Fridman, then a postdoc at MIT, was the lead author. The paper purported to show that Tesla drivers were able to “maintain a relatively high degree of functional vigilance.“ Elon Musk himself took an interest in it, [tweeting about it the day after it was announced](https://twitter.com/elonmusk/status/1114168824599842817?s=61&t=lBweqHplNntlGq1vHXdvog); Fridman discussed it in [his first interview with Musk](https://twitter.com/lexfridman/status/1116722843230834693?s=20&t=ZUTqKnPbMfmBhZT2CweCsA), a few days later.

And then, despite all that interest, the paper vanished. It was never published in a scientific journal, and never replicated; to my knowledge Fridman has published little if anything on driverless cars since. Fridman himself no longer even lists the paper on his list of publications—it’s gone altogether, as if it never existed. Even finding a PDF is difficult. The [website for the paper](https://deeplearning.mit.edu/human-side-of-tesla-autopilot/), which was supposed to have more information, is also gone—replaced by an autogenerated page that says “Coming Soon. This page is not available yet. Stay tuned”, nearly four years later. 

The lab where Fridman was at the time [doesn’t list it in their list of publications](https://agelab.mit.edu/publications/2019/), either. I reached out to three authors of the paper (including Fridman), alerting them to my concerns; none have responded to my inquiries. To me, all this reads as a paper that nobody is willing to stand behind. 

§

Fact is, “Mack” Mackworth was right: humans can’t pay attention 100% of the time. 

The same lab that seems to have pocket vetoed Fridman’s study [published another paper a year later in 2020—minus Fridman](https://dl.acm.org/doi/10.1145/3409120.3410644)—confirming exactly what Mackworth said all along: “As automation improves and failures become rarer, drivers may tend to forgo their monitoring role: be less attentive (more time eyes off-road) and relax direct control (hands off-wheel).” [People can’t pay attention forever.](https://dl.acm.org/doi/pdf/10.1145/3409120.3410644)

The vanished 2019 paper is not even mentioned. Instead, the first article in that 2020 paper’s literature review cites on the topic was called _Is partially automated driving a bad idea? Observations from an on-road study_. And the answer _that_ article gave is pretty clear:

> thematic analysis of video data suggests that drivers are not being properly supported in adhering to their new monitoring responsibilities and instead demonstrate behaviour indicative of complacency and over-trust. These attributes may encourage drivers to take more risks whilst out on the road.

§

Complacency and overtrust. That brings us back to ChatGPT, CNET, and the present. Mackworth was prescient. Automation is a double-edged sword, and there is a kind of uncanny valley. We know perfectly well not to trust lousy systems; and wouldn’t need to pay attention to truly reliable systems, but the closer they get to perfect, the easier it is for mere mortals to space out. The CNET editors probably took a quick look at the large-language model generated prose, and thought it looked good enough; “complacency and over-trust” to their own detriment. 

If the autogenerated articles had been riddled with spelling errors and grammatical errors, the editors might not have trusted them. But at a superficial level the essays looked good enough, and so they editors trusted them, and a bunch of false information slipped through. 

That’s going to happen a whole lot more this year, with synthetic articles. Too many people are starting to count on systems that [inherently can’t keep track of the truth](https://garymarcus.substack.com/p/is-chatgpt-really-a-code-red-for). Few people are likely ever to pay enough attention. 

The stakes may get even higher if people start to rely on immature AI—which is all we have got, so far—for [legal](https://www.npr.org/2023/01/25/1151435033/a-robot-was-scheduled-to-argue-in-court-then-came-the-jail-threats?utm_medium=email&utm_source=pocket_hits&utm_campaign=POCKET_HITS-EN-DAILY-SPONSORED&CALIBER-2023_01_29&sponsored=0&position=4&scheduled_corpus_item_id=65e37e1f-5a77-471e-bcd4-a45e22839b4a) or medical advice. 

We all need to be on our guard. 

_**[Gary Marcus](http://garymarcus.com) **(@garymarcus),**** scientist, bestselling author, and entrepreneur, is a skeptic about current AI but genuinely wants to see the best AI possible for the world—and still holds a tiny bit of optimism. Sign up to his Substack (free!), and [listen to him on Ezra Klein](https://www.nytimes.com/2023/01/06/opinion/ezra-klein-podcast-gary-marcus.html). His most recent book, co-authored with Ernest Davis,[ Rebooting AI](http://rebooting.ai/), is one of Forbes’s 7 Must Read Books in AI. _

[Share](https://garymarcus.substack.com/p/the-cnet-fake-news-fiasco-autopilot?utm_source=substack&utm_medium=email&utm_content=share&action=share)

[1](https://garymarcus.substack.com/p/the-cnet-fake-news-fiasco-autopilot#footnote-anchor-1-99439581)

For a lay introduction to the history of scientists efforts to attention, see Matt Richtel’s _[A Deadly Wandering: A Mystery, a Landmark Investigation, and the Astonishing Science of Attention in the Digital Age](https://www.harpercollins.com/products/a-deadly-wandering-matt-richtel?variant=32205934395426)._
