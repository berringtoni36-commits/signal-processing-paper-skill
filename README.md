# signal-processing-paper skill

A Codex skill for planning, drafting, revising, and reviewing manuscripts aimed at Elsevier's *Signal Processing*, with a focused workflow for nonlinear active noise control and adaptive filtering using RFF, FxNLMS/NLMS, nearest-Kronecker or low-rank models, and maximum correntropy.

The repository contains writing and review instructions, a journal-format snapshot, a literature seed map, experiment and figure checklists, and a lightweight manuscript text auditor. It intentionally contains no unpublished manuscript, private figure, experiment data, or source code from a research project.

## Install

Copy the `signal-processing-paper` directory into your Codex skills directory:

```text
%USERPROFILE%\.codex\skills\signal-processing-paper
```

Restart or refresh Codex skill discovery if the skill is not shown immediately.

## Use

Example prompts:

```text
Use $signal-processing-paper to build a claim-evidence ledger for my NKP-RFF-FxNLMS-MCC paper.
Use $signal-processing-paper to audit these simulation figures for Signal Processing.
Use $signal-processing-paper to rewrite my introduction without overstating novelty.
```

For a plain-text or LaTeX draft:

```bash
python signal-processing-paper/scripts/audit_manuscript_text.py manuscript.tex --strict
```

## Scope and responsibility

The skill provides research-writing and quality-control guidance, not a substitute for author verification. Journal rules change, so the live official guide must be checked at submission time. All citations, equations, data, and claims remain the authors' responsibility.
