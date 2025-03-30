---
layout: post
title: Vibe Coding
date: 2025-03-30 11:00:00
description: Blog version of my presentation
tags: AI
categories: Blog
giscus_comments: true
---

*Note: The following post is written based on a presentation I gave at SKKAI on March 29, 2025.*

### What is "Vibe Coding"?

The term "Vibe Coding" recently caught some buzz, sparked by a [tweet by Andrej Karpathy](https://x.com/karpathy/status/1886192184808149383) back in February 2025. He described it as a new way of coding where you "fully give in to the vibes, embrace exponentials, and forget that the code even exists." This involves using powerful LLMs within tools like [Cursor](https://www.cursor.com/), often interacting through voice commands and barely touching the keyboard.

Karpathy explained the process: making simple requests, accepting code changes without much review ("Accept All"), and just feeding error messages back to the LLM, which usually fixes them. He mentioned the code can grow beyond easy comprehension, and bugs might get worked around rather than deeply debugged. It's less traditional coding and more directing, running, and assembling – letting the LLM handle the nitty-gritty implementation.

Since Karpathy is a co-founder of OpenAI and former head of Tesla's Autopilot vision, this idea is worth paying attention to, especially as the term gains traction in tech circles. The main idea is humans set high-level goals, and the LLM does the detailed work. The workflow shifts to observing, directing, and integrating the AI's output, often without needing deep code understanding yourself.

### From Intelligence to Agency: Making Vibe Coding Possible

A key question is: Is this Vibe Coding thing actually feasible? Based on recent progress, the answer is increasingly yes, though with some catches. This wasn't really practical just a few months ago. The big change? The rise of LLM *Agency*.

To get what Vibe Coding is about, it helps to see the difference between LLM Intelligence and LLM Agency. Intelligence is about knowledge, reasoning, and understanding – areas where LLMs are improving incredibly fast. As I wrote before, trying out benchmarks like MMLU shows that modern LLMs can already have superhuman knowledge in certain areas. But, this intelligence often stays inside a 'box,' like a chat window, limited in how it interacts with the outside world.

Agency, however, is about taking action, having initiative, and controlling things in an environment. It's the LLM's power to *do* tasks and make decisions that affect the real or digital world, going beyond just talking. This is where standard LLM use often stops. For LLMs to really help with complex tasks like coding, they need the agency to act for us.

### Building Agentic LLMs: Better Models and Tools

Developing this agency is key for Vibe Coding. It means LLMs need to use tools, change files, run code, and interact with systems—not just generate text. This ability to *execute* tasks based on instructions is the foundation. So, boosting agency by combining reasoning with action has become a major focus in LLM development.

How do we give LLMs more agency? There seem to be two main routes. First, build smarter models designed for agency. This means training them on data showing agentic behavior, using methods like Reinforcement Learning (RL), and designing models focused on task execution, not just language. We're also seeing evaluation shift, with benchmarks like SWE-bench testing practical coding ability, which needs real agency. Anthropic showing [Claude 3.7 Sonnet](https://www.anthropic.com/news/claude-3-7-sonnet) [playing Pokémon](https://www.anthropic.com/news/visible-extended-thinking) effectively highlights this focus on action and decision-making.

The second route is giving LLMs effective Tools and ways to interact with the world. An LLM's smarts are useless if it can't act. Tools are the bridges connecting the LLM to APIs, databases, file systems, web searches, etc. This needs interfaces allowing the model to reliably get info, run code, and change its environment—turning 'thinking' into 'doing'.

### Standardizing Interaction: The Model Context Protocol (MCP)

Integrating tools used to be a headache. Developers had to manually specify exactly how an LLM should use each API or system—a messy, non-standard process.

To fix this, the [Model Context Protocol (MCP)](https://www.anthropic.com/news/model-context-protocol) was introduced. First proposed by Anthropic and now also adopted by OpenAI, MCP is an open standard aiming to simplify how AI models connect with external tools and data. Think of it as a "USB-C for AI applications."

MCP works by creating a standard communication layer. Model providers (like OpenAI, Anthropic) make their LLMs MCP-compatible. Tool providers (like GitHub, Slack, or even custom local tools) make their tools speak the MCP language. This lets models use any MCP tool via a single interface, and tools become usable by any compatible model easily. The flow is typically: LLM decides tool needed -> sends MCP request -> tool executes -> returns MCP result -> LLM proceeds. This helps build a stable, consistent ecosystem of AI tools.

It's no accident that the places where Vibe Coding is starting to happen—like the [Cursor](https://www.cursor.com/) editor or the [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) interface—are heavily using MCP. These tools give LLMs the agency they need by providing controlled access to crucial tools (file system, terminal, web search) through MCP. The formula seems to be: [Smart Model + Effective Tools (via MCP)] = Agentic Capability → Vibe Coding.

### Limitations and The Road Ahead

Of course, Vibe Coding isn't perfect right now.

*   **Supervision Needed:** You still need to watch closely. LLMs can make mistakes or get stuck.
*   **Scalability:** It works better for smaller projects. Complexity can become an issue.
*   **Understanding:** Relying only on the LLM can mean you don't understand your own codebase well (black box risk).
*   **Maturity:** The tech is new and not ready for everything, especially critical systems.
*   **Debugging:** Fixing bugs in code you didn't write and barely understand is hard.

But, it's important to remember this is likely just the beginning. The tech is improving fast. LLM reasoning and agency are getting better, and standards like MCP are making tool integration easier. While "Vibe Coding" might feel experimental now, the core trend—LLMs becoming capable agents that can handle complex tasks—is real and picking up speed. It's definitely a space worth watching.