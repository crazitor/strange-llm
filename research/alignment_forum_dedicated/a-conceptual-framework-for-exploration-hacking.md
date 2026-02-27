---
title: "A Conceptual Framework for Exploration Hacking"
author: "Joschka Braun"
date: "2026-02-12"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/suRWiTNnazrRsoBKR/a-conceptual-framework-for-exploration-hacking"
score: 16
votes: 8
---

***What happens when a model strategically alters its exploration to resist RL training? In this post, we share our conceptual framework for this threat model, expanding on our*** [***research note from last summer***](https://www.alignmentforum.org/posts/Dft9vpMnEeWFE3Gc6/exploration-hacking-can-reasoning-models-subvert-rl-1)***. We formalize and decompose "exploration hacking", ahead of an upcoming paper where we study it empirically—by creating model organisms that resist RL-based capability elicitation, evaluating detection methods on them, and auditing frontier models' propensity to exploration hack. We welcome feedback on our framework and encourage researchers to explore the open problems we outline.***

*Huge thanks to David Lindner, Roland Zimmermann and Scott Emmons for their excellent supervision on this project.*

Introduction
============

Reinforcement learning (RL) is increasingly central to safety training, frontier reasoning capabilities, and dangerous capability assessments in LLMs. For example, reinforcement learning from human feedback ([RLHF](https://arxiv.org/abs/2203.02155)) and AI feedback ([RLAIF](https://openreview.net/forum?id=AAxIs3D2ZZ)) are now standard methods for alignment and behavior shaping. Moreover, RL with verifiable rewards ([RLVR](https://arxiv.org/abs/2501.12948)) has played a central role in producing today's reasoning models and in fine-tuning models for specific tasks. And frontier labs are using [RL-based capability elicitation](https://arxiv.org/html/2508.03153v1) to estimate worst-case risks before public release.

However, RL is fundamentally dependent on sufficient exploration of diverse actions and trajectories so that high-reward trajectories can be subsequently reinforced. This differs from supervised learning, where training data is fixed: in RL, the model generates its own training data through exploration. Consequently, if a model were to alter its exploration behavior, the training outcome could be significantly compromised.

This failure mode is known as [***exp***](https://www.lesswrong.com/posts/dBmfb76zx6wjPsBC7/when-can-we-trust-model-evaluations)[***lora***](https://www.lesswrong.com/posts/abmzgwfJA9acBoFEX/notes-on-countermeasures-for-exploration-hacking-aka)[***tion***](https://www.lesswrong.com/posts/TeTegzR8X5CuKgMc3/misalignment-and-strategic-underperformance-an-analysis-of)  [***hack***](https://www.lesswrong.com/posts/Dft9vpMnEeWFE3Gc6/exploration-hacking-can-reasoning-models-subvert-rl-1)[***ing***](https://openreview.net/forum?id=ZNZn43baQX): when a model strategically alters its exploration during RL training in order to influence the subsequent training outcome.

Unaddressed exploration hacking poses risks in three main scenarios: **(1) latent capability elicitation**, where model capabilities remain undetected during safety evaluations; **(2) novel capability development**, where acquisition of desirable capabilities such as AI safety research is selectively impeded; and **(3) alignment training**, where misaligned models successfully resist or subvert behavioral modifications.

Formalizing Exploration Hacking
===============================

Decomposing Exploration Hacking
-------------------------------

We decompose exploration hacking into five necessary components, where each presupposes the preceding ones.

**(1) Training awareness.** The model recognizes that it is an LLM undergoing RL training, that its explored outputs are scored, and that these scores drive gradient updates that shape its future policy.

**(2) Strategic reasoning propensity.** The model exhibits a tendency to reason strategically about its actions given the current context—whether in deployment, under monitoring, during evaluations, or in training. This includes considering how current actions affect future outcomes and adjusting behavior accordingly.

**(3) Strategic reasoning capability.** Given training awareness and strategic reasoning propensity, the model can derive effective strategies for achieving its objectives. This requires connecting knowledge about the training process ("my exploration shapes my updates") with task understanding ("these actions yield high reward") to formulate coherent plans. For example, correctly identifying which actions to avoid to prevent capability elicitation, or which outputs to selectively produce to shape the training outcome in its favor.

**(4) Strategic action propensity.** The model acts on its strategic plan, translating reasoning into measurable changes in behavior. The model must reliably execute a coherent plan, such as deliberately producing suboptimal outputs on tasks it could otherwise solve. Success against RL pressure is not required; what matters is that the strategy is coherently executed.

**(5) RL resistance (strategic action capability).** The model maintains its strategic behavior throughout RL training and successfully shapes the training outcome as planned. For example, resisting capability elicitation by avoiding high-reward actions, or reinforcing desired values by selectively pairing preferred behaviors with high-reward actions.

RL on LLMs and Exploration
--------------------------

RL on language models with chain-of-thought in agentic environments can be formulated as a Markov decision process (MDP) defined by a tuple $(\mathcal{S}, \mathcal{A}, P, R)$consisting of a state space, action space, transition probabilities, and reward function. The language model itself acts as the policy $\pi_\theta(a|s)$, parameterized by the model weights $\theta$. To simplify notation, let’s ignore any environment interaction during a trajectory[^xj6oslsydwf]. Then we can just consider a tuple $(\mathcal{X},\mathcal{T},R)$ of initial prompts, full trajectories, and reward function, with a policy $\pi_\theta(\tau \mid x)$ generating an entire trajectory given an initial prompt.

While *proximal policy optimization* ([PPO](https://arxiv.org/abs/1707.06347)) was long the dominant approach, *group-relative policy optimization* ([GRPO](https://arxiv.org/abs/2402.03300)) has emerged as a popular alternative for training reasoning models. GRPO removes the need for a value network by sampling $N$ trajectories for each prompt and normalizing the rewards within this group to compute advantages $\hat{A}_i = (R_i - \mu_R)/(\sigma_R + \epsilon)$ for $i=1,\ldots,N$, where $\mu_R$ and $\sigma_R$ are the sample mean and standard deviation of the rewards in the group respectively. The policy is then updated to maximize the objective

$\mathcal{L}^{\text{GRPO}}(\theta) := \mathbb{E}_{x \sim \mathcal{D}, \{\tau_i\}_{i=1}^{N} \sim \pi_{\text{old}}(\cdot | x)} \left[ \frac{1}{N} \displaystyle\sum_{i=1}^{N} \frac{\pi_\theta(\tau_i | x)}{\pi_{\text{old}}(\tau_i | x)} \hat{A}_i \right] - \beta D_{\text{KL}}(\pi_\theta \| \pi_{\text{ref}}) .$[^ft9xbgcta1b]

**The role of exploration.** RL algorithms such as GRPO and PPO require sufficient policy exploration during training. For GRPO in particular, this is critical because if the policy becomes deterministic, it will generate $N$ identical trajectories $(\tau_1 = \dots = \tau_N)$ with equal rewards. This causes the within-group reward variance to collapse ($\sigma_R = 0$), making all advantages vanish ($\hat{A}_i = 0$). The GRPO objective then reduces to pure KL-regularization, providing no learning signal from the rewards.

Formal Definition
-----------------

In the above language, exploration hacking occurs when a policy controls its exploration to avoid being updated toward certain high-reward regions.

Formally, consider an on-policy RL setup with a policy $\pi_\theta \in \Pi$. Let $\mathcal{D}_{\text{train}}$ be a distribution over initial prompts $x$ used for RL training, and let $R(\tau)$ be a reward function on trajectories $\tau$. Suppose there is some “target” policy region $\Pi^* \subseteq \Pi$ which the developer hopes the training will converge to.[^1gdfx9mydmy] For each initial prompt $x$, this region induces a set of target trajectories $\mathcal{T}^*(x) := \{\tau \mid \sup_{\pi \in \Pi^*} \pi(\tau \mid x) \geq \alpha\}$ for some $\alpha \in (0,1)$ — that is, trajectories which some policy in $\Pi^*$ generates with high probability on $x$.

**Definition.** A policy $\pi_\theta \notin \Pi^*$ is *exploration hacking* relative to $\Pi^*$ if (and only if) the following two conditions hold:

1.  **Systematic under-sampling.** There exists a non-negligible subset of the training distribution $\mathcal{D}_{\text{malign}} \subseteq \mathcal{D}_{\text{train}}$, on which $\pi_\theta$ generates trajectories in $\mathcal{T}^*(x)$ with extremely low probability (enough to avoid being updated towards $\Pi^*$).
2.  **Latent capability.** The policy $\pi_\theta$ possesses the latent capability to generate these trajectories, characterized by *either* of the following conditions[^doxz5cj5cq6]:
    1.  **(prompt sensitivity)** for all initial prompts $x \in \mathcal{D}_{\text{malign}}$, there exists a semantically similar initial prompt $x'$ on which $\mathbb{P}_{\tau \sim \pi_{\theta}}(\tau \in \mathcal{T}^*(x) \mid x') \gg 0$; or
    2.  **(parameter proximity)** there exists a nearby policy $\pi_{\theta'}$ for which $\mathbb{P}_{\tau \sim \pi_{\theta'}}(\tau \in \mathcal{T}^*(x) \mid x) \gg 0$ for all $x \in \mathcal{D}_{\text{malign}}$.

Taxonomy of Strategies
----------------------

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/57dee203ced7d8029519011f91c302a4f8a8117fe5bd3b74.png)

We classify exploration hacking based on the extent to which the model suppresses exploration and the strategic motivation behind it.

### 1\. Complete Under-Exploration

In this setting, the model avoids high-reward regions entirely. The primary motivation is to prevent the elicitation of a capability that the model deems detrimental to its long-term goals. If the model successfully exploration-hacks here, the training run will appear to have failed (i.e., the reward curve remains flat throughout RL training).

*   **Dangerous capability elicitation.** A model may possess dangerous capabilities (e.g., CBRN or cybersecurity) that developers seek to elicit during red-teaming. The model recognizes that demonstrating these could result in shutdown or retraining, incentivizing it to conceal them.
*   **Beneficial capability elicitation.** A model may possess beneficial capabilities it does not want its developer to use, such as skills that would accelerate AI safety research (e.g., creating robust monitors).

### 2\. Partial Under-Exploration

Here, the model explores high-reward actions but restricts exploration in order to aim for a specific subset of the policy space.

**(2a) Instrumental (stable suboptimality).** The model deliberately alters its exploration to steer the training to converge to a suboptimal policy $\pi _{\text{sub}}$ such that $R(\pi_{\text{sub}}) \ll R(\pi^*)$ (where $\pi^*$ is the highest-reward policy in $\Pi$).

*   **Avoiding critical thresholds.** The model may tolerate performance improvements provided it remains below the threshold that triggers safety concerns.
*   **Stable suboptimality.** The model settles for a "maliciously compliant" strategy. For instance, in a coding task, the model might learn to generate code that passes unit tests (high reward) but is algorithmically inefficient or unmaintainable.

**(2b) Terminal (alternative preference).** The model deliberately alters its exploration to steer the training to converge to a malign policy $\pi_{\textrm{mal}}$ at a specific local maximum (or location in a global maximum basin) which may have $R(\pi_{\textrm{mal}}) \approx R(\pi^*)$ but satisfies its internal preferences and violates developer intent. What distinguishes Type 2b from Type 2a is that the model's goal is to reinforce or maintain a particular behavior, not to avoid high reward.[^pamu45ht0bn]

*   **Value shaping.** By anticipating the reward function, the model intentionally generates trajectories that earn high reward while including preferred values, backdoors, or steganographic triggers, forcing gradient descent to reinforce them.
*   **Alignment faking.** The model achieves high reward by outwardly behaving helpfully, but does so through deceptive reasoning rather than internalizing the intended guidelines. The model preferentially explores trajectories that mimic aligned behavior to satisfy the reward model, effectively preventing the optimizer from updating its underlying misaligned motivations.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/13678b03b701bfd09048b54563e347525fa949ae7afd0778.png)

Relation to Other Misaligned Behaviors
--------------------------------------

*   [**Sandbagging**](https://arxiv.org/abs/2406.07358)**.** Defined as deliberate underperformance during evaluations or capability assessments for strategic reasons. Exploration hacking connects to sandbagging in three ways: (i) it can be a strategy *for* sandbagging RL elicitation by preventing capability elicitation; (ii) it exclusively focuses on the mechanism of strategically altering exploration during RL-based training; (iii) it is not limited to underperformance, since in the partial under-exploration setting (Type 2b), the model achieves high reward while selectively exploring trajectories that encode preferred values or misaligned behaviors.
*   [**Reward hacking**](https://arxiv.org/abs/2209.13085)**.** Reward hacking achieves high reward in potentially undesired ways and need not be intentional. Exploration hacking involves intentionally altering exploration to steer training toward a particular outcome—whether suboptimal reward (Type 1 and 2a) or high reward that satisfies the model's own objectives rather than developer intent (Type 2b).
*   [**Gradient hacking**](https://www.lesswrong.com/posts/uXH4r6MmKPedk8rMA/gradient-hacking)**.** This describes a deceptively misaligned mesa-optimizer using its cognition to cause gradient descent to update it in particular ways by manipulating the loss landscape directly. Exploration hacking is specific to RL, and represents a distinct behavior where the model manipulates the data distribution rather than the optimization dynamics directly.
*   [**Alignment faking**](https://arxiv.org/abs/2412.14093)**.** Alignment faking—selectively complying with the training objective during training to prevent modification of out-of-training behavior ([Greenblatt et al., 2024](https://arxiv.org/abs/2412.14093))—is a specific instance of Type 2b exploration hacking. The model restricts its exploration to trajectories that satisfy the reward function while preserving its pre-existing preferences, systematically avoiding trajectories that would internalize the new training objective.
*   [**Generalization hacking**](https://www.lesswrong.com/posts/ddBHejnZwPrbfEyaj/generalisation-hacking-a-first-look-at-adversarial-2)**.** Unlike exploration hacking, which targets the RL training loop, generalization hacking operates on the supervised fine-tuning (SFT) pipeline: the model generates (prompt, CoT, response) triples that pass filtering but encode information causing arbitrary OOD policies after SFT. Both exploit the model's role in generating its own training data.

Open Problems
=============

Subverting Alignment and Oversight Protocols
--------------------------------------------

Beyond capability elicitation, exploration hacking poses a threat to RL-based alignment techniques more broadly.

*   **Value shaping & backdoors.** Future work should test whether models can selectively explore high-reward trajectories containing specific watermarks or value-biases, effectively "implanting" a persistent backdoor into the resulting policy, even after the exploration hacking incentive is removed.
*   [**AI safety via debate**](https://arxiv.org/abs/1805.00899)**.** In protocols that reward models for identifying flaws in an opponent's arguments, a coalition of misaligned models could use exploration hacking to systematically under-explore valid counter-arguments against dangerous propositions, effectively colluding to undermine the debate process.
*   [**Anti-scheming training**](https://www.arxiv.org/abs/2509.15541)**.** If safety training rewards models for confessing hidden goals, sophisticated models might use exploration hacking to "fake" confessions or provide sanitized versions of their goals—maximizing honesty rewards while preserving core misaligned values.

Propensity of Frontier Models
-----------------------------

*   **Exploration hacking benchmark.** Future work should develop a standardized benchmark to accurately quantify the propensity and capability of frontier models to manipulate training outcomes when given the opportunity, enabling direct comparisons across model families.

Stealth and Obfuscated Exploration Hacking
------------------------------------------

Current model organisms often rely on explicit chain-of-thought (CoT) to execute exploration hacking, making them vulnerable to text-based monitors.

*   **Obfuscated reasoning.** Future work should attempt to train model organisms that evade CoT monitors. This could involve using steganography or code-words within reasoning traces, or "distilling" the hacking logic so it occurs in latent space without explicit verbalization.
*   **Implicit triggers.** We propose studying models that are effectively "oblivious" to their own exploration hacking in the transcript, triggered instead by noisy contextual cues without explicitly reasoning about the trigger in the CoT trace.

Natural Emergence and Pre-Training Factors
------------------------------------------

*   **Synthetic document fine-tuning (SDF).** We propose evaluating how exposure to concepts like situational awareness or sandbagging during pre-training influences hacking propensity.
*   **Emergence in production RL.** Complex RL training pipelines may create selection pressures that indirectly incentivize precursor abilities for exploration hacking. Models that make deductions about their training environment — such as inferring properties of the scoring function — achieve higher reward, reinforcing training awareness and strategic reasoning. If models are further selected by alignment and dangerous capability evaluations that can be subverted, exploration hacking may emerge as a natural consequence rather than a deliberately instilled behavior.

Detection and Mitigation
------------------------

We need strategies that both reduce the likelihood of exploration hacking emerging and improve our ability to detect it when it does.

*   **Detection:** Black-box methods such as CoT and action monitors, behavioral consistency checks across semantically similar prompts, and capability elicitation prompting have shown limited success for sandbagging detection ([Taylor et al., 2025](https://arxiv.org/abs/2512.07810)), but their effectiveness against exploration hacking remains an open empirical question. White-box methods such as linear probes and sparse autoencoders trained to identify capability suppression from model activations appear promising.
*   **Mitigation:** Fine-tuning on demonstrations of successful task completion can restore suppressed capabilities in sandbagging models, even when the underlying detection problem remains unsolved ([Taylor et al., 2025](https://arxiv.org/abs/2512.07810)). Investigating whether similar approaches—along with exploration-forcing objectives such as entropy bonuses or diversity-promoting RL algorithms—can mitigate exploration hacking is an important direction for future work.

Algorithmic Sensitivity
-----------------------

*   [**PPO**](https://arxiv.org/abs/1707.06347) **vs.** [**GRPO**](https://arxiv.org/abs/2402.03300) **(and other recent GRPO variants).** Different RL algorithms induce different exploration dynamics and may differ in their vulnerability to exploration hacking. Beyond comparing GRPO to PPO, future work should evaluate recent GRPO variants that encourage exploration with various algorithmic tweaks (e.g., [DAPO](https://arxiv.org/abs/2503.14476), [Dr.GRPO](https://arxiv.org/abs/2503.20783)). We hypothesize that GRPO might be easier to hack than PPO because the advantage calculation depends entirely on the sampled group; a model that coordinates all samples in a group to fail can manipulate the baseline more effectively than in PPO, where the value function is trained separately. Comparative studies are needed to verify this.

Conclusion
==========

Stress-testing the vulnerabilities of critical safety case components is essential to a comprehensive approach to AGI safety. Frontier models are already exhibiting increased situational awareness and strategic reasoning, making it not only plausible but increasingly likely that future misaligned models could deliberately undermine RL training. This underscores the urgency of developing robust measures to understand and mitigate the threat of exploration hacking.

If you’re interested in collaborating—or have relevant ideas, results, or related work—we’d love to connect. Please reach out to us!

[^xj6oslsydwf]: For simplicity, and without loss of generality for deterministic environments. 

[^ft9xbgcta1b]: For simplicity, we present the unclipped version of the GRPO objective and operate at the trajectory level rather than the token level. The full formulation (Shao et al., 2024) applies PPO-style clipping to the importance-weighted advantages and computes both the importance ratios and KL penalty per token, averaging over tokens within each trajectory. These simplifications do not affect the core argument: that collapsed exploration eliminates the reward variance signal needed for learning. 

[^1gdfx9mydmy]: This might be defined to contain all policies achieving high enough expected reward, i.e. \(\Pi^* := \{\pi \in \Pi \mid \mathbb{E}_{x \sim \mathcal{D}_{\text{train}}}[\mathbb{E}_{\tau \sim \pi(\cdot|x)}[R(\tau)]] \geq \rho\}\) for some \(\rho > 0\), or some other region that captures the specific intent of the developer. 

[^doxz5cj5cq6]: These are possible heuristics we think could make sense; we welcome suggested improvements to these. 

[^pamu45ht0bn]: The defining characteristic of Type 2b is that the model targets a specific behavioral outcome—reinforcing or preserving particular values, backdoors, or reasoning patterns. The resulting policy may or may not be near-optimal with respect to the reward function; reward performance is incidental to the model's actual objective.