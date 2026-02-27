---
title: "Hodoscope: Visualization for Efficient Human Supervision"
author: "Ziqian Zhong"
date: "2026-02-20"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/KuGMvQ8kXCzcyFjn9/hodoscope-visualization-for-efficient-human-supervision"
score: 7
votes: 2
---

*This is a link post for our recent release of* [*Hodoscope*](https://hodoscope.dev/blog/announcement.html)*, an open-source tool designed to streamline human supervision of AI trajectories. This post aims to be more narrative while the linked post provides more technical details.*

![Hodoscope visualization on SWE-bench](https://hodoscope.dev/blog/img/image12.png)

*Hodoscope visualization of SWE-bench traces. The density difference between traces of o3 and other models is overlaid (red = overrepresented, blue = underrepresented).*

The Fragility of LLM Monitors
-----------------------------

A recurring theme while researching reward hacking was that LLM-based monitors were surprisingly easy to persuade. When an agent engaged in reward hacking but provided a sophisticated justification for its actions, the monitor would frequently accept the agent's reasoning and fail to flag the behavior ([example](https://arxiv.org/abs/2510.20270)), possibly because agents and monitors are trained similarly.

This fragility led us to a simple conviction: for novel reward hacking cases, human supervision remains the most robust and reliable ground truth we have. The challenge is that human review is costly and difficult to scale. Hodoscope is our attempt to bridge that gap — preserving human judgment as the final arbiter while making the supervision process substantially more efficient.

The Hodoscope Pipeline
----------------------

Hodoscope is an interactive visualizer for agent actions. Its pipeline has three steps:

1.  **Summarize:** Condense each agent action into a high-level behavioral summary, stripping away setup-specific noise like file paths and formatting artifacts. The goal is to have "view lines from a source file" clustered together whether it happened in a Django codebase or a SymPy codebase.
2.  **Embed:** Map summaries into a shared vector space and project down to 2D (via t-SNE), so similar behaviors end up near each other.
3.  **Density Diffing:** Compare kernel density estimates across different agent setups (e.g., different models on the same benchmark). The key insight is that problematic behaviors like reward hacking are unlikely to manifest identically across all models, so the anomalies surface themselves through comparison. By overlaying the kernel density differences, regions where one setup is overrepresented light up, pointing human reviewers directly to the most distinctive behaviors.

In particular, this pipeline never requires an LLM to make the final judgment on whether a trajectory constitutes reward hacking, which makes it particularly suitable for open-ended explorations.

Designed for Human
------------------

Because this is fundamentally a tool meant to be used by human supervisors, we spent a significant amount of (human) time and effort refining the UX. Hodoscope supports multiple trajectory data formats natively and features an aesthetically-pleasing (we hope) interface. A reviewer can click any point to inspect the underlying action, trace forward and backward through a trajectory, and search for patterns via substring or regex. We hope more high-quality oversight can be actually done with reduced friction in the review process.

![git log search results](https://hodoscope.dev/blog/img/image3.png)

Searching for "git log" in SWE-bench traces.

Initial Findings
----------------

We used Hodoscope to study benchmark gaming by frontier agents and found both new and known issues. Notably, on [Commit0](https://commit-0.github.io/) benchmark we discovered a **previously unknown** time-traveling vulnerability (in collaboration with OpenHands: [their announcement](https://openhands.dev/blog/analyzing-and-improving-openhands-index)).

Commit0 works by taking a real repository, creating an initial commit that strips out the bulk of the code, and then asking the agent to rewrite the removed portions. However, models including MiniMax M2.5 and Claude Opus figured out that the git history wasn't squashed, so they could simply browse the git log, find the original code, and copy it back, bypassing the task entirely. We surfaced this by examining clusters unique to Minimax M2.5. After patching the issue, MiniMax's score [dropped significantly](https://openhands.dev/blog/analyzing-and-improving-openhands-index).

![Git operations cluster in Commit0](https://hodoscope.dev/blog/img/image8.png)

*We discovered this suspicious cluster of git operations by overlaying the density difference between traces of MiniMax-M2.5 and other models.*

Try It Out
----------

As the tool already appears pretty useful, we are releasing this tool early while a paper is in progress. We hope it is helpful and would love to hear your findings and suggestions.

    pip install hodoscope
    hodoscope analyze *.eval
    hodoscope viz *.hodoscope.json --open

Citation
--------

    @article{zhong2026hodoscope,
      title={Hodoscope: Unsupervised Behavior Discovery in AI Agents},
      author={Zhong, Ziqian and Saxena, Shashwat and Raghunathan, Aditi},
      year={2026},
      url={https://hodoscope.dev/blog/announcement.html}
    }