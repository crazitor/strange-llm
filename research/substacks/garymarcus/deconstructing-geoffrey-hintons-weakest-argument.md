---
title: "Deconstructing Geoffrey Hinton’s weakest argument"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/deconstructing-geoffrey-hintons-weakest"
---

[](https://substackcdn.com/image/fetch/$s_!y6TJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1f8c754-e739-4059-a7ad-2fc3e2867b3c_1747x1034.jpeg)

“[Don't mess with the Godfather. Geoffrey Hinton savages Gary Marcus](https://x.com/tsarnick/status/1754439023551213845?s=61)”, said one tweet I read this morning. Another was mistakenly convinced that I was “[destroyed](https://x.com/carlosdavila007/status/1754567191339430121?s=61)” by Hinton’s critique.

What Hinton argued is that I was hallucinating in my belief that LLMs remain limited in their understanding of language. You can see the whole clip [here](https://x.com/tsarnick/status/1754439023551213845?s=61), evidently drawn from a talk [he gave in Toronto in October](https://youtu.be/iHCeAotHZa4?si=G3DUd0Xar85vMTPb), but here’s a transcription of his argument:

> These hallucinations as they’re called, or confabulations, they are exactly what people do, we do it all the time. Doing confabulation is: there's someone called Gary Marcus who criticizes neural nets and he says, "Neural nets don't really understand anything, they read on the web." Well that's 'cause he doesn't understand how they work.[1](https://garymarcus.substack.com/p/deconstructing-geoffrey-hintons-weakest#footnote-1-141396248) He's just kind of making up how he thinks it works.
> 
> They don't pastiche together text that they've read on the web, because they're not storing any text. They're storing these weights.
> 
> So actually that's a person doing confabulation. called, or confabulations, they are exactly what people do, we do it all the time

Distilled, Hinton is basically making three arguments::

  1. Because neural networks often perform well, they must understand what they are talking about.

  2. Neural networks don’t store text, so anyone who thinks they are pastisching is hallucinating.

  3. Hallucination errors in LLMs are not a problem, because people hallucinate, too.




None of them flies.

Let’s take them in reverse order. On the point that humans hallucinate too, it is true that humans make errors. But, except in hallucinations associated with disorders like schizophrenia, human errors are very different. Humans rarely make things up wholesale, LLMs do. For example, ChatGPT claimed (falsely yet authoritatively, and without any evidence) that I had a pet chicken named Henrietta:

[](https://substackcdn.com/image/fetch/$s_!ARIo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2fa99ace-1cd1-4aa3-b522-9ab89397dc82_1899x915.jpeg)

Wholesale unintentional fabrication is not the same thing as making a flawed argument, or lying, or spinning facts for political gain, and so on. Instead, it’s an error from recombining little bits of text in wrong ways. Turns out for example that an illustrator named Gary Oswalt illustrated a book named _Henrietta Gets a Nest_ , and perhaps the statistical reconstruction process got muddled. 

[](https://substackcdn.com/image/fetch/$s_!cJAN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb21ece6c-4957-46d2-a9bb-7d0f5ff47746_700x1000.jpeg)

In my entire life I have never met a human that made up something outlandish like that (e.g, that I, Gary Marcus, own a pet chicken named Henrietta), except as a prank or joke. 

One of the most important lessons in cognitive psychology is that any given behavioral pattern (or error) can be caused by many different underlying mechanisms. The mechanisms leading to LLM hallucinations just aren’t the same as me forgetting where I put my car keys. Even the errors themselves are qualitatively different. It’s a shame that Hinton doesn’t get that.

§

On the second point, pastisching, neural networks don’t _literally_ store their input texts (or images etc), and I never said that they did. I generally make clear that the notion of pastische is an analogy, not literal truth, even in podcasts:

> _EZRA KLEIN: You have a nice line in one of your pieces where you say GPT-3, which is the system underneath ChatGPT, is the king of pastiche. What is pastiche, first, and what do you mean by that?_
> 
> _GARY MARCUS: It's a kind of glorified cut and paste. Pastiche is putting together things kind of imitating a style. And in some sense, that's what it's doing. It's imitating particular styles, and it's cutting and pasting a lot of stuff. It's a little bit more complicated than that. But to a first approximation, that's what it's doing is cutting and pasting things._

Being a bit more precise, though still resorting to analogy, what LLMs do is to break down their inputs into lots of little (distributed) bits, and then sometimes reconstruct the originals in the course of their reconstruction process. Because of the immense amounts of data they are now trained on, and because of the immense number of parameters on which they are trained, that reconstruction can in fact sometimes come very close to memorization. The _New York Times versus OpenAI_ lawsuit made that abundantly clear, with a hundred examples like this one, in which ChatGPT reconstructed entire stretches of text (red) from brief prompts[2](https://garymarcus.substack.com/p/deconstructing-geoffrey-hintons-weakest#footnote-2-141396248) (black text in top line):

[](https://substackcdn.com/image/fetch/$s_!0NHE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9ee5238e-513f-4e46-902f-644af57758f5_1142x910.jpeg)

Scientfic work shows this is no fluke. Neural networks do effectively memorize some of what they are trained on, and indeed there is a whole subfield now about the topic. A paper published on November 28 found that it is [hard to get them to ](https://browse.arxiv.org/abs/2311.17035)_[stop](https://browse.arxiv.org/abs/2311.17035)_ : “current alignment techniques do not eliminate memorization”.

Embarrassingly for Hinton, much of the best work on this comes from Nicolas Carlini who has worked at Google for the last several years, where Hinton also worked until his recent retirement. Because data leakage is such a serious problem, and questions of memorization versus generalization loom so large in the field, Hinton surely should have been aware of it. By not even acknowledging the growing literature on memorization (let alone challenging it), Hinton made himself look to be seriously out of touch. 

§

Finally, the argument about understanding is slightly more nuanced. The term _understanding_ itself is not perfectly well-defined. One might conceivably attribute some shallow level of understanding to LLMs, but there are many reasons to doubt that current neural networks have deep understanding. 

“Deep understanding” is a term that Davis and I used throughout our 2019 book, _Rebooting AI,_ literally the conceptual focus of the entire book:

> In short, our recipe for achieving common sense, and ultimately general intelligence, is this: Start by developing systems that can represent the core frameworks of human knowledge: time, space, causality, basic knowledge of physical objects and their inter-actions, basic knowledge of humans and their interactions. Embed these in an architecture that can be freely extended to every kind of knowledge, keeping always in mind the central tenets of abstraction, compositionality, and tracking of individuals.
> 
> Develop powerful reasoning techniques that can deal with knowledge that is com-plex, uncertain, and incomplete and that can freely work both top-down and bottom-up. Connect these to perception, manipulation, and language. Use these to build rich cognitive models of the world. Then finally the keystone: construct a kind of human-inspired learning system that uses all the knowledge and cognitive abilities that the Al has; that incorporates what it learns into its prior knowledge; and that, like a child, voraciously learns from every possible source of information: interacting with the world, interacting with people, reading, watching videos, even being explicitly taught.
> 
> Put all that together, and that's how you get to deep understanding.
> 
> It's a tall order, but it's what has to be done.

Our central claim was that statistical approximators (such as the earlier, smaller LLMs that were then popular) lack common sense, the ability to reason causally, and so on. 

As I put it to Hinton on X today (no reply thus far), reprising and updating what Davis and I have long argued, “Given vast datasets, LLMs approximate well, but their understanding is at best superficial. That’s *why* they are unreliable, and unstable, hallucinate, are constitutionally unable to fact check, etc.”

I stand by all that. I don’t think Hinton has any real argument against it. 

§

There is also something important to be said here about politics and rhetoric. Yann LeCun recently has shifted to my position, and Hinton knows it. But he pretends not to—using an old rhetorical trick—to make it look (falsely) like I stand alone. 

Here’s an example [where Hinton and LeCun discussed this publicly ](https://x.com/geoffreyhinton/status/1728490334336770138?s=12)two months ago, on November 25: 

[](https://substackcdn.com/image/fetch/$s_!1GQE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feaac4003-18d4-4caa-ac52-14da3cfbd177_1142x734.png)

Notice (a) that LeCun makes *exactly* *the same argument I make above and have been making for years, (b) how politely Hinton engages with LeCun, (c) that in the video at the top directed at me Hinton doesn’t address LeCun’s counterargument, and (d) that in the video Hinton does not acknowledge the fact that someone else eminent shares my view—in his effort to falsely portray me as isolated—even though he full well knows that his close colleague LeCun does share that view.

From a politician I might expect such misdirection. From a fellow academic, it is deeply unscholarly.

§

The reality is that Hinton has lost touch. He doesn’t understand the extent to which LLMs do in fact sometimes pastische together huge chunks of texts that have effectively been memorized. LLMs _do_ (sometimes) regurgitate large chunks of effectively stored text, and they _don’t_ understand anything at a deep level. He doesn’t grapple with how his long-time ally has shifted over to my side. And he hasn’t wrapped his head around the many failures (such as regular but unpredictable hallucinations) that show that LLMs are simply approximators, without the true common sense that we would asssociate with deep understanding. 

§

It really isn’t just me, or just me and LeCun. As I was writing this, many others leapt to my defense on X, largely making the same points. A least one tech CEO has said out loud what I was thinking:

[](https://substackcdn.com/image/fetch/$s_!EqsW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4634df92-f734-4e8a-8a93-555bfad8b0dd_1202x293.png)

Tim Crane, a philosopher, from Vienna, wrote “very disappointing comment from Hinton, both in content and tone”. Another philosopher, from Auburn, wrote this

[](https://substackcdn.com/image/fetch/$s_!b9fd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb000529f-edad-4a03-91f8-1633fa59949a_1150x364.png)

From someone with a M.S., in cognitive science from U. Rochester:

[](https://substackcdn.com/image/fetch/$s_!h2V5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa08da546-31fb-452c-92c8-6e36227851ae_1271x443.png)

ML researcher and entrepreneur Chomba Bupe added:

[](https://substackcdn.com/image/fetch/$s_!RnEl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbc67583d-5be3-4701-a46a-1225b35ebe0a_1213x334.png)

The linguist Evelina Leivada was even more scathing:

[](https://substackcdn.com/image/fetch/$s_!RuHv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faae49b2a-16fc-46d7-b27f-367523902643_1170x543.jpeg)

All that pushback against Hinton, just in the last few hours. I am truly not alone.

§

The irony of all this is that in November Hinton publicly accused LeCun of being intellectually self-absorbed, putting heavy weight on his own views while ignoring contradicting views:

[](https://substackcdn.com/image/fetch/$s_!1F7C!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6e494580-afbc-4162-a9b7-c7955dfb2352_1206x221.png)

That’s exactly what Hinton has done here. He has mistaken his own opinion for that of many others (almost all experts in classical AI would disagree with him), all the while arguing for a mistaken view in a most condescending yet (in this case) regrettably uninformed way.

_**Gary Marcus,** Professor Emeritus at NYU, is a scientist who has been writing about the limitations of neural networks for over three decades, in books and articles in leading journals such as Science, Nature, Cognition, and Artificial Intelligence. The core challenges that Marcus pointed out in his 2001 MIT Press book The Algebraic Mind, including hallucinations and unreliability, remain unsolved—23 years later._

[1](https://garymarcus.substack.com/p/deconstructing-geoffrey-hintons-weakest#footnote-anchor-1-141396248)

“They don't pastiche together text that they've read on the web… They’re storing these weights and generating things.” is a somewhere between a false dicotomy and misdirection. LLMs don’t store things in simple databases, but when presented with enough data, their regeneration of distributed bits has demonstrably duplicated lengthy training materials multiple times, a phenomenon that is called memorization in the field.

[2](https://garymarcus.substack.com/p/deconstructing-geoffrey-hintons-weakest#footnote-anchor-2-141396248)

OpenAI will no doubt by now have filtered this specific example so that it can no longer be replicated, now that it has appeared in a lawsuit. But the variety of the examples along with the technical literature on memorization and data leakage in large language models make clear that this kind of reconstruction certainly can happen with some regularity.
