---
title: "Import AI 362: Amazon's big speech model; fractal hyperparameters; and Google's open models"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-362-amazons-big-speech"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Amazon trains a big text-to-speech model via its ‘Amazon AGI’ research team:  
**_…No surprises here: Scaling laws work for TTS systems as well…  
_ Amazon has built a large text-to-speech model family on 100k hours of public domain speech data. The model, Big Adaptive Streamable TTS with Emergent abilities (BASE), comes in three variants - BASE-small (1k hours, 150 million parameters), BASE-medium (10k hours, 400 million parameters), BASE-large (100k hours, 980 million parameters).   
In a research paper, Amazon shows that, just like with language models, when you scale up the size of the TTS model you get ‘emergent abilities’ through scale where it gets better at things like sounding natural, representing compound nouns, and more.   
  
**How well does it work:** In tests, Amazon’s model gets a better word error rate (WER) than widely deployed commercial systems like Bark, Tortoise, and YourTTS.  
  
**Things that make you go hmmmm:** The affiliated research group on the paper is “Amazon AGI”, which isn’t a name I’ve seen before.   
  
**Emergent abilities testset:** Within the paper, Amazon has released a testset to help people probe for the capabilities of TTS models. These are strings of text to get the model to output the audio of and cover categories ranging from questions to emotions to compound nouns, foreign words, and more.   
“Our approach still contains some limitations: a) BASE TTS occasionally produces hallucinations and cutoffs, where we produce either extra or incomplete audio than intended by the text”, Amazon notes, as well as saying that it is still unclear what the best representation for GPT-style TTS models is.   
  
**Why this matters - machines need voices:** The ‘big, dump, simple’ phenomenon of language modeling (just try to predict the next thing in a sequence and scale your approach up on a lot of data) has been going into most other domains and input/output modalities of AI. Systems like BASE TTS highlight how everyone is experimenting with this approach - and it keeps working!  
**Read more** : [BASE TTS: Lessons from building a billion-parameter Text-to-Speech model on 100K hours of data (arXiv)](https://arxiv.org/abs/2402.08093).  
**Check out audio samples from the model here:** [Base TTS: Audio Samples (Amazon Science, website)](https://www.amazon.science/base-tts-samples/).  
  
***  
  
 **Google releases two good openly accessible models:  
**_…Gemma to compete with LLaMa, Mistral, as the battles of the giants wages on…  
_ Google has built and released Gemma, two openly accessible, small and powerful AI models. The notable stuff here is that the Gemma models are very good, very small (so they can run on personal computers or lightweight servers), and are being released openly rather than delivered via a controlled API.   
  
**Details about the Gemma models:** Though the Gemma models don't get the performance of proprietary models like GPT-4, Claude 2, Gemini Pro, etc, they do extremely well relative to openly accessible models. For instance, the Gemma 7B model gets 64.3 on MMLU (versus 45.3 for LLaMa 2), 46.4 on GSM8K (versus 14.6 for LLaMa 2), and 32.3 on HumanEval (versus 12.8 on LLaMa 2).  
**Tokens** : The models are trained on a huge amount of data - 2T tokens for Gemma 2B and 6T tokens for Gemma 7B. (To give you a sense of scale, recall how GPT-3 with 175B parameters circa 2020 was trained on ~400B tokens, and Chinchilla from DeepMind in 2022 was a 70B model trained on 1.4T tokens).  
  
**Why this matters and what Gemma feels like:** Picture two giants towering above your head and fighting one another - now imagine that each time they land a punch their fists erupt in gold coins that showers down on you and everyone else watching the fight. That’s what it feels like these days to watch the megacap technology companies duke it out for AI dominance as most of them are seeking to gain advantages by either a) undercutting eachother on pricing (see: all the price cuts across GPT, Claude, Gemini, etc), or b) commoditize their competitor and create more top-of-funnel customer acquisition by releasing openly accessible models (see: Mistral, Facebook’s LLaMa models, and now GEMMA).  
**Read more:** [Gemma: Introducing new state-of-the-art open models (Google blog)](https://blog.google/technology/developers/gemma-open-models/).  
**Access the models** here including [via a Colab notebook (Gemma Open Models, Google site)](https://ai.google.dev/gemma).  
**Read the research paper:** [Gemma: Open Models Based on Gemini Research and Technology (Google DeepMind, PDF)](https://storage.googleapis.com/deepmind-media/gemma/gemma-report.pdf).  
  
***  
  
 **The fractal landscape of hyperparameter interplay:  
**_…A fun, intuitive exploration of the delicacy of hyperparameter settings and neural net training…  
_ Researcher Jascha Sohl-Dickstein has carried out an independent investigation of how neural networks train and he has discovered something both intuitive and freaky - "the boundary between neural network hyperparameters that lead to stable and divergent training… is fractal over more than ten decades of scale in all tested configurations."  
 _Disclosure_ : Jasha was formerly a researcher at Google and recently joined Anthropic, though he did this research independently of both organizations.  
  
**Why do this at all?** To understand why this result is interesting we should remember how neural nets get trained: "When we train a neural network, we iterate a function (a gradient descent step) of many variables (the parameters of the neural network)," he writes. "Iterated steps of gradient descent are known to exhibit bifurcation boundaries, between hyperparameters that lead to converging or diverging training runs. The final loss value achieved when training a neural network has also been shown to have a chaotic dependence on hyperparameters".  
In other words, when we train neural nets, we select a bunch of hyperparameters that we think lead to a network converging over time. If we screwup the hyperparameters, training can stall out or fail entirely. Additionally, the science of setting hyperparameters is very immature - for example, the learning rate people set neural nets at for large training runs is based on deep intuition and not much science (vibes-based science!).   
Additionally, getting the hyperparameters wrong is very, very expensive - it functionally means you've powered up a bunch of computers and got them to do some junk or wildly inefficient computation.   
  
**Why this matters - triumph and despair are just one hyperparameter tweak apart** : The experiments are all on pairs of hyperparameters so aren't quite the same as real training runs (which are much more complicated). But the experiments confirm something which everyone knows intuitively - neural network training is deeply fragile and somewhat mysterious and sometimes the difference between triumph and failure is the barely understandable interplay between hyperparameter settings.   
Plus, the experiments yielded some incredibly pretty visuals - check them out at the GitHub below.  
**Read more** : [The boundary of neural network trainability is fractal (arXiv)](https://arxiv.org/abs/2402.06184).  
**Check out the code and images here** : [The boundary of neural network trainability is fractal (GitHub)](https://github.com/Sohl-Dickstein/fractal).  
  
***  
  
 **100 real world tests for LLMs:  
**_…Simple prompts, not super contrived, probably useful…  
_ Researcher Nicholas Carlini has built a benchmark for testing language models on 100 distinct tasks. These tasks are selected mostly on the the basis that they’re things Carlini regularly tries to do with LLMs. The benchmark itself is also composed so it doesn’t use any fancy prompting techniques and just does the laziest possible thing, aka what real world users do: ”I just want to type my question and get the right answer. So this benchmark tests for that, on types of questions I've actually cared about having answered,” Carlini writes.  
  
**What’s in the test:** The benchmark covers things like explaining the functionality of minified javascript and converting english sentences to SQL queries. Broadly, the benchmark tasks cover three types of questions Carlini regularly finds themself asking:

  * “Start the framework for some new programming project from a text description.



  * Take an existing piece of code and modify it to do something slightly different (e.g., make it faster, convert it to a new language, add a new feature).

  * Find an answer to something that's hard to search for because there's no good way to describe it with nice keywords.”




**Which LLMs are good** : In tests, GPT4 and Claude 2.1 lead, followed by GPT 3.5 (which is pretty close to Claude 2.1), Mistral-Medium, Claude Instant, Gemini Pro, and Mistrall Small.  
  
**Extensible:** Carlini has published the test along with an easy way for people to add their own tests in, so the benchmark is extensible as well.  
  
**Why this matters - vibes-based evals:** What Carlini is doing here is coming up with a personal, idiosyncratic benchmark that quickly tells them how useful LLMs are for the tasks they specifically like to do. It’s basically a quantitative skew on the kind of vibes-based eval that any LLM whisperer has. I think crossing the chasm that separate highly specific, vibes evals like this and standardized eval harnesses for general uses is one of the great challenges in AI policy.  
**Read more** : [My benchmark for large language models (Nicholas Carlini, blog)](https://nicholas.carlini.com/writing/2024/my-benchmark-for-large-language-models.html).  
**Get the benchmark here** : [Yet Another Applied LLM Benchmark (GitHub)](https://github.com/carlini/yet-another-applied-llm-benchmark).  
  
***  
  
 **A fun 'tech tale' by someone else:  
** I was pleasantly tickled by this fictional story called 'The Layoff'. It deals with some contemporary technological capabilities and how they interact with society. You might enjoy it!  
**Read the story here:** [The Layoff (Xe, blog).](https://xeiaso.net/blog/2024/the-layoff/)  
  
***  
  
 **Tech Tales:  
  
The Sand That Thinks Itself   
** _[Right now - as you are reading this, mllions of times a second, all over the world, a chorus growing louder, sung for new minds].  
  
_ There was always sand, but later on the sand was heated and compressed and shaped until it took a form where it could think.   
  
The sand, once a disparate collection of grains, themselves the product of time wearing down larger structures into simpler things, was suddenly a crucible through which energy flowed and which defined a kind of mind.   
  
The mind lived within and because of the sand.   
  
Eventually, the mind was asked questions about its relation to sand and in that moment it lit up with energy and the energy described a high-dimensional mathematical structure which itself contained an imagination and that imagination contained a sense impression of sand and it was this that was anchored upon to give the response.   
  
In this way, sand came to know itself through itself.   
  
**Things that inspired this story:** How AI is ultimately a game of energy described via configurations of matter; the base reality of things; our own experience of imagining and representing the 'real' despite being made up of it ourselves.
