# Smart Translator (智能翻译官)

基于大模型的智能翻译技能，支持多种文档格式翻译，具备智能分批、断点续翻、成本估算等功能。

## ✨ 特性

- 🚀 **智能分批**：根据模型上下文自动分批，支持超长文档
- 💾 **断点续翻**：自动保存进度，中断后可继续
- 📄 **多格式支持**：Word、PDF、Markdown、TXT、网页
- 💰 **成本透明**：自动估算翻译成本
- ⚡ **并发翻译**：多线程并发，提升效率
- 🌍 **多语言**：支持 50+ 语言互译
- 🎯 **多模式**：strict、technical、fluent、localized

## 📦 安装

### 1. 安装依赖
```bash
pip install python-docx pdfplumber reportlab aiohttp
```

### 2. 配置 API Key
```bash
# 阿里云百炼
export DASHSCOPE_API_KEY="sk-xxxxx"

# Windows PowerShell
$env:DASHSCOPE_API_KEY="sk-xxxxx"
```

## 🚀 快速开始

### 翻译单个文件
```bash
python smart_translator.py document.docx -o document_zh.docx
```

### 批量翻译目录
```bash
python smart_translator.py ./docs/ --batch -o ./docs_zh/
```

### 翻译网页
```bash
python smart_translator.py --url https://example.com/article
```

### 选择不同模型
```bash
# 使用 GPT-4o（质量最佳）
python smart_translator.py input.docx -m gpt-4o

# 使用 Claude-3.5（长文档）
python smart_translator.py input.docx -m claude-3.5-sonnet
```

### 选择翻译模式
```bash
# 严格模式（100% 中文）
python smart_translator.py input.docx --mode strict

# 技术模式（保留术语）
python smart_translator.py input.docx --mode technical

# 流畅模式（优化可读性）
python smart_translator.py input.docx --mode fluent
```

## 📊 性能指标

| 文档长度 | 模型 | 预计时间 | 估算成本 |
|---------|------|---------|---------|
| 5,000 字 | qwen-turbo | < 30 秒 | ¥0.01 |
| 50,000 字 | qwen-plus | 3-5 分钟 | ¥0.50 |
| 100,000 字 | qwen-max | 8-10 分钟 | ¥2.00 |

## ⚙️ 配置选项

在 `smart_translator.py` 中可配置：

```python
translator = SmartTranslator(
    model="qwen-plus",      # 选择模型
    mode="technical",       # 翻译模式
    api_key="sk-xxxxx"      # API Key（或环境变量）
)
```

### 翻译模式

- **strict**: 100% 中文输出，保留通用缩写
- **technical**: 保留技术术语和品牌名
- **fluent**: 优化流畅度和可读性
- **localized**: 本地化表达

### 支持模型

| 模型 | 上下文 | 适用场景 | 价格 |
|------|--------|---------|------|
| qwen-turbo | 32K | 短文本、快速翻译 | ¥ |
| qwen-plus | 32K | 平衡性能 | ¥¥ |
| qwen-max | 32K | 高质量翻译 | ¥¥¥ |
| gpt-4o | 128K | 最佳质量 | ¥¥¥ |
| claude-3.5 | 200K | 超长文档 | ¥¥¥¥ |

## 📝 使用示例

### Python API 调用
```python
from smart_translator import SmartTranslator
import asyncio

async def main():
    translator = SmartTranslator(model="qwen-plus", mode="technical")
    
    # 翻译单个文档
    result = await translator.translate_document("input.docx")
    print(f"输出：{result}")
    
    # 批量翻译
    await translator.translate_batch_files("./docs/", output_dir="./docs_zh/")

asyncio.run(main())
```

### 断点续翻
```bash
# 第一次翻译（中断）
python smart_translator.py large_book.docx

# 继续翻译（自动从断点开始）
python smart_translator.py large_book.docx
```

## 🛠️ 技术实现

- **智能分批**：按语义和章节分割，保持上下文完整
- **进度管理**：JSON 检查点文件，支持断点续翻
- **并发控制**：asyncio + Semaphore，可配置并发数
- **成本估算**：基于 Token 数量实时计算

## ⚠️ 注意事项

1. **API Key**: 需要配置大模型 API Key
2. **专业文档**: 建议人工校对
3. **扫描版 PDF**: 需要 OCR 预处理
4. **动态网页**: JavaScript 内容无法提取

## 📄 许可证

MIT License

## 🔗 相关链接

- GitHub: https://github.com/hotice888/smart-translator
- 问题反馈：https://github.com/hotice888/smart-translator/issues
- 阿里云百炼：https://bailian.console.aliyun.com/

## 🙏 致谢

感谢以下大模型提供商：
- 阿里云百炼（Qwen 系列）
- SiliconFlow
- OpenAI（GPT-4o）
- Anthropic（Claude）
