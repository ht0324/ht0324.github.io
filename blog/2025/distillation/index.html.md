# Knowledge Distillation - Review
_Published: 2025-04-22_
_Tags: AI_
_Categories: Paper_
_Original: https://ht0324.github.io/blog/2025/distillation/_

<p>I’ve known about the concept of knowledge distillation for a while – the core idea is simple: soft labels (the full probability distribution from a model) contain richer information about class relationships than hard labels alone. I first encountered it in a lecture by Geoffrey Hinton (<a href="https://www.youtube.com/watch?v=rGgGOccMEiY">like this one discussing paths to intelligence</a>) and decided to read the original 2015 paper, “<a href="https://arxiv.org/abs/1503.02531">Distilling the Knowledge in a Neural Network</a>,” co-authored with Oriol Vinyals and Jeff Dean. It’s short, but with clear insight.</p>

<h3 id="the-insect-analogy-training-vs-deployment">The Insect Analogy: Training vs. Deployment</h3>

<p>What struck me immediately was the opening analogy:</p>

<blockquote>
  <p>“Many insects have a larval form that is optimized for extracting energy and nutrients from the environment and a completely different adult form that is optimized for the very different requirements of traveling and reproduction.”</p>
</blockquote>

<p>I haven’t seen many ML papers start with a biological analogy like this. I hadn’t thought about insect life stages this way before. The larva is about consumption and growth, slow-moving, maybe not complex, but efficient at extracting resources (like a large training model absorbing information from data). The adult form is optimized for different tasks, lightweight, fast, mobile, focused on specific functions like reproduction (like an efficient deployment model needing low latency and computational cost).</p>

<p>The analogy fits perfectly with the challenge in machine learning:</p>
<ul>
  <li><strong>Training:</strong> We often use huge, “cumbersome” models (or ensembles) that take lots of computation and time but are great at extracting every bit of signal from large datasets.</li>
  <li><strong>Deployment:</strong> We need models that are fast, efficient, and have low latency for real-world use.</li>
</ul>

<p>Distillation, then, is like the <strong>metamorphosis</strong>: transforming the knowledge captured by the cumbersome larva/training model into the efficient adult/deployment model.</p>

<h3 id="knowledge-beyond-weights">Knowledge Beyond Weights</h3>

<p>The paper points out a potential “conceptual block”:</p>

<blockquote>
  <p>“…we tend to identify the knowledge in a trained model with the learned parameter values.”</p>
</blockquote>

<p>This makes it hard to think about transferring knowledge without just copying weights. Prior work like Rich Caruana’s model compression focused on matching the outputs <em>before</em> the final softmax (the logits). Hinton et al.’s approach refines this by using the <em>probabilities</em> from the softmax, arguing that this captures the learned distribution more meaningfully.</p>

<h3 id="the-value-of-wrong-answers">The Value of “Wrong” Answers</h3>

<p>A key insight is how the large, cumbersome model generalizes. It’s not just about getting the right answer.</p>

<blockquote>
  <p>“…a side-effect of the learning is that the trained model assigns probabilities to all of the incorrect answers… The relative probabilities of incorrect answers tell us a lot about how the cumbersome model tends to generalize.”</p>
</blockquote>

<p>The example they give is clear: an image of a BMW might have a tiny probability of being mistaken for a garbage truck, but that probability, however small, is likely higher than it being mistaken for a carrot. This network of similarities and differences between classes is knowledge learned by the teacher model. Hard labels (just “BMW”) throw this information away. Soft labels (the full probability distribution) preserve it.</p>

<p>This aligns with the objective: we don’t just want models to perform well on training data, we want them to <em>generalize</em> well to new data. Soft targets directly transfer the <em>generalization behavior</em> of the teacher model to the student.</p>

<h3 id="the-mechanism-temperature-scaling">The Mechanism: Temperature Scaling</h3>

<p>So how do we use these soft labels? If the teacher model is very confident (assigns probability ~1.0 to the correct class), the probabilities for incorrect classes are tiny. Even if their <em>ratios</em> contain information, they have almost no impact on the cross-entropy loss during student training.</p>

<p>The solution is to “raise the temperature” <code class="language-plaintext highlighter-rouge">T</code> of the softmax function:</p>

<p><code class="language-plaintext highlighter-rouge">q_i = exp(z_i / T) / Σ_j exp(z_j / T)</code></p>

<p>where <code class="language-plaintext highlighter-rouge">z_i</code> are the logits. Normally <code class="language-plaintext highlighter-rouge">T=1</code>. Using a higher <code class="language-plaintext highlighter-rouge">T &gt; 1</code> “softens” the probability distribution, increasing the probabilities of incorrect classes and allowing them to contribute more to the loss function. The student model is trained to match this softened distribution, using the same high temperature <code class="language-plaintext highlighter-rouge">T</code>. (After training, the student uses <code class="language-plaintext highlighter-rouge">T=1</code> for inference).</p>

<p>This temperature scaling is the core mechanism. The paper notes that in the high-temperature limit, this method becomes equivalent to matching the logits (Caruana’s approach), but at intermediate temperatures, it focuses more on matching the more probable incorrect classes, potentially ignoring noise from very negative logits.</p>

<h3 id="training-the-student">Training the Student</h3>

<p>The best results often come from combining two objectives:</p>
<ol>
  <li>Matching the soft targets from the teacher (using cross-entropy with high temperature <code class="language-plaintext highlighter-rouge">T</code>).</li>
  <li>Matching the true hard labels (using cross-entropy with <code class="language-plaintext highlighter-rouge">T=1</code>).</li>
</ol>

<p>They found a weighted average works well, often with a lower weight on the hard target loss. As they say: “Typically, the small model cannot exactly match the soft targets and erring in the direction of the correct answer turns out to be helpful.”</p>

<h3 id="proof-of-generalization-the-mnist-experiment">Proof of Generalization: The MNIST Experiment</h3>

<p>A clear experiment highlights the value of this approach. They trained a student model on MNIST, but <em>omitted all examples of the digit ‘3’</em> from the transfer set. From the student’s perspective, ‘3’ was a “mythical digit” it had never directly seen.</p>

<p>Despite this, the distilled model performed well on classifying ‘3’s at test time (with a bias adjustment). It had learned about ‘3’ indirectly, through the soft targets for other digits, for example, by learning which ‘8’s looked a bit like a ‘3’ according to the teacher model. This is evidence that soft targets transfer generalization capabilities, not just labels.</p>

<h3 id="final-thoughts">Final Thoughts</h3>

<p>This paper is a classic example of clear insight. The claim is simple, but such a powerful one:</p>

<blockquote>
  <p>“…a lot of helpful information can be carried in soft targets that could not possibly be encoded with a single hard target.”</p>
</blockquote>
