---
title: "Import AI 323: AI researcher warns about AI; BloombergGPT; and an open source Flamingo"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-323-ai-researcher-warns"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Bloomberg trains an LLM for finance:  
**_…Better models through proprietary data…  
_ Financial data behemoth Bloomberg has built 'BloombergGPT', a language model based in part on proprietary data from Bloomberg. BloombergGPT sketches out a future where companies pair large-scale internet-scraped datasets with proprietary datasets to create general-ish models that have some specific capability spikes. 

**What is BloombergGPT?** The model is "a 50 billion parameter language model trained on a wide range of financial data." They trained the model on 569 billion tokens, mixed between proprietary financial data (which they call the 'FinPILE'), as well as public data.   
"Our mixed dataset training leads to a model that outperforms existing models on financial tasks by significant margins without sacrificing performance on general LLM benchmarks"

**Compute** : "We use the Amazon SageMaker service provided by AWS to train and evaluate BloombergGPT," Bloomberg writes. "We use the latest version available at the time of training and train on a total of 64 p4d.24xlarge instances. Each p4d.24xlarge instance has 8 NVIDIA 40GB A100 GPUs with NVIDIA NVSwitch intra-node connections (600 GB/s) and NVIDIA GPUDirect using AWS Elastic Fabric Adapter (EFA) inter-node connections (400 Gb/s). This yields a total of 512 40GB A100 GPUs".  
(To put this compute in perspective, GPT-3 used 1.82X as much compute, and Eleuther's quite good GPT-NeoX used 0.33X as much.)   
It's pretty interesting to me to see SageMaker turn up here - I can't recall seeing it being used to train models as large as this. 

**Performance:** In tests, BloombergGPT, unsurprisingly, does quite well on a range of financial specific tasks and evaluations. It does especially well on sentiment analysis about specific stocks - which makes sense, given Bloomberg's proprietary data.   
Performance is a lot more mixed on 'BIG-Bench', where HuggingFace's 'BLOOM' model does substantially better than BloombergGPT.

**No model release because of proprietary data:** "As is well known, LLMs are susceptible to data leakage attacks and it is possible to extract significant segments of text given model weights Carlini et al," Bloomberg writes. "Moreover, even giving selective access to researchers isn’t a guarantee that the model cannot be leaked. Without strong privacy guarantees, we must be concerned that providing access to model weights entails giving access to FinPile. For this reason, we err on the side of caution and follow the practice of other LLM developers in not releasing our model."  
While it's easy to read the above as a cynical justification for non-release, I expect it's true - I worked at Bloomberg as a journalist for a couple of years and the company does take the security and confidentiality of its data and systems incredibly seriously.

**Why this matters - self-seeing organizations / living archives:** I think of BloombergGPT as more like a silicon librarian/historian than a model; by training it on a huge amount of private and internal Bloomberg data, the LLM is in effect a compressed form of 'institutional memory' and a navigator of Bloomberg's many internal systems (including the notorious Bloomberg terminal language). Systems like BloombergGPT will help companies create software entities that can help to navigate, classify, and analyze the company's own data stack.  
**Read more** : [BloombergGPT: A Large Language Model for Finance (arXiv)](https://arxiv.org/abs/2303.17564).

####################################################

**Accomplished AI researcher: Future AI systems will probably out-compete humans:  
**_…The banging is now coming from inside the house. Pay attention…  
_ Dan Hendrycks, an accomplished AI researcher, has written a paper claiming that "Natural Selection Favors AIs over Humans". The implications of the paper are both important and dire: "We argue that natural selection creates incentives for AI agents to act against human interests," he writes. 

**Dan Hendrycks is not a crank:** This is the kind of claim people want to reflexively shrug off as coming from some kind of wild-eyed crank who lives in a cabin in the woods. I want to rebut this upfront: Dan Hendrycks is not a crank, Hendrycks is a researcher whose work has been covered in Import AI multiple times - and tons of his research involves _evaluating_ AI systems - testing out how good they are at things like [coding](https://arxiv.org/abs/2105.09938), [verbal reasoning](https://arxiv.org/abs/2206.04615), [understanding of the law](https://arxiv.org/abs/2103.06268), and so on. He also is a co-inventor of [Gaussian Error Linear Units (GELU)](https://arxiv.org/abs/1606.08415).  
When an expert in not just AI research but in _evaluating AI systems_ writes a paper claiming that future AIs may act selfishly and not in line with human interests, we should pay attention!

**What the paper claims:** Hendrycks' paper states that "it seems likely that the most influential AI agents will be selfish. In other words, they will have no motivation to cooperate with humans, leading to a future driven by AIs with little interest in human values".

**Competition gets us unfriendly AIs:** A key aspect of Hendrycks' point is that humankind is likely to build a bunch of different, powerful AI systems (see the current LLM craze as an example of this). These LLMs will become increasingly agentic - e.g, they'll start to use tools and take multi-step sequences of actions. These AI systems are also competitive, either through economics or national priorities, and so are subject to the evolutionary pressures of competitive environments.   
"Competition not only incentivizes humans to relinquish control but also incentivizes AIs to develop selfish traits. Corporations and governments will adopt the most effective possible AI agents in order to beat their rivals, and those agents will tend to be deceptive, power-seeking, and follow weak moral constraints," Hendrycks writes. 

**This problem gets worse, not better:** As AI systems become more successful, we can expect the pace of AI development to increase as a consequence of a) the AI systems getting smarter, and b) more money getting dumped into the development environment. This means that we'll start to see AI systems being used to design successor AI systems (and this is already happening via things like AI developers using Copilot to write code).   
"This loss of human control over AIs’ actions will mean that we also lose control over the drives of the next generation of AI agents. If AIs run efforts that develop new AIs, humans will have less influence over how AIs behave. Unlike the creation and development of fully functional adult humans, which takes decades, AIs could develop and deploy new generations in an arbitrarily short amount of time."

**Less safe models are already the norm:** This also combines with the fact that, already, the human economy is selecting for AI systems that are not very safe - for instance, the 'Deep Blue' chess computer was partially a symbolic system and therefore interpretable via its rulesets. Deep learning systems are, correspondingly, not easy to interpret. "Over the history of AI development, the fittest models have had fewer and fewer safety properties," Hendrycks writes. 

**Why this matters - the scientists are trying to warn us:** Each week, more and more AI researchers are expressing concern about the state of AI development. In the last year, though, there has been a dramatic rise in the number of scientists expressing concern about humankind being harmed en mass by the development and deployment of AI. Here, Hendrycks isn't warning about specific harms of deployed AI systems (e.g, fairness issues, or cultural magnification/minimization issues), he is literally warning us about a likely future where AI systems utterly dominate humanity and care about us just as much as the average human cares about cockroaches.   
This is an easy argument to scoff at or make fun of, of course. But sit with it for a moment and view it from a position of generous empathy - why is Hendrycks, a scientist who mostly spends their time building and evaluating AI systems, taking time to write a very long paper that people will make fun of which warns us about grave danger? The occam's razor principle says the simplest answer is that Hendrycks is afraid.   
**Read more:**[Natural Selection Favors AIs over Humans (arXiv)](https://arxiv.org/abs/2303.16200).

####################################################

**TikTok data center slurps up local electricity, leaving none for ammunition maker:  
**_…Social media + AI: 1. Bullets: 0…  
_ Weapons manufacturer Nammo says it can't expand one of its main factories because a data center from TikTok is using up all the spare power in the area, according to _The Financial Times_.   
"Elvia, the local energy company, confirmed that the electricity network had no spare capacity after promising it to the data center as it allocates on a first come, first served basis," the FT wrote. 

**Why this matters:** TikTok is the first social media company that is driven by AI - the company uses a far more sophisticated ML recommendation system than those of other social networks and this has helped drive its massive growth in recent years. That ML system has to be computed somewhere. Stories like this are a taste of things to come, as data centers supporting great money-printing machine minds compete with other big industries for electricity.   
This also feels like a short story I might write in this very newsletter. Reality; stranger than fiction, sometimes!   
**Read more:** [European ammunition maker says plant expansion hit by energy-guzzling TikTok site (Financial Times)](https://www.ft.com/content/f85aa254-d453-4542-a50e-fa1171971ab0?accessToken=zwAAAYc-EGaDkdP4WqJU1FNFQtOlDvoRcZcasA.MEUCIQD3nVgiOKr8SocpYu23GXFR9dnqVT5qFc-ifS95rO1F4AIgFk5_u91J4_m4DBivnZJDZJWMGAWm6B0sSR6bXdTicPk&sharetype=gift&token=2c7e6c44-542c-4e5f-9407-e666a27b7b77). 

####################################################

**Open source collective clones DeepMind's 'Flamingo' model and releases it:  
**_…The replications will continue until large companies start shipping or cease publishing...  
_ Here's a fun pattern that has started to appear in the wild west of AI development: a large company announces some research into AI and demonstrates a system based on the research, then a small company or open source collective makes and releases the system - before the originating AI company!   
We've seen that pattern play out a bunch recently - Facebook published research on Toolformer, then OpenAI added tool-using capabilities to chatGPT; Runway released StableDiffusion, then Stability.ai productonized it; and now there's 'OpenFlamingo', an open re-implementation of DeepMind's private 'Flamingo' model. 

**What is Flamingo:** Flamingo ([Import AI 293](https://jack-clark.net/2022/05/02/import-ai-293-generative-humans-few-shot-learning-comes-for-vision-text-models-and-another-new-ai-startup-is-born/)) is a multi-modal vision-language model developed by DeepMind, which lets people converse with an AI, and the AI can also analyze images people upload to it. 

**What is OpenFlamingo:** OpenFlamingo is a few things; a Python framework for training Flamingo-style models; a large-scale dataset with interleaved image and text sequences (75M documents encompassing 400M images and 38B tokens); lan in-context learning evaluation benchmark for vision-language tasks; and an open source 'OpenFlamingo-9B' model based on Facebook's lab leak LLaMA model.   
How good is the model? In tests, the OpenFlamingo model is a little less good than the equivalently sized private model from DeepMind. "This model is still a work in progress but it can already bring a lot of value to the community," the researchers write. 

**Things that make you go 'hmmm':** It's notable that OpenFlamingo is made possible by LLaMA,a model that Facebook half-released and which subsequently leaked onto torrent networks.   
**Read more** : [ANNOUNCING OPENFLAMINGO: AN OPEN-SOURCE FRAMEWORK FOR TRAINING VISION-LANGUAGE MODELS WITH IN-CONTEXT LEARNING (LAION)](https://laion.ai/blog/open-flamingo/). 

####################################################

**Chipmaker releases a family of decent GPT-3 models:  
**_…Cerebras studies the scaling laws…  
_ AI chipmaking company Cerebras has released a family of seven GPT-3 models, ranging in size from 111 million to 13 billion parameters. These models are trained on ~4X the amount of data the original GPT-3 model was trained on, utilizing the 'Chinchilla' insight from DeepMind that language models can be trained on a lot more data to yield better performance. "Cerebras-GPT has faster training times, lower training costs, and consumes less energy than any publicly available model to date," Cerebras writes. "All models, weights, and checkpoints are available on Hugging Face and GitHub under the Apache 2.0 license."

**Performance:** The Cerebras models approach the performance of Pythia, a family of GPT-style models released by open source collective Eleuther AI. "Designed to be complimentary to Pythia, Cerebras-GPT was designed to cover a wide range of model sizes using the same public Pile dataset," Cerebras writes. In tests on 8 downstream language tasks, the Cerebras models set a new state of the art (for equivalent model size) on 5 tasks, with Pythia and Facebook's OPT models winning the others. 

**Why this matters - replications as marketing and lead generation:** As AI has become a technology of significant economic impact, companies are starting to clone proprietary models and release them mostly to serve as marketing devices. Here, the Cerebras models are partially serving as an advertorial for Cerebras's own AI training chips (they were trained on them). This dynamic is an interesting one - we can expect significant benefits to accrue to the open source community as a consequence of commercial competition, though if it turns out there are safety issues with these models, the safety issues will be compounded via open source release and dissemination.  
**Read more:** [Cerebras-GPT: A Family of Open, Compute-efficient, Large Language Models (Cerebras blog)](https://www.cerebras.net/blog/cerebras-gpt-a-family-of-open-compute-efficient-large-language-models/).  
**Get the models here:**[Cerebras Model Zoo (GitHub)](https://github.com/Cerebras/modelzoo).

####################################################

**Tech Tales:**

**Some monsters are too dangerous to hunt**

 _**[** An interview with someone who lived through the great calamity. Interview took place +10 P.C.E. (years from the first Provably Conscious Entity)]._

Back in the early 2000s there was a financial crash that was caused by some clever financial engineering related to the mortgages on houses. The crash happened because people figured out a financial technology to help them trade mortgages in a more intricate way that also changed how you measured the risk profile of mortages. Eventually, the trades got so complicated and the leverage so huge that the markets all toppled over and plunged the Western world into a period of stagnation.

There are all kinds of apocryphal stories of that time, and one of the ones that occurs frequently goes like this:

  * The financial institution was making money from the mortgage technologies. 

  * The risk department of the financial institution had an intuition that something was wrong, but didn't know how to measure it. 

  * When people did measure the risk, their financial institutions mostly didn't believe them because the analysis was so dire and the implications so extreme. 

  * "it is difficult to get a man to understand something when his salary depends upon his not understanding it," as the old author Upton Sinclair is claimed to have said.




The same kind of problem showed up in the ascendancy, right before the first Provably Conscious Entity. Specifically, people figured out new ways to make increasingly capable AI systems, but the technology was so new that they lacked the tools to properly measure and evaluate them.   
This meant people would poke and prod and diagnose their systems and wind up with some uneasy sense of fear. The systems were becoming much more capable, but also had increasingly strange and inscrutable qualities.   
Sometimes, when you tried to break the systems, they would start singing to themselves.   
Over times when you asked them to perform a task they'd carry it out and improvise some parts that didn't seem necessary to the completion.   
When you asked them to diagnose their own problems, the AI systems would generate stories about their behavior which were a) hard to understand and b) as techniques relating to interpretability advanced, seemed increasingly fictitious - the real reasons for their behavior seemed different and they were making up stories for their human audience. 

The issue - and what caused the calamity - was that the strange behavior, though unnerving, couldn't be tied to a direct form of harm. So the people who were tasked with finding some of the scary behaviors had to explain their fears through hypotheticals and forward-facing stories, which were easy to ignore. 

**Things that inspired this story:** Red teaming AI systems; mechanistic interpretability. 
