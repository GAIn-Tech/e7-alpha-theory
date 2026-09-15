# Release disclosure

- **Checked:** 13 exact-real/rational Z3 satisfiability checks of the explicit local clock-response model, replayed from retained SMT-LIB files without receipt regeneration; exact rational comparison of the selected corrected inverse-alpha candidate with NIST CODATA 2022.
- **Empirical inputs:** captured BIPM SI definition, NIST CODATA value, NIST-hosted Lorini et al. 2008 paper and rounded sensitivity coefficients; BACON 2021 abstract and NIST account provide examples of measured ratios, not input time series.
- **Not checked:** an E7 action, nuclear/atomic many-body calculations, field dynamics, a new experiment, an independent absolute alpha extraction, a full error/covariance analysis, or any model-specific exclusion.
- **Not claimed:** Lean-kernel verification, Mathlib compilation, hosted CI, peer review, E7 no-go theorem, explanation of the CODATA residual, discovery significance, or current best-clock records.
- **Approximation:** local first-order sensitivity model; rounded K values are exact only inside the solver model; absolute ratio intercept and nuisance priors are explicit. No nonlinear error bound was supplied.
- **Selection:** the candidate 137+9/250 predates this gate and is already target-informed in the parent investigation. This gate does not tune it or select further terms.
- **Source limitations:** Nature accessible abstract/preview only; NIST comparison full PDF retained; HyperPhysics full HTML fetched over HTTP. NIST equation (12) has a disclosed coefficient-order inconsistency resolved by algebraic differentiation, not by fitting data.
- **Automation:** AI-assisted reasoning and code. Z3 5.1.0 was actually executed. All substantive results, source hashes, exact SMT inputs and replay receipts are retained beside REPORT.md. Review status: self-assessed.
