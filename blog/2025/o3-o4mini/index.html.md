# Thoughts on o3, o4 mini
_Published: 2025-04-17_
_Tags: AI_
_Categories: Blog_
_Original: https://ht0324.github.io/blog/2025/o3-o4mini/_

<p>So, here are my recent thoughts on the release of OpenAI’s <a href="https://openai.com/index/introducing-o3-and-o4-mini/">o3 and o4 mini</a>. In conclusion, it’s a bit of a mixed bag. It’s easy to get caught up in the hype, and there are notable things present. While generally, I think the release and the resulting models are strong, there are subtle nuances that need to be addressed.</p>

<p>For a quick recap for those who haven’t caught up: OpenAI released <strong>o3</strong> and <strong>o4 mini</strong>, new variants of their reasoning models specifically trained to use tools and be agentic. When you see the demos and people’s use cases, it really is fantastic. It has more of a “person feel.” I’ve used it myself, and compared to previous models that primarily did research by fetching and analyzing web info, o3 and o4 mini feel much more agentic. Unlike previous models which ca use function calling but rather in a separate isolated manner, they seem to actively parse information, act based on it, and use various tools such as command‑line interface. In that sense, they are really capable models.</p>

<h3 id="context-and-comparison">Context and Comparison</h3>

<p>But for me, after the initial impression settled, it felt like OpenAI basically released their version of Anthropic’s <a href="https://www.anthropic.com/news/claude-3-7-sonnet">Claude 3.7 Sonnet</a>, which is good at agentic tasks. Because of its agentic capabilities, 3.7 Sonnet became a go‑to enterprise solution, especially for agent‑coding IDEs. While OpenAI’s new models arrived two or three months later and are arguably better, the fundamental paradigm hasn’t drastically changed.</p>

<p>Another thing I really noted was within the ChatGPT interface itself. When serving o3, OpenAI enabled function calling and tool use <em>by default</em>. This means the models can readily use capabilities like data analysis, the coding environment, web search, and others that OpenAI has integrated into ChatGPT. All this combined gives the models a vast array of tools they didn’t have access to so easily before, and it does have a combinatorial effect on model capabilities.</p>

<p>Previously, if I wanted to research a topic while studying, I’d usually paste my content into the chat and query the model. Now, since the model can search the web itself, and it feels less like simple RAG and more like it’s actually fitting the fetched info into its context, I don’t have to provide as much relevant context manually. It feels more reliable in that sense, reducing the need for me to spoon‑feed context. I think the capability of the chat interface itself has changed.</p>

<h3 id="openai-as-a-product-company">OpenAI as a Product Company</h3>

<p>This led me to another thought: the overall trajectory of OpenAI as a company.</p>

<p>When I saw how OpenAI neatly packaged their models and tools onto a platter and served it within the chat interface, it clicked for me: as Sam Altman had <a href="https://www.youtube.com/live/5MWT_doo68k?t=653">said</a>, OpenAI is now officially a product company, though in hindsight, given where their revenue comes from, they always were.</p>

<p><a href="https://medium.com/@furqankhaan/how-openai-and-anthropic-are-cashing-in-on-ai-a-look-at-their-revenue-models-d9d9ae79dd28">If you compare their revenues to Anthropic’s</a>, OpenAI is the market leader, partly due to the network effect of being the first mover. But most of OpenAI’s revenue comes from user subscriptions with a smaller fraction from API usage. Anthropic is the polar opposite, most revenue comes from API usage, though even their API revenue lags behind OpenAI’s API revenue. This suggests subscriptions are more popular than API access, at least for OpenAI.</p>

<p>Then it makes sense for OpenAI to prioritize products because intelligence is becoming cheap, almost too cheap to meter. Model API costs are racing to the bottom, leaving very few margins, especially with competitors like Google, Anthropic, xAI, and others. Subscription is a godsend for cheap cash.</p>

<p>So, what do I mean by OpenAI acting as a product company? As I mentioned, o3/o4 mini feel like a better version of Claude 3.7 Sonnet. There’s a qualitative jump, I’m not denying that, but there’s also an effective way OpenAI executed the <em>delivery</em>.</p>

<p>You see, when Claude 3.7 Sonnet launched, Anthropic just launched an enterprise solution, not a product. And make no mistake, Claude is a capable, agentic model, written more about <a href="/blog/2025/Claude-Code/">here</a>. They also released the Model Context Protocol <a href="https://www.anthropic.com/news/model-context-protocol">(MCP)</a>, which I’ve also <a href="/blog/2025/vibe-coding/">written about and presented on</a>. <strong>However, when it came to their consumer-facing product, Anthropic essentially just slapped this smart model into a basic chat interface <em>without</em> providing the tools necessary to showcase its agentic power.</strong> The end user interacting with Claude AI wouldn’t even realize how smart and agentic the underlying model is.</p>

<p>Looking back, especially after seeing OpenAI’s o3/o4 mini launch, I can see how Anthropic could have stolen OpenAI’s thunder. If they had built the necessary scaffolding and provided adequate tools for Claude to use directly within the chat interface, allowing it to surf the web and execute code agentically, the user experience would have been different. Claude <em>can</em> do these things via MCP, but the defalut interface doesn’t allow it. This forces users like me to manually scaffold MCP and handcraft custom environments just to tap into the model’s full potential, which is far from an ideal experience. With o3, OpenAI made it frictionless; it just works.</p>

<h3 id="mcp-and-financial-realities">MCP and Financial Realities</h3>

<p>In that sense, I was surprised when OpenAI <a href="https://x.com/sama/status/1904957253456941061">announced</a> they would also support MCP on their models. Initially, I was skeptical they’d adopt it as a standard. First, Anthropic developed it. Second, it seemed counter to OpenAI’s strategy. As you can see, they were prepping o3/o4 mini as a <em>product</em>. They serve it via API too, but that doesn’t feel like their main priority. Their strategy seems to be building their own scaffolding and tool integration into the model and selling it as a product. MCP, being an open standard, directly counteracts that by leveraging the open‑source community.</p>

<p>However, I think this kind of standardization is inevitable, so OpenAI likely just followed suit. For MCP proliferation, the open‑weights/source community and Anthropic seem like the main benefactors, not OpenAI. But personally, I think this outcome—broader adoption of open standards—is desirable, even if it wasn’t OpenAI’s first preference.</p>

<p>I believe that to achieve financial independence, OpenAI will aggressively work towards building itself as a product company. I understand the criticisms about OpenAI deviating from its non‑profit roots. But as I’ve <a href="/blog/2025/OpenAI-for-profit/">covered before</a>, the reality seems simple: they need money. They need financial independence to do what they set out to do. Because of scaling laws and everything else, capital is necessary to scale up compute and continue research. I think they feel they have no choice but to pursue this path. I know Sam Altman can sound manipulative, but I think it might be true in a sense that they didn’t fully anticipate this financial necessity early on, and now they feel forced into this position.</p>

<h3 id="the-walled-garden-strategy">The Walled Garden Strategy</h3>

<p>Given this path towards being a product company, OpenAI’s recent moves start to make more sense. Take their <a href="https://x.com/OpenAI/status/1910378768172212636">enhanced memory feature</a>, for example. This is a play for user retention, a step towards building a walled garden. They want users integrated into <em>their</em> ecosystem.</p>

<p>Looking ahead, imagine if OpenAI develops a truly frontier, genius-level model. What if they <em>only</em> offer it through their ChatGPT interface, not the API? Since subscriptions are the real cash cow compared to the low-margin API race, this seems plausible, especially if AGI-level capabilities emerge. A <a href="https://darioamodei.com/machines-of-loving-grace">country of geniuses in a datacenter</a>, only accessible via chatgpt.com. They could make a lot of money this way.</p>

<p>Combine that potential model superiority with features like memory that build up personalized context over time, and the friction for users to switch to a competitor becomes immense. Your interaction history, your personalized AI – it all stays within OpenAI’s walls. Essentially, the memory capability becomes a strategic tool. It makes the platform stickier and much harder to leave. In a way, OpenAI is making our accumulated data a reason to stay, almost holding it hostage to deter us from jumping ship to competitors. Food for thought as these platforms evolve.</p>

<h3 id="conclusion">Conclusion</h3>

<p>So, in conclusion, yes, o3 are qualitatively good models. But I think these kinds of performance improvements were somewhat expected given the trajectory of previous models and the industry. What I think is non‑trivial, and what not enough people seem to be paying attention to, is <em>how</em> OpenAI implemented this. The product integration, the default tool usage in the chat interface, and what this signals about their shift towards being a product‑first company: that’s the bigger story here.</p>

<p>Moreover, although OpenAI’s revenue mix already revealed its product focus, this release cements it. ChatGPT’s first‑mover advantage has generated a network effect: the more users it attracts, the more feedback and data it gathers, which funds better models, which in turn attract even more users. It’s the classic aggregator flywheel. Even though Google currently dazzles with pure‑model wins like Gemini 2.5 Pro, and Anthropic keeps pushing Claude 3.7 Sonnet, neither has managed to match the friction‑free, fully‑integrated product OpenAI now offers. Unless OpenAI makes a catastrophic misstep, I believe that flywheel will accelerate.</p>
