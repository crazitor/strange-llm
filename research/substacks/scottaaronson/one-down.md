---
title: "One down"
author: "Scott Aaronson"
date: "Sun, 30 Apr 2006"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=82"
---

Last summer I posed [Ten Semi-Grand Challenges for Quantum Computing Theory](http://www.scottaaronson.com/writings/qchallenge.html). Today I'm pleased to report that (part of) one of my challenges has been "solved" -- where, as always in this business, the word "solved" is defined broadly so as to include "proven to be not really worth working on, since a solution to it would imply a solution to something else that most of us gave up on years ago."

Challenge 10 involved finding a polynomial-time quantum algorithm to PAC-learn neural networks (that is, the class [TC0](http://qwiki.caltech.edu/wiki/Complexity_Zoo#tc0) of polynomial-size, constant-depth threshold circuits). In a new [ECCC preprint](http://eccc.hpi-web.de/eccc-reports/2006/TR06-057/index.html), Adam Klivans and Alex Sherstov show that, if there's a fast quantum algorithm to learn even depth-2 neural nets, then there's also a fast quantum algorithm for the ~n1.5-approximate shortest vector problem. Embarrassingly for me, once you have the idea -- to use Oded Regev's lattice-based public key cryptosystems -- the quantum hardness of learning (say) depth 4 or 5 neural nets is immediate, while getting down to depth 2 takes another page. This is one of those results that hangs in the wonderful balance between "you could've thought of that" and "nyah nyah, you didn't."

Feel free to post your own challenges in the comments section. But please, no "spouter challenges" like "where does the power of quantum computing come from?" or "is there a deeper theoretical framework for quantum algorithms?" In general, if you're going to pose a scientific challenge, you should (1) indicate some technical problem whose solution would clearly represent progress, and (2) be willing to place at least 25% odds on such progress being made within five years. Or if you're not a gambler, pick technical problems that you yourself intend to solve -- that's the approach I took with Semi-Grand Challenges 4 and 7.

Theoretical computer science is often disheartening: there are so many open problems, and a week later they're all still open, and a week after that, they're all still open. Wait a year, though, or five years, or twenty, and some grad student will have had the insight that's eluded everyone else: that the problem can't be solved with any existing technique, unless Blum integers are factorable in 2n^ε time for all ε>0.
