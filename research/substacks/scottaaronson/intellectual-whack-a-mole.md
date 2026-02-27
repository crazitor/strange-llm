---
title: "Intellectual whack-a-mole"
author: "Scott Aaronson"
date: "Thu, 09 Aug 2007"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=261"
---

Several readers have now written to me independently, asking for my reaction to the following paper:

> [An Optical Solution For The Traveling Salesman Problem](http://www.opticsexpress.org/abstract.cfm?id=140598)  
>  Tobias Haist and Wolfgang Osten
> 
> Abstract: We introduce an optical method based on white light interferometry in order to solve the well-known NP–complete traveling salesman problem. To our knowledge it is the first time that a method for the reduction of non–polynomial time to quadratic time has been proposed. We will show that this achievement is limited by the number of available photons for solving the problem. It will turn out that this number of photons is proportional to NN for a traveling salesman problem with N cities and that for large numbers of cities the method in practice therefore is limited by the signal–to–noise ratio. The proposed method is meant purely as a gedankenexperiment.

Look, this is _really_ not hard. You _really_ don't need a world CompuCrackpotism expert to tell you what to think of this. If you read carefully, the authors were actually kind enough to explain themselves, right in the abstract, why their proposal doesn't scale. (This, of course, is entirely to their credit, and puts them above ~98% of their colleagues in the burgeoning intersection of computer science, physics, and non-correctness.)

_Hint:_ If the number of photons scales exponentially with N, and the photons have high enough energies that you can detect them, then the energy also scales exponentially with N. So by the Schwarzschild bound, the volume also scales exponentially with N; therefore, by locality, so does the time.
