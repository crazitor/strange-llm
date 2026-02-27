---
title: "D-Wave Easter Spectacular"
author: "Scott Aaronson"
date: "Sun, 08 Apr 2007"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=225"
---

Look, I _promise_ this will be the last D-Wave post in a while. But there have been two developments that, as Planet Earth's primary D-Wave skepticism clearinghouse, I feel a duty to report.

First, Jason Pontin's article in the Sunday _New York Times_ [has appeared](http://www.nytimes.com/2007/04/08/business/yourmoney/08slip.html?ref=business). It's not perfect, but to get in a description of quantum computing that was even _somewhat_ accurate required a long, word-by-word and phrase-by-phrase battle with the editors of the business section.

Second, Umesh Vazirani sent me a document summarizing the skeptical case against D-Wave, which anyone coming to this blog from the _Tech Review_ or _New York Times_ might find helpful. (Hey, as long as you're here, stick around for a bit!) I've posted Umesh's criticisms below.

Finally, Happy Easter from all of us here in the shtetl!

**Reasons To Be Skeptical About D-Wave 's Claims**

by Guest Blogger [Umesh Vazirani](http://www.cs.berkeley.edu/~vazirani/)

**1\. An Unconvincing Demo:** D-wave's demo consisted of a computer in a box that could solve simple problems. We have no way of knowing whether the computer in the box was an ordinary classical computer or a quantum computer. For the problem the computer solves -- finding ground states for 16 bit Ising problems -- a classical computer would work just as quickly. This demo is the only public evidence D-wave has presented in support of its claims.

**2\. A Physics Breakthrough?:** Achieving 16 coherent superconducting quantum bits would be quite a breakthrough. Physicists working on superconducting qubits have not been able to achieve more than two coherent quantum bits in the lab. In the absence of evidence from D-Wave that their 16 qubits are coherent, scientists are understandably skeptical. If D-Wave's qubits are not coherent, as many scientists suspect, their computer would be classical, not quantum. This would still be consistent with the results of the demo, since the decohering qubits would act like classical random bits, and the adiabatic computer would act like a classical computer implementing simulated annealing, which would be quite fast for a small 16 bit Ising problem. It is possible to test the quantum states of D-Wave's computer for coherence, but Geordie Rose's statements suggest that no such tests have been made.

**3\. Claims of Big Algorithmic Breakthrough Without Evidence:** 16-bit quantum computers are useless from a practical standpoint because they can only solve very small problems that could just as easily be solved using a classical computer. Thus, D-Wave's demo, even if it really was a quantum computer, will only be practically useful if the technology will scale to the larger problems that cannot be solved with a classical computer. Unless D-Wave has made a major algorithmic breakthrough as well as a major practical one, however, D-Wave's computer, even if implemented with thousands of qubits, will not provide a speedup over classical computers. D-Wave does not implement a general purpose quantum computer, only one that can implement adiabatic optimization. They wish to use it to solve the Ising model, which is thought to be beyond the reach of classical computers, but there is no known efficient algorithm for solving the Ising model using this adiabatic approach. It is possible to achieve a quadratic speedup for unstructured search problems using adiabatic optimization, but that result requires an ability to tune the rate of the adiabatic process -- something which appears to researchers to be extremely hard if not impossible for the Ising problem. Geordie Rose's public statements suggest that he doesn't understand this issue, which makes computer scientists skeptical that any breakthrough has been made.

**To summarize:** For D-Wave to achieve a practically useful quantum computer using their technology, they would have to have made a breakthrough in physics, as well as a breakthrough in the design of their algorithm. Scientists are skeptical both because D-Wave has failed to provide any supporting evidence, and also because their public statements suggest a lack of understanding of the issues involved.

You might ask why researchers are putting so much energy into debunking the D-Wave hype. One reason is that QC researchers feel a responsibility to the public to not overhype quantum computers. Quantum computing is an exciting field that has caught the imagination of the public. This is a good thing. But if the quantum computing effort starts to mingle fact with fiction, then the entire effort loses its credibility.

Another reason is that D-Wave's unsupported claims are undermining the efforts of the researchers who are working very hard on these problems. It's as if there was a new biotech company claiming to be at the brink of a revolutionary cure for cancer. If it is true, it is great, but if it's not, then it undermines the efforts of the legitimate cancer researchers.
