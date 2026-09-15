# Radial perturbative-validity window gate

## Outcome

**There is a nonempty small-epsilon domain for the computed radial one-loop diagnostics in the declared renormalizable truncation. There is not yet a certified controlled physical-pole window for the full EFT.** The latter requires the unresolved IR-stable quantum vacuum, finite matching/cutoff data and higher-order/off-diagonal bounds. No obstruction forces the diagnostic window to be empty, and no missing assumption is silently declared satisfied.

At fixed MSbar Q²=epsilon M² and strict Landau gauge, direct differentiation gives

    Pi'(s0) = epsilon (15.3221386283 + 0.7045652596 i),
    s0 = 4320 epsilon M².

The derivative's modulus is 15.3383292555 epsilon. An independent adaptive tensor/master calculation agrees to 2.55e-23 in coefficient units at the finer finite-difference step; this is numerical agreement, not an interval or physical uncertainty.

For an illustrative **analysis tolerance** tau=0.1 on each diagnostic below, the most restrictive computed necessary inequality is

    0 < epsilon < 7.4910982e-4.

For tau=0.01 and 0.001 its upper endpoint becomes 7.4910982e-5 and 7.4910982e-6. These are not measurements, fitted parameters, EFT matching choices, or rigorous remainder radii. They do not turn the large finite coefficient into a physical mass or width.

## Actual action and scaling

The canonical `shifted-vacuum-gate` action is V=epsilon M⁴ sum F_r(x/M)² with residuals quadratic in canonical fields. In particular its adjoint radial norm term is

    V_A = epsilon (3 r² - 180 M²)²,  r²=B(A,A),  r0²=60 M².

At the specified stationary alignment all Ah residuals vanish. The h1,h2 and Phi norms are M, and A=6Y. The full canonical background has ||x0||²=66 M², not M². Differentiation yields V_A''(r0)=4320 epsilon M²; this is the unique radial tree scalar eigenvalue. The code recomputes action T=d_h H and U=d_h² H and all scalar/vector shell weights.

The family sets g6²=gX²=lambda=epsilon>0 and y=sqrt(epsilon)(1,1,2,3). Hence masses squared are epsilon M² times the listed shell numbers, scalar cubic vertices scale as epsilon M, scalar quartics as epsilon, hVV vertices as epsilon M and derivative SV vertices as sqrt(epsilon). Every one-loop diagonal self-energy term scales as epsilon² M² (with loop factors already in its coefficient). The momentum argument is u=s/(epsilon M²):

    Pi(s)=epsilon² M² f(u),
    Pi'(s0)=epsilon f'(4320).

The derivative is at **fixed Q²**, not a derivative that resets Q²=s. Tadpoles, the stationary tree shift and momentum-independent seagulls do not contribute to Pi'. Direct radial Yukawa vertices vanish for the declared Phi-only masses. The compatible corrected coefficient, retained from the convergence receipt, is

    C = 505145.09996121324 - 235147.46524822008 i,
    delta s = epsilon² M² C,
    |delta s|/s0 = 128.980248132 epsilon.

With inverse propagator s-m_tree²-Pi(s), the next iteration from this diagonal sector would involve Pi'(s0) delta s, of order epsilon³ M². This is not a calculation of all two-loop terms. Likewise the Schur term from zero-tree-offdiagonal one-loop insertions scales as epsilon³ M² away from complementary poles, but its **coefficient has not been bounded**. The scalar isolation test below controls the known diagonal displacement, not the unknown norm of that Schur term.

The original action explicitly leaves epsilon and M free; no prior bound fixes them. Its illustrative epsilon=1e-7 is an unconstrained weak-family sample, not a parameter inferred from alpha or a desired mass. Q²=epsilon M² is a renormalization-scale prescription, not an equation selecting epsilon. Other allowed renormalizable couplings and finite matching values are set to zero as tuned action data, not by symmetry. This EFT is not a derivation from the unresolved E6 compactification.

## Momentum derivative: analytic and independent adaptive methods

For I(a,b;s)=integral log[D(t)-i0]dt, D=s t²+(a-b-s)t+b, differentiation gives

    I' = PV integral t(t-1)/D dt
         + i pi sum_{0<r<1} r(r-1)/|D'(r)|.

Polynomial division and the two roots give 1/s plus residues r(r-1)/D'(r) times log|(1-r)/r|. Below threshold, complex-conjugate roots use the continuous complex primitive. Endpoint residues with zero numerator are taken by their continuous cancellation; a coalescing threshold root is rejected, not regularized with a small denominator. I'(0,0)=1/s, while a massive open channel has a nonzero cut derivative. The i0 branch is retained throughout.

For the first method, these derivatives are inserted into analytically differentiated covariant-action scalar, VV and SV kernels. For the second, scalar and VV logarithms are evaluated with arbitrary-precision root-split adaptive tanh-sinh quadrature, and SV uses its **tensor-first** representation

    K_SV = (6s/v) integral [A(D0)-A(Dv)]dt - 2s.

Here A(D)=D(log|D|-1-i pi theta(-D)); the -2s evanescent term is kept. A five-point derivative at steps 0.01 and 0.005 differentiates these independent momentum functions. Moving roots are recomputed at every momentum. No fixed real-part branch, Goldstone mass, clipping, or integration through unresolved poles is used.

| Sector | Re f' | Im f' |
|---|---:|---:|
| scalar | 17.1508003987 | -0.01155486236 |
| VV | 0.00249026851 | -0.0000698863491 |
| SV | -1.83115203891 | 0.71619000832 |
| total strict Landau | 15.3221386283 | 0.704565259614 |

Adaptive discrepancies are 4.07e-22 and 2.55e-23. There are direct below-threshold rational-integral and equal-mass cut-slope controls. Action tensors and shell projectors remain double precision; physical/Goldstone decomposition changes the scalar Frobenius contraction by 4.75e-6 out of 2.675e7, a relative floating error below 2e-13. The check therefore uses relative, not unjustifiably tiny absolute, tolerance.

## Degenerate modes and thresholds

Squared masses below are divided by epsilon M². All 188 scalars are retained:

| scalar squared mass | multiplicity |
|---|---:|
| 0 | 78 = 67 gauge Goldstones + 11 physical flats |
| 1 | 3 |
| 1.5 | 24 |
| 5/3 | 1 |
| 2 | 2 |
| 4 | 33 |
| 5 | 6 |
| 9 | 20 |
| 10 | 4 |
| 16.5 | 12 |
| 36.5 | 4 |
| 4320 | 1 |

The 11 physical flats are the octet plus triplet. They are not discarded or presumed stabilized. Their radial flat-flat cubic squared contraction is 3421440, so deleting them would remove an actual channel. Their tree threshold is zero; loop-generated physical masses, if consistently established, are O(epsilon² M²), not an arbitrary positive regulator.

The 79 vector mass shells and multiplicities are 0(12), 0.8619522(1), 1(3), 1.5(24), 5(6), 10(4), 16.5(12), 25(12), 34.8047145(1), 36.5(4). The receipt keeps the unrounded means. The 12 unbroken vectors have zero active radial coupling at this order, but remain in the spectrum.

`receipt.json` enumerates each active physical/Goldstone scalar channel, active VV and SV channel, and all Landau projector master thresholds, including its weight, threshold `(sqrt(a)+sqrt(b))²`, and distance from 4320. It also retains inactive scalar pairs and the small omitted numerical support weight. The nearest active physical threshold is **146**, from mass-36.5 pairs, at distance **4174**. This is also the minimum over all active Landau masters. The radial-radial threshold is 17280 and is closed. Every other active channel is open at the tree shell. Open cuts are not a distance of zero: the local continuation on the appropriate sheet is limited by the branch point, not every point along a chosen drawing of its cut.

The nearest different scalar pole is 36.5, a distance **4283.5**. Although the radial-plus-massless kinematic threshold is exactly 4320, its scalar radial coupling vanishes structurally. At the vacuum the radial potential gives `T_h h=(3 rho/r0) h`; hence `e_soft.T T_h h=0`. The measured residual of this parallelism is 2.28e-13. An arbitrary deformation activating this channel requires new near-threshold analysis; multiplying a tiny floating noise weight by a divergent derivative is not meaningful. The numerical shell support classification is explicitly disclosed, not claimed as exact tensor certification.

### General Rxi is not a uniform gauge domain

Goldstone, ghost and longitudinal masses are xi a. Unphysical thresholds include `(sqrt(t)+sqrt(xi a))²` and `xi(sqrt(a)+sqrt(b))²`; complementary gauge poles occur at xi a. Their collision locations are saved channel by channel. For a=36.5, an equal-Goldstone threshold hits s0 at xi=29.5890411 and an unphysical pole hits it at xi=118.3561644. These finite positive xi values do not move when epsilon is made smaller. No epsilon window can enforce noncollision **for every xi**.

The exact conditional on-shell identity does not imply gauge-independent Pi'. Differentiating its displayed `(s-rho)` factors transfers the derivative from Landau to fixed nonexceptional xi, using actual physical C_ai and ordered Z_ab weights. `gauge-cutoff-receipt.json` enumerates all resulting thresholds/poles and obtains:

| xi | Pi'/epsilon | nearest unphysical threshold distance |
|---|---|---:|
| 0 | 15.322139 + 0.704565 i | 4283.5 |
| 1 | 16.446884 + 0.224545 i | 4174 |
| 10 | 24.989346 - 4.356261 i | 2860 |
| 100 | 60.774479 - 45.799186 i | 96.5 |

This table concerns the identity's unphysical differences; the independent physical threshold gap 4174 must also be imposed. Conditional identity transfer inherits floating Ward/kernel premises and zero finite wavefunction matching. At a threshold some sum may have a finite first derivative after cancellation while still lacking an ordinary analytic neighborhood. A finite value is not a license to apply an isolated analytic pole expansion there. Gauges scaling as 1/epsilon are outside fixed-gauge power counting.

## Quantitative conditional inequalities

The full stationary displacement is recomputed from the complete scalar/vector/fermion determinant:

    x_star = x0 + epsilon M d + ...,
    ||d|| = 40.4357841884,
    ||d||/||x0/M|| = 4.97730096467.

The worst block-relative displacement coefficient is 5.05291006451 (adjoint block); h1,h2 give 3.99061149638 and Phi 4.44064833496. The adjoint radial projection is -5.04592023289, not the total adjoint norm. Reconstructed leading displacement differs from the saved exact-inverse-based result by 1.27e-10, and the full linear stationarity residual is 8.55e-11 in coefficient units.

For any stipulated analysis tolerance tau, require each positive diagnostic coefficient times epsilon to be below tau:

| Necessary diagnostic | coefficient multiplying epsilon | epsilon upper for tau=0.1 |
|---|---:|---:|
| complex relative radial shift | 128.980248 | 7.75313e-4 |
| total relative displacement | 4.977301 | 2.00912e-2 |
| worst block-relative displacement | 5.052910 | 1.97906e-2 |
| strict-Landau wavefunction correction | 15.338329 | 6.51961e-3 |
| diagonal shift / other scalar pole gap | 130.079298 | 7.68762e-4 |
| diagonal shift / active threshold gap | 133.491776 | 7.49110e-4 |

The receipt separately retains real and imaginary relative shifts. Using only the real part would understate the complex displacement. At epsilon=1e-7, the complex shift ratio is 1.28980e-5, worst block displacement 5.05291e-7, wavefunction modulus 1.53383e-6 and threshold ratio 1.33492e-5. At epsilon=1 the loop shift is grossly nonperturbative. These tests exclude large epsilon in this prescribed calculation; they do not select the small sample as physical.

## EFT cutoff and operator expansion: epsilon alone is insufficient

The actual displayed action is a tuned **renormalizable** sum of squares, not the earlier engineered high-dimensional spectral potential. It does not specify a cutoff Lambda or a UV derivation of its missing Wilson coefficients. Treating it as an exact renormalizable truncation is conditional action data. A general EFT requires two different checks:

1. Derivative expansion: `p²/Lambda² = 4320 epsilon (M/Lambda)² << 1`. At tolerance 0.1 this gives epsilon < 2.3148148e-5 (Lambda/M)².
2. Background expansion: the adjoint invariant is `r0²/Lambda² = 60(M/Lambda)²` and the total canonical norm gives 66(M/Lambda)². These do **not** shrink with epsilon. Numerical canonical norm is a diagnostic; individual invariants and Wilson normalizations must ultimately be checked. For Lambda=M, momentum smallness can hold but the background expansion fails; for Lambda=10M its adjoint ratio is 0.6, still not below 0.1. No choice among these sample cutoffs is asserted as actual matching data.

There is a sharper obstruction to claiming that epsilon approaching zero controls *unknown* operators. Consider the allowed invariant counterfamily `c6 r^6/Lambda²`, not added to the actual action. Exact first-order algebra around r0 gives

    delta r/r0 = -5(c6/epsilon)(M/Lambda)²,
    delta m²/m_tree² = 10(c6/epsilon)(M/Lambda)².

The second line includes the induced stationary displacement: direct curvature alone would wrongly give 25 instead of 10. Thus a fixed nonzero c6 introduces a **lower** bound on epsilon, not merely a higher cutoff bound. At tolerance 0.1,

    epsilon > 100 |c6| (M/Lambda)².

For the illustrative unit coefficient only, overlap with the radial upper bound requires Lambda/M > 365.3653. For Lambda=M and c6=1 the inequalities have no overlap; the linearized example already excludes the supposed small-correction regime, not a claim about its nonperturbative minimum. Neither c6=1 nor Lambda=M is an assumption of the actual action. If a UV theory forced c6 to scale with epsilon, the bound would change, but no such result is supplied. Consequently the cutoff/operator-controlled domain is **undetermined**, not demonstrably empty or guaranteed, under the actual unspecified matching assumptions.

## Physical interpretation and precise remaining obstruction

The finite scalar and gauge-cut boundary values are retained, including their imaginary parts. Even with a conditional on-shell xi cancellation, they are not a decomposition into observable partial widths. No stable all-mode resummed vacuum, full higher-order self-energy remainder, finite UV matching, or physically matched radial resonance has been established. In particular, the eleven physical zero directions are not repaired by a small radial Pi' or by the positive hard-mode-only Hessian in the predecessor.

Thus the result is a computed nonempty **necessary diagnostic** domain within the fixed renormalizable truncation and nonexceptional gauges. The obstruction to calling it an actual controlled physical-pole domain is missing IR-vacuum and EFT matching/remainder information, not merely the size of C. There is also a precise impossibility of a threshold-free domain uniform in all positive xi. No alpha fit, stabilization assumption, artificial Goldstone mass, arbitrary new coupling, publication, or compactification identification is made.

## Reproduction and integrity

Run the native NumPy interpreter with bytecode disabled:

    C:/Users/mikeb/AppData/Local/hermes/hermes-agent/venv/Scripts/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/adjoint-radial-perturbative-window-gate/run_checks.py

Saved receipts are mandatory and hash-checked before replay; --create is exclusive creation and not a repair for stale evidence. `run_checks.py` replays this lane, the canonical convergence checks (including fresh native mixed action tensors), and the exact conditional symbolic Rxi identity with its designated SymPy interpreter. Negative controls cover massless scaling, wrong/omitted cuts, missing mixed sector, threshold collision, xi-independent wavefunction, wrong epsilon power, and omitted stationary displacement for the dimension-six example. Missing/tampered artifact controls fail closed. `verification.json` stores actual exits and stdout hashes. No Lean theorem, interval certificate, hosted CI or expert review is claimed.

File tools exposed a Cygwin shadow tree. Only this owned lane was transferred to the verified canonical Windows directory before execution; all reported receipts are native artifacts. No predecessor was edited or regenerated. The initial Frobenius absolute-tolerance failure is recorded above as a floating decomposition issue and replaced with an appropriately scaled relative invariant check, not interpreted as new physics.
