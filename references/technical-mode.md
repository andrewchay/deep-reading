# Technical Mode Reference (技术阅读模式)

Loaded by `deep-reading` SKILL.md for **Mode 2 — Technical Reading** (academic papers, lecture slides, technical documentation, research talks, arXiv papers). Do not load for general non-fiction or fiction.

Contents: Format B main-report template, technical module template, 6-phase workflow, WikiLink creation rules, link validation checklist, worked example.

---

## Format B: Technical Reading Report (Modular)

Use for: Academic papers, lecture slides, technical documentation, research talks

### B1. Main Report Structure

#### 🇨🇳 中文模板

```markdown
# 《标题》技术阅读报告

> **类型**: 学术演讲/论文/技术文档  
> **作者**:  
> **时间/场合**:  
> **领域**:  

## 一、概览与定位
- **核心主题**：
- **技术背景**：
- **目标受众**：
- **与作者其他工作的关系**：

## 二、核心贡献（3–5条）
（每条使用「贡献 + 技术意义」结构）

## 三、关键技术点
| 技术点 | 详细说明 | 链接 |
|:---|:---|:---|
| 方法A | 简要描述 | [[技术模块A\|详细笔记]] |
| 方法B | 简要描述 | [[技术模块B\|详细笔记]] |
| 定理/结果 | 简要描述 | [[技术模块C\|详细笔记]] |

## 四、技术细节模块索引
- 📁 [[技术模块-方法论\|方法论详解]]
- 📁 [[技术模块-算法实现\|算法与实现]]
- 📁 [[技术模块-数学推导\|数学推导]]
- 📁 [[技术模块-应用案例\|应用与案例]]
- 📁 [[技术模块-相关文献\|文献与扩展]]

## 五、批判性评估
- **创新点**：
- **局限性**：
- **未解决问题**：
- **后续影响**：

## 六、与其他工作的联系
- **前置基础**：
- **后续发展**：
- **相关技术**：

## 七、个人笔记与思考
（研究想法、疑问、潜在应用）

## 八、一句话总结

## 九、延伸阅读
```

#### 🇬🇧 English Template

```markdown
# {Title} - Technical Reading Report

> **Type**: Academic Talk/Paper/Technical Documentation  
> **Author**:  
> **Date/Venue**:  
> **Domain**:  

## 1. Overview & Positioning
- **Core Topic:**
- **Technical Background:**
- **Target Audience:**
- **Relation to Author's Other Work:**

## 2. Core Contributions (3-5 items)
(Use "Contribution + Technical Significance" structure for each)

## 3. Key Technical Points
| Technical Point | Description | Link |
|:---|:---|:---|
| Method A | Brief description | [[Technical Module A\|Detailed Notes]] |
| Method B | Brief description | [[Technical Module B\|Detailed Notes]] |
| Theorem/Result | Brief description | [[Technical Module C\|Detailed Notes]] |

## 4. Technical Module Index
- 📁 [[Technical Module-Methodology\|Methodology Details]]
- 📁 [[Technical Module-Algorithms\|Algorithms & Implementation]]
- 📁 [[Technical Module-Derivations\|Mathematical Derivations]]
- 📁 [[Technical Module-Applications\|Applications & Cases]]
- 📁 [[Technical Module-References\|References & Extensions]]

## 5. Critical Assessment
- **Innovations:**
- **Limitations:**
- **Unresolved Issues:**
- **Future Impact:**

## 6. Connections to Other Work
- **Foundational Prerequisites:**
- **Subsequent Developments:**
- **Related Techniques:**

## 7. Personal Notes & Reflections
(Research ideas, questions, potential applications)

## 8. One-Sentence Summary

## 9. Extended Reading
```

### B2. Technical Module Template

Each technical module is a separate markdown file. Templates provided in multiple languages:

#### 🇨🇳 中文模板

```markdown
# {主标题} - {模块名}

> **来源**: [[主报告链接\|主报告]]  
> **主题**: {具体技术主题}  
> **相关概念**: [[概念A]], [[概念B]]

---

## 1. 问题设定

### 1.1 背景
{技术背景描述}

### 1.2 形式化定义
```
数学定义、符号说明
```

---

## 2. 核心方法

### 2.1 算法/定理陈述
```
算法伪代码或定理精确表述
```

### 2.2 直观解释
{为什么这个方法有效}

### 2.3 关键假设
- 假设1：...
- 假设2：...

---

## 3. 技术细节

### 3.1 推导过程
```
关键数学推导步骤
```

### 3.2 实现要点
- 数值稳定性：
- 计算复杂度：
- 参数选择：

### 3.3 变体与扩展
| 变体 | 区别 | 适用场景 |
|:---|:---|:---|
| 变体A | ... | ... |
| 变体B | ... | ... |

---

## 4. 与其他模块的联系
- 上游依赖：[[模块X]]
- 下游应用：[[模块Y]]
- 平行概念：[[模块Z]]

---

## 5. 个人注释

### 5.1 关键洞察
{自己的理解}

### 5.2 疑问
{尚未理解的部分}

### 5.3 潜在应用
{研究想法}

---

🏷️ 标签: #technical-note #{domain} #{sub-topic}
🔄 *最后更新: {date}*
```

#### 🇬🇧 English Template

```markdown
# {Main Title} - {Module Name}

> **Source**: [[Main Report Link\|Main Report]]  
> **Topic**: {Specific Technical Topic}  
> **Related Concepts**: [[Concept A]], [[Concept B]]

---

## 1. Problem Formulation

### 1.1 Background
{Technical background description}

### 1.2 Formal Definition
```
Mathematical definitions, notation
```

---

## 2. Core Method

### 2.1 Algorithm/Theorem Statement
```
Algorithm pseudocode or precise theorem statement
```

### 2.2 Intuitive Explanation
{Why this method works}

### 2.3 Key Assumptions
- Assumption 1: ...
- Assumption 2: ...

---

## 3. Technical Details

### 3.1 Derivation Process
```
Key mathematical derivation steps
```

### 3.2 Implementation Notes
- Numerical stability:
- Computational complexity:
- Parameter selection:

### 3.3 Variants & Extensions
| Variant | Difference | Applicable Scenario |
|:---|:---|:---|
| Variant A | ... | ... |
| Variant B | ... | ... |

---

## 4. Connections to Other Modules
- Upstream Dependencies: [[Module X]]
- Downstream Applications: [[Module Y]]
- Parallel Concepts: [[Module Z]]

---

## 5. Personal Annotations

### 5.1 Key Insights
{Your understanding}

### 5.2 Questions
{Parts not yet understood}

### 5.3 Potential Applications
{Research ideas}

---

🏷️ Tags: #technical-note #{domain} #{sub-topic}
🔄 *Last Updated: {date}*
```

---

## Technical Reading Workflow

⚠️ **CRITICAL: Link Validity Rule** — Always create files in dependency order: **leaf nodes (technical modules) first, main report last**. This ensures all WikiLinks point to existing files.

### Phase 1: Analysis & Planning
1. **Detect language** from user request and select appropriate template
2. **Identify material type**: slides, paper, lecture notes, documentation
3. **Extract high-level structure**: main topics, flow of ideas
4. **Map technical topics**: identify distinct technical subjects that deserve separate treatment
5. **Plan file structure**: 
   - List all technical modules to create
   - List all concepts/authors that need pages
   - Determine dependency order (which module references which)

### Phase 2: Infrastructure
6. **Create folder structure**: `Technical Notes/{Title}/`
7. **Prepare index**: Add placeholder entry to reading reports index

### Phase 3: Technical Modules (LEAF NODES FIRST)
8. **Create technical modules in dependency order**:
   - Start with modules that don't depend on others
   - Each module should link back to the (future) main report
   - DO NOT include links to other technical modules yet
   - DO include links to concept pages (they will be created in Phase 4)
9. **Verify module completeness**: Each module should have: source link, content, back-link to main report

### Phase 4: Knowledge Base Pages
10. **Create/update author pages** (if not exists)
11. **Create/update concept pages** (if not exists)
12. **Prepare MOCs**: Ensure domain MOCs exist for linking

### Phase 5: Main Report (ROOT NODE LAST)
13. **Create main report**: 
    - At this point, ALL linked files (modules, concepts, authors) MUST exist
    - Include WikiLinks to all technical modules
    - Include WikiLinks to authors and key concepts
    - Add extended reading links

### Phase 6: Cross-Linking & Finalization
14. **Add inter-module links**: Go back to technical modules and add links between related modules
15. **Update index**: Convert placeholder entry to final link
16. **Final verification**: Ensure no empty WikiLinks exist

---

## WikiLink Creation Rules

### Rule 1: Link Target Must Exist
**BEFORE creating any link, verify the target file exists.**

❌ **Bad**:
```markdown
# Main Report
See [[Technical Notes/Title/Module|detailed notes]]  # Module doesn't exist yet!
```

✅ **Good**:
```markdown
# Main Report (created AFTER module exists)
See [[Technical Notes/Title/Module|detailed notes]]  # Module already exists
```

### Rule 2: Directional Link Strategy

| Link Direction | Creation Order | Example |
|---------------|----------------|---------|
| Main Report → Module | Module first | Phase 3 creates module, Phase 5 links to it |
| Module → Main Report | Main report created after | Use placeholder text if needed |
| Module A → Module B | B before A | If A references B, create B first |
| Any → Concept/Author | Concept/Author first | Phase 4 before Phase 5 |

### Rule 3: Placeholder Handling
If you MUST reference something before it exists:
- Use plain text: `详见后续章节"DPO原理"`
- Or create a minimal placeholder file first
- NEVER create `[[Link|text]]` pointing to non-existent files

### Rule 4: Path Consistency
- Main report: `Second Brain/Reading Reports/{Title} - 技术阅读报告.md`
- Modules: `Second Brain/Reading Reports/Technical Notes/{Title}/{Module}.md`
- Authors: `Second Brain/Database/Authors/{Name}.md`
- Concepts: `Second Brain/Database/Concepts/{Concept}.md`
- MOCs: `Second Brain/MOCs/{Domain}.md`

---

# Link Validation Checklist

**CRITICAL**: Before completing any technical reading report, verify all WikiLinks point to existing files.

## Pre-Creation Checklist
- [ ] Listed all technical modules to create
- [ ] Listed all concept pages to create/update
- [ ] Listed all author pages to create/update
- [ ] Determined creation order (dependencies first)

## During Creation Checklist
- [ ] Phase 3: All technical modules created BEFORE main report
- [ ] Phase 4: All concept/author pages created BEFORE main report
- [ ] Phase 5: Verify each link target exists before including in main report

## Post-Creation Verification
Run this mental check for every `[[...]]` in generated files:

```
For each WikiLink [[path|text]]:
  1. Does the file at 'path' exist?
  2. If not, either:
     - Create the target file, OR
     - Remove the link and use plain text
  3. Is the path format correct?
     - Technical modules: Technical Notes/{Title}/{Module}
     - Authors: Database/Authors/{Name}
     - Concepts: Database/Concepts/{Concept}
     - MOCs: MOCs/{Domain}
```

## Common Mistakes to Avoid

❌ **Creating main report before modules**:
```markdown
# In main report (WRONG)
See [[Technical Notes/Paper/Method|details]]  # File doesn't exist yet!
```

✅ **Correct order**:
```markdown
# Step 1: Create Technical Notes/Paper/Method.md first
# Step 2: Then create main report with:
See [[Technical Notes/Paper/Method|details]]  # File now exists
```

❌ **Linking to future concepts**:
```markdown
# In module (WRONG)
See [[Process Reward Model]] for details  # Concept page not created yet
```

✅ **Correct approach**:
```markdown
# Step 1: Create Database/Concepts/Process Reward Model.md
# Step 2: Then add link in module
```

## Emergency Fix

If you accidentally created empty links:

1. **Identify empty links**: Search for `[[...]]` patterns where target doesn't exist
2. **Create missing targets** or **replace with plain text**
3. **Never leave empty WikiLinks in final output**

---

# Worked Example: Analyzing Brad Efron's Slides (CORRECT ORDER)

When user provides `/Users/chaihao/Library/Mobile Documents/com~apple~CloudDocs/Documents/stat/Great Talks/2009BootstrapMethods.pdf`:

## Phase 1: Analysis & Planning
1. **Identify as technical reading** (academic slides)
2. **Plan structure**:
   - Modules needed: 重采样理论, 自助法算法, 置信区间构造, 方法对比
   - Concepts needed: Bootstrap, Resampling, Empirical Bayes
   - Author: Brad Efron
   - Domain MOCs: 统计学习, 贝叶斯统计

## Phase 2: Infrastructure
3. **Create folder**: `Technical Notes/Bootstrap Methods/`
4. **Add placeholder to index**: Reading Reports Index.md

## Phase 3: Technical Modules (LEAF FIRST)
5. **Create modules in dependency order**:
   - `Technical Notes/Bootstrap Methods/重采样理论基础.md`
     - Content: theory, math
     - Link back to future main report: `[[Bootstrap Methods (Efron 2009) - 技术阅读报告|主报告]]`
   - `Technical Notes/Bootstrap Methods/自助法算法.md`
     - Content: algorithm details
     - Links to: 重采样理论基础 (wait for Phase 6)
   - `Technical Notes/Bootstrap Methods/置信区间构造.md`
     - Content: CI construction methods
   - `Technical Notes/Bootstrap Methods/与其他方法的比较.md`
     - Content: comparison with other methods
     - Links to all other modules (wait for Phase 6)

## Phase 4: Knowledge Base
6. **Create concept pages**:
   - `Database/Concepts/Bootstrap.md` (if not exists)
   - `Database/Concepts/Resampling.md` (if not exists)
   - `Database/Concepts/Empirical Bayes.md` (if not exists)
7. **Update author page**: `Database/Authors/Brad Efron.md`
8. **Update MOCs**: `统计学习.md`, `贝叶斯统计.md`

## Phase 5: Main Report (ROOT LAST)
9. **Create main report**: `Second Brain/Reading Reports/Bootstrap Methods (Efron 2009) - 技术阅读报告.md`
   - All linked modules NOW EXIST
   - All linked concepts NOW EXIST
   - Include: `[[Technical Notes/Bootstrap Methods/重采样理论基础|重采样理论]]`
   - Include: `[[Database/Authors/Brad Efron|Brad Efron]]`
   - Include: `[[Database/Concepts/Bootstrap|Bootstrap]]`

## Phase 6: Cross-Linking
10. **Add inter-module links**:
    - Go back to each module
    - Add links: `[[Technical Notes/Bootstrap Methods/自助法算法|算法实现]]` etc.
11. **Update index**: Convert placeholder to final link
12. **Verify**: All `[[...]]` point to existing files ✓
