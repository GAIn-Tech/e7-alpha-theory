# Shifted-vacuum gate: explicit tadpoles and conditional local continuation

## Outcome

The predecessor's leading angular repair can be advanced to an **explicit shifted stationary point of the hard-mode one-loop action (analytic on the SM-fixed slice)**. This is not just a singlet minimization: all 188 real scalar coordinates, all 79 vector masses, the 67 gauge tangents, and the 121-dimensional physical quotient are constructed. At the action point below, a Newton solution has full canonical gradient norm **2.41e-19 M^3**, with a positive full physical Schur complement (minimum **1.181668 epsilon^2 M^2**). These eigenvalues are double-precision/finite-difference diagnostics, not interval certificates or pole masses.

For the **full unresummed** Landau Coleman–Weinberg determinant, the leading shift is also calculated, including its transverse fermion tadpole. Its real-part residual scales consistently with **epsilon^3 log epsilon**, not a clean analytic epsilon^3 coefficient. The shifted tree scalar matrix has negative eigenvalues, so the unreorganized CW potential is complex. This is an actual IR obstruction to treating that expression as a real C2 potential and blindly applying the ordinary IFT. No fully resummed quantum vacuum is claimed.

## 1. One specified renormalized action

Use the anomaly-remediation field content and charges verbatim, in a four-dimensional canonical truncation of H=(E6_sc x U1_X)/Z3. Add the predecessor h1,h2=27(-2), real A=78(0), and complex Phi=1(+3). Let M=1 in executable units. At a matching scale **mu^2=epsilon M^2**, set

- g6^2=gX^2=lambda=epsilon>0;
- B(U,V)=Tr27(UV)/3, Tr27(Ta Tb)=3 delta_ab;
- Lkin=sum_i |D h_i|^2 + |D Phi|^2 + B(D A,D A)/2; Lgauge=-sum F_a^2/4;
- Vtree=epsilon [V0+(|Phi|^2-M^2)^2], with V0 exactly the earlier norm/overlap/Ah sum of squares;
- all other allowed renormalizable scalar coefficients (including Phi portals, I2 hdag h, flavor mixing, hdag A h and independent V27 coefficients not present in V0) are **zero renormalized matching data**. Their divergent counterterms are not omitted. This is a tuned conditional family, not a symmetry claim;
- retain the original spectator parity and Yukawa channels Phi P Q, Phi† a_j b_j, Phi† c d, with (yP,y1,y2,yc)=sqrt(epsilon)(1,1,2,3). Thus the existing nonzero Yukawa ratios are retained while putting this family in an asymptotically weak region;
- set all FFh Yukawa matrices and other unlisted Yukawas to zero at matching. This is explicit additional action data, not inferred from their angular constancy. Light F_i and s_i are massless in this diagnostic, not realistic fermion phenomenology.

No independent adjoint kinetic rescaling, engineered high-dimensional operator, measured alpha, or added spectator is used. VEVs at epsilon=0 in scaled equations are h1=s0,h2=s1,A0=6Y,Phi=1 (v=sqrt(2)). Absolute M, epsilon and matching prescriptions remain free.

## 2. Full determinants and transverse derivative

Write canonical x in R^188, h=(Re x+i Im x)/sqrt(2), A=sum_a x^a Ta, Phi=(x186+i x187)/sqrt(2). The code constructs the exact polynomial residual representation

    F_r(x)=x^T B_r x/2+c_r,
    J_r=B_r x,
    H0(x)=2 J^T J+2 sum_r F_r B_r.

There are 114 real residuals: three scalar norms, two overlap components, one adjoint norm, and 108 Ah components. **The residual-times-second-derivative term is included off shell**; reusing 2J^T J away from the tree vacuum would be wrong.

For the complete gauge action, R_a are its 79 real antisymmetric canonical scalar generators and

    K_a=R_a x,   MV0^2=K K^T.

The 79th generator rotates h by charge -2 and Phi by +3. Consequently the full abelian/Cartan mixing and its transverse derivatives are included, not dismissed as A-independent. The gauge Ward identity H0 R_a x=R_a grad V0 is numerically tested away from the stationary family (residual 4.12e-15).

In MSbar, Landau gauge, at the declared mu,

    Veff = epsilon V0combined + epsilon^2 L(x),
    L= [Tr_188 f_3/2(H0) +3 Tr_79 f_5/6(MV0^2)
          -4 sum_(d,yhat) d f_3/2(yhat^2 |Phi|^2)]/(64 pi^2),
    f_c(z)=z^2(log z-c),
    (d,yhat)=(27,1),(1,1),(1,2),(1,3).

This counts all real scalars, all vectors (the Landau 3-polarization prescription), and all 30 massive Dirac blocks/60 Weyl modes. The other 84 Weyl fermions have identically zero masses for the declared Yukawa action. Landau massless ghost/longitudinal determinants have no field-dependent mass contribution. The source prescription is Martin hep-ph/0111209, already retained by the predecessor; no new scheme is invented.

The displayed fermions are independent of **A and h at fixed Phi**, because the only nonzero masses are y Phi or y Phi†. But they are **not independent of the transverse Phi radial direction**. Their canonical Phi tadpole is -1.34613417012114 in L. Dropping them changes the leading canonical displacement by norm 0.33653354253028. The previous argument that they are angular constant alone would not justify dropping this derivative. Turning on FFh or Phi portals invalidates these numbers and requires a new determinant, even though the leading angular signs on the old family may remain unchanged.

Analytic spectral differentiation uses W=f'(H), f'=z(2 log z+1-2c):

    grad Tr f(H0)=4 sum_r B_r W J_r +2 J^T [Tr(W B_r)]_r,
    grad Tr f(K K^T)=2 sum_ai (W K)_ai (R_a)_ij.

Independent directional finite differences of the complete determinant agree at relative error about 5.5e-9. Zero modes contribute f'(0)=0 at the base point. For off-shell diagnostics only, log|z| is the explicitly declared **real part**, not a claim that the imaginary part vanishes.

## 3. Gauge-fixed SM singlets and exact Hessian inverse

The representation-generated stabilizer is 12-dimensional. Its simultaneous kernel in the entire scalar representation has dimension 15. Removing the five SM-fixed gauge directions leaves **ten physical SM-singlet directions**. No radial-only ansatz is substituted. The full canonical tree Hessian has 110 positive directions, 67 gauge zero directions and eleven physical zeros. Its smallest positive eigenvalue is numerically 1 (times epsilon M^2), independently consistent with the earlier rational residual spectra and the added Phi mass 4.

Here is a rational, nonorthonormal transverse basis Z in original field coordinates, in the exact order used for the tadpole below. The h entries are raw Re/Im h, not canonical sqrt(2) coordinates. H_i denote the predecessor six original Chevalley Cartans, with 1-based labels:

1. Re h1(s0), 2. Re h2(s1), 3. Re Phi;
4. Re h1(s1)+Re h2(s0);
5. Im h1(s1)-Im h2(s0);
6. H2;
7. (2/3)H1+(4/3)H3+2H4+H5;
8. -(1/3)H1-(2/3)H3-H4+H6;
9–10. the final positive-root Hermitian real/imaginary pair in the predecessor's sorted E6 root basis (canonical generator indices 76,77, zero-based).

The first five Hessian diagonal entries are 8, the final two are 4. The only nontrivial 3x3 block (directions 6–8) and its exact inverse are

    Kc = [[10370, -17280, 13822],
          [-17280, 28800,-23040],
          [13822, -23040,18436]],
    Kc^-1 = [[1,1,1/2],
              [1,33409/28800,7/10],
              [1/2,7/10,1/2]].

Thus K^-1 is diag(1/8 repeated five times, Kc^-1,1/4,1/4). **K=2(Jraw Z)^T(Jraw Z)** is assembled in rational arithmetic, and K K^-1=I is tested exactly with Fraction. Its embedding into the full canonical H0 is independently crosschecked. Gauge orthogonality and SM fixedness are also checked; this is an inverse on a specified gauge slice, not an inverse of the singular full Hessian.

The covector tadpole t=Zcanonical^T grad L and leading coordinate displacement d=-K^-1 t are:

| direction | t | d |
|---|---:|---:|
| 1 | 31.9248919710210 | -3.99061149637763 |
| 2 | 31.9248919710210 | -3.99061149637763 |
| 3 | 35.5251866796577 | -4.44064833495721 |
| 4 | 0 (numerical 1.0e-14) | 0 |
| 5 | 0 (numerical 5.3e-16) | 0 |
| 6 | 261583.161734492 | 0 (cancellation residual 2.2e-11) |
| 7 | -435967.508121872 | 16.2005052461682 |
| 8 | 348768.692774761 | 1.32843068429429 |
| 9,10 | 0 (below 4e-15) | 0 |

The adjoint displacement therefore contains a **new commuting singlet component**, not merely a rescaling of Y. Its radial projection obeys (A0,delta A)/(A0,A0)=-5.04592023290678. The full canonical delta norm is 40.4357841885158. The leading shifted configuration is x=x0+epsilon Zcanonical d; it solves H0 delta+grad L=0 to relative residual below 1e-10. Numerical near-zeros in this table are not labeled exact identities.

### Why the singlet equations give full stationarity, but not stability

An invariant effective potential has an SM-fixed gradient at an SM-fixed point (compact-group averaging/equivariance). Hence nontrivial SM irreducibles cannot acquire a tadpole there. The SM-fixed gauge directions have zero directional derivative by gauge invariance. In a sufficiently small neighborhood where the gauge orbit rank stays 67, the remaining ten singlet equations exhaust the possible gradient components. The code verifies this full tangent decomposition and the full 188-component gradient; it does **not** infer positive physical curvature from singlet positivity. All eleven tree physical flats transform as an octet plus triplet and are non-singlets, so they are absent from the invertible singlet block but must be tested separately.

## 4. Residual scaling and full physical stability

For the full real-part unresummed determinant, inserting only the leading shift gives:

| epsilon | full gradient norm | norm/epsilon^3 | full physical Schur min/epsilon^2 |
|---:|---:|---:|---:|
| 1e-7 | 1.31260e-14 | 1.31260e7 | 1.35113 |
| 5e-8 | 1.82714e-15 | 1.46171e7 | 1.27602 |
| 2.5e-8 | 2.51790e-16 | 1.61145e7 | 1.23367 |

The logarithmic growth of the scaled residual is compatible with the soft-scalar epsilon^3 log epsilon term. The full physical curvature approaches the predecessor's leading octet coefficient 1.18165820923507; the triplet coefficient is 1.40673480316541. These are coefficients of epsilon^2 M^2, with 1/(64 pi^2) included. Both values are read from the actual high-precision predecessor receipt, not rounded input cutoffs. The r=3 negative control gives -1.3074103 and -1.6948383 instead.

At the first shifted point the minimum **tree** scalar mass squared is -2.17984e-10 M^2. Thus log m_tree^2 has an imaginary part. Off-shell tree Goldstone/flat masses cannot be used as physical tachyon diagnoses of the loop-improved stationary point, but equally they cannot be ignored to declare a real smooth full CW action. The finite-difference Schur diagnostics in this table are explicitly real-part diagnostics, not a certified full quantum solution.

### Constructive analytic hard-mode continuation

Isolate the 110 massive eigenvalues of H0 by the spectral gap at x0, retaining the analytic spectral subbundle above 1/2 in a small neighborhood. Keep **all vector and fermion determinants**. On the SM-fixed slice the twelve unbroken vectors stay exactly massless and contribute zero; the massive vector and fermion eigenvalues stay separated from zero. The resulting Lhard is analytic locally **on the SM-fixed slice**. Away from that slice the unbroken-vector terms have the familiar angular fourth-order logarithms; they are C2 rather than analytic, sufficient for the leading Hessian discussion. This is a definite hard-mode one-loop functional, not an assertion that the 78 soft scalar fields do not exist.

The ten-equation map is G(u,epsilon)=partial_u[V0(x0+Zu)+epsilon Lhard(x0+Zu)]. At (0,0), G=0 and D_u G=K is exactly invertible. Ordinary finite-dimensional IFT therefore gives a unique local singlet branch, u(epsilon)=-epsilon K^-1 t+O(epsilon^2). Symmetry and gauge transversality above turn it into full stationarity. This is a constructive conditional local-existence result **for the hard-mode functional**, with an explicit inverse and first derivative; no epsilon-radius interval has been certified.

At epsilon=1e-7, direct Newton solution reduces projected residual (divided by epsilon) from 8.96e-8 to 8.59e-13; the full canonical gradient is 2.40676e-19. Nonzero coordinates are approximately

    u1=u2=-3.99057135054571e-7,
    u3=-4.44064467272687e-7,
    u7= 1.62004831768023e-6,
    u8= 1.32843054130335e-7.

The complete 121x121 physical Hessian is evaluated at this stationary point. Decompose the physical slice into the 110 tree-massive directions P and eleven flats F, and form A=P^T H P, C=P^T H F, D=F^T H F. The Schur complement D-C^T A^-1 C is tested, including mixing, with two finite-difference steps:

| derivative step | min(A)/epsilon | min(Schur)/epsilon^2 |
|---:|---:|---:|
| 2e-5 | 0.999999696781 | 1.181668317922 |
| 1e-5 | 0.999999696781 | 1.181668133656 |

At leading order A=epsilon Hpositive+O(epsilon^2), C=O(epsilon^2), and D=epsilon^2 diag(m8 I8,m3 I3)+O(epsilon^3). The inverse-mixing correction is O(epsilon^3). Analytic singlet continuation, C2 angular behavior and the strict positive leading margins prove existence of some sufficiently small weak-coupling neighborhood of strict hard-mode local minima modulo gauge. The numerical sample is supportive, not a validated explicit radius.

For an IR-resummed full potential, extension of that claim is **conditional** on its remainder preserving the massive gap and the reduced angular Schur margin, e.g. ||delta A||=o(epsilon), ||delta C||=o(epsilon^(3/2)), ||delta Schur||=o(epsilon^2), with a sufficiently regular invariant singlet gradient. Those premises have not been calculated here. The singular unresummed second derivatives do not discharge them. No global orbit selection, physical pole masses, all-orders vacuum, global anomaly, KK matching or alpha result follows.

## 5. What Lean actually proves

`Formalization.lean` compiles in the existing Lean 4.32.1 kernel-only environment. Five declarations print **no axioms** and the process exits zero; no sorry is used.

- `local_stationary_from_contraction_tail` constructs Cauchy iterates from an explicit tail bound plus decay modulus, uses explicit completeness, proves invariant closed-ball membership by induction, obtains a fixed point using continuity/shift/unique limits, then obtains stationarity from the supplied Newton fixed-point bridge. It does not assume existence of the stationary point. Contraction estimates, metric/analytic structure and the gradient bridge remain premises; this is not a Mathlib formalization of the physical IFT.
- `leading_displacement_cancels` constructs the displacement from a right inverse and derives linear tadpole cancellation with explicit negation compatibility.
- `schur_transfer` derives full quadratic positivity by completing the square, using positivity/nonnegativity of **both** blocks and the invertible triangular nonzero split. It does not infer positivity from the singlet block.
- a finite Z3 example instantiates the displacement result, and `wrong_sign_control` proves the opposite-sign candidate cannot solve that example.

The exact E6 matrices and rational K inverse are Python certificates, not Lean-reified matrices. Numerical logarithms and eigensolvers are not inside the Lean trusted kernel. All review is self-assessed and AI-assisted; hosted CI and expert review were not run.

## Reproduction and scope of writes

Only `gap-investigation/shifted-vacuum-gate` is owned/written. Canonical predecessor report, code, receipt and verification files were read; their source hashes and actual diagnostic replay are checked by this lane. No repo AGENTS/current-intent/memory file was found by the initial native discovery; the gap-investigation README and relevant predecessor reports supplied current intent.

Run:

    C:/Users/mikeb/AppData/Local/hermes/hermes-agent/venv/Scripts/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/shifted-vacuum-gate/run_checks.py

The runner checks the **already existing** receipt before recomputation, replays both calculations, builds Lean and its public Challenge, exercises tamper/missing-file/wrong-sign controls, and stores actual exits/stdout plus SHA256 values in `verification.json`. `development-receipt-leading-only.json` preserves the successfully replayed intermediate result before the hard-mode calculation was added. Initial file-tool writes landed in a Cygwin shadow path; only this owned lane was copied to native C:\Users\mikeb and all executed files are now canonical. A direct Lean shell launch also failed its root-directory check; native subprocess cwd fixed it. Neither failure is counted as a successful build.
