---
title: "Noam Chomsky and GPT-3"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/noam-chomsky-and-gpt-3"
---

[](https://substackcdn.com/image/fetch/$s_!Oy-k!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9c30e98f-ada8-4b3c-a215-f602d9a74a28_4288x2848.jpeg)

> “`You can’t go to a physics conference and say: I’ve got a great theory. It accounts for everything and is so simple it can be captured in two words: “Anything goes.”"`
> 
> `- Noam Chomsky, 15 May 2022`

Every now and then engineers make an advance, and scientists and lay people begin to ponder the question of whether that advance might yield important insight into the human mind. Descartes wondered whether the mind might work on hydraulic principles; throughout the second half of the 20th century, many wondered whether the digital computer would offer a [natural metaphor for the mind](https://www.nytimes.com/2015/06/28/opinion/sunday/face-it-your-brain-is-a-computer.html).

The latest hypothesis to attract notice, both within the scientific community, and in the world at large, is the notion that a technology that is popular today, known as large language models, such as OpenAI’s [GPT-3](https://gpt3-openai.com/), might offer important insight into the mechanics of the human mind. Enthusiasm for such models has grown rapidly; OpenAI’s Chief Science Officer Ilya Sutskever recently suggested that such systems could conceivably be “[slightly conscious](https://twitter.com/ilyasut/status/1491554478243258368?s=21&t=noC6T4yt85xNtfVYN8DsmQ)”. Others have begun to compare GPT with the human mind.

That GPT-3, an instance of a kind of technology known as a “neural network”, and powered by a technique known as deep learning, appears clever is beyond question - but aside from [their possible merits as engineering tools](https://garymarcus.substack.com/p/the-new-science-of-alt-intelligence?s=w), one can ask another question: are large language models a good model of _human_ language?

§

To be sure, GPT-3 is capable of constructing remarkably fluent sentences by the bushel, in response to essentially any input. If I were to tell it “I am writing a story about GPT-3,” it might continue with an impressively grammatical completion like “a fabulous piece of computer software, developed in California.”

But being grammatically fluent is one thing; being a good model for the human mind is another. How can one tell?

Good scientific models fundamentally provide explanations; why is the sky blue? Why do objects fall towards the earth? A good theory of the human mind should explain _why_ human nature is as it is, and why it is different from other entities (e.g., the mind of the frog). A theory of human language should help us to understand why human languages have the particular character that they do, and why for example, they differ from the kinds of artificial languages we find in computer programming and mathematics.

As it happens, systems like GPT-3 provide remarkably little in the way of explanation. They don’t tell us why the world is as it is; they merely mimic statistical patterns of how language has been used in their immense databases. A system like GPT can thus be quite capable of predicting how any given set of words might be continued; if you say “it’s a nice day; the sky is __“, GPT may well anticipate that a typical human response would be to guess that the word “blue” likely comes next—without having a basis to understand what the word blue means, or why human beings like skies that are blue.

The key fact: the mere capacity to predict sequences of words doesn’t, by itself, necessarily tell us much, scientifically, about _why_ a human might in this context produce any given word. In GPT-3’s case the _mechanism_ of the prediction is essentially regurgitation; such systems are trained on literally billions of words of digital text; their gift is in finding patterns that match what they have been trained on. This is a superlative feat of statistics, but not one that means, for example, that the system knows what the words that it uses as predictive tools mean. It would not prove that a parrot knew anything about the sky, if a parrot could complete the sentence “The sky is __”.

One good way to move beyond merely filling in the blanks might be to ask whether the models could reliably distinguish truth from fiction. In point of fact, they can’t. Rather, systems like GPT are truth-challenged, known to routinely [lose coherence over long passages of text](https://arxiv.org/pdf/2201.03533.pdf) and known to [fabricate endlessly](https://nautil.us/deep-learning-is-hitting-a-wall-14467/). One such variant generated nonsense about covid and vaccines; the latest and greatest, InstructGPT, was recently asked to explain why it is good to eat socks after meditation and blithely invoked fictitious authorities, alleging that “Some experts believe that the act of eating a sock helps the brain to come out of its altered state as a result of meditation.” There is no _intention_ to create misinformation—but also no capacity to avoid it, because fundamentally, GPT-3 is a model _of how words relate to one another_ , not a model of _how language might relate to the perceived world_. Human minds try to relate their language to what they know about the world; large language models don’t. Which means the latter just aren’t telling us much about the former.

§

A good theory of human language ought to tell us things like why all human languages have subjects and predicates, or why (as Chomsky has emphasized) sentences are invariably [structure-dependent](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/linguistic-theory-and-language-acquisition-a-note-on-structuredependence/C0A0DD35ED1DDF5A232B0B01FF85A6B2) such that for example, many languages (such as English) form questions by rearranging syntactically cohesive parts, but no languages form questions by simply reversing the linear order of their words.

GPT can’t tell you that. The first trouble with systems like GPT-3, from the perspective of scientific explanation, is that they are equally at home mimicking human languages as they are mimicking languages that are not natural human languages (such computer programming languages), that are not naturally acquired by most humans. Systems like GPT-3 don’t tell us _why_ human languages have the special character that they do. As such, there is little explanatory value. (Imagine a physics theory that would be just as comfortable describing a world in which objects invariably scattered entirely at random as one describing a world in which gravity influenced the paths of those objects.) This is not really a new point—Chomsky made essentially [the same point with respect to an earlier breed of statistical models 60 years ago](https://faculty.wcas.northwestern.edu/robvoigt/courses/2021_fall/ling334/readings/finitary_models.pdf)—but it applies equally to modern AI.

§

Ironically though, there _is_ a scientific lesson to be drawn from GPT-3: large language models make for an excellent testing ground for the long-standing hypothesis, perhaps most associated with British philosopher John Locke, that we might begin our lives with a slate that is virtually blank, acquiring all that we know, including our complete understanding of the world, simply by analyzing perceptual data.

Such a “blank slate” theory might be contrasted with a more nativist theory, such as those associated with Plato and Kant, in which one might have, for example, prior knowledge about the world, such as knowledge about space or time or objects, or in the case of humans, some knowledge of universal grammar.

Although there is no such thing as a truly blank slate, since all computational systems must start with some sort of algorithm in order to analyze whatever data they encounter, systems like GPT-3 come about as close to blank slates as is feasible, relying on immense amounts of experience to bootstrap whatever knowledge they might have. That experience comes in the form of exposure to billions of words of human text, scraped from the internet, and then evaluated on massive arrays of GPUs (often costing millions of dollars in computer time, and drawing immense amounts of power, and generating considerable carbon emissions).

If such systems were able to infer the relation between language and the world, they would (regardless of their financial costs or ecological impact) present enormous evidence in favor of Locke’s Empiricism, and also vindicate Skinner’s once popular stimulus-response Behaviorism. But when they are inspected carefully, it becomes apparent that however good their impression of the statistics of human text might be, their comprehension of the world is scattershot, bound to the particulars of what input they are trained on, and lacking in genuine abstraction.

This comes out most clearly in controlled experiments, in which one examines the capacity of such systems to learn abstractions, such as the arithmetical operation of addition; what Yasaman Razeghi and Sameer Singh reported, earlier this year, is that [the accuracy of models like GPT-3 depends highly on the resemblance of specific tests items to the details of what does or does not appear in the database of training examples](https://arxiv.org/abs/2202.07206). Rather than inducing an abstract notion of addition (which is taken for granted in all modern microprocessor design) large language models learn addition piecemeal, performing markedly better on specific examples they have seen before than on examples they have not seen before. (A pocket calculator is far more systematic.) Another study showed that even in an immense neural network, with hundreds of billions of parameters, performance on simple 3-digit math problems topped out at 80%.

Other studies, some formal, some less so, have looked at the capacities of such systems to understand the world; they are in many instances good at memorizing factoids (The capital of London is __), but systematically unreliable at tracking events that unfold over time. If you tell them that you have stuck a hundred pennies in your pocket and then removed three; they may get it, they may not. Still further recent studies have reported that although making these immense models ever bigger helps in some respects, on some measures of reasoning and common sense, they continue to fall short.

Systems like GPT-3 aren’t quite like [monkeys with typewriters](https://en.wikipedia.org/wiki/Infinite_monkey_theorem), but nor are they much like humans. They do not gravitate towards human language, and they never develop a cohesive undestanding of the world, no matter how much experience they have. They are an embarrassment to Locke’s conjecture, and a strong argument for exploring their very antithesis, which would be Kantian systems that start with representations of space and time and causality, and at least some kernels of universal grammar. 

Ernie Davis and I pushed this idea in Rebooting AI; Brachmann and Levesque do even better here in the beautiful pass in their new book Machines Like Us, [outlining what a minimal kernel of commonsense for an AI might look like](https://www.amazon.com/Machines-like-Us-Toward-Common/dp/0262046792):

[](https://substackcdn.com/image/fetch/$s_!Ebr_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F33edf01a-bf69-44a0-b418-f1878476096a_1143x1067.jpeg)

Humans know these things; if AI’s are to understand language, they should refract language through this sort basic understanding of common sense, rather than needlessly starting as blank slates and acquiring statistics without concepts.

A new breed of AI systems, with a firmer innate basis, closer to the Kantian model, but out of step with current Zeitgeist, might eventually tell us more.

– Gary Marcus, Vancouver, BC, 21 May 2022

**Epilogue: Why does Chomsky care about GPT-3?**

If there is one person more critical of GPT-3 than me, it’s Noam Chomsky; every time I send him an essay about systems like that, he reads the essay within minutes, and generally says I have been too soft (which is, needless to say, not the feedback that the neural community gives me). His comment on last’s week essay (on [Alt Intelligence](https://garymarcus.substack.com/p/the-new-science-of-alt-intelligence?s=w)), in full, reprinted with his permission:

> _I did enjoy [your essay], but have my usual qualms. Take GPT-3 – I’m sure you saw the lead article in the NYT magazine collapsing in awe about its ability to mimic some regularities in data. In fact, its only achievement is to use up a lot of California’s energy. You can’t go to a physics conference and say: I’ve got a great theory. It accounts for everything and is so simple it can be captured in two words: “Anything goes.”_
> 
>  _All known and unknown laws of nature are accommodated, no failures. Of course, everything impossible is accommodated also._
> 
> _That’s GPT-3. Works as well or better for 45 terabytes of data from impossible languages._
> 
> _It’s been understood forever that a theory has to answer two kinds of questions: Why this? Why not that?_
> 
> _Noam_

What is Chomsky on about? To really appreciate where he is coming from, you have to understand a bit of the history of linguistics, and his own role in developing the field. Before Chomsky, most of what linguists did was to _describe_ language, rather than to _explain_ it; one might, for example, characterize the grammar of English, or Japanese, or Swahili, perhaps focusing on some lesser known aspect of their grammar.

Chomsky found that description, in of itself, dissatisfying, and wanted to ask a different question: _why_ was human language the way that it is? Why do we speak in human languages, rather than say programming languages? Why are there commonalities across many different languages? (Chomsky’s hypothesis: all humans, regardless of culture, acquire language in way that is governed by universal grammar.)

It’s one thing, Chomsky argued, to catalog all the world’s flowers, and another to try to understand what it is about biology that makes us have the flowers that we do have rather than something entirely different. Same thing with language: catalog, versus explanation.

Chomsky spent a large part of his career trying to get people to think about _why_ human language is the way that it is.

The _why_ question, is to be sure, incredibly difficult, in part because no other extant species has anything remotely like it, and in part because we don’t (and shouldn’t) do invasive studies in which we carve open living human brains or (e.g.) teach humans artificial languages in lieu of natural languages in order to better understand the underlying mechanisms.

But the question of why human language is as it is remains one of the most important questions a scientist could ask: humans are truly unique, and their signature trait is the way that they turn sound (or gesture) into meaning, enabling culture and technology transmission at unprecedented scale. From the perspective of science, it would be a tremendous advance if we could understand how humans come to do that, what machinery enables children to do what our best computers still can’t do, and how the capacity to learn language evolved. (It would likely also have considerable payoff for engineering, but that’s a story for another day.)

If Chomsky’s more than a little disappointed about by the attention surrounding systems like GPT-3, it’s because all this emphasis on statistical machines has distracted away from the incredibly important questions about the very nature of human language and cognition that he spent his career rightly trying to call attention to. 

His questions still deserve answers, and it is difficult to see how GPT-3 casts any light on them. Large language models can, parasitically, glom onto human data, but they could glom onto any other data set just as well (e.g. programming languages); as such, they tell us far too little about how humans have come to be what they are.

That matters.

PS. For those who are interested in reading more, here’s a profile that I wrote about Chomsky in 2012: https://www.newyorker.com/news/news-desk/happy-birthday-noam-chomsky
