---
layout: post
title: Curriculum Learning For LLMs?
date: 2025-01-05 14:40:16
description: How can we address the discrepancy caused by the outdatedness of the training data for large language models?
categories: thoughts
---

Before this, I was aware of Curriculum Learning by Yoshua Bengio. The concept is very appealing, right? You teach a model with a curriculum, starting with easy data and progressing to harder datasets, and the model will learn and generalize better. 

I thought that it could be applied more broadly to large language models. For example, you could teach them kindergarten-level material and then pre-train them on advanced mathematics or science, and they would learn to generalize better, right? I couldn't find any literature discussing this in depth, except for Microsoft's Phi models. They use a synthetic dataset to generate an elementary dataset to teach a very small model English, and it kind of succeeded. 

For frontier models, if the dataset contains the entire corpus of the internet, I think the consensus is that since the dataset is too diverse and the model will eventually look at every part of it, the advantage of a curriculum dataset will dissipate. That's what it seemed, and I prematurely concluded my investigation and didn't think much more about it.

---

But that all changed when, on this day, I was listening to a podcast featuring Yann LeCun and Gary Marcus, hosted by Lex Fridman. What struck me was that the interview was conducted five years ago, in 2019. Half a decade in the machine learning era is a very long time.

In 2019, ChatGPT and GPT-3 didn't even exist, so the models at the time couldn't understand language very well. They didn't have common sense reasoning of any sort. Both LeCun and Marcus were very wrong by today's standards.

But then I realized that current large language models are all pre-trained on a massive global dataset that contains outdated information of this sort. For example, a prominent scientist in 2010 saying that deep learning had hit a dead end or that it couldn't generalize was completely true in that era but is completely false today. During pre-training, language models can't discern that.

So, how could we address this discrepancy caused by the outdatedness of the training data? Should we just filter it out? Should we just let it be? As time goes on, the accumulation of current, up-to-date information grows numerically larger. Should we just dilute the outdated data?

If I'm not mistaken, the pre-training stage is very simple: you just do next-token prediction on the entire corpus and perform backpropagation. There's no secret in the pre-training stage. So, I don't know how to address this.

But if you think about it more, the web contains countless instances of conflicting information. For example, some sources claim that global warming is false, while others state that it is absolutely true. Even worse, there are works of literature, like novels, that aren't factual at all.

Considering this, current language models are still very knowledgeable and, while they do hallucinate, they possess some sort of factual world model. This suggests that the pre-training corpus is so vast that conflicting information essentially cancels out, and the model learns the nuances.

---

So, then, is curriculum learning not needed? I think there's a reason that curriculum learning isn't widely researched: its effect is likely very marginal. While the findings are undetermined, I still believe that if curriculum learning is indeed unnecessary, it basically demonstrates the powerful generalization capability of large language models.

I think I'll still have to revise my thoughts on this matter.