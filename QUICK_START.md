# Deep Reading Analyst - 快速启动指南

> 无需提及 skill 名称的简洁触发方式

---

## 🚀 快速触发命令

### 一般阅读模式 (General Reading)

**适用于**: 书籍、散文、一般非虚构作品

| 触发方式 | 示例 |
|:---|:---|
| `分析 [书名]` | "分析《思考，快与慢》" |
| `阅读 [书名]` | "阅读 Principles" |
| `解读 [书名]` | "解读 The Beginning of Infinity" |
| `总结 [书名]` | "总结 The Elephant in the Brain" |

**完整示例**:
```
"分析《思考，快与慢》，导出到 Obsidian"
"阅读 Principles，生成深度阅读报告"
"解读 The Beginning of Infinity"
```

---

### 技术阅读模式 (Technical Reading)

**适用于**: 学术演讲、论文、技术文档、课程讲义

| 触发方式 | 示例 |
|:---|:---|
| `技术阅读 [标题]` | "技术阅读 2009BootstrapMethods" |
| `分析论文 [标题]` | "分析论文 Large-Scale Inference" |
| `分析演讲 [标题]` | "分析演讲 Bayes/EB Info" |
| `学术阅读 [标题]` | "学术阅读 Tweedie's Formula" |
| `读论文 [标题]` | "读论文 2007SimInference" |
| `读演讲 [标题]` | "读演讲 Model Selection" |

**完整示例**:
```
"技术阅读 2009BootstrapMethods.pdf"
"分析论文 Large-Scale Inference，生成技术模块"
"学术阅读 Bradley Efron 的 Bayes/EB Info 演讲"
"读论文 /Users/chaihao/.../2007SimInference.pdf"
```

---

## 📋 文件路径处理

### 方式 1: 直接提供路径
```
"技术阅读 /Users/chaihao/Library/Mobile Documents/com~apple~CloudDocs/Documents/stat/Great Talks/2009BootstrapMethods.pdf"
```

### 方式 2: 只提供文件名（默认目录）
```
"技术阅读 2009BootstrapMethods.pdf"
```
*默认会在 `/Users/chaihao/Library/Mobile Documents/com~apple~CloudDocs/Documents/stat/Great Talks/` 查找*

### 方式 3: 提供目录 + 文件名
```
"分析演讲 Great Talks/2007SimInference.pdf"
```

---

## 🎯 批量处理

### 批量分析多个文件
```
"技术阅读以下 Efron 的演讲：
- 2007SimInference.pdf
- 2010TweediesFormula.pdf  
- 2012BayesEBInfo.pdf"
```

### 分析整个目录
```
"技术阅读 /Users/chaihao/Library/Mobile Documents/com~apple~CloudDocs/Documents/stat/Great Talks/ 目录下的所有 Efron 演讲"
```

---

## 🔄 导出选项

### 自动导出（默认）
所有分析完成后**自动导出到 Obsidian**，无需额外指令。

### 仅分析不导出
```
"分析《思考，快与慢》，不要导出"
"技术阅读 2009BootstrapMethods，本地预览"
```

### 更新已有报告
```
"更新 Bootstrap Methods 报告"
"重新分析 2009BootstrapMethods，覆盖现有技术模块"
```

---

## 💡 高级用法

### 指定技术模块
```
"技术阅读 2009BootstrapMethods，重点关注：
- Formula X 的推导
- 与置换检验的比较
- 在基因表达数据中的应用"
```

### 对比分析
```
"对比分析以下两篇论文：
1. 2009BootstrapMethods.pdf
2. 2007SimInference.pdf

重点关注它们在处理相关性时的不同方法"
```

### 生成特定输出
```
"技术阅读 2012BayesEBInfo，只生成：
- 核心贡献总结
- 与 2009BootstrapMethods 的联系
- 个人研究想法"
```

---

## 📚 常见场景速查

| 场景 | 指令 |
|:---|:---|
| 读一本书 | "分析《书名》" |
| 读一篇论文 | "读论文 [标题]" 或 "技术阅读 [标题]" |
| 读一个演讲 | "读演讲 [标题]" 或 "技术阅读 [标题]" |
| 读多个论文 | "技术阅读以下文件：[列表]" |
| 读整个目录 | "技术阅读 [目录路径]" |
| 更新已有报告 | "更新 [标题] 报告" |
| 对比多篇材料 | "对比分析 [文件1] 和 [文件2]" |

---

## ⚡ 最简指令

如果记不清具体指令，使用以下通用模式：

```
"[动作] [材料]"
```

**动作**: 分析、阅读、解读、总结、技术阅读、读论文、读演讲  
**材料**: 书名、文件名、路径

**示例**:
```
"分析 The Beginning of Infinity"
"技术阅读 2009BootstrapMethods.pdf"
"读论文 Large-Scale Inference"
"总结 The Elephant in the Brain"
```

---

## 🔍 自动检测

系统会根据输入自动检测阅读模式：

| 检测信号 | 自动选择模式 |
|:---|:---|
| `.pdf` 文件 + 数学公式密集 | 技术阅读 |
| 文件名含年份 (2009, 2010...) | 技术阅读 |
| 书名是常见出版物 | 一般阅读 |
| 用户明确说"技术阅读" | 技术阅读 |
| 用户明确说"论文"/"演讲" | 技术阅读 |

---

🏷️ 标签: #quick-start #deep-reading #commands #triggers

🔄 *最后更新: 2026-03-09*
