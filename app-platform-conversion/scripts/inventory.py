#!/usr/bin/env python3
"""Report conventional project markers and available platform tools, without editing files."""
import argparse
import json
import shutil
from pathlib import Path

MARKERS = ("AGENTS.md", "README.md", "package.json", "web/package.json", "Cargo.toml", "go.mod", "pyproject.toml", "requirements.txt", "pom.xml", "build.gradle", "settings.gradle", "android/app/build.gradle", "pubspec.yaml", "Gemfile", "Package.swift", "stack.yaml", "words.txt", "Dockerfile")
TOOLS = ("git", "node", "npm", "python3", "java", "gradle", "adb", "sdkmanager", "xcodebuild", "flutter", "ghc", "wasm32-wasi-ghc")

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("root", type=Path, help="existing project directory")
    args = p.parse_args()
    root = args.root.expanduser().resolve()
    if not root.is_dir():
        p.error(f"not a directory: {root}")
    print(json.dumps({"root": str(root), "markers": [m for m in MARKERS if (root / m).is_file()],
                      "cabal_files": sorted(x.name for x in root.glob("*.cabal") if x.is_file()),
                      "tools": {t: shutil.which(t) for t in TOOLS}}, indent=2))

if __name__ == "__main__":
    main()
