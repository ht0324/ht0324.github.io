# DDPM - Review
_Published: 2025-03-10_
_Tags: AI_
_Categories: Paper_
_Original: https://ht0324.github.io/blog/2025/DDPM/_

<p>This time, I’m looking at the paper <a href="https://arxiv.org/abs/2006.11239">“Denoising Diffusion Probabilistic Models”</a>, often referred to as DDPM. This paper presented impressive image generation results using diffusion models, a class of models inspired by non-equilibrium thermodynamics.</p>

<p>The core idea is quite interesting: train a model to reverse a gradual noising process. You start with structured data (like an image), progressively add Gaussian noise over many steps until only noise remains, and then train a neural network to reverse this process, starting from noise and gradually denoising it step-by-step to generate a sample.</p>

<hr />

<h3 id="key-concepts">Key Concepts</h3>

<p><strong>Forward Process (Diffusion)</strong><br />
This is a fixed (non-learned) process defined by a variance schedule. At each step <code class="language-plaintext highlighter-rouge">t</code>, a small amount of Gaussian noise is added to the data from step <code class="language-plaintext highlighter-rouge">t-1</code>. This gradually corrupts the input data towards a simple noise distribution (e.g., standard Gaussian) after <code class="language-plaintext highlighter-rouge">T</code> steps. A neat property is that you can sample the noisy state <code class="language-plaintext highlighter-rouge">x_t</code> directly from the original data <code class="language-plaintext highlighter-rouge">x_0</code> using a closed-form equation involving the cumulative product of variances (ᾱ_t), avoiding iteration.</p>

<p><strong>Reverse Process (Denoising)</strong><br />
This is the learned part. It’s also a Markov chain, aiming to reverse the forward process. Starting from pure noise <code class="language-plaintext highlighter-rouge">x_T</code>, it iteratively predicts the distribution of the previous (less noisy) state <code class="language-plaintext highlighter-rouge">x_{t-1}</code> given the current state <code class="language-plaintext highlighter-rouge">x_t</code>. Each step <code class="language-plaintext highlighter-rouge">p_θ(x_{t-1}|x_t)</code> is parameterized as a Gaussian whose mean and variance are predicted by a neural network (often a U-Net) that takes <code class="language-plaintext highlighter-rouge">x_t</code> and the timestep <code class="language-plaintext highlighter-rouge">t</code> as input.</p>

<p><strong>Training Objective (ELBO &amp; Simplified Loss)</strong><br />
Training optimizes a variational lower bound (ELBO) on the data likelihood, similar to VAEs. This ELBO can be expressed as a sum of KL divergence terms comparing the reverse process steps to tractable posteriors of the forward process. However, the authors found that a simplified objective function works very well. Instead of directly predicting the mean of the previous state <code class="language-plaintext highlighter-rouge">x_{t-1}</code>, the network is trained to predict the <em>noise</em> (ε) that was added during the corresponding forward step. The simplified objective becomes a simple mean squared error between the true noise and the predicted noise (ε_θ). This formulation connects diffusion models to denoising score matching and Langevin dynamics.</p>

<hr />

<h3 id="key-takeaways-what-i-learned">Key Takeaways (What I Learned)</h3>

<p><strong>Predicting Noise, Not the Image (Directly)</strong><br />
Initially, the idea of training the network to predict noise (ε_θ) was confusing. Why predict random noise? The insight was that it’s not predicting <em>any</em> noise, but the <em>specific</em> noise vector ε that was sampled and added to a <em>specific</em> <code class="language-plaintext highlighter-rouge">x_0</code> at a <em>specific</em> step <code class="language-plaintext highlighter-rouge">t</code> to produce the input <code class="language-plaintext highlighter-rouge">x_t</code>. By doing this across all timesteps and data points, the network learns the relationship between noise patterns and image structures at different noise levels. It learns the “directionality” needed to remove noise correctly.</p>

<p><strong>The Simplified Loss Works Surprisingly Well</strong><br />
The paper proposes using a simplified objective (L_simple, Eq. 14) which ignores the complex weighting terms present in the full variational bound (derived from Eq. 12). It’s just a mean squared error on the predicted noise. It felt like this was offloading a lot of the theoretical complexity onto the neural network’s learning capacity, but empirically, it leads to the best sample quality. This practical simplification was a significant takeaway.</p>

<p><strong>Discrete Data Needs Care at the End</strong><br />
Since the diffusion process operates in continuous space (adding Gaussian noise), but image data is typically discrete (e.g., pixel values 0-255), the final step of the reverse process needs special handling. Equation 13 describes how to get discrete log-likelihoods by integrating the final continuous Gaussian output <code class="language-plaintext highlighter-rouge">N(x_0; μ_θ(x_1, 1), σ_1^2 * I)</code> over the appropriate “bins” corresponding to each discrete pixel value. It’s a necessary step to bridge the continuous model and discrete data.</p>

<p><strong>Good Samples, Okay Likelihood</strong><br />
The paper notes that while DDPMs achieve excellent sample quality (SOTA FID scores at the time), their log-likelihoods (NLL) weren’t as competitive as some other likelihood-based models like flows or autoregressive models. This suggests an interesting trade-off: the inductive bias of the diffusion process seems particularly good for perceptual quality, even if it doesn’t assign the absolute highest probability density to the training data compared to models explicitly optimizing NLL.</p>

<p><strong>Math is Dense, Intuition is Key</strong><br />
The paper is mathematically quite dense, especially the derivations connecting the ELBO to the noise prediction objective. Following every step was challenging. However, the core intuition: reversing a gradual noising process by learning to predict the noise added at each step, is relatively clear and provides a good handle on how these models work.</p>

<p><strong>Connection to Score Matching &amp; Langevin Dynamics</strong><br />
The noise prediction parameterization <code class="language-plaintext highlighter-rouge">ε_θ</code> explicitly connects DDPM training to denoising score matching across multiple noise scales, and the sampling process resembles annealed Langevin dynamics. This provides a link to other areas of generative modeling and physics-inspired methods.</p>

<hr />

<h3 id="summary--final-thoughts">Summary &amp; Final Thoughts</h3>
<p>DDPMs offer a powerful approach to generative modeling by learning to reverse a fixed diffusion process. The key idea of predicting the added noise at each step, trained with a simplified objective, leads to SOTA sample quality. While the underlying theory is mathematically involved, the core mechanism is intuitive. The trade-off between excellent sample quality and good-but-not-best likelihood scores highlights the unique properties of this model class. It’s a dense paper, but the core ideas are worth understanding.</p>
