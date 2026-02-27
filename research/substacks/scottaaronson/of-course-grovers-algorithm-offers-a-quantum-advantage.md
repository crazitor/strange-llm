---
title: "Of course Grover’s algorithm offers a quantum advantage!"
author: "Scott Aaronson"
date: "Wed, 22 Mar 2023"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=7143"
---

**Unrelated Update:** Huge congratulations to Ethernet inventor Bob Metcalfe, for [winning UT Austin's third Turing Award](https://www.nytimes.com/2023/03/22/technology/turing-award-bob-metcalfe-ethernet.html) after Dijkstra and Emerson!

And also to mathematician Luis Caffarelli, for [winning UT Austin's third Abel Prize](https://www.nytimes.com/2023/03/22/science/abel-prize-math-luis-caffarelli.html)!

* * *

I was really, _really_ hoping that I'd be able to avoid blogging about [this new arXiv preprint](https://arxiv.org/abs/2303.11317), by E. M. Stoudenmire and Xavier Waintal:

> **Grover 's Algorithm Offers No Quantum Advantage**
> 
> Grover's algorithm is one of the primary algorithms offered as evidence that quantum computers can provide an advantage over classical computers. It involves an "oracle" (external quantum subroutine) which must be specified for a given application and whose internal structure is not part of the formal scaling of the quantum speedup guaranteed by the algorithm. Grover's algorithm also requires exponentially many steps to succeed, raising the question of its implementation on near-term, non-error-corrected hardware and indeed even on error-corrected quantum computers. In this work, we construct a quantum inspired algorithm, executable on a classical computer, that performs Grover's task in a linear number of call to the oracle - an exponentially smaller number than Grover's algorithm - and demonstrate this algorithm explicitly for boolean satisfiability problems (3-SAT). Our finding implies that there is no a priori theoretical quantum speedup associated with Grover's algorithm. We critically examine the possibility of a practical speedup, a possibility that depends on the nature of the quantum circuit associated with the oracle. We argue that the unfavorable scaling of the success probability of Grover's algorithm, which in the presence of noise decays as the exponential of the exponential of the number of qubits, makes a practical speedup unrealistic even under extremely optimistic assumptions on both hardware quality and availability.

Alas, inquiries from journalists soon made it clear that silence on my part wasn't an option.

So, desperately seeking an escape, this morning I asked GPT-4 to read the preprint and comment on it just like I would. Sadly, it turns out the technology isn't quite ready to replace me at this blogging task. I suppose I should feel good: in every such instance, _either_ I'm vindicated in all my recent screaming here about generative AI--what the naysayers call "glorified autocomplete"--being on the brink of remaking civilization, _or else_ I still, for another few months at least, have a role to play on the Internet.

So, on to the preprint, as reviewed by the human Scott Aaronson. Yeah, it's basically a tissue of confusions, a mishmash of the well-known and the mistaken. As they say, both novel and correct, but not in the same places.

The paper's most eye-popping claim is that the [Grover search problem](https://en.wikipedia.org/wiki/Grover%27s_algorithm)--namely, finding an n-bit string x such that f(x)=1, given oracle access to a Boolean function f:{0,1}n→{0,1}--is solvable _classically_ , using a number of calls that's only linear in n, or in many cases only constant (!!). Since this claim contradicts a well-known, easily _provable_ lower bound--namely, that Ω(2n) oracle calls are needed for classical brute-force searching--the authors _must_ be using words in nonstandard ways, leaving only the question of how.

It turns out that, for their "quantum-inspired classical algorithm," the authors assume you're given, not merely an oracle for f, but the _actual circuit_ to compute f. They then use that circuit in a non-oracular way to extract the marked item. In which case, I'd prefer to say that they've actually solved the Grover problem with **zero** queries--simply because they've entirely left the black-box setting where Grover's algorithm is normally formulated!

What could possibly justify such a move? Well, the authors argue that _sometimes_ one can use the actual circuit to do better classically than Grover's algorithm would do quantumly, and therefore, they've shown that the Grover speedup is not "generic," as the quantum algorithms people always say it is.

But this is pure wordplay around the meaning of "generic." When we say that Grover's algorithm achieves a "generic" square-root speedup, what we mean is that it solves the generic black-box search problem in O(2n/2) queries, whereas any classical algorithm for that generic problem requires Ω(2n) queries. We don't mean that for _every_ f, Grover achieves a quadratic speedup for searching _that_ f, compared to the best classical algorithm that could be tailored to that f. Of course we don't; that would be trivially false!

Remarkably, later in the paper, the authors seem to realize that they haven't delivered the knockout blow against Grover's algorithm that they'd hoped for, because they then turn around and argue that, well, even for those f's where Grover _does_ provide a quadratic speedup over the best (or best-known) classical algorithm, noise and decoherence could negate the advantage in practice, and solving that problem would require a fault-tolerant quantum computer, but fault-tolerance could require an enormous overhead, pushing a practical Grover speedup far into the future.

The response here boils down to "no duh." Yes, if Grover's algorithm can yield any practical advantage in the medium term, it will _either_ be because we've discovered much cheaper ways to do quantum fault-tolerance, or _else_ because we've discovered "[NISQy](https://en.wikipedia.org/wiki/Noisy_intermediate-scale_quantum_era#:~:text=The%20current%20state%20of%20quantum,enough%20to%20achieve%20quantum%20supremacy.)" ways to exploit the Grover speedup, which avoid the need for full fault-tolerance--for example, via quantum annealing. The prospects are actually better for a medium-term advantage from Shor's factoring algorithm, because of its exponential speedup. Hopefully everyone in quantum computing theory has realized all this for a long time.

Anyway, as you can see, by this point we've already conceded the principle of Grover's algorithm, and are just haggling over the practicalities! Which brings us back to the authors' original claim to have a _principled_ argument against the Grover speedup, which (as I said) rests on a confusion over words.

Some people dread the day when GPT will replace them. In my case, for this task, I can't wait.

* * *

_Thanks to students Yuxuan Zhang (UT) and Alex Meiburg (UCSB) for discussions of the Stoudenmire-Waintal preprint that informed this post. Of course, I take sole blame for anything anyone dislikes about the post!_

* * *

For a much more technical response--one that explains _how_ this preprint's detailed attempt to simulate Grover classically fails, rather than merely proving that it must fail--check out [this comment by Alex Meiburg](https://scottaaronson.blog/?p=7143#comment-1947843).
