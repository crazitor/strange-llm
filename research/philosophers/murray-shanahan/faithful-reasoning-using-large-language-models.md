---
title: "Faithful Reasoning Using Large Language Models"
author: "Murray Shanahan"
date: "2022"
source: "semantic_scholar"
url: "https://www.semanticscholar.org/paper/f0a0e8b6e84207f50db4d24cc4016e40601214ef"
citations: 144
---

## Abstract

Although contemporary large language models (LMs) demonstrate impressive question-answering capabilities, their answers are typically the product of a single call to the model. This entails an unwelcome degree of opacity and compromises performance, especially on problems that are inherently multi-step. To address these limitations, we show how LMs can be made to perform faithful multi-step reasoning via a process whose causal structure mirrors the underlying logical structure of the problem. Our approach works by chaining together reasoning steps, where each step results from calls to two fine-tuned LMs, one for selection and one for inference, to produce a valid reasoning trace. Our method carries out a beam search through the space of reasoning traces to improve reasoning quality. We demonstrate the effectiveness of our model on multi-step logical deduction and scientific question-answering, showing that it outperforms baselines on final answer accuracy, and generates humanly interpretable reasoning traces whose validity can be checked by the user.
