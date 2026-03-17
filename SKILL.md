---
name: smart-translator
version: 2.0.0
author: Administrator
description: WordPDFMarkdown 
tags: [translation, chinese, english, batch, document, llm, smart]
category: document
license: MIT
---

# Smart Translator (?

?

##  

##  

Smart Translator  `config.json` ?API ?

### 

```
active_skills/smart-translator/config.json
```

### 

```bash
# 
python config_manager.py show

# ?
python config_manager.py list

# ?
python config_manager.py preset siliconflow

# 
python config_manager.py preset dashscope

#  CodingPlan
python config_manager.py preset codingplan

# ?OpenAI GPT-4o
python config_manager.py preset openai
```

### 

 `config.json` ?

```json
{
  "provider": "siliconflow",
  "provider_name": "",
  "api_key_env": "SMART_TRANSLATOR_API_KEY",
  "base_url": "https://api.siliconflow.cn/v1/chat/completions",
  "model": "Qwen/Qwen3-8B",
  "model_config": {
    "max_tokens": 32000,
    "batch_size": 10000,
    "temperature": 0.3,
    "price_per_1m_tokens": 0.01
  },
  "translation_mode": "technical",
  "language": "zh-CN"
}
```

###  API Key

**Windows:**
```cmd
setx SMART_TRANSLATOR_API_KEY "sk-your-api-key-here"
```

**Linux/macOS:**
```bash
export SMART_TRANSLATOR_API_KEY="sk-your-api-key-here"
```

### 

| ?|  | ?|  |  |
|--------|------|--------|------|----------|
| SiliconFlow | Qwen/Qwen3-8B | 32K | 0.01/1M | ??|
| SiliconFlow | Qwen/Qwen2.5-72B | 32K | 0.04/1M | ?|
| ?| qwen-plus | 32K | 0.50/1M |  |
| ?| qwen3.5-plus | 32K | 7.9/?| ?|
| OpenAI | gpt-4o | 128K | 5.0/1M | ?|

?`CONFIG_GUIDE.md`


- ****URL HTML ?
- ****Word (.docx)PDFMarkdown (.md)TXT
- ****?
- **?*? 50000 ?

##  

### 1. 
- ?
-  QwenGPT-4oClaude 
- ?

### 2. ?
- Word (.docx) - 
- PDF - 
- Markdown (.md) - 
-  - 

### 3. ?
- Qwen ?
- SiliconFlowDeepSeekQwen?
- OpenAIGPT-4o?
- AnthropicClaude-3.5?

### 4. 
- **strict**: 100% 
- **technical**: ?
- **fluent**: ?
- **localized**: ?

##  

```
1.  ?2.  ?3.  ?4.  ?5. 
```

##  

```yaml
translation:
  model: qwen-plus  # ?
  mode: strict  # 
  target_language: zh  # 
  
batch:
  enabled: true
  max_batch_size: 10000
  max_concurrent: 5
  
checkpoint:
  enabled: true
  cache_dir: .translation_cache
```

##  ?

### 
```bash
pip install python-docx pdfplumber reportlab asyncio aiohttp
```

### 
```bash
python smart_translator.py input.docx --output output_zh.docx
```

### 
```bash
python smart_translator.py ./docs/ --batch --output ./docs_zh/
```

### 
```bash
python smart_translator.py --url https://example.com/article
```

##  

|  |  |  |  |
|---------|------|---------|---------|
| 5000 ?| qwen-turbo | < 30 ?| 0.01 |
| 50000 ?| qwen-plus | 3-5  | 0.50 |
| 100000 ?| qwen-max | 8-10  | 2.00 |

##  

###  1?Word 
```python
from smart_translator import SmartTranslator

translator = SmartTranslator(model="qwen-plus", mode="technical")
result = await translator.translate_document("input.docx")
print(f"{result}")
```

###  2?
```python
translator = SmartTranslator()
await translator.translate_batch("./docs/", output_dir="./docs_zh/")
```

###  3?
```python
# ?
translator = SmartTranslator()
await translator.resume_translation("input.docx")
```

## ??

- ****?
- ****JSON 
- ****asyncio + Semaphore
- ****?Token 

##  

1.  API Key
2. 
3. ?PDF ?OCR ?

##  ?

MIT License

##  

- GitHub: https://github.com/hotice888/smart-translator
- https://github.com/hotice888/smart-translator/issues
