---
title: "On Dwarkesh Patel's 2026 Podcast With Dario Amodei"
author: "Zvi Mowshowitz"
date: ""
source: "substack_thezvi"
url: "https://thezvi.substack.com/p/on-dwarkesh-patels-2026-podcast-with"
---

Some podcasts are self-recommending on the ‘yep, I’m going to be breaking this one down’ level. This was very clearly one of those. So here we go.

[](https://substackcdn.com/image/fetch/$s_!ZU_a!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d49859d-6b3f-4c02-8b72-0f5697368baf_1418x837.png)

As usual for podcast posts, the baseline bullet points describe key points made, and then the nested statements are my commentary. Some points are dropped.

[If I am quoting directly I use quote marks, otherwise assume paraphrases](https://www.dwarkesh.com/p/dario-amodei-2).

What are the main takeaways?

  1. Dario mostly stands by his predictions of extremely rapid advances in AI capabilities, both in coding and in general, and in expecting the ‘geniuses in a data center’ to show up within a few years, possibly even this year.

  2. Anthropic’s actions do not seem to fully reflect this optimism, but also when things are growing on a 10x per year exponential if you overextend you die, so being somewhat conservative with investment is necessary unless you are prepared to fully burn your boats.

  3. Dario reiterated his stances on China, export controls, democracy, AI policy.

  4. The interview downplayed catastrophic and existential risk, including relative to other risks, although it was mentioned and Dario remains concerned. There was essentially no talk about alignment at all. The dog did not bark in the nighttime.

  5. Dwarkesh remains remarkably obsessed with continual learning.




#### Table of Contents

  1. [The Pace of Progress.](https://thezvi.substack.com/i/188060213/the-pace-of-progress)

  2. [Continual Learning.](https://thezvi.substack.com/i/188060213/continual-learning)

  3. [Does Not Compute.](https://thezvi.substack.com/i/188060213/does-not-compute)

  4. [Step Two.](https://thezvi.substack.com/i/188060213/step-two)

  5. [The Quest For Sane Regulations.](https://thezvi.substack.com/i/188060213/the-quest-for-sane-regulations)

  6. [Beating China.](https://thezvi.substack.com/i/188060213/beating-china)




#### The Pace of Progress

  1. AI progress is going at roughly Dario’s expected pace plus or minus a year or two, except coding is going faster than expected. His top level model of scaling is the same as it was in 2017.

     1. I don’t think this is a retcon, but he did previously update too aggressively on coding progress, or at least on coding diffusion.

  2. Dario still believes the same seven things matter: Compute, data, data quality and distribution, length of training, an objective function that scales, and two things around normalization or conditioning.

     1. I assume this is ‘matters for raw capability.’

  3. Dwarkesh asks about Sutton’s perspective that we’ll get human-style learners. Dario says there’s an interesting puzzle there, but it probably doesn’t matter. LLMs are blank slates in ways humans aren’t. In-context learning will be in-between human short and long term learning. Dwarkesh asks then why all of this RL and building RL environments? Why not focus on learning on the fly? 

     1. Because the RL and giving it more data clearly works?

     2. Whereas learning on the fly doesn’t work, even if it did what happens when the model resets every two months?

     3. Dwarkesh has pushed on this many times and is doing so again. 

  4. Timeline time. Why does Dario think we are at ‘the end of the exponential’ rather than ten years away? Dario says his famous ‘country of genuines in a data center’ is 90% within 10 years without biting a bullet on faster. One concern is needing verification. Dwarkesh pushes that this means the models aren’t general, Dario says no we see plenty of generalization, but the world where we don’t get the geniuses is still a world where we can do all the verifiable things.

     1. As always, notice the goalposts. Ten years from human-level AI is ‘long time.’ 

     2. Dario is mostly right on generalization, in that you need verification to train in distribution but then things often work well (albeit less well) out of distribution.

     3. The class of verifiable things is larger than one might think, if you include all necessary subcomponents of those tasks and then the combination of those subcomponents. 

  5. Dwarkesh challenges if you could automate an SWE without generalization outside verifiable domains, Dario says yes you can, you just can’t verify the whole company. 

     1. I’m 90% with Dario here. 

  6. What’s the metric of AI in SWE? Dario addresses his predictions of AI writing 90% of the lines of code in 3-6 months. He says it happened at Anthropic, and that ‘100% of today’s SWE tasks are done by the models,’ but that’s all not yet true overall, and says people were reading too much into the prediction. 

     1. The prediction was still clearly wrong.

     2. A lot of that was Dario overestimating diffusion at this stage.

     3. I do agree that the prediction was ‘less wrong,’ or more right, than those who predicted a lack of big things for AI coding, who thoughts things would not escalate quickly. 

     4. Dario could have reliably looked great if he’d made a less bold prediction. There’s rarely reputational alpha in going way beyond others. If everyone else says 5 years, and you think 3-6 months, you can say 2 years and then if it happens in 3-6 months you still look wicked smart. Whereas the super fast predictions don’t sound credible and can end up wrong. Predicting 3-6 months here only happens if you’re committed to a kind of epistemic honesty.

     5. I agree with Dario that going from 90% of code to 100% of code written by AI is a big productivity unlock, Dario’s prediction on this has already been confirmed by events. This is standard Bottleneck Theory.

  7. “Even when that happens, it doesn’t mean software engineers are out of a job. There are new higher-level things they can do, where they can manage. Then further down the spectrum, there’s 90% less demand for SWEs, which I think will happen but this is a spectrum.”

     1. It would take quite a lot of improved productivity to reduce demand by 90%. 

     2. I’d go so far as to say that if we reduce SWE demand by 90%, then we have what one likes to call ‘much bigger problems.’

  8. Anthropic went from zero ARR to $100 million in 2023, to $1 billion in 2024, to $9-$10 billion in 2025, and added a few more billion in January 2026. He guesses the 10x per year starts to level off some time in 2026, although he’s trying to speed it up further. Adoption is fast, but not infinitely fast.

     1. Dario’s predictions on speed of automating coding were unique, in that all the revenue predictions for OpenAI and Anthropic have consistently come in too low, and I think the projections are intentional lowballs to ensure they beat the projections and because the normies would never believe the real number.

  9. Dwarkesh pulls out the self-identified hot take that ‘diffusion is cope’ used to justify when models can’t do something. Hiring humans is much more of a hassle than onboarding an AI. Dario says you still have to do a lot of selling in several stages, the procurement processes are often shortcutted but still take time, and even geniuses in a datacenter will not be ‘infinitely’ compelling as a product. 

     1. I’ve basically never disagreed with a Dwarkesh take as much as I do here.

     2. Yes, of course diffusion is a huge barrier.

     3. The fact that if the humans knew to set things up, and how to set things up, that the cost of deployment and diffusion would be low? True, but completely irrelevant. 

     4. The main barrier to Claude Code is not that it’s hard to install, it’s that it’s hard to get people to take the plunge and install it, as Dario notes.

     5. In practice, very obviously, even the best of us miss out on a lot of what LLMs can do for us, and most people barely scratch the surface at best.

     6. A simple intuition pump: If diffusion is cope, what do you expect to happen if there was an ‘AI pause’ starting right now, and no new frontier models were ever created? 

     7. Dwarkesh sort of tries to backtrack on what he said as purely asserting that we’re not currently at AGI, but that’s an entirely different claim?

  10. Dario says we’re not at AGI, and that if we did have a ‘country of geniuses in a datacenter’ then everyone would know this.

     1. I think it’s possible that we might not know, in the sense that they might be sufficiently both capable and misaligned to disguise this fact, in which case we would be pretty much what we technically call ‘toast.’ 

     2. I also think it is very possible in the future that an AI lab might get the geniuses and then disguise this fact from the rest of us, and not release the geniuses directly, for various reasons.

     3. Barring those scenarios? Yes, we would know.




#### Continual Learning

It’s a Dwarkesh Patel AI podcast, so it’s time for continual learning in two senses.

  11. Dwarkesh thinks Dario’s prediction for today, from three years ago, of “We should expect systems which, if you talk to them for the course of an hour, it’s hard to tell them apart from a generally well-educated human” was basically accurate. Dwarkesh however is spiritually unsatisfied because that system can’t automated large parts of white-collar work. Dario points out OSWorld scores are already at 65%-70% up from 15% a year ago, and computer use will improve.

     1. I think it is very easy to tell, but I think the ‘spirit of the question’ is not so off, in the sense that on most topics I can have ‘at least as good’ a conversation with the LLM for an hour as with the well-educated human. 

     2. Can such a system automate large parts of white-collar work? Yes. Very obviously yes, if we think in terms of tasks rather than full jobs. If you gave us ten years (as an intuition pump) to adapt to existing systems, then I would predict a majority of current white-collar digital job tasks get automated.

     3. The main current barrier to the next wave of practical task automation is that computer use is still not so good (as Dario says), but that will get fixed.

  12. Dwarkesh asks about the job of video editor. He says they need six months of experience to understand the trade-offs and preferences and tastes necessary for the job and asks when AI systems will have that. Dario says the ‘country of geniuses in a datacenter’ can do that.

     1. I bet that if you took Claude Opus 4.6 and Claude Code, and you gave it the same amount of human attention to improving its understanding of trade-offs, preferences and taste over six months that a new video editor would have, and a similar amount of time training video editing skills, that you could get this to the point where it could do most of the job tasks. 

     2. You’d have to be building up copious notes and understandings of the preferences and considerations, and you’d need for now some amount of continual human supervision and input, but yeah, sure, why not.

     3. Except that by the time you were done you’d use Opus 5.1, but same idea. 

  13. Dwarkesh says he still has to have humans do various text-to-text tasks, and LLMs have proved unable to do them, for example on ‘identify what the best clips would be in this transcript’ they can only do a 7/10 job.

     1. If you see the LLMs already doing a 7/10 job, the logical conclusion is that this will be 9/10 reasonably soon especially if you devote effort to it.

     2. There are a lot of things one could try here, and my guess is that Dwarkesh has mostly not tried them, largely because until recently trying them was a lot slower and more expensive than it is now.

  14. Dwarkesh asks if a lot of LLM coding ability is the codebase as massive notes. Dario points out this is not an accounting of what a human needs to know, and the model is much faster than humans at understanding the code base.

     1. I think the metaphor is reasonably apt, in that in code the humans or prior AIs have written things down, and in other places we haven’t written similar things down. You could fix that, including over time. 

  15. Dwarkesh cites the ‘[the developers using LLMs thought they were faster but were went slower](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)’ study and asks where the renaissance of software and productivity benefits are from AI coding. Dario says it’s unmistakable within Anthropic, and cites that they’ve cut their competitors off from using Claude.

     1. Not letting OpenAI use Claude is a big costly signal that they view agentic coding as a big productivity boost, and even that theirs is a big boost over OpenAI’s versions of the same tools.

     2. It seems very difficult, watching the pace of developments in AI inside and outside of the frontier labs, to think coding productivity isn’t accelerating.

  16. Dario estimates current coding models give 15%-20% speedup, versus 5% six months ago, and that Amdhal’s law means you eventually get a much bigger speedup once you start closing full loops.

     1. It’s against his interests to come up with a number that small.

     2. I also don’t believe a number that small, especially since the pace of coding now seems to be largely rate limited by compute and frequency of human interruptions to parallel agents. It’s very hard to thread the needle and have the gains be this small.

     3. The answer will vary a lot. I can observe that for me, given my particular set of skills, the speedup is north of 500%. I’m vastly faster and better.

  17. Dwarkesh asks again ‘continual learning when?’ and Dario says he has ideas.

     1. There are cathedrals for those with eyes to see.




#### Does Not Compute

  18. How does Dario reconcile his general views on progress with his radically fast predictions on capabilities? Fast but finite diffusion, especially economic. Curing diseases might take years. 

     1. Diffusion is real but Dario’s answer to this, which hasn’t changed, has never worked for me. His predictions on impact do not square with his predictions on capabilities, period, and it is not a small difference. 

  19. Why not buy the biggest data center you can get? If Anthropic managed to buy enough compute for their anticipated demand, they burn the boats. That’s on the order of $5 trillion dollars two years from now. If the revenue does not materialize, they’re toast. Whereas Anthropic can ensure financial stability and profitability by not going nuts, as their focus is enterprise revenue with higher margins and reliability. 

     1. Being early in this sense, when things keep going 10x YoY, is fatal.

     2. That’s not strictly true. You’re only toast if you can’t resell the compute at the same or a better price. But yes, you’re burning the boats if conditions change.

     3. Even if you did want to burn the boats, it doesn’t mean the market will let you burn the boats. The compute is not obviously for sale, nor is Anthropic’s credit good for it, nor would the investors be okay with this.

     4. This does mean that Anthropic is some combination of insufficiently confident to burn the boats or unable to burn them. 

  20. Dario won’t give exact numbers, but he’s predicting more than 3x to Anthropic compute each year going forward.




#### Step Two

  21. Why is Anthropic planning on turning a profit in 2028 instead of reinvesting? “I actually think profitability happens when you underestimated the amount of demand you were going to get and loss happens when you overestimated the amount of demand you were going to get, because you’re buying the data centers ahead of time.” He says they could potentially even be profitable in 2026.

     1. Thus, the theory is that Anthropic needs to underestimate demand because it is death to overestimate demand, which means you probably turn a profit ‘in spite of yourself.’ That’s so weird, but it kind of makes sense.

     2. Dario denies this is Anthropic ‘systematically underinvesting in compute’ but that depends on your point of view. You’re underinvesting post-hoc with hindsight. That doesn’t mean it was a mistake over possible worlds, but I do think that it counts as underinvesting for these purposes.

     3. Also, Dario is saying (in the toy model) you split compute 50/50 internal use versus sales. You don’t have to do that. You could double the buy, split it 75/25 and plan on taking a loss and funding the loss by raising capital, if you wanted that.

  22. Dwarkesh suggests exactly doing an uneven split, Dario says there are log returns to scale, diminishing returns after spending e.g. $50 billion a year, so it probably doesn’t help you that much.

     1. I basically don’t buy this argument. I buy the diminishing return but it seems like if you actually believed Anthropic’s projections you wouldn’t care. As Dwarkesh says ‘diminishing returns on a genius could be quite high.’

     2. If you actually did have a genius in your datacenters, I’d expect there to be lots of profitable ways to use that marginal genius. The world is your oyster. 

     3. And that’s if you don’t get into an AI 2027 or other endgame scenario.

  23. Dario says AI companies need revenue to raise money and buy more compute. 

     1. In practice I think Dario is right. You need customers to prove your value and business model sufficiently to raise money.

     2. However, I think the theory here is underdeveloped. There is no reason why you couldn’t keep raising at higher valuations without a product. Indeed, see Safe Superintelligence, and see Thinking Machines before they lost a bunch of people, and so on, as Matt Levine often points out. It’s better to be a market leader, but the no product, all research path is very viable.

     3. The other advantage of having a popular product is gaining voice.

  24. Dwarkesh claims Dario’s view is compatible with us being 10 years away from AI generating trillions in value. Dario says it might take 3-4 years at most, he’s very confident in the ‘geniuses’ showing up by 2028. 

     1. Dario feels overconfident here, and also more confident than his business decisions reflect. If he’s that confident he’s not burning enough boats.

  25. Dario predicts a Cournot equilibrium, with a small number of relevant firms, which means there will be economic profits to be captured. He points out that gross margins are currently very positive, and the reason AI companies are taking losses is that each model turns a profit but you’re investing in the model that costs [10*X] while collecting the profits from the model that costs [X]. At some point the compute stops multiplying by 10 each cycle and then you notice that you were turning a profit the whole time, the economy is going to grow faster but that’s like 10%-20% fast, not 300% a year fast.

     1. I don’t understand what is confusing Dwarkesh here. I do get that this is confusing to many but it shouldn’t confuse Dwarkesh.

     2. Of course if we do start seeing triple-digit economic growth, things get weird, and also we should strongly suspect we will all soon die or lose control, but in the meantime there’ll be some great companies and I wouldn’t worry about Anthropic’s business model while that is happening.

  26. Dario says he feels like he’s in an economics class.

     1. Honestly it did feel like that. This is the first time in a long time it felt like Dwarkesh flat out was not prepared on a key issue, and is getting unintentionally taken to school (as opposed to when someone like Sarah Paine is taking us to school, but by design.)

  27. Dario predicts an oligopoly, not a monopoly, because of lack of network effects combined with high fixed costs, similar to cloud providers. 

     1. This is a bet on there not being win-more or runaway effects. 

     2. For a while, the battle had catch-up mechanics rather than runaway effects. If you were behind, you can distill and you can copy ideas, so it’s hard to maintain much of a lead.

     3. This feels like it is starting to change as RSI sets in. Claude is built by Claude Code, Codex is built by Codex, Google has to make its own choices and so on. The models are in many ways charged with training their successors.

     4. Also the cycle may be speeding up a la AI 2027. If you’re six months behind that used to be one generation behind. Now it is three. 

     5. And of course, once sufficiently powerful RSI (recursive self-improvement) sets in, and the models become sufficiently capable, that edge starts to translate into various other advantages far more readily. 

     6. Many fates are possible, but don’t rule out monopoly or winner-take-most.

  28. Dario points out different models have different comparative advantages, often in subtle ways. 

     1. True, but a sufficient lead would apply across the board. We’re not there right now, but we’re not that far from it either.

  29. Dario worried Silicon Valley and those connected to it could grow at 50% while everyone else grows at not much above the normal 2%. He says that would be ‘a pretty messed up world.’

     1. I think that turns out fine. You tax the part growing at 50%, everyone wins.

     2. That’s distinct from issues about the AI taking over, or the people in charge of the AI taking over, you still do have to dodge those problems. But if well-meaning humans are in control I don’t worry about distributional issues under extreme growth.

  30. Will robotics get solved soon after we get the ‘geniuses’? Dario says it doesn’t depend on learning like a human, there are many options, and it will happen, we will learn to control robots, and yes the robotics industry will then make trillions. It tacks on maybe a year or two to get going. 

     1. This seems obviously correct if you understand the premise, that we have the geniuses and the geniuses are playing nice for whatever reason.

     2. That premise is not obvious.

  31. Dwarkesh Patel keeps talking about continual learning, Dario Amodei keeps saying that we don’t need it.

     1. I agree with Dario. We don’t need it as such, if nothing else we can easily solve such problems already via [CENSORED].

  32. How should we price AGI? Dario thinks API is durable and will exist alongside other options, including forms of ‘pay for results.’

  33. How did Anthropic end up being the ones to build Claude Code? Dario encouraged experimentation internally, they used it internally, and then Dario said they should launch it externally.




#### The Quest For Sane Regulations

Finally, we ask about making AI ‘go well.’ With that framing you know that everyone is mostly conspicuously ignoring the biggest issues.

  34. Soon there will be lots of misaligned or crazy AIs running around. What to do? Dario correctly reiterates his dismissal of the idea that having a bunch of different AIs keeps them meaningfully in check. He points to alignment work, and classifiers, for the short run. For the long run, we need governance and some sort of monitoring system, but it needs to be consistent with civil liberties, and we need to figure this out really fast.

     1. We’ve heard Dario’s take on this before, he gives a good condensed version.

     2. For my response, see [my discussion of The Adolescence of Technology](https://thezvi.wordpress.com/2026/01/30/on-the-adolescence-of-technology/). I think he’s dodging the difficult questions, problems and clashes of sacred values, because he feels it’s the strategically correct play to dodge them.

     3. That’s a reasonable position, in that if you actively spell out any plan that might possibly work, even in relatively fortunate scenarios, this is going to involve some trade-offs that are going to create very nasty pull quotes.

     4. The longer you wait to make those trade-offs, the worse they get.

  35. Dwarkesh asks, what do we do in an offense-dominated world? Dario says we would need international coordination on forms of defense. 

     1. Yes. To say (less than) the least.

  36. Dwarkesh asks about Tennessee’s latest crazy proposed bill (it’s often Tennessee), which says “It would be an offense for a person to knowingly train artificial intelligence to provide emotional support, including through open-ended conversations with a user” and a potential patchwork of state laws. Dario (correctly) points out that particular law is dumb and reiterates that a blanket moratorium on all state AI bills for 10 years is a bad idea, we should only stop states once we have a federal framework in place on a particular question.

     1. Yes, that is the position we still need to argue against, my lord. 

  37. Dario points out that people talk about ‘thousands of state laws’ but those are only proposals, almost all of them fail to pass, and when really stupid laws pass they often don’t get implemented. He points out that there are many things in AI he would actively deregulate, such as around health care. But he says we need to ramp up the safety and security legislation quite significantly, especially transparency. Then we need to be nimble.

     1. I agree with all of this, as far as it goes.

     2. I don’t think it goes far enough.

     3. Colorado passed a deeply stupid AI regulation law, and didn’t implement it.

  38. What can we do to get the benefits of AI better instantiated? Dwarkesh is worried about ‘kinds of moral panics or political economy problems’ and he worries benefits are fragile. Dario says no, markets actually work pretty well in the developed world.

     1. Whereas Dwarkesh does not seem worried about the actual catastrophic or existential risks from AI.




#### Beating China

  39. Dario is fighting for export controls on chips, and he will ‘politely call the counterarguments fishy.’ 

  40. Dwarkesh asks, what’s wrong with China having its own geniuses? Dario says we could be in an offense-dominant world, and even if we are not then potential conflict would create instability. And he worried governments will use AI to oppress their own people, China especially. Some coalition with pro-human values has to say ‘these are the rules of the road.’ We need to press our edge.

     1. I am sad that this is the argument he is choosing here. There are better reasons, involving existential risks. Politically I get why he does it this way.

  41. Dario doesn’t see a key inflection point, even with his ‘geniuses,’ the exponential will continue. He does call for negotiation with a strong hand.

     1. This is reiteration from his essays. He’s flinching.

     2. There’s good reasons for him to flinch, but be aware he’s doing it.

  42. More discussion of democracy and authoritarianism and whether democracy will remain viable or authoritarianism lack sustainability or moral authority, etc. 

     1. There’s nothing new here, Dario isn’t willing to say things that would be actually interesting, and I grow tired.

  43. Why does Claude’s constitution try to make Claude align to desired values and do good things and not bad things, rather than simply being user aligned? Dario gives the short version of why virtue ethics gives superior results here, without including explanations of why user alignment is ultimately doomed or the more general alignment problems other approaches can’t solve. 

     1. If you’re confused about this see [my thoughts on the Claude Constitution](https://thezvi.substack.com/p/claudes-constitutional-structure). 

  44. How are these principles determined? Can’t Anthropic change them at any time? Dario suggests three sizes of loop: Within Anthropic, different companies putting out different constitutions people can compare, and society at large. He says he’d like to let representative governments have input but right now the legislative process is too slow therefore we should be careful and make it slower. Dwarkesh likes control loop two.

     1. I like the first two loops. The problem with putting the public in the loop is that they have no idea how any of this works and would not make good choices, even according to their own preferences.

  45. What have we likely missed about this era when we write the book on it? Dario says, the extent the world didn’t understand the exponential while it was happening, that the average person had no idea and everything was being decided all at once and often consequential decisions are made very quickly on almost no information and spending very little human compute.

     1. I really hope we are still around to write the book.

     2. From the processes we observe and what he says, I don’t love our chances.



