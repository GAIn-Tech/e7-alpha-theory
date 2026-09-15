# Release disclosure

## Proved by local execution

- Exact `Q(zeta_24)` E7 level-one `S,T`, fusion, normalized unknot/Hopf and framing values.
- Exact bounded E7 lattice-shell charge-square moments and low-order charge-character identity.
- Exact q-series checks of the modular identities used by the sourced threshold formula through degree 40.
- A strict rational lower bound proving nonconstant DKL dependence on the declared `T=it`, `2<=t<=3`, `U=5i` path.
- Six axiom-free Lean declarations: Z2 fusion controls, an abstract observation-fiber obstruction, a nonconstant-observation control, a concrete obstruction, and a positive recoverability control.

## External physical premises

WZW/Chern–Simons surgery relations, E7 level-one primary data, heterotic charge-inserted threshold formulas, eta product and elementary real calculus/standard pi bound are source inputs. Lean does not formalize these physical/analytic premises.

## Not proved

No Tian–Yau threshold is calculated; the explicit counterfamily is N=2 heterotic K3 x T2. No complete string vacuum, alpha value, spacetime dimension/family count, moduli stabilization, or knot-mirror-to-Weyl-chirality map is derived. No Kauffman polynomial is identified with HOMFLY-PT. Ramanujan congruences, nimbers and Dedekind numbers are not threshold inputs.

## Review and automation

Self-assessed. Python standard-library exact arithmetic plus inherited exact cyclotomic code; minimal Lean 4 kernel. PyMuPDF was used only to extract a retrieved source. No hosted CI or independent peer review.
