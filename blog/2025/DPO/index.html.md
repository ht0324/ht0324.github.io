# DPO - Review
_Published: 2025-02-17_
_Tags: AI_
_Categories: Paper_
_Original: https://ht0324.github.io/blog/2025/DPO/_

<p>In this post, I’ll share my thoughts on the paper <a href="https://arxiv.org/abs/2305.18290"><em>Direct Preference Optimization: Your Language Model is Secretly a Reward Model</em></a>, usually called DPO. It approaches Reinforcement Learning with Human Feedback (RLHF) in a simpler way.</p>

<p>The paper starts with the motivation behind alignment: aligning language models (LMs) with human preferences. Existing methods like PPO-based RLHF are effective but notoriously complex and unstable. DPO aims to simplify this by rethinking reward modeling and preference alignment.</p>

<hr />

<h3 id="key-concepts">Key Concepts</h3>

<p><strong>Direct Preference Optimization (DPO)</strong><br />
DPO removes the explicit reward modeling step that’s common in RLHF. Instead of first training a separate reward model and then using RL to maximize that reward, DPO formulates the reward implicitly within the language model itself. This allows solving the alignment problem using a supervised classification objective.</p>

<p><strong>Bradley-Terry Model</strong><br />
DPO builds upon the Bradley-Terry model, a statistical approach for estimating the probability that one option is preferred over another. While it initially seemed random that they picked such an old statistical model, it’s been used previously by OpenAI and DeepMind in RL settings. The Bradley-Terry formula gives an intuitive probability distribution over preferences, making it suitable for learning from human feedback.</p>

<p><strong>Implicit Reward Representation</strong><br />
The key insight in DPO is that the “reward” for a given output can be represented implicitly as the log ratio of the probabilities from the learned LM and a reference LM (usually the SFT or supervised fine-tuned model). Instead of explicitly modeling rewards, DPO directly optimizes this ratio to reflect human preferences.</p>

<p><strong>Simplified Objective (No RL Required)</strong><br />
By using the implicit reward representation, DPO turns preference alignment into a supervised learning problem. The objective is to increase the probability of preferred outputs and decrease the probability of non-preferred ones, scaled by a weighting term reflecting confidence in the model’s preference ranking.</p>

<hr />

<h3 id="key-takeaways-what-i-learned">Key Takeaways (What I Learned)</h3>

<p><strong>Removing the Explicit Reward Model</strong><br />
Initially, I thought the explicit reward model was essential to RLHF. It seemed natural: first learn rewards from humans, then optimize those rewards. DPO surprised me by showing you can skip that step completely. Instead of explicitly modeling human preferences, DPO encodes them directly into the language model’s probabilities. It’s neat, elegant, and way simpler.</p>

<p><strong>The Bradley-Terry Model as the Theoretical Foundation</strong><br />
At first glance, the Bradley-Terry model felt arbitrary to me (it’s a decades-old statistical model). But its use in RLHF contexts actually dates back to earlier work by OpenAI and DeepMind. Bradley-Terry is intuitive because it translates pairwise human preference data directly into probabilities. DPO leverages this model to avoid more complicated RL setups.</p>

<p><strong>DPO’s Loss Function Explained</strong><br />
The loss function in DPO initially confused me because of its signs and terms. However, the intuition eventually clicked: it increases the likelihood of preferred outputs and decreases the likelihood of dispreferred ones. The loss is weighted by how “wrong” the model is about these preferences. If the model is confident but incorrect, it makes larger corrections. This weighting makes the optimization stable and effective.</p>

<p><strong>Why Stability is Important (and How DPO Ensures it)</strong><br />
Standard RLHF methods like PPO often become unstable because they rely on explicit reward models and require careful tuning. DPO bypasses this by using a fixed reference model (usually the SFT model). By avoiding explicit reward estimation and complicated online updates, DPO remains stable, even as the model improves.</p>

<p><strong>Performance Without Complex Tuning</strong><br />
The experimental results show that DPO achieves comparable or better performance than traditional RLHF methods. It reaches high alignment quality without extensive hyperparameter tuning or complex reward sampling.</p>

<p><strong>Philosophical Shift: Overfitting vs. Generalization</strong><br />
An interesting aspect of DPO (and similar recent methods like ORPO) is that it operates entirely offline. Unlike traditional RL methods, which involve interactive environments and trajectories, DPO treats preference alignment purely as supervised learning. It’s a philosophical shift from generalization towards targeted optimization or even intentional overfitting to human preferences. It changed how I think about RLHF.</p>

<p><strong>KL Divergence and Model Drift</strong><br />
I found the authors’ point about KL divergence important but not fully explained in the paper. DPO achieves high alignment quality without significant drift from the original supervised fine-tuned (SFT) model. This matters because extensive drift can degrade other aspects of the model, such as coherence or factual accuracy. Staying close to the original SFT model helps maintain overall quality.</p>

<hr />

<h3 id="some-things-that-were-initially-confusing">Some Things That Were Initially Confusing</h3>

<ul>
  <li><strong>The leap in equation (4)</strong>: I struggled at first to understand how they substituted the optimal policy into their objective so cleanly. It made perfect sense mathematically afterward, but felt like a creative jump rather than an obvious derivation.</li>
  <li><strong>Weighted gradient interpretation</strong>: Initially, the weighting term in the gradient was counterintuitive due to signs. Eventually, I understood it as correcting more strongly when the model’s implicit reward ordering is confidently wrong.</li>
  <li><strong>KL Divergence Interpretation</strong>: It wasn’t clear to me initially why minimizing KL divergence from the reference (initial) policy is inherently desirable. Later I understood it prevents excessive drift from a stable baseline, which preserves other desirable model properties.</li>
</ul>

<hr />

<h3 id="summary--final-thoughts">Summary &amp; Final Thoughts</h3>
<p>DPO simplifies RLHF by removing the explicit reward modeling step, making fine-tuning easier, more stable, and faster. Although it’s not strictly reinforcement learning in a traditional sense (it lacks online updates and explicit reward signals), it captures the essence of aligning models to human preferences in a cleaner and more accessible way.</p>

<p>The simplicity of DPO’s core idea, implicitly encoding rewards directly into language models, is appealing. While it’s not the only method (ORPO takes this further), DPO reduces complexity without sacrificing quality.</p>
