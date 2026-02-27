---
title: "The Hiring Scott Aaronson FAQ"
author: "Scott Aaronson"
date: "Sat, 05 May 2007"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=231"
---

Last weekend, I got back from interviewing at the University of Washington, Stanford, Caltech, Berkeley, and Cornell. Then I fell asleep, and am only just now waking up. On this trip -- surely the most exhausting I've ever been on -- I seem to remember giving a talk on [The Limits of Quantum Computers](http://www.scottaaronson.com/talks/jobtalk4.ppt). (You'll have to go to presentation mode to get the full effect of my PowerPoint animations, and especially the D-Wave montage on slide 2.)

The bulk of the time, however, was taken up with interviews. My interviewers -- maybe 20 or 30 at each school, in CS, physics, applied math, even chemistry and electrical engineering -- asked me good questions, questionable questions, hard questions, soft questions, loaded questions, _lots_ of questions. And that's what enables me, without further ado, to present for your reading enjoyment **The Official Hiring Scott Aaronson FAQ**.

_[Note: The questions below are all things that I was actually asked by at least one interviewer -- in some cases, by dozens of interviewers.]_

**Q:** What will you do if quantum computing doesn't pan out in the next 20 years?

**A:** This question presupposes that quantum computing should be judged as a high-risk engineering project. But that's never been my view. My view is that it should be judged as basic science. What we're trying to do is unify the theory of computing with our best theory of the physical world, and to perform the most stringent tests to which quantum mechanics itself has ever been subjected. For me, the payoff for better scientific understanding is not in some remote future -- it's as soon as the understanding is achieved.

**Q:** But why should we care about basic science?

**A:** Uhh, we are called the computer _science_ department…

**Q:** Does quantum computing really belong in CS departments, as opposed to physics departments?

**A:** It belongs if we want it to belong! In my experience, the _physicists_ have a bigger hurdle than the computer scientists in getting started with quantum computing research. All we need to do is ask ourselves: "what happens if we generalize probability theory to allow minus signs, and base it on the L2 norm instead of the L1 norm?" From then on it's just the concepts we know and love: states, transformations, recursion, reductions, universality, asymptotic efficiency, and so on. Physicists, by contrast, have to learn most of this stuff for the first time. It's been a great personal pleasure to watch physicists who once suspected that CS was devoid of intellectual content, struggle with that content while trying to learn quantum computing!

Now, if we want to take a dramatic scientific development that wouldn't have been possible without computer science, and hand it over to the physicists on a silver platter, that's certainly our prerogative. But is it in our interest as a field?

**Q:** What if quantum computing is fundamentally impossible?

**A:** That would be _much_ more interesting than if it's possible! Merely building a quantum computer would be the more boring outcome -- the one consistent with all the physics we already know.

**Q:** But no one really questions quantum mechanics, do they?

**A:** Well, you just did!

**Q:** No, I only questioned whether quantum _computing_ is possible. Couldn't quantum mechanics be valid, but quantum computing still be impossible because of noise and decoherence?

**A:** If so, then there's something enormous that we don't yet understand about the relevant physics. Look, in light of the [Threshold Theorem](http://www.arxiv.org/abs/quant-ph/9611025) (that if the rate of decoherence per qubit per time step is smaller than some constant threshold, then one can perform an arbitrarily long quantum computation), it's hard to maintain that we're talking about some niggling technical issue. What we're really talking about is this: _to keep track of the state of N entangled particles, does Nature have to do an amount of computational work that increases exponentially with N?_ And if it doesn't, then (turning the question around) is there an efficient classical algorithm to simulate the behavior of N entangled particles? These are not questions that will just go away for some trivial reason that everyone's overlooked.

**Q:** Suppose Ed Witten spent a week thinking about it, and came up with some profound reason why quantum computing is impossible. What would you do next?

**A:** I'd drop whatever else I was doing, and devote all of my time to understanding the implications of his discovery for computer science and physics!

[Pause]

Of course, since this is Witten, maybe he would've spent a _second_ week and worked out all the implications himself. So I guess all I can say is that to my knowledge, he _hasn 't_ in fact been thinking about these issues.

**Q:** How long until we have practical quantum computers?

**A:** In my opinion, quantum computing experiments are not yet at a stage where one can make "Moore's Law" type predictions. We might be in the same situation with quantum computing that Babbage was with classical computing in the 1840's. In other words, we think we know the fundamental principles, and we're right -- but the technology isn't there yet, and might not be for a long time.

Of course, as with any technology, progress could happen faster than almost any of us expect. But I prefer to be pessimistic: that way either you're right, or else you don't mind being wrong!

**Q:** How many qubits are the experimentalists at so far?

**A:** It depends how you measure. People got up to twelve qubits in liquid-state NMR, the platform that was used some years ago to factor 15 into 3×5 (at least with high probability!). The trouble with liquid NMR is that no one knows how to scale it: currently the signal decreases exponentially with the number of qubits. So people turned their attention to other platforms, such as ion traps, photonics, and solid-state NMR. With these platforms the quantum computer's state is much closer to being pure, so the prospects for scalability are much better. But manipulating the qubits is correspondingly harder. With ion traps, Rainer Blatt's group in Innsbruck did tomography of an 8-qubit state, and other groups have done computations involving 2 or 3 qubits. With photonics, it's easy to get a huge number of qubits that are highly coherent; the problem is that photons don't like to talk to each other (in fact they fly right past each other), and therefore you can only apply two-qubit gates by using matter particles as intermediaries.

There are other more exotic proposals for scalable quantum computing, such as "nonabelian anyons." With these I think it's fair to say we're not even at _one_ qubit yet. But if these proposals _did_ work, then the hope would be that they could leapfrog over the other proposals by building in error-correction for free.

**Q:** Which universities in North America are the major centers for quantum computing theory?

**A:** Right now there are four: Waterloo, Caltech, MIT, and Berkeley.

**Q:** Supposing we had scalable quantum computers, are your lower-bound results telling us that they would have no applications?

**A:** Absolutely not. Aside from their intrinsic scientific interest, quantum computers _would_ have real applications. In my opinion, the most important would be the one so obvious that we computer scientists hardly ever talk about it: namely, simulating quantum physics and chemistry! This, of course, is what a quantum computer does in its sleep. At the same time, it's also a fundamental problem in nanotechnology, high-temperature superconductivity, QCD, and other areas, important enough that Nobel prizes have been awarded even for ways to solve special cases efficiently on a classical computer.

Admittedly, you could say that every physical system in the universe is a quantum computer computing its own evolution! But the goal here would be to build a _universal_ quantum simulator: a single machine that can be programmed to efficiently simulate any quantum system of interest. It's the difference between building a wind tunnel versus writing code in order to simulate an airplane.

Now, by a sort of lucky accident, we can _sometimes_ coax a quantum computer into solving classical problems asymptotically faster than we know how to solve them with a classical computer. The famous examples are of course (1) breaking RSA and other cryptographic codes, and (2) solving 'generic' search problems quadratically faster than a classical computer. These discoveries have enormous theoretical interest, but (as far I can tell) only limited practical interest. Maybe I'm wrong though.

**Q:** Granted that quantum computing is already interesting as basic science, do you agree that it would be _more_ interesting if we had practical quantum computers?

**A:** Well, I certainly wouldn't mind it.

**Q:** You work on quantum computing, yet most of your research is about how quantum computers _wouldn 't_ be very powerful. Isn't that a bit strange?

**A:** In the long run, I don't think quantum computing research is helped by falsehood. If we're going to be scientists and not PR flaks, then obviously we ought to welcome the truth, whichever way it goes.

But personally, I'd go even further than that. For me, a model of computation without _any_ limitations would be like Superman without kryptonite. There just wouldn't be a whole lot to say about it! To my way of thinking, a model that lets you factor integers efficiently but not solve NP-complete problems is actually _more_ interesting than a model that gives you everything!

Oh, and one further point: if you're interested (as I am) in the ultimate limits of computation, then you're almost _professionally obligated_ to study quantum computing. Why? Because any time you prove a limit of classical computers, you now have to ask yourself: is this something fundamental, or is it just an artifact of my working in a high-decoherence regime?

**Q:** Why are you so interested in the _limits_ of computation?

**A:** To show that something is possible, you just have to find a way to do it. But to show that something's _not_ possible, you have to consider _every_ way of doing it, and prove that none of them work. This is why negative results are so much rarer than positive results, but also why they often give us deeper understanding.

**Q:** That seems like an extremely male perspective! [said, jokingly, by a female interviewer]

**A:** I respectfully disagree. Look, as with pretty much every area of CS, we could certainly use more talented women in quantum computing theory: maybe a few dozen more Dorit Aharonovs, Julia Kempes, and Barbara Terhals. I find the gender imbalance in CS depressing, and I've long been interested in what it would take to correct it. But the relevant question is this: is the proportion of women working on quantum lower bounds _smaller_ than the proportion working on quantum algorithms? I don't think that it is.

**Q:** What's your vision for where your research is headed in the next 5-10 years?

**A:** I know I'm not supposed to say this in an interview, but I don't have a vision. I have _this_ annoying open problem, _that_ conjecture, _this_ claim that seems wrong to me. I know some people have a coherent vision for where their research is headed. And in experimental areas, obviously you have to justify what you're going to do with your $200 million of equipment. But at least in theoretical computer science, having a "vision" always seemed incredibly difficult to me.

For example, let's say you have a vision that you're going to solve problem X using techniques A, B, C. Then what do you do when you find out that techniques A and C are total nonstarters -- but that technique B, while it's useless for X, does solve a completely unrelated problem Y? What you do is make up a story about how Y was the problem you wanted to solve all along! We all do that: drawing targets around where the arrows hit is simply the business we're in.

What I can tell you is this: I'm interested in fundamental limits on what can be efficiently computed in the physical world. I look for problems that can be addressed with tools from theoretical computer science, but that also have some physical or philosophical _point_ : something that makes me feel like the universe would be a different place if the conjecture were true than if it were false.

In the past, quantum computing has been an incredibly rich source of that sort of problem for me. But it's never been my exclusive interest -- I've also worked on circuit complexity, Bayesian agreement protocols, and even information retrieval and clustering. And if quantum computing ever stops being a source of conceptually rich open problems, then I'll look for those problems somewhere else.

**Q:** I noticed that, on at least three occasions where you proved a new quantum lower bound, other people quickly improved it to an optimal bound. Is there a reason why you didn't prove the optimal bounds yourself?

**A:** Yeah, I don't seem to be very good at tightening my lower bounds! I've had more success in proving the _first_ nontrivial lower bound for a given problem -- that is, in understanding why the complexity scales exponentially rather than polynomially. After that, I'm more than happy to let others pin down the order of the exponential. Every time that's happened, far from feeling disappointed over being "scooped," I felt great that my work gave other people a foundation to build on.

**Q:** You look tired. Would you like some coffee?

**A:** Yes.

**Q:** How did you get interested in quantum computing?

**A:** When I first learned about programming as an 11-year-old, it wasn't only a revelation to me because I now understood how video games worked (though that was definitely important). The real revelation was: _this is how the entire universe must work!_ It's all just bits getting updated by simple rules. I don't have to understand physics if I want to understand physics.

Of course I'd _heard_ of quantum effects, and I knew they were supposed to be important -- but since I didn't understand them, they made no difference to me. Then later, as an undergrad at Cornell, I read the early quantum computing papers, and found out that this "quantum weirdness" the physicists kept babbling about was nothing more than linear algebra over the complex numbers. "Hey, linear algebra … even _I_ can do that!"

But I didn't really become engrossed in quantum computing until a summer internship at Bell Labs. As a diversion from my "real" work that summer (which had to do with multivariate isotone regression), I went through the [Bernstein-Vazirani paper](http://www.cs.berkeley.edu/~vazirani/pubs/bv.ps), and managed to improve their containment BQP ⊆ P#P to BQP ⊆ PP. Then I found out that Lov Grover worked in the same building as me, so I went and told him about my result. Well, it turned out that BQP ⊆ PP was already known -- it had been proved by Adleman, DeMarrais, and Huang the year before. But one consequence of my talking to Lov was that I ended up doing an internship with him the _next_ summer, working (mostly unsuccessfully) on quantum lower bounds. Ashwin Nayak was also working with Lov that summer; from Ashwin I found out about Umesh Vazirani's group at Berkeley and how all the cool people were there.

After that, the main questions in my mind were whether I could get accepted to Berkeley, whether Umesh would take me on as a student, and whether I was good enough to do anything original in this field. I emailed Umesh and he never responded, which I took as an extremely bad sign -- how little I knew back then! Luckily I _did_ get in to Berkeley, I _did_ start working with Umesh, I _did_ stumble on some new results, and I guess the rest is history.

**Q:** How many people work on the computer science side of quantum computing?

**A:** Probably the best way to measure that is by how many people attend the annual [QIP ](http://www.qipworkshop.org)conference (for if they don't go to QIP, do they really exist?) Last year's QIP drew almost 200 attendees.

**Q:** Would you be willing to supervise grad students in classical theoretical computer science?

**A:** Willing is an understatement! I would _love_ to supervise talented grad students in derandomization, circuit lower bounds, learning theory, or any of the other classical areas that I try hard to keep up with and occassionally even work on. Admittedly, when it comes to (say) list decoding, extractors, approximation algorithms, or PCP, the students would first have to teach _me_ what's going on, but after that I'd be happy to supervise them.

**Q:** What would you say if I told you that I think quantum computing is like postmodern literary criticism, just a way for people to churn out one paper after another by switching words around, citing each other in a circular way, recycling the same few mathematically trivial ideas over and over -- and indeed, that the whole field of theoretical computer science has no real ideas and no connections to anything outside itself?

**A:** I'd say thank you very much for your opinion, and you've got me for -- let's see, 25 more minutes, so what can I do for you?
