---
title: "Analysis of Whisper-Tiny Using Sparse Autoencoders"
author: "Omar Khursheed"
date: "2025-12-21"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/aXSuc6pdCy6SkeKZk/analysis-of-whisper-tiny-using-sparse-autoencoders"
score: 9
votes: 4
---

In this project, I attempted to explore the model Whisper-Tiny from OpenAI, which is a speech transcription model that takes in audio and provides a transcript as output. Here’s an example of transcription

    Reference text: CHAPTER SIXTEEN I MIGHT HAVE TOLD YOU OF THE BEGINNING OF THIS LIAISON IN A FEW LINES BUT I WANTED YOU TO SEE EVERY STEP BY WHICH WE CAME I TO AGREE TO WHATEVER MARGUERITE WISHED
    Transcription:  Chapter 16 I might have told you of the beginning of this liaison in a few lines, but I wanted you to see every step by which we came. I to agree to whatever Mark Reid wished.
    Input features shape: torch.Size([80, 3000])
    Audio duration: 14.53 seconds

### Residual Stream Analysis

Whisper is an encoder-decoder style model. We begin by generating some statistics on the residual stream, we mainly look at activation distributions in the last layer of of the encoder across 5 examples and see that the distributions are rather uniform in nature. Due to the nature of the space of these activations (384-dimensions) and the fact that they are non-sparse, these are rather difficult to interpret. We will therefore, later in this document show how we use sparse autoencoders (SAEs) to extract more interpretable features from this space. 

Now, we analyze some attention patterns from the encoder based on an example.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/e945a34fa6bf0821802c56bdbdd2bfbbda3917a7d973d867.png)

We use Claude to generate an explanation of these patterns and verify them

1.  Layer 1 Attention (First Head):
    *   Shows a clear diagonal pattern, indicating that each position is primarily attending to itself and nearby positions.
    *   The diagonal is thin and sharp, suggesting a very focused local attention.
2.  Layer 2 Attention (First Head):
    *   The diagonal pattern is still present but slightly broader.
    *   There's more diffusion of attention around the diagonal, indicating the model is considering a wider context.
3.  Layer 3 Attention (First Head):
    *   The diagonal is even more diffuse, with attention spreading further from the main diagonal.
    *   This suggests the model is integrating information from a broader context in this layer.
4.  Layer 4 Attention (First Head):
    *   The attention pattern is significantly different from the previous layers.
    *   There's a strong focus on the early part of the sequence (top-left corner), with some vertical striping.
    *   This could indicate that the model is using this layer to aggregate information from the entire sequence, with a bias towards earlier elements.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/a7ef7c99aec83321d4f8bc2fc3dcbeae7b9598d4e27145aa.png)

This graph shows the "Attention Entropy across Layers and Heads":

*   The x-axis represents "Layer * Num\_Heads + Head\_Index", effectively flattening all attention heads across all layers into a single dimension.
*   The y-axis represents "Entropy", which measures the randomness or unpredictability of the attention distribution.

We see that the entropy values fluctuate significantly across different heads and layers. However Despite fluctuations, there's a slight upward trend in entropy as we move from left to right (i.e., from earlier to later layers/heads). There are several notable peaks (e.g., around index 15) and troughs (e.g., around index 5).

We developed this experiment with Claude’s help, and allow it to generate our explanation (with verification that it aligns with our observations)

*   Lower entropy suggests more focused attention, while higher entropy indicates more diffuse attention.
*   The variability suggests different heads are specializing in different types of attention patterns.
*   The general upward trend aligns with the heatmap observations: later layers tend to have more diffuse attention patterns, integrating information from a wider context.
*   The peaks could represent heads that are attending broadly across the input, while troughs might be heads that are very selective in their attention.

### SAE Results

We train a sparse autoencoder (using 100000 examples of Librispeech for 50 epochs) on the activations of the  last layer of the encoder and show the change in sparsity across five examples

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/010c7b700cb759d6706dbb92b228a8b527e7da77fa8652a0.png)

As we see, we go from 0 sparsity in the original space to 48% sparse in the encoded space of the SAE. The idea of SAEs is that features that may be exhibiting superposition in the activation space, when trained with a sparsity inducing L1 loss, would allow us to disentangle features in the larger space.

We attempt to disentangle 2 different type of features from the SAE feature space, gender and accent, based on the metadata available in the Mozilla CommonVoice Dataset (the dataset only divides genders into male, female and other, and we are therefore limited in the inclusiveness of the analysis we are able to run).

We run examples of differently gendered voices through the SAE and check which features light up the most, and plot the difference in male/female voices for the top few features

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/dcd2cef4f5df0980eb61f24a9a5acc8eef0b388afeba4c74.png)

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/9a301957a9c426708243cf12db61090cfd5f450027e14336.png)

We also attempt to use a RandomForestPredictor to use the top few features to predict the gender variable, but see that there is essentially zero recall for the female class. This shows that the last layer of the encoder doesn’t necessarily encode information about gender in a separable fashion. We suspect that there may be further information about gender-related voice features in earlier layers, but we leave this hypothesis to be investigated in future work.

For the accents, we pick 25 examples each from 5 different accents:

*   United States English
*   India and South Asia (India, Pakistan, Sri Lanka)
*   Southern African (South Africa, Zimbabwe, Namibia)
*   Filipino
*   West Indies and Bermuda (Bahamas, Bermuda, Jamaica, Trinidad)

For accents, we find more separability in a few features as shown by the box plots below.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/391db0eb295bfc2f3b1232c16d4265c020621b8916896089.png)

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/2eb78c0db93b13b0b0baafb544e6c8ac6654b0ee7f685a0a.png)

We weren’t able to create a predictor for accents to perform a similar analysis as we did for gender due to the small size of the dataset we created, but we have at least directional evidence that the last layer of the whisper encoder encodes some accent related features.

### Conclusions

*   Attention patterns across different encoder layers show that different parts of the network have different behavior, and that the audio encoder attention is extremely local except in the last layer. 
*   Gender is not a feature that we were able to separate using a sparse autoencoder trained to have 3x the dimensional space as the encoder activations
*   We were able to extract features that are at least correlated with different accents. This implies that high level accent features are stored in the MLP layers of the last layer in the encoder.

### Future Work

*   We only explored the encoder, we could do similar analysis for the decoder, focused on the relationship between the encoder embeddings and the transcription.
*   We only trained a single SAE, there are several other layers, both in the encoder and decoder, that could be explored using more SAEs
*   We could explore more demographics and feature ideas, other than gender and accent.

### Notes:

*   I found that I took a little too much on for this project compared to my knowledge of mechinterp, and got a lot of help from Claude 3.5 Sonnet and ChatGPT o1 for the analysis and code. Most of the writing in this doc is my own, except in the places where Claude is explicitly mentioned
*   I was heavily inspired by this work [https://er537.github.io/blog/2023/09/05/whisper_interpretability.html](https://er537.github.io/blog/2023/09/05/whisper_interpretability.html) by Ellena Reid
*   This was submitted as my final project for Bluedot Impact's excellent Fundamentals of AI Safety Course