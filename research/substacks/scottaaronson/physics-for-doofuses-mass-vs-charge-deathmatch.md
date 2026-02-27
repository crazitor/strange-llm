---
title: "Physics for Doofuses: Mass vs. charge deathmatch"
author: "Scott Aaronson"
date: "Sun, 15 Jul 2007"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=244"
---

Back in high school, I was struck by the apparent symmetry between mass and charge. For the one you've got Newton's F=Gm1m2/r2, for the other you've got Coulomb's F=Kq1q2/r2. So then _why, in our current understanding of the universe, are mass and charge treated so differently?_ Why should one be inextricably linked to the geometry of spacetime, whereas the other seems more like an add-on? Why should it be so much harder to give a quantum-mechanical treatment of one than the other? Notwithstanding that such questions occupied Einstein for the last decades of his life, let's plunge ahead.

When we look for differences between mass and charge, we immediately notice several.

**(1) Charge can be negative whereas mass can 't.**

That's why gravity is always attractive, whereas the Coulomb force is both attractive and repulsive. Since positive and negative charges tend to neutralize each other, this already explains why gravity is relevant to the large-scale structure of the universe while electromagnetism isn't. It also explains why there can't be any "charge black holes" analogous to gravitational black holes. (I don't mean charged black holes; I mean "black holes" that are black _because_ of electric charge.) Unfortunately, it still doesn't explain why mass should be related to the geometry of spacetime.

**(2) Charge appears to be quantized (coming in units of 1/3 of an electron charge), whereas mass appears not to be quantized, at least not in units we know.**

**(3) The apparent mass of a moving object increases Lorentzianly, whereas the charge is invariant.**

These are interesting differences, but they also don't seem to get us anywhere.

**(4) Gravity is "many orders of magnitude weaker" than electromagnetism.**

One hears this statement often; the trouble is, what does it _mean_? How does one compare the "intrinsic" strength of gravity and electromagnetism, without plugging in the masses and charges of typical particles that we happen to find in the universe? (Help me.)

**(5) Gravity is transmitted by a spin-2 particle, whereas electromagnetism is transmitted by a spin-1 particle.**

This difference is surely crucial; the trouble with it (to use a pomo word) is that it's too "theory-laden." Since no one has ever seen a graviton, the reason we know gravitons are spin-2 particles in the first place must have to do with more "basic" properties of gravity. So if we want a non-circular explanation for why gravity is different from the Coulomb force, it'd be better to phrase the explanation directly in terms of the more basic properties.

**(6) Charge shows up in only one fundamental equation of physics -- F=Kq1q2/r2 -- whereas mass shows up in two equations: F=Gm1m2/r2 and F=ma.**

Now we finally seem to be getting somewhere. Difference (6) was the basis for Einstein's [equivalence principle](http://en.wikipedia.org/wiki/Equivalence_principle), which was one of the main steps on the road to general relativity.

But while the equivalence principle suggests the _possibility_ of relating mass to spacetime geometry, I could never understand why it implies the _necessity_ of doing so. If we wanted, why couldn't we simply regard the equivalence of gravitational and inertial mass as a weird coincidence? Why are we _forced_ to take the drastic step of making spacetime itself into a pseudo-Riemannian manifold?

The answer seems to be that we're not! It's possible to treat general relativity as just a complicated field theory on flat spacetime, involving a tensor at every point -- and indeed, this is a perspective that both Feynman and Weinberg famously adopted at various times. It's just that most people see it as simpler, more parsimonious, to interpret the tensors geometrically.

So the real question is: why should the field theory of Gmm/r2 involve these complicated tensors (which also turn out to be hard to quantize), whereas the field theory of Kqq/r2 is much simpler and easier to quantize?

After studying this question assiduously for years (alright, alright -- I Googled it), I came across the following point, which struck me as the crucial one:

**(7) Whereas the electric force is mediated by photons, which don 't themselves carry charge, the gravitational force is mediated by gravitons, which _do_ themselves carry energy.**

Photons sail past each other, ships passing in the night. They're too busy tugging on the charges in the universe even to notice each other's presence. (Indeed, this is why it's so hard to build a quantum computer with photons as qubits, despite photons' excellent coherence times.) Gravitons, by contrast, are constantly tugging at the matter in the universe _and at each other_. This is why Maxwell's equations are linear whereas Einstein's are nonlinear -- and that, in turn, is related to why Einstein's are so much harder than Maxwell's to quantize.

When I ran this explanation by non-doofus friends like Daniel Gottesman, they immediately pointed out that I've ignored the strong nuclear force -- which, while it's _also_ nonlinear, turns out to be possible to quantize in certain energy regimes, using the hack called "renormalization." Incidentally, John Preskill told me that this hack only works in 3+1 dimensions: if spacetime were 5-dimensional, then the strong force wouldn't be renormalizable either. And in the other direction, if spacetime were 3-dimensional, then gravity would become a topological theory that we _do_ sort of know how to quantize.

However, I see no reason to let these actual facts mar our tidy explanation. Think of it this way: _if electromagnetism (being linear) is in P and gravity (being nonlinear) is NP-complete, then the strong force is Graph Isomorphism._

My physicist friends were at least willing to concede to me that, while the explanation I've settled on is not _completely_ right, it's not completely wrong either. And that, my friends, means that it more than meets the standards of the Physics for Doofuses series.
