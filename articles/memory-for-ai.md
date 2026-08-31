---
title: memory-for-ai — AI 持久记忆协议
date: 2026-08-30
category: skills
subcategory: 记忆
summary: 一套给 AI 建立长期记忆的协议和工具，用纯 Markdown 文件存记忆，跨工具共享、可审计、可迁移。
---

# memory-for-ai

## 解决什么问题

这是一个**给 AI 存记忆的 skill**。你有没有遇到过：每次换一个 AI 工具，或者开一个新对话，之前告诉过它的事情（你是谁、喜欢什么风格、项目背景）全都忘了，得重新说一遍。

这个 skill 就是解决这个问题的。它把记忆存成**普通的 Markdown 文件**，放在一个文件夹里，这样：

- **任何 AI 工具都能读**，换工具不丢记忆
- **人能直接看、能改**，不是黑盒
- **能用 Git 追踪**，每次改动都有记录，能回看
- **能复制、能迁移**，一个文件夹拷走就行

## 工作流程

它用"一个事实一个文件"的方式存记忆：

**1. 先建一个记忆库**：复制模板文件夹，就得到一个空的记忆库。

**2. 往里记事实**：每条事实存一个文件，比如"张三的职业是开发者"就存在 `张三/职业.md` 里。多条一起记用事务，保证不会记一半出错。

**3. 想查就查**：有专门的查询命令，可以查某个人/某件事的所有记录，也能全文搜索。

**4. 定期校验**：有 lint 命令检查记忆库格式对不对，不对会报出来。

## 使用示例

**例子：记一条事实**

```bash
python3 tools/transact.py begin --idempotency-key "add-zhangsan" --agent me
python3 tools/transact.py add --txn-id <id> --op create_fact --entity 张三 --predicate 职业 --value "开发者"
python3 tools/transact.py commit --txn-id <id> --yes
```

**例子：查询记忆**

```bash
tools/query.sh facts --entity 张三      # 查张三的所有记录
tools/query.sh search "开发者"          # 搜包含"开发者"的内容
```

## 安装

https://github.com/Kolimn-Zhang/memory-for-ai
