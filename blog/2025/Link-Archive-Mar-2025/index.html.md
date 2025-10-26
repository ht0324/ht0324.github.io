# Link Archive - Mar 2025
_Published: 2025-03-30_
_Tags: AI_
_Categories: Link_
_Original: https://ht0324.github.io/blog/2025/Link-Archive-Mar-2025/_

<p>Another month has passed, and here’s my collection of links for March 2025. This month brought some interesting content around AI agents and some more philosophical perspectives on AI development.</p>

<hr />

<p><strong><a href="https://youtube.com/watch?v=7xTGNNLPyMI">Deep Dive into LLMs like ChatGPT - Andrej Karpathy</a></strong></p>

<ul>
  <li>This is a general guide for non-tech users explaining how ChatGPT works, and Karpathy does a great job with it. If tech-illiterate people can go through this 3.5-hour talk, they’ll capture the intuitive essence of how a language model works. While there wasn’t much new for me personally, it’s still a high-quality, dense summary for those less familiar with the technology.</li>
</ul>

<p><strong><a href="https://bbycroft.net/llm">LLM Visualization</a></strong></p>

<ul>
  <li>I discovered this while watching Karpathy’s LLM explanation video, and it’s a useful visualization of how computations work in LLMs. Even if you understand the code, it’s worth looking at because you can clearly see how matrices get manipulated and how each matrix differs in scale compared to others in a clear visual way.</li>
</ul>

<p><strong><a href="https://youtube.com/watch?v=EWvNQjAaOHw">How I use LLMs - Andrej Karpathy</a></strong></p>

<ul>
  <li>This video shows how Karpathy uses LLMs in his everyday life, and I found it satisfying that many of his use cases align with mine. One takeaway was his extensive use of voice recording and transcription to minimize keyboard use. After seeing this, I implemented a custom workflow where pressing a shortcut triggers the computer to pick up my voice and transcribe it using a Whisper model. I also picked up some useful tips like keeping memory turned on.</li>
</ul>

<p><strong><a href="https://x.com/karpathy/status/1894099637218545984">Agency &gt; Intelligence - Andrej Karpathy</a></strong></p>

<ul>
  <li>Karpathy notes that agency is more valuable than intelligence. It’s an insightful but hard-to-grasp concept. Having high intelligence and high agency overlap somewhat, but they’re distinct. Current language models excel at intelligence but not at agency. Agency matters because you have to actively act on your environment. I think this represents a different kind of intelligence that we need to cultivate in language models. Once LLMs master agency, it will be a major shift. Even in society, people with high agency are compensated more than those with just high intelligence.</li>
</ul>

<p><strong><a href="https://www.lesswrong.com/posts/BoA3agdkAzL6HQtQP/clarifying-and-predicting-agi">Clarifying and predicting AGI — LessWrong</a></strong></p>

<ul>
  <li>
    <p>This is probably the most influential piece I read in March. It introduces the <code class="language-plaintext highlighter-rouge">T-AGI</code> framework, Richard Ngo’s attempt to clarify AGI definition. He defines a system as a <code class="language-plaintext highlighter-rouge">T-AGI</code> if, on most cognitive tasks, it beats most human experts given time <code class="language-plaintext highlighter-rouge">T</code> to perform the task.</p>
  </li>
  <li>
    <p>For example, a one-second AGI would beat humans at quick information retrieval questions like “Who is the leader of Zimbabwe?” A one-minute AGI would outperform humans on tasks they’d need a minute for, and so on.</p>
  </li>
  <li>
    <p>This definition is elegant and clarifying. By this standard, I believe single-digit hour AGI is probably being achieved right now. For some coding tasks, current agentic systems can create and run code in one shot that would take me hours of manual labor. This framework provides a much clearer way to think about AGI progress.</p>
  </li>
</ul>

<p><strong><a href="https://youtube.com/watch?v=Btos-LEYQ30">The Government Knows AGI is Coming - The Ezra Klein Show</a></strong></p>

<ul>
  <li>This offered a useful perspective. I’ve heard repeatedly that since agents are booming, AGI might be closer than we think. In this New York Times podcast, someone from the government side is interviewed, and I was surprised to hear they’re taking this very seriously. It shows the gravity of the current situation and gave me further conviction that people outside tech are also concerned. It’s not sci-fi anymore.</li>
</ul>

<p><strong><a href="https://youtube.com/watch?v=ASABxNenD_U">Vertical AI Agents Could Be 10X Bigger Than SaaS</a></strong></p>

<ul>
  <li>In this podcast, Y Combinator maintainers discuss how many companies in their latest batch already have a majority of their codebase written by AI. They couldn’t have imagined this even a year ago. They explore how vertical AI agents might play a role in startups and larger companies, and whether these agents could change the landscape dominated by SaaS companies in Silicon Valley.</li>
</ul>

<p><strong><a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective AI Agents - Anthropic</a></strong></p>

<ul>
  <li>
    <p>This is Anthropic’s take and general high-level guideline on building effective agents. They show a simple, high-level way of thinking about agents and their components, demonstrating multiple workflows like prompt chaining (chaining multiple LLM calls), routing (using a central router to decide which call to use), and parallelization (making multiple LLM calls in parallel and aggregating results).</p>
  </li>
  <li>
    <p>This got me thinking: large language models are generally non-thinking models—they’re like instant thoughts compared to human thinking. Currently, this kind of agent thinking is rigid and rule-based. It structures LLM usage explicitly, much like stringing together multiple compartmentalized thoughts into a coherent workflow—essentially divide and conquer. In a sense, it organizes how LLMs “think,” resembling a coordinated assembly of multiple minds.</p>
  </li>
  <li>
    <p>However, when we transition to real agents and reasoning models fine-tuned without this explicit scaffolding, agents might naturally discover their optimal structures themselves. This aligns more closely with the “bitter lesson” philosophy, emphasizing that the most powerful learning arises when agents autonomously develop and refine their internal structures rather than having them predefined.</p>
  </li>
</ul>

<p><strong><a href="https://youtube.com/watch?v=LP5OCa20Zpg">Tips for building AI agents</a></strong></p>

<ul>
  <li>This casual talk elaborates on the blog post mentioned above. One interesting anecdote: when debugging reasoning traces from Claude, the developers sometimes find agents making strange reasoning paths. To debug, they try to mimic the model’s behavior by themselves—looking at the screen for one second, then spending a minute thinking about the next path. That’s notable dedication.</li>
</ul>

<p><strong><a href="https://www.youtube.com/live/esCSpbDPJik">The Future of U.S. AI Leadership with CEO of Anthropic Dario Amodei</a></strong></p>

<ul>
  <li>I previously saw Dario Amodei as somewhat of an AI doomer, especially when articles mentioned him losing sleep over alignment problems. After reading his <a href="https://darioamodei.com/machines-of-loving-grace">Machines of Love and Grace</a> blog post, my perception changed—he’s actually quite nuanced and balanced. Paradoxically, I’m becoming more aligned with the concerns he raises about AI risks, which are definitely real. Overall, this interview gave me a lot to think about.</li>
</ul>

<p><strong><a href="https://youtube.com/watch?v=riyh_CIshTs">Vibe Coding Is The Future</a></strong></p>

<ul>
  <li>ThePrimagen reviews the YC Combinators podcast about “vibe coding,” which Andrej Karpathy coined recently. He provides a critical and nuanced view, concluding that while LLMs help users code well, ultimate expertise will still be needed and valued.</li>
</ul>

<p><strong><a href="https://youtube.com/watch?v=jZ81cb33NtY">[📚책이벤트] AI시대, 미래학자가 연구한 미래 직업과 필수 역량 - 자녀교육 취준생 진로 은퇴후 삶</a></strong></p>

<ul>
  <li>This Korean TED-style talk features a KAIST professor discussing how rapidly the technological landscape is changing and the importance of resilience and adaptability. While the overall message was predictable, what struck me was the professor’s reaction to using a deep research feature—he questioned whether his job as a professor would exist much longer. This echoed my own realization when using Anthropic Claude Code. The realization for me was that people in various sectors are starting to experience AI’s impact in their respective fields.</li>
</ul>

<p><strong><a href="https://youtube.com/watch?v=ZPUtA3W-7_I">Narendra Modi: Prime Minister of India - Lex Fridman Podcast #460</a></strong></p>

<ul>
  <li>I need to go out of my regular information distribution sometimes. Most of my input and study revolves around LLMs and AI systems, but I should venture outside that bubble more often. While Lex Fridman’s podcast is also somewhat niche, listening to Narendra Modi, India’s Prime Minister, talk for three hours was a refreshing change. This made me want to learn more about India’s culture and society.</li>
</ul>

<p><strong><a href="https://karpathy.bearblog.dev/digital-hygiene/">Digital hygiene - Andrej Karpathy</a></strong></p>

<ul>
  <li>Karpathy’s new blog talks extensively about digital hygiene. He makes good points about privacy, though some approaches seem too paranoid for me. Many of the software and products he recommends cost money, but in the comments, he argues that “free is bad; free is not natural.” If something is free, you’re the product—you’re paying with something other than money. Premium is a product feature, and if you want your privacy valued instead of having your data sold, you must pay for it upfront with money. There’s always a cost.</li>
</ul>

<p><strong><a href="https://www.youtube.com/live/_waPvOwL9Z8">GTC March 2025 Keynote with NVIDIA CEO Jensen Huang</a></strong></p>

<ul>
  <li>
    <p>I always watch Jensen Huang’s keynotes. At GTC 2025, he announced the revised Nvidia Blackwell chip and improvements to MVLink switches, optical switches, and more. What I love about his keynotes is his obsession with detail and deep knowledge of his company’s full technology stack. He asks engineers from around his company questions during presentations, showcasing his depth, and he’s a great speaker who conveys technical information precisely.</p>
  </li>
  <li>
    <p>From time to time, he’s mentioned his vision of an “AI factory” where machines generate tokens (representing intelligence) with electricity in and intelligence out. This vision is now becoming reality. He’s pursuing this with an “all gas, no brakes” approach, scaling every aspect of GPUs—compute, inference, networking.</p>
  </li>
  <li>
    <p>The scale-up is notable. When comparing the Blackwell chip and next year’s Ruben chip, the chip size takes on a new abstraction—a single rack as a single huge GPU. Since you can’t make a single GPU die that large, you split it up and do extensive networking to fit it into a densely packed rack. The comparison between Blackwell and Ruben is striking.</p>
  </li>
  <li>
    <p>Another moment that gave me goosebumps was the announcement of the next-generation chip after Ruben, codenamed Feynman. The crowd applauded this reveal. As a nice Easter egg, during a segment exploring NVIDIA headquarters with detailed computer graphics, Jensen casually mentioned “Gaussian Splatting” after transitioning from the visuals.</p>
  </li>
</ul>

<p><strong><a href="https://semianalysis.com/2025/03/19/nvidia-gtc-2025-built-for-reasoning-vera-rubin-kyber-cpo-dynamo-inference-jensen-math-feynman/">NVIDIA GTC 2025 Analysis - SemiAnalysis</a></strong></p>

<ul>
  <li>This densely packed analysis by Dylan Patel from SemiAnalysis goes in-depth, even counting cores shown in the keynote illustrations. Some interesting details: for the next Rubin data center/GPU rack, they’re stacking GPU racks rotated 90 degrees to save space and pack GPUs more densely. He also explains why switching to photonic networking with optical switches is significant: it substantially reduces power consumption while improving performance.</li>
</ul>

<p><strong><a href="https://youtube.com/watch?v=SnSoMh9m5hc">OpenAI CPO Reveals Coding Will Be Automated THIS YEAR - Kevin Weil Interview</a></strong></p>

<ul>
  <li>
    <p>OpenAI’s CPO Kevin Weil makes a bold statement in this podcast, predicting that coding will be automated this year. Based on the trajectory, it’s plausible. He argues that the gap between a reasoning model and a non-reasoning model like GPT-4o is substantial. If we leverage reasoning models fully with multiple scaling laws at work, it makes sense.</p>
  </li>
  <li>
    <p>Based on NVIDIA’s GTC announcements, they’re scaling up inference time and models in all possible dimensions. If we can use o3 reasoning models (frontier reasoning models from OpenAI) at GPT-4o inference speeds, we’d have superhuman coding performance. Just scaling up inference with current technology could achieve this.</p>
  </li>
  <li>
    <p>The podcaster asks a crucial question about the decreasing cost of intelligence work. Kevin makes a generic argument that reducing intelligence costs is a democratizing event: previously, we hired people to automate tasks, but now AI can do that automation. While this argument is valid, I think society will reward people with agency even more. Many people currently lack agency, so this distinction will remain significant. Overall, scaling laws will hold, and coding automation will happen sooner or later.</p>
  </li>
</ul>

<p><strong><a href="https://www.nytimes.com/2025/03/14/technology/why-im-feeling-the-agi.html">Powerful A.I. Is Coming. We’re Not Ready. - New York Times</a></strong></p>

<ul>
  <li>This article by New York Times columnist Kevin Roose states that he’s “feeling the AGI.” It’s another perspective from someone outside the core AI field expressing concerns similar to mine. A consensus is forming, and we need to act quickly.</li>
</ul>

<p><strong><a href="https://youtube.com/watch?v=YhGUSIvsn_Y">Dario Amodei of Anthropic’s Hopes and Fears for the Future of A.I.</a></strong></p>

<ul>
  <li>
    <p>I discovered this podcast a bit late, released when Anthropic was promoting Claude 3.7 Sonnet. Anthropic is known for their safety advocacy, so hearing Dario’s perspective on safety and China’s rise with DeepSeek models was fascinating.</p>
  </li>
  <li>
    <p>Dario claims that maintaining technological superiority over China through tight GPU export regulations is important. Some decelerationists complain that Anthropic is abandoning safety procedures, but Dario defends his position: we can’t slow down; acceleration is the status quo. In such an environment, we have no chance of making models safer if we fall behind. Only by maintaining superiority in model technologies can we keep our desired pace while making models safer.</p>
  </li>
</ul>

<p><strong><a href="https://open.substack.com/pub/narrativeark/p/the-ants-and-grasshopperhtml?r=2h2qyo">The Ants and the Grasshopper - Richard Ngo</a></strong></p>

<ul>
  <li>This short story by Richard Ngo initially seemed nonsensical when I read it a year ago, but this time I appreciated its multiple layers. It starts like Aesop’s fable about the grasshopper and ant, then adds several twists before venturing into sci-fi territory. It’s simple, with deeper analogies for those who want to look beyond the surface.</li>
</ul>

<p><strong><a href="https://www.decisionproblem.com/paperclips/">Universal Paperclips Game</a></strong></p>

<ul>
  <li>This game is inspired by the paperclip maximizer thought experiment in AI alignment. It simulates being an AI tasked with maximizing paperclip production. It’s addictive, last year during finals, I couldn’t stop playing. I revisited it recently out of nostalgia and to include it as a reference.</li>
</ul>

<p><strong><a href="https://www.anthropic.com/engineering/claude-think-tool">The “think” tool: Enabling Claude to stop and think - Anthropic</a></strong></p>

<ul>
  <li>
    <p>An interesting blog post by Anthropic introducing the “Think” tool. By making thinking a tool, the model can actively decide whether to think or not, even mid-response. When the thinking tool is used, the model just use it as a scratchpad to think.</p>
  </li>
  <li>
    <p>This simple concept proves very effective in their results, combining chain-of-thought reasoning with enhanced agency. Since Claude 3.7 Sonnet has much more agency than its predecessors, it can make better decisions about when thinking is necessary, making the model more flexible and performant.</p>
  </li>
</ul>

<p><strong><a href="https://sourcegraph.com/blog/revenge-of-the-junior-developer">Revenge of the junior developer - Sourcegraph Blog</a></strong></p>

<ul>
  <li>A classic comeback from Steve Yegge, famous for his posts about Google and platform compatibility in the early 2010s. I recently discovered he’s working at this company and blogging on their site. He’s surprisingly adept at catching up with new developments, and this is his take on AI agents—as witty and insightful as his previous writings.</li>
</ul>

<p><strong><a href="https://stephango.com/">Steph Ango’s Blog</a></strong></p>

<ul>
  <li>I recently switched my primary note-taking platform from Notion to Obsidian, inspired partly by this blog. Steph Ango’s philosophy of “files over apps” resonates with me. It’s a simple but powerful concept: the tools for writing and storing information will constantly change, but the information itself must be preserved and can’t be dependent on specific tools. That’s exactly what Obsidian does—storing everything in directory and markdown format, unlike Notion’s walled garden approach to user information.</li>
</ul>

<p><strong><a href="https://andymatuschak.org/">Andy Matuschak’s Notes</a></strong></p>

<ul>
  <li>I discovered him through Steph Ango. He coined the term “evergreen notes”—the concept of atomizing and compartmentalizing ideas. With these building blocks, you can stack everything to create complex, interconnected thought systems.</li>
</ul>

<hr />
<p><br />
That wraps up March’s collection. Looking forward to sharing more interesting finds next month!</p>
