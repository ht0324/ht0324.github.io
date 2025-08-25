---
layout: post
title: Circuit Tracing – Review
date: 2025-04-06 18:00:00
description: Reviewing the Anthropic paper on Circuit Tracing using Transcoders
tags: AI
categories: Paper
giscus_comments: true
---

This time, I'm looking at the Anthropic paper ["Circuit Tracing: Revealing Computational Graphs in Language Models"](https://transformer-circuits.pub/2025/attribution-graphs/methods.html). This paper is interesting because it tackles the challenge of understanding what goes on inside large language models (LLMs). Instead of treating them as black boxes, the authors propose a method to map out the model's internal computations for specific tasks into interpretable graphs. It's like trying to reverse engineer the model's "thinking process."

This paper primarily details the *methods* they developed. There's a companion paper, ["On the Biology of a Large Language Model"](https://transformer-circuits.pub/2025/attribution-graphs/biology.html), which uses these techniques to explore various findings about model internals. I decided to read this methods paper first to get a solid grasp of the techniques before diving into the "biology" results.

The core idea involves using a special type of dictionary learning model called a "cross-layer transcoder" (CLT) to replace parts of the original network (specifically, the MLP layers). This replacement allows them to build "attribution graphs" that show how information flows through interpretable "features" when the model processes a prompt. They provide detailed methods and evaluations, showing how this approach can uncover mechanisms behind various model behaviors.

---

### Key Concepts

**Cross-Layer Transcoder (CLT) & Replacement Model**  
The paper introduces CLTs as the core component. Unlike standard autoencoders that just reconstruct their input, a CLT is trained to *emulate* the output of an LLM's MLP layers using sparse, interpretable features. An encoder reads from the residual stream at one layer, activates a sparse set of features, and decoders associated with these features contribute to approximating the MLP outputs at that layer *and* subsequent layers (hence "cross-layer"). By substituting the original MLPs with these trained CLTs, they create an interpretable "replacement model."

**Attribution Graphs**  
For a specific prompt, the authors construct an attribution graph. This graph visualizes the step-by-step computation within a localized version of the replacement model. Nodes in the graph represent active CLT features, input token embeddings, reconstruction errors, and output logits. Edges represent the direct, linear influence of one node on another (calculated after freezing attention patterns and normalization constants for that prompt). These graphs aim to show the flow of information and computation leading to the model's output.

**Local Replacement Model**  
To ensure the attribution graph accurately reflects the model's output for a *specific* prompt, they use a "local" replacement model. This model uses the CLT features but also incorporates the exact attention patterns and normalization factors from the original model's run on that prompt. It also adds back any difference (error) between the CLT's output and the true MLP output at each step. This makes the local model's final output identical to the original model's for that prompt, providing a precise basis for the attribution graph.

**Features as Interpretable Units**  
The sparse activations learned by the CLTs are treated as "features", ideally, interpretable building blocks of the model's computation (e.g., representing a concept like "digital", a state like "in an acronym", or an action like "say DAG"). The goal is that circuits can be understood as interactions between these meaningful features.

**Validation via Interventions**  
The paper stresses validating the mechanisms found in attribution graphs. Since the replacement model might differ from the original, they use perturbation experiments (like activating or inhibiting specific features) in the *original* model to check if the downstream effects match what the attribution graph predicts.

---

### Key Takeaways (What I Learned)

**Transcoders vs. SAEs: Emulation, Not Just Reconstruction**  
A key distinction clicked for me: Sparse Autoencoders (SAEs) aim to reconstruct their input activations sparsely. Transcoders, however, are trained to *emulate the computation* of a component like an MLP layer, taking the MLP's input and predicting its output using sparse features. This "emulation" aspect is why they work well for circuit analysis; they directly model the transformation step, allowing feature interactions to bridge over the original non-linear MLP. The name "transcoder" feels apt: it's encoding and decoding, but transforming the signal to match a different target (the MLP output).

**Visualizing the "Thinking Process" with Graphs**  
The attribution graphs themselves are useful. Seeing the model's process laid out for a specific prompt, like generating an acronym, felt like getting a glimpse into its internal logic. The way features activate based on input tokens (like "Digital", "Analytics", "Group") and interact to promote the final output ("DAG") makes the computation more tangible than just looking at activations.

**Interactive Exploration: Opening the Black Box**  
The authors developed an interactive interface for exploring these graphs. This seems useful; it is interactive, not a static picture. It feels like having a tool to examine the model and trace the circuitry.

**Layer Progression: From Semantics to Abstraction**  
Looking at the features described and their roles in the graphs, a pattern seemed apparent, matching general intuitions about deep networks. Features in earlier layers often seem more semantic, tied closely to specific input tokens or concepts (e.g., the word "digital"). Features in later layers appear more abstract or functional, involved in manipulating information or preparing the final output (e.g., "say DAG", "sum ~92").

**Addition Circuitry and Number Representation**  
The case study on addition (e.g., `36+59=95`) was interesting. They identified different types of features involved: ones detecting properties of the input numbers ("add function features"), ones acting like lookup tables (e.g., `_6 + _9`), and ones representing properties of the sum ("sum features"). This connects to related work (which the paper cites, e.g., [this paper on helix representations](https://arxiv.org/pdf/2502.00873)) suggesting numbers might be represented in a structured way in embeddings, where arithmetic operations correspond to geometric transformations. Seeing the transcoder find features that seem to implement parts of this arithmetic process in a real model (Claude Haiku) was convincing.

**The Curious Case of the Caps Lock Token**  
A small detail I noticed in the acronym example was the tokenizer using a special "Caps Lock" token (`⇪`). I'm not sure of its exact function, but it was interesting to see it explicitly represented. Makes you wonder how these specific tokenization choices influence learning.

---

### Summary & Final Thoughts
The "Circuit Tracing" paper presents a detailed approach for mapping and understanding the internal workings of LLMs using cross-layer transcoders and attribution graphs. By replacing opaque MLP computations with interpretable feature-based emulations, it allows for detailed tracing of information flow on specific prompts.

The method seems useful, offering a way to move beyond treating LLMs as complete black boxes. The case studies, especially around acronyms and addition, provide concrete examples of the kinds of mechanisms that can be uncovered.

Thinking about the companion paper's title, "On the Biology of a Large Language Model," the term "biology" feels appropriate here. We're not analyzing traditional, rule-based systems like operating systems or computer networks, which are human-designed and follow explicit logic. Instead, these LLMs are more like systems that have been *grown* organically from vast amounts of data. Our process of understanding them involves peering inside, mapping their structures, and figuring out how different parts contribute to behavior, much like studying the anatomy and function of a biological organism. We're dissecting a synthetic brain to understand how it works. This paper provides some sharp tools for that dissection, and it is a step in the right direction for this kind of "AI biology."
