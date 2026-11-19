import argparse
import json
import re
from pathlib import Path

SPDX = re.compile(r"SPDX-License-Identifier:\s*([A-Za-z0-9.+-]+)")
DEFAULT_EXTENSIONS = {".py", ".js", ".ts", ".tsx", ".jsx", ".go", ".sh", ".css", ".java", ".rs"}

def inspect_text(text, max_lines=5):
    for number, line in enumerate(text.splitlines()[:max_lines], start=1):
        match = SPDX.search(line)
        if match:
            return {"found": True, "line": number, "identifier": match.group(1)}
    return {"found": False, "line": None, "identifier": None}

def scan(root, max_lines=5, extensions=None):
    extensions = extensions or DEFAULT_EXTENSIONS
    ignored = {".git", ".venv", "venv", "node_modules", "__pycache__", "dist", "build"}
    paths = [root] if root.is_file() else sorted(p for p in root.rglob("*") if p.is_file())
    findings = []
    for path in paths:
        if path.suffix.lower() not in extensions or any(part in ignored for part in path.parts):
            continue
        result = inspect_text(path.read_text(encoding="utf-8", errors="replace"), max_lines)
        if not result["found"]:
            findings.append({"path": str(path), "issue": "missing-spdx-header"})
    return findings

def main():
    parser = argparse.ArgumentParser(description="Find source files without SPDX license headers.")
    parser.add_argument("path", type=Path)
    parser.add_argument("--lines", type=int, default=5)
    parser.add_argument("--extensions", default=",".join(sorted(DEFAULT_EXTENSIONS)))
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.lines < 1 or not args.path.exists():
        parser.error("Provide an existing path and a positive --lines value.")
    extensions = {value.strip().lower() if value.strip().startswith(".") else "." + value.strip().lower()
                  for value in args.extensions.split(",") if value.strip()}
    findings = scan(args.path, args.lines, extensions)
    if args.json:
        print(json.dumps(findings, indent=2))
    else:
        for item in findings:
            print(f"{item['path']}: missing SPDX header")
        print(f"\n{len(findings)} file(s) missing headers.")

if __name__ == "__main__":
    main()
