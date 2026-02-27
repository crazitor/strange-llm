---
title: "Quantum Complexity Theory Student Project Showcase 2!"
author: "Scott Aaronson"
date: "Sun, 23 Dec 2012"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=1181"
---

_(Note: The "2!" in the title of this post really does mean "2 factorial," if you want it to.)_

With the end of the semester upon us, it's time for a once-every-two-year tradition: showcasing student projects from my [6.845 Quantum Complexity Theory](http://stellar.mit.edu/S/course/6/fa12/6.845/) graduate course at MIT. For my [previous showcase](https://scottaaronson.blog/?p=515), in 2010, I chose six projects that I thought were especially outstanding. This year, however, there were so many great projects--and so many, in particular, that could actually be _useful_ to people in quantum computing--that I decided simply to open up the showcase to the whole class. I had 17 takers; their project reports and 10-minute presentation slides are below.

Let me mention a few projects that tried to do something new and audacious. Jenny Barry [generalizes](http://www.scottaaronson.com/showcase2/report/jenny-barry.pdf) the notion of Partially Observable Markov Decision Processes (POMDPs) to the quantum case, and uses a recent result of Eisert et al., showing that certain problems in quantum measurement theory are undecidable (like, literally _Turing-undecidable_), to show that goal state reachability for "QOMDPs" is also Turing-undecidable (despite being decidable for classical POMDPs). Matt Falk suggests a [novel quantum algorithm](http://www.scottaaronson.com/showcase2/report/matt-falk.pdf) for spatial search on the 2D grid, and gives some numerical evidence that the algorithm finds a marked item in O(√n) time (which, if true, would be the optimal bound, beating the previous runtime of O(√(n log n))). Matt Coudron and Henry Yuen set out to prove that the Vazirani-Vidick protocol for quantum randomness expansion is optimal, and achieve some interesting [partial results](http://www.scottaaronson.com/showcase2/report/henry-yuen-matt-coudron.pdf). Mohammad Bavarian (well, jointly with me) [asks whether](http://www.scottaaronson.com/showcase2/report/mohammad-bavarian.pdf) there's a fast quantum algorithm for PARITY that gets the right answer on just _slightly_ more than 50% of the inputs--and shows, rather surprisingly, that this question is closely related to some of the hardest open problems about Boolean functions, like sensitivity versus block sensitivity.

This year, though, I also want to call special attention to the _survey_ projects, since some of them resulted in review articles that could be of real use to students and researchers in quantum computing theory. Notably, Adam Bookatz [compiled the first list of essentially all known QMA-complete problems](http://www.scottaaronson.com/showcase2/report/adam-bookatz.pdf), analogous to (but shorter than!) Garey and Johnson's listing of known NP-complete problems in 1979. Chris Graves [surveyed](http://www.scottaaronson.com/showcase2/report/chris-graves.pdf) the known quantum fault-tolerance bounds. Finally, three projects took on the task of understanding and explaining some of the most important recent results in quantum complexity theory: Travis Hance on Thomas Vidick and Tsuyoshi Ito's [NEXP in MIP* breakthrough](http://www.scottaaronson.com/showcase2/report/travis-hance.pdf); Emily Stark on [Mark Zhandry's phenomenal results](http://www.scottaaronson.com/showcase2/report/emily-stark.pdf) on the security of classical cryptographic constructions against quantum attack; and Max Zimet on [Jordan-Lee-Preskill's major work](http://www.scottaaronson.com/showcase2/report/max-zimet.pdf) on simulation of quantum field theories.

(Oops, sorry … did I use words like "important," "breakthrough," and "phenomenal" too often in that last sentence, thereby triggering the wrath of the [theoretical computer science excitement police](https://scottaaronson.blog/?p=853)? Well then, come over to my apartment and friggin' arrest me.)

Anyway, thanks so much to all the students for making 6.845 such an awesome class (at least on my end)! Without further ado, here's the complete project showcase:

  * Arturs Backurs. **Influences in Low-Degree Polynomials.** [[Report]](http://www.scottaaronson.com/showcase2/report/arturs-backurs.pdf) [[Slides]](http://www.scottaaronson.com/showcase2/arturs-backurs.pdf)


  * Jenny Barry. **Quantum POMDPs (Partially Observable Markov Decision Processes).** [[Report]](http://www.scottaaronson.com/showcase2/report/jenny-barry.pdf) [[Slides]](http://www.scottaaronson.com/showcase2/jenny-barry.pdf)


  * Mohammad Bavarian. **The Quantum Weak Parity Problem.** [[Report]](http://www.scottaaronson.com/showcase2/report/mohammad-bavarian.pdf) [[Slides]](http://www.scottaaronson.com/showcase2/mohammad-bavarian.pdf)


  * Shalev Ben-David. **Decision-Tree Complexity.** [[Report]](http://www.scottaaronson.com/showcase2/report/shalev-ben-david.pdf) [[Slides]](http://www.scottaaronson.com/showcase2/shalev-ben-david.pptx)


  * Adam Bookatz. **QMA-Complete Problems.** [[Report]](http://www.scottaaronson.com/showcase2/report/adam-bookatz.pdf) [[Slides]](http://www.scottaaronson.com/showcase2/adam-bookatz.pptx)


  * Adam Bouland. **Classifying Beamsplitters.** [[Report]](http://www.scottaaronson.com/showcase2/report/adam-bouland.pdf) [[Slides]](http://www.scottaaronson.com/showcase2/adam-bouland.ppt)


  * Matt Coudron and Henry Yuen. **Some Limits on Non-Local Randomness Expansion.** [[Report]](http://www.scottaaronson.com/showcase2/report/henry-yuen-matt-coudron.pdf) [[Slides]](http://www.scottaaronson.com/showcase2/henry-yuen-matt-coudron.pptx)


  * Charles Epstein. **Adiabatic Quantum Computing.** [[Report]](http://www.scottaaronson.com/showcase2/report/charles-epstein.pdf) [[Slides]](http://www.scottaaronson.com/showcase2/charles-epstein.pdf)


  * Matt Falk. **Quantum Search on the Spatial Grid.** [[Report]](http://www.scottaaronson.com/showcase2/report/matt-falk.pdf) [[Slides]](http://www.scottaaronson.com/showcase2/matt-falk.pptx)


  * Badih Ghazi. **Quantum Query Complexity of PARITY with Small Bias.** [[Report]](http://www.scottaaronson.com/showcase2/report/badih-ghazi.pdf) [[Slides]](http://www.scottaaronson.com/showcase2/badih-ghazi.pdf)


  * Chris Graves. **Survey on Bounds on the Quantum Fault-Tolerance Threshold.** [[Report]](http://www.scottaaronson.com/showcase2/report/chris-graves.pdf) [[Slides]](http://www.scottaaronson.com/showcase2/chris-graves.ppt)


  * Travis Hance. **Multiprover Interactive Protocols with Quantum Entanglement.** [[Report]](http://www.scottaaronson.com/showcase2/report/travis-hance.pdf) [[Slides]](http://www.scottaaronson.com/showcase2/travis-hance.pdf)


  * Charles Herder. **Blind Quantum Computation.** [[Report]](http://www.scottaaronson.com/showcase2/report/charles-herder.pdf) [[Slides]](http://www.scottaaronson.com/showcase2/charles-herder.pdf)


  * Vincent Liew. **On the Complexity of Manipulating Quantum Boolean Circuits.** [[Report]](http://www.scottaaronson.com/showcase2/report/vincent-liew.pdf) [[Slides]](http://www.scottaaronson.com/showcase2/vincent-liew.pptx)


  * Emily Stark. **Classical Crypto, Quantum Queries.** [[Report]](http://www.scottaaronson.com/showcase2/report/emily-stark.pdf) [[Slides]](http://www.scottaaronson.com/showcase2/emily-stark.pdf)


  * Ted Yoder. **Generalized Stabilizers.** [[Report]](http://www.scottaaronson.com/showcase2/report/ted-yoder.pdf) [[Slides]](http://www.scottaaronson.com/showcase2/ted-yoder.pptx)


  * Max Zimet. **Complexity of Quantum Field Theories.** [[Report]](http://www.scottaaronson.com/showcase2/report/max-zimet.pdf) [[Slides]](http://www.scottaaronson.com/showcase2/max-zimet.pdf)


