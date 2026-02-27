---
title: "The arc of complexity is long, but it bends toward lower bounds"
author: "Scott Aaronson"
date: "Fri, 23 Jan 2009"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=381"
---

As MIT grad student Jelani Nelson rightly pointed out to me, an historic world event took place on Tuesday, January 20--an event that many of us have awaited for decades, one that we thought we'd never live to see--and I inexcusably failed my readers by neglecting to blog about it. The event in question, as everyone knows, was [Mark Braverman](http://www.cs.toronto.edu/~mbraverm/) posting to his web page what looks to be a [proof](http://www.cs.toronto.edu/~mbraverm/FoolAC0v5.pdf) of the Linial-Nisan Conjecture. The LN conjecture, posed in 1990, held that

**Polylog-wise independence fools[AC0](http://qwiki.stanford.edu/wiki/Complexity_Zoo:A#ac0)**.

Alright, let me try again in English. The conjecture says that no logic circuit, composed of a polynomial number of AND, OR, and NOT gates (of unbounded [fan-in](http://en.wikipedia.org/wiki/Fan-in)) arranged in a constant number of layers, can distinguish n input bits x1,…,xn that are _truly_ random, from n input bits that _look_ random on every subset of (say) n0.001 bits, but that could be correlated in arbitrary ways across larger scales. In other words, if such a circuit accepts truly random bits with probability close to 1, then it also accepts the pseudorandom bits with probability close to 1, and vice versa. If you want to _distinguish_ the random bits from the pseudorandom bits with noticeable bias, then you need a more powerful kind of circuit: either greater depth (say, log(n) layers instead of O(1)), or more gates (say, exponentially many), or more powerful gates (say, XOR or MAJORITY gates instead of just AND, OR, and NOT). To a constant-depth, polynomial-size, AND/OR/NOT circuit (which we call an AC0 circuit for short--don't ask why), _local randomness looks just the same as global randomness._ Or so says the Linial-Nisan Conjecture.

Now, we've known since the eighties that AC0 circuits have serious limitations. In particular, we've known lots of _specific_ pseudorandom distributions that fool them. What Linial and Nisan conjectured, and Braverman appears to have proved, is that _any_ distribution will do the job, just so long as it "looks random locally."

A year and a half ago, Bazzi proved the Linial-Nisan conjecture in the special case of depth-two circuits, in a [64-page tour de force](http://stuff.mit.edu/people/louay/recent/kwisednf2.pdf). Then Razborov gave an essentially [2-page proof](http://eccc.hpi-web.de/eccc-reports/2008/TR08-081/index.html) of the same result. (Need I explain how awesome that is?) Braverman extends Bazzi's result to circuits of _any_ constant depth; his proof is almost as short as Razborov's.

In proving these lower bounds, the name of the game is the polynomial method (the subject of my [FOCS tutorial](http://www.scottaaronson.com/talks/polymeth.ppt)). Given an AC0 circuit C, you first construct a low-degree real polynomial that approximates C pretty well on _most_ inputs. (How do you construct such a thing? And what does "pretty well" mean? Save it for the comments section.) Then you observe that no low-degree polynomial could possibly distinguish a random string from a string that only _looks_ random locally. Why? Because a low-degree polynomial, by definition, is a sum of local terms, and if none of those individual terms can distinguish truly random bits from pseudorandom ones (as was assumed), then their sum can't distinguish them either, by the deep principle of the universe we call [linearity of expectation](http://en.wikipedia.org/wiki/Expected_value#Linearity). (By contrast, an AND or OR of terms could in principle detect "global" properties of the input that none of the individual terms detected--which is why we couldn't just apply such an argument to the AC0 circuit directly.) It follows, then, that the original circuit couldn't have distinguished local randomness from global randomness very well either, which is what we wanted to show.

So everything boils down to constructing these low-degree approximating polynomials and proving they have the right properties. And in that context, what Braverman does is almost hilariously simple. Given an AC0 circuit C, he first constructs a low-degree polynomial p that agrees with C on _most_ inputs (from whatever fixed probability distribution you want), using the celebrated method of [Valiant-Vazirani](http://en.wikipedia.org/wiki/Valiant-Vazirani_theorem) and [Razborov-Smolensky](http://people.csail.mit.edu/madhu/ST05/scribe/lect06.pdf). He then observes that, when p _fails_ to agree with C, there's another AC0 circuit E, of depth slightly greater than C, that _detects_ the failure. Next he finds a low-degree polynomial q that approximates E in L2-norm, using the also-celebrated 1993 theorem of [Linial-Mansour-Nisan](http://csdl.computer.org/comp/proceedings/sfcs/1989/1982/00/063537.pdf). Then he looks at p(1-q), and shows that it's a polynomial that usually agrees with C, but when it _does_ disagree, usually isn't _too_ far off. And then … well, at that point he's really almost done.

While I had no involvement whatsoever with this beautiful result, I'm pleased to have unwittingly set in motion a chain of events that led to it. Since the summer, I've been trying to get as many lowerbounderati as possible interested in [BQP versus PH](http://www.scottaaronson.com/talks/openqc.ppt), a central open problem of quantum complexity theory that's resisted progress since the prehistoric days of 1993. (There are certain problems that I mentally classify as "rabbits," after the [Killer Rabbit of Caerbannog](http://en.wikipedia.org/wiki/Rabbit_of_Caerbannog) from _Monty Python and the Holy Grail_. BQP vs. PH is one of the fluffiest, most adorable rabbits ever to leap for my throat.)

Concretely, the goal has been to construct an [oracle](http://en.wikipedia.org/wiki/Oracle_machine) relative to which [BQP](http://qwiki.stanford.edu/wiki/Complexity_Zoo:B#bqp) (Bounded-Error Quantum Polynomial-time, the class of problems that are feasible for a quantum computer) is not contained in [PH](http://qwiki.stanford.edu/wiki/Complexity_Zoo:P#ph) (the Polynomial-time Hierarchy, a generalization of [NP](http://qwiki.stanford.edu/wiki/Complexity_Zoo:N#np)). Such a separation would give us probably our best evidence to date that BQP is not contained in NP--or loosely speaking, that not only can quantum computers solve certain problems exponentially faster than classical ones, _they can solve certain problems exponentially faster than classical computers can even verify the answers._

(NerdNote: We _do_ have oracles relative to which BQP⊄NP, and indeed BQP⊄[MA](http://qwiki.stanford.edu/wiki/Complexity_Zoo:M#ma). But we still don't have an oracle relative to which BQP⊄[AM](http://qwiki.stanford.edu/wiki/Complexity_Zoo:A#am). And that sticks in the craw, since we know that AM=NP under a derandomization hypothesis.)

Now, it occurred to me that BQP versus PH is closely related to the Linial-Nisan Conjecture. That's not _quite_ as surprising as it sounds, since you can think of PH as the "exponentially scaled-up version" of AC0 … so that fighting PH ultimately boils down to fighting AC0.

Alright, so consider the following problem, which we'll call Fourier Checking. You're given black-box access to two Boolean functions f,g:{-1,1}n→{-1,1}, and are promised that either

  1. f and g were both generated uniformly at random (independently of each other), or
  2. f and g were generated by first choosing a random 2n-dimensional unit vector v, then setting f(x)=sgn(vx) and g(x)=sgn((Hv)x), where H represents the Fourier transform over Z2n.



The problem is to decide which, with small probability of error.

It's not hard to see that Fourier Checking is in BQP (i.e., is efficiently solvable by a quantum computer). For to solve it, you just go into a uniform superposition over all x∈{-1,1}n, then query f, apply a Quantum Fourier Transform, query g, and see if you're left with (1) random garbage or (2) something close to the uniform superposition that you started with.

On the other hand, one can show that:

  * A certain generalization of Bazzi's Theorem (from "local randomness" to "local almost-randomness"--as usual, ask in the comments section) would imply that Fourier Checking is _not_ in an important subclass of PH called AM (for "Arthur-Merlin"). And thus, we'd get an oracle relative to which BQP⊄AM.
  * The analogous generalization of the _full_ Linial-Nisan Conjecture would imply that Fourier Checking is not in PH. And thus, we'd get our long-sought oracle relative to which BQP⊄PH.



After realizing the above, I tried for months to prove the requisite generalization of Bazzi's Theorem--or better yet, get someone else to prove it for me. But I failed. All I managed to do was to goad Razborov into proving his amazing 2-page version of Bazzi's original theorem, which in turn inspired Braverman to shoot for the full Linial-Nisan Conjecture.

In what appears to be a cosmic prank, about the only conjectures in this area that still _haven 't_ been proved are the ones I needed for the quantum computing problem. And thus, I will offer $100 for a proof that Fourier Checking is not in AM, $200 for a proof that it's not in PH. In so doing, my hope is to make Tuesday, January 20, 2009 remembered by all as the day our economy finally got back on track.
