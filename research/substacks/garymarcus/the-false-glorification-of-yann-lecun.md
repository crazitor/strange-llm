---
title: "The False Glorification of Yann LeCun"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/the-false-glorification-of-yann-lecun"
---

With the support of Meta, and the unwitting assistance of the press, Yann LeCun has for the last decade run one of the more successful PR campaigns in recent scientific history, persistently allowing himself to be painted as the inventor of ideas, techniques, and arguments to which he is not the inventor of. The culmination of that PR campaign came Friday, with [a puff piece in ](https://www.wsj.com/tech/ai/yann-lecun-ai-meta-0058b13c)_[The Wall Street Journal](https://www.wsj.com/tech/ai/yann-lecun-ai-meta-0058b13c)_ , tied to a new startup LeCun is apparently launching, with a grossly misleading headline that styled LeCun as a lone genius. 

[](https://substackcdn.com/image/fetch/$s_!Fbie!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f23da67-0ee2-4b5e-8932-ce527f014070_1237x1604.png)

The headline is wrong in almost every way possible: LeCun has not been right about everything, or even consistent in his own views over time, particularly with respect to LLMs (see below). In many of the things that he is now challenging, he is far from alone, though the headlines sometimes paint him like that, and far from being the first in raising the challenges that he has raised. 

In fact, most of what LeCun says has a long history that precedes him. And in every way possible he conveniently ignores that history, in order to exaggerate the originality of his ideas. By and large he has been effective at this. The myth of him as lone genius has worked for him, at least in the popular imagination. 

But it is not true — or even remotely so. 

For the most part, LeCun is nowadays known in the general public for five ideas: convolutional neural networks, his critique of large language models, his critique of the scaling hypothesis, his advocacy of commonsense and physical reasoning, and his advocacy of world models. The thing is, (a) he originated exactly none of these ideas, and (b) he rarely if ever credits any of the people who actually did. This reflects a consistent pattern known as the [plagiarism of ideas](https://ori.hhs.gov/plagiarism-ideas).

Per the US Office of Research Integrity, the _plagiarism of ideas_ is defined as “Appropriating someone else’s idea (e.g., an explanation, a theory, a conclusion, a hypothesis, a metaphor) in whole or in part, or with superficial modifications without giving credit to its originator”. He has done this over and over and over.

## 1\. Convolutional neural networks 

[Convolutional neural networks](https://en.wikipedia.org/wiki/Convolutional_neural_network) (CNNS) are, without a doubt, a foundational contribution to AI; they found applications in image recognition, speech recognition, natural language processing, recommendation systems, and many other areas. Until large language models became dominant, they were one of the leading techniques used in machine learning. (The LSTM, published by [Hochreiter and Schmidhuber, 1997](https://www.semanticscholar.org/paper/Long-Short-Term-Memory-Hochreiter-Schmidhuber/2e9d221c206e9503ceb452302d68d10e293f2a10), was also in very widespread use, [exceeding CNNs in commercial use according to one study](https://arxiv.org/pdf/1704.04760).) And there is no doubt that LeCun played a role in developing convolutional neural networks. But he neither invented them nor was he the first to apply the back-propagation algorithm to learning their weights (though many people mistakenly believe this).

The foundational work was done by Kunihiko Fukushima in 1979-1980; Wei Zhang et al (1988) beat LeCun to adding the back-propagation to convolutional neural networks in little-known work in [1988](https://people.idsia.ch/~juergen/Zhang-1988-shift-invariant-NN-JSAP-WithEnglishTranslation.pdf) that was published in Japanese (with an English abstract). LeCun had the good fortune of publishing in more prominent places the next year in English, and he has devised important tricks for improving their performance, but his work wasn’t first. LeCun rarely mentions his predecessors.

Schmidhuber has documented this ongoing pattern numerous times, presenting receipts [in a short history of convolution neural networks](https://x.com/SchmidhuberAI/status/1952007922721919219?s=20), in documentation [of how a key paper by LeCun neglects critical past work](https://x.com/SchmidhuberAI/status/1544939700099710976?s=20), in explication of [how a list by LeCun of key recent inventions again neglected critical past work](https://x.com/SchmidhuberAI/status/1594964463727570945?s=20), and [in a detailed discussion of LeCun and his collaborators’s consistent omissions of previous work](https://x.com/SchmidhuberAI/status/1735313711240253567?s=20).

Yet LeCun often slights Zhang’s pioneering work; strikingly, [no mention of it was made at all in LeCun’s most cited survey](https://github.com/CodeRayZhang/Deep-Learning-Papers-Reading-Roadmap/blob/master/1.1-Survey/LeCun%2C%20Yann%2C%20Yoshua%20Bengio%2C%20and%20Geoffrey%20Hinton.%20Deep%20learning.%20Nature%20521.7553%20\(2015\).pdf). He also has given short shrift to Alexander Waibel whose TDNN ([time-delay neural network](https://isl.iar.kit.edu/downloads/phoneme-recognition-using-TDNN-1987.pdf)) in many ways presaged convolutional neural networks, using essentially the same math but for speech rather than vision, and to Les Atlas [for bringing the term convolutional into discussions of neural networks](https://proceedings.neurips.cc/paper_files/paper/1987/file/853f7b3615411c82a2ae439ab8c4c96e-Paper.pdf). 

## 2\. The idea that Large Language Models would not get us to AGI

The Wall Street Journal article is in part about LeCun’s critique of LLMs, and his critique has been noted in the press numerous times. In no way was LeCun there first, either. 

I was likely the first, with a series of challenges to GPT-2 and GPT-3 on Twitter in the fall of [2019](https://x.com/garymarcus/status/1188803198980521986?s=61) and in a series of articles in [2019](https://thegradient.pub/gpt2-and-the-nature-of-intelligence/) and [2020](https://www.technologyreview.com/2020/08/22/1007539/gpt3-openai-language-generator-artificial-intelligence-ai-opinion/).

What is striking is that LeCun was, at the time, publicly hostile to those critiques, accusing me of a “[rearguard action](https://twitter.com/ylecun/status/1188902027495006208?s=20&t=rZorYMVHU32iCXJmFfICOQ).” I spent much of the next several years arguing against LLMs; LeCun frequently tussled with me, and never once publicly supported my critique. (It’s only when ChatGPT eclipsed Meta that LeCun began to be sharply, publicly critical of LLMs) LeCun has in fact probably _never_ cited my own critiques, and always presented his own critiques as if they were his own original ideas.

Likewise, LeCun rarely if ever cites Emily Bender et al’s 2021 prominent [stochastic parrots](https://dl.acm.org/doi/10.1145/3442188.3445922) paper, an influential and important critique of LLMs that also preceded the era in which LeCun began to loudly critique LLMs. 

Over a year later, November 2022, LeCun was still loudly promoting (his company’s) LLMs as “amazing work”:

[](https://substackcdn.com/image/fetch/$s_!L99K!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fad8adc8d-63de-4532-80f0-302945344bf4_1027x686.png)

He only fully changed his mind a few weeks later, after Galactica tanked and ChatGPT ate his lunch. Consistent “for 40 years” he has not been.

Most ludicrous of all is the WSJ portrayal of LeCun as somehow isolated __ in doubting that LLMs can reach AGI. A recent AAAI survey showed that this is in fact [the majority opinion among a broad sampling of researchers and academic scientists, by a wide margin](https://aaai.org/about-aaai/presidential-panel-on-the-future-of-ai-research/)**.**

## 3\. Critique of pure scaling

LeCun is also making waves for his criticism of scaling. The Wall St. Journal reports:

> We are not going to get to human-level AI just by scaling LLMs,” [LeCun] said on Alex Kantrowitz’s [Big Technology podcast](https://www.youtube.com/watch?v=4__gg83s_Do&mod=ANLink) this spring. “There’s no way, absolutely no way, and whatever you can hear from some of my more adventurous colleagues, it’s not going to happen within the next two years. There’s absolutely no way in hell to–pardon my French.”

But, again, LeCun wasn’t here first. Instead, I was probably the first person to doubt this publicly, back in [2022](https://nautil.us/deep-learning-is-hitting-a-wall-238440/):

> There are serious holes in the scaling argument. To begin with, the measures that have scaled have not captured what we desperately need to improve: genuine comprehension… 
> 
> What’s more, the so-called scaling laws aren’t universal _laws_ like gravity but rather mere observations that might not hold forever, much like Moore’s law, a trend in computer chip production that held for decades but arguably [began to slow](https://www.nytimes.com/2015/09/27/technology/smaller-faster-cheaper-over-the-future-of-computer-chips.html) a decade ago.11

At the time LeCun was hardly supportive; instead he trolled my critique on Facebook. In no way has LeCun _ever_ publicly acknowledged that I was on target with my conjecture that scaling LLMs would not lead to AGI. To the contrary, LeCun has repeatedly pretended that the anti-scaling idea originated with him, and he continues to falsely paint himself as the first and lone person to see this. 

## 4\. Common Sense and Physical Reasoning

Another common argument of LeCun in recent years is to say that LLMs lack common sense and are poor at physical reasoning. For years, though, he hardly seemed to emphasize the problem at all; [in LeCun’s famous 2015 Nature paper on deep learning, common sense is only mentioned once, in passing, with zero citations](https://hal.science/hal-04206682/file/Lecun2015.pdf). 

In reality, others that he rarely or never cites had been concerned about the problem for years, going back to John McCarthy (one of AI’s actual godfathers) in the late 1950’s, Pat Hayes in the 1970s and [1980s](https://www.cs.unibo.it/~nuzzoles/courses/intelligenza-artificiale/exam/3-second-naive-physics-manifesto.pdf) and in this last two decades by my long-term collaborator Ernest Davis, literally in the same department as LeCun at NYU for the last quarter century, yet Davis’ work on commonsense reasoning is mentioned by LeCun scandalously rarely. He doesn’t give much notice to Judea Pearl’s pioneering work [causality](https://en.wikipedia.org/wiki/Causality_\(book\)), either.

## 5\. World Models

Also mentioned in the WSJ article is that LeCun is excited about [world models](https://garymarcus.substack.com/publish/post/164369506), “a technology that LeCun thinks is more likely to advance the state of AI than Meta’s current language models”. 

As it happens, the idea of world models is not new. [As noted here a few months ago](https://open.substack.com/pub/garymarcus/p/generative-ais-crippling-and-widespread?r=8tdk6&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false), it goes back to the 1950s, and Herb Simon’s [General Problem Solver](https://en.wikipedia.org/wiki/General_Problem_Solver). Schmidhuber has been advocating adding world models to neural networks, as far back as [1990](https://people.idsia.ch/~juergen/world-models-planning-curiosity-fki-1990.html), and in important technical work [in 2015](https://arxiv.org/abs/1511.09249), as well as [in a more recent article with David Ha](https://arxiv.org/abs/1803.10122), now CEO of the very well-funded Sakana Labs. True to form, LeCun rarely refers to this work in his public presentations. 

Likewise, Ernest Davis and I argued strenuously that the field should pay more attention to world (cognitive) models in our 2019 book _Rebooting AI_ , which LeCun was dismissive of. Challenge with LLMs representing world models have been central to my own critiques of LLMs since the fall of 2019, and were one of four key foci in my 2020 article [The Next Decade in AI](https://arxiv.org/abs/2002.06177), perhaps the first lengthy discussion of the need for integrating world (cognitive) models specifically with LLMs. I don’t believe LeCun has ever acknowledged any of this, except in 2019 [when he originally dismissed my claims](https://twitter.com/ylecun/status/1188902027495006208?s=20&t=rZorYMVHU32iCXJmFfICOQ). 

Similarly, Fei-Fei Li is building a world-model focused AI startup, [World Labs](https://www.worldlabs.ai/); based on past experience, I will be surprised if LeCun ever gives her endeavors much mention.

# Summary

Someone on X summed it up well Saturday:

[](https://substackcdn.com/image/fetch/$s_!QFV_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8e819c3e-b08c-4257-b8d9-5493e54ffb7f_1206x1276.jpeg)

The eminent AI researcher Hector Zenil made similar points on LinkedIn on Sunday morning:

[](https://substackcdn.com/image/fetch/$s_!W6Jp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe37e5392-3931-4042-aa2d-9991544fe980_1135x214.png)

Yann LeCun has, without a doubt made genuine contributions to AI, and I am pleased to see him speak out again the limits on LLMs. But he has also systematically dismissed and ignored the work of others for years, including Schmidhuber, Fukushima, Zhang, Bender, Li and myself, in order to exaggerate his own contributions.[1](https://garymarcus.substack.com/p/the-false-glorification-of-yann-lecun#footnote-1-179057564) With the help of Meta’s media lobby he has succeeded in fooling most of the press and some fraction of the public. LeCun has lapped it up, and done absolutely nothing to set the record straight. 

But the myths about the originality of his thought simply aren’t true. 

Whether he can produce genuinely original ideas in his new startup remains to be seen.

_**Gary Marcus** began critiquing traditional neural networks and calling for hybrid neurosymbolic architectures in his first publication in 1992, advocated vociferously for neurosymbolic cognitive models in his 2001 book The Algebraic Mind, in which he anticipated current troubles with hallucinations and unreliable reasoning. He first warned how these limits would apply to LLMs in 2019, emphasizing their lack of stable world models._

[1](https://garymarcus.substack.com/p/the-false-glorification-of-yann-lecun#footnote-anchor-1-179057564)

Perhaps out of a similar impulse, LeCun has consistently minimized the _negative_ impacts of his work, as the Lovelace Medalist Grady Booch noted to me this morning in a text message. Commenting on a draft of this essay Booch wrote, “ _you may be surprised to know that I don’t think you went far enough in your criticism of LeCun. It’s not just his shallow shiny public person that is the problem but rather a) his work at the center of Meta’s early efforts in AI has contributed greatly to that company’s evil by facilitating the monetization of outrage and b) he has consistently been tone deaf to the implications of his work._ ” 
