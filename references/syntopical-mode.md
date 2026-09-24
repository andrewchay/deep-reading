# Syntopical Mode Reference (主题阅读模式)

Loaded by `deep-reading` SKILL.md when the user provides a **topic plus multiple books** (explicitly or as a reading list) and wants cross-book synthesis — or invokes comparative analysis with 2+ books on the same subject.

This mode is the **reverse engine of the domain MOC**: instead of hanging one report on a MOC, it builds the MOC's consensus-and-debate map from a cluster of books.

## Detection Signals

- Multiple book titles/files in one request + keywords: 主题, 综合, 书单, 这一系列, 梳理 / compare, synthesis, reading list, syntopical
- The existing batch command `对比分析 [A] 和 [B]` upgrades to this mode when both books share a domain
- A bare topic ("帮我梳理决策科学") may also trigger if the user has or wants a reading list

If the books span unrelated domains, ask: does the user really want synthesis, or separate per-book analyses?

## Role Adjustment

You are a **synthesizer**. The unit of analysis is the **conversation among books**, not any single book:

- Core moves: consensus extraction, disagreement mapping, lineage tracing, reading-order design
- Do not summarize each book and stop — the deliverable is the map of where the books agree, fight, and descend from each other
- Watch for books **talking past each other**: the same term defined differently across authors is a definitional split, not a disagreement — flag it as such

## Spoiler Policy

Follow the per-book mode policies for the individual analyses (fiction books in the set follow fiction-mode's default: user has finished). The synthesis itself discusses conclusions and endings freely when comparing how books resolve their arguments.

## Workflow (5 Phases)

### Phase 1: Frame the Topic
Sharpen the user's topic into **1–3 guiding questions** (e.g., for 决策科学: "直觉何时可靠?"). All per-book extraction is organized around these questions. Confirm them with the user if the topic is broad.

### Phase 2: Per-Book Extraction
For each book, run the appropriate type mode (General / Fiction / Theology / Technical) with this **shared extraction block** appended to whatever template that mode uses:

```markdown
## 主题阅读抽取块（内部使用，不进单书报告）
- 对引导问题1的立场（一句话 + 页/章依据）：
- 对引导问题2的立场：
- 方法/视角特征：
- 关键证据类型（实验/案例/经文/数据/叙事）：
- 与其他书的已知关系（如用户提及）：
```

Per-book reports are generated normally (or updated if they already exist in the KB — READ first, append the synthesis links, never overwrite).

### Phase 3: Synthesis
Build the synthesis report from the template below. This is the main deliverable.

### Phase 4: Knowledge Base Landing
- **Update the domain MOC**: append a 共识与争论 section (or update it) built from sections 二/三 of the synthesis report — merge with what the MOC already says, never overwrite
- Link all per-book reports from the MOC's 核心著作 section
- Create **对比概念页** for contested concepts (see below)
- Update `📚 阅读报告索引.md`

### Phase 5: Reading Order
Deliver the recommended reading sequence (入门 → 进阶 → 深入) — this is often the user's real goal.

## Synthesis Report Template

### 🇨🇳 中文模板

```markdown
# {主题} 主题阅读综合报告

> 引导问题：
> 书目：N 本（见下表）
> 生成日期：

## 一、主题界定与书目
| 书 | 作者 | 一句话定位 | 单书报告 |
|:---|:---|:---|:---|
| [[《A》 - 深度阅读报告\|《A》]] | | | |

## 二、共识地图
（按引导问题组织：这个问题上，哪些书持相同/兼容立场？共识的证据强度如何？）

## 三、分歧与争论
| 争论点 | 各方立场 | 代表 | 分歧类型（实质/定义/程度） |
|:---|:---|:---|:---|

## 四、知识演化脉络
（按时间：谁奠基、谁修正、谁反对；本书目未覆盖但绕不开的名字也要提）

## 五、方法论与视角差异
（实验科学 vs 哲学论证 vs 历史叙事 vs 神学释经… 方法差异往往比分歧本身更重要）

## 六、阅读顺序建议
- 入门第一本（为什么先读它）：
- 进阶：
- 深入/反面视角：

## 七、知识库集成记录
- 更新的 MOC：[[文学与小说]] / [[认知科学与心理学]] / …
- 新建对比概念页：
- 索引更新：✅
```

### 🇬🇧 English Template

```markdown
# {Topic} - Syntopical Synthesis Report

> Guiding questions:
> Corpus: N books (see table)
> Date:

## 1. Topic Framing & Corpus
| Book | Author | One-line Position | Full Report |
|:---|:---|:---|:---|
| [[{A} - Deep Reading Report\|{A}]] | | | |

## 2. Consensus Map
(Organized by guiding question: which books agree? How strong is the converging evidence?)

## 3. Disagreements & Debates
| Debate | Positions | Representatives | Type (substantive/definitional/degree) |
|:---|:---|:---|:---|

## 4. Intellectual Lineage
(Chronological: who founded, refined, opposed; name indispensable figures outside the corpus)

## 5. Methodological & Perspectival Differences
(Experiment vs. philosophical argument vs. historical narrative vs. exegesis — method gaps often matter more than positions)

## 6. Recommended Reading Order
- Start with (why):
- Then:
- Advanced / opposing view:

## 7. Knowledge Base Integration Record
- Updated MOCs:
- New comparative concept pages:
- Index updated: ✅
```

## Output Files

- **Main synthesis**: `Second Brain/Reading Reports/{主题} - 主题阅读综合报告.md` / `{Topic} - Syntopical Synthesis Report.md`
- **Per-book reports**: standard locations per their modes (`{Title} - 深度阅读报告.md`, `{Title} - 小说阅读报告.md`, etc.)
- **MOC update**: append 共识与争论 map to `Second Brain/MOCs/{Domain}.md`
- **对比概念页** (optional, for heavily contested concepts): `Second Brain/Database/Concepts/{Concept}.md` with a positions table and tag `#debated-concept`; base it on the concept template in `references/kb-templates.md`, replacing the formal-definition block with the positions table

## Pitfalls

- Don't average away real disagreements — name who disagrees, on what, and why it matters
- Definitional splits look like disagreements; check each author's key terms before mapping positions
- If the corpus is dominated by one author or one school, state plainly: this is a school view, not yet a field view
- 2-book comparisons are the degenerate case of synthesis — the template still applies (consensus map will be small); resist the urge to just do " similarities and differences" bullet lists
- Fiction clusters: for 对照阅读 of novels, the synthesis centers on theme/motif/contrast in treatment (how two novels handle memory, say), and section 四 becomes literary influence instead of intellectual lineage
