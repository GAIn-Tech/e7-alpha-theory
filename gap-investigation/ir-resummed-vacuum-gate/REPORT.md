# IR-resummed shifted-vacuum gate: leading matching and the remaining obstruction

## Verdict

The model-specific one-loop hard self-energy has now been projected on the entire 78-dimensional tree-soft space. Its sum with the tree-Hessian change from the canonical leading shift obeys the Ward cancellation on all 67 broken-gauge directions (operator norm `6.37e-8` before multiplication by `epsilon^2`; the separate terms reach `2.18e4`). On the eleven physical flats it gives eight positive eigenvalues `1.18165815` and three `1.40673474`, in units `epsilon^2 M^2`. Thus the octet/triplet are physical positive **zero-momentum curvatures**, while the 67 Goldstones are symmetry-required zero directions—not 67 additional light particles.

This does **not** close the full resummed-vacuum gate. The necessary hard two-loop self-energy/tadpole and momentum-dependent matching have not been computed. More sharply, the order-one Gaussian Goldstone ring remains non-C2 in a transverse radial coordinate even after imposing its Ward zero at the stationary point. The declared action contains the elementary exact example `Phi`: its phase is one of the 67 gauge tangents and its tree field-dependent mass is `G_Phi=rho^2-2`. At `rho=sqrt(2)`, `(dG_Phi/drho)^2=8`, so the Goldstone contribution to radial zero-momentum curvature contains

    epsilon^2 [1/(4 pi^2)] log(G_Phi/mu0^2).

It tends to minus infinity from the positive-mass side. No `log(abs(m²))`, clipping, or arbitrary mass was used. Consequently the existing hard C2 Schur result cannot simply be promoted to a C2 theorem for this naively ring-improved potential. This is the bounded necessary next component: a complete order-counted stationarity calculation needs the hard two-loop terms whose subtraction/matching cancels or reorganizes this curvature singularity, and pole masses need momentum-dependent two-point functions.

## Prescription and assumptions

The action, normalization, `mu²=epsilon M²`, zero FFh Yukawas and tuned zero portals are exactly those in `shifted-vacuum-gate`; no interaction or fitted parameter was added. With `f(X)=X²(log(X/mu²)-3/2)`, Martin's matrix form at loop order L is

    Vhat = Vfixed + 1/(64 pi²) Tr_soft [
      f(G + Delta) - sum_{n=0}^{L-1} (1/n!) d_t^n f(G+t Delta)|_{t=0}
    ].

For noncommuting matrices the subtraction means the directional Fréchet/Taylor derivative, not eigenvalue-wise pairing. At one-loop fixed order (`L=1`), the original soft trace is subtracted and the matched Gaussian soft term is `Tr f(G+Delta)/(64 pi²)`. The hard self-energy is the Hessian of the hard one-loop functional, and the order-`epsilon²` soft mass matrix also includes the tree Hessian evaluated on the order-`epsilon` shifted background. Keeping only either term violates the Ward identity.

At the stationary branch the matched spectrum is exactly zero in the 67 Goldstone block and positive in the 8+3 physical block. The latter contributes `-4.70995237109555e-29 M^4` at `epsilon=1e-7`; a Decimal envelope is `7.06214e-29`. Its leading soft tadpole is `4.07996e-19 M^3` and the linear compensating singlet displacement has norm `9.44436e-16 M`; these scale as `epsilon^3 log epsilon` and `epsilon² log epsilon`. This is only the physical-soft Gaussian component: missing hard two-loop tadpoles are of the same formal order, so the displacement is not a full shifted solution.

The already-defined hard-mode stationary sample was independently re-evaluated analytically rather than by another finite-difference Hessian: gradient norm `2.40676e-19 M³`, massive-block minimum `0.999999697 epsilon M²`, and Schur minimum `1.18166808 epsilon² M²`. Analytic Hessian-vector products agree with central differences; the difficult shift direction shows quadratic step convergence (`7.29e-6`, `1.82e-6`, `4.56e-7` relative errors for steps `4e-5,2e-5,1e-5`). This remains a hard-functional result.

## Negative controls

* Reversing the self-energy sign leaves a Goldstone-block norm `4.3597e4`; retaining only the shifted tree Goldstone mass leaves `2.1798e4`. Correct matching cancels them.
* A noncommuting 2x2 example verifies directional double-count subtraction: the correct residual is proportional to `t²`, while wrong-sign subtraction leaves an order-`t` residual about `-0.3673 t`.
* Assigning the 67 Ward Goldstones a spurious positive `epsilon²` mass changes the matched one-loop value from `-4.71e-29` to `-2.34e-28`.
* Negative Gaussian masses raise an error rather than being made real by absolute value or clipping.

## Literature and claim boundary

Primary sources retained verbatim under `sources/`: S. P. Martin, *Taming the Goldstone contributions to the effective potential*, arXiv:1406.2355, especially eqs. (3.1)-(3.2); and J. Elias-Miró, J. R. Espinosa, T. Konstandin, *Taming Infrared Divergences in the Effective Potential*, arXiv:1406.2652, especially eqs. (8)-(16). The latter explicitly identifies zero-momentum hard self-energy resummation and explains that effective-potential curvature is a zero-momentum two-point function, not a pole mass.

This is a conditional four-dimensional EFT calculation. It is not derived from Tian-Yau compactification, not a pole-spectrum calculation, not an all-orders or full-quantum vacuum proof, and not an alpha prediction. No Lean file was added: the exact new statement `(dG_Phi/drho)^2=8` is elementary polynomial algebra, while formalizing a generic positivity theorem would not discharge the missing physical two-loop assumptions.

## Reproduction

Run the native interpreter:

    C:/Users/mikeb/AppData/Local/hermes/hermes-agent/venv/Scripts/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/ir-resummed-vacuum-gate/run_checks.py

The runner first validates saved receipt source hashes, then replays the hard projection, exact Phi obstruction, physical-soft tadpole, precision/step controls and tamper controls. `projected-tensors.json` stores the full bases and 78x78 hard/tree/summed matrices. Source hashes include both literature PDFs and every predecessor input.