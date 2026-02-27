---
title: "Quantum Computing: Between Hope and Hype"
author: "Scott Aaronson"
date: "Sun, 22 Sep 2024"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=8329"
---

So, back in June [the White House announced](https://www.whitehouse.gov/briefing-room/statements-releases/2024/06/17/joint-fact-sheet-the-united-states-and-india-continue-to-chart-an-ambitious-course-for-the-initiative-on-critical-and-emerging-technology/) that UCLA would host a binational US/India workshop, for national security officials from both countries to learn about the current status of quantum computing and post-quantum cryptography. It fell to my friend and colleague Rafail Ostrovsky to organize the workshop, which ended up being held last week. When Rafi invited me to give the opening talk, I knew he'd keep emailing until I said yes. So, on the 3-hour flight to LAX, I wrote the following talk in a spiral notebook, which I then delivered the next morning with no slides. I called it "Quantum Computing: Between Hope and Hype." I thought _Shtetl-Optimized_ readers might be interested too, since it contains my reflections on a quarter-century in quantum computing, and prognostications on what I expect soon. Enjoy, and let me know what you think!

* * *

**Quantum Computing: Between Hope and Hype  
by Scott Aaronson**  
**September 16, 2024**

When Rafi invited me to open this event, it sounded like he wanted big-picture pontification more than technical results, which is just as well, since I'm getting old for the latter. Also, I'm just now getting back into quantum computing after a two-year leave at OpenAI to think about the theoretical foundations of AI safety. Luckily for me, that was a relaxing experience, since not much happened in AI these past two years. [Pause for laughs] So then, did anything happen in quantum computing while I was away?

This, of course, has been an extraordinary time for both quantum computing _and_ AI, and not only because the two fields were mentioned for the first time in an American presidential debate (along with, I think, the problem of immigrants eating pets). But it's extraordinary for quantum computing and for AI in very different ways. In AI, practice is wildly ahead of theory, and there's a race for scientific understanding to catch up to where we've gotten via the pure scaling of neural nets and the compute and data used to train them. In quantum computing, it's just the opposite: there's right now a race for _practice_ to catch up to where theory has been since the mid-1990s.

I started in quantum computing around 1998, which is not _quite_ as long as some people here, but which does cover most of the time since Shor's algorithm and the rest were discovered. So I can say: this past year or two is the first time I've felt like the race to build a scalable fault-tolerant quantum computer is actually underway. Like people are no longer merely giving talks about the race or warming up for the race, but running the race.

Within just the last few weeks, we saw the group at Google [announce](https://scottaaronson.blog/?p=8109) that they'd used the Kitaev surface code, with distance 7, to encode one logical qubit using 100 or so physical qubits, in superconducting architecture. They got a net gain: their logical qubit stays alive for maybe twice as long as the underlying physical qubits do. And crucially, they find that their logical coherence time _increases_ as they pass to larger codes, with higher distance, on more physical qubits. With superconducting, there are still limits to how many physical qubits you can stuff onto a chip, and eventually you'll need communication of qubits between chips, which has yet to be demonstrated. But if you could scale Google's current experiment even to 1500 physical qubits, you'd probably be below the threshold where you could use that as a building block for a future scalable fault-tolerant device.

Then, just last week, a collaboration between Microsoft and Quantinuum [announced](https://scottaaronson.blog/?p=8310) that, in the trapped-ion architecture, they applied pretty substantial circuits to logically-encoded qubits---again in a way that gets a net gain in fidelity over not doing error-correction, modulo a debate about whether they're relying too much on postselection. So, they made a GHZ state, which is basically like a Schrödinger cat, out of 12 logically encoded qubits. They also did a "quantum chemistry simulation," which had only two logical qubits, but which required three logical non-Clifford gates--which is the hard kind of gate when you're doing error-correction.

Because of these advances, as well as others--what QuEra is doing with neutral atoms, what PsiQuantum and Xanadu are doing with photonics, etc.--I'm now more optimistic than I've ever been that, if things continue at the current rate, _either_ there are useful fault-tolerant QCs in the next decade, _or else_ something surprising happens to stop that. Plausibly we'll get there not just with one hardware architecture, but with multiple ones, much like the Manhattan Project got a uranium bomb _and_ a plutonium bomb around the same time, so the question will become which one is most economic.

If someone asks me _why_ I'm now so optimistic, the core of the argument is 2-qubit gate fidelities. We've known for years that, at least on paper, quantum fault-tolerance becomes a net win (that is, you sustainably correct errors faster than you introduce new ones) once you have physical 2-qubit gates that are ~99.99% reliable. The problem has "merely" been how far we were from that. When I entered the field, in the late 1990s, it would've been like a _Science_ or _Nature_ paper to do a 2-qubit gate with 50% fidelity. But then at some point the 50% became 90%, became 95%, became 99%, and within the past year, multiple groups have reported 99.9%. So, if you just plot the log of the infidelity as a function of year and stare at it--yeah, _you 'd_ feel pretty optimistic about the next decade too!

Or pessimistic, as the case may be! To any of you who are worried about post-quantum cryptography--by now I'm so used to delivering a message of, _maybe, eventually,_ someone will need to _start thinking about_ migrating from RSA and Diffie-Hellman and elliptic curve crypto to lattice-based crypto, or other systems that could plausibly withstand quantum attack. I think today that message needs to change. I think today the message needs to be: yes, unequivocally, worry about this now. Have a plan.

So, I think this moment is a good one for reflection. We're used to quantum computing having this air of unreality about it. Like sure, we go to conferences, we prove theorems about these complexity classes like BQP and QMA, the experimenters do little toy demos that don't scale. But if this will ever be practical at all, then for all we know, not for another 200 years. It feels really different to think of this as something plausibly imminent. So what I want to do for the rest of this talk is to step back and ask, what are the main reasons why people regarded this as not entirely real? And what can we say about those reasons in light of where we are today?

* * *

**Reason #1**

For the general public, maybe the overriding reason not to take QC seriously has just been that it sounded too good to be true. Like, great, you'll have this magic machine that's gonna exponentially speed up every problem in optimization and machine learning and finance by trying out every possible solution simultaneously, in different parallel universes. Does it also dice peppers?

For this objection, I'd say that our response hasn't changed at all in 30 years, and it's simply, "No, that's not what it will do and not how it will work." We should acknowledge that laypeople and journalists and unfortunately even some investors and government officials have been misled by the people whose job it was to explain this stuff to them.

I think it's important to tell people that the only hope of getting a speedup from a QC is to exploit the way that QM works differently from classical probability theory — in particular, that it involves these numbers called _amplitudes_ , which can be positive, negative, or even complex. With every quantum algorithm, what you're trying to do is choreograph a pattern of interference where for each wrong answer, the contributions to its amplitude cancel each other out, whereas the contributions to the amplitude of the right answer reinforce each other. The trouble is, it's only for a few practical problems that we know how to do that in a way that vastly outperforms the best known classical algorithms.

What are those problems? Here, for all the theoretical progress that's been made in these past decades, I'm going to give the same answer in 2024 that I would've given in 1998. Namely, there's the simulation of chemistry, materials, nuclear physics, or anything else where many-body quantum effects matter. This was Feynman's original application from 1981, but probably _still_ the most important one commercially. It could plausibly help with batteries, drugs, solar cells, high-temperature superconductors, all kinds of other things, maybe even in the next few years.

And then there's breaking public-key cryptography, which is _not_ commercially important, but is important for other reasons well-known to everyone here.

And then there's everything else. For problems in optimization, machine learning, finance, and so on, there's typically a Grover's speedup, but that of course is "only" a square root and not an exponential, which means that it will take much longer before it's relevant in practice. And one of the earliest things we learned in quantum computing theory is that there's no "black-box" way to beat the Grover speedup. By the way, that's also relevant to breaking cryptography — other than the subset of cryptography that's based on abelian groups and can be broken by Shor's algorithm or the like. The centerpiece of my [PhD thesis](https://www.scottaaronson.com/thesis.html), twenty years ago, was the theorem that you can't get more than a Grover-type polynomial speedup for the black-box problem of finding collisions in cryptographic hash functions.

So then what remains? Well, there are all sorts heuristic quantum algorithms for classical optimization and machine learning problems — QAOA (Quantum Approximate Optimization Algorithm), quantum annealing, and so on — and we can hope that _sometimes_ they'll beat the best classical heuristics for the same problems, but it will be trench warfare, not just magically speeding up everything. There are lots of quantum algorithms somehow inspired by the HHL (Harrow-Hassidim-Lloyd) algorithm for solving linear systems, and we can hope that some of those algorithms will get exponential speedups for _end-to-end_ problems that matter, as opposed to problems of transforming one quantum state to another quantum state. We can of course hope that new quantum algorithms will be discovered. And most of all, we can look for entirely new problem domains, where people hadn't even considered using quantum computers before--new orchards in which to pick low-hanging fruit. Recently, [Shih-Han Hung and I](https://arxiv.org/abs/2303.01625), along with others, have proposed using _current_ QCs to generate cryptographically certified random numbers, which could be used in post-state cryptocurrencies like Ethereum. I'm hopeful that people will find other protocol applications of QC like that one — "proof of quantum work." [Another major potential protocol application, which Dan Boneh brought up after my talk, is [quantum one-shot signatures](https://eprint.iacr.org/2020/107).]

Anyway, taken together, I don't think any of this is too good to be true. I think it's genuinely good _and_ probably true!

* * *

**Reason #2**

A second reason people didn't take seriously that QC was actually going to happen was the general thesis of technological stagnation, at least in the physical world. You know, maybe in the 40s and 50s, humans built entirely new types of machines, but nowadays what do we do? We issue press releases. We make promises. We argue on social media.

Nowadays, of course, pessimism about technological progress seems hard to square with the revolution that's happening in AI, _another_ field that spent decades being ridiculed for unfulfilled promises and that's now fulfilling the promises. I'd also speculate that, to the extent there _is_ technological stagnation, most of it is simply that it's become really hard to build new infrastructure—high-speed rail, nuclear power plants, futuristic cities—for legal reasons and NIMBY reasons and environmental review reasons and Baumol's cost disease reasons. But none of that really applies to QC, just like it hasn't applied so far to AI.

* * *

**Reason #3**

A third reason people didn't take this seriously was the sense of "It's been 20 years already, where's my quantum computer?" QC is often compared to fusion power, another technology that's "eternally just over the horizon." (Except, I'm no expert, but there seems to be dramatic progress these days in fusion power too!)

My response to the people who make that complaint was always, like, how much do you know about the history of technology? It took more than a century for heavier-than-air flight to go from correct statements of the basic principle to reality. Universal programmable classical computers surely seemed _more_ fantastical from the standpoint of 1920 than quantum computers seem today, but then a few decades later they were built. Today, AI provides a particularly dramatic example where ideas were proposed a long time ago—neural nets, backpropagation—those ideas were then written off as failures, but no, we now know that the ideas were perfectly sound; it just took a few decades for the scaling of hardware to catch up to the ideas. That's why this objection never had much purchase by me, even _before_ the dramatic advances in experimental quantum error-correction of the last year or two.

* * *

**Reason #4**

A fourth reason why people didn't take QC seriously is that, a century after the discovery of QM, some people still harbor doubts about quantum mechanics itself. Either they _explicitly_ doubt it, like Leonid Levin, Roger Penrose, or Gerard 't Hooft. Or they say things like, "complex Hilbert space in 2n dimensions is a nice _mathematical formalism_ , but mathematical formalism is not reality"--the kind of thing you say when you want to doubt, but not take full intellectual responsibility for your doubts.

I think the only thing for us to say in response, as quantum computing researchers--and the thing I consistently _have_ said--is man, we welcome that confrontation! Let's test quantum mechanics in this new regime. And if, instead of building a QC, we have to settle for "merely" overthrowing quantum mechanics and opening up a new era in physics--well then, I guess we'll have to find some way to live with that.

* * *

**Reason #5**

My final reason why people didn't take QC seriously is the only technical one I'll discuss here. Namely, maybe quantum mechanics is fine but fault-tolerant quantum computing is fundamentally "screened off" or "censored" by decoherence or noise—and maybe the theory of quantum fault-tolerance, which seemed to indicate the opposite, makes unjustified assumptions. This has been the position of Gil Kalai, for example.

The challenge for that position has always been to articulate, what is true about the world instead? Can every realistic quantum system be simulated efficiently by a classical computer? If so, how? What is a model of correlated noise that kills QC without also killing scalable _classical_ computing?—which turns out to be a hard problem.

In any case, I think this position has been dealt a severe blow by the Random Circuit Sampling quantum supremacy experiments of the past five years. Scientifically, the most important thing we've learned from these experiments is that the fidelity seems to decay exponentially with the number of qubits, but "only" exponentially — as it would if the errors were independent from one gate to the next, precisely as the theory of quantum fault-tolerance assumes. So for anyone who believes this objection, I'd say that the ball is now firmly in their court.

* * *

So, if we accept that QC is on the threshold of becoming real, what are the next steps? There are the obvious ones: push forward with building better hardware and using it to demonstrate logical qubits and fault-tolerant operations on them. Continue developing better error-correction methods. Continue looking for new quantum algorithms and new problems for those algorithms to solve.

But there's also a less obvious decision right now. Namely, do we put everything into fault-tolerant qubits, or do we continue trying to demonstrate quantum advantage in the [NISQ](https://arxiv.org/abs/1801.00862) (pre-fault-tolerant) era? There's a case to be made that fault-tolerance will _ultimately_ be needed for scaling, and anything you do without fault-tolerance is some variety of non-scalable circus trick, so we might as well get over the hump now.

But I'd like to advocate putting at least _some_ thought into how to demonstrate a quantum advantage in the near-term. Thay could be via cryptographic protocols, like those that [Kahanamoku-Meyer et al.](https://arxiv.org/abs/2104.00687) have proposed. It could be via pseudorandom peaked quantum circuits, a [recent proposal](https://arxiv.org/abs/2404.14493) by me and Yuxuan Zhang--_if_ we can figure out an efficient way to generate the circuits. Or we could try to demonstrate what William Kretschmer, Harry Buhrman, and I have called ["quantum information supremacy,"](https://arxiv.org/abs/2302.10332) where, instead of computational advantage, you try to do an experiment that directly shows the vastness of Hilbert space, via exponential advantages for quantum communication complexity, for example. I'm optimistic that that might be doable in the very near future, and have been working with Quantinuum to try to do it.

On the one hand, when I started in quantum computing 25 years ago, I reconciled myself to the prospect that I'm going to study what fundamental physics implies about the limits of computation, and maybe I'll never live to see any of it experimentally tested, and that's fine. On the other hand, once you tell me that there _is_ a serious prospect of testing it soon, then I become kind of impatient. Some part of me says, _let 's do this!_ Let's try to achieve forthwith what I've always regarded as the #1 application of quantum computers, more important than codebreaking or even quantum simulation: namely, disproving the people who said that scalable quantum computing was impossible.
