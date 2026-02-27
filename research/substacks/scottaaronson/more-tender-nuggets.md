---
title: "More tender nuggets"
author: "Scott Aaronson"
date: "Fri, 03 Nov 2006"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=153"
---

You asked for 'em, you got 'em. (Do you want fries with that?)

  1. Suppose a baby is given some random examples of grammatical and ungrammatical sentences, and based on that, it wants to infer the general rule for whether or not a given sentence is grammatical. If the baby can do this with reasonable accuracy and in a reasonable amount of time, for any "regular grammar" (the very simplest type of grammar studied by Noam Chomsky), then that baby can also break the RSA cryptosystem.
  2. Oded Regev recently invented a public-key cryptosystem with an interesting property: though it's purely classical, his system only known to be secure under the assumption that certain problems are hard for quantum computers. The upside is that, if these problems are hard for quantum computers, then Regev's system (unlike RSA) is also secure against attack by quantum computers!
  3. Suppose N boys and N girls join a dating service. We write down an N-by-N matrix, where the (i,j) entry equals 1 if the ith boy and the jth girl are willing to date each other, and 0 if they aren't. We want to know if it's possible to pair off every boy and girl with a willing partner. Here's a simple way to find out: first rescale every row of the matrix to sum to 1. Then rescale every column to sum to 1. Then rescale every row, then rescale every column, and so on N5 times. If at the end of this scaling process, every row and column sum is between 1-1/N and 1+1/N, then it's possible to pair off the boys and girls; otherwise it isn't.
  4. If two graphs are isomorphic, then a short and simple proof of that fact is just the isomorphism itself. But what if two graphs aren't isomorphic? Is there also a short proof of that -- one that doesn't require checking every possible way of matching up the vertices? Under a plausible assumption, we now know that there is such a proof, for any pair of non-isomorphic graphs whatsoever (even with the same eigenvalue spectrum, etc). What's the plausible assumption? It has nothing to do with graphs! Roughly, it's that a certain problem, which is known to take exponential time for any one algorithm, still takes exponential time for any infinite sequence of algorithms.
  5. Suppose we had a small "neural network" with only three or four layers of neurons between the input and output, where the only thing each neuron could do was to compute the sum of its input signals modulo 2. We can prove, not surprisingly, that such a neural net would be extremely limited in its power. Ditto if we replace the 2 by 3, 4, 5, 7, 8, 9, or 11. But if we replace the 2 by 6, 10, or 12, then we no longer know anything! For all we know, a three-layer neural network, composed entirely of "mod 6 neurons," could solve NP-complete problems in polynomial time.


