---
title: skills-gateway — 技能网关 Skill
date: 2026-08-30
category: skills
subcategory: 总调度
summary: 一个技能网关，用 @gateway 统一入口调用、安装、管理所有 skill，不用记每个 skill 的具体命令。
---

# skills-gateway

## 解决什么问题

这是一个**管理所有 skill 的网关**。你装了一堆 skill（做 PPT 的、处理 PDF 的、画 UI 的……），每个都有不同的触发词和用法，记起来很麻烦。这个网关就是它们的统一入口：

- **想调用某个 skill** → 不用记它的命令，统一说 `@gateway 用 xx skill 实现 xx` 就行
- **想安装新 skill** → `@gateway 安装 <链接>`，它自动下载、注册
- **想删掉/改某个 skill** → `@gateway 删除/校正 xx`，它帮你改注册表
- **想给所有 skill 统一做一件事** → `@gateway 同步 xx`，它批量执行

一句话：你只需要记住 `@gateway` 这一个入口，剩下的交给它。

## 工作流程

它收到你的话后，先判断你想干嘛，分成四类处理：

**1. 调用**：你说"用 xx skill 实现 xx"，它去注册表里匹配是哪个 skill，然后把任务转交给它。

**2. 安装**：你给一个链接，它 clone 下来、放到 skills 目录、注册进注册表。如果这个仓库不是标准 skill（没有 SKILL.md），它还会自动先调用 repo-to-skill 帮你封装。

**3. 管理**：增删改查注册表。比如"校正 ui 的别名为 xxx"、"卸载某个 skill"（连本地文件一起删）。

**4. 同步**：对指定的或全部 skill 批量执行操作，比如给所有 skill 的 SKILL.md 追加一行约定，而且都能撤销还原。

## 使用示例

**例子：调用技能**

```
@gateway 用 pdf skill 实现 合并这两个 PDF
@gateway 用 ui skill 实现 设计一个首页
```

**例子：安装技能**

```
@gateway 安装 https://github.com/xxx/yyy
```

**例子：管理**

```
@gateway 列出已注册技能
@gateway 校正 ui-ux-pro-max 的别名为 ui
```

## 安装

https://github.com/Kolimn-Zhang/Skills-Gateway
