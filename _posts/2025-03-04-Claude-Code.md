---
layout: post
title: Claude Code
date: 2025-03-04 10:59:59
description: My experience with Claude Code for rapid prototyping, debugging, and implications of AI agency
tags: AI 
categories: blog thoughts
giscus_comments: true
---

Today, I used [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview), an experimental tool released by Anthropic a while ago. I really wanted to use it right at the start of the announcement, but I kept putting it off because I hadn’t found a use case for it yet. But today, I had to rapidly prototype an app, so I decided to give it a shot.

---
<br />
**Claude's Agentic Capabilities**

Claude Code is basically Claude 3.7 Sonnet, which has been updated by Anthropic to have more agentic capabilities. They’ve essentially wrapped it with tools that can run commands and execute terminal operations. Claude can see your repository, view your file directory, edit files, and execute terminal commands. So, yeah, it has much more agency.

I needed to quickly prototype an app that hosts images, allows filtering by tags, and enables image similarity search. And lo and behold, after just 2-3 hours, I had a functioning prototype.

I haven’t used Cursor AI, the VS Code variant that gained traction some time ago and was widely praised by people in the Bay Area. But maybe now I’m experiencing the epiphany that Cursor users had. The experience wasn’t just about typing in my query and having Claude do everything from start to finish - it felt more like pair programming.

It gave me the sense that there was a person behind the terminal, troubleshooting issues and debugging with me. Of course, Claude wasn’t perfect, but the back-and-forth, iterative process was refreshing and much more engaging than just randomly encountering errors and sifting through Stack Overflow links to fix them.

<br />
**A New Kind of Collaboration**

It was a massive time-saver. I provided high-level directions, Claude executed them, and when problems arose, we solved them together. The biggest revelation was how collaborative the process felt - it was much easier and more efficient than doing everything on my own. If I had done this single-handedly, it would have taken days. But for just $3.50 in API costs (which might seem expensive depending on your threshold), I built a prototype that I’m pretty confident in within 2–3 hours.

Claude Code also helped me fix bugs on my self-hosted blog. I’m more of an AI guy, not a web guy, so managing my blog often involved trial and error - throwing things at the wall and seeing what stuck. I had to manually fix bugs and do all sorts of tweaks to get it to look the way I wanted. But with Claude Code, I could simply query my repository - it became conversational. That made it much easier to fix persistent issues in a short amount of time. All in all, it’s an incredibly useful tool.

But the reason why it felt like a collaborative process is that Claude still isn’t perfect in its agentic execution. Don’t get me wrong - Claude is very capable, but it still requires human intervention. For complex tasks, it doesn’t always get things right on the first try. If we ever reach a point where AI no longer needs intervention - where it can figure out even highly complex instructions entirely on its own - then it would no longer feel like collaboration; it would be full automation.

That said, I structured my app development process in a very step-by-step manner, executing tasks sequentially. Maybe that’s why I didn’t run into any major setbacks. If I had given more abstract instructions, I might have been more surprised by what Claude could do. But the key point remains: it still feels like a collaboration because Claude makes mistakes.

Looking at the trajectory of AI progress, though, I don’t think this collaborative phase will last long. Eventually, it won’t be a partnership - it will be a replacement.

---
<br />

I’ve recently seen posts on [X](https://x.com/David_Kasten/status/1893357776702976286) of anecdotes that from recruiters at DeepMind and OpenAI who now assume that junior staffs are AI replaceable. I was initially skeptical of this claim, but now I believe it. Also, in Andrej Karpathy’s [post](https://x.com/karpathy/status/1894099637218545984), he argues that agency is more valuable than intelligence. This struck me as profound.

In terms of intelligence, today’s top LLMs are already more knowledgeable than humans. But in terms of agency, humans still have the upper hand. However, after my interaction with Claude Code, I caught a glimpse of a future where machines will reach agency supremacy as well. When that happens, it won’t be collaboration - it will be full replacement. And that’s what worries me.