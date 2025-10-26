# GAN – Review
_Published: 2025-02-27_
_Tags: AI_
_Categories: Paper_
_Original: https://ht0324.github.io/blog/2025/GAN/_

<p>This time, I’m reviewing the paper <a href="https://arxiv.org/abs/1406.2661">“Generative Adversarial Nets”</a>, known as GAN. This classic 2014 paper by Ian Goodfellow and colleagues introduced adversarial training for generative models, using two networks, a generator and a discriminator.</p>

<p>The central concept is: a generator attempts to produce realistic samples to fool a discriminator, while the discriminator tries to distinguish real samples from generated ones. This competition pushes both models to improve, enabling the generator to produce realistic outputs without directly modeling complex probability distributions.</p>

<hr />

<h3 id="key-concepts">Key Concepts</h3>

<p><strong>Generator and Discriminator</strong><br />
GAN consists of two neural networks trained simultaneously. The <strong>Generator (G)</strong> learns to produce data that looks like real samples from random noise, and the <strong>Discriminator (D)</strong> learns to classify whether a given sample is real or fake. This interplay drives learning.</p>

<p><strong>Minimax Game and Value Function</strong><br />
GAN training is framed as a minimax game, where D tries to maximize its accuracy, while G tries to minimize it. Mathematically, this interaction is captured by a value function involving two competing optimization steps, one ascending (for D) and one descending (for G).</p>

<p><strong>Noise as Input (Latent Representation)</strong><br />
The generator takes random noise as input (often standard Gaussian noise), which it transforms into realistic data. This noise acts as a latent representation, similar in purpose to latent spaces in other generative models like VAE or diffusion models.</p>

<hr />

<h3 id="key-takeaways-what-i-learned">Key Takeaways (What I Learned)</h3>

<p><strong>Police vs. Counterfeiters Analogy</strong><br />
The authors’ analogy (police versus counterfeiters) makes the adversarial setup intuitive: the discriminator tries to catch counterfeit samples, while the generator improves to evade detection. The analogy clarifies the competitive dynamics and why both sides keep improving.</p>

<p><strong>Why the Order of Optimization Matters</strong><br />
In theory, the discriminator should reach optimality before the generator updates. Practically, training typically alternates between discriminator and generator updates, often simplifying to a 1:1 step ratio.</p>

<p><strong>The “Saturation” Problem</strong><br />
Initially, the idea of the generator’s gradient saturating (becoming ineffective) was unclear. The authors point out that if the discriminator becomes too strong too early, the generator’s gradients become nearly zero because it consistently outputs samples easily identified as fake. Understanding this clarified the importance of balancing the discriminator and generator strengths.</p>

<p><strong>Noise as a Form of Latent Space</strong><br />
Initially, calling the generator input “noise” felt unintuitive. Noise serves as a random seed or latent code that gets mapped to structured data, introducing randomness into an otherwise deterministic network and enabling continuous generation and interpolation in the latent space.</p>

<p><strong>Interpolation and Connection to VAEs</strong><br />
GANs achieve interpolation despite the absence of a clearly defined encoder (unlike VAEs). VAEs explicitly model latent spaces to allow interpolation, but GANs achieve this indirectly. Because the generator learns from the discriminator’s feedback rather than directly fitting discrete data points, it learns a continuous representation that supports meaningful interpolations, without explicitly modeling complicated distributions.</p>

<p><strong>Simplicity of Theoretical Results</strong><br />
The theoretical results, particularly the global optimality condition (pg = pdata), are straightforward. By defining an optimal discriminator, the proof shows a Jensen-Shannon divergence between the true and generated distributions.</p>

<p><strong>GANs vs. VAEs</strong><br />
Reflecting on VAE and GAN together: VAE explicitly approximates intractable distributions, while GAN sidesteps this via the adversarial setup. The appeal of GAN is its simplicity paired with strong discriminative feedback, which the generator leverages during training.</p>

<hr />

<h3 id="summary--final-thoughts">Summary &amp; Final Thoughts</h3>
<p>“Generative Adversarial Nets” introduced a framework that pits generators against discriminators to produce realistic data without explicitly modeling complex distributions. The combination of an intuitive training game and a clear theoretical link to divergence minimization helps explain why GANs became foundational in generative modeling.</p>

<p>Exploring GAN alongside VAE deepened my understanding of how different approaches tackle generative tasks.</p>
