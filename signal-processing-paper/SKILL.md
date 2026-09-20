---
name: signal-processing-paper
description: Plan, draft, revise, and audit research papers for Elsevier Signal Processing in nonlinear active noise control and adaptive filtering, especially work involving random Fourier features, filtered-x NLMS, nearest-Kronecker or low-rank models, and maximum correntropy. Use for literature positioning, contribution design, derivation and complexity checks, experiment planning, figure and table preparation, manuscript section writing, citation verification, reviewer simulation, and submission-readiness checks. Do not use for generic signal-processing questions or patent drafting.
---

# Signal Processing Paper

Use this skill to turn an algorithm and its experiments into a defensible journal manuscript. Treat the manuscript as a chain of claims, derivations, and evidence rather than as a prose-only task.

## Evidence Contract

- Never invent citations, equations, experimental values, channel models, hyperparameters, significance tests, or implementation details.
- Separate facts supplied by the author from facts independently verified in sources.
- Mark missing support as `[NEEDS EVIDENCE: ...]` and continue with the supported parts.
- Do not call a method "first", "novel", "state of the art", "robust", or "significantly better" unless the manuscript supplies the required literature search or quantitative test.
- Do not reuse wording from reference papers. Learn their organization and evidence pattern, then write original prose.
- Do not expose unpublished manuscripts, source code, figures, or data when preparing public artifacts.

## Route the Task

Read only the references needed for the current task:

- For the target contribution and notation, read `references/project-profile.md`.
- For section architecture, paragraph logic, abstract, and contributions, read `references/writing-patterns.md`.
- For derivations, complexity, baselines, and experiments, read `references/experiment-and-theory.md`.
- For plots, captions, tables, and visual consistency, read `references/figures-and-tables.md`.
- For the journal scope, format snapshot, and submission package, read `references/signal-processing-journal.md`.
- For citation integrity and reviewer-style audit, read `references/review-and-integrity.md`.
- For a starting literature map, read `references/reference-seed.md`; verify metadata and obtain full text legally before relying on details beyond title, abstract, or bibliographic record.

## Core Workflow

1. Inventory the available evidence: draft text, equations, MATLAB or Python code, figures, path models, data, random seeds, and bibliography.
2. Write a one-sentence problem statement and a one-sentence method claim. Define what the proposed method changes relative to the strongest baseline.
3. Build a claim-evidence ledger with columns: claim, mechanism, equation or algorithm step, experiment, figure or table, source, and status.
4. Freeze notation and algorithm names before drafting. Keep Kronecker rank or term count distinct from the MCC kernel parameter.
5. Draft in this order when starting from results: system model, proposed algorithm, complexity or convergence analysis, experiment protocol, results, introduction, abstract, and conclusion.
6. Audit every comparison for equal information, equal tuning budget, equal initialization, and clearly reported computational cost.
7. Audit figures and tables before polishing prose; weak or inconsistent evidence cannot be repaired by stronger wording.
8. Recheck the live journal guide before submission because page limits, required declarations, and file requirements can change.

## Deliverable Modes

### Paper blueprint

Return a section outline plus a claim-evidence ledger, notation table, experiment matrix, and missing-evidence list.

### Section draft

State which evidence was used. Preserve equation and figure placeholders. Write restrained technical English and keep every quantitative claim traceable.

### Technical audit

Report issues by severity: blocking, major, and minor. Check dimensions, filtered-x signal flow, gradient signs, MCC derivative, normalization, update order, complexity counts, and reproducibility.

### Figure audit

Check each figure against `references/figures-and-tables.md`. Require editable or vector sources when possible. Do not accept screenshots of interactive MATLAB windows as publication figures.

### Submission audit

Use `references/signal-processing-journal.md` and `references/review-and-integrity.md`. Distinguish a current official requirement from a recommendation or an inference.

## Automated Text Audit

For `.txt`, `.md`, or `.tex` drafts, run:

```bash
python scripts/audit_manuscript_text.py PATH [PATH ...]
```

Use `--strict` in CI or before submission. The script detects placeholders, unqualified overclaims, citation gaps, notation-risk phrases, and inconsistent algorithm aliases. Treat the report as a prompt for human review, not as proof of correctness.

## Output Standard

End substantive work with:

- what is now supported;
- what remains unsupported or ambiguous;
- the highest-value next experiment or revision;
- files created or changed, if any;
- current journal requirements that were verified and their official sources.
