---
title: "Licensing is neither feasible nor effective for addressing AI risks"
author: "Arvind Narayanan & Sayash Kapoor"
date: ""
source: "substack_aisnakeoil"
url: "https://www.normaltech.ai/p/licensing-is-neither-feasible-nor"
---

Many people and organizations have argued that one way to make AI safer is by non-proliferation, [similar to nuclear weapons or human cloning](https://www.wsj.com/articles/iaea-for-ai-that-model-has-already-failed-chaptgpt-technology-nuclear-proliferation-4339543b). 

This would mean that only certain licensed companies and organizations can build state-of-the-art AI models. The argument is that this would allow the government to contain the spread of harmful AI models, have oversight into what AI tools are built and how they are deployed, and thus be able to guide the development of AI in a socially beneficial way. 

Similar arguments underlie other attempts to forestall AI development, for instance, in the [Future of Life Institute's letter](https://aisnakeoil.substack.com/p/a-misleading-open-letter-about-sci) arguing for a six-month pause on training models bigger than GPT-4.

#### **Licensing is infeasible to enforce**

If regulators commit to non-proliferation, how would they enforce it? It is not enough to require that developers obtain licenses, because malicious actors can simply ignore the licensing requirements and proceed with training AI models. 

One approach that’s been suggested is to [surveil data centers](https://openai.com/blog/governance-of-superintelligence) where models are trained and hosted. This proposal relies on the fact that AI requires lots of computing resources. In theory, data centers would need to report when a customer uses above a certain level of computing resources, which could prompt an investigation. 

But as algorithmic and hardware improvements reduce costs for training models at a given capability level, this approach would require increasingly draconian surveillance measures and an unprecedented level of international cooperation to be effective. Though training state-of-the-art models like GPT-4 is [expensive](https://www.wired.com/story/openai-ceo-sam-altman-the-age-of-giant-ai-models-is-already-over/), the cost is [rapidly dropping](https://www.mosaicml.com/blog/mpt-7b), both because of the decrease in hardware costs and due to improvements in the algorithms used to train AI models.

To see the long-term trends, we can look at computer vision. Between 2012 and 2019, training an image recognition classifier with the same performance became [44 times cheaper](https://openai.com/research/ai-and-efficiency). 

As of this writing, one of the most capable open-source language models, [Falcon](https://falconllm.tii.ae/), required fewer than 400 GPUs and only two months to train. We estimate that such a model can be trained for a cost of less than USD 1 million.[1](https://www.normaltech.ai/p/licensing-is-neither-feasible-nor#footnote-1-127227859)

Further, the technical know-how required to build large language models is already widespread, and there are several open-source LLMs developed by organizations that share their [entire code and training methodology](https://github.com/mosaicml/llm-foundry). Because of these reasons, non-proliferation is infeasible from an enforcement perspective.

OpenAI and others have proposed that licenses would be required only for the most powerful models, above a certain training compute threshold. Perhaps that is more feasible — but again, unless all capable actors voluntarily comply, enforcement would be possible only by giving governments extraordinary powers. 

And let's be clear about what it could accomplish: It would, at most, buy a few years of time. For any given capability threshold, training costs are likely to keep dropping due to both hardware and algorithmic improvements. Once the costs are low enough, the set of actors who can fund the development of such models will be too high to police.

#### **Licensing will increase concentration and may worsen AI risks**

Despite the proliferation of AI models themselves, a small number of big tech companies stand to [profit greatly](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4135581) from the generative AI wave: whether by integrating it into their apps (e.g., Google, Microsoft, and Apple), by selling API access (e.g., OpenAI and Anthropic), or by selling hardware (NVIDIA).

Such concentration harms competition. Committing to non-proliferation would further increase this risk, because only a handful of companies would be able to develop state-of-the-art AI. 

Further, decades of experience in the field of information security suggest that it’s better to deal with with security risks openly instead of "security through obscurity." In particular, non-proliferation and the resulting concentration of power would impact five major AI risks:

  1. **Monoculture may worsen security risks.** When thousands of apps are all powered by the same model (GPT-3.5 is already in this position today), security vulnerabilities in this model can be exploited across all of these different applications.

  2. **Monoculture may lead to outcome homogenization.** The use of the same AI model across different applications increases [homogenization](https://arxiv.org/abs/2211.13972), including in consequential settings such as resume screening. If a candidate applies to multiple jobs, instead of being evaluated independently by the different companies, they could be rejected from all of them if all companies use the same AI tool for hiring. 

  3. **Defining the boundaries of acceptable speech.** In some ways, generative AI apps are similar to social media platforms where people generate and consume content. If most people use models created by a small group of providers, these developers get outsized power in defining the Overton windows of acceptable speech, by governing what is and isn't allowed in conversations. 

  4. **Influencing attitudes and opinions.** If people use chatbots as conversation partners, the “opinions” expressed by them could influence people’s views on a massive scale. There is evidence for this from a [recent study](https://dl.acm.org/doi/10.1145/3544548.3581196).

  5. **Regulatory capture.** The ongoing lobbying for a licensing regime can be seen as [regulatory capture](https://www.theverge.com/2023/5/19/23728174/ai-regulation-senate-hearings-regulatory-capture-laws). If it succeeds, it would give AI companies even more power in policy debates. Instead of engaging with the arguments, they could [dismiss critics](https://fortune.com/2023/05/15/former-google-ceo-eric-schmidt-tells-government-to-leave-regulation-of-ai-to-big-tech-openai-chatgpt-bardai-midjourney/) as uninformed outsiders lacking expertise on AI capabilities and risks.




One way to avoid concentration is the development and evaluation of state-of-the-art models by a diverse group of academics, companies, and NGOs. We believe this would be a better way to uncover and address AI risks. Of course, open-source AI presents its own risks and requires guardrails. What might those guardrails look like? We plan to share a few ideas soon.

[1](https://www.normaltech.ai/p/licensing-is-neither-feasible-nor#footnote-anchor-1-127227859)

The model was trained on [384 Nvidia A100 GPUs for 60 days](https://pub.towardsai.net/falcon-40b-a-fully-opensourced-foundation-llm-945dd9824157). The hourly rate of using one such GPU on AWS varies from [USD 1.44 to USD 4.10](https://aws.amazon.com/ec2/instance-types/p4/). Bulk costs are generally lower than hourly costs. 
