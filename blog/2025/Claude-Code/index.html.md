# Claude Code
_Published: 2025-03-04_
_Tags: AI_
_Categories: Blog, Thoughts_
_Original: https://ht0324.github.io/blog/2025/Claude-Code/_

<p>Today, I used <a href="https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview">Claude Code</a>, an experimental tool released by Anthropic a while ago. I really wanted to use it right at the start of the announcement, but I kept putting it off because I hadn’t found a use case for it yet. But today, I had to rapidly prototype an app, so I decided to give it a shot.</p>

<hr />
<h3 id="claudes-agentic-capabilities">Claude’s Agentic Capabilities</h3>

<p>Claude Code is basically <a href="https://www.anthropic.com/news/claude-3-7-sonnet">Claude 3.7 Sonnet</a>, which has been updated by Anthropic to have more agentic capabilities. They’ve essentially wrapped it with tools that can run commands and execute terminal operations. Claude can see your repository, view your file directory, edit files, and execute terminal commands. So it has more agency.</p>

<p>I needed to quickly prototype an app that hosts images, allows filtering by tags, and enables image similarity search. After just 2-3 hours, I had a functioning prototype.</p>

<p>I haven’t used <a href="https://www.cursor.com/">Cursor</a>, the VS Code variant that gained traction some time ago and was widely praised by people in the Bay Area. But maybe now I’m experiencing the epiphany that Cursor users had. The experience was about more than typing in my query and having Claude do everything from start to finish; it felt more like pair programming.</p>

<p>It gave me the sense that there was a person behind the terminal, troubleshooting issues and debugging with me. Of course, Claude wasn’t perfect, but the back-and-forth, iterative process was refreshing and much more engaging than just randomly encountering errors and sifting through Stack Overflow links to fix them.</p>

<hr />
<h3 id="a-new-kind-of-collaboration">A New Kind of Collaboration(?)</h3>

<p>It was a time-saver. I provided high-level directions, Claude executed them, and when problems arose, we solved them together. The biggest surprise was how collaborative the process felt. It was much easier and more efficient than doing everything on my own, or switching back and forth using a chat interface.</p>

<p>If I had done this single-handedly, it would have taken days. But for just $3.50 in API costs (which might seem expensive depending on your threshold), I built a prototype that I’m pretty confident in within 2–3 hours.</p>

<p>Claude Code also helped me fix bugs on my self-hosted blog. I’m more of an AI guy, not a web guy, so managing my blog often involved trial and error, throwing things at the wall and seeing what stuck. I had to manually fix bugs and do all sorts of tweaks to get it to look the way I wanted.</p>

<p>But with Claude Code, I could query my repository, and it became conversational. That made it much easier to fix persistent issues in a short amount of time. All in all, it’s a useful tool.</p>

<hr />
<h3 id="collaboration-as-a-mirage">Collaboration as a Mirage</h3>

<p>But the reason why it felt like a collaborative process is that Claude still isn’t perfect in its agentic execution. Don’t get me wrong: Claude is capable, but it still requires human intervention. For complex tasks, it doesn’t always get things right on the first try.</p>

<p>If we ever reach a point where AI no longer needs intervention, where it can figure out even highly complex instructions entirely on its own, then it would no longer feel like collaboration; it would be full automation.</p>

<p>That said, I structured my app development process in a very step-by-step manner, executing tasks sequentially. Maybe that’s why I didn’t run into any major setbacks. If I had given more abstract instructions, I might have been more surprised by what Claude could do. But the key point remains: it still feels like a collaboration because Claude makes mistakes, and I had to intervene to correct them.</p>

<p>Looking at the trajectory of AI progress, though, I don’t think this collaborative phase will last long. Eventually, it won’t be a partnership; it will be a replacement.</p>

<hr />
<h3 id="the-inevitable-shift">The Inevitable Shift</h3>

<p>I’ve recently seen posts on <a href="https://x.com/David_Kasten/status/1893357776702976286">X</a> of anecdotes that from recruiters at frontier labs who now assume that junior staffs are AI replaceable. I was initially skeptical of this claim, but now I kinda believe it. Also, in Andrej Karpathy’s <a href="https://x.com/karpathy/status/1894099637218545984">post</a>, he argues that agency is more valuable than intelligence. This struck me as profound.</p>

<p>In terms of intelligence, today’s top LLMs are already more knowledgeable than humans. But in terms of agency, humans still have the upper hand. However, after my interaction with Claude Code, I caught a glimpse of a future where machines will reach agency supremacy as well. When that happens, it won’t be collaboration; it will be a full <a href="https://www.youtube.com/watch?v=7Pq-S557XQU">Humans Need Not Apply</a>(outdated, but still relevant).</p>

<p>I encourage everyone reading this to try it for themselves. Hearing about it isn’t the same as experiencing it firsthand. Maybe I’m exaggerating, but I stand by my belief that this kind of automation is a matter of when, not if. And this is the worst this technology will ever be, it’s only going to get better from here.</p>
