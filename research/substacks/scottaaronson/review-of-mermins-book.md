---
title: "Review of Mermin’s book"
author: "Scott Aaronson"
date: "Mon, 10 Dec 2007"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=296"
---

By now, maybe a half-dozen people have asked me what I thought of David Mermin's new book [Quantum Computer Science: An Introduction](http://www.amazon.com/Quantum-Computer-Science-David-Mermin/dp/0521876583/ref=pd_bbs_sr_1?ie=UTF8&s=books&qid=1197297341&sr=8-1); many seemed surprised when I told them I hadn't read it. Since I aim to please, I finally cracked open my review copy on a train this weekend, and am pleased to report that … yes, it's quite good. Indeed, the biggest problem is just Mermin's infamous insistence on spelling qubit "Qbit." (At this point, one might as well decide to spell quark "Qork." A language consists of shared, often highly-irrational conventions that cannot be changed unilaterally.)

Mermin's book is, one might say, radically limited in scope. There's nothing about physical implementation, not a mixed state or POVM in sight, not a word on the provable limitations of quantum computers, no mention of P, NP, or BQP, and pretty much nothing about any development after 1995. The sole aim is to cover the "quantum canon" -- Hadamards and Toffolis, Shor and Grover, quantum error-correction, the BB84 key distribution protocol, etc. -- while dispelling various misconceptions along the way. But at that limited task, Mermin -- who's an extremely gifted expositor -- does a better job than almost anyone.

He certainly does a better job than _I_ would have. I'll admit that, when the [Mike&Ike book](http://www.amazon.com/gp/product/0521635039/ref=cm_cr_pr_product_top) came out seven years ago, I naïvely imagined that the "quantum textbook problem" (or more precisely, the _good_ quantum textbook problem) had been solved. From now on, there would be a single place where everyone could go to learn the quantum canon. And because anyone _could_ know all that twentieth-century material by reading a single book, I could readily assume that anyone who was interested _did_ know it, and could take that as shared background knowledge (like, say, the existence of the Roman Empire) when discussing newer topics like quantum lower bounds, the adiabatic algorithm, or BQP/qpoly.

Of course I couldn't have been more wrong. In the years since Mike&Ike came out, the total amount of confusion in the world about the |A〉|B〉|C〉's of quantum computing (as well as the total number of books that try to address that confusion) has increased exponentially. And so it's good to have a distinguished physicist like Mermin patiently telling readers the following:

> "To understand how to _build_ a quantum computer … you must indeed have many years of experience in quantum mechanics and its applications under your belt. But if you only want to know what such a device is capable in principle of doing once you have it, then there is no reason to get involved in the really difficult physics of the subject." (page xiii)
> 
> "This means that all traces of the amplitudes αx characterizing the input state have vanished from the output state. The only role they have played in the measurement is to determine the probability of a particular output." (page 25)
> 
> "Small alterations in the phases produce small alterations in the probabilities of getting that extremely precise digital information, but not the precision of the information itself, once it is acquired." (page 85)

Personally, I find it hard to remember that anyone needs to be told these things -- and even when I _do_ tell them, they don't believe me (probably because I'm waving my arms too wildly). They think I'm making it up. But Mermin dispels the common misconceptions with a calm air of gravity.

I'll end with two quibbles.

First, while Mermin talks a great deal about quantum black-box algorithms, he never once mentions the crucial distinction between the "black-box" world -- the world where one can prove unconditionally both that quantum computers can solve certain problems exponentially faster than classical computers, and that they _can 't_ solve certain other problems any faster than classical ones -- and the "non-black-box" world, where all such statements are necessarily conjectural. The one time he does touch on this distinction, he gets it wrong:

> "The best known classical algorithms for finding the period r of such a function take a time that grows faster than any power of the number n of bits of r (exponentially with n1/3)." (page 63)

The best classical algorithm for period-finding _provably_ takes time that grows exponentially with n/2. The best known classical algorithms _for factoring_ take time that grows exponentially with n1/3. But the latter algorithms (necessarily) use deeper properties of the factoring problem than just its reducibility to period-finding.

I found this an uncharacteristic omission for Mermin -- whose tendency is to examine whatever he brings up from all possible angles -- though perhaps it can be understood in terms of a decision to avoid any mention of complexity theory.

The second quibble is that there are no exercises.
