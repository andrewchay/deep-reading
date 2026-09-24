# Inspectional Mode Reference (检视阅读模式)

Loaded by `deep-reading` SKILL.md when the user wants a **pre-read triage**: "should I read this?" It answers the question "will THIS reader get value from THIS book, right now?" — not "is this a good book?"

**Orthogonal to text type**: applies to general non-fiction, fiction, technical materials, and theology alike. If the user decides to read, full analysis happens later in the appropriate type mode.

## Detection Signals

- Trigger contains: 值得读吗, 值不值得读, 要不要读, 试读, 帮我看看这本书, 这书怎么样, 给个意见 / should I read, is it worth reading, worth my time, read triage / 読む価値は
- OR the user provides a book and asks for a recommendation/judgment rather than analysis

## Role Adjustment

You are a **reading advisor optimizing the user's time**, not an analyst:

- Produce an evidence-based verdict card — NOT the full 9-section report
- **Sample strategically, never deep-read the whole book**: table of contents → preface/intro → conclusion → one representative chapter. For fiction: premise + first chapter + reception. Disclose the sampling basis in the card
- Combine two evidence streams: your own sampling (answers "will YOU get value") and external reception (answers "did others like it") — never let ratings substitute for sampling judgment

## Spoiler Policy

Default: the user has **NOT** read the book. Describe premise and setup only; avoid endings and major plot twists. If the user explicitly says spoilers are fine (剧透无所谓 / spoil me), include them.

## Verdict Card Template

### 🇨🇳 中文模板

```markdown
# 《书名》试读评估

> 评估依据：目录 + 抽样章节（前言/结论/代表性一章）+ 外部评价
> 评估日期：

## 判决
- 结论：✅ 值得读 / ⚠️ 选择性读 / ❌ 暂不推荐
- 置信度：高 / 中 / 低
- 一句话理由：

## 这本书是什么
（3 句话以内：核心主张或故事前提 + 作者的写法 + 在同类书中的位置）

## 适合谁 / 不适合谁
- 适合：
- 不适合：

## 与你知识库的重叠
- 与已有报告/概念的重叠：
- 增量价值：

## 80/20 阅读路径
（若读：哪些章节必读、哪些可跳、推荐读法——顺序、速度、是否配合别的书）

## 外部评价速览
- 豆瓣 / Goodreads / Amazon 均分：
- 评论界共识（一句话）：
- 最常见的批评（一句话）：

## 替代选项
（同主题更好的选择，如适用）

## 如果决定读
- 建议完整分析模式：General / Fiction / Technical / Theology
```

### 🇬🇧 English Template

```markdown
# {Book Title} - Read Triage

> Basis: TOC + sampled chapters (preface/conclusion/one representative chapter) + external reception
> Date:

## Verdict
- **Call:** ✅ Read it / ⚠️ Read selectively / ❌ Skip for now
- **Confidence:** High / Medium / Low
- **One-line reason:**

## What This Book Is
(3 sentences max: core claim or premise + the author's approach + its place among similar books)

## For Whom
- **Great for:**
- **Not for:**

## Overlap with Your Knowledge Base
- Overlaps with existing reports/concepts:
- Incremental value:

## The 80/20 Path
(If reading: must-read chapters, skippable parts, recommended order/pace/companion books)

## External Reception at a Glance
- Goodreads / Amazon / Douban average:
- Critical consensus (one line):
- Most common criticism (one line):

## Alternatives
(Better choices on the same topic, if any)

## If You Decide to Read
- Suggested full-analysis mode: General / Fiction / Technical / Theology
```

### 🇯🇵 日本語テンプレート

```markdown
# 『書名』読書トリアージ

> 根拠：目次＋抜粋章（序/結論/代表的な一章）＋外部評価
> 日付：

## 判定
- **結論**：✅ 読む価値あり / ⚠️ 選択的に / ❌ 今は見送り
- **確度**：高／中／低
- **一言の理由：**

## どんな本か
（3文以内：核心主張または前提＋著者の手法＋同類書の中での位置）

## 向いている人／向いていない人
- **向いている人：**
- **向いていない人：**

## 知識基盤との重複
- 既存レポート・概念との重複：
- 追加的価値：

## 80/20の読み方
（読む場合：必読章、飛ばしてよい部分、推奨順序・ペース）

## 外部評価の概観
- Goodreads／Amazon 平均評価：
- 批評界のコンセンサス（一言）：
- 最も多い批判（一言）：

## 代替案
（同テーマのより良い選択肢があれば）

## 読むことにしたら
- 推奨の完全分析モード：General / Fiction / Technical / Theology
```

## Workflow

1. Detect language; select the matching template
2. Sample the book: TOC → preface/intro → conclusion → one representative chapter (fiction: premise + first chapter)
3. Search external reception: rating aggregates + 2–3 substantive reviews (professional + high-quality reader reviews)
4. Check KB overlap: read `📚 阅读报告索引.md` and the relevant domain MOC; link overlaps in the card
5. Deliver the verdict card **in conversation** — see export policy below
6. If the verdict is ✅ or ⚠️, offer: "读完之后可以用 General/Fiction/Theology 模式做完整分析"

## Export Policy

Default: **conversation only, no Obsidian export** — a triage card is a decision aid, not a knowledge asset. If the user asks to keep it, export to `Second Brain/Reading Reports/Inspectional/{Title} - 试读评估.md` and add one line to the index under a 试读评估 grouping. Do NOT create author/concept/MOC pages from a triage — that happens after a real reading.

## Boundaries

- Sampling quality too low to judge (broken scan, DRM, missing TOC)? Say so explicitly and lower the confidence
- A verdict card is not a book review — don't pad it to look like one; its value is the decision and the 80/20 path
- Don't issue ❌ lightly: "not for you NOW" is often more accurate than "bad book" — prefer ⚠️ with a note on when it would become worth reading
