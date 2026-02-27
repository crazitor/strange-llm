---
title: "Giulio Tononi and Me: A Phi-nal Exchange"
author: "Scott Aaronson"
date: "Fri, 30 May 2014"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=1823"
---

You might recall that last week I [wrote a post](https://scottaaronson.blog/?p=1799) criticizing Integrated Information Theory (IIT), and its apparent implication that a simple Reed-Solomon decoding circuit would, if scaled to a large enough size, bring into being a consciousness vastly exceeding our own. On Wednesday Giulio Tononi, the creator of IIT, was kind enough to send me a fascinating 14-page rebuttal, and to give me permission to share it here:

**[Why Scott should stare at a blank wall and reconsider (or, the conscious grid)](http://www.scottaaronson.com/tononi.docx)**

If you're interested in this subject at all, then I strongly recommend reading Giulio's response before continuing further. But for those who want the tl;dr: Giulio, not one to battle strawmen, first restates my own argument against IIT with crystal clarity. And while he has some minor quibbles (e.g., apparently my calculations of Φ didn't use the most recent, "3.0" version of IIT), he wisely sets those aside in order to focus on the core question: **according to IIT, are all sorts of simple expander graphs conscious?**

There, he doesn't "bite the bullet" so much as devour a bullet hoagie with mustard. He affirms that, yes, according to IIT, a large network of XOR gates arranged in a simple expander graph is conscious. Indeed, he goes further, and says that the "expander" part is superfluous: even a network of XOR gates arranged in a 2D square grid is conscious. In my language, Giulio is simply pointing out here that a √n×√n square grid has _decent_ expansion: good enough to produce a Φ-value of about √n, if not the information-theoretic maximum of n (or n/2, etc.) that an expander graph could achieve. And apparently, by Giulio's lights, Φ=√n is sufficient for consciousness!

While Giulio never mentions this, it's interesting to observe that logic gates arranged in a _1-dimensional line_ would produce a tiny Φ-value (Φ=O(1)). So even by IIT standards, such a linear array would _not_ be conscious. Yet the jump from a line to a two-dimensional grid is enough to light the spark of Mind.

Personally, I give Giulio enormous credit for having the intellectual courage to follow his theory wherever it leads. When the critics point out, "if your theory were true, then the Moon would be made of peanut butter," he doesn't try to wiggle out of the prediction, but proudly replies, "yes, _chunky_ peanut butter--and you forgot to add that the Earth is made of Nutella!"

Yet even as we admire Giulio's honesty and consistency, his stance might also prompt us, gently, to take another look at this peanut-butter-moon theory, and at what grounds we had for believing it in the first place. In his response essay, Giulio offers four arguments (by my count) for accepting IIT despite, or even because of, its conscious-grid prediction: one "negative" argument and three "positive" ones. Alas, while your Φ-lage may vary, I didn't find _any_ of the four arguments persuasive. In the rest of this post, I'll go through them one by one and explain why.

**I. The Copernicus-of-Consciousness Argument**

Like many commenters on my last post, Giulio heavily criticizes my appeal to "common sense" in rejecting IIT. Sure, he says, I might find it "obvious" that a huge Vandermonde matrix, or its physical instantiation, isn't conscious. But didn't people also find it "obvious" for millennia that the Sun orbits the Earth? Isn't the entire point of science to _challenge_ common sense? Clearly, then, the test of a theory of consciousness is not how well it upholds "common sense," but how well it fits the facts.

The above position sounds pretty convincing: who could dispute that observable facts trump personal intuitions? The trouble is, what _are_ the observable facts when it comes to consciousness? The anti-common-sense view gets all its force by pretending that we're in a relatively late stage of research--namely, the stage of taking an agreed-upon scientific definition of consciousness, and applying it to test our intuitions--rather than in an extremely early stage, of _agreeing on what the word "consciousness" is even supposed to mean_.

Since I think this point is extremely important--and of general interest, beyond just IIT--I'll expand on it with some analogies.

Suppose I told you that, in my opinion, the ε-δ definition of continuous functions--the one you learn in calculus class--failed to capture the true meaning of continuity. Suppose I told you that I had a new, _better_ definition of continuity--and amazingly, when I tried out my definition on some examples, it turned out that ⌊x⌋ (the floor function) was continuous, whereas x2 had discontinuities, though only at 17.5 and 42.

You would probably ask what I was smoking, and whether you could have some. But why? Why _shouldn 't_ the study of continuity produce counterintuitive results? After all, even the _standard_ definition of continuity leads to some famously weird results, like that [x sin(1/x)](http://oregonstate.edu/instruct/mth251/cq/Stage5/Practice/Images/pinchTopSine.gif) is a continuous function, even though [sin(1/x)](http://upload.wikimedia.org/wikipedia/commons/a/a4/Sin\(1x\).svg) is discontinuous. And it's not as if the standard definition is God-given: people had been using words like "continuous" for centuries before Bolzano, Weierstrass, et al. formalized the ε-δ definition, a definition that millions of calculus students still find far from intuitive. So why _shouldn 't_ there be a different, better definition of "continuous," and why shouldn't it reveal that a step function is continuous while a parabola is not?

In my view, the way out of this conceptual jungle is to realize that, before any formal definitions, any ε's and δ's, we start with an  _intuition_ for we're trying to capture by the word "continuous." And if we press hard enough on what that intuition involves, we'll find that it largely consists of various "paradigm-cases." A _continuous function_ , we'd say, is a function like 3x, or x2, or sin(x), while a _discontinuity_ is the kind of thing that the function 1/x has at x=0, or that ⌊x⌋ has at every integer point. Crucially, we use the paradigm-cases to guide our choice of a formal definition--not vice versa! It's true that, once we _have_ a formal definition, we can then apply it to "exotic" cases like x sin(1/x), and we might be surprised by the results. But the paradigm-cases are different. If, for example, our definition told us that x2 was discontinuous, that wouldn't be a "surprise"; it would just be evidence that we'd picked a bad definition. The definition failed at the only task for which it could have succeeded: namely, that of capturing what we meant.

Some people might say that this is all well and good in pure math, but empirical science has no need for squishy intuitions and paradigm-cases. Nothing could be further from the truth. Suppose, again, that I told you that physicists since Kelvin had gotten the definition of temperature all wrong, and that I had a new, better definition. And, when I built a Scott-thermometer that measures  _true_ temperatures, it delivered the shocking result that _boiling water is actually colder than ice_. You'd probably tell me where to shove my Scott-thermometer. But wait: how do you know that I'm not the Copernicus of heat, and that future generations won't celebrate my breakthrough while scoffing at your small-mindedness?

I'd say there's an excellent answer: because what we  _mean_ by heat is "whatever it is that boiling water has more of than ice" (along with dozens of other paradigm-cases). And because, if you use a thermometer to check whether boiling water is hotter than ice, then the term for what you're doing is  _calibrating your thermometer_. When the clock strikes 13, it's time to fix the clock, and when the thermometer says boiling water's colder than ice, it's time to replace the thermometer--or if needed, even the entire theory on which the thermometer is based.

Ah, you say, but doesn't modern physics define heat in a completely different, _non_ -intuitive way, in terms of molecular motion? Yes, and that turned out to be a superb definition--not only because it was precise, explanatory, and applicable to cases far beyond our everyday experience, but crucially, _because it matched common sense on the paradigm-cases_. If it _hadn 't_ given sensible results for boiling water and ice, then the only possible conclusion would be that, whatever new quantity physicists had defined, _they shouldn 't call it "temperature,"_ or claim that their quantity measured the amount of "heat." They should call their new thing something else.

The implications for the consciousness debate are obvious. When we consider whether to accept IIT's equation of integrated information with consciousness,_we don 't start with any agreed-upon, independent notion of consciousness against which the new notion can be compared_. The main things we start with, in my view, are certain paradigm-cases that gesture toward what we mean:

  * You are conscious (though not when anesthetized).
  * (Most) other people appear to be conscious, judging from their behavior.
  * Many animals appear to be conscious, though probably to a lesser degree than humans (and the degree of consciousness in each particular species is far from obvious).
  * A rock is not conscious. A wall is not conscious. A Reed-Solomon code is not conscious. Microsoft Word is not conscious (though a Word macro that passed the Turing test conceivably _would_ be).



Fetuses, coma patients, fish, and hypothetical AIs are the x sin(1/x)'s of consciousness: they're the tougher cases, the ones where we might actually _need_ a formal definition to adjudicate the truth.

Now, given a proposed formal definition for an intuitive concept, how can we check whether the definition is talking about same thing we were trying to get at before? Well, we can check whether the definition at least agrees that parabolas are continuous while step functions are not, that boiling water is hot while ice is cold, and that we're conscious while Reed-Solomon decoders are not. If so, then the definition  _might_ be picking out the same thing that we meant, or were trying to mean, pre-theoretically (though we still can't be certain). If not, then the definition is _certainly_ talking about something else.

What else can we do?

**II. The Axiom Argument**

According to Giulio, there _is_ something else we can do, besides relying on paradigm-cases. That something else, in his words, is to lay down "_postulates_ about how the physical world should be organized to support the essential properties of experience," then use those postulates to derive a consciousness-measuring quantity.

OK, so what are IIT's postulates? Here's how Giulio states the five postulates leading to Φ in his response essay (he "derives" these from earlier "phenomenological axioms," which you can find in the essay):

  1. A system of mechanisms exists intrinsically if it can make a difference to itself, by affecting the probability of its past and future states, i.e. it has causal power (existence).
  2. It is composed of submechanisms each with their own causal power (composition).
  3. It generates a conceptual structure that is the specific way it is, as specified by each mechanism's concept -- this is how each mechanism affects the probability of the system's past and future states (information).
  4. The conceptual structure is unified -- it cannot be decomposed into independent components (integration).
  5. The conceptual structure is singular -- there can be no superposition of multiple conceptual structures over the same mechanisms and intervals of time.



From my standpoint, these postulates have three problems. First, I don't really understand them. Second, insofar as I do understand them, I don't necessarily accept their truth. And third, insofar as I do accept their truth, I don't see how they lead to Φ.

To elaborate a bit:

_I don 't really understand the postulates._ I realize that the postulates are explicated further in the many papers on IIT. Unfortunately, while it's possible that I missed something, in all of the papers that I read, the definitions never seemed to "bottom out" in mathematical notions that I understood, like functions mapping finite sets to other finite sets. What, for example, is a "mechanism"? What's a "system of mechanisms"? What's "causal power"? What's a "conceptual structure," and what does it mean for it to be "unified"? Alas, it doesn't help to define these notions in terms of other notions that I also don't understand. And yes, I agree that all these notions can be _given_ fully rigorous definitions, but there could be many different ways to do so, and the devil could lie in the details. In any case, because (as I said) it's entirely possible that the failure is mine, I place much less weight on this point than I do on the two points to follow.

_I don 't necessarily accept the postulates' truth._ Is consciousness a "unified conceptual structure"? Is it "singular"? Maybe. I don't know. It sounds plausible. But at any rate, I'm far less confident about any these postulates--_whatever_ one means by them!--than I am about my own "postulate," which is that you and I are conscious while my toaster is not. Note that my postulate, though not phenomenological, does have the merit of constraining candidate theories of consciousness in an unambiguous way.

_I don 't see how the postulates lead to Φ._ Even if one accepts the postulates, how does one deduce that the "amount of consciousness" should be measured by Φ, rather than by some other quantity? None of the papers I read--including the ones Giulio linked to in his response essay--contained anything that looked to me like a derivation of Φ. Instead, there was general discussion of the postulates, and then Φ just sort of appeared at some point. Furthermore, given the many idiosyncrasies of Φ--the minimization over all bipartite (why just bipartite? why not tripartite?) decompositions of the system, the need for normalization (or something else in version 3.0) to deal with highly-unbalanced partitions--it would be quite a surprise were it possible to derive its specific form from postulates of such generality.

I was going to argue for that conclusion in more detail, when I realized that Giulio had kindly done the work for me already. Recall that Giulio chided me for not using the "latest, 2014, version 3.0" edition of Φ in my previous post. Well, if the postulates uniquely determined the form of Φ, then what's with all these upgrades? Or has Φ's definition been changing from year to year because the postulates _themselves_ have been changing? If the latter, then maybe one should wait for the situation to stabilize before trying to form an opinion of the postulates' meaningfulness, truth, and completeness?

**III. The Ironic Empirical Argument**

Or maybe not. Despite all the problems noted above with the IIT postulates, Giulio argues in his essay that there's a good a reason to accept them: namely, they  _explain various empirical facts from neuroscience, and lead to confirmed predictions._ In his words:

[A] theory's postulates must be able to explain, in a principled and parsimonious way, at least those many facts about consciousness and the brain that are reasonably established and non-controversial. For example, we know that our own consciousness depends on certain brain structures (the cortex) and not others (the cerebellum), that it vanishes during certain periods of sleep (dreamless sleep) and reappears during others (dreams), that it vanishes during certain epileptic seizures, and so on. Clearly, a theory of consciousness must be able to provide an adequate account for such seemingly disparate but largely uncontroversial facts. Such empirical facts, and not intuitions, should be its primary test…

[I]n some cases we already have some suggestive evidence [of the truth of the IIT postulates' predictions]. One example is the cerebellum, which has 69 billion neurons or so -- more than four times the 16 billion neurons of the cerebral cortex -- and is as complicated a piece of biological machinery as any. Though we do not understand exactly how it works (perhaps even less than we understand the cerebral cortex), its connectivity definitely suggests that the cerebellum is ill suited to information integration, since it lacks lateral connections among its basic modules. And indeed, though the cerebellum is heavily connected to the cerebral cortex, removing it hardly affects our consciousness, whereas removing the cortex eliminates it.

I hope I'm not alone in noticing the irony of this move. But just in case, let me spell it out: Giulio has stated, as "largely uncontroversial facts," that certain brain regions (the cerebellum) and certain states (dreamless sleep) are not associated with our consciousness. He then views it as a victory for IIT, if those regions and states turn out to have lower information integration than the regions and states that he _does_ take to be associated with our consciousness.

But _how does Giulio know that the cerebellum isn 't conscious?_ Even if it doesn't produce "our" consciousness, maybe the cerebellum has its own consciousness, just as rich as the cortex's but separate from it. Maybe removing the cerebellum destroys that other consciousness, unbeknownst to "us." Likewise, maybe "dreamless" sleep brings about its own form of consciousness, one that (unlike dreams) we never, ever remember in the morning.

Giulio might take the implausibility of those ideas as obvious, or at least as "largely uncontroversial" among neuroscientists. But here's the problem with that: **he just told us that a 2D square grid is conscious!** He told us that we must _not_ rely on "commonsense intuition," or on any popular consensus, to say that if a square mesh of wires is just sitting there XORing some input bits, doing nothing at all that we'd want to call intelligent, then it's probably safe to conclude that the mesh isn't conscious. So then why shouldn't he say the same for the cerebellum, or for the brain in dreamless sleep? By Giulio's own rules (the ones he used for the mesh), we have no _a-priori_ clue whether those systems are conscious or not--so even if IIT predicts that they're not conscious, that can't be counted as any sort of success for IIT.

For me, the point is even stronger: I, personally, would be a million __ times more inclined to ascribe consciousness to the human cerebellum, or to dreamless sleep, than I would to the mesh of XOR gates. For it's not hard to imagine neuroscientists of the future discovering "hidden forms of intelligence" in the cerebellum, and all but impossible to imagine them doing the same for the mesh. But even if you put those examples on the same footing, still the take-home message seems clear: **you can 't count it as a "success" for IIT if it predicts that the cerebellum in unconscious, while at the same time denying that it's a "failure" for IIT if it predicts that a square mesh of XOR gates is conscious.** If the unconsciousness of the cerebellum can be considered an "empirical fact," safe enough for theories of consciousness to be judged against it, then _surely_ the unconsciousness of the mesh can also be considered such a fact.

**IV. The Phenomenology Argument**

I now come to, for me, the strangest and most surprising part of Giulio's response. Despite his earlier claim that IIT need not dovetail with "commonsense intuition" about which systems are conscious--that it can _defy_ intuition--at some point, Giulio valiantly tries to _reprogram_ our intuition, to make us _feel_ why a 2D grid could be conscious. As best I can understand, the argument seems to be that, when we stare at a blank 2D screen, we form a rich experience in our heads, and that richness must be mirrored by a corresponding "intrinsic" richness in 2D space itself:

[I]f one thinks a bit about it, the experience of empty 2D visual space is not at all empty, but contains a remarkable amount of structure. In fact, when we stare at the blank screen, quite a lot is immediately available to us without any effort whatsoever. Thus, we are aware of all the possible locations in space ("points"): the various locations are right "there", in front of us. We are aware of their relative positions: a point may be left or right of another, above or below, and so on, for every position, without us having to order them. And we are aware of the relative distances among points: quite clearly, two points may be close or far, and this is the case for every position. Because we are aware of all of this immediately, without any need to calculate anything, and quite regularly, since 2D space pervades most of our experiences, we tend to take for granted the vast set of relationship[s] that make up 2D space.

And yet, says IIT, given that our experience of the blank screen definitely _exists_ , and it is precisely the way it is -- it _is_ 2D visual space, with all its relational properties -- there must be physical mechanisms that specify such phenomenological relationships through their causal power … One may also see that the causal relationships that make up 2D space obtain whether the elements are on or off. And finally, one may see that such a 2D grid is necessary not so much to _represent_ space from the extrinsic perspective of an observer, but to _create_ it, from its own _intrinsic_ perspective.

Now, it would be child's-play to criticize the above line of argument for conflating  _our_ consciousness of the screen with the alleged consciousness of the screen itself. To wit: Just because it feels like something to  _see_ a wall, doesn't mean it feels like something to _be_ a wall. You can smell a rose, and the rose can smell good, but that doesn't mean the rose can smell you.

However, I actually prefer a different tack in criticizing Giulio's "wall argument." Suppose I accepted that my mental image of the relationships between certain entities was relevant to assessing whether those entities had  _their own_ mental life, independent of me or any other observer. For example, suppose I believed that, if my experience of 2D space is rich and structured, then that's evidence that 2D space _is_ rich and structured enough to be conscious.

Then my question is this: **why shouldn 't the same be true of 1D space?** After all, my experience of staring at a rope is _also_ rich and structured, no less than my experience of staring at a wall. I perceive some points on the rope as being toward the left, others as being toward the right, and some points as being _between_ two other points. In fact, the rope even has a structure--namely, a natural total ordering on its points--that the wall lacks. So why does IIT cruelly deny subjective experience to a row of logic gates strung along a rope, reserving it only for a mesh of logic gates pasted to a wall?

And yes, I know the answer: because the logic gates on the rope aren't "integrated" enough. But who's to say that the gates in the 2D mesh _are_ integrated enough? As I mentioned before, their Φ-value grows only as the square root of the number of gates, so that the ratio of integrated information to total information tends to 0 as the number of gates increases. And besides, aren't what Giulio calls "the facts of phenomenology" the real arbiters here, and isn't my perception of the rope's structure a phenomenological fact? When you cut a rope, does it not split? When you prick it, does it not fray?

**Conclusion**

At this point, I fear we're at a philosophical impasse. Having learned that, according to IIT,

  1. a square grid of XOR gates is conscious, and your experience of staring at a blank wall provides evidence for that,
  2. by contrast, a linear array of XOR gates is  _not_ conscious, your experience of staring at a rope notwithstanding,
  3. the human cerebellum is _also_ not conscious (even though a grid of XOR gates is), and
  4. unlike with the XOR gates, we don't need a theory to _tell_ us the cerebellum is unconscious, but can simply accept it as "reasonably established" and "largely uncontroversial,"



I personally feel completely safe in saying that this is not the theory of consciousness for me. But I've also learned that other people, _even after understanding the above_ , still don't reject IIT. And you know what? Bully for them. On reflection, I firmly believe that a two-state solution is possible, in which we simply adopt different words for the different things that we mean by "consciousness"--like, say, consciousnessReal for my kind and consciousnessWTF for the IIT kind. OK, OK, just kidding! How about "paradigm-case consciousness" for the one and "IIT consciousness" for the other.

* * *

**Completely unrelated announcement:** Some of you might enjoy [this _Nature News_ piece](http://www.nature.com/news/theoretical-physics-complexity-on-the-horizon-1.15285) by Amanda Gefter, about black holes and computational complexity.
