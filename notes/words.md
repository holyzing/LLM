# 先做一个垃圾出来
- **NLP** Natural Language Processing 自然语言处理
- **pre-train** 预训练
- **SFT** supervised fine-tuning 监督微调
- **PEFT** parameter-efficient fine-tuning 参数高效微调
- **RLHF** reinforcement learning with human feedback 基于人类反馈的强化学习
- **autoregression** 自回归
- **transformer** 神经网络结构中的一种，用于处理序列数据
- **LangChain** 大模型应用开发框架
- **Tokenization** 分词化后与词表映射
- **Prompt** 生成模型的输入,提示词
- **RAG** retrieval-augmented generation 检索增强生成
- **总结、推断、转换** summarization, inference, translation(transformation)
- **基础LLM** 基础LLM是基于文本训练数据，训练出预测下一个单词能力的模型
- **指令微调LLM** Instruction tuned 通过专门的训练，可以更好地理解并遵循指令, 也就是受控的训练过程
- **kaggle** 数据科学竞赛平台
- **colab** 谷歌的在线编程环境
- **LoRA** Low-Rank Adaptation 低秩适应，核心思想是通过添加低秩矩阵来近似表示模型的权重更新，<br/>
  而不是直接更新原始的高维权重矩阵，从而减少参数量，在处理大规模预训练模型时表现出色‌
- **QLoRA** Quantized Low-Rank Adaptation 量化低秩适应，一个使用量化思想对LoRA[2]进行优化的量化算法,
- **T5** Text-to-Text Transfer Transformer  是继 BERT 之后Google的又一力作，它是一个文本到文本迁移（转换）的基于Transformer的NLP模型，<br/>
  通过将 所有任务统一视为一个输入文本并输出到文本(Text-to-Text)中，即将任务嵌入在输入文本中，用文本的方式解决各种NLP的任务。<br/>
  T5是由google的Raffel等人于2019年提出了新的预训练模型，其参数量高达110亿，完爆BertLarge模型，且在多项NLP任务中达到SOTA性能，<br/>
  在NLP兴起了“迁移学习技术”热潮，带来了一系列方法、模型和实距的创新。<br/>
  是基于Transformer结构的序列到序列(Seq2Seq)模型，其主要特点是将多种NLP任务（如翻译、摘要、问答等）转化为一个统一的框架下进行训练。<br/>
  即在不同的具体任务上有不同的prefix指导模型，对预训练目标进行大范围探索，最后得到一个很强的baseline。而我们之后做这方面实验就能参考它的一套参数<br/>
- **GPT** Generative Pre-trained Transformer  是一种基于Transformer的预训练模型，由OpenAI提出，<br/>
  通过大规模的无监督学习，学习到了大量的语言知识，可以用于各种NLP任务，如文本生成、文本分类、文本摘要等。

- **Tokenization** Byte Pair Encoding(BPE) 字节对编码；
- **长短期记忆网络** Long Short-Term Memory(LSTM) 是一种时间递归神经网络，适合于处理和预测时间序列中间隔和延迟非常长的重要事件；