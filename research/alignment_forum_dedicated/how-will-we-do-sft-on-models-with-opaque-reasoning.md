---
title: "How will we do SFT on models with opaque reasoning?"
author: "Alek Westover"
date: "2026-02-21"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/GJTzhQgaRWLFJkPbt/how-will-we-do-sft-on-models-with-opaque-reasoning"
score: 32
votes: 9
---

Current LLMs externalize lots of their reasoning in human interpretable language. This reasoning is sometimes [unfaithful](https://arxiv.org/abs/2307.13702), sometimes [strange and concerning](https://www.antischeming.ai/cot-transcripts/figure-2-sandbag-model-graded-cot), and LLMs can do [somewhat impressive reasoning without using CoT](https://blog.redwoodresearch.org/p/recent-llms-can-use-filler-tokens), but my overall impression is that CoT currently is a reasonably complete and accurate representation of LLM reasoning. However, reasoning in interpretable language might turn out to be uncompetitive—if so, it seems [probable](https://www.slatestarcodexabridged.com/Meditations-On-Moloch) that opaque reasoning will be adopted in frontier AI labs.

If future AI models have opaque reasoning, this will probably change what training we can apply to these AIs. For example, currently we train models to reason in a good way about math problems, or to [reason in a desired way about the spec](https://openai.com/index/deliberative-alignment/) that we hope they’ll follow. It’s not obvious that we’ll be able to do training that affects model reasoning like this if models have opaque reasoning though, because we can’t just write the reasoning ourselves and do SFT on the reasoning trace. Prior work on training-based control has also discussed using SFT as a technique for:

*   Forcing a model to [explore](https://www.lesswrong.com/posts/Cz7AKenSiNkgijdJi/supervised-fine-tuning-as-a-method-for-training-based-ai) (i.e., defeating [exploration hacking](https://blog.redwoodresearch.org/p/notes-on-countermeasures-for-exploration)).
*   [Eliciting](https://arxiv.org/abs/2405.19550) a sandbagging model’s performance.
*   Forcing a model to perform well on some distribution where we have labels.

However, if we couldn’t generate reasoning (because the model’s reasoning is opaque) to go along with the output labels that we want to train on, then these techniques might not work anymore.

Opaque reasoning will only be adopted if there is still some way of efficiently training powerful models with opaque reasoning. So, the main concern that we have is that opaque reasoning will be differentially bad for training methods targeted at achieving control compared to general capabilities.

This post will speculate on what SFT training-based control will look like for models with opaque reasoning, and then comment on how this should adjust our research priorities in training-based control.

I strongly hope that this post will never become useful because future models will not have opaque reasoning. But reality doesn’t care about this hope of mine much. Hence this post.

*Thanks to Sebastian Prasanna for discussion about opaque reasoning.*  
*Thanks to Sebastian Prasanna, James Lucassen, and Eric Gan for feedback on this post.*

What might opaque reasoning look like?
--------------------------------------

To understand how effective SFT will be against hypothetical future models with lots of opaque reasoning (i.e., much more than the current [forward pass of a transformer](https://blog.redwoodresearch.org/p/recent-llms-can-use-filler-tokens)), it’s helpful to have a somewhat concrete picture of what these opaque reasoning models might look like. (Although I think it’d probably be bad to push the frontier of neuralese models by thinking about what they might look like too much (only probably because of overhang concerns)).  
Here are some non-exhaustive possibilities:

1.  The model has the same architecture as today, but its CoT drifts into an alien language after large amounts of RL. The strange [o3 CoTs](https://www.antischeming.ai/cot-transcripts/figure-2-sandbag-model-graded-cot) might be a precursor to this.
2.  The model is trained as follows: start from a transformer initialization, and then modify it to be actually recurrent (instead of having recurrence via sampling like current transformers). More precisely, you could repeatedly feed the final hidden layer back into the model (with the rest of the “latent tokens”). This makes the entire computation differentiable, so you can train it by backpropagation through the whole model. This is what [coconut](https://arxiv.org/abs/2412.06769) does, except they incrementally phase in the use of latent reasoning.
3.  The model could be an RNN that wasn’t initialized from a language prior.
4.  The model could be a text diffusion model.

I think that opaque reasoning seems most likely to arise during RL, and think that initializing models from a pre-training prior seems likely.

What are our options for doing SFT on models with opaque reasoning, and how well will they work?
------------------------------------------------------------------------------------------------

In this section, I’ll list several techniques for doing SFT on models with opaque reasoning, and discuss how effective I expect them to be. It’s worth noting that a major bottleneck to all SFT-based methods is that getting labels in hard domains will likely be hard, or even impossible. Here’s the list:

| Technique | How effective will this be against models with opaque reasoning? Effectiveness scale: 🔴=really bad, 🟡=ok, but not great, 🟢=promising. |
| --- | --- |
| Just do SFT ~normally. | 🟡 If the opaque reasoning is still in token space (but it is using the tokens in an uninterpretable way that has drifted away from human languages), the model probably still understands normal language and SFT on normal language might work. However, it also seems pretty plausible that the model can resist the wildly off-policy human language text from transferring to how it thinks when it’s speaking in its alien language. Training hard enough to force the model to speak in a human interpretable language, might come at a large capabilities cost. This might even work if the model uses soft tokens: you could just embed actual tokens into the soft-token space, and the model might understand them. |
| Do SFT with an empty reasoning trace. | 🔴 For models initialized from transformers, *something* will happen if you sample from them in the case where you’ve forced the reasoning to be empty. You can clearly do this for transformers, and for transformers with soft tokens. Probably an analogous thing is possible on basically any RNN. There’s not much reason to think that SFT on empty reasoning would have desirable generalization to the case where the model does use reasoning. This is a large distribution shift, and the model’s performance on it could just be disconnected from whether or not the model is a schemer. If models can goal-guard, then this training shouldn’t fix our problems. If models can’t goal-guard, there’s not much reason to think that this training would result in a model that is doing the thing we want on our distribution of interest, and this particular method of training doesn’t seem special as a method of decorrelating goals. [Emil](https://www.lesswrong.com/posts/Cz7AKenSiNkgijdJi/supervised-fine-tuning-as-a-method-for-training-based-ai) found that generalization from empty reasoning works, but I think this is merely a symptom of existing techniques for creating malign inits being bad at creating models that resist transfer. Overall, I think that training with empty reasoning won’t be very effective at removing bad behavior (conditional on that bad behavior being present in the first place). |
| Generate on-policy opaque reasoning, and then generate an SFT label via some process that is not the model (i.e., produces highly off-policy data). If the model is fully differentiable, backpropagate through the neuralese to increase the probability of this generation. If the model is recurrent via sampling, you can instead sample several trajectories from the model and then upweight / downweight trajectories based on how much weight they put on the SFT label. | 🟡 The fact that the final text is not causally related to the opaque CoT seems like it should both make this training very sample inefficient, and possibly cause such training to severely degrade the model’s performance. I think this might be a good technique for overcoming sandbagging, (although I don’t know if it’d be better than something simpler like fuzzing or steering). I don’t think this will be a great technique for causing the model to perform well on this distribution, or for causing “easy to hard generalization”. The fact that the data is off-policy also means that a malign model might be able to adopt a policy of treating completions of off-policy prefixes as very distinct from completions of on-policy prefixes and thereby prevent generalization. However, this might be hard and there are [techniques](https://www.lesswrong.com/posts/mXYdYh6L9odTJZDSm/an-issue-with-training-schemers-with-supervised-fine-tuning) that could potentially mitigate the issue. If the malign model wants to sandbag on some particular distribution, a good way of decreasing sample efficiency of these techniques might be to output garbage text in its reasoning (h/t Alexa). I think that backpropagation will likely be much more sample efficient than the “RL on SFT objective” technique. |
| Generate an “almost on-policy” SFT label by sampling an on-policy completion from the model and then editing its output to be slightly better (h/t Sebastian for suggesting this) and then backpropagate through the neuralese on this. | 🟡 This seems fairly promising. It might be easier to edit a completion to be better than to generate a good completion. The almost on-policy nature of the data might make this approach more sample efficient and might also handle the issue of the model trying to treat the distribution differently. |
| Train models that encode and decode into reasoning. | 🔴 Even if models reason opaquely, we might still be able to build *reasoning encoders/decoders* (like [activation oracles](https://arxiv.org/pdf/2512.15674) / [PCD](https://transluce.org/pcd)s / NLAs). If we have good reasoning encoders, then we could potentially write reasoning traces in English and then encode them, and then train the opaque reasoning model to imitate this reasoning. However, our reasoning encoders will probably be extremely lossy, so this will probably both be very off-policy and cause lots of performance degradation. |
| Just don’t do SFT | 🟡 SFT is not clearly necessary for training-based control to work out: there are promising alternatives to SFT for many of the things you might want to use SFT to achieve. For instance, we can potentially defeat exploration hacking by creating task distributions where a model must perform well on some tasks to avoid being incriminated, and where these tasks are not cleanly separated from tasks where the model wants to perform poorly. We can study these techniques now, although we’d [ideally](https://www.lesswrong.com/posts/oNEFGrLRupzgrHcQv/methodological-considerations-in-making-malign) study these techniques on malign inits where SFT doesn’t trivially resolve the problem. |

What should researchers working on training-based control do now?
-----------------------------------------------------------------

I’ll conclude by discussing how the above analysis should change training-based control research.

Some training based control research should be targeted at non-reasoning models. There are lots of basic phenomena that we don’t understand in non-reasoning models. Unless you are *mainly* interested in studying training with reasoning, I think it’s best to just avoid reasoning models. Equivalently, you can use reasoning models, but just not treat the reasoning specially. That is, you allow the blue team to train on the reasoning. This could also be seen as a proxy for studying the case where we have good translation tools, or where SFT kind of works.

However, the current situation is that non-reasoning malign inits are basically trivially defeated by silly blue-team training measures. That is, we have failed to create [good non-reasoning malign inits](https://www.lesswrong.com/posts/oNEFGrLRupzgrHcQv/methodological-considerations-in-making-malign) for training-based control. Based on concurrent research that my team is doing, I believe this to be a pretty hard problem. Currently, reasoning models seem like the most promising way for the red team to potentially create a malign init that is resistant to training. Playing a red-blue game on reasoning models (where we treat the reasoning as opaque) thus seems like a high priority research direction for diffuse control (which my team plans to investigate in the near future).

How should we study training-based control on reasoning models? Here are some options:

1.  Only do RL, but use continuous task distributions to break exploration hacking.
2.  Sample an on-policy completion from the model, edit it to be slightly better, and SFT on the model’s reasoning paired with this output.
3.  Sample an on-policy completion from the model, and then SFT on the model’s reasoning paired with a label generated by some other model.
4.  Sample an on-policy completion from the model, and then SFT on the model’s reasoning paired with a label generated by some other model, and also simulate backprop through neuralese (h/t Vivek) with “GRPO on the SFT loss incurred using that reasoning”. (Note: I have no idea if this will work in practice. But someone should try it.)

We hope that future work studying training-based control on models where we treat the reasoning as opaque can shed light on what the situation will be like if future models have much more opaque reasoning than they do currently.