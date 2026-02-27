---
title: "The Acrobatics of BQP"
author: "Scott Aaronson"
date: "Fri, 19 Nov 2021"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=6129"
---

Just in case anyone is depressed this afternoon and needs something to cheer them up, students [William Kretschmer](https://www.cs.utexas.edu/~kretsch/), [DeVon Ingram](https://www.quantitativebiology.northwestern.edu/2021/02/23/three-students-awarded-prizes-in-the-great-math-challenge-in-biology-contest/), and I have finally put out a new paper:

> **[The Acrobatics of BQP](https://eccc.weizmann.ac.il/report/2021/164/)**
> 
> **Abstract:** We show that, in the black-box setting, the behavior of quantum polynomial-time (BQP) can be remarkably decoupled from that of classical complexity classes like NP. Specifically:
> 
> - There exists an oracle relative to which NPBQP⊄BQPPH, resolving a 2005 problem of Fortnow. Interpreted another way, we show that AC0 circuits cannot perform useful homomorphic encryption on instances of the Forrelation problem. As a corollary, there exists an oracle relative to which P=NP but BQP≠QCMA.
> 
> - Conversely, there exists an oracle relative to which BQPNP⊄PHBQP.
> 
> - Relative to a random oracle, PP=PostBQP is not contained in the "QMA hierarchy" QMAQMA^QMA^…, and more generally PP⊄(MIP*)(MIP*)^(MIP*)^… (!), despite the fact that MIP*=RE in the unrelativized world. This result shows that there is no black-box quantum analogue of Stockmeyer's approximate counting algorithm.
> 
> - Relative to a random oracle, Σk+1⊄BQPΣ_k for every k.
> 
> - There exists an oracle relative to which BQP=P#P and yet PH is infinite. (By contrast, if NP⊆BPP, then PH collapses relative to all oracles.)
> 
> - There exists an oracle relative to which P=NP≠BQP=P#P.
> 
> To achieve these results, we build on the 2018 achievement by Raz and Tal of an oracle relative to which BQP⊄PH, and associated results about the Forrelation problem. We also introduce new tools that might be of independent interest. These include a "quantum-aware" version of the random restriction method, a concentration theorem for the block sensitivity of AC0 circuits, and a (provable) analogue of the Aaronson-Ambainis Conjecture for sparse oracles.

Incidentally, particularly when I've worked on a project with students, I'm often tremendously excited and want to shout about it from the rooftops for the students' sake … but then I also don't want to use this blog to privilege my own papers "unfairly." Can anyone suggest a principle that I should follow going forward?
