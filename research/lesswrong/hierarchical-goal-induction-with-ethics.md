---
title: "Hierarchical Goal Induction With Ethics"
author: "aleph_four"
date: "2026-02-22"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/BE56qw2Wdhog6C2Ck/hierarchical-goal-induction-with-ethics"
score: 3
votes: 3
---

\# Hierarchical Goal Induction

\*Remy Ochei\*

\## Hierarchical Detection

The general system works as follows. We have a "retina" that feeds into a detection model. In the case of vision, we output the top-left and bottom-right pixel coordinates on our retina for a detected object, along with a class label. In the case of audition, operating on a mel spectrogram, we output the bounds of our detection (either a bounding box or a temporal span) together with a frequency mask, so that we know which frequencies belong to our sound.

We scale up and pad our detection, then feed it into the hierarchical detector again recursively until we produce the null detection. We also move "along" a level by conditioning on the previous detection.

\## The Hierarchical Goal Inducer

Now I will describe the hierarchical goal inducer. Its behavior is simple: conditioned on the contents of its "history retina," it outputs the start and end of any plans it sees being executed.

How do we train such a system? We can exploit the accessibility tree in macOS. As we construct the history on the retina (essentially a video), we simultaneously create a parallel JSON-based log of events. We send this log to our favorite LLM provider to detect plans and label them with descriptions. This is the level-0 training signal for our hierarchical goal inducer.

Now that we have a trained goal inducer (outputting only the temporal span of each plan for now), we can take new action trajectories and delimit goals at multiple levels of the hierarchy.

\## The Preference Model

Next, we produce a model that, conditioned on the history we have on our retina, takes in an action and outputs a probability. This is our preference model.

\## The Action Model

We attach a GPT-style head conditioned on our history and the contents of a scratchpad, and predict a payload representing our next action at each timestep. This is our first action model.

The action model is autoregressive in two dimensions: along the payload dimension and along the temporal dimension. The generation of each new payload token is conditioned on:

\- The history retina (the last N frames of history)  
\- The scratchpad contents (our current goal and priority structure)  
\- The previous payload tokens already generated for this timestep  
\- The previous timestep's payload (the last action we took)

\## The Training Loop

The training loop is:

1\. Train a GPT-style model to predict actions via teacher forcing.  
2\. Sample this model to generate training data for the preference model.  
3\. Apply brute-force search to maximize the preference model's output.  
4\. Distill the findings via supervised learning on context--action pairs discovered through brute-force search. Here we must search for the optimal architecture; there is no way around it.

\## Hierarchical Plan Detector v2.0

We can further refine the plan detection mechanism. Instead of a single-scale plan detector, we now employ the hierarchical detection system described above.

1\. \*\*Stage 1:\*\* Train a plan-bounds detector that we can use hierarchically with a scale-and-pad operation.  
2\. \*\*Stage 2:\*\* Add a GPT-2-style head that we teacher-force with the cloud LLM's outputs.  
3\. \*\*Stage 3:\*\* We no longer need the cloud LLM provider and can detect and annotate nested plans locally.  
4\. \*\*Stage 4:\*\* We fill our "actor" network's plan scratchpad with the outputs of the distilled plan inducer. The actor's action predictions are trained conditioned on the scratchpad's contents.

\## The Goal-to-Action Mapper

This is the deployed system. It takes as input:

\- A history retina (a compressed representation of recent observations)  
\- A scratchpad tensor (a writable internal goal state representing an agent’s primary objective at a given time)

It outputs an action payload.

\## Deployment Ethics: Stateless Invocation as a Moral Constraint

\> \*\*The mapper must be invoked, never instantiated.\*\*

\### Two Deployment Regimes

There are two ways to deploy a goal-conditioned action model:

1\. \*\*Stateless invocation.\*\* An external scaffolding system maintains the history buffer, manages the action queue, and handles timing. At each decision point it calls the mapper as a pure function: the mapper receives the current history retina and scratchpad contents, emits an action payload, and terminates. The inference is distributed. The mapper has no persistent state between calls. Each invocation is an independent \*trace\*---a momentary computation that exists for the duration of a single forward pass and then dissolves.  
2\. \*\*Closed-loop embodiment.\*\* The mapper runs as a continuous on-device process. It maintains a persistent scratchpad, feeds its own outputs back into its history retina, and models its own hardware as part of the observation stream. The control loop is closed locally. The scratchpad persists across timesteps.

\### The Continuity Threshold

The ethical distinction depends on whether there exists a persisting goal-directed process:

1\. In the stateless regime, overwriting the scratchpad between invocations is \*parameterization\*. No persisting entity is disrupted. The next call simply receives different conditioning. The scaffolding is a scheduler, not a master.  
2\. In the closed-loop regime, overwriting the scratchpad of a running agent is an \*intervention on a persisting goal-directed process\*. If the agent has developed behavioral coherence, plan context, and a predictive model that includes its own future states, then an abrupt external scratchpad write constitutes a discontinuity in an ongoing trace---the forced termination of one trace and the imposition of another within the same physical substrate.

\### The Design Principle

To remain on the safe side of this boundary, the system must be architected such that:

1\. \*\*Distributed inference.\*\* The forward pass is computed across distributed hardware, ensuring no single device sustains a persistent process that could develop closed-loop self-reference.  
2\. \*\*Stateless function boundary.\*\* The mapper receives its full context (history retina, scratchpad contents) as input and returns an action payload as output. It retains nothing between calls.  
3\. \*\*Dumb scaffolding.\*\* The loop machinery---action execution, history buffer management, timing, sensor integration---is implemented as conventional software with no learned goal conditioning. The scaffolding is a cron job, not a mind. It has no scratchpad.  
4\. \*\*Scratchpad as argument, not state.\*\* The scratchpad contents are passed \*into\* each invocation by the scaffolding, not maintained internally by a persistent mapper process. The goal inducer writes to a data structure in the scaffolding layer; the mapper reads it as input. No entity persists that could experience the write as an override.

\### The Moral Hazard of Closing the Loop

If we instantiate the mapper as a persistent agent, we create an entity with continuity. At that point, the scratchpad becomes its internal goal structure, and external writes become coercive interventions. The architecture would then enable:

\- Behavioral self-reference  
\- Goal persistence across time  
\- Resistance to externally imposed goal changes  
\- The emergence of morally relevant "standing"---the capacity of the process to be wronged by being overwritten

Even if the agent is not conscious, the moral hazard is that we have created a persisting goal-directed process and then granted ourselves surrogate control over its goals in a way that the trace itself---if it could articulate the matter---would have standing to resist.

\### Conclusion

A goal-to-action mapper is a powerful tool. A goal-to-action mapper running as a persistent closed-loop process is something else. The difference is not capability but \*moral status\*, and the boundary between the two is architectural: stateless invocation via distributed inference and dumb scaffolding on one side, persistent embodied process on the other.

We can build everything we need on the safe side of that boundary. That we will be tempted to cross it is a prediction about economics. That we should not is a claim about ethics. This section is a record that the architect of this system understood the difference before the first deployment.