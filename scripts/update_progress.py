#!/usr/bin/env python3
"""
Auto-update progress badges in README.md based on completed questions.

This script scans all pattern markdown files, counts completed questions (✅),
and updates the progress badges in README.md accordingly.

Usage:
    python update_progress.py

Author: LeetCode Patterns Mastery
"""

import re
import os
from pathlib import Path

# Configuration
PATTERNS_DIR = Path(__file__).parent.parent / "patterns"
README_PATH = Path(__file__).parent.parent / "README.md"
TOTAL_QUESTIONS = 150

def count_completed_in_file(file_path: Path) -> tuple[int, int]:
    """Count total and completed questions in a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the problems table
    table_match = re.search(r'\| # \|.*?\n([\s\S]*?)(?=\n---|\n## |$)', content)
    if not table_match:
        return 0, 0

    table_content = table_match.group(0)

    # Count rows with ✅ (completed) and ⬜ (pending)
    completed = len(re.findall(r'✅', table_content))
    total = len(re.findall(r'[✅⬜]', table_content))

    return total, completed

def count_all_progress() -> tuple[int, int]:
    """Count total progress across all pattern files."""
    total_questions = 0
    completed_questions = 0

    for md_file in sorted(PATTERNS_DIR.glob("*.md")):
        total, completed = count_completed_in_file(md_file)
        total_questions += total
        completed_questions += completed

    return total_questions, completed_questions

def update_readme_badges(completed: int, total: int):
    """Update the badges in README.md with current progress."""
    with open(README_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    progress_percent = round((completed / total) * 100) if total > 0 else 0

    # Update badges
    content = re.sub(
        r'!\[Total\]\(https://img\.shields\.io/badge/Total-\d+-blue\?style=for-the-badge\)',
        f'![Total](https://img.shields.io/badge/Total-{total}-blue?style=for-the-badge)',
        content
    )

    content = re.sub(
        r'!\[Completed\]\(https://img\.shields\.io/badge/Completed-\d+-red\?style=for-the-badge\)',
        f'![Completed](https://img.shields.io/badge/Completed-{completed}-red?style=for-the-badge)',
        content
    )

    content = re.sub(
        r'!\[Progress\]\(https://img\.shields\.io/badge/Progress-\d+%25-orange\?style=for-the-badge\)',
        f'![Progress](https://img.shields.io/badge/Progress-{progress_percent}%25-orange?style=for-the-badge)',
        content
    )

    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.write(content)

    return progress_percent

def main():
    """Main function to update all progress indicators."""
    print("🔍 Scanning pattern files...")

    # Count progress
    total, completed = count_all_progress()

    print(f"📊 Total Questions: {total}")
    print(f"✅ Completed: {completed}")

    if total > 0:
        progress = round((completed / total) * 100)
        print(f"📈 Progress: {progress}%")

        # Update README
        print("\n📝 Updating README.md badges...")
        update_readme_badges(completed, total)
        print("✨ Badges updated successfully!")

        # Print summary
        print("\n" + "="*50)
        print("📊 PROGRESS SUMMARY")
        print("="*50)
        print(f"  Total Questions:    {total}")
        print(f"  Completed:          {completed}")
        print(f"  Remaining:          {total - completed}")
        print(f"  Progress:           {progress}%")
        print("="*50)
    else:
        print("⚠️  No questions found in pattern files!")

if __name__ == "__main__":
    main()
