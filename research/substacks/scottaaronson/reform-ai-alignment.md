---
title: "Reform AI Alignment"
author: "Scott Aaronson"
date: "Sun, 20 Nov 2022"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=6821"
---

**Update (Nov. 22):** Theoretical computer scientist and longtime friend-of-the-blog [Boaz Barak](https://www.boazbarak.org/) writes to tell me that, coincidentally, he and Ben Edelman just released a big essay advocating a version of "Reform AI Alignment" [on Boaz's Windows on Theory blog](https://windowsontheory.org/2022/11/22/ai-will-change-the-world-but-wont-take-it-over-by-playing-3-dimensional-chess/), [as well as on LessWrong](https://www.lesswrong.com/posts/zB3ukZJqt3pQDw9jz/ai-will-change-the-world-but-won-t-take-it-over-by-playing-3). (I warned Boaz that, having taken the momentous step of posting to LessWrong, in 6 months he should expect to find himself living in a rationalist group house in Oakland…) Needless to say, I don't necessarily endorse their every word or vice versa, but there's a striking amount of convergence. They also have a much more detailed discussion of (e.g.) which kinds of optimization processes they consider relatively safe.

* * *

Nearly halfway into my year at OpenAI, still reeling from the FTX collapse, I feel like it's finally time to start blogging my AI safety thoughts--starting with a little appetizer course today, more substantial fare to come.

Many people claim that AI alignment is little more a modern eschatological religion--with prophets, an end-times prophecy, sacred scriptures, and even a god (albeit, one who doesn't exist quite yet). The obvious response to that claim is that, while there's some truth to it, "religions" based around technology are a little different from the old kind, because technological progress _actually happens_ regardless of whether you believe in it.

I mean, the Internet is sort of like the old concept of the collective unconscious, except that it actually exists and you're using it right now. Airplanes and spacecraft are kind of like the ancient dream of Icarus--except, again, for the actually existing part. Today GPT-3 and DALL-E2 and LaMDA and AlphaTensor exist, as they didn't two years ago, and one has to try to project forward to what their vastly-larger successors will be doing a decade from now. Though some of my colleagues are still in denial about it, I regard the fact that such systems will have transformative effects on civilization, comparable to or greater than those of the Internet itself, as "already baked in"--as just the mainstream position, not even a question anymore. That doesn't mean that future AIs are going to convert the earth into paperclips, or give us eternal life in a simulated utopia. But their story _will_ be a central part of the story of this century.

Which brings me to a second response. If AI alignment is a religion, it’s now large and established enough to have a thriving "Reform" branch, in addition to the original "Orthodox" branch epitomized by Eliezer Yudkowsky and [MIRI](https://intelligence.org/).  As far as I can tell, this Reform branch now counts among its members a large fraction of the AI safety researchers now working in academia and industry.  (I’ll leave the formation of a Conservative branch of AI alignment, which reacts against the Reform branch by moving _slightly_ back in the direction of the Orthodox branch, as a problem for the future — to say nothing of Reconstructionist or Marxist branches.)

Here’s an incomplete but hopefully representative list of the differences in doctrine between Orthodox and Reform AI Risk:

(1) Orthodox AI-riskers tend to believe that humanity will survive or be destroyed based on the actions of a few elite engineers over the next decade or two.  Everything else--climate change, droughts, the future of US democracy, war over Ukraine and maybe Taiwan--fades into insignificance except insofar as it affects those engineers.

We Reform AI-riskers, by contrast, believe that AI might well pose civilizational risks in the coming century, but so does all the other stuff, and it's all tied together.  An invasion of Taiwan might change which world power gets access to TSMC GPUs.  Almost everything affects which entities pursue the AI scaling frontier and whether they're cooperating or competing to be first.

(2) Orthodox AI-riskers believe that public outreach has limited value: most people can't understand this issue anyway, and will need to be saved from AI despite themselves.

We Reform AI-riskers believe that trying to get a broad swath of the public on board with one's preferred AI policy is something close to a deontological imperative.

(3) Orthodox AI-riskers worry almost entirely about an agentic, misaligned AI that deceives humans while it works to destroy them, along the way to maximizing its strange utility function.

We Reform AI-riskers entertain that possibility, but we worry at least as much about powerful AIs that are weaponized by bad humans, which we expect to pose existential risks much earlier in any case.

(4) Orthodox AI-riskers have limited interest in AI safety research applicable to actually-existing systems (LaMDA, GPT-3, DALL-E2, etc.), seeing the dangers posed by those systems as basically trivial compared to the looming danger of a misaligned agentic AI.

We Reform AI-riskers see research on actually-existing systems as one of the only ways to get feedback from the world about which AI safety ideas are or aren't promising.

(5) Orthodox AI-riskers worry most about the "FOOM" scenario, where some AI might cross a threshold from innocuous-looking to plotting to kill all humans in the space of hours or days.

We Reform AI-riskers worry most about the "slow-moving trainwreck" scenario, where (just like with climate change) well-informed people can see the writing on the wall decades ahead, but just can't line up everyone's incentives to prevent it.

(6) Orthodox AI-riskers talk a lot about a "pivotal act" to prevent a misaligned AI from ever being developed, which might involve (e.g.) using an aligned AI to impose a worldwide surveillance regime.

We Reform AI-riskers worry more about such an act causing the very calamity that it was intended to prevent.

(7) Orthodox AI-riskers feel a strong need to repudiate the norms of mainstream science, seeing them as too slow-moving to react in time to the existential danger of AI.

We Reform AI-riskers feel a strong need to get mainstream science on board with the AI safety program.

(8) Orthodox AI-riskers are maximalists about the power of pure, unaided superintelligence to just figure out how to commandeer whatever physical resources it needs to take over the world (for example, by messaging some lab over the Internet, and tricking it into manufacturing nanobots that will do the superintelligence's bidding).

We Reform AI-riskers believe that, here just like in high school, there are limits to the power of pure intelligence to achieve one's goals.  We'd expect even an agentic, misaligned AI, if such existed, to need a stable power source, robust interfaces to the physical world, and probably allied humans before it posed much of an existential threat.

What have I missed?
