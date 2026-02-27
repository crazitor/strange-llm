---
title: "The LLaMA is out of the bag. Should we expect a tidal wave of disinformation?"
author: "Arvind Narayanan & Sayash Kapoor"
date: ""
source: "substack_aisnakeoil"
url: "https://www.normaltech.ai/p/the-llama-is-out-of-the-bag-should"
---

Ten days ago, Meta [announced](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/) a large language model called LLaMA. The company said the goal was to foster research. It didn’t release the model publicly but allowed researchers to request access through a form. But a week later, someone [leaked](https://analyticsindiamag.com/metas-llama-leaked-to-the-public-thanks-to-4chan/) the model. This is significant because it makes LLaMA the most capable LLM publicly available. It is reportedly [competitive](https://arxiv.org/pdf/2302.13971.pdf) with LaMDA, the model underlying Google’s Bard. Many experts worry that we are about to see an explosion of misuse, such as scams and disinformation.

But let’s back up. Models that are only slightly less capable have been available for years, such as [GPT-J](https://huggingface.co/EleutherAI/gpt-j-6B). And we’ve been told for a while now that a wave of malicious use is coming. Yet, there don’t seem to be any documented cases of such misuse. Not one, except for a [research study](https://techscience.org/a/2019121801/).

One possibility is that malicious use has been happening all along, but hasn’t been publicly reported. But that seems unlikely, because we know of numerous examples of _non-malicious_ misuses: students [cheating](https://aisnakeoil.substack.com/p/students-are-acing-their-homework) on homework, a [Q&A site](https://meta.stackoverflow.com/questions/421831/temporary-policy-chatgpt-is-banned) and a [sci-fi mag](https://www.npr.org/2023/02/24/1159286436/ai-chatbot-chatgpt-magazine-clarkesworld-artificial-intelligence) being overrun by bot-generated submissions, CNET publishing [error-filled investment advice](https://futurism.com/cnet-bankrate-restarts-ai-articles), a university offending staff and students by sending a [bot-generated condolence message](https://www.nationalreview.com/news/vanderbilt-college-dei-office-sends-michigan-shooting-condolence-message-drafted-by-ai-bot/) after a shooting, and, of course, [search engine spam](https://twitter.com/kavirkaycee/status/1599027845094744064).

Malicious use is intended to harm the recipient in some way, while non-malicious misuse is when someone is just trying to save time or make a buck. Sometimes the categorization may be unclear, but all the examples above seem obviously non-malicious. The difference is significant because non-malicious misuse does not rely on open-source models. OpenAI can (and does) try to train ChatGPT to refuse to generate misinformation, but can’t possibly prevent students from using the tool to generate essays.

Seth Lazar [suggests](https://write.as/sethlazar/genb) that the risk of LLM-based disinformation is overblown because the cost of producing lies is not the limiting factor in influence operations. We agree. Spam might be similar. The challenge for spammers is likely not the cost of generating spam emails, but locating the tiny fraction of people who will potentially fall for whatever the scam is. There’s a classic [paper](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/WhyFromNigeria.pdf) that argues that for precisely this reason, spammers go out of their way to make their messages _less_ persuasive. That way, receiving a response is a stronger signal of the recipient’s vulnerability. (**Update:** see below[1](https://www.normaltech.ai/p/the-llama-is-out-of-the-bag-should#footnote-1-106860489)).

We could be wrong about this. People like [Gary Marcus](https://garymarcus.substack.com/) who’ve thought carefully about the topic will no doubt have important counterarguments. But ultimately we should defer to the evidence. Now that LLaMA is out, if reports of malicious misuse continue to be conspicuously absent in the next few months, that should make us rethink the risk. Besides, attempting to control the supply of misinformation or spam seems like a brittle approach compared to giving people the knowhow and the technical [tools](https://www.npr.org/2022/10/28/1132021770/false-information-is-everywhere-pre-bunking-tries-to-head-it-off-early) to defend themselves.

If we are correct about the risk of malicious misuse being lower than widely assumed, that’s an argument in favor of open-sourcing LLMs. To be clear, we don’t have an opinion on whether they should be open-sourced; that question is too complex to tackle here. The risk of misuse is only one factor, albeit an important one. Our goal here is to steer the debate away from false premises. One should be especially cautious about arguments for keeping models proprietary based on evidence-free claims of misuse, considering that the powerful companies that build these models have an obvious vested interest in pushing this view.

Finally, we should demand that companies be much more transparent: those that host LLMs should release audits of how the tools have been used and abused. Social media platforms should [study](https://twitter.com/GaryMarcus/status/1594390688535568385?lang=en) and report the prevalence of LLM-generated misinformation.

**Further reading**

  * The paper [Generative Language Models and Automated Influence Operations: Emerging Threats and Potential Mitigations](https://arxiv.org/abs/2301.04246) has a good overview of hypothetical malicious uses of LLMs — emphasis on hypothetical. The authors are at OpenAI, Georgetown University, and Stanford University.

  * A [paper](https://medium.com/@danieldkang/attacking-chatgpt-with-standard-program-attacks-7eafdd5c409e) by Daniel Kang and others (U of Illinois, Stanford, Berkeley) shows how to bypass LLM content filters to generate misinformation, showing that even models that are behind an API aren’t obviously safe from malicious use. Both this paper and the previous one emphasize that a personalized conversation can be much more persuasive than a one-off, untargeted message. We think this ability — rather than lowering the cost of message generation — is probably the biggest threat from LLMs with respect to both disinformation and fraud.

  * A [report](https://documents.trendmicro.com/assets/white_papers/wp-fake-news-machine-how-propagandists-abuse-the-internet.pdf) from TrendLabs discusses the market for production and dissemination of disinformation.




_Cross-posted on the[Knight First Amendment Institute](https://knightcolumbia.org/) blog._

**Update**. Grady Booch on Twitter points to [examples](https://research.checkpoint.com/2023/opwnai-cybercriminals-starting-to-use-chatgpt/) of [cybercriminals](https://securitytoday.com/articles/2023/01/19/russian-hackers-attempting-to-use-chatgpt-for-malicious-use.aspx?m=1) experimenting with ChatGPT to help create malware. If LLM-enabled malware starts to get used in actual attacks, or if open-source models enable more of this kind of misuse than ChatGPT already does, that would be a point against open-sourcing. Still, note that the availability of technical expertise is not a bottleneck in cybercriminal activity.

[1](https://www.normaltech.ai/p/the-llama-is-out-of-the-bag-should#footnote-anchor-1-106860489)

In this paper, Cormac Herley claims that Nigerian scammers purposefully make their emails implausible to select only the most gullible recipients. Based on years of [on-the-ground research](https://mitpress.mit.edu/9780262017367/invisible-users/), [Jenna Burrell](https://datasociety.net/people/jenna-burrell/) points out that this paper relied on thought experiments that do not match how people use the internet in Nigeria. She raises two objections about the paper's assumptions:

  1. Herley assumes that mentioning Nigeria is not necessarily required for scammers since they can easily transfer money from another country. This is a false assumption since it is not easy for scammers to transfer money from abroad. 

  2. The stories written by scammers shifted to being more plausible over time. These stories should have become less plausible if Herley's assumptions were true.




She said, "the notion that Nigerian scam emails are purposefully implausible isn't really supported by any on-the-ground evidence." This is a compelling reason not to rely on Herley's arguments about scams originating in Nigeria. 
