# Knowledge Base Templates (知识库模板库)

Loaded by `deep-reading` SKILL.md when creating or updating **author pages**, **technical concept pages**, and **domain MOCs**. Select the template matching (1) the page type and (2) the user's request language.

⚠️ The update PROTOCOL — always READ the existing file first, then APPEND/MERGE, NEVER OVERWRITE — lives in SKILL.md ("Obsidian Export & Knowledge Base Update Protocol") and applies to every use of these templates.

---

## Author Page Templates

If not exists, create with template in the appropriate language:

### 🇨🇳 中文模板

```markdown
# {Author Name}

> **领域**: {Domain}
> **知名于**: {Key Contribution}
> **机构**: {Institution}

## 简介

...

## 相关著作

### 书籍
- [[{Book Title} - 深度阅读报告|{Book Title}]]

### 演讲/论文
- [[{Title} - 技术阅读报告|{Title}]] ({Year}, {Venue})

## 技术贡献

### 核心方法
- [[{Method A}]]
- [[{Method B}]]

### 研究领域
- [[{Research Area 1}]]
- [[{Research Area 2}]]

## 相关概念

- [[Second Brain/Database/Concepts/{Concept}|{Concept}]]

> 🏷️ 标签: #author #{technical-domain}
> 🔄 *最后更新: {date}*
```

### 🇬🇧 English Template

```markdown
# {Author Name}

> **Domain**: {Domain}
> **Known For**: {Key Contribution}
> **Institution**: {Institution}

## Biography

...

## Related Works

### Books
- [[{Book Title} - Deep Reading Report|{Book Title}]]

### Talks/Papers
- [[{Title} - Technical Reading Report|{Title}]] ({Year}, {Venue})

## Technical Contributions

### Core Methods
- [[{Method A}]]
- [[{Method B}]]

### Research Areas
- [[{Research Area 1}]]
- [[{Research Area 2}]]

## Related Concepts

- [[Second Brain/Database/Concepts/{Concept}|{Concept}]]

> 🏷️ Tags: #author #{technical-domain}
> 🔄 *Last Updated: {date}*
```

---

## Technical Concept Page Templates

### 🇨🇳 中文模板

```markdown
# {Technical Concept}

> **定义**: {Formal Definition}
> **领域**: {Domain}
> **来源**: [[{Source} - 技术阅读报告|{Source}]]

## 核心定义

### 形式化表述
```
数学定义或算法描述
```

### 直观解释
{为什么这个概念重要，它解决了什么问题}

## 技术细节

### 关键性质
- 性质1：...
- 性质2：...

### 算法/实现
```
伪代码或关键实现细节
```

### 复杂度分析
- 时间复杂度：
- 空间复杂度：

## 变体与扩展

| 变体 | 区别 | 适用场景 |
|:---|:---|:---|
| 变体A | ... | ... |

## 相关方法

- [[{Related Method}]]

## 应用实例

- [[{Application Case}]]

## 相关著作

- [[{Source} - 技术阅读报告|{Source}]]

> 🏷️ 标签: #technical-concept #{domain}
> 🔄 *最后更新: {date}*
```

### 🇬🇧 English Template

```markdown
# {Technical Concept}

> **Definition**: {Formal Definition}
> **Domain**: {Domain}
> **Source**: [[{Source} - Technical Reading Report|{Source}]]

## Core Definition

### Formal Statement
```
Mathematical definition or algorithm description
```

### Intuitive Explanation
{Why this concept matters and what problem it solves}

## Technical Details

### Key Properties
- Property 1: ...
- Property 2: ...

### Algorithm/Implementation
```
Pseudocode or key implementation details
```

### Complexity Analysis
- Time complexity:
- Space complexity:

## Variants & Extensions

| Variant | Difference | Applicable Scenario |
|:---|:---|:---|
| Variant A | ... | ... |

## Related Methods

- [[{Related Method}]]

## Application Examples

- [[{Application Case}]]

## Related Works

- [[{Source} - Technical Reading Report|{Source}]]

> 🏷️ Tags: #technical-concept #{domain}
> 🔄 *Last Updated: {date}*
```

---

## Domain MOC Templates

### 🇨🇳 中文模板

```markdown
# {Technical Domain}

> 核心概念、方法、人物、资源的地图

---

## 🎯 核心概念

### 基础概念
- [[{Concept A}]]
- [[{Concept B}]]

### 进阶方法
- [[{Advanced Method}]]

---

## 👤 关键人物

| 人物 | 贡献 | 代表作 |
|:---|:---|:---|
| [[{Author}]] | {Contribution} | [[{Work}]] |

---

## 📚 核心著作与演讲

### 经典论文
- [[{Paper}]]

### 重要演讲
- [[{Talk} - 技术阅读报告|{Talk}]]

---

## 🔧 技术方法图谱

### 参数估计
- [[{Method 1}]]
- [[{Method 2}]]

### 假设检验
- [[{Test 1}]]
- [[{Test 2}]]

---

## 📝 技术笔记

- [[{Technical Note}]]

---

## 🔗 跨领域连接

- [[{Related Domain}]]

> 🏷️ 标签: #moc #{technical-domain}
> 🔄 *最后更新: {date}*
```

### 🇬🇧 English Template

```markdown
# {Technical Domain}

> Map of core concepts, methods, key figures, and resources

---

## 🎯 Core Concepts

### Fundamental Concepts
- [[{Concept A}]]
- [[{Concept B}]]

### Advanced Methods
- [[{Advanced Method}]]

---

## 👤 Key Figures

| Figure | Contribution | Representative Work |
|:---|:---|:---|
| [[{Author}]] | {Contribution} | [[{Work}]] |

---

## 📚 Core Works & Talks

### Classic Papers
- [[{Paper}]]

### Important Talks
- [[{Talk} - Technical Reading Report|{Talk}]]

---

## 🔧 Technical Methods Map

### Parameter Estimation
- [[{Method 1}]]
- [[{Method 2}]]

### Hypothesis Testing
- [[{Test 1}]]
- [[{Test 2}]]

---

## 📝 Technical Notes

- [[{Technical Note}]]

---

## 🔗 Cross-Domain Connections

- [[{Related Domain}]]

> 🏷️ Tags: #moc #{technical-domain}
> 🔄 *Last Updated: {date}*
```
