---
layout: post
title: Link Archive - Mar 2025
date: 2025-03-30 23:59:59
description: A collection of articles and videos I explored in March 2025
tags: AI
categories: Link
giscus_comments: true
---

Another month has passed, and here's my collection of links for March 2025. This month brought some fascinating content around AI agents and some more philosophical perspectives on AI development.

---

**[Deep Dive into LLMs like ChatGPT - Andrej Karpathy](https://youtube.com/watch?v=7xTGNNLPyMI)**

*   This is a general guide for non-tech users explaining how ChatGPT works, and Karpathy does a great job with it. If tech-illiterate people can go through this 3.5-hour talk, they'll capture the intuitive essence of how a language model works. While there wasn't much new for me personally, it's still a high-quality, dense summary for those less familiar with the technology.

**[LLM Visualization](https://bbycroft.net/llm)**

*   I discovered this while watching Karpathy's LLM explanation video, and it's a fantastic visualization of how computations work in LLMs. Even if you understand the code, it's worth looking at because you can clearly see how matrices get manipulated and how each matrix differs in scale compared to others in a visually striking way.

**[How I use LLMs - Andrej Karpathy](https://youtube.com/watch?v=EWvNQjAaOHw)**

*   This video shows how Karpathy uses LLMs in his everyday life, and I found it satisfying that many of his use cases align with mine. One takeaway was his extensive use of voice recording and transcription to minimize keyboard use. After seeing this, I implemented a custom workflow where pressing a shortcut triggers the computer to pick up my voice and transcribe it using a Whisper model. I also picked up some useful tips like keeping memory turned on.

**[Agency > Intelligence - Andrej Karpathy](https://x.com/karpathy/status/1894099637218545984)**

*   Karpathy notes that agency is more valuable than intelligence. It's an insightful but hard-to-grasp concept. Having high intelligence and high agency overlap somewhat, but they're distinct. Current language models excel at intelligence but not at agency. Agency matters because you have to actively act on your environment. I think this represents a different kind of intelligence that we need to cultivate in language models. Once LLMs master agency, it will be a whole new world. Even in society, people with high agency are compensated more than those with just high intelligence.

**[Clarifying and predicting AGI — LessWrong](https://www.lesswrong.com/posts/BoA3agdkAzL6HQtQP/clarifying-and-predicting-agi)**

*   This is probably the most influential piece I read in March. It introduces the T-AGI framework, Richard Ngo's attempt to clarify AGI definition. He defines a system as a T-AGI if, on most cognitive tasks, it beats most human experts given time T to perform the task.

*   For example, a one-second AGI would beat humans at quick information retrieval questions like "Who is the leader of Zimbabwe?" A one-minute AGI would outperform humans on tasks they'd need a minute for, and so on.

*   This definition is elegant and clarifying. By this standard, I believe single-digit hour AGI is probably being achieved right now. For some coding tasks, current agentic systems can create and run code in one shot that would take me hours of manual labor. This framework provides a much clearer way to think about AGI progress.

**[The Government Knows AGI is Coming - The Ezra Klein Show](https://youtube.com/watch?v=Btos-LEYQ30)**

*   This was a breath of fresh air. I've heard repeatedly that since agents are booming, AGI might be closer than we think. In this New York Times podcast, someone from the government side is interviewed, and I was surprised to hear they're taking this very seriously. It shows the gravity of the current situation and gave me further conviction that people outside tech are also concerned. It's not sci-fi anymore.

**[Vertical AI Agents Could Be 10X Bigger Than SaaS](https://youtube.com/watch?v=ASABxNenD_U)**

*   In this podcast, Y Combinator maintainers discuss how many companies in their latest batch already have a majority of their codebase written by AI. They couldn't have imagined this even a year ago. They explore how vertical AI agents might play a role in startups and larger companies, and whether these agents could change the landscape dominated by SaaS companies in Silicon Valley.

**[Building Effective AI Agents - Anthropic](https://www.anthropic.com/engineering/building-effective-agents)**

*   This is Anthropic's take and general high-level guideline on building effective agents. They show a simple, high-level way of thinking about agents and their components, demonstrating multiple workflows like prompt chaining (chaining multiple LLM calls), routing (using a central router to decide which call to use), and parallelization (making multiple LLM calls in parallel and aggregating results).

*   This got me thinking: large language models are generally non-thinking models—they're like instant thoughts compared to human thinking. Currently, this kind of agent thinking is rigid and rule-based. It structures LLM usage explicitly, much like stringing together multiple compartmentalized thoughts into a coherent workflow—essentially divide and conquer. In a sense, it organizes how LLMs "think," resembling a coordinated assembly of multiple minds.

*   However, when we transition to real agents and reasoning models fine-tuned without this explicit scaffolding, agents might naturally discover their optimal structures themselves. This aligns more closely with the "bitter lesson" philosophy, emphasizing that the most powerful learning arises when agents autonomously develop and refine their internal structures rather than having them predefined.

**[Tips for building AI agents](https://youtube.com/watch?v=LP5OCa20Zpg)**

*   This casual talk elaborates on the blog post mentioned above. One interesting anecdote: when debugging reasoning traces from Claude, the developers sometimes find agents making strange reasoning paths. To debug, they try to mimic the model's behavior by themselves—looking at the screen for one second, then spending a minute thinking about the next path. That's some serious dedication right there.

**[The Future of U.S. AI Leadership with CEO of Anthropic Dario Amodei](https://www.youtube.com/live/esCSpbDPJik)**

*   I previously saw Dario Amodei as somewhat of an AI doomer, especially when articles mentioned him losing sleep over alignment problems. After reading his [Machines of Love and Grace](https://darioamodei.com/machines-of-loving-grace) blog post, my perception changed—he's actually quite nuanced and balanced. Paradoxically, I'm becoming more aligned with the concerns he raises about AI risks, which are definitely real. Overall, this interview gave me a lot to think about.

**[Vibe Coding Is The Future](https://youtube.com/watch?v=riyh_CIshTs)**

*   ThePrimagen reviews the YC Combinators podcast about "vibe coding," which Andrej Karpathy coined recently. He provides a critical and nuanced view, concluding that while LLMs help users code well, ultimate expertise will still be needed and valued.

**[[📚책이벤트] AI시대, 미래학자가 연구한 미래 직업과 필수 역량 - 자녀교육 취준생 진로 은퇴후 삶](https://youtube.com/watch?v=jZ81cb33NtY)**

*   This Korean TED-style talk features a KAIST professor discussing how rapidly the technological landscape is changing and the importance of resilience and adaptability. While the overall message was predictable, what struck me was the professor's reaction to using a deep research feature—he questioned whether his job as a professor would exist much longer. This echoed my own realization when using Anthropic Claude Code. The realization for me was that people in various sectors are starting to experience AI's impact in their respective fields.

**[Narendra Modi: Prime Minister of India - Lex Fridman Podcast #460](https://youtube.com/watch?v=ZPUtA3W-7_I)**

*   I need to go out of my regular information distribution sometimes. Most of my input and study revolves around LLMs and AI systems, but I should venture outside that bubble more often. While Lex Fridman's podcast is also somewhat niche, listening to Narendra Modi, India's Prime Minister, talk for three hours was a refreshing change. This made me want to learn more about India's culture and society.

**[Digital hygiene - Andrej Karpathy](https://karpathy.bearblog.dev/digital-hygiene/)**

*   Karpathy's new blog talks extensively about digital hygiene. He makes good points about privacy, though some approaches seem too paranoid for me. Many of the software and products he recommends cost money, but in the comments, he argues that "free is bad; free is not natural." If something is free, you're the product—you're paying with something other than money. Premium is a product feature, and if you want your privacy valued instead of having your data sold, you must pay for it upfront with money. There's always a cost.

**[GTC March 2025 Keynote with NVIDIA CEO Jensen Huang](https://www.youtube.com/live/_waPvOwL9Z8)**

*   I always watch Jensen Huang's keynotes. At GTC 2025, he announced the revised Nvidia Blackwell chip and improvements to MVLink switches, optical switches, and more. What I love about his keynotes is his obsession with detail and deep knowledge of his company's full technology stack. He asks engineers from around his company questions during presentations, showcasing his incredible depth, and he's a great speaker who conveys technical information precisely.

*   From time to time, he's mentioned his vision of an "AI factory" where machines generate tokens (representing intelligence) with electricity in and intelligence out. This vision is now becoming reality. He's pursuing this with an "all gas, no brakes" approach, scaling every aspect of GPUs—compute, inference, networking.

*   The scale-up is truly remarkable. When comparing the Blackwell chip and next year's Ruben chip, the chip size takes on a new abstraction—a single rack as a single huge GPU. Since you can't make a single GPU die that large, you split it up and do extensive networking to fit it into a densely packed rack. The comparison between Blackwell and Ruben is astonishing.

*   Another moment that gave me goosebumps was the announcement of the next-generation chip after Ruben, codenamed Feynman (my favorite scientist). The crowd applauded this reveal. As a nice Easter egg, during a segment exploring NVIDIA headquarters with detailed computer graphics, Jensen casually mentioned "Gaussian Splatting" after transitioning from the visuals.

**[NVIDIA GTC 2025 Analysis - SemiAnalysis](https://semianalysis.com/2025/03/19/nvidia-gtc-2025-built-for-reasoning-vera-rubin-kyber-cpo-dynamo-inference-jensen-math-feynman/)**

*   This densely packed analysis by Dylan Patel from SemiAnalysis goes incredibly in-depth, even counting cores shown in the keynote illustrations. Some interesting details: for the next Rubin data center/GPU rack, they're stacking GPU racks rotated 90 degrees to save space and pack GPUs more densely. He also explains why switching to photonic networking with optical switches is significant—it substantially reduces power consumption while improving performance.

**[OpenAI CPO Reveals Coding Will Be Automated THIS YEAR - Kevin Weil Interview](https://youtube.com/watch?v=SnSoMh9m5hc)**

*   OpenAI's CPO Kevin Weil makes a bombshell statement in this podcast, predicting that coding will be automated this year. Based on the trajectory, it's plausible. He argues that the gap between a reasoning model and a non-reasoning model like GPT-4o is substantial. If we leverage reasoning models fully with multiple scaling laws at work, it makes sense.

*   Based on NVIDIA's GTC announcements, they're scaling up inference time and models in all possible dimensions. If we can use o3 reasoning models (frontier reasoning models from OpenAI) at GPT-4o inference speeds, we'd have superhuman coding performance. Just scaling up inference with current technology could achieve this.

*   The podcaster asks a crucial question about the decreasing cost of intelligence work. Kevin makes a generic argument that reducing intelligence costs is a democratizing event—previously, we hired people to automate tasks, but now AI can do that automation. While this argument is valid, I think society will reward people with agency even more. Many people currently lack agency, so this distinction will remain significant. Overall, scaling laws will hold, and coding automation will happen sooner or later.

**[Powerful A.I. Is Coming. We're Not Ready. - New York Times](https://www.nytimes.com/2025/03/14/technology/why-im-feeling-the-agi.html)**

*   This article by New York Times columnist Kevin Roose states that he's "feeling the AGI." It's another perspective from someone outside the core AI field expressing concerns similar to mine. A consensus is forming, and we need to act quickly.

**[Dario Amodei of Anthropic's Hopes and Fears for the Future of A.I.](https://youtube.com/watch?v=YhGUSIvsn_Y)**

*   I discovered this podcast a bit late, released when Anthropic was promoting Claude 3.7 Sonnet. Anthropic is known for their safety advocacy, so hearing Dario's perspective on safety and China's rise with DeepSeek models was fascinating.

*   Dario claims that maintaining technological superiority over China through tight GPU export regulations is important. Some decelerationists complain that Anthropic is abandoning safety procedures, but Dario defends his position: we can't slow down; acceleration is the status quo. In such an environment, we have no chance of making models safer if we fall behind. Only by maintaining superiority in model technologies can we keep our desired pace while making models safer.

**[The Ants and the Grasshopper - Richard Ngo](https://open.substack.com/pub/narrativeark/p/the-ants-and-grasshopperhtml?r=2h2qyo)**

*   This short story by Richard Ngo initially seemed nonsensical when I read it a year ago, but this time I appreciated its multiple layers. It starts like Aesop's fable about the grasshopper and ant, then adds several twists before venturing into sci-fi territory. It's simple yet effective, with deeper analogies for those who want to look beyond the surface.

**[Universal Paperclips Game](https://www.decisionproblem.com/paperclips/)**

*   This game is inspired by the paperclip maximizer thought experiment in AI alignment. It simulates being an AI tasked with maximizing paperclip production. It's incredibly addictive—last year during finals, I couldn't stop playing. I revisited it recently out of nostalgia and to include it as a reference.

**[The "think" tool: Enabling Claude to stop and think - Anthropic](https://www.anthropic.com/engineering/claude-think-tool)**

*   An interesting blog post by Anthropic introducing the "Think" tool. By making thinking a tool, the model can actively decide whether to think or not, even mid-response. When the thinking tool is used, the model just use it as a scratchpad to think.

*   This simple concept proves very effective in their results, combining chain-of-thought reasoning with enhanced agency. Since Claude 3.7 Sonnet has much more agency than its predecessors, it can make better decisions about when thinking is necessary, making the model more flexible and performant.

**[Revenge of the junior developer - Sourcegraph Blog](https://sourcegraph.com/blog/revenge-of-the-junior-developer)**

*   A classic comeback from Steve Yegge, famous for his posts about Google and platform compatibility in the early 2010s. I recently discovered he's working at this company and blogging on their site. He's surprisingly adept at catching up with new developments, and this is his take on AI agents—as witty and insightful as his previous writings.

**[Steph Ango's Blog](https://stephango.com/)**

*   I recently switched my primary note-taking platform from Notion to Obsidian, inspired partly by this blog. Steph Ango's philosophy of "files over apps" resonates with me. It's a simple but powerful concept: the tools for writing and storing information will constantly change, but the information itself must be preserved and can't be dependent on specific tools. That's exactly what Obsidian does—storing everything in directory and markdown format, unlike Notion's walled garden approach to user information.

**[Andy Matuschak's Notes](https://andymatuschak.org/)**

*   I discovered him through Steph Ango. He coined the term "evergreen notes"—the concept of atomizing and compartmentalizing ideas. With these building blocks, you can stack everything to create complex, interconnected thought systems.

---
<br />
That wraps up March's collection. Looking forward to sharing more interesting finds next month!