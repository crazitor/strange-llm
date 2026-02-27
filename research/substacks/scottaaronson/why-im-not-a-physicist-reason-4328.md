---
title: "Why I’m not a physicist: reason #4328"
author: "Scott Aaronson"
date: "Sat, 26 Aug 2006"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=118"
---

There's a trivial question about particle accelerators that bugged me for a while. Today I finally figured out the answer, and I'm so excited by my doofus "discovery" that I want to tell the world.

In Ye Olde Times, accelerators used to smash particles against a fixed target. But today's accelerators smash one particle moving at almost the speed of light against another particle moving at almost the speed of light -- that's why they're called particle colliders (duhhh). Now, you'd think this trick would increase the collision energy by a constant factor, but according to the physicists, it does asymptotically better than that: it squares the energy!

My question was, how could that be? Even if both particles are moving, we can clearly imagine that one of them is stationary, since the particles' motion with respect to the Earth is irrelevant. So then what's the physical difference between a particle hitting a fixed target and two moving particles hitting each other, that could possibly produce a quadratic improvement in energy?

[Warning: Spoiler Ahead]

The answer pops out if we consider the rule for adding velocities in special relativity. If in our reference frame, particle 1 is headed left at a v fraction of the speed of light, while particle 2 is headed right at a w fraction of the speed of light, then in particle 1's reference frame, particle 2 is headed right at a (v+w)/(1+vw) fraction of the speed of light. Here 1+vw is the relativistic correction, "the thing you put in to keep the fraction less than 1." If v and w are both close to 0, then of course we get v+w, the Newtonian answer.

Now set v=w=1-ε. Then (v+w)/(1+vw) = 1 - ε2/(2-2ε+ε2), which scales like 1-ε2. Aha!

To finish the argument, remember that relativistic energy increases with speed like 1/sqrt(1-v2). If we plug in v=1-ε, then we get 1/sqrt(2ε-ε2), while if we plug in v=1-ε2, then we get 1/sqrt(2ε2-ε4). So in the case of a fixed target the energy scales like 1/sqrt(ε), while in the case of two colliding particles it scales like 1/ε.

In summary, nothing's going on here except relativistic addition of velocities. As with Grover's algorithm, as with the quantum Zeno effect, it's our intuition about linear versus quadratic that once again leads us astray.
