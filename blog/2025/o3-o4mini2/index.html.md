# Agency Over Retrieval?
_Published: 2025-04-18_
_Tags: AI_
_Categories: Blog_
_Original: https://ht0324.github.io/blog/2025/o3-o4mini2/_

<p>I’ve been thinking more about OpenAI’s o3 and o4 mini models since my <a href="/blog/2025/o3-o4mini-product-path/">last post</a>, and using them led to some additional insights. Specifically, I looked into the <a href="https://x.com/elder_plinius/status/1912567149991776417">system prompt for o3/o4 mini</a> and noticed something interesting: it strongly encourages the model to surf the web whenever a query is even slightly vague or uncertain. Essentially, web search is almost the default behavior.</p>

<p>Initially, I was puzzled by this choice. Why prompt a <em>reasoning and agentic</em> model to search the web so readily? These aren’t primarily web search models like Perplexity AI. Why not rely more on their internal knowledge and reasoning first?</p>

<p>But as I thought deeper about it, everything kind of clicked.</p>

<h3 id="beyond-simple-hallucination-mitigation">Beyond Simple Hallucination Mitigation</h3>

<p>Of course, one part of the answer relates to model hallucination. Getting large language models to be consistently reliable and avoid making things up is still a hard problem. While improvements in data and algorithms have reduced blatant hallucination, ensuring reliability over 99% of the time requires grounding. Accessing relevant, up-to-date information is important for that.</p>

<p>However, I don’t think that’s the full story here. I think OpenAI is doing something more fundamental by leveraging the <em>agentic</em> capabilities of these models.</p>

<h3 id="letting-the-model-choose-its-context">Letting the Model Choose Its Context</h3>

<p>Think about traditional approaches like Retrieval-Augmented Generation (RAG). In those systems, a separate retrieval mechanism analyzes the user’s query, finds potentially relevant source documents, and then stuffs that information into the language model’s context window. The retrieval system decides what the main LLM sees.</p>

<p>What OpenAI seems to be doing with o3/o4 mini is different. They are offloading the task of finding relevant information <em>to the main model itself</em>. Instead of an external system <em>pushing</em> context, the agentic model is encouraged to <em>pull</em> the context it decides it needs by actively searching the web.</p>

<p>Let me break it down with an analogy. Imagine you need to solve a complex problem.</p>
<ul>
  <li><strong>Option A (RAG-like):</strong> Someone else (a separate system) looks at your problem, finds some books or articles they think are relevant, and hands them to you. You then try to solve the problem using only those materials.</li>
  <li><strong>Option B (o3/o4 mini-like):</strong> You look at the problem, and <em>you</em> decide to proactively search your bookshelf, scour the internet, gather information, and based on what you find, iteratively search for more information until <em>you</em> feel you have what you need.</li>
</ul>

<p>Option B gives you autonomy. You actively choose what information you consume. This feels like a more effective way to tackle complex or nuanced problems.</p>

<p>The key difference is agency. The RAG system (Option A) isn’t necessarily as smart or capable as the main LLM it’s feeding context to. Why let a potentially less sophisticated system pre-filter the information? Why not let the powerful base model decide what information is most relevant or needed for its own reasoning process?</p>

<p>This principle of giving the model agency to select its own relevant context seems to be more general than just text retrieval via web search. It applies across modalities. Look at OpenAI’s recent post on <a href="https://openai.com/index/thinking-with-images/">“Thinking with Images”</a>. They demonstrate how o3/o4 mini can use tools to manipulate images during their chain of thought. For instance, if text in an image is upside down or hard to read, the model can use tools to zoom in or rotate that specific part of the image to better understand it. If an image is complex, it can zoom into the most relevant section. This is effectively visual information retrieval, driven by the model’s ability to choose which visual information to focus on using tools, mirroring how it uses web search to retrieve textual information.</p>

<p>Traditional RAG can sometimes feel like it just dumps context verbatim into the window, regardless of whether the model deems it insightful or sufficient. Giving the model the agency to search, whether the web for text or pixels within an image, means it can dynamically gather precisely what it needs, when it needs it. It’s a recursive, almost meta-cognitive approach: the model decides how to inform itself.</p>

<h3 id="consolidation-and-the-bitter-lesson-again">Consolidation and the Bitter Lesson Again?</h3>

<p>This feels like another step in the consolidation trend we’ve seen in AI. Previously, NLP was fragmented into many specific tasks (sentiment analysis, named entity recognition, etc.). With the rise of powerful transformers, many of these specialized tasks converged into the capabilities of large, general models.</p>

<p>Now, agency might be enabling further consolidation. Tasks like information retrieval (textual or visual) and hallucination mitigation, previously handled by separate scaffolding or techniques like RAG, might increasingly become integrated into the model’s core agentic reasoning loop. As models become more general and capable agents, they can take on more of these sub-tasks themselves.</p>

<p>In a way, it feels like the <a href="https://www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf">Bitter Lesson</a> playing out once more. Instead of relying heavily on human-designed scaffolding and rule-based systems (like fixed retrieval strategies), perhaps it’s more effective to give the scaled-up model the agency and tools (like web search or image manipulation) and let it learn the best methods for gathering and utilizing information to solve the task at hand. Don’t inhibit the model with rigid external structures; let its capabilities grow.</p>

<p>It’s a simple shift: prompting the model to search when unsure, or allowing it to manipulate input images, but the underlying principle of empowering the model’s own agency to manage its information needs feels like an important one.</p>
