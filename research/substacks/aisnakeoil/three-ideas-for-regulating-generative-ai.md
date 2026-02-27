---
title: "Three Ideas for Regulating Generative AI"
author: "Arvind Narayanan & Sayash Kapoor"
date: ""
source: "substack_aisnakeoil"
url: "https://www.normaltech.ai/p/three-ideas-for-regulating-generative"
---

Last week, we submitted [comments](https://www.regulations.gov/comment/NTIA-2023-0005-1366) to the National Telecommunication and Infrastructure Authority (NTIA), written in collaboration with [Rishi Bommasani](https://rishibommasani.github.io/), [Daniel Zhang](https://profiles.stanford.edu/danielzhang), and [Percy Liang](https://cs.stanford.edu/~pliang/) at Stanford. In our comments, we describe the need for transparency around the generative AI ecosystem, the need for holistic public evaluations, and the guardrails needed for responsible open-source AI research and development. This post is a summary of our [comments](https://www.regulations.gov/comment/NTIA-2023-0005-1366).

### **Transparency about the digital supply chain that powers generative AI products**

Generative AI models are the building blocks for various digital products and services. They play a central role in the broader AI ecosystem. This [ecosystem](https://crfm.stanford.edu/2022/11/17/helm.html) can be summarized by three types of assets: 

  * **Resources,** including the data (e.g., the billions of words and images in datasets scraped from the Internet) and computational resources (e.g., through cloud providers like Amazon, Google, and Microsoft) necessary for training models.

  * **Foundation models** that can be used for various downstream tasks, such as GPT-4 and Stable Diffusion.

  * **Products and services** built atop these models (e.g., [Bing Search](https://blogs.bing.com/search/march_2023/Confirmed-the-new-Bing-runs-on-OpenAI%E2%80%99s-GPT-4), Khan Academy’s [Khanmigo](https://www.khanacademy.org/khan-labs) tutor). 




Each asset should be tracked for all products and services released to users. This would have clear benefits:

**Enable recourse to stop further harm:** the National Highway Traffic Safety Administration (NHTSA) monitors the automobile supply chain and conducts [recalls](https://www.nhtsa.gov/sites/nhtsa.gov/files/documents/14218-mvsdefectsandrecalls_041619-v2-tag.pdf) when a part, such as a batch of car brakes, is identified to be faulty. Similarly, when an asset used in a generative AI product has flaws, digital supply chain monitoring can help find and address the flaws.

**Identify algorithmic monoculture:** [Monoculture](https://www.pnas.org/doi/10.1073/pnas.2018340118) refers to the pervasive dependence on a single asset (e.g., a single foundation model). As SEC Chair Gary Gensler has [noted](https://mitsloan.mit.edu/ideas-made-to-matter/secs-gary-gensler-how-artificial-intelligence-changing-finance), such dependence can yield “concentrated risk” in finance, for instance, if many people rely on the same model. Monoculture can also amplify other risks, including [security vulnerabilities](https://aisnakeoil.substack.com/p/licensing-is-neither-feasible-nor) and [outcome homogenization](https://openreview.net/forum?id=-H6kKm4DVo). Monitoring can help identify which models are being used pervasively and present a risk of monoculture.

**Expose regulatory opportunities and weaknesses:** Monitoring can help identify which sectors are impacted by foundation models. For example, if many products in a sector depend on foundation models, or data from a sector powers many foundation models, closer regulatory oversight might be needed. Digital supply chain monitoring allows us to identify where sector-specific regulatory authority will not suffice to hold AI companies accountable.

### **Transparency about evaluation**

Evaluating generative AI is tricky, because it is often useful for a wide variety of purposes. Many regulatory bodies have emphasized the importance of holistic evaluations. The UK's foundation model task force is [tasked](https://www.gov.uk/government/news/tech-entrepreneur-ian-hogarth-to-lead-uks-ai-foundation-model-taskforce) with designing evaluations for safe and trustworthy AI. And under the US CHIPS Act, the National Institute for Standards and Technology (NIST) is [mandated](https://archive.is/QOKre#selection-13543.46973-13543.47009) to create multidimensional evaluations for AI.

We outline three requirements that evaluations of generative AI should satisfy:

**Public:** To ensure foundation models are transparent, evaluations should be public and follow clear, openly disclosed practices. Such evaluations will improve the scientific discourse surrounding these models, combatting various forms of hype and advancing our collective understanding of this emerging technology. Public evaluations set the baseline for how we should reason about this technology.

**Holistic:** To ensure public evaluations surface the relevant dimensions of foundation models, these evaluations should be [holistic](https://crfm.stanford.edu/2022/11/17/helm.html): they should measure a range of objectives. For example, models should be evaluated on their accuracy, robustness, trustworthiness, fairness, and efficiency. The National Institute of Standards and Technology (NIST) released an [AI risk management framework](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf) that acknowledges the importance of multidimensional evaluations.

**Implementable regardless of how a model is released:** To ensure public and holistic evaluations hold _all_ generative AI models to account, evaluations should encompass models that are restricted or closed, meaning models that are not openly accessible to researchers and the public. 

Model providers currently adopt a variety of policies to release models. Some models, like EleutherAI’s [GPT-NeoX](https://huggingface.co/docs/transformers/model_doc/gpt_neox), are open-source. Others, like Google’s [Flamingo](https://www.deepmind.com/blog/tackling-multiple-tasks-with-a-single-visual-language-model), are entirely closed to the public. The inability of the public, including researchers and civil society, to investigate and interrogate these models inhibits external scrutiny. 

Since these models power products used by millions, including technologies like Google Search, the models themselves must be evaluated publicly and holistically. To improve the status quo, the government should require model developers to create programs for external researcher access.

### **Guardrails for open-source models**

We have previously [discussed](https://aisnakeoil.substack.com/p/licensing-is-neither-feasible-nor) the drawbacks of requiring licenses for developing AI—in particular, because it would lead to concentration in the hands of a few developers. But on the flip side, open-source models also [pose risks](https://dl.acm.org/doi/10.1145/3531146.3533088). Users could harm themselves or others using these models. 

To ensure responsible use, we suggest four specific guardrails:

**1\. Transparency by model developers:** Developers should be required to perform transparent evaluations of open-source models prior to release, so that stakeholders can understand the capabilities and risks. 

**2\. Compliance by downstream providers:** A foundation model is not a product by itself. Consumers won’t use foundation models directly, but rather products and services that incorporate them. These products and services are subject to consumer protections and product safety restrictions within the specific sector they are deployed (e.g., finance, medicine, or law). Regulatory agencies should enforce these requirements on providers of consumer-facing products or services built using open-source models.

**3\. Resilience of attack surfaces:** Malicious actors may use generative AI to create disinformation, find security vulnerabilities in software, or cause other forms of harm. Each of these malicious uses involves an attack surface. For example, the attack surface for disinformation is typically a social media platform—that is, where influence operators seek to disseminate disinformation and persuade people. For security vulnerabilities, the attack surface may be software codebases. 

While efforts may be taken to prevent the adaptation of foundation models for malicious purposes, policy should [focus on attack surfaces](https://knightcolumbia.org/content/how-to-prepare-for-the-deluge-of-generative-ai-on-social-media) that come under greater pressure due to the proliferation of foundation models. Such policies could include incentivizing social media platforms to strengthen their information integrity efforts, and increasing funding for cybersecurity and infrastructure defense efforts such as via [CISA](https://www.cisa.gov/).

**4\. Research on open-source foundation models:** Open-source foundation models are a nascent technology, and our understanding of the risks of foundation models and ways to address them is [rapidly evolving](https://dl.acm.org/doi/abs/10.1145/3593013.3593981). To realize a thriving and responsible open-source foundation model ecosystem, we need to resolve fundamental research problems in transparency, compliance, and malicious use. Federal funding for research on the risks and mitigations of open-source foundation models would ensure that our understanding of the policy options can keep pace with technology. 

~

Although foundation models are new, well-known interventions such as [transparency](https://www.lawfareblog.com/getting-transparency-right) and [auditing requirements](https://cacm.acm.org/magazines/2023/1/267960-actionable-auditing-revisited/fulltext) can go a long way if applied carefully. We expect that some of our suggestions have broad support, while others are perhaps more controversial. We hope for timely action on matters where there's consensus and informed debate on points where there is disagreement.
