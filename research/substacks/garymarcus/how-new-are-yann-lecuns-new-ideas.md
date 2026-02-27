---
title: "How New are Yann LeCun’s “New” Ideas?"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/how-new-are-yann-lecuns-new-ideas"
---

At 62, the celebrated deep learning pioneer Yann LeCun, NYU professor, winner of the Turing Award, and Chief AI Scientist at Meta, is on a mission to reposition himself, not just as a deep learning pioneer, but as that guy with new ideas about how to move _past_ deep learning. He (or perhaps MetaAI’s PR department) has talked both _Technology Review_ and _ZDNet_ into laudatory profiles, the former entitled _[Yann LeCun has a bold new vision for the future of AI](https://www.technologyreview.com/2022/06/24/1054817/yann-lecun-bold-new-vision-future-ai-deep-learning-meta/)._**** Just**** since the beginning of June, LeCun has also posted [a widely-discussed manifesto](https://openreview.net/forum?id=BZ5a1r-kVsf), and a [review of my own work](https://www.noemamag.com/what-ai-can-tell-us-about-intelligence/) [which differs in some important respects from his] staking out his own position on the important question of symbol-manipulation. But how much of what he is saying is really _new_?

When I read the _ZDNet_ interview, which was published yesterday, I was astounded. And not in a good way. Nearly everything LeCun said, I had said earlier, some almost word for word—most of it in a 2018 paper called [Deep Learning: A Critical Appraisal](https://arxiv.org/abs/1801.00631) **** that LeCun had pilloried at the time as “[mostly wrong](https://twitter.com/ylecun/status/948656980331200512?s=20&t=qY9iFaaRhHGfrAuLBKnMMA)”. 

Here are seven examples; as we shall see, this is but one instance of a larger problem.

  * LeCun, 2022: Today's AI approaches will never lead to true intelligence (reported in the headline, not a verbatim quote); Marcus, 2018: “deep learning must be supplemented by other techniques if we are to reach artificial general intelligence.”

  * LeCun, 2022: [Current Deep learning models] “may be a component of a future intelligent system, but I think it's missing essential pieces."; “I think they're necessary but not sufficient,"; Marcus 2018: “Despite all of the problems I have sketched, I don’t think that we need to abandon deep learning. Rather, we need to reconceptualize it: not as a universal solvent, but simply as one tool among many, a power screwdriver in a world in which we also need hammers, wrenches, and pliers, not to mentions chisels and drills, voltmeters, logic probes, and oscilloscopes.”

  * LeCun, 2022: Reinforcement learning will also never be enough for intelligence; Marcus, 2018: “ it is misleading to credit deep reinforcement learning with inducing concept[s] ”

  * LeCun, 2022: “We're not to the point where our intelligent machines have as much common sense as a cat," observes Lecun. "So, why don't we start there?" Marcus, 2022: “Where else should we look [beyond deep learning]? … A second focal point might be on common sense knowledge”

  * LeCun, 2022: “I think AI systems need to be able to reason,"; Marcus 2018: “Problems that have less to do with categorization and more to do with commonsense reasoning essentially lie outside the scope of what deep learning is appropriate for, and so far as I can tell, deep learning has little to offer such problems.”

  * LeCun, 2022: "You have to take a step back and say, Okay, we built this ladder, but we want to go to the moon, and there's no way this ladder is going to get us there”: Marcus, in _[The New Yorker](https://www.newyorker.com/news/news-desk/is-deep-learning-a-revolution-in-artificial-intelligence)_[ in 2012](https://www.newyorker.com/news/news-desk/is-deep-learning-a-revolution-in-artificial-intelligence): “To paraphrase an old parable, [with deep learning] Hinton has built a better ladder; but a better ladder doesn’t necessarily get you to the moon.”




Nobody has ever reprised my own arguments more closely than LeCun did yesterday, much less without attribution. 

I won’t accuse LeCun of plagiarism, because I think he probably reached these conclusions honestly, after recognizing the failures of current architectures. What I foresaw, he has finally recognized for himself. At some level this is a tremendous victory for me - to have someone so eminent move to a position that I staked out, long ago. 

§

But there is more to the story to than that. A lot more.

To begin with, LeCun is determined to never be seen as echoing anything I have ever said. Since he very publicly criticized my earlier paper, we know he is aware of it. The degreee to which LeCun failed to share any credit—an absolute violation of academic etiquette (we’ve both been professors since the ‘90s, though I retired early)—is striking. 

More than that, to make sure _nobody_ gave me any credit, he took a gratuitious, and completely dishonest potshot at me, in the same interview, alleging, quite falsely “Gary Marcus is not an AI person, by the way, he is a psychologist. He has never contributed anything to AI. He's done really good work in experimental psychology but he's never written a peer-reviewed paper on AI”— which is simply false. In reality, I have published extensively in AI, some in peer-reviewed journals, some not. [My most important AI paper, which did experimental work on neural networks, foresaw in 1998 the challenges of distribution shift and outliers that are preoccupying Yoshua Bengio and others now](https://www.sciencedirect.com/science/article/pii/S0010028598906946). In the last decade, I have published peer-reviewed AI articles on topics such as [common sense](https://cacm.acm.org/magazines/2015/9/191169-commonsense-reasoning-and-commonsense-knowledge-in-artificial-intelligence/fulltext),[ reasoning from incomplete information](https://www.sciencedirect.com/science/article/pii/S0004370217300383), and [limits of simulation and automatic reasoning](https://www.sciencedirect.com/science/article/pii/S0004370215001794), many with the NYU computer scientist Ernest Davis, who happens to be in LeCun’s department. Perhaps my most influential AI work of all happens not to have been a journal article, but a 2001 book _The Algebraic Mind_ (which MIT Press sent out for peer review). Nearly every bit of what LeCun told _ZDNet_ was foreseen there; [two leaders in the fast-growing field of neurosymbolic AI](https://arxiv.org/pdf/2012.05876.pdf)**[](https://arxiv.org/pdf/2012.05876.pdf)**[have said that they see ](https://arxiv.org/pdf/2012.05876.pdf)_[The Algebraic Mind](https://arxiv.org/pdf/2012.05876.pdf)_[ as vital to their approach](https://arxiv.org/pdf/2012.05876.pdf). What LeCun really means is that he hasn’t read any of it; the idea that it isn’t influential is laughable. 

LeCun’s claim was egregious enough that others have come to my defense; _ZDNet_ posted an immediate correction, and as I was drafting this, Miguel Solano, CEO of Vmind.AI wrote this, backing me up: 

[Miguel Ignacio Solano@miguelisolano@GaryMarcus @ZDNET @TiernanRayTech @ylecun This is true, @ylecun. @GaryMarcus's The Algebraic Mind (MIT Press, 2001), for instance, has 868+ citations, and was certainly engaged in the AI literature: [scholar.google.com/scholar?cites=…](https://scholar.google.com/scholar?cites=2332635447613222375&as_sdt=205&sciodt=0,1&hl=en)3:28 PM · Sep 25, 2022

* * *

1 Like](https://twitter.com/miguelisolano/status/1574058386638921728?s=20&t=v__p6SmmTcpObOVpT4yCUQ)

Henning Schwabe was even more pointed, building on remarks from Dagmar Monett:

[Henning Schwabe@SchwabeHenning@ylecun ‘s unfair attack is tragic b/c it will help DL maximalist to dismiss his critique - he should have allied with @GaryMarcus to further his agenda. Ego as always the enemy of reason. Dagmar Monett @dmonettI found explanations for LeCun's behavior in @Eric_Sadin's "The Silicolonization of the World" (2016/2018). See pic & translation. @ZDNET's interview only reinforces this and leaves him in a terrible position. The audacity... How LeCun refers to other academics and their work 😳 https://t.co/qy3WrIcJAb https://t.co/KlPXhYjNxM4:09 PM · Sep 25, 2022

* * *

1 Repost · 2 Likes](https://twitter.com/schwabehenning/status/1574068695365713921?s=21&t=HZKXIk563Of_sThmVVymjg)

Graduate students sometimes play fast and loose with credit to build themselves up; Harold Bloom once wrote a book about what he called _The Anxiety of Influence_. Until this year I had never seen anything like this in someone of LeCun’s stature. 

But this year I have seen it from him, over and over. 

§ 

Each of LeCun’s recent papers and essays has, in its own way, exhibited the same denial of the past.

One essay involved the long standing question of symbol-manipulation. Since I [already responded at length in ](https://www.noemamag.com/deep-learning-alone-isnt-getting-us-to-human-like-ai/)_[Noema](https://www.noemamag.com/deep-learning-alone-isnt-getting-us-to-human-like-ai/)_ , I will summarize only briefly here. LeCun spent part of his career bashing symbols; his collaborator Geoff Hinton even more so, Their jointly written 2015 review of deep learning ends by saying that they “new paradigms are needed to replace rule-based manipulation of symbolic expressions.” 

Nowadays LeCun is _endorsing_ symbol-manipulation (an idea I did not invent but have been defending for 30 years), and acting as if nobody said otherwise—a dispatch from Orwell’s Ministry of Truth. As I put it in _Noema_ , when LeCun and Browning wrote “everyone working in [Deep Learning] agrees that symbolic manipulation is a necessary feature for creating human-like AI,” they are walking back decades of history. Even Stanford AI Professor Christopher Manning (often closer in his views to LeCun then me) was shocked:

[Christopher Manning@chrmanningI sense some evolution in @ylecun’s position—perhaps under Browning's influence; this piece suggests that “everyone working in DL agrees that symbolic manipulation is a necessary feature for creating human-like AI.” Was that really true a decade ago, or is it even true now?!?12:38 AM · Jul 28, 2022

* * *

1 Repost · 23 Likes](https://twitter.com/chrmanning/status/1552453310812401664)

When I pointed all this out at length, LeCun’s only response to my lengthy, detailed analysis article, which was fact-checked by _Noema_ , was, well, lame. In lieu of responding, he retweeted a vague, contentless rejoinder written by his co-author:

[Browning.jake00@Jake_Browning00A reply to our piece from @GaryMarcus But I don't think we agree where he says we do, or disagree on where our disagreements are. But that's the nature of difficult issues, I suppose. Noema Magazine @NoemaMagIs a decades-long AI debate finally coming to a resolution? @garymarcus is seeing signs that it is. Now "we can finally focus on the real issue: how to get data-driven learning & abstract, symbolic representations to work together." https://t.co/QtaxfAEWdv7:13 PM · Aug 14, 2022

* * *

2 Reposts · 8 Likes](https://twitter.com/Jake_Browning00/status/1558894580984070146?s=20&t=v__p6SmmTcpObOVpT4yCUQ)

Not one specific objection to _anything_ that I said in [my scathing rebuttal](https://www.noemamag.com/deep-learning-alone-isnt-getting-us-to-human-like-ai/).

§

Another of LeCun’s recent essays involved the important question of whether large language models are really on the right track to general intelligence, and whether one can really learn enough from language alone. LeCun and his collaborator Browning make a strong case that language input alone (which is the kind of thing that GPT-3 is trained on) is not enough, writing an essay called [AI And The Limits Of Language](https://www.noemamag.com/ai-and-the-limits-of-language/?utm_source=noematwitter&utm_medium=noemasocial) arguing that “A system trained on language alone will never approximate human intelligence, even if trained from now until the heat death of the universe.” 

But here again there’s a lack of credit. Here for example is something I wrote about the same question in February 2020 in an arXiv artcle called _[The Next Decade in AI](https://arxiv.org/abs/2002.06177)_ :

> Waiting for cognitive models and reasoning to magically emerge from larger and larger [language] training corpora is like waiting for a miracle…

— almost exactly what LeCun and Browning concluded. 

But, no, we are not done.

§

The key question is what we as field should _do_ about the fact that you can’t really solve AI from large language models alone. Here was my prescription in January 2020:

> A system like GPT-2, for instance, does what it does, for better and for worse, without any explicit (in the sense of directly represented and readily shared) common sense knowledge, without any explicit reasoning, and without any explicit cognitive models of the world it that tries to discuss.

and in February 2020

> Every moment spent on improving massive models of word-level prediction… might be better spent on developing techniques for deriving, updating, and reasoning over cognitive models.

Sound familiar? Incorporating cognitive models is what LeCun was pitching to _ZDnet_ yesterday, and in many ways the heart of LeCun’s summer manifesto. 

When I first made this point in 2019, guess who publicly bullied me for saying it? That’s right, Yann LeCun. 

I wrote:

[Gary Marcus@GaryMarcusKey problem with systems like GPT-2 is not that they dont deal with quantities (as @ylecun suggests below), it is they don't develop robust representations of *how events unfold over time* Clearest w number, but true in many cases, and it's part of why the quantity cases fail: Yann LeCun @ylecun@StanDehaene @GaryMarcus Actually, machines that are trained to deal with quantities do learn to deal with quantities. Gary merely says that machines trained to predict missing words don't learn much about quantities. Duh!1:02 PM · Oct 28, 2019

* * *

15 Reposts · 36 Likes](https://twitter.com/GaryMarcus/status/1188803198980521986?s=20&t=f7gMMXhQW31d4_gsVik2xA)

which is a different way of saying that the problem with large language models is a lack of cognitive models.

At that time, LeCun accused me of fighting a rear-guard battle:

[Yann LeCun@ylecun@GaryMarcus Wrong. See this: [arxiv.org/abs/1612.03969](https://arxiv.org/abs/1612.03969) Look at Table 2: Row 7 (counting) and 14 (time reasoning) both get 0 error rates (this is on bAbI tasks). When you are fighting a rear-guard battle, it's best to know when you adversary overtook your rear 3 years ago.7:35 PM · Oct 28, 2019

* * *

1 Repost · 11 Likes](https://twitter.com/ylecun/status/1188902027495006208?s=20&t=rZorYMVHU32iCXJmFfICOQ)

Now that he seen the light, he has forgotten that it ever happened. I saw the critical need for cognitive models first; he attacked me; now he claims it as his own.

§

Now here’s the thing: I have a right to be pissed, but I am not alone. 

Deep learning pioneer Jürgen Schmidhuber, author of the commercially ubiquitous LSTM neural network, arguably has even more right to be pissed, as he recently made clear on [Twitter](https://twitter.com/schmidhuberai/status/1544939700099710976?s=46&t=D5CEGCOBlHsn9TEeUhFZBA) and in a lengthy manuscript:

[Jürgen Schmidhuber@SchmidhuberAILecun (@ylecun)’s 2022 paper on Autonomous Machine Intelligence rehashes but doesn’t cite essential work of 1990-2015. We’ve already published his “main original contributions:” learning subgoals, predictable abstract representations, multiple time scales…people.idsia.ch2022 paper by LeCun rehashes but does not cite work of 1990-20157:01 AM · Jul 7, 2022

* * *

191 Reposts · 1.1K Likes](https://twitter.com/schmidhuberai/status/1544939700099710976?s=46&t=D5CEGCOBlHsn9TEeUhFZBA)

“Rehashes but doesn’t cite”—that’s polite peer reviewer-ese for “a lot less original than it pretends to be”.

A large part of LeCun’s new manifesto is a well-motivated call for incorporating a “configurable predictive world model” into deep learning. I’ve been calling for that for a little while, but Schmidhuber deserves more credit, because he had actually been trying to implement that in the forerunners to deep learning the 1990s, and LeCun scarcely gave his team’s work the time of day. 

§

By now some of the Twitterverse is on to LeCun. When LeCun’s manifesto come out, German computational neuroscientist and AI researcher Patrick Krauss tweeted, sarcastically

[Patrick Krauss@Krauss_PKWow! AGI finally solved! 😂 @ylecun discovers what's missing so far in deep learning: common sense and a world model! [technologyreview.com/2022/06/24/105…](https://www.technologyreview.com/2022/06/24/1054817/yann-lecun-bold-new-vision-future-ai-deep-learning-meta/) @GaryMarcus @maier_aktechnologyreview.comYann LeCun has a bold new vision for the future of AI12:23 PM · Jun 25, 2022

* * *

5 Reposts · 45 Likes](https://twitter.com/krauss_pk/status/1540672021146787840?s=12)

This morning, the mononymous Lathropa was even more pointed. As is well known throughout the field, LeCun has taken numerous digs on the title of a widely-read essay I wrote for Nautilus in March 2022, called [Deep Learning Is Hitting A Wall](https://nautil.us/deep-learning-is-hitting-a-wall-238440/). 

So, what is he really trying to say now, a few months later?

[Lathropa@lathropa@GaryMarcus @MetaAI @ylecun "'Okay, we built this ladder, but we want to go to the moon, and there's no way this ladder is going to get us there,' says LeCun of his desire to prompt a rethinking of basic concepts." It's almost as if his approach has run into some sort of wall-shaped obstacle...2:00 AM · Sep 25, 2022

* * *

1 Repost · 19 Likes](https://twitter.com/lathropa/status/1573854861740965889?s=21&t=HZKXIk563Of_sThmVVymjg)

I have so much trouble seeing what’s really new in LeCun’s recent flurry that I asked him yesterday on Twitter to explain.

So far he hasn’t answered.

[Share](https://garymarcus.substack.com/p/how-new-are-yann-lecuns-new-ideas?utm_source=substack&utm_medium=email&utm_content=share&action=share)
