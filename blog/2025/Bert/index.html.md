# BERT - Review
_Published: 2025-01-20_
_Tags: AI_
_Categories: Paper_
_Original: https://ht0324.github.io/blog/2025/Bert/_

<p>Let’s talk about a paper that’s at the heart of NLP: <a href="https://arxiv.org/abs/1810.04805">“BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding”</a>. I wanted to know why everyone went crazy about BERT, especially since its actual architecture seems straightforward. Interestingly, it was simpler than expected, and understanding it shed some light on why later models (like <a href="https://arxiv.org/abs/1907.11692">RoBERTa</a>) made the changes they did.</p>

<hr />

<h2 id="key-concepts">Key Concepts</h2>

<p><strong>Bidirectional Representation (Masked Language Modeling)</strong><br />
Instead of predicting the next word like GPT, BERT randomly masks tokens in the input sequence and forces the model to predict these masked tokens. This means BERT can look at context from both left and right simultaneously, allowing it to learn richer, bidirectional representations.</p>

<p><strong>Next Sentence Prediction (NSP)</strong><br />
BERT adds another pre-training objective called NSP. It tries to predict if two sentences are logically consecutive or randomly paired. The idea was to help BERT learn relationships between sentences, which should improve tasks like question answering and inference.</p>

<p><strong>Masked Token Prediction and Noise</strong><br />
BERT randomly masks 15% of tokens, but with a twist. Among masked tokens, 80% are replaced by <code class="language-plaintext highlighter-rouge">[MASK]</code>, 10% remain unchanged, and 10% are replaced with random tokens. This mixture prevents BERT from relying solely on trivial strategies, encouraging robustness.</p>

<p><strong>Fine-tuning over Feature-based</strong><br />
Previous methods (like ELMo) were mainly feature-based—training a model to produce embeddings and then feeding those embeddings into separate downstream models. BERT popularized the fine-tuning approach: you pre-train one model and directly adjust its parameters for downstream tasks, making the whole thing simpler and more effective.</p>

<hr />

<h3 id="key-takeaways-what-i-learned">Key Takeaways (What I Learned)</h3>

<p><strong>Why Bidirectional is Better</strong><br />
At first glance, bidirectionality seems obviously better than a single-direction model (like GPT). But traditional language models couldn’t do true bidirectionality because tokens could directly “see” themselves during training. BERT’s masking trick neatly bypasses this issue by hiding tokens randomly. Previous methods were fundamentally restricted by directionality.</p>

<p><strong>NSP—Initially Helpful, Eventually Questioned</strong><br />
The NSP task seemed sensible: training the model to understand relationships between sentence pairs should help downstream tasks like QA and NLI. However, later research (notably RoBERTa) showed that NSP wasn’t very helpful. RoBERTa dropped NSP completely and got better performance. This suggests that NSP might have introduced unnecessary bias or noise into the model’s representations.</p>

<p><strong>Robustness Through Masking</strong><br />
The masking strategy, including replacing tokens with random or unchanged tokens, seemed odd at first. But the reasoning makes sense: if the model always sees a masked token, it might get used to always predicting something new. By occasionally giving it unchanged tokens, the model can’t default to always predicting a different word. It feels like they were trying to cover all bases for robustness. It’s a subtle trick.</p>

<p><strong>Understanding RoBERTa through BERT</strong><br />
Right after reading BERT, I jumped into RoBERTa. RoBERTa basically says BERT was good but undertrained and overly complicated with NSP. They dropped NSP entirely, trained longer with dynamic masking (changing masked tokens every epoch), and used a larger and more diverse corpus. Unsurprisingly, performance improved. It clarified to me why RoBERTa, rather than the original BERT, became the go-to choice today.</p>

<p><strong>Decoder vs. Encoder Models</strong><br />
After understanding BERT and RoBERTa, it struck me that decoder models (like GPT) took over partly because their training objective (predicting the next token) is simpler, more scalable, and more versatile. Masked language modeling, while powerful, creates a gap between pre-training and fine-tuning (the [MASK] token doesn’t appear in fine-tuning). GPT’s approach naturally aligns training and inference, making generalization smoother.</p>

<p><strong>Connection with Recent Work (Fill-in-the-Middle)</strong><br />
I also remembered a recent but less-known paper <a href="https://arxiv.org/abs/2207.14255">“Fill-in-the-Middle”</a> that tries a similar idea with decoder-only models. It showed that predicting tokens masked in the middle (like BERT) could improve decoder models without any architectural changes. It felt like a nod to BERT’s approach but adapted to modern, decoder-only models. A trick for incremental performance gains.</p>

<hr />

<h3 id="summary--final-thoughts">Summary &amp; Final Thoughts</h3>
<p>BERT is simpler than it looks. It sidesteps the limitations of unidirectional language models by masking tokens randomly, achieving deep bidirectionality. Although the Next Sentence Prediction objective ended up being unnecessary (as RoBERTa later showed), BERT’s main innovation, the masked language model, is valuable. It laid down the foundations for understanding that bidirectionality can matter, but it also revealed how small, seemingly good ideas (like NSP) can introduce unexpected biases.</p>

<p>In the end, BERT’s approach taught me two things: first, that subtle adjustments (like masking instead of predicting the next word) can fundamentally shift model capabilities; and second, that just because a feature seems intuitive (like NSP), it doesn’t guarantee it will enhance performance—sometimes, simplicity works best.</p>
