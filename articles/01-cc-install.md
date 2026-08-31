---
title: Claude Code 安装与配置
date: 2026-05-11
category: claude-code
summary: Claude Code 的安装步骤以及通过 CC Switch 配置 OpenRouter 的详细教程。
---

## 一、Claude Code 安装

### 1. VS Code 扩展安装

```bash
code --install-extension anthropic.claude-code
```

要求 VS Code 版本 ≥ 1.98.0。安装后按 `Ctrl+Shift+P`，输入 **"Claude Code: Open"** 启动。

### 2. JetBrains IDE 插件安装
**先连接VPN**（参见：[Linux 下 Mihomo 代理配置](/article/07-mihomo-setup)）
$env:HTTP_PROXY="http://127.0.0.1:7897"
$env:HTTPS_PROXY="http://127.0.0.1:7897"

**前置：安装 Claude Code CLI**

```bash
# macOS / Linux / WSL
curl -fsSL https://claude.ai/install.sh | bash

# Windows PowerShell
irm https://claude.ai/install.ps1 | iex
```

安装后配置 PATH：

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
claude --version
```

---

## 二、CC Switch 配置 OpenRouter

> 💡 OpenRouter 充值策略与更多 API 平台对比，见：[AI API 平台性价比推荐](/article/04-coding-plan-recommend)

- CC Switch 是开源桌面工具，用于在 Claude Code 中一键切换 API 供应商（OpenRouter、DeepSeek 等），免去手动修改配置。
- - OpenRouter 是一个LLM 统一 API 聚合平台，用一个兼容 OpenAI 的接口，即可调用全球 60 + 厂商、400 + 大模型。充值10元即可调用免费模型。

### 1. 安装 CC Switch

从 [GitHub Releases](https://github.com/farion1231/cc-switch/releases) 下载，Windows 选 `.msi`，Mac 选 `.dmg`。

### 2. 获取 OpenRouter API Key

1. 注册 [openrouter.ai](https://openrouter.ai)（支持邮箱/GitHub/Google 登录）
2. 右上角头像 → **Keys** → **Create New Key**
3. 复制 API Key（格式：`sk-or-v1-xxxxxxxx`）
4. 如需付费模型，在 **Billing** 中可用支付宝充值（最低 $10）

### 3. 配置 CC Switch

1. 启动 CC Switch，点击右上角 **"+"** → **Add Provider**
2. **Preset** 下拉选择 **OpenRouter**（自动填充请求地址和官网链接）
3. 填入 OpenRouter API Key
4. 展开高级选项 → 模型映射，将 Haiku / Sonnet / Opus 设为目标模型
5. 点击 **添加** → 在供应商列表找到 OpenRouter 卡片，点击 **启用**
6. 终端运行 `claude`，输入简单问题测试是否正常

### 4. 推荐免费模型

| 模型 | 特点 |
|------|------|
| `inclusionai/ling-2.6-1t:free` | 262K 上下文，免费 |
| `qwen/qwen3.6-plus:free` | 通义千问，免费 |
| `nvidia/nemotron-3-super:free` | 超长上下文推理，免费 |

更多免费模型：[openrouter.ai/models?q=free](https://openrouter.ai/models?fmt=cards&q=free)

![示例图片](../pic/1.png)
