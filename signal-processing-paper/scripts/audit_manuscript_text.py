#!/usr/bin/env python3
"""Lightweight advisory audit for signal-processing manuscript text."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


SUPPORTED_SUFFIXES = {".md", ".tex", ".txt"}


@dataclass
class Finding:
    severity: str
    path: str
    line: int
    rule: str
    message: str
    excerpt: str


RULES = [
    (
        "blocking",
        "placeholder",
        re.compile(r"\b(?:TODO|TBD|FIXME|XXX)\b|\[\s*(?:REF|CITATION NEEDED|NEEDS EVIDENCE)[^\]]*\]|\?\?+", re.I),
        "Resolve the placeholder before submission.",
    ),
    (
        "major",
        "unqualified-overclaim",
        re.compile(r"\b(?:the first|first-ever|novel|state[- ]of[- ]the[- ]art|superior|significantly better|excellent performance)\b", re.I),
        "Verify the literature or quantitative evidence and qualify this claim.",
    ),
    (
        "major",
        "robustness-claim",
        re.compile(r"\b(?:robust|robustness)\b", re.I),
        "Tie robustness language to a defined disturbance model, severity range, metric, and repeated-run evidence.",
    ),
    (
        "major",
        "notation-collision",
        re.compile(r"(?:MCC.{0,35}(?:parameter|kernel width).{0,12}\b[Kk]\b|\b[Kk]\b.{0,12}(?:parameter|kernel width).{0,35}MCC)", re.I),
        "Avoid K/k for the MCC parameter when Kronecker rank or term count may also use K; prefer sigma_c and R.",
    ),
    (
        "major",
        "citation-placeholder",
        re.compile(r"\[(?:\s*\?|\s*\d*\s*-\s*\?|\s*REF\s*)\]", re.I),
        "Replace the citation placeholder with a verified source.",
    ),
]


ALIASES = {
    "RFF+NLMS+MCC": re.compile(r"RFF\s*\+\s*NLMS\s*\+\s*MCC", re.I),
    "RFF+FxNLMS+MCC": re.compile(r"RFF\s*\+\s*FxNLMS\s*\+\s*MCC", re.I),
    "RFFxMCC": re.compile(r"\bRFFxMCC\b", re.I),
    "NKP-RFFxMCC": re.compile(r"\bNKP[-+ ]RFFxMCC\b", re.I),
    "NKP-RFF-FxNLMS-MCC": re.compile(r"NKP\s*[-+]\s*RFF\s*[-+]\s*FxNLMS\s*[-+]\s*MCC", re.I),
}


def collect_files(inputs: list[str]) -> list[Path]:
    files: list[Path] = []
    for raw in inputs:
        path = Path(raw)
        if path.is_dir():
            files.extend(
                candidate
                for candidate in path.rglob("*")
                if candidate.is_file() and candidate.suffix.lower() in SUPPORTED_SUFFIXES
            )
        elif path.is_file() and path.suffix.lower() in SUPPORTED_SUFFIXES:
            files.append(path)
        else:
            print(f"warning: skipped unsupported or missing path: {path}", file=sys.stderr)
    return sorted(set(files))


def audit_file(path: Path) -> list[Finding]:
    text = path.read_text(encoding="utf-8", errors="replace")
    findings: list[Finding] = []
    alias_hits: dict[str, list[int]] = {name: [] for name in ALIASES}

    for number, line in enumerate(text.splitlines(), start=1):
        for severity, rule, pattern, message in RULES:
            if pattern.search(line):
                findings.append(
                    Finding(severity, str(path), number, rule, message, line.strip()[:240])
                )
        for name, pattern in ALIASES.items():
            if pattern.search(line):
                alias_hits[name].append(number)

    used_aliases = {name: lines for name, lines in alias_hits.items() if lines}
    if len(used_aliases) > 1:
        summary = "; ".join(f"{name} at {lines[:6]}" for name, lines in used_aliases.items())
        findings.append(
            Finding(
                "major",
                str(path),
                1,
                "algorithm-alias-consistency",
                "Multiple algorithm naming forms were found. Confirm whether they denote distinct algorithms; otherwise choose one canonical name.",
                summary,
            )
        )
    return findings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Advisory audit for placeholders, overclaims, notation risks, and naming inconsistency."
    )
    parser.add_argument("paths", nargs="+", help=".txt, .md, or .tex files or directories")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="exit with status 1 when blocking or major findings exist",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    files = collect_files(args.paths)
    if not files:
        print("No supported manuscript files found.", file=sys.stderr)
        return 2

    findings = [finding for path in files for finding in audit_file(path)]
    if args.json:
        print(json.dumps([asdict(item) for item in findings], ensure_ascii=False, indent=2))
    elif findings:
        for item in findings:
            print(
                f"{item.severity.upper():8} {item.path}:{item.line} "
                f"[{item.rule}] {item.message}\n  {item.excerpt}"
            )
        print(f"\n{len(findings)} finding(s) across {len(files)} file(s).")
    else:
        print(f"No configured text-audit findings across {len(files)} file(s).")

    severe = any(item.severity in {"blocking", "major"} for item in findings)
    return 1 if args.strict and severe else 0


if __name__ == "__main__":
    raise SystemExit(main())
