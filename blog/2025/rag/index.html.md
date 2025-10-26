# RAG - Review
_Published: 2025-04-10_
_Tags: AI_
_Categories: Paper_
_Original: https://ht0324.github.io/blog/2025/rag/_

<p>This time, I’m looking back at the paper <a href="https://arxiv.org/abs/2005.11401">“Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks”</a> by Lewis et al. from Facebook AI Research (published 2020, v4 2021). Although it’s a few years old now, it laid out some foundational ideas for combining large language models with external knowledge retrieval. The core concept is to augment the generation process by first retrieving relevant documents and then conditioning the language model on both the original input and the retrieved text.</p>

<p>Looking at the architecture diagram felt familiar: encoding queries and documents, finding similar documents via vector search (like MIPS), and feeding them into a generator. However, the paper’s framing around combining “parametric memory” (knowledge stored in the LLM’s weights) and “non-parametric memory” (the external document index) was an interesting perspective.</p>

<p>The paper explores how to effectively combine these two memory types, proposing specific methods for training and decoding, particularly focusing on sequence-to-sequence tasks.</p>

<hr />

<h3 id="key-concepts">Key Concepts</h3>

<p><strong>Hybrid Memory: Parametric + Non-Parametric</strong><br />
RAG models explicitly combine two types of knowledge storage:</p>
<ul>
  <li><strong>Parametric Memory:</strong> The knowledge implicitly learned and stored within the parameters of a pre-trained sequence-to-sequence model (like BART in the paper).</li>
  <li><strong>Non-Parametric Memory:</strong> An external knowledge source, typically a large corpus of text (like Wikipedia), indexed for fast retrieval. In RAG, this is often a dense vector index accessed via a neural retriever (like DPR).</li>
</ul>

<p><strong>Core Architecture</strong><br />
The system generally consists of:</p>
<ul>
  <li><strong>Retriever (<code class="language-plaintext highlighter-rouge">p_η(z|x)</code>):</strong> Takes an input <code class="language-plaintext highlighter-rouge">x</code> and retrieves a set of relevant documents <code class="language-plaintext highlighter-rouge">z</code> from the non-parametric memory. This involves a query encoder and a document index (often pre-computed document embeddings). The query encoder is typically fine-tuned.</li>
  <li><strong>Generator (<code class="language-plaintext highlighter-rouge">p_θ(y|x, z)</code>):</strong> A sequence-to-sequence model (like BART) that takes the original input <code class="language-plaintext highlighter-rouge">x</code> and a retrieved document <code class="language-plaintext highlighter-rouge">z</code> to generate the output sequence <code class="language-plaintext highlighter-rouge">y</code>.</li>
</ul>

<p><strong>RAG-Sequence vs. RAG-Token Models</strong><br />
The paper proposes two main variants based on how retrieval and generation interact:</p>
<ul>
  <li><strong>RAG-Sequence:</strong> Retrieves a <em>single</em> set of documents based on the input <code class="language-plaintext highlighter-rouge">x</code> and uses the <em>same</em> document <code class="language-plaintext highlighter-rouge">z</code> (from the retrieved set) to generate the <em>entire</em> output sequence <code class="language-plaintext highlighter-rouge">y</code>. The final probability <code class="language-plaintext highlighter-rouge">p(y|x)</code> involves marginalizing (summing) the sequence probability <code class="language-plaintext highlighter-rouge">p_θ(y|x, z)</code> over the top-k retrieved documents <code class="language-plaintext highlighter-rouge">z</code>, weighted by the retriever probability <code class="language-plaintext highlighter-rouge">p_η(z|x)</code>.</li>
  <li><strong>RAG-Token:</strong> Can potentially use a <em>different</em> document <code class="language-plaintext highlighter-rouge">z</code> for <em>each</em> token <code class="language-plaintext highlighter-rouge">y_i</code> being generated. At each step <code class="language-plaintext highlighter-rouge">i</code>, it calculates the probability of the next token by marginalizing over the top-k documents, conditioned on <code class="language-plaintext highlighter-rouge">x</code> and the previously generated tokens <code class="language-plaintext highlighter-rouge">y_{1:i-1}</code>. The final sequence probability is the product of these per-token probabilities.</li>
</ul>

<p><strong>Decoding Strategies for RAG-Sequence</strong><br />
Because the RAG-Sequence likelihood <code class="language-plaintext highlighter-rouge">p(y|x)</code> involves a sum over documents, it doesn’t factorize neatly per token, making standard beam search difficult. The paper proposes:</p>
<ul>
  <li><strong>Thorough Decoding:</strong> Run beam search separately for <em>each</em> of the top-k documents <code class="language-plaintext highlighter-rouge">z</code>, generating a set of candidate sequences <code class="language-plaintext highlighter-rouge">Y</code>. For each candidate <code class="language-plaintext highlighter-rouge">y</code> in <code class="language-plaintext highlighter-rouge">Y</code>, calculate its full probability <code class="language-plaintext highlighter-rouge">p_θ(y|x, z_i)</code> for <em>every</em> document <code class="language-plaintext highlighter-rouge">z_i</code> in the top-k set. If <code class="language-plaintext highlighter-rouge">y</code> wasn’t found in the beam search for a specific <code class="language-plaintext highlighter-rouge">z_i</code>, run an “additional forward pass” to compute this probability. Finally, calculate the marginal score for <code class="language-plaintext highlighter-rouge">y</code> by summing <code class="language-plaintext highlighter-rouge">p_η(z_i|x) * p_θ(y|x, z_i)</code> across all <code class="language-plaintext highlighter-rouge">z_i</code>.</li>
  <li><strong>Fast Decoding:</strong> An approximation to speed things up. After generating the candidate set <code class="language-plaintext highlighter-rouge">Y</code> from the per-document beam searches, assume <code class="language-plaintext highlighter-rouge">p_θ(y|x, z_i) ≈ 0</code> if <code class="language-plaintext highlighter-rouge">y</code> did not appear in the beam search results for document <code class="language-plaintext highlighter-rouge">z_i</code>. This avoids the need for additional forward passes.</li>
</ul>

<hr />

<h3 id="key-takeaways-what-i-learned">Key Takeaways (What I Learned)</h3>

<p><strong>Parametric/Non-Parametric Framing and Symbolic AI Links</strong><br />
The paper’s distinction between parametric and non-parametric memory resonated with ongoing discussions about pure neural vs. hybrid AI systems (like those involving LeCun or Chollet). RAG explicitly incorporates a non-parametric, retrieval component (which feels somewhat symbolic, like a lookup or search) alongside the parametric LLM. Seeing this framing in a relatively early paper helped contextualize the idea that many powerful “LM” systems aren’t purely parametric end-to-end functions but incorporate structured components.</p>

<p><strong>Untangling RAG-Sequence Decoding</strong><br />
This was the most complex part for me initially. The key steps that became clearer through discussion were:</p>
<ol>
  <li>Run separate beam searches conditioned on each top-k document <code class="language-plaintext highlighter-rouge">z_i</code>.</li>
  <li>Collect <em>all unique</em> hypotheses <code class="language-plaintext highlighter-rouge">y</code> generated across <em>all</em> these beams into a set <code class="language-plaintext highlighter-rouge">Y</code>.</li>
  <li>For <em>each</em> hypothesis <code class="language-plaintext highlighter-rouge">y</code> in <code class="language-plaintext highlighter-rouge">Y</code>, calculate its final score by summing its weighted probability across <em>all</em> top-k documents: <code class="language-plaintext highlighter-rouge">Score(y) = Σ [ p_η(z_i|x) * p_θ(y|x, z_i) ]</code>.</li>
  <li>The tricky part: If a specific <code class="language-plaintext highlighter-rouge">y</code> wasn’t found in the beam search for a specific <code class="language-plaintext highlighter-rouge">z_i</code>, “Thorough Decoding” requires calculating that missing <code class="language-plaintext highlighter-rouge">p_θ(y|x, z_i)</code>.</li>
  <li><strong>How the “Additional Forward Pass” Works:</strong> This isn’t about retrieving more documents. It means taking the generator model, feeding it <code class="language-plaintext highlighter-rouge">x</code> and <code class="language-plaintext highlighter-rouge">z_i</code>, and <em>forcing</em> it to generate the sequence <code class="language-plaintext highlighter-rouge">y</code> token-by-token. At each step <code class="language-plaintext highlighter-rouge">j</code>, you look at the probability the model’s softmax layer assigned to the <em>actual</em> token <code class="language-plaintext highlighter-rouge">y_j</code> (even if it wasn’t the most likely token). Multiplying these probabilities gives the sequence probability <code class="language-plaintext highlighter-rouge">p_θ(y|x, z_i)</code>. This probability might be low, but it’s non-zero. “Fast Decoding” just approximates these low probabilities as zero to save computation.</li>
</ol>

<p><strong>Beam Search for Task-Specific Accuracy vs. LM Generation</strong><br />
It clicked that the use of beam search here feels different from typical open-ended LM generation. For tasks like QA where RAG is often applied, there’s usually a more specific target answer. Beam search helps explore different generation paths conditioned on different evidence documents to find the overall most probable <em>correct</em> answer according to the model’s combined parametric and non-parametric knowledge. This contrasts with sampling strategies in generative LMs aiming for creativity or diversity rather than a single best factual output.</p>

<p><strong>The Synthesis Advantage</strong><br />
The paper (and our discussion) highlighted a key benefit of RAG over purely extractive QA systems. Because RAG <em>generates</em> the final answer based on retrieved context, it can synthesize information or rephrase findings from multiple documents. An extractive system can only return verbatim spans. This ability to combine evidence is useful, as shown in examples where RAG might pull different facts or phrasings from different retrieved passages to construct the final answer.</p>

<hr />

<h3 id="summary--final-thoughts">Summary &amp; Final Thoughts</h3>
<p>The RAG paper introduced a framework for combining the generative power of large sequence-to-sequence models with the knowledge stored in external text corpora. By retrieving relevant documents first and conditioning generation on them, RAG aims to produce more factual and specific outputs, especially for knowledge-intensive tasks.</p>

<p>The distinction between the RAG-Sequence and RAG-Token approaches, and particularly the detailed decoding strategies proposed for RAG-Sequence (Thorough vs. Fast), show that effectively integrating retrieval requires careful thought beyond just concatenating text. It’s more complex than a simple embed-retrieve-generate pipeline, involving marginalization and specific search/scoring techniques like beam search per document.</p>

<p>Reflecting on it now, RAG represents a step in making LLMs more grounded and verifiable, bridging the gap between purely parametric models and external knowledge sources. It also highlights the ongoing evolution of AI architectures, moving towards hybrid systems that leverage different kinds of computation and memory.</p>
