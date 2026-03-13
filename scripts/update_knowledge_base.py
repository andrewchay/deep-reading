#!/usr/bin/env python3
"""
Automatically update Obsidian knowledge base after generating a reading report.
Updates: Author pages, Concept pages, Domain MOCs, and Knowledge Base Index.
"""

import argparse
import os
import re
from datetime import datetime
from pathlib import Path


def ensure_file_exists(filepath: Path, template: str = "") -> None:
    """Create file if it doesn't exist."""
    if not filepath.exists():
        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.write_text(template, encoding='utf-8')


def update_author_page(vault_path: str, author_name: str, book_title: str, domain: str) -> None:
    """Update or create author page."""
    author_file = Path(vault_path) / "Second Brain" / "Database" / "Authors" / f"{author_name}.md"
    
    # Check if file exists
    if author_file.exists():
        content = author_file.read_text(encoding='utf-8')
        
        # Add book link if not exists
        book_link = f"[[{book_title} - 深度阅读报告|{book_title}]]"
        if book_title not in content:
            # Find "## 相关著作" section and add
            if "## 相关著作" in content:
                content = content.replace(
                    "## 相关著作",
                    f"## 相关著作\n\n- {book_link}"
                )
            else:
                content += f"\n\n## 相关著作\n\n- {book_link}"
            
            # Update last updated date
            content = re.sub(
                r'> 🔄 \*最后更新:.*\*',
                f'> 🔄 *最后更新: {datetime.now().strftime("%Y-%m-%d")}*',
                content
            )
            
            author_file.write_text(content, encoding='utf-8')
            print(f"✅ Updated author page: {author_name}")
    else:
        # Create new author page with template
        template = f"""# {author_name}

> **领域**: {domain}  
> **机构**: 待补充  
> **知名于**: 待补充

---

## 简介

{author_name} 是{domain}领域的重要人物。

## 核心贡献

待补充...

## 相关著作

- [[{book_title} - 深度阅读报告|{book_title}]]

## 相关概念

- [[Second Brain/Database/Concepts/待补充|待补充]]

---

> 🏷️ 标签: #author #{domain.lower().replace(' ', '-')}  
> 🔄 *最后更新: {datetime.now().strftime('%Y-%m-%d')}*
"""
        author_file.write_text(template, encoding='utf-8')
        print(f"✅ Created author page: {author_name}")


def update_concept_page(vault_path: str, concept_name: str, book_title: str, context: str = "") -> None:
    """Update or create concept page."""
    concept_file = Path(vault_path) / "Second Brain" / "Database" / "Concepts" / f"{concept_name}.md"
    
    if concept_file.exists():
        content = concept_file.read_text(encoding='utf-8')
        
        # Add book reference if not exists
        book_ref = f"[[{book_title} - 深度阅读报告|{book_title}]]"
        if book_title not in content:
            # Add to related works or see also section
            if "## 相关著作" in content:
                if book_ref not in content:
                    content = content.replace(
                        "## 相关著作",
                        f"## 相关著作\n\n- {book_ref} — {context}"
                    )
            else:
                content += f"\n\n## 相关著作\n\n- {book_ref} — {context}"
            
            # Update last updated
            content = re.sub(
                r'> 🔄 \*最后更新:.*\*',
                f'> 🔄 *最后更新: {datetime.now().strftime("%Y-%m-%d")}*',
                content
            )
            
            concept_file.write_text(content, encoding='utf-8')
            print(f"✅ Updated concept page: {concept_name}")
    else:
        # Create new concept page
        template = f"""# {concept_name}

> **定义**: 待补充  
> **来源**: [[{book_title} - 深度阅读报告|{book_title}]]  
> **应用领域**: 待补充

---

## 核心定义

{context}

## 详细解释

待补充...

## 实践应用

待补充...

## 相关概念

- [[Second Brain/Database/Concepts/待补充|待补充]]

## 相关著作

- [[{book_title} - 深度阅读报告|{book_title}]]

---

> 🏷️ 标签: #concept  
> 🔄 *最后更新: {datetime.now().strftime('%Y-%m-%d')}*
"""
        concept_file.write_text(template, encoding='utf-8')
        print(f"✅ Created concept page: {concept_name}")


def update_domain_moc(vault_path: str, domain: str, book_title: str, author: str, concepts: list) -> None:
    """Update Domain MOC (Map of Content)."""
    # Map domain names to file names
    domain_map = {
        "博弈论": "博弈论与决策科学",
        "政治科学": "博弈论与决策科学",
        "行为经济学": "博弈论与决策科学",
        "game-theory": "博弈论与决策科学",
        "决策科学": "博弈论与决策科学",
        "基督教育儿学": "育儿与家庭神学",
        "家庭神学": "育儿与家庭神学",
        "基督教辅导": "育儿与家庭神学",
        "parenting": "育儿与家庭神学",
        "theology": "育儿与家庭神学",
    }
    
    moc_name = domain_map.get(domain, domain)
    moc_file = Path(vault_path) / "Second Brain" / "MOCs" / f"{moc_name}.md"
    
    # Create MOC if doesn't exist
    if not moc_file.exists():
        template = f"""# {moc_name}

> **定义**: 待补充  
> **核心问题**: 待补充  
> **应用领域**: 待补充

---

## 🎯 核心概念 (Core Concepts)

待补充...

## 👤 关键人物 (Key People)

- [[Authors/{author}|{author}]]

## 📚 核心著作 (Key Works)

- [[{book_title} - 深度阅读报告|{book_title}]]

---

> 🏷️ 标签: #MOC  
> 🔄 *最后更新: {datetime.now().strftime('%Y-%m-%d')}*
"""
        moc_file.write_text(template, encoding='utf-8')
        print(f"✅ Created domain MOC: {moc_name}")
    else:
        # Update existing MOC
        content = moc_file.read_text(encoding='utf-8')
        
        # Add author if not exists
        author_link = f"[[Authors/{author}|{author}]]"
        if author not in content and "## 👤 关键人物" in content:
            content = content.replace(
                "## 👤 关键人物",
                f"## 👤 关键人物\n\n- {author_link}"
            )
        
        # Add book if not exists
        book_link = f"[[{book_title} - 深度阅读报告|{book_title}]]"
        if book_title not in content and "## 📚 核心著作" in content:
            content = content.replace(
                "## 📚 核心著作",
                f"## 📚 核心著作\n\n- {book_link}"
            )
        
        # Add concepts
        if "## 🎯 核心概念" in content:
            for concept in concepts:
                concept_link = f"[[Second Brain/Database/Concepts/{concept}|{concept}]]"
                if concept not in content:
                    content = content.replace(
                        "## 🎯 核心概念 (Core Concepts)",
                        f"## 🎯 核心概念 (Core Concepts)\n\n- {concept_link}"
                    )
        
        # Update timestamp
        content = re.sub(
            r'> 🔄 \*最后更新:.*\*',
            f'> 🔄 *最后更新: {datetime.now().strftime("%Y-%m-%d")}*',
            content
        )
        
        moc_file.write_text(content, encoding='utf-8')
        print(f"✅ Updated domain MOC: {moc_name}")


def update_knowledge_base_index(vault_path: str, author: str = None, concepts: list = None, domain: str = None) -> None:
    """Update main knowledge base index."""
    index_file = Path(vault_path) / "Second Brain" / "Database" / "📚 知识库索引.md"
    
    if not index_file.exists():
        # Create new index
        template = f"""# 📚 知识库索引

> 本知识库包含作者档案、核心概念和跨学科连接。

---

## 👤 作者档案 (Authors)

{f"- [[Authors/{author}|{author}]]" if author else "待添加..."}

## 💡 核心概念 (Concepts)

{chr(10).join([f"- [[Second Brain/Database/Concepts/{c}|{c}]]" for c in concepts]) if concepts else "待添加..."}

---

> 🔄 *最后更新: {datetime.now().strftime('%Y-%m-%d')}*
"""
        index_file.write_text(template, encoding='utf-8')
        print("✅ Created knowledge base index")
    else:
        # Update existing index
        content = index_file.read_text(encoding='utf-8')
        
        # Add author
        if author and author not in content:
            if "## 👤 作者档案" in content:
                content = content.replace(
                    "## 👤 作者档案 (Authors)",
                    f"## 👤 作者档案 (Authors)\n\n- [[Authors/{author}|{author}]]"
                )
        
        # Add concepts
        if concepts:
            for concept in concepts:
                if concept not in content:
                    if "## 💡 核心概念" in content:
                        content = content.replace(
                            "## 💡 核心概念 (Concepts)",
                            f"## 💡 核心概念 (Concepts)\n\n- [[Second Brain/Database/Concepts/{concept}|{concept}]]"
                        )
        
        # Update stats
        content = re.sub(
            r'> 📊 \*当前统计:.*\*',
            f'> 📊 *当前统计: 更新中...*',
            content
        )
        
        content = re.sub(
            r'> 🔄 \*最后更新:.*\*',
            f'> 🔄 *最后更新: {datetime.now().strftime("%Y-%m-%d")}*',
            content
        )
        
        index_file.write_text(content, encoding='utf-8')
        print("✅ Updated knowledge base index")


def main():
    parser = argparse.ArgumentParser(description='Update Obsidian knowledge base')
    parser.add_argument('--vault', required=True, help='Path to Obsidian vault')
    parser.add_argument('--title', required=True, help='Book title')
    parser.add_argument('--author', required=True, help='Author name')
    parser.add_argument('--domain', required=True, help='Domain/field')
    parser.add_argument('--concepts', nargs='+', help='List of concepts')
    
    args = parser.parse_args()
    
    print(f"🔄 Updating knowledge base for: {args.title}")
    print(f"   Author: {args.author}")
    print(f"   Domain: {args.domain}")
    print(f"   Concepts: {args.concepts}")
    print()
    
    # Update author page
    update_author_page(args.vault, args.author, args.title, args.domain)
    
    # Update concept pages
    if args.concepts:
        for concept in args.concepts:
            update_concept_page(args.vault, concept, args.title, f"From {args.title}")
    
    # Update domain MOC
    update_domain_moc(args.vault, args.domain, args.title, args.author, args.concepts or [])
    
    # Update main index
    update_knowledge_base_index(args.vault, args.author, args.concepts, args.domain)
    
    print()
    print("✅ Knowledge base update complete!")


if __name__ == '__main__':
    main()
