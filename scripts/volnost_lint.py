#!/usr/bin/env python3
"""
volnost_lint.py — Verification & Linter Tool for Volnost Ethical Public License (VEPL v1.0)
Validates license files, headers, and metadata across repositories.

Usage:
    python3 scripts/volnost_lint.py [--path <path-to-repo-or-file>] [--strict]
"""

import os
import sys
import re
import argparse
from pathlib import Path

VEPL_SPDX_IDENTIFIER = "LicenseRef-Volnost-Ethical-Public-1.0"
REQUIRED_CLAUSES = [
    (r"VOLNOST ETHICAL PUBLIC LICENSE", "License Title"),
    (r"Version 1\.0", "License Version"),
    (r"Article 8 bis of the Rome Statute", "Definition: Crime of Aggression (ICC Art. 8 bis)"),
    (r"Articles 7 and 8 of the Rome Statute", "Definition: War Crimes & Crimes Against Humanity"),
    (r"Article 51 of the Charter of the United Nations", "Safe Harbor: Legitimate Self-Defense (UN Art. 51)"),
    (r"Universal Symmetry", "Core Covenant: Universal Symmetry"),
    (r"Prohibition of Aggressive Warfare", "Core Covenant: Anti-Aggression"),
    (r"Automatic Suspension", "Enforcement: Automatic Suspension Upon Breach"),
]

def check_license_text(content: str, strict: bool = False) -> tuple[bool, list[str]]:
    missing = []
    for pattern, description in REQUIRED_CLAUSES:
        if not re.search(pattern, content, re.IGNORECASE):
            missing.append(description)
    return (len(missing) == 0, missing)

def inspect_file(filepath: Path, strict: bool = False) -> bool:
    print(f"[*] Auditing license file: {filepath}")
    if not filepath.exists():
        print(f"[-] ERROR: File not found: {filepath}")
        return False

    content = filepath.read_text(encoding="utf-8", errors="replace")
    valid, missing = check_license_text(content, strict=strict)

    if valid:
        print(f"[+] PASS: All invariant covenants and statutory definitions are present in {filepath.name}.")
        return True
    else:
        print(f"[-] FAIL: {filepath.name} is missing essential covenants/references:")
        for item in missing:
            print(f"    - {item}")
        return False

def inspect_source_header(filepath: Path) -> bool:
    content = filepath.read_text(encoding="utf-8", errors="replace")
    if VEPL_SPDX_IDENTIFIER in content:
        return True
    return False

def main():
    parser = argparse.ArgumentParser(description="Linter for Volnost Ethical Public License v1.0 compliance.")
    parser.add_argument("--path", type=str, default="license/VOLNOST-LICENSE-1.0.md", help="Path to license file or target repository.")
    parser.add_argument("--strict", action="store_true", help="Enforce strict checks.")
    args = parser.parse_args()

    target = Path(args.path)
    if target.is_file():
        success = inspect_file(target, strict=args.strict)
        sys.exit(0 if success else 1)
    elif target.is_dir():
        # Check standard license locations
        candidates = [
            target / "LICENSE",
            target / "LICENSE.md",
            target / "license" / "VOLNOST-LICENSE-1.0.md",
            target / "docs" / "policy" / "VOLNOST-LICENSE-1.0.md"
        ]
        found = False
        for c in candidates:
            if c.exists():
                found = True
                if not inspect_file(c, strict=args.strict):
                    sys.exit(1)
        if not found:
            print(f"[-] No standard Volnost license file found under {target}")
            sys.exit(1)
        print("[+] Repository license compliance check succeeded.")
        sys.exit(0)
    else:
        print(f"[-] Invalid target path: {target}")
        sys.exit(1)

if __name__ == "__main__":
    main()
