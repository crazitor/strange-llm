---
title: "I was wrong about Joy Christian"
author: "Scott Aaronson"
date: "Thu, 10 May 2012"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=1028"
---

**Update:** I decided to close comments on this post and the previous Joy Christian post, because they simply became too depressing for me.

I've further decided to impose a moratorium, on this blog, on all discussions about the validity of quantum mechanics in the microscopic realm, the reality of quantum entanglement, or the correctness of theorems such as Bell's Theorem. I might lift the moratorium at some future time. For now, though, life simply feels too short to me, and the _actually-interesting questions_ too numerous. Imagine, for example, that there existed a devoted band of crackpots who believed, for complicated, impossible-to-pin-down reasons of topology and geometric algebra, that _triangles actually have five corners_. These crackpots couldn't be persuaded by rational argument--indeed, they didn't even use words and sentences the same way you do, to convey definite meaning. And crucially, they had _infinite energy_ : you could argue with them for weeks, and they would happily argue back, until you finally threw up your hands in despair for all humanity, at which point the crackpots would gleefully declare, "haha, we won! the silly 'triangles have 3 corners' establishment cabal has admitted defeat!" And, in a sense, they _would have_ won: with one or two exceptions, the vast majority who know full well how many corners a triangle has simply never showed up to the debate, thereby conceding to the 5-cornerists by default.

What would you in such a situation? What would you do? If you figure it out, please let me know (but by email, not by blog comment).

* * *

In response to my [post](https://scottaaronson.blog/?p=993) criticizing his "disproof" of Bell's Theorem, Joy Christian [taunted](https://scottaaronson.blog/?p=993#comment-43446) me that "all I knew was words." By this, he meant that my criticisms were entirely based on circumstantial evidence, for example that (1) Joy clearly didn't understand what the word "theorem" even meant, (2) every other sentence he uttered contained howling misconceptions, (3) his papers were written in an obscure, "crackpot" way, and (4) several people had written very clear papers pointing out mathematical errors in his work, to which Joy had responded only with bluster. But I hadn't _actually_ studied Joy's "work" at a technical level. Well, yesterday I finally did, and I confess that I was astonished by what I found. Before, I'd actually given Joy some tiny benefit of the doubt--possibly misled by the length and semi-respectful tone of the papers refuting his claims. I had assumed that Joy's errors, though _ultimately_ trivial (how could they not be, when he's claiming to contradict such a well-understood fact provable with a few lines of arithmetic?), would nevertheless be artfully concealed, and would require some expertise in geometric algebra to spot. I'd also assumed that _of course_ Joy would have some well-defined hidden-variable model that reproduced the quantum-mechanical predictions for the Bell/CHSH experiment (how could he not?), and that the "only" problem would be that, due to cleverly-hidden mistakes, his model would be subtly nonlocal.

What I actually found was a thousand times worse: closer to the stuff freshmen scrawl on an exam when they have no clue what they're talking about but are hoping for a few pity points. It's _so_ bad __that I don 't understand how even Joy's fellow crackpots haven't laughed this off the stage. Look, Joy has a hidden variable λ, which is either 1 or -1 uniformly at random. He also has a measurement choice a of Alice, and a measurement choice b of Bob. He then defines Alice and Bob's __measurement outcomes A and B via the following functions:

A(a,λ) = something complicated = (as Joy correctly observes) λ

B(b,λ) = something complicated = (as Joy correctly observes) -λ

I shit you not. A(a,λ) = λ, and B(b,λ) = -λ. Neither A nor B has any dependence on the choices of measurement a and b, and the complicated definitions that he gives for them turn out to be completely superfluous. No matter what measurements are made, A and B are always perfectly anticorrelated with each other.

You might wonder: what could lead anyone--no matter how deluded--even to _think_ such a thing could violate the Bell/CHSH inequalities? Aha, Joy says you only ask such a naïve question because, lacking his deep topological insight, you make the rookie mistake of looking at the actual outcomes that his model actually predicts for the actual measurements that are actually made. What you _should_ do, instead, is compute a "correlation function" E(a,b) that's defined by dividing A(a,λ)B(b,λ) by a "normalizing factor" that's a product of the quaternions a and b, with a divided on the left and b divided on the right. Joy seems to have obtained this "normalizing factor" via the technique of pulling it out of his rear end. Now, as [Gill shows](http://arxiv.org/abs/1203.1504), Joy actually makes an algebra mistake while computing his nonsensical "correlation function." The answer should be -a.b-a×b, not -a.b. But that's truthfully beside the point. It's as if someone announced his revolutionary discovery that P=NP implies N=1, and then critics soberly replied that, no, the equation P=NP can also be solved by P=0.

So, after 400+ comments on my previous thread--including heady speculations about M-theory, the topology of spacetime, the Copenhagen interpretation, continuity versus discreteness, etc., as well numerous comparisons to Einstein--_this_ is what it boils down to. A(a,λ) = λ and B(b,λ) = -λ.

I call on FQXi, in the strongest possible terms, to stop lending its legitimacy to this now completely-unmasked charlatan. If it fails to do so, then **I will resign from FQXi, and will encourage fellow FQXi members to do the same.**

While I don't know the exact nature of Joy's relationship to Oxford University or to the Perimeter Institute, I also call on those institutions to sever any connections they still have with him.

Finally, with this post I'm going to try a new experiment. I will allow comments through the moderation filter if, and only if, they exceed a minimum threshold of sanity and comprehensibility, and do not randomly throw around terms like "M-theory" with no apparent understanding of what they mean. Comments below the sanity threshold can continue to appear freely in the [previous Joy Christian thread](https://scottaaronson.blog/?p=993#comments) (which already has a record-setting number of comments…).

**Update (May 11):** A commenter pointed me to a [beautiful preprint](http://philosophyfaculty.ucsd.edu/faculty/wuthrich/PhilPhys/WeatherallJames2011Man_ScopeBellThm.pdf) by James Owen Weatherall, which tries sympathetically to make as much sense as possible out of Joy Christian's ideas, and then carefully explains why the attempt fails (long story short: because of Bell's theorem!). Notice the contrast between the precision and clarity of Weatherall's prose--the way he defines and justifies each concept before using it--and the obscurity of Christian's prose.

**Another Update:** Over on the previous Joy Christian thread, [some commenters](https://scottaaronson.blog/?p=993#comment-44665) are now using an extremely amusing term for people who believe that theories in physics ought to say something comprehensible about the predicted outcomes of physics experiments. The term: "computer nerd."

**Third Update:** Quite a few commenters seem to assume that I inappropriately used my blog to "pick a fight" with poor defenseless Joy Christian, who was minding his own business disproving and re-disproving Bell's Theorem. So let me reiterate that I wasn't looking for this confrontation, and in fact _took great pains to avoid it for six years_ , even as Joy became more and more vocal. It was Joy, not me, who finally forced matters to a head through his [absurd demand](https://scottaaronson.blog/?p=902#comment-43327) that I pay him $100,000 "with interest," and then his subsequent attacks.
