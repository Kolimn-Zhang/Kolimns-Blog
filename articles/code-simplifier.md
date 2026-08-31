---
title: code-simplifier — 代码简化与重构 Skill
date: 2026-08-30
category: skills
subcategory: 通用技能
summary: 一个代码简化与重构 skill，把冗长难懂的代码改得更短、更清晰、更好维护。
---

# code-simplifier

## 解决什么问题

这是一个**帮你简化代码的 skill**。写代码时间长了，经常会出现这样的问题：代码越写越长、重复的东西一大堆、一个函数塞了几十行、读起来费劲，想改又怕改坏。

这个 skill 解决的就是这个问题。你跟它说"简化这段代码"或"重构这个函数"，它会把代码改得更短、更清晰、更好维护，同时**保证行为不变**（该干嘛还干嘛，只是写得更干净）。

## 工作流程

它的用法很直接：

**1. 你把代码发给它**，说清楚要简化还是重构。

**2. 它分析代码**，找出冗余、重复、过长的地方，套用标准的重构方法（比如用列表推导式代替循环、提取重复代码成函数、拆解长函数）。

**3. 它输出改好的代码**，并说明改了哪里、为什么这么改更好。

它内置了最佳实践、重构模式、常见问题排查这几份参考文档，遇到典型问题有据可依。

## 使用示例

**例子：简化一段代码**

输入：

```python
def f(a):
    result = []
    for i in range(len(a)):
        result.append(a[i] * 2)
    return result
```

它改成：

```python
def f(a):
    return [x * 2 for x in a]
```

## 安装

https://api.skillhub.cn/clawhub_aqbjqtd/code-simplifier
