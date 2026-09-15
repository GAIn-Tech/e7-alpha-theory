# Adjoint radial numerical convergence gate

## Outcome

The predecessor's 256-versus-512 difference is a real logarithmic-endpoint quadrature bias, not an imaginary-cut ambiguity or a fermion contribution. The corrected scalar/fermion coefficient is **511999.946 - 238193.186 i**, in units epsilon^2 M^2. Relative to its 512-node receipt, the real coefficient changes by **-0.3645523614**. No predecessor is edited.

After end-to-end read-only replay of scalar, zero-momentum vector, finite transverse-vector, and recovered mixed-sector receipts, compatible strict-Landau bookkeeping gives **505145.100 - 235147.465 i**. This is **not a certified full pole, gauge-independent observable, or width**. The vector stationary shift -45.10700126487947 is included exactly once. The zero-momentum vector Hessian is not additionally added.

## Definition and conventions retained

The canonical isolated tree radial eigenvector satisfies H h=4320 h. Masses and s inside integrals are divided by epsilon M^2; Q^2=epsilon M^2. The action has V=epsilon sum f_r^2, f_r=x^T B_r x/2+c_r. We reuse the actual differentiated trilinear T=d_h H and quartic U=d_h^2 H, diagonalize the full 188-scalar Hessian, and retain its 78-dimensional soft block (not only its 67 gauge Goldstones). No new mass is assigned to the exact soft limit.

I(a,b;s)=integral_0^1 log[ta+(1-t)b-st(1-t)-i0] dt.

The scalar coefficient is the stationary tree shift plus sum U_hhii m_i^2(log m_i^2-1)/(32 pi^2) plus sum_ij T_hij^2 I(m_i^2,m_j^2;4320)/(32 pi^2). The ordered sum includes the identical-line factor 1/2; unordered mass-shell rows in the new receipt explicitly double unequal-shell weights. Summed weights reproduce the complete trilinear Frobenius contraction. Quartic tadpoles and the scalar stationary shift are not momentum bubbles and are not counted twice through an additional CW curvature. The inverse propagator is s-m_tree^2-Pi(s), with local MSbar poles removed and finite local counterterms zero by declaration.

The 27+1 Dirac y=1 blocks and single y=2,3 blocks depend only on Phi, not h. Their direct h-fermion vertices and direct 1PI are zero; the replayed fermion stationary shift is 3.7028601476e-32, numerical zero. No fermion quadrature causes this discrepancy.

## Channel diagnosis

Rows use squared masses; differences below mean weighted GL256 minus GL512, in coefficient units. Every active shell pair is retained in receipt.json, including numerically negligible ones.

| Pair | Difference |
|---|---:|
| (0,0) | 0.792270786265 |
| (0,1.5) | 0.150989213312 |
| (1,1) | 0.042492759773 |
| (1.5,1.5) | 0.037871947889 |
| (0,5) | 0.027123028729 |
| (5/3,5/3) | 0.014162065558 |
| (0,10) | 0.010141702012 |
| (0,16.5) | 0.009896315579 |
| (5,5) | 0.003459453086 |
| (0,36.5) | 0.001499210040 |
| (10,10) | 0.000613483596 |
| (16.5,16.5) | 0.000240840929 |
| (36.5,36.5) | 0.000051807486 |
| (9,9) | 0.000004909013 |
| (4,4) | 0.000001456214 |

The complete channel sum is 1.0908189794639545, within 4e-11 of the original 1.0908189794281498 (different floating summation order). The soft-soft shell dominates. Splitting at threshold roots does not remove logarithmic endpoint singularities, hence the slow approximately n^-2 convergence of ordinary Gauss-Legendre quadrature.

## Independent error evidence

For real roots r1,r2 of Delta=s(t-r1)(t-r2), the exact real integral is log(s)+F(r1)+F(r2), F(r)=(1-r)log|1-r|+r log|r|-1, with 0 log 0=0. Imaginary part is -pi times the length of the negative-Delta intervals. Complex-conjugate roots below threshold are handled with the real part of the complex primitive, not by discarding their imaginary parts. The script explicitly tests the closed radial-radial channel and the massless identity I(0,0)=log(s)-2-i pi.

A second evaluation uses adaptive arbitrary-precision tanh-sinh integration of the factored quadratic, split at all real roots, at 40 and 70 decimal digits. Factoring prevents subtractive cancellation at endpoints. The exact-root value is assigned zero only on a measure-zero endpoint if rounding lands exactly there; no neighborhood, finite mass, or denominator floor is introduced. Neither a log(abs mass squared) replacement nor dropping the i0 is used: the real log absolute Delta is paired with its exact signed cut.

| GL nodes | Scalar bubble real | Error from analytic |
|---|---:|---:|
|128|555572.468528224|5.798903536|
|256|555568.124996029|1.455371341|
|512|555567.034177049|0.364552361|
|1024|555566.760851707|0.091227019|

The analytic bubble is 555566.669624688 - 238193.1864245565 i. Sum of absolute channel-weighted analytic/adaptive differences is 8.60e-36 at 40 dps and 6.00e-66 at 70 dps. This checks endpoint resolution against a closed antiderivative rather than asserting a bound from two agreeing grids. The analytic eta scan approaches the exact zero-mass result: bubble differences at eta=1e-8,1e-16,1e-32 are 8.031e-6,1.330e-13,2.386e-29. The quartic eta log eta terms vanish continuously; their zero-limit sum is 21783.295989971135. Scalar stationary shift remains -65350.01921701597.

These are numerical discrepancies, **not certified interval enclosures**. High-precision integration does not upgrade double-precision action tensors, eigenspaces, or shell grouping to exact input data. Grouping follows the scalar predecessor's 8-decimal shell keys with actual mean masses; zero modes follow the independently replayed Ward kernel. We report coefficients only to 0.001, conservatively below the demonstrated numerical differences, not as a physical uncertainty estimate.

## Vector and mixed checks, combination

The finite VV predecessor uses an analytic root antiderivative at positive s, so its n=256/n=512 agreement is not an independent convergence check. Its older separate direct-grid checker differs by 0.21265 and floors denominators. This gate does not use that floor as evidence. It independently replaces all vector master integrals with the high-precision analytic and adaptive routines, retains the +2 evanescent projector term and identical-vector symmetry factor, and recomputes the weighted tensor contraction.

The result is 76.73560821014124 - 31.929018580578234 i; analytic/adaptive difference is 8.763e-67 and original double-precision receipt difference 1.117e-10. The separate vector seagull remains 15.035667088293076. The mixed checker reconstructs its saved tensors from the native action and replays its receipt: -6901.5107104635135 + 3077.6501949169956 i. Its separate 512-node tensor-parameter check differs by 2.274e-6; it is not upgraded to arbitrary precision by this audit. SV has no constant-background tadpole and does not contain the vector seagull. The recovered vector stationary shift is -45.10700126487947.

All combined terms share the same action, isolated tree shell, MSbar/Q convention, strict Landau boundary, inverse-propagator convention, and linear stationary-displacement prescription. Scalar+fermion, VV bubble, vector seagull, vector stationary displacement, and SV each enter once. The stored unrounded bookkeeping value is 505145.09996121324 - 235147.46524822008 i.

## Unclosed physical gates

No general-xi longitudinal/Goldstone/ghost or Nielsen cancellation is proved. The mixed predecessor's isolated-shell Schur-complement loop counting is retained, not replaced with computed one-loop off-diagonal amplitudes. Hard two-loop tadpoles, higher-order mixing, finite EFT/UV matching and independently fixed finite counterterms remain outside scope. A scheme change can shift the real coefficient. Gauge-artifact cuts cannot be read as physical widths. This gate does not derive the EFT from compactification or predict alpha.

## Reproduction and integrity

Run the native NumPy interpreter with -B:

`C:/Users/mikeb/AppData/Local/hermes/hermes-agent/venv/Scripts/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/adjoint-radial-pole-convergence-gate/verify.py`

mpmath 1.3.0 is vendored locally because the native environment lacked it. The existing receipt is mandatory for replay; --create uses exclusive creation and must not be used to conceal stale evidence. Every predecessor source/receipt/report/checkpoint is hashed before replay and checked unchanged afterwards. The saved deterministic payload and verifier hash are compared exactly. Release integrity additionally uses run_checks.py and manifest.json. No predecessor verification writer was invoked: zero-momentum and finite-vector calculation entry points themselves replay the saved receipts without writing.

Native path discovery exposed a file-tool shadow tree; the verifier was transferred to and executed from the canonical Windows repository, not merely written to the tool-visible shadow. No AGENTS.md or intent file was found in the native e7 repository; the legacy README was read as historical claims, not adopted as the scientific boundary. No hosted CI, Lean kernel proof, or independent expert review was performed.

