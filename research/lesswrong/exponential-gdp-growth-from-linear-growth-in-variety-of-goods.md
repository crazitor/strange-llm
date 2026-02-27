---
title: "Exponential GDP growth from linear growth in variety of goods"
author: "Will_Howard"
date: "2026-02-23"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/FmayBpqJbrmyrEiKx/exponential-gdp-growth-from-linear-growth-in-variety-of"
score: 4
votes: 5
---

In an interview, Philip Trammell presented a model of the economy where growth is dominated by “mid-life” technologies, which are mature enough to have a meaningful share of GDP, but are still growing rapidly:

> you get this hump: new goods - small share; goods that have been around for a medium length of time that we’re mediumly productive at - high share, they dominate GDP; old goods like food - small share. So we’re continually going through this hump.

— Philip Trammell, [Epoch After Hours](https://epoch.ai/epoch-after-hours/economics-of-ai), around 00:56:00

For context, GDP growth is calculated like this:

$$
g = \sum_i \text{GDP\_share}_i \times \text{growth\_rate}_i
$$

*This is a sum over types of good*[^soktdm3zg9]* (e.g. motor vehicles & parts, chemical products).*

The idea is that for new goods, growth is high but GDP share is low. For mature goods, GDP share may be high, but growth is flat because demand is satiated[^c5n05pu2bj]. As a result, the growth number is dominated by these mid-life goods. Some examples of goods that fit each of these stages from recent years:

*   **New:** Quantum computing (~$2B, 0.002% GDP), humanoid robots (~$2B, 0.002% GDP).
*   **Mid-life:** EVs (~0.8% GDP, 20% growth), conventional cloud computing (~0.6% GDP, 20% growth)
*   **Mature:** Smartphones (growth ~3-5%, was explosive 2007-2015), personal computers (the 1990s mid-life tech, now ~1% growth), landline telephones (actively dying, -16% subscriptions in 2024)

![](https://substackcdn.com/image/fetch/$s_!5col!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7e7b9ac7-c158-4dfa-b99b-963edffbe469_1800x1050.png)

As stated this is just a toy model that bears some resemblance to the real economy. As far as I can find there has been no quantitative study evaluating this. The point of this post is to show that if you work this through, it can easily produce exponential GDP growth from linear growth in the number of goods available, without these goods being particularly exceptional. For this and other reasons I’ve become convinced that the way GDP (growth) is calculated makes it quite far from the common sense conception of it as “amount of stuff you can buy” or “amount of impact you can have on the world”.

Example: A linear increase in number of goods produces exponential GDP growth
=============================================================================

A scenario that is a plausible description of the real economy generates this result. At `t = 0`, suppose the GDP share is:

*   60% “necessities”: food, housing etc. These have flat (0%) growth and flat GDP share (practically this means demand is satiated or supply is limited)
*   40% “other mature goods”: things like TVs, mechanical pencils, fidget spinners. For simplicity suppose that there is a large number of these (small GDP share each), and they are all mature to begin with (0% growth)

In this economy growth is 0% overall. Suppose now that a new good type is invented, the Schmartphone, which follows this trajectory:

*   `t = 0`: It is invented, has a high price and fast growth among early adopters, but still ~0% GDP share
*   `t = 1` to `t = 10`: Mid-life phase: It is adopted by more people as they learn about it. Plus, further development means the price comes down and/or the product quality increases, driving demand from people previously on the fence. During this phase it has moderate GDP share (say 10%[^r5zw80i9ww]), and still high growth (say 50% YoY)
*   `t = 10` onwards: Saturation and commodification: Eventually everyone who wants one has one and replacements are sold at a constant rate, so growth falls to 0% YoY. You can also suppose that continued innovation + amortising the initial investment drives the price down until Schmartphones are <1% of GDP

From `t = 1` to `t = 10` this economy had 5% growth overall. (50% growth) * (10% GDP share) for Schmartphones, (0% growth) * (90% GDP share) for everything else. Over the 10 years, the addition of this new good would ~1.6x overall GDP. 50% YoY growth for 10 years means that annual sales of Schmartphones would 60x over the time period, while maintaining constant GDP share. This is not crazy, but obviously for the real economy you’d need slightly lower numbers to be realistic (and the real peak GDP share of smartphones was more like 1%).

Now suppose at `t = 10` another new good type is invented (the Schmair Fryer), and goes through the same cycle: Early adoption, mid-life high growth high GDP share phase, saturation and merging into the mass of “other mature goods”. Again from `t = 11` to `t = 20` the economy would have 5% growth, 1.6x-ing again by `t = 20`.

You can repeat this indefinitely, and after 5 new goods GDP would be 11.5x its original size. After 10 it would be 132x, and so on.

The growth experienced by consumers however would be linear by any common sense understanding of the situation. At `t = 0`, you work all day to spend 60% of your income on necessities, and 40% on several of say 100 “other mature goods”. At `t = 100` you have 110 to choose from, but GDP has apparently increased by 132x. You do buy and enjoy these new goods (they must be good to have accounted for 10% of GDP during their mid-life phase), but it’s not the same as being able to buy 132x what you could at `t = 0`, and your real economic constraint of buying necessities is unaffected.

Relationship to the real economy
================================

As mentioned above, it seems that there’s no existing research that can definitively say whether this is a description of the real economy or not, so I’m keeping my cached view as “individual economic power grows exponentially over time” for now.

James Bessen’s [”AI and Jobs: The Role of Demand”](https://www.nber.org/papers/w24235) documents this hump-shaped pattern empirically for textiles, steel, and automotive over 200 years of data. Each shows a rise in employment and expenditure share during its growth phase, followed by a decline as the industry matures.

I tried to do a similar exercise with recent technologies. Smartphones fit the pattern nicely: explosive growth from 2007-2015, peak GDP share around 1-1.5%, now essentially flat. Cloud computing looks mid-hump right now at ~0.6% of GDP and 20% growth. EVs similarly at ~0.5% of GDP and 20% growth. Personal computers are clearly post-hump, having peaked around 2010. These are very rough so I think it’s not particularly worth including the sources. To make the case strongly, you would need to categorise all sources of GDP growth and fit them into this framework.

Furthermore there’s a question of whether this exponential-from-linear effect can apply to other methods for calculating GDP, as the “chain weighting” method above was introduced fairly recently (1996 in the US). I’m not sure about this. From spending a few minutes thinking about it, I think a similar argument applies to “fixed base year” GDP calculations. In that case a new good is counted going forward at whatever price it entered the market at. Two things would need to be true to produce a result that is similar to the one above, with a similar newly-invented good:

*   The typical price of new products is proportional to people’s incomes (fixed % of GDP pie), rather than staying at a fixed real dollar value. E.g., in 1950 a new gizmo would enter the market at 50 real dollars, whereas in 2026 a new gadget would enter at 500 real dollars, because people’s real incomes (according to GDP) have gone up
*   The product starts being counted when the price is high and adoption is low, so it’s counting people who are unusually rich or get unusual utility out of the product. As the product is adopted more widely, it’s counted towards GDP at this initial price, but this is not a fair representation of utility because the non-early-adopters buying it would never consider buying it at the initial price (and don’t get that much value out of it).

Bonus example: *No* increase in number of goods produces exponential GDP growth
===============================================================================

Here’s a more extreme version that doesn’t even require new goods to be invented. I don’t believe this looks that much like the real economy, but it’s nice to illustrate the point that GDP growth can become divorced from common sense. Suppose you have one good that goes in and out of fashion, in an economy where everything else is static (0% growth, though GDP shares can move around to make room for this fashionable good):

1.  The good becomes fashionable. Its price rises until it goes from 1% to 10% of GDP. No change in quantity sold, so no GDP growth during this phase.
2.  At 10% GDP share, more suppliers enter the market and the quantity sold doubles. GDP share stays constant throughout this, meaning prices halve. GDP contribution: 10% share × 100% growth = **+10% GDP growth**.
3.  Too many suppliers enter the market, prices fall until the good is 1% of GDP. Again no quantity change, no GDP growth.
4.  The good goes out of fashion. At 1% GDP share, quantity sold halves back to where it started. GDP contribution: 1% share × -50% growth = **-0.5% GDP growth**.

Over the full cycle, the good’s quantity and GDP share are back where they started, but GDP has grown by ~9.5%. The expansion happened at high share (10%) and the contraction at low share (1%), so they don’t cancel out. You can repeat this indefinitely for persistent GDP growth from a fixed number of goods with no net change in quantities. I think this maps onto what is called [“Chain drift”](https://www.bea.gov/research/papers/2005/chain-drift-leading-superlative-indexes) in the economics literature.

[^soktdm3zg9]: Actually I lied, only 30% of the GDP calculation in the US is from countable goods. Another 50% is from services where there is an agreed price index, the logic of this post goes through for that case as well (as long as new services are invented, even if they fit within an existing category). The other 20% is services with no agreed price index, in which case some kind of input-based accounting is used. I’m not sure if the post’s logic works there. 

[^c5n05pu2bj]: Additionally, further innovation or amortisation of earlier investments will tend to just drive the price down, which will also lower GDP share. Though in practice we see some mature goods (housing) that have persistently high GDP share and some which have it frittered away over time (televisions). 

[^r5zw80i9ww]: This requires the GDP share of our “necessities” + “mature innovated goods” to shrink to 90% during this period. In a more continuous case you can imagine that there is a gradual price reduction among “mature innovated goods” which makes room for this (but no growth in the number of these goods due to saturated demand, so still 0% GDP growth from this). It could also be due to people temporarily working more hours to create the new type of good.