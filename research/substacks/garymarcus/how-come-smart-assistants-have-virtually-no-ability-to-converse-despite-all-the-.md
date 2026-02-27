---
title: "How come smart assistants have virtually no ability to converse, despite all the spectacular progress with large language models?"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/how-come-smart-assistants-have-virtually"
---

[](https://substackcdn.com/image/fetch/$s_!ixLv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc154c79e-f0af-4a38-993a-4dfa41be402a_1719x1541.jpeg)

Just got a fantastic question from a cognitive science Ph.D. student Mercury Mason, good and important enough that it could be a final exam. See if you can figure it out: 

[merc@___merc___@GaryMarcus why is it that “smart assistants” have virtually no ability to converse. not even poorly — it’s completely absent (besides responding to known prompts). is it a scale issue or something? genuinely curious.1:50 AM · Nov 22, 2022](https://twitter.com/___merc___/status/1594870857251573760?s=12)[merc@___merc___@j_q_balter @GaryMarcus i’d argue that the tech *exists* — it isn’t perfect by any means, but the state of the art language models are decent and are far more sophisticated than what is currently available from siri, alexa, google, etc. why they don’t even try to build that in is what i was wondering3:33 PM · Nov 22, 2022](https://twitter.com/___merc___/status/1595078051922169857?s=12.)

It's worth asking since (a) Amazon is apparently greatly reducing Alexa's staff, (b) hasn't added significant features in years, and (c) seems clumsy and limited compared to GPT-3. And it gets at some important realities about current AI that aren't fully appreciated. 

I will give five answers of my own, below (but you can pause here if you want to take a guess, yourself).

§

Let’s start with some answers that probably aren’t right.

Could it be that nobody at Amazon has read the recent literature? Almost certainly not. Amazon probably *is* using large language models for product search. (This may be why you often get good results for synonyms and typos, but also get a lot of stuff you don't want, like asking for AAA batteries and getting a bunch of C batteries mixed in). Yet Alexa obviously isn't conversing in the way that GPT-3 is. 

Another theory? Maybe Amazon doesn't want to pay the licensing fees. Nope, that's not it either; they could easily spin up an instance of an LLM on AWS, and probably afford the cost (one-time training is expensive, runtime less so). 

And I don’t think scaling is the real issue either. Amazon’s engineers are Masters of Scale, and certainly the company doesn’t lack for processing power or data, either.

Here are my five best guesses; I suspect all five contributed:

  1. LLMs are inherently unreliable. If Alexa were to make frequent errors, people would stop using it. Amazon would rather you trust Alexa for a few things like timers and music than sell you a system with much broader scope that you stop trusting and stop using.

  2. LLMs are unruly beasts; nobody knows how to make them refrain 100% of time from insulting users, giving bad advice, or just plain making stuff up. (Galactica was an epic failure in this regard.)

  3. Amazon doesn't want to get sued. Any one of these scenarios of LLMs gone awry (bad advice, insults, lies etc) could hurt the Amazon brand, open up litigation, etc.. It's just not worth the risk.

  4. Alexa has to do stuff in the world, like turning on lights, playing music, opening shades, etc; if Alexa could converse freely, user expectations would go through the roof, and mostly be unmeetable. (You could tell Alexa to wash the dishes, but until their robot division really picks up speed, that ain’t happening.)

  5. LLMs spit our words, not actions (and not API calls either). When an LLM produces a sentence, you can't directly use that sentence to control stuff, unless you build another system to parse the sentences into actions. Nobody knows how to do this reliably, either.




Bottom line: From the outset Large Language Models like GPT-3 have great at generating surrealist prose, and they can beat a lot of benchmarks, but they are not (and may never be) great tech for reliably inferring user intent from what users say.

Turning LLMs into a product that controls your home and talks to you in a way that would be reliable enough to use at scale in millions of homes is still a long, long way away. See also [my essay on Google’s Palm-SayCan](https://garymarcus.substack.com/p/whats-wrong-with-googles-new-robot), for what might happen if this tech were embedded in robots, which would be even more risky.

. 
