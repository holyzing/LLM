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
- **RAG** Retrieval-Augmented Generation 检索增强生成；[干货！带你了解7种检索增强生成 (RAG) 技术](https://mp.weixin.qq.com/s/6VxttYwYok_YPUeA7CIorA)
- **MOE** Mixture of Experts 专家混合模型;

- **self-attention** 自注意力机制是一种内部注意力机制，其核心思想是让序列中的每个元素（如单词、图像区域）与其他所有元素进行交互，
通过计算相关性权重，动态调整对每个元素的关注程度。<br/>
与传统注意力的区别：传统注意力机制需要依赖外部序列（如Encoder-Decoder中的目标序列），而自注意力仅需在单一序列内部完成交互，无需外部信息参与。<br/>
核心目标：解决长距离依赖问题，增强模型对全局上下文的理解能力.
- **multi-head attention** 多头注意力机制

# DeepSeek 的优点
1. 弱化了提示词工程的复杂性，降低了提示词技巧的门槛
2. DeepSeek-R1, GPT-o1 属于推理模型 （resoning model），对应的 GPT-4o, 文心一言等模型都属于 指令模型 (instruction model)
3. DeepSeek-R1 具有知识涌现的能力
4. 大语言模型回答不出 草莓（strawberry）中有个 字母 r 的原因是，该单词被 Tokenization 后的 Token序列 中没有 r 字母，而推理模型 <br/>
   可以通过推理的方式回答出草莓中有个字母 r，虽然推理过程较慢，较复杂，但是可以回答出这个问题

# 大模型的局限性
1. 知识库语料的时间局限性，大模型的知识库语料是有限的，无法获取到最新的知识，有三重时间壁垒，<br/>
   - 语料库准备的时间局限性，比如数据清洗与结构化都是需要耗费大量时间的
   - 模型训练的时间局限性
   - 训练完成之后的模型微调，强化学习等时间局限性
2. 缺乏自我认知，和自我学习的能力，即 AGI 的能力, 比如询问模型你是谁，因为语料库的问题，经常回答错误，出现幻觉，<br/>
   而回答正确也是因为有可能 模型厂商做过特定的处理。
3. 上下文长度限制（DeepSeek-R1 的为 64K-128K），即使你给投喂太长的文本，模型也是通过 RAG 的方式进行处理，<br/>
4. 对话轮次过多会出现上下文遗忘
5. 输出长度有限（4k-8k），比如万字长文的翻译等是无法一次性输出的，如果要输出长文，则可通过循环或者是列提纲的方式让模型分次输出

# 模型特点和技巧
- 04:27 模型特点1：推理模型vs指令模型
- 07:08 模型特点2：知识截止时间
- 11:29 模型特点3：缺乏自我认知
- 12:51 模型特点4：记忆限制
- 13:47 模型特点5：输出长度限制
- 14:56 技巧1：提出明确要求
- 16:11 技巧2：要求特定风格
- 17:13 技巧3：提供充分背景
- 17:48 技巧4：标注知识状态
- 18:34 技巧5：定义目标而非过程
- 19:34 技巧6：提供AI不具备的知识
- 20:17 技巧7：从开放到收敛

# 对于 DeepSeek-R1 无效的提示词技巧
+ 思维链提示
+ 结构化提示词
+ 要求扮演专家角色
+ 假装完成任务后给奖励
+ 少示例提示 （few-shot）
+ 角色扮演
+ 对已知概念进行解释
