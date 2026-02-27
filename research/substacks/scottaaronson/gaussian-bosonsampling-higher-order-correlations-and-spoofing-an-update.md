---
title: "Gaussian BosonSampling, higher-order correlations, and spoofing: An update"
author: "Scott Aaronson"
date: "Sun, 10 Oct 2021"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=5868"
---

In my [last post](https://scottaaronson.blog/?p=5859), I wrote (among other things) about an ongoing scientific debate between the group of Chaoyang Lu at USTC in China, which over the past year has been doing experiments that seek to demonstrate quantum supremacy via Gaussian BosonSampling; and the group of Sergio Boixo at Google, which had a [recent paper](https://arxiv.org/abs/2109.11525) on a polynomial-time classical algorithm to sample approximately from the same distributions.  I reported the facts as I understood them at the time.  Since then, though, a long call with the Google team gave me a new and different understanding, and I feel duty-bound to share that here.

A week ago, I considered it obvious that if, using a classical spoofer, you could beat the USTC experiment on a metric like total variation distance from the ideal distribution, then you would’ve completely destroyed USTC’s claim of quantum supremacy. The reason I believed _that_ , in turn, is a proposition that I hadn’t given a name but needs one, so let me call it **Hypothesis H** :

> The only way a classical algorithm to spoof BosonSampling can possibly do well in total variation distance, is by correctly reproducing the high-order correlations (correlations among the occupation numbers of large numbers of modes) — because that’s where the complexity of BosonSampling lies (if it lies anywhere).

Hypothesis H had important downstream consequences. Google’s algorithm, by the Google team’s own admission, does not reproduce the high-order correlations. Furthermore, because of limitations on both samples and classical computation time, Google’s paper calculates the total variation distance from the ideal distribution only on the marginal distribution on roughly 14 out of 144 modes. On that marginal distribution, Google’s algorithm does do better than the experiment in total variation distance. Google presents a claimed extrapolation to the full 144 modes, but eyeballing the graphs, it was far from clear to me what would happen: like, maybe the spoofing algorithm would continue to win, but maybe the experiment would turn around and win; who knows?

Chaoyang, meanwhile, made a clear prediction that the experiment would turn around and win, because of

  1. the experiment’s success in reproducing the high-order correlations,
  2. the admitted failure of Google’s algorithm in reproducing the high-order correlations, and
  3. the seeming impossibility of doing well on BosonSampling _without_ reproducing the high-order correlations (Hypothesis H).



Given everything my experience told me about the central importance of high-order correlations for BosonSampling, I was inclined to agree with Chaoyang.

Now for the kicker: it seems that Hypothesis H is false.  A classical spoofer could beat a BosonSampling experiment on total variation distance from the ideal distribution, without even bothering to reproduce the high-order correlations correctly.

This is true because of a combination of two facts about the existing noisy BosonSampling experiments.  The first fact is that the contribution from the order-k correlations falls off like 1/exp(k).  The second fact is that, due to calibration errors and the like, the experiments already show significant deviations from the ideal distribution on the order-1 and order-2 correlations.

Put these facts together and what do you find?  Well, suppose your classical spoofing algorithm takes care to get the low-order contributions to the distribution exactly right.  Just for that reason alone, it could already win over a noisy BosonSampling experiment, as judged by benchmarks like total variation distance from the ideal distribution, or for that matter linear cross-entropy.  Yes, the experiment will beat the classical simulation on the higher-order correlations.  But because those higher-order correlations are exponentially attenuated anyway, they won’t be enough to make up the difference.  The experiment’s lack of perfection on the low-order correlations will swamp everything else.

Granted, I still don’t know for sure that this _is_ what happens — that depends on whether I believe Sergio or Chaoyang about the extrapolation of the variation distance to the full 144 modes (my own eyeballs having failed to render a verdict!).  But I now see that it’s logically possible, maybe even plausible.

So, let’s imagine for the sake of argument that Google’s simulation wins on variation distance, even though the experiment wins on the high-order correlations.  In that case, what would be our verdict: would USTC have achieved quantum supremacy via BosonSampling, or not?

It’s clear what each side could say.

Google could say: by a metric that Scott Aaronson, the coinventor of BosonSampling, thought was perfectly adequate as late as last week — namely, total variation distance from the ideal distribution — we won.  We achieved lower variation distance than USTC’s experiment, and we did it using a fast classical algorithm.  End of discussion.  No moving the goalposts after the fact.

Google could even add: BosonSampling is a _sampling_ task; it’s right there in the name!  The only purpose of any benchmark — whether Linear XEB or high-order correlation — is to give evidence about whether you are or aren’t sampling from a distribution close to the ideal one.  But that means that, if you accept that we _are_ doing the latter better than the experiment, then there’s nothing more to argue about.

USTC could respond: even if Scott Aaronson _is_ the coinventor of BosonSampling, he’s extremely far from an infallible oracle.  In the case at hand, his lack of appreciation for the sources of error in realistic experiments caused him to fixate inappropriately on variation distance as the success criterion.  If you want to see the quantum advantage in our system, you have to deliberately subtract off the low-order correlations and look at the high-order correlations.

USTC could add: from the very beginning, the whole point of quantum supremacy experiments was to demonstrate a clear speedup on _some_ benchmark — we never particularly cared which one! That horse is out of the barn as soon as we’re talking about quantum supremacy at all — something the Google group, which itself reported the first quantum supremacy experiment in Fall 2019, again for a completely artificial benchmark — knows as well as anyone else. (The Google team even has experience with adjusting benchmarks: when, for example, [Pan and Zhang](https://arxiv.org/abs/2103.03074) pointed out that Linear XEB as originally specified is pretty easy to spoof for random 2D circuits, the most cogent rejoinder was: OK, fine then, add an extra check that the returned samples are sufficiently different from one another, which kills Pan and Zhang's spoofing strategy.) In that case, then, why isn’t a benchmark tailored to the high-order correlations as good as variation distance or linear cross-entropy or any other benchmark?

Both positions are reasonable and have merit — though I confess to somewhat greater sympathy for the one that appeals to my doofosity rather than my supposed infallibility!

OK, but suppose, again for the sake of argument, that we accepted the second position, and we said that USTC gets to declare quantum supremacy as long as its experiment does better than any known classical simulation at reproducing the high-order correlations.  We’d still face the question: does the USTC experiment, in fact, do better on that metric?  It would be awkward if, having won the right to change the rules in its favor, USTC still lost even under the new rules.

Sergio tells me that USTC directly reported experimental data only for up to order-7 correlations, and at least individually, the order-7 correlations are easy to reproduce on a laptop (although _sampling_ in a way that reproduces the order-7 correlations might still be hard—a point that Chaoyang confirms, and where further research would be great). OK, but USTC also reported that their experiment seems to reproduce up to order-19 correlations. And order-19 correlations, the Google team agrees, are hard to sample consistently with on a classical computer by any currently known algorithm.

So then, why don’t we have direct data for the order-19 correlations?  The trouble is simply that it would’ve taken USTC an astronomical amount of computation time.  So instead, they relied on a statistical extrapolation from the observed strength of the lower-order correlations — there we go again with the extrapolations!  Of course, if we’re going to let Google rest its case on an extrapolation, then maybe it’s only sporting to let USTC do the same.

You might wonder: why didn’t we have to worry about any of this stuff with the _other_ path to quantum supremacy, the one via random circuit sampling with superconducting qubits?  The reason is that, with random circuit sampling, all the correlations except the highest-order ones are completely trivial — or, to say it another way, the reduced state of any small number of output qubits is exponentially close to the maximally mixed state.  This is a real difference between BosonSampling and random circuit sampling—and even 5-6 years ago, we knew that this represented an advantage for random circuit sampling, although I now have a deeper appreciation for just how great of an advantage it is.  For it means that, with random circuit sampling, it’s easier to place a “sword in the stone”: to say, for example, _here_ is the Linear XEB score achieved by the trivial classical algorithm that outputs random bits, and lo, our experiment achieves a higher score, and lo, we challenge anyone to invent a fast classical spoofing method that achieves a similarly high score.

With BosonSampling, by contrast, we have various metrics with which to judge performance, but so far, for none of those metrics do we have a plausible hypothesis that says “ _here 's_ the best that any polynomial-time classical algorithm can possibly hope to do, and it’s completely plausible that even a noisy current or planned BosonSampling experiment can do better than that.”

In the end, then, I come back to the exact same three goals I would’ve recommended a week ago for the future of quantum supremacy experiments, but with all of them now even more acutely important than before:

  1. Experimentally, to increase the fidelity of the devices (with BosonSampling, for example, to observe a larger contribution from the high-order correlations) — a much more urgent goal, from the standpoint of evading classical spoofing algorithms, than further increasing the dimensionality of the Hilbert space.
  2. Theoretically, to design better ways to verify the results of sampling-based quantum supremacy experiments classically — ideally, even ways that could be applied via polynomial-time tests.
  3. For Gaussian BosonSampling in particular, to get a better understanding of the plausible limits of classical spoofing algorithms, and exactly how good a noisy device needs to be before it exceeds those limits.



Thanks so much to Sergio Boixo and Ben Villalonga for the conversation, and to Chaoyang Lu and Jelmer Renema for comments on this post. Needless to say, any remaining errors are my own.
