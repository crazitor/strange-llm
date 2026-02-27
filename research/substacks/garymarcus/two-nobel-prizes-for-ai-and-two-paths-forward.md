---
title: "Two Nobel Prizes for AI, and Two Paths Forward"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/two-nobel-prizes-for-ai-and-two-paths"
---

As you have surely read by now, not one but two Nobel Prizes went to AI this week. Physics went to John Hopfield and Geoff Hinton; Chemistry went half to David Baker (for developing novel proteins) and half to Demis Hassabis and John Jumper for their work on AlphaFold. 

To my mind, these two decisions are quite different. Bear with me as I walk through some concerns about the first prize; I am quite enthusiastic about the second, and promise there is an important, positive message to the field therein at the end.

§

Let’s start with Hinton’s award, which has led a bunch of people to scratch their head. He has absolutely been a leading figure in the machine learning field for decades, original, and, to his credit, persistent even when his line of research was out of favor. Nobody could doubt that he has made major contributions. But the citation seems to indicate that he won it for inventing back-propagation, but, well, he didn’t.

The esteemed computational neuroscientist Steven Grossberg wrote about this yesterday on the decades-running neural network professional email list [Connectionists](https://mailman.srv.cs.cmu.edu/mailman/listinfo/connectionists) (which Hinton has been known to read and post on):

> Paul Werbos developed back propagation into its modern form, and worked out computational examples, for his 1974 Harvard PhD thesis.
> 
> Then David Parker rediscovered it in 1982, etc.
> 
> Schmidhuber provides an excellent and wide-ranging history of many contributors to Deep Learning and its antecedents:
> 
> [https://www.sciencedirect.com/science/article/pii/S0893608014002135?casa_token=k47YCzFwcFEAAAAA:me_ZGF5brDqjRihq5kHyeQBzyUMYBypJ3neSinZ-cPn1pnyi69DGyM9eKSyLsdiRf759I77c7w](https://urldefense.proofpoint.com/v2/url?u=https-3A__www.sciencedirect.com_science_article_pii_S0893608014002135-3Fcasa-5Ftoken-3Dk47YCzFwcFEAAAAA-3Ame-5FZGF5brDqjRihq5kHyeQBzyUMYBypJ3neSinZ-2DcPn1pnyi69DGyM9eKSyLsdiRf759I77c7w&d=DwMGaQ&c=slrrB7dE8n7gBJbeO0g-IQ&r=wQR1NePCSj6dOGDD0r6B5Kn1fcNaTMg7tARe7TdEDqQ&m=TgoVG9eYKrsxVFII37rTTmxcKLEoHZxFJ15o2_DXT0Tcj6Pa9iuU37B8Q4EZRUiH&s=oAERegVRi_JWDeemk3mENEZlt9ALCK_4etVtBBo0KmA&e=)
> 
> This article has been cited over 23,000 times.

Even more harshly he wrote, in defense of Werbos who preceded Hinton:

> I believe that what I wrote about the 1974 work of Paul Werbos, which also developed computational examples, gives him modern priority for back propagation.
> 
> Mentioning lots of other applications does not diminish Paul’s priority.
> 
> What Paul did not do well was to market his work.
> 
> But good marketing does not imply priority, just as Voltaire’s “marketing” of the discoveries of Newton on the Continent did not diminish Newton’s priority. 

Schmidhuber himself just posted a long summary of all that on X (reminding me in an email that there was plenty of work before Werbos as well):

[](https://substackcdn.com/image/fetch/$s_!zJve!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02badeba-aac7-437e-bb35-6fa57e3be97a_1250x2086.jpeg)

[](https://substackcdn.com/image/fetch/$s_!QGs_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fce0c1135-4139-422f-abd8-57b669f4feef_1313x856.jpeg)Links for the above: <https://people.idsia.ch/~juergen/ai-priority-disputes.html> and <https://people.idsia.ch/~juergen/deep-learning-history.html>

Even Steve Hanson, a long-time Hinton defender, acknowledged “we agree on the fact that the "Scientific committee of the Nobel commitee" didn't know the N[eural] N[etwork] history very well”. 

Hinton has certainly had a profound influence on machine learning, but it’s still not entirely clear what he specifically won the prize for, or how that has advanced physics. People will probably be asking questions about this particular award for a long time.

§

Hassabis’s win (shared with DeepMind researcher John Jumper), in contrast, is a slam dunk. (So is Baker’s - I first saw him speak in 2017 at an event organized by Paul Allen and his work on synthesizing new proteins was so mindblowing that it was immediately obvious Baker would win a Nobel sooner or later). 

AlphaFold is a huge contribution to both chemistry and biology. It arguably still hasn’t lived up to the extreme hype that I have sometimes seen, but it’s a fantastic contribution, used widely by biologists, and in my mind one of the two biggest contributions of AI to date, if not the biggest. (Web search is powered by AI, and has been transformational in different ways).

&

All that is history. What’s next? To my mind, Hinton and Hassabis represent two different paths forward. Hinton has long stood for back-propagation (or something similar all the way down); in recent decades, he has [ridiculed neurosymbolic AI](https://x.com/tabithagold/status/1070736319901519876?s=61) — which would bring together ideas from classical AI (that Hinton has aligned himself against) and neural networks (which he has favored). 

Hassabis has quietly been advancing neurosymbolic AI (including [the recent AlphaGeometry work that I praised in July](https://garymarcus.substack.com/p/alphaproof-alphageometry-chatgpt)) and been far less dogmatic than Hinton.

§

Many who have followed Hinton’s advice have sought to build “end-to-end” neural networks. Hassabis and Jumper’s [AlphaFold2](https://www.nature.com/articles/s41392-023-01381-z) is something quite different. It does _not_ work directly from a sequences of nucleotides to a the output of proposed 3d structure with a single massive neural network, as the end-to-end tradition might attempt. 

Rather, it is considerably more structured: there is both a custom-built neural network [the second row in the figure below] AND quite a lot classical symbolic machinery for information integration and search tools, in which the neural network is embedded:

[](https://substackcdn.com/image/fetch/$s_!yLu6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fabf1abc6-fdf5-4c1c-af8e-f6c6f32c4a02_1747x1901.webp)

[](https://substackcdn.com/image/fetch/$s_!6-KN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2aa0c4cd-a3d8-43f5-94be-9bc62db06af4_2016x362.png)

It is, as far as I can tell, the first Nobel Prize for Neurosymbolic AI.

§

In my view, Hinton made machine learning popular, but has [too often bullied people ](https://www.cs.toronto.edu/~hinton/)advocating work outside of his tradition. But the anti-neurosymbolic tradition is limited; its most visible manifestation, LLMs, has brought fame and money, but no robust solution to solving any particular problem with great reliability. It remains opaque, hobbled with hallucinations and bone-headed errors, and greedy to the extreme in its need for electricity, water, and data.

It’s time for a new approach, and Hassabis sees that. His open-mindedness will serve the field well.

_**Gary Marcus** hopes to see a new, more trustworthy breed of AI before long._
