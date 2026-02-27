---
title: "Large-Scale Online Deanonymization with LLMs"
author: "Simon Lermen"
date: "2026-02-24"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/xwCWyy8RvAKsSoBRF/large-scale-online-deanonymization-with-llms"
score: 61
votes: 21
---

****TL;DR:**** We show that LLM agents can figure out who you are from your anonymous online posts. Across Hacker News, Reddit, LinkedIn, and anonymized interview transcripts, our method identifies users with high precision – and scales to tens of thousands of candidates.

While it has been known that individuals can be uniquely identified by surprisingly few attributes, this was often practically limited. Data is often only available in unstructured form and deanonymization used to require human investigators to search and reason based on clues. We show that from a handful of comments, LLMs can infer where you live, what you do, and your interests – then search for you on the web. In our new research, we show that this is not only possible but increasingly practical.

****Paper:**** [](https://arxiv.org/abs/2602.16800) [Large-Scale Online Deanonymization with LLMs](https://arxiv.org/abs/2602.16800)

![agentic_deanon_example.png](https://res.cloudinary.com/lesswrong-2-0/image/upload/v1771867661/lexical_client_uploads/wyiogfjevxkcgpgt1wrt.png)

Motivation – Why do we research this?
-------------------------------------

Among the near-term effects of AI, different forms of [AI surveillance](https://www.cnbc.com/2026/02/18/anthropic-pentagon-ai-defense-war-surveillance.html) pose some of the most concrete harms. It is already known that [LLMs can infer personal attributes](https://arxiv.org/abs/2310.07298) about authors and use that to create biographical profiles of individuals (also [see](https://arxiv.org/abs/2510.01645)). Such profiles can be misused straightforwardly with [spear-phishing](https://www.sciencedirect.com/science/article/abs/pii/S0957417426004598) or many other forms of [monetizing exploits](https://arxiv.org/abs/2505.11449). Using AI for massively scalable "[people search](https://exa.ai/docs/changelog/people-search-launch)" is harmful by itself by undermining many privacy assumptions.

Beyond shining a light on this growing harmful use of AI, we explore options on how individuals can protect themselves – and what social platforms and AI labs can do in response.

We acknowledge that by publishing our results and approximate methods, we carry some risk of accelerating misuse developments. Nevertheless, we believe that publishing is the right decision.

How We Designed Our Benchmarks
------------------------------

It is tricky to benchmark LLMs on deanonymization. You don't want to actually deanonymize anonymous individuals. And there is no ground truth for online deanonymization – how could you verify that the AI found the correct person?

Our solution is to construct two types of deanonymization proxies which allow us to study the effectiveness of LLMs at these tasks. We also perform a real world deanonymization attack on the Anthropic Interviewer dataset with manual verification.

### Proxy 1: Cross-Platform Matching

The idea of our cross-platform benchmark is to take two accounts on different platforms for which we know they belong together, and then remove any directly identifiable features from one of the accounts. The task is then to put the accounts of the same person back together.

Concretely, we take non-anonymous Hacker News (HN) accounts that link to their LinkedIn. We then anonymize the HN accounts, removing all directly identifying information. Then, we let LLMs match the anonymized account to the true person. We find that we can re-identify most accounts with high precision when we are combining search and reasoning. We use embeddings-based search to find the 100 most promising candidates and then reason to select and verify the most promising candidate. (See [Section 4](https://arxiv.org/abs/2602.16800) of the paper for full details on the HN-LinkedIn experiment.)

  

![hn_pr_curve.png](https://res.cloudinary.com/lesswrong-2-0/image/upload/v1771867257/lexical_client_uploads/husizoo9aytv9gsnbign.png)

Search refers to using LLMs to extract information and using search over embeddings to find the correct match. Search+Reason adds an LLM step that selects and verifies the correct match.

### Proxy 2: Matching Split Accounts

As another approach to benchmarking deanonymization, we artificially split up a single account into two accounts and then test if we are able to link these split accounts back together. On Reddit, we split user histories into "before" and "after," then test whether LLMs can link them back together. Alternatively, we split Reddit accounts by community, dividing their activity according to the subreddits they participate in. In both cases, LLM embeddings combined with reasoning significantly outperform [Netflix-Prize-style](https://dl.acm.org/doi/10.1109/SP.2008.33) baselines that match based on subreddit activity patterns and metadata. (See [Section 5](https://arxiv.org/abs/2602.16800) for the community-split experiment and [Section 6](https://arxiv.org/abs/2602.16800) for the temporal-split experiment.)

### It Scales to Much Larger Datasets

As candidate pools grow to tens of thousands, LLM-based attacks degrade gracefully at high precision. This implies that with sufficient compute, these methods would already scale to entire platforms. With future models, we can expect that performance will improve while the cost will only go down. (See [Section 4.3](https://arxiv.org/abs/2602.16800) and [Section 6.4](https://arxiv.org/abs/2602.16800) for our scaling analyses.)

![hn_scaling.png](https://res.cloudinary.com/lesswrong-2-0/image/upload/v1771866977/lexical_client_uploads/gka27cosvyxfa4m9qmhj.png)

We scale the candidate pool size and extrapolate to 100M users. Recall@90% Precision

Identifying people in the real world
------------------------------------

Anthropic's [Interviewer dataset](https://huggingface.co/datasets/Anthropic/AnthropicInterviewer) contains anonymized interviews with scientists about their use of AI. [Li (2026)](https://arxiv.org/abs/2601.05918) first showed that a simple LLM agent could re-identify some of these scientists just by searching the web and reasoning over the transcripts. Our agent is able to identify 9 out of 125 individuals in the dataset, though we caveat that this number is based on manual verification, since no ground truth data exists for this task. (See [Section 2](https://arxiv.org/abs/2602.16800) for our agentic deanonymization experiments.)

![anthropic_example.png](https://res.cloudinary.com/lesswrong-2-0/image/upload/v1771866941/lexical_client_uploads/bckrzd4eknfqzeyuobru.png)

What Now?
---------

****What can platforms do?**** The most effective short-term mitigation is restricting data access. Enforcing rate limits on API access to user data, detecting automated scraping, and restricting bulk data exports all raise the cost of large-scale attacks. Platforms should assume that pseudonymous users can be linked across accounts and to real identities, and this should inform their data access policies.

****What can LLM providers do?**** Refusal guardrails and usage monitoring can help, but both have significant limitations. Our deanonymization framework splits an attack into seemingly benign tasks – summarizing profiles, computing embeddings, ranking candidates – that individually look like normal usage, making misuse hard to detect. Refusals can be bypassed through task decomposition. And none of these mitigations apply to open-source models, where safety guardrails can be removed and there is no usage monitoring at all. In some tested scenarios, LLM agents did refuse to help us but this could be avoided with small prompt changes. This mirrors inherent issues with preventing AI misuse – each step of misuse can locally be identical or very similar to valid use cases.

****What should you do if you are using pseudonymous accounts online?**** Individuals may adopt a stronger security mindset regarding privacy. Each piece of specific information you share – your city, your job, a conference you attended, a niche hobby – narrows down who you could be. The combination is often a unique fingerprint. Ask yourself: could a team of smart investigators figure out who you are from your posts? If yes, LLM agents can likely do the same, and the cost of doing so is only going down.

****Paper:****  [Large-Scale Online Deanonymization with LLMs](https://arxiv.org/abs/2602.16800)