---
title: "DeepMind and OpenAI achieve IMO Gold. What does it all mean?"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/deepmind-and-openai-achieve-imo-gold"
---

[](https://substackcdn.com/image/fetch/$s_!g0Ik!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0b71f560-8e59-4661-9823-a74b43d7f791_1536x1024.png)Drawing (and typo) by ChatGPT

The big news in AI in the last few days is that both [OpenAI](https://x.com/OpenAI/status/1946594928945148246) and [DeepMind](https://deepmind.google/discover/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/) have announced AI systems that achieved a score of 35 points out of 42 in the International Mathematical Olympiad, a score that would have earned a human contestant, among the world’s most mathematically gifted high school students, a gold medal.

Without question, these are impressive accomplishments. Exactly how impressive how much it matters for the future of the field is _much_ harder to say, particularly since neither company gives much detail about how their systems work.

Nonetheless we have dug to the extent that we can. Here, we’ll talk about what we can know now (including a tentative comparison of the two systems to the extent that details have been revealed), what we would like to know (about the details of their construction and training), and what may not be knowable for years: the ultimate significance of these results for math specifically and AI more generally.

DeepMind's system is an advanced version of Gemini Deep Think; we will abbreviate that to "Deep Think". OpenAI has not named their system; we will call it "OpenAI-IMO". 

## What Is the International Mathematical Olympiad (IMO)?

The [IMO](https://www.imo-official.org/) is a yearly international competition for mathematically gifted high school students. It began in 1959 and is one of the most prestigious student mathematical competitions at any level. In 2025, there were 630 contestants from 110 countries. Contestants qualify for the IMO by being the top scorers in preliminary national math contests.

The competition lasts for two days. Each day, a contestant is given three problems and has 4-1/2 hours to work on them. During the exam, they may not communicate with anyone and have nothing to use but pen and paper. Answers are graded by experts. Each question is graded on a scale of 0 to 7; thus a perfect score is 42.

Medals are awarded in terms of percentage rank rather than absolute score; typically, around 8% of the contestants get a gold medal, 17% get a silver, and 25% get a bronze. In 2025, 72 contestants got a gold medal; the cutoff score was 35 out of 42. Of that 72, 45 got exactly a score of 35, same as the programs. (The cutoff score for medals varies from one year to the next, reflecting the difficulty of the exam. In 2024, the cutoff score for a gold medal was 29 out of 42.) Five contestants achieved perfect scores of 42. 

Twenty-six contestants scored better than either program.

## How impressive is IMO gold-medal performance for an AI?

_Awfully_ impressive. To be able to solve math problems at the level of the top 67 high school students in the world is to have really good math problem solving chops. The problems range in difficulty from tough to nightmarishly tough.

A gold medal in the IMO is an accomplishment that even very successful mathematicians and scientists may well highlight on their CVs all their lives.

Both Deep Think and OpenAI-IMO got 35 points out of 42, getting perfect marks on problem 1-5 and 0 points for problem 6. Problem 6 was _much_ harder than the others; only 6 of the 630 contestants got a perfect score on that problem. (45 participants got 1 point of partial credit on problem 6 and 10 got between 2 and 5 points.)

Both new systems also outscore earlier systems like gemini-2.5-pro, o3 (high), o4-mini (high), Grok 4, and DeepSeek-R1-0528 as [reported in a test by “MathArena](https://matharena.ai/)”. None of them did well enough for even a bronze medal. (Gemini-2.5-pro did best by a considerable margin, with an average score of 13. None of the others had an average score above 7.) So OpenAI-IMO and Deep Think are much stronger than any of those. 

Last year, DeepMind [tested an earlier system](https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/), a combination of AlphaProof and AlphaGeometry2 , on IMO-2024. It scored 28/42, which last year (criteria vary each year) was the highest possible score for a silver medal. However, that version required the questions to be manually preprocessed and ran over the 4-1/2 hour time limit. This year, Deep Think took the exam under the same conditions as the human contestants. Presumably OpenAI-IMO did likewise, though OpenAI has not actually stated that. We can safely conclude that there has been significant progress.

§

That said, some of the hype has reached completely absurd levels.

OpenAI’s Sebastian Bubeck, for example, tweeted, “It may end up looking like a moon-landing moment for AI.”

[](https://substackcdn.com/image/fetch/$s_!t56A!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F09a31783-3fb5-46c2-96e5-e62945410df2_1849x704.png)

That’s simply preposterous. Being part of a 45-way tie for 27th place in a math contest for elite high school students is really not the kind of historic event that the moon landing was.

## Is this result significant for applications of AI to mathematical research?

Only time will tell. It is true that many top mathematicians did well on these kinds of contests in their youth. It’s also true that many top-notch mathematicians did not, and that many top scorers on the IMO ended up as competent but not stellar mathematicians. (Additionally, of course, many top scorers pursued other kind of careers.) The specific skills tested by IMO problems are sometimes useful in pursuing original mathematics, but they are far from the most important skills in original math research. As mathematician Kevin Buzzard [posted](https://leanprover.zulipchat.com/#narrow/channel/219941-Machine-Learning-for-Theorem-Proving/topic/Blind.20Speculation.20about.20IMO.202025/near/529569966) over the weekend; it’s hardly a sure thing that solving IMO problems will equate to direct progress in actual math research

[](https://substackcdn.com/image/fetch/$s_!s8MP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F151fd9ed-49a2-47fd-8c00-00db5e8d9267_1453x451.png)

Eric Schmidt’s recent [prediction](https://x.com/slow_developer/status/1946007007493804055?s=46) (made before IMO 2025), that there will be AI-based “world-class mathematicians” within a year, is pure fantasy. In the real world, only one theorem of middling importance (the [Robbins conjecture](https://en.wikipedia.org/wiki/Robbins_algebra)) has ever been proved autonomously by an AI system, and that was back in 1996. Tying for 27th place in a highly elite high school mathematics competition will not immediately change that.

## 

## **Design:**

Neither DeepMind nor OpenAI has given any substantial information about how their systems are designed and trained. No technical description of Deep Think has been published. Deep Mind has stated in its blog, “[W]e additionally trained this version of Gemini on novel reinforcement learning techniques that can leverage more multi-step reasoning, problem-solving and theorem-proving data. We also provided Gemini with access to a curated corpus of high-quality solutions to mathematics problems, and added some general hints and tips on how to approach IMO problems to its instructions.” That's pretty much all we know.

OpenAI has been equally closed-mouthed. They have stated that OpenAO is “ that it is an LLM doing next-token prediction (see the post from Sebastian Bubeck above); that it uses “new experimental general purpose techniques”; and that nothing in its design reflects a specific orientation toward mathematical reasoning.

Neither company has provided any information that explains why their systems work so much better than previous LLMs. Absent any information of that kind, there is little reason to take on faith that whatever unknown techniques allowed them to do so well on IMO problems will generalize to any other kind of problem.

## **Quality**

Though both Deep Think and OpenAI-IMO gave correct answers to IMO problems 1-5, Deep Think’s answers were better in two respects, one significant and the other very strange.

First, a _correct_ answer to a mathematical problem is not the same thing as a _good_ answer; and three of OpenAI-IMO’s answers, though correct, were significantly worse than Deep Think’s answers. This is most conspicuous in problem 2, a difficult Euclid-style geometry problem. Deep Think gave the kind of Euclid-style answer that the problem authors undoubtedly had in mind and that the human contestants undoubtedly produced. OpenAI-IMO simply translated the whole thing into a collection of algebraic constraints and gave an answer consisting of 300+ lines (not counting blank lines) of algebraic manipulations. OpenAI-IMO’s answer to problems 1 and 4 were also considerably longer and less well structured than Deep Think’s. This difference may reflect a limit in the OpenAI-IMO’s understanding. It certainly suggests that OpenAI-IMO would not make a very effective expositor of mathematical results.

Second: The proofs produced by Deep Think and by every single earlier LLM, whether correct or incorrect, are written in a smooth, elegant style. They could be cut and pasted into an journal article or into a textbook with little or no editing. The worst you can say of them is that they are sometimes verbose.

By contrast, OpenAI-IMO writes proofs in the style of an informal spoken presentation by a mathematician who is not very practiced or competent at giving informal presentations, and regularly mutters reassurances to themselves that they’re on the right track.

Here are two passages from the beginnings of the solutions to problem 4 to illustrate: first Deep Think then OpenAI-IMO. (The larger context is not important; the point is the difference in style.)

[](https://substackcdn.com/image/fetch/$s_!ftwW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3fc434d9-43a4-44e3-85bf-bcb1c8f3af23_1827x1164.png)Sample output from Deep Think

[](https://substackcdn.com/image/fetch/$s_!sCpa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa8949f8b-bc65-49ec-93c4-4a6985068446_1819x952.png)Sample output from OpenAI-IMO

To be clear: We’re not saying that OpenAI-IMO should have points deducted for this informal style. Obviously the IMO judges accept and grade as correct many human submissions that are not nearly as perfectly written as Deep Think’s; quite possibly they receive and give full marks to answers that are as scratchy in style as OpenAI-IMO’s. [OpenAI, it should be noted, did not submit their answers to IMO for formal review, but rather hired their own judges.] 

_Our point is just that the scratchy style is completely atypical of LLMs and suggests strongly that OpenAI-IMO is not simply a standard LLM, whatever it is_. That in turns raises questions about the claim that it can be applied across a wide range of fields in the way that we are used to from other LLMs.

## **Process**

DeepMind coordinated closely with the IMO administration. Deep Think was run under the supervision of the IMO and its answers were graded by the IMO. In compliance with the request of the IMO, DeepMind held off announcing its success until after the competition was over, so as not to overshadow the celebration of the human contestants, which is the IMO’s chief concern. They state in their blog that the system will be released, first to external testers, and then to Google AI Ultra subscribers.

In contrast, OpenAI communicated very little with the IMO prior to announcing their success. They administered the running of OpenAI-IMO themselves using some methodology that they have not fully described. They announced their success before the competition celebrations had ended. They have not made clear plans to release the system generally or make it available for experimentation. They have made it clear that it will not be available for months, even in the best case.

Many in the mathematical community have taken umbrage at their behavior. Terry Tao, who is universally acknowledged to be one of the greatest living mathematicians, and who in general has been very favorable toward the use of AI in mathematical research, posted [a statement](https://mathstodon.xyz/@tao/114881418225852441) decrying the fact that OpenAI has not made clear the methodology that it used in obtaining the results. His tweet concluded:

> "In the absence of a controlled test methodology that was not self-selected by the competing teams, one should be wary of making apples-to-apples comparisons between the performance of various AI models on competitions such as the IMO, or between such models and the human contestants.
> 
> Related to this, I will not be commenting on any self-reported AI competition performance results for which the methodology was not disclosed in advance of the competition."

That is to say, Tao is refusing to acknowledge (or even name) OpenAI and its accomplishment at all.

This reflects a general difference between the cultures of the two labs. DeepMind has a history of fruitful cooperation with mathematicians and scientists; AlphaFold is the most prominent result of that, but there have been several others. OpenAI has not made contributions to science on the same level.

## What information would be most useful in evaluating these systems?

In the hopes that these systems are someday released to outside review, here are some questions that we hope some day will be answered.

  * How do these systems work and how were they trained? What allows them to do so much better than earlier systems? Do they come with a cost in solving other sorts of problems? In the case of OpenAI-IMO, do the "new techniques" employed at all explain the stylistic weirdness?

  * What is the scope of these systems? Do they generalize to other kinds of mathematical problems, to scientific problems, to more general classes of problems? Or can they be extended to deal with these? Or would they be a useful component in a larger system that dealt with these?

  * What was the cost per problem, both for inference time (clearly high) and any domain-specific expertise required for training/augmentation etc and what would the economics of using these models be when it is released?

  * Are these system compatible with tools such as computational tools, coding, and web search?

  * What did the two systems do with problem 6, the one they couldn’t correctly answer? Did they give up, did they produce a partial answer that was in the right direction, or did they hallucinate a nonsensical answer?




Overall, the new work certainly might be exciting. Until outside scientists get to dig for a serious review we won’t really know for sure what it all means.

_Plot Twist and Update:_ As we were about to post this, we stumbled [on a report by Yichen Huang and Lin Yang](https://arxiv.org/abs/2507.15855) on how, using a multi-step protocol and prompt engineering, they were able to coax Gemini Pro 2.5 into answering 5 (the same 5) of the 6 IMO questions. In two cases, they had to include problem-specific hints in their prompts, which makes the result less clear-cut than the other two. However, the transparency and inclusion of actual detail in their report is delightful. 

It will be a while before all this settles out.

_**Ernest Davis** is Professor of Computer Science at NYU. In his junior year in high school, he placed sixth on the USA Math Olympiad; in his sophomore year of college, he had a top 5 finish in the Putnam exam._ _**Gary Marcus** , Professor Emeritus at NYU, is a scientist, author, and entrepreneur. His most recent book is Taming Silicon Valley. **Neither author has any affiliation with Google, OpenAI or the IMO.**_
