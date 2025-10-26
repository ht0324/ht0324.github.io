# NeRF - Review
_Published: 2025-02-20_
_Tags: AI_
_Categories: Paper_
_Original: https://ht0324.github.io/blog/2025/NERF/_

<p>In this post I’ll talk about the paper <a href="https://arxiv.org/abs/2003.08934">“NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis”</a>. This paper introduces NeRF, a method to represent complex scenes as continuous neural fields, enabling high-quality view synthesis from sparse images.</p>

<p>NeRF uses a simple architecture: a fully-connected neural network (MLP) that takes continuous 5D inputs (3D coordinates plus viewing angles) and outputs both color and volume density. This setup synthesizes previously unseen views by querying the network and performing differentiable volume rendering along camera rays.</p>

<hr />

<h3 id="key-concepts">Key Concepts</h3>

<p><strong>Neural Radiance Field (NeRF)</strong><br />
A NeRF is essentially a neural network that maps a 5D coordinate (3D spatial location <code class="language-plaintext highlighter-rouge">(x, y, z)</code> plus viewing direction <code class="language-plaintext highlighter-rouge">(θ, φ)</code>) to two outputs: volume density (opacity) and RGB color. It represents an entire scene within a compact neural network rather than explicitly storing a dense voxel grid or using complex 3D models.</p>

<p><strong>Volume Rendering</strong><br />
To synthesize novel views, NeRF employs classical volume rendering techniques. Camera rays traverse the scene, accumulate opacity and color values from sampled points, and project these values into an image. This process is differentiable, allowing the network to learn directly from images without explicit 3D geometry supervision.</p>

<p><strong>Positional Encoding</strong><br />
Directly feeding spatial coordinates into a neural network doesn’t capture fine details well. The authors use positional encoding, mapping coordinates into higher-dimensional spaces using sinusoidal functions to help the network learn high-frequency variations in geometry and appearance.</p>

<p><strong>Hierarchical Sampling (Coarse &amp; Fine Networks)</strong><br />
To make the rendering efficient, NeRF uses a hierarchical sampling strategy. Initially, it samples points coarsely to estimate areas of importance, then densely samples those areas with a second “fine” network. This two-stage approach improves efficiency and quality.</p>

<hr />

<h3 id="key-takeaways-what-i-learned">Key Takeaways (What I Learned)</h3>

<p><strong>The Surprising Power of Simple MLPs</strong><br />
Initially, I assumed NeRF would require complex architectures. Surprisingly, a plain fully-connected network (MLP) was sufficient. This challenged my assumption that complex scenes need complicated models; NeRF achieves complexity through smart input encoding and sampling strategies rather than architectural depth.</p>

<p><strong>Positional Encoding Makes a Huge Difference</strong><br />
At first glance, positional encoding seemed like a minor tweak. But without it, the model struggles to capture high-frequency details like textures and sharp edges. This was counterintuitive, since I thought neural networks naturally handle continuous inputs well. Positional encoding acts like a cheat sheet for frequencies the network should attend to.</p>

<p><strong>Hierarchical Sampling – Efficiency through Bias</strong><br />
The hierarchical sampling was something I wouldn’t have thought of myself. Instead of uniformly sampling every point, NeRF first broadly samples (“coarse”) to identify important regions. Then, based on these initial guesses, it strategically places more samples in regions with higher density (or significance). It effectively biases sampling toward regions that matter, improving computational efficiency.</p>

<p><strong>Overfitting as a Feature, Not a Bug</strong><br />
One realization was that NeRF intentionally overfits to a specific scene. Unlike models aimed at generalization, NeRF constructs a specialized network for each scene, optimizing for accuracy within that context. It felt unconventional but makes sense because NeRF’s goal isn’t generalization—it’s photorealistic rendering for a given scene.</p>

<p><strong>Why This Matters for Interpolation and Rendering Quality</strong><br />
NeRF’s method naturally leads to strong interpolation between views, providing realistic novel perspectives even from limited viewpoints. Because it learns a continuous representation instead of discrete samples, it produces smooth transitions between views. It’s simple and effective.</p>

<p><strong>Comparisons and Connections with VAEs and GANs</strong><br />
Reflecting on my earlier reviews (VAE and GAN), I realized NeRF shares a fundamental idea: continuous latent representations. While VAEs explicitly enforce structured latent distributions and GANs rely on adversarial learning, NeRF takes a more straightforward approach by embedding spatial coordinates directly into neural networks. However, it still captures continuous structures that allow interpolation, something VAE explicitly constructs and GAN achieves implicitly.</p>

<hr />

<h3 id="summary--final-thoughts">Summary &amp; Final Thoughts</h3>
<p>NeRF shows how neural networks can represent entire scenes using only a few images and positional encodings. By intentionally overfitting and employing hierarchical sampling, it achieves photorealistic results without explicit geometric models.</p>

<p>Simple design choices can change the approach and performance of neural models in tasks like 3D view synthesis. These choices help explain why NeRF has become a common reference in neural rendering research.</p>
