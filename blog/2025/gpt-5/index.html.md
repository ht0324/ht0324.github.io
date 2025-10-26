# My Take on GPT-5
_Published: 2025-08-18_
_Tags: AI_
_Categories: Thoughts_
_Original: https://ht0324.github.io/blog/2025/gpt-5/_

<p>OpenAI recently released GPT-5, with claims of a new state-of-the-art model that tops benchmarks. After spending some time with it, my initial impression is that while it’s a decent model, it doesn’t feel groundbreaking. However, I’ve come to realize that this release wasn’t really intended for power users like me. For the majority of people, this model is a game-changer.</p>

<h3 id="the-divide-between-power-users-and-everyday-users">The Divide Between Power Users and Everyday Users</h3>

<p>Before GPT-5, I used OpenAI’s o3 model almost exclusively since March. As I’ve discussed in a <a href="/blog/2025/o3-o4mini2/">previous post</a>, I have high regard for o3, mainly because of its “agentic” nature. It could actively surf the web to gather context and provide more reliable answers. This ability to use tools like web search and retrieve context on its own, in my opinion, separates a useful AI from a toy.</p>

<p>This is why it sometimes frustrates me to see friends and colleagues, even those with a ChatGPT Plus subscription, stick to the basic GPT-4o model. They often complain that it hallucinates or makes things up, and when I ask which model they’re using, most of the time it’s the 4o model. A model without a dedicated reasoning process and tool usage is going to be less reliable for complex tasks. I’ve made it a personal rule to never trust a non-reasoning model for anything beyond simple tasks like drafting an email or editing my writing.</p>

<p>The value of a “thinking” model comes from test-time compute scaling. When you allow a model to “think harder” about a problem, the quality of the result is much better than what a non-reasoning model can produce. With GPT-5, this capability is now dynamically available to everyone.</p>

<h3 id="the-router-a-cornerstone-for-a-new-business-model">The Router: A Cornerstone for a New Business Model</h3>

<p>The most significant change with GPT-5 isn’t the base model itself, but the introduction of the <strong>router</strong>. This system dynamically decides whether a query requires the deeper “GPT-5 Thinking” model or can be handled by a simpler one.</p>

<p>A recent <a href="https://semianalysis.com/2025/08/13/gpt-5-ad-monetization-and-the-superapp/">article</a> from SemiAnalysis by Dylan Patel and his team really opened my eyes to the business implications of this. They argue that the router is the cornerstone for OpenAI to finally monetize its massive base of free users. The router can distinguish between a trivial query like, “What is the capital of France?” and a commercially valuable one like, “What are the best running shoes I can buy?”</p>

<p>The first query doesn’t require deep reasoning and is cheap to answer. The second, however, has high commercial intent. The router can allocate more resources to it, use web search, and provide a detailed, reasoned recommendation. This creates an opportunity for OpenAI to take a transaction fee or affiliate revenue, turning the chatbot into a monetizable super-app. It’s a way to monetize without resorting to intrusive ads, which Sam Altman has expressed a distaste for.</p>

<p>While I agree that the router enables this, I’d push back slightly and argue that a sufficiently advanced model could theoretically make these decisions on its own. Still, implementing it as a dedicated router is a clear and deliberate step toward this new paradigm.</p>

<h3 id="final-thoughts">Final Thoughts</h3>

<p>My experience with GPT-5 has solidified a key belief: always use a thinking model. Since its release, I’ve used “GPT-5 Thinking” exclusively, and I don’t care about the automatic routing for my own use.</p>

<p>If you’re reading this, the main takeaway I want to leave you with is this: whenever you have the choice, opt for the model that thinks. The difference in quality and reliability is night and day. For the average user, GPT-5’s greatest gift is making that choice for them, seamlessly bringing the power of reasoning to hundreds of millions of users for the first time.</p>
