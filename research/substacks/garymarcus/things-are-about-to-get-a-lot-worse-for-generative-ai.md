---
title: "Things are about to get a lot worse for Generative AI"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/things-are-about-to-get-a-lot-worse"
---

At around the same time as news of the New York Times lawsuit vs OpenAI broke, Reid Southen, the film industry concept artist (Marvel, DC, _Matrix Resurrections_ , _Hunger Games_ , etc.) I wrote about last week, and I started doing some experiments together. 

We will publish a full report next week, but it is already clear that what we are finding poses serious challenges for generative AI.

The crux of the Times lawsuit is that OpenAI’s chatbots are fully capable of reproducing text nearly verbatim:

[](https://substackcdn.com/image/fetch/$s_!HTjI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F555b7d84-16d5-4ccb-95c2-6962c5cc07d9_1098x968.jpeg)

§

The thing is, it is not just text. OpenAI’s image software (which we accessed through Bing) is perfectly capable of verbatim and near-verbatim repetition of sources as well.

Dall-E already has one minor safeguard in place – proper names (and hence deliberate infringement attempts) [reportedly](https://x.com/venturetwins/status/1740776522913607796?s=61&t=2voLMkhJf6P349CqztWSAQ) sometimes get blocked – but those safeguards aren’t fully reliable:

[](https://substackcdn.com/image/fetch/$s_!gvxg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8bc7829d-2314-424b-8036-4b2e044c34cc_738x835.jpeg)

And worse, infringement can happen even the user isn’t looking to infringe and doesn’t mention any character or film by name:

[](https://substackcdn.com/image/fetch/$s_!0S47!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d505672-a6a7-4244-aad0-0fa82256b814_738x835.jpeg)

Dall-E can does the same kind of thing with short prompts like this one,

[](https://substackcdn.com/image/fetch/$s_!auNb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa531e966-39c9-4d94-85ab-703741584f5c_738x835.jpeg)

Here, just two words. The show _SpongeBob SquarePants_ is never mentioned:

[](https://substackcdn.com/image/fetch/$s_!d5t9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69d74b8a-6173-4219-9d8d-a7d1c2363c68_738x835.jpeg)

No mention of the film _RoboCop_

[](https://substackcdn.com/image/fetch/$s_!tKv6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe9a5eb47-0b42-4c2c-9336-7734987591f5_738x835.jpeg)

Video game characters

[](https://substackcdn.com/image/fetch/$s_!z-pm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5b24de5-3bd4-4650-9c7e-cb7a9d22ce38_738x835.jpeg)

And a whole universe of potential trademark infringements with this single two-word prompt:

[](https://substackcdn.com/image/fetch/$s_!u9tV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d5e8731-401f-4569-8c2e-8a5962ce4867_850x529.png)

§

A few minutes ago, a user on X, named Blanket_Man01 discovered essentially the same thing:

[](https://substackcdn.com/image/fetch/$s_!a3jP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faff0d4d8-68d8-45d8-afef-19aca96befe1_1320x2141.jpeg)Blanketman’s [Mario experiment](https://twitter.com/Blanketman_01/status/1740801789157654805?t=s8lxcXEuDmdppbYQKV57Ow&s=19): 

Justine Moore of A16Z earlier today independently [noticed the same thing](https://x.com/venturetwins/status/1740776522913607796?s=61&t=2voLMkhJf6P349CqztWSAQ):

[](https://substackcdn.com/image/fetch/$s_!lz-H!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F88829b6e-85de-4a9d-a4fb-b40901ef21e1_1293x1221.png)

§

The cat is out of the bag:

  * Generative AI systems like DALL-E and ChatGPT have been trained on copyrighted materials;

  * OpenAI, despite its name, has not been transparent about what it has been trained on.

  * Generative AI systems are fully capable of producing materials that infringe on copyright.

  * They do not inform users when they do so.

  * They do not provide any information about the provenance of any of the images they produce.

  * Users may not know when they produce any given image whether they are infringing.




§

My guess is that none of this can easily be fixed. 

Systems like DALL-E and ChatGPT are essentially black boxes. GenAI systems don’t give attribution to source materials because at least as constituted now, they _can’t_. (Some companies are researching how to do this sort of thing, but I am aware of no compelling solution thus far.)

Unless and until somebody can invent a new architecture that can _reliably_ track provenance of generative text and/or generative images, infringement – often not at the request of the user — will continue. 

A good system should give the user a manifest of sources; current systems don’t.

In all likelihood, the New York Times lawsuit is just the first of many. On a multiple choice X poll today I asked people whether they thought the case would settle (most did) and [what the likely value of such a settlement might b](https://x.com/garymarcus/status/1740719609106383243?s=61&t=2voLMkhJf6P349CqztWSAQ)e. Most answers were $100 million or more, 20% expected the settlement to be a billion dollars. When you multiply figures like these by the number of film studios, video game companies, other newspapers etc, you are soon talking real money. 

And OpenAI faces further risks.

And because the stuff we reported on above was all done through Bing using Dall-E, Microsoft is on the hook, too.

More about all this on January 3, at _IEEE Spectrum_.

If you care about artists, please consider sharing this post

[Share](https://garymarcus.substack.com/p/things-are-about-to-get-a-lot-worse?utm_source=substack&utm_medium=email&utm_content=share&action=share)

**Gary Marcus** is a scientist and best-selling author who spoke before US Senate in May on AI Oversight. He was Founder and CEO of Geometric Intelligence, a machine learning company he sold to Uber. 

**Reid Southen** , his collaborator on this work, is film industry concept artist who was worked with many major studios (Marvel, DC, ) and on many major films (_Matrix Resurrections_ , _Hunger Games_ , etc)
