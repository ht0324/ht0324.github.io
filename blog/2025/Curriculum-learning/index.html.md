# Curriculum learning for LLMs?
_Published: 2025-01-05_
_Tags: AI_
_Categories: Thoughts_
_Original: https://ht0324.github.io/blog/2025/Curriculum-learning/_

<p>I was previously aware of Curriculum Learning, a concept introduced by Yoshua Bengio. The idea is straightforward: you train a model with a curriculum, starting with easier data and progressing to harder datasets. This approach is believed to enhance the model’s ability to learn and generalize.</p>

<p>I thought this concept could be relevant to large language models. For instance, one could start by teaching them basic concepts, like those found in kindergarten materials, and then gradually introduce more advanced subjects like mathematics or science. This structured approach, I believed, would lead to better generalization.</p>

<p>However, I couldn’t find much literature exploring this idea in depth, except for Microsoft’s Phi models. These models use synthetic datasets to generate elementary-level data, teaching a small model to learn English, with some success. For larger, more advanced models trained on the vast expanse of the internet, the consensus seemed to be that the diversity of the dataset would negate the benefits of a curriculum.</p>

<p>The sheer volume and variety of data would mean the model would eventually encounter all parts of the dataset, regardless of the order. This conclusion led me to prematurely end my investigation.</p>

<hr />
<h3 id="a-shift-in-perspective">A Shift in Perspective</h3>

<p>My perspective shifted when I listened to a podcast featuring Yann LeCun and Gary Marcus, interviewed by Lex Fridman. It struck me that these interviews were conducted five years ago, in 2019. In the rapidly evolving field of machine learning, five years is a long time.</p>

<p>Back in 2019, models like ChatGPT and GPT-3 didn’t exist, and the ability of models to understand language and exhibit common sense reasoning was limited. The assessments made by LeCun and Marcus, while accurate for their time, are outdated in the current landscape.</p>

<h3 id="the-challenge-of-outdated-information">The Challenge of Outdated Information</h3>

<p>A significant challenge arises from the fact that current large language models are pre-trained on massive datasets encompassing information from across the globe and various time periods. These datasets inevitably contain outdated information. For example, a statement from a prominent scientist in 2010 claiming that deep learning had hit a dead end would have been accurate then but is false today.</p>

<p>During pre-training, language models struggle to discern the temporal validity of such statements. This raises several questions: How should we address this discrepancy caused by outdated training data? Should we filter out outdated information, or let it be?</p>

<p>As time progresses, the volume of current, up-to-date information will increase. Could we simply dilute the outdated data with newer information? The pre-training stage, as far as I understand, is relatively straightforward, involving next-token prediction and backpropagation across the entire corpus.</p>

<p>There doesn’t seem to be any inherent mechanism within this process to handle the issue of outdated information. I’m unsure how to effectively address this challenge.</p>

<h3 id="the-paradox-of-conflicting-information">The Paradox of Conflicting Information</h3>

<p>However, upon further reflection, the internet is replete with conflicting information. For instance, one can find sources claiming that global warming is false, while others assert its truth. Furthermore, there’s a vast amount of literature, like novels, that are fictional and not meant to be factual.</p>

<p>Despite this, current language models demonstrate a degree of knowledge and, while prone to hallucinations, possess a semblance of a factual world model. This suggests that the vastness of the pre-training corpus might be a factor. It’s possible that conflicting information effectively cancels each other out, allowing the model to learn the nuances of different perspectives.</p>

<hr />
<h3 id="reconsidering-curriculum-learning">Reconsidering Curriculum Learning</h3>

<p>This leads to the question: is curriculum learning then unnecessary? I suspect that the limited research on curriculum learning for large language models might be due to its marginal impact.</p>

<p>While the effectiveness of curriculum learning remains uncertain, I believe that if it is not needed, it would be a testament to the generalization capabilities of large language models. They are able to learn from a chaotic sea of information, discerning patterns and nuances without explicit guidance.</p>

<p>I believe I still need to refine my thoughts on this matter. The interplay between the vastness of training data, the presence of conflicting information, and the potential benefits of curriculum learning is a complex issue that warrants further investigation.</p>
