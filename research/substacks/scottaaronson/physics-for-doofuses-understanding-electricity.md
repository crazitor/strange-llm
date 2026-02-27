---
title: "Physics for Doofuses: Understanding Electricity"
author: "Scott Aaronson"
date: "Sun, 15 Apr 2007"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=220"
---

Welcome to an occasional new _Shtetl-Optimized_ series, where physicists get to amuse themselves by watching me struggle to understand the most basic concepts of their discipline. I'll consider my post on [black hole singularities](https://scottaaronson.blog/?p=213) to be retroactively part of this series.

Official motto: _" Because if I talked about complexity, you wouldn't understand it."_

Unofficial motto: _" Because if I talked about climate change, I'd start another flamewar -- and as much as I want to save civilization, I want even more for everyone to like me."_

Today's topic is **Understanding Electricity**. First of all, what makes electricity confusing? Well, besides electricity's evil twin magnetism (which we'll get to another time), what makes it confusing is that there are six things to keep track of: [charge](http://en.wikipedia.org/wiki/Charge_%28physics%29), [current](http://en.wikipedia.org/wiki/Electric_current), [energy](http://en.wikipedia.org/wiki/Energy), [power](http://en.wikipedia.org/wiki/Power_%28physics%29), [voltage](http://en.wikipedia.org/wiki/Voltage), and [resistance](http://en.wikipedia.org/wiki/Electrical_resistance), which are measured respectively in coulombs, amps, joules, watts, volts, and ohms. And I mean, sure you can memorize formulas for these things, but what _are_ they, in terms of actual electrons flowing through a wire?

Alright, let's take 'em one by one.

**Charge** is the q in kqq/r2. Twice as many electrons, twice as much charge. 'Nuff said.

**Current** is charge per unit time. It's how many electrons are flowing through a cross-section of the wire every second. If you've got 100 amps coming out, you can send 50 this way and 50 that way, or π this way and 100-π that way, etc.

**Energy** … Alright, even _I_ know this one. Energy is what we fight wars to liberate. In our case, if you have a bunch of electrons going through a wire, then the energy scales like the number of electrons times the speed of the electrons squared.

**Power** is energy per unit time: how much energy does your appliance consume every second? Duh, that's why a 60-watt light bulb is environmentally-friendlier than a 100-watt bulb.

**Voltage** is the first one I had trouble with back in freshman physics. It's energy per charge, or power per current. Intuitively, voltage measures how much energy gets imparted to each individual electron. Thus, if you have a 110-volt hairdryer and you plug it into a 220-volt outlet, then the trouble is that the electrons have twice as much energy as the hairdryer expects. This is what _transformers_ are for: to ramp voltages up and down.

Incidentally, the ability to transform voltages is related to why what comes out of your socket is _alternating current_ (AC) instead of _direct current_ (DC). AC, of course, is the kind where the electrons switch direction 60 times or so per second, while DC is the kind where they always flow in the same direction. For computers and other electronics, you clearly want DC, since logic gates are unidirectional. And indeed, the earliest power plants did transmit DC. In the 1890's, [Thomas Edison](http://en.wikipedia.org/wiki/Thomas_edison) [fought vigorously](http://en.wikipedia.org/wiki/War_of_Currents) against the adoption of AC, going so far as to electrocute dogs, horses, and even an elephant using AC in order to "prove" that it was unsafe. (These demonstrations proved about as much as D-Wave's quantum computer -- since needless to say, one can _also_ electrocute elephants using DC. To draw any conclusions a comparative study is needed.)

So why did AC win? Because it turns out that it's not practical to transmit DC over distances of more than about a mile. The reason is this: the longer the wire, the more power gets lost along the way. On the other hand, the higher the voltage, the _less_ power gets lost along the way. This means that if you want to send power over a long wire and have a reasonable amount of it reach its destination, then you want to transmit at high voltages. But high voltages are no good for household appliances, for safety and other reasons. So once the power gets close to its destination, you want to convert back down to lower voltages.

Now, the simplest way to convert high voltages to low ones was discovered by [Michael Faraday](http://en.wikipedia.org/wiki/Michael_Faraday), and relies on the [principle of electromagnetic induction](http://en.wikipedia.org/wiki/Electromagnetic_induction). This is the principle according to which a changing electric current creates a changing magnetic field, which can in turn be used to drive another current. (Damn, I knew we wouldn't get far without bumping into electricity's evil and confusing magnetwin.) And that gives us a simple way to convert one voltage to another -- analogous to using a small, quickly-rotating gear to drive a big, slowly-rotating gear.

So to make a long story short: while _in principle_ it's possible to convert voltages with DC, it's more practical to do it with AC. And if you don't convert voltages, then you can only transmit power for about a mile -- meaning that you'd have to build millions of tiny power plants, unless you only cared about urban centers like New York.

**Resistance** is the trickiest of the six concepts. Basically, resistance is the thing you need to cut in half, if you want to send twice as much current through a wire at the same voltage. If you have two appliances hooked up serially, the total resistance is the sum of the individual resistances: Rtot = R1 \+ R2. On the other hand, if you have two appliances hooked up in parallel, the reciprocal of the total resistance is the sum of the reciprocals of the individual resistances: 1/Rtot = 1/R1 \+ 1/R2. If you're like me, you'll immediately ask: _why_ should resistance obey these identities? Or to put it differently, why should the thing that obeys one or both of these identities be _resistance_ , defined as voltage divided by current?

Well, as it turns out, the identities _don 't_ always hold. That they do in most cases of interest is just an empirical fact, called [Ohm's Law](http://en.wikipedia.org/wiki/Ohm%27s_law). I suspect that much confusion could be eliminated in freshman physics classes, were it made clear that there's nothing obvious about this "Law": a new physical assumption is being introduced. (Challenge for commenters: can you give me a handwaving argument for _why_ Ohm's Law should hold? The rule is that your argument has to be grounded in terms of what the actual electrons in a wire are doing.)

Here are some useful formulas that follow from the above discussion:

Power = Voltage2/Resistance = Current2 x Resistance = Voltage x Current  
Voltage = Power/Current = Current x Resistance = √(Power x Resistance)  
Resistance = Voltage/Current = Power/Current2 = Voltage2/Power  
Current = Power/Voltage = Voltage/Resistance = √(Power/Resistance)

Understand? Really? [Take the test!](http://www.southernct.edu/~bidarian/phy1xx-chap23.htm)

**Update (4/16):** Chad Orzel [answers my question](http://scienceblogs.com/principles/2007/04/basic_concepts_ohms_law.php) about Ohm's Law.
