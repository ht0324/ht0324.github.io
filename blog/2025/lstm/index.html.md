# Revisiting the 2014 Sequence-to-Sequence Paper
_Published: 2025-04-20_
_Tags: AI_
_Categories: Paper_
_Original: https://ht0324.github.io/blog/2025/lstm/_

<p>I recently went back to read the 2014 paper “<a href="https://arxiv.org/abs/1409.3215">Sequence to Sequence Learning with Neural Networks</a>” by Sutskever, Vinyals, and Le. Since it’s such a seminal paper, practically ancient by today’s ML standards, I thought it would be interesting to look back. While the method itself (LSTM encoder-decoder) is relatively simple compared to modern architectures, focusing on their thinking process back when deep learning was still in its infancy was insightful. I found some things they mentioned almost casually that felt non-trivial to me now.</p>

<p>Here are some of my main takeaways:</p>

<h3 id="refreshing-views-on-dnn-power">Refreshing Views on DNN Power</h3>

<p>The paper starts by framing Deep Neural Networks (DNNs) in ways I hadn’t explicitly considered before. They state:</p>

<blockquote>
  <p>“DNNs are powerful because they can perform arbitrary parallel computation for a modest number of steps.”</p>
</blockquote>

<p>This sentence, while true and maybe obvious in retrospect, struck me. Of course, we know matrix multiplications are parallelizable and run well on GPUs, but thinking about it from the perspective of <em>individual neurons</em> performing computations in parallel felt like a useful angle on <em>why</em> NNs are suited for this hardware.</p>

<p>They also highlight:</p>

<blockquote>
  <p>“…their ability to sort N N-bit numbers using only 2 hidden layers of quadratic size…”</p>
</blockquote>

<p>Again, a specific example of computational power packed into a relatively simple network that I hadn’t really internalized.</p>

<h3 id="the-core-problem-and-the-lstm-solution">The Core Problem and the LSTM Solution</h3>

<p>The authors clearly state the limitation they were tackling:</p>

<blockquote>
  <p>“Despite their flexibility and power, DNNs can only be applied to problems whose inputs and targets can be sensibly encoded with vectors of fixed dimensionality.”</p>
</blockquote>

<p>This was a major hurdle for many important tasks like machine translation or question answering, where sequence lengths vary. This is where the Long Short-Term Memory (LSTM) network comes in.</p>

<p>For me, the biggest contribution of this paper is that they took the LSTM and <em>successfully trained an encoder-decoder architecture at scale</em> on a difficult task (English-to-French translation). They showed that LSTMs weren’t just a theoretical curiosity; they were <em>practical</em> for real-world, large-scale NLP problems. This was the first paper that demonstrated LSTMs could <em>work</em> in this way, paving the path for much future research.</p>

<h3 id="the-input-reversal-trick">The Input Reversal Trick</h3>

<p>One specific technical detail that stood out was their trick of reversing the input sentence:</p>

<blockquote>
  <p>“…reversing the order of the words in all source sentences (but not target sentences) improved the LSTM’s performance markedly, because doing so introduced many short term dependencies between the source and the target sentence which made the optimization problem easier.”</p>
</blockquote>

<p>My first reaction was: Okay, reversing the input brings the <em>first</em> source word closer to the <em>first</em> target word, which makes sense for translation since the beginning often sets the context. But what about the <em>last</em> words of the source sentence? Don’t they get pushed really far away from the end of the target sentence?</p>

<p>That’s a valid point, but I think it highlights a trade-off. Getting the beginning of the translation right is often very important; it lays the groundwork. By reversing the input, they made it easier for the optimization process (SGD) to “establish communication” between the early parts of the source and target sequences. The performance gains they reported (perplexity dropping from 5.8 to 4.7, BLEU jumping from 25.9 to 30.6) suggest this was an effective trade-off, making the model learn better, even if it seems counter-intuitive for the tail end of the sequences.</p>

<h3 id="final-thoughts">Final Thoughts</h3>

<p>Reading this paper was a great reminder of how far the field has come, but also of the clear thinking that set the foundations. I admire Ilya Sutskever’s way of thinking; when I listen to him on podcasts, he often speaks with clarity. Looking at this early work reinforces that impression. Maybe I should make a point of reading through more of his papers.</p>
