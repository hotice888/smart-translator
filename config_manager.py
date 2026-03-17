#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Smart Translator 配置管理工具
用法：python config_manager.py [command] [options]
"""

import json
import sys
import os
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "config.json"

# 预设配置模板
PRESETS = {
    "siliconflow": {
        "provider": "siliconflow",
        "provider_name": "硅基流动",
        "api_key_env": "SILICONFLOW_API_KEY",
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
    },
    "dashscope": {
        "provider": "dashscope",
        "provider_name": "阿里云百炼",
        "api_key_env": "DASHSCOPE_API_KEY",
        "base_url": "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation",
        "model": "qwen-plus",
        "model_config": {
            "max_tokens": 32000,
            "batch_size": 10000,
            "temperature": 0.3,
            "price_per_1m_tokens": 0.5
        },
        "translation_mode": "technical",
        "language": "zh-CN"
    },
    "codingplan": {
        "provider": "codingplan",
        "provider_name": "阿里云 CodingPlan",
        "api_key_env": "OPENAI_API_KEY",
        "base_url": "https://coding.dashscope.aliyuncs.com/v1/chat/completions",
        "model": "qwen3.5-plus",
        "model_config": {
            "max_tokens": 32000,
            "batch_size": 15000,
            "temperature": 0.3,
            "price_per_1m_tokens": 0.0
        },
        "translation_mode": "technical",
        "language": "zh-CN"
    },
    "openai": {
        "provider": "openai",
        "provider_name": "OpenAI",
        "api_key_env": "OPENAI_API_KEY",
        "base_url": "https://api.openai.com/v1/chat/completions",
        "model": "gpt-4o",
        "model_config": {
            "max_tokens": 128000,
            "batch_size": 50000,
            "temperature": 0.3,
            "price_per_1m_tokens": 5.0
        },
        "translation_mode": "technical",
        "language": "zh-CN"
    }
}

def show_config():
    """显示当前配置"""
    if not CONFIG_PATH.exists():
        print("Error: config.json not found")
        return
    
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    print("\n" + "=" * 60)
    print("Smart Translator Configuration")
    print("=" * 60)
    print(f"Provider: {config.get('provider_name', 'Unknown')}")
    print(f"Model: {config.get('model', 'Unknown')}")
    print(f"Base URL: {config.get('base_url', 'Unknown')}")
    print(f"API Key Env: {config.get('api_key_env', 'Unknown')}")
    print(f"Translation Mode: {config.get('translation_mode', 'technical')}")
    print(f"Max Tokens: {config.get('model_config', {}).get('max_tokens', 'Unknown')}")
    print(f"Batch Size: {config.get('model_config', {}).get('batch_size', 'Unknown')}")
    print(f"Price: RMB {config.get('model_config', {}).get('price_per_1m_tokens', 0)}/1M tokens")
    print("=" * 60 + "\n")

def set_preset(preset_name):
    """设置预设配置"""
    if preset_name not in PRESETS:
        print(f"Error: Unknown preset '{preset_name}'")
        print(f"Available: {', '.join(PRESETS.keys())}")
        return
    
    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        json.dump(PRESETS[preset_name], f, indent=2, ensure_ascii=False)
    
    print(f"OK: Switched to {preset_name} preset")
    show_config()

def set_model(model_name):
    """设置模型"""
    if not CONFIG_PATH.exists():
        print("Error: config.json not found")
        return
    
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    config['model'] = model_name
    
    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    
    print(f"OK: Model set to '{model_name}'")

def set_api_key(api_key):
    """设置 API Key 到环境变量"""
    if not CONFIG_PATH.exists():
        print("Error: config.json not found")
        return
    
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    env_var = config.get('api_key_env', 'SILICONFLOW_API_KEY')
    os.environ[env_var] = api_key
    
    print(f"OK: API Key set to environment variable '{env_var}'")
    print("Note: This is temporary. For permanent setup, use: setx {env_var} \"your-key\"")

def list_presets():
    """列出所有预设"""
    print("\nAvailable Presets:")
    print("-" * 40)
    for name, config in PRESETS.items():
        print(f"  {name:15} - {config['provider_name']:15} ({config['model']})")
    print("-" * 40)
    print("\nUsage: python config_manager.py preset <name>")

def main():
    if len(sys.argv) < 2:
        show_config()
        return
    
    command = sys.argv[1]
    
    if command == "show":
        show_config()
    elif command == "preset":
        if len(sys.argv) < 3:
            list_presets()
        else:
            set_preset(sys.argv[2])
    elif command == "model":
        if len(sys.argv) < 3:
            print("Usage: python config_manager.py model <model_name>")
        else:
            set_model(sys.argv[2])
    elif command == "apikey":
        if len(sys.argv) < 3:
            print("Usage: python config_manager.py apikey <your_api_key>")
        else:
            set_api_key(sys.argv[2])
    elif command == "list":
        list_presets()
    else:
        print(f"Unknown command: {command}")
        print("Commands: show, preset, model, apikey, list")

if __name__ == '__main__':
    main()
