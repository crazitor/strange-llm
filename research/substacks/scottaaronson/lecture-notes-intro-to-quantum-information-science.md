---
title: "Lecture notes!  Intro to Quantum Information Science"
author: "Scott Aaronson"
date: "Sun, 26 Aug 2018"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=3943"
---

Someone recently wrote that my blog is "too high on nerd whining content and too low on actual compsci content to be worth checking too regularly." While that's surely one of the mildest criticisms I've ever received, I hope that today's post will help to even things out.

In Spring 2017, I taught a new undergraduate course at UT Austin, entitled Introduction to Quantum Information Science. There were about 60 students, mostly CS but also with strong representation from physics, math, and electrical engineering. One student, Ewin Tang, made a [previous appearance](https://scottaaronson.blog/?p=3880) on this blog. But today belongs to another student, Paulo Alves, who took it upon himself to make detailed notes of all of my lectures. Using Paulo's notes as a starting point, and after a full year of procrastination and delays, I'm now happy to release the full lecture notes for the course. Among other things, I'll be using these notes when I teach the course a second time, starting … holy smokes … _this Wednesday_.

I don't pretend that these notes break any new ground. Even if we restrict to undergrad courses only (which rules out, e.g., [Preskill's legendary notes](http://www.theory.caltech.edu/people/preskill/ph229/)), there are already other great quantum information lecture notes available on the web, such as [these from Berkeley](https://inst.eecs.berkeley.edu/~cs191/fa14/) (based on a course taught by, among others, my former adviser Umesh Vazirani and committee member Birgitta Whaley), and [these from John Watrous in Waterloo](https://cs.uwaterloo.ca/~watrous/LectureNotes/CPSC519.Winter2006/all.pdf). There are also dozens of books--including [Mermin's](https://www.amazon.com/Quantum-Computer-Science-David-Mermin/dp/0521876583), which we used in this course. The only difference with these notes is that … well, they cover exactly the topics _I 'd_ cover, in exactly the order I'd cover them, and with exactly the stupid jokes and stories I'd tell in a given situation. So if you like my lecturing style, you'll probably like these, and if not, not (but given that you're here, there's hopefully some bias toward the former).

The only prerequisite for these notes is some minimal previous exposure to linear algebra and algorithms. If you read them all, you might not be ready yet to do research in quantum information--that's what a grad course is for--but I feel good that you'll have an honest understanding of what quantum information is all about and where it currently stands. (In fact, where it _already_ stood by the late 1990s and early 2000s, but with many comments about the theoretical and experimental progress that's been made since then.)

Also, if you're one of the people who read _[Quantum Computing Since Democritus](https://www.amazon.com/Quantum-Computing-since-Democritus-Aaronson/dp/0521199565)_ and who was disappointed by the lack of basic quantum algorithms in that book--a function of the book's origins, as notes of lectures given to graduate students who already _knew_ basic quantum algorithms--then consider these new notes my restitution. If nothing else, no one can complain about a dearth of basic quantum algorithms _here_.

I welcome comments, bugfixes, etc. Thanks so much, not only to Paulo for transcribing the lectures (and making the figures!), but also to Patrick Rall and Corey Ostrove for TA'ing the course, to Tom Wong and Supartha Podder for giving guest lectures, and of course, to all the students for making the course what it was.

  * [Lecture 1](https://www.scottaaronson.com/qclec/1.pdf): Course Intro, Church-Turing Thesis (3 pages)
  * [Lecture 2](https://www.scottaaronson.com/qclec/2.pdf): Probability Theory and QM (5 pages)
  * [Lecture 3](https://www.scottaaronson.com/qclec/3.pdf): Basic Rules of QM (4 pages)
  * [Lecture 4](https://www.scottaaronson.com/qclec/4.pdf): Quantum Gates and Circuits, Zeno Effect, Elitzur-Vaidman Bomb (5 pages)
  * [Lecture 5](https://www.scottaaronson.com/qclec/5.pdf): Coin Problem, Inner Products, Multi-Qubit States, Entanglement (5 pages)
  * [Lecture 6](https://www.scottaaronson.com/qclec/6.pdf): Mixed States (6 pages)
  * [Lecture 7](https://www.scottaaronson.com/qclec/7.pdf): Bloch Sphere, No-Cloning, Wiesner's Quantum Money (6 pages)
  * [Lecture 8](https://www.scottaaronson.com/qclec/8.pdf): More on Quantum Money, BB84 Quantum Key Distribution (5 pages)
  * [Lecture 9](https://www.scottaaronson.com/qclec/9.pdf): Superdense Coding (2 pages)
  * [Lecture 10](https://www.scottaaronson.com/qclec/10.pdf): Teleportation, Entanglement Swapping, GHZ State, Monogamy (5 pages)
  * [Lecture 11](https://www.scottaaronson.com/qclec/11.pdf): Quantifying Entanglement, Mixed State Entanglement (4 pages)
  * [Lecture 12](https://www.scottaaronson.com/qclec/12.pdf): Interpretation of QM (Copenhagen, Dynamical Collapse, MWI, Decoherence) (10 pages)
  * [Lecture 13](https://www.scottaaronson.com/qclec/13.pdf): Hidden Variables, Bell's Inequality (5 pages)
  * [Lecture 14](https://www.scottaaronson.com/qclec/14.pdf): Nonlocal Games (7 pages)
  * [Lecture 15](https://www.scottaaronson.com/qclec/15.pdf): Einstein-Certified Randomness (4 pages)
  * [Lecture 16](https://www.scottaaronson.com/qclec/16.pdf): Quantum Computing, Universal Gate Sets (8 pages)
  * [Lecture 17](https://www.scottaaronson.com/qclec/17.pdf): Quantum Query Complexity, Deutsch-Jozsa (8 pages)
  * [Lecture 18](https://www.scottaaronson.com/qclec/18.pdf): Bernstein-Vazirani, Simon (7 pages)
  * [Lecture 19](https://www.scottaaronson.com/qclec/19.pdf): RSA and Shor's Algorithm (6 pages)
  * [Lecture 20](https://www.scottaaronson.com/qclec/20.pdf): Shor, Quantum Fourier Transform (8 pages)
  * [Lecture 21](https://www.scottaaronson.com/qclec/21.pdf): Continued Fractions, Shor Wrap-Up (4 pages)
  * [Lecture 22](https://www.scottaaronson.com/qclec/22.pdf): Grover (9 pages)
  * [Lecture 23](https://www.scottaaronson.com/qclec/23.pdf): BBBV, Applications of Grover (7 pages)
  * [Lecture 24](https://www.scottaaronson.com/qclec/24.pdf): Collision and Other Applications of Grover (6 pages)
  * [Lecture 25](https://www.scottaaronson.com/qclec/25.pdf): Hamiltonians (10 pages)
  * [Lecture 26](https://www.scottaaronson.com/qclec/26.pdf): Adiabatic Algorithm (10 pages)
  * [Lecture 27](https://www.scottaaronson.com/qclec/27.pdf): Quantum Error Correction (8 pages)
  * [Lecture 28](https://www.scottaaronson.com/qclec/28.pdf): Stabilizer Formalism (9 pages)
  * [Lecture 29](https://www.scottaaronson.com/qclec/29.pdf): Experimental Realizations of QC (9 pages)



And by popular request, here are the 2017 problem sets!

  * [Set 1](https://www.scottaaronson.com/qclec/ps1.pdf)
  * [Set 2](https://www.scottaaronson.com/qclec/ps2.pdf)
  * [Set 3](https://www.scottaaronson.com/qclec/ps3.pdf)
  * [Set 4](https://www.scottaaronson.com/qclec/ps4.pdf)
  * [Set 5](https://www.scottaaronson.com/qclec/ps5.pdf)
  * [Set 6](https://www.scottaaronson.com/qclec/ps6.pdf)
  * [Set 7](https://www.scottaaronson.com/qclec/ps7.pdf)
  * [Set 8](https://www.scottaaronson.com/qclec/ps8.pdf)
  * [Set 9](https://www.scottaaronson.com/qclec/ps9.pdf)
  * [Set 10](https://www.scottaaronson.com/qclec/ps10.pdf)
  * [Set 11](https://www.scottaaronson.com/qclec/ps11.pdf)



I _might_ post solutions at a later date.

**Note:** If you're taking the course in 2018 or a later year, these sets should be considered outdated and for study purposes only.

* * *

**Notes and Updates (Aug. 27)**

[Here's a 184-page combined file](https://www.scottaaronson.com/qclec/combined.pdf). Thanks so much to Robert Rand, Oscar Cunningham, Petter S, and Noon van der Silk for their help with this.

If it wasn't explicit: these notes are copyright Scott Aaronson 2018, free for personal or academic use, but not for modification or sale.

I've freely moved material between lectures so that it wasn't arbitrarily cut across lecture boundaries. This is one of the reasons why some lectures are much longer than others.

I apologize that some of the displayed equations are ugly. This is because we never found an elegant way to edit equations in Google Docs.

If you finish these notes and are still hankering for more, try my [Quantum Complexity Theory](http://stellar.mit.edu/S/course/6/fa14/6.845/materials.html) or [Great Ideas in Theoretical Computer Science](http://stellar.mit.edu/S/course/6/sp16/6.045/materials.html) lecture notes, or my [Barbados lecture notes](http://www.scottaaronson.com/barbados-2016.pdf). I now have links to all of them on the sidebar on the right.
