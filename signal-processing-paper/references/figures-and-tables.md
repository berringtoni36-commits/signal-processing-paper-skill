# Figures and Tables for Publication

## Non-negotiable figure cleanup

- Export from the plotting code; do not submit a screenshot of a MATLAB window.
- Remove toolbars, data cursors, selection boxes, crosshairs, and interactive callouts.
- Do not embed `Fig. 3`, a manuscript caption, or a long explanatory title inside the axes.
- Put the complete caption in the manuscript and keep only essential labels or panel letters in the graphic.
- Prefer PDF, EPS, or SVG for line art. Use high-resolution raster only when the content requires it.
- Use a white or transparent background, restrained grid lines, consistent fonts, and legible line widths.
- Ensure curves remain distinguishable in grayscale by combining color with line style or marker shape.
- Keep legends compact and use the same canonical algorithm names everywhere.

## Project-specific consistency checks

- Use the same algorithm labels in logistic-chaotic, alpha-stable, and Gaussian comparisons.
- Do not mix `RFF+NLMS+MCC`, `RFF+FxNLMS+MCC`, `RFFxMCC`, and `NKP-RFFxMCC` unless they are genuinely different methods.
- Use one iteration horizon across directly compared experiments, or explain why horizons differ.
- Reserve `R` for Kronecker rank/term count and `sigma_c` for the MCC kernel width; avoid ambiguous `K` versus `k` labels.
- If a curve diverges, preserve that information. Use a defined vertical cap, inset, failure marker, or companion table rather than silently clipping it.
- Avoid text boxes that obscure data. Put exact selected parameter values in the caption or table.

## Recommended figure sequence

1. ANC block diagram and signal definitions.
2. Complexity or parameter-count trade-off versus rank/term count.
3. Primary, secondary, and estimated-secondary path responses.
4. Representative nonlinear/chaotic input and its generation definition.
5. MCC kernel-width and rank sensitivity.
6. Logistic-chaotic comparison.
7. Alpha-stable impulsive comparison.
8. Gaussian comparison.
9. Ablation or secondary-path-mismatch result.
10. Optional residual waveform, spectrum, or spectrogram for physical interpretation.

Renumber to fit the final argument; do not preserve legacy numbers merely because plots were generated in that order.

## Caption formula

A stand-alone caption should identify:

- what is plotted and the metric units;
- the experiment condition and changed variable;
- the fixed parameters needed to interpret the result;
- whether lines are single runs or means, and what shading or error bars represent;
- panel meanings, if applicable.

Do not repeat the entire discussion or make an unsupported conclusion in the caption.

## Axes and legends

- Include physical units or state `dimensionless`.
- Use scientific notation consistently.
- Do not use excessively large labels that dominate the data.
- Place legends where they do not cover convergence or steady-state behavior.
- Use a log scale only when it improves interpretation and state it clearly.
- Define smoothing or moving-average windows in the caption or methods.

## Tables

Use editable tables for parameters, complexity, quantitative outcomes, and ablations. A recommended results table includes mean, dispersion, convergence time, failure rate, multiplications/sample, memory, and the relevant condition. Do not use images of tables.

## Final visual QA

Inspect every figure at its expected column width and in grayscale. Check for clipped annotations, overlapping captions and axis labels, tiny markers, inconsistent decimal precision, and missing panel references. Verify that every figure is cited in the text in numerical order.
