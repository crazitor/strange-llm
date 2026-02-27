---
title: "Breaking: Marcus weighs in (mostly) for LeCun"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/breaking-marcus-weighs-in-mostly"
---

[](https://substackcdn.com/image/fetch/$s_!H8FJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F22a30759-9e6c-4e75-9fd6-046b1b898026_1206x863.jpeg)Screengrab from [Yann LeCun’s recent interview at the FT](https://www.ft.com/content/e3c4c2f6-4ea7-4adf-b945-e58495f836c2)

Yann LeCun [is not a savory character](https://open.substack.com/pub/garymarcus/p/the-false-glorification-of-yann-lecun?utm_campaign=post-expanded-share&utm_medium=web); but he is certainly a character. For the last few days the tech world has been gossiping about the saga of his departure from Meta, in which every aspect of his character, negative and positive, from his arrogance and certitude to his commitment to science, has been on full display. You can get a glimpse of this in the excerpt [from his interview with the FT](https://www.ft.com/content/e3c4c2f6-4ea7-4adf-b945-e58495f836c2), above.

A [long tweet](https://x.com/nadzi_mouad/status/2008078841734942973?s=46) below sums up some of the back story, mostly taking LeCun’s side. The funny thing is that – with a huge technical asterisk discussed below — I, a longstanding critic of LeCun, am basically on LeCun’s side in the fracas. 

[](https://substackcdn.com/image/fetch/$s_!oaj8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a09f1df-a5a5-458e-8183-b87bfe654669_1163x1400.jpeg)

[](https://substackcdn.com/image/fetch/$s_!MXs-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72b5e460-2b72-49ba-b475-f4b1a0c93324_1093x2065.jpeg)

More power to LeCun for standing his ground. Zuckerberg doesn’t know more about AI than LeCun does, and Wang doesn’t either. Furthermore, what LeCun does best is research. He [may not be as original as he pretends to be](https://open.substack.com/pub/garymarcus/p/the-false-glorification-of-yann-lecun?utm_campaign=post-expanded-share&utm_medium=web), but he (mostly) has good intellectual taste, and someone like Wang, known mainly for a [somewhat “sordid” data collection company](https://www.sfgate.com/tech/article/sf-tech-startup-scale-ai-sued-wage-theft-19976761.php) rather than any particular technical vision has no business telling LeCun what to think. 

And it goes without saying that I too have huge doubts about LLMs. At this point so do [literally hundreds of other researchers](https://aaai.org/about-aaai/presidential-panel-on-the-future-of-ai-research/), even prominent machine learning insiders like Sutskever and Sutton. By sidelining LeCun, Zuck and Wang made it impossible for LeCun to stay. LeCun was right to depart, and justified as an accomplished scientist to want to pursue his own vision. 

And, also to the good, LeCun is very interested in world models, which is something I too [have often stressed ](https://open.substack.com/pub/garymarcus/p/generative-ais-crippling-and-widespread?utm_campaign=post-expanded-share&utm_medium=web)(sometimes under the term cognitive models) for many years, especially in my 2020 article [The Next Decade in AI](https://arxiv.org/abs/2002.06177).

So I’m glad that LeCun’s new company will investigating a new approach. That said, I doubt that it will succeed, for two reasons.

§

The first reason is technical. LeCun talks about world models, but (because of what appears to be an ego-related mental block against classical symbolic AI, which he has always allied himself against) I don’t think LeCun actually understands what a world model needs to be. 

A world model (if my [2020 article](https://arxiv.org/abs/2002.06177) is correct) needs to be full of explicit, structured, directly retrievable knowledge about time, space, causality, people, places, objects, events, and so on. You need all that for formal reasoning. (In my 2020 paper, I give a detailed example from Doug Lenat.) And you need all that to avoid hallucinations. 

Alas, LeCun, who knows neural networks but refuses to engage in discussion about what classical AI brings to the table, doesn’t really see that. My own view, which I stand by, is that we need “[neurosymbolic](https://open.substack.com/pub/garymarcus/p/how-o3-and-grok-4-accidentally-vindicated?utm_campaign=post-expanded-share&utm_medium=web)” contributions from both traditions if we are to get to trustworthy AI.

So what LeCun has wound up with for “world models” is just another opaque, uninterpretable neural network that doesn’t lend itself to reasoning. It’s a genuine effort, to be praised, at trying to have a system represent the world, over and beyond mere statistics of how language gets used on the web, but it will still likely fall short. I don’t expect it to solve many of the problems that have been plaguing LLMs. 

Indeed LeCun has _already_ been working on his newapproach, JEPA [Joint Embedding Predictive Architecture], with what appears to be a reasonably large team (by academic standards) at Meta for the last few years with not a whole lot to show for it, just a handful of papers that don’t seem earth-shaking. He has the right name for a thing we need (“world model”) but an inadequate implementation.

A [smart though technical post at LinkedIn from Denis O. a month ago, reprinted below, stated the situation extremely well](https://www.linkedin.com/posts/denis-o-b61a379a_ai-activity-7397286659504951296-A0mZ?utm_source=share&utm_medium=member_ios&rcm=ACoAAADWNLsBTecu6qYye_VvYggHb9x236IeOdY). If you don’t follow the technical jargon, you can just skim, and focus especially on the part about what JEPA is — and is not:

_It is useful, it is clever, and it improves how neural nets extract latent structure from sensory streams. But it is not a path to general intelligence, it is not a spatial understanding engine, and it is not the thing that will carry us into real autonomy…. People keep treating JEPA as if it is secretly building a world model. But there is no geometry in JEPA. No structure. No physics. No causal map. No internal dynamics that can hold together when the world becomes discontinuous. JEPA does not understand anything about space. … once the sensory stream drifts outside of the training manifold, JEPA has no stabilizing mechanism to rebuild coherence.”_

Denis O’s closing summary absolutely nails it: “ _JEPA helps deep learning to ‘see’ the world more cleanly… But seeing is not understanding. And understanding needs structure, not just prediction or perception._ ” So it’s not really a model of the world. 

[](https://substackcdn.com/image/fetch/$s_!0cW1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fae3a3810-48a8-4386-93fd-49d2cc9d71b8_1593x1537.png)

That’s the technical problem. Then there is a management problem. LeCun is extraordinarily poor at acknowledging other people’s work, verging on, if not crossing over fully into, intellectual dishonesty. He has systematically ignored and in some cases belittled many people who have preceded him rarely if ever acknowledging most of them, a pattern that goes back to the early days of his career in the late 1980s. I wrote a whole essay about this in November, listing nearly a dozen scholars who have gotten the LeCun treatment (Jürgen Schmidhuber, David Ha, Kunihiko Fukushima, Wei Zhang, Herb Simon, John McCarthy, Pat Hayes, Ernest Davis, Fei-Fei Li, Emily Bender, and myself) and promptly received various emails about three others who have been similarly mistreated, including Alexander Waibel (a CMU professor whose [TDNN](https://isl.iar.kit.edu/pdf/Waibel1989d.pdf) preceded and directly prefigured LeCun’s most famous work), Les Atlas (who crystallized the term convolutional for neural networks before LeCun did), and LeCun’s fellow Turing Award winner Judea Pearl, who was talking about causality for many years before LeCun was. If LeCun pulls the same stuff in his new company, morale will be deathly low.

Still for all that, LeCun’s new company is trying to explore something genuinely new and that’s what we in the field of AI desperately needs. Even if LeCun isn’t doing world models the right way, he is certainly trying. And for that I salute him.
