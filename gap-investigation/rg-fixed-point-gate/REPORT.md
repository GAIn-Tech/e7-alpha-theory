# E7 RG fixed-point gate: a real asymptotic lever, not an alpha solution

## Outcome and scope

Nonlinear running opens a mechanism the earlier affine gate did not test: in a specified massless gauge-matter theory, different gauge boundary couplings can approach the same infrared fixed point. Here a minimal *family* means one gauge group, one matter representation, no elementary scalar or Yukawa sector, not a claim that its successful member has the smallest possible number of particles.

For compact simply connected E7 with N massless Dirac fermions in 56, exact two-loop algebra admits an interacting IR zero precisely for integer N=4,...,8. One Dirac 56 has no positive one- or two-loop interacting zero. N=8 is the closest integer below loss of asymptotic freedom and is the weak-coupling example chosen by that rule, not by any experimental coupling target. This reproduces a known exceptional-group Banks-Zaks mechanism, new to this repository's gap test rather than new to physics.[1]

The N=8 fixed point is perturbatively promising, but extremely weakly attractive. It fixes a limiting E7 coupling in a declared convention, not a finite-scale electromagnetic observable. No CODATA value enters the code, matter choice, or acceptance conditions. No Standard Model matching is claimed.

## Action, conventions and sourced inputs

Work in four dimensions, non-supersymmetric, on the exactly massless fermion subspace:

`L = -1/4 F^a_mu_nu F^{a mu nu} + sum(i=1..N) i bar(psi_i) gamma^mu (partial_mu - i g A_mu^a T^a_56) psi_i`.

Here `F^a=dA^a+g f^{abc} A^b A^c`, with the usual antisymmetrized components; gauge fixing/ghosts are implicit. There are N four-component Dirac fermions, equivalently 2N two-component Weyl fields, and **zero real or complex scalars**, no gaugino, no Yukawa couplings and no scalar potential. This is vectorlike: Dirac conjugate pairs avoid chiral gauge-anomaly obstructions. Bare masses are set to zero as a model restriction, not derived. A mass deformation or breaking sector would leave this restricted system. The canonical action and mass-independent scheme convention are those of the original beta-function calculation.[2]

Hermitian generators obey `Tr_R(T^a T^b)=T(R) delta_ab` and `sum_a T^a T^a=C2(R) I`. Choose the sources' normalization parameter b=1:

`CA=C2(adj)=T(adj)=18; TF=T(56)=6; CF=C2(56)=57/4; dimG=133; dimF=56`.

The exceptional-group calculation lists these in Table I (p.7); the original general beta-function paper gives CA, TF and dimensions in its table following eq.(16), with `CF=TF dimG/dimF`.[1][2] The exact executable trace identity checks `56*(57/4)=133*6`. An intentional doubled-CF-only negative control fails. These are independently sourced, not inherited from exp44's inconsistent normalization.

The separate `../next-gate/REPORT.md`, read during this investigation, derives the same convention from full weights: Bphys=2B0, with trace coefficients 6 and 18; B0 instead doubles **all** Casimirs and indices. We do not rerun/count that lane's representation proofs. Its illustrative rigid N=1 SUSY two-chiral-56-plus-singlet model is **not** this nonsupersymmetric Dirac family.

Set `a=g^2/(16 pi^2)=alpha_E7/(4 pi)`, `t=ln(mu)`. Then

`da/dt = -2 a^2 [b0 + b1 a + b2 a^2 + ...]`,

or `dg/dt=-b0 g^3/(16 pi^2)-b1 g^5/(16 pi^2)^2+...`. The factor 2 matters: the original source defines its a-beta against `ln(mu^2)`; the exceptional paper eq.(2) uses `(8 pi)^(-1) d alpha/d ln(mu)`.[1][2]

For Dirac flavors, the first two universal coefficients and the MS-bar three-loop diagnostic are Appendix A, eqs.(A1-A3) of source 1 and eq.(8) of source 2:[1][2]

```
b0 = (11/3) CA - (4/3) TF N = 66 - 8N
b1 = (34/3) CA^2 - [4 CF + (20/3) CA] TF N = 3672 - 1062N
b2 = (2857/54) CA^3
   + [2 CF^2 -(205/9) CF CA -(1415/27) CA^2] TF N
   + [(44/9) CF +(158/27) CA] TF^2 N^2
```

Counting Weyl fields instead replaces N by N_W/2, giving `b0=66-4N_W`, not the Dirac formula with N_W substituted directly. The two-loop fermion contribution is likewise halved per Weyl field. Only even N_W=2N is in the chosen Dirac family. No scalar beta coefficients are needed or silently included.

## Existence and stability: exact results

At one loop the only fixed point is a=0 for every allowed integer N: b0 vanishes at the noninteger value N=33/4. For N<=8, the Gaussian point is UV attractive (marginal at linear order); for N>=9 it is IR attractive. A formal continuous N=33/4 would make the entire one-loop beta vanish, but two-loop running removes that artifact; it is not an allowed integer matter theory here.

At two loops `a*=-b0/b1`. An asymptotically free positive zero requires `b0>0>b1`, equivalently `204/59<N<33/4`. Exact Z3 integer classification returns N=4 through 8, with no search outside a bounded diagnostic table. For nonnegative integer N there is **no** b0<0<b1 region and hence no interacting two-loop UV-attractive zero in this family. For N=0,...,3 the positive-coupling flow has no two-loop zero; for N>=9 both coefficients are negative and the Gaussian IR zero remains.

The slope at a positive zero is `omega=beta'(a*)=-2 b0^2/b1>0`. Since the IR corresponds to decreasing t, this sign means IR attraction, not UV attraction. For `0<a<a*`, beta<0, so a increases toward a* as mu decreases; above a*, beta>0, so a decreases toward a*. Statements about the high-coupling side are properties of the truncated polynomial only, not evidence it remains reliable there. The AF trajectory lies in `0<a<a*`.

| N Dirac | b0 | b1 | a* (two loops) | omega | CA a* | abs(b2 a*/b1) |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 58 | 2610 | none | — | — | — |
| 4 | 34 | -576 | 17/288 | 289/72 | 17/16 | 242981/18432 |
| 5 | 26 | -1638 | 1/63 | 52/63 | 2/7 | 4369/2184 |
| 6 | 18 | -2700 | 1/150 | 6/25 | 3/25 | 6707/10000 |
| 7 | 10 | -3762 | 5/1881 | 100/1881 | 10/209 | 720515/3145032 |
| 8 | 2 | -4824 | 1/2412 | 1/603 | 1/134 | 6745/215472 |

Every table entry is recomputed with Fraction in `check_rg.py`. This is not a fit over representations, scalars, thresholds or experimental values.

## Perturbative reliability, not a fabricated remainder bound

A one-loop calculation cannot alone establish the interacting root: the one- and two-loop terms cancel there by definition. Their ratio being one is thus not itself a convergence test. Assess group-weighted expansion parameters and the next independent term.

For N=8, `CA a*=1/134`, `CF a*=19/3216`, and `N TF a*=4/201`. The leading mass anomalous dimension in the convention `-d ln m/d ln mu` is `6 CF a*=19/536`, using source 1 eqs.(3),(A5).[1] These are small. In MS-bar `b2=-364230`; the magnitude of the third-loop beta term relative to the second at the two-loop root is exactly `6745/215472`. Exact rational bisection encloses the unique positive root of `2-4824 a-364230 a^2=0`; it is approximately `0.0004023695493699846`, a relative downward shift of approximately `0.029484646919597138` from a2. The receipt stores rational endpoints, not a floating-point equality test.

This roughly 3% shift supports a useful weak-coupling candidate, **not** a rigorous all-orders error bar or a proof of the full quantum conformal phase. The first two beta coefficients are universal in the specified mass-independent setting, whereas higher coefficients and the coordinate value of a fixed-point coupling depend on scheme.[2] No all-orders beta ansatz or ladder estimate is accepted as a theorem. N=4,5 have next-term ratios exceeding one and cannot support a reliable two-loop prediction; N=6 has a large correction, N=7 a smaller but non-negligible one. We make no exact conformal-window claim for those stronger-coupling cases. There is no continuously adjustable color rank for E7; analytic continuation in flavor number is a perturbative organizing device, not additional physical matter choices.[1]

Changing generator normalization rescales a and the coefficients consistently; it does not alter invariant expansion products such as CA*a or create an electromagnetic prediction. Reporting `alpha_E7*=4 pi/2412` is a convention-dependent E7 perturbative result, not identifying e or its Thomson-limit alpha.

## Does attraction remove boundary sensitivity?

**Asymptotically, conditionally yes.** For the two-loop massless model, initial conditions in the AF basin all tend to a* as t tends to minus infinity. A bounded monotone trajectory can only approach a zero; the sign structure excludes a=0 as the IR limit for strictly positive AF initial data. The exact fixed point trajectory is also allowed. Linearizing near a*,

`delta a(mu) = delta a(mu0) (mu/mu0)^omega`.

At N=8, omega=1/603: halving an infinitesimal displacement in this linearized regime requires `mu/mu0=2^(-603)` (not a physical scale assignment). The receipt's corresponding squared-scale ratio is `mu^2/mu0^2=2^(-1206)`. Attraction is exceptionally slow precisely where perturbation theory is best. This is a local sensitivity estimate, not a global flow simulation or an accuracy guarantee.

**At any finite regular interval, no exact erasure.** A polynomial beta function is locally Lipschitz, so distinct finite initial values cannot merge while the solutions stay finite. More explicitly, for the N=8 two-loop beta and two solutions x(t),y(t), their difference satisfies

`d(x-y)/dt = (x-y) [-4(x+y)+9648(x^2+xy+y^2)]`.

Z3 checks this polynomial factorization. On a finite regular interval the bracket is finite and continuous, so the difference equals its initial value times an exponential of its integral, which is strictly positive. Thus a nonzero difference stays nonzero. The analytic ODE uniqueness/exponential argument is provided here, **not** claimed as a Lean/Z3 theorem of analysis. Z3 separately checks injectivity of multiplication by a positive factor. In general the sensitivity Jacobian is `exp(integral beta'(a(t)) dt)`, nonzero at finite regular time. It can tend to zero in the infinite IR limit without contradiction.

A crossover/RG-invariant scale still labels trajectories. Finite hierarchy can suppress uncertainty, but a sufficiently long massless unbroken interval, its endpoints, the basin, and a quantified tolerance must be specified. Imposing `a=a*` exactly at a finite scale is an additional trajectory/boundary choice unless an independent construction selects the conformal theory. Relevant fermion masses, symmetry breaking, and thresholds can end the flow before its limit. Asymptotic freedom in the UV alone does not select the crossover scale.

## Missing bridge to a physical alpha prediction

The following are still missing, and not supplied by the fixed-point algebra:

1. An independent reason for E7 and N=8 massless Dirac 56s rather than other matter, and protection or derivation of masslessness; the minimal N=1 Dirac member fails the interacting-zero gate.
2. An E7-breaking sector, potential/vacuum, breaking scales and full massive spectrum. Adding scalars, Yukawas or supersymmetry changes beta functions and introduces stability directions. This report gives gauge-direction stability **only on the fixed massless subspace**, not IR stability under all action deformations.
3. A Standard Model chiral spectrum and actual subgroup/charge embedding, including hypercharge normalization/embedding indices, electroweak breaking and the relation of gY and g2 to e. A simple-group coupling is not already electromagnetism.
4. Threshold matching at each heavy mass and all subsequent gauge/matter running in a specified renormalization scheme; possible abelian kinetic mixing where multiple U(1)s survive; conversion to the desired low-energy observable, including massive QED and hadronic effects as appropriate.
5. A reason a finite matching scale is close enough to the IR limit, or independently fixed trajectory data, plus higher-loop/nonperturbative error control. No target-informed threshold or boundary correction is allowed.

The earlier affine no-selection result is therefore not a blanket RG no-go. This gate establishes a concrete attractive alternative in a restricted family, while showing exactly why it does not yet determine measured alpha. Stop here rather than introduce adjustable breaking scales to match a number.

## Verification, disclosure and reproduction

`check_rg.py` generated `receipt.json`, 10 named SMT-LIB obligations, then default-mode replay loaded those existing files without regeneration and compared the deterministic exact payload and source hashes. Nine unit tests include negative normalization/window controls and a three-loop rational bracket. Source snapshots are `exceptional-source.txt` and `beta-source.txt`, saved from actual PDF extraction; `sources.json` holds verified verbatim evidence and source IDs. `verification.json` captures real subprocess arguments, return codes, output and artifact hashes.

```
C:/Users/mikeb/e7-alpha-theory/gap-investigation/.venv/Scripts/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/rg-fixed-point-gate/check_rg.py
C:/Users/mikeb/e7-alpha-theory/gap-investigation/.venv/Scripts/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/rg-fixed-point-gate/check_rg.py --test
```

Use `--write` only for deliberate initial receipt generation; default verification fails if evidence is missing/stale. Z3 proves the encoded algebra conditional on supplied beta coefficients and group data, not those physical inputs themselves. No new Lean proof, full Mathlib build, hosted CI, lattice calculation, independent expert review, publication or push is claimed. Research/code/prose are AI-assisted, with primary-source inspection and local executable checks. Only this gate's repository directory is written. The known file-tool shadow-path issue occurred and was corrected by native Python byte-for-byte copying before canonical execution.

## Sources

[1] https://arxiv.org/pdf/1206.2652
[2] https://arxiv.org/pdf/hep-ph/9701390
