# Mamba - Review
_Published: 2025-02-10_
_Tags: AI_
_Categories: Paper_
_Original: https://ht0324.github.io/blog/2025/Mamba/_

<p>This time I’m reviewing <a href="https://arxiv.org/abs/2312.00752">“Mamba: Linear-Time Sequence Modeling with Selective State Spaces”</a>, a paper aiming to replace attention in Transformers with <a href="https://arxiv.org/abs/2111.00396">state space models (SSMs)</a> which I covered <a href="/blog/2025/S4">here</a> that scale linearly with sequence length. The main idea is to introduce “selectivity” into state-space models, enabling them to dynamically focus on or ignore parts of the input, which helps address limitations in traditional Transformer attention models. While interesting, I found this paper particularly challenging, both intuitively and conceptually, due to its complexity and depth of prior research.</p>

<hr />

<h3 id="key-concepts">Key Concepts</h3>

<p><strong>Selective State Space Models (SSMs)</strong><br />
The core idea is to use SSMs, traditionally linear and time-invariant (LTI), but introduce selectivity so the parameters can dynamically adapt based on input content. This modification breaks the time-invariance and allows the model to selectively remember or ignore information depending on the input. It’s somewhat similar to gating in LSTMs, but more general.</p>

<p><strong>Time-Invariance and Its Breakage</strong><br />
Typical SSMs, like the previous S4 model, are time-invariant, meaning model parameters don’t change with the input or sequence position. Mamba intentionally breaks this constraint, allowing the state update parameters (like the matrix $\Delta$) to be dynamically computed based on the current input. This lets the model “select” what to remember or forget based on the input content.</p>

<p><strong>Parallelism (Training vs. Inference)</strong><br />
During training, Mamba operates in a parallel (convolution-like) mode for efficiency. During inference, it runs in a sequential (recurrent) mode, calculating one step at a time. This hybrid approach gives both efficiency (during training) and flexibility (during inference).</p>

<p><strong>Dimensions (D vs. N confusion)</strong><br />
In Mamba, each input channel or embedding dimension (denoted as D) has its own independent state-space model. Within these channels, there’s a latent dimension N that represents the internal hidden state. This separation was tricky to grasp. In simpler terms, each embedding dimension independently runs its own selective SSM with a small latent state N; these dimensions don’t directly interact during the Mamba step.</p>

<p><strong>Broadcasting and Selective Updates ($\Delta$ parameter)</strong><br />
A key detail is that the selectivity parameter $\Delta$ is computed from the input and broadcasted across dimensions. $\Delta$ essentially decides how strongly to integrate the current input into the hidden state. A larger $\Delta$ resets the hidden state to pay attention to the current input, while a smaller $\Delta$ lets the hidden state carry more historical information.</p>

<p><strong>Connection to Gated Mechanisms (LSTMs)</strong><br />
I realized that Mamba closely resembles gated RNNs like LSTMs. Indeed, the authors explicitly mention that when simplified, selective SSMs reduce to an LSTM-like gate mechanism. Mamba can be thought of as a refined and generalized form of an LSTM, just scaled up and implemented more efficiently.</p>

<hr />

<h3 id="key-takeaways-what-i-learned">Key Takeaways (What I Learned)</h3>

<p><strong>Selective Attention</strong><br />
Mamba is an advanced form of RNN or LSTM without using explicit attention. By dynamically adjusting how strongly it integrates each input, it selectively “attends” to important tokens. This felt like a neat solution that addresses the drawbacks of simple recurrent models (which can’t selectively filter out irrelevant context) and convolutions (which see everything globally but without context-specific adjustments).</p>

<p><strong>Linear-time Sequence Modeling</strong><br />
Transformers scale quadratically with sequence length, limiting practicality for very long sequences. Mamba achieves linear-time scaling because the state updates happen independently per channel, avoiding attention’s quadratic complexity. This means it can scale efficiently to very long sequences, like millions of tokens.</p>

<p><strong>Compression vs. Retrieval Trade-off</strong><br />
An important trade-off is what Mamba makes compared to attention models. Attention can retrieve information from any position losslessly because it explicitly connects tokens. Mamba, however, compresses all context into a hidden state vector. This is memory-efficient but lossy. If crucial information from the distant past isn’t preserved carefully, the model might lose it permanently. On the other hand, this compression is precisely what makes Mamba efficient.</p>

<p>For tasks like “needle in a haystack”—finding rare but critical information—this should be a disadvantage, but Mamba performs well. My guess is the model learned effective strategies for compressing and selectively preserving crucial information.</p>

<p><strong>Complexity and Interpretability Issues</strong><br />
Mamba is a theoretically elegant but practically complex model. Its architecture is dense, with a lot of prior literature, especially around the S4 and S6 architectures from Albert Gu and others. Understanding Mamba deeply requires solid familiarity with foundational SSM concepts, which can be daunting without prior study. This complexity might affect its adoption, even if performance is strong.</p>

<p><strong>Hardware-Aware Optimization</strong><br />
Another aspect that stood out was Mamba’s hardware optimization. They discuss parallel scans, kernel fusion, and reducing computational overhead by taking advantage of structured matrices. These optimizations are critical because Mamba inherently loses some parallel efficiency due to its recurrence. However, these steps mitigate performance drawbacks.</p>

<hr />

<h3 id="summary--final-thoughts">Summary &amp; Final Thoughts</h3>
<p>Mamba tries to replace attention-based Transformers with a linear-time, recurrent, state-space-based approach enhanced by dynamic selectivity. By breaking the traditional LTI assumption, it gains the flexibility to adapt its hidden states selectively, efficiently modeling long sequences. However, this brings trade-offs in interpretability, retrieval capacity, and complexity.</p>

<p>Ultimately, Mamba offers a practical alternative to Transformers for handling very long sequences. I see it less as a universal replacement and more as a specialized architecture optimized for scenarios where efficient, long-range modeling with moderate compressive trade-offs makes sense.</p>

<p>It’s interesting, but I think its complexity and rigidity might limit broader adoption compared to simpler architectures like Transformers or even more straightforward RNN variants. The idea itself is clever and worth exploring further, but for now it feels more niche than general-purpose.</p>
