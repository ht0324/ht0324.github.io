# Rethinking Sequence-to-Sequence - Review
_Published: 2025-04-26_
_Tags: AI_
_Categories: Paper_
_Original: https://ht0324.github.io/blog/2025/attention/_

<p>Reading foundational papers often provides a clearer perspective on how current ideas evolved. Recently, I went through the 2015 ICLR paper <a href="https://arxiv.org/abs/1409.0473">Neural Machine Translation by Jointly Learning to Align and Translate</a> by Dzmitry Bahdanau, KyungHyun Cho, and Yoshua Bengio. It tackles a core problem in early sequence-to-sequence models for machine translation.</p>

<p>The main issue they identified was the “bottleneck” inherent in the standard RNN Encoder-Decoder framework popular at the time. These models tried to compress the entire meaning of a source sentence, regardless of its length, into a single fixed-length vector. As the paper noted, this makes it difficult to handle long sentences well, performance tended to drop off significantly as sentences got longer.</p>

<p>Their proposed solution was to allow the decoder to look back at the source sentence and selectively focus on relevant parts when generating each target word. This avoids forcing all information through one fixed vector.</p>

<h3 id="key-concepts">Key Concepts</h3>

<p>Here’s a breakdown of the core ideas discussed:</p>

<ul>
  <li><strong>The Problem: Fixed-Length Vector Bottleneck:</strong> Standard encoder-decoders map an input sequence <code class="language-plaintext highlighter-rouge">x = (x_1, ..., x_{T_x})</code> to a fixed context vector <code class="language-plaintext highlighter-rouge">c</code>. The decoder then generates the output <code class="language-plaintext highlighter-rouge">y = (y_1, ..., y_{T_y})</code> based solely on <code class="language-plaintext highlighter-rouge">c</code> and previously generated words. This compression limits the model’s capacity, especially for long inputs.</li>
  <li><strong>The Solution: Alignment Mechanism (Decoder Focus):</strong> Instead of one <code class="language-plaintext highlighter-rouge">c</code>, the proposed model computes a <em>distinct</em> context vector <code class="language-plaintext highlighter-rouge">c_i</code> for each target word <code class="language-plaintext highlighter-rouge">y_i</code>. This <code class="language-plaintext highlighter-rouge">c_i</code> is a weighted sum of <em>annotations</em> <code class="language-plaintext highlighter-rouge">(h_1, ..., h_{T_x})</code> from the encoder. Each <code class="language-plaintext highlighter-rouge">h_j</code> corresponds to a source word <code class="language-plaintext highlighter-rouge">x_j</code> (or rather, the hidden state around it).</li>
  <li><strong>How it Works: Alignment Model &amp; Context Vector:</strong>
    <ul>
      <li>The weight <code class="language-plaintext highlighter-rouge">a_{ij}</code> for each annotation <code class="language-plaintext highlighter-rouge">h_j</code> when generating <code class="language-plaintext highlighter-rouge">y_i</code> depends on how well the input around position <code class="language-plaintext highlighter-rouge">j</code> aligns with the output at position <code class="language-plaintext highlighter-rouge">i</code>.</li>
      <li>These weights are calculated using an “alignment model” <code class="language-plaintext highlighter-rouge">a</code>, which takes the previous decoder hidden state <code class="language-plaintext highlighter-rouge">s_{i-1}</code> and the encoder annotation <code class="language-plaintext highlighter-rouge">h_j</code> as input to produce a score <code class="language-plaintext highlighter-rouge">e_{ij}</code>.</li>
      <li><code class="language-plaintext highlighter-rouge">e_{ij} = a(s_{i-1}, h_j)</code></li>
      <li>The weights <code class="language-plaintext highlighter-rouge">a_{ij}</code> are obtained by normalizing these scores with a softmax: <code class="language-plaintext highlighter-rouge">a_{ij} = exp(e_{ij}) / Σ_k exp(e_{ik})</code>.</li>
      <li>The context vector <code class="language-plaintext highlighter-rouge">c_i</code> is then the weighted sum: <code class="language-plaintext highlighter-rouge">c_i = Σ_j a_{ij} h_j</code>.</li>
      <li>Crucially, the alignment model <code class="language-plaintext highlighter-rouge">a</code> (parameterized as a small feedforward network) is trained <em>jointly</em> with the rest of the system.</li>
    </ul>
  </li>
  <li><strong>Soft vs. Hard Alignment:</strong> The paper uses the term “soft alignment.” This contrasts with “hard alignment,” which would involve making a deterministic choice of which single source word aligns with the target word. Soft alignment uses a weighted average over <em>all</em> source annotations. This makes the mechanism differentiable and allows the model to learn alignments implicitly through backpropagation. It also naturally handles situations where a target word might depend on multiple source words, or vice-versa.</li>
  <li><strong>The Encoder: Bidirectional RNN (BiRNN):</strong> To ensure the annotation <code class="language-plaintext highlighter-rouge">h_j</code> captures context from both before and after the source word <code class="language-plaintext highlighter-rouge">x_j</code>, they used a BiRNN. This consists of a forward RNN processing the sequence from <code class="language-plaintext highlighter-rouge">x_1</code> to <code class="language-plaintext highlighter-rouge">x_{T_x}</code> and a backward RNN processing it from <code class="language-plaintext highlighter-rouge">x_{T_x}</code> to <code class="language-plaintext highlighter-rouge">x_1</code>. The annotation <code class="language-plaintext highlighter-rouge">h_j</code> is the concatenation of the forward hidden state <code class="language-plaintext highlighter-rouge">\vec{h}_j</code> and the backward hidden state <code class="language-plaintext highlighter-rouge">\cev{h}_j</code>. While BiRNNs weren’t new, their use here makes sense for creating richer annotations.</li>
</ul>

<h3 id="key-takeaways">Key Takeaways</h3>

<p>Reflecting on the paper, several points stand out:</p>

<ul>
  <li><strong>Performance Improvement (Especially on Long Sentences):</strong> The results clearly show the benefit. The standard RNNencdec model’s performance drops sharply with sentence length, while the proposed RNNsearch model remains much more robust. The BLEU scores confirm a significant improvement, bringing NMT closer to traditional phrase-based systems of the time.</li>
  <li><strong>Interpretability via Alignment:</strong> The alignment weights <code class="language-plaintext highlighter-rouge">a_{ij}</code> can be visualized. This provides insight into what parts of the source sentence the model focuses on when generating a specific target word. The visualizations showed mostly monotonic alignments (as expected between English and French) but also the ability to handle local reordering (like adjective-noun flips) correctly. This interpretability is a nice side effect compared to trying to understand a monolithic RNN.</li>
  <li><strong>Handling Reordering and Length Differences:</strong> The soft alignment naturally deals with source and target phrases having different lengths or requiring non-trivial mappings, without needing explicit mechanisms like NULL tokens used in traditional SMT.</li>
  <li><strong>Evolutionary Link to Transformers:</strong> Reading this <em>after</em> knowing about Transformers makes the connection clear. The core mechanism, scoring source annotations based on the current decoder state, using softmax for weights, and computing a weighted sum, is essentially the attention mechanism. It reads as a precursor; the Transformer built upon this by removing recurrence and adding multi-head attention, positional encodings, etc. It’s like seeing an earlier stage in the “evolution” of sequence models.</li>
</ul>

<h3 id="summary--final-thoughts">Summary &amp; Final Thoughts</h3>

<p>This paper reads as a big step in NMT. It addressed a clear limitation (the fixed-length vector bottleneck) with a straightforward solution: allowing the model to learn where to focus in the source sequence. The “soft alignment” mechanism introduced is, in essence, the attention mechanism that became central to later architectures like the Transformer.</p>

<p>Looking back now, the ideas seem intuitive, but implementing this effectively and showing its benefits in 2014/2015 was a contribution. It’s a clear paper that explains the problem, the proposed solution, and provides evidence. Reading it helps appreciate the progression of ideas leading to the models we use today.</p>
