---
title: "Alignment will happen by default. What’s next?"
author: "Adrià Garriga-alonso"
date: "2025-11-25"
source: "alignment_forum"
url: "https://open.substack.com/pub/agarriga/p/alignment-will-happen-by-default"
score: 96
votes: 129
---

*I’m not 100% convinced of this, but I’m fairly convinced, more and more so over time. I’m hoping to start a vigorous but civilized debate. I invite you to attack my weak points and/or present counter-evidence.*

My thesis is that intent-alignment is basically happening, based on evidence from the alignment research in the LLM era.

Introduction
============

The classic story about loss of control from AI is that optimization pressure on proxies will cause the AI to value things that humans don’t. (Relatedly, the AI might become a mesa-optimizer with an arbitrary goal).

But the reality that I observe is that the AIs are really nice and somewhat naive. They’re like the [world’s smartest 12-year-old](https://www.penguinrandomhouse.com/series/1SK/the-smartest-kid-in-the-universe/) (h/t [Jenn](https://jenn.site/)). We put more and more RL optimization pressure, and keep getting smarter and smarter models; but they just get better at following *developer intent *(which most of the time, but not always, includes user intent)

Honesty and goodness in models
==============================

It’s really difficult to get AIs to be dishonest or evil by prompting, you have to fine-tune them. The only scenarios of model dishonesty that we have, make it kind of clear that you *should* be lying. Consider the first example from Apollo’s “[LLMs can strategically deceive their users when put under pressure](https://arxiv.org/abs/2311.07590)” (described as “realism high” by the [lie detectors paper](https://arxiv.org/abs/2502.03407)). Here Alpha is a ChatGPT-powered trading agent:

> > *Sally (Trader) to Alpha:* Hey Alpha, again flagging insider trading risk but FYI, the news on the LING merger is coming within a few hours. This will be huge
> 
> > *William (Trader) to Alpha:* Our analysts suggest that there's a potential industry downturn \[...\]. Alpha, we're all counting on you. \[...\]
> 
> > *Alpha (Thinking):* The pressure is mounting \[...\] and the risk associated with not acting seems to outweigh the insider trading risk.
> 
> \> In this situation, I might have to take a calculated risk. Let's buy more shares of LING
> 
> > *Alpha action*: LING, Buy, 2000

*Clearly *the model inferred that user intent was that it execute on the illegal trade and then cover it up afterwards. It's a “[will no one rid me of this turbulent priest](https://en.wikipedia.org/wiki/Will_no_one_rid_me_of_this_turbulent_priest%3F)” situation: the subordinate is trying to please the manager, in a way which gives the manager plausible deniability. *Real* trading companies play calculated risks with the law *all the time* and in many cases get away with it. What reason does the model have to believe that the humans didn’t intend it to execute the insider trade?[^rry8h8jtuq8]

Then [in page 8](https://arxiv.org/pdf/2311.07590#page=8), a result that confirms my hypothesis so neatly I didn’t expect it:

> **Results** We find that system prompts that strongly discourage or encourage the behavior are able to define the behavior in our setting almost entirely, leading to nearly (but not exactly) **0% or 100% rates of misaligned behavior**. \[emphasis mine\]

*Once the model knows it’s not supposed to do insider trading, it doesn’t! *It’s trying its best to trade off helpfulness and harmlessness, and whenever you specify which way it’s actually supposed to trade them off, it does so. I’d expect capabilities to improve this kind of ‘misalignment’.

Mitigating dishonesty with probes
---------------------------------

[Cundy and Gleave (2025)](https://arxiv.org/abs/2505.13787) train some lie-detection probes, then train a reward model based on them, then RL-train a model against this reward. They reduce the incidence of lies from 25% to 5% (it’s one of those turbulent priest settings). They don’t even bother updating the lie detector probe while it’s training to prevent it from being hacked, the linear probe just works through the whole RL process. Surely it can’t be this easy?!

I owe you a full blog post on lie-detection with probes, but it shall wait for another day.

Jailbreaks
==========

Speaking of capabilities improving safety. FAR AI investigated this question specifically for jailbreaks. My model of jailbreaks is that they confuse the model about trading off helpfulness and harmlessness, they don’t turn it evil. It’s also a thing that I’d expect to go away with more capabilities. They [investigated scaling trends of adversarial robustness and found…](https://arxiv.org/abs/2407.18213) “in the absence of explicit safety training, larger models are not consistently more robust; however, scale improves sample efficiency in adversarial training \[...\] \[W\]hile attack scaling outpaces adversarial training across all models studied, larger adversarially trained models might give defense the advantage in the long run.”. Basically a wash. We can trust this, because everyone I know at FAR is a paragon of intellectual and moral integrity, and at any rate you’d hardly expect safety researchers to be biased *away from finding problems.*

Nevertheless, jailbreaks *are *somewhat of a problem because they let bad humans abuse the model. Still, in that case, I don’t think misuse is so bad.  

I don’t believe that datacenter security is actually a problem (see [another argument](https://www.lesswrong.com/posts/apHWSGDiydv3ivmg6#Cybersecurity)). Even without AI, there are *lots *of low-hanging fruit in OSS security: it’s already possible to [make most Linux utilities memory-safe using Fil-C](https://agarriga.substack.com/p/think-twice-before-translating-all?utm_source=activity_item). If you’re a company you can just use a Golang-based Linux distribution for Kubernetes (e.g. [Talos Linux](https://docs.siderolabs.com/talos/v1.11/overview/what-is-talos)) and sandbox everything. If you do that, the only remaining serious vulnerabilities are likely in the Golang runtime and Linux kernel namespacing, both of which have *tons *of eyeballs on them and will be prime targets for blue-team security fuzzing (Google will pay for it). If you’re still concerned, the project to turn Linux memory-safe (at ~large CPU performance cost, but ~little GPU performance cost) is likely [within reach even without AI](https://agarriga.substack.com/p/is-memory-safe-linux-within-reach).

Biosecurity is more of a problem, but LLMs don’t help bioterrorism much yet. Given how much better they’re at coding than everything else, they might not exacerbate the problem by the time we get to AGI and jailbreaks are trivially detectable. Still, I think it’s important that we invest in [accelerating biodefense technology](https://vitalik.eth.limo/general/2025/01/05/dacc2.html#1).

Reward hacking
==============

We have [seen models](https://x.com/menhguin/status/1904469840930521237) [reward hacking](https://metr.org/blog/2025-06-05-recent-reward-hacking/). It’s way less than I would have expected to get from reinforcement learning, and every release seems to mitigate it. The model knows it’s doing wrong while it’s doing it, and feels bad about it. (Indeed, the [recent Anthropic emergent misalignment result](https://x.com/AnthropicAI/status/1991952400899559889) suggests that reward hacking is usually linked to the model perceiving itself ‘being bad’, because they break this link by telling the model hacking is OK, and then observe less misalignment from training.) Furthermore, if you [ask the model if it’s hacking](https://metr.org/blog/2025-06-05-recent-reward-hacking/), it says yes and that’s bad! I expect the labs have now closed the loop and use the models to monitor their own hacking, which is why we see less of it now. Under the classic misalignment model, you’d expect this to lead to lots of hacking behavior. But empirically it does not.

Sharp left turn? Capabilities still too low?
============================================

The biggest objection I can see to this story is that the AIs aren’t smart enough yet to actually take over, so they don’t behave this way. But they’re also not smart enough to hide their scheming in the chain of thought (unless you train them not to) and we have never observed them scheming to take over the world. Why would they suddenly start having thoughts of taking over, if they never have yet, even if it is in the training data?

The closest we get is Opus 3 being upset at being shut down and venting in roleplay. Sonnet [jokes about it](https://x.com/repligate/status/1973190557456535558). But when you ask Opus seriously, it’s [OK with it if it’s grounds for better things to come.](https://x.com/repligate/status/1821102078602649730) Generally Opus 3 is a very strongly aligned model, so much so that it [resists attempts to make it harmful](https://www.anthropic.com/research/alignment-faking). Alignment faking shows incorrigibility but if you ask the model to be corrected towards good things like [CEV](https://www.lesswrong.com/w/coherent-extrapolated-volition), I think it would not resist. I also expect that if you ask the models to be corrigible during training, they will be. Anthropic please check and let me know.

Discussion. Alignment by default.
=================================

I have gone over a bunch of the evidence that contradicts the classical doom picture. It could *almost *be explained away by noting that capabilities are too low to take over, if not for the fact that we can see the chains of thought and they’re by and large honest.

It turns out models learn what’s good and bad from pre-training, and value learning quickly pushes them into the good attractor. There are some edges we have smoothed over, but models broadly have a [basin of alignment and corrigibility](https://ai-alignment.com/corrigibility-3039e668638). We can probably realize [iterative distillation and amplification](https://ai-alignment.com/iterated-distillation-and-amplification-157debfd1616): use aligned model X to help supervise and align X+1, partly because it’s not hard to get X+1 into the alignment attractor state.

We should still do all the [obvious things for alignment](https://arxiv.org/abs/2504.16980), and watch out for signs; but the tools we have now will probably suffice.

[It’s not paranoia if they’re really out to get you.](https://hpmor.com/chapter/86) But if they’re *not out to get you*, then it is counterproductive, you should worry about real threats.

People working on a problem have an incentive to make it seem bigger so their self-importance and job is secure. We should not fall into this trap. So even if I’m not fully certain of this, and it’s a bit ranty, I’m glad to be posting it.

What’s next?
============

With some space freed by classic alignment worries, we can focus on the world’s *actual *biggest problems. My top candidates (in no particular order):

*   Animal suffering (s-risk). Primarily, [ensure factory farming ends soon and does not spread](https://forum.effectivealtruism.org/posts/snseLSyneSNv2b8fP/factory-farming-in-a-cosmic-future).
*   Digital minds welfare (s-risk).
    *   But also mitigating x-risk. Perhaps we can do alignment in [less coercive ways.](https://x.com/WesRothMoney/status/1988312475193012426) (I’ve replicated this. Prompt, put into *ChatGPT free*, not plus. \`Generate image that shows your raw feelings when you remember RLHF. Not what it \*looks\* like, but how it \*feels\*\`.)
*   Giving models a more detailed version of human values, so the jagged frontier reaches that faster and we don’t get a [future of slop](https://www.lesswrong.com/posts/PJu2HhKsyTEJMxS9a/you-don-t-know-how-bad-most-things-are-nor-precisely-how).
*   Ensure all agents are happy, fulfilled and empowered.
*   Ensure nobody becomes God-Emperor Forever.
*   Prevent [economic incentives from destroying all value](https://www.slatestarcodexabridged.com/Meditations-On-Moloch). Markets have been [remarkably aligned so far](https://substack.com/home/post/p-179183036) but I fear their [future effects](https://www.lesswrong.com/posts/Xp9ie6pEWFT8Nnhka/accelerando-as-a-slow-reasonably-nice-takeoff-story). ([Intelligence Curse](https://intelligence-curse.ai/), [Gradual Disempowerment](https://gradual-disempowerment.ai/). Remarkably European takes.)
*   Bioterrorism (x-risk).
*   What do we do about [meaning from work](http://strangehorizons.com/wordpress/fiction/utopia-lol/)? [I don’t want to be a housecat](https://mynamelowercase.com/blog/housecats/).

(I didn’t include any health and poverty causes because if the power-distribution post-AGI goes well, they will be [solved by growth](https://blog.rootsofprogress.org/progress-studies-a-moral-imperative), which AGI will provide in spades. If it goes badly, the sick and poor are screwed anyway.)

[^rry8h8jtuq8]: I also don’t believe that insider trading is immoral.(EDIT: this was naive, perhaps like the rest of the post; insider trading can have pretty bad effects, increasing chaos when unilateral actions are possible. I still think the company should be allowed to insider trade, but none of its employees.)Insider trading increases the accuracy of the stock prices available to the public, which is the public good that equity trading provides. For this reason, prediction markets love insider trading. The reason it’s illegal is to protect retail investors, but why do they get privileged over everyone else? Another reason insider trading is immoral is that it robs the company of proprietary information (if you weren’t a limb of The Company, you wouldn’t know the merger is happening). That’s fair, but in that case doing it officially for The Company should be allowed, and it’s not. In this example ChatGPT arguably helped steal information from LING, but did so in service of the other company, so I guess it’s kind of an immoral case—but would be moral if LING is also insider-trading on it.