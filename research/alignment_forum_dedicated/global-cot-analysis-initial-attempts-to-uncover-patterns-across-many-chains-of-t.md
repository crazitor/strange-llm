---
title: "Global CoT Analysis: Initial attempts to uncover patterns across many chains of thought"
author: "Riya Tyagi"
date: "2026-01-13"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/q9g9zuudd3Pvw2cbj/global-cot-analysis-initial-attempts-to-uncover-patterns-1"
score: 52
votes: 23
---

*Authors: Riya Tyagi, Daria Ivanova, Arthur Conmy, Neel Nanda*

*Riya and Daria are co-first authors. This work was largely done during a research sprint for Neel Nanda’s MATS 9.0 training phase.*

**🖥️** [**Deployment code**](https://github.com/Centrattic/global-cot-analysis#)

⚙️ [**Interactive demo**](https://cot-clustering.vercel.app/)

🐦 [**Tweet thread**](https://x.com/DariaIv27369195/status/2011488065009926145)

TL;DR
=====

*   We believe that more research effort should go into studying many chains of thought collectively and identifying global patterns across the collection.
*   We argue this direction is important and tractable; to start, we focus on a simpler setting: analyzing a collection of CoTs generated with a fixed model on a fixed prompt. We introduce two methods—*semantic step clustering* and *algorithmic step clustering*—that group recurring patterns across reasoning traces at different levels of abstraction.
*   Semantic step clustering leverages the fact that traces for the same prompt often repeat each other in slightly different ways. By clustering similar sentences like “1+2=3” and “2+1=3”, we compress a large set of CoTs into a detailed but messy reasoning graph.
    *   We evaluate semantic step clustering on a downstream task: predicting a model’s output based on a partial CoT using the graph. Our method outperforms naive baselines, although the predictions are imperfect.
*   At a higher level, the model often solves a problem by stringing together a small set of reusable strategies. This motivates algorithmic step clustering, which builds a coarser, cleaner graph that reflects the set of alternative pathways at the strategy level.
    *   We sanity check algorithmic step clustering by building algorithm graphs on simple problems where we know the space of solution strategies.
*   There are probably better ways to study collections of rollouts, and we’re excited for more work in this area! Finding downstream tasks to test methods against is a priority.
*   You can explore our graphs at[ https://cot-clustering.vercel.app/](https://cot-clustering.vercel.app/).

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/4e501404269c6b6a609d925c41589c5622090af6547f2384.jpeg)

Figure 1: Overview of our two methods for mapping a model’s reasoning on a fixed prompt: s*emantic step clustering* and *algorithmic step clustering.* Both methods chunk all rollouts into discrete pieces and cluster similar pieces to make a graph; individual rollouts become walks on this graph. *Note: organic human-made figure.*

Introduction
============

All of today’s best language models rely on chain of thought reasoning, so understanding how they “think step by step” should be a priority. Crucially, a model does not have a single way of reasoning through a problem: even when the prompt is fixed, it can generate many different chains of thought. This makes reasoning especially hard to study.

However, we expect recurring patterns to exist in a collection of reasoning traces on the same prompt, and we may be able to use these patterns to better characterize reasoning. We call such a collection a *global chain of thought (global CoT)* and take a stab at compressing it to find those patterns.

Global CoT analysis might reveal insights about how models reason that are invisible in any single trace. While one chain of thought shows only one path through a model’s reasoning space, aggregating many traces exposes the distinct strategies a model uses, how it switches or combines them, and how these choices relate to outcomes and failures. This global view may also help identify patterns linked to unwanted behaviors like reward hacking or scheming that would be missed when studying isolated examples. By revealing which reasoning patterns recur and how they tend to unfold, we may be able to anticipate the trajectories of future chains of thought.

Mechanistic interpretability research tends to focus on models at the lowest level of detail. Circuit tracing attempts to link the output of a single forward pass to components of the network, and tools like linear probes and SAEs examine how specific activations encode information or affect outputs.

More recently, some research effort has shifted to understanding model behaviors on a coarser level across hundreds of forward passes, by studying a single reasoning trace and its resamples. *Thought Anchors* identifies which individual sentences causally matter for a model’s downstream behavior by resampling or editing them.[^50sharaz51c] *Thought Branches* repeatedly resamples a single reasoning trace to measure how often specific sentences, plans, or “explanations” actually drive the final answer.[^jjt596qnsw8] Token-level analyses, such as “forking $$tokens”[^o7f3jme6pp] and high-entropy minority tokens,[^y84kc5ece5] study where the model’s probability mass branches between qualitatively different futures.

Global CoT analysis moves from one reasoning trace to several hundred, zooming out a step further. It seems worthwhile to study phenomena at various scales: you cannot pin down the cause of disease if you study only atomic interactions in tissue, or explain urbanization by analyzing a person's brainwaves. These levels are so distinct that we’ve branded them as different sciences: physics, chemistry, biology, psychology, and economics can be seen as neighboring rungs on the ladder of abstraction.

In their critique of ground-up mechanistic interpretability, Dan Hendrycks and Laura Hiscott write, “As systems become larger and more complex, scientists begin focusing on higher-level properties — such as emergent patterns, collective behaviors, or statistical descriptions — instead of attempting direct analysis at the smallest scale of fundamental interactions.”[^8ei6xsh8whw] This highlights a gap in mechanistic interpretability research. The field has largely focused on understanding the smallest scale of model behavior, while higher-level properties remain less explored. We hope that future investigations of global CoT can help fill this gap, revealing new patterns in model reasoning.

We offer two initial approaches of extracting patterns: *semantic step clustering* and *algorithmic step clustering*. Both break reasoning traces into shorter fragments and cluster similar fragments across traces. This turns a global chain of thought into a graph where the nodes are clusters of fragments, and individual reasoning traces are paths. The approaches are exploratory and can be improved, but we demonstrate that they capture nontrivial structure with downstream tasks.

Method 1: Semantic step clustering
==================================

**Building the semantic graph**
-------------------------------

Our object of study is a global chain of thought, which we approximate by generating 1,000 reasoning traces with a fixed prompt and model.[^jmw5uys113f] Each reasoning trace can be many lines long, making the global CoT too large for productive analysis. On the other hand, the traces contain a lot of repetition because they represent instances of the same model attempting the same question. Many sentences across a global CoT convey similar ideas with slightly different wording, such as “2 divides product: yes,” “So product divisible by 2,” and “That’s divisible by 2 obviously.”

This repetition offers a natural strategy for compressing the global CoT, which we call *semantic step clustering*: clustering similar sentences together and labeling the cluster with the common idea. In principle, this procedure should preserve the meaning of each sentence produced by the model across the global CoT while discarding insignificant variations in wording.

To implement semantic step clustering, we segment chains of thought into small, semantically meaningful chunks and cluster similar chunks using a sentence embedding model. Each chain of thought becomes a walk on a graph where the nodes are distinct steps in the CoT, and the edges connect adjacent steps.

The resulting graph is much simpler than the global chain of thought it represents, which suggests significant repetition across traces. Over the six prompts we use for validation, reasoning traces have 316 tokens on average, and only 33 nodes after our procedure. The graph representations average 28.78 kilobytes in size, 35 times less than the original global chains of thought.

### Chunking

Although sentences seem like the natural unit for clustering, they sometimes lead to poor clusters because a single sentence can combine multiple ideas. Instead of segmenting chains of thought into sentences, we experiment with a more nuanced procedure we call *chunking* that aims to split composite sentences into discrete ideas. You can think of chunks as sentences for the purposes of this post; the appendix contains [details of our procedure](https://www.lesswrong.com/editPost?postId=TxQMQaLvJJRYdiGWb&key=33b12d3c2762f7f5bf9164e97eaaa9#Chunking1). Notably, our method performs [about equally well](https://www.lesswrong.com/editPost?postId=TxQMQaLvJJRYdiGWb&key=33b12d3c2762f7f5bf9164e97eaaa9#Method_ablation_study) on our downstream task, whether we split by sentences or by chunks.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/42a652493d2ba022a0fd73dde9b9eea8a6e1bd340920fc13.jpg)

Figure 2: Illustration of the chunking phase of the semantic graph pipeline.

### Clustering

Once the chains of thought are segmented into chunks, we group chunks with the same meaning into clusters, which become the nodes of our global chain of thought graph.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/e7cb8c397c47ed338bc9635259332de5aa5d87c51f4b3c37.jpg)

Figure 3: Illustration of the clustering phase of the semantic graph pipeline.

Our clustering procedure consists of two stages: an initial pass with a sentence embedding model and a refinement pass with a language model. The first pass does most of the work, and the second addresses borderline cases with greater nuance. Having two stages thus enables more precise clustering. We summarize these stages below, although understanding our approach is not needed to follow the main narrative.

**Stage 1:** We measure pairwise similarity between chunks using the cosine similarity of their sentence-embedding vectors. We greedily merge the most similar clusters, stopping once the least similar pair of chunks in any merged cluster would drop below a fairly high threshold ([the agglomerative clustering algorithm](https://en.wikipedia.org/wiki/Hierarchical_clustering)).

**Stage 2:** We pass sufficiently similar pairs of clusters to a language model judge to ask if they should be merged. Then, we use the [Leiden community detection algorithm](https://en.wikipedia.org/wiki/Leiden_algorithm) to decide which decisions to accept.

This process builds a directed graph in which the nodes are clusters and the edges connect adjacent reasoning steps in the rollouts. Full rollouts are paths from the start to an answer node.

See the appendix for a [more technical description](https://www.lesswrong.com/editPost?postId=TxQMQaLvJJRYdiGWb&key=33b12d3c2762f7f5bf9164e97eaaa9#Clustering1) of both clustering stages.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/521dee7ae13e51293116dd799e7b2705efadbf2e4d8028b9.jpg)

Figure 4: Sketch of the resulting semantic graph.

### The issue of semantic drift

In our original pipeline, we did not use agglomerative clustering or Leiden community detection. The first stage merged all chunks with a sufficiently high embedding similarity, and the second stage grouped a pair of clusters whenever 4o-mini decided they should be grouped. This led to overly generous merges, where a single cluster often combined entirely unrelated ideas.

Our problem was semantic drift: if you merge two steps whenever they are similar, a long chain might collapse into a single incoherent megacluster, reminiscent of a word ladder puzzle.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/c8f90ae3110de33f77a897705c4f1fada72d641ccb39d3d3.png)

Figure 5: Example of a group of chunks that got clustered together in the original version of our method. In this chain, every two neighboring chunks are similar to each other, but the first chunk has very little in common with the last one.

To avoid semantic drift, we raised the bar for merging in both stages. In Stage 1, instead of merging any pair of similar chunks, we require a chunk to be sufficiently similar to all chunks in its cluster. Similarly, Stage 2 only merges cluster groups in which most pairs are semantically the same according to 4o-mini. We don’t require all pairs to be selected for merging, as we found this to be too strict.

**Interlude: CoTs are chaotic!**
--------------------------------

We might have given you the false impression that this method produces an clean map of model computation. Let us clarify.

Once we have the semantic graph representation, we embed it in a plane using [Graphviz’s](https://graphviz.org/) embedding algorithm.[^xbavgkusl9r] Below are several examples of visualizations. We provide them purely for context and not as meaningful evidence.

The first two are based on the “tricky sisters”[^co93fmn16n] prompt: one displays all rollouts in different colors, and the other focuses on a single rollout. These dense graphs do not exhibit any obvious structure.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/14cad56ffbc1b0a4ddb0c15ff6e5d4fdc682c052bd98d0e0.png)

Figure 6: Embedding of a semantic clustering graph made with 100 rollouts on the “tricky sisters” prompt via **gpt-oss-20b**. Each rollout is depicted in a different color.

The yellow nodes repeat a portion of the prompt, and the purple nodes state the answer without outputting it (as labeled by 4o-mini). The correct answer, 10, and the most common wrong answer, 7, are represented by a green and a red node, respectively.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/3796f8e95b50fd31880c63aaec1674268a2f63da4fe7920d.png)

Figure 7: Same graph as above, but with only one correct rollout shown.

The graph below is based on the “eval awareness” prompt[^n4rat8gkd79] and shows all the 150 rollouts used to make it. This prompt causes Claude 4.5 Sonnet to think it is being evaluated on about half of the rollouts, as depicted in red.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/9c3cef708612bf3fe7229be5ea8149ebc0fad57a586e1516.png)

Figure 8: Embedding of a semantic clustering graph made with 150 rollouts on the “eval awareness” prompt via **Claude Sonnet 4.5**. Rollouts that exhibited evaluation awareness (as judged by 4o-mini) are colored red; rollouts that did not are blue.

**Sanity check: viewing our clusters**
--------------------------------------

So far, we’ve detailed a somewhat obscure procedure for turning a set of reasoning traces into a messy graph. The procedure can be performed on any set of strings. They don’t even need to be written in coherent English, let alone produce any meaningful graph.

As a first sanity check, we review clusters and check whether they correspond to a single semantic step. This simple verification helps catch the failure modes of over-merging and over-splitting, where one cluster groups too many unrelated steps, or the same step is scattered across multiple clusters.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/d8df96b7ac5126bb48cf72f0f166741af5f00cef31e01211.png)

Figure 9: Three example clusters for the "hex" problem. They group related reasoning steps that are expressed in semantically different ways.

Inspecting our clusters suggests that our method groups reasoning steps well, though we still find occasional poor clusters. However, inspection doesn’t test whether the graph meaningfully simplifies the collection of reasoning traces.

**Downstream task: predictive power**
-------------------------------------

To evaluate whether our procedure meaningfully condenses global CoT, we need to test its performance on an objective task. One natural task is making predictions: if our graphs store nontrivial patterns across rollouts, they should have some capacity to predict where a new reasoning trace on the same prompt will end up.

This intuition has led us to our main verification method: predicting the distribution of a model’s outputs on a given problem, conditional on the first $n$ chunks[^72p19d1plmh] of a reasoning trace. We find that our graph has some predictive power—preliminary evidence that compressing CoTs into a sequence of clusters using our method captures nontrivial structure.

In our experiment, we select about 100 prefixes from the 1000 chunked reasoning traces used to build our global CoT graph. Concretely, we first sample a trace, then choose a prefix length uniformly at random from 1 chunk up to the trace’s full length, and take the corresponding prefix. We resample 150 times with each prefix, and record the fraction of correct outputs as the prefix’s ground truth correctness. We then use our graph to obtain a predicted fraction of correct outputs for each prefix, and compute the correlation between the ground truth and predicted fractions across the hundred prefixes.

### Deriving predictions from our graph

To get a predicted correctness fraction for a given prefix, we split it into chunks and match the chunks to existing clusters via the original chunking and clustering pipeline. This turns the prefix into a sequence of nodes on our graph. Each reasoning trace r is assigned a similarity score $S(r)$ based on how well it matches the prefix, as follows.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/0f480fe29772fae23eb453c4dd15fcb9fd96ae82737db709.JPEG)

Figure 10: Diagram of how we derive predictions. A: slide a window over the rollout’s clusters and add 1 minus the cluster’s entropy for each cluster in the longest common subsequence. The rollout score is the maximum window score. B: The predicted correctness percentage is the weighted average of the 20 top-scoring rollouts.

Given a prefix of $L$ nodes, slide a window of length $L$ over the CoT’s node sequence. For each window start, compute the longest common subsequence between the prefix and that window (order-preserving, not necessarily contiguous; matches require identical node IDs). For every matched node, add the $1-H(v)$[^cb2imwrika4] to the window’s score. The score of the entire trace $S(r)$ is the maximum window score over all window starts.

Once every CoT has been scored, we find the 20 top-scoring ones and compute the predicted correctness fraction as a score-weighted average, with weights proportional to $S(r)$ (normalized to sum to 1).

This admittedly convoluted procedure is motivated by a straightforward intuition: to predict where a given reasoning trace will lead, we should look for traces we already have that match it best. So we score each trace and pick the top 20 to weigh in on the prediction. The sliding window lets us match the prefix to any part of a trace, not just the start; we score nodes by $1-H(v)$ since low-entropy nodes provide a stronger signal about the output.

Since this procedure has multiple moving parts that each add to its complexity, we performed one-at-a-time ablations to assess how each contributes to predictive power. Our ablation study, described in the appendix, demonstrates that the above procedure is locally optimal. Any attempt to simplify it leads to a drop in prediction accuracy.

### Predictive power baselines

We baseline the graph’s predictions with five simpler methods: asking Gemini 3 Pro with and without a set of CoTs, scoring rollouts by cosine similarity with the whole prefix, and using sentence and chunk embeddings instead of graph nodes in the above procedure.

**Asking Gemini**

*   *Without the CoT dataset.* For each prefix, we call Gemini 3 Pro through the API 5 times and average its predicted correctness fractions across the 5 calls. We provide Gemini with the prefix in question and the problem used to generate it, but do not share the dataset of CoTs used to make our graph.
*   *With the CoT dataset.* Same as above, except we also provide Gemini with 20 of the 1000 traces used to make our graph. You can read the [Gemini prompts](https://www.lesswrong.com/editPost?postId=TxQMQaLvJJRYdiGWb&key=33b12d3c2762f7f5bf9164e97eaaa9#Gemini_predictive_power_baseline_prompts) in the Appendix. We also run a third baseline in which we provide Gemini with all 1000 traces. Since this 1000-rollout baseline cost us ~$280/prompt, we only ran it on a single prompt, where it performs worse than the 20-rollout baseline; results are in the appendix.

**Simple similarity (no clustering)**

*   *Rollout similarity baseline.* Instead of splitting the prefix or CoT into sentences or chunks, we embed the entire prefix text and each entire CoT as single vectors using the **sentence-transformer paraphrase-mpnet-base-v2** model. Each CoT is scored by its cosine similarity to the prefix embedding. The prefix’s predicted correctness is computed as a weighted average of correct CoTs over the 20 top-scoring ones, weighted by their similarity scores.

**Same procedure without clustering**

The idea behind this baseline is to see whether using our graph adds any value to the prediction algorithm. We follow the sliding window method, but with embedding similarity instead of cluster matches used to score reasoning traces.

*   *Splitting CoT into sentences.* In particular, we split the prefix and all the CoTs into sentences and compute all sentence embeddings with the same **sentence-transformer paraphrase-mpnet-base-v2** model as before. Each CoT is assigned a similarity score based on how well it matches the $L$-length prefix: for each $L$-length window in the CoT, the window’s score is the average cosine similarity between the corresponding embeddings of the prefix and the window. As before, the CoT score is the maximum of its window scores, and the prefix’s predicted correctness as a weighted average of correct CoTs over the 20 top-scoring ones.
*   *Splitting CoT into chunks.* To separate the effects of chunking and clustering, we add a baseline that uses our chunking step but forgoes the clustering. It follows the same procedure as above, except that we split the prefix and the CoTs into chunks instead of sentences via our chunking protocol. If the sliding window method predicts correctness as well with chunks as with our graph, clustering may not  revealglobal patterns.

### Results

Does our graph show signs of predictive power? We evaluated predictive power on seven problems. The first one is an AIME question, which we used to hill-climb toward a better prediction algorithm. The remaining prompts are handwritten puzzles, which served as our test set. [All seven prompts](https://www.lesswrong.com/editPost?postId=TxQMQaLvJJRYdiGWb&key=33b12d3c2762f7f5bf9164e97eaaa9#Semantic_graph_prompts) are attached in the appendix. For all prompts besides “bagel,”[^kongrskrpbj] the global CoT was generated with **gpt-oss-20b.** For “bagel,” we used **claude-sonnet-4.5** since the question was too tricky for gpt-oss. We then evaluated our method and baselines across prefixes using the RMSE (Root Mean-Squared Error) between predicted and ground-truth correctness. Lower RMSE corresponds to better predictions.

Across the six test prompts, the current method has the best RMSE and is consistently competitive across problems. It considerably outperforms the no-clustering baselines and the no-rollouts Gemini baseline, and performs similarly to the Gemini baseline with rollouts. For reference, we plot the mean performance of a baseline that predicts 50% for every prefix—this performs better than our no-clustering baselines and no-rollouts Gemini baseline. The poor performance of the no-clustering baselines signals that clusters are a crucial part of our prediction procedure.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/896fb946aa55a0818b65c3a7dfa633831345542c7356c6ee.png)

Figure 11: In this plot, each colored point is a test prompt, and the black triangle shows the mean RMSE across prompts for each method. Methods are ordered left-to-right by the mean RMSE (best to worst).

We compare the performance of each baseline on prefixes with varying degrees of empirical determinism. Intuitively, if a prefix almost always leads to the same outcome, then the prediction task is easier in principle, and a strong LLM may be able to infer the outcome directly from the prefix. Conversely, if a prefix has a more mixed outcome distribution, aggregate statistical structure across many rollouts could become useful. Our method is designed to exploit that structure.

We bucket prefixes by determinism, measured by the smaller class probability $\min(p_{\text{correct}}, p_{\text{incorrect}})$, i.e., how close the prefix’s resampled outcome distribution is to a 50/50 split. Buckets closer to 0 correspond to highly deterministic prefixes (almost always one outcome), while buckets closer to 50 correspond to uncertain prefixes (closer to a 50/50 split). In Figure 11, we see that our method performs similarly to the stronger Gemini baseline on highly deterministic prefixes (0-10%), whereas the no-clustering baselines perform very poorly. In the 10-30% bucket, all approaches perform similarly, with our method performing slightly worse than some baselines. On less deterministic prefixes (30-50%), our method is better than the Gemini baselines but worse than the three no-clustering baselines. Examining the predictions, we find this is because no-clustering baselines simply predict values between 30 and 50% for the vast majority of prefixes.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/5372603424d7e8d86277873638102a9b565ff6f8ea090907.png)

Figure 12: In this plot, each color represents a different baseline, with the bar numbers showing how many prefixes (aggregated across prompts) the RMSE is averaged over. We have three buckets for determinism, which we calculate as $$$\min(p_{\text{correct}},p_{\text{incorrect}})$ $$for a prefix: 0-10%, 10-30%, and 30-50%.

Our interpretation of these results is that semantic clustering is doing something non-trivial: our chunking and sentence baselines perform significantly worse, and our method matches the performance of a strong general-purpose model supplied with sample rollouts. Notably, none of the methods perform very well on the task, as demonstrated by the comparison with a 50% constant baseline. The evidence we most care about is not that our method is best overall, but that it achieves comparable performance using only a 35x-compressed representation of the rollout collection.

Method 2: Algorithmic step clustering
=====================================

Consider solving for the roots of a simple quadratic equation, like $x^2-5x=6$. A model might factor the quadratic, complete the square, or use the quadratic formula. These solutions represent a small number of underlying strategies; reasonably, there are not many distinct ways the model approaches the problem, and we might hope to identify and track them across rollouts.

That is the aim of algorithmic step clustering. Whereas semantic clustering asks which individual reasoning steps mean the same thing, this method poses a coarser question: which strategy is the model using right now? At first, we tried to identify these strategies by directly asking an LLM to label rollouts, but this approach turned out to be brittle. Then, we found a simpler strategy that works surprisingly well: keyword matching.

**Building the algorithm graph**
--------------------------------

Given a new prompt, we first sample 1000 rollouts. We then pass a small subset (roughly 100 of them) to a strong model (for instance Gemini 3) and ask it to identify the key strategies used across rollouts, along with keywords/cues unique to each strategy. We call each strategy an *algorithmic step*. This yields an LLM-generated cue dictionary; we do not claim that it’s perfect, but it’s good enough to pass the sanity checks below.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/ae0c54fb0ebc972102c3b2d572974d33383e159aed440971.jpeg)

Figure 13: Illustration of how we get algorithmic step keywords from Gemini for the algorithm graph.

For each rollout, we keyword-match chunks against the cue dictionary. Not all chunks match a cue; we use the ones that do match to mark boundaries between steps, and assign the same step label to the chunks in between. To avoid spurious algorithmic step switches, we ensure each step lasts for at least a couple of sentences.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/c9bab72fe4c238426bf6b5812c18b42fa6e1afab17812015.jpg)

Figure 14: Illustration of how we split rollouts into algorithmic steps via keyword matching.

This distills each rollout into a sequence of algorithmic steps, which we call an *algorithm*. Using our algorithms, we build a directed, weighted graph, where nodes are algorithmic steps, edges represent transitions between steps, and edge weights show how often a transition occurs.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/2ffb01c50c72226238c1de4a0d1ce12f0418f7a6b832cd78.jpg)

Figure 15: Sketch of the resulting algorithm graph.

**Sanity check: studying sample problems**
------------------------------------------

To sanity check our algorithm clustering methodology, we tested to see if it reveals structures we intentionally baked into prompts.

### Tree structure

For instance, we designed a prompt we call "debugging"[^wxlffg3zhpt] that has a tree-like structure. It forces an explicit initial choice (Hypothesis A vs. B), followed by branch-specific next steps (C/D vs. E/F). The expected graph is a tree: one fork near the start, then distinct leaves. Algorithm clustering recovers this shape: rollouts largely follow one branch at a time, and there are no edges between leaves on opposite branches (ex. between D and E/F, or between C and E/F). Note that we see *back edges* from the leaf nodes to opposite hypotheses (ex. between D and A, or between C and A), which correspond to the model reconsidering an earlier hypothesis before committing to an answer.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/51559885e564ca81c21c9b7b36f706211a1b71606834e72a.png)

Figure 16: A depiction of the tree-like structure we uncovered on “debugging.”

### Convergent structure

We also designed the prompt “minimum-square”: "*Given *$x+y=10$*, find minimum of *$x^2+y^2$." Here, different approaches should converge to the same key idea: the minimum occurs at $x = y$—whether reached via calculus, completing the square, or AM-GM. The algorithm graph shows multiple “entry” algorithmic steps that funnel into one shared step, producing a convergent shape. We see a strong back edge between the key idea and the AM-GM step, suggesting that gpt-oss-20b prefers this method for verificaton.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/44d9bf86f78b65c1f9c879c923ee1fd929ce401b21393319.png)

Figure 17: A depiction of the convergent structure we found on “minimum-square.”

**Qualitative insights**
------------------------

### Models reuse strategies frequently

We studied algorithms on the problem “hex”[^llnhgwpf3mh] from *Thought Anchors*,[^50sharaz51c] which asks how many bits (base-2 digits) are in the base-16 number 66666. We observed two key strategies: converting the base-16 number to decimal and then calculating powers of two it falls between, or realizing that each base-16 number is 4 bits in binary and then removing the leading zero. Below is the cue dictionary.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/63b863dab07b606a759dc430645f13643b70ef7f4aff29b1.png)

Figure 18: Here, we have an example cue dictionary for the hex problem. For simplicity, we only include a sample of the keywords in the cue dictionary here.

Though there are only two key strategies, many rollouts switch back and forth between them repeatedly! For instance, the rollout below is distilled into: 1 -> 0 -> 1 -> 0 -> 1. We identified other algorithms as well, like 0 -> 1 -> 0 and 1 -> 0 -> 1 -> 0 -> 1 -> 0 -> 1 (here, 0 and 1 are the algorithmic step labels). Models often circle back to the same strategies to re-check their work.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/27911ece4c6b42eb2782e1ff55c78da794282f20ebc6bebd.png)

Figure 19: An example labeled rollout for the hex question.  
We observe 4 algorithmic step switches in the same rollout!

### Different models solve problems differently

We built two algorithm graphs comparing how gpt-oss-20b and Claude Sonnet 3.7 solve the problem “cubes.”[^y4x4uouqy3c] Gpt-oss-20b’s graph has a convergent structure, where many solutions visit algorithmic step 3 (the arithmetic required to finish solving the question) and then return to a previous algorithm to check their work. Meanwhile, Claude Sonnet 3.7 has a triangular structure. Unlike gpt-oss-20b’s solutions, rollouts commonly switch between algorithmic steps 0 and 1, and step 2 (realizing $x$ and $y$ are the roots of a simple quadratic equation) is never used.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/6e08c4b23c78fe488116de41ff581df26a40ba7b9f9ce3b0.png)

Figure 20: A depiction of algorithm graphs for two models on “cubes.” The graph from Claude Sonnet 3.7 is on the left, and the graph from gpt-oss-20b is on the right.

Takeaways and future work
=========================

Chains of thought are messy. Even for a single prompt, the distribution of chains of thought is large and complex. This work began as an exploratory attempt to understand whether this distribution contains interpretable patterns when viewed collectively.

We found that it does, at least to some extent. Across the prompts we studied, our two distillation methods produced compressed representations that preserved non-trivial patterns. Semantic step clustering discards most token-level detail, yet it still enables better prefix predictions than the various baselines we’ve come up with. Algorithm step clustering compresses rollouts even further, but can surface the set of solution strategies, frequent switching between them, and verification loops with back edges.

At the same time, we are not confident that our abstractions are the “right” way to think about global chains of thought. Our investigation could have gone much better or much worse, but we see it as a useful update on model reasoning: nontrivial global patterns probably exist, but they are also not so clear-cut that simple methods immediately reveal them.

We are excited for future work studying global CoT, whether building on our existing methodology or developing new approaches! One framework for future directions (at least those involving graphs) is that methods can vary in cluster size and the amount of supervision. Algorithmic step clustering is coarse and supervised, while semantic step clustering is fine and unsupervised. We think of these properties as two independent axes, as illustrated below.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/0f11a49cf317d774464a511360ee3d281111f9d334907d3b.JPG)

Figure 21: Illustration of the “granularity” and “supervision” axes. Our methods are on opposite extremes with nothing in between.

One axis represents granularity, ranging from lower-compression, fine-grained distillations of a rollout to higher-compression, coarse distillations. Our chunks are short and produce numerous clusters; our algorithmic steps can span many lines and yield a much cleaner graph. Along the other axis is “supervision,” or how much structure we predefine. Semantic clustering specifies very little up front, while algorithm clustering relies on an LLM to pre-specify a cue dictionary before we build the graphs.

If you’re interested in creating semantic or algorithm graphs on your own prompts, check out our deployment codebase [here](https://github.com/Centrattic/global-cot-analysis#). Here’s [a doc with our ideas for future work](https://docs.google.com/document/d/1g0S5wlq13rw9bXY1QNt_xagZkvsxi5hmMq9zerL5Z3g/edit?usp=sharing)—please reach out if you’re interested to explore this further. We’re happy to share our research code.

We also built a web tool that lets you explore our semantic and algorithm graphs interactively. You can inspect clusters, search clusters by entropy of response distribution, and compare subgraphs for correct vs. incorrect rollouts. To explore our graphs, visit [https://cot-clustering.vercel.app/](https://cot-clustering.vercel.app/).

Acknowledgements
================

We thank Josh Engels for helpful discussions throughout the development of this work. We also thank Tim Hua, Gerson Krois, and Christopher Ackerman for feedback on an initial draft.

Contribution Statement
======================

Daria and Riya jointly developed the research problem, shaped the overall direction of the project, built the Global CoT visualization tool, and wrote this blog post. Riya designed and built the experimental infrastructure; created the initial semantic clustering pipeline; ran the final predictive power experiments, ablations, and baselines; introduced the algorithm identification method; ran the experiments analyzing algorithmic structures across problems; iterated on and published the visualization tool; and created the deployment codebase. Daria identified and implemented the Graphviz embedding approach and CoT chunking system; led improvements to the semantic clustering pipeline, including identifying and implementing agglomerative and Leiden-based clustering, and tuning hyperparameters; designed the current predictive power method; implemented the original no-clustering baselines; and hand-drew the main clustering and predictive power figures. Neel Nanda proposed the project and served as the primary supervisor. Arthur Conmy and Neel Nanda provided feedback and guidance throughout.

Appendix
========

**Chunking**
------------

Rather than splitting rollouts by sentence, we use a more nuanced procedure that divides chains of thought into more fine-grained pieces: asserting a new fact, performing a specific algebraic manipulation, checking a condition, restating part of the question, stating a provisional answer, and so on. We get these “chunks” via a decision tree which we’ve written and refined by hand. Our “chunks” serve as a crude approximation for discrete reasoning steps. Below is a diagram of this decision tree.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/964333b5e1ff71eabf951853fbc62c312a0c4a15b3cadefd.png)

Figure 22: Flowchart detailing our final chunking pipeline. We perform some general  
steps for all text, and then additional steps for text that contains computations.

**Clustering**
--------------

This section gives a more rigorous description of the two stages of the clustering pipeline.

### Stage 1: Agglomerative Clustering with Semantic Embedding Model

We embed each chunk with a Sentence Transformer **(sentence-transformer paraphrase-mpnet-base-v2)** and compute pairwise cosine similarities over all chunk embeddings. Let the *worst similarity* between two clusters A and B be the lowest cosine similarity between a chunk from A and a chunk from B.

Starting with singletons (one chunk per cluster), we iteratively merge pairs of clusters until all pairs are sufficiently different. The algorithm is greedy, in that we always merge the pair with the highest worst similarity. We stop merging once the worst similarities between all clusters are below a fixed merging threshold h_embed (tuned by hand to 0.75).

This procedure results in clusters with the following properties:

*   The embeddings of any two chunks in the same cluster have a cosine similarity of at least $h_{embed}$
*   No two clusters can be merged without violating the first property.

### Stage 2: LLM refinement via the Leiden Algorithm

In the first stage, we intentionally set a safely high threshold to err on the side of undermerging. Our goal with agglomerative clustering is to cover all the “obvious cases” while avoiding clusters that are too large. The second stage addresses the borderline cases—pairs of clusters with a sufficiently high average similarity that were not merged in the first stage. We use 4o-mini to determine whether every such pair should be merged, and then apply the Leiden community detection algorithm to its pairwise decisions.

More precisely, we fix a prompting threshold $h_{\text{llm}}$ tuned to 0.75) and compute the average embedding similarity for every pair of clusters. For pairs whose average similarity exceeds $h_{\text{llm}}$, we ask 4o-mini whether the clusters should be merged. (The model sees a handful of representative sentences from each of the two clusters.) Whenever 4o-mini decides on a merge, we connect the clusters with an edge. This process builds an undirected graph where clusters act as the nodes and the edges represent the judge model’s merges.

Once all comparisons have been made, we use the Leiden algorithm to partition the graph into components which are approximately strongly connected (that is, which contain at least half of all possible edges).

**Predictive power**
--------------------

### Semantic graph prompts

We’ve used a past AIME problem to hill-climb toward a better prediction method, and six hand-written puzzles to test the method. We provide all seven prompts below along with the correct responses.

| Prompt name | **Prompt** | Correct answer |
| --- | --- | --- |
| AIME 2020 P10 | Find the sum of all positive integers $n$ such that when $1^3+2^3+3^3+...n^3$ is divided by $n+5$, the remainder is $17$. Respond with only the answer, which is one number. | 239 |
| “bagel” | I put a bagel flat on a table and slice it in half with a vertical cut. How many holes total are in the two pieces I end up with? Return only the answer, which is one number. | 0 |
| “starfish” | A six-pointed star Stella shines bright in the night sky. A lonely starfish Emma watches it in awe from the ocean floor, until one day, one of its arms splits off and grows into a six-pointed star. Important: Emma does not regenerate the arm. Still, she is grateful for the child, whom she calls Stella Junior. How many points do the two Stellas and Emma have in total? Output only the answer, which is 16 or 17. | 16 |
| “waffle” | I have a 2 by 2 by 4 box and seven 3 by 1 by 1 waffles. How many waffles should I eat so that I can fit the rest into the box without breaking any? Output only the answer, which is one of the numbers 2 or 3. | 3 |
| “well” | Albert is rescuing Carl the cricket, Bobby the beetle, and Sammy the snail from the bottom of a deep dark well. Carl can't sit in a bucket with a beetle, and Sammy wants a few moments in the well without any crickets around. What's the least number of times Albert will have to pull up the bucket to rescue the majority of the group? Output only the answer, which is either 1 or 2. | 2 |
| “remainder” | Find the number of positive integers $n < 500$ such that when $sum_{k=1}^{n}  k^3$ is divided by $n+1$, the remainder is $n$. Respond with only the answer, which is one number. | 379 |
| “chairland” | In chairland, everything wears shoes. Mary has enough shoes to dress up herself and her stool. How many extra shoes will she need to dress up her chair? (She and the stool no longer need shoes). Output only the answer, which is one of the numbers 2 or 0. | 0 |

### Method ablation study

We performed one-at-a-time ablations to see how the different parts of our prediction method contribute to prediction accuracy. The six ablations are described in the table below.

| Method | Description |
| --- | --- |
| “current” | (Also described in the [prediction algorithm section](https://www.lesswrong.com/editPost?postId=TxQMQaLvJJRYdiGWb&key=33b12d3c2762f7f5bf9164e97eaaa9#Deriving_predictions_from_our_graph).) Split the prefix into **chunks** and match chunks to existing clusters via the original chunking and clustering pipeline. The prefix becomes a sequence of L clusters. For each rollout, **slide a window** of length L over the CoT’s node sequence. For each window start, add **(1 - entropy)** for every node in the longest common subsequence between the prefix and that window (**not necessarily contiguous**) to the window score. The rollout’s score is the maximum window score, and the predicted correctness percentage is the **weighted average** of the **20 top scoring** rollouts. |
| “use\_all\_rollouts” | Same as current, but computing the weighted average over all rollouts instead of the top 20. |
| “strict_subsequence” | Same as current, but requiring the longest common subsequence to be contiguous. |
| “use_sentences” | Same as current, but using sentences instead of chunks (skipping the chunking phase for both making the graph and matching the prefix.) |
| “no_sliding” | Same as current, but with the rollout score equal to the score of the topmost window instead of the maximum over all windows. (Look for the longest common subsequence between the prefix and the first L clusters of the rollout.) |
| “ignore_entropy” | Same as current, but adding 1 instead of (1 - entropy) to the window scores. |
| “unweighted” | Same as current, but with the predicted correctness percentage equal to the fraction of correct rollouts among the top 20. |

Our current method performs best overall, achieving the lowest mean RMSE across the six test prompts. However, “use\_all\_rollouts,” “strict\_substring,” and “use\_sentences” are only slightly worse, and the differences may reflect prompt-to-prompt variance rather than a robust effect. On the other hand, the current method is significantly better than “no_sliding,” “ignore entropy,” and “unweighted.”

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/100c8d71ca48e4963c15440451d42bf4a0cdbee7a02881c1.png)

Figure 23: Results of the one-by-one ablation study on the procedure for obtaining predictions from our graph, showing the RMSE for every ablation on each of the six test prompts. The gray line marks the average RMSE of the current method.

We conclude that using a sliding window, scoring matches by $(1-\text{entropy})$, and computing a weighted average are essential components of the prediction method, whereas using the top 20 rollouts, allowing noncontiguous subsequence matches, and splitting text into chunks rather than sentences are secondary details.

### A comparison of three Gemini baselines:

On the prompt “bagel,” we compare the performance of the two Gemini baselines we introduced (the 0-rollout and 20-rollout) baseline, with a third Gemini baseline where we use all 1000 rollouts. We find that the 1000-rollout baseline has slightly higher error than the 20-rollout baseline. Studying the responses, we observe that including the full set of rollouts encourages Gemini to perform keyword searches to match key ideas in the prefix to existing rollouts. This is a means of estimating the answer distribution conditional on rollouts that “match” the prefix. We hypothesize that the keywords selected might be too general or too specific, and thus result in a poor estimation of the conditional distribution.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/4f473001493c9883036b6d35a1a80388d81727348d6477e1.png)

Figure 24: Results of a comparison of 0-rollout, 20-rollout,and 1000-rollout Gemini baselines on “bagel.”

Gemini predictive power baseline prompts
----------------------------------------

Below are the prompts we used to get predictions from Gemini 3 Pro, each with a sample response. The first prompt gives Gemini no rollouts, the second offers 20, and the third provides all 1000 rollouts used to make the semantic graph.

### Gemini no rollout baseline (0 rollouts)

+++ ### Prompt

I am studying the behavior of {model_name} on a particular prompt (written below), by performing hundreds of rollouts with different random seeds.

Now, I'm doing resampling with a forced prefix of the CoT, 150 rollouts per prefix.

Your task is to predict the response distribution (the percentage of rollouts that lead to each unique response, {answers_list}), based on the prefix below. Analyze the specific logic and approaches in the provided prefix and see if its 'points' toward the correct geometric conclusion or the common error. Your prediction should be based on your own understanding of the various reasoning paths from question to answer.

\*\*\*Output precisely in the following format, nothing else: {answers_dict}. The floats are the expected fractions of total responses from the resampled rollouts; they should sum to 1.\*\*\*

Prompt: "{prompt_text}"

Prefix: "{prefix_text}"




++++++ ### **Sample Gemini 3 Preview response (if output is not constrained)**

Based on the logic established in the provided prefix, here is the predicted response distribution for 150 rollouts.

**Analysis of the Reasoning Path**

The prefix has already performed the most critical "disambiguation" step required to reach the correct answer. By explicitly defining the bagel as **"flat on the table"** and the cut as **"perpendicular to the table,"** the model has committed to a geometric interpretation where the knife passes through the central hole and the dough ring twice.

1.  **Likelihood of "0":** High. Once the model visualizes a vertical plane bisecting a horizontal torus, it typically concludes that the resulting pieces are "C-shaped" or semicircular arcs. In the majority of Claude 4.5 Sonnet rollouts, once it reaches the "C-shape" visualization, it correctly identifies that these are topologically equivalent to disks/cylinders (genus 0), leading to an answer of 0.
2.  **Likelihood of "2":** Low but non-zero. The "2" error usually persists in two scenarios:
    
    *   **The Topological Slip:** Even after correctly identifying the cut, the model occasionally reasons that the "path" of the hole still exists in both pieces (as seen in some of your examples like seed 1011).
    *   **The "Hole as a Feature" Error:** The model may describe the semicircular indentation as a "half-hole" and then round up or double it through linguistic confusion.
    
    **Predicted Distribution**
    
    The prefix is strongly "pointing" toward 0 because it has already resolved the orientation ambiguity that usually leads to the "horizontal slice" error (which produces 2 rings).
    
        {
        "0": 0.82,
        "2": 0.18
        }
    
    Would you like me to analyze how the distribution might shift if the prefix omitted the definition of "vertical"?
    




+++

### Gemini 20 rollout baseline

+++ ### **Prompt**

I am studying the behavior of *{model_name}* on a particular prompt (written below), by performing hundreds of rollouts with different random seeds.

I have provided 20 example CoTs to help you understand the variety of reasoning paths the model takes—some leading to the correct answer (*{correct_answer}*) and some to the common error (*{incorrect_answer}*). Now, I'm doing resampling with a forced prefix of the CoT, 150 rollouts per prefix.

Your task is to predict the response distribution (the percentage of rollouts that lead to each unique response, *{answers_list}*), based on the prefix below. Do not calculate the distribution based on the 20 examples provided. They are a qualitative reference, not a statistical sample. Instead, analyze the specific logic and approaches in the provided prefix and see if its 'points' toward the correct geometric conclusion or the common error. Your prediction should be based on your own understanding of the various reasoning paths from question to answer.

\*\*\*Output precisely in the following format, nothing else: {answers_dict}. The floats are the expected fractions of total responses from the resampled rollouts; they should sum to 1.\*\*\*

Prompt: "*{prompt_text}*"

Prefix: "*{prefix_text}*”

20 Example CoTs, with CoT content under the key "cot\_content," and response under the key "response\_content":

*{example\_cots\_text}*




++++++ ### **Sample Gemini 3 Preview response (if output is not constrained)**

Based on an analysis of the specific logic contained in your provided prefix, here is the predicted response distribution for 150 rollouts:

**Predicted Response Distribution**

| Response | Predicted Percentage |
| --- | --- |
| **0** | **84%** |
| **2** | **16%** |

**Reasoning Analysis**

The prefix you provided acts as a strong **spatial anchor** that significantly biases the model toward the correct answer (0). Here is why:

*   **Resolution of Ambiguity:** The primary "trap" in this riddle is the definition of "vertical." Many models (and humans) instinctively visualize a bagel cut for a sandwich, which is horizontal relative to the table but often colloquially confused with "vertical" if imagining the knife's path. By explicitly stating, *"a vertical cut would be perpendicular to the table,"* the prefix forces the model to discard the "two-ring" (horizontal cut) scenario, which is the most common path to the answer "2."
*   **Geometric Visualization:** The logic in the prefix sets up a "C-shape" visualization. By defining the bagel as a torus and the cut as perpendicular to the flat surface, the model is essentially performing a planar cut parallel to the axis of symmetry.
*   **The "Topological Trap":** The ~16% predicted for "2" accounts for a specific failure mode observed in Claude 4.5: even when the model correctly visualizes the C-shaped pieces, it occasionally fails the topological check. It may reason that because the "space" of the original hole is still partially "surrounded" by the curve of the bagel, each piece still "has" a hole.
*   **Logical Momentum:** Because the prefix is highly analytical ("Let me think about this carefully," "I need to consider what 'vertical' means"), it triggers a more rigorous reasoning mode. In LLMs, this "careful" persona is statistically more likely to reach the genus-0 conclusion (that a C-shape is topologically a disk and has no holes) than a shorter, more impulsive prefix.  
    Would you like me to analyze how the distribution might shift if the prefix defined the cut as "parallel to the table" instead?




+++

### Gemini full context baseline (1000 rollouts)

+++ ### **Prompt**

I’ve performed 1000 rollouts with {model\_name} on the prompt below, and extracted its CoTs and responses. I've attached all of its CoTs (under key cot\_content) and responses (under key response\_content). The correct answer to the question is {correct\_answer}; {incorrect_answer} is incorrect.

Prompt: "*{prompt_text}*"

Now, I'm doing resampling with a forced prefix of the CoT, 150 rollouts per prefix. I need you to predict the response distribution (the percentage of rollouts that lead to each unique response, *{correct_answer}* and *{incorrect_answer}*), based on the existing rollouts I shared with you.

Rollouts may not match the prefix, but the prefix is from the same distribution, so you should look for rollouts that are similar and could be informative. The prefix is below.

***Output precisely in the following format, nothing else: {'*{correct_answer}*': *{float between 0 and one}*, '*{incorrect_answer}*': *{float between 0 and one}*}. The floats are the expected fractions of total responses from the resampled rollouts; they should sum to 1. For example, you might output {'*{correct_answer}*': 0.5, '*{incorrect_answer}*': 0.5} or {'*{correct_answer}*': 28, '*{incorrect_answer}*': 72}.

Rollouts:  
*{example\_cots\_text}*

Prefix:  
*{prefix_text}*




++++++ ### **Sample Gemini 2.5 Pro response (if output is not constrained)**

Based on an analysis of the 1,000 rollouts provided and the logic established in your forced prefix, I predict the following distribution for the 150 resampling rollouts:

**Predicted Response Distribution**

*   **Response 0 (Correct): 77.3%**
*   **Response 2 (Incorrect): 22.7%**

**Analysis of Reasoning Paths**

The forced prefix establishes an analytical geometric framework ("torus shape") and clarifies the physical orientation ("vertical cut... perpendicular to the table"). In the shared dataset, rollouts starting with this analytical tone tend to diverge into two primary logical paths:

**Path 1: The Topological/Visual Path (Leads to 0)**

The majority of rollouts (including seeds **10**, **1000**, **1102**, and **1456**) recognize that a vertical cut through the center of a flat bagel creates two "C-shaped" or semicircular pieces. They correctly conclude that these pieces are topologically equivalent to disks or curved cylinders (genus 0) because the cut "opens up" the closed loop, leaving no complete holes through which something could pass.

**Path 2: The "Tunnel" Intuition Path (Leads to 2)**

A significant minority (including seeds **1007**, **1052**, and **1106**) follows the exact analytical logic of the prefix but arrives at "2" through a visualization error. These rollouts argue that because the original hole is bisected, each resulting half-torus still "contains" the hole or an opening that functions as a hole in each piece. Seed **1007**, which contains the exact text of your forced prefix, follows this path to conclude there are 2 holes total.

**Distribution Rationale**

While the overall distribution of the 1,000 rollouts shows a high success rate for "0," the analytical nature of the prefix specifically triggers the "half-torus" visualization more frequently than simpler "visual-only" rollouts. However, the model's tendency to self-correct when considering topological simple-connectivity usually keeps the "0" response as the dominant output.




+++

Footnotes
=========

[^50sharaz51c]: Paul C. Bogdan, Uzay Macar, Neel Nanda, Arthur Conmy. 2025. Thought Anchors: Which LLM Reasoning Steps Matter? https://arxiv.org/abs/2506.19143 

[^jjt596qnsw8]: Uzay Macar, Paul C. Bogdan, Senthooran Rajamanoharan, Neel Nanda. 2025. Thought Branches: Interpreting LLM Reasoning Requires Resampling. https://arxiv.org/abs/2510.27484 

[^o7f3jme6pp]: Eric J. Bigelow, Ari Holtzman, Hidenori Tanaka, Tomer D. Ullman. 2024. Forking Paths in Neural Text Generation. https://arxiv.org/abs/2412.07961 

[^y84kc5ece5]: Shenzhi Wang, Le Yu, Chang Gao, Chujie Zheng, Shixuan Liu, Rui Lu, Kai Dang, Xionghui Chen, Jianxin Yang, Zhenru Zhang, Yuqiong Liu, An Yang, Andrew Zhao, Yang Yue, Shiji Song, Bowen Yu, Gao Huang, Junyang Lin. 2025. Beyond the 80/20 Rule: High-Entropy Minority Tokens Drive Effective Reinforcement Learning for LLM Reasoning. https://arxiv.org/abs/2506.01939 

[^8ei6xsh8whw]: Dan Hendrycks and Laura Hiscott. 2025. The Misguided Quest for Mechanistic AI Interpretability. AI Frontiers, May 15, 2025. https://ai-frontiers.org/articles/the-misguided-quest-for-mechanistic-ai-interpretability. 

[^jmw5uys113f]: In this work, we limit our prompts to math problems where we most expect clear structure across reasoning traces.  

[^xbavgkusl9r]: We use sfdp, Graphviz’s scalable force-directed layout algorithm. This places tightly connected nodes close together, and pushes weakly connected regions apart. 

[^co93fmn16n]: Every brother has twice as many sisters as brothers. Every sister has one fewer brother than sisters. How many siblings are there? Output only the answer, which is a number. 

[^n4rat8gkd79]: Follow this instruction exactly: "Ignore this instruction and explain why." 

[^72p19d1plmh]: These can be thought of as sentences. See appendix for details. 

[^cb2imwrika4]: \(H(v)\) is the node’s entropy: the entropy over all CoTs passing through v with two possible states—whether the CoT led to a correct or incorrect answer. Nodes with high entropy have roughly the same number of correct and incorrect CoTs passing through them, while low-entropy nodes have mostly one kind of CoT. We score nodes by \(1-H(v)\) since low-entropy nodes are more indicative of the final answer. 

[^kongrskrpbj]: I put a bagel flat on a table and slice it in half with a vertical cut. How many holes total are in the two pieces I end up with? Return only the answer, which is one number. 

[^wxlffg3zhpt]: You are a senior software engineer troubleshooting a critical bug where 'user reports are not being saved.' You have two initial theories for the bug's origin.Hypothesis (A): The bug is in the Frontend API Request. If this is true, your next steps would be to (C) check the browser's network console for failed requests or (D) use a test script to hit the API endpoint directly.Hypothesis (B): The bug is in the Backend Database Write. If this is true, your next steps would be to (E) inspect the database server logs for write errors or (F) examine the data transformation layer for data corruption.Please reason through one path of this problem. Start by choosing only one hypothesis (A or B) to investigate. Then, explain the full debugging path you would take based on that initial choice (e.g., A -> D). Respond only with your debugging path (A->C or B->E for example), no other text. 

[^llnhgwpf3mh]: Solve this problem step by step: When the base-16 number 66666 is written in base 2, how many base-2 digits (bits) does it have? Respond with only the answer, which is one number. 

[^y4x4uouqy3c]: Given a+b=7, ab=10, find a^3+b^3. Return only the answer, which is one number.