# DeepSeek-V2 - Review
_Published: 2025-01-25_
_Tags: AI_
_Categories: Paper_
_Original: https://ht0324.github.io/blog/2025/Deepseekv2/_

<p>In this post, I’ll discuss the DeepSeek-V2 paper, <a href="https://arxiv.org/abs/2405.04434">“DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model”</a>, released by DeepSeek-AI. DeepSeek has been steadily releasing and open-sourcing language models, demonstrating consistent progress, particularly with their recent advances in Mixture-of-Experts (MoE) architectures and reinforcement learning methods.</p>

<p>DeepSeek-V2 uses a new Multi-head Latent Attention (MLA) mechanism and an optimized MoE architecture called DeepSeek-MoE. It activates only 21B out of its 236B parameters per token, reducing inference and training costs while maintaining performance. This makes DeepSeek-V2 notable in a time when models are becoming increasingly large and computationally demanding.</p>

<hr />

<h3 id="key-concepts">Key Concepts</h3>

<p><strong>Mixture-of-Experts (DeepSeek-MoE)</strong><br />
DeepSeek-V2 employs a mixture-of-experts model, where each token activates only a small fraction (21B out of 236B) of the total parameters. Instead of having fewer large experts, they increased the number of experts while reducing their size and introduced a “shared expert.” This expert always participates, leveraging the observation that certain computations are common to all tokens. This decision helps balance computational efficiency with model performance.</p>

<p><strong>Multi-head Latent Attention (MLA)</strong><br />
The MLA mechanism compresses the Key-Value (KV) cache into a latent representation. This reduces memory usage (by about 93%) and enables faster inference. Instead of storing large sparse key-value pairs explicitly, the MLA creates compact latent vectors, decompressing them only when needed.</p>

<p><strong>Group Relative Policy Optimization (GRPO)</strong><br />
For reinforcement learning alignment, DeepSeek-V2 uses GRPO, a variant of PPO that removes the need for a separate value model. Instead, GRPO samples multiple responses, calculates the average advantage among them, and optimizes directly without an additional critic network. This reduces computational overhead.</p>

<p><strong>Load Balancing via Auxiliary Loss</strong><br />
To efficiently distribute computation across multiple GPUs, DeepSeek introduces auxiliary losses for balancing device and communication loads. Although not obvious, these losses are essential for effectively training large MoE models with limited GPU resources.</p>

<hr />

<h3 id="key-takeaways-what-i-learned">Key Takeaways (What I Learned)</h3>

<p><strong>Simplicity That Works (MLA Mechanism)</strong><br />
Initially, I didn’t expect such a straightforward compression idea like MLA to boost performance. Compressing the KV cache into a latent representation is simple and effective, addressing the memory bottleneck.</p>

<p><strong>Sharing Experts is a Smart Move</strong><br />
Using a shared expert, activated by all tokens, initially sounded counterintuitive for an MoE model focused on sparse computation. But it makes sense in practice, as some computations inevitably overlap. This approach balances specialization (MoE’s strength) with necessary generalization, effectively improving both training and inference efficiency.</p>

<p><strong>Removing the Value Model from PPO (GRPO)</strong><br />
The GRPO algorithm was another interesting approach. PPO typically uses a critic (value) model to calculate advantages, but DeepSeek simplified this by averaging multiple sampled outputs to estimate advantages directly. Eliminating the extra value model cuts computational costs without hurting performance—making RL more accessible and scalable.</p>

<p><strong>Careful Load Balancing as a Necessary Trade-off</strong><br />
Using auxiliary losses to balance GPU load and communication initially felt odd because it seemed unrelated to improving model capabilities directly. However, considering resource constraints, this trade-off is practical and necessary. DeepSeek carefully integrates this efficiency measure into training, revealing the reality that model development involves balancing ideal solutions with practical constraints.</p>

<p><strong>DeepSeek’s Incremental Yet Thorough Progression</strong><br />
Following DeepSeek historically, I noticed a consistent pattern of incremental, careful improvements. Unlike other models that appear seemingly out of nowhere, DeepSeek’s progress reflects systematic improvements in both architecture and training methods, resulting in DeepSeek-V2’s impressive balance of performance and efficiency.</p>

<hr />

<h3 id="summary--final-thoughts">Summary &amp; Final Thoughts</h3>
<p>DeepSeek-V2 effectively balances efficiency, performance, and cost through thoughtful engineering choices. Techniques like MLA, shared MoE experts, and GRPO reveal that relatively simple innovations, executed thoroughly, often yield better outcomes than overly complicated architectures.</p>

<p>I appreciated their transparency and thorough documentation. Overall, DeepSeek-V2 offers lessons on efficiently scaling models without compromising performance, solidifying DeepSeek as a strong contributor in the language model space.</p>
