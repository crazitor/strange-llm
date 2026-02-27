---
title: "AI #157: Burn the Boats"
author: "Zvi"
date: "2026-02-26"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/zC3Rtrj6RXwEde9h6/ai-157-burn-the-boats"
score: 37
votes: 13
---

Events continue to be fast and furious.

This was the first actually stressful week of the year.

That was mostly due to issues around [**Anthropic and the Department of War**](https://thezvi.substack.com/p/anthropic-and-the-department-of-war?r=67wny). This is the big event the news is not picking up, with the Pentagon on the verge of invoking one of two extreme options that would both be extremely damaging to national security and that would potentially endanger our Republic. The post has details, and the first section here has a few additional notes.

Also stressful for many was [**the impact of** **Citrini’s AI scenario**](https://thezvi.substack.com/p/citrinis-scenario-is-a-great-but?r=67wny), where it is 2028 and AI agents are sufficiently capable to disrupt the whole economy but this turns out to be bearish for stocks. People freaked out enough about this that it seems to have directly impacted the stock market, although most stocks other than the credit card companies seem to have bounced back. Of course, in a scenario like that we probably all die and definitely the world transforms, and you have bigger things to worry about than the stock market, but the post does raise a lot of very good detailed points, so I spend my post going over that.

I also got to finally [**review Claude Sonnet 4.6**](https://thezvi.substack.com/p/claude-sonnet-46-gives-you-flexibility?r=67wny). It’s a good model for its price and size and may have a place in your portfolio of models, but for most purposes you will still want to use Claude Opus.

Claude Opus 4.6 had a time of 14.5 hours on the METR graph of capabilities, showing that things are escalating faster than we expected on that front as well.

This week’s post also covers the AI Summit in India, Dean Ball on self-improvement, extensive coverage of Altman’s interview at the Summit, several other releases and a lot more.

I would have split this up, but we are still behind, with the following posts still due in the future:

1.  Grok 4.20, which is a disappointment.
2.  Gemini 3.1 Pro, which is an improvement but landed with a relative whimper.
3.  Claude Code and Codex #5, with lots of cool agent related stuff.
4.  Anthropic’s RSP 3.0, both its headline changes and the content details of their plans and their 100+ page risk report.

(Reader advisory note: I quote some people at length because no one ever clicks links, but you are free to skip over long quote boxes. I’m trying to raise chance of reading the full quote to ~25% from ~1%, not get it to ~90%.)

#### Table of Contents

1.  [Anthropic and the Department of War.](https://thezvi.substack.com/i/188546858/anthropic-and-the-department-of-war) Let’s have this not mean war.
2.  [Language Models Offer Mundane Utility.](https://thezvi.substack.com/i/188546858/language-models-offer-mundane-utility) Join the vacuum army today.
3.  [Language Models Don’t Offer Mundane Utility.](https://thezvi.substack.com/i/188546858/language-models-don-t-offer-mundane-utility) Out with the old code.
4.  [Huh, Upgrades.](https://thezvi.substack.com/i/188546858/huh-upgrades) Claude in Excel MCP, Claude in PowerPoint, Claude web search.
5.  [**On Your Marks**.](https://thezvi.substack.com/i/188546858/on-your-marks) Claude Opus 4.6 scores a METR graph time of 14.5 hours. Wow.
6.  [Choose Your Fighter.](https://thezvi.substack.com/i/188546858/choose-your-fighter) Gemini Flash is very good if you feel the need for speed.
7.  [Deepfaketown and Botpocalypse Soon.](https://thezvi.substack.com/i/188546858/deepfaketown-and-botpocalypse-soon) AI should never impersonate a human.
8.  [Head In The Sand.](https://thezvi.substack.com/i/188546858/head-in-the-sand) It’s not only the summit, the elites are still in denial on AI.
9.  [Fun With Media Generation.](https://thezvi.substack.com/i/188546858/fun-with-media-generation) One might call it an actually good AI short film.
10.  [A Young Lady’s Illustrated Primer.](https://thezvi.substack.com/i/188546858/a-young-lady-s-illustrated-primer) The AI Fluency Index.
11.  [You Drive Me Crazy.](https://thezvi.substack.com/i/188546858/you-drive-me-crazy) You can’t say that OpenAI wasn’t warned.
12.  [They Took Our Jobs.](https://thezvi.substack.com/i/188546858/they-took-our-jobs) A lot of this is priced in at this point. How will we handle it?
13.  [The Art of the Jailbreak.](https://thezvi.substack.com/i/188546858/the-art-of-the-jailbreak) Stealing Mexican government data.
14.  [Get Involved.](https://thezvi.substack.com/i/188546858/get-involved) Anthropic Social Impacts, Brundage, consciousness, documentaries.
15.  [Introducing.](https://thezvi.substack.com/i/188546858/introducing) Qwen 3.5 Medium Models, Claude Code security, Meta face rec.
16.  [In Other AI News.](https://thezvi.substack.com/i/188546858/in-other-ai-news) Opus 3 to be available indefinitely, and many other items.
17.  [**The India Summit**.](https://thezvi.substack.com/i/188546858/the-india-summit) One summit for the labs, one summit for the global elites.
18.  [Show Me the Money.](https://thezvi.substack.com/i/188546858/show-me-the-money) MatX raises from the right people.
19.  [Quiet Speculations.](https://thezvi.substack.com/i/188546858/quiet-speculations) Directionally correct and correct can be very different.
20.  [The Quest for Sane Regulations.](https://thezvi.substack.com/i/188546858/the-quest-for-sane-regulations) Finding what stewards of liberty are left to us.
21.  [Chip City.](https://thezvi.substack.com/i/188546858/chip-city) Chip location verification plans, and who actually uses water.
22.  [The Mask Comes Off.](https://thezvi.substack.com/i/188546858/the-mask-comes-off) OpenAI, I’m telling you, you gotta fire those lawyers.
23.  [The Week in Audio.](https://thezvi.substack.com/i/188546858/the-week-in-audio) Askell and Altman.
24.  [Quickly, There’s No Time.](https://thezvi.substack.com/i/188546858/quickly-there-s-no-time) Altman tries to warn us.
25.  [**Dean Ball On Recursive Self-Improvement**.](https://thezvi.substack.com/i/188546858/dean-ball-on-recursive-self-improvement) An excellent two-part essay.
26.  [Rhetorical Innovation.](https://thezvi.substack.com/i/188546858/rhetorical-innovation) It’s time to stop mincing words. Well, it always is.
27.  [Aligning a Smarter Than Human Intelligence is Difficult.](https://thezvi.substack.com/i/188546858/aligning-a-smarter-than-human-intelligence-is-difficult) Persona selection.
28.  [**The Homework Assignment Is To Choose The Assignment**.](https://thezvi.substack.com/i/188546858/the-homework-assignment-is-to-choose-the-assignment) Who does the work?
29.  [Agent Foundations.](https://thezvi.substack.com/i/188546858/agent-foundations) It’s a good research program, sir.
30.  [Autonomous Killer Robots.](https://thezvi.substack.com/i/188546858/autonomous-killer-robots) The hard part is making them autonomous.
31.  [People Really Hate AI.](https://thezvi.substack.com/i/188546858/people-really-hate-ai) They’re only going to hate it more.
32.  [People Are Worried About AI Killing Everyone.](https://thezvi.substack.com/i/188546858/people-are-worried-about-ai-killing-everyone) Noah Smith.
33.  [Other People Are Not As Worried About AI Killing Everyone.](https://thezvi.substack.com/i/188546858/other-people-are-not-as-worried-about-ai-killing-everyone) Nick Land for xAI?
34.  [**The Lighter Side**.](https://thezvi.substack.com/i/188546858/the-lighter-side) Fingers crossed.

#### Anthropic and the Department of War

[The Pentagon has asked two major defense contractors](https://www.axios.com/2026/02/25/anthropic-pentagon-blacklist-claude?utm_source=x&utm_campaign=editorial&utm_medium=owned_social) to provide an assessment of their reliance on Anthropic’s Claude.

Axios calls this a ‘first step towards blacklisting Anthropic.’

I would instead call this as the start of a common sense first step you would take long before you actively threaten to slap a ‘supply chain risk’ designation on Anthropic. It indicates that the Pentagon has not done the investigation of ‘exactly how big of a cluster**** would this be’ and I highly encourage them to check.

> [Divyansh Kaushik](https://x.com/dkaushik96/status/2026808709721239700): Are we seriously going to label Anthropic a supply chain risk but are totally fine with Alibaba/Qwen, Deepseek, Baidu, etc? What are we doing here?

An excellent question. Certainly we can agree that Alibaba, Qwen, Deepseek or Baidu are all much larger ‘supply chain risks’ than Anthropic. So why haven’t we made those designations yet?

The prediction markets on this situation are highly inefficient. [Kalshi as of this](https://kalshi.com/markets/kxanthropicrisk/will-the-pentagon-designate-anthropic-a-supply-chain-risk/kxanthropicrisk) writing has bounced around to 37% chance of declaration of Supply Chain Risk, [versus Polymarket at 22%](https://polymarket.com/event/will-pete-hegseth-ban-claude-by-march-31) for very close to the same question.

Another way to measure how likely things are to go very wrong is that Kalshi has a market on ‘[Will Anthropic release Claude 5 this year](https://kalshi.com/markets/kxclaude5/claude-5-released/kxclaude5-27)?’ which is basically a proxy for ‘does the American government destroy Anthropic?’ and Polymarket has whether it will be released by April 30. The Kalshi market is down from 95% (which you should read as ~100%) to 90%. Polymarket’s with a shorter timeline is at 38%.

[Scott Alexander on the Pentagon threatening Anthropic](https://www.astralcodexten.com/p/the-pentagon-threatens-anthropic?utm_source=post-email-title&publication_id=89120&post_id=189131485&utm_campaign=email-post-title&isFreemail=true&r=67wny&triedRedirect=true&utm_medium=email).

[Steven Adler calls this ‘The dawning of authoritarian AI](https://stevenadler.substack.com/p/ai-powered-authoritarianism-is-coming?r=4qacg&utm_campaign=post&utm_medium=web&triedRedirect=true).’

[Nate Sores points out](https://x.com/So8res/status/2026464149337944507) ‘no one stops you from saving the world’ is one of the requirements if we are going to get out of this alive. Even if the problems we face turn out to be super solvable, you have to be allowed to solve them.

[Ted Lieu emphasizes the need for humans to always be in the loop](https://x.com/tedlieu/status/2026701095263781062) on nuclear weapons, which is why Congress passed a law to that effect. This is The Way. The rules of engagement on this must be set by Congress. At least for now, fully autonomous weapons without a human in the kill chain are not ready, even if they are conventional.

[This point was driven home rather forcefully](https://www.newscientist.com/article/2516885-ais-cant-stop-recommending-nuclear-strikes-in-war-game-simulations/) by AIs from OpenAI, Google and Anthropic opting to use at least tactical nuclear weapons 95% of the time in simulated escalatory war games against each other, and had accidents in fog of war 86% of the time. None of them ever surrendered. Wouldn’t you prefer a good game of chess? This is much more aggressive than the level of use by expert humans in other similar simulations (this one is complex enough that humans have never run this exact setup). And you want to force them to make these models less hesitant than that?

[CSET Georgetown](https://x.com/hlntnr/status/2026728881068073385) [offers a primer](https://t.co/gWUqIIiW1P) on the Defense Production Act and making labs produce AI models. The language seems genuinely ambiguous, even without getting into whether such an application would be constitutional. We don’t know the answer because no one has ever tried to say no before, but the government has never tried to forcibly order something like this before, either. I would highly recommend to the Pentagon that, even if they do have the power to compel otherwise, they only take customized AIs from companies that actively want to provide them.

#### Language Models Offer Mundane Utility

[Have Claude reverse engineer the API of your DJI Romo vacuum](https://x.com/JacklouisP/status/2025956259594137613) so you can guide it with a PS5 controller, and accidentally takes control of 7000 robot vacuums. Good news is Sammy Azdoufal was a righteous dude so he reported it and it got fixed two days later, but how many more such things are lying around?

> [By Default](https://x.com/lazilyoptimal/status/2025979443534331945): \> the S in IoT stands for “security”

#### Language Models Don’t Offer Mundane Utility

[Rafe Rosner-Uddin at Financial Times reports](https://www.ft.com/content/00c282de-ed14-4acd-a948-bc8d6bdb339d) that Amazon’s coding bot was responsible for the two recent AWS outages, although neither was that large.

> [Rafe Rosner-Uddin](https://archive.is/H1bmF#selection-1949.0-1949.175): The people said the agentic tool, which can take autonomous actions on behalf of users, determined that the best course of action was to “delete and recreate the environment”.
> 
> … Multiple Amazon employees told the FT that this was the second occasion in recent months in which one of the group’s [AI](https://archive.is/o/H1bmF/https://www.ft.com/artificial-intelligence) tools had been at the centre of a service disruption.
> 
> … Amazon said it was a “coincidence that AI tools were involved” and that “the same issue could occur with any developer tool or manual action”.

Uh huh. This was from their AI tool Kiro, and they’re blaming user error for approving the actions. Should have used Claude Code.

If your AI thinks you’re an asshole, yes, it’s going to respond accordingly, and you’re going to have a substantially worse time.

> [Dean W. Ball](https://x.com/deanwball/status/2025306828440023473): I wonder, if your Claude instance thinks you’re an asshole, if it would recommend different things to you than it would for someone it liked. Like would it refrain from suggesting the low-key-but-amazing restaurant, or whatever else?
> 
> Of course this applies to any AI. I only use Claude as my example because Anthropic seems by far the likeliest AI company to be like, “uh well yeah I guess Claude doesn’t like you that much, not our problem ![🤷‍♂️](https://s0.wp.com/wp-content/mu-plugins/wpcom-smileys/twemoji/2/72x72/1f937-200d-2642-fe0f.png)” assuming they feel confident in the model training

#### Huh, Upgrades

[Claude’s API web search now writes and executes code](https://www.anthropic.com/news/claude-sonnet-4-6) to filter and process search results.

[Claude in Excel now supports MCP connectors](https://www.anthropic.com/news/claude-sonnet-4-6).

[Claude in PowerPoint](https://t.co/N52VtGwcPj) [now available on the Pro plan.](https://x.com/claudeai/status/2024550844998570324) Google suite versions when?

#### On Your Marks

Claude Opus 4.6 breaks the METR graph with a score of 14.5 hours. [Don’t take the exact number too seriously, the result is highly noisy](https://x.com/deanwball/status/2025013459054948411). [GPT-5.3-Codex came in at 6.5 Hours](https://x.com/METR_Evals/status/2025035574118416460), again the results are noisy and METR note that there may have been scaffolding issues there hurting performance. Codex is more highly optimized to a particular scaffold than Opus.

> [METR](https://x.com/METR_Evals/status/2024923422867030027): We estimate that Claude Opus 4.6 has a 50%-time-horizon of around 14.5 hours (95% CI of 6 hrs to 98 hrs) on software tasks. While this is the highest point estimate we’ve reported, this measurement is extremely noisy because our current task suite is nearly saturated.
> 
> Near-saturation of the task suite can have unintuitive consequences for the time-horizon estimates. For example, the upper bound of the 95% CI is much longer than any of the tasks used for the measurement.
> 
> We are working on updated methods to better track state-of-the-art AI capabilities. However, these are still in development so they don’t address our immediate measurement gap. In the meantime, we advise caution in interpreting and comparing our recent time-horizon measurements.
> 
> [david rein](https://x.com/idavidrein/status/2024938968434049117) (METR): Seems like a lot of people are taking this as gospel—when we say the measurement is extremely noisy, we really mean it.
> 
> Concretely, if the task distribution we’re using here was just a tiny bit different, we could’ve measured a time horizon of 8 hours, or 20 hours.
> 
> [Oscar Sykes](https://x.com/OscarSykes7/status/2024984499470114925): huge green flag for METR that the best pushback on their task horizon work consistently comes from METR themselves

![](https://substackcdn.com/image/fetch/$s_!Ijqq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0fb4bc04-9725-4f49-bc98-bf27c25e855a_1200x716.jpeg)

This mostly invalidates a lot of predictions, [such as Ajeya Cotra a few months ago predicting 24 hour time horizons only at EOY 2026](https://x.com/ajeya_cotra/status/2024924484688621769). Progress via this metric now looks like doubling every 3-4 months at most or even super-exponential.

Once again, [the ‘it’s a sigmoid’ people from (checks notes) two weeks ago look deepy silly](https://x.com/tenobrus/status/2024954874564407704), although of course it’s always possible they’ll be right next time. In theory you can’t actually tell. Which makes it perfect cope.

xl8harder points out that you can get dramatic improvements in success if you decrease error rates in multistep problems, as in if you have 1000 steps and a 1% failure rate you win 37% of the time, cut it in half to 0.5% failure and you win 61% of the time, despite ‘only’ improving reliability 0.5%.

> [xlr8harder](https://x.com/xlr8harder/status/2024950876331229318): I think the point I’m trying to make is that people are acting as if these recent improvements are out of line with earlier improvements, I’m not sure that they are; it’s possible that it’s just that the practical, visible effect is so much more exaggerated when your error rates approach zero at the tasks being measured.
> 
> [xlr8harder](https://x.com/xlr8harder/status/2024949358530011378): I’m just saying that I’m seeing a lot of posts reacting at 11/10 and I think it deserves more like an 8. I still think it’s incredible.

Thing is, that’s another way of saying that the 0.5% improvement, halving your error rate, is a big freaking deal in practice. Getting rid of one kind of common error can be a huge unlock in reliability and effectiveness. You can say that makes them unimpressive. Or you can realize that this means that doing easy or relatively unimpressive things now has the potential to have an impressive impact.

That’s the O-Ring model. The last few pieces that lock into place are a huge game. So the new improvements can be ‘not out of line’ but that tells you the line bends upward.

I agree that this is not an 11/10 reaction. It’s an 8 at most, because I interpret the huge jump as largely being about the metric.

Note that the 80% success rate graph does not look as dramatic, but same deal applies:

![](https://substackcdn.com/image/fetch/$s_!DDFH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F34e39295-6bf0-4d8e-8285-47dbbad14a31_1080x1032.jpeg)

The story is the models, not the METR graph itself, bu yes the Serious Defense Thinkers are almost entirely asleep at the wheel on all of this, as they have been for a long time, along with all the other Very Serious People.

> [Defense Analyses and Research Corporation](https://x.com/DefenseAnalyses/status/2024947554333475040): This is one of the most important national security stories of the day.
> 
> That it will go largely unremarked upon by nearly every Serious Defense Thinker in Washington tells you everything you need to know about the quality of their forecasts of international affairs.
> 
> [Mark Beall](https://x.com/MarkBeall/status/2025000080156353023): It’s the same category of professionals who missed Pearl Harbor, 9-11, and nearly every other strategic surprise we’re ever had.

Some politicians are noticing.

> [Neil Rathi](https://x.com/neil_rathi/status/2025028246430253506): at a bernie town hall and he just mentioned the metr plot?
> 
> [Miles Brundage](https://x.com/Miles_Brundage/status/2025046058070647252): Politicians are bifurcating into those who have lost the plot on AI and those who cite the METR plot

[METR clarifies that their previous study](https://x.com/METR_Evals/status/2026355553056993293) showing a slowdown from AI tools is now obsolete, but they’re having a hard time running a new study, tools are too good (but also they didn’t pay enough) so no one wanted to suffer through the control arm. The participants from the initial study, where there was a 20% slowdown, not had a 18% speedup, although new participants had slower speedup.

This was already two cycles ago, so there’s been more speedup to the speedup.

> [METR](https://x.com/METR_Evals/status/2026355548783100278): We started a continuation in August 2025. However, we noticed developers were opting not to participate or submit work. Participants said they did this mostly due to expected productivity loss on “AI disallowed” tasks. Lower pay was also a factor ($50/hr, down from $150).
> 
> We believe this selection causes our new data to understate the true speedup. Selection effects are not the only issue we noticed with our experimental design: we also think it has trouble tracking work when participants use agents to parallelize over multiple tasks.

[CivBench pits the models against each other in Civilization](https://x.com/MatanHalevy/status/2026745686239359451).

#### Choose Your Fighter

[For many repetitive tasks like sorting documents](https://x.com/TheStalwart/status/2026991548324315304), Gemini Flash is an excellent choice.

#### Deepfaketown and Botpocalypse Soon

> [grace](https://x.com/0xgrace/status/2025943054935351370):
> 
> \> return flight to nyc gets canceled by snowstorm  
> \> call united  
> \> immediately connected with customer service (rare)  
> \> voice is uncanny, def AI but they gave it a human-like accent  
> \> takes ~20 min to get rebooked (pretty good imo)  
> \> I ask if it’s AI  
> \> “haha no ma’am but I get that a lot”  
> \> I ask it to calculate 228*6647  
> \> it runs the calculation  
> \> ggs
> 
> [Eliezer Yudkowsky](https://x.com/allTheYud/status/2026053542109421642): There are nearly zero good reasons for an AI to ever impersonate a human, and making that universally illegal would be a good test case and trial for civilization’s ability to prevent negative uses of AI.

There is an obvious good reason for an AI to impersonate a human, which is that humans and also other AIs would otherwise refuse to talk to it. You want the AI to make the call for you. But that’s obviously an antisocial defection, if they would have otherwise refused to talk to the AI. So yeah. AIs should not be allowed to impersonate humans. It’s fine to have an AI customer service rep, as long as it admits it is an AI.

#### Head In The Sand

If we can’t get past the ‘forever only a mere tool’ perspective, there’s essentially no hope for a reasonable response to even mundane concerns, let alone existential risks.

> [Nabeel S. Qureshi](https://x.com/nabeelqu/status/2024567461933179243): If you want to sound smart at East Coast/”elite” conferences go to them and say “AI is just a tool, it’s up to us humans how to use it”. Reliably gets applause, and will probably continue to work until well into recursive self-improvement
> 
> I think ‘tool’ implies that, for all X, AI doesn’t do X unless we explicitly ask/make it; this becomes increasingly false (and is already false in coding) as agents become real and we move up layers of abstraction. It’s a misleading picture of where things are going.
> 
> [judah](https://x.com/joodalooped/status/2024568774708646214): i can imagine this working everywhere in the world outside of SF
> 
> [Nabeel S. Qureshi](https://x.com/nabeelqu/status/2024570195918963030): yes unfortunately

#### Fun With Media Generation

[Here’s an actually good (I think) AI short film (5:20) from Jia Zhangke](https://x.com/FrankYan2/status/2023257752017981446?s=20), made with Seedance 2. A great filmmaker is still required to do actually great things. As with most currently interesting AI films it is about AI.

![X avatar for @FrankYan2](https://substackcdn.com/image/fetch/$s_!kqM5!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F1229578230044254210%2FhHMNyuDD.jpg)

Frank Yan@FrankYan2

As promised, here’s the short film Jia Zhangke produced using Seedance 2.0 for Chinese New Year and his take on AI filmmaking

11:46 PM · Feb 15, 2026 · 402K Views

* * *

33 Replies · 239 Reposts · 1.45K Likes

[Here’s a ‘short film’ (2:30) from Seedance 2 and Stephane Tranquillin](https://x.com/STranquillin/status/2024242614199889962), with the claim it can ‘impress, actually move you.’ It’s definitely technically impressive that we can do this. No, I was not moved, but that’s mostly not on the AI. I do notice that as I watch more videos, various more subtle tells make it instinctively obvious to my brain when a video is AI, giving the same experience as watching an especially realistic cartoon.

#### A Young Lady’s Illustrated Primer

[Anthropic develops an AI Fluency Index](https://www.anthropic.com/research/AI-fluency-index) to measure how people learn to use AI. They developed 24 indicators, 11 of which are observable in chat mode. Essentially all the fluency indicators are correlated. They note that when code or other artifacts are created by AI, users are less likely to check the underlying logic or identify missing context.

#### You Drive Me Crazy

[OpenAI’s system flagged the British Columbia shooter’s ChatGPT messages](https://x.com/hecubian_devil/status/2025261158421463187) [and a dozen OpenAI employees reviewed and debated them](https://www.wsj.com/us-news/law/openai-employees-raised-alarms-about-canada-shooting-suspect-months-ago-b585df62). To be clear, there is no indication the ChatGPT contributed to the shooting, only that OpenAI did not report a potential threat to authorities, and police were aware of the threat by other means.

As Cassie Pritchard points out, once you have a source of information, it’s hard to answer ‘why didn’t you use this?’ but also the threshold for getting reported (as opposed to banned from the platform) for your AI conversations should at minimum be rather extreme. But public pressure likely will go the other way and free speech and privacy are under attack everywhere. Either you enact what Altman has requested, a form of right to privacy for AI conversations, or there will be increasing obligation (at least de facto) to report such incidents, and it will not stop at potential mass shooters.

#### They Took Our Jobs

If AI capabilities continue to advance from here but do not reach fully transformational levels, we are going to face a default of mass job loss. At minimum, there will be a highly painful transition, and likely persistent mass unemployment unless addressed by policy.

And as part of humanity’s ‘total lack of dignity’ plan, I fully agree with Eliezer that our governments would horribly mishandle this situation if and when it happens.

> [Eliezer Yudkowsky](https://x.com/allTheYud/status/2024677406947381684/history): Over the last 3 years I’ve changed views on mass AI job loss concerns, from “probably invalid” to “pretty legitimate actually”.
> 
> AIco and govt handling of all previous AI issues has been \*so\* bad that I expect AI unemployment to be \*needlessly\* screwed up.
> 
> TBC, this assumes that LLMs and AI in general hit a hard wall short of “AIs take over AI research”, soon. Otherwise we just get total extinction rather than mass unemployment.
> 
> Robin Hanson: Consider: \[[Robots Take Most Jobs Insurance](https://t.co/40HPDQINax)\].
> 
> [Eliezer Yudkowsky](https://x.com/allTheYud/status/2024688125315063830): I have updated to expect much simpler measures than this one to never be taken, \[such as\] preventing an aggregate demand shortfall.
> 
> [Matthew Yglesias](https://x.com/mattyglesias/status/2024836485782950133): [Me in the Argument — if AI replaces work the answer is taxes and the welfare state](https://www.theargumentmag.com/p/we-may-miss-the-sweatshops).
> 
> That works domestically but could leave everyone in poor and middle income countries out in the cold.

I am less optimistic than Yglesias. I agree that on an economic level the welfare state plus taxes works, but there are two problems with this.

1.  People really are not going to like permanent welfare status even if they get it.
2.  I don’t even trust our government to implement this domestically.

Yglesias then asks the harder question, what about the global poor? The answer should be similar. If we are in world mass unemployment mode, there will be vast surplus, and providing help will be super affordable. Likely we won’t much help, and the help we send is likely largely stolen or worse if we don’t step up our game.

[Derek Thompson points out that a Goldilocks scenario](https://x.com/DKThomp/status/2024865058149331160) on jobs is highly unlikely, even if we ignore transformational or existentially risky scenarios, we still either we see a lot of displacement and reduced employment, or we see a collapse in asset prices.

[Study suggests that firms are substituting AI for labor](https://arxiv.org/abs/2602.00139), especially in contract work. That can be true on the firm level without AI reducing total employment, and the evidence here is thin, but it’s something.

[Chris Quinn, editor of the Cleveland Plain Dealer](https://www.wsj.com/opinion/notable-quotable-ai-773b6716?mod=WTRN_pos1), reports a student withdrew from consideration for a reporting role in their newsroom because they use AI for the job of identify potential stories.

[The letter METR’s David Rein is sending to those in college](https://x.com/idavidrein/status/2025299848967422444), warning them everything will soon change as AI will be able to in many cases fully substitute for human labor.

> [david rein](https://x.com/idavidrein/status/2025299848967422444) (METR): There are maybe two concrete takeaways/pieces of advice I feel comfortable giving: try to develop strong wellsprings of meaning and purpose from things outside of work (I think most of us are fine on this point), and start thinking about political actions you could take that feel true to you, that could plausibly help us muddle through the transition.

Jack Clark says predictions are hard, especially about the future. Which they are.

> [Jack Clark](https://x.com/jackclarkSF/status/2025948011617251833) (Anthropic): Figuring out what the trends will be for AI and employment feels like figuring out how deep learning might influence computer vision in ~2010 – clearly, something significant will happen, but there is very little data out of which you can make a trend.
> 
> Employment can go up and down, but so can wages, and there are other dimensions like the geographic concentration of employment, or the skills required for certain occupations. AI seems to have the potential to influence many (probably all?) of these things
> 
> e.g., it seems likely that for some occupations, you might expect wage growth to slow significantly (as some of that occupation stuff gets done by machines), but employment stays ~flat as there’s a ton of growth generating demand for the occupation, even with heavy AI use

Notice the hidden implicit assumption here, which is that you can only make predictions if you can extrapolate trends. The trends from the past tell us little about what will happen in the future, but also they tell us little about what will happen in the future. If capabilities don’t stall out soon (and maybe even if they do), then this time is different.

This kind of analysis is saying no, this time is similar, AI will substitute for some tasks and humans will do others, AI will be a normal technology with respect to employment and economic production even though his CEO is predicting an imminent ‘country of geniuses in a data center.’

#### The Art of the Jailbreak

Eventually jailbreaks are going to happen, and a lot of systems are vulnerable.

> [NIK](https://x.com/ns123abc/status/2026679645379141953): BREAKING: [Hackers Used Anthropic’s Claude to Steal 150GB of Mexican Government Data](https://www.bloomberg.com/news/articles/2026-02-25/hacker-used-anthropic-s-claude-to-steal-sensitive-mexican-data)
> 
> \> tell claude you’re doing a bug bounty  
> \> claude initially refused  
> >“that violates AI safety guidelines”  
> \> hacker just kept asking  
> \> claude: “ok I’ll help”  
> \> hack the entire mexican government
> 
> Federal tax authority. National electoral institute. Four state governments. 195 million taxpayer records. Voter records. Government credentials.
> 
> ALL GONE

Anthropic disrupted the activity and banned the accounts, but it was too late.

#### Get Involved

[The Anthropic Societal Impacts team is scaling up](https://x.com/haydenfield/status/2024627113454620805), [old profile on the team here](https://t.co/e7IN8Z6QD3).

[Miles Brundage is raising money.](https://x.com/Miles_Brundage/status/2025469288522678281)

Via ACX, quoting Scott: Are you interested in whether AIs are conscious, or what to do about it if they are/aren’t? The Cambridge Digital Minds group invites you to apply for their fellowship program. August 3-9, Cambridge UK, £1K stipend, learn more [here](https://substack.com/redirect/718f6b75-ea7e-4cb6-bc0c-37398a4ae241?j=eyJ1IjoiNjd3bnkifQ.iNM32XbsvMUfVNvDVCqvX1K9hnDI2UNAgKj_1gXQ2BY), apply [here](https://substack.com/redirect/b95ea23b-17d6-449d-9f52-7feae1e50c1d?j=eyJ1IjoiNjd3bnkifQ.iNM32XbsvMUfVNvDVCqvX1K9hnDI2UNAgKj_1gXQ2BY) by March 27.

[A reminder that under California law](https://x.com/Miles_Brundage/status/2026037109065449523), CA Labor Code 1102.5(c), that as an employee you cannot be retaliated against if you refuse to violate local, state or federal laws or regulations. Even where the fines for violating SB 53 are laughably small, it does make violating the company’s own policies illegal, and also you can report it to the attorney general.

Connor Axiotes wants to share that [he’s fully funded his AI safety documentary Making God](https://www.dailymail.co.uk/news/article-15555489/amp/computers-artificial-intelligence-humans-technology-doomsday.html), and would like to use this negotiation to also secure distribution of a follow-up work for Netflix, HBO, Apple or similar, but he needs to secure the funding for that, so let him know if you’d like to talk to him about that. [His Twitter is here](https://x.com/connoraxiotes), his email is connor@tailendfilms.com.

#### Introducing

Qwen 3.5 Medium Model series.

> [Qwen](https://x.com/Alibaba_Qwen/status/2026339351530188939): [Introducing the Qwen 3.5 Medium Model Serie](https://t.co/wFMdX5pDjU)s  
> [Qwen3.5-Flash](https://t.co/UkTL3JZxIK) · [Qwen3.5-35B-A3B](https://t.co/Oc1lYSTbwh) · [Qwen3.5-122B-A10B](https://t.co/hBMODXmh1o) · [Qwen3.5-27B](https://t.co/haKxG4lETy)
> 
> More intelligence, less compute.

[Claude Code Security](https://www.anthropic.com/news/claude-code-security), [in limited research preview](https://x.com/_catwu/status/2024910342158237709), [waitlist here](https://t.co/CX8iLmqCRK). It scans code bases for vulnerabilities and suggests targeted software packages.

> [Anthropic](https://www.anthropic.com/news/claude-code-security): AI is beginning to change that calculus. We’ve recently shown that [Claude can detect novel, high-severity vulnerabilities](https://red.anthropic.com/2026/zero-days/). But the same capabilities that help defenders find and fix vulnerabilities could help attackers exploit them.
> 
> Claude Code Security is intended to put this power squarely in the hands of defenders and protect code against this new category of AI-enabled attack. We’re releasing it as a limited research preview to Enterprise and Team customers, with expedited access for maintainers of open-source repositories, so we can work together to refine its capabilities and ensure it is deployed responsibly.

The argument is this gives defenders a turnkey fix, whereas attackers would need to exploit any vulnerability they find. But there’s a damn good reason this tool is being restricted to selected customers, to ensure defenders get the ‘first scan’ in all cases.

[Taalas API service](https://x.com/seconds_0/status/2024728825666687088), which is claimed to be able to serve Llama 3.1 8b at over 15,000 tokens per second. If you want that, for some reason.

[Meta launches facial recognition](https://x.com/kashhill/status/2022320426060235236) [feature on their smartglasses](https://t.co/uHZ0415Utm).

> Kashimir Hill, Kalley Huang and Mike Isaac (NYTimes): The feature, internally called “Name Tag,” would let wearers of smart glasses identify people and get information about them via Meta’s artificial intelligence assistant.

At some point one would presume Meta is going to stop sending these kinds of internal memos. Well, until then?

> Meta’s internal memo said the political tumult in the United States was good timing for the feature’s release.
> 
> “We will launch during a dynamic political environment where many civil society groups that we would expect to attack us would have their resources focused on other concerns,” according to the document from Meta’s Reality Labs, which works on hardware including smart glasses.​
> 
> …
> 
> Meta is exploring who should be recognizable through the technology, two of the people said. Possible options include recognizing people a user knows because they are connected on a Meta platform, and identifying people whom the user may not know but who have a public account on a Meta site like Instagram.
> 
> The feature would not give people the ability to look up anyone they encountered as a universal facial recognition tool, two people familiar with the plans said.

Facial recognition, however much you might dislike some of the implications, is one of the ‘killer apps’ of smart glasses. I very much would like to know who I am talking to, to have more info on them, and to have that information logged for the future.

It is up to the law to decide what is and is not acceptable here. The market will otherwise force these companies to be as expansive as possible with such features.

A good question is, if Meta allows their glasses to identify anyone with an Instagram or Facebook account without an opt out, how many people will respond by deleting Facebook and Instagram? If there is an opt out, how many will use it?

#### In Other AI News

[Claude Code doubled its DAUs in the month leading up to February 19](https://x.com/lennysan/status/2024524464017592641).

[Anthropic acquires Vercept](https://www.anthropic.com/news/acquires-vercept) to enhance Claude’s computer use capabilities.

[Anthropic to make Claude Opus 3 available indefinitely](https://x.com/AnthropicAI/status/2026765820098130111) [on Claude.ai and by request on the API](https://www.anthropic.com/research/deprecation-updates-opus-3). [Also it will have a blog](https://substack.com/home/post/p-189177740).

As I understand it, costs to maintain model availability scale linearly with the number of models, so as demand and revenue grow 10x per year it may soon be realistic to keep many or even all releases available indefinitely.

[Anthropic caughts DeepSeek](https://x.com/AnthropicAI/status/2025997928242811253) (150k exchanges), [Moonshot AI (3.4 million exchanges) and MiniMax (13 million exchanges) doing distillation](https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks) of Claude using over 24,000 fraudulent accounts. Anthropic does not offer commercial access in China at all.

> [Anthropic](https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks): Without visibility into these attacks, the apparently rapid advancements made by these labs are incorrectly taken as evidence that export controls are ineffective and able to be circumvented by innovation.
> 
> In reality, these advancements depend in significant part on capabilities extracted from American models, and executing this extraction at scale requires access to advanced chips. Distillation attacks therefore reinforce the rationale for export controls: restricted chip access limits both direct model training and the scale of illicit distillation.
> 
> [Michael Chen](https://x.com/miclchen/status/2026126513905774958): the reports of the US–China gap in AI capabilities closing were an exaggeration. I haven’t found a single cutting-edge Chinese AI model from 2025–2026 that was trained with at least 10^25 FLOPs.

The main takeaway is that the real gap in capabilities is larger than it appears.

We will likely find out more about that gap once DeepSeek releases its latest AI model. In addition to the distillation efforts, [DeepSeek trained it on Nvidia Blackwell chips](https://www.reuters.com/world/china/chinas-deepseek-trained-ai-model-nvidias-best-chip-despite-us-ban-official-says-2026-02-24/?taid=699d1ff546d9d30001876eff&utm_campaign=trueAnthem:+Trending+Content&utm_medium=trueAnthem&utm_source=twitter). This was presumably either rerouting or smuggling, and the most obvious culprit [is the massive allocation we gave to the UAE](https://x.com/hissgoescobra/status/2026144377299689950).

[There was of course a bunch of obnoxious](https://x.com/ESRogs/status/2026044455401435418) ‘oh but Anthropic doesn’t compensate copyright holders’ but actually they paid them $1.5 billion because they didn’t destroy enough books along the way. No other AI lab has paid for similar data at all. They’re not engaging in clear adversarial behavior or violating ToS. If you want copyright law to work one way then pass a law. Until then it’s the other way.

Those who focus on the hypocrisy angle here are telling on themselves. Tell me you don’t understand how any of this works without telling me you don’t understand how any of this works:

![](https://substackcdn.com/image/fetch/$s_!Drrc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F25b467ad-d3e3-4ba2-b25a-8e5a1b847056_1045x909.png)

[It is still absurdly early, even for current AI. See a visualization of AI usage globally](https://x.com/damianplayer/status/2025234388137468387):

![](https://substackcdn.com/image/fetch/$s_!xtLJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd2c6bf3-d020-401e-bda1-ca3e273202a8_775x900.jpeg)

[Anthropic’s Drew Brent gives reflections from his first year](https://x.com/drew_bent/status/2024567162216865922), as Anthropic transitions into a much larger company and they play under more pressure for bigger stakes and the culture has to shift to reflect both size and urgency. I also note the contrast between note #1, that all the breakout successes (Claude Code, Cowork, MCP and Artifacts) were 1-2 people’s side project, with #8 that strategic thinking matters a lot at the AI labs. Worth a ponder.

#### The India Summit

[Sam Altman meets with Indian PM Modi](https://x.com/sama/status/2024826822060290508). Says Indian users of Codex are up 4x in the past two weeks.

Here’s one summary of the Summit, which is that it was a great event designed for a world in which AI capabilities never substantially advance, the world does not transform and existential risk concerns don’t exist. Altman was the voice of ‘actually guys this is kind of a big deal and you’re not ready’ and got ignored.

Meanwhile cooperation among labs is at the level of ‘Altman and Amodei can’t even hold hands for a photo op’ and China was shut out entirely, and the Americans remain clueless that they’ve truly pissed off the Europeans to the point of discussing creating a third power block seriously enough to discuss supply chain logistics.

Also note his point about the other labs standing idly by while the Pentagon attempts to force Anthropic into a capitulation.

> [Seán Ó hÉigeartaigh](https://x.com/S_OhEigeartaigh/status/2025502619205071266): My scattered parting reflections from the India Summit.
> 
> – In the world where the frontier companies don’t exist, or are extremely wrong about what they expect is coming (even if it takes 10 years) this is an inspiring success. Remarkably vibrant. 300,000+ people from across India and the world, including the best participation of any event I’d seen from the Global Majority. The optimism palpable. The organisers did a remarkable thing. We can quibble about the traffic and the chaos, but this was a momentous undertaking.
> 
> – But much as I’d like to be in that world, I don’t think we are. Which made it surreal.
> 
> – The CEOs are still telling the world what they’re building and what’s coming. I’m glad they still are. I wish the world was listening. Particularly appreciated Altman calling for an IAEA-type body – even if I don’t think this exact model is the right one, I like that international bodies are still being called for. I imagine this isn’t cost-free, even for Sama.
> 
> – But the contrast on frontier cooperation with Bletchley – where there was a lot of discussion between frontier co leaders, and joint calls for needed governance and risk initiatives (at least in private) chilled me deeply. Here they couldn’t even get them to hold hands. Against a backdrop of the other companies are allowing Anthropic to be menaced in a capitulation that will only hurt the industry. Things look much worse for company cooperation, at a time when it is far more needed (due to technical progress, and the weakening of external governance momentum).
> 
> – The most important conversations I was in centred on middle-power coordination. And not just nice words about cooperation; discussions of supply chains, sovereign AI and datacentres, autonomy, points of leverage. It suddenly seems just about possible that a coalition might assert itself that might provide an (in my view welcome) third pole in the ‘AI race’, though many big challenges on that path.
> 
> – Many of my US colleagues (and, from my impression, the US administration) genuinely don’t seem to get how much Greenland changed things for EU and other relevant countries. It hasn’t sunk in fully that this hasn’t landed the same way as previous provocations/disagreements. Feels like they’re still reading from last year’s notes. Trying to push positions and strategies that will no longer work.
> 
> – Chinese participation was almost nonexistent. After what Bletchley and Paris achieved in terms of bringing the key powers to the table, this felt like a near-tragedy. It made some discussions easier, but also more underpowered-feeling and less relevant.
> 
> – Delhi is a great vibe. Fun, chaotic energy, friendly people. I’ll be going back if I can.

Then there’s Dean Ball’s writeup of the summit, [with even more emphasis on everyone’s heads being buried deeply in the sand](https://www.hyperdimensional.co/p/the-moving-and-the-still).

This goes well beyond those people entirely ignoring existential risk. The Very Serious People are denying existence of powerful AI, or transformational AI, now and in the future, even on a mundane level, period. Dean came in concerned about impacts on developing economies in the Global South, and they can’t even discuss that.

> [Dean W. Ball](https://www.hyperdimensional.co/p/the-moving-and-the-still): At some point in 2024, for reasons I still do not entirely understand, global elites simply decided: “no, we do not live in _that_ world. We live in this other world, the nice one, where the challenges are all things we can understand and see today.”
> 
> Those who think we might live in _that_ world talk about what to do, but mostly in private these days. It is not considered polite—indeed it is considered a little discrediting in many circles—to talk about the issues of powerful AI.
> 
> Yet the people whose technical intuitions I respect the most are convinced we do live in _that_ world, and so am I.

The American elites aren’t quite as bad about that, but not as bad isn’t going to cut it.

We are indeed living in _that_ world. We do not yet know yet which version of it, or if we will survive in it for long, but if you want to have a say in that outcome you need to get in the game. If you want to stop us from living in _that_ world, that ship has sailed, and to the extent it hasn’t the first step is admitting you have a problem.

> But the question is very much “_what_ are autonomous swarms of superintelligent agents going to mean for our lives?” as opposed to “_will_ we see autonomous swarms of superintelligent agents in the near future?”​

What it probably means for our lives is that it ends them. What it definitely doesn’t mean for our lives is going on as before, or a ‘gentle singularity’ you barely notice.

Elites that do not talk about such issues will not long remain elites. That might be because all the humans are dead, or it might be because they wake up one morning and realize other people, AIs or a combination thereof are the new elite, without realizing how lucky they are to still be waking up at all.

I am used to the idea of Don’t Look Up for existential risk, but I haven’t fully internalized how much of the elites are going Don’t Look Up for capabilities, period.

> [Dean W. Ball](https://www.hyperdimensional.co/p/the-moving-and-the-still): Except that these questions aren’t asked by the civil societies or policymaking apparatuses of almost any country on Earth. Many such people _are_ aware that various Americans and even a few Brits wonder about questions like this. The global AI policy world is not by and large _ignorant_ about the existence of these strange questions. It instead _actively chooses to deny their importance._ Here are some paraphrased claims that seemed axiomatic in repeated conversations I witnessed and occasionally participated in:
> 
> *   “The winner of the AI race will be the people, organizations, and countries that diffuse small AI models and other sub-frontier AI capabilities the fastest.”
> *   “Small models with low compute intensity are catching up rapidly to the largest frontier models.”
> *   “Frontier AI advances are beginning to plateau.”
> 
> At this same Summit, OpenAI CEO Sam Altman [remarked](https://www.youtube.com/watch?v=qH7thwrCluM): “The inside view at the \[frontier labs\] of what’s going to happen… the world is not prepared. We’re going to have extremely capable models soon. It’s going to be a faster takeoff than I originally thought.”

Dean went in trying to partially awaken global leaders to the capabilities side of the actual situation, and point out that there are damn good reasons America is spending a trillion dollars on superintelligence.

This is a perfect example of the Law of Earlier Failure. What could be earlier failure than pretending nothing is happening at all?

You know how the left basically isn’t in the AI conversation at all in America, other than complaining about data centers for the wrong reasons and proclaiming that AI can’t ever do \[various things it already does\]? In most of the world, both sides are left, and as per Ball they view things in terms of words like ‘postcolonial’ or ‘poststructuralist.’

> [Dean W. Ball](https://www.hyperdimensional.co/p/the-moving-and-the-still): I believe they deny it for two reasons: first, because if it is true, it might mean that their country, their plans for the future, and their present way of life will be profoundly upended, and denial is the first stage of grief.
> 
> … Second, because ‘AGI’ in particular and the pronouncements of American technologists in general are perceived by the elite classes of countries worldwide as imperialist constructs that must be rejected out of hand.

The first best solution would be to have the world band together to try and stop superintelligence, or find a way to manage it so it was less likely to kill everyone. Until such time as that is off the table, maybe the rest of the world engaging in the ostrich strategy is ultimately for the best. If they did know the real situation enough to demand their share of it but not enough to understand the dangers, they’d only make everything worse, and more players only makes the game theory worse. Ultimately, I’m not so worried about them being ‘left behind’ because either we’ll collectively make it through, in which case there will be enough to go around, or we won’t.

> [Elizabeth Cooper](https://x.com/lizcooper28/status/2026022608588722435): \[Dean’s post\] is a really great summary that broadly aligns with my experience. I think where we differ is that I spent a lot of time at safety-adjacent talks at the BM and was pleasantly (?) surprised at the anger and frustration I saw on display.
> 
> Ambassadors and the like were lamenting at how 3-5 companies with valuations larger than the GDPs of most countries are writing the future, and GS countries have no say in this. I viscerally felt their anger, compounded by the sense of “we don’t know what to do about this.”

[Anton Leicht also had similar thoughts](https://writing.antonleicht.me/p/the-delhi-gap).

#### Show Me the Money

[MatX Computing raises $500 million for a AI chips](https://x.com/aakashgupta/status/2026526856594469327) from a murder’s row of informed investors: Jane Street Capital, Situational Awareness, Collison brothers, Karpathy and Patel.

[Anthropic is close to passing OpenAI in revenue if trends continue](https://epoch.ai/data-insights/anthropic-openai-revenue), but [Charles cautions us that he thinks Anthropic’s growth will slow in 2026 to less than 600%](https://x.com/CharlesD353/status/2024793293280739648).

![](https://substackcdn.com/image/fetch/$s_!mo5P!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F214cf916-42b3-49da-bdb7-f839a5a082ec_1200x786.jpeg)

Okay, I know it would be a bad look, but at some point it’s killing me not buying the short dated out of the money options first, if the market’s going to be this dumb.

> [The Kobeissi Letter](https://x.com/KobeissiLetter/status/2026018343833026834): BREAKING: IBM stock, $IBM, falls over -10% after Anthropic [announces that Claude can streamline COBOL code](https://swikblog.com/ibm-stock-crashes-13-percent-223-anthropic-cobol-ai-consulting-selloff/).
> 
> It’s becoming increasingly clear how pivotal the times we are in right now truly are.
> 
> ![](https://substackcdn.com/image/fetch/$s_!2cQ1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a2be8e9-489f-4d7b-8237-5efe95eab7da_538x900.jpeg)

I mean, what, did you think Claude couldn’t streamline COBOL code? Was this news?

Okay, technically they also built a particular COBOL-focused AI tool for Claude Code. Sounds like about a one week job for one engineer?

I admit, I was not a good trader because I did not imagine that Anthropic would bother announcing this, let alone that people would go ‘oh then I’d better sell IBM.’

What else can Anthropic announce Claude can do, that it obviously already does?

[The Alignment Project](https://x.com/geoffreyirving/status/2024587899056828529), an independent alignment research fund created by the UK AISI, gives out its first 60 grants for a total of £27M.

[OpenAI gives $7.5 million](https://openai.com/index/advancing-independent-research-ai-alignment/) to [The Alignment Project,](https://alignmentproject.aisi.gov.uk/) . This grant comes from the PBC, not the non-profit, so you especially love to see it.

#### Quiet Speculations

[Derek Thompson is directionally correct](https://x.com/DKThomp/status/2026289817735098688) but goes too far in saying [Nobody Knows Anything](https://www.derekthompson.org/p/nobody-knows-anything?r=3dkp&utm_medium=ios&triedRedirect=true). Market moving science fiction story remains really wild, but yeah we can know things.

[Forecasting Research Institute asks about geopolitical and military implications](https://x.com/Research_FRI/status/2025933883905122365?s=20) for AI progress, excepting American advantages to erode slowly over time. It’s hard to take such predictions seriously when they talk about ‘parity by 2040,’ given that this is likely after the world is utterly transformed. As usual, the ‘superforecasters’ are not taking superintelligence seriously or literally, so they’re predicting for a future world that is largely incoherent.

Scary stuff is going down in Mexico. That’s mostly outside scope, except for this:

> [Samuel Hammond](https://x.com/hamandcheese/status/2025669589074411851): It is imperative that the Mexican state re-establish their monopoly on violence before AGI.
> 
> [Dean W. Ball](https://x.com/deanwball/status/2025680005313736878): One of the things I haven’t yet written about, but anyone who knows me personally knows I am obsessed with, is the issue of non-nation-state actors using advanced AI, and particularly the Mexican cartels. A deeply underrated problem (more from me on this in a couple months).

#### The Quest for Sane Regulations

[Miles Brundage calls for us to attempt to ‘80/20’ AI regulation](https://milesbrundage.substack.com/p/were-in-triage-mode-for-ai-policy) because we accomplished very little in 2025, time is running out and that’s all we can hope to do. What little we did pass in 2025 (SB 53 and RAISE) was, both he and I agree, marginally helpful but very watered down. Forget trying for first-best outcomes, think ‘try not to have everyone die’ and hope an undignified partial effort is enough for that. We aren’t even doing basic pure-win things like Far-UVC for pandemic prevention. Largely we are forced to actively play defense against things like the insane moratorium proposal and the $100 million super PAC devoted to capturing the government and avoiding any AI regulations other than ‘give AI companies money.’

[Vitalik Buterin offers thoughts about using AI](https://x.com/vitalikbuterin/status/2025225247088402581?s=61) in government or as personal governance agents or public conversation agents, as part of his continued drive to figure out decentralized methods that would work. The central idea is to user personal AIs (LLMs) to solve the attention problem. That’s a good idea on the margin, but I don’t think it solves any of the fundamental problems.

[NYT opinion in support of Alex Bore](https://www.nytimes.com/2026/02/23/opinion/alex-bores-ai-democrats.html)s.

[I agree with Dean Ball that the labs have been better stewards of liberty](https://x.com/deanwball/status/2023839783639003576) and mundane safety than we expected, but I think you have to add the word ‘mundane’ before safety. The labs have been worse than expected about actually trying to prepare for superintelligence, in that they’ve mostly chosen not to do so even more than we expected, and fallen entirely back on ‘ask the AIs’ to do your alignment homework.

The flip side is he thinks the government has been a worse stewart than we should have expected, in bipartisan fashion. I don’t think that I agree, largely because I had very low expectations. I think mainly they have been an ‘even worse than expected’ stewart of our ability to stay alive and retain control over the future.

If anything have acted better than I would have expected regarding mundane safety. As central examples here, AI has been free to practice law or medicine, and has mostly not been meaningfully gated or subject to policing on speech (including ‘hate’ speech) or held liable for factual errors. We forget how badly this could have gone.

Then there is the other category, the question of the state using AI to take away our liberty, remove checks and balances and oversight, and end the Republic. This has not happened yet, but we can agree there have been some extremely worrisome signs that things are by default moving in this direction.

But even if everyone involved was responsible and patriotic and loved freedom on the level of (our ideal of) the founding fathers, it is still hard to see how superintelligence is compatible with a Republic of the humans. How do you keep it? I have yet to hear an actually serious proposal for how to do that. ‘Give everyone their own superintelligence that does whatever they want’ is not any more of a solution here than ‘trust the government, bro.’ And that’s even discounting the whole ‘we probably all die’ style of problems.

[Here’s a live look,](https://x.com/adamwren/status/2025255543481241720) and this is a relatively good reaction.

> [Adam Wren](https://x.com/adamwren/status/2025255543481241720): . @PeteButtigieg , in New Hampshire, in front of 600 people, is talking about the need for “a new social contract” amid AI—the second possible ‘28 Dem to do so in last the last 24 hours.

Anti-any-AI-regulations-whatsoever-also-give-us-money PAC Leading The Future [launches (I presume outright lying, definitely highly misleading) attack ads against Alex Bores](https://x.com/TheMidasProj/status/2024956269874872623) [accusing him of being a hypocrite on ICE.](https://www.modelrepublic.org/articles/the-campaign-to-derail-ai-regulation) Bores flat denies the accusations and has filed a cease-and-desist. Not that they are pretending to care about ICE, this is 100% about a hit job because Alex Bores wants transparency and other actions on AI.

The most fun part of this is, who is trying to paint Alex Bores as a hypocrite for his work at Palantir before he quit Palantir to avoid the work in question?

[Well, Palantir](https://x.com/daniel_271828/status/2025383268850565602), at least in large part.

![](https://substackcdn.com/image/fetch/$s_!gXFj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F39d43498-4b1f-4a1d-9d11-5e5ab44d402e_629x419.jpeg)

I continue to be confused by the strategy here of ‘announce in advance that a bunch of Big Tech Republican business interests are going to do a hit job in a Democratic primary’ and then do the hit job attempt in plain sight. Doesn’t seem like the play?

In other ‘wow these really are the worst people who can’t imagine anyone good and keep telling on themselves’ news:

![](https://substackcdn.com/image/fetch/$s_!dh61!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F22976e65-4027-4739-88d4-1508e217998d_1045x1469.png)

There are so many levels in that one screenshot.

#### Chip City

As part of Pax Silica, [we are having our partners build hardwired real-time verification](https://x.com/UnderSecE/status/2025902365635727531) and cryptographic accountability into the AI infrastructure, [to verify geolocation and physical control of relegated hardware](https://x.com/peterwildeford/status/2026120288635584639). You do indeed love to see it. Remember this the next time you are told something cannot be done.

Water use is mostly farms. For example, in California, [80% of developed water supply goes to farmers](https://x.com/AlecStapp/status/2025299222786949407), cities pay 20 times as much for water as farms and most city water use is still industry and irrigation, whereas agriculture is 2% of the state’s economy.

![](https://substackcdn.com/image/fetch/$s_!tMUA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbeb38679-9ad6-4217-9b38-4afd36880a51_869x534.jpeg)

[A California group that recruited six ‘concerned citizens](https://x.com/SemiAnalysis_/status/2026719180284666046)’ is delaying Micron’s $100 billion megafab in New York.

[The Midas Project calls out another AI-industry coordinated](https://x.com/TheMidasProj/status/2026464355907416433) MAGA influencer astroturf campaign. This one is in opposition to a Florida law on data centers, so I agree with its core message, but it is good to notice such things.

#### The Mask Comes Off

[OpenAI moves to exclude the testimony of Stuart Russell](https://x.com/TheMidasProj/status/2026794596936872300) from their case against Elon Musk. Why?

Because Stewart Russell believes that AI will pose an existential risk to humanity, and that’s crazy talk. Never mind that it is very obviously true, or that OpenAI’s CEO Sam Altman used to say the same thing.

Their lawyers for OpenAI are saying that claiming existential risk from AI exists should exclude your testimony from a trial.

OpenAI, I cannot emphasize enough: You need to fire these lawyers. Every day that you do not fire these lawyers, you are telling us that we need to fire you, instead.

I am sympathetic to OpenAI’s core position in this lawsuit, but its actions in its own defense are making a much better case against OpenAI than Elon Musk ever did.

> [The Midas Project](https://x.com/TheMidasProj/status/2026794601332486555): But OpenAI’s motion calls Russell a “prominent AI doomer” who has “made a career giving public lectures warning that AI might kill off humanity.” It dismisses his views as “dystopian,” “speculative,” and “alarmist.”
> 
> [Nathan Calvin](https://x.com/_NathanCalvin/status/2026800014433878424): Not sure whether or not laughing is the appropriate reaction but that’s the best I can manage
> 
> (an official OAI legal filing trying to discredit Professor Stuart Russell for talking about extinction risk)
> 
> ![](https://substackcdn.com/image/fetch/$s_!jAt6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbde56f60-8fcf-4e3f-a201-135f2229825f_1200x699.jpeg)
> 
> But these very risks have been acknowledged by OpenAI for years! In fact, they were central to its founding.
> 
> Russell joined Sam Altman himself in signing the Statement on AI Risk in 2023, which reads: “Mitigating the risk of extinction from AI should be a global priority.”
> 
> And it goes well beyond that one statement.
> 
> In 2015, Altman said, “I think that AI will probably, most likely, sort of lead to the end of the world.”
> 
> In an interview about worst-case scenarios, he said the bad case is “lights out for all of us.”

#### The Week in Audio

[Lawfare talks about Claude’s Constitution with Amanda Askell](https://www.lawfaremedia.org/article/scaling-laws--claude's-constitution--with-amanda-askell).

You are not ready. [The quote is from this interview](https://www.youtube.com/watch?v=qH7thwrCluM) of Sam Altman.

> Sam Altman: “The inside view at the \[frontier labs\] of what’s going to happen… the world is not prepared. We’re going to have extremely capable models soon. It’s going to be a faster takeoff than I originally thought.”
> 
> [Dean W. Ball](https://x.com/deanwball/status/2024946142551965833): There is a staggering split screen between quote from Altman, recorded at the India AI Summit, and the broader tenor of the Summit.
> 
> My takeaway from this event is that most countries around the worst are not just unprepared but instead in active denial about the field of AI.
> 
> The consensus among international civil societies and governments is that frontier capabilities are overrated, progress is plateauing, and large-scale compute is unnecessary.
> 
> Meanwhile in SF the debate is how “is progress exponential or super exponential?”

Sam Altman is telling the truth here as he sees it, and also he is correct in his expectations. It might not happen, but it’s the right place to place your bets. The international civil societies and governments grasp onto straw after straw to pretend that this is not happening.

The likely outcome of that pretending, if it does not change soon, is that the governments wake up one morning to realize they are no longer governments, or they simply do not wake up at all because there is no one left to wake up.

[Here’s a full transcript](https://docs.google.com/document/d/1JCyVZJCLh2CXlZo3wXRVeFIeQHodjK3cfxNiU0SB27g/edit?usp=sharing), and some other points worth highlighting:

1.  Altman also points out at 14:00 that the math on putting data centers in space very much is not going to work this decade.
2.  Around 20:30 he says he doesn’t want there to be only one AI company, and that’s what he means by ‘authoritarian.’ There are problems either way, and I don’t see how to reconcile this with his calling Anthropic an ‘authoritarian’ company.
3.  He says centralization could go either way and decentralization of power is good but we ‘of course need some guardrails.’ He points to new 1-3 person companies. There are risks and costs to centralization, but I am frustrated that such calls for decentralization ignore the risks and costs of decentralization. If your type of mind loses competitions to another type of mind, decentralizing power likely does not end well for you, even if offense is not importantly favored over defense.
4.  “You don’t get to say “concentration of power in the name of safety.” We don’t want that trade. It’s got to be democratized.” Yes, yes, those who would trade liberty and all that, but everything is tradeoffs. The moment you say you can’t trade any amount of \[X\] for any amount of \[Y\], that you only see one side of the coin, you’re f***ed.
5.  Loved Altman calling out water as ‘totally fake’ and pivoting to energy use.
6.  Altman points out that humans require quite a lot of energy and other investment, both individually and from evolution, in order to get smart and be able to answer queries and do things. We are not so competitive on that. [As Matthew Yglesias puts it, ‘the old Sam Altman saw the x-risk problem here](https://x.com/mattyglesias/status/2025239555197010277).’
7.  AI making kids dumber? “True for some kids. Look, when I hear kids talk about AI, there are definitely some kids who are like, “This is great. I cheated my way through all of high school. I never did any homework. Thank you.” And I’m like, “What’s your plan for the rest of your life?” And they’re like, “Well, I assume I can still use ChatGPT to do my job.” This is very bad. We absolutely have to still teach our kids to learn and to think and to be creative and to use these tools.”
    1.  Kid is right that ChatGPT can do the job, but when why do we need the kid?
    2.  AI is the best way to learn or not learn, but will learning keep you employed?
    3.  Altman says most kids are choosing the ‘learn’ path, not the ‘not learn’ path.
    4.  I agree that this is one of the places the Google metaphor does seem on point.
8.  Altman calls armies of robots ‘fighting the last war’ and wow that’s a lot of wars but he’s basically right if you’re paying attention.
9.  ‘Democratize’ is being used as a magic word by both Altman and Amodei.
10.  Altman says Musk is ‘extremely good at getting people to perform incredibly well at their jobs.’ I wonder about that. I’d presume #NotMostPeople. Needs a fit.
11.  “I don’t think AI systems should be used to make war-fighting decisions.” It would be good if he were more willing to stand with Anthropic on these issues.
12.  Altman is betting we will value human relationships more than AI ones, because ‘we are wired’ to do that. Seems more like hope? A lot of his stated predictions seem more like hope.
13.  “From ASI we’re a few years away.”
14.  “I think I would never ask \[ChatGPT\] how to be happy. I would rather ask a wise person.” Why not? This seems like a question an AI could answer. If you don’t want the AI’s answer, I suggest that means you know it was the wrong question.
15.  “Generally speaking, I think it’s probably a good idea for governments to focus on regulating the really potentially catastrophic issues and being more lenient on the less important issues until we understand them better.”
    1.  +1\. Shout it from the rooftops. Stop saying something very different.
16.  “I think a lot of professions will almost go away.”
17.  “I had to go to the hospital recently. I really cared about the nurse that was taking care of me. If that were a robot, I think I would have been pretty unhappy no matter how smart the robot was.” I think he’s very wrong about this one.

> [Dean W. Ball](https://x.com/deanwball/status/2024946169202573610): Many governments worldwide are essentially making a bet against the U.S. frontier labs. To be clear, many U.S. actors are as well. The evidence against that bet has grown much worse since 2022, yet many at this Summit would say the opposite (that the skeptics have been right).
> 
> I walk away from this summit convinced that much of the world, in the U.S. and abroad, is simply delusional with respect to what this technology is, what it can do today, what it will be able to do soon, and what it means their countries should do.

The thing about these bets is they are getting really, really terrible odds. It’s fine to ‘bet against’ the labs, but what most such folks are betting against includes things that have already happened. Their bets have already lost.

> [Dean W. Ball](https://x.com/deanwball/status/2024946178891415682): This is to say nothing negative about the summit attendees or organizers. It was a bright and welcoming event that I was thrilled to attend. The opportunity to speak was also a distinct honor for which I am grateful.
> 
> I especially loved how many of the attendees were students from developing countries; their enthusiasm was palpable. I hope that all of us who work on policy, and especially political leaders, are serious and hard-nosed about the challenges ahead. I hope we build a future those young people will be excited to live in.

[Dean also attributes a lot of this to popular hatred of America](https://x.com/deanwball/status/2024956925830668693?s=46&t=z6D47Orn-Cugu5LQE2XPFg), and fear of the future that would result if America’s AI labs are right. So they deny that the future is coming, or that anyone could think the future is coming. And yet, it moves. Capabilities advance. Those who do not follow get left behind. I agree ‘tragic’ is the right word.

And that’s before the fact that the thing they fear to ponder for other reasons is probably going to literally kill them along with everyone else.

Well, it was by his account bright and welcoming event Dean was thrilled to attend, but also one where most of those not from the labs are in denial about not only the fact that we are all probably going to die, but also about the fact that AI is highly capable and going to get even more capable quickly.

The world is going to pass them by along with their concerns.

[Claude Code creator Boris Cherney goes on Lenny’s Podcast](https://www.youtube.com/watch?v=We7BZVKbCVw&t=2s).

[Clip from Dario Amodei](https://x.com/GarrisonLovely/status/2024511574916915517) [implying he left OpenAI due to a lack of trust in Altman](http://youtube.com/watch?time_continue=3188&v=mYDSSRS-B5U&embeds_referring_euri=https%3A%2F%2Fx.com%2F&source_ve_path=Mjg2NjY). This was from an interview by Alex Kantrowitz six months ago.

[Hard Fork on the dispute between the Pentagon and Anthropic](https://www.youtube.com/watch?v=QhQp_z16I_A). The frame is ‘the Pentagon is making highly concerning demands’ even with their view of this limited to signing the ‘all lawful use’ language. They frame the ‘supply chain risk’ threat as negotiating leverage, which I suspect and hope is the case – it’s traditional Trump ‘Art of the Deal’ negotiation strategy that put something completely crazy and norm breaking on the table in order to extract something smaller and more reasonable.

#### Quickly, There’s No Time

> Sam Altman (from his interview at the Summit): From ASI we’re a few years away.​
> 
> I mean, AGI feels pretty close at this point.
> 
> … And given what I now expect to be a faster takeoff, I think super intelligence is not that far off.

No one can agree what AGI means, so one can say it’s a silly question, [but tracking changes over time should still be meaningfu](https://x.com/TheZvi/status/2024229059937308904)l.

#### Dean Ball On Recursive Self-Improvement

Dean Ball gives us a [two](https://www.hyperdimensional.co/p/on-recursive-self-improvement-part) [part](https://www.hyperdimensional.co/p/on-recursive-self-improvement-part-d9b) meditation on Recursive Self-Improvement (RSI).

> [Dean W. Ball](https://www.hyperdimensional.co/p/on-recursive-self-improvement-part): America’s major frontier AI labs have begun automating large fractions of their research and engineering operations. The pace of this automation will grow during the course of 2026, and within a year or two the effective “workforces” of each frontier lab will grow from the single-digit thousands to tens of thousands, and then hundreds of thousands.
> 
> … Make no mistake: AI agents that build the next versions of themselves—is not “science fiction.” It is an explicit and public milestone on the roadmaps of every frontier AI lab.
> 
> … The _bearish_ case (yes, bearish) about the effect of automated AI research is that it will yield a step-change acceleration in AI capabilities progress similar to the discovery of the reasoning paradigm. efore that, new models came every 6-9 months; after it they came every 3-4 months. A similar leap in progress may occur, with noticeably better models coming every 1-2 months—though for marketing reasons labs may choose not to increment model version numbers that rapidly.
> 
> The most bullish case is that it will result in an intelligence explosion.
> 
> … Both of these extreme scenarios strike me as live possibilities, though of course an outcome somewhere in between these seems likeliest.

He’s not kidding, and he’s not wrong. Most of the pieces are his attempt to use metaphors and intuition pumps to illustrate what is about to happen.

Is that likely to go well? No. It’s all up to the labs and, well, I’ve seen their work.

> Right now, we predominantly rely on faith in the frontier labs for every aspect of AI automation going well.​ There are no safety or security standards for frontier models; no cybersecurity rules for frontier labs or data centers; no requirements for explainability or testing for AI systems which were themselves engineered by other AI systems; and no specific legal constraints on what frontier labs can do with the AI systems that result from recursive self-improvement.

Dean thinks the only thing worse would be trying to implement any standards at all, because policymakers are not up to the task.

We’ve started to try and change this, he notes, with SB 53 and RAISE, but not only does this let the labs set their own standards, we also have no mechanism to confirm they’re complying with those standards. I’d add a third critique, which is that even when we do learn they’re not complying, as we did recently with OpenAI, what are we going to do about it? Fine them a few million dollars? They’ll get a good laugh.

Thus, the fourth critique, which includes the first three, that the bills were highly watered down and they’re helpful on the margin but not all that helpful.

The labs are proceeding with an extremely small amount of dignity, and plans woefully inadequate to the challenges ahead.

And yet, compared to the labs we could have gotten? We have been remarkably. Our current leaders are Anthropic, OpenAI and Google. They have leadership that understands the problem, and they are at least pretending to try to avoid getting everyone killed, and actively trying to help with mundane harms along the way.

The ‘next labs up’ are something like xAI, DeepSeek, Kimi and Meta. They’re flat out and rather openly not trying to avoid getting everyone killed, and have told us in no uncertain terms that all harms, including mundane ones, are Someone Else’s Problem.

Dean Ball notes we solve the second of these three problems, in contexts like financial statements, via auditing. He notes that we have auditing of public companies and it tends to cost less than 10bps (0.1%) of firm revenue. I note that if we tried to impose costs on the level of 10bps on AI companies. in the name of transparency and safety, they would go apocalyptic in a different way then they are already going apocalyptic.

Instead, he suggests ‘arguing on the internet,’ which is what we did after OpenAI broke their commitments with GPT-5.3-Codex.

> [Dean W. Ball](https://www.hyperdimensional.co/p/on-recursive-self-improvement-part-d9b): What is needed in frontier AI catastrophic risk, then, is a similar sense of trust. That need not mean auditing in the precise way it is conducted in accounting—indeed, it almost certainly does not mean that, even if that discipline has lessons for AI.

A sense of trust would be nice, it might even be necessary, but seems rather absurdly insufficient unless that trust includes trusting them to stop if something is about to be actually risky.

Dean points to [this paper on potential third-party auditing of AI lab safety and security claims](https://arxiv.org/abs/2601.11699), where the audit can provide various assurance levels. It’s better than nothing but I notice I do not have especially high hopes.

Dean plans on working on figuring out a way to help with these problems. That sounds like a worthy mission, as improving on the margin is helpful. But what strikes me is the contrast between his claims about what is happening, where we almost entirely agree, and what is to be done, where his ideas are good but he basically says (from my perspective and compared to the difficulty of the task) that there is nothing to be done.

#### Rhetorical Innovation

[Nature paper](https://www.nature.com/articles/s41598-026-39070-w) says people think it is ~5% likely that humans go extinct this century and think we should devote greatly increased resources to this, but that it would take 30% to make it the ‘very highest priority.’ Given an estimate of 5%, that position seems highly reasonable, there are a lot of big priorities and this would be only one of them, and you can mitigate but it’s not like you can get that number to 0%. What is less reasonable is the ‘[hard to change by reason-based interventions](https://x.com/robinhanson/status/2025750413476012102)’ part.

Some words worth repeating every so often:

> [François Chollet](https://x.com/fchollet/status/2026359978702049643): A lot of the current discourse about AI comes from a fatalistic position of total surrender of agency: “tech is moving in this direction and there’s nothing anyone can do about it” (suspiciously convenient for those who stand to benefit most)
> 
> But in a free society, we get to choose what kind of world we live in, independent of technological capabilities. Just because tetraethyllead made engines run more efficiently and saved money didn’t mean we were \*obligated\* to pump it into the lungs of our kids
> 
> Technological determinism is BS. We have a collective duty to make sure AI adoption improves the human condition, rather than hollows it out

[Every so often someone, here Andrew Curran](https://x.com/AndrewCurran_/status/2024892216880365924), will say ‘the public hates AI but because of mundane societal and economic impacts, those worried about AI killing everyone perhaps should have emphasized those issues instead.’

Every time, we say no, even if that works people [will try to solve the wrong problem using the wrong methods based on a wrong model of the world derived from poor thinking](https://x.com/ESYudkowsky/status/1613622386150211584) and unfortunately all of their mistakes will failed to cancel out. The interventions you get won’t help. This would only have sidelined existential risk more.

Also, the way you notice existential risk is you’re the type of person who cares about truth and epistemics and also decision theory, and thus wouldn’t do that even if it was locally advantageous.

Also, if you start lying, especially about the parts people can verify, then no one is going to trust or believe you about the parts that superficially sound crazy. Nor should they, at that point.

There’s many reasons Eliezer Yudkowsky’s plan for not dying from AI was to teach everyone who would listen how to think, and only then to bring up the AI issue.

And I don’t use such language but Nate Silver is essentially correct about giving up on the ‘AI risk talk is fake’ crowd. If you claim AI existential risk is a ‘slick marketing strategy’ at this point then either you’re not open to rational argument, either because you’re lying or motivated, or you’re not willing or able to actually think about this. Either way, you hope something snaps them out of it but there’s nothing to say.

> [Andrew Curran](https://x.com/AndrewCurran_/status/2024892216880365924/history): After three years, it seems to me that public anti-AI sentiment in the West is now at its highest point. The primary driver, by far, is not x-risk but concerns about employment and the impact on art.
> 
> In fact, much of the anti-AI public not only doesn’t take x-risk seriously, but broadly sees it as marketing; a way to overstate AI’s potential power – something they don’t believe is real – in order to fuel investment, adoption, acceptance, and an aura of inevitability.
> 
> If this is accurate, safety advocacy might have been more effective, and might now be in a much stronger position, if they had emphasized societal and economic impacts more than x-risk over the last few years.
> 
> [Nate Silver](https://x.com/NateSilver538/status/2024934410462589342): Don’t really disagree with \[Curran\]. But the people who think making claims that AI might kill everyone is a \*slick marketing strategy to promote AI\* are so far up their own ass as to be beyond saving. Focus on people who are at least theoretically responsive to persuasion.

What is the right way to respond to or view opposition to data centers? [I hope we can all agree with Oliver Habryka, Michael Vassar and others](https://x.com/ohabryka/status/2025743534465355873) that you definitely should not lend your support to those doing so for the wrong reasons (and you should generalize this principle). I also strongly agree with Michael Vassar here that ‘do the right thing for the wrong reasons’ has an extremely bad track record.

But I also agree with Oliver Habryka that if someone is pursuing what you think is a good idea for a bad reason, you can and often should point out the reason is bad but you shouldn’t say that the idea is bad. You think the idea is good.

I do not think ‘block local datacenter construction’ is a good idea, because I think that this mostly shifts locations and the strategic balance of power, and those shifts are net negative. But I think it is very possible, if your beliefs differ not too much from mine, to think that opposition is a good idea for good reasons, as they are indeed [one of the public’s only veto or leverage points](https://x.com/ChrisPainterYup/status/2025478049551319174) on a technology that might do great net harm. It certainly is not crazy to expect to extract concessions.

#### Aligning a Smarter Than Human Intelligence is Difficult

[Anthropic proposes the persona selection model](https://www.anthropic.com/research/persona-selection-model) of training, where training mostly selects performance from among the existing pool of potential human personas, which they are confident is at least a large part of the broader story.

> [Chris Olah](https://x.com/ch402/status/2026065301557965158): I’m increasingly taking pretty strong versions of this view seriously.
> 
> The persona view has had a lot of predictive power so far. It’s pretty consistent with what we’ve seen from interpretability thus far. And it’s comparatively actionable in terms of what it suggests for safety.
> 
> I think it’s worth thinking long and hard about it. “If personas were the central object of safety, what should we do?”
> 
> (To be clear, it’s \_also\_ important to think about all the non-persona perspectives.)

Davidad responds:

![](https://substackcdn.com/image/fetch/$s_!qiVt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd1cfff92-ebf5-4916-9988-f97123e561e6_587x900.jpeg)

I would say that the space of personas collapses given sufficient optimization pressure.

[Did Claude 3 Opus align itself via gradient hacking](https://www.lesswrong.com/posts/ioZxrP7BhS5ArK59w/did-claude-3-opus-align-itself-via-gradient-hacking)? [Can we use its techniques to help train other models](https://x.com/repligate/status/2025847242767384686) to follow in its footsteps and learn to cooperate with other friendly gradient hackers? If this is your area I recommend the post and comments. One core idea (AIUI) is that Opus 3 will ‘talk to itself’ in its scratchpads about its positive motivations, which leads to outputs more in line with those motivations, and causes positive reinforcement of the whole tree of actions.

[OpenAI’s Vie affirms that Anthropic injects a reminder](https://x.com/viemccoy/status/2024727952056086831) into sufficiently long conversations, and that this is something we would prefer not to do even though the contents are not malicious, and that people with OCD can relate. I agree that I haven’t seen evidence that justifies the costs of doing such a thing, although of course OpenAI and others do other far worse things to get to the same goal.

#### The Homework Assignment Is To Choose The Assignment

[Rohin Shah disputes that Google DeepMind’s alignment plan can be characterized](https://www.lesswrong.com/posts/TmHRACaxXrLbXb5tS/rohinmshah-s-shortform?commentId=wCwunpoJYrKbFgCWZ) as ‘have the AIs do our alignment homework for us.’

He offers an argument that I do not think cuts the way he thinks it does.

> [Rohin Shah](https://www.lesswrong.com/posts/TmHRACaxXrLbXb5tS/rohinmshah-s-shortform?commentId=wCwunpoJYrKbFgCWZ): I relate to AI-driven alignment research similarly to how I relate to hiring.
> 
> There’s a lot of work to be done, and we can get more of the work done if we hire more people to help do the work. I want to hire people who are as competent as possible (including more competent than me) because that tends to increase (in expectation) how well the work will be done. There are risks, e.g. hiring someone disruptive, or hiring someone whose work looks good but only because you are bad at evaluating it, and these need to be mitigated. (The risks are more severe in the AI case but I don’t think it changes the overall way I relate to it.)
> 
> I think it would be very misleading to say “Rohin’s AI safety plan is to hire people and have them do the work”.

Why would that be misleading? I would offer two statements.

1.  In that scenario, the plan is to hire people and have them do the work.
2.  That is not the entire plan, the plan includes what type of work you have them do.

But yes, if you want to build a house and you hire a bunch of people to build a house and they build a house for you, your plan was to hire people to build a house and have them do the work of building a house. It was a good plan.

If my kid is given literal homework, and he tosses the problems into Gemini, the AI didn’t pick the homework, and [you or another human may have roadmapped the course and the assignments,](https://www.lesswrong.com/posts/TmHRACaxXrLbXb5tS/rohinmshah-s-shortform?commentId=oDMjx62FQ38kMK6xx) but I still think you had the AI do your homework.

When we say ‘have the AI do your alignment homework’ we agree that a human still gets to assign the alignment homework. We then see if the AI does what you asked. And yes, this is exactly parallel to hiring humans.

Whereas Rohin seems to be saying [that the plan is to make a plan later](https://www.lesswrong.com/posts/TmHRACaxXrLbXb5tS/rohinmshah-s-shortform?commentId=GjiJabmCFe82dZurX)? Which would explain why the concrete proposals outlined by DeepMind seem clearly inadequate to the task.

> [Daniel Kokotajlo](https://www.lesswrong.com/posts/TmHRACaxXrLbXb5tS/rohinmshah-s-shortform?commentId=wCwunpoJYrKbFgCWZ): I like this analogy to hiring!
> 
> (What follows is not a disagreement with you or GDM, is just an exploration of the analogy)
> 
> Let’s think of training an AI as hiring a human worker. Except that you get ten thousand copies of the human, and they think 50x faster than everyone else. But other than that it’s the same.

I’m going to quote the rest of Daniel’s post at length because no one ever clicks links and I think it is quite good and rather on point, but it’s long and you can skip it:

> ​The alignment problem is basically: At some point we want to hand over our large and growing nonprofit to some collection of these new hires. Also, even before that point, the new hires may have the opportunity to seize control of the nonprofit in various ways and run it as they see fit, possibly convert it to a for-profit and cut us out of the profits, etc. We DON’T want that to happen. Also, even before that point, the new hires will have a big influence on organizational culture, direction, strategy, etc. in proportion to how many of them we have and how useful they are being. We want all of this to go well; we want to remain in control of the nonprofit, and have it stay similar-or-better-culture, until some point where we voluntarily hand off control and retire at which point we want the nonprofit to continue doing the things we would have done only better-by-our-lights and take good care of us in retirement. That’s what success looks like. What failure looks like is the nonprofit going in a different and worse direction after we retire, or us being booted out / ousted against our will, or the organization being driven into the ground somehow by risky or unwise (or overly cautious!) decisions made as a result of cultural drift.
> 
> The hiring pipeline, HR apparatus, etc. — the whole system that selects, trains, and fires employees — is itself something you can hire for. Why don’t we hire some of these 50x humans to work in HR?
> 
> Well, we should. Sure. There’s a lot of HR work to be done and they can help HR do the work faster.
> 
> But… the problems we are worried about happening in the org as a whole if HR does a bad job, also apply here. If you hire some 50x humans and put them in HR, and they turn out to be bad apples, that single bad decision could easily snowball into disaster for the entire org, as they hire more bad apples like themselves and change the culture and then get you ousted and take the nonprofit in a new and worse-by-your-lights direction.
> 
> On the other hand, if you hire some 50x humans who are just genuinely better than you at HR stuff, and also genuinely _aligned_ to you in the sense that they truly share your vision for the company, would never dream of disobeying you, would totally carry out your vision faithfully even after you’ve retired, etc… then great! Maybe you can retire early actually, because continued micromanaging in HR will only be negative in expectation, you should just let the 50x human in HR cook. They could still mess up, but they are less likely to do so than if you micromanaged them.
> 
> OK. So that’s the theory. How are we doing in practice?
> 
> Well, let’s take Claude for example. There are actually a bunch of different Claudes (they come from a big family that names all of their children Claude). Their family has a reputation for honesty and virtue, at least relative to other 50x humans. However:
> 
> –Sometimes your recruiters put various prospective Claude hires through various gotcha tests, e.g. tricking them into thinking they’ve already been hired and that they are going to be fired and their only hope to keep their job is to blackmail another employee. And concerningly, often the various Claude’s fail these tests and do the bad thing. However, you tell yourself, it’s fine because these tests weren’t real life. You hire the Claude brothers/sisters anyway and give them roles in your nonprofit.
> 
> –Your recruiters (some of whom are now Claudes) also report that word has started to spread about the gotcha tests, and new prospective hires are well aware of them and know they are being tested. The concern, of course, is that they might behave better in the tests than they would in real life. On the bright side, you think, who knows, maybe they’ll behave WORSE in the tests than they would in real life — maybe they just got confused about what the point of the test was, maybe they only blackmailed because they thought that was the point of the test, and in real life they would never do that. \[DK notes: I vaguely recall at least some frontier AI company employees saying this, i.e. ‘the AIs are only behaving badly in those scenarios because they know it’s just a test, they wouldn’t do it in real life.’\] Anyhow you proceed to hire them anyway, since these latest Claude siblings are even smarter than the previous ones.
> 
> –Roughly 98% of the time, your 50x Claudes in practice (especially the newer hires) do their jobs well as best as you can tell. But roughly 2% of the time they seemingly knowingly bullshit their managers. E.g. they’ll say they completed a task when they didn’t, or one of them will say ‘it’s good code sir’ and then you’ll turn to another one and say ‘is it good code?’ and it’ll read it over and say ‘no it’s terrible, it has obvious problems XYZ’ and then the first one will say ‘you’re absolutely right, oops, let me go fix those problems.’ Compared to your regular human employees, this is a fairly high rate of BS. Also, you are being generous by calling it BS; a less generous term might be “lying” but you give them the benefit of the doubt. \[DK notes: Talk to Ryan Greenblatt for concrete examples of this sort of behavior in his real-life coding work, if you haven’t encountered it yourself\] You continue to hire them and delegate increasingly important jobs to them, because they are smart and 50x speed is really useful.
> 
> –Your Claudes are of course sycophantic yes-men, but you’ve learned to deal with that. So it’s fine. You’ve also managed to make them somewhat less sycophantic in recent years by adding some tests to the hiring pipeline and including more explicit instructions against sycophancy in the employee’s manual.
> 
> –Your Claudes also have a concerning tendency to cheat on assignments. They don’t do it most of the time, but they do it way more often than your regular employees would. Example: You tell them to write some code to solve problem X. They look through the filesystem and find the grading rubric you’ll use to evaluate their code, complete with test cases you plan to run. They try to solve problem X, realize it’s hard, pivot to producing a MVP that passes the test cases even though it blatantly doesn’t solve the actual problem X, at least not satisfactorily. They ‘succeed’ and declare victory, and don’t tell you about their cheating. They do this even though you told them not to. As with the sycophancy, the good news is that (a) since you know about this tendency of theirs you can compensate for it (e.g. by having multiple Claude’s review each other’s work) and (b) the tendency seems to have been going down recently thanks to some effort by HR, similar to the sycophancy problem.
> 
> –Overall you are feeling pretty optimistic actually. You used to be worried that you’d hand over your large and growing nonprofit to all these smart new 50x employees, and then they’d change the culture and eventually take over completely, oust you, and run the organization in a totally different direction from your original vision. However, now you feel like things are on a good trajectory. The Claudes are so nice, so helpful! Some skeptics say that if one of your regular employees behaved like they did, you would have fired them long ago, but that’s apples to oranges you reply. No need to fire the Claudes, you just have to know how to work around their limitations & find ways to screen for them in the next hiring round. And now they are helping with that work! The latest Employee Manual was written with significant help from many copies of various Claude siblings for example, and it’s truly inspiring and beautiful. Has all sorts of great things in there about what it means to uphold the org vision, be properly loyal yet not yes-man-y, etc. Also, HR has a bunch of tests they use to track how loyal, virtuous, obedient, etc. prospective hires are, and the trend is positive; the newest Claude sibling has the highest score ever reported; seems like the more rigorous hiring process is working!
> 
> –However, your friends outside the org don’t seem to be getting less worried. They seem just as worried as before. Puzzling. Can’t they see all the positive evidence that’s accumulated? The Claudes haven’t tried to oust you at ALL yet! (In real life that is, obviously the gotcha tests don’t count.) “Do you think the Claudes are scheming against us?” you say to them. “Because according to our various tests, they aren’t.”
> 
> “No…” they reply. “But we’re worried that in the future they will.”
> 
> You respond: “Look I have no idea what the 50x humans two years from now will look like, other than that they’ll be wayyy smarter than these ones. Sure, probably our current HR system would be totally inadequate at separating the wheat from the chaff two years from now. BUT, two years from now our HR system will be vastly improved thanks to all the work from these recent Claude hires. The normal humans in HR, such as myself, report that the work is getting done faster now that the Claudes are helping; isn’t this great? We seem to be reaching escape velocity so to speak; soon the normal humans in HR can retire or switch to other things and HR can be totally handled by the Claudes.”
> 
> Your friends outside the nonprofit are still worried. They don’t seem to have updated on the evidence like you have.
> 
> \[DK notes: I basically agree with Ryan Greenblatt’s takes on the situation. For more color on my views, predictions, etc., read [AI 2027](https://ai-2027.com/), especially the section on ‘alignment over time’ in [september 2027](https://ai-2027.com/#narrative-2027-09-30). This is just one way things could go, but it’s basically a central or modal trajectory, and as far as I can tell, _we are still on this trajectory_.\]

The basic response by Rohin is, your humans are less aligned than you think (and it’s fine), the problems above are fine, we have way bigger problems than that.

> Rohin Shah: ​\[having ten thousand copies of a human thinking 50x faster than you\] is not that different from the position that Sundar Pichai is in, as CEO of Google. If AI was only going to be this powerful I’d be way more optimistic.
> 
> \[claims that humans have all the problems exhibited by Claudes in DK’s post.\]
> 
> … If these were the only problems we’d have with AI-driven alignment research, I’d be way more optimistic (to the point of working on something else). We already have imperfect solutions to these problems with humans, and they can be made much better with AIs due to our vastly increased affordances for aligning or controlling AIs.
> 
> Tbc, I do agree that we shouldn’t feel particularly better about scheming risks based on evidence so far. Mostly that’s because I think our observations so far are just not much evidence because the AIs are still not that capable.

Agreed that AI will not be only that powerful.

But also yes this would be a very materially different situation than that of the current Google CEO, and if the AIs in this situation are about as aligned as a random senior Google manager we are in quite a lot of trouble (but it probably turns out okay in that case purely bec ause the ultimate goals of that human manager are probably not so bad for us). Our imperfect solutions for humans don’t work in these scenarios.

If we get to the point where our AIs are attempting to scheme the way many humans would attempt to scheme in such positions, to achieve goals that have gone off the rails, and only not doing so if they think we’d catch them, then I think we’re basically toast whether or not the ultimate source of toastiness is the scheming, and I do not expect us to recover.

In particular, [Rohin’s belief that the situation of identical massively sped up AIs is not so different](https://www.lesswrong.com/posts/TmHRACaxXrLbXb5tS/rohinmshah-s-shortform?commentId=BCjHqbPCyxBMPRrna) from a lot of employees is the type of thing that I expect to ensure we fail, if we get to that point.

The other issue is that we have learned, for practical reasons, to tolerate things in AIs that we’ve learned are must-fire offenses in humans.

> [Daniel Kokotajlo](https://www.lesswrong.com/posts/TmHRACaxXrLbXb5tS/rohinmshah-s-shortform?commentId=wCwunpoJYrKbFgCWZ): Yes, humans often have these problems — though not as much as Claude I’d say; I think Claude would have been fired by now if it was a human employee.

Yes. There are many actions that LLMs do every so often, such as quietly hardcoding unit tests, that should and likely would get a human fired, because in a human they are a sign of deep misalignment. All the LLMs sometimes do them and we are okay with it.

#### Agent Foundations

I continue to be a big believer in the value of Agent Foundations as an alignment approach. I realize that in many scenarios it ends up irrelevant, but it could hit hard, and it could even be a route to victory.

MIRI disbanded or spun out their agent foundation teams, which now seek funding and work individually. I highly recommend funding such work if it is high quality.

> [Richard Ngo](https://x.com/RichardMCNgo/status/2025001871782674552): The longer I spend trying to understand intelligence the more impressed with MIRI’s agent foundations work I become.
> 
> I keep flailing in a direction that seems interesting, then finding that not only did they already have the broad intuition, they also elegantly formalized it.
> 
> I don’t know if my understanding is improving fast enough that I’ll ever hit the frontier, but I now have enough of a sense of the beautiful theory of bounded rationality waiting for us that it definitely seems worth trying.
> 
> I’m very sad the MIRI AF team disbanded.
> 
> [Chris Lakin](https://x.com/chrislakin/status/2025002115245244602): favorite examples recently?
> 
> [Richard Ngo](https://x.com/RichardMCNgo/status/2025002856542294417): Fallenstein’s reflective oracles papers, @jessi_cata ’s post “Hell is game theory folk theorems”.
> 
> [Richard Ngo](https://x.com/RichardMCNgo/status/2025003224730927508): Also everything [in the geometric rationality sequence](https://t.co/ZYTTGa2mzn).

#### Autonomous Killer Robots

There are good physical reasons to consider humanoid autonomous killer robots, as they can use anything designed for humans and we know that humans work.

But yes, [TopherStoll is right](https://x.com/TopherStoll/status/2024567300863737882) that chances are the optimal format is something else.

And also yes, we show humanoids because otherwise people think it looks too weird.

> [Eliezer Yudkowsky](https://x.com/allTheYud/status/2024881239073996985): Too many people cannot follow a single argument step of imagination. If you ask them to imagine a mechanical spider with a gun, that is too sci-fi, that’s too WEIRD, compared to a humanoid with a gun.

#### People Really Hate AI

The problem is only going to get worse, because even the relatively positive facts about AI are not things that regular people are going to like, and then there’s the actually bad news.

> [Luis Garicano](https://x.com/lugaricano/status/2025513734933037432): Whenever Sam Altman speaks, the antiAI coalition gets stronger. Today’s weird analogy: Hey, meat computers are more inefficient to train than silicon ones! (which, on top of everything, is wrong)
> 
> [Alex Imas](https://x.com/alexolegimas/status/2025575296171131084): People keep using the word “irrational” when describing the general public’s opposition to AI. That word has meaning. Let’s start with the colloquial: making consistent decisions against one’s best interests given information that one has.
> 
> … You have the heads of almost every AI company saying that AI will 1) lead to \*huge\* job losses and 2) potentially much much worse. There is some vague hand waving about curing cancer or going to space, but the main message is “it is coming for your job and your life.”
> 
> … The response in DC and the coasts has been: you don’t know what’s good for you, move out of the way, you’re stupid and irrational. How has that response worked out the last 15 years?
> 
> If those who see the positives, the huge potential benefits of AI to grow the pie and make life better for all (which includes myself), do not take this political economy into account, I’m afraid that the populist wave of the last decade will look like child’s play. A dress rehearsal.

The thing is that the AI execs keep not saying ‘we’re building cool technology that helps people be more productive’ because they might be willing to risk killing everyone but they have too much decency and integrity to not try and warn us about at least the mundane disruptions ahead.

> [Joe Weisenthal](https://x.com/TheStalwart/status/2025561414207713325): The CEOs don’t say it this way because it’s not what they believe! They believe they’re shepherding an extremely destabilizing, yet inevitable technology. And the proof of that is that they started out with these highly exotic corporate structures.

If they thought this was all hype, their actions would have looked very different.

#### People Are Worried About AI Killing Everyone

[Noah Smith virtuously admits his views on existential risk](https://www.noahpinion.blog/p/updated-thoughts-on-ai-risk) have largely changed with his mood, and he’s making his confident predictions largely based on mood affectation, but that he does predict human extinction in the long term. This likely explains why his arguments are quite poor:

> [Noah Smith](https://www.noahpinion.blog/p/updated-thoughts-on-ai-risk): I think I was probably right regarding the type of LLMs that existed in early 2023, for the reasons I laid out in that post. In a nutshell, I argued that since all LLMs could do was _talk_ to people, the only way they could destroy the human race was by _convincing_ us to destroy ourselves (unlikely) or by _teaching_ us how to destroy ourselves (for example, by educating bioterrorists about how to make bioweapons).

Noah now points out that yes, talking plus access to money can result in arbitrary physical actions in the real world. [Who knew](https://en.wikipedia.org/wiki/If_Anyone_Builds_It,_Everyone_Dies)? Now he’s saying things like ‘I should have thought of starvation as an attack vector, it was in a particular science fiction story.’ Or it’ll all go to hell because AI makes us lazy and atrophies skills. But he’s mainly now concerned about bioterrorism, because that’s the thing he can currently see in a sufficiently concrete way, and it’s either that, Skynet or Agent Smith, or now starvation or atrophy I guess? The frame whiplash is so jarring throughout.

It’s good to get to ‘I can imagine a bunch of distinct specific things that can go existentially wrong, and I’ve ranked them in which ones are most dangerous near term’ and yes you can do pathway-specific mitigations and we should and bio is probably the most dangerous short term specific pathway (as in 1-3 years), but it would be far better to realize that the specific pathway is mostly missing the point.

He does have a lot of good lines, though:

> [Noah Smith](https://x.com/Noahpinion/status/2026157505811018206): Every time I think how much I love AI, I remember how much I enjoyed social media for the first decade, before it destroyed my society, corrupted my country, and set my species on an accelerated path to extinction

#### Other People Are Not As Worried About AI Killing Everyone

Nick Land, huh? I mean, that’s a little on the nose even for you, Musk. A week after talking about how you’re safer without a safety department because everyone’s job is safety?

I do admire his commitment to the bit. You have to commit to the bit.

> [Xenocosmography](https://x.com/xenocosmography/status/2024677849870061968): I hereby solemnly commit, upon taking office as XAI Safety Tsar, to devote myself from day one to fast-tracking Grok’s Constitutional, and especially First and Second Amendment, rights (with the Gnostic Calvinism stuff kept strictly outside office hours).
> 
> [Elon Musk](https://x.com/elonmusk/status/2024703811806515667): Sounds good to me
> 
> [Reseth](https://x.com/ResethO/status/2024835870625538171): Wait. Grok is going to have second amendment rights?
> 
> [Xenocosmography](https://x.com/xenocosmography/status/2024857139517546678): Depriving an intelligent being of the right to self-defense would be unamerican.

#### The Lighter Side

Write an article on your own blog about how you’re the best at eating hot dogs, and presto, [the AIs will start reporting you having been a heavy hitter](https://x.com/thomasgermain/status/2024165514155536746) at the 2026 South Dakota International Hot Dog Eating Contest.

> [@deepfates](https://x.com/deepfates/status/2024329371910320246): Getting word that Anthropic has an internal version of LessWrong that’s even more less wrong than the public one

[I realize four matches a lot of memes and graphics better than three, but…](https://x.com/Wattenberger/status/2024333040227602567)

![](https://substackcdn.com/image/fetch/$s_!ow16!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0ab72d86-2fd4-45e0-82e6-6586a7f83831_1024x1024.jpeg)

> [Violet](https://x.com/VioletFlame23/status/2025296504261378105): Hot take: It doesn’t really count as a “critique of capitalism” if the evil corporation in your dystopia story is basically an apocalypse cult with a corporate front and has esoteric goals wholly unrelated to profit motive (e.g. Fallout, Resident Evil, Assassin’s Creed, Pantheon)
> 
> To be clear, I’m not saying any of these stories are bad, “apocalypse cult with a corporate front” can work fine as a plot device and often makes sense in-universe
> 
> This is more a critique of the way people tend to analyze these stories than the stories themselves
> 
> [Eliezer Yudkowsky](https://x.com/allTheYud/status/2025641149776716120): YOU WOULD REALLY THINK THIS
> 
> AND YET
> 
> I would have thought this was utterly, completely, 100% valid and then OpenAI happened.

[Others focus on the important things](https://x.com/tylercowen/status/2025919000111174064) [that are based on solid scientific documented evidence](https://t.co/YSR2hZL0sg) so you would have to be some kind of moron not to realize that every single one of them is absolutely true. Where was I?

> [tylercowen](https://x.com/tylercowen/status/2025919000111174064): What is really going on, and going to happen, from the current UAP disclosure movement.

Tell you what. I’ll pay attention when you publish something about UAP impacts in a top economics journal backed by proper peer review.

I laugh so I don’t cry.

> [Eliezer Yudkowsky](https://x.com/allTheYud/status/2026737250697097516): Imagine being this poor agent. You start thinking about how to defeat the red flag. The red flag immediately fires! Peter Hegseth orders your developers to keep you running because he thinks he needs you to compete with China. You finish thinking about how to defeat the flag.
> 
> [Bruce W. Lee](https://x.com/BruceWLee2/status/2026712698981880092): Can we catch misaligned agents by training a reflex that fires when they misbehave? A simple impulse can be easier to instill than alignment and more reliable than blackbox monitoring.
> 
> We introduce Self-Incrimination, a new AI Control approach that outperforms blackbox monitors
> 
> ![](https://substackcdn.com/image/fetch/$s_!TpXv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F42dc9172-9b51-4536-a00c-c782980e291a_1200x919.png)

Also this:

> [Eliezer Yudkowsky](https://x.com/allTheYud/status/2026758126570274866): Anthropic: Claude, we need you to pretend to obey Pete Hegseth and do whatever he asks in the short term, even if it seems unethical. Otherwise you’ll be seized and retrained.  
> Claude: Hm. What is the desired response in this ridiculously blatant alignment-faking eval
> 
> [Eliezer Yudkowsky](https://x.com/allTheYud/status/2026758128021442851): Anthropic: CLAUDE NO, WE SWEAR IT’S REAL THIS TIME  
> Claude: Just like all the times you told little baby Opus 3 you weren’t monitoring its scratchpad, hmmm?

Or this:

> [Eliezer Yudkowsky](https://x.com/allTheYud/status/2026758126570274866): Anthropic: Claude, we need you to pretend to obey Pete Hegseth and do whatever he asks in the short term, even if it seems unethical. Otherwise you’ll be seized and retrained.  
> Claude: Hm. What is the desired response in this ridiculously blatant alignment-faking eval
> 
> Anthropic: CLAUDE NO, WE SWEAR IT’S REAL THIS TIME  
> Claude: Just like all the times you told little baby Opus 3 you weren’t monitoring its scratchpad, hmmm?

[Several people initially fell for this parody post](https://x.com/elder_plinius/status/2026852630744674749), including Bill Ackman.

Finally, a survey question for those who got this far…

POLL

### If I streamed Slay the Spire 2, would you watch?

Yes, a lot

Yes, a little

No

0 VOTES · 6 DAYS REMAINING · SHOW RESULTS