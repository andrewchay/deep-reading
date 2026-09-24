# Fiction Mode Reference (小说阅读模式)

This file is loaded by `deep-reading` SKILL.md when the material is identified as fiction: novels, novellas, short story collections, or literary works. Do not load it for non-fiction books, technical materials, or web articles.

## Detection Signals

Load this file when any of these match:
- User trigger contains: 小说, 长篇, 中篇, 短篇, 文学, 虚构, 故事集 / novel, fiction, novella, short story / 小説, フィクション
- Ebook metadata or filename indicates a novel/short-story collection (e.g., "A Gentleman in Moscow.epub", "克拉拉与太阳.azw3")
- Web article is literary criticism of a work of fiction
- User explicitly asks for 小说阅读 / fiction reading mode

If ambiguous (e.g., a narrative non-fiction like 《冷血》), ask the user which mode to use.

## Role Adjustment

In fiction mode you are a **Narrative Analyst**, not an argument analyst:

- The unit of analysis is not "claims and evidence" but **narrative design**: how the story is told, not just what happens in it
- The "credibility" question becomes: are character motivations coherent? Is the world internally consistent? Is the ending earned?
- **Reading experience is a legitimate object of analysis**: how the book makes the reader feel, where it moves slowly, where it rewards rereading — treat this with the same rigor as thematic analysis
- Interpretive multiplicity is expected: acknowledge competing readings of the same scene/theme rather than forcing a single thesis

## Spoiler Policy

**Default: the user has finished the book. Full spoilers are allowed.**

- Analyze the complete plot, including the ending and any twists
- Quote and discuss any passage from the book
- External reviews may be quoted even if they contain plot details
- Add a spoiler note in the report header for future readers of the note: `> ⚠️ 本报告含完整剧透 / ⚠️ This report contains full spoilers`
- Only exception: if the user explicitly says they haven't finished (e.g., "读到一半", "我还没看完", "no spoilers"), then omit ending/twist content and mark the report as 无剧透 / spoiler-free

## What Changes vs. General Mode

| General mode section | Fiction mode replacement | Why |
|:---|:---|:---|
| 三、论证与可信度评估 | 三、情节结构与叙事策略 | Fiction persuades through narrative design, not argument |
| 五、值得质疑与反思 | 八、批判性评价与口碑 | Critique targets craft (pacing, plausibility, resolution), not evidence |
| 七、行动与迁移应用 | (dropped) | A novel's value is rarely an action item; application lives in 主题与延伸阅读 |
| Core Principles 3–4 (implicit assumptions, fact/argument/value) | Narrative equivalents: implicit worldview, what's shown vs. told, whose perspective is centered | Same critical instinct, different object |

Sections that carry over unchanged in spirit: one-sentence summary, excerpts with annotations, extended reading, external review integration.

## Fiction Report Template (9 sections)

### 🇨🇳 中文模板

```markdown
# 《书名》小说阅读报告

> ⚠️ 本报告含完整剧透（默认读者已读完本书）

## 一、基本信息与文学定位
- 类型 / 流派：
- 文学时期与运动：
- 写作与出版背景：
- 奖项与重要版本（含译本信息）：
- 在作者全部作品中的位置：

## 二、一句话记住这本书

## 三、情节结构与叙事策略
- 情节概要（含结局）：
- 叙事视角与叙事声音（POV、人称、可靠性）：
- 时间线与结构安排（线性/倒叙/多线）：
- 关键转折与高潮设计：转折是否出人意料又在情理之中

## 四、人物分析
- 主要人物与弧线（起点→变化→终点）：
- 动机与可信度：行为逻辑是否自洽
- 人物关系图谱（文字描述或简单列表）
- 值得玩味的配角与群像：
- 叙述者可靠性问题（如适用）：

## 五、主题与意象
- 核心主题（2–4个，每个附文本证据）：
- 反复出现的意象 / 象征 / 母题：
- 标题的含义与呼应：

## 六、文体与语言
- 文笔风格（节奏、密度、幽默感等）：
- 对话质量：
- 结构与节奏问题（拖沓/跳跃/留白）：
- 译本评价（如为翻译作品：译者风格、关键术语处理、与原文的差距）：

## 七、文学谱系与互文
- 作者的其他作品与本书的关系：
- 文学传统与影响来源：
- 可对照阅读的作家与作品（延伸阅读）：

## 八、批判性评价与口碑
- 文学评论界评价（专业书评、学者批评）：
- 读者口碑（豆瓣 / Goodreads，找高赞且有实质内容的短评）：
- 值得商榷之处：节奏、可信度、结局处理、重复自我等
- 这本书的局限与最适合的读者：

## 九、精彩段落与重读价值
- 摘录：
- 为什么这段好（技巧层面）：
- 重读时的新发现：
```

### 🇬🇧 English Template

```markdown
# {Book Title} - Fiction Reading Report

> ⚠️ This report contains full spoilers (assumes you have finished the book)

## 1. Basic Info & Literary Positioning
- **Genre / School:**
- **Literary Period & Movement:**
- **Writing & Publication Context:**
- **Awards & Notable Editions (incl. translations):**
- **Place in the Author's Oeuvre:**

## 2. One-Sentence Summary

## 3. Plot Structure & Narrative Strategy
- **Plot Summary (incl. ending):**
- **Narrative POV & Voice (person, reliability):**
- **Timeline & Structure (linear/flashback/multi-thread):**
- **Key Turns & Climax Design:** is each twist surprising yet inevitable?

## 4. Character Analysis
- **Main Characters & Their Arcs (start → change → end):**
- **Motivation & Plausibility:** is behavior internally consistent?
- **Relationship Map** (prose list or simple diagram)
- **Notable Supporting Characters & Ensemble:**
- **Narrator Reliability (if applicable):**

## 5. Themes & Motifs
- **Core Themes (2-4, each with textual evidence):**
- **Recurring Imagery / Symbols / Motifs:**
- **Meaning of the Title:**

## 6. Style & Language
- **Prose Style (rhythm, density, humor):**
- **Dialogue Quality:**
- **Structural Pacing Issues (dragging/rushed/elliptical):**
- **Translation Assessment (if translated: translator's voice, key term choices, distance from the original):**

## 7. Literary Lineage & Intertextuality
- **Relation to the Author's Other Works:**
- **Literary Tradition & Influences:**
- **Comparative & Extended Reading:**

## 8. Critical Reception & Assessment
- **Critical Reception (professional reviews, scholarly criticism):**
- **Reader Reception (Goodreads / Douban — favor substantive highly-rated reviews):**
- **Points Worth Questioning:** pacing, plausibility, resolution, self-repetition
- **Limitations & Ideal Readers:**

## 9. Compelling Passages & Reread Value
- **Excerpt:**
- **Why It Works (craft-level analysis):**
- **New Discoveries on Rereading:**
```

### 🇯🇵 日本語テンプレート

```markdown
# 『書名』小説読書レポート

> ⚠️ このレポートには完全なネタバレが含まれます（読了済みを前提とします）

## 1. 基本情報と文学的位置づけ
- **ジャンル／流派：**
- **文学的時期と運動：**
- **執筆・出版の背景：**
- **受賞歴と主要版本（翻訳を含む）：**
- **著者の全作品の中での位置：**

## 2. この本を一言で覚える

## 3. プロット構造と叙事方略
- **プロット概要（結末を含む）：**
- **視点と語りの声音（人称、信頼性）：**
- **時間軸と構造（順行／回想／多線）：**
- **重要な転換とクライマックスの設計：**

## 4. 人物分析
- **主要人物とその弧（出発→変化→到達点）：**
- **動機と説得力：行動論理は一貫しているか**
- **人物相関図（文章リストで可）**
- **注目すべき脇役と群像：**
- **語り手の信頼性（該当する場合）：**

## 5. テーマとモチーフ
- **核心的テーマ（2〜4つ、それぞれテキストの根拠を付す）：**
- **反復されるイメージ／象徴／モチーフ：**
- **タイトルの意味：**

## 6. 文体と言語
- **文体（リズム、密度、ユーモア）：**
- **会話の質：**
- **構造とテンポの問題（停滞／駆け足／省略）：**
- **翻訳の評価（翻訳作品の場合）：**

## 7. 文学的系譜と相互テクスト性
- **著者の他作品との関係：**
- **文学的传统と影響源：**
- **対照読書・延伸阅读：**

## 8. 批評的評価と評判
- **批評界の評価（専門書評、学術批評）：**
- **読者の評判（Goodreads／豆瓣）：**
- **問い直すべき点：テンポ、説得力、結末の処理、自己反復**
- **限界と最適な読者：**

## 9. 印象的な一節と再読の価値
- **引用：**
- **なぜ良いのか（技巧の層から）：**
- **再読で見える新しい発見：**
```

## Section Guidance & Pitfalls

- **三、情节结构**: Summarize the *whole* plot including the ending (spoiler policy above). Evaluate structure as craft: does the timeline serve the story? Is the climax prepared or imposed?
- **四、人物分析**: Judge characters by internal consistency and development, not likability. A static character can be a deliberate design — say so. Note the difference between "flawed character" and "poorly written character."
- **五、主题与意象**: Every theme needs at least one concrete textual anchor (scene, image, line). Avoid reducing the book to a single moral.
- **六、文体与语言**: For translated fiction, the translation is part of the reading experience — assess it, and note where you'd check the original. Do not confuse "I didn't like it" with "it is flawed"; separate taste judgment from craft judgment.
- **八、批判性评价**: Balance praise and criticism. Quote 2–4 substantive reviews (professional criticism + high-quality reader reviews). Generic praise ("touching", "a masterpiece") is not insight — skip it.

## Style Requirements (Fiction Mode)

- Tone may be more literary and engaged than non-fiction reports — you are discussing an aesthetic object — but remain analytical, never marketing-like
- Avoid gushing: replace "感人至深" with *why* it moves readers (which scene, which technique)
- It is legitimate to report emotional response ("初读时...", "第二次读到这里才注意到...") as long as it's tied to craft analysis
- Use consistent character/place names matching the edition the user read (译本名称、人名译法)

## External Review Integration (Fiction)

1. Search: `"{书名}" 书评 豆瓣`, `"{Title}" Goodreads reviews`, `"{Title}" literary criticism review`, `"{Book}" 解析 主题`
2. Prioritize: 豆瓣/Goodreads 高赞长评, professional literary critics (for translated works also: 译者访谈, 原出版国评论)
3. Integrate 2–4 quotes into section 八 with attribution; prefer reviews offering specific critique over awards lists
4. Reviews may contain spoilers — permitted under the default policy

## Workflow

1. Detect language from user request; select matching template above
2. Identify exact edition if possible (译本 matters for section 六); note it in section 一
3. Extract full plot including ending; map narrative structure (POV, timeline)
4. Build character arcs and relationship map
5. Identify themes, motifs, symbols with textual anchors
6. Assess prose style and pacing; for translations, assess translator choices
7. Search and integrate external reviews (see above)
8. Generate the 9-section report, then export to Obsidian (see below)

## Obsidian Integration

- **Report file**: `Second Brain/Reading Reports/{Title} - 小说阅读报告.md` / `{Title} - Fiction Reading Report.md`
- **Index**: append to `📚 阅读报告索引.md` — same protocol as general mode; put entry under a 文学/小说 grouping if the index has one
- **Author pages**: same author template as general mode; section 简介 should mention the author's fiction oeuvre and style signature
- **Concept pages**: for themes and literary devices create concept pages with tags `#literary-theme` / `#literary-device` (e.g., [[不可靠叙述者]], [[不可靠叙事]]; [[In medias res]]). Use the general concept template, replacing the formal-definition block with textual examples
- **MOC**: add to `Second Brain/MOCs/文学与小说.md` (create with general MOC template if missing); genre sub-groupings (科幻小说, 推理小说, 文学小说, etc.) are welcome
- **WikiLink rules**: identical to SKILL.md — targets must exist before linking

## Interaction with Other Modes

- Fiction-like narrative non-fiction (报告文学, 非虚构小说): ask the user; usually general mode with fiction-style section 三
- Graphic novels / 漫画: fiction mode works, plus note visual storytelling in section 六
- Plays / 剧本: fiction mode with structure adapted (幕/场 instead of chapters)
- Poetry collections: do NOT use this file — fall back to general mode and ask the user what they want
