# Writing Patterns for a Signal Processing Article

These patterns are distilled from related *Signal Processing* work and an open author-version survey on nonlinear ANC. They describe organization and reasoning, not reusable sentences.

## Recommended article architecture

1. Introduction
2. ANC system model and preliminaries
3. Proposed NKP-RFF-FxNLMS-MCC algorithm
4. Convergence, stability, and computational analysis
5. Simulation or experimental results
6. Conclusion

Move long proofs or supplementary sensitivity results to appendices only when the journal guide permits and the main argument remains complete.

## Abstract: five moves

Write one compact paragraph in this order:

1. Practical problem and why the baseline class is insufficient.
2. Specific gap: computational growth, impulsive sensitivity, or both.
3. Proposed mechanism, with the exact role of NKP, RFF, filtered-x adaptation, and MCC.
4. Analytical result: complexity or convergence result that is actually derived.
5. Quantitative evidence under named conditions, followed by a restrained conclusion.

Avoid literature review, undefined acronyms, citations, equations, and general claims such as "excellent performance" in the abstract.

## Introduction: argument sequence

Use six functional blocks:

1. Establish the ANC problem and the practical nonlinearities.
2. Explain why linear FxLMS/FxNLMS is inadequate in the stated regime.
3. Review nonlinear modeling approaches and position RFF as a fixed-dimensional approximation.
4. Review robust losses and explain what MCC addresses under non-Gaussian or impulsive errors.
5. Review low-rank/Kronecker methods and identify the unresolved integration or analysis gap.
6. State contributions, then give the paper organization.

Organize related work by limitation and mechanism, not as a chronological list of papers.

## Contribution bullets

Use two to four orthogonal bullets. Each bullet should contain:

- the new technical object;
- the mechanism or derivation;
- the evidence location;
- a bounded benefit.

Weak: "A novel robust algorithm with superior performance is proposed."

Stronger pattern: "A rank-`R` Kronecker parameterization is introduced into the RFF filtered-x controller, yielding the update in Algorithm 1 and reducing the per-sample multiplication count under the stated dimension assumptions."

Do not put measured improvements into a contribution bullet unless the result is stable across repeated runs and the comparison protocol is described.

## Method sections

Follow the signal flow. Define the plant and signals before the loss, the loss before the gradient, and the full-dimensional update before the factorized update. For every vector or matrix, give its dimension on first use.

A derivation paragraph should follow:

1. purpose of the step;
2. equation;
3. definition of new symbols;
4. assumption or approximation;
5. interpretation and computational consequence.

Do not hide a nontrivial approximation behind phrases such as "it is easy to show".

## Results sections

Start with a reproducibility subsection covering paths, feature mapping, filter lengths, noise generation, hyperparameters, seeds, run count, metrics, and hardware or software for runtime results.

For each experiment, use:

1. question;
2. controlled setup;
3. observation with values and uncertainty;
4. mechanism-based interpretation;
5. limitation or boundary condition.

Separate observation from explanation. A lower curve is an observation; the proposed reason must be supported by an ablation, analysis, or cited theory.

## Conclusion

Restate the solved problem, mechanism, principal supported findings, and remaining limitation. Do not introduce a new citation, experiment, or universal claim. Name a concrete next step, such as secondary-path mismatch tests, measured acoustic paths, or real-time implementation.

## Style controls

- Use present tense for equations and paper organization; use past tense for completed experiments.
- Prefer concrete subjects: "the factorization reduces..." rather than "it can be seen that...".
- Keep one technical claim per sentence when equations or conditions are involved.
- Define every acronym once and use it consistently.
- Use `Fig.` and `Table` according to the journal template; never alternate `Fig.`, `Figure`, and localized labels without a reason.
- Use cautious verbs: `indicates`, `suggests`, or `outperforms under the tested conditions` when the evidence is empirical.
