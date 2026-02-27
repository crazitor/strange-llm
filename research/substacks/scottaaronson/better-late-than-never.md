---
title: "Better late than never"
author: "Scott Aaronson"
date: "Tue, 03 May 2011"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=613"
---

No, I'm not talking about Osama, but about my reactions below to a _New Yorker_ article about quantum computing--reactions whose writing was rudely interrupted by last night's news. Of _all the possible times_ in the past decade to get him, they had to pick one that would overshadow an important _Shtetl-Optimized_ discussion about complexity theory, the Many-Worlds Interpretation, and the popularization of science? Well, I guess I'll let it slide.

* * *

As already discussed on [Peter Woit's blog](http://www.math.columbia.edu/~woit/wordpress/?p=3656), this week's _New Yorker_ has a [long piece about quantum computing](http://www.newyorker.com/reporting/2011/05/02/110502fa_fact_galchen) by the novelist Rivka Galchen (unfortunately the article is behind a paywall). Most of the article is about the quantum computing pioneer David Deutsch: his genius, his eccentricity, his certainty that parallel universes exist, his insistence on rational explanations for everything, his disdain for "intellectual obfuscators" (of whom Niels Bohr is a favorite example), his indifference to most of the problems that occupy other quantum computing researchers, the messiness of his house, his reluctance to leave his house, and his love of the TV show _House_.

Having spent a wonderful, mind-expanding day with Deutsch in 2002--at his house in Oxford, of course--I can personally vouch for all of the above (except the part about _House_ , which hadn't yet debuted then). On the one hand, Deutsch is one of the most brilliant conversationalists I've ever encountered; on the other hand, I was astonished to find myself, as a second-year graduate student, explaining to the father of quantum computing what [BQP](http://en.wikipedia.org/wiki/BQP) was. So basically, David Deutsch is someone who merits a _New Yorker_ profile if anyone does. And I was pleased to see Galchen skillfully leveraging Deutsch's highly-profilable personality to expose a lay audience (well, OK, a chardonnay-sipping Manhattan socialite audience) to some of the great questions of science and philosophy.

However, reading this article also depressed me, as it dawned on me that the entire thing could have __ been written fifteen years ago, with only minor changes to the parts about experiment and zero change to the theoretical parts. I thought: "has there _really_ been that little progress in quantum computing theory the past decade and a half--at least progress that a _New Yorker_ reader would care about?" Even the sociological observations are dated: Galchen writes about interest in quantum computing as the "Oxford flu," rather than the "Waterloo flu" or "Caltech flu" that it's been since 2000 or so (the latter two capitals of the field aren't even mentioned!). A good analogy would be an article about the Web, published today __, that described the strange and exciting new world of Netscape, HotBot, and AltaVista.

* * *

A more serious issue is that the article falls victim to almost every misleading pop-science trope about quantum computing that some of us have trying to correct for the past decade. For example:

With one millionth of the hardware of an ordinary laptop, a quantum computer could store as many bits of information as there are particles in the universe.

Noooooo! That's only for an extremely strange definition of "store"…

Oxford's eight-qubit quantum computer has significantly less computational power than an abacus, but fifty to a hundred qubits could make something as powerful as any laptop.

Noooooo! __ Fifty to a hundred qubits could _maybe_ replace your laptop, _if_ the only thing you wanted to use your laptop _for_ was simulating a system of fifty to a hundred qubits…

In a 1985 paper, Deutsch pointed out that, because Turing was working with classical physics, his universal computer could imitate only a subset of possible computers. Turing's theory needed to account for quantum mechanics if its logic was to hold. Deutsch proposed a universal quantum computer based on quantum physics, which would have calculating powers that Turing's computer (even in theory) could not simulate.

There are at least three problems here. The first is conflating simulation with _efficient_ simulation. At the risk of going hoarse, **a classical Turing machine can calculate absolutely everything that a quantum computer can calculate!** It might "merely" need exponentially more time. Second, no one has proved that a classical Turing machine really _does_ need exponentially more time, i.e., that it can't efficiently simulate a quantum computer. That remains a (deep, plausible, and widely-believed) _conjecture_ , which will take enormous mathematical advances to resolve. And third, Deutsch's landmark paper wasn't among the ones to give _evidence_ for that conjecture. The first such evidence only came later, with the work of Bernstein-Vazirani, Simon, and Shor.

To be fair to Galchen, Deutsch himself has often been inaccurate on these points, even though he ought to (and does!) know better. Specifically, he conflates the original [Church-Turing Thesis](http://en.wikipedia.org/wiki/Church%E2%80%93Turing_thesis) (which isn't challenged in the slightest __by quantum computing) with its modern, polynomial-time version (which is), and he neglects to mention the conjectural __status of quantum computers ' speedup. Here are two examples out of many, from _The Fabric of Reality_ :

"quantum computers can perform computations of which no (human) mathematician will ever, even in principle, be capable."  
"if the visible universe were the extent of physical reality, physical reality would not even remotely contain the resources required to factorize such a large number."

Am I just harping over technicalities here? In my view, the issue goes deeper. All of the above oversights can be understood as symptoms of **complexophobia** : _the fear of acknowledging that one is actually making statements about computational complexity theory_. Again and again, I've seen science writers go through strange verbal contortions to avoid the question of _how anyone could know that a computation inherently requires a huge amount of time_ --as if the reader must be prevented, at all costs, from seeing such a claim as anything other than obvious. It can be fascinating to watch, in the same way it's fascinating to watch a politician discuss (say) Confederate History Month [without mentioning slavery](http://www.politicsdaily.com/2010/04/08/va-governor-sorry-for-not-mentioning-slavery-in-confederate-his/). How long can you poke and prod the P versus NP beast without rousting it?

On the other hand, complexity theory _does_ show up in Galchen's article, and in an extremely interesting context: that of explaining where Deutsch got the idea for quantum computing.

According to Deutsch, the insight for [his famous 1985 paper] came from a conversation in the early eighties with the physicist Charles Bennett, of I.B.M., about computational-complexity theory, at the time a sexy new field that investigated the difficulty of a computational task.

Is "at the time" meant to imply complexity theory is no longer sexy, or merely that it's no longer new? Leaving that aside…

Mass, for instance, is a fundamental property, because it remains the same in any setting; weight is a relative property, because an object's weight depends on the strength of gravity acting on it … If computational complexity was like mass--if it was a relative property--then complexity was quite profound; if not, then not.

"I was just sounding off," Deutsch said. "I said they make too much of this"--meaning complexity theory--"because there's no standard computer with respect to which you should be calculating the complexity of the task." Just as an object's weight depends on the force of gravity in which it's measured, the degree of computational complexity depended on the computer on which it was measured. One could find out how complex a task was to perform on a particular computer, but that didn't say how complex a task was _fundamentally_ , in reference to the universe … Complexity theorists, Deutsch reasoned, were wasting their time.

The tale continues with Bennett pointing out that the universe _itself_ could be taken to be the "fundamental computer," which leads Deutsch to the shocking realization that the complexity theorists weren't _complete_ morons. Sure, they had a silly theory where all the answers depended on which computer you chose (which somehow none of them ever noticed), but luckily, it could be fixed by the simple addition of quantum mechanics!

Over the anguished howls of my classical complexity-theorist friends, I should point out that this story isn't _completely_ false. There's no denying that merging quantum mechanics with theoretical computer science was a major advance in human knowledge, and that the people who first had the idea to merge the two were _not_ computer scientists, but physicists like Deutsch and Feynman (the latter's role is completely left out of Galchen's story).

But complexity theory wasn't so much a flawed early attempt at quantum computing as an _essential prerequisite_ to it: the thing that made it possible to articulate how quantum computers might differ from classical computers in the first place. Indeed, it occurs to me that Deutsch and Bennett's conversation provides the key to resolving a puzzle discussed in the article:

"Quantum computers should have been invented in the nineteen-thirties," [Deutsch] observed near the end of our conversation. "The stuff that I did in the late nineteen-seventies and early nineteen-eighties didn't use any innovation that hadn't been known in the thirties." That is straightforwardly true. Deutsch went on, "The question is why."

I used to go around saying the same thing: "someone like John von Neumann could have _easily_ invented quantum computing in the 1930s, had he just put the pieces together!" But I now suspect this view is a mistake, the result of projecting what's obvious today onto a much earlier era. For there's at least _one_ essential ingredient for quantum computing that wouldn't enter scientific consciousness until the 1970s or so: complexity theory, and particularly the distinction between polynomial and exponential time.

* * *

Over the years, I've developed what I call the **Minus-Sign Test** , a reliable way to rate popularizations of quantum mechanics. To pass the Minus-Sign Test, all a popularization needs to do is _mention the minus signs:_ i.e., interference between positive and negative amplitudes, the defining feature of quantum mechanics, the thing that makes it _different_ from classical probability theory, the reason why we _can 't_ say Schrödinger's cat is "really either dead or alive," and we simply don't know which one, the reason why the entangled particles _can 't_ have just agreed in advance that one would spin up and the other would spin down. Another name for the Minus-Sign Test is the **High-School Student Test** , since it's the thing that determines whether a bright high-school student, meeting quantum mechanics for the first time through the popularization, would come away thinking of superposition as

(a) one of the coolest discoveries about Nature ever made, or  
(b) a synonym used by some famous authority figures for ignorance.

Despite the low bar set by the Minus-Sign Test, I'm afraid almost every popular article about quantum mechanics ever written has failed it, the present piece included.

* * *

Reading [Not Even Wrong](http://www.math.columbia.edu/~woit/wordpress/?p=3656), I was surprised at first that the discussion centered around Deutsch's argument that quantum computing proves the existence of [Many Worlds](http://en.wikipedia.org/wiki/Many-worlds_interpretation). (More precisely, Deutsch's position is that Many Worlds is an established fact _with or without_ quantum computing, but that for those who are too dense or stubborn to see it, a working quantum computer will be useful for hitting them over the head.)

As others pointed out: yes, the state of the universe as described by quantum mechanics is a vastly, _exponentially_ bigger thing than anything dreamt of in classical physics; and a scalable quantum computer would be dramatic evidence that this exponentiality is really "out there," that it's not just an artifact of our best current theory. These are not merely truths, but truths worth shouting from the rooftops.

However, there's then the further question of whether it's useful to talk about _one quantum-mechanical universe_ as an exponential number of parallel semi-classical universes. After all, to whatever extent the branches of a superposition successfully contribute to a quantum computation, to that extent they're not so much "parallel universes" as one giant, fault-tolerantly-encoded, self-interfering blob; and to whatever extent those branches _do_ look like parallel universes, to that extent they're now forever out of causal contact with each other--the branches other than our own figuring into our explanations for observable events only in the way that classical counterfactuals figure in.

Anyway, I thought: does anyone still _care_ about these issues? Wasn't every possible argument and counterargument explored to death years ago?

But this reaction just reveals my personal bias. Sometime in graduate school, I realized that I was less interested in winning philosophical debates than in discovering new phenomena for philosophers to debate about. Why brood over the true meaning of (say) Gödel's Theorem or the Bell Inequality, when there are probably other such worldview-changing results still to be found, and those results might render the brooding irrelevant anyway? Because of this attitude, I confess to being less interested in whether Many-Worlds is _true_ than in whether it's scientifically fruitful. As Peter Shor once memorably put it on this blog: why not be a Many-Worlder on Monday, a Bohmian on Tuesday, and a Copenhagenist on Wednesday, if that's what helps you prove new theorems?

Ironically, this attitude seems to me to mesh well with Deutsch's own emphasis on _explanation_ as the goal of science. Ask not whether the parallel universes are "really there," or whether they should really be called "parallel universes"--ask what explanatory work they do for _you_! (That is, over and above the explanatory work that QM itself already does for you, assuming you accept it and know how to use it.)

So for me, the single strongest argument in favor of Many-Worlds is what I call the "Deutsch argument":

_Many-Worlds is scientifically fruitful, because it led David Deutsch to think of quantum computing._

This argument carries considerable force for me. On the other hand, if we accept it, then it seems we should also accept the following argument:

_Bohmian mechanics is scientifically fruitful, because it led John Bell to think of the Bell inequality._

Furthermore, consider the following facts:

_David Deutsch is a brilliant, iconoclastic theoretical physicist, who thought deeply about quantum foundations at a time when it was unfashionable to do so. His extraordinary (and not wholly-unjustified!) self-confidence in his own powers of reasoning has led to his defending not one but many heterodox ideas._

Is it possible that these facts provide a common explanation for Deutsch's certainty about Many-Worlds _and_ his pioneering role in quantum computing, without our needing to invoke the former to explain the latter?

* * *

Let me end with a few miscellaneous reactions to Galchen's article.

Physics advances by accepting absurdities. Its history is one of unbelievable ideas proving to be true.

I'd prefer to say the history of physics is one of a vast number of unbelievable ideas proving to be _false_ , and a few _specific_ unbelievable ideas proving to be true--especially ideas having to do with the use of negative numbers where one might have thought only positive numbers made sense.

[Robert Schoelkopf and his group at Yale] have configured their computer to run what is known as a Grover's algorithm, one that deals with a four-card-monte type of question: Which hidden card is the queen? It's a sort of Shor's algorithm for beginners, something that a small quantum computer can take on.

No, small quantum computers can and have taken on both Shor's _and_ Grover's algorithms, solving tiny instances in each case. The _real_ difference between Shor's and Grover's algorithms is one that complexophobia might prevent Galchen from mentioning: Shor gives you a (conjectured) exponential speedup for some highly-specific problems (factoring and discrete log), while Grover gives you "merely" a quadratic speedup, but for a much wider class of problems.

"Look," [Deutsch] went on, "I can't stop you from writing an article about a weird English guy who thinks there are parallel universes. But I think that style of thinking is kind of a put-down to the reader. It's almost like saying, If you're not weird in these ways, you've got no hope as a creative thinker. That's not true. The weirdness is only superficial."

This was my favorite passage in the article.
