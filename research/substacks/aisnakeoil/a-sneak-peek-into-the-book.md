---
title: "A sneak peek into the book"
author: "Arvind Narayanan & Sayash Kapoor"
date: ""
source: "substack_aisnakeoil"
url: "https://www.normaltech.ai/p/a-sneak-peak-into-the-book"
---

In April 2022, many images like this one went viral. What was special about it was that it was generated using a text-to-image AI system called _DALL-E 2_ , using just a one-line description: “A photo of an astronaut riding a horse”.

[](https://substackcdn.com/image/fetch/$s_!CxPn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F70a3e8c5-aab4-4ab4-92a8-ef93a2deee43_2164x2170.png)_(via[OpenAI](https://twitter.com/OpenAI/status/1511714545529614338/photo/1))_

Tools such as _DALL-E 2_ and Google’s _[Imagen](https://imagen.research.google/)_ have made stunning improvements in creating realistic-looking images based on one-line prompts.

In May 2016, ProPublica published a shocking report showing that _COMPAS_ , a tool used to predict whether a defendant would commit a crime if released before trial, was twice as likely to falsely accuse a Black defendant compared to a white one. 

[](https://substackcdn.com/image/fetch/$s_!WzAt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F15192616-4254-409e-b6bb-6c68d66ea4d6_1072x664.png) _(via[VICE](https://www.vice.com/en/article/paqwmv/bail-algorithms-compas-recidivism-are-as-accurate-as-people-doing-online-survey))_

More worryingly, researchers [found](https://www.science.org/doi/10.1126/sciadv.aao5580) that _COMPAS_ , which used hundreds of data points about a person to make a decision, was not very effective at predicting the future at all—it was as good as leaving the decisions up to people with no background in criminal justice. In fact, _COMPAS_ was no better than using just two pieces of information to predict if someone would commit a crime: their age and the number of prior offenses!

Both _DALL-E 2_ and _COMPAS_ work by learning patterns from data, and can be thought of as AI. **Why is AI so good at creating images from text, and yet so bad at predicting who will commit a crime?**

AI is an umbrella term. Today, it is used to refer to a large number of related but different applications. Some of them have made massive progress, such as _DALL-E 2._ Others, such as _COMPAS_ , do not work—and perhaps never will. So how can we understand which AI systems can work and which ones cannot? 

That’s where our book comes in. We explore what makes AI click, what makes certain problems resistant to AI, and how to tell the difference. AI is everywhere today, so this is essential knowledge if you ever make decisions about AI-powered products or services, whether at work or in your personal life. It is also essential for policymakers, journalists, and many others.

### **How AI has gotten so good in some areas**

Our phones have apps that can [instantly recognize](https://en.wikipedia.org/wiki/Shazam_\(application\)) which song is playing in the background or transcribe our speech fairly accurately. Machines have [trounced](https://en.wikipedia.org/wiki/AlphaGo) the world champion at games such as Go. None of these was possible a decade or two ago. What do these applications have in common?

AI has made massive progress in applications where there is little uncertainty or ambiguity. For instance, when training a face recognition model, the model uses labels that tell it whether any two photos represent the same person or not. So, given enough data and computational resources, it will learn the patterns that distinguish one face from another. 

Though there have been some [notable](https://www.cbsnews.com/news/facial-recognition-60-minutes-2021-05-16/) [failures](https://www.nytimes.com/2020/12/29/technology/facial-recognition-misidentify-jail.html) of face recognition, it continues to get much more accurate (and that’s [exactly why we should worry](https://www.nature.com/articles/d41586-020-03187-3)).

Similarly, the game Go has clear rules, and we can generate as much data as we want by just letting the machine play against itself. Again, the lack of ambiguity and the abundance of data allow AI to get better at playing Go.

But the progress that’s been made in face recognition or Go-playing does not transfer to other domains. Limitations of AI are [amplified](https://www.wired.com/story/adaptation-if-computers-are-so-smart-how-come-they-cant-read/) when there are no clear rules, when collecting additional data is hard or impossible, and when reasonable people can disagree about the right answer. 

### **AI is not a magic 8-ball**

Given enough data and computational resources, is everything predictable? 

In 2017, our colleagues at Princeton University [tried to answer that question](https://www.fragilefamilieschallenge.org/). They organized a prediction competition: using over 10,000 data points about children, collected based on hours and hours of surveys and in-depth interviews with each family, hundreds of researchers aimed to predict how well each child would do in the future. 

[](https://substackcdn.com/image/fetch/$s_!3iEi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F095cc9aa-7334-4765-8a53-a2b91df16663_1538x1294.png) _(via[VentureBeat](https://venturebeat.com/2020/03/30/ai-is-bad-at-predicting-gpa-grit-eviction-job-training-layoffs-and-material-hardship/))_

They were massively disappointed to find that the latest AI techniques barely [performed](https://www.pnas.org/doi/10.1073/pnas.1915006117) better than simple linear regression and just four pieces of information about the children, such as race and mother’s education level. None of the models could predict future outcomes very well, reminiscent of _COMPAS_. 

There are many reasons why [predicting the future is hard](https://www.cs.princeton.edu/~arvindn/teaching/limits-to-prediction-pre-read.pdf): peoples’ lives could face sudden shocks, such as getting laid off or winning a lottery, that no model can predict. Small changes in a person’s life, such as one visit to the emergency room, could have compounding effects on their future, for instance, due to large medical bills. 

Yet, many companies and developers claim that their products can predict the future. For example, HireVue claims to predict future job performance using questions such as “Is your desk busy or minimal?” to infer applicants’ personalities. That’s basically a horoscope, yet this tool decides the fate of [millions of people every month](https://www.globenewswire.com/en/news-release/2021/10/19/2316607/0/en/HireVue-customers-conduct-over-1-million-video-interviews-in-just-30-days.html).

HireVue is not alone in claiming to predict individuals’ futures: [EAB Navigate](https://themarkup.org/machine-learning/2021/03/02/major-universities-are-using-race-as-a-high-impact-predictor-of-student-success) claims to predict which students will drop out of college and the [Allegheny Family Screening Tool](https://www.wired.com/story/excerpt-from-automating-inequality/) claims to predict which children are at risk of maltreatment. Each of these tools is an attempt to use AI to predict social outcomes of interest.

However, unlike speech transcription or image generation, there is no ground truth here, since the outcomes being predicted are in the future—they haven’t happened yet. On top of that, it is often impossible to collect the kinds of data required to make good predictions. 

We think many applications of AI for social prediction are [Snake Oil](https://www.cs.princeton.edu/~arvindn/talks/MIT-STS-AI-snakeoil.pdf)—they don’t work and perhaps will never work.

### **Can good judgment be automated?**

In April 2018, Mark Zuckerberg was [grilled](https://www.washingtonpost.com/news/the-switch/wp/2018/04/10/transcript-of-mark-zuckerbergs-senate-hearing/) by the U.S. Congress about what Facebook was doing about objectionable content such as troll accounts, election interference, fake news, terrorism content, and hate speech. His answer in all these cases was that AI tools would take care of it. The policymakers appeared to mostly accept his answers at face value, and didn’t know enough about tech and AI to call him out.

Content moderation is an example of what we call “automating judgment.” Why do we think AI won’t solve the problem? Since Facebook records the judgment of human moderators on millions of pieces of content, shouldn’t it be able to automate their work by training a model to recognize the patterns in their decisions?

There are two main barriers. The first is that AI remains notoriously bad at nuance and context. Google’s algorithms [reported](https://www.nytimes.com/2022/08/21/technology/google-surveillance-toddler-photo.html) a man to the police and terminated his account — causing him to lose access to more than a decade of contacts, emails, and photos — because he took a picture of his toddler’s infected genitals to send to the doctor. Predictably, the algorithms mistook this for child sexual abuse imagery. There are thousands and thousands of stories like that one.

Even if these problems can someday be overcome, there’s a much deeper one. AI can’t _make_ policy, only _implement_ it. Once human moderators have already labeled thousands of examples on either side of the line between acceptable and unacceptable nudity, or acceptable speech and calls to violence, AI can learn where the line is. _But the hard part is drawing the line_. New examples come up all the time that test our understanding of where the line is. This requires judgments based on our values. In the hard part of content moderation, AI does not and [cannot](https://journals.sagepub.com/doi/full/10.1177/2053951720943234) have a role. 

In our chapter, we’ll elaborate on these arguments and show you many more reasons why AI’s potential for automating judgment isn’t what it’s cracked up to be. These reasons apply not just to content moderation, but many other problems that at first seem very different but share some essential features, ranging from preventing imminent self-harm to automated essay grading (yes, that’s a thing, and it’s [widespread](https://www.npr.org/2018/06/30/624373367/more-states-opting-to-robo-grade-student-essays-by-computer) today). 

### **Why do myths persist?**

If AI can only work in a narrow domain of tasks, why do myths about AI persist? 

Researchers, companies, and the media can (even unwittingly) collude to create hype about AI, and public understanding of AI is collateral damage. 

[Hundreds of thousands](https://ourworldindata.org/grapher/annual-number-of-ai-publications?country=~OWID_WRL) of papers on AI are published every year, and most claim to make some advances. How many of these can be trusted? 

A cornerstone of scientific progress is the ability of independent researchers to verify previous results. Worryingly, research in AI falls short. For example, out of 400 recent papers in top AI conferences, [none](https://ojs.aaai.org/index.php/AAAI/article/view/11503/11362) documented their methods in enough detail such that an independent team could verify that their research was correct. 

In addition, many scientific fields such as radiology, psychology, and economics have also begun to adopt AI. However, AI methods are tricky to use correctly, and when errors occur, they are hard to detect. As a result, there are widespread errors due to adopting AI in [at least 17 different fields](https://reproducible.cs.princeton.edu/) (and likely in many more!). This is in part because a misplaced trust in AI leads to lesser scrutiny of flashy results.

Just as researchers have incentives to make [overhyped claims](https://prospect.org/culture/books/myth-of-artificial-intelligence-kissinger-schmidt-huttenlocher/) about AI, so do companies. In fact, not having to publish peer-reviewed research, nothing stops companies from making unsubstantiated claims about the effectiveness of their AI products. This works. Research has [shown](https://arxiv.org/abs/2203.01157) that venture capitalists who fund startups and clients who buy AI tools are swayed by these claims and don’t inspect them too carefully. 

Worse, companies exploit the fact that AI is an umbrella term without a precise definition. Whatever it is that they are selling and whether it works or not, claiming that it uses AI helps sell it — even when it’s [humans](https://www.theguardian.com/technology/2018/jul/06/artificial-intelligence-ai-humans-bots-tech-companies) behind the scenes! In other words, companies both capitalize on and contribute to public confusion about AI’s capabilities and limits.

Commercial AI hype is so successful because it is [amplified](https://medium.com/@emilymenonbender/on-nyt-magazine-on-ai-resist-the-urge-to-be-impressed-3d92fd9a0edd) by the media. Newsroom budgets have been decimated, so it’s always tempting for journalists to simply rewrite press releases, add a quote, and hit ‘publish’. Sensationalist headlines and misleading stock photos take the hype to the next level.

[](https://substackcdn.com/image/fetch/$s_!o-l7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd918c851-d05c-44a9-a586-1ab26cf6b3cd_2046x1614.png)_A screenshot of a[CNN Health article](https://www.cnn.com/2019/09/25/health/ai-disease-diagnosis-scli-intl/index.html). Despite the cover image, the article has nothing to do with robots. _

Bombarded with hype from researchers, companies, and journalists, it’s hard for any of us to evaluate claims about AI critically. On top of that, we share cognitive biases that make us especially susceptible to hype. For example, we tend to anthropomorphize AI—treat it as if it is an agent with human-like qualities. That leads to [misplaced trust in AI systems](https://link.springer.com/article/10.1007/s11948-020-00228-y). 

Cognitive biases can also prevent us from recognizing the limits of our own knowledge. For instance, we are often [overconfident](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3062901/) in our understanding of how things work—we feel that we understand complex phenomena in more detail than we actually do.

All of these result in a warped understanding of AI progress. The public is ready to believe that there is a high likelihood of AI achieving human-level intelligence [in the next 10 years](https://governanceai.github.io/US-Public-Opinion-Report-Jan-2019/us_public_opinion_report_jan_2019.pdf)! 

Because people are awed by this technology, there’s not nearly enough resistance when [flawed](https://dl.acm.org/doi/fullHtml/10.1145/3531146.3533158), black-box AI is deployed in hugely consequential situations, such as in criminal justice or hiring, with no opportunity for people to challenge decisions made about them.

### **What can be done about AI snake oil?**

Obviously, we think researchers and companies need to do better at avoiding hype. But we’re not holding our breath. The problem is that the incentives favor bold and unverifiable claims, and there are few consequences for misleading the public.

In 2016, AI pioneer Geoffrey Hinton [claimed](https://www.youtube.com/watch?v=2HMPRXstSvQ): “If you work as a radiologist, you're like the coyote that's already over the edge of the cliff but hasn't yet looked down, so he doesn’t realize there’s no ground underneath him. People should stop training radiologists now. It's just completely obvious that within five years, deep learning is going to do better than radiologists.” Six years later, deep learning or any other form of AI has not even come close to replacing radiologists. AI for healthcare has been failure after failure. Asked about this in 2022, Hinton [claimed](https://www.politico.com/news/2022/08/15/artificial-intelligence-health-care-00051828) he never predicted that AI would replace radiologists.

Journalists and advocates can play a role in shifting these incentives. Consider the issue of AI bias. Over the last five years, a loose community of scholars and activists has had [considerable](https://facctconference.org/) [success](https://www.codedbias.com/) in changing the narrative that AI is just math, and thus unbiased. People now understand that AI will, by default, reflect society’s biases. This has shifted the burden on companies to actively counteract bias.

A similar shift needs to happen with regard to AI’s accuracy. Companies deploying AI need to improve their standards for public reporting and allow external audits to evaluate stated accuracy claims. The burden of proof needs to shift to the company to affirmatively show that their AI systems work before they can be deployed.

Change starts with each of us. On this blog, we’ll give you ideas on how to resist AI snake oil in your own way — in the way you interact with AI products and vendors, read news articles, or evaluate your elected representatives and their approach to the AI industry.
