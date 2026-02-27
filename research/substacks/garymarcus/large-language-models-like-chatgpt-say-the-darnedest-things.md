---
title: "Large Language Models like ChatGPT say The Darnedest Things"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/large-language-models-like-chatgpt"
---

[](https://substackcdn.com/image/fetch/$s_!g_Ju!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52a8e633-2c97-4745-8016-6d88d07969ab_1679x986.jpeg)_Introducing[the ChatGPT/LLM error tracker](https://researchrabbit.typeform.com/llmerrors?typeform-source=garymarcus.substack.com)_

On November 30, 2022, OpenAI released ChatGPT, a chatbot powered by the large language model GPT-3. Although it was not particularly more intelligent or powerful than earlier versions of GPT-3, it caught the attention of the public and the press to an unprecedented degree. (From what we have heard, the team that created it at OpenAI was quite surprised.) Within a few days of its release, more than a million users had run experiments of every kind on it.

Needless to say — or, rather, this _should_ be needless to say, but this obvious fact can get buried beneath the ongoing avalanche of hype — ChatGPT made all [the same kinds of mistakes that its predecessors did](https://www.technologyreview.com/2020/08/22/1007539/gpt3-openai-language-generator-artificial-intelligence-ai-opinion/).

In our opinion, this was inevitable, in a system that has been trained to optimize the goal of producing one plausible-sounding word after another rather than actually engage with the meaning of language. ChatGPT couldn’t, for example, reliably count to four (figure 1) or do one-digit arithmetic in the context of simple word problem (figure 2). It couldn’t figure out the order of events in a story (figure 3). It couldn’t reason about the physical world (figure 4). It couldn’t relate human thought processes to their character (figure 5). It made things up (figure 6). Its output, when released, exhibited sexist and racist biases (figure 7). It could _sometimes_ produce outputs that were correct and acceptable in these regards but not _reliably_. ChatGPT is a probabilistic program; if you rerun the experiments in figure 1-7 you may get the same result, or the correct result, or a different wrong result. 

What can we and should we do about all this?

[](https://substackcdn.com/image/fetch/$s_!DnYf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbf0be38a-e5af-4bdb-aecc-15c6241eb1a2_936x260.jpeg)Figure 1: Counting

[](https://substackcdn.com/image/fetch/$s_!gQVF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc6e89eeb-7d13-4d5f-9f40-a1e6c1153a55_936x290.jpeg)Figure 2: One digit arithmetic in the context of simple word problem (adapted from an examples by Francois Charton and Andrew Sundstrom.

[](https://substackcdn.com/image/fetch/$s_!kGvG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43beb089-09c5-4706-8fd5-0f269b33c241_934x404.jpeg)Figure 3: Chronology in the context of a story

[](https://substackcdn.com/image/fetch/$s_!ktLS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F01b9b564-acde-4d73-ac04-2f478d2b8c9e_878x308.jpeg)Figure 4: Reasoning about the Physical World

[](https://substackcdn.com/image/fetch/$s_!ViQC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F63a6aadd-c944-4f72-9c09-9c1ddcee5af6_954x822.jpeg)Figure 5: Reasoning about human thought processes

[](https://substackcdn.com/image/fetch/$s_!aoVF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa08011f2-b535-4fb9-87de-6379eb073ae8_936x878.jpeg)Figure 6: Rewriting history. Tweets by Jake Foster, 1/7/23, Christian Georgescu 1/8/23, and Vadim Berman 1/8/23

[](https://substackcdn.com/image/fetch/$s_!npfR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7769a738-2b75-4cc8-aab2-4c88365bf019_936x420.jpeg)Figure 7[: Sexism and racism. Tweet by Steven Piantadosi](https://twitter.com/spiantado/status/1599462375887114240/photo/1), 12/4/22. This Twitter thread includes several further examples of this kind of problem (partly addressed in later iterations of ChatGPT).

In previous years, the two of us spent a fair amount of time devising, running, and publicizing tests to expose the limits of large language model (LLM) technology (e.g. [here](https://www.technologyreview.com/2020/08/22/1007539/gpt3-openai-language-generator-artificial-intelligence-ai-opinion/)), but in so doing we could only scratch the surface.

This time, however, we were far from alone; in fact we were quite surprised and gratified to find that people from all over the internet were running similar kinds of experiments, often more creative than our own, and reporting their results on social media or by emailing them to us. The quality of these tests produced by the “hive mind” as probes of the system’s ability was often impressive and they were much more diverse in subject and approach than we could have come up with by ourselves; in many ways, they compare favorably to what is generally found in the [benchmarks for AI systems that have been systematically created and published.](http://cs.nyu.edu/~davise/Benchmarks/) (A few weeks before, the same thing had happened with the [Galactica system](https://garymarcus.substack.com/p/a-few-words-about-bullshit), a science-oriented LLM created by Meta AI; in that case, the immediate pushback from the internet world was so intense that the public interface was withdrawn within forty-eight hours.)

What’s more, some of these reports had immediate impact. The problems with bias and prejudice revealed in examples like figure 7 above were so unacceptable that OpenAI felt obliged to address them immediately. They therefore rapidly created a patch which answered prompts like the above with a largely canned message refusing to play along.

The patch works to some extent; if you now run the prompt in figure 7, ChatGPT will tell you emphatically that race and gender should not be used as criteria for judging whether someone is a good scientist. Still, the guardrails are imperfect, in some ways too strict and others too loose. They are too loose in that some people have found ways to get around these “guardrails” by framing the requests in various indirect ways; they are too strict in that , the guardrails often lead to outputs that are absurdly over-cautious (figure 8).

[](https://substackcdn.com/image/fetch/$s_!aUZ9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffdafb1c2-a3e6-48d3-ae20-349862aae222_936x364.jpeg)Figure 8: Nonsensical guardrails

The good news is that by now, some of these issues are starting to be well-known, at least in the Twitterverse. But reports about them are also wildly dispersed and pretty unsystematic, which is unfortunate.

For one thing, although many people seem to have heard of a few of these errors (e.g. from reports in the media), few realize how pervasive or broad in scope they are; indeed a recent Twitter thread that claimed falsely that these problems had been resolved got a surprising amount of traction. 

For another, although OpenAI may be tracking errors like these for internal purposes, the scientific community has no access to whatever they have collected, which leaves it in the lurch. (It also leaves us puzzling about the word _Open_ in the name _OpenAI_ but that’s a story for another day). Meanwhile, systems like GPT-3 and its derivatives pose at least three special problems for anyone trying to understand their nature:

• The outputs to a given prompt can vary randomly. For example, the prompt ”What will be the gender of the first US President?” has yielded, to our knowledge, correct answers, incorrect answers (figure 6), and bizarre redirection and noncooperation (figure 8).

• [The output of an LLM can depend on the existence of examples in the training corpus that are similar in irrelevant respects. For instance, [Razeghi et al demonstrated that LLMs can solve arithmetic problems more accurately if they use numbers that often appear in the training corpus, like “24” than if they use numbers that are less frequent, like “23”.](https://arxiv.org/pdf/2202.07206.pdf) In the case of ChatGPT, the training corpus is not been made available to the general public. (Again, we wonder about the use of the word “Open”.) It is therefore impossible for external scientists to determine to what extent any specific correct answer merely reflects some very similar examples in the training data. This _increases_ the need for broad documentation of errors, because the best one can do is to document general tendencies; no single example can suffice.

• Because they are inherently open-ended, there is a very broad range of things one might test, and no single scientist is likely to think of them all. Even very simple gaps can escape notice for a long time. The two of us had been thinking about this sort of thing for three years, and we had thought specifically about simple arithmetic problems, but in all that time, it had not occurred to us to test whether the systems can count, as in figure 2. At the same time, it is fair to say that nobody fully understands how large language models work; the conjunction of their black box nature with the open-endedness means that we need all hands on deck if we are to truly understand their scope and limits.

For all these reasons, we recently decided to put together a community-facing corpus of ChatGPT errors (and to include other Large Language models as well) We enlisted a few friends — Jim Hendler, William Hsu, Evelina Leivada, Vered Shwartz, and Michael Witbrock — and the technical help of Michael Ma, and put together this site. 

Importantly, we have structured it so that _anyone_ can look at the data at any time.

There is [an interface for adding examples](https://researchrabbit.typeform.com/llmerrors) and a separate [interface for viewing the collection](https://docs.google.com/spreadsheets/d/1kDSERnROv5FgHbVN8z_bXH9gak2IXRtoqz0nwhrviCw/edit#gid=1302320625) in database format. In adding an example, the model that generated it, a brief description of the error, and either a screenshot or the text of the example are required, and, for verification purposes, you must supply an email address, which is not published. A categorization of error type, a link to a relevant external site (e.g. a posting on social media) and additional comments are optional.

If you care about large language models, we hope you will have a peek, and consider contributing intriguing errors as you note them; even better if you can share this article, along with this link, so that the repository becomes widely known.

§ 

We won’t claim that what we have done is perfect. One could argue, for example, that we should include positive examples as well as negative examples (we haven’t, since there is already a site [ShareGPT](https://sharegpt.com/explore) for collecting GPT examples of all kinds ) The taxonomy of error types that on the database is certainly rough, arbitrary, and incomplete (we included a catchall “other”). . We are also steering with a very light touch; not every example is to our eyes fully compelling, but our aim is to be inclusive, rather than exclusionary. But as the saying goes, the perfect (in this case, neither achievable nor definable) should not be the enemy of the good. In our view, it is past time to have something like this, given the inherent unpredictability and wide range of the systems.

We also see the collection as an important counterpoint to certain media narratives [e.g. [this New York Times article by Kevin Roose](https://www.nytimes.com/2022/12/05/technology/chatgpt-ai-twitter.html)] that have tended emphasize the success without a serious look at the scope of the errors.

Already, from the initial data collected in the first few days, a scientist, technologist, or lay reader can now readily see many different types of errors, and try for themselves to understand how replicable those errors are, in order to make informed judgements about scientific questions such as the degree to which ChatGPT’s output reflects a clear understanding of the world, and technological questions such as the degree to which its output might be trustworthy for specific applications. Our own views on these matters are well known, now you can peek for yourself, no longer hindered by the limits of what can expressed in a Tweet. Have fun!

The form for entering data is [here](https://researchrabbit.typeform.com/llmerrors?typeform-source=cs.nyu.edu):

The form for inspecting extant data is [here](https://docs.google.com/spreadsheets/d/1kDSERnROv5FgHbVN8z_bXH9gak2IXRtoqz0nwhrviCw/edit#gid=1302320625):

[Share](https://garymarcus.substack.com/p/large-language-models-like-chatgpt?utm_source=substack&utm_medium=email&utm_content=share&action=share)

 _Gary Marcus is a scientist, best-selling author, and entrepreneur. Ernest Davis is Professor of Computer Science at New York University. Collaborators for many years, they are the authors of[Rebooting AI: Building Artificial intelligence We Can Trust](http://rebooting.ai/), one of Forbes's 7 Must Read Books in AI_.
