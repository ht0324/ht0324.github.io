---
layout: post
title: DeepSeekMath - Review
date: 2025-01-27 15:00:00
description: Reviewing DeepSeekMath paper
tags: AI
categories: Paper
giscus_comments: true
---

In this post, I'm reviewing ["DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models"](https://arxiv.org/abs/2402.03300), which introduces DeepSeekMath 7B, a math-specialized language model.  

What stands out about this paper isn't just the performance of DeepSeekMath but the philosophy behind its design. DeepSeek consistently focuses on first-principles thinking—stripping down unnecessary complexity, focusing on what's truly important, and optimizing aggressively for efficiency. Given that DeepSeek operates under serious GPU constraints due to US export regulations, this emphasis on efficiency isn't just a preference but a necessity, shaping their entire research trajectory.  

The key technical contribution of this paper is **Group Relative Policy Optimization (GRPO)**—a modification of Proximal Policy Optimization (PPO) that eliminates the need for a separate value model, making reinforcement learning (RL) significantly more efficient.  

---

### Key Concepts

**Mathematical Reasoning in LLMs**  
Mathematical reasoning is tough for language models. Unlike general NLP tasks, where fluency and coherence are enough, math requires structured problem-solving. DeepSeekMath is specifically trained with 120B math-related tokens and fine-tuned with reinforcement learning to improve its reasoning ability.

**Reinforcement Learning (RL) for Mathematical Reasoning**  
DeepSeekMath uses RL to refine its outputs by training with a reward model. Instead of just relying on standard instruction tuning, RL helps align model responses towards more precise and logically structured solutions.

**Group Relative Policy Optimization (GRPO)**  
GRPO is the highlight of the paper. It's a **compute-efficient** alternative to standard PPO. Traditional PPO requires a separate value model to estimate advantage, which is computationally expensive. Instead, GRPO ranks multiple sampled responses and calculates rewards based on their relative ranking, removing the need for an explicit value function. This aligns well with the original spirit of PPO while making it much more efficient.

**Why Efficiency Matters Here**  
DeepSeek, as a company, has repeatedly [emphasized](https://www.thefai.org/posts/deepseek-s-success-reinforces-the-case-for-export-controls) that their biggest bottleneck is compute, not talent. This constraint forces them to innovate in ways that maximize training efficiency. By making reinforcement learning more efficient, GRPO allows them to run **more iterations** of training within the same compute budget. Given that experience (the number of training iterations) is a critical factor in model performance, this approach compounds over time.

---

### Key Takeaways (What I Learned)

**First-Principles Thinking in Model Design**  
One of the biggest takeaways from this paper is how DeepSeek consistently strips things down to what actually matters. The removal of the value model in PPO is a prime example of this. Instead of treating it as an unavoidable cost, they found a way to compute advantage **without it**, saving compute while still aligning with the core principle of PPO.

**Reinforcement Learning Efficiency Can Directly Impact Model Performance**  
A lot of research in RL for LLMs focuses on making models "better," but this paper indirectly makes another point—**efficiency itself is a performance factor**. If you can run 2x or 3x more RL iterations for the same compute budget, you might end up with a better-trained model even if the method itself isn't inherently more powerful. This is a perspective that isn't always emphasized but makes a lot of sense in practice.

**GRPO is an Elegant Fix to a Known Problem**  
PPO's requirement for a separate value model has long been a pain point due to its added complexity and compute cost. GRPO solves this by leveraging relative ranking instead of absolute value estimation. What I like about this approach is that it's not just a random heuristic—it actually aligns **better** with the fundamental idea of PPO while also making it more practical. This kind of solution—where something becomes both *simpler* and *better*—is rare and always worth paying attention to.

**DeepSeek's Strategy of Leaning into Efficiency is Paying Off**  
The efficiency-first approach DeepSeek is taking is starting to show real results. It's easy to get caught up in scaling laws and assume more compute is always better, but DeepSeek is proving that **how** you use that compute is just as important. By optimizing RL efficiency, they can squeeze more training out of their limited resources, which in turn compounds into better models. This approach is clearly working, as seen later in DeepSeek R1, which made a significant impact.

---

### Summary & Final Thoughts  

DeepSeekMath is a great example of how efficiency-driven research can lead to meaningful improvements. GRPO streamlines PPO by removing the need for a value model, reducing computational cost while staying true to the original PPO formulation. This enables DeepSeek to run more RL iterations, which in turn leads to better-trained models.  

This paper reinforces the idea that **efficiency isn't just a secondary concern—it's a core factor that directly influences model performance**. It also shows how taking a first-principles approach to ML research can lead to both simpler and more effective solutions. While DeepSeekMath itself is a step forward in mathematical reasoning, I think the bigger impact of this work is in how it shapes reinforcement learning efficiency going forward.