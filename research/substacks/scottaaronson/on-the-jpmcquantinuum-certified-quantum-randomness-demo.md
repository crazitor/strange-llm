---
title: "On the JPMC/Quantinuum certified quantum randomness demo"
author: "Scott Aaronson"
date: "Wed, 26 Mar 2025"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=8746"
---

These days, any quantum computing post I write ought to begin with the disclaimer that the armies of Sauron are triumphing around the globe, this is the darkest time for humanity most of us have ever known, and nothing else matters by comparison. Certainly not quantum computing. Nevertheless stuff happens in quantum computing and it often brings me happiness to blog about it--certainly more happiness than doomscrolling or political arguments.

* * *

So then: today JP Morgan Chase announced that, together with Quantinuum and DoE labs, they've experimentally demonstrated the protocol I proposed in 2018, and further developed in a [STOC'2023 paper with Shih-Han Hung](https://arxiv.org/abs/2303.01625), for using current quantum supremacy experiments to generate certifiable random bits for use in cryptographic applications. [See here for our paper in _Nature_](https://www.nature.com/articles/s41586-025-08737-1)--the JPMC team was gracious enough to include me and Shih-Han as coauthors.

Mirroring a conceptual split in the protocol itself, Quantinuum handled the quantum hardware part of my protocol, while JPMC handled the rest: modification of the protocol to make it suitable for trapped ions, as well as software to generate pseudorandom challenge circuits to send to the quantum computer over the Internet, then to verify the correctness of the quantum computer's outputs (thereby ensuring, under reasonable complexity assumptions, that the outputs contained at least a certain amount of entropy), and finally to extract nearly uniform random bits from the outputs. The experiment used Quantinuum's 56-qubit trapped-ion quantum computer, which was given and took a couple seconds to respond to each challenge. Verification of the outputs was done using the Frontier and Summit supercomputers. The team estimates that about 70,000 certified random bits were generated over 18 hours, in such a way that, using the best currently-known attack, you'd need _at least_ about four Frontier supercomputers working continuously to spoof the quantum computer's outputs, and get the verifier to accept non-random bits.

We should be clear that this gap, though impressive from the standpoint of demonstrating quantum supremacy with trapped ions, is not yet good enough for high-stakes cryptographic applications (more about that later). Another important caveat is that the parameters of the experiment aren't yet good enough for my and Shih-Han's formal security reduction to give assurances: instead, for the moment one only has "practical security," or security against a class of simplified yet realistic attackers. I hope that future experiments will build on the JPMC/Quantinuum achievement and remedy these issues.

* * *

The story of this certified randomness protocol starts seven years ago, when I had lunch with [Or Sattath](https://orsattath.wordpress.com/about/) at a Japanese restaurant in Tel Aviv. Or told me that I needed to pay more attention to the then-recent [Quantum Lightning](https://arxiv.org/abs/1711.02276) paper by Mark Zhandry. I already know that paper is great, I said. You don't know the half of it, Or replied. As one byproduct of what he's doing, for example, Mark gives a way to measure quantum money states in order to get certified random bits--bits whose genuine randomness (_not_ pseudorandomness) is certified by computational intractability, something that wouldn't have been possible in a classical world.

Well, why do you even need quantum money states for that? I asked. Why not just use, say, a quantum supremacy experiment based on Random Circuit Sampling, like the one Google is now planning to do (i.e., the experiment Google [_would_ do](https://www.nature.com/articles/s41586-019-1666-5), a year later after this conversation)? Then, the more I thought about that question, the more I liked the idea that these "useless" Random Circuit Sampling experiments would do something potentially useful _despite themselves_ , generating certified entropy as just an inevitable byproduct of passing our benchmarks for sampling from certain classically-hard probability distributions. Over the next couple weeks, I worked out some of the technical details of the security analysis (though not all! it was a big job, and one that only got finished years later, when I brought Shih-Han to UT Austin as a postdoc and worked with him on it for a year).

I emailed the Google team about the idea; they responded enthusiastically. I also got in touch with UT Austin's intellectual property office to file a provisional patent, the only time I've done that my career. UT and I successfully licensed the patent to Google, though the license lapsed when Google's priorities changed. Meantime, a couple years ago, when I visited Quantinuum's lab in Broomfield, Colorado, I learned that a JPMC-led collaboration toward an experimental demonstration of the protocol was then underway. The protocol was well-suited to Quantinuum's devices, particularly given their ability to apply two-qubit gates with all-to-all connectivity and fidelity approaching 99.9%.

I should mention that, in the intervening years, others had _also_ studied the use of quantum computers to generate cryptographically certified randomness; indeed it became a whole subarea of quantum computing. See especially the [seminal work](https://arxiv.org/abs/1804.00640) of Brakerski, Christiano, Mahadev, Vazirani, and Vidick, which gave a certified randomness protocol that (unlike mine) relies only on standard cryptographic assumptions and allows verification in classical polynomial time. The "only" downside is that implementing their protocol securely seems to require a full fault-tolerant quantum computer (capable of things like Shor's algorithm), rather than current noisy devices with 50-100 qubits.

* * *

> For the rest of this post, I'll share a little FAQ, adapted from my answers to a journalist's questions. Happy to answer additional questions in the comments. 
> 
>   * To what extent is this a world-first?
> 


Well, it’s the first experimental demonstration of a protocol to generate cryptographically certified random bits with the use of a quantum computer.

To remove any misunderstanding: if you’re just talking about the use of quantum phenomena to generate random bits, without _certifying_ the randomness of those bits to a faraway skeptic, then that’s been easy to do for generations (just stick a Geiger counter next to some radioactive material!). The new part, the part that requires a quantum computer, is all about the certification.

Also: if you’re talking about the use of separated, entangled parties to generate certified random bits by violating the Bell inequality (see eg [here](https://arxiv.org/abs/1111.6054)) — that approach does give certification, but the downside is that you need to believe that the two parties really are unable to communicate with each other, something that you couldn’t certify in practice over the Internet. A quantum-computer-based protocol like mine, by contrast, requires just a single quantum device.

>   * Why is the certification element important?
> 


In any cryptographic application where you need to distribute random bits over the Internet, the fundamental question is, why should everyone trust that these bits are truly random, rather than being backdoored by an adversary?

This isn’t so easy to solve.  If you consider any classical method for generating random bits, an adversary could substitute a cryptographic pseudorandom generator without anyone being the wiser.

The key insight behind the quantum protocol is that a quantum computer can solve certain problems efficiently, but _only_ (it’s conjectured, and proven under plausible assumptions) by sampling an answer randomly — thereby giving you certified randomness, once you verify that the quantum computer really has solved the problem in question. Unlike with a classical computer, there’s no way to substitute a pseudorandom generator, since randomness is just an inherent part of a quantum computer’s operation — specifically, when the entangled superposition state randomly collapses on measurement.

>   * What are the applications and possible uses?
> 


One potential application is to proof-of-stake cryptocurrencies, like Ethereum.  These cryptocurrencies are vastly more energy-efficient than “proof-of-work” cryptocurrencies (like Bitcoin), but they require lotteries to be run constantly to decide which currency holder gets to add the next block to the blockchain (and get paid for it).  Billions of dollars are riding on these lotteries being fair.

Other potential applications are to zero-knowledge protocols, lotteries and online gambling, and deciding which precincts to audit in elections. [See here](https://arxiv.org/abs/2503.19759) for a nice perspective article that JPMC put together discussing these and other potential applications.

Having said all this, a **major problem** right now is that verifying the results using a classical computer is extremely expensive — indeed, basically as expensive as spoofing the results would be. This problem, and other problems related to verification (eg “why should everyone else trust the verifier?”), are the reasons why most people will probably pass on this solution in the near future, and generate random bits in simpler, non-quantum-computational ways.

We do know, from e.g. Brakerski et al.'s work, that the problem of making the verification fast is solvable _with sufficient advancements in quantum computing hardware_. Even without hardware advancements, it might also be solvable with new theoretical ideas — one of my favorite research directions.

>   * Is this is an early win for quantum computing?
> 


It’s not directly an advancement in quantum computing hardware, but yes, it’s a very nice _demonstration_ of such advancements — of something that’s possible today but wouldn’t have been possible just a few short years ago. It’s a step toward using current, non-error-corrected quantum computers for a practical application that’s not itself about quantum mechanics but that really does inherently require quantum computers.

Of course it’s personally gratifying to see something I developed get experimentally realized after seven years. Huge congratulations to the teams at JP Morgan Chase and Quantinuum, and thanks to them for the hard work they put into this.

* * *

**Unrelated Announcement:** [See here](https://www.youtube.com/watch?v=WB9bvr_Nf4w) for a podcast about quantum computing that I recorded with, of all organizations, the FBI. As I told the gentlemen who interviewed me, I'm glad the FBI still _exists_ , let alone its podcast!
