# ViT - Review
_Published: 2025-01-23_
_Tags: AI_
_Categories: Paper_
_Original: https://ht0324.github.io/blog/2025/Vit/_

<p>This time, I review the paper <a href="https://arxiv.org/abs/2010.11929">“An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale”</a>, commonly known as ViT (Vision Transformer). My initial impression was that the idea behind ViT is simple: take a standard Transformer (originally designed for NLP) and apply it to images by splitting them into patches. Despite the simplicity, the results are strong, especially when scaled with large datasets.</p>

<hr />

<h3 id="key-concepts">Key Concepts</h3>

<p><strong>Transformer on Images (Patches as Tokens)</strong><br />
ViT treats images exactly like text: an image is divided into small patches, each patch flattened into a vector, and these vectors become tokens fed into the Transformer model. Each patch is analogous to a “word” in NLP, which is intuitive and effective.</p>

<p><strong>Linear Embedding of Patches</strong><br />
Each image patch is flattened and projected linearly into a fixed-dimensional vector (embedding). Unlike CNNs, which explicitly encode spatial locality, ViT relies on these embeddings and positional encoding to implicitly learn spatial relationships.</p>

<p><strong>Learnable Classification Token</strong><br />
An additional learnable <strong>“CLS”</strong> token is prepended to the patch embeddings. This special token aggregates global information through the Transformer’s layers and serves as the final representation for classification, inspired by the approach from BERT.</p>

<p><strong>Position Embeddings</strong><br />
ViT uses standard learnable 1D positional embeddings. These embeddings help the model recognize positions, although they’re less spatially intuitive than explicit 2D positional encodings. They work, and the authors saw no significant advantage in switching to more complex 2D embeddings.</p>

<p><strong>Hybrid Models (Optional)</strong><br />
They also briefly experimented with a hybrid approach where CNN feature maps replace raw patches. It’s worth noting but ultimately secondary; the pure Transformer approach already performs well without CNN pre-processing, suggesting CNN’s inductive biases might not be strictly necessary for strong performance when data scale is sufficient.</p>

<hr />

<h3 id="key-takeaways-what-i-learned">Key Takeaways (What I Learned)</h3>

<p><strong>Surprisingly Simple Yet Effective</strong><br />
The biggest surprise for me was how straightforward this approach is. It feels almost trivial: patch up an image, pass it through a Transformer, and let self-attention handle the rest. There aren’t complicated tweaks specific to images, yet it achieves solid performance. The simplicity makes the model generalizable and scalable.</p>

<p><strong>Less Inductive Bias, More Flexibility</strong><br />
ViT intentionally lacks many inductive biases built into CNNs, like locality, translational invariance, and hierarchical features. This initially felt like a disadvantage. But instead, it allows ViT to learn entirely from scratch, potentially finding more generalizable patterns. CNNs bake in assumptions about images; ViT does not. This made me reconsider how inductive biases might restrict model capacity, especially when enough data is available.</p>

<p><strong>Why Positional Embeddings Can Be Problematic</strong><br />
One point I found confusing at first was positional embeddings. If the input resolution changes (for example, when fine-tuning on higher resolution images), positional embeddings trained for smaller sequences can lose their meaning. Because patches correspond to positions in a fixed grid, changing resolution changes their relative indices. The paper solves this by simply interpolating positional embeddings. However, I still wonder if using relative positional coordinates normalized within [0,1] in 2D would have been better. That could preserve relative positions across resolutions better than interpolating discrete embeddings.</p>

<p><strong>Hybrid Approach (CNN + Transformer)</strong><br />
The authors briefly mentioned a hybrid approach—extracting patches from CNN feature maps instead of raw pixels. This was interesting because it mixes the inductive bias of CNNs with the global context modeling of Transformers. But the paper showed no strong advantage in this method compared to a pure Transformer. This suggests that minimal architecture-specific inductive biases can be beneficial if you have large-scale data. I initially thought a hybrid model might be superior, but apparently, the simplicity of pure ViT is good enough.</p>

<p><strong>Changing Trends in Transformer Norm Placement</strong><br />
I also noticed ViT applies LayerNorm before each block, unlike earlier Transformer implementations (e.g., original Vaswani et al.). This subtle trend, now common in later models like GPT-3, seemed older than I realized, dating back at least to this 2021 paper. It made me rethink when exactly this architectural pattern became standard practice.</p>

<hr />

<h3 id="summary--final-thoughts">Summary &amp; Final Thoughts</h3>
<p>ViT successfully adapts Transformers directly to images by treating image patches as tokens. The approach feels almost too straightforward, yet it works well, especially given sufficient data. The minimal inductive bias is both a limitation and an advantage—it forces the model to learn spatial structure entirely from scratch but allows greater flexibility in generalizing patterns.</p>

<p>The paper reinforced my belief that simplicity, when applied thoughtfully, often beats complicated hand-crafted architectures. ViT isn’t doing something fundamentally complex, just taking a proven model and changing its input modality. Still, it offers a clear and insightful shift in how we approach image processing. It shows we can sometimes trust the Transformer’s power without overcomplicating things, and that’s worth keeping in mind.</p>
