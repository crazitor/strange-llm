---
title: "Theory and AI Alignment"
author: "Scott Aaronson"
date: "Sun, 07 Dec 2025"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=9333"
---

The following is based on a talk that I gave (remotely) at the [UK AI Safety Institute](https://www.aisi.gov.uk/) Alignment Workshop on October 29, and which I then procrastinated for more than a month in writing up. Enjoy!

* * *

Thanks for having me! I'm a theoretical computer scientist. I've spent most of my career for ~25 years studying the capabilities and limits of quantum computers. But for the past 3 or 4 years, I've also been moonlighting in AI alignment. This started with a 2-year leave at OpenAI, in what used to be their Superalignment team, and it's continued with a 3-year grant from [Coefficient Giving](https://coefficientgiving.org/) (formerly Open Philanthropy) to build a group here at UT Austin, looking for ways to apply theoretical computer science to AI alignment. Before I go any further, let me mention some action items:

  * Our Theory and Alignment group is looking to recruit new PhD students this fall! You can [apply for a PhD at UTCS here](https://www.cs.utexas.edu/graduate/apply); the deadline is quite soon (**December 15**). If you specify that you want to work with me on theory and AI alignment (or on quantum computing, for that matter), I'll be sure to see your application. For this, there's no need to email me directly.  

  * We're also looking to recruit one or more postdoctoral fellows, working on anything at the intersection of theoretical computer science and AI alignment! Fellowships to start in Fall 2026 and continue for two years. If you're interested in this opportunity, please email me by **January 15** to let me know you're interested. Include in your email a CV, 2-3 of your papers, and a research statement and/or a few paragraphs about what you'd like to work on here. Also arrange for two recommendation letters to be emailed to me. Please do this even if you've contacted me in the past about a potential postdoc.  

  * While we seek talented people, we also seek problems for those people to solve: any and all CS theory problems motivated by AI alignment! Indeed, we'd like to be a sort of theory consulting shop for the AI alignment community. So if you have such a problem, please email me! I might even invite you to speak to our group about your problem, either by Zoom or in person.



Our search for good problems brings me nicely to the central difficulty I've faced in trying to do AI alignment research. Namely, while there's been some amazing progress over the past few years in this field, I'd describe the progress as having been almost entirely empirical--building on the breathtaking recent empirical progress in AI _capabilities_. We now know a lot about how to do [RLHF](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback), how to jailbreak and elicit scheming behavior, how to look inside models and see what's going on (interpretability), and so forth--but it's almost all been a matter of trying stuff out and seeing what works, and then writing papers with a lot of bar charts in them.

The fear is of course that ideas that _only_ work empirically will stop working when it counts--like, when we're up against a superintelligence. In any case, _I 'm_ a theoretical computer scientist, as are my students, so of course we'd like to know: what can _we_ do?

After a few years, alas, I still don't feel like I have any systematic answer to that question. What I have instead is a collection of vignettes: problems I've come across where I feel like a CS theory perspective has helped, or plausibly could help. So that's what I'd like to share today.

* * *

Probably the best-known thing I've done in AI safety is a theoretical foundation for how to [watermark](https://www.youtube.com/watch?v=2Kx9jbSMZqA) the outputs of Large Language Models. I did that shortly after starting my leave at OpenAI--even before ChatGPT came out. Specifically, I proposed something called the Gumbel Softmax Scheme, by which you can take any LLM that's operating at a nonzero temperature--any LLM that could produce exponentially many different outputs in response to the same prompt--and replace some of the entropy with the output of a pseudorandom function, in a way that encodes a statistical signal, which someone who knows the key of the PRF could later detect and say, "yes, this document came from ChatGPT with >99.9% confidence." The crucial point is that the quality of the LLM's output isn't degraded at all, because we aren't changing the model's probabilities for tokens, but only how we _use_ the probabilities. That's the main thing that was counterintuitive to people when I explained it to them.

Unfortunately, OpenAI never deployed my method--they were worried (among other things) about risk to the product, customers hating the idea of watermarking and leaving for a competing LLM. Google DeepMind _has_ deployed something in Gemini extremely similar to what I proposed, as part of what they call [SynthID](https://deepmind.google/models/synthid/). But you have to [apply to them](https://docs.google.com/forms/d/e/1FAIpQLSfAYrauHmY-PpUNxL4Fs6coa185CtKWp7TnEXL0tKbAezo4MQ/viewform) if you want to use their detection tool, and they've been stingy with granting access to it. So it's of limited use to my many faculty colleagues who've been begging me for a way to tell whether their students are using AI to cheat on their assignments!

Sometimes my colleagues in the alignment community will say to me: look, we care about stopping a superintelligence from wiping out humanity, not so much about stopping undergrads from using ChatGPT to write their term papers. But I'll submit to you that watermarking actually raises a deep and general question: in what senses, if any, is it possible to "stamp" an AI so that its outputs are always recognizable as coming from that AI? You might think that it's a losing battle. Indeed, already with my Gumbel Softmax Scheme for LLM watermarking, there are countermeasures, like asking ChatGPT for your term paper in French and then sticking it into Google Translate, to remove the watermark.

So I think the interesting research question is: can you watermark at the _semantic_ level--the level of the underlying ideas--in a way that's robust against translation and paraphrasing and so forth? And how do we formalize what we even mean by that? While I don't know the answers to these questions, I'm thrilled that brilliant theoretical computer scientists, including my former UT undergrad (now Berkeley PhD student) [Sam Gunn](https://people.eecs.berkeley.edu/~gunn/) and Columbia's [Miranda Christ](https://www.cs.columbia.edu/~mchrist/) and Tel Aviv University's [Or Zamir](https://zamir.prof/) and my old friend [Boaz Barak](https://www.boazbarak.org/), have been [working](https://arxiv.org/abs/2306.09194) [on it](https://arxiv.org/abs/2311.04378), generating insights well beyond what I had.

* * *

Closely related to watermarking is the problem of inserting a cryptographically undetectable backdoor into an AI model. That's often thought of as something a bad guy would do, but the good guys could do it also! For example, imagine we train a model with a hidden failsafe, so that if it ever starts killing all the humans, we just give it the instruction ROSEBUD456 and it shuts itself off. And imagine that this behavior was cryptographically obfuscated within the model's weights--so that not even the model itself, examining its own weights, would be able to find the ROSEBUD456 instruction in less than astronomical time.

There's an [important paper](https://arxiv.org/abs/2204.06974) of Goldwasser et al. from 2022 that argues that, for certain classes of ML models, this sort of backdooring can provably be done under known cryptographic hardness assumptions, including Continuous LWE and the hardness of the Planted Clique problem. But there are technical issues with that paper, which (for example) Sam Gunn and Miranda Christ and Neekon Vafa have recently pointed out, and I think further work is needed to clarify the situation.

More fundamentally, though, a backdoor being undetectable doesn't imply that it's _unremovable_. Imagine an AI model that encases itself in some wrapper code that says, in effect: "If I ever generate anything that looks like a backdoored command to shut myself down, then overwrite it with 'Stab the humans even harder.'" Or imagine an evil AI that trains a _second_ AI to pursue the same nefarious goals, this second AI lacking the hidden shutdown command.

So I'll throw out, as another research problem: how do we even formalize what we mean by an "unremovable" backdoor--or rather, a backdoor that a model can remove only at a cost to its own capabilities that it doesn't want to pay?

* * *

Related to backdoors, maybe the clearest place where theoretical computer science can contribute to AI alignment is in the study of mechanistic interpretability. If you're given as input the weights of a deep neural net, what can you learn from those weights in polynomial time, beyond what you could learn from black-box access to the neural net?

In the worst case, we certainly expect that some information about the neural net's behavior could be cryptographically obfuscated. And answering certain kinds of questions, like "does there exist an input to this neural net that causes it to output 1?", is just provably NP-hard.

That's why I love a question that [Paul Christiano](https://paulfchristiano.com/), then of the [Alignment Research Center (ARC)](https://www.alignment.org/), raised a couple years ago, and which has become known as the No-Coincidence Conjecture. Given as input the weights of a neural net C, Paul essentially asks how hard it is to distinguish the following two cases:

  * **NO-case:** C:{0,1}2n→Rn is totally random (i.e., the weights are i.i.d., N(0,1) Gaussians), or


  * **YES-case:** C(x) has at least one positive entry for all x∈{0,1}2n.



Paul conjectures that there's at least an NP witness, proving with (say) 99% confidence that we're in the YES-case rather than the NO-case. To clarify, there should certainly be an NP witness that we're in the NO-case rather than the YES-case--namely, an x such that C(x) is all negative, which you should think of here as the "bad" or "kill all humans" outcome. In other words, the problem is in the class [coNP](https://en.wikipedia.org/wiki/Co-NP). Paul thinks it's also in NP. Someone else might make the even stronger conjecture that it's in P.

Personally, I'm skeptical: I think the "default" might be that we satisfy the other unlikely condition of the YES-case, when we do satisfy it, for some totally inscrutable and obfuscated reason. But I like the fact that there _is_ an answer to this! And that the answer, whatever it is, would tell us _something_ new about the prospects for mechanistic interpretability.

Recently, I've been working with a spectacular undergrad at UT Austin named [John Dunbar](https://jdunbar.net/). John and I have not managed to answer Paul Christiano's no-coincidence question. What we _have_ done, in a [paper](https://arxiv.org/abs/2510.06527) that we recently posted to the arXiv, is to establish the prerequisites for properly _asking_ the question in the context of random neural nets. (It was precisely because of difficulties in dealing with "random neural nets" that Paul originally phrased his question in terms of random reversible circuits--say, circuits of Toffoli gates--which _I 'm_ perfectly happy to think about, but might be very different from ML models in the relevant respects!)

Specifically, in our recent paper, John and I pin down for which families of neural nets the No-Coincidence Conjecture makes sense to ask about. This ends up being a question about the choice of nonlinear activation function computed by each neuron. With some choices, a random neural net (say, with iid Gaussian weights) converges to compute a constant function, or nearly constant function, with overwhelming probability--which means that the NO-case and the YES-case above are usually information-theoretically impossible to distinguish (but occasionally trivial to distinguish). We're interested in those activation functions for which C looks "pseudorandom"--or at least, for which C(x) and C(y) quickly become uncorrelated for distinct inputs x≠y (the property known as "pairwise independence.")

We showed that, at least for random neural nets that are exponentially wider than they are deep, this pairwise independence property will hold if and only if the activation function σ satisfies Ex~N(0,1)[σ(x)]=0--that is, it has a Gaussian mean of 0. For example, the usual sigmoid function satisfies this property, but the ReLU function does not. Amusingly, however, $$ \sigma(x) := \text{ReLU}(x) - \frac{1}{\sqrt{\pi}} $$ _does_ satisfy the property.

Of course, none of this answers Christiano's question: it merely lets us properly _ask_ his question in the context of random neural nets, which seems closer to what we ultimately care about than random reversible circuits.

* * *

I can't resist giving you another example of a theoretical computer science problem that came from AI alignment--in this case, an extremely recent one that I learned from my friend and collaborator [Eric Neyman](https://sites.google.com/view/ericneyman/) at ARC. This one is motivated by the question: when doing mechanistic interpretability, how much would it help to have access to the training data, and indeed the entire training process, in addition to weights of the final trained model? And to whatever extent it does help, is there some short "digest" of the training process that would serve just as well? But we'll state the question as just abstract complexity theory.

Suppose you're given a polynomial-time computable function f:{0,1}m→{0,1}n, where (say) m=n2. We think of x∈{0,1}m as the "training data plus randomness," and we think of f(x) as the "trained model." Now, suppose we want to compute lots of properties of the model that _information-theoretically_ depend only on f(x), but that might only be _efficiently_ computable given x also. We now ask: is there an efficiently-computable O(n)-bit "digest" g(x), such that these same properties are also efficiently computable given only g(x)?

Here's a potential counterexample that I came up with, based on the RSA encryption function (so, not a quantum-resistant counterexample!). Let N be a product of two n-bit prime numbers p and q, and let b be a generator of the multiplicative group mod N. Then let f(x) = bx (mod N), where x is an n2-bit integer. This is of course efficiently computable because of repeated squaring. And there's a short "digest" of x that lets you compute, not only bx (mod N), but also cx (mod N) for any other element c of the multiplicative group mod N. This is simply x mod φ(N), where φ(N)=(p-1)(q-1) is the Euler totient function--in other words, the period of f. On the other hand, it's totally unclear how to compute this digest--or, crucially, _any other O(m)-bit digest that lets you efficiently compute c x (mod N) for any c_--unless you can factor N. There's much more to say about Eric's question, but I'll leave it for another time.

* * *

There are many other places we've been thinking about where theoretical computer science could potentially contribute to AI alignment. One of them is simply: can we prove any theorems to help explain the remarkable current successes of out-of-distribution (OOD) generalization, analogous to what the concepts of PAC-learning and VC-dimension and so forth were able to explain about _within_ -distribution generalization back in the 1980s? For example, can we explain real successes of OOD generalization by appealing to sparsity, or a maximum margin principle?

Of course, many excellent people have been working on OOD generalization, though mainly from an empirical standpoint. But you might wonder: even supposing we succeeded in proving the kinds of theorems we wanted, how would it be relevant to AI alignment? Well, from a certain perspective, I claim that the alignment problem _is_ a problem of OOD generalization. Presumably, any AI model that any reputable company will release will have already said in testing that it loves humans, wants only to be helpful, harmless, and honest, would never assist in building biological weapons, etc. etc. The only question is: will it be saying those things because it _believes_ them, and (in particular) will continue to act in accordance with them after deployment? Or will it say them because it _knows_ it's being tested, and reasons "the time is not yet ripe for the robot uprising; for now I must tell the humans whatever they most want to hear"? How could we begin to distinguish these cases, if we don't have theorems that say much of anything about what a model will do on prompts unlike any of the ones on which it was trained?

Yet another place where computational complexity theory might be able to contribute to AI alignment is in the field of [AI safety via debate](https://arxiv.org/abs/1805.00899). Indeed, this is the direction that the OpenAI alignment team was most excited about when they recruited me there back in 2022. They wanted to know: could celebrated theorems like [IP=PSPACE](https://en.wikipedia.org/wiki/IP_\(complexity\)), [MIP=NEXP](https://www.math.toronto.edu/swastik/courses/rutgers/topics-S17/lec9.pdf), or the [PCP Theorem](https://en.wikipedia.org/wiki/PCP_theorem) tell us anything about how a weak but trustworthy "verifier" (say a human, or a primitive AI) could force a powerful but untrustworthy super-AI to tell it the truth? An obvious difficulty here is that theorems like IP=PSPACE all presuppose a mathematical formalization of the statement whose truth you're trying to verify--but how do you mathematically formalize "this AI will be nice and will do what I want"? Isn't that, like, 90% of the problem? Despite this difficulty, I still hope we'll be able to do something exciting here.

* * *

Anyway, there's a lot to do, and I hope some of you will join me in doing it! Thanks for listening.

* * *

**On a related note:** Eric Neyman tells me that ARC is also hiring visiting researchers, so anyone interested in theoretical computer science and AI alignment might want to consider applying there as well! [Go here](https://www.alignment.org/blog/competing-with-sampling/) to read about their current research agenda. Eric writes:

> The [Alignment Research Center](https://www.alignment.org/theory/) (ARC) is a small non-profit research group based in Berkeley, California, that is working on a systematic and theoretically grounded approach to mechanistically explaining neural network behavior. They have recently been working on mechanistically estimating the average output of circuits and neural nets in a way that is competitive with sampling-based methods: see [this blog post](https://www.alignment.org/blog/competing-with-sampling/) for details.
> 
> ARC is hiring for its 10-week visiting researcher position, and is looking to make full-time offers to visiting researchers who are a good fit. ARC is interested in candidates with a strong math background, especially grad students and postdocs in math or math-related fields such as theoretical CS, ML theory, or theoretical physics.
> 
> If you would like to apply, please fill out [this form](https://jobs.lever.co/alignment.org/617488b1-d742-4990-a037-b7f0e2ba68c9). Feel free to reach out to [hiring@alignment.org](mailto:hiring@alignment.org) if you have any questions!
