---
title: "The No-Cloning Theorem and the Human Condition: My After-Dinner Talk at QCRYPT"
author: "Scott Aaronson"
date: "Mon, 19 Sep 2016"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=2903"
---

The following are the after-dinner remarks that I delivered at [QCRYPT'2016](http://2016.qcrypt.net/), the premier quantum cryptography conference, on Thursday Sep. 15 in Washington DC. You could compare to [my after-dinner remarks at QIP'2006](https://scottaaronson.blog/?p=49) to see how much I've ""matured"" since then. Thanks so much to Yi-Kai Liu and the other organizers for inviting me and for putting on a really fantastic conference.

* * *

It's wonderful to be here at QCRYPT among so many friends--this is the first significant conference I've attended since I moved from MIT to Texas. I do, however, need to register a complaint with the organizers, which is: why wasn't I allowed to bring my concealed firearm to the conference? You know, down in Texas, we don't look too kindly on you academic elitists in Washington DC telling us what to do, who we can and can't shoot and so forth. Don't mess with Texas! As you might've heard, many of us Texans even support a big, beautiful, physical wall being built along our border with Mexico. Personally, though, I don't think the wall proposal goes far enough. Forget about illegal immigration and smuggling: I don't even want Americans and Mexicans to be able to win the [CHSH game](https://en.wikipedia.org/wiki/CHSH_inequality) with probability exceeding 3/4. Do any of you know what kind of wall could prevent _that_? Maybe a _meta_ physical wall.

OK, but that's not what I wanted to talk about. When Yi-Kai asked me to give an after-dinner talk, I wasn't sure whether to try to say something actually relevant to quantum cryptography or just make jokes. So I'll do something in between: I'll tell you about research directions in quantum cryptography that are _also_ jokes.

The subject of this talk is a deep theorem that stands as one of the crowning achievements of our field. I refer, of course, to the [No-Cloning Theorem](https://en.wikipedia.org/wiki/No-cloning_theorem). Almost everything we're talking about at this conference, from [QKD](https://en.wikipedia.org/wiki/Quantum_key_distribution) onwards, is based in some way on quantum states being unclonable. If you read [Stephen Wiesner's paper from 1968](http://dl.acm.org/citation.cfm?id=1008920), which founded quantum cryptography, the No-Cloning Theorem already played a central role--although Wiesner didn't call it that. By the way, here's my #1 piece of research advice to the students in the audience: if you want to become immortal, just find some fact that everyone already knows and give it a name!

I'd like to pose the question: why should our universe be governed by physical laws that make the No-Cloning Theorem true? I mean, it's _possible_ that there's some other reason for our universe to be quantum-mechanical, and No-Cloning is just a byproduct of that. No-Cloning would then be like the armpit of quantum mechanics: not there because it does anything useful, but just because there's gotta be _something_ under your arms.

OK, but No-Cloning _feels_ really fundamental. One of my early memories is when I was 5 years old or so, and utterly transfixed by my dad's home fax machine, one of those crappy 1980s fax machines with wax paper. I kept thinking about it: is it really true that a piece of paper gets transmaterialized, sent through a wire, and reconstituted at the other location? Could I have been _that_ wrong about how the universe works? Until finally I got it--and once you get it, it's hard even to recapture your original confusion, because it becomes so obvious that the world is made not of stuff but of copyable bits of information. "Information wants to be free!"

The No-Cloning Theorem represents nothing less than a partial return to the view of the world that I had before I was five. It says that quantum information _doesn 't_ want to be free: it wants to be private. There is, it turns out, a kind of information that's tied to a particular place, or set of places. It can be moved around, or even teleported, but it can't be copied the way a fax machine copies bits.

So I think it's worth at least entertaining the possibility that we don't have No-Cloning because of quantum mechanics; we have quantum mechanics because of No-Cloning--or because quantum mechanics is the simplest, most elegant theory that has unclonability as a core principle. But if so, that just pushes the question back to: why _should_ unclonability be a core principle of physics?

* * *

**Quantum Key Distribution**

A first suggestion about this question came from Gilles Brassard, who's here. Years ago, I attended a talk by Gilles in which he speculated that the laws of quantum mechanics are what they are _because_ Quantum Key Distribution (QKD) has to be possible, while bit commitment has to be _im_ possible. If true, that would be awesome for the people at this conference. It would mean that, far from being this exotic competitor to RSA and Diffie-Hellman that's distance-limited and bandwidth-limited and has a tiny market share right now, QKD would be the entire reason why the universe is as it is! Or maybe what this really amounts to is an appeal to the Anthropic Principle. Like, if QKD _hadn 't_ been possible, then we wouldn't be here at QCRYPT to talk about it.

* * *

**Quantum Money**

But maybe we should search more broadly for the reasons why our laws of physics satisfy a No-Cloning Theorem. Wiesner's paper sort of hinted at QKD, but the main thing it had was a scheme for unforgeable quantum money. This is one of the most direct uses imaginable for the No-Cloning Theorem: to store economic value in something that it's physically impossible to copy. So maybe _that 's_ the reason for No-Cloning: because God wanted us to have e-commerce, and didn't want us to have to bother with blockchains (and certainly not with credit card numbers).

The central difficulty with quantum money is: how do you authenticate a bill as genuine? (OK, fine, there's also the dificulty of how to keep a bill coherent in your wallet for more than a microsecond or whatever. But we'll leave that for the engineers.)

In Wiesner's original scheme, he solved the authentication problem by saying that, whenever you want to verify a quantum bill, you bring it back to the bank that printed it. The bank then looks up the bill's classical serial number in a giant database, which tells the bank in which basis to measure each of the bill's qubits.

With this system, you can actually get information-theoretic security against counterfeiting. OK, but the fact that you have to bring a bill to the bank to be verified negates much of the advantage of quantum money in the first place. If you're going to keep involving a bank, then why not just use a credit card?

That's why over the past decade, some of us have been working on _public-key_ quantum money: that is, quantum money that anyone can verify. For this kind of quantum money, it's easy to see that the No-Cloning Theorem is no longer enough: you also need some cryptographic assumption. But OK, we can consider that. In recent years, we've achieved glory by proposing a huge variety of public-key quantum money schemes--and we've achieved even greater glory by breaking almost all of them!

After a while, there were basically two schemes left standing: [one based on knot theory](https://arxiv.org/abs/1004.5127) by Ed Farhi, Peter Shor, et al. That one has been proven to be secure under the assumption that it can't be broken. The [second scheme](http://arxiv.org/abs/1203.4740), which Paul Christiano and I proposed in 2012, is based on hidden subspaces encoded by multivariate polynomials. For our scheme, Paul and I were able to do better than Farhi et al.: we gave a _security reduction_. That is, we _proved_ that our quantum money scheme is secure, _unless_ there's a polynomial-time quantum algorithm to find hidden subspaces encoded by low-degree multivariate polynomials (yadda yadda, you can look up the details) with much greater success probability than we thought possible.

Today, the situation is that my and Paul's security proof remains completely valid, but meanwhile, our money is completely insecure! Our reduction means the opposite of what we thought it did. There _is_ a break of our quantum money scheme, and _as a consequence_ , there's also a quantum algorithm to find large subspaces hidden by low-degree polynomials with much better success probability than we'd thought. What happened was that first, some French algebraic cryptanalysts--Faugere, Pena, I can't pronounce their names--used Gröbner bases to [break](https://hal.inria.fr/hal-01098223/document) the noiseless version of scheme, in classical polynomial time. So I thought, phew! At least I had acceded when Paul insisted that we also include a noisy version of the scheme. But later, Paul noticed that there's a quantum reduction from the problem of breaking our noisy scheme to the problem of breaking the noiseless one, so the former is broken as well.

I'm choosing to spin this positively: "we used quantum money to discover a striking new quantum algorithm for finding subspaces hidden by low-degree polynomials. Err, yes, that's exactly what we did."

But, bottom line, until we manage to invent a better public-key quantum money scheme, or otherwise sort this out, I don't think we're entitled to claim that God put unclonability into our universe in order for quantum money to be possible.

* * *

**Copy-Protected Quantum Software**

So if not money, then what about its cousin, copy-protected software--could _that_ be why No-Cloning holds? By copy-protected quantum software, I just mean a quantum state that, if you feed it into your quantum computer, lets you evaluate some Boolean function on any input of your choice, but that _doesn 't_ let you efficiently prepare _more_ states that let the same function be evaluated. I think this is important as one of the preeminent _evil_ applications of quantum information. Why should nuclear physicists and genetic engineers get a monopoly on the evil stuff?

OK, but is copy-protected quantum software even possible? The first worry you might have is that, yeah, maybe it's possible, but then every time you wanted to run the quantum program, you'd have to make a measurement that destroyed it. So then you'd have to go back and buy a new copy of the program for the next run, and so on. Of course, to the software company, this would presumably be a feature rather than a bug!

But as it turns out, there's a fact many of you know--sometimes called the "Gentle Measurement Lemma," other times the "Almost As Good As New Lemma"--which says that, as long as the outcome of your measurement on a quantum state could be predicted almost with certainty given knowledge of the state, the measurement can be implemented in such a way that it hardly damages the state at all. This tells us that, if quantum money, copy-protected quantum software, and the other things we're talking about are possible at all, then they can also be made reusable. I summarize the principle as: "if rockets, then space shuttles."

Much like with quantum money, one can show that, relative to a suitable oracle, it's possible to quantumly copy-protect _any_ efficiently computable function--or rather, any function that's hard to learn from its input/output behavior. Indeed, the implementation can be not only copy-protected but also _obfuscated_ , so that the user learns nothing _besides_ the input/output behavior. As Bill Fefferman pointed out in his talk this morning, the No-Cloning Theorem lets us bypass Barak et al.'s famous result on the impossibility of obfuscation, because their impossibility proof assumed the ability to _copy_ the obfuscated program.

Of course, what we really care about is whether quantum copy-protection is possible in the _real_ world, with no oracle. I was [able to give](http://www.scottaaronson.com/papers/noclone-ccc.pdf) candidate implementations of quantum copy-protection for extremely special functions, like one that just checks the validity of a password. In the general case--that is, for arbitrary programs--Paul Christiano has a beautiful proposal for how to do it, which builds on our hidden-subspace money scheme. Unfortunately, since our money scheme is currently in the shop being repaired, it's probably premature to think about the security of the much more complicated copy-protection scheme! But these are wonderful open problems, and I encourage any of you to come and scoop us. Once we know whether uncopyable quantum software is possible at all, we could then debate whether it's the "reason" for our universe to have unclonability as a core principle.

* * *

**Unclonable Proofs and Advice**

Along the same lines, I can't resist mentioning some favorite research directions, which some enterprising student here could totally turn into a talk at next year's QCRYPT.

Firstly, what can we say about clonable versus unclonable quantum _proofs_ --that is, QMA witness states? In other words: for which problems in [QMA](https://en.wikipedia.org/wiki/QMA) can we ensure that there's an accepting witness that lets you efficiently create as many additional accepting witnesses as you want? (I mean, besides the QCMA problems, the ones that have short classical witnesses?) For which problems in QMA can we ensure that there's an accepting witness that _doesn 't_ let you efficiently create any additional accepting witnesses? I do have a few observations about these questions--ask me if you're interested--but on the whole, I believe almost anything one can ask about them remains open.

Admittedly, it's not clear how much _use_ an unclonable proof would be. Like, imagine a quantum state that encoded a proof of the Riemann Hypothesis, and which you would keep in your bedroom, in a glass orb on your nightstand or something. And whenever you felt your doubts about the Riemann Hypothesis resurfacing, you'd take the state out of its orb and measure it again to reassure yourself of RH's truth. You'd be like, _" my preciousssss!"_ And no one else could copy your state and thereby gain the same Riemann-faith-restoring powers that you had. I dunno, I probably won't hawk this application in a DARPA grant.

Similarly, one can ask about clonable versus unclonable _quantum advice states_ --that is, initial states that are given to you to boost your computational power beyond that of an ordinary quantum computer. And that's also a fascinating open problem.

OK, but maybe none of this quite gets at why our universe has unclonability. And this is an after-dinner talk, so do you want me to get to the _really_ crazy stuff? Yes?

* * *

**Self-Referential Paradoxes**

OK! What if unclonability is our universe's way around the paradoxes of self-reference, like the unsolvability of the halting problem and Gödel's Incompleteness Theorem? Allow me to explain what I mean.

In kindergarten or wherever, we all learn Turing's proof that there's no computer program to solve the halting problem. But what isn't usually stressed is that that proof actually does more than advertised. If someone hands you a program that they claim solves the halting problem, Turing doesn't merely tell you that that person is wrong--rather, he shows you exactly _how_ to expose the person as a jackass, by constructing an example input on which their program fails. All you do is, you take their claimed halt-decider, modify it in some simple way, and then feed the result back to the halt-decider as input. You thereby create a situation where, if your program halts given its own code as input, then it must run forever, and if it runs forever then it halts. "WHOOOOSH!" [head-exploding gesture]

OK, but now imagine that the program someone hands you, which they claim solves the halting problem, is a _quantum_ program. That is, it's a quantum state, which you measure in some basis depending on the program you're interested in, in order to decide whether that program halts. Well, the truth is, this quantum program _still_ can't work to solve the halting problem. After all, there's some classical program that simulates the quantum one, albeit less efficiently, and we already know that the classical program can't work.

But now consider the question: how would you actually produce an example input on which this quantum program failed to solve the halting problem? Like, suppose the program worked on every input you tried. Then ultimately, to produce a counterexample, you might need to follow Turing's proof and make a copy of the claimed quantum halt-decider. But then, of course, you'd run up against the No-Cloning Theorem!

So we seem to arrive at the conclusion that, while of course there's no quantum program to solve the halting problem, there _might_ be a quantum program for which no one could explicitly _refute_ that it solved the halting problem, by giving a counterexample.

I was pretty excited about this observation for a day or two, until I noticed the following. Let's suppose your quantum program that allegedly solves the halting problem has n qubits. Then it's possible to prove that the program can't possibly be used to compute more than, say, 2n bits of Chaitin's constant Ω, which is the probability that a random program halts. OK, but if we had an actual oracle for the halting problem, we could use it to compute as many bits of Ω as we wanted. So, suppose I treated my quantum program _as if_ it were an oracle for the halting problem, and I used it to compute the first 2n bits of Ω. Then I would _know_ that, assuming the truth of quantum mechanics, the program must have made a mistake somewhere. There would still be something weird, which is that I wouldn't know on which input my program had made an error--I would just know that it must've erred somewhere! With a bit of cleverness, one can narrow things down to two inputs, such that the quantum halt-decider must have erred on at least one of them. But I don't know whether it's possible to go further, and concentrate the wrongness on a single query.

We can play a similar game with other famous applications of self-reference. For example, suppose we use a quantum state to encode a system of axioms. Then that system of axioms will still be subject to Gödel's Incompleteness Theorem (which I guess I believe despite the umlaut). If it's consistent, it won't be able to prove all the true statements of arithmetic. But we might never be able to produce an explicit example of a true statement that the axioms don't prove. To do so we'd have to clone the state encoding the axioms and thereby violate No-Cloning.

* * *

**Personal Identity**

But since I'm a bit drunk, I should confess that all this stuff about Gödel and self-reference is just a warmup to what I _really_ wanted to talk about, which is whether the No-Cloning Theorem might have anything to do with the mysteries of personal identity and "free will." I first encountered this idea in Roger Penrose's book, [_The Emperor 's New Mind_](https://www.amazon.com/Emperors-New-Mind-Concerning-Computers/dp/0192861980). But I want to stress that I'm not talking here about the possibility that the brain is a quantum computer--much less about the possibility that it's a quantum-gravitational hypercomputer that uses microtubules to solve the halting problem! I might be drunk, but I'm not _that_ drunk. I also think that the Penrose-Lucas argument, based on Gödel's Theorem, for why the brain has to work that way is fundamentally flawed.

But here I'm talking about something different. See, I have a lot of friends in the Singularity / Friendly AI movement. And I talk to them whenever I pass through the Bay Area, which is where they congregate. And many of them express great confidence that before too long--maybe in 20 or 30 years, maybe in 100 years--we'll be able to upload ourselves to computers and live forever on the Internet (as opposed to just living 70% of our lives on the Internet, like we do today).

This would have lots of advantages. For example, any time you were about to do something dangerous, you'd just make a backup copy of yourself first. If you were struggling with a conference deadline, you'd spawn 100 temporary copies of yourself. If you wanted to visit Mars or Jupiter, you'd just email yourself there. If Trump became president, you'd not run yourself for 8 years (or maybe 80 or 800 years). And so on.

Admittedly, some awkward questions arise. For example, let's say the hardware runs three copies of your code and takes a majority vote, just for error-correcting purposes. Does that bring three copies of you into existence, or only one copy? Or let's say your code is run homomorphically encrypted, with the only decryption key stored in another galaxy. Does that count? Or you email yourself to Mars. If you want to make sure that you'll wake up on Mars, is it important that you delete the copy of your code that remains on earth? Does it matter whether anyone runs the code or not? And what exactly counts as "running" it? Or my favorite one: could someone threaten you by saying, "look, I have a copy of _your_ code, and if you don't do what I say, I'm going to make a thousand copies of it and subject them all to horrible tortures?"

The issue, in all these cases, is that in a world where there could be millions of copies of your code running on different substrates in different locations--or things where it's not even clear whether they _count_ as a copy or not--we don't have a principled way to take as input a description of the state of the universe, and then identify where in the universe _you_ are--or even a probability distribution over places where you could be. And yet you seem to need such a way in order to make predictions and decisions.

A few years ago, I wrote this gigantic, post-tenure essay called [The Ghost in the Quantum Turing Machine](http://www.scottaaronson.com/papers/giqtm3.pdf), where I tried to make the point that we don't know at what level of granularity a brain would need to be simulated in order to duplicate someone's subjective identity. Maybe you'd only need to go down to the level of neurons and synapses. But _if_ you needed to go all the way down to the molecular level, then the No-Cloning Theorem would immediately throw a wrench into most of the paradoxes of personal identity that we discussed earlier.

For it would mean that there were some microscopic yet essential details about each of us that were fundamentally uncopyable, localized to a particular part of space. We would all, in effect, be quantumly copy-protected software. Each of us would have a core of unpredictability--not merely probabilistic unpredictability, like that of a quantum random number generator, but genuine unpredictability--that an external model of us would fail to capture completely. Of course, by having futuristic nanorobots scan our brains and so forth, it would be possible in principle to make extremely realistic copies of us. But those copies necessarily wouldn't capture quite everything. And, one can speculate, maybe not enough for your subjective experience to "transfer over."

Maybe the most striking aspect of this picture is that sure, you could teleport yourself to Mars--but to do so you'd need to use quantum teleportation, and as we all know, quantum teleportation necessarily destroys the original copy of the teleported state. So we'd avert this metaphysical crisis about what to do with the copy that remained on Earth.

Look--I don't know if any of you are like me, and have ever gotten depressed by reflecting that all of your life experiences, all your joys and sorrows and loves and losses, every itch and flick of your finger, could in principle be encoded by a huge but finite string of bits, and therefore by a single positive integer. (Really? No one else gets depressed about that?) It's kind of like: given that this integer has existed since before there was a universe, and will continue to exist after the universe has degenerated into a thin gruel of radiation, what's the point of even going through the motions? You know?

But the No-Cloning Theorem raises the possibility that at least this integer is really _your_ integer. At least it's something that no one else knows, and no one else could know in principle, even with futuristic brain-scanning technology: you'll always be able to surprise the world with a new digit. I don't know if that's true or not, but if it _were_ true, then it seems like the sort of thing that would be worthy of elevating unclonability to a fundamental principle of the universe.

So as you enjoy your dinner and dessert at this historic Mayflower Hotel, I ask you to reflect on the following. People can photograph this event, they can video it, they can type up transcripts, in principle they could even record everything that happens down to the millimeter level, and post it on the Internet for posterity. But they're not gonna get the quantum states. There's _something_ about this evening, like about every evening, that will vanish forever, so please savor it while it lasts. Thank you.

* * *

**Update (Sep. 20):** Unbeknownst to me, Marc Kaplan _did_ video the event and put it up on YouTube! [Click here to watch.](https://www.youtube.com/watch?v=kXerI-tnW50) Thanks very much to Marc! I hope you enjoy, even though of course, the video can't precisely clone the experience of having been there.

[_Note:_ The part where I raise my middle finger is an inside joke--one of the speakers during the technical sessions inadvertently did the same while making a point, causing great mirth in the audience.]
