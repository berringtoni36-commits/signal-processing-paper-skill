# Theory, Complexity, and Experiment Checklist

## Derivation audit

Check the following before writing performance claims:

- State the ANC signal model and the sign of `e(n)`.
- Distinguish the primary path, true secondary path, and estimated secondary path.
- Define the RFF mapping, distribution used to draw frequencies and phases, scaling, and feature dimension.
- Show how the filtered reference enters the gradient. If the implementation uses an approximation, state it.
- Write the MCC loss or criterion and derive its influence or gradient term with the chosen kernel width.
- Define the NKP factorization, reshaping convention, factor dimensions, rank, and reconstruction order.
- Verify dimensions and update order for every factor.
- State independence, small-step-size, stationarity, or other assumptions used in convergence analysis.
- Separate a theorem or proposition from an empirical observation.

## Complexity audit

Report more than big-O notation. For each algorithm, state per-sample:

- real multiplications and additions;
- exponential or nonlinear-function evaluations;
- memory footprint;
- any periodic decomposition or initialization cost;
- latency-critical operations.

Define whether preprocessing, secondary-path filtering, RFF generation, and output reconstruction are included. Compare algorithms at matched feature capacity or explain why a different budget is scientifically fair.

If a plot varies the Kronecker rank or number of terms, accompany it with a table or formula that shows how that variable changes both cost and parameter count.

## Required experiment matrix

### Noise or excitation regimes

- Gaussian condition as a conventional-control check.
- Symmetric alpha-stable or other impulsive condition across more than one severity setting.
- Logistic-chaotic condition with the generating equation, parameters, initialization, and role of the signal clearly stated.

Clarify whether each process is the reference input, primary disturbance, measurement noise, or a contamination of the error signal. Do not call all of them simply "noise".

### Ablations

- RFF alone versus RFF plus MCC.
- RFF plus MCC versus NKP-RFF plus MCC.
- Rank or term-count sweep.
- MCC kernel-width sweep.
- Feature-dimension sweep.
- Secondary-path estimate mismatch.

### Dynamic and practical tests

- abrupt path or signal-statistics change;
- actuator saturation or another stated nonlinearity;
- measured or standard acoustic paths when available;
- runtime and memory on named hardware if real-time relevance is claimed.

## Fair-comparison protocol

- Use the same input realization and plant for paired runs.
- Give each baseline a documented tuning range and comparable tuning budget.
- State initialization, warm-up, clipping, normalization, and stopping rules.
- Use enough independent runs to report a mean and dispersion; retain individual-run data.
- Do not smooth one curve more heavily than another.
- Do not crop a diverging baseline without saying so. Show the divergence or report a clearly defined failure count.
- If step sizes are different, explain whether they were optimized for fastest stable convergence, matched steady state, or another objective.

## Metrics

Define every metric mathematically and include its averaging window:

- attenuation or average noise reduction (ANR);
- MSE or NMSE;
- convergence time to a stated threshold;
- steady-state mean and standard deviation or confidence interval;
- divergence/failure rate;
- operation count, memory, and measured runtime.

A single final ANR value is not sufficient to support claims about convergence speed, stability, and robustness simultaneously.

## Statistical reporting

Plot the mean learning curve with a shaded interval or report tabulated intervals. When using significance language, name the test, paired structure, sample size, effect size, and multiple-comparison handling. Otherwise use descriptive language.

## Reproducibility inventory

The manuscript or supplement should make available, when policy and confidentiality allow:

- plant coefficients or measured-path files;
- random seeds or seed-generation rule;
- full parameter table;
- algorithm pseudocode and initialization;
- figure-generation code;
- environment and version information;
- data and code availability statement.
