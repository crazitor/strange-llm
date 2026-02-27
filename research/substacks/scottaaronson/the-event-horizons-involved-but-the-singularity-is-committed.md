---
title: "The event horizon’s involved, but the singularity is committed"
author: "Scott Aaronson"
date: "Thu, 22 Mar 2007"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=213"
---

Lenny Susskind -- the Stanford string theorist who _Shtetl-Optimized_ readers will remember from [this](https://scottaaronson.blog/?p=181) entry -- is currently visiting Perimeter Institute to give a [fascinating series of lectures](http://www.perimeterinstitute.ca/images/pifiles/l_susskind_minicourse_pi.pdf) on "Black Holes and Holography."

After this morning's lecture (yes, I'm actually getting up at 10am for them), the following question occurred to me: _what 's the connection between a black hole having an event horizon and its having a singularity?_ In other words, once you've clumped enough stuff together that light can't escape, why have you _also_ clumped enough together to create a singularity? I _know_ there's a physics answer; what I'm looking for is a conceptual answer.

Of course, one direction of the correspondence -- that you can't have a singularity without also having an event horizon -- is the famous [Cosmic Censorship Hypothesis](http://en.wikipedia.org/wiki/Cosmic_censorship) popularized by Hawking. But what about the other direction?

When I posed this question at lunch, Daniel Gottesman patiently explained to me that singularities and event horizons just sort of go together, "like bacon and eggs." However, this answer was unsatisfying to me for several reasons -- one of them being that, with my [limited bacon experience](http://dabacon.org/pontiff/), I don't _know_ why bacon and eggs go together. (I _have_ eaten eggs with turkey bacon, but I wouldn't describe their combined goodness as greater than the sum of their individual goodnesses.)

So then Daniel gave me a second answer, which, by the time it lodged in my brain, had morphed itself into the following. By definition, an event horizon is a surface that twists the causal structure in its interior, so that none of the geodesics (paths taken by light rays) lead outside the horizon. But geodesics can't just _stop_ : assuming there are no closed timelike curves, they have to either keep going forever or else terminate at a singularity. In particular, if you take a causal structure that "wants" to send geodesics off to infinity, and shoehorn it into a finite box (as you do when creating a black hole), the causal structure gets _very, very angry_ -- so much so that it has to "vent its anger" somewhere by forming a singularity!

Of course this can't be the full explanation, since why can't the geodesics just circle around forever? But if it's even _slightly_ correct, then it makes me much happier. The reason is that it reminds me of things I already know, like the [hairy ball theorem ](http://en.wikipedia.org/wiki/Hairy_ball_theorem)(there must be a spot on the Earth's surface where the wind isn't blowing), or [Cauchy's integral theorem](http://en.wikipedia.org/wiki/Cauchy_integral_theorem) (if the integral around a closed curve in the complex plane is nonzero, then there must be a singularity in the middle), or even the [Nash equilibrium theorem](http://en.wikipedia.org/wiki/Nash_equilibrium). In each of these cases, you take a geometric structure with some global property, and then deduce that having that property makes the structure "angry," so that it needs a special point (a singularity, an equilibrium, or whatever) to blow off some steam.

So, question for the relativistas: is there a theorem in GR anything like my beautiful story, or am I just [talking out of my ass](https://scottaaronson.blog/?p=119) as usual?

**Update (3/22):** Well, it turns out that I was ignorantly groping toward the famous [Penrose-Hawking singularity theorems](http://en.wikipedia.org/wiki/Penrose-Hawking_singularity_theorems). Thanks to Dave Bacon, Sean Carroll, and ambitwistor for immediately pointing this out.
