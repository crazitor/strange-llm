---
title: "Avi Wigderson’s “Permanent” Impact on Me"
author: "Scott Aaronson"
date: "Wed, 12 Oct 2016"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=2925"
---

_The following is the lightly-edited transcript of a talk that I gave a week ago, on Wednesday October 5, at[Avi Wigderson's 60th birthday conference](https://www.math.ias.edu/avi60) at the Institute for Advanced Study in Princeton. Videos of all the talks (including mine) are [**now available here**](https://video.ias.edu/sm)._

_Thanks so much to Sanjeev Arora, Boaz Barak, Ran Raz, Peter Sarnak, and Amir Shpilka for organizing the conference and for inviting me to speak; to all the other participants and speakers for a great conference; and of course to Avi himself for being Avi. -SA_

* * *

I apologize that I wasn't able to prepare slides for today's talk. But the good news is that, ever since I moved to Texas two months ago, I now carry concealed chalk everywhere I go. [Pull chalk out of pocket]

My history with Avi goes back literally half my life. I spent a semester with him at Hebrew University, and then a year with him as a postdoc here at IAS. Avi has played a bigger role in my career than just about anyone--he helped me professionally, he helped me intellectually, and once I dated and then married an Israeli theoretical computer scientist (who was also a postdoc in Avi's group), Avi even helped me learn Hebrew. Just today, Avi taught me the Hebrew word for the permanent of a matrix. It turns out that it's [throaty noises] _pehhrmahnent_.

But it all started with a talk that Avi gave in Princeton in 2000, which I attended as a prospective graduate student. That talk was about the following function of an n×n matrix A∈Rn×n, the [_permanent_](https://en.wikipedia.org/wiki/Permanent):

$$ \text{Per}(A) = \sum_{\sigma \in S_n} \prod_{i=1}^n a_{i,\sigma(i)}. $$

Avi contrasted that function with a superficially similar function, the _determinant_ :

$$ \text{Det}(A) = \sum_{\sigma \in S_n} (-1)^{\text{sgn}(\sigma)} \prod_{i=1}^n a_{i,\sigma(i)}. $$

In this talk, I want to share a few of the amazing things Avi said about these two functions, and how the things he said then reverberated through my entire career.

Firstly, like we all learn in kindergarten or whatever, the determinant is computable in polynomial time, for example by using Gaussian elimination. By contrast, Valiant proved in 1979 that [computing the permanent is #P-complete](https://en.wikipedia.org/wiki/Sharp-P-completeness_of_01-permanent)--which means, at least as hard as any combinatorial counting problem, a class believed to be even harder than NP-complete.

So, despite differing from each other only by some innocent-looking -1 factors, which the determinant has but the permanent lacks, these two functions effectively engage different regions of mathematics. The determinant is linear-algebraic and geometric; it's the product of the eigenvalues and the volume of the parallelipiped defined by the row vectors. But the permanent is much more stubbornly combinatorial. It's not quite as pervasive in mathematics as the determinant is, though it does show up. As an example, if you have a bipartite graph G, then the permanent of G's adjacency matrix counts the number of perfect matchings in G.

When n=2, computing the permanent doesn't look too different from computing the determinant: indeed, we have

$$  
\text{Per}\left(  
\begin{array}  
[c]{cc}%  
a & b\\\  
c & d  
\end{array}  
\right) =\text{Det}\left(  
\begin{array}  
[c]{cc}%  
a & -b\\\  
c & d  
\end{array}  
\right).  
$$

But as n gets larger, the fact that the permanent is #P-complete means that it _must_ get exponentially harder to compute than the determinant, unless basic complexity classes collapse. And indeed, to this day, the fastest known algorithm to compute an n×n permanent, [_Ryser 's algorithm_](https://en.wikipedia.org/wiki/Computing_the_permanent#Ryser_formula), takes O(n2n) time, which is only modestly better than the brute-force algorithm that just sums all n! terms.

Yet interestingly, not _everything_ about the permanent is hard. So for example, if A is nonnegative, then in 1997, [Jerrum, Sinclair, and Vigoda](http://www.cc.gatech.edu/~vigoda/Permanent.pdf) famously gave a polynomial-time randomized algorithm to approximate Per(A) to within a 1+ε multiplicative factor, for ε>0 as small as you like. As an even simpler example, if A is nonnegative and you just want to know whether its permanent is zero or nonzero, that's equivalent to deciding whether a bipartite graph has at least one perfect matching. And we all know that that can be done in polynomial time.

* * *

OK, but the usual algorithm from the textbooks that puts the matching problem in the class P is already a slightly nontrivial one--maybe first grade rather than kindergarten! It involves repeatedly using depth-first search to construct augmenting paths, then modifying the graph, etc. etc.

Sixteen years ago in Princeton, the first thing Avi said that blew my mind is that there's a vastly simpler polynomial-time algorithm to decide whether a bipartite graph has a perfect matching--or equivalently, to decide whether a nonnegative matrix has a zero or nonzero permanent. This algorithm is not quite as efficient as the textbook one, but it makes up for it by being more magical.

So here's what you do: you start with the 0/1 adjacency matrix of your graph. I'll do a 2×2 example, since that's all I'll be able to compute on the fly:

$$ \left(  
\begin{array}  
[c]{cc}%  
1 & 1\\\  
0 & 1  
\end{array}  
\right). $$

Then you normalize each row so it sums to 1. In the above example, this would give

$$ \left(  
\begin{array}  
[c]{cc}%  
\frac{1}{2} & \frac{1}{2} \\\  
0 & 1  
\end{array}  
\right). $$

Next you normalize each _column_ so it sums to 1:

$$ \left(  
\begin{array}  
[c]{cc}%  
1 & \frac{1}{3} \\\  
0 & \frac{2}{3}  
\end{array}  
\right). $$

OK, but now the problem is that the rows are no longer normalized, so you normalize them again:

$$ \left(  
\begin{array}  
[c]{cc}%  
\frac{3}{4} & \frac{1}{4} \\\  
0 & 1  
\end{array}  
\right). $$

Then you normalize the columns again, and so on. You repeat something like n3log(n) times. If, after that time, all the row sums and column sums have become within ±1/n of 1, then you conclude that the permanent was nonzero and the graph had a perfect matching. Otherwise, the permanent was zero and the graph had no perfect matching.

What gives? Well, it's a nice exercise to prove why this works. I'll just give you a sketch: first, when you multiply any row or column of a matrix by a scalar, you multiply the permanent by that same scalar. By using that fact, together with the arithmetic-geometric mean inequality, it's possible to prove that, in every iteration but the first, when you rebalance all the rows or all the columns to sum to 1, you can't be decreasing the permanent. The permanent increases monotonically.

Second, _if_ the permanent is nonzero, then after the first iteration it's at least 1/nn, simply because we started with a matrix of 0's and 1's.

Third, the permanent is always at most the product of the row sums or the product of the column sums, which after the first iteration is 1.

Fourth, at any iteration where there's some row sum or column sum that's far from 1, rescaling must not only increase the permanent, but increase it by an appreciable amount--like, a 1+1/n2 factor or so.

Putting these four observations together, we find that _if_ the permanent is nonzero, then our scaling procedure must terminate after a polynomial number of steps, with every row sum and every column sum close to 1--since otherwise, the permanent would just keep on increasing past its upper bound of 1.

But a converse statement is also true. Suppose the matrix can be scaled so that every row sum and every column sum gets within ±1/n of 1. Then the rescaled entries define a _flow_ through the bipartite graph, with roughly the same amount of flow through each of the 2n vertices. But if such a flow exists, then [Hall's Theorem](https://math.berkeley.edu/~sagrawal/su14_math55/notes_hall.pdf) tells you that there must be a perfect matching (and hence the permanent must be nonzero)--since if a matching _didn 't_ exist, then there would necessarily be a bottleneck preventing the flow.

Together with Nati Linial and Alex Samorodnitsky, Avi [generalized this](http://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/LSW98/lsw00.pdf) to show that scaling the rows and columns gives you a polynomial-time algorithm to _approximate_ the permanent of a nonnegative matrix. This basically follows from the so-called [Egorychev-Falikman Theorem](https://en.wikipedia.org/wiki/Permanent#Van_der_Waerden.27s_conjecture), which says that the permanent of a doubly stochastic matrix is at least n!/nn. The approximation ratio that you get this way, ~en, isn't nearly as good as Jerrum-Sinclair-Vigoda's, but the advantage is that the algorithm is _deterministic_ (and also ridiculously simple).

For myself, though, I just filed away this idea of matrix scaling for whenever I might need it. It didn't take long. A year after Avi's lecture, when I was a beginning grad student at Berkeley, I was obsessing about the foundations of quantum mechanics. Specifically, I was obsessing about the fact that, when you measure a quantum state, the rules of quantum mechanics tell you how to calculate the probability that you'll see a particular outcome. But the rules are silent about so-called _multiple-time_ or _transition_ probabilities. In other words: suppose we adopt Everett's [Many-Worlds](https://en.wikipedia.org/wiki/Many-worlds_interpretation) view, according to which quantum mechanics needs to be applied consistently to every system, regardless of scale, so in particular, the state of the entire universe (including us) is a quantum superposition state. We perceive just one branch, but there are also these other branches where we made different choices or where different things happened to us, etc.

OK, fine: for me, that's not the troubling part! The troubling part is that quantum mechanics rejects as meaningless questions like the following: given that you're in _this_ branch of the superposition at time t1, what's the probability that you'll be in _that_ branch at time t2, after some unitary transformation is applied? Orthodox quantum mechanics would say: well, either someone measured you at time t1, in which case their act of measuring collapsed the superposition and created a whole new situation. Or else no one measured at t1--but in that case, your state at time t1 _was_ the superposition state, full stop. It's sheer metaphysics to imagine a "real you" that jumps around from one branch of the superposition to another, having a sequence of definite experiences.

Granted, in practice, branches of the universe's superposition that split from each other tend never to rejoin, for the same thermodynamic reasons why eggs tend never to unscramble themselves. And as long as the history of the Everettian multiverse has the structure of a tree, we _can_ sensibly define transition probabilities. But if, with some technology of the remote future, we were able to do quantum interference experiments on human brains (or other conscious entities), the rules of quantum mechanics would no longer predict what those beings should see--not even probabilistically.

I was interested in the question: suppose we just wanted to _postulate_ transition probabilities, with the transitions taking place in some fixed orthogonal basis. What would be a mathematically reasonable way to do that? And it occurred to me that one thing you could do is the following. Suppose for simplicity that you have a pure quantum state, which is just a unit vector of n complex numbers called _amplitudes_ :

$$ \left(  
\begin{array}  
[c]{c}%  
\alpha_{1}\\\  
\vdots\\\  
\alpha_{n}%  
\end{array}  
\right) $$

Then the first rule of quantum mechanics says that you can apply any _unitary transformation_ U (that is, any norm-preserving linear transformation) to map this state to a new one:

$$ \left(  
\begin{array}  
[c]{c}%  
\beta_{1}\\\  
\vdots\\\  
\beta_{n}%  
\end{array}  
\right) =\left(  
\begin{array}  
[c]{ccc}%  
u_{11} & \cdots & u_{1n}\\\  
\vdots & \ddots & \vdots\\\  
u_{n1} & \cdots & u_{nn}%  
\end{array}  
\right) \left(  
\begin{array}  
[c]{c}%  
\alpha_{1}\\\  
\vdots\\\  
\alpha_{n}%  
\end{array}  
\right). $$

The second rule of quantum mechanics, the famous _Born Rule_ , says that if you measure in the standard basis before applying U, then the probability that you'll find youself in state i equals |αi|2. Likewise, if you measure in the standard basis _after_ applying U, the probability that you'll find youself in state j equals |βj|2.

OK, but what's the probability that you're in state i at the initial time, _and then_ state j at the final time? These joint probabilities, call them pij, had better add up to |αi|2 and |βj|2, if we sum the rows and columns respectively. And ideally, they should be "derived" in some way from the unitary U--so that for example, if uij=0 then pij=0 as well.

So here's something you could do: start by replacing each uij by its absolute value, to get a nonnegative matrix. Then, normalize the ith row so that it sums to |αi|2, for each i. Then normalize the jth column so that it sums to |βj|2, for each j. Then normalize the rows, then the columns, and keep iterating until hopefully you end up with all the rows _and_ columns having the right sums.

So the first question I faced was, does this process converge? And I remembered what Avi taught me about the permanent. In this case, because of the nonuniform row and column scalings, the permanent no longer works as a progress measure, but there's something else that _does_ work. Namely, as a first step, we can use the [Max-Flow/Min-Cut Theorem](https://en.wikipedia.org/wiki/Max-flow_min-cut_theorem) to show that there exists a nonnegative matrix F=(fij) such that fij=0 whenever uij=0, and also

$$ \sum_j f_{ij} = \left|\alpha_i\right|^2 \forall i,\ \ \ \ \ \sum_i f_{ij} = \left|\beta_j\right|^2 \forall j. $$

Then, letting M=(mij) be our current rescaled matrix (so that initially mij:=|uij|), we use

$$ \prod_{i,j : u_{ij}\ne 0} m_{ij}^{f_{ij}} $$

as our progress measure. By using the nonnegativity of the [Kullback-Leibler divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence), one can prove that this quantity never decreases. So then, just like with 0/1 matrices and the permanent, we get eventual convergence, and indeed convergence after a number of iterations that's polynomial in n.

I was pretty stoked about this until I went to the library, and discovered that Erwin Schrödinger had proposed the same matrix scaling process in 1931! And Masao Nagasawa and others then [rigorously analyzed it](http://www.springer.com/la/book/9783034805599). OK, but their motivations were somewhat different, and for some reason they never talked about finite-dimensional matrices, only infinite-dimensional ones.

I can't resist telling you my favorite open problem about this matrix scaling process: namely, is it stable under small perturbations? In other words, if I change one of the αi's or uij's by some small ε, then do the final pij's also change by at most some small δ? To clarify, several people have shown me how to prove that the mapping to the pij's is _continuous_. But for computer science applications, one needs something stronger: namely that when the matrix M, and the row and column scalings, actually arise from a unitary matrix in the way above, we get strong uniform continuity, with a 1/nO(1) change to the inputs producing only a 1/nO(1) change to the outputs (and hopefully even better than that).

The more general idea that I was groping toward or reinventing here is called a _hidden-variable theory_ , of which the most famous example is [Bohmian mechanics](https://en.wikipedia.org/wiki/De_Broglie%E2%80%93Bohm_theory). Again, though, Bohmian mechanics has the defect that it's only formulated for some exotic state space that the physicists care about for some reason--a space involving pointlike objects called "particles" that move around in 3 Euclidean dimensions (why 3? why not 17?).

Anyway, this whole thing led me to wonder: under the Schrödinger scaling process, or something like it, what's the computational complexity of _sampling_ an entire history of the hidden variable through a quantum computation? ("If, at the moment of your death, your whole life history flashes before you in an instant, what can you _then_ efficiently compute?")

Clearly the complexity is at least [BQP](https://en.wikipedia.org/wiki/BQP) (i.e., quantum polynomial time), because even sampling where the hidden variable is at a _single_ time is equivalent to sampling the output distribution of a quantum computer. But could the complexity be even more than BQP, because of the _correlations_ between the hidden variable values at different times? I noticed that, indeed, sampling a hidden variable history would let you do some crazy-seeming things, like solve the Graph Isomorphism problem in polynomial time (OK, fine, that seemed more impressive at the time than it does after [Babai's breakthrough](https://arxiv.org/abs/1512.03547)), or find collisions in arbitrary cryptographic hash functions, or more generally, solve any problem in the complexity class [SZK](https://complexityzoo.uwaterloo.ca/Complexity_Zoo:S#szk) (Statistical Zero Knowledge).

But you might ask: what evidence do we have that any these problems are hard even for garden-variety quantum computers? As many of you know, it's widely conjectured today that NP⊄BQP--i.e., that quantum computers can't solve NP-complete problems in polynomial time. And in the "black box" setting, where all you know how to do is query candidate solutions to your NP-complete problem to check whether they're valid, it's been _proven_ that quantum computers don't give you an exponential speedup: the best they can give is the square-root speedup of [Grover's algorithm](https://en.wikipedia.org/wiki/Grover%27s_algorithm).

But for these SZK problems, like finding collisions in hash functions, who the hell knows? So, this is the line of thought that led me to probably the most important thing I did in grad school, the so-called [quantum lower bound for collision-finding](http://www.scottaaronson.com/papers/collision.pdf). That result says that, if (again) your hash function is only accessible as a black box, then a quantum computer can provide at most a polynomial speedup over a classical computer for finding collisions in it (in this case, it turns out, at most a two-thirds power speedup). There are several reasons you might care about that, such as showing that one of the basic building blocks of modern cryptography could still be secure in a world with quantum computers, or proving an oracle separation between SZK and BQP. But my original motivation was just to understand how transition probabilities would change quantum computation.

* * *

The permanent has also shown up in a much more direct way in my work on quantum computation. If we go back to Avi's lecture from 2000, a _second_ thing he said that blew my mind was that apparently, or so he had heard, even the fundamental particles of the universe know something about the determinant and the permanent. In particular, he said, fermions--the matter particles, like the quarks and electrons in this stage--have transition amplitudes that are determinants of matrices. Meanwhile, bosons--the force-carrying particles, like the photons coming from the ceiling that let you see this talk--have transition amplitudes that are permanents of matrices.

Or as Steven Weinberg, one of the great physicists on earth, memorably put it in the first edition of his recent [quantum mechanics textbook](https://www.amazon.com/Lectures-Quantum-Mechanics-Steven-Weinberg/dp/1107028728/ref=sr_1_2?ie=UTF8&qid=1476303789&sr=8-2&keywords=weinberg+quantum+mechanics): "in the case of bosons, it is also a determinant, except without minus signs." I've had the pleasure of getting to know Weinberg at Austin, so recently I asked him about that line. He told me that _of course_ he knew that the determinant without minus signs is called a permanent, but he thought no one else would know! As far as he knew, the permanent was just some esoteric function used by a few quantum field theorists who needed to calculate boson amplitudes.

Briefly, the reason why the permanent and determinant turn up here is the following: whenever you have n particles that are identical, to calculate the amplitude for them to do something, you need to sum over all n! possible permutations of the particles. Furthermore, each contribution to the sum is a product of n complex numbers, one uij for each particle that hops from i to j. But there's a difference: when you swap two identical bosons, nothing happens, and that's why bosons give rise to the permanent (of an n×n complex matrix, if there are n bosons). By contrast, when you swap two identical fermions, the amplitude for that state of the universe gets multiplied by -1, and that's why fermions give rise to the determinant.

Anyway, Avi ended his talk with a quip about how unfair it seemed to the bosons that they should have to work so much harder than the fermions just to calculate where they should be!

And then that one joke of Avi--that way of looking at things--rattled around in my head for a decade, like a song I couldn't get rid of. It raised the question: wait a minute, bosons--particles that occur in Nature--are governed by a #P-complete function? Does that mean we could actually use bosons to solve #P-complete problems in polynomial time? That seems ridiculous, like the kind of nonsense I'm fighting every few weeks on my blog! As I said before, most of us don't even expect quantum computers to be able to solve NP-complete problems in polynomial time, let alone #P-complete ones.

As it happens, [Troyansky and Tishby](http://www.cs.huji.ac.il/labs/learning/Papers/perm.pdf) had already taken up that puzzle in 1996. (Indeed Avi, being the social butterfly and hub node of our field that he is, had learned about the role of permaments and determinants in quantum mechanics from them.) What Troyansky and Tishby said was, it's true that if you have a system of n identical, non-interacting bosons, their transition amplitudes are given by permanents of n×n matrices. OK, but amplitudes in quantum mechanics are not directly observable. They're just what you use to calculate the probability that you'll see this or that measurement outcome. But if you try to encode a hard instance of a #P-complete problem into a bosonic system, the relevant amplitudes will in general be exponentially small. And that means that, if you want a decent estimate of the permanent, you'll need to repeat the experiment an exponential number of times. So OK, they said, nice try, but this doesn't give you a computational advantage after all in calculating the permanent compared to classical brute force.

In our [2011 work on BosonSampling](http://www.scottaaronson.com/papers/optics.pdf), my student Alex Arkhipov and I reopened the question. We said, not so fast. It's true that bosons don't seem to help you in estimating the permanent of a _specific_ matrix of your choice. But what if your goal was just to sample a _random_ n×n matrix A∈Cn×n, in a way that's somehow biased toward matrices with larger permanents? Now, _why_ would that be your goal? I have no idea! But this sampling is something that a bosonic system would easily let you do.

So, what Arkhipov and I proved was that this gives rise to a class of probability distributions that can be sampled in quantum polynomial time (indeed, by a very rudimentary type of quantum computer), but that can't be sampled in classical polynomial time unless the [polynomial hierarchy](https://en.wikipedia.org/wiki/Polynomial_hierarchy) collapses to the third level. And even though you're not solving a #P-complete problem, the #P-completeness of the permanent still plays a crucial role in explaining why the sampling problem is hard. (Basically, one proves that the probabilities are #P-hard even to approximate, but that _if_ there were a fast classical sampling algorithm, then the probabilities could be approximated in the class BPPNP. So if a fast classical sampling algorithm existed, then P#P would equal BPPNP, which would collapse the polynomial hierarchy by [Toda's Theorem](https://en.wikipedia.org/wiki/Toda%27s_theorem).)

When we started on this, Arkhipov and I thought about it as just pure complexity theory--conceptually clarifying what role the #P-completeness of the permanent plays in physics. But then at some point it occurred to us: bosons (such as photons) _actually exist_ , and experimentalists in quantum optics like to play with them, so maybe they could demonstrate some of this stuff in the lab. And as it turned out, the quantum optics people were looking for something to do at the time, and they ate it up.

Over the past five years, a trend has arisen in experimental physics that goes by the name "Quantum Supremacy," although some people are now backing away from the name because of Trump. The idea is: without yet having a universal quantum computer, can we use the hardware that we're able to build today to demonstrate the reality of a quantum-computational speedup as clearly as possible? Not necessarily for a useful problem, but just for _some_ problem? Of course, no experiment can prove that something is scaling polynomially rather than exponentially, since that's an asymptotic statement. But an experiment could certainly raise the stakes for the people who deny such a statement--for example, by solving something a trillion times faster than we know how to solve it otherwise, using methods for which we don't know a reason for them _not_ to scale.

I like to say that for me, the #1 application of quantum computing, more than breaking RSA or even simulating physics and chemistry, is simply disproving the people who say that quantum computing is impossible! So, quantum supremacy targets _that_ application.

Experimental BosonSampling has become a major part of the race to demonstrate quantum supremacy. By now, at least a half-dozen groups around the world have reported small-scale implementations--the [record](https://scottaaronson.blog/?p=2435), so far, being an experiment at Bristol that used 6 photons, and experimentally confirmed that, yes, their transition amplitudes are given by permanents of 6×6 complex matrices. The challenge now is to build single-photon sources that are good enough that you could scale up to (let's say) 30 photons, which is where you'd really start seeing a quantum advantage over the best known classical algorithms. And again, this whole quest really started with Avi's joke.

A year after my and Arkhipov's work, I noticed that one also can run the connection between quantum optics and the permanent [in the "reverse" direction](http://www.scottaaronson.com/papers/sharp.pdf). In other words: with BosonSampling, we used the famous theorem of Valiant, that the permanent is #P-complete, to help us argue that bosons can solve hard sampling problems. But if we know by some other means that quantum optics lets us encode #P-complete problems, then we can use that to give an independent, "quantum" proof that the permanent is #P-complete in the first place! As it happens, there _is_ another way to see why quantum optics lets us encode #P-complete problems. Namely, we can use celebrated work by [Knill, Laflamme, and Milburn](https://arxiv.org/abs/quant-ph/0006088) (KLM) from 2001, which showed how to perform universal quantum computation using quantum optics with the one additional resource of "feed-forward measurements." With minor modifications, the construction by KLM also lets us encode a #P-complete problem into a bosonic amplitude, which we know is a permanent--thereby proving that the permanent is #P-complete, in what I personally regard as a much more intuitive way than Valiant's original approach based on cycle covers. This illustrates a theme that we've seen over and over in the last 13 years or so, which is the use of quantum methods and arguments to gain insight even about classical computation.

Admittedly, I wasn't proving anything here in classical complexity theory that wasn't already known, just giving a different proof for an old result! Extremely recently, however, my students Daniel Grier and Luke Schaeffer have extended my argument based on quantum optics, to show that computing the permanent of a unitary or orthogonal matrix is #P-complete. (Indeed, even over finite fields of characteristic k, computing the permanent of an orthogonal matrix is a [ModkP](https://complexityzoo.uwaterloo.ca/Complexity_Zoo:M#modkp)-complete problem, as long as k is not 2 or 3--which turns out to be the tight answer.) This is not a result that we previously knew by _any_ means, whether quantum or classical.

I can't resist telling you the biggest theoretical open problem that arose from my and Arkhipov's work. We would like to say: even if you had a polynomial-time algorithm that sampled a probability distribution that was merely _close_ , in variation distance, to the BosonSampling distribution, that would already imply a collapse of the polynomial hierarchy. But we're only able to prove that assuming a certain problem is #P-complete, which no one has been able to prove #P-complete. That problem is the following:

> Given an n×n matrix A, each of whose entries is an i.i.d. complex Gaussian with mean 0 and variance 1 (that is, drawn from N(0,1)C), estimate |Per(A)|2, to within additive error ±ε·n!, with probability at least 1-δ over the choice of A. Do this in time polynomial in n, 1/ε, and 1/δ.

Note that, if you care about exactly computing the permanent of a Gaussian random matrix, _or_ about approximating the permanent of an arbitrary matrix, we know how to prove both of those problems #P-complete. The difficulty "only" arises when we combine approximation and average-case in the same problem.

At the moment, we don't even know something more basic, which is: what's the _distribution_ over |Per(A)|2, when A is an n×n matrix of i.i.d. N(0,1)C Gaussians? Based on numerical evidence, we conjecture that the distribution converges to lognormal as n gets large. By using the interpretation of the determinant as the volume of a parallelipiped, we can [prove](https://arxiv.org/abs/1309.7460) that the distribution over |Det(A)|2 converges to lognormal. And the distribution over |Per(A)|2 looks almost the same when you plot it. But not surprisingly, the permanent is harder to analyze.

* * *

This brings me to my final vignette. Why would anyone even suspect that approximating the permanent of a Gaussian _random_ matrix would be a #P-hard problem? Well, because if you look at the permanent of an n×n matrix over a large enough _finite_ field, say Fp, that function famously has the property of [_random self-reducibility_](https://en.wikipedia.org/wiki/Random_self-reducibility). This means: the ability to calculate such a permanent in polynomial time, on 90% all matrices in Fpn×n, or even for that matter on only 1% of them, implies the ability to calculate it in polynomial time on _every_ such matrix.

The reason for this is simply that the permanent is a low-degree polynomial, and low-degree polynomials have extremely useful error-correcting properties. In particular, if you can compute such a polynomial on any large fraction of points, then you can do noisy polynomial interpolation (e.g., the [Berlekamp-Welch algorithm](https://en.wikipedia.org/wiki/Berlekamp%E2%80%93Welch_algorithm), or [list decoding](https://en.wikipedia.org/wiki/List_decoding)), in order to get the value of the polynomial on an _arbitrary_ point.

I don't specifically remember Avi talking about the random self-reducibility of the permanent in his 2000 lecture, but he obviously _would have_ talked about it! And it was really knowing about the random self-reducibility of the permanent, and how powerful it was, that led me and Alex Arkhipov to the study of BosonSampling in the first place.

In complexity theory, the random self-reducibility of the permanent is hugely important because it was sort of the spark for some of our most convincing examples of _non-relativizing_ results--that is, results that fail relative to a suitable oracle. The most famous such result is that #P, and for that matter even [PSPACE](https://en.wikipedia.org/wiki/PSPACE), admit interactive protocols (the [IP=PSPACE theorem](https://en.wikipedia.org/wiki/IP_\(complexity\))). In the 1970s, Baker, Gill, and Solovay pointed out that non-relativizing methods would be needed to resolve P vs. NP and many of the other great problems of the field.

In 2007, Avi and I wrote [our only joint paper so far](http://www.scottaaronson.com/papers/alg.pdf). In that paper, we decided to take a closer look at the non-relativizing results based on interactive proofs. We said: while it's true that these results don't relativize--that is, there are oracles relative to which they fail--nevertheless, these results hold relative to all oracles that themselves encode low-degree polynomials over finite fields (such as the permanent). So, introducing a term, Avi and I said that results like IP=PSPACE _algebrize_.

But then we also showed that, if you want to prove P≠NP--or for that matter, even prove circuit lower bounds that go "slightly" beyond what's already known (such as [NEXP](https://en.wikipedia.org/wiki/NEXPTIME)⊄[P/poly](https://en.wikipedia.org/wiki/P/poly))--you'll need techniques that are not only non-relativizing, but _also_ non-algebrizing. So in some sense, the properties of the permanent that are used (for example) in proving that it has an interactive protocol, just "aren't prying the black box open wide enough."

I have a more recent result, from 2011 or so, that I never got around to finishing a paper about. In this newer work, I decided to take another look at the question: what is it about the permanent that _actually_ fails to relativize? And I prove the following result: relative to an _arbitrary_ oracle A, the class #P has complete problems that are both random self-reducible and downward self-reducible (that is, reducible to smaller instances of the same problem). So, contrary to what certainly I and maybe others had often thought, it's _not_ the random self-reducibility of the permanent that's the crucial thing about it. What's important, instead, is a further property that the permanent has, of being _self-checkable_ and _self-correctible_.

In other words: given (say) a noisy circuit for the permanent, it's not just that you can correct that circuit to compute whichever low-degree polynomial it was close to computing. Rather, it's that you can confirm that the polynomial is in fact the permanent, and nothing else.

I like the way Ketan Mulmuley thinks about this phenomenon in his [Geometric Complexity Theory](http://gct.cs.uchicago.edu/), which is a speculative, audacious program to try to _prove_ that the permanent is harder than the determinant, and to tackle the other great separation questions of complexity theory (including P vs. NP), by using algebraic geometry and representation theory. Mulmuley says: the permanent is a polynomial in the entries of an n×n matrix that not only satisfies certain symmetries (e.g., under interchanging rows or columns), but is _uniquely characterized_ by those symmetries. In other words, if you find a polynomial that passes certain tests--for example, if it behaves in the right way under rescaling and interchanging rows and columns--then that polynomial _must_ be the permanent, or a scalar multiple of the permanent. Similarly, if you find a polynomial that passes the usual interactive proof for the permanent, that polynomial must be the permanent. I think this goes a long way toward explaining why the permanent is so special: it's not just any hard-to-compute, low-degree polynomial; it's one that you can recognize when you come across it.

* * *

I've now told you about the eventual impact of one single survey talk that Avi gave 16 years ago--not even a particularly major or important one. So you can only imagine what Avi's impact must have been on all of us, if you integrate over all the talks he's given and papers he's written and young people he's mentored and connections he's made his entire career. May that impact be permanent.
