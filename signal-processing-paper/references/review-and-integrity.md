# Review and Research-Integrity Audit

## Citation verification

For every reference used to support a technical claim:

- verify title, authors, venue, year, volume, pages or article number, and DOI from a primary or authoritative record;
- read the full text legally before describing methods, assumptions, equations, or results in detail;
- distinguish a published version from a preprint or accepted manuscript;
- cite the primary algorithm paper rather than a later paper that merely mentions it;
- do not cite a search snippet as evidence.

Maintain a table with columns: citation key, claim supported, access level, verified metadata, full text read, and notes.

## Similarity and originality

Use related papers to learn rhetorical structure, baseline selection, and reporting depth. Do not reproduce distinctive wording, sentence order, equations without attribution, or figure designs. Re-derive the proposed method from the project's own notation and implementation.

## AI-use control

Human authors must verify all generated text, equations, citations, and claims. Do not list an AI system as an author. Check the current Elsevier policy and disclose use when required. Keep confidential manuscript content out of public tools or repositories unless the authors have explicitly authorized release.

## Reviewer simulation rubric

Score each category from 0 to 3 and justify the score with manuscript locations:

| Category | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Journal fit | unclear | application-heavy | signal-processing contribution visible | central and well motivated |
| Novelty | combination only | gap asserted | precise distinction | distinction and value convincingly demonstrated |
| Correctness | major gaps | assumptions hidden | mostly checked | dimensions, gradients, and assumptions fully auditable |
| Theory | absent | descriptive | partial analysis | analysis directly supports claims |
| Experiments | anecdotal | limited baselines | fair and repeated | comprehensive, reproducible, and diagnostic |
| Complexity | omitted | big-O only | operation/memory table | matched-budget plus runtime evidence |
| Clarity | inconsistent | understandable with effort | clear | concise, consistent, and publication-ready |
| Reproducibility | missing | partial parameters | protocol reported | code/data or complete reconstruction path |

Any zero is blocking. A score of one in novelty, correctness, experiments, or reproducibility is a major-revision condition.

## Common major-review questions

- What is new beyond a direct combination of known NKP, RFF, FxNLMS, and MCC components?
- Is the factorized update mathematically equivalent to, or only inspired by, the full update?
- Are complexity savings measured at equal nonlinear modeling capacity?
- Why were these baselines and hyperparameters selected?
- Are improvements stable across random features and Monte Carlo trials?
- Does MCC help under Gaussian conditions, or only under impulsive errors?
- How sensitive is the method to secondary-path mismatch and kernel width?
- Can the method run in real time at the claimed filter length and sample rate?
- Are chaotic and alpha-stable conditions physically motivated and reproducible?

## Decision report format

Return:

1. overall readiness: not ready, major revision, minor revision, or submission-ready;
2. blocking issues with exact manuscript locations;
3. claim-evidence mismatches;
4. required new experiments or derivations;
5. figure and notation corrections;
6. citation-verification gaps;
7. a prioritized revision sequence.
