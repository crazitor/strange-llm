---
title: "Can Current AI Match (or Outmatch) Professionals in Economically Valuable Tasks?"
author: "saahir.vazirani"
date: "2026-02-20"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/e2bmJgBS8kHzeBjwh/can-current-ai-match-or-outmatch-professionals-in"
score: 6
votes: 2
---

A Demonstration Utilizing OpenAI’s GDPval Benchmark
===================================================

### Saahir Vazirani

saahir.vazirani@gmail.com

Abstract
--------

This project demonstrates current AI capability for the audiences of nonprofits, civil society organizations, worker advocacy groups, and professional associations—and secondarily among policymakers who interpret these signals into regulation or economic policy. I adapt GDPval, a benchmark measuring AI performance on economically valuable real-world tasks, into an interactive display navigable by constituency or profession (e.g., financial managers). The research question is whether seeing present-day, task-level capabilities within one’s own field meaningfully increases support for responsible AI strategies such as equitable deployment expectations, public-interest AI infrastructure investment, and workforce adaptation planning. Early prototyping and GDPval’s documented findings suggest that profession-aligned displays make AI capability more tangible for civil society and provide policymakers with a clearer grounding for economic transition and AI safety considerations.

Introduction
------------

Most AI safety assessments remain theoretical, highly technical, or aimed at very long-term scenarios. Yet, the majority of decisions that legislators and civil society actors are actually making in the present are economic and sectoral: the impact of AI on work, wages, productivity, bargaining power, regionalized economic sectors, and a labor force in transition. This project fills a missing link - most evidence presented to policymakers is abstracted without a clear connection to the chosen constituency. GDPval provides a channel to make “model capability level” tangible in the space of real tasks. My work involves adapting GDPval for a public-facing, exploratory demo that is publicly accessible to a filtered stakeholder audience. Project success is evidenced by a deployable demo that successfully renders profession-specific model capabilities in actual tasks, empirically boosting policymakers' perceived levels of economic urgency and the need for proactive deployment policies based on responsible safety standards, as opposed to reactionary crisis responses. 

The two-prong impact of this project is evident in its ease of use. Civil society groups can assess the limitations of AI in their field of work across numerous tasks; from there, they can conclude the usages of AI within their career, its efficacy, and if their concerns are warranted. Additionally, policymakers can craft policies to regulate AI usage in the workforce, especially when dealing with sensitive data in healthcare and financial fields. Concurrently, the regulation of “AI employees” may arise as the advent of AI agents with MCPs and tool access takes over diverse sectors. 

Methods
-------

This project relies on the publicly documented GDPval benchmark (Measuring the Performance of Our Models on Real-World Tasks, 2025) and (Patwardhan et al., 2025) as the real-world capability source. First, I ingest the GDPval open subset dataset hosted on Hugging Face (OpenAI, 2024). This dataset contains a defined task schema for a standardized task, including prompt text, expected deliverable type, reference files, and occupational metadata. I create an index of all tasks, obtain occupational uniqueness, and apply occupational filtering so that a user can select a relevant occupation for their constituency (“First-Line Supervisors of Office and Administrative Support Workers” in the “Health Care and Social Assistance” sector, for example). Second, as each task is required in a live demo execution, the system retrieves the prompt and any attachment files, then invokes a selected model through the various APIs from OpenAI, Anthropic, and particularly Manus (model switcher: different frontier or non-frontier models can be positioned and compared next to each other). Since full GDPval evaluation is conducted through blind human professional grading (noted in the OpenAI paper above), and this cannot be achieved live at scale, the audience of professionals will be the ones to determine the accuracy of the output deliverables. Thus, the demo outputs: (1) live feed of deliverable being created, (2) downloadable deliverables in PDF, .xslx, and text formats (3) relative inference cost/time differences in comparison to a comparable human-created task as determined by those in the relative profession (inferred through model's run time and token cost assessed throughout the demo).

**Figure 1**

*Example Output With “Accountants and Auditors” Task* 

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/19f58a9e01a8bfce7e7108122e046a5c1480fe416c2b8981.png)

*Note*. Above is what the model (Manus) actually outputted as downloadable files; the prompt task (id: 83d10b06-26d1-4636-a32c-23f92c57f30b). Its output consists of a spreadsheet with three tabs as indicated in the full task prompt.

Implications & Future Directions
--------------------------------

To evaluate the demonstration’s efficacy, next steps would include an initial single profession pilot (of those available in the dataset; otherwise closest profession match), and then additional professions in sequence to be presented. To further the impact of the demonstration, increased depth in regard to the chain-of-thought process of the model, creating the work deliverable, could be implemented. Supplementing this, anonymous survey responses measuring whether seeing task-level model parity increases belief that (1) AI capability is relevant to their economic domain now, (2) they support proactive/responsible deployment governance frameworks, and (3) they support investment in adaptation policies will be rolled out.

Next, integrating comparative model testing to show differences in capability trajectories across models, as measured using the same GDPval task, would allow for a more comprehensive view of model capabilities from different organizations. All findings and code will reference only publicly documented methods and publicly available benchmark sources (OpenAI GDPval blog: [https://openai.com/index/gdpval](https://openai.com/index/gdpval), GDPval paper: [https://arxiv.org/abs/2510.04374](https://arxiv.org/abs/2510.04374), dataset: [https://huggingface.co/datasets/openai/gdpval](https://huggingface.co/datasets/openai/gdpval)) so that policymakers and researchers can independently verify, reproduce, and audit methodology. The end deliverable goal is a public demonstration that supports public understanding of economic impact and responsible development and use of AI in the economy, as well as evidence-driven policy prioritization.

In the long-term, various organizations affiliated with lobbying for policies regulating AI (i.e., Encode), civil society sectors themselves, and members from CivAI could present this demonstration to legislators; particularly, these efforts would begin at the national level within the U.S., as the GDPval benchmark was primarily focused on the U.S. economy. As the program receives more feedback, along with evaluation as determined by the efforts of legislators championing policies related to AI usage within the economy, coupled with civil society sectors’ reactions to the demonstrations, the program can be scaled to be presented to entities outside the U.S.

Discussion
----------

The following preliminary findings are established relative only to the verified public findings and published findings of GDPval itself - not user testing of this demo (as these demo sessions have yet to be conducted with those in the relevant fields). OpenAI explains that GDPval tasks were developed by professionals with an average of ~14 years in practice and represent real-world deliverables (Measuring the Performance of Our Models on Real-World Tasks, 2025). Per the GDPval paper findings (Patwardhan et al., 2025), for some of the more advanced models, expert-quality output is achieved on a substantial percentage of these tasks, meaning that significant relative capability does not reflect hypothetical economic disruption. Furthermore, the open subset contains diverse, multi-format tasks (OpenAI, 2024), suggesting that this benchmark is not like an academic multiple-choice exam benchmark. Therefore, these published findings support GDPval as a benchmark for socioeconomic-risk demos because deliverables are economically relevant tasks from the professional world, and a policymaker assessing capability relative to their constituency (financial managers, manufacturing engineers, etc.) can witness a concrete task-level equivalent indication. Therefore, this finding supports an empirical approach to suggesting socioeconomic transition research relative to responsible AI implementation policies, socioeconomic adjustment resources, and labor force transition financing, as it substantiates a real-world basis for compelling the policy sooner than later based on documented findings emphasized by this demo.

Conclusion
----------

Spurred by the lack of regulation and awareness of current AI abilities in the workforce, this project provides a crucial solution: incentives toward better understanding the use of AI in the workforce and developing policies to address misuse. The GDPval benchmark provides a multifaceted dataset with prompts for tasks of diverse sectors, adding reference files as needed to provide context as a human employee would possess. Prioritizing the current capacity of AI agents that have overtaken tasks done at a computer, given the proper material, models can be compared to one another, and what a human would do in that same field. In cases of total failure in providing what a task is asking for, a civil society sector may not be surprised by how AI can “do their job” as a generalist with seemingly expert-level knowledge. Though in situations where an AI model matches or outmatches the work of those in crucial fields such as finance, the reactions may vary; the optimist may shudder, while the legislator is compelled to push a bill requiring transparency of AI usage by companies, changing the minds and hearts of those who are unaware of what AI can truly do. The poster of this project can be viewed [here](https://docs.google.com/presentation/d/1XnND8DmZZ6B49X2NFpQeYVx9rbygIN_4_MloIbEd06g/edit?usp=sharing).  

**Figure 2**

*Poster  for the Supervised Program for Alignment Research Demo Day* 

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/c74a44aa204809ee604e85bbada96a2a2051baeae5d41bc6.png)

References
----------

Measuring the performance of our models on real-world tasks. (2025, November 3). Openai.com.         [https://openai.com/index/gdpval](https://openai.com/index/gdpval) 

Patwardhan, T., Dias, R., Proehl, E., Kim, G., Wang, M., Watkins, O., Fishman, S. P., Aljubeh, M., Thacker, P., Fauconnet, L., Kim, N. S., Chao, P., Miserendino, S., Chabot, G., Li, D., Sharman, M., Barr, A., Glaese, A., & Tworek, J. (2025). *GDPval: Evaluating AI Model Performance on Real-World Economically Valuable Tasks*. ArXiv.org. [https://arxiv.org/abs/2510.04374](https://arxiv.org/abs/2510.04374) 

​​OpenAI. (2024). *gdpval*. Huggingface.co. https://huggingface.co/datasets/openai/gdpval