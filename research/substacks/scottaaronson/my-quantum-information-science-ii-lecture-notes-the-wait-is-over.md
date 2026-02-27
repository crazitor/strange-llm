---
title: "My Quantum Information Science II Lecture Notes: The wait is over!"
author: "Scott Aaronson"
date: "Wed, 31 Aug 2022"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=6685"
---

**[Here they are [PDF]](https://www.scottaaronson.com/qisii.pdf).**

They're 155 pages of awesome--for a certain extremely specific definition of "awesome"--which I'm hereby offering to the world free of charge (for noncommercial use only, of course). They cover material that I taught, for the first time, in my Introduction to Quantum Information Science II undergrad course at UT Austin in Spring 2022.

The new notes pick up exactly where my older [QIS I lecture notes](https://www.scottaaronson.com/qclec.pdf) left off, and they presuppose familiarity with the QIS I material. So, if you're just beginning your quantum information journey, then please start with my QIS I notes, which presuppose only linear algebra and a bit of classical algorithms (e.g., recurrence relations and big-O notation), and which self-containedly explain all the rules of QM, moving on to (e.g.) quantum circuits, density matrices, entanglement entropy, Wiesner's quantum money, QKD, quantum teleportation, the Bell inequality, interpretations of QM, the Shor 9-qubit code, and the algorithms of Deutsch-Jozsa, Bernstein-Vazirani, Simon, Shor, and Grover. Master all that, and you'll be close to the quantum information research frontier of circa 1996.

My new QIS II notes cover a bunch of topics, but the main theme is "perspectives on quantum computing that go beyond the bare quantum circuit model, and that became increasingly central to the field from the late 1990s onwards." Thus, it covers:

  * Hamiltonians, ground states, the adiabatic algorithm, and the universality of adiabatic QC
  * The stabilizer formalism, the 1996 Gottesman-Knill Theorem on efficient classical simulation of stabilizer QC, my and Gottesman's 2004 elaborations, boosting up to universality via "magic states," transversal codes, and the influential 2016 concept of _stabilizer rank_
  * Bosons and fermions: the formalism of Fock space and of creation and annihilation operators, connection to the permanents and determinants of matrices, efficient classical simulation of free fermionic systems (Valiant's 2002 "matchcircuits"), the 2001 Knill-Laflamme-Milburn (KLM) theorem on universal optical QC, BosonSampling and its computational complexity, and the current experimental status of BosonSampling
  * Cluster states, Raussendorf and Briegel's 2000 measurement-based quantum computation (MBQC), and Gottesman and Chuang's 1999 "gate teleportation" trick
  * Matrix product states, and Vidal's 2003 efficient classical simulation of "slightly entangled" quantum computations



Extra bonus topics include:

  * The 2007 Broadbent-Fitzsimons-Kashefi (BFK) protocol for blind and authenticated QC; brief discussion of later developments including Reichardt-Unger-Vazirani 2012 and Mahadev 2018
  * Basic protocols for quantum state tomography
  * My 2007 work on PAC-learnability of quantum states
  * The "dessert course": the black hole information problem, and the Harlow-Hayden argument on the computational hardness of decoding Hawking radiation



Master all this, and hopefully you'll have the conceptual vocabulary to understand a large fraction of what people in quantum computing and information care about today, how they now think about building scalable QCs, and what they post to the quant-ph arXiv.

Note that my QIS II course is complementary to my graduate course on quantum complexity theory, for which [the lecture notes are here](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-845-quantum-complexity-theory-fall-2010/lecture-notes/). There's very little overlap between the two (and even less overlap between QIS II and _[Quantum Computing Since Democritus](https://www.amazon.ca/Quantum-Computing-since-Democritus-Aaronson/dp/0521199565)_).

The biggest, most important topic related to the QIS II theme that I _didn 't_ cover was [topological quantum computing](https://en.wikipedia.org/wiki/Topological_quantum_computer). I'd wanted to, but it quickly became clear that topological QC begs for a whole course of its own, and that I had neither the time nor the expertise to do it justice. In retrospect, I do wish I'd at least covered the [Kitaev surface code](https://en.wikipedia.org/wiki/Toric_code).

Crucially, these lecture notes don't represent my effort alone. I worked from draft scribe notes prepared by the QIS II students, who did a far better job than I had any right to expect (including creating the beautiful figures). My wonderful course TA and PhD student Daniel Liang, along with students Ethan Tan, Samuel Ziegelbein, and Steven Han, then assembled everything, fixed numerous errors, and compiled the bibliography. I’m grateful to all of them. At the last minute, we had a LaTeX issue that none of us knew how to fix--but, in response to a plea, _Shtetl-Optimized_ reader Pablo Cingolani generously volunteered to help, completed the work by the very next day (I'd imagined it taking a month!), and earned a fruit basket from me in gratitude.

Anyway, let me know of any mistakes you find! We'll try to fix them.
