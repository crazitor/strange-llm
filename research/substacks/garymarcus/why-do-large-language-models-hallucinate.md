---
title: "Why DO large language models hallucinate?"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/why-do-large-language-models-hallucinate"
---

Regular readers of the newsletter will know that I have long been negatively impressed by the routine hallucinations of LLMs, and that my favorite example has involved an alleged pet chicken named Henrietta that I allegedly own:

[](https://substackcdn.com/image/fetch/$s_!oyPu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6804a3c2-e84a-4018-b9d5-8890c42ab7a8_1492x742.jpeg)

This, sent to me by a reader in 2023, is of course a hallucination. I don’t actually own a pet chicken, nor any pet named Henrietta. If I did own a pet chicken I rather doubt I would call it Henrietta. 

I do, however, know the legendary Harry Shearer, and was lucky enough to dine with him yesterday in LA. Antecedent to our breakfast, he sent me a problematic biography of him (“vomited by AI” in the words of a professor friend of his who forwarded it to him), along with the comment “No pet chicken, but still…”:

[](https://substackcdn.com/image/fetch/$s_!s-Z2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F16d7f3a1-5944-40ea-beb1-825ab96547f2_1390x862.png)

The joke was that, as we have come to expect, the AI’s output was truth mixed with untruth, intermingled so finely that to the uninitiated it might appear as truth — especially given the encyclopedia-like tone.

And indeed some of it is true. Harry really does act and do voiceovers for a lot of the Simpson characters, and he did play the bass player in the legendary _[This is Spinal Tap](https://en.wikipedia.org/wiki/This_Is_Spinal_Tap)_.

But, come on, the name of the bass player in _Spinal Tap_ was [Derek Smalls](https://en.wikipedia.org/wiki/Derek_Smalls), not David Stanhill (a made-up name that doesn’t correspond to anyone Harry or I know, in that film or otherwise). And Harry is an _American_ actor, not British, born and raised in Los Angeles. And whatever X may allege, Harry assures me that he didn’t have anything to do with Jaws. 

And then there are the errors of omission; Harry didn’t just play Derek Smalls, he co-wrote _This is_ _Spinal_ _Tap_ , a rather important credit to omit. He wrote for and performed on Saturday Night Live, and acted in many other movies from _The Truman Show_ to _A Mighty Wind_ , [wrote and directed a documentary about Hurricane Katrina](https://www.imdb.com/title/tt1702441/), and so on. No mention either of lovely and talented wife [Judith Owen](https://en.wikipedia.org/wiki/Judith_Owen), his radio shows or his Primetime Emmy Award or Grammy nominations, either. 

The extra embarrassing part about all of this for GenAI is that almost of the above information could have been found quickly and easily with a two second search for [his wikipedia page](https://en.wikipedia.org/wiki/Harry_Shearer), and most of it could be found in the first screenful at that.

[](https://substackcdn.com/image/fetch/$s_!768t!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F07b502cf-9997-4131-9899-94832814400f_1637x1422.png)

Three paragraphs and a box, and Google AI Overviews couldn’t get it right. Which raises the question: _how could GenAI be so dumb that it could not fact check its own work against wikipedia_? (And also, for another time, [how could anyone think that a system so dumb is tantamount to AGI?](https://garymarcus.substack.com/p/openais-o3-and-tyler-cowens-misguided?r=8tdk6))

§

As they occasionally say in the entertainment business, thereby lies a tale.

It is a tale of confusion: between what humans do, and what machines do.

That tale first started in 1965 with the simple AI system Eliza, which used a bunch of dopey keyword searches to fool humans into thinking it was far more intelligent than it actually was. You say “my girlfriend and I had a fight”, it matched the word “girlfriend” and spat back a phrase like “tell me more about your relationship”, and voila, some people imagined intelligence where there is nothing more than a simple party trick.

Because LLMS statistically mimic the language people have used, they often _fool people_ into thinking that they operate like people.

But they don’t operate like people. They don’t, for example, ever _fact check_ (as humans sometimes, when well motivated, do). They _mimic the kinds of things of people say in various contexts_. And that’s essentially all they do.

You can think of the whole output of an LLM as a little bit like Mad Libs. 

**[Human H] is a [Nationality N] [Profession P] known for [Y].**

By sheer dint of crunching unthinkably large amounts of data about words co-occurring together in vast of corpora of text, sometimes that works out. Shearer and _Spinal Tap_ co-occur in enough text that the systems gets that right. But that sort of statistical approximations lacks reliability. It is often right, but also routinely wrong. For example, some of the groups of people that Shearer belongs to, such as entertainers, actors, comedians, musicians and so forth includes many people from Britain, and so words for entertainers and the like co-occur often with words like British. To a next-token predictor, a phrase like _Harry Shearer_ lives in a particular part of a multidimensional space. Words in that space are often followed by words like _“British actor”._ So out comes a hallucination. 

And although I don’t own a pet chicken named Henrietta, another Gary (Oswalt) illustrated a book with Henrietta in the title. In the word schmear that is LLMs, that was perhaps enough to get an LLM to synthesize the bogus sentence with me and Henrietta. 

[](https://substackcdn.com/image/fetch/$s_!Iovh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fba1d0ee2-446e-450e-8f12-9fcf16fb533c_700x1000.jpeg)

Of course the systems are probabilistic; not every LLM will produce a hallucination every time. But the problem is not going away; OpenAI’s recent o3 [actually hallucinates ](https://www.theleftshift.com/openai-admits-newer-models-hallucinate-even-more/)_[more](https://www.theleftshift.com/openai-admits-newer-models-hallucinate-even-more/)_[ than some its predecesssors](https://www.theleftshift.com/openai-admits-newer-models-hallucinate-even-more/). 

The chronic problem with creating [fake citations in research papers](https://www.forbes.com/sites/larsdaniel/2025/01/29/the-irony-ai-experts-testimony--collapses-over-fake-ai-citations/) and [faked cases in legal briefs](https://www.rawstory.com/lindell-dominion-2671843170/) is a manifestation of the same problem; LLMs correctly “model” the structure of academic references, but often make up titles, page numbers, journals and so on — once again failing to sanity check their outputs against information (in this case lists of references) that are readily found on the internet. So to is the[ rampant problem with numerical errors in financial reports](https://www.vals.ai/benchmarks/finance_agent-04-22-2025), documented in a recent benchmark.

Just how bad is it? One recent study showed [rates of hallucinations of between 15% and 60% ](https://research.aimultiple.com/ai-hallucination/)across various models on a benchmark of 60 questions that were _easily verifiable relative to easily found CNN source articles that were directly supplied in the exam_. Even the best performance (15% hallucination rate) is, relative to an open-book exam with sources supplied, pathetic. That same study reports that, “According to Deloitte, 77% of businesses who joined the study are concerned about AI hallucinations”.

If I can be blunt, it is an absolute embarrassment that a technology that has collectively cost about half a trillion dollars can’t do something as basic as (reliably) check its output against wikipedia or a CNN article that is handed on a silver plattter. But LLMs still cannot - and on their own may never be able to — reliably do even things that basic. 

LLMs don’t actually know what a nationality, or who Harry Shearer is; they know what words are and they know which words predict which other words in the context of words. They know what kinds of words cluster together in what order. And that’s pretty much it. They don’t operate like you and me. They don’t have a database of records like any proper business would (which would be a strong basis to solve the problem); and they don’t have what people like Yann LeCun or Judea Pearl or I would call a _world model_. 

Even though they have surely digested Wikipedia, they can’t reliably stick to what is there (or justify their occasional deviations therefrom). They can’t even [properly leverage the readily available database that parses wikipedia boxes into machine-readable form](https://enterprise.wikimedia.com/blog/structured-contents-wikipedia-infobox/), which really ought to be child’s play for any genuinely intelligent system. (Those systems also can’t reliably stick to the rules of chess despite having them – and millions of games – in their database, a manifestation of the related problem of extracting statistical tendencies without every fully deriving and apprehending the correct abstractions).

LLMs have their uses – next-token prediction is great for a kind of fancy autocomplete for coding, for example — but it is a fallacy to think that because GenAI outputs sound human-like that their computations are human-like. LLMs mimic the rough structure of human language, but 8 years and roughly half a trillion dollars after their introduction, they continue to lack a grasp of a reality. 

And they have such a superficial understanding of their own output that they can’t begin to fact check it.

We will eventually get to something better, but continuing to put all our eggs in the Henrietta’s LLM basket is absurd to the point of being [delusional](https://en.wikipedia.org/wiki/Extraordinary_Popular_Delusions_and_the_Madness_of_Crowds).

_**Dr. Gary Marcus** has been warning people about the inherent problem of hallucinations in neural networks since 2001. _

Bonus track: Harry Shearer contemplating LLMs, May 4, 2025, in his hometown of Los Angeles, photo by the author:

[](https://substackcdn.com/image/fetch/$s_!My3M!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc244dd8e-c33c-41d3-9fa3-756eed953071_4208x5611.jpeg)
