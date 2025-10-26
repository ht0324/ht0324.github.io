# Vibe Coding
_Published: 2025-03-30_
_Tags: AI_
_Categories: Blog_
_Original: https://ht0324.github.io/blog/2025/vibe-coding/_

<p><em>Note: The following post is written based on a presentation I gave at SKKAI on March 29, 2025.</em></p>

<h3 id="what-is-vibe-coding">What is “Vibe Coding”?</h3>

<p>The term “Vibe Coding” recently caught some buzz, sparked by a <a href="https://x.com/karpathy/status/1886192184808149383">tweet by Andrej Karpathy</a> back in February 2025. He described it as a new way of coding where you “fully give in to the vibes, embrace exponentials, and forget that the code even exists.” This involves using powerful LLMs within tools like <a href="https://www.cursor.com/">Cursor</a>, often interacting through voice commands and barely touching the keyboard.</p>

<p>Karpathy explained the process: making simple requests, accepting code changes without much review (“Accept All”), and feeding error messages back to the LLM, which usually fixes them. He mentioned the code can grow beyond easy comprehension, and bugs might get worked around rather than deeply debugged. It’s less traditional coding and more directing, running, and assembling, letting the LLM handle the nitty-gritty implementation.</p>

<p>Since Karpathy is a co-founder of OpenAI and former head of Tesla’s Autopilot vision, this idea is worth paying attention to, especially as the term gains traction in tech circles. The main idea is humans set high-level goals, and the LLM does the detailed work. The workflow shifts to observing, directing, and integrating the AI’s output, often without needing deep code understanding yourself.</p>

<h3 id="from-intelligence-to-agency-making-vibe-coding-possible">From Intelligence to Agency: Making Vibe Coding Possible</h3>

<p>A key question is: Is this Vibe Coding thing actually feasible? Based on recent progress, the answer is increasingly yes, though with some catches. This wasn’t really practical just a few months ago. The big change? The rise of LLM <em>Agency</em>.</p>

<p>To get what Vibe Coding is about, it helps to see the difference between LLM Intelligence and LLM Agency. Intelligence is about knowledge, reasoning, and understanding, areas where LLMs are improving fast. As I wrote before, trying out benchmarks like MMLU shows that modern LLMs can already have superhuman knowledge in certain areas. But, this intelligence often stays inside a ‘box,’ like a chat window, limited in how it interacts with the outside world.</p>

<p>Agency, however, is about taking action, having initiative, and controlling things in an environment. It’s the LLM’s power to <em>do</em> tasks and make decisions that affect the real or digital world, going beyond just talking. This is where standard LLM use often stops. For LLMs to really help with complex tasks like coding, they need the agency to act for us.</p>

<h3 id="building-agentic-llms-better-models-and-tools">Building Agentic LLMs: Better Models and Tools</h3>

<p>Developing this agency is key for Vibe Coding. It means LLMs need to use tools, change files, run code, and interact with systems, not just generate text. This ability to <em>execute</em> tasks based on instructions is the foundation. So, boosting agency by combining reasoning with action has become a major focus in LLM development.</p>

<p>How do we give LLMs more agency? There seem to be two main routes. First, build smarter models designed for agency. This means training them on data showing agentic behavior, using methods like Reinforcement Learning (RL), and designing models focused on task execution, not just language. We’re also seeing evaluation shift, with benchmarks like SWE-bench testing practical coding ability, which needs real agency. Anthropic showing <a href="https://www.anthropic.com/news/claude-3-7-sonnet">Claude 3.7 Sonnet</a> <a href="https://www.anthropic.com/news/visible-extended-thinking">playing Pokémon</a> effectively highlights this focus on action and decision-making.</p>

<p>The second route is giving LLMs effective Tools and ways to interact with the world. An LLM’s smarts are useless if it can’t act. Tools are the bridges connecting the LLM to APIs, databases, file systems, web searches, etc. This needs interfaces allowing the model to reliably get info, run code, and change its environment—turning ‘thinking’ into ‘doing’.</p>

<h3 id="standardizing-interaction-the-model-context-protocol-mcp">Standardizing Interaction: The Model Context Protocol (MCP)</h3>

<p>Integrating tools used to be a headache. Developers had to manually specify exactly how an LLM should use each API or system, a messy, non-standard process.</p>

<p>To fix this, the <a href="https://www.anthropic.com/news/model-context-protocol">Model Context Protocol (MCP)</a> was introduced. First proposed by Anthropic and now also adopted by OpenAI, MCP is an open standard aiming to simplify how AI models connect with external tools and data. Think of it as a “USB-C for AI applications.”</p>

<p>MCP works by creating a standard communication layer. Model providers (like OpenAI, Anthropic) make their LLMs MCP-compatible. Tool providers (like GitHub, Slack, or even custom local tools) make their tools speak the MCP language. This lets models use any MCP tool via a single interface, and tools become usable by any compatible model easily. The flow is typically: LLM decides tool needed -&gt; sends MCP request -&gt; tool executes -&gt; returns MCP result -&gt; LLM proceeds. This helps build a stable, consistent ecosystem of AI tools.</p>

<p>It’s no accident that the places where Vibe Coding is starting to happen, like the <a href="https://www.cursor.com/">Cursor</a> editor or the <a href="https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview">Claude Code</a> interface, are heavily using MCP. These tools give LLMs the agency they need by providing controlled access to crucial tools (file system, terminal, web search) through MCP. The formula seems to be: [Smart Model + Effective Tools (via MCP)] = Agentic Capability → Vibe Coding.</p>

<h3 id="limitations-and-the-road-ahead">Limitations and The Road Ahead</h3>

<p>Of course, Vibe Coding isn’t perfect right now.</p>

<ul>
  <li><strong>Supervision Needed:</strong> You still need to watch closely. LLMs can make mistakes or get stuck.</li>
  <li><strong>Scalability:</strong> It works better for smaller projects. Complexity can become an issue.</li>
  <li><strong>Understanding:</strong> Relying only on the LLM can mean you don’t understand your own codebase well (black box risk).</li>
  <li><strong>Maturity:</strong> The tech is new and not ready for everything, especially critical systems.</li>
  <li><strong>Debugging:</strong> Fixing bugs in code you didn’t write and barely understand is hard.</li>
</ul>

<p>But, it’s important to remember this is likely just the beginning. The tech is improving fast. LLM reasoning and agency are getting better, and standards like MCP are making tool integration easier. While “Vibe Coding” might feel experimental now, the core trend—LLMs becoming capable agents that can handle complex tasks—is real and picking up speed. It’s definitely a space worth watching.</p>
