# Transformer Circuits(Anthropic) - Review
_Published: 2025-01-13_
_Tags: AI_
_Categories: Paper_
_Original: https://ht0324.github.io/blog/2025/Transformer-Circuits/_

<p>This post reviews the paper “<a href="https://transformer-circuits.pub/2021/framework/index.html">A Mathematical Framework for Transformer Circuits</a>” by Anthropic. The authors take a clear, step-by-step approach to understanding how attention heads work in simplified transformer models, focusing especially on how the internal mechanics of these models can be mathematically described and interpreted. It’s a dense paper but an insightful one; I picked up a few high‑level ideas I hadn’t seen before.</p>

<hr />

<h3 id="key-concepts">Key Concepts</h3>

<p><strong>1. Attention Heads as Independent Operations</strong><br />
Attention heads are usually presented as concatenating their outputs and then multiplying by a large projection matrix (<code class="language-plaintext highlighter-rouge">W_O</code>). However, the authors emphasize a more intuitive (though mathematically equivalent) interpretation: attention heads independently compute results and add them directly to the residual stream. This simpler view helps clarify how a single head behaves, even as the implementation stays efficient via concatenation.</p>

<p><strong>2. Residual Stream as a Communication Channel</strong><br />
The residual stream is a shared space where layers communicate intermediate results. Each attention or MLP layer can both “read” from and “write” into it, allowing layers to build increasingly sophisticated and context-aware representations. This means the residual stream carries information about token meanings, syntactic roles, semantic relationships, and intermediate predictions — a shared whiteboard among specialists.</p>

<p><strong>3. Virtual Weights and Composing Layers</strong><br />
Each transformer layer performs linear transformations on the residual stream. When layers interact, these transformations can be multiplied out, forming “virtual weights,” which directly connect non-adjacent layers. Instead of thinking of each layer independently, virtual weights represent the total combined transformation of several layers together, like composing several functions into a single step.</p>

<p><strong>4. QK and OV Circuits: “Which” vs. “What”</strong><br />
Attention heads split their tasks clearly into two components:</p>
<ul>
  <li><strong>QK circuit (Query-Key)</strong> decides <strong>which</strong> tokens to pay attention to.</li>
  <li><strong>OV circuit (Output-Value)</strong> decides <strong>what</strong> information from the selected tokens should be communicated.</li>
</ul>

<p>Separating these operations makes attention modular, allowing heads to specialize. It’s like a mail delivery system where route-planning (QK) is separate from package-handling (OV).</p>

<p><strong>5. Skip-Trigrams in One-Layer Transformers</strong><br />
A one-layer transformer (attention-only) can model relationships called skip-trigrams, patterns of the form “A… B C.” The QK circuit identifies the earlier token (A), while the OV circuit determines how it affects the likelihood of a later token (C), given the current context (B). It shows the transformer’s ability to capture context across short sequences effectively.</p>

<p><strong>6. Copying and Primitive In-Context Learning</strong><br />
One-layer attention heads often learn simple copying behavior: predicting a token identical to or closely related to an earlier one. Although basic, this copying behavior represents a primitive form of in-context learning, as the model uses context to influence predictions. It’s limited but forms the foundational mechanism upon which more advanced contextual adaptation is built.</p>

<p><strong>7. Induction Heads and Advanced In-Context Learning</strong><br />
Two-layer transformers introduce <strong>induction heads</strong>, a more advanced mechanism for in-context learning:</p>
<ul>
  <li>They look back in the sequence for previous occurrences of the current token.</li>
  <li>They then predict the token that historically followed that occurrence.</li>
</ul>

<p>Compared to simple copying, induction heads understand sequences and contexts better, allowing them to adapt predictions more robustly, even in completely random sequences. This mechanism relies heavily on <strong>K-composition</strong>, meaning the second layer attention head uses information from a first-layer head that attends to an earlier token. This effectively shifts attention back one token, making complex pattern matching possible.</p>

<hr />

<h3 id="key-takeaways-what-i-learned">Key Takeaways (What I Learned)</h3>

<p><strong>A Clearer Mental Model of Attention Heads</strong><br />
Previously, I viewed attention heads as opaque, intertwined mechanisms. Now, clearly separating QK (attention pattern) from OV (content selection) circuits provides a cleaner and more intuitive mental model. It makes interpreting attention heads simpler, since I can independently analyze “where the model is looking” and “what information it is moving.”</p>

<p><strong>Virtual Weights as a Useful Conceptual Tool</strong><br />
The concept of virtual weights—where interactions between distant layers are explicitly multiplied out into direct connections—was a real “aha” moment. Instead of considering each layer in isolation, understanding their combined effect simplifies interpretation and clarifies how layers collaborate to build richer representations.</p>

<p><strong>Understanding Primitive In-Context Learning (Copying)</strong><br />
Initially, I was skeptical about calling simple copying “in-context learning.” However, after reflection, I realized copying does constitute a basic form of adapting predictions based on context, even if the adaptation is trivial. This simple mechanism sets the stage for the more advanced in-context learning found in deeper transformers. Recognizing this helps me appreciate how complexity emerges incrementally.</p>

<p><strong>Induction Heads: How Transformers Learn Repetition</strong><br />
The mechanism of induction heads, especially the “shifting the key” idea via K‑composition, stood out clearly. Rather than relying solely on statistical likelihoods (as simpler copying does), induction heads effectively form sequence-based “rules” (“If you saw token A before, predict what followed A previously”). Seeing this happen even in random sequences made it clear that induction heads capture sequence structures, not just statistics.</p>

<p><strong>Analyzing Transformers Through Eigenvectors</strong><br />
I found the use of eigenvectors and eigenvalues to analyze OV circuits interesting. Eigenvectors show how the transformer clusters tokens that mutually reinforce each other’s probabilities (like groups of related words), while positive eigenvalues specifically highlight copying or self-amplifying behavior. Although this analysis isn’t perfect, it’s a useful tool to uncover meaningful structures inside the transformer’s enormous matrices.</p>

<p><strong>Limits of Current Interpretability Approaches</strong><br />
Finally, this paper clarified that while some parts of transformers are now interpretable (especially attention mechanisms and induction heads), the role of MLP layers and more complex interaction patterns remains a challenge. This work sets a clear baseline for interpretability, but fully understanding transformers still requires significant advances, especially in interpreting neuron-level behavior within MLP layers.</p>

<hr />

<h3 id="summary--final-thoughts">Summary &amp; Final Thoughts</h3>

<p>The Transformer Circuits paper offers a clear mathematical framework for understanding simplified transformers. By explicitly separating the roles of attention heads, introducing concepts like virtual weights, and highlighting how induction heads enable sophisticated in-context learning, it makes transformer internals more transparent.</p>

<p>While this approach significantly clarifies the mechanics behind simpler transformers, interpreting larger, realistic models remains challenging—especially MLP layers. Nonetheless, this framework offers solid building blocks for deeper understanding and a useful first step toward interpretable neural networks.</p>
