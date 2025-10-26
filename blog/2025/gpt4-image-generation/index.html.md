# Thoughts on GPT-4o Image Generation
_Published: 2025-03-26_
_Tags: AI_
_Categories: Thoughts_
_Original: https://ht0324.github.io/blog/2025/gpt4-image-generation/_

<p>Today, OpenAI revealed GPT-4o’s <a href="https://openai.com/index/introducing-4o-image-generation/">image generation capabilities</a>. While this feature was previewed in the initial 4o announcement about <a href="https://openai.com/index/hello-gpt-4o/">a year ago</a>, the actual results are still surprising. Playing with it triggered some realizations about the future implications of direct image generation that I want to share here.</p>

<hr />

<h3 id="the-multimodal-approach">The Multimodal Approach</h3>

<p>The concept isn’t new. When OpenAI introduced GPT-4o, they described it as modeling input as text, pixels, and sounds, combining all modalities with one big autoregressive transformer. The output would likewise be text, images, and audio.</p>

<p>They presented it as straightforward, though there are complicated architectural decisions behind the scenes. But the impact is clear: the model is much more capable at image generation.</p>

<p>In previous systems (diffusion models or other chatbot interfaces), images were generated through a two-step process. The language model would generate a sophisticated prompt and feed that into a separate image model. GPT-4o eliminates this by directly generating images.</p>

<p>Since the large language model directly generates images, it’s more capable in this context. We can also feed in images, and the results speak for themselves. The images show more consistency. When previous chatbots wanted to modify an image, they had to create a detailed description of that image and feed it into another diffusion model. This was a bottlenecked process, but with 4o, it can handle images directly, modifying them with more consistency.</p>

<p>What’s notable is how refined the model’s text generation capabilities are within images. Previous diffusion models struggled with generating clean, readable text in images; it was often distorted, nonsensical, or limited to a few words. GPT-4o can generate clean text, and lots of it. The text is consistently readable and contextually appropriate.</p>

<hr />

<h3 id="spark-of-software-20">Spark of Software 2.0</h3>

<p>My most visceral moment came from an example where they showed a cat image being iteratively transformed into a game interface. Through multiple iterations, they turned it into an image of a game with a UI, and the text was accurate. The model produced an image with a clean interface, and everything was consistent.</p>

<p>That’s when it hit me: if the model can generate UI and text so accurately, in the future our computer interfaces could be entirely AI-generated in real-time with all the context available from the user. Large language models could generate your computer interface frame by frame based on your input and feedback.</p>

<p>Imagine a user interface that changes based on user needs. Our current operating systems (macOS, Linux, Windows) are rule-based with fixed definitions. But what if a large language model generated a new UI that helped the user get things done? It would be adaptive and different for every user, changing styles and functionality based on preferences or context.</p>

<p>What would a word processor look like in that interface? The possibilities seem endless. Currently, an OS has the lower-level kernel with renderers and shaders that produce pixels. But this would be an end-to-end network - a large language model OS directly generating pixels from our input.</p>

<p>The concept of world simulators isn’t new: NVIDIA is already using their <a href="https://blogs.nvidia.com/blog/what-is-robotics-simulation/">Isaac Sim platform</a> to <a href="https://blogs.nvidia.com/blog/openusd-sdg-advance-robot-learning/">generate synthetic data for training robot models</a>, Google DeepMind has developed <a href="https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/">Genie 2</a> that can generate interactive 3D environments, and Microsoft Research recently unveiled <a href="https://www.microsoft.com/en-us/research/blog/introducing-muse-our-first-generative-ai-model-designed-for-gameplay-ideation/">Muse</a>, their first generative AI model designed for gameplay ideation. But what if instead of simulating physical worlds, we used these capabilities to simulate an operating system? That’s where my realization really hit me.</p>

<p>One of the most compelling aspects of this approach would be how it leverages context. Context is incredibly important for large language models. Your previous conversations, actions, and preferences inform their responses. Current operating systems gather tons of contextual information about how we use them, but this data isn’t being utilized well. What if an OS could learn and adapt from your previous interactions, inputs, preferences, and habits while you used it? Every aspect of your computing experience could be customized not by explicit settings, but by the system understanding you over time.</p>

<p>This is basically <a href="https://karpathy.medium.com/software-2-0-a64152b37c35">Software 2.0</a> and <a href="https://x.com/karpathy/status/1723140519554105733">LLM OS</a> that Andrej Karpathy described. I was aware of this idea before, but I hadn’t felt it would be feasible in such a short time. With some effort, this kind of OS might be technically possible now with large-scale servers and APIs, but it would be largely impractical. Yet the implications are large, and I believe this kind of OS is inevitable.</p>

<p>Of course, it wouldn’t be a fully end-to-end neural network. There would be some rule-based systems guiding the LLMs. But my point still stands: we might be seeing the first glimpse of a new OS approach.</p>

<p>Karpathy mainly discussed Software 2.0 replacing rule-based software stacks, which is already happening. But I think Software 2.0 will also eventually replace the OS stack itself.</p>
