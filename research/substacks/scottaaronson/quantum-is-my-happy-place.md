---
title: "Quantum is my happy place"
author: "Scott Aaronson"
date: "Thu, 29 Jan 2026"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=9528"
---

  * [Here's a 53-minute podcast](https://youtube.com/watch?si=WA8EAW5OT3Fc8bxS&v=bMdoBxa6YkE&feature=youtu.be) that I recorded this afternoon with a high school student named Micah Zarin, and which ended up covering … _[checks notes]_ … consciousness, free will, brain uploading, the Church-Turing Thesis, AI, quantum mechanics and its various interpretations, quantum gravity, quantum computing, and the discreteness or continuity of the laws of physics. I strongly recommend 2x speed as usual.



  * [QIP'2026](https://qip2026.lu.lv/), the world's premier quantum computing conference, is happening right now in Riga, Latvia, locally organized by a team headed by the great Andris Ambainis, who I've known since 1999 and who's played a bigger role in my career than almost anyone else. I'm extremely sorry not to be there, despite what I understand to be the bitter cold. Family and teaching obligations mean that I jet around the world so much less than I used to. But many of my students and colleagues _are_ there, and I'll plan a blog post on news from QIP next week.


  * Greg Burnham of Epoch AI tells me that Epoch has released a [list of AI-for-math challenge problems](https://epoch.ai/frontiermath/open-problems)--i.e., open math problems that are below the level of P vs. NP and the Riemann Hypothesis but still of _very_ serious research interest, and that they're putting forward as worthy targets right now for trying to solve with AI assistance. A few examples that should be familiar to some _Shtetl-Optimized_ readers: degree vs. sensitivity of Boolean functions, improving the constant in the exponent of the General Number Field Sieve, giving an algorithm to test whether a knot has unknotting number of 1, and extending Apéry's proof of the irrationality of ζ(3) to other constants. Notably, for each problem, alongside a beautifully written description by a (human) expert, they also show you what the state-of-the-art models were able to do on that problem when they tried.


  * Tonight, on the arXiv, I noticed a nice survey article entitled [Computer Science Challenges in Quantum Computing: Early Fault-Tolerance and Beyond](https://arxiv.org/abs/2601.20247), by a distinguished list of authors including several who might be known to _Shtetl-Optimized_ readers. I haven't read the whole thing, but agreed with what I read.


  * There's been a [_major_ advance in understanding constant-depth quantum circuits](https://arxiv.org/abs/2601.03243), by my former PhD student Daniel Grier (now a professor at UCSD), along with _his_ PhD student Jackson Morris and Kewen Wu of IAS. Namely, they show that any function computable in TC0 (constant-depth, polynomial-size classical circuits with threshold gates) is also computable in QAC0 (constant-depth quantum circuits with 1-qubit and generalized Toffoli gates), as long as you provide many copies of the input. Two examples of such TC0 functions, which we therefore now know to be in QAC0 given many copies of the input, are Parity and Majority. It's been a [central open problem](https://arxiv.org/abs/quant-ph/9903046) of quantum complexity theory for a quarter-century to prove that Parity is _not_ in QAC0, complementing the celebrated result from the 1980s that Parity is not in _classical_ AC0 (a constant-depth circuit class that, for all we know, might be incomparable with QAC0). It's known that showing Parity∉QAC0 is equivalent to showing that QAC0 can't implement the "fanout" function, which makes many copies of an input bit. To say that we've gained a new understanding of why this problem is so hard would be an understatement.


