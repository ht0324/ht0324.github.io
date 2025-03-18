---
layout: post
title: Review of Andrej Karpathy's "Let's Build GPT From Scratch"
date: 2025-01-12 14:00:00
description: My thoughts and notes on Andrej Karpathy's video on building GPT from scratch
tags: AI
categories: Paper Blog
giscus_comments: true
---

Andrej Karpathy’s video ["Let's build GPT: from scratch, in code, spelled out"](https://www.youtube.com/watch?v=kCc8FmEb1nY) offers a clear, practical walkthrough of implementing a simplified GPT from the ground up. Karpathy intentionally keeps things simple, training a character-level GPT on a tiny Shakespeare dataset (just 1MB), making the implementation approachable without getting lost in complexity.

Below is a quick summary and my main insights from going through the video:

---

### Key Concepts

1. **Data Preparation**
   - Encodes characters into numerical tokens (65 unique tokens from Tiny Shakespeare).
   - Data split into training (90%) and validation (10%).

2. **Chunking**
   - Transformers use fixed-length contexts (`block_size`) rather than full text.
   - Random sampling of batches (`batch_size`) for computational efficiency.

3. **Bigram Language Model**
   - Simplest language model: predicting next character from current one.
   - Uses embedding tables (`token embedding table`) to convert tokens into prediction logits.

3. **Self-Attention Mechanism**
   - Computes relevance between tokens via queries and keys.
   - Uses masking (`tril` matrix) to prevent looking into future tokens.

4. **Multi-Head Attention**
   - Each head independently calculates attention on different subsets of token embeddings.
   - Outputs from multiple heads concatenated and projected linearly.

5. **Feed-Forward Networks**
   - Simple MLP layers placed after attention to process token-level details.
   - Typically have 4× embedding dimensionality internally.

5. **Residual Connections and LayerNorm**
   - Residual connections (identity pathways) make training stable, preventing vanishing gradients.
   - Layer Normalization stabilizes activations and gradients across token dimensions.

6. **Scaling the Model**
   - Increasing parameters (layers, heads, embedding size) significantly improves performance.
   - Hyperparameter tuning (like learning rate reduction) is crucial at larger scales.

---

### Important Insights & My Key Takeaways

These points stood out most clearly to me while watching and thinking through the lecture:

**The Asymmetry of Queries and Keys**

Initially, it felt odd to separate queries and keys, since they're computed similarly from the same input. But the asymmetry is deliberate: queries ask questions, and keys provide labels. Reversing them breaks this logic. Their differentiation is crucial for attention to correctly measure relevance between tokens.

**Masking After Attention Calculation**

At first, masking after calculating full attention scores seemed inefficient, as we’re discarding some calculations. But this makes computations easier and faster on GPUs, leveraging parallelization. The simplicity and efficiency outweigh the wasted computation.

**The Role of Value Vectors**

Values store the actual content aggregated by attention. At first, they felt redundant, but it's clear now that keys and queries only determine how much each token contributes, whereas values contain what exactly is being communicated. This distinction makes the attention mechanism powerful and expressive.

**Why Multi-Head Attention Works Well**

Having multiple heads isn’t arbitrary. Each head focuses on different features or relationships (like syntax vs. semantics). The “divide and conquer” approach is effective; it boosts representational capacity without drastically increasing complexity.

**Residual Connections: Essential for Stability**

Residual connections aren't just nice-to-have—they’re critical. They allow gradients to flow freely, preventing problems with vanishing gradients. Transformers’ depth would be severely limited without them.

**LayerNorm vs. BatchNorm**

Layer Normalization works better than Batch Normalization for Transformers because it normalizes across features, not batches. It stabilizes gradients across sequences, which BatchNorm struggles to handle. I appreciated this insight—subtle but important.

---

### Final Thoughts

Building GPT from scratch, even on a tiny dataset, clarified a lot of my confusion about Transformers. It demystified how queries, keys, values, attention, and normalization layers come together. It also showed me the importance of small implementation details like masking and residual connections, which can seem trivial at first glance but make or break the entire architecture.

Overall, Karpathy’s video made GPT’s internal workings clear and intuitive—definitely a valuable learning experience.