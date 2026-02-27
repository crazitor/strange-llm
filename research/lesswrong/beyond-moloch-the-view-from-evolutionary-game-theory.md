---
title: "Beyond Moloch: The view from Evolutionary Game Theory"
author: "Jonah Wilberg"
date: "2026-02-25"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/PDQ2Ajbpe8cjymn22/beyond-moloch-the-view-from-evolutionary-game-theory"
score: 23
votes: 9
---

In the [previous](https://www.lesswrong.com/posts/rJuq9iwYgobsRGzJJ/why-moloch-is-actually-the-god-of-evolutionary-prisoner-s) [posts](https://www.lesswrong.com/posts/n3pQdCP3pAmBf6xgm/defeating-moloch-the-view-from-evolutionary-game-theory) in this sequence, I've made the case that Evolutionary Prisoner's Dilemma (EPD) is the real subject-matter of Scott Alexander's [Meditations on Moloch](https://www.lesswrong.com/posts/TxcRbCYHaeL59aY7E/meditations-on-moloch) (MoM), and that its opposite, Evolutionary Harmony (EH), provides a model for the [Goddess of Everything Else](https://www.lesswrong.com/posts/MFNJ7kQttCuCXHp8P/the-goddess-of-everything-else) as our best hope of [defeating Moloch](https://www.lesswrong.com/posts/n3pQdCP3pAmBf6xgm/defeating-moloch-the-view-from-evolutionary-game-theory).

But treating these as two separate models leaves a crucial explanatory gap: there’s no account of how Moloch and the Goddess interact, or of the conditions that determine which of these dynamics win out.

In this post I close that gap by exploring three modifications to the basic EPD model: iterated interaction, spatial and network structure, and assortment through partner choice. 

Each of these produces a unified framework in which Moloch and the Goddess are not separate forces but different attractors within a single dynamical system. In each case, an identifiable parameter determines which attractor the system approaches - and this helps frame a strategic approach to the civilization-scale challenges Moloch represents.

And I’ll close with some thoughts on the mythological plane - how a more unified model allows us to go beyond Moloch to a myth that can hold pessimism and optimism in a single vision, and gives humanity a more meaningful role.

**Iterated Prisoner’s Dilemma**
===============================

The EPD model discussed in an [earlier post](https://www.lesswrong.com/posts/rJuq9iwYgobsRGzJJ/why-moloch-is-actually-the-god-of-evolutionary-prisoner-s) assumes that when individuals interact they play a single round of [Prisoner’s Dilemma](https://www.lesswrong.com/w/prisoner-s-dilemma) (PD). 

As a quick reminder, since we’ll be using these terms, PD is defined by the payoff ordering:

T>R>P>S

where:

*   R is the reward for mutual cooperation
*   T is the temptation to defect
*   P is the punishment for mutual defection
*   S is the sucker’s payoff

**Repeated Games**
------------------

The standard way to model the so-called Iterated Prisoner's Dilemma (IPD) is to say that - instead of just playing a single round - the interaction continues on to another round with probability *w*. This then results in an average number of rounds per interaction of: 1/(1−w).

This captures a plausible feature of real-world interactions between agents - the idea that future interactions with the same partner are possible but uncertain.

(It also sidesteps a technical problem with fixed-length games - if you know exactly when the game ends, ‘backward induction’ means the situation [reduces to the one-shot version](https://www.lesswrong.com/posts/jbgjvhszkr3KoehDh/the-truly-iterated-prisoner-s-dilemma) of prisoner’s dilemma.)

This framework opens up a new space of possible strategies that incorporate a memory of your partner’s previous action. The most famous is Tit-for-Tat (TfT): you cooperate on the first move, and then do whatever your partner did last round. 

Against another TfT player, TfT earns the mutual cooperation payoff R every round. Against a continual defector, TfT cooperates once (earning the sucker's payoff S) and defects every round thereafter (earning P). 

The total expected value of a fully cooperative interaction is the sum of a geometric series: R/(1−w). For TfT to outcompete a strategy of continual defection, this discounted stream of cooperation benefits must outweigh the expected value of defection - which leads to the condition that w must exceed a threshold determined by the payoff structure, essentially

w > (T−R)/(T−P)

**Practical Implications**
--------------------------

So it turns out that by replacing one-shot games with repeated games, we get a unified model that has the properties needed to explain under what conditions cooperation can emerge from prisoner’s dilemma interactions.

When the so-called  ‘shadow of the future’ is long enough - when *w* is high enough - cooperation becomes stable. When it is short, defection wins out: Moloch-as-EPD becomes just one attractor within a broader system that can be practically nudged towards EH-style cooperation. 

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/9bff288ba57b9dd52b771b24f4621b3ef2310c183e0e8cfb.png)

Institutions that create stable, long-term relationships between parties - professional associations, diplomatic channels, regulatory bodies with ongoing oversight - can all serve to raise *w*,  in addition to helping ensure the payoff structure meets the conditions required for cooperation.

Transparency is important too: without the ability to identify each other and track histories, strategies based on memory become impossible to implement. In the case of risks from AI, for example, this idea can support moves towards greater transparency about strategic decisions and model evaluations. 

Likewise, short time horizons in any sphere of activity reduces the likelihood of repeated interaction, lowering *w* and pushing the system toward the Moloch attractor. So the model also highlights the need to *make time* for the repeated interactions required for cooperation - for example by slowing or pausing critical processes.

**Spatial Structure and Networks**
==================================

Another core assumption of the EPD model I described earlier was that “at each time step, individuals are randomly paired to play each other in PD.” 

That’s what’s known as a ‘well-mixed population’ - everyone interacts with everyone else, with an equal probability.

**Spatial structures**
----------------------

Spatially structured versions of EPD modify this assumption. Individuals are placed on a lattice - think of a grid, with each person occupying a cell - and each individual interacts only with their immediate neighbours. 

Payoffs are summed over these local interactions, and in each generation, an individual either survives or is replaced by a copy of whichever neighbour earned the highest payoff. 

And it turns out this minimal change is sufficient to sustain cooperation indefinitely. 

The reason becomes clear once you watch the dynamics: cooperators cluster together, and the interior of a cooperator cluster interacts almost exclusively with other cooperators, earning the full mutual cooperation payoff R on most interactions. 

Defectors on the boundary of a cluster can exploit the cooperators they touch, but they can’t reach the cluster's interior. Meanwhile, cooperators in that interior - shielded from defectors - earn enough to outcompete the boundary defectors in subsequent generations. 

The clusters contract at their edges but resist being consumed entirely. The result, depending on payoff parameters, is one of three outcomes: cooperation dominates, defection dominates, or a dynamic coexistence of both.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/8fed22811f88d37386549f14fe44f4d8d8cda38e6ec00935.png)

The formal condition for cooperation to survive turns out to depend on how b/c (the benefit to cost ratio of a cooperative act, which can be derived from the PD payoffs) compares to the number of neighbours k: cooperation is favoured when:

b/c > k

Fewer neighbours means a tighter cluster and more robust cooperation.

**Scale-free networks**
-----------------------

Spatial EPD has also been extended to more realistic network topologies - particularly so-called ‘scale-free networks’, in which a few highly connected hubs interact with many others while most individuals have few connections. 

This topology is relevant to many networks that contribute to global catastrophic risks: the handful of frontier AI labs whose deployment choices cascade through thousands of dependent systems; the small number of state producers or investors whose decisions determine the emissions of global energy infrastructure; or financial and banking networks where a few systemically important institutions can propagate failure through the whole economic system.

It turns out that in scale-free networks, cooperation fares considerably better than on random networks. The key is the influence of hubs. When a hub individual adopts cooperation, it benefits an outsized number of neighbours, many of whom copy the cooperative strategy. 

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/488e2ebeafdaf84cf68fb367cdd17ef0366c304a84cbf0ce.png)

The mathematics here involves the degree distribution of the network: the heavier-tailed this distribution (the more extreme the hubs), the more robustly cooperation can survive. A highly heterogeneous network can sustain cooperation at payoff parameters where a random network cannot.

Together, lattice and scale-free results give us the same kind of unified model as the IPD approach: a single framework in which cooperation or defection can dominate depending on identifiable structural parameters - the density of local connections, the clustering coefficient, the degree of network heterogeneity.

**Practical Implications. **
----------------------------

If geography and network structure determine whether cooperation survives, then deliberately shaping those structures is another lever for defeating Moloch. The goal is to design interaction structures that enable clustering among cooperators and limit their exposure to defectors.

This highlights the value of building dense, well-connected communities or networks of actors committed to prosocial norms. Within AI governance, for example, tightly coupled networks of safety-focused labs, researchers, and policymakers may be more resilient to Molochian pressure than loosely coupled ecosystems where everyone interacts equally.

It also highlights the practical importance of hubs. If highly connected nodes defect, the damage propagates widely. If they cooperate, so does much of the network. This suggests a specific strategic approach, concentrating effort on the most connected actors in any system. 

**Assortment and Partner Choice**
=================================

The spatial and network model achieves positive assortment through geography and network structure: cooperators end up interacting more with each other due to their position in the network or lattice. 

**Assortment**
--------------

But there’s a more general mechanism for achieving the same result: allowing individuals to actively choose their interaction partners.

This is the framework of assortment and partner choice. In this model, individuals have an ability to select who they interact with - including the ability to exit interactions with defectors and seek cooperators instead. 

The concept of assortment is usually measured by a parameter r that captures how much more likely a cooperator is to interact with another cooperator than chance alone would predict. r = 0 is the well-mixed baseline; r = 1 means cooperators only ever meet other cooperators. 

Hamilton's Rule, originally derived in the context of genetic relatedness and kin selection (a parallel explanation for the Darwinian evolution of cooperation in animals), turns out to be a general statement about assortment: cooperation is evolutionarily favoured whenever 

rb > c

where b is the benefit delivered to an interaction partner, c is the cost paid by the cooperator, and r is the assortment coefficient. 

When r is zero, the inequality requires b > c/0, which is impossible - full defection dominates, exactly as in EPD. As r rises, cooperation becomes progressively more viable.

The beauty of Hamilton's Rule is that r doesn’t have to reflect genetic relatedness. It can measure any positive assortment between cooperators -whether due to spatial proximity, shared membership in institutions, reputation systems that allow cooperators to identify and find each other, or explicit partner choice. 

**Partner Choice**
------------------

Take partner choice. When individuals can walk away from defectors and seek out cooperators, defection becomes less profitable because defectors increasingly find themselves paired with other defectors (earning the mutual defection payoff P) rather than with cooperators (earning the higher temptation payoff T). 

Cooperators, meanwhile, increasingly *find the others*. As this sorting process plays out, the effective assortment coefficient r rises - and with it, the conditions for cooperation. The system can move from an EPD-like regime (low r, defection wins) to an EH-like regime (high r, cooperation wins) through the endogenous process of partner selection.

When partner choice is cheap and accurate, cooperation dominates. When partner choice is costly or unreliable, defection recovers. Key variables are the costs of switching partners and the accuracy of reputation information.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/3d1ae0bf9b7ad708c4213275e2b9f879a285e0d1ee24dff7.png)

**Practical implications. **
----------------------------

The partner choice framework points toward a set of interventions quite different from the previous two. Where the IPD suggests extending time horizons and where spatial structure suggests shaping network topology, partner choice suggests investing in the infrastructure of reputation and exit.

Reputation systems that allow actors to credibly signal a history of cooperation, and to identify a defection history of potential partners, raise the effective assortment coefficient r by allowing cooperators to find each other and avoid defectors. 

Transparency and verifiable track records are thus mechanistically important for shifting a system from Molochian toward cooperative dynamics. Audit mechanisms, certification schemes, open publication of safety practices, and independent evaluations of AI labs all function, in evolutionary game-theoretic terms, as assortment-enhancing infrastructure.

Exit options are equally important. When actors are locked into interactions with defectors, the assortment mechanism breaks down. 

So maintaining genuine competitive alternatives, supporting new entrants with cooperative profiles, and reducing switching costs all preserve the partner-choice mechanism. 

In AI governance terms, this highlights the danger of monopolistic consolidation, which destroys the partner-choice mechanism by removing exit options. 

**Beyond Moloch**
=================

**A Unified Model**
-------------------

The practical and theoretical challenge I raised for the [Moloch vs Goddess](https://www.lesswrong.com/posts/n3pQdCP3pAmBf6xgm/defeating-moloch-the-view-from-evolutionary-game-theory) framework is that since EPD and EH are separate models, there’s no account of how they interact or of the conditions that determine which dynamics prevail. Culture change and piecemeal governance appear, at best, as exogenous shocks to EPD that reset the initial condition without changing the underlying dynamics.

The three extensions of EPD explored above - iterated interactions, spatial structure, and assortment through partner choice - each address this challenge by producing a unified model in which Moloch and the Goddess are not separate forces but two attractors within a single dynamical system. 

The parameter that controls which attractor the system approaches is different in each case: the repetition probability *w* in IPD, the spatial structure or degree distribution in spatial/network models, and the assortment coefficient r in partner choice. 

But the message is the same in each case: Moloch and the Goddess are merely specific dynamics that can emerge within a deeper underlying system. And we can model this system in ways that suggest practical strategies for improving the system’s dynamics.

**Beyond payoffs **
-------------------

An emerging theme in this sequence is that the evolutionary game theory framing of Moloch allows us to move beyond governance approaches that aim only at changing the payoffs: rewarding cooperation and punishing defection. While this is not wrong - it is genuinely part of the answer - it is also importantly incomplete, and leaves out other strategies for addressing Moloch.

In the [previous post](https://www.lesswrong.com/posts/n3pQdCP3pAmBf6xgm/defeating-moloch-the-view-from-evolutionary-game-theory) I argued that the evolutionary harmony framing of the Goddess of Everything Else points to the need to ensure that interventions increase the fitness of cooperative individuals and institutions relative to defectors, in a way that propagates.

In this post I’ve pointed to the ways in which more unified models in evolutionary game theory highlight additional practical strategies that revolve around long-term relationships, reputation, transparency, building alliances or communities, and offering opportunities to connect with other cooperative actors and exit from exploitative relationships.

These are not novel ideas in themselves. What evolutionary game theory provides is the strategic framework that explains *why* they work, and allows us to reason about their relative importance.

**A Myth Beyond Moloch**
------------------------

Translating these unified models into the mythic register of *Meditations on Moloch*, we could say that Moloch and the Goddess are expressions or avatars of a more fundamental godhead.

As we saw, the *Meditations *portray a pessimistic, Lovecraftian monism, where the Molochian godhead goes by other names: Azathoth, Gnon, etc. 

*The Goddess of everything else* turns this into a dualistic Manichaeism, a cosmic war between good and evil.

The arguments above represent the third step of the dialectic, a synthesis that transcends and includes both of the previous steps. 

We transcend or ‘go beyond’ Moloch and the Goddess by reframing them both as aspects of a larger divine unity, one which allows us to hold both Lovecraftian pessimism and utopian hope in a single vision.

And it turns out that this larger cosmic vision is one in which humanity has a more meaningful place. We’re not just subject to the will of some ultra-powerful Gods. Instead, we play a critical role in driving the system, shaping parameters that can summon either Moloch or the Goddess.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/0afc99597ba8418aeab67da46e22f57408f85d506f36289b.png)

*Thanks to* [*Euan McLean*](https://www.lesswrong.com/users/euanmclean) *for comments on an earlier draft and to Claude Sonnet 4.6 for writing assistance.*