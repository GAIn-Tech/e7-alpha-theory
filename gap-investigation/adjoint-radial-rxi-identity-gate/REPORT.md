# All-xi radial pole-difference identity gate

## Outcome
The seven-channel Rxi-minus-Landau expression has an exact symbolic free-master coefficient identity for arbitrary xi, conditional on action-derived Ward relations and stationary-shift kernel compatibility. Every independent A0/B0 coefficient is collected before the on-shell substitution; no integral is sampled and cancellation is not an axiom. The actual 188-scalar/79-vector action passes a separate double-precision audit. This is not exact certification of its floating tensors and not a full pole, width, matching, UV, or compactification result.

## Conventions and derivation
The predecessor action, fixed-background gauge `F_a=partial.A_a-xi g(R_a x).eta`, MSbar scale, inverse propagator `s-rho-Pi`, and power counting are unchanged. The masters are `I(a,b;s)=int_0^1 log[z a+(1-z)b-sz(1-z)-i0]dz` and `A(a)=a(log a-1)`. The full complex i0 branch is retained. The independent reducer polynomial-divides the action VV and SV numerators in `D1=u-a,D2=v-b` and uses dimensional-regularization tadpole identities; it does not call the predecessor numerical kernels.

Potential invariance gives `H R phi=R grad V`. At a stationary background, with `K_a=R_a x`, `L_a=R_a h`, and `Hh=rho h`, differentiation gives
`HK_a=0`, `T K_a+H L_a=rho L_a`, and `U K_a+2T L_a=R_a t_hh`.
For `G_a=K_a/sqrt(a)`, physical eigenmode mass t, `C_ai=L_a.e_i`, and `Z_ab=K_a.L_b`, this yields
`T_iG_a=(rho-t)C_ai/sqrt(a)`, `T_GaGb=rho Z_ab/sqrt(ab)`, and symmetric Z. These are derived from the action, not selected to cancel loops.

For each massive direction let `tau_a=V'''[G_a,G_a,.]`, `q_a=G_a.U.G_a`, and `ell_a=L_a.(H-rho)L_a`. Differentiated invariance gives `a tau_a=-H R_a K_a` and `a q_a-2ell_a=-t_hh.R_a K_a`. With the transverse stationary solution `d_a=-Hplus tau_a`, `sigma_a=t_hh.d_a`,
`q_a+sigma_a=2ell_a/a-kappa_a`, where `kappa_a=t_hh.(1-Hplus H)R_aK_a/a`.
Thus the exact unmet-assumption residual, if compatibility fails, is `-sum_a kappa_a A(xi a)/(32pi^2)`. Gauge zero directions are controlled by Ward identities; the 11 physical flats are not discarded. The actual invariant-singlet shell solves verify this compatibility numerically.

## Master decomposition
After adding the action-derived scalar seagull and stationary shift, and setting kappa=0, all channel coefficients reduce to two blocks (common `1/(32pi^2)` omitted):

- physical/Goldstone, weight `C_ai^2`:
`2(s-rho)/a {A(xi a)-(s+rho-2t)[I(t,xi a)-I(t,0)]}`;
- ordered symmetric vector/Goldstone, weight `Z_ab^2`:
`(s-rho)/(ab){A(xi a)+A(xi b)-(s+rho)[I(xi a,xi b)-I(0,0)]}`.

Every coefficient vanishes exactly at `s=rho` for arbitrary xi and unequal a,b. Intermediate channel coefficients remain in `symbolic_receipt.json`. Missing ghost leaves `2xi^2 I(xi a,xi b)`; wrong ghost sign leaves `4xi^2`; missing displacement leaves `-sigma A(xi a)`; wrong displacement sign leaves `-2sigma A(xi a)`. An explicit invariant Abelian quartic action witness has nonzero `sigma=-6lambda`, so the displacement controls are nonvacuous.

## Actual tensor evidence
No mass rounding is used in Ward tests. Recorded norms include: differentiated Ward 8.06e-12; twice-differentiated Ward 9.75e-13; Goldstone-tadpole Ward 3.42e-11; kernel compatibility 1.29e-10; individual quartic-plus-shift 1.19e-10; maximum shell A-coefficient residual 1.07e-9; maximum shell stationary residual 2.77e-9. Off-stationary action Ward tests are also included. Shell rounding only identifies degenerate groups for invariant summation. Exact tensors, certified enclosures, and a full quantum Slavnov-Taylor functional remain absent.

## Analytic and perturbative boundary
The identity applies for fixed positive xi and its proper Landau boundary limit, on either side of unphysical cuts. It never uses `log(abs)` or drops imaginary parts. At a threshold the finite boundary value is understood continuously, while singular derivatives defeat an ordinary isolated-pole expansion. Require an isolated physical radial eigenvalue, no unphysical pole/threshold within the loop shift, small loop coefficients, small relative displacement, and `|Pi'|<<1`. xi scaling as `1/epsilon`, degeneracy, or threshold collision needs a resummed determinant. Finite symmetry-preserving counterterms alter the absolute pole but not this difference; finite EFT matching remains unresolved.

## Lean and replay
Pinned Lean is 4.32.1 (`f054605...`). The actual `import Init` probe fails because this minimal distribution lacks Init. A kernel-only restatement would not substantively formalize the master algebra, so no Lean theorem or axiom count is claimed. `lean_environment.json` records the blocker. SymPy 1.13.3 exact algebra is trusted CAS evidence, not a small-kernel proof.

Run:
`C:/Users/mikeb/AppData/Local/hermes/hermes-agent/venv/Scripts/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/adjoint-radial-rxi-identity-gate/run_checks.py`

The runner reads and hash-validates saved receipts before replaying them, never regenerates acceptance evidence, checks failure controls, and replays the Lean blocker. Hosted CI and peer review were not run.
