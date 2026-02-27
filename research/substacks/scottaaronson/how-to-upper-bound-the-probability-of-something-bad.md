---
title: "How to upper-bound the probability of something bad"
author: "Scott Aaronson"
date: "Fri, 13 Apr 2018"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=3712"
---

Scott Alexander has a [new post](http://slatestarcodex.com/2018/04/12/recommendations-vs-guidelines/) decrying how rarely experts encode their knowledge in the form of detailed guidelines with conditional statements and loops--or what one could also call flowcharts or expert systems--rather than just blanket recommendations.  He gives, as an illustration of what he's looking for, an algorithm that a psychiatrist might use to figure out which antidepressants or other treatments will work for a specific patient--with the huge proviso that you shouldn't try his algorithm at home, or (most importantly) sue him if it doesn't work.

Compared to a psychiatrist, I have the huge advantage that if _my_ professional advice fails, normally no one gets hurt or gets sued for malpractice or commits suicide or anything like that.  OK, but what do I actually know that can be encoded in if-thens?

Well, one of the commonest tasks in the day-to-day life of any theoretical computer scientist, or mathematician of the Erdös flavor, is to _upper bound the probability that something bad will happen_ : for example, that your randomized algorithm or protocol will fail, or that your randomly constructed graph or code or whatever it is won't have the properties needed for your proof.

So without further ado, here are my secrets revealed, my ten-step plan to probability-bounding and computer-science-theorizing success.

**Step 1.** "1" is definitely an upper bound on the probability of your bad event happening.  Check whether that upper bound is good enough.  (Sometimes, as when this is an inner step in a larger summation over probabilities, the answer will actually be yes.)

**Step 2.** Try using [Markov’s inequality](https://en.wikipedia.org/wiki/Markov%27s_inequality) (a nonnegative random variable exceeds its mean by a factor of k at most a 1/k fraction of the time), combined with its close cousin in indispensable obviousness, the [union bound](https://en.wikipedia.org/wiki/Boole%27s_inequality) (the probability that any of several bad events will happen, is at most the sum of the probabilities of each bad event individually).  About half the time, you can stop right here.

**Step 3.** See if the bad event you’re worried about involves a sum of independent random variables exceeding some threshold. If it does, hit that sucker with a [Chernoff](https://en.wikipedia.org/wiki/Chernoff_bound) or [Hoeffding](https://en.wikipedia.org/wiki/Hoeffding%27s_inequality) bound.

**Step 4.** If your random variables aren't independent, see if they at least form a [martingale](https://en.wikipedia.org/wiki/Martingale_\(probability_theory\)): a fancy word for a sum of terms, each of which has a mean of 0 conditioned on all the earlier terms, even though it might depend on the earlier terms in subtler ways.  If so, [Azuma](https://en.wikipedia.org/wiki/Azuma%27s_inequality) your problem into submission.

**Step 5.** If you don’t have a martingale, but you still feel like your random variables are only weakly correlated, try calculating the [variance](https://en.wikipedia.org/wiki/Variance) of whatever combination of variables you care about, and then using [Chebyshev’s inequality](https://en.wikipedia.org/wiki/Chebyshev%27s_inequality): the probability that a random variable differs from its mean by at most k times the standard deviation (i.e., the square root of the variance) is at most 1/k2.  If the variance doesn't work, you can try calculating some higher moments too--just beware that, around the 6th or 8th moment, you and your notebook paper will likely both be exhausted.

**Step 6.**  OK, umm … see if you can upper-bound the [variation distance](https://en.wikipedia.org/wiki/Total_variation_distance_of_probability_measures) between your probability distribution and a different distribution for which it’s already known (or is easy to see) that it’s unlikely that anything bad happens. A good example of a tool you can use to upper-bound variation distance is [Pinsker’s inequality](https://en.wikipedia.org/wiki/Pinsker%27s_inequality).

**Step 7.** Now is the time when you start ransacking Google and Wikipedia for things like the [Lovász Local Lemma](https://en.wikipedia.org/wiki/Lov%C3%A1sz_local_lemma), and [concentration bounds for low-degree polynomials](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/03/polycon.pdf), and [Hölder's inequality](https://en.wikipedia.org/wiki/H%C3%B6lder%27s_inequality), and [Talagrand's inequality](https://en.wikipedia.org/wiki/Talagrand%27s_concentration_inequality), and other [isoperimetric-type inequalities](https://en.wikipedia.org/wiki/Isoperimetric_inequality), and [hypercontractive inequalities](https://www.cs.cmu.edu/~odonnell/boolean-analysis/lecture16.pdf), and other stuff that you’ve heard your friends rave about, and have even seen successfully used at least twice, but there’s no way you’d remember off the top of your head under what conditions any of this stuff applies, or whether any of it is good enough for your application. (Just between you and me: you may have _already_ visited Wikipedia to refresh your memory about the earlier items in this list, like the Chernoff bound.) "Try a hypercontractive inequality" is surely the analogue of the psychiatrist’s “try electroconvulsive therapy,” for a patient on whom all milder treatments have failed.

**Step 8.** So, these bad events … how bad are they, anyway? Any chance you can live with them?  (See also: Step 1.)

**Step 9.** You _can’t_ live with them? Then back up in your proof search tree, and look for a whole different approach or algorithm, which would make the bad events less likely or even kill them off altogether.

**Step 10.** Consider the possibility that the statement you’re trying to prove is false--or if true, is far beyond any existing tools.  (This might be the analogue of the psychiatrist's: consider the possibility that evil conspirators _really  are_ out to get your patient.)
