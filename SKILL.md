---
name: smart-translator
version: 2.0.0
author: Administrator
description: 基于大模型的智能翻译技能，支持网页、Word、PDF、Markdown 文档翻译，智能分批处理，断点续翻，成本透明
tags: [translation, chinese, english, batch, document, llm, smart]
category: document
license: MIT
---

# Smart Translator (智能翻译官)

基于大模型的智能翻译技能，支持多种文档格式翻译，具备智能分批、断点续翻、成本估算等功能。

## 🎯 使用场景

- **网页翻译**：URL 链接、HTML 内容、博客文章
- **文档翻译**：Word (.docx)、PDF、Markdown (.md)、TXT
- **批量翻译**：多个文件批量处理
- **长文档翻译**：> 50000 字智能分批

## 🚀 核心能力

### 1. 智能分批处理
- 根据模型上下文限制动态调整分批大小
- 支持 Qwen、GPT-4o、Claude 等多种大模型
- 自动断点续翻，避免重复翻译

### 2. 多格式支持
- Word (.docx) - 保持格式
- PDF - 重新生成布局
- Markdown (.md) - 保持结构
- 网页 - 提取正文翻译

### 3. 大模型集成
- 阿里云百炼（Qwen 系列）
- SiliconFlow（DeepSeek、Qwen）
- OpenAI（GPT-4o）
- Anthropic（Claude-3.5）

### 4. 翻译模式
- **strict**: 100% 中文输出
- **technical**: 保留技术术语
- **fluent**: 优化流畅度
- **localized**: 本地化表达

## 📋 工作流程

```
1. 解析文档 → 2. 智能分批 → 3. 创建检查点 → 4. 并发翻译 → 5. 合并输出
```

## ⚙️ 配置选项

```yaml
translation:
  model: qwen-plus  # 选择大模型
  mode: strict  # 翻译模式
  target_language: zh  # 目标语言
  
batch:
  enabled: true
  max_batch_size: 10000
  max_concurrent: 5
  
checkpoint:
  enabled: true
  cache_dir: .translation_cache
```

## 🚀 快速开始

### 安装依赖
```bash
pip install python-docx pdfplumber reportlab asyncio aiohttp
```

### 翻译文档
```bash
python smart_translator.py input.docx --output output_zh.docx
```

### 批量翻译
```bash
python smart_translator.py ./docs/ --batch --output ./docs_zh/
```

### 翻译网页
```bash
python smart_translator.py --url https://example.com/article
```

## 📊 性能指标

| 文档长度 | 模型 | 预计时间 | 估算成本 |
|---------|------|---------|---------|
| 5000 字 | qwen-turbo | < 30 秒 | ¥0.01 |
| 50000 字 | qwen-plus | 3-5 分钟 | ¥0.50 |
| 100000 字 | qwen-max | 8-10 分钟 | ¥2.00 |

## 📝 使用示例

### 示例 1：翻译 Word 文档
```python
from smart_translator import SmartTranslator

translator = SmartTranslator(model="qwen-plus", mode="technical")
result = await translator.translate_document("input.docx")
print(f"输出：{result}")
```

### 示例 2：批量翻译
```python
translator = SmartTranslator()
await translator.translate_batch("./docs/", output_dir="./docs_zh/")
```

### 示例 3：断点续翻
```python
# 自动检测未完成的翻译
translator = SmartTranslator()
await translator.resume_translation("input.docx")
```

## 🛠️ 技术实现

- **智能分批**：按语义和章节分割
- **进度管理**：JSON 检查点文件
- **并发控制**：asyncio + Semaphore
- **成本估算**：基于 Token 计算

## ⚠️ 注意事项

1. 需要配置大模型 API Key
2. 专业文档建议人工校对
3. 扫描版 PDF 需要 OCR 预处理

## 📄 许可证

MIT License

## 🔗 相关链接

- GitHub: https://github.com/hotice888/smart-translator
- 问题反馈：https://github.com/hotice888/smart-translator/issues
