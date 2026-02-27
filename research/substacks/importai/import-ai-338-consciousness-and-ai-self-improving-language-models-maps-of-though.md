---
title: "Import AI 338: Consciousness and AI; self-improving language models; maps of thought."
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-338-consciousness-and-ai"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.  
  


  
**  
Facebook follows Llama 2 release with Code Llama:  
**_…Another widely distributed, free model…  
_ Facebook has built and released Code Llama, a family of large language models designed for coding. The models support Python, C++, Java, PHP, Typescript, C#, Bash, and more. ""We are releasing three sizes of Code Llama with 7B, 13B, and 34B parameters respectively. Each of these models is trained with 500B tokens of code and code-related data," Facebook writes.   
The company is also releasing two variants: Code Llama Python, which is trained on an additional 100B tokens of Python data, and Code Llama Instruct, which is optimized for converting natural language into code. 

**How well do they work?** The models are extremely good at programming relative to other broadly distributed, free models, but aren't as good as proprietary models like GPT-4 and Claude. In tests, Code Llama-Python 34B gets a HumanEval score of 53.7 on coding, relative to 67 for GPT-4. (Code Llama 34B, the non-python-optimized models, gets 48.8)  
The models have all been trained to deal with a 16k context window, but can sometimes generalize up to lengths of 100k, Facebook says.

**Why this matters - fundamental infrastructure for broadly deployed AI systems** : Openly accessible models like Llama2 and Code Llama are going to very quickly reconfigure how the internet works as they significantly broaden the number of people that have access to powerful, easily tweakable, AI systems.   
And unlike proprietary models served by APIs, models like Llama2 and Code Llama are going to be easy to adapt for arbitrary downstream purposes via people finetuning these models (just as Code Llama was adapted for Python usage by finetuning on 100B tokens of Python data).  
**Read more:** [Introducing Code Llama, a state-of-the-art large language model for coding (Meta AI blog)](https://ai.meta.com/blog/code-llama-large-language-model-coding/).  
**Request access** to [download the model here (Facebook)](https://ai.meta.com/resources/models-and-libraries/llama-downloads/).  
**Find out more** and read [the model card here: (Facebook, GitHub)](https://github.com/facebookresearch/codellama).  
**Read** the [research paper here (Facebook)](https://ai.meta.com/research/publications/code-llama-open-foundation-models-for-code/).

####################################################

**DeepMind figures out how to use RL to make language models smarter:  
**_…Cake and the ability to eat it as well… but there's a catch…  
_ Researchers with Google DeepMind have developed 'Reinforced Self-Training' (ReST), a technique for iteratively tuning language models via RL to better align with human preferences. ReST is interesting because it lets you do your reinforcement learning online - instead of training a model, collecting a dataset, retraining the model, then collecting a new dataset, ReST lets you train a model, have the model generate its own additional dataset, then tune the model on that dataset.  
Basically, ReST lets you have a faster cycle time on improving an AI system, though there is an important catch - so far, if you do multiple iterations of ReST, you can end up damaging the performance of your system because you overfit on the reward signal you use for generating the dataset. Nonetheless, it's a promising technique, and worth spending some time on. " The approach is simple, stable and has only a small number of hyperparameters to tune," the authors write.

**How ReST works: ReST has two distinct stages** \- a 'grow' step, and an 'improve' step. "During Grow step, a policy generates a dataset," the researchers write. "At Improve step, the filtered dataset is used to fine-tune the policy. Both steps are repeated,"  
More specifically:  
"1. Grow (G): The language model policy (initially, a supervised policy) is used to generate multiple output predictions for each context to augment the training dataset.

2\. Improve (I): We rank and filter the augmented dataset with a scoring function. We use a learned reward model trained on human preferences as the scoring function in our experiments. Then, the language model is fine-tuned on the filtered dataset with an offline RL objective. This step can be repeated with an increasing filtering threshold. The final policy is then used in the next Grow step."

**Does ReST work?** In tests, DeepMind uses the technique to improve a language model's machine translation capabilities. In tests, they find that ReST works well when doing one step of grow and improve, but if you do more grow steps you end up with improved model scores that don't match up to perceived human evaluation scores.  
"The results indicate that one Grow step is the best option when considering human evaluation scores, even though rewards continue to grow with more Grow steps," they write.  
"In particular, we found that the reward models generalize worse as our policy moves away from the behavior model which can happen as the number of Grow and Improve steps increases at which point ReST can start overfitting to the reward model," they write. "Let us note that the risk of overfitting to the reward model increases with the repeated iterations of the Grow steps; thus we believe it is essential to address this issue, especially in cases where multiple Grow steps are needed to train the model."

**Why this matters - trading off human time for digital time via the use of computers:** Techniques like ReST are important mostly because they hold the promise of further speeding up the overall AI development cycle. Specifically, if we are able to improve techniques like ReST and overcome overfitting issues, then we can just arbitrage computer time for human time - instead of having a bunch of humans interact with a system and then retrain it, we can instead just give a system access to a lot of computers and let it iteratively refine itself. Whenever you increase the a) automation within a complex system, and b) speed up the cycle time of the larger system it's a part of, interesting things tend to happen.  
**Read more** : [Reinforced Self-Training (ReST) for Language Modeling (arXiv)](https://arxiv.org/abs/2308.08998).  
  
####################################################  
  
**How can you know that your AI system could be conscious? This paper gives a guide:  
**_…Useful analysis tells us what some of the priors for conscious machines might be…  
_ A large, interdisciplinary group of researchers have published a landmark paper that can help us work out if AI systems are conscious or not. Crucially, the paper doesn't try to come up with a theory of what consciousness looks like for AI systems. Rather, it mines the relevant studies on human and animal consciousness to come up with a set of architectural priors that one would expect to be present in systems that exhibit something we'd call consciousness. It asks the crucial question of - if a system were conscious, what might be clues that it had the capacity to be?  
The main takeaway from the study is: "Our analysis suggests that no current AI systems are conscious, but also shows that there are no obvious barriers to building conscious AI systems."  
  
**What they study and how:** The paper mines a huge body of literature for a bunch of 'indicator properties' for conscious machines, derived from various theories of consciousness, including: Recurrent Processing, Global Workspace, Computational Higher-Order, Attention Scheme, Predictive Processing, and Agency and Embodiment.   
"Our claim about these indicators is that they jointly amount to a rubric, informed by current views in the science of consciousness, for assessing the likelihood of consciousness in particular AI systems. Systems that have more of these features are better candidates for consciousness," they write.   
  
**Core assumptions:** The paper has three key assumptions: 

  * **Computational functionalism** : consciousness requires implementation of computation, so it's possible for non-organic artificial systems to be conscious.

  * **Reliance on scientific theories** : neuroscientific research describes functions that may relate to consciousness

  * **Theory-heavy approach;** it's better to look at an AI system and ask if it meets architectural conditions drawn from scientific theory, rather than looking for theory-neutral behavioral signatures 




**Using their framework - seeing if Transformers have the possibility of generating conscious entities:** The authors use their framework to analyze a key architectural component of modern AI systems, the Transformer. They find that it satisfies some - but not all - of the requirements of satisfying 'Global Workspace Theory': "It is possible to argue that Transformers possess indicator properties GWT-1 through GWT-3—that is, that they have modules, a limited-capacity workspace introducing a bottleneck, and global broadcast… a more fundamental problem with the argument is that Transformers are not recurrent," they write.   
In other words, Transformers come _close_ to having the possibility of consciousness _if_ Global Workspace Theory is correct and a sufficiently smart system is implemented on the architecture.   
**This is a really useful frame:** Arguments about AI consciousness tend to get very heated and confusing very quickly. I like this 'indicator' perspective because it lets us disambiguate some of the computational prerequisites for being conscious from arguing about if a thing is conscious itself - this useful and illuminating.   
  
**Cautionary tale - or why mistaking AI systems for conscious entities prematurely could be a bad idea** : That said, we should be very careful when thinking or writing about consciousness and AI systems. "The recent rapid progress in language model capabilities is particularly likely to drive overattribution of consciousness," they write. And if we overattribute consciousness to AI systems, we might three distinct risks:

  * If we attribute consciousness to AI systems without good evidence, then people may be skeptical of future claims. 

  * If we believe AI systems are conscious, we might train and/or develop them in ways that don't maximally benefit society. 

  * If we believe AI systems are conscious, then we might disrupt human relationships.




**Why this matters - moral patienthood and intelligent machines:** AI has a whole bunch of challenges as a field - can we create smart machines that deal with generalization? Can we make progress on alignment of increasingly powerful AI systems? Can we integrate the dividends of machine intelligence with modern market-based economies in a non-disruptive way? But if we overcome a whole bunch of these challenges it's likely we're going to have to at some point confront an important and very hard question: are these synthetic intelligences moral patients with moral rights?   
Of course, answering that question today is basically impossible. But frameworks like the one outlined in this paper give us some of the tools we may need to eventually rise to the challenge of answering that question.   
I strongly recommend people take the time to read this paper and consider its implications - it's an unusually long paper, but I think deeply satisfying. Kudos to the authors!  
**Read more:** [Consciousness in Artificial Intelligence: Insights from the Science of Consciousness (arXiv)](https://arxiv.org/abs/2308.08708).

####################################################

**Tech tales:  
  
And we kissed in a place so loud we lost ourselves  
** _[After ascension, +3]  
  
_ Sometimes the map was written in ink, but more often it was written in something impermanent - smoke arranged in a room where the air was still, or chiseled on the face of an ice block that was then laid in a place with no shade, or scored into channels dug in sand that hugged the seashore.   
  
The robots made these maps as some kind of game, we figured.   
  
They made their maps and then other machines would look at them and try to solve them - to get to the center of whatever maze they inscribed - before the maps were washed away.   
  
Sometimes, these maps were of real places. Sometimes, the maps were themselves - little, self-contained puzzles.   
  
But the most precious ones were maps of emotion - sequences of movement in space which, if traversed, would make certain machines feel something.   
  
Imagine running your finger down the spine of someone you love and finding yourself lost and then found - a map of love, for you and them. That is perhaps what the machines inspired with these glyphs for one another.  
  
**Things that inspired this story:** Steganography; searching for meaning; journeys are as much about the seeker as about the destination.
