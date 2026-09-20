# Project Profile and Notation Guardrails

## Working research question

Can a nearest-Kronecker or other structured low-rank parameterization reduce the cost of an RFF-based nonlinear filtered-x adaptive controller while retaining or improving convergence and robustness under Gaussian, impulsive alpha-stable, and chaotic excitation conditions?

This is a project hypothesis, not a proven contribution. Convert it into claims only after the derivation and experiments support it.

## Candidate paper identity

- Domain: nonlinear active noise control and robust adaptive filtering.
- Baseline family: RFF-FxNLMS or RFF-NLMS, optionally with MCC.
- Proposed family: structured NKP/low-rank RFF-FxNLMS-MCC.
- Central trade-off: nonlinear modeling capacity and robustness versus arithmetic, memory, and convergence behavior.
- Target journal fit: adaptive/statistical signal processing, machine learning for signal processing, and audio/acoustic signal processing.

## Novelty guardrail

Do not claim novelty merely from combining NKP, RFF, NLMS/FxNLMS, and MCC. State the precise new object, for example:

- a new factorized controller parameterization;
- a derived filtered-x update under a correntropy loss;
- a complexity reduction at a matched feature budget;
- a stability or mean-convergence condition;
- an empirically supported operating regime not covered by prior methods.

At least one contribution must be algorithmically nontrivial, and every contribution bullet must point to an equation, proposition, algorithm box, or experiment.

## Freeze the terminology

Choose one canonical algorithm name and use it in the title, abstract, equations, legends, and tables. Recommended working names:

- `RFF-FxNLMS`
- `RFF-FxNLMS-MCC`
- `NKP-RFF-FxNLMS-MCC`

Use `NLMS` only if the secondary-path filtered reference is genuinely absent. Do not switch casually among `NLMS`, `FxNLMS`, `RFFxMCC`, and `NKP-RFFxMCC`.

## Notation table

| Symbol | Reserved meaning | Guardrail |
|---|---|---|
| `n` | discrete-time index | Never reuse for Monte Carlo run count. |
| `L` | adaptive filter length | State whether it applies before or after feature mapping. |
| `D` | total RFF feature dimension | Report the exact real-valued feature convention. |
| `D_1, D_2` | factor dimensions | Verify `D_1 D_2 = D` or explain the chosen structure. |
| `R` | Kronecker rank or number of terms | Prefer `R` so it cannot be confused with an MCC parameter. |
| `sigma_c` | MCC kernel width | Do not denote this by `K` or an undefined lowercase `k`. |
| `mu` | adaptation step size | Report tuning range and final value for every baseline. |
| `epsilon` | normalization regularizer | State units and sensitivity if influential. |
| `P(z)` | primary path | State whether linear, nonlinear, measured, or simulated. |
| `S(z)` | true secondary path | Keep distinct from the estimated path. |
| `S_hat(z)` | estimated secondary path | Report mismatch or identification procedure. |
| `e(n)` | error microphone signal | Define the sign convention before deriving a gradient. |

If the existing manuscript uses `K` for both Kronecker terms and an MCC parameter, rename one before any further drafting.

## Claim-evidence ledger

Maintain one row for each paper-level claim:

| Claim | Mechanism | Equation/algorithm | Required evidence | Status |
|---|---|---|---|---|
| Lower cost | Factorized parameterization | Exact update and operation count | Matched-budget complexity table and runtime | Pending |
| Faster convergence | Better structured adaptation | Learning curves | Repeated-run convergence time with dispersion | Pending |
| Better steady state | Robust loss and model structure | Loss/update relation | Steady-state ANR mean and interval | Pending |
| Impulsive robustness | Bounded/reweighted error influence | MCC influence analysis | Alpha-stable tests across severity | Pending |
| No Gaussian penalty | Same controller remains competitive | Same protocol | Gaussian comparison and ablation | Pending |

Replace `Pending` only when the evidence exists and is traceable.

## Minimum baseline set

- Conventional FxNLMS, when meaningful for the nonlinear plant.
- RFF-FxNLMS without MCC.
- RFF-FxNLMS-MCC without NKP.
- NKP-RFF-FxNLMS-MCC.
- A relevant low-rank or nonlinear adaptive baseline when implementable under a fair budget.

Use ablations to isolate RFF, MCC, and NKP. A comparison between only the full baseline and full proposal cannot show which component caused the change.
