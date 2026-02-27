---
title: "Stephen Wiesner (1942-2021)"
author: "Scott Aaronson"
date: "Fri, 13 Aug 2021"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=5730"
---

[](https://scottaaronson.blog/wiesner-sm.jpg)Photo credit: Lev Vaidman

These have [not](https://scottaaronson.blog/?p=5566) been an auspicious few weeks for Jewish-American-born theoretical physicists named Steve who made epochal contributions to human knowledge in the late 1960s, and who I had the privilege to get to know a bit when they were old.

This morning, my friend and colleague [Or Sattath](https://orsattath.wordpress.com/about/) brought me the terrible news that [Stephen Wiesner](https://en.wikipedia.org/wiki/Stephen_Wiesner) has passed away in Israel. [Because people have asked: I’ve now also heard directly from Wiesner’s daughter Sarah.]

Decades ago, Wiesner left academia, embraced Orthodox Judaism, moved from the US to Israel, and took up work there as a construction laborer--believing (or so he told me) that manual labor was good for the soul. In the late 1960s, however, Wiesner was still a graduate student in physics at Columbia University, when he wrote [Conjugate Coding](http://users.cms.caltech.edu/~vidick/teaching/120_qcrypto/wiesner.pdf): arguably the foundational document of the entire field of quantum information science. ~~Famously, this paper was so far ahead of its time that it was rejected over and over from journals, taking nearly 15 years to get published.~~ (Fascinatingly, Gilles Brassard tells me that this isn't true: it was rejected _once_ , from _IEEE Transactions on Information Theory_ , and then Wiesner simply shelved it.) When it finally appeared, in 1983, it was in _[SIGACT News](https://dl.acm.org/newsletter/sigact)_ --a venue that I know and love, where I've published too, but that's more like the house newsletter for theoretical computer scientists than an academic journal.

But it didn't matter. By the early 1980s, Wiesner's ideas had been successfully communicated to [Charlie Bennett](https://en.wikipedia.org/wiki/Charles_H._Bennett_\(physicist\)) and [Gilles Brassard](https://en.wikipedia.org/wiki/Gilles_Brassard), who refashioned them into the first scheme for [quantum key distribution](https://en.wikipedia.org/wiki/Quantum_key_distribution)--what we now call [BB84](https://en.wikipedia.org/wiki/BB84). Even as Bennett and Brassard received scientific acclaim for the invention of quantum cryptography--including, a few years ago, the [Wolf Prize](https://en.wikipedia.org/wiki/Wolf_Prize) (often considered second only to the Nobel Prize), at a ceremony in the Knesset in Jerusalem that I attended--the two B's were always careful to acknowledge their massive intellectual debt to Steve Wiesner.

* * *

Let me explain what Wiesner does in the Conjugate Coding paper. As far as I know, this is the first paper ever to propose that quantum information--what Wiesner called "polarized light" or "spin-1/2 particles" but we now simply call [qubits](https://en.wikipedia.org/wiki/Qubit)--works differently than classical bits, in ways that could _actually be useful_ for achieving cryptographic tasks that are impossible in a classical world. What could enable these cryptographic applications, wrote Wiesner, is the fact that there's no physical means for an attacker or eavesdropper to _copy_ an unknown qubit, to produce a second qubit in the same quantum state. This observation--now called the [No-Cloning Theorem](https://en.wikipedia.org/wiki/No-cloning_theorem)--would only be named and published in 1982, but Wiesner treats it in his late-1960s manuscript as just obvious background.

Wiesner went further than these general ideas, though, to propose an explicit scheme for [quantum money](https://en.wikipedia.org/wiki/Quantum_money) that would be physically impossible to counterfeit--a scheme that's still of enormous interest half a century later (I teach it every year in my [undergraduate course](https://www.scottaaronson.com/qclec.pdf)). In what we now call the Wiesner money scheme, a central bank prints "quantum bills," each of which contains a classical serial number as well as a long string of qubits. Each qubit is prepared in one of four possible quantum states:

  * |0⟩,
  * |1⟩,
  * |+⟩ = (|0⟩+|1⟩)/√2, or
  * |-⟩ = (|0⟩-|1⟩)/√2.



The bank, in a central database, stores the serial number of every bill in circulation, as well as the preparation instructions for each of the bill's qubits. If you want to _verify_ a bill as genuine--this, as Wiesner knew, is the big drawback--you have to bring it back to the bank. The bank, using its secret knowledge of how each qubit was prepared, measures each qubit in the appropriate basis--the {|0⟩,|1⟩} basis for |0⟩ or |1⟩ qubits, the {|+⟩,|-⟩} basis for |+⟩ or |-⟩ qubits--and checks that it gets the expected outcomes. If even one qubit yields the wrong outcome, the bill is rejected as counterfeit.

Now consider the situation of a counterfeiter, who holds a quantum bill but lacks access to the bank's secret database. When the counterfeiter tries to copy the bill, they won't know the right basis in which to measure each qubit--and if they make the wrong choice, then it's not only that they fail to make a copy; it's that the measurement destroys even the _original_ copy! For example, measuring a |+⟩ or |-⟩ qubit in the {|0⟩,|1⟩} basis will randomly collapse the qubit to either |0⟩ or |1⟩--so that, when the bank later measures the same qubit in the correct {|+⟩,|-⟩} basis, it will see the wrong outcome, and realize that the bill has been compromised, with 1/2 probability (with the probability increasing to nearly 1 as we repeat across hundreds or thousands of qubits).

Admittedly, the handwavy argument above, which Wiesner offered, is far from a security proof by cryptographers' standards. In 2011, I [pointed that out on StackExchange](https://cstheory.stackexchange.com/questions/11363/rigorous-security-proof-for-wiesners-quantum-money). My post, I'm happy to say, spurred Molina, Vidick, and Watrous to write a [beautiful 2012 paper](https://arxiv.org/abs/1202.4010), where they rigorously proved for the first time that in Wiesner's money scheme, no counterfeiter consistent with the laws of quantum mechanics can turn a single n-qubit bill into two bills that both pass the bank's verification with success probability greater than (3/4)n (and this is tight). But the intuition was already clear enough to Wiesner in the 1960s.

In 2003--when I was already a PhD student in quantum information, but incredibly, had never heard of Stephen Wiesner or his role in founding my field--I rediscovered the idea of quantum states |ψ⟩ that you could store, measure, and feed into a quantum computer, but that would be _usefully uncopyable_. (My main interest was in whether you could create "unpiratable quantum software programs.") Only in 2006, at the University of Waterloo, did Michele Mosca and his students make the connection for me to quantum money, Stephen Wiesner, and his Conjugate Coding paper, which I then read with amazement--along with a [comparably amazing followup work](https://static.aminer.org/pdf/PDF/000/120/546/quantum_cryptography_or_unforgeable_subway_tokens.pdf) by Bennett, Brassard, Breidbart, and Wiesner.

But it was clear that there was still a great deal to do. Besides unpiratable software, Wiesner and his collaborators had lacked the tools in the early 1980s seriously to tackle the problem of secure quantum money that _anybody_ could verify, not only the bank that had created the money. I realized that, if such a thing was possible at all, then just like unpiratable software, it would require cryptographic hardness assumptions, a restriction to polynomial-time counterfeiters, and (hence) ideas from quantum computational complexity. The No-Cloning Theorem couldn't do the job on its own.

That realization led to my 2009 paper [Quantum Copy-Protection and Quantum Money](https://arxiv.org/abs/1110.5353), and from there, to the "modern renaissance" of Wiesner's old idea of quantum money, with well over a hundred papers (e.g., [my 2012 paper with Paul Christiano](https://arxiv.org/abs/1203.4740), Farhi et al.'s [quantum state restoration paper](https://arxiv.org/abs/0912.3823), their [quantum money from knots paper](https://arxiv.org/abs/1004.5127), Mark Zhandry's 2017 [quantum lightning paper](https://arxiv.org/abs/1711.02276), Dmitry Gavinsky's [improvement of Wiesner's scheme](https://arxiv.org/abs/1109.0372) wherein the money is verified by classical communication with the bank, Broduch et al.'s [adaptive attack](https://arxiv.org/abs/1404.1507) on Wiesner's original scheme, my [shadow tomography paper](https://arxiv.org/abs/1711.01053) proving the necessity for the bank to keep a giant database in information-theoretic quantum money schemes like Wiesner’s, Daniel Kane's [strange scheme based on modular forms](https://arxiv.org/abs/1809.05925)…). The purpose of many of these papers was either to break the quantum money schemes proposed in previous papers, or to patch the schemes that were previously broken.

After all this back-and-forth, spanning more than a decade, I'd say that Wiesner's old idea of quantum money is now in good enough theoretical shape that the main obstacle to its practical realization is merely the "engineering difficulty"--namely, how to get the qubits in a bill, sitting in your pocket or whatever, to maintain their quantum coherence for more than a few nanoseconds! (Or possibly a few hours, if you're willing to schlep a cryogenic freezer everywhere you go.) It's precisely because quantum key distribution doesn't have this storage problem--because there the qubits are simply sent across a channel and then immediately measured on arrival--that QKD is actually practical today, although the market for it has proven to be extremely limited so far.

In the meantime, while the world waits for the quantum error-correction that could keep qubits alive indefinitely, there's Bitcoin. The latter perversely illustrates just how immense the demand for quantum money might someday be: the staggering lengths to which people will go, diverting the electricity to power whole nations into mining rigs, to get around our current inability to realize Wiesner's elegant quantum-mechanical solution to the same problem. When I first learned about Bitcoin, shortly after its invention, it was in the context of: "here's something I'd better bring up in my lectures on quantum money, in order to explain how much better WiesnerCoin could eventually be, when it's the year 2200 or whatever and we all have quantum computers wired up by a quantum Internet!" It never occurred to me that I should forget about the year 2200, liquidate my life savings, and immediately buy up all the Bitcoin I could. [Added: I've since learned that Wiesner's daughter Sarah is a professional in the Bitcoin space.]

* * *

Photo credit: Or Sattath

In his decades as a construction laborer, Wiesner had (as far as I know) no Internet presence; many of my colleagues didn't even realize he was still alive. Even then, though, Wiesner never turned his back _so_ far on his previous life, his academic life, that the quantum information faculty at Hebrew University in Jerusalem couldn't entice him to participate in some seminars there. Those seminars are where I had the privilege to meet and talk to him several times over the last decade. He was thoughtful and kind, listening with interest as I told him how I and others were trying to take quantum money into the modern era by making it publicly verifiable.

I also vividly remember a conversation in 2013 where Steve shared his fears about the American physics establishment and military-industrial complex, and passionately urged me to

  1. quit academia and get a "real job," and
  2. flee the US immediately and move my family to Israel, because of a wave of fascism and antisemitism that was about to sweep the US, just like with Germany in the 1930s.



I politely nodded along, pointing out that my Israeli wife and I had considered living in Israel but the job opportunities were better in US, silently wondering when Steve had gone _completely_ off his rocker. Today, Steve's urgent warning about an impending fascist takeover of the US seems … uh, _slightly_ less crazy than in 2013? Maybe, just like with quantum money, Wiesner was simply too far ahead of his time to sound sane.

Wiesner also talked to me about his father, [Jerome Wiesner](https://en.wikipedia.org/wiki/Jerome_Wiesner), who was a legendary president of MIT--still spoken about in reverent tones when I taught there--as well as the chief science advisor to John F. Kennedy. One of JFK's most famous decisions was to override the elder Wiesner's fervent opposition to sending humans to the moon (Wiesner thought it a waste of money, as robots could do the same science for vastly cheaper).

While I don't know all the details (I hope someone someday researches it and writes a book), Steve Wiesner made it clear to me that he did not get along with his famous father _at all_ --in fact they became estranged. Steve told me that his embrace of Orthodox Judaism was, at least in part, a reaction against everything his father had stood for, including militant scientific atheism. I suppose that in the 1960s, millions of young Americans defied their parents via sex, drugs, and acoustic guitar; only a tiny number did so by donning [tzitzit](https://en.wikipedia.org/wiki/Tzitzit) and moving to Israel to pray and toil with their hands. The two groups of rebels did, however, share a tendency to grow long beards.

Wiesner's unique, remarkable, _uncloneable_ life trajectory raises the question: who are the young Stephen Wiesners of our time? Will we be faster to recognize their foresight than Wiesner's contemporaries were to recognize his?

* * *

Feel free to share any other memories of Stephen Wiesner or his influence in the comments.

* * *

**Update (Aug. 14):** See also [Or Sattath's memorial post](https://orsattath.wordpress.com/2021/08/14/stephen-wiesner/), which (among other things) points out something that my narrative missed: namely, besides quantum money, Wiesner _also_ invented [superdense coding](https://en.wikipedia.org/wiki/Superdense_coding) in 1970, although he and Bennett only published the idea 22 years later (!).

And I have more photos! Here's [Wiesner with an invention of his](https://www.scottaaronson.com/wiesner2.jpg) and [another photo](https://www.scottaaronson.com/wiesner3.jpg) (thanks to his daughter Sarah). Here's [another photo from 1970](https://www.scottaaronson.com/wiesner1970.jpg) and [Charlie Bennett's handwritten notes](https://www.scottaaronson.com/wiesnernotes1970.jpg) (!) after first meeting Wiesner in 1970 (thanks to Charlie Bennett).

**Another Update:** Stephen’s daughter Sarah gave me the following fascinating information to share.

> In the 70's he lived in California where he worked in various Silicon Valley startups while also working weekends as part of a produce (fruits and vegetables) distribution co-op. During this time he became devoted to the ideas of solar energy, clean energy and space migration and exploration. He also became interested in Judaism. He truly wanted to help and make our world more peaceful and safe with his focus being on clean energy and branching out into space. He also believed that instead of fighting over the temple mount in Jerusalem, the Third Temple should be built in outer-space or in a structure above the original spot, an idea he tried to promote to prevent wars over land.
