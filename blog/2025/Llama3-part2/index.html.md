# Llama 3 Paper - Review (Part 2)
_Published: 2025-03-25_
_Tags: AI_
_Categories: Paper_
_Original: https://ht0324.github.io/blog/2025/Llama3-part2/_

<p>This is part 2 of my review of Meta’s Llama 3 technical paper. In <a href="/blog/2025/Llama3-part1">part 1</a>, I covered the core language model architecture, training methodology, and overall performance. Now I’ll dive into the multimodal aspects of the model (vision, video, and speech), which represent significant additions to the Llama ecosystem.</p>

<p>What strikes me about Meta’s approach is their consistent focus on compositionality. Instead of training entirely new models from scratch, they extend the existing Llama 3 language models with specialized adapters. This pragmatic approach allows them to add new capabilities while preserving the existing text understanding abilities.</p>

<hr />

<h3 id="key-concepts">Key Concepts</h3>

<p><strong>Compositional Multimodal Architecture</strong><br />
Meta adopts a modular, compositional approach for all multimodal capabilities in Llama 3. Rather than training joint models from scratch, they combine pre-trained language models with modality-specific encoders connected through adapter layers. This architecture has several advantages: it enables parallel development of language and vision/audio capabilities, avoids the complexities of joint training on multiple modalities, preserves text-only performance, and reduces computational overhead during inference by processing input modalities efficiently.</p>

<p><strong>Vision Encoder and Adapter</strong><br />
The vision module consists of a pre-trained ViT-H/14 image encoder (modified to include 850M parameters) combined with cross-attention layers that connect the visual representations to the language model. These cross-attention layers are substantial, adding about 100B parameters to the 405B model. To preserve fine-grained visual information, they extract features from multiple intermediate layers of the vision encoder rather than just using the final layer output, which helps with tasks requiring detailed localization.</p>

<p><strong>Video Recognition Architecture</strong><br />
The video module builds on the image module by adding two key components: a “temporal aggregator” that merges frames to capture temporal relationships, and dedicated video cross-attention layers. The aggregator uses a perceiver resampler architecture to compress multiple frames into a more compact representation. During pre-training, they start with 16 frames (aggregated to 1) and scale up to 64 frames during fine-tuning to handle longer videos more effectively.</p>

<p><strong>Speech Understanding Approach</strong><br />
Unlike the vision module, the speech component doesn’t use cross-attention layers. Instead, it generates embeddings that directly integrate with text tokens in the language model. The speech module consists of a 1B-parameter Conformer encoder followed by a smaller adapter. This direct integration approach allows the speech interface to leverage the language model’s existing capabilities without modifying its parameters, which works well at larger scales.</p>

<p><strong>Speech Generation</strong><br />
For text-to-speech capabilities, Meta takes a different approach. Rather than fine-tuning the language model for speech generation, they implement a streaming text-to-speech system that uses Llama 3 embeddings to enhance text normalization and prosody modeling. The embeddings from Llama 3 are used to improve context-aware text normalization and more natural-sounding prosody.</p>

<p><strong>Scaling and Training Challenges</strong><br />
Training these multimodal adapters introduces unique challenges beyond those faced when training the core language model. The model computation becomes heterogeneous (some tokens require more processing than others), data shows high variance in token counts across modalities, and there are numerical instability issues from combining different types of representations. Meta addresses these through pipeline design, sequence parallelization, and using higher precision for gradient accumulation.</p>

<hr />

<h3 id="key-takeaways-what-i-learned">Key Takeaways (What I Learned)</h3>

<p><strong>Compositional Design Makes Technical Sense</strong><br />
Initially, I had concerns about the compositional approach. I wondered if mapping the higher-dimensional image modality into the latent space of a language model might cause significant information loss. While the dimensionality itself is an implementation detail, I believe the inherent modality of text fundamentally contains less information than images. However, when I saw GPT-4o generating accurate images from text prompts and handling complex visual tasks, it became clear that language model latent spaces are robust at encoding visual concepts. This suggests the limitation I was worried about may not be as severe in practice. The cross-attention mechanism with multi-layer feature extraction appears to be effective at preserving the detailed information from higher-dimensional modalities.</p>

<p><strong>Multi-layer Feature Extraction Preserves Fine-grained Information</strong><br />
One insight I found particularly interesting was how they addressed the problem of CLIP-like models failing to preserve fine-grained localization information. Instead of relying solely on the final layer output, they extract features from multiple intermediate layers of the vision encoder (specifically the 4th, 8th, 16th, 24th, and 31st layers). This approach makes sense because the lower layers retain more spatial and detailed information before it gets abstracted away in higher layers. I hadn’t previously considered this limitation of contrastive learning approaches, but it explains why models like CLIP might struggle with tasks requiring precise visual details or localization.</p>

<p><strong>Handling Many-shot Jailbreaking in Long Context Models</strong><br />
Something that caught my attention was the vulnerability of long-context models to many-shot jailbreaking attacks. The longer context window enables a new attack vector: they mentioned specifically that 256-shot attacks become possible. They mitigated this by fine-tuning models on datasets that include examples of safe behavior even when unsafe behavior appears in context. The fact that they could achieve this without impacting false refusal rates or helpfulness metrics shows the model’s ability to distinguish between demonstrations in context and actual instructions.</p>

<p><strong>Safety Becomes Increasingly Granular</strong><br />
What struck me about Meta’s safety approach is how granular it’s becoming. Rather than having a generic “harmful content” classifier, they’re developing increasingly specialized safety mechanisms for specific types of risks. This categorization of safety concerns (into areas like cybersecurity, coding, spear-phishing, etc.) reveals how the frontier of AI safety is evolving from broad mitigation to very specific risk assessment and targeted interventions. It also suggests that as models get more capable, the attack vectors multiply, requiring more complex safety strategies.</p>

<p><strong>Contextual Safety Challenges</strong><br />
The paper mentions that 256-shot attacks become possible with longer context windows. It shows that extending a model’s capabilities (like context length) can introduce new safety vulnerabilities that weren’t relevant before. This suggests a kind of “safety debt” that comes with each capability enhancement: each new ability potentially opens up novel attack vectors that need additional mitigations.</p>

<hr />

<h3 id="summary--final-thoughts">Summary &amp; Final Thoughts</h3>

<p>Meta’s approach to expanding Llama 3’s capabilities into multimodal territory shows a thoughtful balance between pragmatism and innovation. Rather than developing entirely new architectures or joint pre-training approaches, they extend the existing language model through specialized adapters and compositional design. This strategy allows them to leverage the strengths of existing pre-trained components while adding new capabilities incrementally.</p>

<p>The paper also highlights the ongoing tension between capability enhancement and safety. As models gain new abilities (like longer context), new vulnerabilities emerge that require additional mitigations. This suggests that safety work isn’t a one-time effort but an ongoing process that must evolve alongside model capabilities.</p>

<p>As these models continue to develop, I’m particularly interested in seeing how the compositional approach scales to even more modalities and how it affects overall model capabilities. Does adding more modalities lead to emergent abilities through cross-modal transfer? Do certain modalities complement each other in unexpected ways? The Llama 3 paper doesn’t directly address these questions, but it provides a solid foundation for exploring them in future work.</p>
