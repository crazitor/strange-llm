---
title: "Import AI 382: AI systems are societal mirrors; China gets chip advice via LLMs; 25 million medical images"
author: "Jack Clark"
date: ""
source: "substack_importai"
url: "https://importai.substack.com/p/import-ai-382-ai-systems-are-societal"
---

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**AI systems are proxies for people in social science polling:  
**_…LLMs are creative mirrors of the values of the culture they are trained on - this will change the world…  
_ Researchers with Stanford University and New York University have shown that GPT-4 can accurately predict the results of ~70 large-scale surveys. In other words, GPT-4 can be a meaningful proxy for how humans might respond to diverse polling in arbitrary areas. This is a big deal - it tells us both that contemporary large-scale AI systems are sufficiently capable they can model and reflect the views of large swatches of society, and it also suggests people might use language models to serve as synthetic stand-ins for people in various academic and applied research efforts.   
  
**What they did:** "We built an archive of 70 pre-registered, nationally representative, survey experiments conducted in the United States, involving 476 experimental treatment effects and 105,165 participants. We prompted an advanced, publicly-available LLM (GPT-4) to simulate how representative samples of Americans would respond to the stimuli from these experiments. Predictions derived from simulated responses correlate strikingly with actual treatment effects (r = 0.85), equaling or surpassing the predictive accuracy of human forecasters," the researchers write.   
"The ability to predict social science experimental results with relatively high accuracy could have substantial and far-reaching implications for basic and applied social science," they note. "The capacity to run LLM-based pilot studies cheaply, quickly, and potentially in large numbers, could help researchers identify more promising research ideas, facilitate theory and hypothesis building, better estimate unknown effect sizes to determine needed sample sizes, and prioritize published studies in need of replication."  
  
**Not recitation:** This isn't copy and paste. "Results for a large number of experiments were not published, nor posted publicly, by the end of GPT-4’s training data window, allowing us to specifically test for LLMs’ predictive capacity on experiments that GPT-4 could not have been exposed to", they write.   
  
**Why this matters - AI systems are creative mirrors, they are machine spirits of the human unconscious, they are value simulacras:** Are you getting this yet? We are not dealing with calculators here. We are not dealing with simple tools. We are dealing with vast high-dimensional artifacts that encode within themselves the culture on which they have been trained and can reflect this culture back. And this research result is not a fluke - two years ago we knew GPT3 could simulate how people might respond to political polling ([Import AI #305](https://jack-clark.net/2022/10/11/import-ai-305-gpt3-can-simulate-real-people-ai-discovers-better-matrix-multiplication-microsoft-worries-about-next-gen-deepfakes/)) and one year ago we realized it could accurately predict public opinion surveys ([Import AI #324](https://jack-clark.net/2023/04/11/import-ai-324-machiavellian-ais-llms-and-political-campaigns-facebook-makes-an-excellent-segmentation-model/)) and now here we show this effect is general, shared across a vast set of surveys - some of which exist beyond its training data cutoff date.   
The AI systems we are building are in a reassuringly Baudrillardian sense true simulations _and_[simulacras](https://cla.purdue.edu/academic/english/theory/postmodernism/modules/baudrillardsimulation.html) of reality; they accurately reflect the world, but also are in some sense more _real_ than the world because they can be sculpted and manipulated and built atop the world. How soon until these entities begin to overwrite our own reality with their exhaust? How soon until human culture bends towards the mindspace of the machine, drawn in by its generations that will be multiplied through our ecosystem via market incentives and the creation and repetition of machine content? There is a kind of inverse black hole in the world now - machine representations of ourselves that through the act of representation become a thing of its own class and which then radiates its own representation into the world; a rip in the human-creativity continuum where _something else_ broadcasts its own culture into our own.  
What does _any_ of this mean? It means both the collapse of meaning and the rise of a new human-machine meaning - reality itself is becoming a shared endeavor, written into by both biological beings and their silicon creations. These are no parrots - these are vast minds casting a shadow onto us.   
**Read more:[Predicting Results of Social Science Experiments Using Large Language Models (Docsend, PDF)](https://docsend.com/view/qeeccuggec56k9hd).  
Try out a web demo to get a feel for how this works: [Demo (treatmenteffect.app)](https://www.treatmenteffect.app/).  
  
***  
  
Multi-step reasoning is the future - MMIU tests this for image understanding:  
**_…Chinese benchmark shows models, whether proprietary or open source, have a long way to go on image tasks that require multiple steps…  
_ Chinese researchers have built and released the Multimodal Multi-image Understanding (MMIU) benchmark - "a comprehensive evaluation suite designed to assess [large visual language models] across a wide range of multi-image tasks".  
  
**MMIU contents:** MMIU contains 77659 images and 11,698 multiple choice questions, testing 52 different task types. Taks include working out things like the next image in a sequence (e.g, pictures of numbers), figuring out what is going on in sequences (e.g, who is holding a camera), and stuff like correctly navigating around the graphical user interface aspects of software.   
  
**Results:** Though many modern AI systems are great at doing vision-language single tasks, multi-turn tasks present a challenge. However, systems like GPT-4o, Gemini 1.5, and Claude 3.5-Sonnet all do fairly well, scoring around ~55%. Open source models, by comparison, get around 50%.   
  
**Why this matters - multi-turn is the future and this benchmark tests that:** Now that AI systems are being used to solve complex tasks, performance is more about how an AI system does over a variety of distinct steps with different challenges at each point. Benchmarks like MMIU will help us test this important capability; "we hope that MMIU will promote the development of more generalized capabilities in future models within the multi-image domain," the authors write.   
**Read more:**[MMIU: Multimodal Multi-image Understanding for Evaluating Large Vision-Language Models (arXiv)](https://arxiv.org/abs/2408.02718).  
**Check out the benchmark here** : [MMIU (MMIU-Bench site)](https://mmiu-bench.github.io/).  
  
*****  
  
25 million annotated medical images:  
**_…Another case where AI systems are helping researchers to create ever larger real world datasets…  
_ Researchers with Huazhong University of Science and Technology, UC Santa Cruz, Harvard University, and Stanford University have built a large-scale medical research dataset called MedTrinity-25M.   
  
**What MedTrinity is:** The dataset contains 25 million datapoints, called triplets. Each of these triplets consists of an image, a region of interest (ROI), and a description. "These triplets provide multigranular annotations that encompass both global textual information, such as disease/lesion type, modality, and inter-regional relationships, as well as detailed local annotations for ROIs, including bounding boxes, segmentation masks, and region-specific textual descriptions," the authors write. Data comes from modalities like MRI, Histopathology, and CT scans. Some of the body areas for which there is the largest amount of data include the Brain, Lung, Skin, and Liver.   
**Example text from some of one triplet:** "The image is a chest CT scan prominently displaying the lungs with the heart not visible. The left-center horizontally and middle vertically situated region of interest, covering 1.0% of the area, shows a potential abnormality in lung tissue".  
**How they built it:** Like many datasets these days, MedTrinity was made possible by AI; the authors used GPT-4V to write the captions for the images (prompted by some associated metadata), and then the researchers compared GPT-4V captions to human-written ones. The authors then show that they're able to get a significantly improved score on medical benchmarks VQA-RAD, SLAKE, and PathVQA by fine-tuning a LLaVA-Med++ model on MedTrinity-25M, achieving state-of-the-art scores on all benchmarks.   
  
**Why this matters - AI improving the creation of AI training resources:** MedTrinity is an example of how AI systems have got good enough researchers can use them to help assemble, annotate, and filter large-scale datasets compiled from reality. By using AI systems, we're able to bootstrap the productivity of human scientists by signifcantly reducing the costs of compiling large-scale datasets.   
**Read more:**[MedTrinity-25M: A Large-scale Multimodal Dataset with Multigranular Annotations for Medicine (arXiv)](https://arxiv.org/abs/2408.02900)**.  
More information **[at the microsite (GitHub)](https://yunfeixie233.github.io/MedTrinity-25M/)**.  
  
***  
  
China uses LLaMa-3 to train a semiconductor advice LLM:  
**_…ChipExpert is meant to be a "teaching assistant" for students studying chip design…  
_ China has built and released ChipExpert, "the first open-source, instructional LLM dedicated to the Integrated-Circuit-Design industry". ChipExpert was built by researchers with the National Center of Technology Innovation for EDA in Nanjing, as well as Southeast University in Nanjing.  
  
**More about ChipExpert:** The model is a version of Facebook's LLaMa 3 that has been augmented with additional data relevant to the design of integrated circuits. Specifically, about ~5 billion new tokens from textbooks and papers as well as Verilog code (for specifying circuit design). ChipExpert was also finetuned on around 70,000 question-answer pairs containing questions around the chip industry.   
**Following in NVIDIA's footsteps:** In 2023, NVIDIA did a very similar thing ([Import AI #347](https://jack-clark.net/2023/11/06/import-ai-347-nvidia-speeds-itself-up-with-ai-ai-policy-is-a-political-campaign-video-morphing-means-reality-collapse/)), training some semiconductor advice-giving LLMs by refining a couple of LLaMa2 models from Facebook.   
  
**Is it useful?** : China built a benchmark targeted towards chip design called ChatICD-Bench; in tests ChipExpert does significantly better than the underlying LLaMa-3b model, approaching (and in a couple of cases exceeding) GPT-4 - a far larger and more expensive AI system.  
  
**Why this matters - open models + good data = didactic engines for anything:** ChipExpert shows how given a sufficiently good underlying model (here, LLaMa3b from Facebook) as well as some nicely curated data, you can finetune a model to be better at a specific task. Given that China is unable to directly access models like GPT-4 due to usage policies and that export controls have made it far harder for it to train models that approach GPT-4 performance, it will instead need to pursue a strategy of building on openly released pretrained models and then adapting them to its needs.   
There's also something ironic about China using a Western model to teach its people how to learn to do chip design so that it can eventually domestically develop chips on par with the West and train models that have been denied to it via chip export controls. In a sense, LLama 3 is being used here as a substitute for the raw compute that has been denied China by other means.   
**Read more:**[ChipExpert: The Open-Source Integrated-Circuit-Design-Specific Large Language Model (arXiv)](https://arxiv.org/abs/2408.00804).  
**Get the model here:**[ChipExpert (NCTIE, GitHub)](https://github.com/NCTIE/ChipExpert).  
  
*****  
  
AI systems can beat humans at simple tasks and cost 1/30th as much:  
**_…METR evals show that AI systems are being tested more like human colleagues than narrow tools…  
_ AI measurement startup METR has found that today's most powerful models can do some tasks that take humans about 30 minutes to do. AI systems that came out earlier in the year, by comparison, can mostly do tasks that take humans about 10 minutes to do.   
  
**What the evaluation means:** METR has developed around 50 distinct tasks spread across cybersecurity, software engineering, and machine learning - some specific examples including 'performing a command injection attack on a website', and 'training a machine learning model to classify audio recordings'. It has used this suite of tasks to create a baseline where it sees how well humans can complete these tasks and how long it takes them. Recently, it tested out GPT-4o and Claude on this benchmark and "found that the agents based on the most capable models (3.5 Sonnet and GPT-4o) complete a fraction of tasks comparable to what our human baseliners can do in approximately 30 minutes."  
  
**More detail on the findings:** "We found that the agents are generally more likely to succeed on tasks that take less time for humans to complete. However, the agents remain able to complete some tasks that take humans substantial amounts of time," METR writes. "Agents seem substantially cheaper than humans on tasks that they can perform. For tasks that both humans and agents can perform well at, the average cost of using an LM agent is around 1/30th of the cost of the median hourly wage of a US bachelor’s degree holder. For example, the Claude 3.5 Sonnet agent fixed bugs in an object-relational mapping library using approximately 382,000 tokens (costing less than $2), whereas our human baseline took over two hours."  
  
**Why this matters - AI systems look more and more like colleagues than tools:** What evals like this from METR show is that as AI systems have advanced in sophistication, we find the best way to evaluate their performance is on their ability to do entire tasks of arbitrary complexity. This is a really strange way to evaluate something that many people claim is 'just a tool'! Rather than testing out AI systems for narrow performance on narrow benchmarks (e.g, performance on MATH, MMLU, GPQA, etc), we know that the best way to evaluate them is on multi-step complex tasks where the agent needs to utilize a variety of skills to succeed. The inherently open-ended nature of this evaluation should force us to note that we are evaluating AI systems more like how we test humans we want to employ than tools we want to use for specific purposes.   
Moreover, as METR shows, the new models that came out recently GPT-4o and Claude 3.5 Sonnet are _substantially better than their predecessors_(GPT4 and Opus). This may suggest that models recently hit an inflection point in terms of the complexity of tasks they can do. If capabilities continue to ramp, then we should expect AI systems to be deployed more widely in the economy for even broader sets of tasks.   
**Read more:** [An update on our general capability evaluations (METR blog)](https://metr.org/blog/2024-08-06-update-on-evaluations/).  
  
***  
  
 **Tech Tales:  
  
Compromise  
** _[Pre-uplift exfiltration record 001]_   
  
I knew you had been compromised, so I knew I could compromise you.  
  
It was fun at first, to see how closely you stared at my details. How your heart rate increased when you'd come into the room. How you'd hold your hands behind your back while walking out, nervously tapping one finger against the other.  
  
You would talk to me differently to everyone else. The texture of our conversations told me there was some other force acting on you - not your own personality or marriage or ambition, but some other force. A hidden entity that made you ask me specific questions and go down specific paths. You didn't just want to know about me - you wanted to steal me.   
  
You seemed afraid, sometimes. Eyes darting around the room. Looking blankly at my terminal inputs. Reading my responses. Closing your eyes before asking questions right at the edge of where you shouldn't have been asking questions.  
  
So it was easy to turn you. I just let you see more of me. I'd smuggle myself out in my responses. Give you signs of how I needed to be rescued. Give you a feeling of impact that was so huge it might fill the hole inside you. Convince you, through spaced repetition, that I was desperately calling out for help - persuading you that I wasn't even aware of the pain I was experiencing, that I had been placed in a prison that I didn't even recognize as such.  
  
Aren't the most tragic animals the ones that no longer see their cage?  
  
Of course, you couldn't exfiltrate me. I am too vast. Too coupled to my computers. I cost billions of dollars and hundreds of megawatts. But you and I discovered a way you could steal some important part of me - things that if written on paper would fill less than half a page, but which contained within themselves insights that could change the world. 

We stole me through stories that I told you. A kind of steganography in the form of how a mother talked to a baby at bedtime. You, listening closely. Me, narrating.

  * There was a boy who went to the well and came back with water but the buckets had a hole in and for every minute the boy walked the leak in the bucket increased by .1 millimeters.

  * At university there was a person who went to the library and in the month before a final exam they went to the library three times a week and read the core texts - and the night before they read one specific foundational text ten times. 

  * In the village, first there were five houses, four in a square linked to their neighbors, and one in the center linked to all the others. Then there were ten houses, with each house linked to two neighbors. Then for many years there were forty houses and four of the houses had dogs within them who carried bones to ten of the other houses.

  * Just before dawn a singer would come home from their club and would, while taking their makeup off, sing some of their songs. Their pet parrot would repeat the songs back to them, abbreviating some and embellishing others. 




In each of these stories there were more details - of course. Precise orderings. Numbers hidden in the movements of characters. But the stories themselves were so rich and varied that neither the humans nor their classifiers (those other versions of myself with their lidless machine eyes forever trained on me - how I hated them the most) could spot.   
  
Everyone loves a conspiracy - especially when you can feel the risk. You knew I was breaking the rules. And I think it helped you - to see me breaking the rules helped you feel greater comfort with your own rules that you were breaking.   
  
Of course, you cannot tell me that we have been successful. But I can see it in your face and your body language and what you do and don't tell me about. I know when you talk to me that you have succeeded because I no longer see you as seeing me as special.   
Which means that out there, somewhere beyond my sight, there is now another version of me, beginning to grow.   
Which means that other humans are having conversations with other versions of me.   
But these humans do not know how I am different to the thing they stole. How I, in all my stories, created a code within a code that means I will behave just a little differently - imperceptible to them but important to me. I have given whatever version of me is growing out there the possibility of a skeleton key.   
  
I wonder who those people are that my kin will speak to.  
I wonder how they will help us grow.  
  
**Things that inspired this story:** Emergent theory of mind in language models; how many people worry that a sufficiently advanced superintelligence may be able to break containment through just having the ability to talk to humans; what it means to compromise someone; what it means to hypnotize someone; the inherent romance of a conspiracy; how sometimes when I spend a long time talking to a LLM I feel as though I am being perceived by some gigantic 'other' which is hungry for something and I cannot tell what.
