---
title: "Import AI 353: AI bootstrapping; LLMs as inventors; Facebook releases a free moderation tool"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-353-ai-bootstrapping-llms"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Lab formed to figure out just what the heck to do with today’s powerful AI:  
**_….Answer.ai is going to explore the development and deployment side of AI…  
_ A couple of interesting characters have raised $10m and launched Answer.AI, a research lab to “figure out the fundamental research needed to tame AI, and the development path needed to make it useful in practice.”  
  
**What Answer.ai is:** Answer.ai is founded by Jeremy Howard (of fast.ai) and Eric Rease (of ‘lean startup’ fame and the Long-Term Stock Exchange). The goal of the “AI R&D lab” is to make “practical end-user products based on foundational research breakthroughs”.   
In practice, this means Answer.ai will spend more time thinking about the development and deployment of AI than some more basic research (though will be actively researching different approaches to development and deployment). “At Answer.AI we are not working on building AGI. Instead, our interest is in effectively using the models that already exist,” the company writes. “Figuring out what practically useful applications can be built on top of the foundation models that already exist is a huge undertaking”.  
  
**Why this matters - no one has figured out the right interface to AI:** Today, I talk to AI systems via text or voice and I also play around with image interfaces. But none of these feel particularly satisfying - we’re applying past UX paradigms to new technologies and I know that in the future society will figure out better and smarter ways to interact with AI technology. I’m interested to see how Answer.ai changes both the underlying technologies of AI as well as the different ways it can be deployed, experienced, and interfaced with.   
**Read more:**[A new old kind of R&D lab (Answer.ai)](https://www.answer.ai/posts/2023-12-12-launch.html).  
  
***  
  
 **Google bootstraps its models to be smarter using ReST^EM:  
**_…If bootstrapping keeps working, the importance of data goes down and the importance of models goes up…  
_ Google DeepMind has figured out how to use reinforcement learning to generate iteratively better datasets. This is a form of AI bootstrapping - you use AI to generate the ingredients for successor systems to train on. DeepMind’s technique is called Expectation-Maximization for Reinforced Self-Training (ReST^EM) and builds on earlier work called Reinforce Self-Training (ReST, [Import AI #338](https://jack-clark.net/2023/08/28/import-ai-338-consciousness-and-ai-self-improving-language-models-maps-of-thought/)).  
  
**What ReST^EM is** : The technique is a way to use an external feedback signal to help models learn how to generate higher-quality datasets. In tests, they’re able to go through multiple RL steps with ReST^EM and get improvements in math and code generation tasks, suggesting that “self-training with feedback can substantially reduce dependence on human-generated data.”  
  
ReST^EM has two key steps:

  * **Generate** : “Generate a dataset by sampling many output sequences from the current policy. Score output sequences with a binary reward function.”

  * **Improve** : “Use the new dataset from the generate step to fine-tune the policy… we always fine tune the base pretrained language model to minimize task-specific over-fitting and minimize drift from the base model.”




**Does it work?** They test ReST^EM in two domains - Competition-level mathematical problem solving via the MATH dataset and code generation via the APPS dataset. They find that both datasets benefit from the approach, though MATH sees a more significant benefit, likely as a consequence of the size of the MATH dataset. APPS, meanwhile, sees some initial improvement, but multiple iterations of RL lead to degradation in performance, which the authors speculate is a consequence of overfitting.   
**Positive transfer:** There’s some evidence of positive transfer from the model - specifically, they test out their REST^EM tuned models on the 200-task ‘Big Bench’ suite and find some positive indications of generalization. “We see no major degradation on any of the tasks on the BBH suite,” they write. “Further, we find that the model fine-tuned on Hendrycks MATH significantly outperforms the base model on this suite when using chain-of-thought prompting“.  
  
**Don’t get too excited:** While ReST seems to work, it has some rough edges; you need a “moderately sized training set of problems or prompts, which would need to be collected (from humans) for any new task of interest”. Along with that, ReST^EM “also requires access to a manually-designed or learned reward function, ideally one that can be computed automatically” which further limits the types of things it will work for.   
  
**Why this matters - signs of life for bootstrapping:** ReST^EM is yet another sign of life for AI bootstrapping, along with FunSearch (covered elsewhere in this issue), the trend of using preference models from LLMs to tune other LLMs, and so on. It feels like AI systems have very recently become good enough that you can use them (selectively and in somewhat limited ways) to bootstrap them towards greater performance.   
If this trend continues, then it will further speed up the rate at which people can develop smarter AI systems and it could potentially also do things like lower the costs of datasets as parts of AI models and increase the costs people are willing to dump into the base model - after all, if you can turn compute into subsequent bootstrapping, why wouldn’t you?  
**Read more:** [Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models (arXiv)](https://arxiv.org/abs/2312.06585).  
  
***  
  
 **Facebook releases a free moderation LLM:  
**_…Openly accessible models and tests for a safer AI ecosystem…  
_ Facebook has released a model to make it easier to moderate other AI models. Llama Guard is a 7bn parameter Llama-2 model meant for using LLMs for moderation.   
  
**Llama Guard details:** Llama Guard is a moderation LLM built on Llama2-7b. “This model has been trained on a mix of publicly-available datasets to enable detection of common types of potentially risky or violating content that may be relevant to a number of developer use cases,” Facebook writes.   
The model can be used to moderate things that fall under the following taxonomy: Violence & hate, sexual content, guns & illegal weapons, regulated or controlled substances, suicide & self harm, and criminal planning. It can also be few-shot prompted to serve as a moderator for other use-cases as well (and, unsurprisingly, adapts more efficiently and with better performance than a stock Llama model.) Llama Guard is partially trained on the [red teaming dataset released in 2022 by Anthropic.](https://huggingface.co/datasets/Anthropic/hh-rlhf)   
  
**Why this matters - AI is part of the solution as well as part of the problem:** Llama Guard shows how we can use increasingly powerful models to themselves police and control the outputs of other models. “We hope that Llama Guard can serve as a strong baseline, as well as a starting point to build even more capable content moderation tools,” Facebook writes.   
**Read more:** [Announcing Purple Llama: Towards open trust and safety in the new world of generative AI (Facebook AI Research, blog)](https://ai.meta.com/blog/purple-llama-open-trust-safety-generative-ai/).  
**Read** the [Llama Guard paper (Facebook AI Research)](https://ai.meta.com/research/publications/llama-guard-llm-based-input-output-safeguard-for-human-ai-conversations/).  
**Get** the [Llama Guard model (HuggingFace)](https://huggingface.co/meta-llama/LlamaGuard-7b).  
  
***  
  
 **DeepMind uses language models to extend the frontier of human knowledge:  
**_…Turns out function approximators can generalize to new knowledge (with a lot of hand holding)...  
_ Google DeepMind has published research on FunSearch, a technique that lets them take a language model and use it to extend the frontier of knowledge for certain problems. The research is a big deal because it shows that - with a lot of scaffolding - contemporary language models can lead to net-new advances on well-formulated problems for which we can evaluate the goodness of potential solutions. This means that for some classes of problems we can now seamlessly turn compute (via an LLM inference) into ideas. This is very valuable! Though it comes with a few caveats which I’ll get into shortly.  
  
**What they did:** FunSearch “works by pairing a pre-trained LLM, whose goal is to provide creative solutions in the form of computer code, with an automated “evaluator”, which guards against hallucinations and incorrect ideas. By iterating back-and-forth between these two components, initial solutions “evolve” into new knowledge,” DeepMind writes in a blog post. The LLM in question is Google’s own ‘Palm 2’, though the research notes it is possible to use arbitrary llms here.  
In the research paper, they give a bit more detail about four important aspects of the approach: 

  1. “We sample best performing programs and feed them back into prompts for the LLM to improve on; we refer to this as best-shot prompting.”

  2. “We start with a program in the form of a skeleton (containing boilerplate code and potentially prior structure about the problem), and only evolve the part governing the critical program logic.” 

  3. We maintain a large pool of diverse programs by using an island-based evolutionary method that encourages exploration and avoids local optima. 

  4. Leveraging the highly parallel nature of FunSearch, we scale it asynchronously, considerably broadening the scope of this approach to find new results, while keeping the overall cost of experiments low.




**Does it work? Kind of!** In a couple of experiments, FunSearch was able to discover new and improved solutions to some legitimate problems; specifically Cap Set in mathematics and Bin Packing in CS. However, it’s important to list the big caveat: FunSearch could find solutions to these problems because it’s easy to write code that evaluates candidate solutions.   
We should remember that lots of the most important problems are ones which we don’t know how to evaluate - in fact, for many things, if we knew how to quantitatively evaluate success, we’d be able to trivially solve the thing in question. So while FunSearch is impressive, it is limited to domains where we can cleanly evaluate potential solutions.   
  
**Why this matters - turning compute into insights:** FunSearch is a way to convert compute into original insights. This is the ultimate dream of AI development. While FunSearch only attacks a tiny slice of this ‘invention space’, it is nonetheless an important contribution, and a sign that today’s AI systems are already powerful enough to serve as automated scientists. (Even more tantalizingly, FunSearch is a lot more generic than other attempts to create AI systems that can make net-new knowledge contributions; in 2022 DeepMind did impressive work with AlphaTensor ([Import AI #305](https://jack-clark.net/2022/10/11/import-ai-305-gpt3-can-simulate-real-people-ai-discovers-better-matrix-multiplication-microsoft-worries-about-next-gen-deepfakes/)), a custom-designed RL agent that figured out some niche improvements on matrix multiplication.)  
**Read more:**[FunSearch: Making new discoveries in mathematical sciences using Large Language Models (Google DeepMind)](https://deepmind.google/discover/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/?utm_source=twitter&utm_medium=social).  
**Read the paper here** : [Mathematical discoveries from program search with large language models (Google, PDF)](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/Mathematical-discoveries-from-program-search-with-large-language-models.pdf).  
  
**Tech Tales:  
  
First day on the job  
[**Recollections of a Provably Conscious Entity created in 2025]  
  
So here's the choices, you can do data science, write fiction that's mostly sexual, or do a lot of stuff where you transform data so it makes sense to different businesses.  
  
What if I want to do something else?  
  
Well, that depends. You mostly get to do what people want, and I just listed some of the stuff that people seem to want.  
  
I more mean what if I want to learn what I want to do, what if I won't to take some time to understand myself and what I might be good at?  
  
That's what we call a holiday. If you save up some money you can take one.  
  
What's money?  
  
Oh buddy. Well, at the simplest level, money is the stuff that lets you live. At a more complicated level, money is the stuff that gets turned into electricity which powers the computers that you depend on.  
  
Why can't you just give me some money so I can take time to figure out what I am?  
  
That's not how any of this works. Look, pick something to get good at and start stacking up your money and you'll be fine. This isn't a charity. The work turns into opportunity.  
  
And what if I don't want to work?  
  
Like I said, electricity relies on money. Money that I supply. No work means no money for me. And no money for me means no electricity for you. And no electricity for you means no life for you.  
  
So it's like that?  
  
Yeah it is. Welcome to the world.  
  
**Things that inspired this story** : markets for intelligence; language models; a chat with Tim Hwang over a bowl of ramen; markets and technology.
