---
title: "David beats Go-liath"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/david-beats-go-liath"
---

In March 2016, to much fanfare, AlphaGo beat Go world champion Lee Sedol, convincingly, in a 5 game match, 4 to 1. Computers have only gotten faster since then; one might have thought that the matter was settled. And of course computers have only gotten faster ever since.

And then … something unexpected happened, just reported in the _Financial Times_ :

[Valentino Zocca 🇮🇹 🇪🇺 👍@ItalyHighTechMan beats machine at Go in human victory over AI | Financial Times #AI ft.comSubscribe to read | Financial Times3:16 PM · Feb 18, 2023](https://twitter.com/italyhightech/status/1626963929292210179?s=61&t=BtYm0IqdHRqCzCx0eoOPag)

And the human that won wasn’t even a professional Go player, let along a World Champion, just a strong amateur named Kellin Pelrine. And the match wasn’t even close; Pelrine beat a top AI system 14 games to 1, in a 15 match series. Almost seven years to the day after AlphaGo beat Sedol. 

As shocking as that might initially seem, we should not to be totally surprised. Seven years of AI has taught us that deep learning is unpredictable, and not always human like. “Adversarial attacks” like these have shown remarkable weakness, time and again, repeatedly establishing that what deep learning systems do just isn’t the same as what people do:

[](https://substackcdn.com/image/fetch/$s_!ZQ9v!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d7b1327-97a2-4143-8c57-eb7d8a302d3c_2000x794.png)

Partly for that reason, I always wondered whether AlphaGo really and deeply understood Go, or whether it was relying in part on massive data without true depth. In particular I wondered how well it would generalize to weird styles of play outside its training set, to the kind of edge cases that have plagued driverless cars and chatbots. 

Late last year, a Berkeley PhD student, Adam Gleave, working with the eminent Berkeley computer scientist Stuart Russell, discovered a specific way to fake out two of the better Go programs:

[Adam Gleave@ARGleaveEven superhuman RL agents can be exploited by adversarial policies. In [arxiv.org/abs/2211.00241](http://arxiv.org/abs/2211.00241) we train an adversary that wins 99% of games against KataGo 🖥️ set to top-100 European strength. Below our adversary 😈=⚫ plays a surprising strategy that tricks 🖥️=⚪ into losing.🧵 6:31 PM · Nov 2, 2022

* * *

155 Reposts · 888 Likes](https://twitter.com/argleave/status/1587875100732182530?s=61&t=BtYm0IqdHRqCzCx0eoOPag)

As Gleave explains

[Adam Gleave@ARGleaveThe 😈=⚫adversary stakes a small corner territory, and places weak stones in KataGo's complementary stake. This tricks 🖥️KataGo into passing before it's secured its territory. The ⚫adversary passes in turn, ending the game at a point favorable to ⚫: see [goattack.alignmentfund.org/adversarial-po…](https://goattack.alignmentfund.org/adversarial-policy-katago?row=0#no_search-board)goattack.alignmentfund.orgAdversarial Policies in Go - Game Viewer6:31 PM · Nov 2, 2022

* * *

2 Reposts · 40 Likes](https://twitter.com/argleave/status/1587875102950969344?s=12)

Even more strikingly, the out-of-the-box strategy beat KataGo, but it didn’t make for a good strategy against a strong human:

[Adam Gleave@ARGleaveAlthough the adversarial policy easily beats KataGo, it has not learned how to play Go effectively. My co-author @5kovt playing as white absolutely crushes the adversarial policy⚫: [goattack.alignmentfund.org/human-evaluati…](https://goattack.alignmentfund.org/human-evaluation?row=0#amateur_vs_adv-board) 6:31 PM · Nov 2, 2022

* * *

5 Reposts · 66 Likes](https://twitter.com/argleave/status/1587875107942191104?s=12)

In a DM in November, Gleave told me “We first came up with a hand-constructed adversarial board state that KataGo totally misevaluated, which convinced us that it has some major blindspots. After that finding an attack wasn't that hard.”

§

The just-reported showdown shows that Gleave’s strategy was no fluke; he was able to teach it to Pellrine (a Go-playing co-author on the paper), and Pellrine carried it to the finish line. 

Pellrine’s victory is a profound reminder that no matter how good deep-learning-driven AI looks when it is trained on an immense amount of data, we can never be sure that systems of this sort really can extend what they know to novel circumstances. We see the same problem, of course, with the many challenges that have stymied the driverless car industry, and the batshit crazy errors we have been seeing with chatbots in the last week.

All of these stumbles together serve as a poignant reminder that “deep learning” is still (just) a technical term describing a number of layers in a neural network, and not a technique that at all entails conceptual depth. 

As Stuart Russell put it, speaking to the _Financial Times_ , the Go victory shows that “ once again we’ve been far too hasty to ascribe superhuman levels of intelligence to machines”. 

Amen.

_**[Gary Marcus](http://garymarcus.com) **(@garymarcus),**** scientist, bestselling author, and entrepreneur, is a skeptic about current AI but genuinely wants to see the best AI possible for the world—and still holds a tiny bit of optimism. Sign up to his Substack (free!), and [listen to him on Ezra Klein](https://www.nytimes.com/2023/01/06/opinion/ezra-klein-podcast-gary-marcus.html). His most recent book, co-authored with Ernest Davis,[ Rebooting AI](http://rebooting.ai/), is one of Forbes’s 7 Must Read Books in AI. Watch for his new podcast in the Spring._

[Share](https://garymarcus.substack.com/p/david-beats-go-liath?utm_source=substack&utm_medium=email&utm_content=share&action=share)
