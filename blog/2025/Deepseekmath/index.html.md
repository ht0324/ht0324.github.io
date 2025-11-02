# DeepSeekMath - Review
_Published: 2025-01-27_
_Tags: AI_
_Categories: Paper_
_Original: https://ht0324.github.io/blog/2025/Deepseekmath/_

<p>In this post, I’m reviewing <a href="https://arxiv.org/abs/2402.03300">“DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models”</a>, which introduces DeepSeekMath 7B, a math-specialized language model.</p>

<p>What stands out about this paper is the performance of DeepSeekMath and also the philosophy behind its design. DeepSeek consistently focuses on first-principles thinking: stripping down unnecessary complexity, focusing on what’s important, and optimizing for efficiency. Given that DeepSeek operates under serious GPU constraints due to US export regulations, this emphasis on efficiency is a necessity that shapes their research trajectory.</p>

<p>The key technical contribution of this paper is <strong>Group Relative Policy Optimization (GRPO)</strong>: a modification of <a href="https://arxiv.org/abs/1707.06347">Proximal Policy Optimization (PPO)</a> that eliminates the need for a separate value model, making RL more efficient.</p>

<hr />

<h3 id="key-concepts">Key Concepts</h3>

<p><strong>Mathematical Reasoning in LLMs</strong><br />
Mathematical reasoning is tough for language models. Unlike general NLP tasks, where fluency and coherence are enough, math requires structured problem-solving. DeepSeekMath is specifically trained with 120B math-related tokens and fine-tuned with reinforcement learning to improve its reasoning ability.</p>

<p><strong>RL for Mathematical Reasoning</strong><br />
DeepSeekMath uses RL to refine its outputs by training with a reward model. Instead of just relying on standard instruction tuning, RL helps align model responses towards more precise and logically structured solutions.</p>

<p><strong>Group Relative Policy Optimization</strong><br />
GRPO is the highlight of the paper. It’s a <strong>compute-efficient</strong> alternative to standard PPO. Traditional PPO requires a separate value model to estimate advantage, which is computationally expensive. Instead, GRPO ranks multiple sampled responses and calculates rewards based on their relative ranking, removing the need for an explicit value function. This aligns well with the original spirit of PPO while making it much more efficient.</p>

<p><strong>Why Efficiency Matters Here</strong><br />
DeepSeek, as a company, has repeatedly <a href="https://www.thefai.org/posts/deepseek-s-success-reinforces-the-case-for-export-controls">emphasized</a> that their biggest bottleneck is compute, not talent. This constraint forces them to innovate in ways that maximize training efficiency. By making reinforcement learning more efficient, GRPO allows them to run <strong>more iterations</strong> of training within the same compute budget. Given that experience (the number of training iterations) is a critical factor in model performance, this approach compounds over time.</p>

<hr />

<h3 id="key-takeaways-what-i-learned">Key Takeaways (What I Learned)</h3>

<p><strong>First-Principles Thinking in Model Design</strong><br />
One of the biggest takeaways from this paper is how DeepSeek consistently strips things down to what actually matters. <strong>The removal of the value model in PPO is a prime example of this.</strong> Instead of treating it as an unavoidable cost, they found a way to compute advantage <strong>without it</strong>, saving compute while still aligning with the core principle of PPO.</p>

<p><strong>Reinforcement Learning Efficiency Can Directly Impact Model Performance</strong><br />
A lot of research in RL for LLMs focuses on making models “better”, but this paper indirectly makes another point: <strong>efficiency itself is a performance factor</strong>. If you can run 2x or 3x more RL iterations for the same compute budget, you might end up with a better-trained model even if the method itself isn’t inherently more powerful. This is a perspective that isn’t always emphasized but makes sense in practice.</p>

<p><strong>GRPO Addresses a Known Problem</strong><br />
PPO’s requirement for a separate value model has long been a pain point due to its added complexity and compute cost. GRPO solves this by leveraging relative ranking instead of absolute value estimation. What I like about this approach is that it’s not a random heuristic; it aligns <strong>better</strong> with the fundamental idea of PPO while also making it more practical. This kind of solution, where something becomes both <em>simpler</em> and <em>better</em>, is rare and worth noting.</p>

<p><strong>DeepSeek’s Efficiency-Focused Strategy and Results</strong><br />
The efficiency-first approach DeepSeek is taking is starting to show results. It’s easy to get caught up in scaling laws and assume more compute is always better, but DeepSeek suggests that <strong>how</strong> you use that compute is important. By optimizing RL efficiency, they can squeeze more training out of their limited resources, which in turn can compound into better models. This approach appears to be working, as seen later in DeepSeek R1, which had a notable impact.</p>

<hr />

<h3 id="summary--final-thoughts">Summary &amp; Final Thoughts</h3>

<p>DeepSeekMath shows how efficiency-driven research can lead to improvements. GRPO streamlines PPO by removing the need for a value model, reducing computational cost while staying true to the original PPO formulation. This enables DeepSeek to run more RL iterations, which in turn can lead to better-trained models.</p>

<p>This paper reinforces the idea that <strong>efficiency is a core factor that directly influences model performance</strong>. It also shows how taking a first-principles approach to ML research can lead to both simpler and more effective solutions. While DeepSeekMath itself is a good model for mathematical reasoning, I think the bigger impact of this work is in how it shapes reinforcement learning efficiency going forward.</p>
