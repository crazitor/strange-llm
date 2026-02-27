---
title: "AGI will not happen in your lifetime. Or will it?"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/agi-will-not-happen-in-your-lifetime"
---

[Grady Booch@Grady_BoochAGI will not happen in your lifetime Or in the lifetime of your children Or in the lifetime of your children’s children6:20 AM · Jan 17, 2023

* * *

83 Reposts · 756 Likes](https://twitter.com/grady_booch/status/1615232611026341889?s=61&t=sZG_g2JIvHpAUAjApB1mmw)

 _Grady Booch, a Fellow at IBM, and one of the deepest minds on software development in the history of the field, is one of my favorite people that I have met through Twitter._

_We rarely disagree about anything. On Twitter we sometimes tag team Yann LeCun, and on more than a few occasions we have retweeted each other’s cynical tweets. Neither one of us believes for a minute that large language models are remotely close to artificial general intelligence, and what’s more, we mostly agree about what’s missing: semantics, reasoning, common sense, theory of mind and so on._

_But I found myself disagreeing with the Tweet above. My own skepticism has limits. I do think we will eventually reach AGI (artificial general intelligence), and quite possibly before the end of this century._

_On the theory that our differences might represent some kind of teachable moment, I invited him to talk about it on the record; he immediately agreed. Here’s a very lightly edited transcript of our conversation (approved by both of us)._

**Gary Marcus** : Grady, I get that AGI is hard, and that we aren’t there yet. I think we are wasting funding and bright young minds on an approach that probably isn’t on the right path. I don’t think we have great answers yet for a bunch of core issues, like how to get machines to represent abstract knowledge, and how to get them to induce complex models from the events that they see or read about it. When I think about how little deep progress has been made in the last 75 years, I get depressed. 

But I am cautiously optimistic that we’ll do better in the next 75, that once the hype cools off, people will finally dive deeper into neurosymbolic AI, and start to take some important steps. Our data problems are solved, our compute problems are mostly solved; it’s now mostly a matter of software, and of rethinking how we build AI. Why be so sure we can’t do that in the next 75 years? 

**Grady Booch** : Gary, you and I are in frighteningly close agreement on so many subjects: that the mind is computable; that large language models are inherently wonky; that our field has made incredible progress in our lifetimes and that as such we are on the cusp of something amazing; that we as an industry know there are hard problems to be solved with regard to causality, common sense reasoning, abductive reasoning, embodiment, and so on; that we have some ideas how to approach these problems; that scale is not enough; that pineapple on pizza is good.  
  
Well, I might be making that last one up.  
  
Where we diverge, I think, is largely on timing: you posit that we will see AGI within a few decades, I think it is more like a few generations.  
  
In the spirit of full disclosure, I have to admit that I, being a historian of computing, have a rather jaded and cynical view of the hyperbolic optimism of our field and as such am somewhat conditioned to be a contrarian when it comes to predictions such as this. Take the singularity, for example, something that von Neuman first spoke of in the 1950s and which certain of our colleagues have predicted with alarming precision that we'd achieve by 2045. The term is sufficiently imprecise, filled with emotional and historic baggage, and touches some of humanity's deepest hopes and fears that it's hard to have a rational discussion therein. AGI is just like this. Greek mythology speaks of golums created from clay; Mary Shelly built life from human parts whose very souls were ignited by lightning; da Vinci imagined mechanical knights to fight wars; Edison built dolls that moved and talked; Weiner - who coined the term cybernetics - thought we might build artifical intelligenes through analog mechanisms, Simon and Newll thought it so through formal logic, Feigenbaum through knowlege engineering, and now we see our colleagues who expect that AGI is right around the corner if and only we had enough data and a level built of enough GPUs such that we could move the world.  
  
In short, AGI seems just around the corner, and you yourself fall into that trap when you say "it's now mostly a matter of software".  
  
It's never just a matter of software. Just ask Elon and his full self driving vehicle, or the Air Force and the software-intensive infrastructure of the F-17, or the IRS with their crushing technical debt. I have studied many of the cognitive architectures that are proported to be on the path of AGI: SOAR, Sigma, ACT-R, MANIC, AlphaX and its variations, ChatGPT, Yann's latest work, and as you know have dabbled in one myself (Self, an architecture that combines the ideas of Minsky's society of mind, Rod's subsumption architecture, and Hofstadter's strange loops). In all of these cases, we all think we grok the right architecture, the right significant design decisions, but there is so much more to do. Heck, we've mapped the entire neural network of the common worm, and yet we don't see armies of armored artificial worms with laser beams taking over the world. With ever step we move forward, we discover things we did not know we needed to know. It took evolution about 300 million years to move from the first organic neurons to where we are today, and I don't think we can compress the remaining software problems associated with AGI in the next few decades.  
  
Indeed, this leads me to also observe, in the spirit of full disclosure, to suggest that we as computer scientists not only vastly overestimate our abilities to create an AGI, we vastly underestimate and underrepresent what behavioral scientists, psychologists, cognitive scientists, neurologists, social scientists, and even the poets, philosophers and storytellers of the world know about what it means to be human. There is much we can and should learn from them to guide our work as computer scientists in our journey.  
  
In fact, let me posit that, while someday we will likely build an artificial mind, perhaps the most important outcome of that journey is that is will compel us to understand what it means to be human.

**Gary Marcus** : Turns out I _am_ good with the pineapple on pizza; we should’ve had some together when I visited you in Maui! Real pineapple, straight from the farm, not from a can. And I also very much agree with something else you said:

> _we as computer scientists not only vastly overestimate our abilities to create an AGI, we vastly underestimate and underrepresent what behavioral scientists, psychologists, cognitive scientists, neurologists, social scientists, and even the poets, philosophers and storytellers of the world know about what it means to be human._

Just the other day, in fact, in my introduction to the AGI Debate, I quoted the late Drew McDermott’s closely-related line: 

> _“It is hard to know where [AI researchers] have gone wronger: in underestimating language or overestimating computer programs”_

And Darwin knows, I too am pretty jaded. 

§

But all that said, I certainly think there are lots of cases of early failures that turned out reasonably quickly, once some key idea was unlocked. Alchemy turned into a decently worked-out chemistry fairly quickly, once the basic idea behind the periodic table was discovered; it wasn’t too long between when Oswald Avery figured that the basis of Mendel’s factors was DNA rather than a protein (1944) and when Watson and Crick (with help of Franklin’s data) figured out the structure of the DNA (1953 ). Fast forward another few years and the amino acid-nucleotide code was cracked; Monod and Jacob had worked out the basics of gene expression by the 1960s; Kary Mullis had worked out PCR by 1983. That’s an astonishing amount progress in just under 40 years. Of course there was a long period of stasis just before, when people misguidedly thought that genes were instead made of proteins. But once they got off that wrong-headed track, things moved very quickly indeed.

And we have some advantages nowadays, even relatively to the 50s and 60s; computers can allow new ideas to be tested at unprecedented speed and scale, and good ideas can percolate really really fast, like diffusion as a better way of reconstructing images, which swept through the whole field in a matter of months (and is only a few years old, dating back to 2015). Transformers, invented 2017, ubiquitous in 2023, have (perhaps both for better and worse) spread extremely rapidly.

Since we are (at least to my mind, though I note that you disagree) primarily talking software, there’s no complex manufacturing processes, and so on. Even if we need to invent a new chip type as a prerequisite, that could be a thirty year process rather a one hundred year process. 

What I think we are missing are (a) ideas and (b) large scale databases of machine-interpretable knowledge. Ideas are hard to predict; we don’t know when they will come, and we don’t know how many genuinely new, important ideas we need; on the machine-interpretable knowledge front, we have problems too. But 75+ years worth? Enough to keep us _that_ busy, with so many people working on the problem and so much money (at least currently) somewhat directed at the problem?

In my darkest moments, I actually agree with you. For one thing, most of the money right now is _not_ going to the wrong place: it’s mostly going to large language models, and for you, like for me, that just seems like an approximation to intelligence, not the real thing, and as such as frustrating distraction. And I’ve been concerned for a long time that a fixation on Big Data has sucked the oxygen (as Emily Bender likes to put it) from a lot of other ideas that might be better. For another, I don’t really feel like that many people are working on the right problems right now, and I think a lot of core problems from 75 years ago are still unsolved; McCarthy worried about common sense in 1959, and I still don’t see a solution I can take all that seriously.

But I see some signs that are promising. The neurosymbolic AI community is growing fast; conferences that used to be dozens are now thousands. (I’m looking forward to giving on of the keynotes at the [IBM Neurosymbolic conference](https://ibm.github.io/neuro-symbolic-ai/neuro-symbolic-ai/events/ns-workshop2023/) on Wednesday). [Meta’s Cicero is a great mix of handcrafted structure and knowledge – just where is it needed - and corpus-driven machine learning.](https://garymarcus.substack.com/p/what-does-meta-ais-diplomacy-winning) I take that as a hopeful sign that the scaling-über-alas narrative is losing force, and that more and more people are open to new things. We can only have advances in science once there is recognition of problems, and too much of the rhetoric in ML has in recent times been aimed at stifling critics like us, but I am finally seeing at least a bit of that necessary recognition. 

The rubber-that-meets-the-road question in the end is _how many key discoveries do still we need to make, and how long do we need to make them?_ Do you have any take on that, what the key discoveries we need to make are, and what it might take to foster them, and why you think they might take so long to incubate?

**Grady Booch** : There is this wonderful scene in the Will Smith movie "I Robot" in which the detective Del Spooner meets the avatar of Dr. Alfred Lanning, the father of modern robotics in Asimov's universe who - as a human - had just committed suicide with the help of an NS5 humanoid robot named Sonny. Lanning's death was part of his plan to stop the US Robotics robots from taking over the world. Lanning's avatar was not sentient, but it could reply with truthfullness to any well-formed question.

This, of course, immediately distinguishes itself from ChatGPT, which demonstrably produces bullshit at scale. But that is another topic for another time.

Anyway, Spooner keeps asking the Lanning avatar questions about the suicide, to which the avatar often replies "I'm sorry, my responses are limited. You must ask the right question". Eventually Spooner asks the question "whose's revolution?" and in turn Lanning's avatar replies "detective, that is the right question".

You asked me "how many key discoveries do still we need to make, and how long do we need to make them?"

Gary, that is the right question.

Let me begin by saying that I would be delighted if my prediction (that AGI will not happen anytime soon) was utterly and completely wrong and that you were right. If this comes to pass, I'll buy you an extra large pizza with ham and pineapple and we can share it on the beach as we watch the fall of civilization.

For you see, while I would be delighted at the technical advances made by the field of computing, I would be simultaneously frightened at how humanity would face the presence of a synthetic intelligence suddenly formed in its midst within a single generation. We as a species are ill-prepared to properly metabolize such a superior intelligence, and the ethical issues of how we humans and these artificial sentient beings should treat one another are far beyond the capacity of earth's societies and governments to address with any degree of wisdom or dignity (stares at the US House of Representatives). What power and rights would we individuals have in the shadow of any metacorporation who would undoubly have been the one to bring such a creation into being at scale? Would we treat these new minds as literal slaves? How would this further divide the rich and the poor of this world?

But that also is another topic for another time.

To answer your question, however, I have to address the elephant in the room: what is AGI? I can't suggest what we need to do next until we agree on where we are going.

I'll be direct, which is my style. AGI is a term that has considerable emotional and historic baggage and as such - much like the term "singularity" - is often best used for selling books (stares at Ray) or for naming clickbait articles. It's complex, but I will assert that the mind is computable and therefore it is concievable that synthetic minds can be formed, minds that exhibit the behavior of organic ones.

An aside: we must remember in all this that we humans live in a Flatland, and so we have considerable human bias when it comes to the semantics of intelligence. I therefore assert that it is concievable that other kinds of intelligence can be found in the cosmos.

Intelligence is, for me, just the first phase in a spectrum that collectively we might speak of as synthetic sentience. Intelligence, I think, encompasses reasoning and learning. Indeed, I think in the next few decades, we will see astonishing progress in how we can build software-intensive systems that attend to inductive, deductive, and abductive reasoning. Pearl's ideas regarding cauality will likely become manifest. We'll might see some breakthroughs in common sense reasoning (although like you, i'm skeptical). Similarly, I think in the next few decades, we will see astonishing progress in learning, with advances in self-directed learning, perhaps even with breakthroughs in artificial curosity and synthetic play.

Conciousness and self-consciousness are the next phases in my spectrum. I suspect we'll see some breakthroughs in ways to represent long term and short term memory, in our ability to represent theories of the world, theories of others, and theories of the self.

Sentience and then sapience fill out this spectrum. The world of AI has not made a lot of progress in the past several years, nor do I see much attention being spent here, largely because - as you observe - current funding and corporate interests have pretty much sucked all the oxygen in the air to blow on the embers of transformer-based AI. Transformers are not enough. Scale is not enough. Work needs to be done in the area of planning, decision making, goals and agency, and action selection.

We also need to make considerable progress in metacognition and mechanisms for subjective experience.

These things, collectively, define what I'd call a synthetic mind. In the next decade, we will likely make interesting progress in all those parts I mentioned.

But, we still don't know how to architect these parts into a whole. Evolution took several million years to get us squishy minds to the point where your squishy bits and my squishy bits can wave our fingers across keyboards and send these thoughts across an ocean. I don't see anything in the near future of computing that will compress what needs to get AI from where it is today to where it needs to be to form a non-squishy mind. This is not a problem of scale; this is not a problem of hardware. This is a problem of architecture.

Indeed, Alan Newell said something to this effect in 1990: "The question for me is how can the human mind occur in the physical universe. We now know that the world is governed by physics. We now understand the way biology nestles comfortably within that. The issue is how will the mind do that as well. The answer must have the details. I got to know how the gears clank and how the pistons go and all the rest of that detail. My question leads me down to worry about the architecture".

And that, detective, is the right question.

**Gary Marcus** : Let me start by outlining a _lot_ of agreement. I am not at all sure how humanity would fare in the presence of a superior intelligence. ChatGPT is (at least in many ways) a far _inferior_ intelligence, that, despite having some undeniable talents, cannot at all be trusted. And yet trust it, many humans do.

To their peril. Already we have seen minor abuses; plagiarism, for example, will never be the same. Troll farms may well starting using it to create misinformation at unprecedented scale; we can also expect more and circles of fake web sites in order to sell advertisements; ChatGPT been apparently used to create malware, and it has already infected journalism, with CNET using it produce news stories that were filled with errors. Bias is likely to be huge issue, too. Even if large models never acquire a volition of their own (I hope not!), we have already seen that in the wrong hands (either with malice or, as in the case of CNET, negligence), bad things can and probably will happen. In a recent Wired article, I predicted that 2023 see the first death attributable to large language models, and I stand by that prediction.

ChatGPT is a dress rehearsal, and I wouldn’t say we as a society have gone through it with flying colors. What would happen with even more potent AI is indeed a disconcerting question, not yet well answered.

(Aside for another day: I think that better AI, in which we could directly instill values, might actually make us safer than the world in which we inhabit now, in which so much of what happens is down to the vagaries of what happens to be in this or that training set; I don’t leave my kids moral development to chance, and it terrifies me that so much of current AI is dependent on random details of training corpora that are not available to scientists for inquiry. This seems like a really bad idea.)

But we are not, per se, here to debate whether or not AGI will lead to the fall of civilization (not today, anyway); back to our original question of _when_ it might arrive.

I don’t see you arguing never. I also don’t see you entirely defining your terms. One way to ago would be to say, “we won’t get to AGI until we get sentient AI”; is that the argument you are making?

I find that one to be tough – I see no clear criteria for sentience – but also not entirely relevant. In a[ recent bet that put to Elon Musk](https://garymarcus.substack.com/p/dear-elon-musk-here-are-five-things?) (still no word!), I defined AGI, with the blessings of two of these who coined the term, Ben Goertzel and Shane Legg, as

> **“** a shorthand for any intelligence ... that is flexible and general, with resourcefulness and reliability comparable to (or beyond) human intelligence”

I don’t think that kind of flexibility in any way rests on or demands on sentience. I have in mind something more like the fairly general kind of intelligence we see in science-fiction, in the Star Trek computer, in __ C-3P0, in Scarlett Johannsen’s assistant in _Her_. These characters (especially perhaps the latter two) might or might not be argued to be sentient, but it seems to be that they are flexible, resourceful, reliably (in a way that LLMs certainly aren’t), and adaptive. For me that counts. If we had an AI that smart, I could retire.

But we don’t yet. Question is, again, what it would take to get there. I am fully with you on need deeper semantics, abduction, common sense reasoning etc. (That was the whole point of _Rebooting AI_).

I am also with you in doubting that there will be a single magic singularity moment. Intelligence is multidimensional; we’ve made progress in some of those dimensions (searches of certain complex spaces, some kinds of pattern recognition) and not others (e.g. everyday physical and psychological reasoning).

And they won’t come in all at once. I expect for example that physical reasoning will improve (a radical boon for domestic robots) before psychological reasoning; there won’t be a magic day in which we say “aha AGI landed on January 27, 2062” or whatever it is.

Machines will just get more and more reliable and more general. Maybe _the big landmark will be the day in which they can learn enough on their own that they no longer need us to teach them_.

You might well agree there, too. (And sure, other kinds of intelligence probably do exist in the cosmos; AGI is unlikely to be exactly humanlike, but I don’t see being a replica is a necessity; adaptivity is key, and that is probably achievable by multiple means).

With all that considerable agreement noted, I am still not seeing a _principled_ argument that constructing flexible, adaptive systems with commonsense reasoning, deeper semantics, and so on will take us past the end of the current century.

Of course nothing is guaranteed; we might not get there because we blow ourselves up, or because we waste so much time on large language models that other important challenges—like semantics, causality, commonsense reasoning, abduction and so forth—never get the attention they deserve.

Or because we can’t come up with something better than the current systems that are so greedy in both data and energy consumption that they could asymptote before anything really general emerges.

But certainly the hunger is there, the funding is there, and my guess is that patience for LLMs (which I see as a detour) is not infinite. A decent fraction of the AI community has already recognized that the primary forte of large language models is in generating bullshit; many also see that the current path to autonomous vehicles is not making the progress that some expected. There are whole lot of us, you and me, and the entire neurosymbolic community, but also even folks Yann LeCun and Geoff Hinton, who see that we have currently is not enough.

So I don’t think we will waste more than 5 years before a substantial fraction of AI effort is looking outside the limited streetlight that currently are sucking up so much mental energy. Eventually, and not before too too long, I think the field itself on a better path.

About the only argument I see for needing more than another 75 years, assuming we don’t blow ourselves up, and do eventually face the limits of large language models head on, is that there is simply a lot to do. I don’t doubt that for a minute. But if we need 7 discoveries, and find them once a decade, I still win the bet.

That said, I will close with a final point of agreement: architecture is all.

Integrating the parts in a whole is a huge huge unsolved problem. LLMs give some illusion of having solved that (because they can talk about so much), and OpenAI just confirmed that they are working on a model with video input, which will surely be interesting, but I think that in achieving AGI we will have _no choice but to find ways of integrating whatever we can get out of deep learning with explicit knowledge and explicit cognitive models_.

I am still not seeing a clean path there, and I don’t think we can say with a straight face that we have achieved the integration we need if a system can’t even check its output against Wikipedia or the AP News Wire.

Since you have thought more about system architecture than anyone I know, I’d especially like to know how you handicap the systems integration race. When will we get to machines that can, like humans, take in information across essentially arbitrary domains and modalities, and put it all together into a reasonably cogent (if occasionally erroneous) understanding of the world?

**Grady Booch:** Yes, ChatGPT is just the start. Yes, a better AI in which we could instill values could make us safer. (But, whose values? Were you and I in leadership positions in the Government of the People’s Republic of China, we’d be having a very different conversation.)  
  
Writing in my best James Bond voice, I never say never. Indeed, as I asserted earlier, the mind is computable and ergo I expect that someday we will have a synthetic mind. The essence of our dissonance seems to be when, and an enumeration of the things we must do to get there.  
  
I think we can agree that the terms AGI and intelligence and sentience and all that are incredibly imprecise and full of emotional baggage. As such, I suspect we are indeed in almost perfect alignment as to the essence of the future except that we are slip sliding on the edges of these symbols. This is why I eschew using the term AGI and why I speak of a spectrum of behaviors. In the next few decades, I expect - as do you - that we’ll go a long way down that path: better common-sense reasoning, some degree of adductive reasoning and theory making and physical reasoning, systems that require far less energy, systems are are more embodied than chatbots that are currently untethered from the physical world and its consequences. We will likely even build AIs that have some sense of self. It’s going to be crazy wonderful. You and I would have been quickly burned at the stake in the 1200s for even suggesting that such things were possible and yet, here we are, both expecting that these things will become manifest almost before our very eyes.  
  
And yes, when we have an AI that can say “I don’t know how to do X but I do have the skills to figure out how to do X and so I will go that, play with it a bit, and then keep trying to do X until I get a reasonable result” that will be a momentous shift. This is why the theories of the world/other/self are important to me: if I have an AI that has some level of cognition, imagine if I apply that cognition to itself. Mechanisms for metacognition are still in their infancy.  
  
There is one other thing I find missing, and you said it yourself: adaptability. Plasticity; agency across domains.  
  
This is why I like [Legg and Hutter’s definition](https://arxiv.org/pdf/0706.3639.pdf) “Intelligence is an agent’s ability to achieve goals in a wide range of environments.” We can today teach an AI how to play any number of different kinds of video games within a particular envelope of behaviors, but getting an AI that has the agency to apply those skills to a completely different domain - controlling a crane in a ship yard, navigating a New York City street to shop, making a meal in a never-before-seen kitchen - we have considerable work to do.  
  
So yes, I think it’s about architecture, the problem of integrating the parts. As I look at the history of cognitive architectures from Simon and Newell’s Logic Theorist to Yann’s latest sketches, we have and we continue to have made remarkable progress in all the individual pieces, but we have not yet found the whole.  
  
To be fair, I must recognize that I have consierable bias and hubris in what I just said, because - as a systems architect - I'm looking at the future of AI from the lens of architecture, and I see progress lacking. We as a field are still very much in the experimental phase of cognitive architectures that scale, but we as an industry are properly trying new things and nudging them to be better and better. The reality that field of AI has begun to discover common design patterns (for example, transfomers) is a sign of growing maturation.  
  
How do we make progress? Far too much money and minds, it seems to me, are focusing on incremental improvements, such that I fear that the field is settling in on a local minimum. I'm happy to see Hinton and others thinking radically. But I think this is only a start.  
  
If I had a complete answer to your question, Gary, I'd be building it right now. Alas, I don't and so I can only try new things and nudge, which is exactly what I'm doing. This, I suppose, is the nature of scientific progress.  
  
I want to close by observing that our dialog has been a great deal of fun for me. These are issues that stike at the heart of what it means to be human, and I can think of fewer other endeavors that give one the privilege and the responsibility to work on things that sit on the edge of something that has the power to amplify the best in us while simultaneously having the power to amplify the worst. This is why these things cannot be left up to us technologists; we should be only one voice in this journey, for what we are doing has the potential to change civilization.

**Gary Marcus** : Hear, hear! When we finally get to software with enough “agency to apply [its] skills to a completely different domain - controlling a crane in a ship yard, navigating a New York City street to shop, making a meal in a never-before-seen kitchen”, one of us will owe the other a pizza!

Thanks for chatting. This was indeed great fun! And I also agree that we need many other voices, not just technologists, speaking up in this journey. (Stay tuned for a sequel!)

[Share](https://garymarcus.substack.com/p/agi-will-not-happen-in-your-lifetime?utm_source=substack&utm_medium=email&utm_content=share&action=share)

 _**[Gary Marcus](http://garymarcus.com) , **scientist, bestselling author, and entrepreneur, is a skeptic about current AI but genuinely wants to see the best AI possible for the world—and still holds a tiny bit of optimism. Sign up to his Substack (free!), and [listen to him on Ezra Klein](https://www.nytimes.com/2023/01/06/opinion/ezra-klein-podcast-gary-marcus.html)._

**Grady Booch** , per Wikipedia, “is an American [software engineer](https://en.wikipedia.org/wiki/Software_engineer), best known for developing the [Unified Modeling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language) (UML) with [Ivar Jacobson](https://en.wikipedia.org/wiki/Ivar_Jacobson) and [James Rumbaugh](https://en.wikipedia.org/wiki/James_Rumbaugh). He is recognized internationally for his innovative work in software architecture, software engineering, and [collaborative development environments](https://en.wikipedia.org/wiki/Collaborative_development_environment).
