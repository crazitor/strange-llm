---
title: "A far-off dream: automating a problem in P"
author: "Scott Aaronson"
date: "Fri, 25 Aug 2006"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=116"
---

In a comment on my [last post](https://scottaaronson.blog/?p=115), Bram Cohen writes:

> This whole business of 'formality' and 'review' is really kind of dumb. A mathematical theorem is only really proven when a computer can verify the proof. Until then, it's just hand-waving which has some degree of utility when generating a real proof.
> 
> Were it standard to present proofs in computer-checkable form, there would be no review process at all. In fact it would be possible to send a proof to a theorem server which would automatically accept any proof which checked out. Had Perelman submitted to one of those, we wouldn't have had any review process at all, and had complete confidence from day 1, and there wouldn't be any of this stupid game of who really proved it by making the arguments sufficiently 'formal' or 'detailed'.
> 
> I view the switch to doing mathematics in the style just described as inevitable…

Like Bram, I also hope and expect that mathematicians will eventually switch to machine-readable proofs supplemented by human-readable explanations. That would certainly beat the current standard, proofs that are readable by neither machines nor humans.

So then why hasn't it happened already? Probably the best way to answer this question is to show you the proof, in a state-of-the-art formal verification system called [HOL Light](http://www.cl.cam.ac.uk/%7Ejrh13/hol-light/), that the square root of 2 is irrational.

> 
>     let rational = new_definition
>     `rational(r) = ?p q. ~(q = 0) / abs(r) = &p; / &q;`;;
>     
>     let NSQRT_2 = prove
>     (`!p q. p * p = 2 * q * q ==> q = 0`,
>     MATCH_MP_TAC num_WF THEN REWRITE_TAC[RIGHT_IMP_FORALL_THM] THEN
>     REPEAT STRIP_TAC THEN FIRST_ASSUM(MP_TAC o AP_TERM `EVEN`) THEN
>     REWRITE_TAC[EVEN_MULT; ARITH] THEN REWRITE_TAC[EVEN_EXISTS] THEN
>     DISCH_THEN(X_CHOOSE_THEN `m:num` SUBST_ALL_TAC) THEN
>     FIRST_X_ASSUM(MP_TAC o SPECL [`q:num`; `m:num`]) THEN
>     POP_ASSUM MP_TAC THEN CONV_TAC SOS_RULE);;
>     
>     let SQRT_2_IRRATIONAL = prove
>     (`~rational(sqrt(&2))`,
>     SIMP_TAC[rational; real_abs; SQRT_POS_LE; REAL_POS; NOT_EXISTS_THM] THEN
>     REPEAT GEN_TAC THEN DISCH_THEN(CONJUNCTS_THEN2 ASSUME_TAC MP_TAC) THEN
>     DISCH_THEN(MP_TAC o AP_TERM `x. x pow 2`) THEN
>     ASM_SIMP_TAC[SQRT_POW_2; REAL_POS; REAL_POW_DIV; REAL_POW_2; REAL_LT_SQUARE;
>     REAL_OF_NUM_EQ; REAL_EQ_RDIV_EQ] THEN
>     ASM_MESON_TAC[NSQRT_2; REAL_OF_NUM_EQ; REAL_OF_NUM_MUL]);;

Cool -- now let's do Fermat and Poincaré! Any volunteers?

Seriously, the biggest accomplishments to date have included formal proofs of the Jordan Curve Theorem (75,000 lines) and the Prime Number Theorem (30,000 lines). If you want to know which other famous theorems have been formalized, check out [this](http://www.cs.ru.nl/%7Efreek/100/) excellent page. Or look at [these](http://www.math.ohio-state.edu/%7Efriedman/pdf/CStalk060806.pdf#search=%22100%20theorems%20harvey%20friedman%22) notes by Harvey Friedman, which cut through the crap and tell us exactly where things stand.

A huge part of the problem in this field seems to be that there's neither a standard proof format nor a standard proof repository -- no TeX or HTML, no arXiv or Wikipedia. Besides HOL Light, there's also [ProofPower](http://www.lemma-one.com/ProofPower/index/), [Isabelle](http://www.cl.cam.ac.uk/Research/HVG/Isabelle/), [Coq](http://coq.inria.fr/), [Mizar](http://mizar.uwb.edu.pl/project/), and several other competitors. I'd probably go with Mizar, simply because the proofs in it look the most to me like actual math.

Friedman gives machine-readable proofs fifty years to catch on among "real" mathematicians. That seems about right -- though the time could be reduced if the Don Knuth, Tim Berners-Lee, Paul Ginsparg, or Jimmy Wales of proof-checking were to appear between now and then. As usual, it mostly comes down to humans.

Update: Freek Wiedijk put together a [fantastic online book](http://www.cs.ru.nl/%7Efreek/comparison/comparison.pdf), which shows the proofs that the square root of 2 is irrational in 17 different formal systems. The ["QED Manifesto"](http://www.rbjones.com/rbjpub/logic/qedres00.htm) is also worth a look. This manifesto makes it clear that there are people in the formal verification world with a broad enough vision -- if you like, the [Ted Nelsons](http://en.wikipedia.org/wiki/Ted_Nelson) of proof-checking. Nelson is the guy who dreamed in 1960 of creating a global hypertext network. In his case, it took 35 years for the dream to turn into software and protocols that people actually wanted to use (not that Nelson himself is at all happy with the result). How long will it take in the case of proof-checking?
