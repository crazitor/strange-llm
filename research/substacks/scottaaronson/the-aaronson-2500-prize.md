---
title: "The Aaronson $25.00 Prize"
author: "Scott Aaronson"
date: "Sun, 28 Oct 2007"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=284"
---

[Update]

For those of you who've been living in a non-wifi-enabled cave, four days ago Stephen Wolfram [awarded a $25,000 prize](http://blog.wolfram.com/2007/10/the_prize_is_won_the_simplest.html) to a 20-year-old undergraduate named Alex Smith, for proving that a particular two-state, three-symbol Turing machine is universal. The prize was to celebrate the fifth anniversary of Wolfram's paradigm-smashing, foundation-shaking masterpiece, [_A New Kind of Science_](http://en.wikipedia.org/wiki/A_new_kind_of_science). (More from [Bill Gasarch's blog](http://weblog.fortnow.com/2007/10/wolfram-prize-won-there-is-23-utm.html), _[Nature](http://www.nature.com/news/2007/071024/full/news.2007.190.html)_ , and _[Scientific American](http://www.sciam.com/article.cfm?articleID=D8F2082D-E7F2-99DF-36D4F98C7C2A7674&pageNumber=1&catID=1)_.)

Smith sounds like a swell guy who entered this contest for exactly the right reasons: he was at his parents' place over summer break and had nothing better to do. He deserves the money, and I sincerely hope the CS theory community hasn't heard the last from him.

Predictably, though, as soon as this story broke I started getting emails from journalists asking me about the far-reaching scientific implications of the new universality proof. In trying to give them an honest answer -- one that wouldn't be misunderstood, or spun to support a pre-existing storyline with which I disagreed -- I inevitably came off like an ornery old sourpuss. From _Scientific American_ :

> Of course, there may be a reason the problem languished. "Finding the smallest universal [Turing machines] is a neat recreational pursuit," quantum computation researcher Scott Aaronson of the Massachusetts Institute of Technology says, but "it's no longer seen as connected to the central questions of the field." …
> 
> "The impact of NKS on all the areas of computer science and physics I'm familiar with has been basically zero," he says. "As far as I can tell, the main impact is that people now sometimes use the adjective 'Wolframian' to describe breathtaking claims for the trivial or well-known." [Martin] Davis offers a sunnier take: "The book has a lot of beautiful pictures."

And from _Nature_ :

> The solution isn't hugely relevant to modern computer science, says Scott Aaronson, a computer scientist at the Massachusetts Institute of Technology (MIT) in Cambridge, Massachusetts. "Most theoretical computer scientists don't particularly care about finding the smallest universal Turing machines," he wrote in an e-mail. "They see it as a recreational pursuit that interested people in the 60s and 70s but is now sort of 'retro'."

Having partially degrumpified, in the remainder of this post I wish to offer something positive.

But first some background: a month after NKS came out, I wrote a [review](http://www.arxiv.org/abs/quant-ph/0206089) of it for the journal _Quantum Information and Computation_ , in which I examined Wolfram's claims about quantum mechanics and computational complexity, and explained what I saw as the problems with them. (Rather than rehash the review, I'll just point you there if you're interested.)

Today I'd like to celebrate the fifth anniversary of my critical review of NKS, by offering a $25 prize for stodgy, conventional work in the field of quantum complexity theory.

**The Aaronson $25.00 Challenge**

In NKS, Wolfram places himself among those computer scientists and physicists who doubt the possibility of quantum computers, not for any practical reason but as a consequence of their disbelieving quantum mechanics itself. As he writes on page 771:

> Indeed within the usual formalism [of quantum mechanics] one can construct quantum computers that may be able to solve at least a few specific problems exponentially faster than ordinary Turing machines. But particularly after my discoveries in Chapter 9 ['Fundamental Physics'], I strongly suspect that even if this is formally the case, it will still not turn out to be a true representation of ultimate physical reality, but will instead just be found to reflect various idealizations made in the models used so far.

Here, then, is the challenge:

**If a quantum computer can efficiently solve a problem, can it also efficiently convince Wolfram that the solution is correct? More formally, does every language in the class[BQP](http://qwiki.caltech.edu/wiki/Complexity_Zoo#bqp) admit an interactive protocol where the prover is in BQP and the verifier is in [BPP](http://qwiki.caltech.edu/wiki/Complexity_Zoo#bpp)?**

In other words: _can quantum computers always "show their work"?_ It's obvious, for example, that if a quantum computer spit out the factors of a 5,000-digit number, you wouldn't have to believe quantum mechanics (or even know what it was) to check whether the answer was right. I'm asking whether _every_ problem solvable by a quantum computer has the same property. And to make things fair to the quantum computer, I'll let it give not just a static proof but also an [interactive protocol](http://en.wikipedia.org/wiki/Interactive_proof_system), by which a distrustful polynomial-time classical verifier could become convinced, to arbitrarily high confidence, that the quantum computer knows the right answer.

(An example for the uninitiated: suppose you had two graphs G and H, and suppose you picked one of the graphs at random, randomly permuted its vertices, and gave the result to a quantum computer. And suppose the quantum computer could unfailingly tell you which graph you started with. Clearly this should convince you that G and H are not isomorphic -- since if they _were_ isomorphic, then the quantum computer couldn't have done better than guessing! And this is true even though you never received a _proof_ of non-isomorphism that you could hand to someone else.)

I'll award $25 either for a proof that every quantum computation can be "counter-Wolframized," _or_ for an oracle relative to which some quantum computation provably can't be. If both problems are solved then I'll award $25 for each. Every serious submission will be reviewed by a Prize Committee consisting of me. The Committee may also choose to award smaller prizes for partial results.

**Note:** Much as I'd like to "pull a Wolfram," the beautiful question above was (to my knowledge) first asked by Daniel Gottesman, at a conference in February 2004. Also, the idea of a $25 prize was suggested to me by Mike Mosca.

**Update (10/30):** A commenter pointed me to [this thread ](http://cs.nyu.edu/pipermail/fom/2007-October/012120.html) in the Foundations of Mathematics (FOM) mailing list, which contains an actual technical discussion of Smith's universality proof. Of particular interest:

  1. an [argument](http://cs.nyu.edu/pipermail/fom/2007-October/012156.html) by Vaughan Pratt that Smith's universality proof is wrong,
  2. a [response](http://forum.wolframscience.com/showthread.php?s=c34045c0feab14e8092c93f9d4f0268b&threadid=1472) by Todd Rowland of Wolfram Research,
  3. a [post from Wolfram himself](http://cs.nyu.edu/pipermail/fom/2007-October/012149.html), which, though written in his trademark way, comes the closest I’ve seen of anything by him to addressing actual hard questions about the definition of universality, and
  4. [this comment](http://cs.nyu.edu/pipermail/fom/2007-October/012141.html) from John McCarthy: "In the 1950s I thought that the smallest possible (symbol-state product) universal Turing machine would tell something about the nature of computation. Unfortunately, it didn't. Instead as simpler universal machines were discovered, the proofs that they were universal became more elaborate, and [so] did the encodings of information."



In judging the correctness of Smith's proof, the key question is what counts as "universality." As I explained to the journalists who emailed me, the rules of Wolfram’s prize left a huge gray area by explicitly refusing to specify this. In particular: what kinds of input and output encodings are allowed? How do we make sure the real computational work is done by the Turing machine itself and not the encoding procedures? Does the tape have to be filled with 0’s initially, or can it be filled with other patterns, and if so which ones? Since the two-state Turing machine in question has no “halt” state, what external conditions can we impose to determine when the machine has halted?

Still, I decided not to make a fuss about such things in my original post, since it seemed clear from Smith’s writeup that (1) he was aware of these issues, and (2) there was _some_ nontrivial sense in which he proved universality. I wasn’t going to lose sleep over _which_ sense, for the simple reason that I’d never lost sleep over the (2,3) universality question itself!
