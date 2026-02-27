---
title: "It’s hard to think when someone Hadamards your brain"
author: "Scott Aaronson"
date: "Tue, 25 Sep 2018"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=3975"
---

"Unperformed measurements have no results." --[Asher Peres](https://en.wikipedia.org/wiki/Asher_Peres)

* * *

With two looming paper deadlines, two rambunctious kids, an undergrad class, program committee work, faculty recruiting, and an imminent trip to Capitol Hill to answer congressional staffers' questions about quantum computing (and for good measure, to give talks at UMD and Johns Hopkins), the only sensible thing to do is to spend my time writing a blog post.

So: a bunch of people asked for my reaction to the new _Nature Communications_ paper by Daniela Frauchiger and Renato Renner, provocatively titled ["Quantum theory cannot consistently describe the use of itself."](https://www.nature.com/articles/s41467-018-05739-8) Here's the abstract:

Quantum theory provides an extremely accurate description of fundamental processes in physics. It thus seems likely that the theory is applicable beyond the, mostly microscopic, domain in which it has been tested experimentally. Here, we propose a Gedankenexperiment to investigate the question whether quantum theory can, in principle, have universal validity. The idea is that, if the answer was yes, it must be possible to employ quantum theory to model complex systems that include agents who are themselves using quantum theory. Analysing the experiment under this presumption, we find that one agent, upon observing a particular measurement outcome, must conclude that another agent has predicted the opposite outcome with certainty. The agents’ conclusions, although all derived within quantum theory, are thus inconsistent. This indicates that quantum theory cannot be extrapolated to complex systems, at least not in a straightforward manner.

I first encountered Frauchiger and Renner's argument back in July, when Renner (who I've known for years, and who has many beautiful results in quantum information) presented it at a summer school in Boulder, CO where I was also lecturing. I was sufficiently interested (or annoyed?) that I pulled an all-nighter working through the argument, then discussed it at lunch with Renner as well as John Preskill. I enjoyed figuring out exactly where I get off Frauchiger and Renner's train--since I _do_ get off their train. While I found their paper thought-provoking, I reject the contention that there's any new problem with QM's logical consistency: for reasons I'll explain, I think there's only the same quantum weirdness that (to put it mildly) we've known about for quite some time.

In more detail, the paper makes a big deal about how the new argument rests on just three assumptions (briefly, QM works, measurements have definite outcomes, and the "transitivity of knowledge"); and how if you reject the argument, then you must reject at least one of the three assumptions; and how different interpretations (Copenhagen, Many-Worlds, Bohmian mechanics, etc.) make different choices about what to reject.

But I reject an assumption that Frauchiger and Renner never formalize. That assumption is, basically: "it makes sense to chain together statements that involve superposed agents measuring each other's brains in different incompatible bases, as if the statements still referred to a world where these measurements weren't being done." I say: in QM, even statements that look "certain" in isolation might really mean something like "_if_ measurement X is performed, _then_ Y will certainly be a property of the outcome." The trouble arises when we have multiple such statements, involving different measurements X1, X2, …, and (let's say) performing X1 destroys the original situation in which we were talking about performing X2.

But I'm getting ahead of myself. The first thing to understand about Frauchiger and Renner's argument is that, as they acknowledge, it's not entirely new. As Preskill helped me realize, the argument can be understood as simply the "[Wigner's-friendification](https://en.wikipedia.org/wiki/Wigner%27s_friend)" of [Hardy's Paradox](https://en.wikipedia.org/wiki/Hardy%27s_paradox). In other words, the new paradox is exactly what you get if you take Hardy's paradox from 1992, and promote its entangled qubits to the status of conscious observers who are in superpositions over thinking different thoughts. Having talked to Renner about it, I don't think he fully endorses the preceding statement. But since _I_ fully endorse it, let me explain the two ingredients that I think are getting combined here--starting with Hardy's paradox, which I confess I didn't know (despite knowing Lucien Hardy himself!) before the Frauchiger-Renner paper forced me to learn it.

Hardy's paradox involves the two-qubit entangled state

$$\left|\psi\right\rangle = \frac{\left|00\right\rangle + \left|01\right\rangle + \left|10\right\rangle}{\sqrt{3}}.$$

And it involves two agents, Alice and Bob, who measure the left and right qubits respectively, both in the {|+〉,|-〉} basis. Using the Born rule, we can straightforwardly calculate the probability that Alice and Bob both see the outcome |-〉 as 1/12.

So what's the paradox? Well, let me now "prove" to you that Alice and Bob can _never_ both get |-〉. Looking at |ψ〉, we see that conditioned on Alice's qubit being in the state |0〉, Bob's qubit is in the state |+〉, so Bob can never see |-〉. And conversely, conditioned on Bob's qubit being in the state |0〉, Alice's qubit is in the state |+〉, so Alice can never see |-〉. OK, but since |ψ〉 has no |11〉 component, at least one of the two qubits _must_ be in the state |0〉, so therefore at least one of Alice and Bob must see |+〉!

When it's spelled out so plainly, the error is apparent. Namely, what do we even  _mean_ by a phrase like "conditioned on Bob's qubit being in the state |0〉," unless Bob actually _measured_ his qubit in the {|0〉,|1〉} basis? But if Bob measured his qubit in the {|0〉,|1〉} basis, then we'd be talking about a different, counterfactual experiment. In the actual experiment, Bob measures his qubit only in the {|+〉,|-〉} basis, and Alice does likewise. As Asher Peres put it, "unperformed measurements have no results."

Anyway, as I said, if you strip away the words and look only at the actual setup, it seems to me that Frauchiger and Renner's contribution is basically to combine Hardy's paradox with the earlier Wigner's friend paradox. They thereby create something that doesn't involve counterfactuals quite as obviously as Hardy's paradox does, and so requires a new discussion.

But to back up: what _is_ Wigner's friend? Well, it's basically just Schrödinger's cat, except that now it's no longer a cat being maintained in coherent superposition but a person, and we're emphatic in demanding that this person be treated as a quantum-mechanical observer. Thus, suppose Wigner entangles his friend with a qubit, like so:

$$ \left|\psi\right\rangle = \frac{\left|0\right\rangle \left|FriendSeeing0\right\rangle + \left|1\right\rangle \left|FriendSeeing1\right\rangle}{\sqrt{2}}. $$

From the friend's perspective, the qubit has been measured and has collapsed to either |0〉 or |1〉. From Wigner's perspective, no such thing has happened--there's only been unitary evolution--and in principle, Wigner could even confirm that by measuring |ψ〉 in a basis that included |ψ〉 as one of the basis vectors. But how can they both be right?

Many-Worlders will yawn at this question, since for them, _of course_ "the collapse of the wavefunction" is just an illusion created by the branching worlds, and with sufficiently advanced technology, one observer might experience the illusion even while a nearby observer doesn't. Ironically, the neo-Copenhagenists / Quantum Bayesians / whatever they now call themselves, though they consider themselves diametrically opposed to the Many-Worlders (and vice versa), will _also_ yawn at the question, since their whole philosophy is about how physics is observer-relative and it's sinful even to _think_ about an objective, God-given "quantum state of the universe." If, on the other hand, you believed both that

  1. collapse is an objective physical event, and
  2. human mental states can be superposed just like anything else in the physical universe,



then Wigner's thought experiment probably _should_ rock your world.

OK, but how do we Wigner's-friendify Hardy's paradox? Simple: in the state

$$\left|\psi\right\rangle = \frac{\left|00\right\rangle + \left|01\right\rangle + \left|10\right\rangle}{\sqrt{3}},$$

we "promote" Alice's and Bob's entangled qubits to two conscious observers, call them Charlie and Diane respectively, who can think two different thoughts that we represent by the states |0〉 and |1〉. Using far-future technology, Charlie and Diane have been not merely placed into coherent superpositions over mental states but also entangled with each other.

Then, as before, Alice will measure Charlie's brain in the {|+〉,|-〉} basis, and Bob will measure Diane's brain in the {|+〉,|-〉} basis. Since the whole setup is mathematically identical to that of Hardy's paradox, the probability that Alice and Bob both get the outcome |-〉 is again 1/12.

Ah, but now we can reason as follows:

  1. Whenever Alice gets the outcome |-〉, she knows that Diane must be in the |1〉 state (since, if Diane were in the |0〉 state, then Alice would've certainly seen |+〉).
  2. Whenever Diane is in the |1〉 state, she knows that Charlie must be in the |0〉 state (since there's no |11〉 component).
  3. Whenever Charlie is in the |0〉 state, she knows that Diane is in the |+〉 state, and hence Bob can't possibly see the outcome |-〉 when he measures Diane's brain in the {|+〉,|-〉} basis.



So to summarize, Alice knows that Diane knows that Charlie knows that Bob can't possibly see the outcome |-〉. By the "transitivity of knowledge," this implies that Alice herself knows that Bob can't possibly see |-〉. And yet, as we pointed out before, quantum mechanics predicts that Bob _can_ see |-〉, even when Alice has also seen |-〉. And Alice and Bob could even do the experiment, and compare notes, and see that their "certain knowledge" was false. Ergo, "quantum theory can't consistently describe its own use"!

You might wonder: compared to Hardy's original paradox, what have we gained by waving a magic wand over our two entangled qubits, and calling them "conscious observers"? Frauchiger and Renner's central claim is that, by this gambit, they've gotten rid of the illegal counterfactual reasoning that we needed to reach a contradiction in our analysis of Hardy's paradox. After all, they say, none of the steps in _their_ argument involve any measurements that aren't actually performed! But clearly, even if no one literally measures Charlie in the {|0〉,|1〉} basis, he's still _there_ , thinking either the thought corresponding to |0〉 or the thought corresponding to |1〉. And likewise Diane. Just as much as Alice and Bob, Charlie and Diane both exist even if no one measures them, and they can reason about what they know and what they know that others know. So then we're free to chain together the "certainties" of Alice, Bob, Charlie, and Diane in order to produce our contradiction.

As I already indicated, I reject this line of reasoning. Specifically, I get off the train at what I called step 3 above. Why? Because the inference from Charlie being in the |0〉 state to Bob seeing the outcome |+〉 holds for the _original_ state |ψ〉, but in my view it ceases to hold once we know that Alice is going to measure Charlie in the {|+〉,|-〉} basis, which would involve a drastic unitary transformation (specifically, a "Hadamard") on the quantum state of Charlie's brain. I.e., I don't accept that we can take knowledge inferences that would hold in a hypothetical world where |ψ〉 remained unmeasured, with a particular "branching structure" (as a Many-Worlder might put it), and extend them to the situation where Alice performs a rather violent measurement on |ψ〉 that changes the branching structure by scrambling Charlie's brain.

In quantum mechanics, measure or measure not: there is no _if_ you hadn't measured.

* * *

**Unrelated Announcement:** My awesome former PhD student [Michael Forbes](http://miforbes.cs.illinois.edu/), who's now on the faculty at the University of Illinois Urbana-Champaign, asked me to advertise that the UIUC CS department is [hiring](https://cs.illinois.edu/about-us/faculty-positions) this year in all areas, emphatically including quantum computing. And, well, I guess my desire to do Michael a solid outweighed my fear of being tried for treason by my own department's recruiting committee…

* * *

**Another Unrelated Announcement:** As of Sept. 25, 2018, it is the official editorial stance of _Shtetl-Optimized_ that the Riemann Hypothesis and the abc conjecture both remain open problems.
