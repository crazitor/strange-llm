---
title: "Staggering toward quantum fault-tolerance"
author: "Scott Aaronson"
date: "Thu, 07 Dec 2023"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=7651"
---

Happy Hanukkah! I'm returning to Austin from a Bay Area trip that included the annual [Q2B (Quantum 2 Business)](https://q2b.qcware.com/2023-conferences/silicon-valley/agenda/) conference. This year, for the first time, I _opened_ the conference, with a talk on ["The Future of Quantum Supremacy Experiments,"](https://www.scottaaronson.com/talks/futureqs.pptx) rather than closing it with my usual ask-me-anything session.

* * *

The biggest talk at Q2B this year was [yesterday's announcement](https://www.quera.com/press-releases/harvard-quera-mit-and-the-nist-university-of-maryland-usher-in-new-era-of-quantum-computing-by-performing-complex-error-corrected-quantum-algorithms-on-48-logical-qubits), by a Harvard/MIT/[QuEra](https://www.quera.com/) team led by Misha Lukin and Vlad Vuletic, to have demonstrated "useful" quantum error-correction, for some definition of "useful," in neutral atoms ([see here](https://www.nature.com/articles/s41586-023-06927-3) for the _Nature_ paper). To drill down a bit into what they did:

  * They ran experiments with up to 280 physical qubits, which simulated up to 48 logical qubits.
  * They demonstrated [surface codes](https://en.wikipedia.org/wiki/Toric_code) of varying sizes as well as [color codes](https://errorcorrectionzoo.org/c/color).
  * They performed over 200 two-qubit [transversal gates](https://errorcorrectionzoo.org/list/quantum_transversal) on their encoded logical qubits.
  * They did a couple demonstrations, including the creation and verification of an encoded [GHZ state](https://en.wikipedia.org/wiki/Greenberger%E2%80%93Horne%E2%80%93Zeilinger_state) and (more impressively) an encoded [IQP circuit](https://strawberryfields.ai/photonics/demos/run_iqp.html), whose outputs were validated using the [Linear Cross-Entropy Benchmark](https://en.wikipedia.org/wiki/Cross-entropy_benchmarking) (LXEB).
  * Crucially, they showed that in their system, the use of logically encoded qubits produced a modest "net gain" in success probability compared to not using encoding, consistent with theoretical expectations (though see below for the caveats). With a 48-qubit encoded IQP circuit with a few hundred gates, for example, they achieved an LXEB score of 1.1, compared to a record of ~1.01 for unencoded physical qubits.
  * At least with their GHZ demonstration and with a particular decoding strategy (about which more later), they showed that their success probability _improves with increasing code size_.



Here are what I currently understand to be the limitations of the work:

  * They didn't directly demonstrate applying a _universal_ set of 2- or 3-qubit gates to their logical qubits. This is because they were limited to transversal gates, and the [Eastin-Knill Theorem](https://en.wikipedia.org/wiki/Eastin%E2%80%93Knill_theorem) shows that transversal gates can't be universal. On the other hand, they were able to simulate up to 48 [CCZ gates](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.CCZGate), which _do_ yield universality, by using [magic initial states](https://en.wikipedia.org/wiki/Magic_state_distillation).
  * They didn't demonstrate the "full error-correction cycle" on encoded qubits, where you'd first correct errors and then proceed to apply more logical gates to the corrected qubits. For now it's basically just: prepare encoded qubits, then apply transversal gates, then measure, and use the encoding to deal with any errors.
  * With their GHZ demonstration, they needed to use what they call "correlated decoding," where the code blocks are decoded in conjunction with each other rather than separately, in order to get good results.
  * With their IQP demonstration, they needed to postselect on the event that no errors occurred (!!), which happened about 0.1% of the time with their largest circuits. This just further underscores that they haven't yet demonstrated a full error-correction cycle.
  * They don't claim to have demonstrated _quantum supremacy_ with their logical qubits--i.e., nothing that's _too_ hard to simulate using a classical computer. (On the other hand, if they can really do 48-qubit encoded IQP circuits with hundreds of gates, then a convincing demonstration of encoded quantum supremacy seems like it should follow in short order.)



As always, experts are strongly urged to correct anything I got wrong.

I should mention that this _might_ not be the first experiment to get a net gain from the use of a quantum error-correcting code: Google might or might not have gotten one in an experiment that they reported in a [_Nature_ paper](https://www.nature.com/articles/s41586-022-05434-1) from February of this year (for discussion, see a [comment by Robin](https://scottaaronson.blog/?p=7651#comment-1961344)). In any case, though, the Google experiment just encoded the qubits and measured them, rather than applying hundreds of logical gates to the encoded qubits. Quantinuum also previously reported an experiment that at any rate got very close to net gain (again see the comments for discussion).

Assuming the result stands, I think it's plausibly the top experimental quantum computing advance of 2023 (coming in just under the deadline!). We clearly still have a long way to go until "actually useful" fault-tolerant QC, which might require thousands of logical qubits and millions of logical gates. But this is already beyond what I expected to be done this year, and (to use the AI doomers' lingo) it "moves my timelines forward" for quantum fault-tolerance. It should now be possible, among other milestones, to perform the first demonstrations of Shor's factoring algorithm with logically encoded qubits (though still to factor tiny numbers, of course). I'm slightly curious to see how Gil Kalai and the other quantum computing skeptics wiggle their way out _now_ , though I'm absolutely certain they'll find a way! Anyway, huge congratulations to the Harvard/MIT/QuEra team for their achievement.

* * *

In other QC news, IBM got a lot of press for [announcing a 1000-qubit superconducting chip](https://www.nature.com/articles/d41586-023-03854-1) a few days ago, although I don't yet know what two-qubit gate fidelities they're able to achieve. Anyone with more details is encouraged to chime in.

* * *

Yes, I'm well-aware that _60 Minutes_ recently ran a segment on quantum computing, featuring the [often-in-error-but-never-in-doubt](https://scottaaronson.blog/?p=7321) Michio Kaku. I wasn't planning to watch it unless events force me to.

* * *

Do any of you have strong opinions on whether, once my current contract with OpenAI is over, I should focus my research efforts more on quantum computing or on AI safety?

On the one hand: I’m now completely convinced that AI will transform civilization and daily life in a much deeper way and on a shorter timescale than QC will — and that’s _assuming_ full fault-tolerant QCs eventually get built, which I’m actually somewhat optimistic about (a bit more than I was last week!). I’d like to contribute if I can to helping the transition to an AI-centric world go well for humanity.

On the other hand: in quantum computing, I feel like I’ve somehow been able to correct the factual misconceptions of 99.99999% of people, and this is a central source of self-confidence about the value I can contribute to the world. In AI, by contrast, I feel like _at least_ a thousand times more people understand everything I do, and this causes serious self-doubt about the value and uniqueness of whatever I can contribute.

* * *

**Update (Dec. 8):** A different talk on the Harvard/MIT/QuEra work—not the one I missed at Q2B—is [now on YouTube](https://t.co/ux2cWGj4KU).
