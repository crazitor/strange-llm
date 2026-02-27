---
title: "The Myth of the Ivory Tower"
author: "Scott Aaronson"
date: "Thu, 31 May 2007"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=239"
---

I know I [promised](https://scottaaronson.blog/?p=225) no more posts about D-Wave and its "commercial" "quantum" computer for a while. But will you look at the [bait](http://dwave.wordpress.com/2007/05/11/horizontal-wisdom-transfer/) that D-Wave founder Geordie Rose has been dangling in front of me on his blog?

> People tend to approach problems and form opinions through the lens of their expertise. This happens all the time when disciplines are close … but it also happens in wierder [sic] situations, where the area of expertise is entirely disjoint from the situation being analyzed -- like when theoretical computer scientists have opinions about real computers for example.

In Geordie's comments section, the message is clearer still. One commenter writes that "the Professors didn’t get there first and they are angry; all truth must first come from them." Another imagines "the Aaronsons of the world" fervently hoping that "their fragile self-created self-contained ecosystem can be re-built just the way they like it."

For commenters like these, it would seem that the issue has nothing to do with decoherence rates or scalability, or with what the evidence is that D-Wave is actually harnessing quantum effects to obtain a computational speedup. So in this post, I want to step back and try to understand what the real issue is.

I propose that more than a few technology enthusiasts -- not just the D-Wave supporters quoted above -- are in the thrall of _The Myth of the Ivory Tower_. According to this Myth, the basic function of academic scientists is to sit around in their armchairs, pompously declaring to be impossible what plucky inventors like Thomas Edison or the Wright Brothers then roll up their sleeves and do. Now, I might be an academic myself, but I'm also a proud American (currently residing in the [51st state](http://en.wikipedia.org/wiki/Canada)), and I won't deny that this most American of myths has a certain resonance even for me. In the end, though, I believe that the Myth tells us more about our Zeitgeist, or our collective psyche, or something like that, than it does about the actual history of technology.

The "evidence" for the Myth (when such is offered) usually consists of famous last words from distinguished scientific authorities. You know the sort of thing I'm talking about:

> Heavier-than-air flying machines are impossible.  
>  Radio has no future.  
>  X-rays will prove to be a hoax.  
>  -William Thomson (Lord Kelvin)
> 
> I think there is a world market for maybe five computers.  
>  -Thomas Watson
> 
> There is no reason anyone would want a computer in their home.  
>  -Ken Olsen

(Watson and Olsen were of course CEO's, but for the purposes of the Myth they stand in here as "academics.")

However, as soon as we think about these predictions and what they're supposed to demonstrate, we notice some glaring problems. The first one is confirmation bias. No one compiles lists of pessimistic technological forecasts made by experts that turned out to be _right_ -- where would you even start?

The second problem is that many of the juiciest predictions come from a single individual: [Lord Kelvin](http://en.wikipedia.org/wiki/Lord_Kelvin). Furthermore, they come from the twilight of his career, when he was considered to have lost his vortices even by most of his colleagues. Seeking to better understand this great physicist of the 19th century who was so wrong about the technologies of the 20th, I just read an excellent biography called [Degrees Kelvin](http://www.amazon.com/Degrees-Kelvin-Genius-Invention-Tragedy/dp/0309096189/ref=pd_bbs_sr_1/102-9634350-4564154?ie=UTF8&s=books&qid=1180576058&sr=8-1). One thing I learned is that, if the selective historians chose to focus on the _first_ half of Kelvin's career rather than the second, they could find equally exquisite anecdotes illustrating the _reliability_ of academic opinions.

In the laying of the first [transatlantic telegraph cable](http://en.wikipedia.org/wiki/Transatlantic_telegraph_cable) in the 1850's, there were two colorful personalities: Kelvin and [Wildman Whitehouse](http://en.wikipedia.org/wiki/Wildman_Whitehouse). Whitehouse, the "practical" man, detested any math or physics he couldn't understand, and insisted that a transatlantic cable would just be a longer version of existing cables. Kelvin, the "theorist," said that while a transatlantic cable was certainly _possible_ , it would need thicker insulation, a different kind of receiver, etc. than previous cables to work reliably, and that more testing and research was needed. As it happened, after laying a cable that was every bit as unreliable as Kelvin said it would be, Whitehouse (1) had to use Kelvin's receiver to get any signal through at all, (2) faked the transcripts to make it look like he used his own receiver, (3) fatally damaged the cable by sending 2,000 volts through it in a desperate attempt to get it to work properly, and then (4) insisted the cable was still fine after it had permanently gone silent. Eventually the cable companies learned their lesson.

Despite this and other successes (e.g., the Second Law of Thermodynamics), Kelvin's doofus predictions in later life do illustrate two important points. The first is that, if you're going to make skeptical pronouncements, you'd better distinguish clearly between the _provably_ impossible, the _presumably_ impossible, and the merely _difficult and not yet achieved_. The second is that, if you're going to claim something's impossible, you'd better have an _argument_ , and you'd better understand what assumptions it rests on.

Alright, so let's move on to Watson and Olsen's predictions about the computer industry. The funny thing is, these predictions weren't nearly as stupid as they sound! Why? Because there's nothing inevitable about the concept of a _personal_ computer. Instead of billions of home PC's, we could just as easily imagine most of the world's computing power concentrated in a few servers, accessible remotely to anyone who wanted it. In this alternate universe, your desktop PC would be little more than a glorified information portal -- a "browser," if you will -- while most of the actual application software (email, calendars, maps, etc.) ran elsewhere. I admit that this is just a fanciful, hypothetical scenario, but what does that matter to a theorist like me?

Speaking of which, the Internet was of course the child of DARPA and NSF, raised to adolescence in university CS departments. (DARPA has since reoriented itself toward projects with shorter-term payoff, its previous funding model having failed so disastrously.) The Web was created by Tim Berners-Lee at CERN, and the first popular web browser by Marc Andreessen at the University of Illinois. (And yes, Al Gore had a [nontrivial role](http://en.wikipedia.org/wiki/Al_gore#Internet_and_technology) in funding this work.) R, S, and A were all at MIT. If you're going to argue for the irrelevance of academic research, the Internet is not the place to start.

But what about some of the other spectacular inventions of the last fifty years: the laser, the transistor, the fiber-optic cable, the communications satellite? Didn't _those_ come from the private sector? As it happens, they came from Bell Labs, which is interesting as the sort of mammoth exception that proves the rule. Because of AT&T's government-sanctioned monopoly, for much of the 20th century Bell Labs was able to function like the world's largest university, devoting billions of dollars to "irrelevant" research. So in the 1980's, when Congress decided to deregulate the phone system, many people predicted that Bell Labs would die a slow, agonizing death -- a prediction that's been borne out over the last 25 years.

But surely other companies must have picked up the slack? No, not really. While Microsoft, IBM, NEC, Xerox, and a few others all provide welcome support for basic research, none of them do so on the old Ma Bell's scale. From a CEO's perspective, the problem with basic research is obvious: a rising tide lifts all boats, your competitors' as well as yours. (The famous cautionary example here is Xerox PARC, which made the "mistake" of giving the world the windowing system, the mouse, and the laser printer.)

For those who adhere to the religion of capitalism, have the [Arrow-Debreu Theorem](http://en.wikipedia.org/wiki/Arrow-Debreu_model) tattoed across their chests, etc., it might be difficult to understand how a system based on peer review rather than the free market could lead so consistently to technological breakthroughs. I mean, all those ivory-tower academics growing fat off government grants: what incentive could they possibly have to get the right answers? Without picky customers or venture capitalists breathing down their necks, what's the penalty for being wrong?

I'm lucky enough to be friends with [Robin Hanson](http://hanson.gmu.edu/), a brilliant economist and futurist who starts where Ayn Rand would've suffered a loss of nerve and keeps going from there. Robin has [long argued](http://hanson.gmu.edu/gamble.html) that the scientific peer review process is broken, and ought to be supplanted by a futures market that would reward scientists for making correct predictions. As he writes:

> The pace of scientific progress may be hindered by the tendency of our academic institutions to reward being popular, rather than being right … Academia is still largely a medieval guild, with a few powerful elites, many slave-like apprentices, and members who hold a monopoly on the research patronage of princes and the teaching of their sons …
> 
> Imagine that academics are expected to "put up or shut up" and accompany claims with at least token bets, and that statistics are collected on how well people do. Imagine that funding agencies subsidize pools on questions of interest to them, and that research labs pay for much of their research with winnings from previous pools. And imagine that anyone could play, either to take a stand on an important issue, or to insure against technological risk.

Personally, I hope that Robin's science futures market gets tried on a significant scale, and I can't wait to see the results. (Naturally, even the marketplace of ideas has to compete in the marketplace of ideas!) I agree with Robin that academic science is often [tradition-bound to the point of absurdity](http://www.scottaaronson.com/writings/journal.html), and that its institutions ought to be as open to scrutiny and replacement as its theories. But I don't go as far as he apparently does in the direction of the Myth of the Ivory Tower. For me, the interesting thing about science is not that it's broken, but rather that it's about the _least_ broken enterprise in the whole sorry history of our species.
