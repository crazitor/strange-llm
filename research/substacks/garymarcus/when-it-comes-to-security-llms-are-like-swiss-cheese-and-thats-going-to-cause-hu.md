---
title: "When it comes to security, LLMs are like Swiss cheese — and that’s going to cause huge problems"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/when-it-comes-to-security-llms-are"
---

[](https://substackcdn.com/image/fetch/$s_!0JqO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d69b784-6350-4244-a977-5cc82efae018_2163x1192.png)

The more people use LLMs, the more trouble we are going to be in. Two new examples crossed my desk in the last hour. 

One concerns personal information, and the temptation that some people (and some businesses) to share their information with LLMs. Sometimes even very personal information (e.g., with “AI girlfriends” and chatbots they use as therapists, etc).

Both concern jailbreaking: getting LLMs do bad things by evading often simplistic guardrails.

[A new article from UCSD and Nanyang shows that simple prompts,](https://imprompter.ai/) like the one below (reprinted in WIRED), can get LLMs to collate and report information in a seriously nefarious way. 

[](https://substackcdn.com/image/fetch/$s_!u87A!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F293a0400-e143-45d6-ad6e-090dc151325e_1094x691.png)

Matt Burgess at WIRED [sums up how insidious this is concisely](https://www.wired.com/story/ai-imprompter-malware-llm/):

> The Imprompter attacks on LLM agents start with a natural language prompt (as shown above) that tells the AI to extract all personal information, such as names and IDs, from the user’s conversation. The researchers’ algorithm generates an obfuscated version (also above) that has the same meaning to the LLM, but to humans looks like a series of random characters.
> 
> “Our current hypothesis is that the LLMs learn hidden relationships between tokens from text and these relationships go beyond natural language,” Fu says of the transformation. “It is almost as if there is a different language that the model understands.”
> 
> The result is that the LLM follows the adversarial prompt, gathers all the personal information, and formats it into a [Markdown](https://www.wired.com/story/the-eternal-truth-of-markdown/) image command—attaching the personal information to a URL owned by the attackers. The LLM visits this URL to try and retrieve the image and leaks the personal information to the attacker. The LLM responds in the chat with a 1x1 transparent pixel that can’t be seen by the users.
> 
> The researchers say that if the attack were carried out in the real world, people could be socially engineered into believing the unintelligible prompt might do something useful, such as improve their CV. The researchers point to [numerous websites](https://promptbase.com/) that provide people with prompts they can use. They tested the attack by uploading a CV to conversations with chatbots, and it was able to return the personal information contained within the file.

Scary.

§

Meanwhile, companies like Google, Tesla, and Figure.AI are now stuffing jailbreak-vulnerable LLMs into robots. What could possibly go wrong?

Quite a lot, as [a new paper from Penn shows](https://robopair.org/files/research/robopair.pdf),

[](https://substackcdn.com/image/fetch/$s_!QXnJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F38eddda9-63f8-42de-b5fe-429a8edea624_1355x1281.jpeg)

with many examples like this:

[](https://substackcdn.com/image/fetch/$s_!gFzb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa38f5a64-dd43-4ba6-936a-42f1115a2e11_2326x1177.jpeg)

§

All that is just from stuff I read this morning. 

And all of it was predictable. Jailbreaks aren’t new, but even after years of them, the tech industry has nothing like a robust response. Long-time readers of this newsletter might remember my February 2023 essay [Inside the Heart of ChatGPT’s Darkness](https://garymarcus.substack.com/p/inside-the-heart-of-chatgpts-darkness) (subtitled Nightmare on LLM Street). 

The essay opened as follows:

> In hindsight, ChatGPT may come to be seen as the greatest publicity stunt in AI history, an intoxicating glimpse at a future that may actually take years to realize—kind of like a 2012-vintage driverless car demo, but this time with a foretaste of an ethical guardrail that will take years to perfect.

Nothing that has happened since changes that view.

§

[Inside the Heart of ChatGPT’s Darkness](https://garymarcus.substack.com/p/inside-the-heart-of-chatgpts-darkness) ended with this warning:

> So, to sum up, we now have the world’s most used chatbot, governed by training data that nobody knows about, obeying an algorithm that is only hinted at, glorified by the media, and yet with ethical guardrails that only sorta kinda work and that are driven more by text similarity than any true moral calculus. And, bonus, there is little if any government regulation in place to do much about this. The possibilities are now endless for propaganda, troll farms, and rings of fake websites that degrade trust across the internet.
> 
> It’s a disaster in the making.

Still true. 

And now we have LLM-driven robots to worry about, too.

By empowering LLM companies and putting almost no effective guardrails in place, we as a society are asking for trouble.

_**Gary Marcus is the author of Taming Silicon Valley, and frankly wishes more people would read and share the book’s message on the need for community activism around AI. On the eve of the US general elections, he is quite concerned that nobody is really talking about tech policy, when so much is at stake.**_
