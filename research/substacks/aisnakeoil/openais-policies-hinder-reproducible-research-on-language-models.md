---
title: "OpenAI’s policies hinder reproducible research on language models"
author: "Arvind Narayanan & Sayash Kapoor"
date: ""
source: "substack_aisnakeoil"
url: "https://www.normaltech.ai/p/openais-policies-hinder-reproducible"
---

Researchers rely on ML models created by companies to conduct research. One such model, OpenAI's Codex, has been used in about a hundred academic papers[1](https://www.normaltech.ai/p/openais-policies-hinder-reproducible#footnote-1-110079526). Codex, like other OpenAI models, is not open source, so users rely on OpenAI for accessing the model. 

On Monday, OpenAI [announced](https://twitter.com/deliprao/status/1638014532680335363?s=20) that it would discontinue support for Codex by Thursday. Hundreds of academic papers would no longer be reproducible: independent researchers would not be able to assess their validity and build on their results. And developers building applications using OpenAI's models wouldn't be able to ensure their applications continue working as expected.

[](https://substackcdn.com/image/fetch/$s_!WvqE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff412703c-7c62-4d4a-94e2-cab2860f422a_1766x964.png)_OpenAI asked users to switch to GPT 3.5 with less than a week's notice.[Source](https://twitter.com/deliprao/status/1638014532680335363?s=20)._

#### **The importance of reproducibility**

Reproducibility—the ability to independently verify research findings—is a cornerstone of research. Scientific research already suffers from a reproducibility crisis, including in [fields that use ML](https://sites.google.com/princeton.edu/rep-workshop). 

Since small changes in a model can result in significant downstream effects, a prerequisite for reproducible research is access to the exact model used in an experiment. If a researcher fails to reproduce a paper’s results when using a newer model, there’s no way to know if it is because of differences between the models or flaws in the original paper. 

OpenAI responded to the criticism by saying they'll allow researchers access to Codex. But the [application process](https://openai.com/form/researcher-access-program) is opaque: researchers need to fill out a form, and the company decides who gets approved. It is not clear who counts as a researcher, how long they need to wait, or how many people will be approved. Most importantly, Codex is only available through the researcher program “for a limited period of time” (exactly how long is unknown).

OpenAI regularly updates newer models, such as GPT-3.5 and GPT-4, so the use of those models is automatically a barrier to reproducibility. The company does offer snapshots of specific versions so that the models continue to perform in the same way in downstream applications. But OpenAI only maintains these snapshots for [three months](https://archive.is/CUtId#selection-591.43-591.115). That means the prospects for reproducible research using the newer models are also dim-to-nonexistent.

Researchers aren't the only ones who could want to reproduce scientific results. Developers who want to use OpenAI's models are also left out. If they are building applications using OpenAI's models, they cannot be sure about the model's future behavior when current models are deprecated. OpenAI says developers should switch to the newer GPT 3.5 model, but this model is [worse](https://twitter.com/goodside/status/1638064664046186496?s=61&t=m1xXlmx_tov7wXvbG0f4Jw) than Codex in some settings.

#### **LLMs are research infrastructure**

Concerns with OpenAI's model deprecations are amplified because LLMs are becoming key pieces of infrastructure. Researchers and developers rely on LLMs as a [foundation layer](https://crfm.stanford.edu/report.html), which is then fine-tuned for specific applications or answering research questions. OpenAI isn't responsibly maintaining this infrastructure by providing versioned models.

Researchers had less than a week to shift to using another model before OpenAI deprecated Codex. OpenAI asked researchers to switch to GPT 3.5 models. But these models are [not comparable](https://twitter.com/deliprao/status/1638019705742020611?s=20), and researchers' old work becomes irreproducible. The company's hasty deprecation also falls short of standard practices for deprecating software: companies usually offer months or even years of advance notice before deprecating their products.

#### **Open-sourcing LLMs aids reproducibility**

LLMs hold exciting possibilities for research. Using publicly available LLMs could [reduce](https://twitter.com/random_walker/status/1637079520560676870?s=20) the resource gap between tech companies and academic research, since researchers don't need to train LLMs from scratch. As research in generative AI shifts from developing LLMs to using them for downstream tasks, it is important to ensure reproducibility. 

OpenAI's haphazard deprecation of Codex shows the need for caution when using closed models from tech companies. Using open-source models, such as [BLOOM](https://arxiv.org/abs/2211.05100), would circumvent these issues: researchers would have access to the model instead of relying on tech companies. Open-sourcing LLMs is a complex question, and there are many other factors to consider before deciding whether that's the right step. But open-source LLMs could be a key step in ensuring reproducibility.

[1](https://www.normaltech.ai/p/openais-policies-hinder-reproducible#footnote-anchor-1-110079526)

We searched CS arxiv papers with the term Codex in their abstracts written after August 2021. This resulted in [96 results](https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term=Codex&terms-0-field=abstract&classification-computer_science=y&classification-physics_archives=all&classification-include_cross_list=include&date-year=&date-filter_by=date_range&date-from_date=2021-08&date-to_date=&date-date_type=submitted_date&abstracts=show&size=50&order=-announced_date_first). This is likely an undercount: it ignores papers submitted to venues other than arxiv and papers still being drafted.
