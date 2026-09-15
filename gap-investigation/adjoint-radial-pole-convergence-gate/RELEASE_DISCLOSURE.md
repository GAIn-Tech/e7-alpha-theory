# Release disclosure

**Accepted scope:** additive numerical convergence diagnosis for the declared adjoint-radial scalar/fermion subset; read-only receipt replays; independent high-precision vector-master audit; compatible-sector bookkeeping in strict Landau/MSbar. Existing action, particle content, normalization, i0 and tadpole prescriptions are unchanged.

**Established numerically:** real endpoint bias explains the old 1.0908189794281498 grid discrepancy. Corrected scalar coefficient rounds to 511999.946 - 238193.186 i. Compatible sum rounds to 505145.100 - 235147.465 i; it includes -45.10700126487947 once. See REPORT.md and the complete mass-channel receipt for evidence.

**Not established:** full or gauge-independent pole; physical width; general-xi cancellation; finite UV matching; independently fixed finite counterterms; two-loop tadpoles; explicit one-loop external-mixing amplitudes; a compactification derivation or alpha prediction. General-xi and finite matching are substantive open gates, not numerical formatting problems.

**Precision:** adaptive/analytic 40/70-dps integral checks are numerical, not directed-rounding interval proofs. Inputs and eigenspaces are double precision, grouped by predecessor mass shells. Printed high-precision integral digits do not certify action data or physical uncertainty. Mixed sector remains checked at about 2.3e-6 by an independent parameter integral. Headline values are deliberately rounded to 0.001 coefficient units.

**Provenance:** predecessors are preserved and SHA-256 checked before/after execution. verify.py exclusively creates receipt.json once and thereafter requires exact replay. manifest.json binds release files and vendored mpmath 1.3.0 sources. No original receipt was regenerated. All accepted executions use the canonical native Windows repository.

**Review:** AI-assisted derivation, coding and self-review only; no external peer review, hosted CI or Lean-kernel proof. Root README historical overclaims are not endorsed. This gate narrows one numerical prerequisite and does not complete the physical program.

