---
layout: post
title: DeepSeek OCR, and why I think vision eats language
date: 2025-10-24 12:00:00
description: Notes on DeepSeek OCR
tags: AI
categories: Blog
giscus_comments: true
---

Recently I’ve been trying to get along with school and all the coursework and settling into a new environment. So I wasn’t putting much effort into reading papers, which I used to enjoy. But this week was different. I found a paper that pulled me back in: [DeepSeek OCR](https://arxiv.org/abs/2510.18234). It’s a peculiar paper in a good way. I like DeepSeek’s papers: they’re thorough and open, they don’t hide things from researchers.

Depending on your interpretation, its findings are very much aligned with the Bitter Lesson.

### Key Takeaways

The core takeaway from the paper is that using a vision encoder to process documents as images they were able to achieve ten times more efficiency than using text tokens. In other words, it's vastly more efficient to screenshot a document and feed it to a large language model than to paste the raw text, with little to no loss in performance.

But this isn't entirely new. About a year ago, when Gemini 2.5 Pro came out, I was playing with it in Google AI Studio. I pasted a document and compared it to drag‑and‑drop upload. The full text token count was much larger than the image‑based upload. They were converting files to images and counting vision tokens. So they already kind of knew this.

Also, I don’t know about ChatGPT, but for a long time, Anthropic’s Claude seemed to feed uploaded documents as images, not parsed text, from their webpage. They must have tested it and green‑lit it because it was more feasible and efficient.

### Where does vision stop and language begin?

This also reminded me of a 2020 Lex Fridman conversation with Ilya Sutskever:

> [Ilya Sutskever:](https://youtu.be/13CZPWmke6A?t=1566) Where does vision stop and language begin? If I show you a piece of paper with letters on it, you have a vision system, you say it’s the best human‑level vision system, I open a book and show you letters: will it understand how these letters form into words and sentences and meaning? Is this part of the vision problem?

> [Lex Fridman:](https://youtu.be/13CZPWmke6A?t=1612) Where does vision stop and language begin? Thats an really interesting question... One possibility is that it’s impossible to achieve really deep understanding in either images or language without basically using the same kind of system, so you’re going to get the other for free...   
> Ilya Sutskever: A lot of it depends on your definitions of perfect vision: because really, you know, reading is vision. but should it count?

I emphasize again: this was recorded in 2020. Five years is a long time in this field. But still, when I think of this converstation, there is a lot of food for thought.

My opinion: vision precedes language here; or said differently, for documents, language sits inside vision. If you can see the page, you can get the language. Starting from text alone can’t recover layout, typography, figures, or spatial structure. All that subtle rich signals are lost when you flatten the document into text. It's not just about efficiency, it's about the nature of the task.

### Bitter Lesson vibes

This feels like the Bitter Lesson again. Methods that scale win. Text is one‑dimensional and throws away structure; you end up with fragile pipelines. Vision is two‑dimensional and more general. If we want to be more Bitter‑Lesson‑aligned and pursue methods that scale, language tasks will increasingly be subsumed by vision tasks for documents. Looking at human modality: we have five senses. There is no “text modality.” What we do for “natural language processing” in our brains, the modality is auditory and vision. For text, it’s purely vision.

Twenty years ago, to take notes people have to type and store strings. Today, if I want to copy a whiteboard or an announcement in a classroom, everybody takes pictures. Nobody writes it down. It’s more general. I think the same thing will happen with language models. Twenty years from now, god knows how we'll interact with AI models, but we’ll probably do the equivalent of taking pictures of text for much more capable models, and look back at “paste-the-whole-document-as-text-language-models” as quaint.


### Final thoughts

I think we’re getting the answer Ilya hinted at back in 2020. Where does vision stop and language begin? For documents, language lives inside vision. DeepSeek OCR is interesting not because it invents a new modality, but because it treats the obvious with rigor: for documents, seeing beats parsing. Once you accept that, a lot of design choices get simpler.

The fact that labs like Anthropic have long defaulted to image‑based document uploads suggests they already tested this and know it’s more feasible and efficient. It makes you wonder how much frontier models already know—and how far ahead they are.
