---
title: "Turn down the quantum volume"
author: "Scott Aaronson"
date: "Thu, 05 Mar 2020"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=4649"
---

Several people asked me to comment on the recent announcement by Honeywell that they'll soon have what they call "the most powerful" quantum computer (see [here for press release](https://www.honeywell.com/en-us/newsroom/news/2020/03/behind-the-scenes-of-a-major-quantum-breakthrough), [here for _Forbes_ article](https://www.forbes.com/sites/moorinsights/2020/03/03/honeywell-surprisingly-announces-it-will-be-releasing-the-most-powerful-quantum-computer-in-the-world/#c271c5114b4a), [here for paper](https://www.honeywell.com/content/dam/honeywell/files/Beta_10_Quantum_3_3_2020.pdf)). 

I'm glad that Honeywell, which many people might know as an air-conditioner manufacturer, has entered the race for trapped-ion QC. I wish them success. I've known about what they were doing in part because Drew Potter, my friend and colleague in UT Austin's physics department, took a one-year leave from UT to contribute to their effort.

Here I wanted to comment about one detail in Honeywell's announcement: namely, the huge emphasis on "quantum volume" as the central metric for judging quantum computing progress, and the basis for calling their own planned device the "most powerful." One journalist asked me to explain why quantum volume is such an important measure. I had to give her an honest answer: I don't know whether it is.

Quantum volume was invented a few years ago by a group at IBM. According to one of [their papers](https://arxiv.org/pdf/1811.12926.pdf), it can be defined roughly as 2k, where k is the largest number such that you can run a k-qubit random quantum circuit, with depth k and with any-to-any connectivity, and have at least (say) 2/3 probability of measuring an answer that passes some statistical test. (In the paper, they use what Lijie Chen and I named [Heavy Output Generation](https://arxiv.org/abs/1612.05903), though Google's Linear Cross-Entropy Benchmark is similar.)

I don't know why IBM takes the "volume" to be 2k rather than k itself. Leaving that aside, though, the idea was to invent a single "goodness measure" for quantum computers that can't be gamed _either_ by building a huge number of qubits that don't maintain nearly enough coherence (what one might call "the D-Wave approach"), _or_ by building just one perfect qubit, _or_ by building qubits that behave well in isolation but don't interact easily. Note that the any-to-any connectivity requirement makes things harder for architectures with nearest-neighbor interactions only, like the 2D superconducting chips being built by Google, Rigetti, or IBM itself.

You know the notion of a researcher's [h-index](https://en.wikipedia.org/wiki/H-index)--defined as the largest h such that she's published h papers that garnered h citations each? Quantum volume is basically an h-index for quantum computers. It's an attempt to take several different yardsticks of experimental progress, none terribly useful in isolation, and combine them into one "consumer index."

Certainly I sympathize with the goal of broadening people's focus beyond the "but how many qubits does it have?" question--since the answer to that question is meaningless without further information about what the qubits can _do_. From that standpoint, quantum volume seems like a clear step in the right direction.

Alas, [Goodhart's Law](https://en.wikipedia.org/wiki/Goodhart%27s_law) states that "as soon as a measure becomes a target, it ceases to be a good measure." That happened years ago with the h-index, which now regularly pollutes academic hiring and promotion decisions, to the point where [its inventor expressed regrets](https://arxiv.org/abs/2001.09496). Quantum volume is now looking to me like another example of Goodhart's Law at work.

The position of Honeywell's PR seems to be that, if they can build a device that can apply 6 layers of gates to 6 qubits, with full connectivity and good fidelity, that will then count as "the world's most powerful quantum computer," since it will have the largest volume. One problem here is that such a device could be simulated by maintaining a vector of only 26=64 amplitudes. This is nowhere near quantum supremacy (i.e., beating classical computers at some well-defined task), which is a necessary though not sufficient condition for doing anything useful.

Think of a university that achieves an average faculty-to-student ratio of infinity by holding one class with zero students. It gets the "best score" only by exploiting an obvious defect in the scoring system.

So what's the alternative? The policy _I_ prefer is simply to tell the world all your system specs, as clearly as you can, with no attempts made to bury the lede. How many qubits do you have? With what coherence times? With what connectivity? What are the 1- and 2-qubit gate fidelities? What depth of circuit can you do? What resources do the standard classical algorithms need to simulate your system? Most importantly: what's the main drawback of your system, the spec that's the _worst_ , the one you most need to improve? What prevents you from having a scalable quantum computer right now? And are you going to tell me, or will you make me scour Appendix III.B in your paper, or worse yet, ask one of your competitors?

I confess that the answers to the above questions are hard to summarize in a single number (unless you, like, concatenated binary encodings of them or something). But they _can_ be ineffably combined, to produce a progress metric that one of my postdocs suggested calling "quantum scottness," and which roughly equals the number of expressions of wide-eyed surprise minus the number of groans.
