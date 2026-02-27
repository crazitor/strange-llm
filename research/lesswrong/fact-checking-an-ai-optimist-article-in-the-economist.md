---
title: "Fact-checking an AI optimist article in The Economist"
author: "ToSummarise"
date: "2026-02-23"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/N8HtJC75T33bbKuFX/fact-checking-an-ai-optimist-article-in-the-economist"
score: 35
votes: 17
---

On 26 January 2026, The Economist (a very well-respected, mainstream publication) published an optimistic [article](https://www.economist.com/finance-and-economics/2026/01/26/why-ai-wont-wipe-out-white-collar-jobs) arguing that AI won’t displace white collar jobs. Specifically, the article claimed:

> *Rather than wipe out office jobs, artificial intelligence will expand their scope and raise their value.*
> 
> — “[Why AI won’t wipe out white-collar jobs](https://www.economist.com/finance-and-economics/2026/01/26/why-ai-wont-wipe-out-white-collar-jobs)” in *The Economist* (26 Jan 2026)

They followed that up with [a podcast on 19 February](https://www.economist.com/podcasts/2026/02/19/the-splitting-image-yoon-verdict-will-deepen-divisions) making the same points. Some of the numbers in that article (and repeated in the podcast), pinged my BS detector. I was particularly sceptical of their claim that “America has … 21% more paralegals than three years ago”, as well as the figures in the below infographic:

![Infographic from The Economist showing change in US employment between 2022 and 2025 for selected roles](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/e7b584d37c08b8e7e481b598e0e9fba47787438d66d4679d.jpg)

So, I decided to look up the data on [FRED](http://fred.stlouisfed.org/), which also shows data from the Bureau of Labour Statistics, at an annual frequency. I found three significant problems:

1.  There was **no baseline** given for comparison
2.  The roles appear to be **cherry-picked**
3.  Some of the **data does not seem reliable**

**1\. No baseline**
-------------------

The first issue is that The Economist had shown job growth rates for certain occupations between 2022-2025, without providing a baseline for comparison. How do we know the growth in these white-collar occupations didn’t just reflect growth in the US economy more generally? How did job growth compare to previous 3-year periods?

So I compared the 2022-2025 job growth figures with the 2016-2019 figures for the same roles. (I skipped over 2019-2022 because of Covid.) Here’s what I found (units are in thousands of persons):

| Occupation | 2016 | 2019 | Change (%) | 2022 | 2025 | Change (%) | Difference |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Business and Financial operations](https://fred.stlouisfed.org/data/LEU0254474300A) | 6195 | 6748 | 8.93% | 7799 | 8463 | 8.51% | -0.41% |
| [Computer and mathematical occupations](https://fred.stlouisfed.org/data/LEU0254476900A) | 4104 | 4947 | 20.54% | 5733 | 6297 | 9.84% | -10.70% |
| [Nurse practitioners](https://fred.stlouisfed.org/data/LEU0254487900A) | 2498 | 2640 | 5.68% | 2753 | 2896 | 5.19% | -0.49% |
| [Paralegals and legal assistants](https://fred.stlouisfed.org/data/LEU0254483600A) | 351 | 364 | 3.70% | 388 | 378 | -2.58% | -6.28% |
| [Computer programmers](https://fred.stlouisfed.org/data/LEU0254477100A) | 403 | 425 | 5.46% | 422 | 352 | -16.59% | -22.05% |
| [Software developers](https://fred.stlouisfed.org/data/LEU0254477200A) | 1351 | 1714 | 26.87% | N/A | N/A |   |   |
| [Customer service representatives](https://fred.stlouisfed.org/data/LEU0254500400A) | 1850 | 1977 | 6.86% | 2097 | 1928 | -8.06% | -14.92% |
| [Office and administrative support](https://fred.stlouisfed.org/data/LEU0254498800A) | 13866 | 13954 | 0.63% | 12808 | 12812 | 0.03% | -0.60% |

The picture is considerably bleaker when you compare job growth over the last 3 years with that in 2016-2019. In **every chosen category**, job growth was weaker between 2022-2025 compared to 2016-2019. For example, while “Computer and mathematical occupations” showed 9.8% job growth between 2022-2025, this was actually a steep *drop* from 20.54% job growth between 2016-2019.

To be fair, there are other differences between the 2016-2019 period and the 2022-2025 period. Perhaps the 2022-2025 saw slower job growth in tech because firms had overhired during the pandemic, rather than because of AI. But the weaker job growth was not confined to tech roles. This is by no means definitive proof that AI is displacing white-collar jobs — but it is hardly reassurance that these jobs are safe.

**2\. Cherry-picked data**
--------------------------

You may notice that the roles in my above table do not exactly match the roles in The Economist’s infographic. This is because the FRED website only provides data for certain broad categories, and The Economist seems to have cherry-picked a couple of small subcategories that showed particularly strong job growth.

According to their infographic, the top 3 roles that showed the biggest job growth were:

*   Business-operations specialists;
*   Mathematical science operations; and
*   Project-management specialists.

However, under the BLS’s [Standard Occupational Classification system](https://www.bls.gov/oes/2023/may/oes_stru.htm#13-0000), both Business-operations specialists (13-1000) and Project management specialists (13-1082) are subsets of the much broader “Business and Financial Operations” category (13-0000). In May 2023, [that broader category](https://www.bls.gov/oes/2023/may/oes131082.htm) was **more than 10 times larger** than the [Project management specialists](https://www.bls.gov/oes/2023/may/oes131082.htm) subcategory, so is likely to be much less noisy. I suspect much of the “growth” in subcategories was actually just caused by employment shifting between categories. In particular, the “Project management specialists” category was [only added in 2018](https://www.bls.gov/soc/2018/soc_2018_whats_new.pdf) and saw around ~30% “growth” according to The Economist’s infographic. But since the broader “Business and Financial Operations” category saw < 10% growth, I suspect much of the growth in Project management specialists came at the expense of other subcategories.

Similarly, Mathematical science operations (15-2000) is a subset of the much broader “Computer and Mathematical Occupations” category (15-0000). There were barely 370,000 workers in the former subcategory in 2023. The broader category had [over 5 million](https://www.bls.gov/oes/2023/may/oes150000.htm).

**3\. Data does not seem reliable**
-----------------------------------

It was the Economist’s claim that paralegals had seen +21% job growth over the 2022 to 2025 period that piqued my interest in the first place. As my table above shows, the the FRED data showed a -2.6% *decline* in paralegal jobs between 2022 and 2025.

Now, I’m not saying The Economist just made up their figures. When I first emailed them about this figure, they said they had used a 6-month moving average of monthly disaggregated household data from [EPI Microdata Extracts](https://microdata.epi.org/), which might explain the difference. This microdata is not very user-friendly, and I am not a data scientist, which is why I used the FRED summaries of the annual figures instead. The Economist may well have legitimately gotten a different figure using 6-month moving averages for the microdata. 

But the size of this difference should be enough to make one question the reliability of the data. If the data is noisy enough to produce a gap of almost 25 percentage points depending on whether you take a 6-month or annual average, one should hesitate before drawing any conclusions from it.

**Conclusion**
--------------

On 8 February, I wrote a second email to The Economist explaining my concerns (my first email just asked about their data source). To date, I haven’t received a response to my concerns.

Overall, I felt pretty disappointed. I’ve followed The Economist for over 10 years and pay to subscribe to their podcasts. I know that The Economist has a certain ideological bent (classical liberalism, pro-market), so I wasn’t surprised to see them publish a techno-optimist article arguing that worries about AI displacing jobs were overblown, and that new tasks will emerge. The future is inherently hard to predict, and reasonable people can disagree on how bad the labour disruption may get.

But fairly interpreting statistics about the *past* shouldn’t be that difficult, and the issues above are (imo) pretty glaring. I had always considered The Economist to be a reasonably credible source of news, with high editorial and fact-checking standards. I’m not writing them off entirely — I still think they’re better than most news outlets — but I have certainly downgraded my view of them.