# Karpathy's "Let's Build GPT From Scratch" - Review
_Published: 2025-01-12_
_Tags: AI_
_Categories: Paper, Blog_
_Original: https://ht0324.github.io/blog/2025/Karpathy-gpt/_

<p>Andrej Karpathy’s video <a href="https://www.youtube.com/watch?v=kCc8FmEb1nY">“Let’s build GPT: from scratch, in code, spelled out”</a> offers a clear, practical walkthrough of implementing a simplified GPT from the ground up. Karpathy intentionally keeps things simple, training a character-level GPT on a tiny Shakespeare dataset (just 1MB), making the implementation approachable without getting lost in complexity.</p>

<p>Below is a quick summary and my main insights from going through the video:</p>

<hr />

<h3 id="key-concepts">Key Concepts</h3>

<ol>
  <li><strong>Data Preparation</strong>
    <ul>
      <li>Encodes characters into numerical tokens (65 unique tokens from Tiny Shakespeare).</li>
      <li>Data split into training (90%) and validation (10%).</li>
    </ul>
  </li>
  <li><strong>Chunking</strong>
    <ul>
      <li>Transformers use fixed-length contexts (<code class="language-plaintext highlighter-rouge">block_size</code>) rather than full text.</li>
      <li>Random sampling of batches (<code class="language-plaintext highlighter-rouge">batch_size</code>) for computational efficiency.</li>
    </ul>
  </li>
  <li><strong>Bigram Language Model</strong>
    <ul>
      <li>Simplest language model: predicting next character from current one.</li>
      <li>Uses embedding tables (<code class="language-plaintext highlighter-rouge">token embedding table</code>) to convert tokens into prediction logits.</li>
    </ul>
  </li>
  <li><strong>Self-Attention Mechanism</strong>
    <ul>
      <li>Computes relevance between tokens via queries and keys.</li>
      <li>Uses masking (<code class="language-plaintext highlighter-rouge">tril</code> matrix) to prevent looking into future tokens.</li>
    </ul>
  </li>
  <li><strong>Multi-Head Attention</strong>
    <ul>
      <li>Each head independently calculates attention on different subsets of token embeddings.</li>
      <li>Outputs from multiple heads concatenated and projected linearly.</li>
    </ul>
  </li>
  <li><strong>Feed-Forward Networks</strong>
    <ul>
      <li>Simple MLP layers placed after attention to process token-level details.</li>
      <li>Typically have 4× embedding dimensionality internally.</li>
    </ul>
  </li>
  <li><strong>Residual Connections and LayerNorm</strong>
    <ul>
      <li>Residual connections (identity pathways) make training stable, preventing vanishing gradients.</li>
      <li>Layer Normalization stabilizes activations and gradients across token dimensions.</li>
    </ul>
  </li>
  <li><strong>Scaling the Model</strong>
    <ul>
      <li>Increasing parameters (layers, heads, embedding size) significantly improves performance.</li>
      <li>Hyperparameter tuning (like learning rate reduction) is crucial at larger scales.</li>
    </ul>
  </li>
</ol>

<hr />

<h3 id="important-insights--my-key-takeaways">Important Insights &amp; My Key Takeaways</h3>

<p>These points stood out most clearly to me while watching and thinking through the lecture:</p>

<p><strong>The Asymmetry of Queries and Keys</strong></p>

<p>Initially, it felt odd to separate queries and keys, since they’re computed similarly from the same input. But the asymmetry is deliberate: queries ask questions, and keys provide labels. Reversing them breaks this logic. Their differentiation is crucial for attention to correctly measure relevance between tokens.</p>

<p><strong>Masking After Attention Calculation</strong></p>

<p>At first, masking after calculating full attention scores seemed inefficient, as we’re discarding some calculations. But this makes computations easier and faster on GPUs, using GPU parallelism. The simplicity and efficiency outweigh the wasted computation.</p>

<p><strong>The Role of Value Vectors</strong></p>

<p>Values store the actual content aggregated by attention. At first, they felt redundant, but it’s clear now that keys and queries only determine how much each token contributes, whereas values contain what exactly is being communicated. This distinction makes the attention mechanism expressive.</p>

<p><strong>Why Multi-Head Attention Works Well</strong></p>

<p>Having multiple heads isn’t arbitrary. Each head focuses on different features or relationships (like syntax vs. semantics). The “divide and conquer” approach is effective; it boosts representational capacity without drastically increasing complexity.</p>

<p><strong>Residual Connections: Essential for Stability</strong></p>

<p>Residual connections are essential in allowing gradients to flow freely, preventing problems with vanishing gradients. Transformers’ depth would be severely limited without them.</p>

<p><strong>LayerNorm vs. BatchNorm</strong></p>

<p>Layer Normalization works better than Batch Normalization for Transformers because it normalizes across features, not batches. It stabilizes gradients across sequences, which BatchNorm struggles to handle. I appreciated this subtle point.</p>

<hr />

<h3 id="final-thoughts">Final Thoughts</h3>

<p>Building GPT from scratch, even on a tiny dataset, clarified a lot of my confusion about Transformers. It clarified how queries, keys, values, attention, and normalization layers come together. It also showed me the importance of small implementation details like masking and residual connections, which can seem trivial at first glance but still matter.</p>

<p>Overall, Karpathy’s video made GPT’s internal workings clear and intuitive. It was a useful learning experience.</p>
