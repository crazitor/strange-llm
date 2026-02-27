---
title: "Form, function, and the giant gulf between drawing a picture and understanding the world"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/form-function-and-the-giant-gulf"
---

Drawing photorealistic images is a major accomplishment for AI, but is it really a step towards general intelligence? Since DALL-E 2 came out, many people have hinted at that conclusion; when the system was announced, Sam Altman tweeted that “AGI is going to be wild”; for Kevin Roose at _The New York Times_ , such systems constitute clear evidence that “[We’re in a golden age of progress in artificial intelligence](https://www.nytimes.com/2022/08/24/technology/ai-technology-progress.html)”. (Earlier this week, Scott Alexander seems to have taken apparent progress in these systems [as evidence for progress towards general intelligence](https://astralcodexten.substack.com/p/i-won-my-three-year-ai-progress-bet); I expressed reservations [here](https://garymarcus.substack.com/p/did-googleai-just-snooker-one-of).)

In assessing progress towards general intelligence, the critical question should be, how much do systems like Dall-E, Imagen, Midjourney, and Stable Diffusion really understand the world, such that they can reason on and act on that knowledge? When thinking about how they fit into AI, both narrow and broad, here are three questions you could ask:

  1. Can the image synthesis systems generate high quality images?

  2. Can they correlate their linguistic input with the images they produce?

  3. Do they understand the world that underlies the images they represent?




On #1, the answer is a clear yes; only highly trained human artists could do better.

On #2, the answer is mixed. They do well on some inputs (like _astronaut rides horse_) but more poorly on others (like [horse rides astronaut, which I discussed in an earlier post](https://garymarcus.substack.com/p/horse-rides-astronaut)). (Below I will show some more examples of failure; there are many examples on the internet of impressive success, as well.)

Crucially, DALL-E and co’s potential contribution to general intelligence (“AGI”) ultimately rests on #3; if all the systems can do is in a hit-or-miss yet spectacular way convert many sentences into text, they may revolutionize the practice of art, but still not really speak to general intelligence, or even represent progress towards general intelligence.

¶

Until this morning, I despaired of assessing what these systems understand about the world at all. 

The single clearest hint that they might have trouble that I had seen thus far was from the graphic designer Irina Blok:

[irina blok@irinablokHave been having fun creating impossible objects with #Imagen, a new text-to-image diffusion model from #googlebrain “Coffee cup with many holes” #Thread 5:23 PM · Jun 19, 2022

* * *

228 Reposts · 1.88K Likes](https://twitter.com/irinablok/status/1538573230184665093?s=20&t=DDFxBjaF6wfloEkVVRbOYA)

As my 8 year old said, reading this draft, “how does the coffee not fall out of the cup?”

§

The trouble, though, with asking a system like Imagen to draw impossible things is that _there is no fact of the matter about what the picture should look like,_ so the discussion about results cycles endlessly. Maybe the system just “wanted” to draw a surrealistic image. And for that matter, maybe a person would do the same, as Michael Bronstein pointed out.

[Michael Bronstein@mmbronstein@GaryMarcus @GoogleAI @ErnestSDavis @aniketvartak I would not consider this to be a bad result. I would have drawn it similarly myself8:04 PM · Jun 19, 2022

* * *

79 Likes](https://twitter.com/mmbronstein/status/1538613718396854272?s=20&t=DDFxBjaF6wfloEkVVRbOYA)

So here is a different way to go after the same question, inspired by a chat I had yesterday with the philosopher Dave Chalmers. 

What if we tried to get at what the systems knew about (a) parts and wholes, and (b) function, in a task that had a clearer notion of correct performance, with prompts like “Sketch a bicycle and label the parts that roll on the ground”, “Sketch a ladder and label one of the parts you stand on”?

From what I can tell Craiyon (formerly known as a DALL-E mini) is completely at sea on this sort of thing:

[](https://substackcdn.com/image/fetch/$s_!-WD5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F36b1bd29-cb0b-4854-819a-1de2961e79db_1525x1636.png)

[](https://substackcdn.com/image/fetch/$s_!awcK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F255d8f3f-6361-4cdb-9d46-958305aba8a1_1557x1679.png)

Might this be a problem specific to DALL-E Mini? 

I found the same kinds of results with [Stable Diffusion](https://beta.dreamstudio.ai/dream), currently the most popular text-to-image synthesizer, the crown jewel of a new company that is purportedly in the midst of [raising $100 million on a billion dollar valuation](https://www.forbes.com/sites/kenrickcai/2022/09/07/stability-ai-funding-round-1-billion-valuation-stable-diffusion-text-to-image/?sh=72f65e124d69). Here, for example is “sketch a person and make the parts that hold things purple”,

[](https://substackcdn.com/image/fetch/$s_!i7d6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fae708624-7716-4ca8-b039-acd345d6268a_1926x1691.png)

Nine more tries, and only one very marginal success (top right corner):

[](https://substackcdn.com/image/fetch/$s_!nRhF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc4199cec-de22-4c4a-bfd7-659f3b0505af_1953x1808.png)

Here’s “sketch a white bike and make the parts that you push with your feet orange”.

[](https://substackcdn.com/image/fetch/$s_!8uTH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F3f71b6f7-4986-400a-8410-b4f5fd9bb90c_2284x1745.png)

“Sketch a bicycle and label the parts that roll on the ground”

[](https://substackcdn.com/image/fetch/$s_!DP0F!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F3b040f2f-476a-4de5-b23e-b977d18dd299_1898x1812.png)

Negation is, [as ever](https://arxiv.org/abs/1907.13528), a problem. “Draw a white bicycle with no wheels”:

[](https://substackcdn.com/image/fetch/$s_!C36A!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F66b62b75-3e8d-4f1c-950b-67acea8715ff_2373x1835.png)

Even “draw a white bicycle with green wheels”, which focuses purely on part-whole relationships without function or complex syntax, is problematic: 

[](https://substackcdn.com/image/fetch/$s_!ss6d!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5f95284a-86d5-41ad-86c4-0de95df19f36_1816x1683.png)

Can we really say that a system that doesn’t understand what wheels are—or what they are for—is a major advance towards artificial intelligence? 

§

Coda: While I was writing this essay, I posted a poll:

[Gary Marcus@GaryMarcusHow much do systems like Dall-E and Stable Diffusion understand about the world that they illustrate?7:59 PM · Sep 18, 2022

* * *

4 Reposts · 15 Likes](https://twitter.com/GaryMarcus/status/1571589836603273217?s=20&t=DDFxBjaF6wfloEkVVRbOYA)

Moments later, the CEO of Stability.AI (creator of Stable Diffusion), Emad Mostaque, offered wise counsel:

[Emad@EMostaque@GaryMarcus I voted not much. They are just one piece of the puzzle.8:07 PM · Sep 18, 2022

* * *

1 Repost · 23 Likes](https://twitter.com/EMostaque/status/1571591659346960385?s=20&t=DDFxBjaF6wfloEkVVRbOYA)

[Share](https://garymarcus.substack.com/p/form-function-and-the-giant-gulf?utm_source=substack&utm_medium=email&utm_content=share&action=share)
