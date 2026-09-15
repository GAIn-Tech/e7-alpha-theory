# Goldstone pole matching: the leading radial IR logarithm cancels

## Outcome

The leading two-Goldstone scalar bubble has been calculated from the actual 188-field action, 79 generators and 67 gauge tangents. Its momentum subtraction cancels the Gaussian Goldstone curvature logarithm at every fixed nonzero momentum, including an **isolated physical adjoint radial tree eigenmode with m_A^2=4320 epsilon M^2**. The entire **121x121 gauge-transverse logarithm-coefficient matrix** is also constructed, not just a Phi-coordinate example.

The premise about zero-momentum curvature needs refinement. The primary literature explicitly permits G^2 log G terms to remain singular after two derivatives; it resolves this mass-calculation problem through nonzero-momentum self-energies, not by demanding a C2 effective potential. Hard two-loop stationarity remains unfinished, but making the radial curvature finite is not its acceptance criterion. See SOURCE_NOTES.md, Elias-Miro et al. printed p.3 and Appendix A, and Martin p.18. The previous report and receipts are retained unchanged.

This is a **leading one-loop diagram-subset calculation**, not the complete gauge-independent scalar pole spectrum. The imaginary parts below belong to unphysical Goldstone cuts in that subset and are not physical decay widths.

## Action, gauge and orders

The source action is exactly shifted-vacuum-gate: canonical scalar kinetic metric, MSbar Landau gauge, g6^2=gX^2=lambda=epsilon, fixed Yukawa ratios, mu^2=epsilon M^2, tuned zero portals and FFh couplings. No interaction or matching parameter is added. Coordinates and tensors below use M=1; dimensional powers are displayed in the final self-energy.

The tree residuals are

    f_r=x^T B_r x/2+c_r,  J_r=B_r x,
    V_tree=epsilon sum_r f_r^2,
    H0=2 J^T J+2 sum_r f_r B_r.

All 114 residual tensors, including their off-shell residual-times-B term, are imported from the predecessor. Its rational singlet Hessian/inverse receipt is reconstructed and compared exactly. The complete canonical gauge action gives K_a=R_a x0. The imported orthonormal Goldstone frame N spans im K^T; Q spans ker K and has 121 columns. The physical flats F have eleven columns.

The common squared mass G=epsilon M^2 eta assigned to the 67 Goldstone propagators below is **only an auxiliary IR regulator**, removed as eta approaches zero from above. It is not a claimed positive mass for Ward Goldstones or a modification of the action. No negative mass is replaced by an absolute value. Absolute values in the numerical quadrature evaluate the real part of the analytically specified timelike logarithm, whose imaginary part is retained separately.

## Trilinears and self-energy sign

For any canonical unit field direction v, differentiate the exact polynomial Hessian:

    T(v)=d_v H0
        =2[(Bv)^T J+J^T(Bv)+sum_r (Jv)_r B_r].

The real symmetric trilinear coupling matrix to two gauge Goldstones is

    L_v=N^T T(v) N,
    lambda_(vab)=epsilon M (L_v)_ab,
    V_int=(1/2) sum_ab lambda_(vab) h_v chi_a chi_b.

This is a projection of the original interactions, not a fitted Goldstone vertex. The tested differentiated gauge Ward identity is

    T(v) R_a x0 + H0 R_a v = R_a H0 v.

The maximum residual is 2.45e-15. The gauge-frame projection residual is 1.53e-14. Direct Hessian finite differences give projected trilinear errors below 5.5e-13. These are floating-point checks of an explicit polynomial identity, not interval or Lean certificates.

Define Pi so that the inverse propagator is s I - M_tree^2 - Pi(s). Then the curvature matrix is M_tree^2+Pi(0). With the identical-real-scalar symmetry factor 1/2, the bubble is

    Pi^GG_ij(s)=epsilon^2 M^2 C_ij I(shat,eta),
    C_ij=Tr(L_i L_j)/(32 pi^2),
    shat=s/(epsilon M^2),
    I(shat,eta)=integral_0^1 log[eta-shat t(1-t)-i0] dt.

Our I is minus B of Elias-Miro et al. eq. (A.4); its sign is not interchangeable with that source's B. In particular I(0,eta)=log eta. The momentum-independent quartic-Goldstone tadpole is proportional to eta(log eta-1) and does not alter the surviving log coefficient. Other diagrams, including mixed massive/massless bubbles and physical-soft loops, are outside this two-Goldstone subset.

The Gaussian Goldstone trace produces exactly the same coefficient in curvature:

    H^GG_curv,ij = epsilon^2 M^2 C_ij log eta + terms vanishing as eta log eta.

Therefore the pole-matching combination, entry by entry, is

    H^GG_curv + [Pi^GG(s)-Pi^GG(0)]
      =epsilon^2 M^2 C [log eta + I(shat,eta)-log eta]
      ->epsilon^2 M^2 C [log(-shat-i0)-2].

The limiting expression agrees with the sourced massless B(0,0), eq. (A.5). The cancellation does **not** mean either zero-momentum object separately has a finite eta->0 limit.

## A nondegenerate physical radial eigenmode

A robust radial target is the adjoint norm direction

    v_A=(0_h1,0_h2,A0/sqrt(B(A0,A0)),0_Phi),
    B(A0,A0)=60.

It is gauge-orthogonal because B(A0,[T,A0])=0. The Ah residuals annihilate this variation at the stated alignment, and the adjoint norm residual is 3 B(A,A)-180. Thus its Jacobian norm squared is (6 sqrt(60))^2, giving **H0 v_A=4320 v_A**. The full numerical 188x188 spectrum confirms this eigenvalue has multiplicity one, so its leading on-shell projection is unambiguous; nondegenerate eigenvector changes enter at higher order. This avoids relying on an unresolved Phi degeneracy.

The original Goldstone vertices give

    C_AA = 44240.64929382796.

At shat=4320 and eta=1e-60, all entries below are divided by epsilon^2 M^2:

| quantity | value |
|---|---:|
| singular curvature | -6112071.57410075 |
| real momentum subtraction | +6393929.22329664 |
| finite sum | 281857.649195889 |
| analytic massless real limit | 281857.649195889 |
| subset imaginary part | -138986.098811532 |

The 90-digit analytic evaluation finds regulator-limit error 3.09e-57 in the scaled subset. The tensor coefficient itself is only double precision: these many digits test the integral limit, **not** 57-digit knowledge of the model's mass correction. This is one calculable term in the pole shift, not the full mass shift. The predecessor hard-curvature projection in this direction is 30100.792136402; its missing momentum dependence must still be included.

## Phi really mixes

The tree singlet eigenvalue 4 has a three-dimensional degenerate subspace E. Although bare Re Phi is a tree eigenvector, it is not an eigenvector of the next-order hard mass matrix

    H1 = d_delta H0 + Hessian(L_hard),
    delta = predecessor leading canonical vacuum shift.

Its off-diagonal H1 norm is 16.4859193. Diagonalizing E^T H1 E gives shifts

    -32.03056015, -28.10123572, +0.99279336,

with Phi weights 0.47208281, approximately zero, and 0.52791719. The maximum-Phi hard-curvature eigenmode has canonical components

    0.4858409275 e_6 + 0.4858409275 e_67 + 0.7265790985 e_186.

It is gauge-transverse, satisfies H0 v=4v, and diagonalizes the degenerate hard correction. Its Goldstone log coefficient is **0.05497678156734**, not the bare-Phi coefficient 1/(4 pi^2). Finite-epsilon diagonalizations on the shifted transverse singlet slice have squared overlaps exceeding 0.999999999996 with this limiting mode. The sample uses x0+epsilon delta, not a claim of full resummed stationarity.

At shat=4 its diagonal matched bubble approaches

    epsilon^2 M^2 [-0.0337395608554 - 0.172714653090 i].

There is an important further boundary: E^T C E does not commute with E^T H1 E (commutator norm 1.46414). Thus even this hard-curvature eigenmode cannot be called a completed pole eigenstate. The receipt includes the complex eigenvalues of the **partial** degenerate matrix H1_E+C_E(log4-2-i pi), but labels them explicitly as incomplete. The nondegenerate v_A result above is the clean leading physical radial eigenmode calculation. A full Phi pole calculation must diagonalize the complete momentum-dependent degenerate block.

## Full transverse block and limit controls

`tensors.json` retains N, Q, both radial vectors, both 67x67 radial trilinears and the full 121x121 C. `transverse-trilinears.npy` retains all 121 symmetric 67x67 coupling matrices. C is a Gram matrix and hence analytically positive semidefinite; the computed minimum -6.48e-12 is roundoff at a maximum eigenvalue 44240.6664. Numerically it has 110 eigenvalues above 1e-8. Contraction onto the eleven tree physical flats gives trilinear norm 3.03e-13: the leading two-Goldstone log is absent there. This is not an octet/triplet pole-mass calculation.

The cancellation formula applies to the **whole block at one fixed external momentum**. Different on-shell eigenvalues require their respective momentum evaluations, not substitution of a different momentum into each matrix entry. For the loop-light physical flats, p^2~epsilon^2 M^2 and a separate soft power counting remains necessary.

The integral implementation has three controlled regimes:

- For shat<0, b=sqrt(1+4 eta/|shat|), I=log eta-2+b log[(b+1)^2/(4 eta/|shat|)].
- For shat>4 eta, b=sqrt(1-4 eta/shat), I=log eta-2+b log[(1+b)^2/(4 eta/shat)]-i pi b.
- For |shat/eta|<0.1, the convergent beta-integral expansion is I=log eta-sum_(n>=1) (shat/eta)^n (n!)^2/[n(2n+1)!]. Forty-nine-term evaluation avoids cancellation near zero momentum.

Six independent branch-split Gauss-Legendre tests, at 128/256/512 points, agree with the analytic formulas. The largest final error is 1.46e-11; timelike errors fall by about sixteen per point doubling. This is a numerical convergence cross-check, not a rigorous quadrature error enclosure. Fixed nonzero timelike and spacelike momentum scans take eta from 1e-4 to 1e-60 for both radial modes. At fixed positive eta, the small-momentum scan verifies (I(s)-I(0))/(s/eta)->-1/6. Consequently the G->0 and p^2->0 limits are nonuniform; setting p=0 first cannot yield an IR-safe pole estimate.

Negative controls are executed, not just listed:

- Omitting the subtraction Pi(0) leaves a log eta slope C.
- Reversing the sign of Pi(s)-Pi(0) leaves slope 2C.
- Both slopes are checked numerically in the final two regulator decades of each scan; the correct expression reaches the finite analytic limit.

## Physical next gate

1. Compute all one-loop nonzero-momentum scalar self-energies for the declared gauge/Yukawa action, including physical-soft scalars, mixed scalar/vector terms, fermions, necessary counterterms and scalar/vector mixing. Keep tadpole and wavefunction conventions consistent with the same shifted action.
2. Solve the complete degenerate singlet pole matrix rather than reporting the hard-curvature Phi mixture as an observable. Demonstrate cancellation of gauge-parameter dependence/unphysical cuts in actual poles; this Landau two-Goldstone subset cannot do that.
3. Separately compute order-consistent hard two-loop tadpoles and soft matching to close resummed stationarity. Require an IR-safe potential value/first derivative and controlled pole/physical-soft behavior, **not** a C2 zero-momentum radial potential.

This bounded run adds no alpha fit, UV interaction, publication, Tian-Yau derivation, or claim of a full two-loop theory. No decorative Lean arithmetic theorem was added.

## Reproduction

    C:/Users/mikeb/AppData/Local/hermes/hermes-agent/venv/Scripts/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/goldstone-pole-matching-gate/run_checks.py

The runner validates saved hashes before replay, replays the three predecessor IR calculations read-only, reproduces this calculation and tensors, and saves actual outputs under this lane. `verification.json` records exit codes, output hashes and unchanged predecessor receipt hashes. Original development Phi-only artifacts are preserved in `development-phi-hard-mode/`; current claims use the top-level receipt. File-tool writes initially used the known Cygwin shadow mapping and were explicitly copied into the verified native owned directory before execution. One overly absolute 90-digit cancellation threshold failed for the much larger adjoint coefficient and was replaced by a coefficient-scaled numerical precision threshold; no physical acceptance limit was relaxed.
