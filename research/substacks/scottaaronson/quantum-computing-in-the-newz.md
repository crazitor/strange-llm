---
title: "Quantum computing in the newz"
author: "Scott Aaronson"
date: "Tue, 09 Oct 2012"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=1136"
---

**Update (10/10).** In case anyone is interested, here's a [comment](http://blogs.discovermagazine.com/cosmicvariance/2012/10/09/nobel-prize-to-haroche-and-wineland/#comment-269371) I posted over at Cosmic Variance, responding to a question about the relevance of Haroche and Wineland's work for the interpretation of quantum mechanics.

> The experiments of Haroche and Wineland, phenomenal as they are, have zero implications one way or the other for the MWI/Copenhagen debate (nor, for that matter, for third-party candidates like Bohm  ). In other words, while doing these experiments is a tremendous challenge requiring lots of new ideas, no sane proponent of  _any_ interpretation would have made predictions for their outcomes other than the ones that were observed. To do an experiment about which the proponents of different interpretations might  _conceivably_ diverge, it would be necessary to try to demonstrate quantum interference in a much,  _much_ larger system — for example, a brain or an artificially-intelligent quantum computer. And even then, the different interpretations arguably don’t make differing predictions about what the published  _results_ of such an experiment would be. If they differ at all, it’s in what they claim, or refuse to claim, about the experiences of the  _subject_ of the experiment, while the experiment is underway. But if quantum mechanics is right, then the subject would necessarily have  _forgotten_ those experiences by the end of the experiment — since otherwise, no interference could be observed!
> 
> So, yeah, barring any change to the framework of quantum mechanics itself, it seems likely that people will be arguing about its interpretation forever. Sorry about that. 

* * *

_Where**is** he? So many wild claims being leveled, so many opportunities to set the record straight, and yet he completely fails to respond. Where's the passion he showed just four years ago? Doesn't he realize that having the facts on his side isn't enough, has never been enough? It's as if his mind is off somewhere else, or as if he's tired of his role as a public communicator and no longer feels like performing it. Is his silence part of some devious master plan? Is he simply suffering from a lack of oxygen in the brain? What's going on?_

Yeah, yeah, I know. I should blog more. I'll have more coming soon, but for now, two big announcements related to quantum computing.

Today the [2012 Nobel Prize in Physics](http://www.nobelprize.org/nobel_prizes/physics/laureates/2012/) was awarded jointly to Serge Haroche and David Wineland, for _" for ground-breaking experimental methods that enable measuring and manipulation of individual quantum systems."_ I'm not very familiar with Haroche's work, but I've known of Wineland for a long time as possibly the top quantum computing experimentalist in the business, setting one record after another in trapped-ion experiments. In awarding this prize, the Swedes have recognized the phenomenal advances in atomic, molecular, and optical physics that have _already happened_ over the last two decades, largely motivated by the goal of building a scalable quantum computer (along with other, not entirely unrelated goals, like more accurate atomic clocks). In so doing, they've given what's arguably the first-ever "Nobel Prize for quantum computing research," without violating their policy to reward only work that's been directly confirmed by experiment. Huge congratulations to Haroche and Wineland!!

In other quantum computing developments: yes, I'm aware of the [latest news from D-Wave](http://www.technologyreview.com/news/429429/the-cia-and-jeff-bezos-bet-on-quantum-computing/), which includes millions of dollars in new funding from Jeff Bezos (the founder of [Amazon.com](http://www.amazon.com), recipients of a large fraction of my salary). Despite having officially [retired](https://scottaaronson.blog/?p=639) as Chief D-Wave Skeptic, I posted a [comment](http://www.technologyreview.com/news/429429/the-cia-and-jeff-bezos-bet-on-quantum-computing/#comments) on Tom Simonite's article in _MIT Technology Review_ , and also sent the following email to a journalist.

> I'm probably not a good person to comment on the "business" aspects of D-Wave. They've been extremely successful raising money in the past, so it's not surprising to me that they continue to be successful. For me, three crucial points to keep in mind are:
> 
> (1) D-Wave still hasn't demonstrated 2-qubit entanglement, which I see as one of the non-negotiable "sanity checks" for scalable quantum computing. In other words: if you're producing entanglement, then you might or might not be getting quantum speedups, but if you're not producing entanglement, then our current understanding fails to explain how you could _possibly_ be getting quantum speedups.
> 
> (2) Unfortunately, the fact that D-Wave's machine solves some particular problem in some amount of time, and a specific classical computer running (say) simulated annealing took more time, is not (by itself) good evidence that D-Wave was achieving the speedup _because_ of quantum effects. Keep in mind that D-Wave has now spent ~$100 million and ~10 years of effort on a highly-optimized, special-purpose computer for solving one specific optimization problem. So, as I like to put it, quantum effects could be playing the role of "the stone in a stone soup": attracting interest, investment, talented people, etc. to build a device that performs quite well at its specialized task, but not ultimately _because_ of quantum coherence in that device.
> 
> (3) The quantum algorithm on which D-Wave's business model is based -- namely, the quantum adiabatic algorithm -- has the property that it "degrades gracefully" to classical simulated annealing when the decoherence rate goes up. This, fundamentally, is the thing that makes it difficult to know what role, if any, quantum coherence is playing in the performance of their device. If they were trying to use Shor's algorithm to factor numbers, the situation would be much more clear-cut: a decoherent version of Shor's algorithm just gives you random garbage. But a decoherent version of the adiabatic algorithm still gives you a pretty good (but now essentially "classical") algorithm, and that's what makes it hard to understand what's going on here.
> 
> As I've said before, I no longer feel like playing an adversarial role. I really, genuinely hope D-Wave succeeds. But the burden is on them to demonstrate that their device uses quantum effects to obtain a speedup, and they still haven't met that burden. When and if the situation changes, I'll be happy to say so. Until then, though, I seem to have the unenviable task of repeating the same observation over and over, for 6+ years, and confirming that, no, the latest sale, VC round, announcement of another "application" (which, once again, might or might not exploit quantum effects), etc., hasn't changed the truth of that observation.
> 
> Best,  
>  Scott
