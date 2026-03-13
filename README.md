# Deep Reading

<p align="center">
  <b>Transform any book or technical material into a high-value cognitive asset</b><br>
  <b>将任何书籍或技术材料转化为高价值的认知资产</b><br>
  <b>任意の本や技術資料を高価値な認知資産に変換する</b>
</p>

<p align="center">
  <a href="#english">🇬🇧 English</a> •
  <a href="#中文">🇨🇳 中文</a> •
  <a href="#日本語">🇯🇵 日本語</a>
</p>

---

<h2 id="english">🇬🇧 English</h2>

An AI skill for [Kimi Code CLI](https://github.com/yuyarin/deep-reading) that performs deep, critical analysis of books, papers, and web content. Automatically generates structured reading reports and maintains an interconnected knowledge base in Obsidian.

### ✨ Features

- **🌍 Multi-Language Support**: Auto-detects your input language and generates reports in Chinese, English, Japanese, and more
- **📚 Dual Reading Modes**:
  - **General Reading**: For books, essays, non-fiction
  - **Technical Reading**: For papers, talks, slides with modular technical notes
- **🌐 Universal Web Support**: Analyze any URL (articles, blogs, news, documentation)
- **📖 Ebook Support**: PDF, EPUB, AZW3, MOBI, TXT
- **🔗 Automatic Knowledge Base**: Exports to Obsidian with WikiLinks, updates author pages, concepts, and domain MOCs
- **🔍 External Review Integration**: Searches and integrates book reviews from multiple sources

### 🚀 Quick Start

```bash
# General reading
"Analyze Thinking, Fast and Slow"
"Read Principles"
"Summarize The Psychology of Money"

# Technical reading
"Technical reading 2009BootstrapMethods.pdf"
"Analyze paper Large-Scale Inference"
"Read arXiv 2401.12345"

# Web content
"Analyze https://example.com/article"
"Read article https://blog.site.com/post"

# Ebooks
"Analyze ebook ~/Books/book.epub"
```

### 📋 Report Structure

**General Reading Report (9 sections)**:
1. Domain & Positioning
2. Core Takeaways (3-7 items)
3. Argument & Credibility Assessment
4. Quality Reviews & Secondary Perspectives
5. Points Worth Questioning
6. Compelling Excerpts
7. Action Recommendations
8. One-Sentence Summary
9. Extended Reading

**Technical Reading Report**:
- Main overview with links to detailed technical modules
- Modular technical notes for deep dives
- Cross-linked knowledge base entries

### 🔧 Installation

1. Copy this skill to your Kimi CLI skills directory:
   ```bash
   cp -r deep-reading ~/.config/agents/skills/
   ```

2. Configure your Obsidian vault path in the scripts (optional)

3. Start using trigger commands - no explicit skill name needed!

### 📁 Project Structure

```
deep-reading/
├── SKILL.md              # Complete skill documentation
├── QUICK_START.md        # Quick reference guide
├── README.md             # This file
├── scripts/
│   ├── export_to_obsidian.py
│   └── update_knowledge_base.py
└── assets/
    └── domain-moc-template.md
```

---

<h2 id="中文">🇨🇳 中文</h2>

适用于 [Kimi Code CLI](https://github.com/your-repo/kimi-cli) 的 AI Skill，对书籍、论文和网页内容进行深度批判性分析。自动生成结构化阅读报告，并在 Obsidian 中维护互联的知识库。

### ✨ 功能特点

- **🌍 多语言支持**：自动检测输入语言，生成中文、英文、日文等多种语言的报告
- **📚 双阅读模式**：
  - **一般阅读**：适用于书籍、散文、非虚构作品
  - **技术阅读**：适用于论文、演讲、幻灯片，支持模块化技术笔记
- **🌐 通用网页支持**：分析任意 URL（文章、博客、新闻、技术文档）
- **📖 电子书支持**：PDF、EPUB、AZW3、MOBI、TXT
- **🔗 自动知识库**：导出到 Obsidian，带 WikiLinks，自动更新作者页面、概念和领域 MOC
- **🔍 外部书评整合**：搜索并整合多来源的书评

### 🚀 快速开始

```bash
# 一般阅读
"分析《思考，快与慢》"
"阅读 Principles"
"总结 The Psychology of Money"

# 技术阅读
"技术阅读 2009BootstrapMethods.pdf"
"分析论文 Large-Scale Inference"
"读arXiv 2401.12345"

# 网页内容
"分析链接 https://example.com/article"
"阅读文章 https://blog.site.com/post"

# 电子书
"分析电子书 ~/Books/book.epub"
```

### 📋 报告结构

**一般阅读报告（9节结构）**：
1. 领域与定位
2. 核心 Takeaways（3-7条）
3. 论证与可信度评估
4. 高质量书评 / 二级观点
5. 值得质疑与反思的地方
6. 精彩书摘
7. 行动与迁移应用建议
8. 一句话记住这本书
9. 延伸阅读与对照书目

**技术阅读报告**：
- 主报告概览，链接到详细技术模块
- 模块化技术笔记，支持深度研究
- 交叉链接的知识库条目

### 🔧 安装

1. 将此 skill 复制到 Kimi CLI 的 skills 目录：
   ```bash
   cp -r deep-reading ~/.config/agents/skills/
   ```

2. 在脚本中配置你的 Obsidian vault 路径（可选）

3. 开始使用触发命令 - 无需显式提及 skill 名称！

---

<h2 id="日本語">🇯🇵 日本語</h2>

[Kimi Code CLI](https://github.com/your-repo/kimi-cli) 向けの AI スキル。本、論文、ウェブコンテンツを深く批判的に分析します。構造化された読書レポートを自動生成し、Obsidian で相互接続された知識ベースを維持します。

### ✨ 機能

- **🌍 多言語サポート**：入力言語を自動検出し、中国語、英語、日本語などでレポートを生成
- **📚 2つの読書モード**：
  - **一般読書**：本、エッセイ、ノンフィクション向け
  - **技術読書**：論文、講演、スライド向け。モジュール式技術ノート
- **🌐 汎用ウェブサポート**：任意の URL を分析（記事、ブログ、ニュース、ドキュメント）
- **📖 電子書籍サポート**：PDF、EPUB、AZW3、MOBI、TXT
- **🔗 自動知識ベース**：Obsidian へのエクスポート、WikiLinks、著者ページ・概念・ドメイン MOC の自動更新
- **🔍 外部レビュー統合**：複数ソースからの書評を検索・統合

### 🚀 クイックスタート

```bash
# 一般読書
"分析『思考、速くそして遅く』"
"読む Principles"
"要約 The Psychology of Money"

# 技術読書
"技術読み 2009BootstrapMethods.pdf"
"論文を分析 Large-Scale Inference"
"arXivを読む 2401.12345"

# ウェブコンテンツ
"分析 https://example.com/article"
"記事を読む https://blog.site.com/post"

# 電子書籍
"電子書籍を分析 ~/Books/book.epub"
```

### 📋 レポート構成

**一般読書レポート（9セクション）**：
1. 領域と位置づけ
2. 核心の要点（3-7項目）
3. 論証と信頼性の評価
4. 高品質な書評・二次的見解
5. 疑問と反省に値する点
6. 印象的な引用
7. 行動と応用の推奨事項
8. この本を一言で覚える
9. 延伸阅读・関連書目

**技術読書レポート**：
- 詳細技術モジュールへのリンク付き主レポート
- 深い探求のためのモジュール式技術ノート
- 相互リンクされた知識ベースエントリ

### 🔧 インストール

1. このスキルを Kimi CLI の skills ディレクトリにコピー：
   ```bash
   cp -r deep-reading ~/.config/agents/skills/
   ```

2. スクリプトで Obsidian vault パスを設定（オプション）

3. トリガーコマンドを使って開始 - スキル名を明示的に述べる必要はありません！

---

## 🌐 Supported Languages / 支持的语言 / サポート言語

| Language | Code | Status |
|:---|:---:|:---:|
| 🇨🇳 中文 (Chinese) | zh | ✅ Fully Supported |
| 🇬🇧 English | en | ✅ Fully Supported |
| 🇯🇵 日本語 (Japanese) | ja | ✅ Fully Supported |
| 🇰🇷 한국어 (Korean) | ko | ✅ Supported |
| 🇫🇷 Français (French) | fr | ✅ Supported |
| 🇩🇪 Deutsch (German) | de | ✅ Supported |
| 🇪🇸 Español (Spanish) | es | ✅ Supported |
| 🇷🇺 Русский (Russian) | ru | ✅ Supported |

---

## 📚 Documentation

| Document | Description |
|:---|:---|
| [SKILL.md](./SKILL.md) | Complete skill documentation with all templates |
| [QUICK_START.md](./QUICK_START.md) | Quick reference for common commands |

---

## 📝 License

MIT License - feel free to use and modify for your own knowledge management workflow.

---

<p align="center">
  Made with ❤️ for deep readers and knowledge builders<br>
  为深度阅读者和知识构建者精心打造<br>
  深い読者と知識構築者のために
</p>
