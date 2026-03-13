#!/usr/bin/env python3
"""
Export deep reading report to Obsidian vault with WikiLinks.
"""

import argparse
import os
import re
import sys
from datetime import datetime
from pathlib import Path


def sanitize_filename(title: str) -> str:
    """Convert title to safe filename."""
    # Remove or replace unsafe characters
    unsafe = '<>:"/\\|?*'
    for char in unsafe:
        title = title.replace(char, '')
    # Replace multiple spaces with single space
    title = re.sub(r'\s+', ' ', title)
    return title.strip()


def generate_report_filename(book_title: str) -> str:
    """Generate filename for the report."""
    safe_title = sanitize_filename(book_title)
    return f"{safe_title} - 深度阅读报告.md"


def generate_index_entry(book_title: str, author: str, domain: str, report_path: str) -> str:
    """Generate entry for books index."""
    link = f"[[{report_path}|{book_title}]]"
    return f"| {link} | {author} | {domain} | {datetime.now().strftime('%Y-%m-%d')} |"


def create_obsidian_report(
    book_title: str,
    author: str,
    domain: str,
    sub_domain: str,
    takeaways: list,
    credibility: dict,
    reviews: str,
    critiques: dict,
    quotes: list,
    actions: dict,
    one_liner: str,
    further_reading: list,
    vault_path: str,
    output_folder: str = "Second Brain/Reading Reports"
) -> str:
    """
    Create Obsidian markdown report with WikiLinks.
    Returns the path to created file.
    """
    
    # Ensure output directory exists
    output_dir = Path(vault_path) / output_folder
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate filename
    filename = generate_report_filename(book_title)
    filepath = output_dir / filename
    
    # Create relative path for WikiLinks
    rel_path = f"{output_folder}/{filename.replace('.md', '')}"
    
    # Build report content
    content = f"""# 《{book_title}》深度阅读报告

> **作者**: {author}  
> **分析日期**: {datetime.now().strftime('%Y-%m-%d %H:%M')}  
> **标签**: #book-report #{' #'.join(domain.lower().split()) if domain else 'reading'}

---

## 一、领域与定位

| 维度 | 内容 |
|------|------|
| **核心领域** | {domain} |
| **子领域** | {sub_domain} |
| **目标读者** | {credibility.get('target_readers', '待补充')} |
| **试图解决的问题** | {credibility.get('problem', '待补充')} |

---

## 二、核心 Takeaways

"""
    
    # Add takeaways
    for i, takeaway in enumerate(takeaways, 1):
        content += f"""### {i}. {takeaway.get('title', f'Takeaway {i}')}
{takeaway.get('explanation', '')}

"""
    
    content += f"""---

## 三、论证与可信度评估

| 维度 | 评估 |
|------|------|
| **主要论证方式** | {credibility.get('method', '待补充')} |
| **数据来源** | {credibility.get('sources', '待补充')} |
| **可信度** | {'⭐' * credibility.get('rating', 3)} ({credibility.get('rating_text', '中')}) |
| **主要限制** | {credibility.get('limitations', '待补充')} |

---

## 四、高质量书评 / 二级观点

{reviews if reviews else '> 待补充外部书评与批评观点'}

---

## 五、值得质疑与反思

### 隐含前提
{chr(10).join(['- ' + p for p in critiques.get('assumptions', ['待补充'])])}

### 可能的偏差
{chr(10).join(['- ' + b for b in critiques.get('biases', ['待补充'])])}

### 反例或未讨论
{chr(10).join(['- ' + c for c in critiques.get('counterexamples', ['待补充'])])}

---

## 六、精彩书摘

"""
    
    # Add quotes
    for i, quote in enumerate(quotes, 1):
        content += f"""> {quote.get('text', '')}
> —— *{quote.get('location', '书中')}*

**价值说明**: {quote.get('value', '待补充')}

**可使用场景**: {quote.get('scene', '待补充')}

---

"""
    
    content += f"""## 七、行动与迁移应用

### 普通读者
{chr(10).join(['- ' + a for a in actions.get('general', ['待补充'])])}

### 专业人士
{chr(10).join(['- ' + a for a in actions.get('professional', ['待补充'])])}

---

## 八、一句话记住这本书

> **{one_liner}**

---

## 九、延伸阅读

"""
    
    # Add further reading with potential links
    for book in further_reading:
        title = book.get('title', '')
        author = book.get('author', '')
        relation = book.get('relation', '')
        # Create potential wikilink if book exists in vault
        content += f"- **[[{title}]]** - {author} ({relation})\n"
    
    content += f"""
---

## 🔗 相关链接

- [[Second Brain/Reading Reports/📚 阅读报告索引|返回阅读报告索引]]
- [[Second Brain/Areas/{'/'.join(domain.split()[:2]) if domain else 'Reading'}/{'/'.join(domain.split()[:2]) if domain else 'Reading'}|相关领域]]

---

> 📖 *本报告由 Deep Reading Analyst AI 生成*  
> 🏷️ 标签: #book-report #{' #'.join(domain.lower().split()[:3]) if domain else 'reading'} #{' #'.join(author.lower().split()[:2]) if author else 'unknown-author'}
"""
    
    # Write file
    filepath.write_text(content, encoding='utf-8')
    
    return str(filepath), rel_path


def update_books_index(
    vault_path: str,
    book_title: str,
    author: str,
    domain: str,
    report_path: str,
    index_path: str = "Second Brain/Reading Reports/📚 阅读报告索引.md"
) -> None:
    """Update or create books index file."""
    
    index_file = Path(vault_path) / index_path
    entry = generate_index_entry(book_title, author, domain, report_path)
    
    if index_file.exists():
        # Read existing content
        content = index_file.read_text(encoding='utf-8')
        # Add entry if not exists
        if book_title not in content:
            # Find the table and add entry
            content = content.rstrip()
            if not content.endswith('\n'):
                content += '\n'
            content += entry + '\n'
            index_file.write_text(content, encoding='utf-8')
    else:
        # Create new index
        content = f"""# 📚 阅读报告索引

> 本索引包含所有 AI 深度阅读报告，按分析日期排序。

## 书籍列表

| 书名 | 作者 | 领域 | 分析日期 |
|------|------|------|----------|
{entry}

---

## 按领域分类

待整理...

---

## 按作者分类

待整理...

---

> 🔄 *最后更新: {datetime.now().strftime('%Y-%m-%d %H:%M')}*
"""
        index_file.parent.mkdir(parents=True, exist_ok=True)
        index_file.write_text(content, encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description='Export deep reading report to Obsidian')
    parser.add_argument('--vault', required=True, help='Path to Obsidian vault')
    parser.add_argument('--title', required=True, help='Book title')
    parser.add_argument('--author', default='Unknown', help='Book author')
    parser.add_argument('--domain', default='', help='Core domain')
    parser.add_argument('--output-folder', default='Second Brain/Reading Reports', 
                       help='Output folder within vault')
    
    args = parser.parse_args()
    
    # Example usage - in real usage, these would come from the analysis
    print(f"Creating report for: {args.title}")
    print(f"Vault: {args.vault}")
    print(f"Output: {args.output_folder}")
    
    # Placeholder - actual data would come from the AI analysis
    filepath, rel_path = create_obsidian_report(
        book_title=args.title,
        author=args.author,
        domain=args.domain,
        sub_domain="",
        takeaways=[],
        credibility={},
        reviews="",
        critiques={},
        quotes=[],
        actions={},
        one_liner="",
        further_reading=[],
        vault_path=args.vault,
        output_folder=args.output_folder
    )
    
    print(f"Report created: {filepath}")
    print(f"WikiLink: [[{rel_path}]]")


if __name__ == '__main__':
    main()
