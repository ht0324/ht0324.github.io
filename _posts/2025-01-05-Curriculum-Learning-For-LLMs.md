---
layout: post
title: Curriculum Learning For LLMs?
date: 2025-01-05 14:40:16
description: How can we address the discrepancy caused by the outdatedness of the training data for large language models?
tags: AI
categories: thoughts
---

I was previously aware of Curriculum Learning, a concept introduced by Yoshua Bengio. The idea is quite appealing: you train a model with a curriculum, starting with easier data and progressing to harder datasets. This approach is believed to enhance the model's ability to learn and generalize.

I thought this concept could be particularly relevant to large language models. For instance, one could start by teaching them basic concepts, like those found in kindergarten materials, and then gradually introduce more advanced subjects like mathematics or science. This structured approach, I believed, would lead to better generalization.

However, I couldn't find much literature exploring this idea in depth, except for Microsoft's Phi models. These models use synthetic datasets to generate elementary-level data, teaching a small model to learn English, with some success. For larger, more advanced models trained on the vast expanse of the internet, the consensus seemed to be that the diversity of the dataset would negate the benefits of a curriculum.

The sheer volume and variety of data would mean the model would eventually encounter all parts of the dataset, regardless of the order. This conclusion led me to prematurely end my investigation.

---
<br />
**A Shift in Perspective**

My perspective shifted when I listened to a podcast featuring Yann LeCun and Gary Marcus, interviewed by Lex Fridman. It struck me that these interviews were conducted five years ago, in 2019. In the rapidly evolving field of machine learning, half a decade is an eternity.

Back in 2019, models like ChatGPT and GPT-3 didn't exist, and the ability of models to understand language and exhibit common sense reasoning was limited. The assessments made by LeCun and Marcus, while accurate for their time, are outdated in the current landscape.

<br />
**The Challenge of Outdated Information**

A significant challenge arises from the fact that current large language models are pre-trained on massive datasets encompassing information from across the globe and various time periods. These datasets inevitably contain outdated information. For example, a statement from a prominent scientist in 2010 claiming that deep learning had hit a dead end would have been accurate then but is demonstrably false today.

During pre-training, language models struggle to discern the temporal validity of such statements. This raises several questions: How should we address this discrepancy caused by outdated training data? Should we filter out outdated information, or simply let it be?

As time progresses, the volume of current, up-to-date information will naturally increase. Could we simply dilute the outdated data with newer information? The pre-training stage, as far as I understand, is relatively straightforward, involving next-token prediction and backpropagation across the entire corpus.

There doesn't seem to be any inherent mechanism within this process to handle the issue of outdated information. I'm currently unsure how to effectively address this challenge.

<br />
**The Paradox of Conflicting Information**

However, upon further reflection, the internet is replete with conflicting information. For instance, one can find sources claiming that global warming is false, while others assert its undeniable truth. Furthermore, there's a vast amount of literature, like novels, that are fictional and not meant to be factual.

Despite this, current language models demonstrate a considerable degree of knowledge and, while prone to hallucinations, possess a semblance of a factual world model. This suggests that the sheer vastness of the pre-training corpus might be a factor. It's possible that conflicting information effectively cancels each other out, allowing the model to learn the nuances of different perspectives.

---
<br />
**Reconsidering Curriculum Learning**

This leads to the question: is curriculum learning then unnecessary? I suspect that the limited research on curriculum learning for large language models might be due to its marginal impact.

While the effectiveness of curriculum learning remains uncertain, I believe that if it is indeed not needed, it would be a testament to the powerful generalization capabilities of large language models. They are able to learn from a chaotic sea of information, discerning patterns and nuances without explicit guidance.

I believe I still need to refine my thoughts on this matter. The interplay between the vastness of training data, the presence of conflicting information, and the potential benefits of curriculum learning is a complex issue that warrants further investigation.