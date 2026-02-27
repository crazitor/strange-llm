---
title: "Ryan Williams strikes again"
author: "Scott Aaronson"
date: "Mon, 24 Feb 2025"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=8680"
---

**Update (Feb. 27):** While we're on the subject of theoretical computer science, friends-of-the-blog Adam Klivans and Raghu Meka have asked me to publicize that [STOC'2025 TheoryFest](https://stoc2025theoryfest.netlify.app/), to be held June 23-27 in Prague, is eagerly seeking proposals for workshops. The deadline is March 9th.

* * *

  * Because of a recent [breakthrough](https://eccc.weizmann.ac.il/report/2023/174/) by Cook and Mertz on Tree Evaluation, Ryan [now shows that](https://eccc.weizmann.ac.il/report/2025/017/) every problem solvable in t time on a multitape Turing machine is also solvable in close to √t space  

  * As a consequence, he shows that there are problems solvable in O(n) space that require nearly quadratic time on multitape Turing machines  

  * If this could be applied recursively to boost the polynomial degree, then P≠PSPACE  

  * On Facebook, someone summarized this result as “there exists an elephant that can’t fit through a mouse hole.” I pointed out that for decades, we only knew how to show there was a blue whale that didn’t fit through the mouse hole  

  * I’ll be off the Internet for much of today (hopefully only today?) because of jury duty! Good thing you’ll have Ryan’s amazing new paper to keep y’all busy…



**Update (Feb. 25):** It occurs to me that the new result is yet another vindication for Ryan’s style of doing complexity theory—a style that I’ve variously described with the phrases “ironic complexity theory” and “caffeinated alien reductions,” and that’s all about using surprising upper bounds for one thing to derive unsurprising lower bounds for a different thing, sometimes with a vertigo-inducing chain of implications in between. This style has a decidedly retro feel to it: it’s been clear since the 1960s both that there _are_ surprising algorithms (for example for matrix multiplication), and that the time and space hierarchy theorems let us prove at least _some_ separations. The dream for decades was to go fundamentally beyond that, separating complexity classes by “cracking their codes” and understanding the space of all possible things they can express. Alas, except for low-level circuit classes, that program has largely failed, for reasons partly explained by the Natural Proofs barrier. So Ryan achieves his successes by simply doubling down on two things that _have_ worked since the beginning: (1) finding even more surprising algorithms (or borrowing surprising algorithms from other people), and then (2) combining those algorithms with time and space hierarchy theorems in clever ways to achieve new separations.
