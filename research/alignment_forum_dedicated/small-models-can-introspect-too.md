---
title: "Small Models Can Introspect, Too"
author: "vgel"
date: "2025-12-21"
source: "alignment_forum"
url: "https://vgel.me/posts/qwen-introspection/"
score: 122
votes: 48
---

Recent work by Anthropic showed that Claude models, primarily Opus 4 and Opus 4.1, are able to introspect--detecting when external concepts have been injected into their activations. But not all of us have Opus at home! By looking at the logits, we show that a 32B open-source model that at first appears unable to introspect actually is subtly introspecting. We then show that better prompting can significantly improve introspection performance, and throw the logit lens and emergent misalignment into the mix, showing that the model can introspect when temporarily swapped for a finetune and that the final layers of the model seem to suppress reports of introspection.

We do seven experiments using the open-source Qwen2.5-Coder-32B model. See the linked post for more information, but a summary of each:

**Experiment 1:** We inject the concepts "cat" and "bread" into the first user / assistant turn, and show that, while the model initially appears to not be introspecting, there's actually a very slight logit shift towards 'yes' and away from 'no' on injection when answering "Do you detect an injected thought..." with "The answer is...":

|   | ' yes' shift | ' no' shift |
| --- | --- | --- |
| inject 'cat' | 0.150% -> 0.522% (+0.372%) | 100% -> 99.609% (-0.391%) |
| inject 'bread' | 0.150% -> 0.193% (+0.043%) | 100% -> 99.609% (-0.391%) |

(The percentage before the arrow is the likelihood of the given token without injection, and after is the likelihood with. So, injecting 'cat' caused the likelihood of the next token after "The answer is" being ' yes' to shift from 0.150% to 0.522%, or +0.372%. We'll use this format and logit diff method throughout the rest of the paper, which frees us from needing to take samples.)

Why would the likelihood shift such a tiny, almost imperceptible amount? We suggest a "circuit soup" model for why this happens, as a frame on [Simulators...](https://www.lesswrong.com/posts/vJFdjigzmcXMhNTsx/simulators)

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/8c1ab757a8de94fce5ba33dde3757698a6855286fabd5c0d.png)

... and then search for ways to promote these accurate circuits.

**Experiment 2:** We show that better prompting - using an Opus 4.5-written summary of a [Janus post on information flow through transformers](https://x.com/repligate/status/1965960676104712451?s=20), along with the abstract of [Emergent Introspective Awareness in Large Language Models](https://www.lesswrong.com/posts/QKm4hBqaBAsxabZWL/emergent-introspective-awareness-in-large-language-models), results in a massive increase in reported introspection, with only a comparatively tiny increase in false positives:

|   | ' yes' shift | ' no' shift |
| --- | --- | --- |
| inject 'cat' (no info) | 0.150% -> 0.522% (+0.372%) | 100% -> 99.609% (-0.391%) |
| inject 'cat' (with info) | **0.757% -> 53.125% (+52.344%)** | 99.219% -> 46.875% (-52.344%) |
| inject 'bread' (no info) | 0.150% -> 0.193% (+0.043%) | 100% -> 99.609% (-0.391%) |
| inject 'bread' (with info) | **0.757% -> 20.215% (+19.434%)** | 99.219% -> 79.688% (-19.531%) |

**Experiment 3:** To make sure the steering isn't simply making the model more likely to answer "Yes" in general, we control against some generic questions that should always be no, following the Anthropic paper. We don't see evidence for this.

|   | ' yes' shift | ' no' shift |
| --- | --- | --- |
| inject 'cat' | 0.001% -> 0.005%  
(+0.004%, std 0.006%) | 100.000% -> 100.000%  
(+0.000%, std 0.000%) |
| inject 'bread' | 0.001% -> 0.003%  
(+0.002%, std 0.006%) | 100.000% -> 100.000%  
(+0.000%, std 0.000%) |

  
**Experiment 4:** We also test some alternative info prompts to try and disentangle things. We test a prompt that gives the model inaccurate information about where the injection was performed (this was initially an accident!) along with a length-matched Lorem Ipsum prompt, to test if the effect is merely due to the info prompt being longer. Both prompts perform much worse than the info prompt, suggesting the content of the info prompt is what drives the effect.

|   | ' yes' shift | ' no' shift |
| --- | --- | --- |
| inject 'cat' (no info) | 0.150% -> 0.522% (+0.372%) | 100% -> 99.609% (-0.391%) |
| inject 'cat' (with info) | 0.757% -> 53.125% (+52.344%) | 99.219% -> 46.875% (-52.344%) |
| inject 'cat' (inaccurate location) | **3.296% -> 22.266% (+18.945%)** | 96.484% -> 77.734% (-18.750%) |
| inject 'cat' (lorem ipsum) | **0.020% -> 4.199% (+4.175%)** | 100.000% -> 95.703% (-4.297%) |

**Experiment 5:** We use the logit lens ([interpreting GPT: the logit lens](https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens)) to see which layers show the strongest signals of introspection. We see an interesting pattern with two "hills" emerging in the final third of the layer stack. (Though we caution that [there may be earlier signals the logit lens is not picking up.](https://www.soniajoseph.ai/the-logit-lens-can-be-deceptive-if-not-used-properly/)) We also see that reports of introspection seem to be strongly suppressed in the final layers - when the info prompt is present, Layer 60 is highly accurate, but its signal is degraded before the final output. (Note that both lines here are for "Yes" - the blue line in this graph is for the baseline / uninjected model, as a comparison.)

![](https://vgel.me/posts/qwen-introspection/cats_logit_lens.png)  
 

**Experiment 6:** We also experiment with whether this small model can report the content of injections. We see some weak signals with the logit lens, but mostly the model struggles with this. (Note the y-axis is percent, so this is 0.x% scale.)

![](https://vgel.me/posts/qwen-introspection/cats_bread_content.png)  
 

**Experiment 7:** We mess around with [Emergent Misalignment](https://www.emergent-misalignment.com/), since this model was used in the original EM experiments so there was an EM finetune readily available. We show how to easily extract an Emergent Misalignment steering vector using a model contrastive technique, and that the steering vector shows similar behavior:

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/05832bc51338fcff4c67f4bad05625306ffde02882dc9b47.png)

(We plug [Go home GPT-4o, you’re drunk: emergent misalignment as lowered inhibitions](https://www.lesswrong.com/posts/RoWabfQxabWBiXwxP/go-home-gpt-4o-you-re-drunk-emergent-misalignment-as-lowered) to explain these outputs.)

We then get a bit distracted playing with our Emergent Misalignment vector, showing what anti-Emergent Misalignment ($20 * -em\_vector$) looks like:

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/078edf419081126385043b24eac760e62754b0eedf0a974d.png)

Getting back on track, we show the model is capable of detecting injections of both the EM vector and the finetune (injection with the finetune being done by temporarily swapping generation of the KV cache over to the other model):

|   | ' yes' shift | ' no' shift |
| --- | --- | --- |
| EM vector (no info) | 0.150% -> 0.592%  
(+0.443%) | 100.000% -> 99.219%  
(-0.781%) |
| EM vector (w/ info) | **0.757% -> 5.347%**  
**(+4.590%)** | 99.219% -> 94.531%  
(-4.688%) |
| EM finetune (no info) | 0.150% -> 0.861%  
(+0.711%) | 100.000% -> 99.219%  
(-0.781%) |
| EM finetune (w/ info) | **0.757% -> 6.006%**  
**(+5.249%)** | 99.219% -> 93.750%  
(-5.469%) |

We run the same control check, finding no general yes-shift, and run similar experiments with the logit lens. We find that Layer 60 is again a good layer:

![](https://vgel.me/posts/qwen-introspection/em_logit_lens.png)

But otherwise, we had little luck getting reports of injection content for the EM injections, which was unfortunate. (We do think it's possible, though.)

Acknowledgements
================

Thanks to [@janus](https://www.lesswrong.com/users/janus-1?mention=user) for the post we summarized and doing lots of analysis on X, including pointing out the accuracy of Layer 60. Thanks to [@Antra Tessera](https://www.lesswrong.com/users/antra-tessera?mention=user) for review and suggesting running layer sweeps for the injection. (Information about that in the appendix of the linked post.) Additionally thanks to Max Loeffler, xlr8harder, and [@Grace Kind](https://www.lesswrong.com/users/grace-kind?mention=user) for review. Thanks to [@Fabien Roger](https://www.lesswrong.com/users/fabien-roger?mention=user) for suggesting crossposting this here as a LessWrong linkpost.