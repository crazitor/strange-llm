---
title: "The Pareto curve of freedom"
author: "Scott Aaronson"
date: "Wed, 30 Jul 2008"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=342"
---

[](https://scottaaronson.blog/freedom.jpg)

Inspired by the discussion of my [fable](https://scottaaronson.blog/?p=341), and specifically a [comment](https://scottaaronson.blog/?p=341#comment-22669) of Ronald de Wolf, today I decided to do some amateur political science. Specifically, I created a scatterplot that ranks 156 of the world's countries (those for which data was available) along two axes:

  1. Their "political freedom", as rated by [Freedom House](http://www.freedomhouse.org/template.cfm?page=1)'s [2008 Freedom in the World survey](http://www.freedomhouse.org/template.cfm?page=351&ana_page=342&year=2008). This is a 0-to-100 scale, which includes 60 points for various civil liberties (such as freedom of speech and freedom of religion) and 40 points for various political rights (such as transparent elections). (Note that I used the raw scores, rather than the less informative 1-to-7 rankings.)
  2. Their "economic freedom", as rated by the [Heritage Foundation](http://www.heritage.org/) and _[Wall Street Journal](http://online.wsj.com/public/us)_ 's [2008 Index of Economic Freedom](http://www.heritage.org/research/features/index/index.cfm). This is also a 0-to-100 scale, which ranks the sorts of things libertarians and laissez-faire economists love: free trade, deregulation, privatization, low taxes and tariffs, low or nonexistent minimum wage, etc.



The motivation was simple. Among educated people, political freedom is universally acknowledged as both good and important, whereas economic freedom (as defined by Heritage and the _Wall Street Journal_) is not. Indeed, a huge fraction of the disagreement between liberals and conservatives--at least over economics--seems to boil down to a single question: _Is economic freedom (again, as defined by Heritage/WSJ) the friend or enemy of political freedom?_

On one side of this question, we have Milton Friedman:

> Historical evidence speaks with a single voice on the relation between political freedom and a free market.  I know of no example in time or place of a society that has been marked by a large measure of political freedom that has not also used something comparable to a free market to organize the bulk of economic activity. (From _[Capitalism and Freedom](http://www.amazon.com/gp/product/0226264211/ref=cm_cr_pr_product_top)_ , quoted by Wu and Davis)

On the other side we have anti-globalization activists like Naomi Klein (author of _The Shock Doctrine_), who say that "economic freedom" simply means the freedom of multinational corporations to exploit the public, and as such is _incompatible_ with political freedom.  Klein argues that free-market economic policies almost never win democratically, and hence the ruling elites have had to force these policies on unwilling populations using strong-arm tactics of the World Bank and IMF, cynical exploitation of wars, hurricanes, and other disasters, and (when all else fails) state-sponsored torture and murder.

My modest goal was to use the available cross-country data to test these two hypotheses. But before we get to that, a few caveats.

**Caveat #1:** I know full well that the questions I'm talking about have already been studied in great detail by professional political scientists. Google Scholar turned up [Lundström 2005](http://smye2002.univ-paris1.fr/program/paper/b5_lun.pdf) doing a correlational study between the Freedom House index and various components of the [Economic Freedom of the World](http://www.freetheworld.com/index.html) index (which is similar to the Heritage index), as well as [Wu and Davis 1999](http://www.springerlink.com/index/X3134V3236W27774.pdf), [Wu and Davis 2005](http://www.fas.nus.edu.sg/ppp/docs/wp/wp48.pdf), [Berggren 2003](http://www.ratio.se/pdf/wp/nb_efi.pdf), [Carbone 2007](http://www.sisp.it/sisp_convegnoannuale_paperroom_download.asp?id=644), and lots more. (Though see also [Doucouliagos 2005](http://www.blackwell-synergy.com/doi/abs/10.1111/j.0950-0804.2005.00252.x) for evidence of publication bias in this area.) So why bother to reinvent the wheel?  A few answers:

  * This project was really just a way to procrastinate.
  * I like making charts.
  * My methods were somewhat different from those in the published literature. Rather than using the accepted methodology of the social sciences--which consists of reducing all questions to chi-squared significance tests--I felt free to use my own Doofus Methodology, which consists of staring at graphs and seeing if something pops out at me. After careful deliberation, I decided on the latter methodology for three reasons. First, ultimately I only care about correlations that are strong enough to be obvious to the naked eye.  Second, I might actually know something about some of the countries in question--they're not just interchangeable data points--and given how informal this study was anyway, I saw no reason to jettison that knowledge.  Third, as we'll see, when we're asking about the _best_ forms of government, doing regression analysis on all the countries that happen to exist today can be seriously misleading.  To put it bluntly, the majority of countries are so abysmal in terms of both economic freedom _and_ political freedom, that trying to gain insight from them into a hypothesized tradeoff between the two freedoms is like studying a remedial class of second-graders to find out whether algebraic or geometric insight is more important for winning the Fields Medal.  It's the outlier countries, the Singapores and Icelands, that should interest us at least as much as the pack.



**Caveat #2:** The problems with the Freedom House and Heritage surveys--and for that matter, _any_ surveys that try to rank countries on some linear scale of "freedom"--are evident. Indeed, reading the survey methodologies, I found plenty of things to complain about, as I'm sure you would as well. Nevertheless, both surveys struck me as (1) having reasonably consistent methodologies, (2) being reasonably well-accepted by social scientists, and (3) giving results that agree pretty well with intuition, for _most_ of the countries I know something about.  So lacking a better alternative, I decided to go along with these indices.  Just to double-check, I also looked at the Freedom House index versus the Economic Freedom of the World index, and the plot was extremely similar to the one versus the Heritage index.

**Caveat #3:** A major limitation of my scatterplot is that it only looks at the world of 2008, and disregards a vast wealth of historical examples (Chile under Pinochet, the US under Reagan…).  Future research by amateur procrastinating bloggers should clearly take the available historical data into account as well.

Granting all of this, what can we potentially learn?

**1\. Political and economic freedom are correlated.** Any doofus could have predicted this, and lo and behold, it's apparent from even a glance at the data. Looking at the countries in question, it seems clear that part of this correlation is due to _both_ freedoms being correlated with economic development, i.e. "having your national shit together."  In a country like Denmark, you can criticize the government _and_ start a business. In a country like North Korea, you can neither criticize the government _nor_ start a business, at least without being shot.  The studies I linked to above claim some evidence that this obvious correlation has a causal component, as follows: by and large, economic freedom helps make countries richer, and being richer helps make them more politically free.  Assuming that claim is correct, score one for Milton Friedman.

**2\. A wide range of economic freedom levels is compatible with a "near-maximal" level of political freedom.** Let's look only at the countries on the far right of the scatterplot--those with "US-or-above" levels of political freedom (Australia, Austria, Bahamas, Barbados, Belgium, Canada, Chile, Cyprus, Czech Republic, Denmark, Estonia, Finland, Germany, Iceland, Ireland, Luxembourg, Malta, Netherlands, New Zealand, Norway, Portugal, Spain, Sweden, Switzerland, UK, US, and Uruguay). Here the correlation between economic and political freedom seems to disappear entirely, or even become slightly negative. The economic freedom scores of these countries range from 64.3 to 82.4, which is almost half of the total spread across all countries on earth (excepting a few dictatorships like North Korea, Cuba, and Zimbabwe). More to the point, this list includes countries commonly regarded as "socialist" in contemporary political debate (like the Scandinavian countries), _and_ countries regarded as "capitalist" (like Australia, Chile, and the US).  Thus, the idea that countries that _already have_ a high level of political freedom, would increase their political freedom even more by lowering taxes, privatizing industries, etc., does not seem to be borne out by this dataset.

**3\. There _might_ be a "Pareto curve of freedom": that is, a basic tension between economic and political freedom that prevents them from being maximized ****simultaneously****.** I'll admit that the evidence on this point is inconclusive.  Firstly, there aren't enough data points; secondly, the lack of any example of a country maximizing both freedoms is obviously not an impossibility proof.  A true believer in Ayn Rand's utopia, like a true believer in Marxism, could always disregard any empirical finding by saying that the right experiment has never been tried yet, and would self-evidently succeed if it were.

However, if we do construct the "Pareto curve of freedom" for the Freedom House/Heritage data, what we find is this:

  * Iceland, with economic freedom score of 76.5 and political freedom score of 100
  * Canada, with economic freedom score of 80.2 and political freedom score of 99
  * Ireland, with economic freedom score of 82.4 and political freedom score of 97
  * Singapore, with economic freedom score of 87.4 and political freedom score of 49



(The US is conspicuously not on the Pareto curve, though wounded patriots can console themselves that it's the only country of anywhere near its population size that comes close.)

Note that Hong Kong is not in this dataset, since as part of China, it isn't ranked separately by Freedom House. However, Heritage gives Hong Kong an economic freedom score of 90.3, which is the highest in the world (Singapore is #2). The political freedom score for China itself is a dismal 18. So, if we assigned Hong Kong the point (18,90.3), that would be a fifth point on the Pareto curve.

To check the robustness of the Pareto curve, I recalculated it using the Economic Freedom in the World index in place of the Heritage index.   The result was basically similar: clustered on the right we find Finland, Iceland, and Luxembourg maximizing political freedom, then Canada, then Switzerland, then New Zealand, and then, as before, Singapore way off on its own maximizing economic freedom.

To confirm the hypothesis of a tradeoff between economic freedom and political freedom, what we'd need in the dataset are "more Singapores"--or better yet, some countries that interpolated between the Western democracies and Singapore.  Conversely, to disprove the tradeoff hypothesis, all it would take is a single country that dominated the rest of the world on _both_ axes, with the political freedom of Scandinavia and the economic freedom of Singapore.  I find it interesting that no such country seems to exist, not even a small city-state or island.

Incidentally, the tradeoff idea is not necessarily rejected by libertarians.  Friedman himself stressed that "political freedom, once established, has a tendency to destroy economic freedom."  To put it bluntly, if poor people can vote, one of the main things they vote for is to redistribute money to themselves.  There are then three possibilities: either redistribution takes place (and economic freedom as defined by Heritage and the _Wall Street Journal_ goes down), or the poor majority is violently suppressed (and political freedom goes down), or the government is overthrown.  Amusingly, Friedman and Klein seem to be in complete agreement on this central point: it's just that one of them laments it while the other relishes it.

In summary, I conjecture that the relationship between economic freedom and political freedom is similar to that between jogging and health.  In general, we expect people to be healthier the more they jog, with at least part of the relationship being causal. But it doesn't follow that jogging 20 hours per day is healthier than jogging one hour; indeed the former _might_ even be detrimental.

Of course, people could accept all this (even find it plunkingly obvious), and still vehemently disagree about the quantitative aspect: exactly how far out _is_ the Pareto curve?  How much jogging is too much?  As usual, it's the complexity-theoretic questions that are the interesting ones.  The tragedy is that you never even get to those questions if you're too hung up on computability.
