---
title: "Postdocs, matrix multiplication, and WSJ: yet more shorties"
author: "Scott Aaronson"
date: "Fri, 07 Oct 2022"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=6745"
---

I'm proud to say that [Nick Hunter-Jones](https://twitter.com/nickrhj) and [Matteo Ippoliti](https://matteoippoliti.com/)--both of whom work at the interface between quantum information science and condensed-matter physics (Nick closer to the former and Matteo to the latter)--have joined the physics faculty at UT Austin this year. And Nick, Matteo, and I are jointly seeking postdocs to start in Fall 2023! [Please check out our call for applications here.](https://academicjobsonline.org/ajo/jobs/23104) The deadline is December 1; you apply through AcademicJobsOnline rather than by emailing me as in past years.

* * *

The big news in AI and complexity theory this week was DeepMind's [AlphaTensor](https://www.deepmind.com/blog/discovering-novel-algorithms-with-alphatensor), and its automated discovery of new algorithms for matrix multiplication. ([See here for the _Nature_ paper.](https://www.nature.com/articles/s41586-022-05172-4)) More concretely, they've used AI to discover (among other things) an algorithm for multiplying 4×4 matrices, over finite fields of characteristic 2, using only 47 scalar multiplications. This beats the 49=7×7 that you'd get from [Strassen's algorithm](https://en.wikipedia.org/wiki/Strassen_algorithm). There are other improvements for other matrix dimensions, many of which work over fields of other characteristics.

Since I've seen confusion about the point on social media: this does _not_ improve over the best known asymptotic exponent for matrix multiplication, which over any field, still stands at the human-discovered 2.373 (meaning, we know how to multiply two N×N matrices in O(N2.373) time, but not faster). But it _does_ asymptotically improve over Strassen's O(N2.81) algorithm from 1968, conceivably even in a way that could have practical relevance for multiplying hundreds-by-hundreds or thousands-by-thousands matrices over F2.

Way back in 2007, I [gave a talk](http://www.scottaaronson.com/talks/wildidea.ppt) at MIT CSAIL's "Wild and Crazy Ideas Session," where I explicitly proposed to use computer search to look for faster algorithms for 4×4 and 5×5 matrix multiplication. The response I got at the time was that it was hopeless, since the search space was already too huge. Of course, that was before the deep learning revolution.

* * *

This morning, the _Wall Street Journal_ published an [article by Karen Hao](https://www.wsj.com/articles/china-competing-us-quantum-computing-11664997892) about competition between China and the US in quantum computing. Unfortunately paywalled, but includes the following passage:

> Meanwhile, American academics say it’s gotten harder for Chinese students to obtain visas to conduct quantum research in the U.S. “It’s become common knowledge that when Chinese students or postdocs come to the U.S., they can’t say they’re doing quantum computing,” says Scott Aaronson, director of the Quantum Information Center at the University of Texas, Austin.
