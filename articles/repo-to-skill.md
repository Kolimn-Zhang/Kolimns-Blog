---
title: repo-to-skill — 把 GitHub 仓库转成 Skill
date: 2026-08-30
category: skills
subcategory: Skill 制造
summary: 把一个 GitHub 开源仓库自动转换成一个测试过、可用的 skill，解决"AI 不会用开源工具"的问题。
---

# repo-to-skill

## 解决什么问题

这是一个**把 GitHub 仓库变成 skill 的 skill**。GitHub 上有海量好用的开源工具，但 AI 大多不知道它们怎么用，你让 AI 用某个工具，它经常瞎猜、用错命令。

这个 skill 解决的就是这个问题。你给它一个仓库地址，它会去读这个仓库的代码、文档、示例，搞清楚这个工具到底怎么用，然后生成一个 AI 能直接加载的 skill，还帮你测试过、评估过。

## 工作流程

它分六步，全自动：

**1. 分析**：读仓库的 README、文档、示例、命令行帮助。

**2. 分类**：判断这是个命令行工具、代码库、框架还是服务。

**3. 生成**：产出 SKILL.md + 参考文档 + 脚本。

**4. 测试**：真的把这个工具装起来跑一遍，确认能用。

**5. 校验**：检查生成的结构合不合格（篇幅、格式、有没有泄露密钥）。

**6. 评估**：用几个真实问题，对比"有 skill"和"没 skill"的 AI 表现，证明它确实有用。

## 使用示例

```
@gateway 用 repo-to-skill skill 实现 把 https://github.com/xxx/yyy 做成 skill
```

它会自动完成上面的六步，最后给你一个测试过的 skill，和一个"用它比不用强多少"的评估报告。

## 安装

https://github.com/shuyhere/repo-to-skill
