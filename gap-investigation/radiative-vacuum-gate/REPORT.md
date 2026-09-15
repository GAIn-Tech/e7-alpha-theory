# Bounded radiative vacuum-alignment gate

## Verdict

**A conditional lower-order repair exists at leading one loop for the declared renormalizable field content.** The complete E6 vector determinant gives positive curvature to both formerly flat SM multiplets, and puts the fixed-norm SU4 x U1 competitor above the SM orbit. The already-declared scalar potential contributes with the opposite sign. Their sum still lifts all eleven physical angular flats in an open coupling interval. No engineered dimension-16 operator is used anywhere in this calculation.

For the explicitly declared family Vtree = lambda V0, with V0 exactly the predecessor's sum of squares, define r=lambda/g6^2. With the kinetic convention below, both angular masses are positive for **0<r<2.1513814517**. The SM orbit is also below the SU4 x U1 comparison orbit for **0<r<1.8835648441**. These are calculated conditional inequalities, not measured/fitted couplings. r=1 is an interior diagnostic point; r=3 is an executed tachyonic negative control. This does not establish global selection among all orbits, a fully renormalized combined-model vacuum, or a prediction for alpha.

## 1. Prerequisite and canonical normalization

The canonical `e6-vacuum-gate/checks.py` was inspected before deriving this calculation and its saved receipt was subsequently independently replayed by this lane. That replay itself replays the exact breaking/embedding predecessors. It checks the full 186-field V0 Jacobian rank 109, 66 gauge directions, and eleven physical zero modes, and the uniqueness of the adjoint quartic. No dimension-16 lifting is used as a physical premise, though the predecessor replay necessarily also executes its separate engineered-EFT checks. The anomaly extension report was read, not independently re-solved here; its local anomaly cancellation remains a predecessor input.

Take h1=M s0, h2=M s1, A0=6 M Y, I2=Tr27 A^2=180 M^2. The predecessor allowed an unspecified positive adjoint kinetic coefficient. We now explicitly fix it, rather than claiming its inertia calculation fixed physical masses:

    B(U,V)=Tr27(UV)/3,
    Lkin = sum_i |D h_i|^2 + (1/2) B(D A,D A),
    Lgauge = -1/4 sum_a F_a^2,   B(Ta,Tb)=delta_ab.

This agrees with the breaking gate's Bphys=2 Cartan matrix; Tr27(Ta Tb)=3 delta_ab. Real/imaginary h coordinates have metric 2; real adjoint coordinates have metric B. We whiten the original nonorthogonal Chevalley-derived basis with its actual Gram matrix, not a Euclidean identity. A different independent adjoint kinetic normalization changes the scalar/gauge mass ratio and requires recomputation; it is action data, not a convention to ignore after fixing A0.

The full E6 gauge matrix is

    (mV^2)ab/g6^2 = B(i[Ta,A],i[Tb,A])
                    + 2 Re sum_i (Ta h_i)^dagger (Tb h_i).

For each of 36 positive roots, E+E^T and i(E-E^T) have trace norm 12. Thus each normalized root plane has two equal eigenvalues

    m_alpha^2 = g6^2 [(alpha(A))^2 + M^2 n_alpha/2],

where n_alpha counts actual raising/lowering links from the two singlets. This coefficient is derived from the representation matrices and canonical kinetic term, not assigned as a threshold mass. The remaining six Cartan eigenvalues are A-independent on this Cartan orbit. The code independently assembles and diagonalizes the full 78x78 matrix and matches this root formula at both comparison orbits.

External X and Phi affect only the A-independent abelian/Cartan block: A is X neutral, commutes with Cartans, and the individual singlet expectation values have no root expectation. Including their abelian mixing therefore does not change this bounded angular determinant. This is not a KK-tower calculation; it is the declared four-dimensional canonical truncation.

## 2. Sourced one-loop prescription and derivatives

Use dimensional regularization, modified minimal subtraction (MS-bar), Landau gauge:

    V1,V = 3/(64 pi^2) sum_a m_a^4 [ln(m_a^2/mu^2)-5/6],
    V1,S = 1/(64 pi^2) sum_real_s m_s^4 [ln(m_s^2/mu^2)-3/2],
    V1,F = -2/(64 pi^2) sum_Weyl_f m_f^4 [ln(m_f^2/mu^2)-3/2].

Source: Stephen Martin, hep-ph/0111209v2, section 3, equations (3.1)-(3.5); its loop-expansion convention factors 1/(16 pi^2) from V^(1). The original PDF text was retrieved and retained as `sources/martin-0111209.txt`. In particular 5/6 is not replaced by 3/2 using a supersymmetric DR prescription.

Write a=A0/M and b=H1 for the octet, b=H5 for the triplet, represented on all 27 weights. In each case Tr27(ab)=0, B(b,b)=4. Use the genuine fixed-norm curve

    A(t)/M = (a+t b)/sqrt(1+k t^2),  k=Tr27 b^2/180.

Its acceleration subtracts the radial derivative. A straight-line Hessian of V1 alone would give the wrong effective angular mass before radial minimization. For a root, d=alpha(a), e=alpha(b), x=d^2+n/2, x'=2de, x''=2e^2-2kd^2. With f(x)=x^2(ln x-c),

    f'=x(2 ln x+1-2c),   f''=2 ln x+3-2c,
    d^2 f/dt^2 = f''(x)(x')^2+f'(x)x''.

Massless x=0 terms start as t^4 ln(t^2) and contribute zero second derivative; we do not evaluate ln(0). Decimal 70-digit analytic derivatives are crosschecked by symmetric finite differences at three step sizes down to 1e-7. Unbroken SM covariance extends the one octet/triplet representative to the entire irreducible multiplet; these are exactly the 8+3 physical flats in the predecessor. Gauge-orbit directions remain gauge directions, not additional physical scalars.

## 3. Results, with loop prefactors displayed

Define SV by V1,V=3 g6^4 M^4 SV/(64 pi^2), omitting angular constants, and SS by V1,S=lambda^2 M^4 SS/(64 pi^2). The canonical second derivatives (divide by B(b,b)) are:

| contribution | octet | triplet |
|---|---:|---:|
| SV | +314.309637430745 | +377.820339095258 |
| SS for V0 | -196.528972295450 | -244.890392998612 |

Thus the leading angular curvature masses are

    m8^2 = M^2/(64 pi^2) [942.928912292235 g6^4 -196.528972295450 lambda^2],
    m3^2 = M^2/(64 pi^2) [1133.461017285774 g6^4 -244.890392998612 lambda^2].

The numerical coefficients are computed from the exact representation, not a fit. The receipt retains more digits than displayed. At r=1, the bracket coefficients divided by g6^4 are +746.399939996785 and +888.570624287163. At r=3 they become -825.831838366811 and -1070.552519701733: loop lifting is not automatically stabilization.

Compare the SU5 fundamental eigenvalues (-2,-2,-2,3,3) against sqrt(3/2)(1,1,1,1,-4); both give Tr27 A^2=180 M^2. The second has SU4 x U1 stabilizer. The calculated energy difference is

    V1(SU4)-V1(SM)
      = M^4/(64 pi^2) [4088.301237615522 g6^4 -1152.342916355750 lambda^2].

This proves only this two-orbit comparison, not global minimization on the adjoint sphere. Between r=1.8835648441 and r=2.1513814517 the SM remains locally angular-stable but this SU4 competitor is lower. The full gauge-only term does NOT stabilize the wrong competitor for this chosen ratio of singlet/adjoint norms; extrapolation to other VEV ratios is not justified.

## 4. Scalar and fermion content: no new spectators

The scalar determinant is calculated for lambda times precisely the existing V0, not for an invented scalar mass ansatz. At every point of this SU5 sphere all V0 residuals vanish, hence Hess V0=2J^T J. Whiten its 186-column Jacobian with h metric 2 and adjoint metric B, then compute the nonzero eigenvalues using 2JJ^T.

Independently, the Ah residual block has the form diag(a_w^2)+2K B^-1 K^T. Grouping weights with equal squared SU5 characters makes this a set of constant rational blocks plus a_w^2 times the identity. The inverse-Gram matrix and residual blocks are checked by integer matrix identities; rational eigenvalue multiplicities are certified by exact rank, not a floating threshold. This gives an independent scalar spectral formula with offsets 0,1/2,1,5/3. Its analytic derivatives and 70-digit finite differences agree, and a full-matrix floating diagonalization provides an additional crosscheck. The exactly constant radial eigenvalue 4320 is removed before floating finite differences to avoid catastrophic cancellation; it is not removed from the trace-mass-fourth check. Norm/overlap residual masses are angular constants as well.

All predeclared renormalizable fermion masses are A-independent on this curve: yP Phi P Q and singlet spectator Yukawas depend on Phi, while allowed FFh masses depend on h1,h2. Their one-loop determinant is therefore angular constant, irrespective of unspecified flavor values. A bare P A Q term has X charge -3 and is forbidden. Phi P A Q is dimension five and was not declared in this action. No such term, arbitrary spectator, or adjustable fermion mass coefficient is inserted to obtain a favorable answer. New portal coefficients, or unequal coefficients of the V0 squares, change scalar threshold functions and would need a new calculation; their absence here is a renormalized action choice, not a symmetry theorem.

## 5. Counterterms and scale: why the full E6 answer matters

There is no independent renormalizable pure-E6 angular quartic. The allowed counterterms have the predecessor's form

    delta V27(h) + delta mA^2 I2 + delta lambdaA I2^2
      + sum_ij [delta mu_ij h_i^dagger A h_j
                 + delta eta_ij I2 h_i^dagger h_j
                 + delta kappa_ij h_i^dagger A^2 h_j],

plus field/vacuum renormalization, and in the anomaly extension the renormalizable Phi norm potential and portals |Phi|^2 I2 and |Phi|^2 h_i^dagger h_j. All restrict to angular constants here: A h_i=0 and I2,h,Phi norms are fixed. Consequently no independent finite E6-renormalizable counterterm can tune these leading angular signs. Changing finite renormalized scalar coefficients changes the declared tree action/thresholds, which is a different, explicitly parameter-dependent question.

For the complete gauge root spectrum the code obtains sum_root m_a^4/(g6^4 M^4)=16702 at both orbits and independent angular perturbations; the Cartan contribution is constant. The underlying reason is E6 invariance plus the unique adjoint quartic and allowed mixed invariants, not merely agreement of sample points. The full scalar trace m^4 is also constant. Thus explicit changes of mu or the vector subtraction constant cancel from the leading angular derivatives and energy differences; ln g6^2 and ln lambda cancel for the same reason. Coupling running changes this only at the next perturbative order. This explains the simple homogeneous r inequalities above.

If instead one keeps only the unbroken-SU5 gauge multiplet, its trace m^4 is angular-dependent. A standalone SU5 EFT permits both (tr5 A^2)^2 and tr5 A^4 counterterms; omitting the second and varying mu generates spurious alignment conclusions. Matching from the full E6 action fixes the finite SU5 quartic threshold; it is not a new free E6 quartic. The executed SU5-truncation negative control detects this nonconstant trace. Heavy E6 vectors cannot be dropped here without that matching.

## 6. Gauge dependence, perturbative scope, and next input

The effective potential away from extrema is gauge-dependent; its curvature is not automatically a pole mass. Andreassen-Frost-Schwartz, arXiv:1408.0287, discusses the Nielsen identity, order counting, and this distinction; its primary PDF text is retained. At order hbar, the Nielsen identity gives partial_xi V1=-C1 dot grad V0. The entire fixed-norm family used here consists of full tree stationary points, so the leading restricted potential is gauge independent under a regular perturbative expansion. This observation does not authorize gauge-independent claims about an arbitrary off-shell gauge-only determinant. In Landau gauge the zero tree Goldstone determinants vanish on the family; no 66 physical massless particles are added. Massless modes with t^4 ln t^2 behavior have finite second angular derivatives. Higher-order transverse derivatives can encounter the Goldstone IR problem and require resummation; no all-orders result is claimed.

Take g6^2=epsilon, lambda=r epsilon with fixed interior r and epsilon sufficiently small. The tree positive transverse masses are order epsilon, the new angular masses order epsilon^2/(16 pi^2), and their mixing-induced Schur-complement correction starts at higher order. Require group-weighted scalar/gauge loop factors and threshold logarithms small, not merely g6<1; the large radial normalization of V0 makes unit couplings an unsafe perturbative benchmark. The numbers g6=lambda=1 in the dimensionless spectral evaluation are factorization devices, not a claimed perturbative physical parameter point. There is an asymptotically weak-coupling region at fixed r=1 with strict leading angular margins. This is a substantive conditional perturbative repair of the eleven-flat obstruction.

**Next missing input:** specify the renormalized combined action at a matching scale (all independent V27/mixed/Phi portals, Yukawa structure, adjoint kinetic normalization and threshold scales), then solve its transverse one-loop tadpoles and verify the physical Hessian/Schur complement at the shifted stationary point, with IR/pole-mass treatment as needed. The existing positive transverse tree gap makes local continuation plausible in the stated weak-coupling expansion, but no complete shifted 186-plus-Phi-field stationary solution is certified here. Other competing orbits, global anomalies, KK thresholds, realistic masses and alpha remain separate gates.

## Evidence and reproduction

`diagnostic.py` owns the exact block calculations, Decimal derivatives, matrix crosschecks, countercases and exclusive-create/replay receipt. `run_checks.py` reads and verifies the existing receipt, runs actual replay and corruption/missing-receipt controls, and records subprocess output in `verification.json`. Run with the explicit native interpreter:

    C:/Users/mikeb/AppData/Local/hermes/hermes-agent/venv/Scripts/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/radiative-vacuum-gate/run_checks.py

No publication, other-lane edits, Lean theorem, hosted CI, expert review, full-model vacuum claim or electromagnetic fit. Initial bare-python background launch failed in the harness before script execution; native foreground execution succeeded. File-tool shadow paths were corrected by copying only owned files into the canonical native lane before execution.
