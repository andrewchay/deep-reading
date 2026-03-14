#!/usr/bin/env python3
"""
Automatically update Obsidian knowledge base after generating a reading report.
Updates: Author pages, Concept pages, Domain MOCs, and Knowledge Base Index.
Compatible with Kimi CLI, Claude Code, and other AI coding assistants.
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


def update_author_page(vault_path: str, author_name: str, book_title: str, domain: str, language: str = "en") -> None:
    """Update or create author page."""
    author_file = Path(vault_path) / "Second Brain" / "Database" / "Authors" / f"{author_name}.md"
    
    report_suffix = " - Deep Reading Report" if language == "en" else " - 深度阅读报告"
    book_link = f"[[{book_title}{report_suffix}|{book_title}]]"
    
    # Check if file exists
    if author_file.exists():
        content = author_file.read_text(encoding='utf-8')
        
        # Add book link if not exists
        if book_title not in content:
            # Find "## Related Works" or "## 相关著作" section and add
            if "## Related Works" in content or "## 相关著作" in content:
                content = content.replace(
                    "## Related Works",
                    f"## Related Works\n\n- {book_link}"
                )
                content = content.replace(
                    "## 相关著作",
                    f"## 相关著作\n\n- {book_link}"
                )
            else:
                content += f"\n\n## Related Works\n\n- {book_link}"
            
            # Update last updated date
            content = re.sub(
                r'> 🔄 \*Last Updated:.*\*|> 🔄 \*最后更新:.*\*',
                f'> 🔄 *Last Updated: {datetime.now().strftime("%Y-%m-%d")}*',
                content
            )
            
            author_file.write_text(content, encoding='utf-8')
            print(f"✅ Updated author page: {author_name}")
    else:
        # Create new author page with template
        if language == "zh":
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

- {book_link}

## 相关概念

- [[Second Brain/Database/Concepts/TBD|TBD]]

---

> 🏷️ 标签: #author #{domain.lower().replace(' ', '-')}  
> 🔄 *最后更新: {datetime.now().strftime('%Y-%m-%d')}*
"""
        else:
            template = f"""# {author_name}

> **Domain**: {domain}  
> **Institution**: TBD  
> **Known For**: TBD

---

## Biography

{author_name} is an important figure in the field of {domain}.

## Core Contributions

To be added...

## Related Works

- {book_link}

## Related Concepts

- [[Second Brain/Database/Concepts/TBD|TBD]]

---

> 🏷️ Tags: #author #{domain.lower().replace(' ', '-')}  
> 🔄 *Last Updated: {datetime.now().strftime('%Y-%m-%d')}*
"""
        author_file.write_text(template, encoding='utf-8')
        print(f"✅ Created author page: {author_name}")


def update_concept_page(vault_path: str, concept_name: str, book_title: str, context: str = "", language: str = "en") -> None:
    """Update or create concept page."""
    concept_file = Path(vault_path) / "Second Brain" / "Database" / "Concepts" / f"{concept_name}.md"
    
    report_suffix = " - Deep Reading Report" if language == "en" else " - 深度阅读报告"
    book_ref = f"[[{book_title}{report_suffix}|{book_title}]]"
    
    if concept_file.exists():
        content = concept_file.read_text(encoding='utf-8')
        
        # Add book reference if not exists
        if book_title not in content:
            # Add to related works or see also section
            if "## Related Works" in content or "## 相关著作" in content:
                if book_ref not in content:
                    content = content.replace(
                        "## Related Works",
                        f"## Related Works\n\n- {book_ref} — {context}"
                    )
                    content = content.replace(
                        "## 相关著作",
                        f"## 相关著作\n\n- {book_ref} — {context}"
                    )
            else:
                content += f"\n\n## Related Works\n\n- {book_ref} — {context}"
            
            # Update last updated
            content = re.sub(
                r'> 🔄 \*Last Updated:.*\*|> 🔄 \*最后更新:.*\*',
                f'> 🔄 *Last Updated: {datetime.now().strftime("%Y-%m-%d")}*',
                content
            )
            
            concept_file.write_text(content, encoding='utf-8')
            print(f"✅ Updated concept page: {concept_name}")
    else:
        # Create new concept page
        if language == "zh":
            template = f"""# {concept_name}

> **定义**: 待补充  
> **来源**: {book_ref}  
> **应用领域**: 待补充

---

## 核心定义

{context}

## 详细解释

待补充...

## 实践应用

待补充...

## 相关概念

- [[Second Brain/Database/Concepts/TBD|TBD]]

## 相关著作

- {book_ref}

---

> 🏷️ 标签: #concept  
> 🔄 *最后更新: {datetime.now().strftime('%Y-%m-%d')}*
"""
        else:
            template = f"""# {concept_name}

> **Definition**: TBD  
> **Source**: {book_ref}  
> **Application Areas**: TBD

---

## Core Definition

{context}

## Detailed Explanation

To be added...

## Practical Applications

To be added...

## Related Concepts

- [[Second Brain/Database/Concepts/TBD|TBD]]

## Related Works

- {book_ref}

---

> 🏷️ Tags: #concept  
> 🔄 *Last Updated: {datetime.now().strftime('%Y-%m-%d')}*
"""
        concept_file.write_text(template, encoding='utf-8')
        print(f"✅ Created concept page: {concept_name}")


def update_domain_moc(vault_path: str, domain: str, book_title: str, author: str, concepts: list, language: str = "en") -> None:
    """Update Domain MOC (Map of Content)."""
    # Map domain names to file names (could be extended)
    domain_map = {
        "game theory": "Game Theory and Decision Science",
        "decision science": "Game Theory and Decision Science",
        "parenting": "Parenting and Family Theology",
        "family theology": "Parenting and Family Theology",
        "theology": "Parenting and Family Theology",
    }
    
    moc_name = domain_map.get(domain.lower(), domain)
    moc_file = Path(vault_path) / "Second Brain" / "MOCs" / f"{moc_name}.md"
    
    report_suffix = " - Deep Reading Report" if language == "en" else " - 深度阅读报告"
    
    # Create MOC if doesn't exist
    if not moc_file.exists():
        if language == "zh":
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

- [[{book_title}{report_suffix}|{book_title}]]

---

> 🏷️ 标签: #MOC  
> 🔄 *最后更新: {datetime.now().strftime('%Y-%m-%d')}*
"""
        else:
            template = f"""# {moc_name}

> **Definition**: TBD  
> **Core Questions**: TBD  
> **Applications**: TBD

---

## 🎯 Core Concepts

TBD...

## 👤 Key People

- [[Authors/{author}|{author}]]

## 📚 Key Works

- [[{book_title}{report_suffix}|{book_title}]]

---

> 🏷️ Tags: #MOC  
> 🔄 *Last Updated: {datetime.now().strftime('%Y-%m-%d')}*
"""
        moc_file.write_text(template, encoding='utf-8')
        print(f"✅ Created domain MOC: {moc_name}")
    else:
        # Update existing MOC
        content = moc_file.read_text(encoding='utf-8')
        
        # Add author if not exists
        author_link = f"[[Authors/{author}|{author}]]"
        if author not in content and ("## 👤 关键人物" in content or "## 👤 Key People" in content):
            content = content.replace(
                "## 👤 关键人物 (Key People)",
                f"## 👤 关键人物 (Key People)\n\n- {author_link}"
            )
            content = content.replace(
                "## 👤 Key People",
                f"## 👤 Key People\n\n- {author_link}"
            )
        
        # Add book if not exists
        book_link = f"[[{book_title}{report_suffix}|{book_title}]]"
        if book_title not in content and ("## 📚 核心著作" in content or "## 📚 Key Works" in content):
            content = content.replace(
                "## 📚 核心著作 (Key Works)",
                f"## 📚 核心著作 (Key Works)\n\n- {book_link}"
            )
            content = content.replace(
                "## 📚 Key Works",
                f"## 📚 Key Works\n\n- {book_link}"
            )
        
        # Add concepts
        if "## 🎯 核心概念" in content or "## 🎯 Core Concepts" in content:
            for concept in concepts:
                concept_link = f"[[Second Brain/Database/Concepts/{concept}|{concept}]]"
                if concept not in content:
                    content = content.replace(
                        "## 🎯 核心概念 (Core Concepts)",
                        f"## 🎯 核心概念 (Core Concepts)\n\n- {concept_link}"
                    )
                    content = content.replace(
                        "## 🎯 Core Concepts",
                        f"## 🎯 Core Concepts\n\n- {concept_link}"
                    )
        
        # Update timestamp
        content = re.sub(
            r'> 🔄 \*Last Updated:.*\*|> 🔄 \*最后更新:.*\*',
            f'> 🔄 *Last Updated: {datetime.now().strftime("%Y-%m-%d")}*',
            content
        )
        
        moc_file.write_text(content, encoding='utf-8')
        print(f"✅ Updated domain MOC: {moc_name}")


def update_knowledge_base_index(vault_path: str, author: str = None, concepts: list = None, domain: str = None, language: str = "en") -> None:
    """Update main knowledge base index."""
    index_file = Path(vault_path) / "Second Brain" / "Database" / "📚 Knowledge Base Index.md"
    
    if not index_file.exists():
        # Create new index
        if language == "zh":
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
        else:
            template = f"""# 📚 Knowledge Base Index

> This knowledge base contains author profiles, core concepts, and interdisciplinary connections.

---

## 👤 Authors

{f"- [[Authors/{author}|{author}]]" if author else "TBD..."}

## 💡 Core Concepts

{chr(10).join([f"- [[Second Brain/Database/Concepts/{c}|{c}]]" for c in concepts]) if concepts else "TBD..."}

---

> 🔄 *Last Updated: {datetime.now().strftime('%Y-%m-%d')}*
"""
        index_file.write_text(template, encoding='utf-8')
        print("✅ Created knowledge base index")
    else:
        # Update existing index
        content = index_file.read_text(encoding='utf-8')
        
        # Add author
        if author and author not in content:
            if "## 👤 Authors" in content or "## 👤 作者档案" in content:
                content = content.replace(
                    "## 👤 Authors (Authors)",
                    f"## 👤 Authors (Authors)\n\n- [[Authors/{author}|{author}]]"
                )
                content = content.replace(
                    "## 👤 作者档案 (Authors)",
                    f"## 👤 作者档案 (Authors)\n\n- [[Authors/{author}|{author}]]"
                )
        
        # Add concepts
        if concepts:
            for concept in concepts:
                if concept not in content:
                    if "## 💡 Core Concepts" in content or "## 💡 核心概念" in content:
                        content = content.replace(
                            "## 💡 Core Concepts (Concepts)",
                            f"## 💡 Core Concepts (Concepts)\n\n- [[Second Brain/Database/Concepts/{concept}|{concept}]]"
                        )
                        content = content.replace(
                            "## 💡 核心概念 (Concepts)",
                            f"## 💡 核心概念 (Concepts)\n\n- [[Second Brain/Database/Concepts/{concept}|{concept}]]"
                        )
        
        # Update stats
        content = re.sub(
            r'> 📊 \*Statistics:.*\*|> 📊 \*当前统计:.*\*',
            f'> 📊 *Statistics: Updating...*',
            content
        )
        
        content = re.sub(
            r'> 🔄 \*Last Updated:.*\*|> 🔄 \*最后更新:.*\*',
            f'> 🔄 *Last Updated: {datetime.now().strftime("%Y-%m-%d")}*',
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
    parser.add_argument('--language', default='en', choices=['en', 'zh'], help='Language')
    
    args = parser.parse_args()
    
    print(f"🔄 Updating knowledge base for: {args.title}")
    print(f"   Author: {args.author}")
    print(f"   Domain: {args.domain}")
    print(f"   Concepts: {args.concepts}")
    print(f"   Language: {args.language}")
    print()
    
    # Update author page
    update_author_page(args.vault, args.author, args.title, args.domain, args.language)
    
    # Update concept pages
    if args.concepts:
        for concept in args.concepts:
            update_concept_page(args.vault, concept, args.title, f"From {args.title}", args.language)
    
    # Update domain MOC
    update_domain_moc(args.vault, args.domain, args.title, args.author, args.concepts or [], args.language)
    
    # Update main index
    update_knowledge_base_index(args.vault, args.author, args.concepts, args.domain, args.language)
    
    print()
    print("✅ Knowledge base update complete!")


if __name__ == '__main__':
    main()
