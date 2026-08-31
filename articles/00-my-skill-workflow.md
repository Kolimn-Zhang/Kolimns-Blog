---
title: 我的 Skill 工作流
date: 2026-08-31
category: skills
subcategory: 总览
summary: 梳理我注册的全部 17 个 skill 的分工与协作关系——skills-gateway 统一调度、superpowers 定计划、ui 设计前端、code-simplifier 简化代码、obsidian 存记忆，配一张可交互架构图。
---

# 我的 Skill 工作流

## 一句话看懂

这些 skill 不是一个个孤立用的，而是组成一条流水线。我只需要记住一个入口 `@gateway`，剩下的由它们自动分工协作。

## 完整架构图

<iframe src="/static/diagrams/skill-workflow.html" width="100%" height="640" style="border:1px solid var(--color-border);border-radius:12px;background:var(--color-card);"></iframe>

> 图为可交互 HTML，支持缩放、拖拽、明暗主题切换。点击节点或连线可高亮查看关系。

## 全部 skill 的分工（共 17 个）

我把注册的全部 skill 分成 6 类，每一类各司其职：

### 1. 总调度 —— skills-gateway（1 个）

这是大脑，所有 skill 都注册在它那里。我只要说 `@gateway 用 xx skill 实现 xx`，它就知道该派谁干活。它还能安装新 skill、删除/校正、给所有 skill 批量做统一操作。

### 2. Skill 制造（3 个）

负责"造出新 skill"，是流水线的上游：

| skill | 作用 |
|-------|------|
| `repo-to-skill` | 把一个 GitHub 仓库自动封装成 skill |
| `skill-creator` | 从零创建 / 更新 skill 的官方指南 |
| `find-skills` | 搜索、发现、安装现成的 skill |

### 3. 核心工作流（3 个）

承接开发任务的核心三件套：

| skill | 作用 |
|-------|------|
| `superpowers` | 先规划再动手，TDD 写代码 |
| `ui-ux-pro-max` | 设计前端界面 |
| `code-simplifier` | 简化、重构代码 |

### 4. 工具（2 个）

| skill | 作用 |
|-------|------|
| `archify` | 画架构图、流程图 |
| `git-manager` | 生成 git / GitHub 命令 |

### 5. 通用执行（7 个）

具体干活的"叶子"技能：

| skill | 作用 |
|-------|------|
| `docx` / `pdf` / `xlsx` / `pptx` | 处理 Word、PDF、表格、PPT |
| `agent-browser` | 浏览器自动化（打开网页、截图、点击） |
| `playwright-cli` | 浏览器测试、抓取 |
| `多模态内容生成` | 生成图片、视频、3D |

### 6. 记忆（1 个）

| skill | 作用 |
|-------|------|
| `memory-for-ai` | 存对话与经验，其他 skill 执行前可查 |

## 核心逻辑：记忆贯穿一切

这套体系最特别的一点，是 `memory-for-ai` **贯穿所有环节**：

- 任何 skill 干活时产生的对话、经验、结论，都可以存进记忆库。
- **别的 skill 下次执行命令前，可以先查记忆库**，看有没有相关历史经验，避免重复踩坑。
- 这样整个体系会"越用越聪明"，而不是每次从零开始。

## 一个完整例子串起来

假设我说："帮我做一个带登录页的个人网站"：

1. **`@gateway` 入口** → skills-gateway 接到，判断这是开发任务
2. **制定计划** → 交给 superpowers，先规划要做什么、拆成小任务
3. **设计界面** → 交给 ui-ux-pro-max，给出配色、字体、布局
4. **写代码** → 写完后交给 code-simplifier 简化、优化
5. **画架构图** → 需要画图时交给 archify
6. **全程记忆** → memory-for-ai 把设计决策、踩的坑存起来

下次再做类似的网站，相关 skill 会**先查记忆库**，直接复用上次经验。

## 核心逻辑总结

| 环节 | 负责的 skill | 作用 |
|------|-------------|------|
| 入口/调度 | skills-gateway | 统一接收、派活 |
| 制造 | repo-to-skill / skill-creator / find-skills | 造出更多 skill |
| 计划 | superpowers | 先想清楚再动手 |
| 设计 | ui-ux-pro-max | 界面与视觉 |
| 简化 | code-simplifier | 代码更干净 |
| 工具 | archify / git-manager | 画图、管版本 |
| 执行 | docx/pdf/xlsx/pptx/浏览器/多模态 | 具体干活 |
| 记忆 | memory-for-ai | 沉淀经验、供复用 |

一句话：**gateway 是入口，superpowers 定方向，ui 管好看，simplifier 管代码质量，obsidian 管记忆，让整个体系越用越聪明。**
