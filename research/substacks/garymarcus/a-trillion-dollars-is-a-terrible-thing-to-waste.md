---
title: "A trillion dollars is a terrible thing to waste"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/a-trillion-dollars-is-a-terrible"
---

Breaking news from famed machine learning researcher Ilya Sutskever:

[](https://substackcdn.com/image/fetch/$s_!XMEf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F819a7586-0a0a-4713-89e8-4255ca710295_1253x1147.png)

Below is another summary of a just-released [interview](https://www.dwarkesh.com/p/ilya-sutskever-2) of his that is making waves, a bit more technical. Basically Sutskever is saying that scaling (achieving improvements in AI through more chips and more data) is flattening out, and that we need new techniques; he is even open to [neurosymbolic](https://open.substack.com/pub/garymarcus/p/how-o3-and-grok-4-accidentally-vindicated?r=8tdk6&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) techniques, and innateness. He is clearly not forecasting a bright future for pure large language models.

[](https://substackcdn.com/image/fetch/$s_!R9kz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F604596b2-f33f-4364-bfb3-c787ffac18df_1349x1505.jpeg)

Sutskever also said that “ _The thing which I think is the most fundamental is that these models somehow just generalize dramatically worse than people. And it’s super obvious. That seems like a very fundamental thing._ ”

Some of this may come as news to a lot of the machine learning community; it might be surprising coming from Sutskever, who is an icon of deep learning, having worked, inter alia, on the critical 2012 paper that showed how much GPUs could improve deep learning, the foundation of LLMs, in practice. He is also a co-founder of OpenAI, considered by many to have been their leading researcher until he departed after a failed effort to oust Sam Altman. 

But none of what Sutskever said should actually come as a surprise, especially not to readers of this Substack, or to anyone who followed me over the years. Essentially _all_ of it was in my pre-GPT 2018 article “ _[Deep learning: A Critical Appraisal](https://arxiv.org/pdf/1801.00631)_ ”, which argued for neurosymbolic approaches to complement neural networks (as Sutskever now is), for more [innate](https://arxiv.org/abs/1801.05667) (i.e., built-in, rather than learned) constraints (what Sutskever calls “new inductive constraints”) and/or in my 2022 “ _[Deep learning is hitting a wall](https://nautil.us/deep-learning-is-hitting-a-wall-238440/)_ ” evaluation of LLMs, which explicitly argued that the Kaplan scaling laws would eventually reach a point of diminishing returns (as Sutskever just did), and that problems with hallucinations, truth, generalization and reasoning would persist even as models scaled, much of which Sutskever just acknowledged. 

Subbarao Kambhampati, meanwhile, has been arguing or years about [limits on planning with LLMs](https://cotopaxi.eas.asu.edu). Emily Bender has been saying for ages that an excess focus on LLMs has been “sucking the oxygen from the room” relative to other research approaches. The [unfairly dismissed Apple reasoning paper](https://open.substack.com/pub/garymarcus/p/a-knockout-blow-for-llms?r=8tdk6&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) laid bare the generalization issues; another paper called “[Is Chain-of-Thought Reasoning of LLMs Mirage? A Data Distribution Lens](https://arxiv.org/abs/2508.01191v3)” put a further nail in the LLM reasoning and generalization coffin. 

_None_ of what Sutskever said should come as a surprise. A machine learning researcher at Samsung, Alexia Jolicoeur-Martineau summed the situation up well on X, Tuesday, following the release of the Sutskever’s interview:

[](https://substackcdn.com/image/fetch/$s_!zSvc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7e70d67c-7675-4986-a1cc-dd57c78bcbc4_1263x367.png)

§

Of course it ain’t over til it’s over. Maybe pure scaling (adding more data and compute without fundamental architectural changes) _will_ somehow magically yet solve what researchers as such Sutskever, LeCun, Sutton, Chollet and myself no longer think it could. 

And investors may be loathe to kick the habit. As Phil Libin put it presciently last year, scaling—not the generation of new ideas—is what investors know best

[](https://substackcdn.com/image/fetch/$s_!QFgM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff01c2271-6378-4e97-a0bc-70b79df4acb1_1195x1503.jpeg)

And it’s not just that venture capitalists know more about scaling businesses than inventing new ideas, it’s for the venture capitalists that have driven so much of field, scaling, even if it fails, has been a great run: it’s been a way to take their 2% management fee investing someone else’s money on plausible-ish sounding bets that were truly massive, which makes them rich no matter how things turn out. To be sure, the VC get even richer still if the investments pan out, to be sure. but they are covered either way; even if it all falls apart, the venture capitalists themselves will become wealthy from the management fees alone. (It is their clients, such as pension funds, that will take the hit). So venture capitalists may continue to support LLM mania, at least for a while.

But let’s suppose for the sake of argument that Sutskever and the rest of us are correct, and that AGI will never emerge straight from LLMs, and that to a certain extent that they have run their course, and that we do in fact need new ideas. 

The question then becomes, what did it cost the field and society that it took so long for the machine learning mainstream to figure out what some of us, including virtually the entire neurosymbolic AI community had been saying for years?

§

The first and most obvious answer is money, which I estimate, back of the envelope as (roughly) a trillion dollars, much of it on Nvidia chips and massive salaries. (Zuckerberg has apparently hired some machine learning experts at salaries of $100,000,000 a year). 

According to Ed Zitron’s calculations, “[Big Tech Needs $2 Trillion In AI Revenue By 2030 or They Wasted Their Capex](https://www.wheresyoured.at/big-tech-2tr/)”. If Sutskever and I are right about the limits of LLMs, the only way to get to that $2T is to invent new ideas.

If the definition of insanity is doing the same thing over and over and expecting different results, trillion dollar investments in ever more expensive experiments aiming to reach AGI may be delusional to the highest degree.

To a first approximation, all the big tech companies, from OpenAI to Google to Meta to xAI to Anthropic to several Chinese companies, keep doing the same experiment over and over: building ever larger LLMs in hopes of reaching AGI. 

It has never worked. Each new bigger, more expensive model ekes out measurable improvements, but returns appear to be diminishing (that’s what Sutskever is saying about [the Kaplan laws](https://arxiv.org/abs/2001.08361)) and none of these experiments has solved core issues around hallucinations, generalization, planning and reasoning, as Sutskever too now recognizes. 

But it’s not just that a trillion dollars or more might go down the drain, but that there might be considerable collateral damage, to the rest of society, both economic and otherwise (e.g., in terms of how [LLMs have undermined college education](https://nymag.com/intelligencer/article/openai-chatgpt-ai-cheating-education-college-students-school.html)). As Rogé Karma put in a recent article in The Atlantic, “[The entire U.S. economy is being propped up by the promise of productivity gains that seem very far from materializing.](https://www.theatlantic.com/economy/archive/2025/09/ai-bubble-us-economy/684128/)” 

To be fair, nobody knows for sure what the blast radius would be. If LLM-powered AI didn’t meet expectations and became valued less, who would take the hit? Would it just be the “limited partners” like pension funds who entrusted their money with VC firms? Or might the consequences be much broader? Might banks go down with the ship, in 2008-style liquidity crisis,possibly forcing taxpayers to bail them out? In the worst case, the impact of a deflated AI bubble could be immense. (Consumer spending, much of it fueled by wealthy people who could a hit on the stock market, might also drop, a recipe for recession.) 

Even the White House has admitted concerns about this. As the White House AI and Crypto Czar David Sacks himself put it earlier this week, referring to a Wall Street Journal analysis, “Al-related investment accounts for half of GDP growth. A reversal [in that] would risk recession.” 

Quoting from Karma’s article in The Atlantic :

> That prosperity [that GenAI was supposed to deliver] has largely yet to materialize anywhere other than their share prices. (The exception is Nvidia, which provides the crucial inputs—advanced chips—that the rest of the Magnificent Seven are buying.) As _The Wall Street Journal_ reports, Alphabet, Amazon, Meta, and Microsoft have seen their [free cash flow](https://www.wsj.com/economy/the-ai-booms-hidden-risk-to-the-economy-731b00d6) decline by 30 percent over the past two years. By one [estimate](https://www.wheresyoured.at/the-haters-gui/), Meta, Amazon, Microsoft, Google, and Tesla will by the end of this year have collectively spent $560 billion on AI-related capital expenditures since the beginning of 2024 and have brought in just $35 billion in AI-related revenue. OpenAI and Anthropic are [bringing](https://www.reuters.com/business/anthropic-hits-3-billion-annualized-revenue-business-demand-ai-2025-05-30/) in lots of revenue and are growing fast, but they are still [nowhere](https://www.reuters.com/technology/artificial-intelligence/openai-does-not-expect-be-cash-flow-positive-until-2029-bloomberg-news-reports-2025-03-26/?utm_source=chatgpt.com) [near](https://ca.finance.yahoo.com/news/anthropic-projects-soaring-growth-34-002016322.html?utm_source=chatgpt.com) profitable. Their valuations—roughly [$300 billion](https://www.nytimes.com/2025/08/01/business/dealbook/openai-ai-mega-funding-deal.html) and [$183 billion](https://www.reuters.com/business/anthropics-valuation-more-than-doubles-183-billion-after-13-billion-fundraise-2025-09-02/), respectively, and [rising](https://www.nytimes.com/2025/08/19/technology/openai-chatgpt-stock-sale-valuation.html)—are many multiples higher than their current revenues. (OpenAI [projects](https://www.bloomberg.com/news/articles/2025-03-26/openai-expects-revenue-will-triple-to-12-7-billion-this-year) about $13 billion in revenues this year; [Anthropic](https://www.theinformation.com/articles/anthropic-projects-soaring-growth-to-34-5-billion-in-2027-revenue), $2 billion to $4 billion.) Investors are betting heavily on the prospect that all of this spending will soon generate record-breaking profits. If that belief collapses, however, investors might start to sell en masse, causing the market to experience a large and painful correction.
> 
> …
> 
> The dot-com crash was bad, but it did not trigger a crisis. An AI-bubble crash could be different. AI-related investments have already [surpassed](https://paulkedrosky.com/honey-ai-capex-ate-the-economy/) the level that telecom hit at the peak of the dot-com boom as a share of the economy. In the first half of this year, business spending on AI added more to GDP growth than all consumer spending _combined_. Many experts believe that a major reason the U.S. economy has been able to weather tariffs and mass deportations without a recession is because all of this AI spending is acting, in the [words](https://paulkedrosky.com/honey-ai-capex-ate-the-economy/) of one economist, as a “massive private sector stimulus program.” An AI crash could lead broadly to less spending, fewer jobs, and slower growth, potentially dragging the economy into a recession. The economist Noah Smith [argues](https://www.noahpinion.blog/p/will-data-centers-crash-the-economy) that it could even lead to a financial crisis if the unregulated “private credit” loans funding much of the industry’s expansion all go bust at once.

The whole thing looks incredibly fragile. 

§

To put it bluntly, the world has gone “all in” on LLMs, but, as Sutskever’s interview highlights, there are many reasons to doubt that LLMs will ever deliver the rewards that many people expected. 

The sad part is that most of the reasons have been known – though not widely accepted – for a very long time. It all could have been avoided. But the machine learning community has arrogantly excluded other voices, and indeed whole other fields like the cognitive sciences. And we all now may be about to pay the price. 

An old saying about such follies is that “six months in the lab can you save you an afternoon in the library”; here we may have wasted a trillion dollars and several years to rediscover what cognitive science already knew.

A trillion dollars is a terrible amount of money to have perhaps wasted. If the blast radius is wider it could be a lot more. It is all starting to feel like a tale straight out of Greek tragedy, an avoidable mixture of arrogance and power that just might wind up taking down the economy. 
