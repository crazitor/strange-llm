---
title: "On being wrong about AI"
author: "Scott Aaronson"
date: "Thu, 14 Dec 2023"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=7672"
---

**Update (Dec. 17):** Some of you might enjoy a [3-hour podcast I recently did with Lawrence Krauss](https://www.youtube.com/watch?v=u00OqCvRhuw), which was uploaded to YouTube just yesterday. The first hour is about my life and especially childhood (!); the second hour's about quantum computing; the third hour's about computational complexity, computability, and AI safety.

* * *

I'm being attacked on Twitter for … no, _none_ of the things you think. This time it's some rationalist AI doomers, [ridiculing me](https://twitter.com/RokoMijic/status/1734357777227645434) for a [podcast](https://bloggingheads.tv/videos/2220) I did with Eliezer Yudkowsky way back in 2009, one that I knew even then was a piss-poor performance on my part. The rationalists are reminding the world that I said back then that, while I knew of no principle to rule out superhuman AI, I was radically uncertain of how long it would take--my "uncertainty was in the exponent," as I put it--and that for all I knew, it was plausibly thousands of years. When Eliezer expressed incredulity, I doubled down on the statement.

I was wrong, of course, not to contemplate more seriously the prospect that AI might enter a civilization-altering trajectory, not merely eventually but _within the next decade_. In this case, I don't need to be reminded about my wrongness. I go over it every day, asking myself what I should have done differently.

If I were to mount a defense of my past self, it would look something like this:

  1. _Eliezer himself_ didn't believe that staggering advances in AI were going to happen the way they did, by pure scaling of neural networks. He seems to have thought someone was going to discover a revolutionary "key" to AI. That _didn 't_ happen; you might say I was right to be skeptical of it. On the other hand, the scaling of neural networks led to better and better capabilities in a way that _neither_ of us expected.
  2. For that matter _, hardly anyone_ predicted the staggering, civilization-altering trajectory of neural network performance from roughly 2012 onwards. Not even most AI experts predicted it (and having taken a bunch of AI courses between 1998 and 2003, I was well aware of that). The few who _did_ predict what ended up happening, notably Ray Kurzweil, made lots of other confident predictions (e.g., the Singularity around 2045) that seemed so absurdly precise as to rule out the possibility that they were using any sound methodology.
  3. Even with hindsight, I don't know of any principle by which I should've predicted what happened. Indeed, we _still_ don't understand why deep learning works, in any way that would let us predict which capabilities will emerge at which scale. The progress has been almost entirely empirical.
  4. Once I saw the empirical case that a generative AI revolution was imminent--sometime during the pandemic--I updated, hard. I accepted what's turned into a two-year position at OpenAI, thinking about what theoretical computer science can do for AI safety. I endured people, on this blog and elsewhere, confidently ridiculing me for not understanding that GPT-3 was just a stochastic parrot, no different from ELIZA in the 1960s, and that nothing of interest had changed. I didn't try to invent convoluted reasons why it didn't matter or count, or why my earlier skepticism had been right all along.
  5. It's still _not_ clear where things are headed. Many of my academic colleagues express confidence that large language models, for all their impressiveness, will soon hit a plateau as we run out of Internet to use as training data. Sure, LLMs might automate most white-collar work, saying more about the drudgery of such work than about the power of AI, but they'll never touch the highest reaches of human creativity, which generate ideas that are fundamentally new rather than throwing the old ideas into a statistical blender. Are these colleagues right? _I don 't know._
  6. **(Added)** In 2014, I _was_ seized by the thought that it should now be possible to build a vastly better chatbot than ["Eugene Goostman"](https://scottaaronson.blog/?p=1858) (which was basically another ELIZA), by training the chatbot on all the text on the Internet. I wondered why the experts weren't already trying that, and figured there was probably some good reason that I didn't know.



Having failed to foresee the generative AI revolution a decade ago, how should I fix myself? Emotionally, I _want_ to become even more radically uncertain. If fate is a terrifying monster, which will leap at me with bared fangs the instant I venture any guess, perhaps I should curl into a ball and say _nothing_ about the future, except that the laws of math and physics will probably continue to hold, there will still be war between Israel and Palestine, and people online will still be angry at each other and at me.

But here's the problem: in saying "for all I know, human-level AI might take thousands of years," _I thought I was being radically uncertain already_. I was explaining that there was no trend you could knowably, reliably project into the future such that you'd end up with human-level AI by roughly such-and-such time. And in a sense, I was right. The trouble, with hindsight, was that I placed the burden of proof only on those saying a dramatic change _would_ happen, not on those saying it _wouldn 't_. Note that this is the same mistake most of the world made with COVID in early 2020.

I would sum up the lesson thus: **one must never use radical ignorance as an excuse to default, in practice, to the guess that everything will stay basically the same.** Live long enough, and you see that year to year and decade to decade, everything _doesn 't_ stay the same, even though most days and weeks it seems to.

The hard part is that, as soon as you venture a particular way in which the world might radically change--for example, that a bat virus spreading in Wuhan might shut down civilization, or Hamas might attempt a second Holocaust while the vaunted IDF is missing in action and half the world cheers Hamas, or a gangster-like TV personality might threaten American democracy more severely than did the Civil War, or a neural network trained on all the text on the Internet might straightaway start conversing more intelligently than most humans--say that all the prerequisites for one of these events seem to be in place, and you'll face, not merely disagreement, but _ridicule_. You'll face serenely self-confident people who call the entire existing order of the world as witness to your wrongness. That's the part that stings.

Perhaps the wisest course for me would be to admit that I'm not and have never been a prognosticator, Bayesian or otherwise--and then _stay consistent_ in my refusal, rather than constantly getting talked into making predictions that I'll later regret. I should say: I'm just someone who likes to draw conclusions validly from premises, and explore ideas, and clarify possible scenarios, and rage against obvious injustices, and not have people hate me (although I usually fail at the last).

* * *

The rationalist AI doomers also dislike that, in their understanding, I [recently](https://scottaaronson.blog/?p=7064) expressed a "p(doom)" (i.e., a probability of superintelligent AI destroying all humans) of "merely" 2%. The doomers' probabilities, by contrast, tend to [range between 10% and 95%](https://twitter.com/AISafetyMemes/status/1729892336782524676)--that's why they're called "doomers"!

In case you're wondering, I arrived at my 2% figure via a rigorous Bayesian methodology, of taking the geometric mean of what my rationalist friends might consider to be sane (~50%) and what all my other friends might consider to be sane (~0.1% if you got them to entertain the question at all?), thereby ensuring that both camps would sneer at me equally.

If you read my [post](https://scottaaronson.blog/?p=7064), though, the main thing that interested me was _not_ to give a number, but just to unsettle people's confidence that they even understand what should count as "AI doom." As I [put it](https://www.astralcodexten.com/p/mantic-monday-12423/comment/44819549) last week on the other Scott's blog:

> To set the record straight: I once gave a ~2% probability for the classic AGI-doom paperclip-maximizer-like scenario. I have a much higher probability for an existential catastrophe in which AI is causally involved in one way or another — there are many possible existential catastrophes (nuclear war, pandemics, runaway climate change…), and many bad people who would cause or fail to prevent them, and I expect AI will soon be involved in just about everything people do! But making a firm prediction would require hashing out what it means for AI to play a “critical causal role” in the catastrophe — for example, did Facebook play a “critical causal role” in Trump’s victory in 2016? I’d say it’s still not obvious, but in any case, Facebook was far from the only factor.

This is not a minor point. That AI will be a central force shaping our lives now seems certain. Our new, changed world will have many dangers, among them that all humans might die. Then again, human extinction has _already_ been on the table since at least 1945, and outside the "paperclip maximizer"--which strikes me as just one class of scenario among many--AI will presumably be far from the _only_ force shaping the world, and chains of historical causation will still presumably be complicated even when they pass through AIs.

I have a dark vision of humanity's final day, with the Internet (or whatever succeeds it) full of thinkpieces like:

  * Yes, We're All About to Die. But Don't Blame AI, Blame Capitalism
  * Who Decided to Launch the Missiles: Was It President Boebert, Kim Jong Un, or AdvisorBot-4? 
  * Why Slowing Down AI Development Wouldn't Have Helped



* * *

Here's what I want to know in the comments section. Did _you_ foresee the current generative AI boom, say back in 2010? If you did, what was your secret? If you didn't, how (if at all) do you now feel you should've been thinking differently? Feel free also to give your p(doom), under any definition of the concept, so long as you clarify which one.
