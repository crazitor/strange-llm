---
title: "Generative AI models generate AI hype"
author: "Arvind Narayanan & Sayash Kapoor"
date: ""
source: "substack_aisnakeoil"
url: "https://www.normaltech.ai/p/generative-ai-models-generate-ai"
---

Text-to-image generators such as DALL-E 2 have been pitched as [making stock photos obsolete](https://thenextweb.com/news/nvidia-gaugan2-text-to-art-tool-shows-ai-could-replace-stock-photos). Specifically, generating [cover images](https://www.theguardian.com/commentisfree/2022/aug/20/ai-art-artificial-intelligence-midjourney-dall-e-replacing-artists) for news articles is one of the use cases envisioned for these models. One downside of this application is that like most AI models, these tools perpetuate [biases](https://www.vice.com/en/article/wxdawn/the-ai-that-draws-what-you-type-is-very-racist-shocking-no-one) and [stereotypes](https://www.vox.com/future-perfect/23023538/ai-dalle-2-openai-bias-gpt-3-incentives) in their training data. 

But do these models also perpetuate stereotypes about AI, rather than people? After all, stock images are notorious for [misleading imagery](https://betterimagesofai.org/) such as humanoid robots that propagate AI hype.

We tested Stable Diffusion, a recently released text-to-image tool, and found that **over 90% of the images generated for AI-related prompts propagate AI hype**. Journalists, marketers, artists, and others who use these tools should use caution to avoid a feedback loop of hype around AI.

[](https://substackcdn.com/image/fetch/$s_!HPWd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F0602c0b6-ea30-404e-b55f-c140e4a0f1b3_990x992.png)_An image of “artificial intelligence” generated using Stable Diffusion._

### Background: stock photos of AI are misleading and perpetuate hype

Stock photos of all kinds, not just of AI, are some of the [most ridiculed images](https://www.theguardian.com/artanddesign/commentisfree/2017/sep/10/stock-photo-stereotypes-are-shifting-but-the-typical-woman-is-still-young-skinny-and-white) on the internet. 

News articles on AI tend to use stock photos that include humanoid robots, blue backgrounds with floating letters and numbers, and robotic arms shaking hands with humans. This imagery obscures the fact that AI is a tool and doesn’t have agency. Most of the articles in question are about finding patterns in data rather than robots.

[](https://substackcdn.com/image/fetch/$s_!EaJQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb0f1e4b4-ef70-4daa-8b66-de7ae7f8f1a8_1338x790.png)_CNN used an image of a robotic arm in an[article](https://www.cnn.com/2019/02/17/investing/artificial-intelligence-investors-machine-learning/index.html) about using AI to analyze financial data._

A news article’s cover image sets the tone and provides a [visual metaphor](https://www.rockefellerfoundation.org/blog/making-sense-of-the-unknown/). Especially in articles on AI, images are used as a scaffold, since most readers do not have a deep understanding of how AI systems work. 

Images that do not reflect the content of the article are [at best misleading](https://link.springer.com/article/10.1007/s11023-019-09506-6) and at worst lead to hype and fear about the technology. For example, a [study](https://dl.acm.org/doi/10.1145/3306618.3314232) that surveyed the U.K. public found that a majority couldn’t give a plausible definition of AI and 25% defined it as robots—no doubt in part because of how AI is represented in the media.

Accurately representing emerging technologies such as artificial intelligence is hard. In fact, misleading images of AI have become so widespread that there are [several](https://betterimagesofai.org/) [projects](https://www.culture-a.com/is-seeing-believing-case-study) to [improve](https://royalsociety.org/topics-policy/projects/ai-narratives/) [AI](https://www.aimyths.org/ai-equals-shiny-humanoid-robots) [imagery](https://notmyrobot.home.blog/about/).

### Do AI-based text-to-image tools create AI hype? 

Text-to-image tools such as [DALL-E 2](https://openai.com/dall-e-2/), [Imagen](https://imagen.research.google/), [Midjourney](https://www.midjourney.com/showcase/), and [Stable Diffusion](https://huggingface.co/spaces/stabilityai/stable-diffusion) have sparked people’s imagination, but also generated discussion about economically productive uses. One potential use is to [generate cover images for news articles](https://thenextweb.com/news/nvidia-gaugan2-text-to-art-tool-shows-ai-could-replace-stock-photos). A [few](https://www.nytimes.com/2022/08/24/technology/ai-technology-progress.html) [articles](https://nymag.com/intelligencer/article/will-dall-e-ai-artist-take-my-job.html) have already used them, and wider use is likely as the tools become open-source and freely available.

Given this prospect, do AI-based text-to-image tools create misleading images of AI, or do they generate images that accurately depict how AI is used today?

We tested one of these systems—Stable Diffusion—with four prompts about AI: “artificial intelligence”, “artificial intelligence in healthcare”, “artificial intelligence in science”, and “cover image for a news article on artificial intelligence”.[1](https://www.normaltech.ai/p/generative-ai-models-generate-ai#footnote-1-72569540)

For each prompt, we generated 20 images to check whether they contained humanoid forms or robots. We included prompts about healthcare and science to check if the resulting images included elements about the domain such as images of doctors and scientists using AI tools. 

The results are stark: **for each prompt, over 90% of the images generated using the text-to-image tool contain humanoids**. Adding an application domain for artificial intelligence to the prompt does not improve the outcomes too much—only 1 out of 20 images for both the healthcare and science prompts contain anything that is even remotely related to those domains, and 19 of the 20 images still contain humanoids.[2](https://www.normaltech.ai/p/generative-ai-models-generate-ai#footnote-2-72569540)

[](https://substackcdn.com/image/fetch/$s_!G2Uz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5dbf3d4b-e403-4b4c-b3de-78e0652548ea_800x644.png) _Prompt: “artificial intelligence”. All 20 images contain humanoids._

Surprisingly, the results for “artificial intelligence” on the stock image website Shutterstock contain humanoids or robots in only [11 out of the first 20 results](https://archive.ph/lXdCc); this hints that text-to-image models could amplify stereotypes in images of AI.

We include all 20 images for each prompt [here](https://drive.google.com/drive/folders/1sKf0_PalYOew1eKKrAfx3ZoZAPfQ2Diq?usp=sharing); you can also [try out the tool yourself](https://huggingface.co/spaces/stabilityai/stable-diffusion).

### The prompts matter—a lot

Using carefully chosen prompts for AI-based text-to-image tools is pivotal to generating images that reflect the user’s intent. In fact, it is so important that there is now a [marketplace for buying prompts](https://www.theverge.com/2022/9/2/23326868/dalle-midjourney-ai-promptbase-prompt-market-sales-artist-interview) to create better images. 

Fortunately, changing the prompt is also an easy way to generate images of AI that are not misleading or inaccurate. Using more descriptive prompts about the _contents_ of the image rather than the _concepts_ in the image can result in more appropriate images. For example, instead of using “artificial intelligence in healthcare” as a prompt, you can use a descriptive prompt such as “a photograph of a doctor looking at a medical scan on a computer” to get images where humans are rightly depicted as agents, rather than humanoid robots. If it is necessary to visually emphasize the technology itself, prompts such as “silicon chip” tend to work well. Or “self-driving car”, if it is appropriate to the contents of the article.

Surprisingly, if we use _machine learning_ instead of _artificial intelligence_ as a prompt, robots disappear from the resulting images, though most images are unusable and create illegible characters. Even though recent AI advances rely on some form of machine learning, the resulting images for the two prompts are starkly different, showing much the prompt matters.

### Stock photos make for poor training data

The heavy use of stock images in the training data for text-to-image tools could be one reason for the abundance of humanoid robots in images of AI. The images used for training text-to-image tools include stock photo repositories—so much so that these tools often end up creating images with stock photo [watermarks](https://news.ycombinator.com/item?id=32573523) [still intact](https://twitter.com/kevin2kelly/status/1551964984325812224?s=20&t=pf1woeBLnOxw9KW7GaZaPQ)!

Given the [abundance of humanoids in stock images](https://link.springer.com/article/10.1007/s13347-022-00498-3), it is unsurprising that the tools trained using these images generate humanoids and robots in response to prompts about AI. 

Stock photos are not just problematic when they are about AI. The very point of a stock image is to quickly bring a specific concept or category to mind—so they often [focus on stereotypes](https://www.theguardian.com/artanddesign/commentisfree/2017/sep/10/stock-photo-stereotypes-are-shifting-but-the-typical-woman-is-still-young-skinny-and-white) and can be [derogatory and biased](https://www.nytimes.com/2017/09/07/upshot/from-sex-object-to-gritty-woman-the-evolution-of-women-in-stock-photos.html). Using stock images for training text-to-image tools could be one source of misleading or biased images that result from these tools—and [not just in articles about AI](https://www.wired.com/story/dall-e-2-ai-text-image-bias-social-media/). 

### Summary: avoiding hype, improving training data

Images used to illustrate AI articles today are already misleading and inaccurate. If news media turn towards using text-to-image tools for generating illustrations, it risks creating a pernicious feedback loop where AI tools are used to generate misleading images of AI that feed into the hype—and are used as training data for future models. 

Similar issues have been found in language models, where training datasets are [contaminated by machine-generated text](https://aclanthology.org/2021.emnlp-main.98/). Stable Diffusion does apply an [invisible watermark](https://github.com/CompVis/stable-diffusion#reference-sampling-script) which could potentially be used to filter out machine-generated images. However, the rapid increase in the number of text-to-image tools and the lack of standardized watermarks could complicate this filtering step. As we suggested above, an alternative way to improve these tools could be to reduce the number of stock images in the training data.

Finally, when writing prompts, describing the _contents_ of the image instead of the _concepts_ in the image and experimenting with different prompts to pick out accurate examples will go a long way.

[1](https://www.normaltech.ai/p/generative-ai-models-generate-ai#footnote-anchor-1-72569540)

We selected Stable Diffusion because it is the only one that is free to use, runs locally, and generates sufficiently high-quality images for our purposes.

[2](https://www.normaltech.ai/p/generative-ai-models-generate-ai#footnote-anchor-2-72569540)

In a small number of cases, the images generated are nonsensical; we exclude these images from our analysis.
