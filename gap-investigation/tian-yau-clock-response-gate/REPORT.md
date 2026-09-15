# Tian–Yau standard embedding: canonical moduli → clock response

## Outcome and claim boundary

The actual predecessor is the smooth Tian–Yau free Z3 quotient Q, tangent bundle standard embedding, identity Wilson line, visible E6 (not E7), h11=6, h21=9, nine 27 and six conjugates, net three. Butbaia et al. specify this geometry and discuss normalization of its physical Yukawas.[4] We keep the predecessor's geometry, bundle, orientation and large-radius/weak-string-coupling approximation. **Its unbroken E6 theory does not yet contain a specified realistic photon/atomic sector.** The ultraviolet coupling and its canonical gradient below follow from the heterotic action; the onward photon/clock map is explicitly conditional on additional breaking/matching data.

The advance over `atomic-clock-gate` and `clock-matching-gate` is to replace their freely chosen exponential scalar kinetic function with the sourced heterotic dilaton and Kähler metric, derive its universal tree gradient and its volume–dilaton mixing, and exhibit an actual same-geometry family. No alpha value, clock observation, arbitrary scalar mass or assumed oscillation was inserted. The tree fractional pure-dilaton response **is fixed by the leading action**, although not by net-three topology. The absolute intercept, mass-eigenstate direction and physical low-energy response are not fixed.

## 1. Conventions and dimensional reduction

Use signature (-+++), reduced Einstein-frame Planck mass M, connection convention `L_gauge=-1/4 g_a^-2 F_a^A F_a^A`, with a fixed generator normalization. Let Phi be the dimensionless ten-dimensional string dilaton, V the dimensionless **string-frame** CY volume, and `S=s+i a`, with `s=V exp(-2 Phi)>0`. Kim's section 3 explicitly concerns heterotic standard embeddings; equations (3.49)–(3.50) give this chiral field and `K=Khat-ln(S+Sbar)`, while (3.73), (3.79), (3.82) fix the inverse gauge-coupling convention.[2] A constant convention factor in dimensionless V or S is absorbed once into the definition of S and affine levels; it cannot be varied to fit a coupling.

The dimensional-reduction content can be written without an ambiguous trace prefactor:

```
S10,g = -(1/4 g10,0^2) integral d10x sqrt(-G_s) exp(-2 Phi) B(F_MN,F^MN)
S4,g = -(V_phys exp(-2 Phi)/(4 g10,0^2)) integral d4x sqrt(-g_s) B(F_mn,F^mn)
g_a^-2 = k_a s,       f_a^hol = k_a S                 [tree]
```

Here g10,0 and B define the ten-dimensional normalization, and the fixed string-volume unit is chosen to match the preceding sourced S convention. The integral of a spacetime gauge zero mode gives V_phys, not a Chern number. The universal exp(-2 Phi) string-tree prefactor and reduction are consistent with the sourced four-dimensional result `s=V exp(-2 Phi)`; no numerical 10D trace/alpha-prime coefficient is imported from a differently normalized action. For the level-one E6 commutant, k6=1 in this convention. The hidden factor shares the tree dilaton, not necessarily its loop corrections.[2]

The four-dimensional string gravitational coefficient is proportional to `s R_s`. Setting `g_E=(s/s_ref) g_s` gives a constant Einstein coefficient. In four dimensions, `sqrt(-g_s) g_s^mu rho g_s^nu sigma` is invariant under this Weyl rescaling: determinant weight +4 cancels the two inverse metrics' weight -4. **No extra s power multiplies F² in Einstein frame.** Weyl transformations do change dimensionful masses/scales; they must be consistently transformed in RG logarithms. Dimensionless local frequency ratios remain frame independent. Kim discusses this frame distinction and the loop-corrected linear/chiral dilaton map.[2, sections 2 and 3] We do not transplant the type-IIB Einstein-volume Kähler potential from his section 2.2 into the heterotic model.

## 2. Canonical coordinates, including volume

At leading large-radius tree order and vanishing charged-field background,

```
K/M² = -ln(S+Sbar) - ln V(t) + Kcs(z,zbar),
V(t) = (1/6) d_ijk t^i t^j t^k,    T^i=t^i+i b^i.
L_E,kin = -M² Khat_IJbar partial Z^I partial Zbar^Jbar.
```

The heterotic Kähler-volume potential and real-part convention are equations (4.12)–(4.13) of Anderson et al.; the dilaton factor is Kim (3.49).[3][2] This is not an assertion that Q has h11=1: restrict its **six-dimensional Kähler cone to a scaling ray**, `t^i=lambda t0^i`, with shape, complex structure, bundle coordinates and axions held fixed as a kinematic submanifold, not stabilized. Homogeneity gives `V=lambda³ V0` and the pullback `K_TTbar=3/(4 lambda²)`. Therefore

```
Lkin = -M²/(4s²) (partial s)² -3 M²/(4lambda²) (partial lambda)²
     = -1/2 (partial sigma)² -1/2 (partial rho)²,
sigma = M/sqrt(2) ln(s/s0),
rho   = sqrt(3/2) M ln(lambda/lambda0) = M/sqrt(6) ln(V/V0).
```

Complex derivatives have a factor 1/4 relative to the Hessian with respect to real parts; omitting it produces an incorrect canonical coupling. In dimensionless canonical coordinates `u=sigma/M`, `v=rho/M`,

```
s=s0 exp(sqrt(2) u),    V=V0 exp(sqrt(6) v),
Phi-Phi0=(sqrt(6) v-sqrt(2) u)/2,
f6=s0 exp(sqrt(2) u),
partial_(u,v) ln(g6²)=(-sqrt(2),0).
```

This replaces the predecessor's arbitrary b with **sqrt(2)** in its appropriate M normalization. In its `F=sqrt(2) M` scalar convention the exponent would be 2, not sqrt(2). The sign reverses if one defines the canonical dilaton with the opposite orientation; no physical ambiguity remains after fixing the displayed orientation.

Three distinct statements must not be conflated:

* Volume varied at fixed **s**: pure rho direction, zero tree gauge response; Phi co-varies.
* Volume varied at fixed **Phi**: `d ln s=d ln V`. Along this constrained line `d ell/M=sqrt(2/3) d ln V`, hence `d ln g6²/d(ell/M)=-sqrt(3/2)` for increasing volume. It is not a pure rho mode.
* A canonically unit direction `(cos theta,sin theta)` has tree fractional coupling `-sqrt(2) cos theta`. No theta or time evolution is selected by the metric. A future stabilized mass eigenvector could mix these and other moduli.

The tree gradient norm is sqrt(2), independent of s0 and of the index. This is a real universal leading-action constraint, not an E6/Tian–Yau or three-family signature. At loop level the canonical coordinates themselves need correction: Kim (3.56)–(3.58) show `K=Khat-ln(S+Sbar+6 V_GS)` and distinguish linear from chiral multiplets.[2] The function V_GS here is **not CY volume**. We retain it as missing data instead of claiming tree canonical coordinates hold at all orders.

## 3. Thresholds and the conditional photon bridge

For a fixed renormalization prescription, Kim gives at the retained one-loop level

```
g_a^-2(mu)=k_a s + [b_a ln(Mst²/mu²)+Delta_a+k_a Delta_univ]/(16 pi²),
b_a=sum_r T_a(r)-3 T_a(G).
```

The source also separates the holomorphic one-loop function from Kähler/matter-metric contributions via the Kaplunovsky–Louis relation, and supplies a charge-inserted worldsheet trace integral for Delta_a, (3.70)–(3.71).[2, equations (3.75)–(3.82)] Thus `Re f^hol` alone is not a physical low-energy inverse coupling. A vanishing standard-embedding Bianchi source does **not** set Delta_a, Delta_univ or their derivatives to zero. The net chiral index is not the entire charge-inserted massive string spectrum.

For a **conditional**, independently fixed index-one E6→SO(10)→SU(5) Standard Model embedding with standard Y and no unaccounted light U(1) mixing, the predecessor's trace calculation gives `kY=5/3`, `k2=1`. Its matching then becomes

```
H=e_atom^-2 = C s + D(s,V,z,...),  C=8/3,  alpha_atom=1/(4 pi H),
A_u=partial_u ln alpha_atom=-(C sqrt(2) s + D_u)/H,
A_v=partial_v ln alpha_atom=-D_v/H.
```

D includes string thresholds, universal corrections, all broken-spectrum running/matching, electroweak/QED decoupling and conversion to the same low-energy alpha convention as the atomic calculation. D_u and D_v are **total derivatives** at fixed declared physical endpoints, including implicit dependence through masses and couplings. At fixed M in Einstein units `Mst` also depends on s: Kim (3.78) gives `M²=Mst² s` in his convention, so `partial_u ln Mst=-1/sqrt(2)`; omitting this while calling the upper endpoint the string scale is wrong.[2] Equivalently choose a fixed Einstein renormalization endpoint and absorb the moving string-scale matching into D, with no double counting.

For a physical heavy threshold h, `partial_I R_a=(bL-bH) partial_I ln m_h/(8 pi²)` at fixed endpoints; arbitrary matching-scale derivatives cancel between running and finite matching. This is the previously executed `clock-matching-gate` result, not a newly computed spectrum for Q. The earlier unbroken/vectorlike E7 RG fixed-point spectra are **not** inherited by this chiral E6 compactification.

No complete Wilson-line/Higgs vacuum, realistic photon, mirror-removal masses, SUSY-breaking scale or threshold functional has been derived for the actual identity-Wilson-line candidate. Accordingly the conditional H equation is the gate toward clocks, not a claim that this candidate already predicts laboratory atoms.

## 4. Two sourced clock ratios and their full local response map

Use the numerator orders **Al+/Hg+** and **Hg+/Cs**, at fixed specified transitions/isotopes. Lorini's definitions give optical `nu_i=Rinf c C_i F_i(alpha)` and hyperfine `nu_Cs=Rinf c C_Cs alpha² (me/mp) g_Cs F_Cs(alpha)` up to declared corrections.[5, equations (7)–(8)] Define `m=delta ln(me/mp)`, `n=delta ln g_Cs`. His rounded `KAl≈0`, `KHg≈-3.2`, `KCs≈0.8` give

```
y1=delta ln(nu_Al/nu_Hg) = (16/5) a + epsilon1,
y2=delta ln(nu_Hg/nu_Cs) = -6 a -m-n + epsilon2,
a=A_u delta u + A_v delta v + sum_shape A_A delta w^A.
```

As the existing clock lane established, his printed coefficient after equation (12) reverses the Al/Hg subtraction: we preserve this source inconsistency, use the defining derivatives, and reject the wrong sign in the controls.[5] Rounded atomic numbers are exact rationals only in this algebraic test, not new high-precision atomic computations.

For the two-modulus slice, let `B_I=partial_I ln(me/mp)`, `N_I=partial_I ln g_Cs`. Do not set them to zero on the grounds of universal tree gauge coupling. The symbolic map is

```
[ y1 ]   [ (16/5) A_u          (16/5) A_v       ] [delta u]   [epsilon1]
[ y2 ] = [ -6 A_u-B_u-N_u     -6 A_v-B_v-N_v    ] [delta v] + [epsilon2].
```

For nuclear modeling one may expand `N_I=sum_q kappa_Cs,q partial_I ln(mq/LambdaQCD)+...`; kappa and the quark/QCD responses are missing nuclear/particle inputs, not topology. Matter metrics and physical Yukawa normalization are genuine moduli-dependent quantities in the sourced compactification.[4] The leading optical row suppresses recoil/finite-size and other effects only as an approximation; restoring them adds more nuisance columns.

The determinant is `(16/5)[A_v(B_u+N_u)-A_u(B_v+N_v)]`. Two known noncollinear response directions could locally identify both canonical excursions; determinant zero cannot. Without those independent response functions, the more honest nuisance-augmented map on `(delta u,delta v,m,n)` has rows `(16 A_u/5,16 A_v/5,0,0)` and `(-6 A_u,-6 A_v,-1,-1)`. Its generic rank is two, with kernel generators

```
(A_v,-A_u,0,0),       (0,0,1,-1).
```

Hence the clean optical ratio can identify **a**, but not distinguish the gauge-blind modulus direction, mass from nuclear response, the absolute coupling intercept, or an unknown scalar history. In the tree photon idealization `D=0`, `A=(-sqrt(2),0)`: clocks see delta u and m+n, not delta v. The exact/SVD checks below reuse the existing nullspace implementation and independently certify these conclusions symbolically. If an unconstrained optical systematic is admitted, even a is not identifiable. A tree directional response does not predict a drift: replacing excursions by time derivatives leaves actual velocities entirely unspecified.

## 5. Explicit fixed-topology counterfamily, and what remains fixed

Choose any smooth Ricci-flat representative J0 on the actual quotient, sufficiently large in string units, and a constant sufficiently weak Phi0. For parameters lambda>0 and real delta near 1 and 0 respectively, define the **family of constant backgrounds**

```
J_(lambda,delta)=lambda J0,
Phi_(lambda,delta)=Phi0+delta,
V_(lambda,delta)=lambda³ V0,
A_visible=spin connection of J_(lambda,delta),
s_(lambda,delta)=s0 lambda³ exp(-2 delta).
```

The complex manifold, free Z3 quotient, tangent-bundle descent and integral Chern classes are unchanged. Constant metric rescaling leaves the connection unchanged; Ricci flatness and HYM zero contraction survive, and F=R keeps the Bianchi cancellation. Index `-1/2 integral c3=3`, h11 and h21 remain fixed. This extends the predecessor's actual geometric scaling argument, not an invented c3 assignment. Remain in a small open neighborhood of an initially controlled weak-coupling/large-radius point; no uncontrolled limit is required.

At delta=0 and any lambda≠1, s changes. At lambda=1 and delta≠0, s also changes. Thus the integer index does not fix s0 or the absolute `df6/du=sqrt(2) s`. Conversely choosing `delta=(3/2) ln lambda` leaves s fixed while V and Phi change: even an independently determined **tree** gauge coupling does not identify both moduli. These are parameterized static solutions at the declared leading order, **not arbitrary functions lambda(t), delta(t)** claimed to solve the dynamical equations.

Nuance: all backgrounds in this family retain `partial_u ln g6²=-sqrt(2)` and `partial_v ln g6²=0` in their local tree canonical frames. It would be false to claim that every response coefficient is free. Those values come from the universal action and chosen direction, not the chiral index; threshold-corrected low-energy A, nuclear/mass responses and the mass-eigenstate direction remain uncomputed. Nothing here is a no-go for a specified stabilized heterotic vacuum or controlled corrections selecting a coupling.

## 6. Executed mathematical scope and missing physical inputs

`calculate.py` differentiates the two canonical maps and their induced kinetic metric exactly with SymPy, computes both symbolic response matrices and kernels, and compares the tree-slice kernel dimension with the **read-only reused** `shifted-vacuum-gate/calculation.py:null` SVD function. It emits SMT-LIB cases, executes them with the existing Z3 environment, and compiles the local kernel-only Lean module. `--verify` requires existing certificate bytes and compares the complete deterministic payload without regenerating it first. Negative controls reject wrong Weyl/canonical powers, a wrong clock subtraction sign, and corrupted/missing receipts. All solver witnesses are algebraic controls, not invented experimental data.

`Formalization.lean` proves that recovering only a projection from data identifies that projection despite arbitrary latent coordinates; separately, two distinct states in an observation fiber obstruct **any** full left inverse. A concrete two-state constant observation supplies a nonvacuous obstruction witness. This advances the prior full-inverse composition statement by treating partial identifiability. Lean does not formalize real calculus, CY geometry, atomic structure or threshold QFT. Real-arithmetic claims are separate SMT/exact checks. No Init/Mathlib, hosted CI or independent peer review is claimed.

A numerical prediction still requires: a sourced viable E6 breaking and full charged spectrum; mirror lifting and physical mass/Yukawa functions; string and field-theory thresholds plus scheme/conversion; corrected moduli metric; a derived stabilization potential, actual vacuum and mass eigenvectors; cosmological/environmental solution and initial conditions for any time signal; atomic/nuclear response functions and controlled experimental nuisances. No missing item is filled with an alpha fit, arbitrary masses or scalar evolution.

## 7. Standing cross-domain arrows

| Arrow | Classification here |
|---|---|
| Actual tangent-bundle Dirac index → net chirality | Model-dependent geometric theorem, inherited and retained. |
| Heterotic action → canonical dilaton response | Sourced leading-action derivation, new in this lane. |
| Canonical response → two clock ratios | Conditional matching plus sourced atomic Jacobian, not a photon vacuum proof. |
| Charge-inserted worldsheet trace → threshold | Sourced physical formula, not evaluated for this CY.[2] |
| Kauffman/HOMFLY knot chirality → this Dirac index | Unsupported without a specified map; not supplied here. |
| Ramanujan numbers/congruences, nimbers, prime/partition arithmetic → s or stabilization | Unsupported, distinct mathematical objects; no numerical substitutions. |
| Dedekind eta/partition state counts → threshold integer | Only after full relevant CFT/charge insertions; Dedekind numbers are not the eta function. |
| Cs mass number 133 = dim E7 → four dimensions/alpha | Numerical coincidence without an action map; HyperPhysics explains transitions, not compactification selection.[1] |

Only this lane was written. Sources retain exact HTTP bytes (without TLS authenticity), PDF bytes, text, URL/hash provenance and source excerpts; the fresh HyperPhysics HTML hash agrees with the predecessor capture. HTTP succeeded; HTTPS extraction failed. Native execution required correcting the known Cygwin shadow-file mapping. See `certificate.json` for actual test results rather than counting planned checks.

## Sources

[1] http://hyperphysics.phy-astr.gsu.edu/hbase/acloc.html — HyperPhysics Atomic Clocks
[2] https://arxiv.org/pdf/2305.08263 — Kim: On one-loop corrected dilaton action, retained v4
[3] https://arxiv.org/pdf/0905.1748 — Anderson et al: Stability Walls in Heterotic Theories
[4] https://arxiv.org/pdf/2401.15078 — Butbaia et al: Physical Yukawa Couplings
[5] https://tf.nist.gov/general/pdf/2295.pdf — Lorini: Recent atomic clock comparisons
