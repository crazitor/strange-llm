---
title: "What is the name of this post?"
author: "Scott Aaronson"
date: "Fri, 21 Apr 2006"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=77"
---

No need to thank me for my [turnabout](https://scottaaronson.blog/?p=76) -- we've got work to do. There's a new complexity class in town, and I need you to help me name it.

My new class is like [P/poly](http://qwiki.caltech.edu/wiki/Complexity_Zoo#pslashpoly), except that the polynomial-size advice can't be trusted -- you have to verify it. Or to put it another way, it's like [NP intersect coNP](http://qwiki.caltech.edu/wiki/Complexity_Zoo#npiconp), except that there's only one witness for each input length. Give me that witness, and I'll correctly decide every input of size n. Give me a different witness, and for every input of size n I'll either output the right answer or else say "I don't know."

Now, anyone could make up a name for this animal -- even I could! But I want the name to be naturally extensible to further classes. For example, if (hypothetically speaking) I was able to use a new result about the learnability of quantum states to prove that AvgBQP/qpoly is contained in AvgQMA/poly, but my proof actually yielded the stronger result that AvgBQP/qpoly is contained in the subclass of AvgQMA/poly where there's only one QMA witness for each input length, then your naming convention should immediately give me a name for that subclass.

So let the christening commence! And for extra credit, prove or (relative to an oracle) disprove that if my class contains NP, then P=NP.
