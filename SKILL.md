---
name: smart-translator
version: 2.1.0
author: hotice888
description: 智能翻译助手，支持 Word/PDF/Markdown 文档翻译，基于大模型 API，自动分批处理，断点续翻
tags: [translation, chinese, english, batch, document, llm, smart]
category: document
license: MIT
repository: https://github.com/hotice888/smart-translator
---

# Smart Translator (智能翻译官)

基于大模型 API 的智能翻译技能，支持多种文档格式翻译，具备智能分批、断点续翻、成本透明等功能。

## 🚀 使用场景

- **网页翻译**: URL 链接、HTML 内容、博客文章
- **文档翻译**: Word (.docx)、PDF、Markdown (.md)、TXT
- **批量翻译**: 多个文件批量处理
- **长文档翻译**: 50000+ 字智能分批

## ✨ 核心能力

### 1. 智能分批处理
- 根据模型上下文限制动态调整分批大小
- 支持 Qwen、GPT-4o、Claude 等多种大模型
- 自动断点续翻，避免重复翻译

### 2. 多格式支持
- Word (.docx) - 保持格式
- PDF - 提取文本翻译
- Markdown (.md) - 保持结构
- 网页/HTML - 提取内容

### 3. 多模型支持
- **SiliconFlow**: Qwen/Qwen3-8B (性价比最高)
- **阿里云**: qwen-plus, qwen3.5-plus
- **OpenAI**: gpt-4o
- **DeepSeek**: DeepSeek-V2

### 4. 翻译模式
- **strict**: 100% 中文，不允许英文
- **technical**: 保留技术品牌名 (推荐)
- **fluent**: 优化流畅度
- **localized**: 本地化表达

### 5. 成本透明
- 实时估算翻译成本
- qwen-plus: ¥0.50/50000 字
- gpt-4o: ¥5.00/50000 字

## 📦 安装方法

### 方法 1: 从 ClawHub 安装

```bash
clawdhub install hotice888/smart-translator
```

### 方法 2: 手动安装

```bash
# 克隆仓库
git clone https://github.com/hotice888/smart-translator.git
cd smart-translator

# 复制技能文件
cp -r * ~/.copaw/active_skills/smart-translator/

# 安装依赖
pip install python-docx pdfplumber reportlab
```

### 方法 3: 从 GitHub 下载

```bash
# 下载技能文件
curl -L https://github.com/hotice888/smart-translator/archive/main.zip -o smart-translator.zip
unzip smart-translator.zip
cp -r smart-translator-main/* ~/.copaw/active_skills/smart-translator/
```

## 🔧 配置方法

### 1. 设置 API Key

**推荐方式** (技能专用):
```bash
# Windows
setx SMART_TRANSLATOR_API_KEY "sk-your-api-key-here"

# Linux/macOS
export SMART_TRANSLATOR_API_KEY="sk-your-api-key-here"
```

**或使用提供商专用变量**:
```bash
# SiliconFlow
setx SILICONFLOW_API_KEY "sk-sf-xxxxxxxx"

# 阿里云
setx DASHSCOPE_API_KEY "sk-ds-xxxxxxxx"

# OpenAI
setx OPENAI_API_KEY "sk-oa-xxxxxxxx"
```

### 2. 编辑配置文件

编辑 `config.json`:
```json
{
  "provider": "siliconflow",
  "provider_name": "硅基流动",
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

### 3. 使用配置管理工具

```bash
cd ~/.copaw/active_skills/smart-translator

# 查看当前配置
python config_manager.py show

# 列出所有预设
python config_manager.py list

# 切换到 SiliconFlow
python config_manager.py preset siliconflow

# 切换到阿里云
python config_manager.py preset dashscope
```

## 💡 使用示例

### 示例 1: 翻译 Word 文档

```python
import asyncio
from smart_translator import SmartTranslator

async def translate_doc():
    translator = SmartTranslator()
    
    await translator.translate_document(
        file_path="input.docx",
        output_path="output_cn.docx",
        max_concurrent=5
    )

asyncio.run(translate_doc())
```

### 示例 2: 翻译网页

```python
import asyncio
from smart_translator import SmartTranslator

async def translate_webpage():
    translator = SmartTranslator()
    
    await translator.translate_document(
        file_path="https://example.com/article",
        output_path="article_cn.md"
    )

asyncio.run(translate_webpage())
```

### 示例 3: 批量翻译

```python
import asyncio
from smart_translator import SmartTranslator

async def batch_translate():
    translator = SmartTranslator()
    
    await translator.translate_batch_files(
        input_dir="docs/en",
        output_dir="docs/cn",
        max_concurrent=3
    )

asyncio.run(batch_translate())
```

### 示例 4: 自定义配置

```python
import asyncio
from smart_translator import SmartTranslator

async def custom_translate():
    # 使用特定模型和模式
    translator = SmartTranslator(
        model="gpt-4o",
        mode="technical",
        api_key="sk-xxxxx"  # 可选，优先级最高
    )
    
    await translator.translate_document(
        file_path="technical_doc.docx",
        output_path="technical_doc_cn.docx",
        max_concurrent=5
    )

asyncio.run(custom_translate())
```

## 📊 支持的模型

| 提供商 | 模型 | 上下文 | 价格 (元/百万 tokens) | 推荐场景 |
|--------|------|--------|----------------------|----------|
| SiliconFlow | Qwen/Qwen3-8B | 32K | ¥0.01 | 快速翻译 ⭐ |
| SiliconFlow | Qwen/Qwen2.5-72B | 32K | ¥0.04 | 高质量翻译 |
| 阿里云 | qwen-plus | 32K | ¥0.50 | 平衡性能 |
| 阿里云 | qwen3.5-plus | 32K | ¥7.9/月 | 无限次使用 ⭐ |
| OpenAI | gpt-4o | 128K | ¥5.0 | 最高质量 |
| DeepSeek | DeepSeek-V2 | 128K | ¥0.14 | 性价比之王 |

## 🎯 翻译模式说明

| 模式 | 说明 | 适用场景 |
|------|------|----------|
| **strict** | 100% 中文，不允许英文 (除通用缩写) | 正式文档 |
| **technical** | 保留技术品牌名 (React, Vue 等) | 技术文档 ⭐推荐 |
| **fluent** | 优化流畅度，意译为主 | 营销文案 |
| **localized** | 本地化表达，符合中文习惯 | 产品文档 |

## ⚠️ 注意事项

### 1. API Key 安全
- ✅ 使用环境变量存储 API Key
- ✅ 不要将 API Key 提交到版本控制
- ✅ 定期更新 API Key

### 2. 成本估算
- 翻译 1 万字约 ¥0.01-0.10 (取决于模型)
- 建议先测试小文档
- 使用 `get_api_key_info()` 查看配置

### 3. 断点续翻
- 自动保存进度到 `.translation_cache/`
- 中断后重新运行即可继续
- 避免重复翻译节省费用

## 🐛 故障排查

### 问题 1: API Key 未配置

**错误**: `ValueError: API Key 未配置`

**解决**:
```bash
setx SMART_TRANSLATOR_API_KEY "sk-your-api-key-here"
# 重启命令行
```

### 问题 2: 编码错误

**错误**: `UnicodeDecodeError: 'utf-8' codec can't decode bytes`

**解决**:
- 确保文件使用 UTF-8 编码
- Python 脚本开头添加 `# -*- coding: utf-8 -*-`

### 问题 3: 模型不支持

**错误**: `model xxx is not supported`

**解决**:
- 检查 `config.json` 中的模型名称
- 确认 API Key 有权限访问该模型

## 📚 相关文档

- **API_KEY_GUIDE.md** - API Key 配置完全指南
- **CONFIG_GUIDE.md** - 配置完全指南
- **QUICKSTART.md** - 快速开始指南
- **README.md** - 项目介绍

## 🔄 更新日志

### v2.1.0 (2026-03-17)
- ✅ 优化 API Key 配置 (使用 SMART_TRANSLATOR_API_KEY)
- ✅ 支持优先级配置策略
- ✅ 新增 API Key 验证方法
- ✅ 新增配置信息查询方法
- ✅ 增强错误提示信息

### v2.0.0 (2026-03-17)
- ✅ 代码块验证和清理
- ✅ 错误重试机制
- ✅ 智能分批策略
- ✅ 详细错误报告
- ✅ UTF-8 编码强制

### v1.0.0 (2026-03-16)
- 初始版本

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 仓库
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 📞 联系方式

- **GitHub**: https://github.com/hotice888/smart-translator
- **Email**: hotice888@users.noreply.github.com

---

**维护者**: hotice888  
**最后更新**: 2026-03-17  
**版本**: 2.1.0
