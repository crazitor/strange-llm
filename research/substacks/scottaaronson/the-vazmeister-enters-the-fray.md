---
title: "The Vazmeister enters the fray"
author: "Scott Aaronson"
date: "Sat, 17 Feb 2007"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=204"
---

Here's a letter that Umesh Vazirani (my adviser at Berkeley) sent to _The Economist_ , and which he kindly permitted me to share. I'm guessing they'll print this one instead of mine, which is fine by me.

> Sir,
> 
> Your article "Orion's belter" regarding D-Wave's demonstration of a "practical quantum computer", sets a new standard for sloppy science journalism. Most egregious is your assertion that quantum computers can solve NP-complete problems in "one shot" by exploring exponentially many solutions at once. This mistaken view was put to rest in the infancy of quantum computation over a decade ago when it was established that the axioms of quantum physics severely restrict the type of information accessible during a measurement. For unstructured search problems like the NP-complete problems this means that there is no exponential speed up but rather at most a quadratic speed up.
> 
> Your assertions about D-Wave are equally specious. A 16 qubit quantum computer has smaller processing power than a cell phone and hardly represents a practical breakthrough. Any claims about D-Wave's accomplishments must therefore rest on their ability to increase the number of qubits by a couple of orders of magnitude while maintaining the fragile quantum states of the qubits. Unfortunately D-Wave, by their own admission, have not tested whether the qubits in their current implementation are in a coherent quantum state. So it is quite a stretch to assert that they have a working quantum computer let alone one that potentially scales. An even bleaker picture emerges when one more closely examines their algorithmic approach. Their claimed speedup over classical algorithms appears to be based on a misunderstanding of a paper my colleagues van Dam, Mosca and I wrote on "The power of adiabatic quantum computing". That speed up unfortunately does not hold in the setting at hand, and therefore D-Wave's "quantum computer" even if it turns out to be a true quantum computer, and even if it can be scaled to thousands of qubits, would likely not be more powerful than a cell phone.
> 
> Yours sincerely,  
>  Umesh Vazirani  
>  Roger A. Strauch Professor of Computer Science  
>  Director, Berkeley Quantum Computing Center

**Update (2/18):** There's now a [_Nature_ news article](http://www.nature.com/news/2007/070212/full/070212-8.html) about D-Wave (hat tip to the [Pontiff](http://dabacon.org/pontiff/?p=1446)). Like pretty much every other article, this one makes no attempt to address the fundamental howlers about the ability of quantum computers to solve NP-complete problems -- but at least it quotes me saying that "almost every popular article written on this has grotesquely over-hyped it."
