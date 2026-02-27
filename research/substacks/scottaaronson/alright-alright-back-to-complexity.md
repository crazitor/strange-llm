---
title: "Alright, alright, back to complexity"
author: "Scott Aaronson"
date: "Wed, 26 Apr 2006"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=80"
---

I've learned my lesson, at least for the next day or two.

And speaking of learning -- in computational learning theory, there's an "obvious" algorithm for learning a function from random samples. Here's the algorithm: output any hypothesis that minimizes the error on those samples.

I'm being intentionally vague about what the learning model is -- since as soon as you specify a model, it seems like some version of that algorithm is what you want to do, if you want the best tradeoff between the number of samples and the error of your hypothesis. For example, if you're trying to learn a Boolean function from a class C, then you want to pick any hypothesis from C that's consistent with all your observations. If you're trying to learn a Boolean function based on noisy observations, then you want to pick any hypothesis that minimizes the total number of disagreements. If you're trying to learn a degree-d real polynomial based on observations subject to Gaussian noise, then you want to pick any degree-d polynomial that minimizes the least-squared error, and so on.

Here's my question: is the "obvious" algorithm always the best one, or is there a case where a different algorithm needs asymptotically fewer samples? That is, do you ever want to pick a hypothesis that disagrees with more of your observations over one that disagrees with less?

While I'm on the subject, have you ever wished you could help Scott Aaronson do his actual research, and even be thanked -- by name -- in the acknowledgments of one of his papers? Well then, don't miss this chance! All you have to do is read [this](http://www.cs.technion.ac.il/%7Eshai/noga.ps.gz) seminal paper by Alon, Ben-David, Cesa-Bianchi, and Haussler, and then tell me what upper bound on the sample complexity of p-concept learning follows from their results. (Perversely, all they prove in the paper is that some finite number of samples suffices -- must be a mathematician thing.)
