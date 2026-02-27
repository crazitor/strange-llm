---
title: "The Aaronson-Ambainis Conjecture (2008-2019)"
author: "Scott Aaronson"
date: "Sun, 17 Nov 2019"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=4414"
---

**Update:** Sadly, Nathan Keller and Ohad Klein tell me that they've retracted their preprint, because of what currently looks like a fatal flaw in Lemma 5.3, uncovered by Paata Ivanishvili. I wish them the best of luck in fixing the problem. In the meantime, I'm leaving up this post for "historical" reasons.

Around 1999, one of the first things I ever did in quantum computing theory was to work on a problem that [Fortnow and Rogers](https://arxiv.org/abs/cs/9811023) suggested in a paper: is it possible to separate [P](https://en.wikipedia.org/wiki/P_\(complexity\)) from [BQP](https://en.wikipedia.org/wiki/BQP) relative to a [random oracle](https://en.wikipedia.org/wiki/Random_oracle)? (That is, without first needing to separate P from PSPACE or whatever in the real world?) Or to the contrary: suppose that a quantum algorithm Q makes T queries to a Boolean input string X. Is there then a classical simulation algorithm that makes poly(T) queries to X, and that approximates Q's acceptance probability for _most_ values of X? Such a classical simulation, were it possible, would still be consistent with the existence of quantum algorithms like [Simon's](https://en.wikipedia.org/wiki/Simon%27s_problem) and [Shor's](https://en.wikipedia.org/wiki/Shor%27s_algorithm), which are able to achieve exponential (and even greater) speedups in the black-box setting. It would simply demonstrate the importance, for Simon's and Shor's algorithms, of global structure that makes the string X extremely _non_ -random: for example, encoding a periodic function (in the case of Shor's algorithm), or encoding a function that hides a secret string s (in the case of Simon's). It would underscore that superpolynomial quantum speedups depend on structure.

I never managed to solve this problem. Around 2008, though, I noticed that a solution would follow from a perhaps-not-obviously-related conjecture, about _influences_ in low-degree polynomials. Namely, let p:Rn→R be a degree-d real polynomial in n variables, and suppose p(x)∈[0,1] for all x∈{0,1}n. Define the _variance_ of p to be  
Var(p):=Ex,y[|p(x)-p(y)|],  
and define the _influence_ of the ith variable to be  
Infi(p):=Ex[|p(x)-p(xi)|].  
Here the expectations are over strings in {0,1}n, and xi means x with its ith bit flipped between 0 and 1. Then the conjecture is this: there must be some variable i such that Infi(p) ≥ poly(Var(p)/d) (in other words, that "explains" a non-negligible fraction of the variance of the entire polynomial).

Why would this conjecture imply the statement about quantum algorithms? Basically, because of the seminal result of [Beals et al.](https://arxiv.org/abs/quant-ph/9802049) from 1998: that if a quantum algorithm makes T queries to a Boolean input X, then its acceptance probability can be written as a real polynomial over the bits of X, of degree at most 2T. Given that result, if you wanted to classically simulate a quantum algorithm Q on most inputs--and if you only cared about query complexity, not computation time--you'd simply need to do the following:  
(1) Find the polynomial p that represents Q's acceptance probability.  
(2) Find a variable i that explains at least a 1/poly(T) fraction of the total remaining variance in p, and query that i.  
(3) Keep repeating step (2), until p has been restricted to a polynomial with not much variance left--i.e., to nearly a constant function p(X)=c. Whenever that happens, halt and output the constant c.  
The key is that by hypothesis, this algorithm will halt, with high probability over X, after only poly(T) steps.

Anyway, around the same time, Andris Ambainis had a major break on a different problem that I'd told him about: namely, whether randomized and quantum query complexities are polynomially related for all partial functions with permutation symmetry (like the collision and the element distinctness functions). Andris and I decided to write up the two directions jointly. The result was our 2011 paper entitled [The Need for Structure in Quantum Speedups](https://arxiv.org/abs/0911.0996).

Of the two contributions in the "Need for Structure" paper, the one about random oracles and influences in low-degree polynomials was clearly the weaker and less satisfying one. As the reviewers pointed out, that part of the paper didn't solve anything: it just reduced one unsolved problem to a new, slightly different problem that was _also_ unsolved. Nevertheless, that part of the paper acquired a life of its own over the ensuing decade, as the world's experts in analysis of Boolean functions and polynomials began referring to the "Aaronson-Ambainis Conjecture." Ryan O'Donnell, Guy Kindler, and many others had a stab. I even got Terry Tao to spend an hour or two on the problem when I visited UCLA.

Now, at long last, Nathan Keller and Ohad Klein say they've proven the Aaronson-Ambainis Conjecture, in a preprint whose title is a riff on ours: ["Quantum Speedups Need Structure."](https://arxiv.org/abs/1911.03748)

Their paper hasn't yet been peer-reviewed, and I haven't yet carefully studied it, but I _could_ and _should_ : at 19 pages, it looks very approachable and clear, if not as radically short as (say) [Huang's proof of the Sensitivity Conjecture](https://scottaaronson.blog/?p=4229). Keller and Klein's argument subsumes all the earlier results that I knew would need to be subsumed, and involves all the concepts (like a real analogue of block sensitivity) that I knew would need to be involved somehow.

My plan had been as follows:  
(1) Read their paper in detail. Understand every step of their proof.  
(2) Write a blog post that reflects my detailed understanding.

Unfortunately, this plan did not sufficiently grapple with the fact that I now have two kids. It got snagged for a week at step (1). So I'm now executing an alternative plan, which is to jump immediately to the blog post.

Assuming Keller and Klein's result holds up--as I expect it will--by combining it with the observations in my and Andris's paper, one immediately gets an explanation for why no one has managed to separate P from BQP relative to a _random_ oracle, but only relative to non-random oracles. This complements the work of [Kahn, Saks, and Smyth](https://www.uncg.edu/mat/faculty/cdsmyth/thesis.pdf), who around 2000 gave a precisely analogous explanation for the difficulty of separating P from NP∩coNP relative to a random oracle.

Unfortunately, the polynomial blowup is quite enormous: from a quantum algorithm making T queries, Keller and Klein apparently get a classical algorithm making O(T18) queries. But such things can almost always be massively improved.

Feel free to use the comments to ask any questions about this result or its broader context. I'll either do my best to answer from the limited amount I know, or else I'll pass the questions along to Nathan and Ohad themselves. Maybe, at some point, I'll even be forced to understand the new proof.

Congratulations to Nathan and Ohad!

**Update (Nov. 20):** Tonight I finally did what I should've done two weeks ago, and worked through the paper from start to finish. Modulo some facts about noise operators, hypercontractivity, etc. that I took on faith, I now have a reasonable (albeit imperfect) understanding of the proof. It's great!

In case it's helpful to anybody, here's my one-paragraph summary of how it works. First, you hit your bounded degree-d function f with a random restriction to attenuate its higher-degree Fourier coefficients (reminiscent of [Linial-Mansour-Nisan](http://www.ma.huji.ac.il/~ehudf/courses/anal09/LMN.pdf)).  Next, in that attenuated function, you find a small "coalition" of influential variables--by which we mean, a set of variables for which there's _some_ assignment that substantially biases f.  You keep iterating--finding influential coalitions in subfunctions on n/4, n/8, etc. variables. All the while, you keep track of _the norm of the vector of all the block-sensitivities of all the inputs_ (the authors don't clearly explain this in the intro, but they reveal it near the end). Every time you find another influential coalition, that norm goes down by a little, but by approximation theory, it can only go down O(d2) times until it hits rock bottom and your function is nearly constant. By the end, you'll have approximated f itself by a decision tree of depth poly(d, 1/ε, log(n)).  Finally, you get rid of the log(n) term by using the fact that f essentially depended on at most exp(O(d)) variables anyway. 

Anyway, I'm not sure how helpful it is to write more: the [paper itself](https://arxiv.org/pdf/1911.03748.pdf) is about 95% as clear as it could possibly be, and even where it isn't, you'd probably need to read it first (and, uh, know something about influences, block sensitivity, random restrictions, etc.) before any further clarifying remarks would be of use. But happy to discuss more in the comments, if anyone else is reading it.
