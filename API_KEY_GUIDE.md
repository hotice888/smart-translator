# Smart Translator API Key 配置指南

**版本**: v2.1  
**更新日期**: 2026-03-17

---

## 🎯 配置策略

Smart Translator v2.1 采用**分层配置策略**，提供灵活的 API Key 管理方式。

### 优先级顺序

```
1. 构造函数参数 (最高优先级)
   ↓
2. 技能专用环境变量 (SMART_TRANSLATOR_API_KEY)
   ↓
3. 配置文件指定的环境变量 (api_key_env)
   ↓
4. 提供商专用环境变量 (SILICONFLOW_API_KEY, DASHSCOPE_API_KEY 等)
```

---

## 🔑 推荐配置方式

### 方式 1: 技能专用环境变量 ⭐ 推荐

**优点**:
- ✅ 统一命名，易于管理
- ✅ 适用于所有提供商
- ✅ 切换提供商无需更改变量名

**设置方法**:

#### Windows
```cmd
setx SMART_TRANSLATOR_API_KEY "sk-your-api-key-here"
```

#### Linux/macOS
```bash
export SMART_TRANSLATOR_API_KEY="sk-your-api-key-here"
```

#### 永久设置 (Linux/macOS)
在 `~/.bashrc` 或 `~/.zshrc` 中添加:
```bash
export SMART_TRANSLATOR_API_KEY="sk-your-api-key-here"
```

---

### 方式 2: 配置文件指定

编辑 `config.json`:
```json
{
  "api_key_env": "YOUR_CUSTOM_ENV_VAR",
  "provider": "siliconflow",
  "model": "Qwen/Qwen3-8B"
}
```

然后设置环境变量:
```bash
export YOUR_CUSTOM_ENV_VAR="sk-your-api-key-here"
```

---

### 方式 3: 提供商专用环境变量

**适用场景**: 同时使用多个提供商，需要隔离配置

#### SiliconFlow
```bash
export SILICONFLOW_API_KEY="sk-sf-xxxxxxxx"
```

#### 阿里云 DashScope
```bash
export DASHSCOPE_API_KEY="sk-ds-xxxxxxxx"
```

#### OpenAI
```bash
export OPENAI_API_KEY="sk-oa-xxxxxxxx"
```

---

## 📋 不同提供商的配置示例

### SiliconFlow (硅基流动)

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
    "price_per_1m_tokens": 0.01
  }
}
```

**API Key 格式**: `sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` (32+ 字符)

**设置命令**:
```bash
setx SMART_TRANSLATOR_API_KEY "sk-gfxyhuxdewmsgcwyualykobblrxefsrmeuqwjfydhqyebfxy"
```

---

### 阿里云 DashScope

```json
{
  "provider": "dashscope",
  "provider_name": "阿里云百炼",
  "api_key_env": "SMART_TRANSLATOR_API_KEY",
  "base_url": "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation",
  "model": "qwen-plus",
  "model_config": {
    "max_tokens": 32000,
    "batch_size": 10000,
    "price_per_1m_tokens": 0.5
  }
}
```

**API Key 格式**: `sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` (32+ 字符)

---

### 阿里云 CodingPlan

```json
{
  "provider": "codingplan",
  "provider_name": "阿里云 CodingPlan",
  "api_key_env": "SMART_TRANSLATOR_API_KEY",
  "base_url": "https://coding.dashscope.aliyuncs.com/v1/chat/completions",
  "model": "qwen3.5-plus",
  "model_config": {
    "max_tokens": 32000,
    "batch_size": 15000,
    "price_per_1m_tokens": 0.0
  }
}
```

**API Key 格式**: `sk-sp-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` (套餐 Key)

---

### OpenAI GPT-4o

```json
{
  "provider": "openai",
  "provider_name": "OpenAI",
  "api_key_env": "SMART_TRANSLATOR_API_KEY",
  "base_url": "https://api.openai.com/v1/chat/completions",
  "model": "gpt-4o",
  "model_config": {
    "max_tokens": 128000,
    "batch_size": 50000,
    "price_per_1m_tokens": 5.0
  }
}
```

**API Key 格式**: `sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` (20+ 字符)

---

## 🔍 验证配置

### 方法 1: 使用 Python 验证

```python
import sys
sys.path.insert(0, r'active_skills/smart-translator')

from smart_translator import SmartTranslator

translator = SmartTranslator()

# 获取配置信息
info = translator.get_api_key_info()
print(f"配置状态：{info['configured']}")
print(f"来源：{info['source']}")
print(f"提供商：{info['provider']}")
print(f"模型：{info['model']}")
print(f"格式有效：{info['valid_format']}")
```

### 方法 2: 检查环境变量

#### Windows
```cmd
echo %SMART_TRANSLATOR_API_KEY%
```

#### Linux/macOS
```bash
echo $SMART_TRANSLATOR_API_KEY
```

### 方法 3: 测试翻译

```python
import asyncio
from smart_translator import SmartTranslator

async def test():
    translator = SmartTranslator()
    
    # 验证 API Key
    if not translator.validate_api_key():
        print("API Key 无效或未配置")
        return
    
    # 测试翻译
    result = await translator.call_llm("Translate: Hello World")
    print(result)

asyncio.run(test())
```

---

## ❌ 常见错误

### 错误 1: API Key 未配置

```
ValueError: API Key 未配置！请通过以下方式之一设置：
  1. 技能专用：SMART_TRANSLATOR_API_KEY
  2. 配置文件指定：SMART_TRANSLATOR_API_KEY
  3. 提供商专用：SILICONFLOW_API_KEY
```

**解决方法**:
```bash
setx SMART_TRANSLATOR_API_KEY "sk-your-api-key-here"
# 重启命令行
```

### 错误 2: API Key 格式无效

```
API Key 格式检查失败
```

**原因**:
- Key 长度不足
- Key 前缀不正确
- Key 包含空格或特殊字符

**解决方法**:
```bash
# 检查 Key 是否正确复制
echo %SMART_TRANSLATOR_API_KEY%
# 确保没有多余空格
setx SMART_TRANSLATOR_API_KEY "sk-xxxxxxxx"
```

### 错误 3: 环境变量未生效

**原因**:
- 设置后未重启命令行
- 多个环境变量冲突
- 配置文件优先级问题

**解决方法**:
1. 重启命令行或 IDE
2. 检查所有相关环境变量
3. 使用 `get_api_key_info()` 查看实际使用的来源

---

## 🎯 最佳实践

### 1. 使用技能专用变量名

```bash
# ✅ 推荐
export SMART_TRANSLATOR_API_KEY="sk-xxxxx"

# ❌ 不推荐 (仅限特定提供商)
export SILICONFLOW_API_KEY="sk-xxxxx"
```

### 2. 不要硬编码 API Key

```python
# ✅ 推荐 - 从环境变量读取
translator = SmartTranslator()

# ❌ 不推荐 - 硬编码
translator = SmartTranslator(api_key="sk-xxxxx")
```

### 3. 使用配置文件管理多提供商

创建多个配置文件:

**config.siliconflow.json**:
```json
{
  "provider": "siliconflow",
  "model": "Qwen/Qwen3-8B"
}
```

**config.openai.json**:
```json
{
  "provider": "openai",
  "model": "gpt-4o"
}
```

切换时复制为 `config.json`。

### 4. 定期验证 API Key

```python
# 定期检查 API Key 状态
translator = SmartTranslator()
info = translator.get_api_key_info()

if not info['valid_format']:
    print("警告：API Key 格式可能无效")
```

### 5. 安全存储 API Key

- ✅ 使用环境变量
- ✅ 使用密钥管理服务 (如 Azure Key Vault, AWS Secrets Manager)
- ✅ 使用 `.env` 文件 (不提交到 Git)
- ❌ 不要硬编码到代码中
- ❌ 不要提交到版本控制

---

## 📊 配置对比

| 配置方式 | 优点 | 缺点 | 推荐场景 |
|----------|------|------|----------|
| **SMART_TRANSLATOR_API_KEY** | 统一命名，易于管理 | 需要设置新变量 | ⭐ 所有场景 |
| **提供商专用变量** | 隔离不同提供商 | 切换需更改变量 | 多提供商并行 |
| **配置文件指定** | 灵活定制 | 配置复杂 | 高级用户 |
| **构造函数参数** | 最高优先级 | 每次都要传递 | 测试/临时使用 |

---

## 🔄 迁移指南

### 从旧版本迁移

**如果你之前使用 `SILICONFLOW_API_KEY`**:

1. **保留旧配置** (向后兼容):
   ```bash
   # 旧配置仍然有效
   export SILICONFLOW_API_KEY="sk-xxxxx"
   ```

2. **推荐迁移到新配置**:
   ```bash
   # 设置新变量
   setx SMART_TRANSLATOR_API_KEY "sk-xxxxx"
   
   # 验证
   python -c "from smart_translator import SmartTranslator; print(SmartTranslator().get_api_key_info())"
   ```

3. **删除旧变量** (可选):
   ```bash
   # Windows (需要注册表编辑器)
   # Linux/macOS
   unset SILICONFLOW_API_KEY
   ```

---

## 📞 故障排查

### 问题 1: 配置不生效

**检查步骤**:
1. 验证环境变量已设置
2. 重启命令行/IDE
3. 检查配置文件路径
4. 使用 `get_api_key_info()` 查看实际配置

### 问题 2: 多个环境变量冲突

**解决方法**:
```python
# 查看实际使用的来源
translator = SmartTranslator()
info = translator.get_api_key_info()
print(f"API Key 来源：{info['source']}")
```

### 问题 3: 切换提供商后配置错误

**解决方法**:
1. 更新 `config.json` 中的 `provider` 和 `base_url`
2. 设置新的 API Key
3. 验证配置

---

## 📚 相关文档

- **SKILL.md**: 技能功能说明
- **CONFIG_GUIDE.md**: 配置完全指南
- **QUICKSTART.md**: 快速开始指南
- **README.md**: 项目介绍

---

**最后更新**: 2026-03-17  
**版本**: v2.1  
**维护者**: Smart Translator Team
