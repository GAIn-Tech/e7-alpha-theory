# Physical-flat resummed vacuum: finite IR advance, not a full-vacuum certificate

## Results

The complete 188-dimensional scalar decomposition is reconstructed from the canonical action: 110 massive directions, 67 gauge tangents, and eleven physical flats. Full 188x188 octet/triplet projectors and 11x11 matrices are retained in `matrices.json`. Projector closure residual is 9.92e-13; residual-symmetry commutators are below 4.65e-11. Actual unbroken-generator Casimirs are 3 on the octet and 2 on the triplet. Thus these are charged physical scalars, not eleven gauge Goldstones.

Recomputing the full hard one-loop functional and stationary displacement gives

    m8^2 = epsilon^2 M^2 (1.1816582 + ...),
    m3^2 = epsilon^2 M^2 (1.4067348 + ...).

These agree with the predecessor at its floating precision. The complete leading soft Ward cancellation has norm 2.09e-9 in coefficient units; changing the hard self-energy sign leaves 43596.75. No gauge mass is supplied by hand. The previously established radial Goldstone curvature singularity does not occur in the leading physical-flat two-Goldstone cubic: the complete soft-soft cubic with any physical-flat external leg has norm 1.86e-13.

**New finite next-order IR matrix.** From the covariant-action transverse scalar/vector kernel, with an internal *physical*, resummed scalar mass and a massless unbroken vector, the on-shell contribution is

    delta M_soft,SV^2 = epsilon^3 M^2 / (16 pi^2)
       [3 lambda8 (7 - 3 log(epsilon lambda8)) I8
        direct-sum 2 lambda3 (7 - 3 log(epsilon lambda3)) I3].

At epsilon=1e-7 its coefficient is **1.2313967 on the octet and 0.9679791 on the triplet**. Both are positive; neither splits its residual multiplet nor makes a tachyon. Relative corrections to the leading masses are 1.04209e-7 and 6.88103e-8. This is a finite projected 11x11 *sector*, not the completed NLO mass. The full matrices at three epsilons are in `gauge-soft-matrices.json`.

The nonanalytic log-epsilon matrix has eigenvalues -0.06734644 (eight) and -0.05344951 (three), multiplying epsilon^3 M^2 log epsilon. Its positive small-epsilon contribution vanishes relative to epsilon^2 masses as epsilon |log epsilon|. There is no absorptive part at this leading on-shell endpoint. However the massless-vector plus same-scalar threshold sits precisely at the putative mass: the momentum function has threshold nonanalyticity and its derivative cannot be treated as the isolated radial analytic-pole problem. No finite wavefunction residue, colored asymptotic particle, physical width, or all-gauge pole claim follows.

## Source-derived scalar matching: a cancellation missed by a Gaussian tadpole alone

Write V0=sum f_r^2, f_r=x^T B_r x/2+c_r, J_r=B_r x, H=2 J^T J at x0. For orthonormal physical-flat frame F define

    b_rab=F_a^T B_r F_b,
    T_iab=2 sum_r J_ri b_rab,
    U_abcd=2 sum_r (b_rab b_rcd+b_rac b_rbd+b_rad b_rbc).

These are differentiated action tensors, not assigned interactions. Eliminating the heavy normal coordinates h_i=-1/2 (H+)_ij T_jab q_a q_b gives

    Ueff_abcd = U_abcd
      - T_iab (H+)_ij T_jcd
      - T_iac (H+)_ij T_jbd
      - T_iad (H+)_ij T_jbc.

All 11^4 entries are computed. The bare quartic reaches 216; Ueff has maximum residual 4.01e-11, consistent with zero and with the tree stationary manifold. Consequently the scalar zero-derivative epsilon^3 log-epsilon coefficient Ueff_abcd (M1)_cd/(32 pi^2) vanishes within 1.32e-12 norm. Omitting heavy exchange leaves norm **12.21918**. This combines the heavy normal displacement/tadpole and the crossed heavy exchange contributions; keeping only the predecessor physical-soft Gaussian tadpole would not be a matched scalar stability calculation.

The remaining induced derivative tensor from h(q) is nonzero (Frobenius norm 0.1833333). Its coefficients scale as 1/M^2, and scalar loops at p^2,msoft^2=O(epsilon^2 M^2) first yield O(epsilon^4 M^2 log epsilon), not O(epsilon^3) nonderivative scalar masses. Loop-induced potential cubic/quartic couplings likewise begin at epsilon^2 and contribute beyond the scalar zero-derivative order just cancelled. These order statements do not omit massless unbroken gauge interactions: g^2=epsilon makes their calculated contribution epsilon^3 log epsilon.

A second bounded NLO piece, the heavy Schur matrix -F^T A P (P^T H P)^-1 P^T A F with A=T(delta)+Hess V1hard, is numerically zero (norm below 3e-21). This is compatible with residual representation selection; it is not a negative instability. Tiny negative floating eigenvalues are retained, not clipped. The script does not assert an exact representation-theoretic proof of that zero.

## Leading resummed effective action and double counting

In local quotient coordinates q with the heavy normal modes minimized at tree level,

    Gamma_soft = integral [1/2 g_ab(q) Dq_a Dq_b
                  - epsilon^2 M^4 W1(q/M) + ...]
                 + gauge kinetic terms + matched hard operators,

where Hess W1(0)=lambda8 I8 direct-sum lambda3 I3 and g(0)=I. D contains the actual unbroken generators extracted from the 79-generator action. The physical Gaussian trace starts at epsilon^4 M^4 log epsilon. Its value is -4.7099524e-29 M^4 at epsilon=1e-7. At one-loop resummation this trace replaces the original soft trace; at the next fixed order its first self-energy insertion must be subtracted as the matrix Frechet derivative, per Martin 1406.2355 and Elias-Miro et al. 1406.2652 retained in the predecessor sources. We never add the replacement trace and its un-subtracted fixed-order ancestor.

The 67 gauge tangents remain Ward zeros, not positive physical regulator masses. Gauge-fixed internal Goldstones are still required in hard matching. The present massless SV calculation sums only the unbroken gauge action inside the physical-soft representation; it is not a license to replace the full internal scalar spectrum by the quotient.

## Finite-momentum derivation and checks

The source is `adjoint-radial-mixed-pole-gate/finite_momentum.py`, definitions A,B,K, with inverse propagator s-m^2-Pi(s), Landau gauge and MSbar Q^2=epsilon M^2. Only those source function definitions are executed; no inherited radial coefficient is reused. Its massless-vector kernel is

    K(x,0,s)=3(x+s) B(x,0;s)+3 A(x)-2s,
    A(x)=x(log x-1), B=-integral log[t x-s t(1-t)-i0]dt.

At s=x>0, B=2-log x and K=x(7-3 log x). Independently, the covariant tensor numerator gives

    K(x,0,x)=-6x integral_0^1 (1-t) log(x t^2)dt -2x.

The -2x is the finite evanescent projector contribution. A transformed Gauss integral t=exp(-u), 0<u<60 agrees with the source master and closed result; the omitted tail is below 1e-21 in the bracket for the declared samples. This tail bound is not a certified quadrature or action-tensor error. Omitting the evanescent term changes the matrix coefficient norm by 0.1411932. K(x,0,0)=0 independently checks why this correction was invisible to the zero-momentum hard potential. No negative mass log, mass clipping, or fake Goldstone regulator enters the calculation.

## Exact missing terms and remaining stability boundary

The genuinely unresolved complete epsilon^3 mass coefficient must still contain hard two-loop matching and order-consistent hard wavefunction/stationarity contributions. To specify the missing calculation rather than assign it, set

    x*=x0+epsilon delta+epsilon^2 e+...,
    delta=-H+ grad V1hard,
    H e = -[1/2 T(delta,delta)+Hess V1hard delta
             +grad V2hard + t_soft^(3)],

on the gauge-transverse heavy subspace. The known Gaussian physical-soft tadpole is only one contribution to t_soft^(3), with subtraction/matching as above; it cannot set grad V2hard to zero. In fixed canonical frames the next curvature block requires

    F^T [T(e)+1/2 U(delta,delta)
          + (d_delta Hess V1hard)+Hess V2hard] F,

plus the transported quotient/metric terms, the heavy Schur term computed here, and momentum subtraction. At each leading soft shell, hard analytic self-energy momentum dependence adds lambda_r times the projected one-loop hard derivative at zero; the finite soft SV matrix above supplies a distinct nonanalytic contribution. The full gauge-fixed hard diagram set, counterterms and their stationary displacement must be matched in the same convention. Neither V2hard, its gradient/Hessian, nor the complete projected hard derivative is evaluated here. This is an explicit operator-level missing term, not a fitted coefficient or a bounded remainder.

Residual symmetry forces any symmetry-preserving scalar mass correction to have octet/triplet block form, but it does not fix either missing scalar coefficient. The computed IR terms favor the present local alignment; no demonstrated IR tachyon arises in these sectors. Without bounds on the omitted coefficients no numerical epsilon interval is certified for the actual quantum vacuum. The radial necessary window epsilon<7.4911e-4 for a 10% diagnostic cannot supply those missing bounds. Unknown cutoff/Wilson matching and background expansion remain separate; epsilon alone does not suppress unknown operators. This tuned renormalizable four-dimensional EFT is not the unresolved Tian-Yau compactification action or its stabilized solution.

## Reproduction and evidence class

Run the native NumPy interpreter on `run_checks.py`. Both scripts require existing receipts, check source hashes before replay and compare deterministic full matrix payloads without rewriting them. A missing-receipt subprocess control fails closed. All reported computation is floating action-tensor evidence with analytic order identities; no interval theorem, Lean proof, hosted CI or independent expert review is claimed. Predecessors are preserved. A file-tool Cygwin shadow write was transferred only within this owned lane to the canonical Windows directory before execution. The native NumPy environment lacked mpmath; independent integration uses transformed NumPy Gauss quadrature instead of installing packages.
