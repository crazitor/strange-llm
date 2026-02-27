---
title: "Decoding (and debunking) Hard Fork’s Kevin Roose"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/decoding-and-debunking-hard-forks"
---

Kevin Roose’s [latest essay](https://www.nytimes.com/2025/02/27/technology/personaltech/vibecoding-ai-software-programming.html?smid=nytcore-ios-share&referringSource=articleShare) in The New York Times is, like a lot of essays, dreamy, offering a vision of bold new reality, while underplaying the obstacles to that reality. His editors, and his audience, seem to love this sort of thing. 

To be candid, I don’t. A lot of it feels to me like marketing for big tech, and only serves to make the tech oligarchs stronger. Roose’s latest essay is a case in point. It’s brilliantly written, and I am sure will be one of the most read this weekend. Like so many of Roose’s essays, it promises imminent revolution. 

This essay is about using AI tools to code:

[](https://substackcdn.com/image/fetch/$s_!-Ar9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6c076d9-1fed-40ee-b67f-1086773eee3b_1648x2119.jpeg)

In the meat of the essay, Roose describes his process building apps with new AI tools, and Roose even lets the readers use a variation on one the apps he created, called LunchBox Buddy. Take a picture of your fridge, and get lunch ideas:

[](https://substackcdn.com/image/fetch/$s_!S5uD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F576133f8-4862-444b-bf1c-b516aa93fe17_2062x1456.png)In principle you can visit [https://www.nytimes.com/2025/02/27/technology/personaltech/vibecoding-ai-software-programming.html](https://www.nytimes.com/2025/02/27/technology/personaltech/vibecoding-ai-software-programming.html?smid=nytcore-ios-share&referringSource=articleShare) for a live demo. I couldn’t get it to work on my Ipad, however.

along with an impressive-seeming backstage view at the code the AI system generated:

[](https://substackcdn.com/image/fetch/$s_!dLZP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3013f56a-b403-4b52-9664-5e45d6850fe8_2071x1490.png)

The piece isn’t just enthusiastic, it’s over-the-top:

> … building software this way — describing a problem in a sentence or two, then watching a powerful A.I. model go to work building a custom tool to solve it — is a mind-blowing experience. It produces a feeling of [A.I. vertigo](https://www.nytimes.com/2024/05/17/podcasts/hardfork-gpt4o-ai-overviews.html), similar to what I felt after using ChatGPT for the first time.

Almost every reader is likely to be similarly blown away.

§

Alas, what you look at the _details_ in what he wrote, there are four serious problems. 

  1. As Ernest Davis and I discussed in the introduction to Rebooting AI (see excerpt at the end of this essay), the most important question in AI always is: is some apparently impressive behavior general? Are we just seeing regurgitation? How far can the system go before it breaks down? As it turns out, there are _already_ lots of libraries and tutorials on the web for code to take photos of fridges and propose recipes. Roose’s idea of recipe-from-photo is not original, and the code for it already exists; the systems he is using presumably trained on that code. It is seriously negligent that Roose seems not to have even asked that question.

Here’s the first example I found on Github, called Deep-food, essentially identical in spirit, “Make a photo of your fridge, recognize ingredients and generate matching recipes with deep learning”. Anyone can download the code, and probably most or all of the AI systems were trained on this and other similar examples.

[](https://substackcdn.com/image/fetch/$s_!WjOU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc448010f-e222-4b21-bdf2-1ffb2e9c2b2b_2370x1448.jpeg)

For that matter, versions of the entire app are already out there (and unmentioned), like this one:




[](https://substackcdn.com/image/fetch/$s_!icoJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F235cdcce-9144-43bf-ad84-9b0e40d8c46a_1657x1441.png)

I have seen “AI influencers” trumpeting AI code systems writing code for Tetris and Breakout (which often serves as coding 101 tutorials); this is not much better.

Needless to say, the art of coding generally lies in building something _new_. Here Roose has displayed the cardinal sin of looking only at regurgitation rather than generalization. History has told us over and over that systems can be good at the former and still face enormous challenges at the latter. 

  2. Roose has also committed (not for the first time) the fallacy of misunderstanding the 80:20 rule that guides so much of AI: it’s often easy to get a solution that is 80% correct, and extremely difficult to get the last 20%. Driverless cars have been like that for _decades_. (Roose acknowledge that current systems are buggy but never seriously considers that it might actually be quite a challenge to get the last 20% correct.) We have seen this before. In 2023, for example, he wrote some effusive pieces about chatbots, in which he acknowledged the existence of hallucinations, but wildly underestimated how recalcitrant they would be. A new study of the latest system, GPT 4.5 [showed that by on one standardized measure over 1/3 of the outputs are still hallucinations](https://ca.news.yahoo.com/openai-admits-model-still-hallucinates-140042140.html). Errors in the code of automatic code writing systems will likely persist for decades, especially when they are forced to construct genuinely novel systems.

  3. Any coder with any chops at all knows that is one thing to write code, and another to debug it (and still another to maintain it, a year or a decade latter, which is even harder). By his own admission, Roose has never written a line of code, so presumably never debugged one, either, which is often a much harder task. Perhaps for this reason, he has wildly underestimated how hard for a noncoder fix the code written by these autogenerated systems. What happens if the image system goes astray? If the recipe recommends an ingredient that is hard to source? Or the system fails to understand that given recipe that requires more of some ingredient than is currently in the fridge? How will the user fix any of this? None of this may matter much in a lunch-recipe recommender, but errors in an automatic email writing system could cause serious harm. I can’t imagine that noncoders are really going to get those systems to work well enough for prime time (except perhaps in very very narrow use cases), let alone know what do when the back end internet calls break. Omitting the challenges in debugging the output of automated code systems very much distorts how readily these systems can and will be used in the real world. 

  4. The Times has (evidently) let Roose have his say yet again without forcing him to run his ideas past experts. Almost anyone in the field could have told him that the examples he used were too easy and too obvious to serve as a real test of anything, and that he was wildly underestimating what would be involved in debugging or pushing these kinds of tools to more complex use cases, let alone maintaining the code in the long run. In the end, this essay, like a lot of Roose’s pieces, comes off as marketing for AI companies, even though it is framed as reporting. The Times owes its readers better. 




You can see similar things for example in Roose’s NYT Hard Fork podcast the other day with Anthropic’s CEO Dario Amodei, in which he and his co-host Casey Newton essentially accept everything Amodei says without questioning, doing more to channel Amodei than to challenge him. Newton, whose boyfriend recently started work for Amodei’s Anthropic, assures us that there is no conflict of interest, but it is hard to imagine a friendlier interview. How can we say there no punches pulled, when no punches were even thrown? [Ed Zitron](https://www.wheresyoured.at/rockstars/) and [Edward Ongweso Jr](https://thetechbubble.substack.com/p/the-phony-comforts-of-useful-idiots) attacked Newton for his closeness with tech industry and oversimplified narratives and I can see why.

§

HardFork gives you [credulous dialog like this:](https://www.nytimes.com/2025/02/28/podcasts/hardfork-anthropic-dario-amodei.html?showTranscript=1)

[](https://substackcdn.com/image/fetch/$s_!lV8P!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa58d4cda-b2cb-438e-afe2-66797a6e8a56_1542x789.png)

They never let you know that a significant number of real world coders are deeply frustrated with automated coding tools like Cursor.AI (which is in part powered by Anthropic’s Claude):

[](https://substackcdn.com/image/fetch/$s_!OX06!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1777b109-2b9b-495e-8358-331a79a1a723_1422x947.jpeg)

and [this long, devastating analysis from the technology author Mayo Olshin](https://x.com/mayowaoshin/status/1833557628401627245?s=61):

[](https://substackcdn.com/image/fetch/$s_!8P7B!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffb5feb5b-50c8-442f-a14e-a715c96bf208_2634x2349.jpeg)

The last paragraph says it all “If however, you simply "trust" the Al outputs due to lack of knowledge, skill, or willingness to review results, the long term damage will outweigh the initial productivity gains you got so "hyped" about.”

§

So what’s news here, where Roose and his HardFork partner Newton are already so chummy with industry, often only giving one side of a story?

My specific concern here, and [I hinted at this once before in a different context](https://garymarcus.substack.com/p/the-hottest-new-programming-language), is that children are going to stop learning to code based on a misrepresentation of reality. Many parents and educators will read what and take seriously what Roose has to say, given how prominent the Times is, and that may have consequences. People are increasingly going to discourage American children from learning to code based on naive enthusiasm from people like Roose. They will think there is little incentive to code or to understand how software really works. This will leave the US flat-foooted. 

My guess is that the powers-that-be in China won’t be so foolish; in times, we will lose our historically strong lead in coding, and wind up seriously behind. Already, of course, DeepSeek has shown that our once strong lead is diminishing.

At least for another decade or two and probably more, big projects are always going to require software architects who know what they are doing. If hype deters kids from learning to code, we are screwed.

§

Lest this section seem speculative, I would note that we have actually seen this movie before. In 2016 Geoff Hinton said “We should stop training radiologists now, it's just completely obvious within five years deep learning is going to do better than radiologists”. Nine years later and hundreds of startups later, my understanding is that not one radiologist has been replaced, and many parts of the world actually have a _shortage_ of radiologists. 

With people like Roose hyping automated coding, we may well find ourselves with too few coders. By hyping the tech largely uncritically, the Rooses and Newtons of the world make the tech oligarchy stronger; society inevitably has to bear the costs.

[Share](https://garymarcus.substack.com/p/decoding-and-debunking-hard-forks?utm_source=substack&utm_medium=email&utm_content=share&action=share)

 _Gary Marcus and his long time_ _collaborator gave some advice to journalists in their 2019 book Rebooting AI that is reprinted below._

[](https://substackcdn.com/image/fetch/$s_!moGN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43cbb054-ba81-4d72-b328-fbec97db0f05_1177x955.jpeg)
