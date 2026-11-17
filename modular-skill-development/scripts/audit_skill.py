#!/usr/bin/env python3
"""Advisory checks for a skill's structure and local Markdown links."""
import argparse
import re
from pathlib import Path
from urllib.parse import unquote


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('skill', type=Path)
    args = parser.parse_args()
    root = args.skill.resolve()
    entry = root / 'SKILL.md'
    if not entry.is_file():
        parser.error('SKILL.md not found in skill directory')
    issues = []
    for doc in root.rglob('*.md'):
        text = doc.read_text(encoding='utf-8')
        for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', text):
            target = unquote(target.split('#', 1)[0].strip().split(' ', 1)[0])
            if not target or '://' in target or target.startswith(('mailto:', 'skill:')):
                continue
            if not (doc.parent / target).exists():
                issues.append(f'{doc.relative_to(root)}: missing link {target}')
    print(f'SKILL.md: {len(entry.read_text(encoding="utf-8").splitlines())} lines')
    for directory in ('scripts', 'references', 'assets'):
        d = root / directory
        print(f'{directory}: {sum(p.is_file() for p in d.rglob("*")) if d.is_dir() else 0} files')
    for issue in issues:
        print('ISSUE:', issue)
    print('Advisory only: verify behavior and judgment separately.')
    return bool(issues)


if __name__ == '__main__':
    raise SystemExit(main())
