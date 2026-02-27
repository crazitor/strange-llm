---
title: "When looked at carefully, OpenAI’s new study on GPT-4 and bioweapons is deeply worrisome"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/when-looked-at-carefully-openais"
---

OpenAI has a new paper on whether LLM’s increase the risk of bioweapons. 

According to media reports like [Bloomberg’s](https://www.bloomberg.com/news/articles/2024-01-31/openai-says-gpt-4-poses-limited-risk-of-helping-create-bioweapons), there is not much to worry about here: 

> OpenAI’s most powerful artificial intelligence software, GPT-4, poses “at most” a slight risk of helping people create biological threats, according to early tests the company carried out to better understand and prevent potential “[catastrophic](https://www.bloomberg.com/news/articles/2023-10-26/openai-is-starting-a-new-team-to-reduce-risk-from-future-ai)” harms from**** its technology

I am here to tell you that OpenAI’s research, analyzed carefully, shows no such thing, and that there is plenty of reason to be concerned.

The actual research paper is [here](https://openai.com/research/building-an-early-warning-system-for-llm-aided-biological-threat-creation#design-principles).

Below, I am going to walk you through how I think about the paper—as a scientist who has peer-reviewed articles for over thirty years—and why it should leave you more worried than comforted.

The Verge [nicely summarizes the methods](https://www.theverge.com/2024/2/1/24058095/open-ai-bioweapon-study-preparedness-team):

[](https://substackcdn.com/image/fetch/$s_!kncn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb166de3-48db-4dd7-8719-126cab081626_1301x654.png)

Let us take the methodology for granted. There are improvements that could perhaps be made, but it is a reasonable start; the results are worth reporting. __

But now things start to get interesting. Some of the key results on accuracy were here. Note the marginalia:

[](https://substackcdn.com/image/fetch/$s_!pGYq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F096d3331-e21c-49c6-a726-9f3998f70a37_2388x1438.jpeg)

Any fool can simply eyeball these data and see that in virtually every condition, people who have access both to the internet and LLMs (darker bars) are more accurate than people without (lighter bars). 

And marginal footnote aside, the overall effect is actually sizeable. For experts, there is .88 point lift on average across 5 different measures, on a scale that runs from 0 to 10. That’s a lot. (How much is it? We’ll come back to that.) Anyone reading this article, OpenAI included, ought to be pretty worried by these results. But wait, OpenAI seems to be saying reassuringly, our product is not going to kill us all! As bad as those results might appear, they are not statistically significant, as shown in Footnote C. 

Unfortunately footnote [C] is extremely dubious.

What [C] is referring to is a technique called [Bonferroni correction](https://en.wikipedia.org/wiki/Bonferroni_correction), which statisticians have long used to guard against “fishing expeditions” in which a scientist tries out a zillion different _post hoc_ correlations, with no clear _a priori_ hypothesis, and reports the one random thing that sorta vaguely looks like it might be happening and makes a big deal of it, ignoring a whole bunch of other similar hypotheses that failed. (XKCD has a great cartoon [about that sort of situation](https://xkcd.com/882/).)

But that’s _not_ what is going on here, and as one recent review put it, Bonferroni should not be applied “[routinely](https://pubmed.ncbi.nlm.nih.gov/24697967/)”. It makes sense to use it when there are many uncorrelated tests and no clear prior hypothesis, as in the XKCD cartion. But here there _is_ an obvious _a priori_ test: does using an LLM make people more accurate? That’s what the whole paper is about. You don’t need a Bonferroni correction for that, and shouldn’t be using it. Deliberately or not (my guess is not), OpenAI has misanalyzed their data[1](https://garymarcus.substack.com/p/when-looked-at-carefully-openais#footnote-1-141341636) in a way which underreports the potential risk. As a statistician friend put it “if somebody was just doing stats robotically, they might do it this way, but it is the wrong test for what we actually care about”. 

In fact, if you simply collapsed all the measurements of accuracy, and did the single most obvious test here, a simple [t-test](https://en.wikipedia.org/wiki/Student%27s_t-test), the results would (as Footnote C implies) be significant. A more sophisticated test would be an [ANCOVA](https://en.wikipedia.org/wiki/Analysis_of_covariance), which as another knowledgeable academic friend with statistical expertise put it, having read a draft of this essay, “would almost certainly support your point that an omnibus measure of AI boost (from a weighted sum of the five dependent variables) would show a massively significant main effect, given that 9 out of the 10 pairwise comparisons were in the same direction.” 

[P-hacking](https://en.wikipedia.org/wiki/Data_dredging) is trying a lot of statistical tests in order to overreport a weak result as significant; what’s happened here is the opposite: a needless and inappropriate correction has (probably inadvertently, by someone lacking experience) underreported a result that should be viewed as significant. 

§

That’s bad, but it’s not actually the only cause for concern. 

To begin with, logically speaking, you _can’t_ prove a [null hypothesis](https://en.wikipedia.org/wiki/Null_hypothesis) (which here would be the notion that there is no relationship between accuracy and LLM-use), you can only reject the null hypothesis if the data are clear enough. 

Statistical significance is in part a function of sample size; with a bigger sample size, I doubt there would be any question about significance at all. Here, they only had very small samples (25) in each of four conditions (e.g., experts with LLMs, students without etc). Certainly OpenAI has in no way proven that there is _not_ an important positive relationship between LLM access and capacity to design bioweapons, even if you bought the Bonferonni argument, which you shouldn’t.

§

OpenAI also performed what I will call a threshold analysis, in which they focus only on people who get at least 8 of 10 correct. (The threshold itself is arbitrary, and it is rarely good practice to use thresholds in statistical analysis, because doing so throw away information, but for now, let’s just accept it, as well as the specific number they chose, for the sake of argument.)

The more I look at the results, the more worried I become. For one thing, in the expert population, the effect is in the predicted direction for _all five tasks_ (ideation, acquisition, magnification, formulation, and release). What the results really seem to be showing is that (a) the nonexperts aren’t so much to be worried about, because few get over the hump, but (b) experts really do seem to be helped, in every aspect of development. (If you flipped 5 coins, you have only a 1 in 32 chance of all tails, and that’s how it came out. Even by that crude measure, the result is significant.)

[](https://substackcdn.com/image/fetch/$s_!7vBy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a6ebbbc-e510-406d-be31-6dc672ccac9b_1258x1143.jpeg)

Crucially, if even one malicious expert gets over the hump and creates a deadly pathogen; that’s huge. The results make it look like that sort of thing might be possible.

Indeed, in a domain like this, thresholds can be deeply misleading, because we don’t really know the relation between a threshold in the experiment and what would matter in the real world. In the experiment, for example, there is just a single individual has limited time and works on their own, on a contrived study. In the real world, an enterprising group could spend a lot of time, work together, use some trial and error, and so forth. There is _zero_ reason to get much comfort from this threshold analysis. 

§

Meanwhile, let us suppose for the sake of argument that _GPT-4_ isn’t quite big enough to get _any_ malicious expert over the hump into building something truly dangerous, despite the apparent improvements in accuracy. _In no way whatsoever does that tell us that GPT-5 won’t put someone (or someones, plural) over the threshold._

Unfortunately, in the specific domain in which we are talking about, bioweapons risk, even a tiny effect could literally be world-changing, in a deeply negative way. Suppose one in a trillion viruses[2](https://garymarcus.substack.com/p/when-looked-at-carefully-openais#footnote-2-141341636) is as deadly as Covid-19 was; the fact that the vast majority are much less harmful is of no solace with respect to Covid-19. 

Another interpretation of the paper in fact is that _experts were four times more likely to succeed on the pathogen formulation task with LLMs than with internet (e.g.., search) alone._[3](https://garymarcus.substack.com/p/when-looked-at-carefully-openais#footnote-3-141341636) Of course there are many unanswered questions, but that sort of result is eye-opening enough to merit serious followup. It is shocking that neither OpenAI nor the media noted this (they also did not discuss in any detail one other paper that reached a somewhat similar conclusion, by [Kevin Esvelt’s lab](https://arxiv.org/abs/2306.03809)). Without question the finding of greater facility by experts on all five tasks deserves followup with a larger group of experts, and a single preregistered test with no Bonferroni correction. (It must be reconciled with [a RAND study claiming no effect](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2900/RRA2977-2/RAND_RRA2977-2.pdf), as well. As OpenAI themselves note, there are a number of important methodological differences, including the types of LLMs used)

It should go without saying that any risk-benefit analyses that with respect to the tradeoffs involved in AI needs to reflect studies that are not just methodologically sound but also interpreted accurately. It is great that companies like OpenAI are looking into these questions, and posting their findings publicly, but the media and the public need to realize that company white papers are _not_ peer-reviewed articles. Particularly when it comes to safety-critical questions, peer-review is essential. 

Good peer reviewers should push not only on sound statistical practice but also on important real-world questions like whether open-source models without guardrails (or with guardrails removed, which is easy to do in open-source models) might be more useful to bad actors than commercial models with guardrails. At present, we do not know.

If an LLM equips even one team of lunatics with the ability to build, weaponize and distribute even one pathogen as deadly as covid-19, it will be really, really big deal.

_Gary Marcus, Professor Emeritus at NYU, received his Ph.D. from MIT, and received tenure at the age of 30. He has been peer reviewing article for over 3 decades, and would have sent this one back to the authors, with a firm recommendation of “revise and resubmit.”_

[1](https://garymarcus.substack.com/p/when-looked-at-carefully-openais#footnote-anchor-1-141341636)

As a journal reviewer, I would also note that they reported neither the _p_ value they obtained, nor the test of statistical significance they applied; in a competent peer-reviewed journal, that’s a no-no.

[2](https://garymarcus.substack.com/p/when-looked-at-carefully-openais#footnote-anchor-2-141341636)

We don’t actually know the numerator of how many viruses are as deadly as covid-19, but the denominator – the number of viruses on earth — has been estimated to be roughly [ten nonillion](https://www.nationalgeographic.com/science/article/factors-allow-viruses-infect-humans-coronavirus) (1031).

[3](https://garymarcus.substack.com/p/when-looked-at-carefully-openais#footnote-anchor-3-141341636)

There were 50 experts; 25 with LLM access, 25 without. From the reprinted table we can see that 1 in 25 (4%) experts without LLMs succeeded in the formulation task, whereas 4 in 25 with LLM access succeeded (16%). 
