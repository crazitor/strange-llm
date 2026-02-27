---
title: "I set up a ChatGPT voice interface for my 3-year old. Here’s how it went."
author: "Arvind Narayanan & Sayash Kapoor"
date: ""
source: "substack_aisnakeoil"
url: "https://www.normaltech.ai/p/i-set-up-a-chatgpt-voice-interface"
---

A few weeks ago I set up a voice interface to ChatGPT for my 3-year old. I wasn’t sure what to expect, but the experience has been surprisingly positive. I ended up learning a lot about the opportunities and risks of young children’s interaction with chatbots.

**Why do this?**

I expect that AI agents will be a big part of my children’s lives, so it felt natural to expose them to chatbots sooner than later. I have always been an early adopter of tech. I’m also pretty optimistic about the potential for AI agents to enrich our lives — although mindful of the risks and limitations, which is what we primarily cover on this blog.

My wife and I have a pro-screen time approach to parenting, and our 3-year old has long had her own iPad. More accurately, I believe that screen time is [not a useful category](https://rachel.fast.ai/posts/2022-09-06-homeschooling/), and whether or not screen time is beneficial entirely depends on what’s on the screen. Active interaction with a bot is a much better use of screen time than passive video watching. Finally, the chatbot is not a replacement for quality time with a parent. It _is_ quality time with a parent: her use of the chatbot always involves a parent participating in the interaction as well.

**OK, but why write about it?**

If any parents are considering allowing a young child to use chatbots, I hope that this writeup will be useful to help get the most out of chatbots and minimize the risks. I’m not advocating that anyone do this — it’s an intensely personal decision.

On that note, if you have opinions about my parenting and are looking for the comment button, please keep your thoughts to yourself. Like I said, these decisions are intensely personal, and I’m not going to debate them on the Internet.

**How to set up a chatbot voice interface**

For young kids to use chatbots, two customizations are necessary. The first is voice input and output. Many apps that extend ChatGPT are available, but I decided to roll my own using the OpenAI API. For voice input, I found that Apple dictation is good enough, so I went with that. And even if it makes an error, ChatGPT is really good at inferring what was meant! But for voice _output_ , Apple’s native text-to-speech feature is unfortunately atrocious, so I had to plug it into [Google’s service](https://cloud.google.com/text-to-speech) instead. ChatGPT was extremely helpful for doing the programming, especially dealing with unfamiliar APIs, and cut the development time a lot.

The second customization is to use the system prompt in the OpenAI API to inform ChatGPT that the user is a 3-year old. The bot was surprisingly good at adjusting the content, vocabulary, and tone of its output appropriately. This is what made the whole thing a success. I’ll give examples throughout the rest of the post. 

Now let me tell you how my daughter has been using it.

**Use case 1: learning**

Literally the first question my daughter asked was:

What happens when the lights turn out?

Here was the response:

> When the lights turn out, it gets dark, and it can be a little scary. But don't worry! There are lots of things you can do to feel safe and comfortable in the dark.
> 
> One thing you can do is use a nightlight. A nightlight is a small light that stays on all night long. It can help you see a little bit in the dark and make you feel less scared.
> 
> You can also use a flashlight or a torch to help you see in the dark. You can ask your mom or dad to show you how to use one.
> 
> Remember that it's normal to feel a little bit scared in the dark, and that it's okay to ask for help if you need it. You can always call out for your parents if you need them, and they will be there to help you.

I was taken aback by the fact that it simulates empathy for the child. In fact, this turned out to be a consistent feature: the bot took on the role of an adult friend. I did not explicitly ask it to adopt this personality. 

My daughter was visibly relieved to hear the reassuring explanation. We had no idea that she had any anxiety about the dark. If she’d asked me the question, I would have assumed she was asking out of curiosity about light and electricity and stuff. But she’s never asked us that. Something about how she conceptualizes the chatbot seems to have gotten her to open up.

Note that without telling ChatGPT that the user is a child, when asked the same question it produces responses that are completely unsuitable for a young child in terms of the conceptual and vocabulary level.

> When the lights turn off, the absence of light can result in a number of changes depending on the environment and the time of day. Here are a few examples:

(I won’t bore you with the rest of the answer.)

My daughter uses the bot to learn about many topics, including ChatGPT itself. She knows that the bot isn’t a person, that it doesn’t have a body or feelings, and that the responses are coming from a computer far away through Internet cables.

The idea that she can independently explore things that she wants to learn without depending on an adult is empowering (although, for now, her chatbot interactions are supervised). Independence is a big theme in young children’s development.

The accuracy of ChatGPT’s responses is not an issue because essentially any question that 3-year olds tend to ask is simple enough that ChatGPT seems to answer correctly. 

**Use case 2: stories**

My daughter loves to hear stories, especially new ones she hasn’t heard before. Having to make up new stories on demand can quickly get exhausting for a parent!

ChatGPT is in some ways better than people and in other ways worse than people at telling stories to 3-year olds. When you simply ask it to tell a story, the stories it tells have a formulaic structure. I’ve also seen reports that its stories reflect gender stereotypes. I don’t doubt this, but it hasn’t happened so far (and if it does, I’m confident that it’s avoidable by modifying the system prompt).

ChatGPT shines when you ask for a story about a specific topic. My daughter wanted a story about a T-Rex that ate legos. ChatGPT responded with a story of a T-Rex whose owners tried many things to get it to eat real food instead of legos, and finally succeeded in tricking it by making lego-shaped vegetables. The story was way funnier than anything I could have come up with on the spot.

Here’s an example of a story about my daughter and her 1-year old brother. The system prompt includes a few basic details about them, which it incorporated into the story. (I changed the names for privacy and regenerated the audio.)

0:00

-1:47

Audio playback is not supported on your browser. Please upgrade.

**Other use cases**

With [ChatGPT plugins](https://openai.com/blog/chatgpt-plugins) — I don’t have access yet — a ton of use cases become possible. Here are two that I’m thinking about.

With the [retrieval](https://github.com/openai/chatgpt-retrieval-plugin) plugin, ChatGPT has access to past conversations and personal documents (including photos — GPT-4 is multimodal). This makes it sort of like a diary or journal that you can talk to. (e.g. “How long ago did I go to the museum and which friends did I go with?”)

With a text-to-image generation plugin, it can generate storybooks on demand, on a topic of the user’s choosing. Here’s a simple example to show what’s possible (not cherrypicked; it’s the first output I got). It is far from perfect, but it’s good enough to be fun, and these tools are improving quickly. Many companies are working on text-to-video as well.

[](https://substackcdn.com/image/fetch/$s_!eYfX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4c96246-5046-4828-b03b-869c77a3845f_1434x1048.png)

[](https://substackcdn.com/image/fetch/$s_!1BC6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54f53288-600e-459a-aba5-9f9ced600f47_512x512.png)

_Image using the above prompt using Stable Diffusion_

**Risks**

The usual set of risks from children’s use of apps applies to chatbots. Let’s talk about the two main ones.

The one I’m most worried about is addiction. It’s not yet an issue for us, but once visual output is integrated into the app, I expect that it will be. I plan to be cautious about introducing AI-generated storybooks or videos. We regularly talk to our daughter about tech addition, and believe that the best approach is to help children learn how to resist. Banning tech is likely to backfire.

So far, the bot has not output any harmful content. There have been a couple of borderline cases. One of the stories involved a character dying of old age. Death is not an off-limits topic in our family, so this was not a problem for us. In any case, given how good it is at following instructions in the system prompt, I expect that specifying certain topics as off-limits topics will be quite effective.

In another instance, when asked for activity ideas, it suggested that the university campus is a good place for a solitary walk. This is the only case where it clearly failed to follow the age-appropriateness instruction in the system prompt. Of course, my daughter knows that she’s not supposed to be out on her own. Overall, safety hasn’t been a real concern so far, but this may change.

**The worst of both worlds?**

There’s an elephant in the room: it’s against OpenAI’s terms of service for children to use ChatGPT. I’m using the API, which doesn’t have that restriction, but sending the personal data of kids under 13 to OpenAI is prohibited. That means some of the most exciting applications, like diarying using the retrieval plugin, aren’t allowed. Even the system prompt customization to address the child by name might be prohibited. If there’s AI-specific child safety regulation, these policies might get further tightened.

We seem to be poised to repeat the mistakes of social media with chatbots. Most social media platforms decided to ban pre-teens rather than comply with child privacy laws. The only thing this accomplished was to force kids to [lie about their ages](https://zephoria.medium.com/protect-elders-ban-television-2b18ab49988b) and use social media _without_ protections that platforms could have designed. 

The way I see it, we have two choices when it comes to kids and chatbots. One is to pressure companies to allow kids to use them, but with appropriate protections. The other is to overreact to the risks, pass overzealous child-safety legislation, and attain a worst-of-both words outcome as kids ignore terms of service and chatbot makers pretend that kids aren’t using them.
