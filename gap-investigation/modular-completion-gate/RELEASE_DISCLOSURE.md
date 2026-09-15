# Claim boundary

This gate closes the missing modular-sector assembly for the **E7 level-one lattice/affine worldsheet building block**, in two explicit ways: its diagonal left-right completion, and its E7 x A1 even unimodular E8 extension. It is not a full string vacuum.

## Proved / checked
- Exact rational E7 determinant and coset norms, bounded lattice shells, exact Q(zeta_24) S/T modular relations, unitarity, diagonal invariance and E8 extension-vector covariance are recomputed by Python.
- Five substantive finite discriminant-form declarations are checked by the Lean 4.32.1 kernel without axioms: two polarization identities, diagonal isotropy, converse isotropy (unique glue), and the obstruction to an E7-only nonzero isotropic extension.
- Analytic lattice/affine-character identification and theta modular transformation are cited external mathematics, not formalized here. Infinite lattice gluing is justified in REPORT.md by lattice inclusions/index and the explicit determinant-one Gram matrix, not inferred solely from matching low coefficients.
- The previous unsourced character, c=7 and h-dual=18 claims now have retrieved primary-author/research-paper support. Sources quote established background as well as their own results; this is not a reproof of general Sugawara theory.

## Not proved
No compactification geometry, spin structure/GSO choice, critical central-charge balance, BRST cohomology, internal Dirac index, anomaly-free spacetime spectrum, family selection, stabilization, preferred spacetime dimension, prime energy scale, or coupling matching has been supplied. Worldsheet chirality, four-dimensional Weyl chirality, knot mirror chirality, and a Specht determinant sign remain distinct. No alpha fits or empirical prediction was attempted.

The complex S/T identities are Python exact algebra, **not** Lean theorems. The Lean code proves the bounded discriminant algebra underlying the extension; it does not prove a VOA construction or a string consistency theorem. No hosted CI or independent expert review ran. AI-assisted, self-assessed local release.
