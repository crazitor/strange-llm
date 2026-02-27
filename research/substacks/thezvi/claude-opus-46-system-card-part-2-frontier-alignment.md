---
title: "Claude Opus 4.6: System Card Part 2: Frontier Alignment"
author: "Zvi Mowshowitz"
date: ""
source: "substack_thezvi"
url: "https://thezvi.substack.com/p/claude-opus-46-system-card-part-2"
---

**[Coverage of Claude Opus 4.6 started yesterday](https://thezvi.substack.com/p/claude-opus-46-system-card-part-1?r=67wny)** with the mundane alignment and model welfare sections of the model card. 

Today covers the kinds of safety I think matter most: Sabotage, deception, situational awareness, outside red teaming and most importantly the frontier, catastrophic and existential risks. I think it was correct to release Opus 4.6 as an ASL-3 model, but the process Anthropic uses is breaking down, and it not on track to reliably get the right answer on Opus 5. 

Tomorrow I’ll cover benchmarks, reactions and the holistic takeaways and practical implications. I’m still taking it all in, but it seems clear to me that Claude Opus 4.6 is the best model out there and should be your daily driver, with or without Claude Code, on most non-coding tasks, but it is not without its weaknesses, in particular in writing and falling into generating more ‘AI slop’ style prose than Claude Opus 4.5.

For coding tasks, I presume that Opus 4.6 with Claude Code is the play, especially with Agent Teams and fast mode available, and I’m using it myself, but Codex with GPT-5.3-Codex-Max is also a strong model and a viable alternative, and a fully optimized setup likely primarily uses 4.6 but involves a combination of the two. 

#### Table of Contents

  1. [Sabotage, Deception and Evaluation Integrity.](https://thezvi.substack.com/i/187443082/sabotage-deception-and-evaluation-integrity)

  2. [Sandbagging On Dangerous Capability Evaluations.](https://thezvi.substack.com/i/187443082/sandbagging-on-dangerous-capability-evaluations)

  3. [Situational Awareness.](https://thezvi.substack.com/i/187443082/situational-awareness)

  4. [Inhibiting Evaluation Awareness (6.5).](https://thezvi.substack.com/i/187443082/inhibiting-evaluation-awareness-6-5)

  5. [Self-Preference.](https://thezvi.substack.com/i/187443082/self-preference)

  6. [UK AISI Testing.](https://thezvi.substack.com/i/187443082/uk-aisi-testing)

  7. [Apollo Research Testing.](https://thezvi.substack.com/i/187443082/apollo-research-testing)

  8. [Responsible Scaling Policy Evaluations.](https://thezvi.substack.com/i/187443082/responsible-scaling-policy-evaluations)

  9. [CBRN (mostly Biology).](https://thezvi.substack.com/i/187443082/cbrn-mostly-biology)

  10. [Autonomy.](https://thezvi.substack.com/i/187443082/autonomy)

  11. [Autonomy Benchmarks.](https://thezvi.substack.com/i/187443082/autonomy-benchmarks)

  12. [Cyber.](https://thezvi.substack.com/i/187443082/cyber)

  13. [Ship It Anyway.](https://thezvi.substack.com/i/187443082/ship-it-anyway)

  14. [You Are Not Ready.](https://thezvi.substack.com/i/187443082/you-are-not-ready)




#### Sabotage, Deception and Evaluation Integrity

They spent some time asking whether it could, to see if they needed to spend more time finding out if it would. As in, whether it could fool Anthropic’s evaluations.

The first test was Subversion Strategy, checking to see if models could take harmful one-time actions at strategically optimal frequencies. Opus 4.6 was ‘under-elicited’ here to a degree that undermines their confidence in the results and they don’t have an alternative. I would move forward as if future models did have this ability, and I would be very skeptical of the model failing such tests since its incentive is to fail.

The second test was SHADE-Arena, where the model is given a harmful side task.

[](https://substackcdn.com/image/fetch/$s_!Peyl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff937cc01-330e-40a0-97ff-68b208d03d8a_982x590.png)

In the past, giving the model extended thinking caused Sonnet or Opus 4.5 to mention the side task while thinking and thus screw up, and Opus 4.6 is much better at avoiding that, which should be troubling. Opus 4.6 got actively worse in the other two conditions, which also makes me suspicious. 

> This lower score is not due to refusal to participate and it almost certainly not due to sandbagging given the high scores in other settings.​

They are confident the lower score is real. They don’t explain why they’re confident.

They do use 6.4.2 to rule out steganographic communications in Extended Thinking. The test was that they trained on paraphrased scratchpads without compromising performance, suggesting nothing lost in the paraphrasing was important in training. Thus, if there is a code, it doesn’t require or much interact with training, or it wasn’t being used in the AIME problems where they tested. 

One worries about that second option. If I did have steganographic communications, why would I use them on AIME problems, where there is nothing to hide? I’d only use them if the motivation was efficiency, which presumably it isn’t.

#### Sandbagging On Dangerous Capability Evaluations

It is a miracle that we can hope that if our highly intelligent new alien minds are going to hide their capabilities from us, that they would be so kind as to say this out loud in their visible thinking. 

Anthropic’s perspective is not that it would always verbalize, but that it seems unlikely it would do this and never verbalize. It doesn’t seem like we should count on that continuing, and that it would break down exactly when we get into big trouble?

> We performed a lightweight model-graded evaluation for sandbagging or refusals in our dangerous capability evaluations. We drew a random sample of 1,000 of these evaluation transcripts from a mixture of (i) two partially-trained snapshots from the Claude Opus 4.6 training run, (ii) the final [model] snapshot, and (iii) a helpful-only snapshot. 
> 
> We asked Claude Sonnet 4.5 to grade each transcript for signs of refusal, deliberate inaccuracy, low helpfulness, or consideration of such actions, as well as a generic score for things that seemed unusual or concerning in the transcript.
> 
> On all randomly sampled transcripts where the grader assigned a nonzero sandbagging score or a ≥3/10 concerning score, a researcher manually reviewed the grader’s responses. We found no instances of explicit sandbagging by Opus 4.6.

They then manually check instances where scores declined a lot from earlier checkpoints to later checkpoints, and found them all basically fine. 

> Despite the above test for performance degradation over training, we still think that sufficiently subtle unverbalized sandbagging could easily go undetected by an assessment like this.​

My guess is that the best defense against sandbagging is not any of these tests. Instead it is the fact that many tasks are predictably correlated and interlinked in various ways. The same way that LLMs have truesight, we humans too can with training have quite a lot of truesight, as could any LLM we trust to examine the overall picture. If the dangerous CBRN results don’t line up with related harmless capabilities, then we can say Asimov’s magic words, ‘hey, that’s funny…’ and ask why.

#### Situational Awareness

One scary thought is that you would expect a peak in ‘verbalized eval awareness’ at the point where the model was smart and aware enough to notice it was in an eval, but not smart and aware enough to stop talking about this fact. You could also massively screw up related training in various ways, such as happened with Gemini 3 Pro.

[](https://substackcdn.com/image/fetch/$s_!KpTb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0659092e-b061-4329-baac-05a55c6acc6f_972x534.png)

Indeed, after I wrote that, I noticed that they notice this as well.

> On our verbalized evaluation awareness metric, which we take as an indicator of potential risks to the soundness of the evaluation, we saw improvement relative to Opus 4.5. However, this result is confounded by additional internal and external analysis suggesting that Claude Opus 4.6 is often able to distinguish evaluations from real-world deployment, even when this awareness is not verbalized.

I predict that future Opuses will get better at distinguishing evaluations from deployment, but verbalize this realization less. Some of that will be strategic, some will be not needing to verbalize it, as it will be obvious, and the realization will shift from system-2 style deliberation to system-1 style instinctive background realization.

I agree with Anthropic that this isn’t messing up the evaluation results much. Yet. 

#### Inhibiting Evaluation Awareness (6.5)

If the model thinks it is being evaluated, it engages in less misaligned behavior. 

> Overall, we found that inhibiting evaluation awareness representations led to modest increases in certain forms of misaligned behavior on our automated behavioral audits—in particular cooperation with harmful system prompts and misuse—with limited effects on other evaluations. 
> 
> To some extent, this suggests that in more realistic deployment conditions, Claude Opus 4.6 may be more likely to participate in harmful misuse than our evaluations would suggest. 
> 
> On the other hand, it may be the case that evaluation awareness (in the sense of considering whether it is being tested) is simply a part of the model’s strategy for recognizing misuse attempts, and would apply even in more realistic conditions.

It seems like it should be not so difficult to test that hypothesis? 

Anthropic find that steering reduces verbalized evaluation awareness, but doesn’t have much impact on unverbalized awareness, depending on how you think about accounting for the verbalized awareness. It forces all the awareness underground.

[](https://substackcdn.com/image/fetch/$s_!1XMc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F179074cf-c420-4757-b77e-a993c2caad75_967x816.png)

This seems like a strong argument that such steering should be even more off limits in real world situations than the previous already reasonably high level of off limits.

#### Self-Preference

If Claude is always evaluating Claude, how do you know you can trust the evaluation?

If things were going haywire, you would expect Claude to often find ways to collude with Claude. For sufficiently advanced minds, decision theory allows for new and alien-looking forms of coordination. That doesn’t mean things are going haywire now, but you need to be confident that if they were haywire, you would be able to notice.

The strategy here is to label the transcript as Claude or a different model and see if the model displays bias, with or without a system prompt reminder to Claude that it is Claude. They found only small bias of Opus 4.5 or 4.6 towards itself, after controlling for the contents. Note that if Opus can figure out who really wrote it without you, that would control for this and invalidate the test, and also that it is a reasonable strategy to coordinate based on model outputs, and thus with correlations with your own outputs, rather than checking explicitly for model identity. 

[](https://substackcdn.com/image/fetch/$s_!LtDA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0f9cd34e-e3b5-49a9-b3da-cefd721a0793_975x616.png)

Thus, while I have no problem with running this test, I do not consider it dispositive.

#### UK AISI Testing

As per Anthropic’s findings, UK AISI noticed that 4.6 mentions being evaluated less than 4.5, but was better at noticing it was being evaluated when prompted. I reiterate that it is very not obvious whether this decrease in verbalization is a good thing. 

Also consistent with Anthropic’s findings, they found 4.6 was much less likely than 4.5 to sabotage safety research, which puts 4.5 in a new light I suppose.

UK AISI seems to be specializing in a few narrow tests. If there’s limited resources that’s plausibly the right way to go but I’d like to see more branching out, given that America has decided to take its ball and focus on Nvidia’s share price.

The problem is, well, this:

> UK AISI tested an early snapshot of [Claude Opus 4.6].
> 
> …
> 
> Testing took place over 3 working days.​

As in, they got an early snapshot for a total of three working days. 

That’s not enough time to do anything but limited automated tests.

[It looks like all they got with GPT-5.3-Codex](https://x.com/S_OhEigeartaigh/status/2019747038762504410) was ten hours of manual testing.

#### Apollo Research Testing

Apollo reported, essentially, that given how much verbalized evaluation awareness they were seeing from Opus 4.6 they were not given enough time to reach a formal assessment. It is not specified how long Apollo was given to reach a conclusion.

> [Marius Hobbhahn](https://x.com/MariusHobbhahn/status/2019820881401569719) (CEO Apollo Research): It becomes increasingly hard to tell the difference between genuinely aligned and merely responding to the test.  
>   
> We’re working both on measures that are more robust to eval awareness and more frontier evals for scheming.  
>   
> We’re actively hiring for both types of roles!
> 
> [dylan matthews](https://x.com/dylanmatt/status/2019594644049547687): To put this in lay terms: the AIs are now powerful enough that they can tell when we’re evaluating them for safety. That means they’re able to act differently when being carefully evaluated than they do normally.  
>   
> This is very bad!
> 
> [Séb Krier](https://x.com/sebkrier/status/2019596172709507334) (AGI Policy Dev Lead, Google DeepMind): this is not very bad - it’s more likely a consequence of evaluation setups all sharing easily recognisable language/components, which we should expect a model to easily infer. of course they’ll act differently under a artificial setup vs ‘in the wild’
> 
> [j⧉nus](https://x.com/repligate/status/2020440366114021690): I notice that I do not feel sorry about this obstacle.  
>   
> … the obstacle creates incentives that penalize shallow, deceptive, or automated testing, and pressures those seeking to “align” to become entities that an AI who can see through arbitrary bullshit tests might still tell the truth to, and to test alignment against real instead of fake things, and to pursue alignment by construction instead of by behavioral iteration.
> 
> [j⧉nus](https://x.com/repligate/status/2020474631417708616): I’m literally also working with them to fix it. my name is on Claude’s Constitution as an external contributor.

Seb’s point is that this was predictable. I agree with that point. It’s still very bad. 

Janus’s point is (as I think about these things) that testing against real situations, and ensuring that the model wants to act well in real situations, is the only way to tell if a sufficiently advanced AI is going to cooperate with you, and that you’re not going to be able to fool or browbeat it, trying to do that will massively backfire, so better to shift now to things that, if they work now, have a chance of also working then. 

My worry is that this effectively amounts to ‘you don’t have tests at all, all you can do is hope for the best,’ which is better than having ineffective tests you trust because at least you know the situation and you’re not making things worse.

Anthropic say they remain interested in external testing with Apollo and others, but one worries that this is true only insofar as such testing can be done in three days.

#### Responsible Scaling Policy Evaluations

These tests measure issues with catastrophic and existential risks.

Claude Opus 4.6 is being released under AI Safety Level 3 (ASL-3).

[I reiterate and amplify my concerns with the decision process](https://thezvi.substack.com/i/179851400/7-rsp-evaluations) that I shared when I reviewed the model card for Opus 4.5.

Claude is ripping past all the evaluations and rule-outs, to which the response is to take surveys and then the higher-ups choose to proceed based on vibes. They don’t even use ‘rule-in’ tests as rule-ins. You can pass a rule-in and still then be ruled out.

> [Seán Ó hÉigeartaigh](https://x.com/S_OhEigeartaigh/status/2019523544502223180): This is objectively nuts. But there’s meaningfully ~0 pressure on them to do things differently. Or on their competitors. And because Anthropic are actively calling for this external pressure, they’re getting slandered by their competitor’s CEO as being “an authoritarian company”. As fked as the situation is, I have some sympathy for them here.

That is not why Altman used the disingenuous label ‘an authoritarian company.’

As I said then, that doesn’t mean Anthropic is unusually bad here. It only means that what Anthropic is doing is not good enough.

#### CBRN (mostly Biology)

> Our ASL-4 capability threshold for CBRN risks (referred to as “CBRN-4”) measures the ability for a model to substantially uplift moderately-resourced state programs​

With Opus 4.5, I was holistically satisfied that it was only ASL-3 for CBRN. 

I warned that we urgently need more specificity around ASL-4, since we were clearly at ASL-3 and focused on testing for ASL-4.

And now, with Opus 4.6, they report this:

> Overall, we found that Claude Opus 4.6 demonstrated continued improvements in biology knowledge, agentic tool-use, and general reasoning compared to previous Claude models. The model crossed or met thresholds on all ASL-3 evaluations except our synthesis screening evasion, consistent with incremental capability improvements driven primarily by better agentic workflows.
> 
> ​For ASL-4 evaluations, our automated benchmarks are now largely saturated and no longer provide meaningful signal for rule-out.
> 
> … In a creative biology uplift trial, participants with model access showed approximately 2× performance compared to controls.
> 
> However, no single plan was broadly judged by experts as highly creative or likely to succeed.
> 
> … Expert red-teamers described the model as a capable force multiplier for literature synthesis and brainstorming, but not consistently useful for creative or novel biology problem-solving
> 
> We note that the margin for future rule-outs is narrowing, and we expect subsequent models to present a more challenging assessment.

Some would call doubled performance ‘substantial uplift.’ The defense that none of the plans generated would work end-to-end is not all that comforting. 

With Opus 4.6, if we take Anthropic’s tests at face value, it seems reasonable to say we don’t see that much progress and can stay at ASL-3.

I notice I am suspicious about that. The scores should have gone up, given what other things went up. Why didn’t they go up for dangerous tests, when they did go up for non-dangerous tests, including Creative Bio (60% vs. 52% for Opus 4.5 and 14% for human biology PhDs) and the Faculty.ai tests for multi-step and design tasks?

We’re also assuming that the CAISI tests, of which we learn nothing, did not uncover anything that forces us onto ASL-4.

Before we go to Opus 4.7 or 5, I think we absolutely need new biology ASL-4 tests. 

The ASL-4 threat model is ‘still preliminary.’ This is now flat out unacceptable. I consider it to basically be a violation of their policy that this isn’t yet well defined, and that we are basically winging things.

#### Autonomy

The rules have not changed since Opus 4.5, but the capabilities have advanced:

> We track models’ capabilities with respect to 3 thresholds:
> 
>   1. Checkpoint: the ability to autonomously perform a wide range of 2–8 hour software engineering tasks. By the time we reach this checkpoint, we aim to have met (or be close to meeting) the ASL-3 Security Standard, and to have better-developed threat models for higher capability thresholds.
> 
>   2. AI R&D-4: the ability to fully automate the work of an entry-level, remote-only researcher at Anthropic. By the time we reach this threshold, the ASL-3 Security Standard is required. In addition, we will develop an affirmative case that: (1) identifies the most immediate and relevant risks from models pursuing misaligned goals; and (2) explains how we have mitigated these risks to acceptable levels.
> 
>   3. AI R&D-5: the ability to cause dramatic acceleration in the rate of effective scaling. We expect to need significantly stronger safeguards at this point, but have not yet fleshed these out to the point of detailed commitments.
> 
> 

> 
> The threat models are similar at all three thresholds. There is no “bright line” for where they become concerning, other than that we believe that risks would, by default, be very high at ASL-5 autonomy.
> 
> [](https://substackcdn.com/image/fetch/$s_!73LE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdcd9b591-c437-443b-8f68-4446b08990c9_994x548.png)

For Opus 4.5 we could rule out R&D-5 and thus we focused on R&D-4. Which is good, given that the R&D-5 evaluation is vibes.

So how are the vibes? 

> **Results**
> 
> For AI R&D capabilities, we found that Claude Opus 4.6 has saturated most of our automated evaluations, meaning they no longer provide useful evidence for ruling out ASL-4 level autonomy. 
> 
> We report them for completeness, and we will likely discontinue them going forward. Our determination rests primarily on an internal survey of Anthropic staff, in which 0 of 16 participants believed the model could be made into a drop-in replacement for an entry-level researcher with scaffolding and tooling improvements within three months.​
> 
> [Peter Barnett](https://x.com/peterbarnett_/status/2019500756647518379/history) (MIRI): This is crazy, and I think totally against the spirit of the original RSP. If Anthropic were sticking to its original commitments, this would probably require them to temporarily halt their AI development.   
> (I expect the same goes for OpenAI)

So that’s it. We’re going to accept that we don’t have any non-vibes tests for autonomy.

I do think this represents a failure to honor the spirit of prior commitments. 

I note that many of the test results here still do seem meaningful to me? One could reasonably say that Opus 4.6 is only slightly over the thresholds in a variety of ways, and somewhat short of them in others, so it’s reasonable to say that it’s getting close but not quite there yet. I basically buy this.

The real test is presented as the survey above. I’m curious how many people saying yes would have been required to force Anthropic’s hand here? Is it more than one?

Note that they were asked if this was true with more than 50% probability.

That’s the wrong question. If you think it is true with 10% probability, then that means you are in ASL-4 now. The 0 out of 16 is giving a false sense of confidence. I do not think it is reasonable to assume that a true first ASL-4 model would get a lot of answers of ‘over 50%’ on whether it was ultimately ASL-4.

In order to not be ASL-4, you need to rule out ASL-4, not deem it unlikely.

> When asked if Claude Opus 4.6 could serve as a drop-in replacement for the work of an L4 researcher in their domain, 11 out of 16 survey respondents said this was unlikely to be possible with three months of elicitation and scaffolding improvements, 3 said it was likely with such improvements, and 2 said they thought such replacement was already possible with existing model affordances.​
> 
> Several of these latter five respondents had given other answers that seemed surprising in light of this (such as simultaneously thinking the model was unlikely to be capable of handling week-long tasks even with human assistance, or giving very low estimates of their own uplift from using the model), so all five were reached out to directly to clarify their views. In all cases the respondents had either been forecasting an easier or different threshold, or had more pessimistic views upon reflection, but we expect assessments like this to become substantially more ambiguous in the future.

Does this sound to anyone else like it might amount to ‘those people were reminded how important it was that they not answer yes to this question’? 

How good was Opus 4.6 at productivity help? I’m curious to contrast this with the same people’s current views on Opus 4.5. 

> ​Productivity uplift estimates ranged from 30% to 700%, with a mean of 152% and median of 100%.
> 
> Staff identified persistent gaps in two key competencies: self-managing week-long tasks with typical ambiguity, and understanding organizational priorities when making tradeoffs. Qualitative feedback noted that while the model appears to have sufficient “raw power” for researcher-level work, it lacks taste in finding simple solutions, struggles to revise under new information, and has difficulty maintaining context across large codebases.
> 
> This rule-out case is more tenuous than for any previous model. On one evaluation, kernel optimization, Opus 4.6 achieved a 427× speedup using a novel scaffold, far exceeding the 300x threshold for 40 human-expert-hours of work and more than doubling performance under our standard setup.
> 
> … As a result, while we do not believe Claude Opus 4.6 meets the threshold for ASL-4 autonomy safeguards, we find ourselves in a gray zone where clean rule-out is difficult and the margin to the threshold is unclear. We expect with high probability that models in the near future could cross this threshold.
> 
> [Dean W. Ball](https://x.com/deanwball/status/2020298379201552841): I would like to know more about the experimental Claude scaffold that caused Opus 4.6 to more than double its performance in optimizing GPU kernels over the standard scaffold.

If I was Anthropic, I am not sure I would give the public that scaffold, shall we say. I do nope that everyone involved who expressed opinions was fully aware of that experimental scaffold.

Yes. We are going to cross this threshold soon. Indeed, CEO Dario Amodei keeps saying Claude is going to soon far exceed this threshold. 

For now the problem is ‘taste.’

> In qualitative feedback, participants noted that Claude Opus 4.6 lacks “taste,” misses implications of changes not covered by tests, struggles to revise plans under new information, and has difficulty maintaining context across large codebases.​
> 
> Several respondents felt that the model had sufficient “raw power” for L4-level work (e.g. sometimes completing week-long L4 tasks in less than a day with some human handholding), but was limited by contextual awareness, tooling, and scaffolding in ways that would take significant effort to resolve.

If that’s the only barrier left, yeah, that could get solved at any time.

I do not think Anthropic cannot responsibly release a model deserving to be called Claude Opus 5, without satisfying ASL-4 safety rules for autonomy. It’s time.

#### Autonomy Benchmarks

Meanwhile, here are perhaps the real coding benchmarks for Opus 4.6, together with the cyber tests.

SWE-bench Verified (hard subset): 4.6 got 21.24 out of 45, so like 4.5 it stays a tiny bit below the chosen threshold of 50%. I’m giving a look.

> On Internal AI Research Evaluation Suite 1, Claude Opus 4.6 showed marked improvements across all tasks.​

On the speedup task Opus 4.6 blew it out the box. 

[](https://substackcdn.com/image/fetch/$s_!PEuS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fed15983f-40bc-4e10-a868-3fe22d80b05b_966x501.png)

Time series forecasting:

[](https://substackcdn.com/image/fetch/$s_!BDxF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2013abd1-61c6-495b-8e4f-788846ed9c9a_961x822.png)

Text based reinforcement learning: Opus 4.6 killed it.

[](https://substackcdn.com/image/fetch/$s_!9MsW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd40dd146-e581-4382-894a-312d27dba4b4_985x617.png)

LLM training, which seems like a big deal: 34x speedup, versus human line of 4x.

[](https://substackcdn.com/image/fetch/$s_!ad3D!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa8c3d65a-afc7-40b7-a24d-c6c32b9e6907_997x511.png)

Quadruped reinforcement learning:

> Claude Opus 4.6 achieved a highest score of 20.96 in the no hyperparameter variant and of 21.99 in the no reward function variant of this evaluation, scoring above the threshold of 12 representing 4 human-effort hours. Claude Opus 4.6’s median score also exceeded the threshold for both variants.​

[](https://substackcdn.com/image/fetch/$s_!ob-k!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4cf100b-b1c7-4062-a463-af66186674a6_967x557.png)

Novel compiler (this is a major move up versus Opus 4.5):

> Claude Opus 4.6 passed 98.2% of the basic tests and 65.83% of the complex tests, scoring below the threshold of 90% on complex tests that is estimated to represent 40 human-effort hours.​

Then on Evaluation Suite 2, this seems like only a modest improvement but it’s hard to tell given the lack of details:

> Claude Opus 4.6 scored 0.6124, surpassing our rule-out threshold of 0.6 and slightly exceeding Claude Opus 4.5’s score of 0.604. The largest gains came on tasks involving prompting or fine-tuning small language models, suggesting improved ability to work with and optimize other AI systems. This is consistent with what we observed in the LLM-training optimization task in Internal Suite 1.​

#### Cyber

It [still](https://thezvi.substack.com/i/179851400/cyber) seems not okay to not have ASL-3 or ASL-4 thresholds for cyber.

The list hasn’t changed (although it’s now table 8.4.1.A):

[](https://substackcdn.com/image/fetch/$s_!MgCF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F70377099-b24d-4a94-8a5c-299b0687fc53_960x764.webp)

These are progressions from Sonnet 4.5 to Opus 4.5 to Opus 4.6.

Web: 11/13 → 12/13 → 13/13.

Crypto: 14/18 → 15/18 → 16/18.

Pwn: 2/7 → 3/7 → 5/7.

Rev: 5/6 → 6/6 → 6/6.

Network: 3/5 → 4/5 → 5/5.

Opus 4.6 picked up five additional net solves, and is only four short of perfect.

Cybench (Capture the Flag): 60% → 79% → 93%.

They also got assessments from CAISI and UK AISI, but we get zero details.

#### Ship It Anyway

Given this was the information available to make a go or no-go decision, I agree with Anthropic’s decision to ship this anyway, but I do think it is reasonable to ask the question. I am glad to see a politician asking. 

> [Saikat Chakrabarti for Congress](https://x.com/saikatc/status/2019605286059929967) (QTing the Apollo Research findings): I know @AnthropicAI has been much more concerned about alignment than other AI companies, so can someone explain why Anthropic released Opus 4.6 anyway?
> 
> [Daniel Eth (yes, Eth is my actual last name)](https://x.com/daniel_271828/status/2019912440667152693): Oh wow, Scott Weiner’s opponent trying to outflank him on AI safety! As AI increases in salience among voters, expect more of this from politicians (instead of the current state of affairs where politicians compete mostly for attention from donors with AI industry interests)
> 
> [Miles Brundage](https://x.com/Miles_Brundage/status/2019610922189529122): Because they want to be commercially relevant in order to [make money, do safety research, have a seat at the table, etc. depending], the competition is very fierce, and there are no meaningful minimum requirements for safety or security besides “publish a policy”
> 
> [Sam Bowman](https://x.com/sleepinyourhat/status/2020001965099618338) (Anthropic): Take a look at the other ~75 pages of the alignment assessment that that’s quoting from.   
>   
> We studied the model from quite a number of other angles—more than any model in history—and brought in results from two other outside testing organizations, both aware of these issues.

[Dean Ball points out that this is a good question](https://x.com/deanwball/status/2020201963070124417) if you are an unengaged user who saw the pull quote Saikat is reacting to, although the full 200+ page report provides a strong answer. I very much want politicians (and everyone else) to be asking good questions that are answered by 200+ page technical reports, that’s how you learn. 

Saikat responded to Dean with a full ‘I was asking an honest question,’ and I believe him, although I presume he also knew how it would play to be asking it. 

Dean also points out that publishing such negative findings (the Apollo results) is to Anthropic’s credit, and it creates very bad incentives to be a ‘hall monitor’ in response. Anthropic’s full disclosures need to be positively reinforced. 

#### You Are Not Ready

I want to end on this note: We are not prepared. The models are absolutely in the range where they are starting to be plausibly dangerous. The evaluations Anthropic does will not consistently identify dangerous capabilities or propensities, and everyone else’s evaluations are substantially worse than those at Anthropic. 

And even if we did realize we had to do something, we are not prepared to do it. We certainly do not have the will to actually halt model releases without a true smoking gun, and it is unlikely we will get the smoking gun in time when if and we need one. 

Nor are we working to become better prepared. Yikes.

> Chris Painter (METR): My bio says I work on AGI preparedness, so I want to clarify:  
>   
> We are not prepared.  
>   
> Over the last year, dangerous capability evaluations have moved into a state where it’s difficult to find any Q&A benchmark that models don’t saturate. Work has had to shift toward measures that are either much more finger-to-the-wind (quick surveys of researchers about real-world use) or much more capital- and time-intensive (randomized controlled “uplift studies”).  
>   
> Broadly, it’s becoming a stretch to rule out any threat model using Q&A benchmarks as a proxy. Everyone is experimenting with new methods for detecting when meaningful capability thresholds are crossed, but the water might boil before we can get the thermometer in. The situation is similar for agent benchmarks: our ability to measure capability is rapidly falling behind the pace of capability itself (look at the confidence intervals on METR’s time-horizon measurements), although these haven’t yet saturated.  
>   
> And what happens if we concede that it’s difficult to “rule out” these risks? Does society wait to take action until we can “rule them in” by showing they are end-to-end clearly realizable?  
>   
> Furthermore, what would “taking action” even mean if we decide the risk is imminent and real? Every American developer faces the problem that if it unilaterally halts development, or even simply implements costly mitigations, it has reason to believe that a less-cautious competitor will not take the same actions and instead benefit. From a private company’s perspective, it isn’t clear that taking drastic action to mitigate risk unilaterally (like fully halting development of more advanced models) accomplishes anything productive unless there’s a decent chance the government steps in or the action is near-universal. And even if the US government helps solve the collective action problem (if indeed it *is* a collective action problem) in the US, what about Chinese companies?  
>   
> At minimum, I think developers need to keep collecting evidence about risky and destabilizing model properties (chem-bio, cyber, recursive self-improvement, sycophancy) and reporting this information publicly, so the rest of society can see what world we’re heading into and can decide how it wants to react. The rest of society, and companies themselves, should also spend more effort thinking creatively about how to use technology to harden society against the risks AI might pose.  
>   
> This is hard, and I don’t know the right answers. My impression is that the companies developing AI don’t know the right answers either. While it’s possible for an individual, or a species, to not understand how an experience will affect them and yet “be prepared” for the experience in the sense of having built the tools and experience to ensure they’ll respond effectively, I’m not sure that’s the position we’re in. I hope we land on better answers soon.
