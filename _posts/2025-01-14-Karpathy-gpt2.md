---
layout: post
title: Let's Reproduce GPT-2 by Karpathy - Review
date: 2025-01-14 20:30:00
description: My notes and takeways on Andrej Karpathy's GPT-2 reproduction video
tags: AI
categories: Paper
giscus_comments: true
---

I recently watched Andrej Karpathy's ["Let's Reproduce GPT-2 (124M)"](https://youtube.com/watch?v=l8pRSuU81PU) video. This post covers the core ideas and key insights I learned, especially around positional embeddings, transformer architecture tweaks, and practical considerations when implementing models like GPT-2.

---

### Key Concepts

**Transformer Modifications: Pre-Layer Normalization (Pre-LN)**  
In the original transformer, Layer Normalization comes after attention and feedforward layers (Post-LN). GPT-2 switched this, applying normalization beforehand (Pre-LN). This seemingly small tweak stabilizes training by improving gradient flow, especially in deeper models.

**Transformer as MapReduce**  
Karpathy uses an analogy: Transformers operate similarly to a MapReduce process. Self-attention acts like a "Reduce" step, combining information from all tokens, while the subsequent MLP acts like "Map," independently processing each token's representation.

**Optimizing Attention Computation (Tensor Gymnastics)**  
GPT-2's attention mechanism involves tensor reshaping for efficiency. Input tensors are projected simultaneously into queries, keys, and values across all heads using batch matrix multiplication. These tensors are then reshaped and transposed efficiently for multi-head attention computation.

**FlashAttention**  
FlashAttention is a recent, efficient algorithm for speeding up attention computations. By breaking attention into smaller "tiles" and combining multiple computations (kernel fusion), it reduces memory usage, allowing transformers to handle longer sequences faster.

**Weight Sharing Between Input and Output Layers**  
GPT-2 shares weights between the token embedding layer (`wte`) and the final linear output layer (`lm_head`). This design choice helps the model learn more consistent representations and often results in better generalization, despite initially seeming counterintuitive.

---

### Key Takeaways (What I Learned)

**Why Learned Positional Embeddings Work Well**  
Initially, positional embeddings felt abstract. Now I see they're powerful because each embedding channel independently captures different positional information, like long-range versus short-range patterns. This allows the model to adapt its position representations specifically to the training data, unlike fixed sine-cosine methods.

**The Impact of Pre-LN on Training Stability**  
Before this, I thought normalization order wouldn't matter much. But moving LayerNorm before each attention and MLP block stabilizes gradients, helping especially in deeper transformer stacks. This highlights the subtle but meaningful effects minor architectural tweaks can have.

**Autoregressive Prediction and the "Last Vector" Mystery**  
I always wondered why GPT predicts from only the last token's embedding, even though the whole sequence is processed. The reason: the last token embedding naturally contains information from the entire context due to causal attention, preserving autoregressiveness efficiently. Using earlier vectors directly would break this causal property.

**Why Attention Head Dimensionality (`head_size`) Matters**  
Each attention head having a smaller, separate dimensionality (`head_size`) surprised me at first. But now, it makes sense: smaller head dimensions force each attention head to specialize in capturing distinct relationships, making the model both efficient and expressive.

---

### Summary & Final Thoughts  
This GPT-2 deep dive clarified many subtle yet significant details such as positional embeddings, attention optimizations, and training nuances. Small architectural choices, like moving normalization or adjusting head dimensions, can meaningfully impact performance.  

The MapReduce analogy particularly helped demystify transformers, clarifying the internal data flow. Also, understanding why GPT predicts using only the final token made its autoregressive nature clear.  

Overall, transformers have subtle complexities beneath their simplicity, and Karpathy's reproduction video made me appreciate these subtleties more deeply.
