---
title: "Google’s Sycamore chip: no wormholes, no superfast classical simulation either"
author: "Scott Aaronson"
date: "Fri, 02 Dec 2022"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=6871"
---

**Update (Dec. 6):** I'm having a blast at the [Workshop on Spacetime and Quantum Information](https://www.ias.edu/sns/scientific-program-qubit-2022) at the Institute for Advanced Study in Princeton. I'm learning a huge amount from the talks and discussions here--and also simply enjoying being back in Princeton, to see old friends and visit old haunts like the [Bent Spoon](https://palmersquare.com/directory/the-bent-spoon/). Tomorrow I'll speak about my [recent work with Jason Pollack](https://arxiv.org/abs/2210.15601) on polynomial-time AdS bulk reconstruction. [[New: click here for video of my talk!]](https://www.youtube.com/watch?v=DLjsRy6fKXo&t=1s)

But there's one thing, relevant to this post, that I can't let pass without comment. Tonight, David Nirenberg, Director of the IAS and a medieval historian, gave an after-dinner speech to our workshop, centered around how auspicious it was that the workshop was being held a mere week after the momentous announcement of _a holographic wormhole on a microchip (!!)_ --a feat that experts were calling the first-ever laboratory investigation of quantum gravity, and a new frontier for experimental physics itself. Nirenberg asked whether, a century from now, people might look back on the wormhole achievement as today we look back on Eddington's 1919 eclipse observations providing the evidence for general relativity.

I confess: this was the first time I felt visceral anger, rather than mere bemusement, over this wormhole affair. Before, I had implicitly assumed: no one was _actually_ hoodwinked by this. No one _really, literally_ believed that this little 9-qubit simulation opened up a wormhole, or helped prove the holographic nature of the real universe, or anything like that. I was wrong.

To be clear, I don't blame Professor Nirenberg at all. If _I_ were a medieval historian, everything he said about the experiment's historic significance might strike me as perfectly valid inferences from what I'd read in the press. I don't blame the It from Qubit community--most of which, I can report, was grinding its teeth and turning red in the face right alongside me. I don't even blame most of the authors of the wormhole paper, such as Daniel Jafferis, who gave a perfectly sober, reasonable, technical talk at the workshop about how he and others managed to compress a simulation of a variant of the SYK model into a mere 9 qubits--a talk that eschewed all claims of historic significance and of literal wormhole creation.

But it's now clear to me that, between

(1) the It from Qubit community that likes to explore speculative ideas like holographic wormholes, and

(2) the lay news readers who are now under the impression that Google just did one of the greatest physics experiments of all time,

_something_ went terribly wrong--something that risks damaging trust in the scientific process itself. And I think it's worth reflecting on what we can do to prevent it from happening again.

* * *

This is going to be one of the many _Shtetl-Optimized_ posts that I didn't feel like writing, but was given no choice but to write.

News, social media, and my inbox have been abuzz with two claims about Google's Sycamore quantum processor, the one that now has 72 superconducting qubits.

The first claim is that Sycamore created a wormhole (!)--a historic feat possible only with a quantum computer. See for example the _[New York Times](https://www.nytimes.com/2022/11/30/science/physics-wormhole-quantum-computer.html)_ and _[Quanta](https://www.quantamagazine.org/physicists-create-a-wormhole-using-a-quantum-computer-20221130/)_ and _[Ars Technica](https://arstechnica.com/science/2022/12/no-physicists-didnt-make-a-real-wormhole-what-they-did-was-still-pretty-cool/)_ and _[Nature](https://www.nature.com/articles/d41586-022-03832-z)_ (and of course, the [actual paper](https://www.nature.com/articles/s41586-022-05424-3)), as well as [Peter Woit's blog](https://www.math.columbia.edu/~woit/wordpress/?p=13181) and [Chad Orzel's blog](https://chadorzel.substack.com/p/wormhole-to-2006).

The second claim is that Sycamore's pretensions to quantum supremacy have been refuted. The latter claim is based on [this recent preprint](https://arxiv.org/abs/2211.03999) by Dorit Aharonov, Xun Gao, Zeph Landau, Yunchao Liu, and Umesh Vazirani. No one--least of all me!--doubts that these authors have proved a strong new technical result, solving a significant open problem in the theory of noisy random circuit sampling. On the other hand, it might be less obvious how to interpret their result and put it in context. See also a [YouTube video](https://www.youtube.com/watch?v=zDnA1gu4QO0) of Yunchao speaking about the new result at this week's Simons Institute Quantum Colloquium, and of a panel discussion afterwards, where Yunchao, Umesh Vazirani, Adam Bouland, Sergio Boixo, and your humble blogger discuss what it means.

On their face, the two claims about Sycamore might seem to be in tension. After all, if Sycamore can't do anything beyond what a classical computer can do, then how exactly did it _bend the topology of spacetime_?

I submit that neither claim is true. On the one hand, Sycamore did not "create a wormhole." On the other hand, it remains pretty hard to simulate with a classical computer, as far as anyone knows. To summarize, then, our knowledge of what Sycamore can and can't do remains much the same as last week or last month!

* * *

Let's start with the wormhole thing. I can't really improve over how I put it in Dennis Overbye's _NYT_ piece:

> “The most important thing I’d want New York Times readers to understand is this,” Scott Aaronson, a quantum computing expert at the University of Texas in Austin, wrote in an email. “If this experiment has brought a wormhole into actual physical existence, then a strong case could be made that you, too, bring a wormhole into actual physical existence every time you sketch one with pen and paper.”

More broadly, Overbye's _NYT_ piece explains with admirable clarity what this experiment did and didn't do--leaving only the question "wait … if that's all that's going on here, then why is it being written up in the _NYT_??" This is a rare case where, in my opinion, the _NYT_ did a much better job than _Quanta_ , which unequivocally accepted and amplified the "QC creates a wormhole" framing.

Alright, but what's the actual basis for the "QC creates a wormhole" claim, for those who don't want to leave this blog to read about it? Well, the authors used 9 of Sycamore's 72 qubits to do a crude simulation of something called the [SYK (Sachdev-Ye-Kitaev) model](https://en.wikipedia.org/wiki/Sachdev%E2%80%93Ye%E2%80%93Kitaev_model). SYK has become popular as a toy model for quantum gravity. In particular, it has a holographic dual description, which can indeed involve a spacetime with one or more wormholes. So, they ran a quantum circuit that crudely modelled the SYK dual of a scenario with information sent through a wormhole. They then confirmed that the circuit did what it was supposed to do--i.e., what they’d already classically calculated that it _would_ do.

So, the objection is obvious: if someone simulates a black hole on their classical computer, they don't say they thereby "created a black hole." Or if they do, journalists don't uncritically repeat the claim. Why should the standards be different just because we're talking about a quantum computer rather than a classical one?

Did we at least _learn anything new_ about SYK wormholes from the simulation? Alas, not really, because 9 qubits take a mere 29=512 complex numbers to specify their wavefunction, and are therefore trivial to simulate on a laptop. There's some argument in the paper that, if the simulation were scaled up to (say) 100 qubits, then maybe we _would_ learn something new about SYK. Even then, however, we'd mostly learn about certain corrections that arise _because_ the simulation was being done with "only" n=100 qubits, rather than in the n→∞ limit where SYK is rigorously understood. But while those corrections, arising when n is "neither too large nor too small," would surely be interesting to specialists, they'd have no obvious bearing on the prospects for creating real physical wormholes in our universe.

And yet, this is not a sensationalistic misunderstanding invented by journalists. Some prominent quantum gravity theorists themselves--including some of my close friends and collaborators--persist in talking about the simulated SYK wormhole as "actually being" a wormhole. What are they thinking?

Daniel Harlow explained the thinking to me as follows (he stresses that he's explaining it, not necessarily endorsing it). If you had two entangled quantum computers, one on Earth and the other in the Andromeda galaxy, and if they were both simulating SYK, and if Alice on Earth and Bob in Andromeda both _uploaded their own brains into their respective quantum simulations_ , then it seems possible that the simulated Alice and Bob could have the experience of jumping into a wormhole and meeting each other in the middle. Granted, they couldn't get a message back _out_ from the wormhole, at least not without "going the long way," which could happen only at the speed of light--so only simulated-Alice and simulated-Bob themselves could ever _test_ this prediction. Nevertheless, _if true_ , I suppose some would treat it as grounds for regarding a quantum simulation of SYK as "more real" or "more wormholey" than a classical simulation.

Of course, this scenario depends on strong assumptions not merely about quantum gravity, but _also_ about the metaphysics of consciousness! And I'd _still_ prefer to call it a simulated wormhole for simulated people.

For completeness, here's Harlow's passage from the _NYT_ article:

> Daniel Harlow, a physicist at M.I.T. who was not involved in the experiment, noted that the experiment was based on a model of quantum gravity that was so simple, and unrealistic, that it could just as well have been studied using a pencil and paper.
> 
> “So I’d say that this doesn’t teach us anything about quantum gravity that we didn’t already know,” Dr. Harlow wrote in an email. “On the other hand, I think it is exciting as a technical achievement, because if we can’t even do this (and until now we couldn’t), then simulating more interesting quantum gravity theories would CERTAINLY be off the table.” Developing computers big enough to do so might take 10 or 15 years, he added.

* * *

Alright, let's move on to the claim that quantum supremacy has been refuted. What Aharonov et al. actually show in their [new work](https://arxiv.org/abs/2211.03999), building on [earlier work by Gao and Duan](https://arxiv.org/abs/1810.03176), is that Random Circuit Sampling, with a constant rate of noise per gate and no error-correction, can't provide a _scalable_ approach to quantum supremacy. Or more precisely: as the number of qubits n goes to infinity, and assuming you're in the "anti-concentration regime" (which in practice probably means: the depth of your quantum circuit is at least ~log(n)), there's a classical algorithm to approximately sample the quantum circuit's output distribution in poly(n) time (albeit, not yet a practical algorithm).

Here's what's crucial to understand: this is _100% consistent_ with what those of us working on quantum supremacy had assumed since at least 2016! We _knew_ that if you tried to scale Random Circuit Sampling to 200 or 500 or 1000 qubits, while you also increased the circuit depth proportionately, the signal-to-noise ratio would become exponentially small, meaning that your quantum speedup would disappear. That's why, from the very beginning, we targeted the "practical" regime of 50-100 qubits: a regime where

  1. you can still see explicitly that you're exploiting a 250- or 2100-dimensional Hilbert space for computational advantage, thereby confirming one of the main predictions of quantum computing theory, but
  2. you _also_ have a signal that (as it turned out) is large enough to see with heroic effort. 



To their credit, Aharonov et al. explain all this perfectly clearly in their abstract and introduction. I'm just worried that _others_ aren't reading their paper as carefully as they should be!

So then, what's the new advance in the Aharonov et al. paper? Well, there had been some hope that circuit depth ~log(n) might be a sweet spot, where an exponential quantum speedup might both exist _and_ survive constant noise, even in the asymptotic limit of n→∞ qubits. Nothing in Google's or USTC's actual Random Circuit Sampling experiments depended on that hope, but it would've been nice if it were true. What Aharonov et al. have now done is to kill that hope, using powerful techniques involving summing over Feynman paths in the Pauli basis.

Stepping back, what _is_ the current status of quantum supremacy based on Random Circuit Sampling? I would say it's still standing, but more precariously than I'd like--underscoring the need for new and better quantum supremacy experiments. In more detail, [Pan, Chen, and Zhang](https://arxiv.org/abs/2111.03011) have shown how to simulate Google's 53-qubit Sycamore chip classically, using what I estimated to be 100-1000X the electricity cost of running the quantum computer itself (_including_ the dilution refrigerator!). Approaching from the problem from a different angle, [Gao et al.](https://arxiv.org/abs/2112.01657) have given a polynomial-time classical algorithm for spoofing Google's Linear Cross-Entropy Benchmark (LXEB)--_but_ their algorithm can currently achieve only about 10% of the excess in LXEB that Google's experiment found.

So, though it's been under sustained attack from multiple directions these past few years, I'd say that the flag of quantum supremacy yet waves. The Extended Church-Turing Thesis is still on thin ice. The wormhole is still open. Wait … _no_ … that's not what I meant to write…

* * *

**Note:** With this post, as with future science posts, _all off-topic comments will be ruthlessly left in moderation_. Yes, even if the comments "create their own reality" full of anger and disappointment that I talked about what I talked about, instead of what the commenter wanted me to talk about. Even if merely _refuting_ the comments would require me to give in and talk about their preferred topics after all. Please stop. This is a wormholes-'n-supremacy post.
