---
title: "ChatGPT is a bullshit generator. But it can still be amazingly useful"
author: "Arvind Narayanan & Sayash Kapoor"
date: ""
source: "substack_aisnakeoil"
url: "https://www.normaltech.ai/p/chatgpt-is-a-bullshit-generator-but"
---

The philosopher Harry Frankfurt defined bullshit as speech that is [intended to persuade without regard for the truth](https://en.wikipedia.org/wiki/On_Bullshit). By this measure, OpenAI’s new chatbot ChatGPT is the greatest bullshitter ever. Large Language Models (LLMs) are trained to produce [plausible](https://fediscience.org/@ct_bergstrom/109465410043497711) text, not true statements. ChatGPT is shockingly good at sounding convincing on any conceivable topic. But OpenAI is [clear](https://openai.com/blog/chatgpt/) that there is no source of truth during training. That means that using ChatGPT in its current form would be a bad idea for applications like education or answering health questions. Even though the bot often gives excellent answers, sometimes it fails badly. And it’s always convincing, so it’s hard to tell the difference.

Yet, there are three kinds of tasks for which ChatGPT and other LLMs can be extremely useful, despite their inability to discern truth in general:

  1. Tasks where it’s easy for the user to check if the bot’s answer is correct, such as debugging help.

  2. Tasks where truth is irrelevant, such as writing fiction.

  3. Tasks for which there does in fact exist a subset of the training data that acts as a source of truth, such as language translation.




Let’s dive in. First the bad news, then the good.

### **Accuracy is critical in many applications**

ChatGPT is the best chatbot released so far. It has delighted users over the last week by generating fantastically weird text, such as an explanation of [how to remove a peanut butter sandwich from a VCR... in biblical verse](https://mobile.twitter.com/tqbf/status/1598513757805858820).

But people are also excited about more serious applications, such as using it as a learning tool. Some are even [predicting](https://twitter.com/jdjkelly/status/1598021488795586561) that it will make Google redundant. Yes, ChatGPT is often extremely good at answering questions. But the danger is that you can't tell when it's wrong unless you already know the answer. We tried some basic information security questions. In most cases, the answers [sounded plausible but were, in fact, bullshit](https://twitter.com/random_walker/status/1598383507214020608). And here’s what happened with more complex questions:

[Arvind Narayanan @randomwalker@mastodon.social@random_walkerI gave it q's from my infosec final exam at Princeton that require critical thinking. I had to read some of the answers three times before feeling confident I was reading nonsense. It was so unsettling I had to look at my reference solutions to make sure I wasn't losing my mind.6:37 PM · Dec 1, 2022

* * *

24 Reposts · 253 Likes](https://twitter.com/random_walker/status/1598385725363261441)

Another trope about ChatGPT and education: universities are doomed because ChatGPT can write essays. That's silly. Yes, LLMs can write plausible essays. But the death of homework essays is a good thing for learning! We wrote about this [a month ago](https://aisnakeoil.substack.com/p/students-are-acing-their-homework), and nothing has really changed. 

What about search? Google's knowledge panels are already notorious for presenting misinformation authoritatively. Replacing them with an LLM could make things much worse. A [paper](https://dl.acm.org/doi/pdf/10.1145/3498366.3505816) by Chirag Shah and Emily Bender explores how things could go wrong if we replace search engines with LLMs.

The fact that these models can’t discern the truth is why Meta’s [Galactica](https://www.technologyreview.com/2022/11/18/1063487/meta-large-language-model-ai-only-survived-three-days-gpt-3-science/), an LLM for science, was an ill-conceived idea. In science, accuracy is the whole point. The backlash was swift, and the public demo was pulled down after three days. Similarly, [correctness and reliability](https://www.jmir.org/2018/9/e11510/) are everything if you want to use an LLM for answering health-related queries.

### **But aren’t these models improving quickly?**

Of course. But their ability to sound convincing is getting better just as [quickly](https://garymarcus.substack.com/p/how-come-gpt-can-seem-so-brilliant)! So we suspect it's getting harder for even experts to spot mistakes. 

In fact, models such as Galactica and ChatGPT are great at generating authoritative-sounding text in any requested style: legalese, bureaucratese, wiki pages, academic papers, lecture notes, and even answers for Q&A forums. One side effect is that we can no longer rely on the _form_ of a text to gauge trustworthiness and legitimacy. 

[StackOverflow found out the hard way](https://meta.stackoverflow.com/questions/421831/temporary-policy-chatgpt-is-banned). On the website, users answer programming questions to earn points, and points bring privileges like fewer ads and access to moderator tools. After ChatGPT was released openly to the public, the Q&A forum got thousands of incorrect answers generated using the LLM. But because the answers were written in the right style, they had to be vetted by experts before they could be removed. Within a week, the company had to ban answers generated using ChatGPT to reduce the number of plausible-sounding incorrect answers.

Unless the accuracy of LLM responses can be improved, we suspect that the set of legitimate applications will remain relatively circumscribed. Note that GPT-3 is 2.5 years old. We're told the field is progressing every week, so that's like centuries. When it was released, people confidently predicted that there would be a “Cambrian explosion” of applications. But so far, there have been zero mainstream applications — except GitHub Copilot, if you count programming as mainstream. 

The accuracy issue is not necessarily hopeless. Intriguingly, LLMs seem to acquire some capacity to discern truth as a byproduct of learning to sound convincing. When researchers [asked](https://arxiv.org/pdf/2207.05221.pdf) an LLM to evaluate its own proposed answers for accuracy, it did far better than random chance! Work is underway to integrate this ability into the default behavior of chatbots, so that accurate answers are more likely to be produced.

Meanwhile, here are three kinds of tasks for which LLMs are already useful.

### **Coding: the user can access ground truth**

Debugging code is an application where programmers, especially novices, could benefit from LLMs. Note that once a bug is pointed out, it is generally easy to verify, so the fact that the bot’s answers might sometimes be wrong isn’t as much of a concern.

[Amjad Masad ⠕@amasadChatGPT could be a good debugging companion; it not only explains the bug but fixes it and explain the fix 🤯 7:53 PM · Nov 30, 2022

* * *

905 Reposts · 6.1K Likes](https://twitter.com/amasad/status/1598042665375105024)

 _Generating_ code is a tricker story. In theory, the user can verify that automatically generated code is free of bugs (perhaps with the help of LLMs). But it is unclear whether this would be faster than manually writing the code. Security bugs are a particularly serious concern. A [study](https://arxiv.org/abs/2108.09293) last year found that Copilot generated insecure code 40% of the time. They don’t compare this figure to human programmers or offer an opinion on whether and when Copilot use is appropriate, but it is clear from the result that caution is warranted.

Copilot is intended to increase the productivity of experts. What about users who can’t code — can they use AI tools to generate simple scripts? There’s a lot of promise here, too. Here’s one small experiment:

[Arvind Narayanan @randomwalker@mastodon.social@random_walkerThe most valuable generative AI use cases are those where its abilities are complementary to humans. Here ChatGPT struggles to write a Python program that correctly reverses each string in a list, but even a user who can't code can guide it by reporting what went wrong each time. 3:48 PM · Dec 4, 2022

* * *

15 Reposts · 121 Likes](https://twitter.com/random_walker/status/1599430575102001153)

The use of LLMs for code generation is an [active area](https://www.deepmind.com/blog/competitive-programming-with-alphacode) of [research](https://arxiv.org/pdf/2207.01780.pdf). There’s a lot of room for improvement in terms of increasing the correctness of the generated code and decreasing the frequency of bugs. This is an exciting area to watch.

### **Entertainment: truth is irrelevant**

ChatGPT has been a source of entertainment over the last week. From [writing jokes on specific personalities](https://twitter.com/gfodor/status/1598916489993940993) to explaining algorithms in the [style of fast-talking wise guys](https://twitter.com/goodside/status/1598077257498923010), people have found many creative uses for the tool. But could we use ChatGPT for more ambitious projects, such as writing fiction?

LLMs are quite far from being able to produce long pieces of text, such as entire novels, because they can only store a [small number of tokens at a time](https://twitter.com/goodside/status/1598882343586238464?s=20&t=9aOBVGU1F7x9k4S14HxwJg). Still, authors and researchers are experimenting with them to generate ideas, [expand](https://www.wired.com/story/k-allado-mcdowell-gpt-3-amor-cringe/) on their prompts, and change the style of a text (e.g., "[rewrite this text to be more Dickensian](https://dl.acm.org/doi/fullHtml/10.1145/3490099.3511105)"). Interactive fiction games like [AI Dungeon](https://play.aidungeon.io/main/home) use LLMs to flesh out storylines using user inputs. We believe there is no fundamental barrier to continuing improvements in this area.

Similarly, text-to-image and image-to-image tools are useful for entertainment because creators can tune the prompt till they find an image they like. The latest app to make waves is [Lensa](https://prisma-ai.com/lensa), which creates portraits in various styles once the user uploads a few selfies. Its backend uses Stable Diffusion, an open-source image generation model from Stability AI.

Before we get carried away by this potential: racist, sexist, and biased outputs are still a problem for all generative models, [including ChatGPT](https://twitter.com/spiantado/status/1599462375887114240?s=20&t=vV-g_kUAg3L2era1c5G_aw). The model includes a [content filter](https://openai.com/blog/chatgpt/) that declines inappropriate requests, which works well enough to feel like a big improvement over previous tools, but there is still a long way to go.

### **Translation: exploiting a lurking source of truth**

Remarkably, GPT-3 [performs](https://arxiv.org/abs/2005.14165) roughly on par with special-purpose language translation models, and ChatGPT likely does as well. The likely reason is that it can exploit ground truth in the corpus (which consists, to a first approximation, of all text on the web). For example, there are web pages that are translated into multiple languages. Of course, during training, no explicit labels are provided to tell the model which texts correspond to each other, but presumably, the model can figure this out automatically[1](https://www.normaltech.ai/p/chatgpt-is-a-bullshit-generator-but#footnote-1-88973379).

It’s not obvious why a chatbot would be a better tool for translation than existing tools like Google translate if their performance is equivalent. One possibility is that in a conversation between two speakers of different languages, a tool like ChatGPT could play the role of an interpreter, the advantage being that a tool used within a conversation can keep track of the dialog. This would allow it to rely on context and perform much more effectively and with far less awkwardness for the users.

### **Conclusion: too early to tell if it will be transformative**

Generative AI releases tend to look impressive based on cherry-picked examples that go viral. But that's [not the full picture](https://twitter.com/fchollet/status/1598147044744777729). For many applications, even a 10% failure rate is too high. There seem to be a fairly limited set of use cases where the lack of a source of truth isn’t a deal breaker. While these uses are still tremendously exciting, it’s far from obvious that people will soon be using chatbots in their everyday lives — for learning, or as a search replacement, or as a conversation partner.

Meanwhile, we’ve seen the first prominent use of LLMs for misinformation (on Stack Overflow). Of course, spammers were already using GPT-3 for search engine marketing and are [delighted](https://twitter.com/kavirkaycee/status/1599027845094744064) to get their hands on ChatGPT. But just as the predictions of transformation are overblown, we don’t agree with claims that the web will soon drown in an ocean of misinformation.

We look forward to how people will use LLMs creatively as much as we cringe at the hype and the usual [self-serving AGI talk](https://twitter.com/elonmusk/status/1599128577068650498?s=20&t=-51HkNswEoX8uyGOw5_xPg). 

[1](https://www.normaltech.ai/p/chatgpt-is-a-bullshit-generator-but#footnote-anchor-1-88973379)

Suppose we have two separate datasets of texts in different languages. We don’t even require that documents in one be translations of documents in the other. If we build separate word embeddings of those two languages, those embeddings will approximately be [linear transformations](https://arxiv.org/pdf/1710.04087.pdf) of each other! And it is possible to learn this mapping in an unsupervised way. The details of what’s happening in LLMs are quite different, but this shows that, in principle, an explicitly labeled parallel corpus isn’t required for translation.
