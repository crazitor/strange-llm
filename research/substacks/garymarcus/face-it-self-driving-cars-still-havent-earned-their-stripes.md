---
title: "Face it, self-driving cars still haven’t earned their stripes"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/face-it-self-driving-cars-still-havent"
---

[](https://substackcdn.com/image/fetch/$s_!Br5I!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb61eddce-217b-4fa2-befc-dbd52ad840d8_1100x609.jpeg)From a 2016 _New York Times_ article on self-driving cars, which began “Autonomous cars have arrived. Major automakers have been investing billions in development, while tech players … have been testing their versions in American cities.” How’s that working out?

I hate to say I told you so, and I am by no means the only one who said so, but driverless cars (still) have a problem. That problem, which I have emphasized dozens of times over the last several years, is _edge cases_ , out-of-the-ordinary circumstances that often confound machine learning algorithms. The more complicated a domain is, the more unanticipated outliers there tend to be. And the real world is really complicated and messy; there’s no way to list all the crazy and out of ordinary things that can happen. Nobody has yet figured out how to build a driverless car that can deal with that fact.

One of the the first times I emphasized how challenging the edge case problem was for driving was in a [2016 interview](https://www.edge.org/conversation/gary_marcus-is-big-data-taking-us-closer-to-the-deeper-questions-in-artificial), when tired of the hype, I unloaded at length. It’s eerie to read the transcript now, more or less just as applicable today as it was then; nearly every word still applies:

> All of this apparent progress is being driven by the ability to use brute force techniques on a scale we've never used before. That originally drove Deep Blue for chess and the Atari game system stuff. It's driven most of what people are excited about. At the same time, it's not extendable to the real world if you're talking about domestic robots in the home or driving in the streets. 
> 
> … think about driverless cars. What you find is that in the common situations, they're great. If you put them in clear weather in Palo Alto, they're terrific. If you put them where there's snow or there's rain or there's something they haven't seen before, it's difficult for them. There was a great piece by Steven Levy about the Google automatic car factory, where he talked about how the great triumph of late 2015 was that they finally got these systems to recognize leaves. 
> 
> It's great that they do recognize leaves, but there're a lot of scenarios like that, where if there's something that's not that common, there's not that much data. You and I can reason with common sense. We can try to figure out what this thing might be, how it might have gotten there, but the systems are just memorizing things. So that's a real limit… 
> 
> The same thing might happen with behavior. You try this out in Palo Alto, all the drivers are relaxed; you try it in New York, and you see a whole different style of driving. The system may not generalize well to a new style of driving… 
> 
> You and I can use some reasoning about the world. If we see a parade, maybe we don't have a lot of data about parades, but we see the parade and we say, "There're a lot of people, so let's stop and wait a while." Maybe the car gets that, or maybe it gets confused by the mass of people and doesn't recognize it because it doesn't quite fit into its files for individual people...
> 
> There's a huge problem in general with the whole approach of machine learning, which is that it relies on a training set and a test set, the test set being similar to the training set. Training is all the data that you've memorized, essentially, and the test set is what happens in the real world. 
> 
> When you're using machine learning techniques, it very much depends on how similar the set of test data to the training data that I've seen before is.

Snow and rain aren’t quite as much as a problem as they were then, but edge cases have by no means gone away. The degree to which you are safe in a driverless car still depends too much on the vagaries of data, and not enough on reasoning. (If that doesn’t remind you of LLMs, you aren’t paying attention.)

§

Yet the lust for getting this not yet-fully-baked technology continues unabated. Just last week the California Public Utilities Commission approved Cruise and Waymo, two of the biggest groups attempting to build self-driving cars, for operation 24/7, across all of San Francisco, given the companies far more leeway to test their cars.

A few hours later, one well-known techno-optimist all but declared victory, posting on X, “They promised us self-driving cars, and all we got was self-driving cars, slightly late”.

Well, no, not exactly. To begin with, license to test the car is not the same thing as saying they work; it was a (mis)calculated bet by some bureaucrats, not a definitive, peer-reviewed scientific thumbs up. 

In fact, the truth is we don’t actually have _any_ truly self-driving cars yet. As Cade Metz explained to me a couple months ago on my podcast, _Humans versus Machines_ , literally every “self-driving vehicle” on public roads has either a human safety driver on board, or some human somewhere watching remotely who can help the vehicle out when issues arises.

And, it’s not just that literally every proto-self-driving-car stills need a nanny. It’s that they also still struggle (that’s what the whole episode with Metz was about). And sure enough increasing operations has led chaos. And it didn’t take long. One of my favorite colleagues in the field wrote to me on Monday, shortly after the CPUC decision, “I am super confident this is going to be a &)@$ show”.

She was right. And it didn’t take long to find out.

§

Less than a week in fact. Five days later, the _The New York Times_ reads on one of my own litanies on AI Gone Wrong:

[](https://substackcdn.com/image/fetch/$s_!jB9V!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9c8ce15c-b389-4b7b-af4c-ab0449d80d19_1346x1208.jpeg)

Stuck in concrete?? Now there’s a novel edge case. Even more hilarious than [a Tesla running into a parked jet](https://www.youtube.com/watch?v=umbpc47iR64).

No matter how much data these things are trained on, there’s _always_ something new. 

§ 

Another ten “self-driving” cars failed in the last week because they lost contact with mission control, and without it, they were lost, stalled right in the middle of a busy street:

[](https://substackcdn.com/image/fetch/$s_!CsXr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd5598c99-b9cb-4128-973f-c74bbe74760a_1262x431.jpeg)

§ 

Driverless cars have been given every advantage in life: [over $100 billion in funding](https://www.bloomberg.com/news/features/2022-10-06/even-after-100-billion-self-driving-cars-are-going-nowhere), almost as much adulatory press as (the far more deserving) Taylor Swift, and, now, license to roam, despite all the known issues and the well-established reality that the unknown unknowns seemingly never end. 

I honestly don’t know what the California Public Utilities Commission was thinking; none of the independent scientists I know follow these things would have endorsed the idea.

Scaling up to driving everywhere all the time without a well-vetted serious, well-vetted solution to the edge case problem was insane; it was quite literally an accident (or series of accidents) waiting to happen.

I hope some lessons have been learned.

§

And not just for driverless cars, but for mission-critical uses of machine learning in general. 

Edge cases are everywhere; they are in driving, they are in medicine, they there will be a zillion of them humanoid robots, if and when we roll them out. Anyone who thinks any of this is going to be easy is fooling themselves.

In a different world, less driven by money, and more by a desire to build AI that we could trust, we might pause and ask a very specific question: _have we discovered the right technology to address edge cases that pervade our messy really world_? And if we haven’t, shouldn’t we stop hammering a square peg into a round hole, and shift our focus towards developing new methodologies for coping with the endless array of edge cases?

If we don’t, we are likely to see reprises of what we see now with driverless cars, in automated doctors, automated psychiatrists, all purpose virtual assistants, home robots, and more, probably for years to come.

§ 

As a brief coda, I wrote this essay on an airplane, a 747-400 to be exact. The 747 has an autopilot, engaged for a very large fraction of the nine hour flight, but it has a human crew, too, and that’s the way I like it, humans-in-the-loop. 

I wouldn’t trust a self-driving plane, and I don’t think any quasi-self-driving car has yet earned its stripes either. 

[Share](https://garymarcus.substack.com/p/face-it-self-driving-cars-still-havent?utm_source=substack&utm_medium=email&utm_content=share&action=share)

**Gary Marcus** , is co-founder and CEO of ca-tai.org, and in May spoke about some (but not all) of the many risks of AI at a US Senate Judiciary Subcommittee on AI oversight. For more on driverless cars, you can listen to Episode 2 of his eight-part podcast _Humans versus Machines_.
