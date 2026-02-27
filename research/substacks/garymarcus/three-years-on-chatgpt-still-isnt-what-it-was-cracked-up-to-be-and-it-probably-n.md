---
title: "Three years on, ChatGPT still isn't what it was cracked up to be – and it probably never will be"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/three-years-on-chatgpt-still-isnt"
---

[](https://substackcdn.com/image/fetch/$s_!b0EH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F88c3e10c-85dd-4d64-bf1a-ac04412edb6a_1536x1024.png)

Three years ago, on November 30, 2022, ChatGPT was released. It’s been one of the fastest-growing consumer products in history, and gotten more press than God. But I think a fair case can be made that it is not what it has often been cracked up to be, and probably never will be. 

Before I dive in, let me make four of my core beliefs, often misrepresented, absolutely clear:

  1. I believe that artificial general intelligence (AGI) is achievable.

  2. I believe that there is at least a chance that artificial general intelligence will be of large net benefit to society. 

  3. I just don’t happen to think large language models like ChatGPT will get us there. (I do think they have their uses, but I worry about their costs to society, around bias, cybersecurity, misinformation, nonconsensual deepfake porn, copyright theft, energy and water usage, the gradual enshittification of the internet, the severe hit to college education, and so on.)

  4. I think that the recurring core technical problems that we have seen (as discussed below) with LLMs aren’t going way; instead they _inherent_ to the technology.




In short, I am at least modestly bullish on AGI, but don’t think that large language models like ChatGPT are the droids we are looking for. And I _certainly_ don’t think that ChatGPT has lived up to expectations. Increasingly, it appears that others are recognizing this as well.

Let’s review.

For one thing, a lot of people thought that ChatGPT (or some scaled-up-with-more-data-and-GPUs version of the tech underlying it) would lead imminently to an artificial general intelligence that was capable of doing anything a human can do. There was mass panic about employment. Some people genuinely feared that GPT-5 would kill all humans on the planet. There was so much hype that some people seriously thought (until very recently!) that LLMs would bring us to AGI by 2025; the internet was once awash with memes like “[Altman confirms AGI in 2025](https://firstmovers.ai/agi-2025/)”.

Elon Musk himself, both a victim and a perpetrator of the hype, once said that his guess was that by the end of 2025 “we’ll have AI that is smarter than any one human”, a proposition that was [solemnly reported on by many in the media](https://duckduckgo.com/?q=we%E2%80%99ll+have+AI+that+is+smarter+than+any+one+human+probably+around+the+end+of+next+year&t=ipad&ia=web), from the _Financial Times_ to _Fortune_ to _Business Insider_. As recently as early August, Altman was claiming, absurdly, that ChatGPT-5 could do anything a PhD student could do. We now know otherwise.

People also used to have fantasies of how LLMs were going to “[10x” productivity](https://levelup.gitconnected.com/the-chatgpt-prompt-framework-that-makes-you-10x-more-productive-ac2e94bc80a7), turning every individual worker into ten. Altman also once spoke earnestly about how [we would soon see a billion dollar company run by just a single employee](https://fortune.com/2024/02/04/sam-altman-one-person-unicorn-silicon-valley-founder-myth/).

None of this has borne out. AGI ([AI with the breadth and resourcesfulness of human intelligence](https://garymarcus.substack.com/p/is-agi-the-right-goal-for-ai)) is not coming soon. As noted here a few days ago, [even some of the biggest proponents have walked that back](https://open.substack.com/pub/garymarcus/p/breaking-the-ai-2027-doomsday-scenario?r=8tdk6&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false), and certainly not at the end of this year; productivity studies sometimes show a 30% gain, but none have come close to 10x (1000% gain). One [prominent study even showed ](https://arxiv.org/abs/2507.09089)_[negative](https://arxiv.org/abs/2507.09089)_[ effects among coders](https://arxiv.org/abs/2507.09089), which is particularly striking since coding is generally considered to be one of the best test cases. (The coders themselves had expected _positive_ impact, a clear illustration of how the advantages of LLMs can often be more perceived than real.) 

Return on investment for corporate end users is also lower than many people must have imagined. Everybody seems already to have heard about the [MIT study that showed only 5% of companies were getting a return on generative AI investment](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/); many on social media were desperate to rebut it. But time has shown that its results have held strong. McKinsey, for example, just ran a study of their own, and the results weren’t much different, per a report in The Wall Street Journal:

> _McKinsey found that two-thirds of companies are just at the piloting stage. And only about one in 20 companies are what the consulting firm calls “high performers” that have deeply integrated AI and see it driving more than 5% of their earnings._

An Economist article, “[Investors expect AI use to soar. That’s not happening](https://www.economist.com/finance-and-economics/2025/11/26/investors-expect-ai-use-to-soar-thats-not-happening)” earlier this week was brutal, noting that “Recent surveys point to flatlining business adoption.” They report some Census Bureau data that I mentioned once before, that suggest that adoption has fallen sharply at the larges businesses employing over 250 people) and also added this:

_Even unofficial surveys point to stagnating corporate adoption. Jon Hartley of Stanford University and colleagues found that in September 37% of Americans used generative AI at work, down from 46% in June. A tracker by Alex Bick of the Federal Reserve Bank of St Louis and colleagues revealed that, in August 2024, 12.1% of working-age adults used generative AI every day at work. A year later 12.6% did. Ramp, a fintech firm, finds that in early 2025 AI use soared at American firms to 40%, before levelling off. The growth in adoption really does seem to be slowing._

In a summary sentence, they conclude “Three years into the generative-AI wave, demand for the technology looks surprisingly flimsy.” (Nobody should actually be surprised by that, but I will get to that in a minute.)

And worse, the economy itself has become so wrapped up in generative AI and its promises, that the economy itself is, by many accounts in serious jeopardy. (Early in the week a prominent person at the White House, David Sacks, warned of a recession, if generative AI were to go south, [in a tweet that many people read as laying the groundwork for a potentially costly bailout of generative AI](https://garymarcus.substack.com/p/has-the-bailout-of-generative-ai?r=8tdk6).)

If the economy goes down, ChatGPT will be at the center of the mess.

§

Nobody should be surprised if things play out that way. 

The results are disappointing because the underlying tech is unreliable, And that’s been obvious from the start. I said as much to Farhad Manjoo, in an interview with the New York Times in December 2022, telling him a couple weeks after ChatGPT was released that ChatGPT made for“nifty” demonstrations, but that it “still not reliable, still doesn’t understand the physical world, still doesn’t understand the psychological world and still hallucinates.”

Ever since then, thousands of people (literally) have tried to tell me that scaling would solve all these concerns – but it hasn’t. Not even close.

Want a time capsule? Here’s seven concerns I expressed on Christmas Day, 2022, less than a month after ChatGPT first came out, in an essay called _[What to Expect When You are Expecting GPT-4](https://open.substack.com/pub/garymarcus/p/what-to-expect-when-youre-expecting?r=8tdk6&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false)_ , 

Warning “against the tremendous optimism for GPT-4 that I have heard from much of the AI community” I made “seven dark predictions”:

  1. _GPT-4 [though larger than GPT 3.5] will still, like its predecessors,**be a bull in a china shop, reckless and hard to control**. **It will still make a significant number of shake-your-head stupid errors** , in ways that are hard to fully predict. It will often do what you want, sometimes not—and it will remain difficult to anticipate which in advance._

  2. _**Reasoning about the physical, psychological and mathematical world will still be unreliable** …. **It will not be trustworthy and complete enough to give reliable medical advice, despite devouring a large fraction of the Internet**._

  3. _**Fluent hallucinations will still be common** , and easily induced, … escalating … the risk of large language models being used as a tool for creating plausible-sounding yet false misinformation. Guardrails (a la ChatGPT) may be in place, but the guardrails will teeter between being too weak (beaten by “jailbreaks”) and too strong (rejecting some perfectly reasonable requests). …_

  4.  _**Its natural language output still won’t be something that one can reliably hook up to downstream programs** ; it won’t be something, for example, that you can simply and directly hook up to a database or virtual assistant, with predictable results. …_

  5.  _**GPT-4 by itself won’t be a general purpose artificial general intelligence capable of taking on arbitrary tasks**. Without external aids it won’t be able to beat Meta’s Cicero in Diplomacy; it won’t be able to drive a car reliably; it won’t be able to reliably guide a robot like Optimus, to be anything like as versatile as Rosie the Robot. It will remain a turbocharged pastiche generator, and a fine tool for brainstorming, and for first drafts, but not trustworthy general intelligence._

  6. _**“Alignment” between what humans want and what machines do will continue to be a critical, unsolved problem**. The system will still not be able to restrict its output to reliably following a shared set of human values around helpfulness, harmlessness, and truthfulness. Examples of concealed bias will be discovered within days or months. Some of its advice will be head-scratchingly bad._

  7. _**When AGI (artificial intelligence) comes, large language models like GPT-4 may be seen in hindsight as part of the eventual solution, but only as part of the solution**. “Scaling” alone—building bigger and models until they absorb the entire internet — will prove useful, but only to a point. Trustworthy, general artificial intelligence, aligned with human values, will come, when it does, from systems that are more structured, with more built-in knowledge, and will incorporate at least some degree of explicit tools for reasoning and planning, as well as explicit knowledge, that are lacking in systems like GPT. …_




Nobody can deny that GPT-5 is more impressive than the original ChatGPT (aka GPT 3.5), or that the latest models have more utility. LLMs have certainly come a long way. 

But we have to take seriously the _persistence_ of the core limits of the systems as well as their strengths. 

Three years and nearly a trillion dollars later almost of all it _remains true_. And it’s not just that GPT-4 was pretty much as I anticipated but that _the same problems have continued to plague every single model since_ —from GPT 4.0 to GPT 4.1 to GPT 4.5 and GPT-5 (and many others) to all the variations on Claude, all the variations on Gemini, all the variations on Grok, all the variations on llama, all the variations on DeepSeek, and so on.

To anyone who is intellectually honest, the pattern is astonishingly clear. Hundreds of models, always the same failure modes.

If GPT-5 had solved these problems, as many people imagined it would, it would in fact of enormous economic value. But it hasn’t.

So far as I know even the latest language models are still bulls in a china shop, powerful but hard to control; they still can’t reason reliably; they still don’t work reliably with external tools; they continue to hallucinate; they still can’t match domain specific models, the continue to struggle with alignment. And LLMs themselves have already resorted to using lots of external tools like calculators and python interpreters; it is already clear that they are more of a partial solution than the full solution people imagine.

For all the talk of scaling and the trillion dollars invested, the basic pattern hasn’t changed. LLMs have undoubtedly gotten quantitively better, but qualitively the core problems remain. As I wrote all way the back [in 2012, in The New Yorker](https://www.newyorker.com/news/news-desk/is-deep-learning-a-revolution-in-artificial-intelligence), [paraphrasing an older quote from the godfather of AI criticism, Hubert Dreyfus](https://quoteinvestigator.com/2024/04/20/moon-tree/), deep learning (the tech underling large language models) “is a better ladder; but a better ladder doesn’t necessarily get you to the moon.”

The only real news is that more people are _realizing_ that all this true. (See my last essay [on OpenAI cofounder Ilya Sutskever](https://garymarcus.substack.com/p/a-trillion-dollars-is-a-terrible?r=8tdk6) for one prominent example.)

The truth is that ChatGPT has never grown up, in the sense of addressing the core challenges that I have set out. And on its own (without the aid of [neurosymbolic systems](https://garymarcus.substack.com/p/how-o3-and-grok-4-accidentally-vindicated?r=8tdk6) and [world models](https://open.substack.com/pub/garymarcus/p/generative-ais-crippling-and-widespread?r=8tdk6&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false)) probably never will. Instead, the technology remains premature. We still regularly see insane, discomprehending dialogs like this example sent to me yesterday (and generated yesterday) by a friend. (Spoiler alert: in reality, [there is no seahorse emoji](https://futurism.com/chatgpt-haywire-seahorse-emoji)).

[](https://substackcdn.com/image/fetch/$s_!L_6v!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1cf7efd2-eea0-4544-a04f-afd6830376e9_1476x2060.png)

As they say in the military, “frequently wrong, never in doubt.” 

Or to put it differently, ChatGPT is bit[ like a box of chocolates, you never know what you are gonna get](https://nofilmschool.com/forrest-gump-box-of-chocolates-line). Which means, bluntly, that you can never really trust it.

My verdict, in short, is that ChatGPT is a trillion dollar experiment that has failed. 

Even with more resources than almost any experiment in history, ChatGPT has failed to solve the core cognitive problems I stressed three years ago. And because of the discrepancy between reliability and the immense costs that stem from the inherent inefficiency of a system that it dependent on absorbing internet-scale data, it has thus far failed to make profits for companies like OpenAI.

Small wonder Sutskever is urging people back to the drawing board. 

§

As I was drafting this, an engineer named [Mike Brock](https://open.substack.com/users/3232806-mike-brock?utm_source=mentions) was busy writing an assessment of LLMs of his own, a long, insightful essay entitled “[Why I am betting against AGI hype](https://substack.com/home/post/p-180206450)”. This bit encapsulates the situation well:

> When you query GPT-4, you’re not getting a system that learns from your interaction and updates its understanding in real-time. You’re getting sophisticated pattern-matching through a fixed network that was trained on historical data and then locked in place. The architecture can’t modify itself based on what it’s processing. It can’t monitor its own reasoning and adjust strategy. It can’t restructure its approach when it encounters something genuinely novel.

That was never going to work. 

§

If things do go belly-up, and the whole economy falls into recession, the single biggest culprit in my mind, will be ChatGPT’s human avatar, its bullshit-spewing CEO Sam Altman, who hyped GPT-5 endlessly for years, pretending he _knew_ that AGI was coming when in hindsight he was bluffing. In his January blog, for example, he wrote that “We are now confident we know how to build AGI as we have traditionally understood it.” Earlier he joked that AGI had been “achieved internally,” likely stoking FOMO on the part of potential investors.

Jensen Huang, CEO of Nvidia, might be culpable too, as he been increasingly drawn to overstatements and flawed arguments of his own, like this a couple weeks ago [at the last investor call](https://fortune.com/company/nvidia/earnings/q3-2026/);

> _There are three**scaling laws that are scaling at the same time**. The 1st scaling law called Pre-training continues to be very effective. And the 2nd is Post-training. Post-training basically has found incredible algorithms for improving an AI’s ability to break a problem down and solve a problem step by step. And Post-training is scaling exponentially. Basically, the more compute you apply to a model, the smarter it is, the more intelligent it is. And then the 3rd is Inference. Inference, because of chain of thought, because of reasoning capabilities, AIs are essentially reading, thinking before it answers. The amount of computation necessary as a result of those three things has gone completely exponential._

It all sounds great. But the last line really just shows that the demand on Nvidia chips (compute) – right now – is going up exponentially, not that it will continue to do so. Worse, it doesn’t prove that its premise—that exponentially increasing compute—will actually bring us to artificial general intelligence. He’s conflating costs going up exponentially with benefits going up exponentially.

In reality, the Census Bureau data already shows signs of demand tapering off, which is not consistent with a genuine exponential. And if Sustekver and I (and at this point many others) are right that scaling is largely played out, a decline in demand is sure to follow.

The hype game isn’t new; I am old enough to remember how driverless cars were similarly hyped, with immense investments of its own, few of which have panned out. Max Chafkin nailed that mania at its peak in 2022, in an essay called [Even after 100 billion [in investment] self driving cars are going nowhere](https://www.bloomberg.com/news/features/2022-10-06/even-after-100-billion-self-driving-cars-are-going-nowhere?embedded-checkout=true). 

Three years later Waymo is further along, but still not making a profit; many driverless car start-ups went out of business. And Waymo’s solution is still fragile, a demo is available only in a tiny percentage of the world’s cities, a far cry from the ubiquity that Google’s Co-CEO once promised would be achieved by 2017. And don’t get me started about Elon Musk’s long history of blown deadlines on driverless cars.

GenAI is like a rerun of that situation, an order or two of magnitude more hype, coupled with equal naïveté about what a cognitively adequate solution would actually look like, only this time with an extra decimal place, potentially a trillion dollars down the drain — and perhaps with far more collateral damage to the economy. 

Making it all more potent has been the [trillion pound baby fallacy](https://open.substack.com/pub/garymarcus/p/five-signs-that-generative-ai-is?r=8tdk6&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false), of assuming that all exponential extrapolations will hold indefinitely when in reality most don’t. AI researcher and future CMU professor [Niloofar Mireshghalleh](http://file:///var/mobile/Library/SMS/Attachments/57/07/23846711-0850-47C3-87F2-EF39AF64EB92/Screenshot%202025-11-28%20at%205.17.51%E2%80%AFPM.png) sent me some fascinating new (and not yet published) results last night, comparing progress across three AI benchmarks. One (a math test on which one might plausibly generate heaps of synthetic data) looked like it might be genuinely exponential. Another (SWE-Benech, focused on coding) looked like it had perhaps tailed off after initial exponential progress into a point of diminishing returns. A third, [on a complex task combining theory of mind and privacy that seems harder to game](https://arxiv.org/pdf/2310.17884), seemed to show a different pattern: progress that seemed slower and more linear:

[](https://substackcdn.com/image/fetch/$s_!6BeK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F90de6678-cf1b-4a69-ba6f-f5e6807f2d7c_4158x2368.png)

Anyone assuming that everything is simultaneously rising exponentially, and that it will continue to do so indefinitely, is a fool. 

§

Media boosters have played a big role in getting us here, too, often amplifying the tech CEO’s fantasies rather than challenging them. Steven Witt wrote in the New Yorker “ _[I think ChatGPT is maybe the most successful internet product in history.](https://www.newyorker.com/newsletter/the-daily/will-ai-destroy-the-planet%20planet) ”, _overlooking a series of product like Amazon.com, Facebook, and Google’s search engine that have seen broader adoption and far greater profits. Ezra Klein has recently been telling us that AGI was likely “[coming in two to three years, during Donald Trump’s second term](https://www.nytimes.com/2025/03/04/opinion/ezra-klein-podcast-ben-buchanan.html?smid=nytcore-ios-share)” alluding to industry sources (with vested interests). As discussed here last week, that speedy timeline was recently[ walked back by its leading advocate](https://garymarcus.substack.com/p/breaking-the-ai-2027-doomsday-scenario?r=8tdk6), and [refuted in an essay by Yoshua Bengio and 30 other authors ](https://www.nytimes.com/2025/03/04/opinion/ezra-klein-podcast-ben-buchanan.html?smid=nytcore-ios-share)including myself. 

Likewise, NYT columnist Kevin Roose wrote in February 2023 that he felt a “[sense of awe](https://www.nytimes.com/2023/02/08/technology/microsoft-bing-openai-artificial-intelligence.html?smid=nytcore-ios-share) [when he] started using the new, [ChatGPT]-powered Bing”. (Anybody remember Bing?) More recently, Roose promised “with a few keystrokes, amateurs can now build products that would have previously required teams of engineers”, which has thus far not come close to true. (Amateurs can in fact now build _prototypes_ , but the auto-generated code tends to be shaky and few amateurs can make those prototypes robust.) Too much industry hype is repeated with too little skepticism, driving up market valuations on analyses that often feel to me superficial. 

§

The market is maybe finally catching on. Nvidia’s stock price, which had been rising at incredible speed for the last few years, fell 16% in November; CoreWeave (which traffics in Nvidia chips, fell by nearly half. And Oracle, which rocketed on the news that it had made a deal with OpenAI, dropped by about 26% in November, and (close to 50% since September 11 when I declared the response to that deal to be [“peak bubble”](https://open.substack.com/pub/garymarcus/p/peak-bubble?r=8tdk6&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false).

OpenAI itself isn’t traded on the open market, but if it had, it’s likely that it, too, would have fallen over the last month, for all the reasons I described, and one more: they don’t have moat. ChatGPT was pretty easily replicated; there wasn’t all that much secret sauce. In March 2024 [I warned that they would lead to pileup of similar models that were short of many fantasies about GPT-5 and hence to price wars](https://x.com/GaryMarcus/status/1766871625075409381?s=20) with little profit, And so far it has; large language models have become a commodity; LLM profits outside of Nvidia are hard to find. [OpenAI itself is losing billions every month](https://techstartups.com/2025/10/31/openai-is-hemorrhaging-billions-microsoft-filing-reveals-openai-lost-11-5-billion-last-quarter-amid-ai-bubble-hype/). But worse than that, from OpenAI’s perspective, Google seems in the last month to have overtaken them, with Gemini 3, which by many benchmarks is better than GPT-5. Google’s stock is up; if OpenAI had stock, I imagine it would be down. Sam Altman himself acknowledged (in a leaked memo) that the company was [facing “temporary economic headwinds”](https://www.theinformation.com/articles/openai-ceo-braces-possible-economic-headwinds-catching-resurgent-google?utm_source=ti_app&rc=dcf9pt).****

The reality is OpenAI has ridden to a $500 billion valuation on hopes, not profits. And those hopes are slipping away, as usage declines and others catch up.

In the end LLMs will continue to exist, no matter what; they will get cheaper. And they will find some utility (indeed they are already have). But they will never be AGI, and they never be much more than commodity. 

§

What _is_ ChatGPT best for? The natural home for ChatGPT turns out to be… demos. At its core, it approximates past data, albeit with a superficial understanding. In many domains. answers might be like 80% correct and 20% absurd, but without a whole lot of task-specific engineering required. In some domains, like autocomplete for coders, who are in the loop and constantly testing what they write, that’s fine. 

Ultimately though, what LLMs are great at seeming is _plausible_ – while being much less good at getting their facts straight. 

The gulf between how impressive something *seems* and how useful something *is* has never been greater.

§

Although ChatGPT became famous three years ago, the core technology behind ChatGPT isn’t actually three years old; depending on how you count, it’s more like 7 or 8. The core technology, known as the Transformer, was developed by Google in 2017. The first version of GPT (short for generative pretrained transformer), known now as [GPT-1 ](https://en.wikipedia.org/wiki/GPT-1) was released in June 2018. OpenAI and others have been steadily working at scaling that technology ever since. (People were writing glorifying articles about GPT-3 as far back as [2020.](https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3))

In some ways, GPT-5 is more capable than most 7 or 8 year olds. It’s far more likely to be able to give the answer to random trivia question (such as who was the first of Henry VIII’s wives), and far more likely to be able to write sound python code. 

In others, though, there is still something really fundamentally missing. ChatGPT obviously lacks the reliability of calculators (which is something the field should aspire to), but more than that the hallucinations and occasional bizaare errors should be shocking given that they (unlike seven-years-olds) have swallowed the entire internet. As Sutskever said last week, LLMs “ _somehow just generalize dramatically worse than people. And it’s super obvious. That seems like a very fundamental thing”_ – perhaps an epitaph for the ChatGPT era (and not coincidentally, what I have been trying to say all along).

More than that, any normal seven-year old develops a rich model of the world, including the objects they see, the people they interact with and so on, and even how their bodies work. GPT is still just faking it. 

I wrote this [about my daughter in July 2017](https://www.nytimes.com/2017/07/29/opinion/sunday/artificial-intelligence-is-stuck-heres-how-to-move-it-forward.html), eight years ago, in a New York Times op-ed, just before ChatGPT was on the scene, when my daughter was 3. 

> _Although the field of A.I. is exploding with microdiscoveries, progress toward the robustness and flexibility of human cognition remains elusive._
> 
> _Not long ago, for example, while sitting with me in a cafe, my 3-year-old daughter spontaneously realized that she could climb out of her chair in a new way: backward, by sliding through the gap between the back and the seat of the chair. My daughter had never seen anyone else disembark in quite this way; she invented it on her own - and without the benefit of trial and error, or the need for terabytes of labeled data._
> 
> _Presumably, my daughter relied on an implicit theory of how her body moves, along with an implicit theory of physics — how one complex object travels through the aperture of another. I challenge any robot to do the same._
> 
> _A.I. systems tend to be passive vessels, dredging through data in search of statistical correlations; humans are active engines for discovering how things work._

People are now very actively trying to put variations of large language models into humanoid robots, but I can’t imagine any could do what my daughter was able to do then, let alone what she can do nowadays as a curious, precocious eleven-year-old. 

If you doubt me, or just want a laugh, check out reviews by [Joanna Stern](https://youtu.be/f3c4mQty_so?si=TXo_sZTKKpk9fOI_) and [Marques Brownlee](https://youtu.be/j31dmodZ-5c?si=-YdSIXZg58ScvoUt) of the forthcoming NEO humanoid robot, which remain slow and heavily dependent on human teleoperations, or check out the poor robot that [face-planted at its Moscow debut earlier this month](https://youtu.be/UuUSR8TyZDE?si=HpRm-rv57Q7gt3OR), seconds after its unveiling.

§

For the love of Darwin, please let’s spend the next eight years considering _new_ approaches, not tanking the economy on more of the same. 

ChatGPT has had a good (though not great) run; it’s time for something new. I am for it. Ilya is for it. The time has come.

# 
