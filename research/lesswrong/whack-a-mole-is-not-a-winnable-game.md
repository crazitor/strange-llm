---
title: "Whack-a-Mole is Not a Winnable Game"
author: "Sable"
date: "2026-02-26"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/QAB3BEDRziBerNAih/whack-a-mole-is-not-a-winnable-game"
score: 64
votes: 30
---

When I went to college for Electrical Engineering, they put all the engineers in an Engineering 101 course our freshman year. It was meant to give us a taste of what we’d be getting ourselves into.

The goal, we were told, was to build a hovercraft that would navigate an obstacle course. We had access to all the equipment we’d need - stiff pieces of foam for the body, fans, micro-controllers, batteries, etc.

But then there was a list of rules, not for the competition, but for how we were allowed to build our robot. I remember two of them.

The first was that we had to use Nickel-Metal-Hydride batteries instead of Lithium-Ion batteries, even though the latter had a better energy-to-weight ratio, which really matters when you’re trying to make something hover.

The second was that we had to put these plastic grates over our fans, even though doing so reduced the airflow and thus the thrust.

We all looked at these rules, and I remember asking the TA why they were there.

I bet you can guess.

See, *apparently* some dumbass stuck their finger in the fan in a previous year and nearly chopped it off, so now we had to use plastic grates.

Even better, the previous year someone had short-circuited their Lithium-Ion battery, causing it to catch fire, at which point they decided, in their infinite wisdom, to *throw it at the TA.*

The teachers, administrators, and (probably) the university’s lawyers, agreed afterwards that measures had to be taken:

No more open fans, and no more Lithium-Ion batteries for us baby engineers.

This is an approach to problem-solving I’ve come to think of as playing Whack-A-Mole. Whack-A-Mole is an arcade game with multiple openings where little moles pop out, and the player has to hit them with a padded baton. Moles keep emerging and the player keeps hitting them until the game ends and the player gets a score.

![Whack A Mole Game For Sale](https://substackcdn.com/image/fetch/$s_!Ln2A!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5c6843b-bb3e-4c8e-baa0-bd886856a3ee_898x670.jpeg)

Whoever designed this mole-art clearly didn’t know a lot about moles.

Year after year, the list of rules for the Engineering 101 class I was in would grow longer, as more people made mistakes or found stupid things to do. Importantly, it would *only* grow longer.

Think about it - imagine an argument about taking one of the rules off the list. A lawyer would easily argue that doing so would clearly be endangering the students, and the university could be sued. And keeping any single rule on the list is hardly a big deal, right?

Even if the list grows so long that it starts severely hampering students’ ability to complete the course, well, safety first.

Except that what’s at stake isn’t always a student’s ability to get a hovercraft to navigate an obstacle course. Sometimes it’s the healthcare system, or the economy, or an immigrant’s ability to legally enter a country.

**Playing Whack-A-Mole**
========================

Playing Whack-A-Mole when problem-solving looks something like this:

> If we just fix this *specific exploit*, this *specific kind of way that things went wrong this one time*, that’ll fix the problem.

This is a kind of problem solving that is unable - or uninterested - in addressing root causes. It’s not focused on the underlying dynamics that drive the existence of problems; rather, it merely attempts to patch over whatever the most recent problem happens to be.

It says, *if there’s a battery fire, ban that kind of battery.*

It says, *if a dam springs a leak, just plug up the hole.*

It says, *if a patient has a symptom, just alleviate that symptom.*

This is not sustainable, in the long term. It is a kind of problem-solving that is guaranteed to fail eventually, because it refuses to *actually solve the real problem*.

And I see it show up again and again in the real world, but especially in what I’ll call, for the purposes of this post, an *adversarial game*.

**Adversarial Games**
=====================

There’s a kind of dynamic - let’s call it an adversarial game - where there are (at least) two sides. One side (the Designer) makes rules based on the behavior it wants, and the other side (the Player) attempts to exploit those rules to do what they wanted to do in the first place (e.g. win).

**Example 1: The US Tax Code**
------------------------------

A good example of this is the U.S. tax code. The Designer, in this case Congress and the IRS, attempt to make certain rules about what kind of money gets taxed. The Player, in this case mostly rich people, attempt to keep as much of their money from being taxed as possible.

How does this play out over time?

In this case, the Designer adds a rule: we’ll tax income above a certain threshold.

So the Player adapts, using tax-avoidance strategies that are legal at the time like:

1.  **Timing the realization of their income (e.g. when they sold their stocks).** Because capital gains aren’t taxed until they’re realized, and long-term capital gains are taxed at a lower rate than income, the players manipulate their money to fall under this category and time the realization of those gains, avoiding the taxes they would’ve owed if they’d simply gotten the money as income.
2.  **Using paper losses to offset their taxable income.** [Depreciating assets](https://www.finance.senate.gov/imo/media/doc/Prttax2-1.pdf) like real estate, farm losses, depletion of oil and gas wells, and so on allowed the wealthy to make it look, for tax purposes, as if they had zero income.
3.  **Stock options.**  A *stock option* is a contract allowing the recipient to buy a stock for a specific price in the future. If that price is lower than the market price - the contract allows a stock worth $200 to be purchased for $100 - then the owner of the stock option can simply pocket the difference ($100) by buying and selling the stock. Under the [1950 Revenue Act](https://scholarship.law.marquette.edu/cgi/viewcontent.cgi?article=3292&context=mulr), executives receiving qualified stock options only paid the 25% capital gains rate for these, instead of the ordinary income tax:
    
    > The most important advantage is that the employee-stockholder is now able to time the taking of a capital gain for his own tax advantage and need pay no more than a flat 25% maximum effective rate on long term gains.
    
    Predictably, [by 1951 many top executives in the country](https://secfi.com/learn/history-of-employee-stock-options) had stock options as part of their compensation packages.
    

All of this is called “exploiting a loophole” by those watching.

The Designer complains that this isn’t what they intended, so they make a new rule (pass a new law/regulation) to “patch the hole”. They’ll add a new tax, or change the math on how stock is taxed.

So the Player adapts. Instead of selling stock and paying a capital gains tax, they’ll *borrow money against the value of their stock*, using that money to buy what they want and paying interest on the debt. As long as the value of their stock goes up faster than the amount they owe, this works until the person dies of old age. This is the so-called [buy-borrow-die](https://budgetlab.yale.edu/research/buy-borrow-die-options-reforming-tax-treatment-borrowing-against-appreciated-assets) strategy, and is a known loophole in current tax law.

The Designer complains that this isn’t what they intended, so they-

And on and on it goes.

**Example 1.5: (Case Study) The Alternative Minimum Tax**
---------------------------------------------------------

In 1969, [Treasury Secretary Joseph Barr testified before Congress](https://www.jec.senate.gov/reports/91st%20Congress/The%201969%20Economic%20Report%20of%20the%20President%20Part%20I%20%28436%29.pdf) that about 155 Americans with high income (over $200,000 at the time, about $2 million today) paid zero federal income tax in the 1966-67 tax year.

This provoked an outrage. I couldn’t substantiate the claim, but apocryphally, members of congress received more letters from constituents about this tax avoidance than about the *Vietnam War.*

Under such pressure, what could the designers do but try to whack the mole before them?

The result of said mole-whacking was the [Tax Reform Act of 1969](https://en.wikipedia.org/wiki/Tax_Reform_Act_of_1969#Alternative_minimum_tax), which created the Alternative Minimum Tax, or AMT. At the time the AMT functioned as an additional tax layered on top of the regular income tax in order to close the loopholes exploited by those 155 high-income earners.

Just for funsies, the loopholes (‘tax preference items’) *(which, by the way, were a legitimate part of the tax code that Congress wrote; those rich assholes weren’t actually breaking any laws)*:

1.  **Capital gains exclusion.** At the time, if you sold stock after holding it long enough, half the profit wasn’t taxed.
2.  **Accelerated depreciation on real property.** Real estate bullshit. If you read this, you might be aware I’ve got opinions on land value, and how America fails to tax it properly. Allowing people to get out of paying taxes *through* property value is even worse.
3.  **Accelerated depreciation on personal property subject to net lease**. Because the government shouldn’t be taxing people because their personal property got less valuable, for some reason?
4.  **Amortization of certified pollution control facilities**. “Oh no, I made too much money, so I’m just gonna do my taxes as if this pollution treatment plant I own exploded magically.”
5.  **Amortization of railroad rolling stock**. I like trains as much as the next vaguely-autistic person, but come on.
6.  **Stock options.** This was a loophole created earlier, that became a mole.
7.  **Bad debt reserves of financial institutions**. Yeah, congress, subsidize bad financial institutions. *That’s* going to end well.
8.  **Percentage depletion**.  
    *In the room where this was suggested:*  
    Let’s let people not pay taxes because their oil wells ran dry, Steve.  
    → Great idea, John! Next we’ll let them deduct hookers and blow, too.

Like most tax law, the AMT was written for lawyers and accountants, not human beings, so I found it weird and difficult to understand, but it seems work by totaling all the tax exemptions the rich were claiming, subtract out a $30,000 exemption and whatever federal taxes they actually paid, and then they owe 10% of whatever’s left as the AMT.

So let’s say you made $400,000, but but managed (through ‘tax preference items’ (ways to reduce your tax burden) that were **part of the existing tax code**) to get your taxable income to $50,000, and you’d pay $20,000 in taxes on that. You’d pay an AMT of $400,000 (your tax preference items) - $30,000 (exemption) - $20,000 (the federal income tax you would’ve paid) x 10%, or $35,000 in AMT that year.

This law - the AMT - was so poorly designed that it had to be changed [*at least 18 times*](https://www.everycrsreport.com/files/20130117_RL30149_d9056c88ab035377592c596ef672995ace6ca147.html) since its enactment:

> Since its enactment in 1969, the individual minimum tax has been modified numerous times, in 1971, in 1976, in 1977, in 1978, in 1982, in 1986, in 1990, in 1993, in 1997, in 1998, in 2001, in 2002, in 2003, in 2004, in 2006, in 2007, in 2008, and in 2009. The Tax Reform Act of 1976 was the first major modification, adding new preference items to the add-on minimum tax base and increasing the tax rate to 15%.

This is a textbook example of Congress seeing a mole - a bunch of rich people not paying federal income tax (which, I can’t emphasize this enough, *the rich people were just exploiting the existing tax code that Congress wrote*) \- and whacking it, in the process creating even *more* complex tax law that created *new* moles that had to be whacked.

One of the stupidest parts of the original AMT was that it [wasn’t even indexed for inflation](https://www.everycrsreport.com/files/20130117_RL30149_d9056c88ab035377592c596ef672995ace6ca147.html), so Congress was always going to have to step in and change the law as more and more middle-class Americans began to be affected by it.

**Example 2: Banking Regulation**
---------------------------------

Another good example is the way banks are regulated in America.

The Designer, in this case the US Government, tries to regulate a system of banks such that there are no bank runs or financial disasters. The Player, in this case the banks, try to make money any way they can.

Leading up to 2008, one of the main ways the banks made money was by selling a financial asset backed by numerous mortgages. This was called a Mortgage-Backed Security. Derivatives, a financial product that functions like a bet on other financial products, were then built on top of Mortgage-Backed Securities, and were unregulated at the time.

This is the Player making money while not *technically* violating the letter of the law.

But when enough of these derivatives piled up like a house of cards and the table beneath them collapsed, the whole thing fell apart, forcing the government (The Designer) to step in and provide a massive infusion of cash.

This taught the Player that there was a rule the Designer obeyed but didn’t explicitly state: If the system collapsed due to their own actions, they would be bailed out by the Designer.

The Designer, in an effort to stop this from happening again, tried to patch the holes in the dam. In 2010 congress passes the [Dodd-Frank Wall Street Reform and Consumer Protection Act](https://en.wikipedia.org/wiki/Dodd%E2%80%93Frank_Wall_Street_Reform_and_Consumer_Protection_Act), which claims to establish oversight and regulation of all of this, preventing another such disaster.

The Player adapted: new methods were tried and new products were invented.

Then in 2023, interest rate changes cause Silicon Valley Bank (SVB) to go under, causing another bank run, the exact thing Dodd-Frank was supposed to prevent.

And it’s possible Dodd-Frank would have prevented it, but Dodd-Frank regulations for SVB-sized banks were [rolled back in 2018](https://www.barclaydamon.com/alerts/The-Dodd-Frank-Banking-Rule-Rollback-Explained-06-04-2018). In the adversarial game between the regulators (Designer) and the banks (Player), the regulators whacked a mole, thought they’d solved the problem, and then another popped up because the banks had lobbyists and could play the game too.

Now the Designer says that *this* is just another hole that needs patching, so-

Here we go again.

**Example 3: The DEA and the Controlled Substances Act**
--------------------------------------------------------

The [Controlled Substances Act](https://www.dea.gov/drug-information/csa) divides regulated substances (drugs) into five schedules, each of which is then regulated as a category based on how dangerous it is. On the surface, this isn’t dumb; while I get plenty annoyed at needing prescriptions for some things, there are plenty of very dangerous drugs (like opioids) that stand a high chance of ruining people’s lives if they had easy, over-the-counter access to them.

The problem is this: as you can see by looking through the [law](https://uscode.house.gov/view.xhtml?path=/prelim@title21/chapter13&edition=prelim), every scheduled chemical compound is specifically named. In other words, a compound is only a schedule-1 drug if *that specific arrangement of atoms* is regulated by the DEA. Slap a fluorine atom onto any of them, and it’s a whole new molecule, meaning it has to go through the *entire regulatory process again*.

The law attempts to regulate, among other things, cannabis, i.e. the stuff in weed that gets you high.

Except that there are hundreds of these synthetic drugs, with more being discovered over time. Between 2008 and 2014, [European agencies identified 142 new ones](https://pmc.ncbi.nlm.nih.gov/articles/PMC5135680/), and there are over [1400 recognized globally](https://www.unodc.org/LSS/Page/NPS/DataVisualisations). How many more do you think are going to be identified in the near future, especially with biomedical advances like AI-based protein folding and molecule discovery?

Congress tried to whack this mole with the [Federal Analog Act in 1986](https://en.wikipedia.org/wiki/Federal_Analogue_Act), but their efforts didn’t succeed. They tried again in [2012](https://obamawhitehouse.archives.gov/ondcp/ondcp-fact-sheets/synthetic-drugs-k2-spice-bath-salts), banning 26 synthetic drugs, but there are thousands of possible molecules, and whack-a-mole ain’t cutting it.

The [HALT Fentanyl Act in 2025](https://www.naco.org/news/halt-fentanyl-act-signed-law) is better, covering an entire chemical class, although with our luck it’s going to turn out that there’s a drug that looks a lot like fentanyl that slows down aging or prevents erectile dysfunction, and we’ll never know because the whole thing has been declared illegal. It’s a real tradeoff made necessary by the government’s approach to regulating substances.

Also, the HALT act only applies to Fentanyl, so Congress is just whacking a bunch of moles at once and hoping that works better.

Just for extra credit, here’s a news article [*explicitly calling synthetic drugs out as a game of whack-a-mole*](https://www.acsh.org/news/2016/04/27/designer-drug-whack-a-mole-like-juggling-jello)*.* Here’s Senator Chuck Grassley calling the whole thing a “[deadly game of whack-a-mole](https://www.grassley.senate.gov/news/news-releases/grassley-feinstein-pitch-new-framework-combat-synthetic-drugs)”. [Here’s](https://www.grassley.senate.gov/news/news-releases/to-avoid-deadly-game-of-whack-a-mole-law-enforcement-groups-urge-extension-of-critical-tool-to-combat-lethal-fentanyl-analogues) a bunch of law enforcement agencies also directly calling it whack-a-mole.

**The Metaphor(s)**
-------------------

One way to look at this is as the [Dutch boy](https://en.wikipedia.org/wiki/Hans_Brinker,_or_The_Silver_Skates) attempting to plug leaks in a dam, sticking his fingers in the leaks to plug them. Of course, a new leak springs open after the last has been plugged, because plugging the individual leaks did nothing to alleviate the root cause, or in other words:

> Patching holes does nothing to address the pressure causing them.

In the metaphor of the dam, the pressure is caused by the weight of water the dam holds back. In real Adversarial Games, the pressure is caused by the players optimizing for their own goals against the Designer.

Then there’s the title of the post: the game of Whack-a-Mole.

The thing about Whack-A-Mole, though, is that the player never actually closes any of the holes through which the moles emerge or kills any of the moles. The game runs on a timer because there is no victory condition possible, no end state a player can reach where moles will never trouble them again.

Whack-a-Mole is not a winnable game, because hitting moles as they emerge - fixing loopholes as Players find them - changes nothing about the fundamental dynamics of the game. The Designer makes a rule, the Player circumvents it, the Designer whacks the mole by changing the rules, and the Player finds another hole.

To use another metaphor, treating the symptoms of a disease does not cure the patient. Treating the *effects* of the disease may stop problems from being visible, but the disease is still there, wreaking havoc.

**Don’t Hate The Player, Fault The Designer For Making A Bad Game**
===================================================================

There’s a line of thinking (especially looking at the tax example above) that goes something like:

*Rich people should be paying their fair share in taxes. We should try to get them (via changing culture or whatever) to stop trying to avoid paying taxes.*

In general, this can be summarized as “Let’s try to get the Player to not optimize for their own goals against the Designer’s wishes.”

That would be great!

It’s just that, from the perspective of the Designer, *that’s not something you get to control.* I’m sure the IRS would love it if everyone decided to stop trying to hide their taxable income. I’m sure the healthcare system would love it if everyone dieted and exercised regularly. I’m sure the FDIC would adore banks that never tried to maximize their profits by exposing themselves to too much systemic risk. I’m sure the DEA would be thrilled if people stopped designing new synthetic drugs worth billions of dollars.

The thing is:

> Designers don’t get to control the choices players make, so long as the players obey the letter of the rules of the game.

Players are trying to achieve their own goals and desires. They’re following their own incentives. That’s the nature of the world. It’s the responsibility of the Designer to create a system wherein players doing so leads to the social good, because the Designer is the one imposing this system in the first place. Imposing a system with loopholes and complaining about players taking advantage of it is like building a boat with holes in the hull and blaming water for rushing in.

**The Nature of the Game**
==========================

The Designer is fundamentally at a disadvantage in this kind of Adversarial Game.

Why?

The action space available to the Players - what actions they’re allowed to take - is infinite. They can always invent new things, discover new exploits, uncover new loopholes. A Player can do anything.

The action space available to the Designer, on the other hand, is limited: all a Designer can do is create and enforce specific rules.

Additionally, the Designer is stuck playing defense. They can’t spot the loopholes in their own rules (if they could, they’d hopefully adjust the rule to account for it), so they’re stuck waiting for Players to discover and exploit them before patching.

You can’t plug the leak in the dam before it appears; you don’t know which hole the mole is coming out of until it pops out at you.

**Changing The Game**
=====================

So what’s the solution, from the perspective of the Designer? Are they cursed to be forever a step behind, whacking moles as they go but never actually solving the problem?

No.

The solution is to change the nature of the game, usually (but not always) by changing the nature of the incentives the Player has.

**Example 1: LVT instead of Income Tax**
----------------------------------------

Income - or, more broadly, *compensation* \- can be hidden, mutated, and otherwise obscured in an infinite number of ways. Stock, stock options, health insurance, life insurance, paying for room/board/internet, getting a company car, being able to use the company credit card… The list goes on and on. There is no way for governments to be able to fully account, forever, for every new method of compensating an employee.

Income tax avoidance, therefore, is a game of Whack-a-Mole from the perspective of the IRS. It’s an unwinnable game they keep playing because they’re legally obligated to.

*Land ownership*, in contrast, cannot be hidden or transmuted. It can’t be squirreled away in a Swiss bank account or converted into crypto. And it can’t be obscured from the government, because the very meaning of owning a piece of land is that the government acknowledges that you own that piece of land.

*(One might attempt to point out that shell companies can be used to hide land ownership. If I own a company that owns a company that owns a subsidiary that owns a company that owns a piece of land, then won’t the government have to trace that all back to me to know who to tax? The answer is no, at least in theory. The government doesn’t have to know or care who really owns the land in the end, only that they charged the entity, person or corporation, listed as owning the property with the tax, and then that entity either pays or doesn’t. If that entity doesn’t pay, the government seizes the land and auctions it off. No tracing required.)*

So taxing land value - technically property taxes in general, but I’m too much of a Georgist to want improvements to the land to be taxed - is an entirely different game that sharply limits the Player’s moves. The Player still has moves; in general they’ll try to get their land assessed for only a small fraction of its value and lower their taxes that way, but the point still stands. And even that exploit can be curtailed if land valuations are made public, because it’ll be really obvious to everyone that the land owned by the billionaire who just had lunch with the President is worth way less than it should be.

Land Value Taxes, and Property Taxes in general, are a much better source of government revenue than income taxes, because they’re impossible to dodge the way that income taxes can be dodged.

**Example 2: Banking**
----------------------

I don’t understand the banking industry all that well, so I’m pulling from economist [John Cochrane’s ideas](https://download.ssrn.com/14/04/16/ssrn_id2425883_code16295.pdf?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE4aCXVzLWVhc3QtMSJGMEQCIHKlJlSKqC0FO1ePzz16pHHvwWMIGUhs3sR8tvYY4zYBAiBdURSS%2FyGHTZ5b6OVynptqYOjkDZZf5ZKln%2FdBnILilyq9BQgXEAQaDDMwODQ3NTMwMTI1NyIMRe8gkMpaf7EsPzk6KpoFEcoBXT9Sy69uqELz3YE8FvATH1eDDJrJ3gLEpTf3oV1yhz9NkG15A5i%2Br3%2BVOYeV1abYy8suCgWZt7FNUe%2BudcQwF5oWRRWPq7DV8YHSehq9mApdybaWDR0%2BX0NrQwI6J3mCFcl7mpvv8EclLnh3%2FtNcFH68TDQHB67QfZFWmjpswkEZ7yCo6vkZGaLefDWTAjAPJYIbRDnNMJ%2FyR0djkE09i2Uyyp40JmRuPyIPCJNsaL6PVcQlEVNG5LtbTIR%2FKLvLJPBFERFSpk4mB4WLFVXmJv1%2BDfBPXtP%2FqyjwyxGG8jmIDkNWy9V%2B8AApDR9Wkwa%2BMHstYYSkC9PpvGwC0PrPu%2FrJpHBtQxOgi%2FsrKzobuU%2FMysFKZD2u6YeCVs1VRjDB0TzL96nOhkYmQzBX8Ovw7F6wDprG%2FZcZNDZgzCblbwShinyq1Gjihe13onGUA0YGCHMuO8iLWnHGeHoey3ty66o3KSqnIHWHYIvOsWcYxcLBg0RmNSySwjZn5cwlkAZYo24B6CfirX68V%2BurvCExNVwDfAyOzefg99bBq8vQq%2FUAJhZSc7xsY25vhBHlI%2FeSWLUNwz7oyttv6MReFbcf9u7hKn4HWepoiJftEm6hfqLXTTbvpBtFauQH62npHWqyQmSapNoPxLKpdn8JmIiGKGLbifujKV%2FUgMKfSdlNIGK0v0Fl7DlmID7NQTwsKeaMq%2Bv%2Fi%2FozZSqiJznF1XGXXa%2Bt81xmDwMIg1niDqGNClc0aKUz%2BgwOYYRCzkAj2uTDd2CaExCpdcuxWzXzDABhwwcEq5Zw%2B4NYVHO5uZZDyj0QoWb%2ByO0XKT4o4txm0OO29uLGXeh4E5w0sBlhu2V6M%2Bfo8H5tvX%2BE5jQ3IN1J3KlTf1F9uAlOMPeYjcwGOrIBpm5CgpDN5bJ41SxB8t0r1uO0rDaafJJ2k3nJa%2Fz%2Fb7NYgGD19GQtmqPe4vzsHthE%2B7n5rzRhBnyf1DHooWgnYAqn5YJ%2FLTX2uc0pMzVm1dxmd53V4k2vKOt2Vnkqwer9D5DQQPAXFVT%2Fuz0zgvdJc%2F9%2F%2BZxbz7Nr%2FziL2ji1yIletp2aFfeYA8LgYtBj0L5h7Hr%2BuXiqKoMWgijGVZw8UtN4%2B%2FnLc8z7gF0YvTRF6zM%2F%2Fg%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20260204T143742Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAUPUUPRWETUKI3I33%2F20260204%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=cd44eb578894f6d43de0b57c3ded36b4aa0e31b772c42f77d26277299be7bdf1&abstractId=2425883) here.

Current banks fund themselves through debt. All the money you have in a bank is technically money that the bank owes you - a short-term debt that the bank carries.

The bank uses the money you put in it to make loans to other customers - businesses, mortgages, etc. These loans are repaid with interest, and the bank makes money on the interest, giving a portion of that to you.

The issue is that a) the bank only ever *actually possesses* a small fraction of what it owes, and b) it repays its short-term debt (gives your money back to you) on a first-come, first-served basis.

An example:

Ten people, including you, put $10,000 in the bank. Now the bank owes each of you $10,000, and has $100,000 to work with. The bank only keeps $20,000 on hand, and lends out $80,000 worth of mortgages, business loans, etc.

Now a bank run is possible. If three people who deposited $10,000 want to pull out their money, only two of them can do so - the bank only literally possesses $20,000 to give. This causes everyone to think the bank is going to fail, and since only the first two people to withdraw their money actually get their money back if the bank fails, everyone rushes to be one of the first two.

That’s a bank run.

Dr. Cochrane’s idea is to make banks fund themselves entirely through equity, e.g. stock, or long-term debt, the way other companies do. In other words, separate out the functionality of holding money and payment processing from the functionality of borrowing and lending.

‘Narrow banks’ would take over holding people’s money and processing payments for a small fee; they’d be where your checking account lives. And these Narrow Banks would be legally required to hold 100% of the assets they claim to have either in cash or short-term treasuries, so there would never be a run on them. If 10 people put in $10,000, they’d have to have $100,000 on hand at all times to give back.

Current banks, on the other hand, would operate as businesses whose business model is lending money and making money off the interest payments. All the money they’re lending, instead of belonging to *customers* of the bank, would belong to *shareholders* of the bank. If the bank fails, then the *shareholders* who invested in the bank lose the money they invested, but this is no different from any other business going bankrupt. It doesn’t affect the average American’s ability to access their savings.

This is a way the Designer can change the nature of the game to eliminate the possibility of a bank run, by changing *whose money* the Player is allowed to gamble with. Currently, banks are regulated but allowed to gamble with their depositors’ (the American people’s) money. In Dr. Cochrane’s system, the Player (banks) are only allowed to gamble with *their own* (investor’s) money. And investing is already known to be risky, whereas putting your money in a bank is supposed to be safe.

**Example 3: The DEA and the Controlled Substances Act**
--------------------------------------------------------

I’m no expert on regulating drugs, but the idea that the US Government needs to have an opinion on the legality of *every psychoactive molecule in existence* seems like it’s destined to fail no matter how many resources it throws at the problem.

Besides, the demand for drugs is enormous, and there’s a *lot* of money to be made, which means that people have a rather large incentive to create supply to meet that demand. No amount of law enforcement or War on Drugs is going to change that.

So how do we change the game?

Synthetic cannabinoids exist because cannabis - weed - is illegal in plenty of places in America, whereas synthetic cannabinoids aren’t *technically* illegal until ruled so. (This matters for things like drug testing.) There’s demand for something that isn’t weed but still gets you high *like* weed, *because* weed is illegal.

For synthetic cannabinoids in particular, the answer is simple: legalize, regulate, and tax cannabis. If people can get access to the real thing, it massively reduces the demand for legally-distinct alternatives.

*(I’m aware there are plenty of other considerations here. This is an example of how to stop playing whack-a-mole, not a comprehensive argument for cannabis legalization.)*

Of course, this doesn’t solve the problem for other classes of drugs; I’m not necessarily a fan of legalizing, regulating, and taxing *fentanyl*. So how else might we do this?

One approach might be to try to regulate drugs by *effect* rather than by *molecule*, but that can be legally thorny; you wind up having to prove what a drug does to a person in court, and that’s difficult and has failed before.

It’s a difficult problem, and I don’t have a miracle solution.

What I *do* know is that trying to ban one molecule at a time, or even one drug class at a time, isn’t going to work in the long term.

**Whack-A-Mole Leads to Bureaucracy and Sclerotic Government**
==============================================================

The US tax code is an ever-growing beast of regulations. If you include just the explicit rules it comes to [around 2,600 pages](https://taxfoundation.org/blog/how-many-words-are-tax-code/), but plenty of tax law is based in court rulings, and court rulings are based on precedent, so once you account for all that, the whole thing clocks in at some 70,000 pages long:

![](https://substackcdn.com/image/fetch/$s_!gpAc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7fdff0e9-b535-42ec-9eb1-9dc014bba4a1_600x601.png)

I wonder what happened in the 1940s- oh right.

Why is it a monotonically-increasing morass of byzantine rules?

Well, part of the reason is a reliance on previous case law.

But the other part is that *laws and regulations keep being added to patch holes people find.*

And patching each hole requires significant political effort, will, and support, because US congresspeople and senators are overwhelmingly rich, and so likely benefit from those very loopholes. (At time of writing, [330 members of the 535](https://www.quiverquant.com/congress-live-net-worth/) senators and congresspeople are millionaires, and many are multimillionaires.)

The same is true for banking regulations; Dodd-Frank added some [243](https://web.archive.org/web/20101105014342/http://www.davispolk.com/files/Publication/7084f9fe-6580-413b-b870-b7c025ed2ecf/Presentation/PublicationAttachment/1d4495c7-0be0-4e9a-ba77-f786fb90464a/070910_Financial_Reform_Summary.pdf) new rules, and while things may improve for a while, the incentives of the Players have not changed. The water is still rising behind the dam, and just because the US government stuck their finger in one hole doesn’t mean others won’t appear. And in the meantime, the amount of regulations *keeps going up*.

This pattern is *everywhere*, in private companies and governments and university courses. Every time a mistake is made or someone does something stupid, a new rule joins the bureaucracy, and things get a little tighter, a little more limited. And each and every time it’s *easier*, more *convenient,* to just ban whatever the problem was and keep going, instead of actually fixing the system by changing the incentives of the Player.

**Refactoring as the Anti-Whack-A-Mole**
========================================

In software engineering, [*refactoring*](https://en.wikipedia.org/wiki/Code_refactoring) is the process of changing a working codebase to fix existing problems with the structure, *without changing the external behavior of the code*. In other words, refactoring is about taking the time to fix issues with the underlying structure of the codebase, instead of just whacking mole after mole and hoping for the best.

Any software engineer knows that code *needs* to be refactored regularly, or else it becomes an unmanageable mess in short order. If left without a refactor for even a single year, a major codebase rapidly decays into incomprehensible spaghetti code that can’t be effectively patched anymore, because the whole thing is nothing *but* a pile of patches and Band-Aids.

And that’s after a single year.

The US Government hasn’t been substantially refactored for *a quarter of a millennium.*

Instead, it’s grown almost monotonically over time, rule and procedure and regulation and law and judicial precedent all piled on top of each other, at every level of our federal republic, compromise added to compromise and patch added to patch until it’s almost impossible to fix anything at all.

No wonder it’s such a mess.

**Conclusion**
==============

If there’s one rule of human nature I subscribe to, one constant that governs the entire species, it’s this:

> In the aggregate, people will follow their incentives.

If people have an incentive to make more money, or keep more of their money from being taxed, *which they do*, they’ll try to do so.

If the people running banks have an incentive to make a profit, *which they do*, they’ll keep trying to make more and more profit via riskier and riskier loans and financial products, because they don’t have an equal incentive not to lose their customers’ money (after all, it’s not the CEO’s money being gambled with).

If people have an incentive to keep generating synthetic drugs, [*which they do*](https://www.govinfo.gov/content/pkg/CHRG-114hhrg20165/html/CHRG-114hhrg20165.htm), they’ll keep doing it.

The Designer - in all three cases here, the US Government - keeps trying to patch holes in a system, while the Players have a constant incentive to poke more holes. In the process, patch after patch and change after change pile up, until the dam is more patch than structure, until the ground is more filled-in mole-hole than neat green lawn.

I’m not saying that problems don’t need to be fixed or that there aren’t any trade-offs.

What I’m saying is that if you find yourself in a position, as the Designer, where you’re spending all your time whacking moles, consider that it may be time for a refactor. Consider that you are playing an unwinnable game, and playing that game is causing your own rules to become longer and more difficult to understand over time.

Consider that the institution you stand for is decaying around you because it’s spending all its time addressing symptoms and refusing to address root causes.

I’m saying that the game of Whack-A-Mole belongs in an arcade, not the real world.

At least that way someone can have the high score.