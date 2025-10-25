---
layout: post
title: Rethinking Sequence-to-Sequence - Review
date: 2025-04-26 09:00:00
description: Looking back at the 2015 paper that introduced an attention-like mechanism to NMT.
tags: AI
categories: Paper
giscus_comments: true
---

Reading foundational papers often provides a clearer perspective on how current ideas evolved. Recently, I went through the 2015 ICLR paper [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473) by Dzmitry Bahdanau, KyungHyun Cho, and Yoshua Bengio. It tackles a core problem in early sequence-to-sequence models for machine translation.

The main issue they identified was the "bottleneck" inherent in the standard RNN Encoder-Decoder framework popular at the time. These models tried to compress the entire meaning of a source sentence, regardless of its length, into a single fixed-length vector. As the paper noted, this makes it difficult to handle long sentences well, performance tended to drop off significantly as sentences got longer.

Their proposed solution was to allow the decoder to look back at the source sentence and selectively focus on relevant parts when generating each target word. This avoids forcing all information through one fixed vector.

### Key Concepts

Here's a breakdown of the core ideas discussed:

*   **The Problem: Fixed-Length Vector Bottleneck:** Standard encoder-decoders map an input sequence `x = (x_1, ..., x_{T_x})` to a fixed context vector `c`. The decoder then generates the output `y = (y_1, ..., y_{T_y})` based solely on `c` and previously generated words. This compression limits the model's capacity, especially for long inputs.
*   **The Solution: Alignment Mechanism (Decoder Focus):** Instead of one `c`, the proposed model computes a *distinct* context vector `c_i` for each target word `y_i`. This `c_i` is a weighted sum of *annotations* `(h_1, ..., h_{T_x})` from the encoder. Each `h_j` corresponds to a source word `x_j` (or rather, the hidden state around it).
*   **How it Works: Alignment Model & Context Vector:**
    *   The weight `a_{ij}` for each annotation `h_j` when generating `y_i` depends on how well the input around position `j` aligns with the output at position `i`.
    *   These weights are calculated using an "alignment model" `a`, which takes the previous decoder hidden state `s_{i-1}` and the encoder annotation `h_j` as input to produce a score `e_{ij}`.
    *   `e_{ij} = a(s_{i-1}, h_j)`
    *   The weights `a_{ij}` are obtained by normalizing these scores with a softmax: `a_{ij} = exp(e_{ij}) / Σ_k exp(e_{ik})`.
    *   The context vector `c_i` is then the weighted sum: `c_i = Σ_j a_{ij} h_j`.
    *   Crucially, the alignment model `a` (parameterized as a small feedforward network) is trained *jointly* with the rest of the system.
*   **Soft vs. Hard Alignment:** The paper uses the term "soft alignment." This contrasts with "hard alignment," which would involve making a deterministic choice of which single source word aligns with the target word. Soft alignment uses a weighted average over *all* source annotations. This makes the mechanism differentiable and allows the model to learn alignments implicitly through backpropagation. It also naturally handles situations where a target word might depend on multiple source words, or vice-versa.
*   **The Encoder: Bidirectional RNN (BiRNN):** To ensure the annotation `h_j` captures context from both before and after the source word `x_j`, they used a BiRNN. This consists of a forward RNN processing the sequence from `x_1` to `x_{T_x}` and a backward RNN processing it from `x_{T_x}` to `x_1`. The annotation `h_j` is the concatenation of the forward hidden state `\vec{h}_j` and the backward hidden state `\cev{h}_j`. While BiRNNs weren't new, their use here makes sense for creating richer annotations.

### Key Takeaways

Reflecting on the paper, several points stand out:

*   **Performance Improvement (Especially on Long Sentences):** The results clearly show the benefit. The standard RNNencdec model's performance drops sharply with sentence length, while the proposed RNNsearch model remains much more robust. The BLEU scores confirm a significant improvement, bringing NMT closer to traditional phrase-based systems of the time.
*   **Interpretability via Alignment:** The alignment weights `a_{ij}` can be visualized. This provides insight into what parts of the source sentence the model focuses on when generating a specific target word. The visualizations showed mostly monotonic alignments (as expected between English and French) but also the ability to handle local reordering (like adjective-noun flips) correctly. This interpretability is a nice side effect compared to trying to understand a monolithic RNN.
*   **Handling Reordering and Length Differences:** The soft alignment naturally deals with source and target phrases having different lengths or requiring non-trivial mappings, without needing explicit mechanisms like NULL tokens used in traditional SMT.
*   **Evolutionary Link to Transformers:** Reading this *after* knowing about Transformers makes the connection clear. The core mechanism, scoring source annotations based on the current decoder state, using softmax for weights, and computing a weighted sum, is essentially the attention mechanism. It reads as a precursor; the Transformer built upon this by removing recurrence and adding multi-head attention, positional encodings, etc. It's like seeing an earlier stage in the "evolution" of sequence models.

### Summary & Final Thoughts

This paper reads as a big step in NMT. It addressed a clear limitation (the fixed-length vector bottleneck) with a straightforward solution: allowing the model to learn where to focus in the source sequence. The "soft alignment" mechanism introduced is, in essence, the attention mechanism that became central to later architectures like the Transformer.

Looking back now, the ideas seem intuitive, but implementing this effectively and showing its benefits in 2014/2015 was a contribution. It's a clear paper that explains the problem, the proposed solution, and provides evidence. Reading it helps appreciate the progression of ideas leading to the models we use today.
