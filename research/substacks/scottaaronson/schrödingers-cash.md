---
title: "Schrödinger’s cash"
author: "Scott Aaronson"
date: "Thu, 15 Apr 2010"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=444"
---

There's an [article in this week's _New Scientist_](http://www.newscientist.com/article/mg20627562.700-schrodingers-cash-minting-quantum-money.html?full=true) by Justin Mullins about unforgeable quantum money. By the standards of "quantum mechanics journalism," the article is actually really good; I'd encourage you to read it if you want to know what's going on in this area. In particular, Mullins correctly emphasizes that the point of studying quantum money is to understand quantum mechanics better, not to mint practical QCash anytime soon (to do the latter, you'd first have to solve the minor problem of the money decohering within microseconds…).

My main quibble is just that I think the article overstates my own role! In my [Complexity'09 paper](http://www.scottaaronson.com/papers/noclone-ccc.pdf), the main thing I showed is that secure quantum money that anyone can verify is possible, _assuming_ the counterfeiters only have black-box access to the device for verifying the money. I also showed that, to get quantum money that anyone can verify, you have to make computational assumptions. (By contrast, [Stephen Wiesner's scheme](http://portal.acm.org/citation.cfm?id=1008920) from the 1960s, in which only the bank could verify the money, was information-theoretically secure.) But in terms of coming up with actual candidate quantum money schemes (as well as breaking those schemes!), the other members of the "quantum money club"--Andy Lutomirski, Avinatan Hassidim, David Gosset, Ed Farhi, Peter Shor--have been more active than me.

Two other quibbles:

(1) Mullins writes: "Then last year, Aaronson proposed a new approach that does away with the banknote and concentrates instead on the stream of information that represents quantum cash." In Wiesner's scheme, too, I think it was pretty clear that the "banknote with qubits stuck to it" was just a fun way to tell the story…

(2) The article does a good job of explaining the distinction between information-theoretic and computational security. But it doesn't stress that, with the latter, we can't actually _prove_ that any of the "hard problems" are hard, without also proving P≠NP! (I'll admit that the importance of this point is slightly hard to convey in a popular article, possibly because many people, or so I'm told, go about their lives without proving anything.) The best we can do is show that, _if_ you could solve this problem, then you could also solve this other problem that people have studied for a long time. But in the case of quantum money, we don't even know how to do _that_ --which is what we meant when we wrote in our [ICS paper](http://arxiv.org/abs/0912.3825) that "it seems possible that public key quantum money intrinsically requires a new mathematical leap of faith."

Considered as research topics in complexity theory, uncloneable quantum money, copy-protected quantum software, and so on are almost as wide-open today as public-key encryption was in the 1970s. That is, we don't have a compelling intuition as to whether these tasks are possible at all: all quantum mechanics does is open up the possibility of them, which wasn't there in the classical world. Unfortunately, in the case of quantum money, most of the ideas we've had for realizing the possibility have turned out to be insecure--often for non-obvious reasons. Assuming quantum money _is_ possible, we don't know what the right protocols are, what types of math to base them on, or how to argue for their security. So if you're not impressed by the results we have, why don't _you_ try your hand at this quantum money business? Maybe you'll have better luck than we did.

(_Addendum:_ I also have a [PowerPoint presentation](http://www.scottaaronson.com/talks/qmoney-uw.ppt) on quantum money, which ironically goes into more detail than my Complexity paper.)

  

