---
title: "Computer scientists crash the Solvay Conference"
author: "Scott Aaronson"
date: "Thu, 09 Jun 2022"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=6457"
---

Thanks so much to everyone who sent messages of support following my [last post](https://scottaaronson.blog/?p=6444)! I vowed there that I'm going to stop letting online trolls and sneerers occupy so much space in my mental world. Truthfully, though, while there _are_ many trolls and sneerers who terrify me, there are also some who merely amuse me. A good example of the latter came a few weeks ago, when an anonymous commenter calling themselves "String Theorist" submitted the following:

> It’s honestly funny to me when you [Scott] call yourself a “nerd” or a “prodigy” or whatever _[I don 't recall ever calling myself a "prodigy," which would indeed be cringe, though "nerd" certainly --SA]_, as if studying quantum computing, which is essentially nothing more than glorified linear algebra, is such an advanced intellectual achievement. For what it’s worth I’m a theoretical physicist, I’m in a completely different field, and I was still able to learn Shor’s algorithm in about half an hour, that’s how easy this stuff is. I took a look at some of your papers on arXiv and the math really doesn’t get any more advanced than linear algebra. To understand quantum circuits about the most advanced concept is a tensor product which is routinely covered in undergraduate linear algebra. Wheras in my field of string theory grasping, for instance, holographic dualities relating confirmal field theories and gravity requires vastly more expertise (years of advanced study). I actually find it pretty entertaining that you’ve said yourself you’re still struggling to understand QFT, which most people I’m working with in my research group were first exposed to in undergrad  The truth is we’re in entirely different leagues of intelligence (“nerdiness”) and any of your qcomputing papers could easily be picked up by a first or second year math major. It’s just a joke that this is even a field (quantum complexity theory) with journals and faculty when the results in your papers that I’ve seen are pretty much trivial and don’t require anything more than undergraduate level maths.

Why does this sort of trash-talk, reminiscent of [Luboš Motl](https://en.wikipedia.org/wiki/Lubo%C5%A1_Motl), no longer ruffle me? Mostly because the boundaries between quantum computing theory, condensed matter physics, and quantum gravity, which were never clear in the first place, have steadily gotten fuzzier. Even in the 1990s, the field of quantum computing attracted amazing physicists--folks who definitely _do_ know quantum field theory--such as Ed Farhi, John Preskill, and Ray Laflamme. Decades later, it would be fair to say that the physicists have banged their heads against many of the same questions that we computer scientists have banged _our_ heads against, oftentimes in collaboration with us. And yes, there were cases where actual knowledge of particle physics gave physicists an advantage--with some famous examples being the algorithms of Farhi and collaborators (the [adiabatic algorithm](https://en.wikipedia.org/wiki/Adiabatic_quantum_computation), the [quantum walk on conjoined trees](https://arxiv.org/abs/quant-ph/0209131), the [NAND-tree algorithm](https://scottaaronson.blog/?p=207)). There were other cases where computer scientists' knowledge gave _them_ an advantage: I wouldn't know many details about that, but conceivably shadow tomography, BosonSampling, PostBQP=PP? Overall, it's been what you wish _every_ indisciplinary collaboration could be.

What's new, in the last decade, is that the scientific conversation centered around quantum information and computation has dramatically "metastasized," to encompass not only a good fraction of all the experimentalists doing quantum optics and sensing and metrology and so forth, and not only a good fraction of all the condensed-matter theorists, but even many leading string theorists and quantum gravity theorists, including Susskind, Maldacena, Bousso, Hubeny, Harlow, and yes, [Witten](https://arxiv.org/abs/1805.11965). And I don't think it's _just_ that they're too professional to trash-talk quantum information people the way commenter "String Theorist" does. Rather it's that, because of the intellectual success of "It from Qubit," we're increasingly participating in the same [conversations](https://www.youtube.com/watch?v=1CpzigpEJnU) and working on the same technical questions. One particularly exciting such question, which I'll have more to say about in a future post, is the truth or falsehood of the Quantum Extended Church-Turing Thesis for observers who jump into black holes.

Not to psychoanalyze, but I've noticed a pattern wherein, the more secure a scientist is about their position within their own field, the readier they are to admit ignorance about the _neighboring_ fields, to learn about those fields, and to reach out to the experts in them, to ask simple or (as it usually turns out) not-so-simple questions.

* * *

I can't imagine any better illustration of these tendencies better than the 28th Solvay Conference on the Physics of Quantum Information, which I attended two weeks ago in Brussels on my 41st birthday.

[](https://scottaaronson.blog/wp-content/uploads/2022/06/solvay.jpg)As others pointed out, the proportion of women is not as high as we all wish, but it's higher than in 1911, when there was exactly one: Madame Curie herself.

It was my first trip out of the US since before COVID--indeed, I'm so out of practice that I nearly missed my flights in _both_ directions, in part because of my lack of familiarity with the COVID protocols for transatlantic travel, as well as the immense lines caused by those protocols. My former adviser Umesh Vazirani, who was also at the Solvay Conference, was [proud](https://scottaaronson.blog/?p=40).

The Solvay Conference is the venue where, legendarily, the fundamentals of quantum mechanics got hashed out between 1911 and 1927, by the likes of Einstein, Bohr, Planck, and Curie. (Einstein complained, in a letter, about being called away from his work on general relativity to attend a ["witches' sabbath."](https://www.europhysicsnews.org/articles/epn/pdf/2011/05/epn2011425p15.pdf)) Remarkably, it's still being held in Brussels every few years, and still funded by the same Solvay family that started it. The once-every-few-years schedule has, we were constantly reminded, been interrupted only three times in its 110-year history: once for WWI, once for WWII, and now once for COVID (this year's conference was supposed to be in 2020).

This was the first ever Solvay conference organized around the theme of quantum information, and apparently, the first ever that counted computer scientists among its participants (me, Umesh Vazirani, Dorit Aharonov, Urmila Mahadev, and Thomas Vidick). There were four topics: (1) many-body physics, (2) quantum gravity, (3) quantum computing hardware, and (4) quantum algorithms. The structure, apparently unchanged since the conference's founding, is this: everyone attends every session, without exception. They sit around facing each other the whole time; no one ever stands to lecture. For each topic, two ["rapporteurs"](https://en.wikipedia.org/wiki/Rapporteur) introduce the topic with half-hour prepared talks; then there are short prepared response talks as well as an hour or more of unstructured discussion. Everything everyone says is recorded in order to be published later.

* * *

Daniel Gottesman and I were the two rapporteurs for quantum algorithms: Daniel spoke about quantum error-correction and fault-tolerance, and I spoke about ["How Much Structure Is Needed for Huge Quantum Speedups?"](https://www.scottaaronson.com/talks/aar-solvay.ppt) The link goes to my PowerPoint slides, if you'd like to check them out. I tried to survey 30 years of history of that question, from Simon's and Shor's algorithms, to huge speedups in quantum query complexity (e.g., glued trees and Forrelation), to the recent quantum supremacy experiments based on BosonSampling and Random Circuit Sampling, all the way to the [breakthrough](https://arxiv.org/abs/2204.02063) by Yamakawa and Zhandry a couple months ago. The last slide hypothesizes a "Law of Conservation of Weirdness," which after all these decades still remains to be undermined: “For every problem that admits an exponential quantum speedup, there must be some weirdness in its detailed statement, which the quantum algorithm exploits to focus amplitude on the rare right answers.” My title slide also shows [DALL-E2](https://openai.com/dall-e-2/)'s impressionistic take on the title question, "how much structure is needed for huge quantum speedups?":

[](https://scottaaronson.blog/wp-content/uploads/2022/06/speedups.jpg)

The discussion following my talk was largely a debate between me and Ed Farhi, reprising many debates he and I have had over the past 20 years: Farhi urged optimism about the prospect for large, practical quantum speedups via algorithms like [QAOA](https://arxiv.org/abs/1411.4028), pointing out his group's past successes and explaining how they wouldn't have been possible without an optimistic attitude. For my part, I praised the past successes and said that optimism is well and good, but at the same time, companies, venture capitalists, and government agencies are right now pouring billions into quantum computing, in many cases--as I know from talking to them--because of a mistaken impression that QCs are _already known_ to be able to revolutionize machine learning, finance, supply-chain optimization, or whatever other application domains they care about, and to do so _soon_. They're genuinely surprised to learn that the consensus of QC experts is in a totally different place. And to be clear: among quantum computing theorists, I'm not at all unusually pessimistic or skeptical, just unusually willing to say in public what others say in private.

Afterwards, one of the string theorists said that Farhi’s arguments with me had been a highlight … and I agreed. What's the point of a friggin’ Solvay Conference if everyone's just going to _agree_ with each other?

* * *

Besides quantum algorithms, there was naturally lots of animated discussion about the practical prospects for building scalable quantum computers. While I'd hoped that this discussion might change the impressions I'd come with, it mostly confirmed them. Yes, the problem is staggeringly hard. Recent ideas for fault-tolerance, including the use of LDPC codes and bosonic codes, might help. Gottesman's talk gave me the insight that, at its core, quantum fault-tolerance is all about _testing_ , _isolation_ , and _contact-tracing_ , just for bit-flip and phase-flip errors rather than viruses. Alas, we don't yet have the quantum fault-tolerance analogue of a vaccine!

At one point, I asked the trapped-ion experts in open session if they'd comment on the startup company [IonQ](https://ionq.com/), whose stock price recently fell precipitously in the wake of a scathing analyst report. Alas, none of them took the bait.

On a different note, I was tremendously excited by the quantum gravity session. Netta Engelhardt spoke about her and others' [celebrated recent work](https://www.quantamagazine.org/netta-engelhardt-has-escaped-hawkings-black-hole-paradox-20210823/) explaining the Page curve of an evaporating black hole using Euclidean path integrals--and by questioning her and others during coffee breaks, I finally got a handwavy intuition for how it works. There was also lots of debate, again at coffee breaks, about Susskind's [recent speculations](https://www.youtube.com/watch?v=1CpzigpEJnU) on observers jumping into black holes and the quantum Extended Church-Turing Thesis. One of my main takeaways from the conference was a dramatically better understanding of the issues involved there--but that's a big enough topic that it will need its own post.

Toward the end of the quantum gravity session, the experimentalist John Martinis innocently asked what actual experiments, or at least thought experiments, had been at issue for the past several hours. I got a laugh by explaining to him that, while the gravity experts considered this too obvious to point out, the thought experiments in question all involve forming a black hole in a known quantum pure state, with total control over all the Planck-scale degrees of freedom; then waiting outside the black hole for ~1070 years; collecting every last photon of Hawking radiation that comes out and routing them all into a quantum computer; doing a quantum computation that might actually require exponential time; _and then_ jumping into the black hole, whereupon you might either die immediately at the event horizon, or else learn something in your last seconds before hitting the singularity, which you could then never communicate to anyone outside the black hole. Martinis thanked me for clarifying.

* * *

Anyway, I had a total blast. Here I am amusing some of the world's great physicists by letting them mess around with GPT-3.

[](https://scottaaronson.blog/wp-content/uploads/2022/06/gpt3.jpg)Back: Ahmed Almheiri, Juan Maldacena, John Martinis, Aron Wall. Front: Geoff Penington, me, Daniel Harlow. Thanks to Michelle Simmons for the photo.

I also had the following exchange at my birthday dinner:

**Physicist:** So I don’t get this, Scott. Are you a physicist who studied computer science, or a computer scientist who studied physics?

**Me:** I’m a computer scientist who studied computer science.

**Physicist:** But then you…

**Me:** Yeah, at some point I learned what a boson was, in order to invent BosonSampling.

**Physicist:** And your courses in physics…

**Me:** They ended at thermodynamics. I couldn’t handle PDEs.

**Physicist:** What are the units of h-bar?

**Me:** Uhh, well, it’s a conversion factor between energy and time. (*)

**Physicist:** Good. What’s the radius of the hydrogen atom?

**Me:** Uhh … not sure … maybe something like 10-15 meters?

**Physicist:** OK fine, he’s not one of us.

(The answer, it turns out, is more like 10-10 meters. I’d stupidly substituted the radius of the _nucleus_ --or, y'know, a positively-charged hydrogen _ion_ , i.e. proton. In my partial defense, I was massively jetlagged and at most 10% conscious.)

(*) Actually h-bar is a conversion factor between energy and _1/time_ , i.e. frequency, but the physicist accepted this answer.

* * *

Anyway, I look forward to attending more workshops this summer, seeing more colleagues who I hadn't seen since before COVID, and talking more science … including branching out in some new directions that I'll blog about soon. It does beat worrying about online trolls.
