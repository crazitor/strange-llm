---
title: "FAQ on Microsoft’s topological qubit thing"
author: "Scott Aaronson"
date: "Thu, 20 Feb 2025"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=8669"
---

**Q1.** Did you [see](https://azure.microsoft.com/en-us/blog/quantum/2025/02/19/microsoft-unveils-majorana-1-the-worlds-first-quantum-processor-powered-by-topological-qubits/) [Microsoft's](https://www.nature.com/articles/d41586-025-00527-z) [announcement](https://www.nytimes.com/2025/02/19/technology/microsoft-quantum-computing-topological-qubit.html)?  
A. Yes, thanks, you can stop emailing to ask! Microsoft's Chetan Nayak was even kind enough to give me a personal briefing a few weeks ago. Yesterday I did a [brief interview](https://www.bbc.co.uk/sounds/play/w3ct60h5) on this for the BBC's World Business Report, and I also [commented](https://www.technologyreview.com/2025/02/19/1112072/a-new-microsoft-chip-could-lead-to-more-stable-quantum-computers/) for MIT Technology Review.

**Q2.** What _is_ a topological qubit?  
**A.** It's a special kind of qubit built using nonabelian [anyons](https://en.wikipedia.org/wiki/Anyon), which are excitations that can exist in a two-dimensional medium, behaving neither as fermions nor as bosons. The idea grew out of seminal work by Alexei Kitaev, Michael Freedman, and others starting in the late 1990s. Topological qubits have proved harder to create and control than ordinary qubits.

**Q3.** Then why do people care about topological qubits?  
**A.** The dream is that they could _eventually_ be more resilient to decoherence than regular qubits, since an error, in order to matter, needs to change the _topology_ of how the nonabelian anyons are braided around each other. So you'd have some robustness built in to the physics of your system, rather than having to engineer it laboriously at the software level (via [quantum fault-tolerance](https://en.wikipedia.org/wiki/Threshold_theorem)).

**Q4.** Did Microsoft create the first topological qubit?  
**A.** Well, they say they did! [**Update:** Commenters point out to me that buried in _Nature_ 's review materials is the following striking passage: "The editorial team wishes to point out that the results in this manuscript do not represent evidence for the presence of Majorana zero modes in the reported devices. The work is published for introducing a device architecture that might enable fusion experiments using future Majorana zero modes." So, the situation is that Microsoft is unambiguously claiming to have created a topological qubit, _and_ they just published a relevant paper in _Nature_ , but their claim to have created a topological qubit has not yet been accepted by peer review.]

**Q5.** Didn't Microsoft claim the experimental creation of Majorana zero modes--a building block of topological qubits--back in 2018, and didn't they then need to [retract](https://spectrum.ieee.org/majorana-microsoft-backed-quantum-computer-research-retracted) their claim?  
**A.** Yep. Certainly that history is making some experts cautious about the new claim. When I asked Chetan Nayak how confident I should be, his response was basically "look, we now have a topological qubit that's behaving fully as a qubit; how much more do people want?"

**Q6.** Is this a big deal?  
**A.** _If_ the claim stands, I'd say it would be a scientific milestone for the field of topological quantum computing and physics beyond. The number of topological qubits manipulated in a single experiment would then have finally increased from 0 to 1, and depending on how you define things, arguably a "new state of matter" would even have been created, one that doesn't appear in nature (but only in _Nature_).

**Q7.** Is this useful?  
**A.** Not yet! If anyone claims that a single qubit, or even 30 qubits, are already _useful_ for speeding up computation, you can ignore anything else that person says. (Certainly Microsoft makes no such claim.) On the question of what we believe quantum computers will or won't _eventually_ be useful for, see like half the archives of this blog over the past twenty years.

**Q8.** Does this announcement vindicate topological qubits as the way forward for quantum computing?  
**A.** Think of it this way. _If_ Microsoft's claim stands, then topological qubits have finally reached some sort of parity with where more traditional qubits were 20-30 years ago. I.e., the non-topological approaches like superconducting, trapped-ion, and neutral-atom have an absolutely _massive_ head start: there, Google, IBM, Quantinuum, QuEra, and other companies now routinely do experiments with dozens or even hundreds of entangled qubits, and thousands of two-qubit gates. Topological qubits can win if, and only if, they turn out to be _so much_ more reliable that they leapfrog the earlier approaches--sort of like the transistor did to the vacuum tube and electromechanical relay. Whether that will happen is still an open question, to put it extremely mildly.

**Q9.** Are there other major commercial efforts to build topological qubits?  
**A.** No, it's pretty much just Microsoft [**update:** apparently Nokia Bell Labs also has a smaller, quieter effort, and Delft University in the Netherlands also continues work in the area, having ended an earlier collaboration with Microsoft]. Purely as a scientist who likes to see things tried, I'm grateful that at least one player stuck with the topological approach even when it ended up being a long, painful slog.

**Q10.** Is Microsoft now on track to scale to a million topological qubits in the next few years?  
**A.** In the world of corporate PR and pop-science headlines, sure, why not? As Bender from _Futurama_ [says](https://www.youtube.com/watch?v=DGZ10kZ4lmE), "I can guarantee anything you want!" In the world of reality, a "few years" certainly feels overly aggressive to me, but good luck to Microsoft and good luck to its competitors! I foresee exciting times ahead, provided we still have a functioning civilization in which to enjoy them.

**Update (Feb 20):** Chetan Nayak himself [comments here](https://scottaaronson.blog/?p=8669#comment-2003328), to respond to criticisms about Microsoft’s _Nature_ paper lacking direct evidence for majorana zero modes or topological qubits. He says that the paper, though published this week, was submitted a year ago, before the evidence existed. Of course we all look forward to the followup paper.
