# Geometric-neutral cubic F equations on the Tian–Yau Higgs branch

## Outcome

**The missing geometric-neutral equations do not obstruct the verified branch at massless perturbative cubic order.** The nine complex-structure couplings are computed from an actual relative tangent-monad family: the geometric deformation operator kills all nine invariant charged representatives, before Serre pairing. The first required slices on `(c0,c1; beta0,beta1)` are therefore zero for every geometric direction. Holomorphy and the ungauged perturbative axion shifts exclude independent dilaton and complexified-Kahler `X L B` superpotential terms. This is not a claim that every gauge-neutral mode has zero coupling: the four established bundle-neutral tensors remain nonzero.

Combining this result with the predecessor's sixteen bundle-neutral equations closes the **all-neutral massless cubic F gate** on the explicit branch, in the classical geometric/perturbative Wilsonian regime specified below. It does not establish the full superpotential, moduli stabilization, a stable compactification vacuum, an exact string background, or an E7 construction.

## 1. Model and inventory without double counting

The retained geometry is the smooth Fermat/bilinear `(3,0),(1,1),(0,3)` complete intersection in `P3_x x P3_y`, with free diagonal Z3 quotient Q and `V=TQ`, plus the already selected flat E6 Wilson line. The standard embedding and the actual Tian–Yau family are described by Butbaia et al.; the local geometry has an enhanced (2,2) worldsheet description before the commuting Wilson projection.[2][1]

The following are **parent-gauge singlet chiral multiplets near the standard-embedding origin**, not the additional SM-singlet components of charged multiplets after Higgsing:

| Sector | Complex count | Meaning and boundary |
|---|---:|---|
| `Z^mu` | 9 | Invariant complex-structure directions, `H1(TQ) = H^(2,1)(Q)` |
| `T^I` | 6 | Complexified Kahler classes; each includes one internal B-field axion |
| `S` | 1 | Four-dimensional dilaton plus the universal axion dual to spacetime B_(mu nu) |
| `s^a` | 16 | Inherited `H1(End_0 TQ)` infinitesimal bundle deformations: twelve polynomial and four actual degree-one survivors |
| **Total** | **32** | Infinitesimal chiral singlets in this retained approximation, not 32 unobstructed exact moduli |

The quotient Hodge numbers `(h11,h21)=(6,9)` are the geometry predecessor's sourced inputs and agree with the invariant chain spaces used here. The splitting of simultaneous geometric/bundle infinitesimal deformations is a nontrivial theorem at the standard embedding, not a general heterotic direct-product assumption: Chisamanga–McOrist–Picard–Svanes prove `H_Dbar^(0,1) = H11 + H21 + H1(End_0 V)` in the first-order supergravity approximation, equations (1.2), (3.19) and section 5.[1]

The six internal axions and universal axion are seven **real partners inside the listed seven chiral multiplets**, not seven further chiral multiplets. The volume is a combination of the six Kahler coordinates, not another modulus. The complex scale of Omega is a choice of frame of the Hodge line, not a tenth complex-structure modulus. The first two ambient divisor directions do not exhaust `h11=6`. The four nonambient Kahler directions must not be omitted merely because the monad has two Euler summands.

Although `H1(TQ)` also supplies the nine L flavors and `H1(T*Q)` supplies the six B flavors, those carry `(1,3,bar3)` and `(1,bar3,3)` respectively. They arise in a different gauge representation from metric/B deformations; they are not the neutral `Z,T` fields. In particular beta0 and beta1 are charged **left-handed conjugate-representation** chiral fields, not conjugate complex numbers and not identified with neutral axions by dimension. The distinction follows from the E8 branching and bundle-valued matter cohomology.[2] The inherited hidden bundle has no continuous bundle modes because it is trivial and `H1(O_Q)=0`; the flat finite Wilson choice supplies no continuous Wilson-line moduli for the same reason on the simply connected cover.

### Induced connection variation and the Atiyah constraint

A geometric complex-structure fluctuation Delta must be accompanied by an induced change of the tangent connection. The relevant equation is schematically

```
Dbar_A a = Delta contraction F,
a^sigma_tau = nabla_tau Delta^sigma + a0^sigma_tau.
```

For `F=R`, curvature symmetries show that the induced first term solves the equation for every complex-structure direction; `a0` is the separately closed bundle fluctuation. The source proves both the Atiyah-map triviality and the additional anomaly-extension splitting, including the `B+iJ` correction, in equations (3.2)–(3.19).[1] These are cohomological splittings, not claims that the curvature or local off-diagonal operators vanish. The spin connection is induced, not a second independent copy of sixteen bundle multiplets.

This is essential for the cubic question: holding the tangent holomorphic connection fixed while changing complex structure computes the wrong neutral direction. Conversely the nonzero `a0 L B` Yoneda products cannot be discarded using a (2,2) argument for **geometric** moduli.

## 2. Actual family differentiation, not a derivative of a stored zero

### Relative complex

Write `f=(f_x,b,f_y)` for the defining equations. The tangent complex is

```
A=O^2  --E-->  B=O(1,0)^4 + O(0,1)^4  --J--> C=O(3,0)+O(1,1)+O(0,3),
monad degrees -1,0,1;
E_(i,b)=z_i delta_(b,x/y block),  J_(r,i)=partial_i f_r.
```

It is a complex on Q because `J E = (d_(r,b) f_r)`. The predecessor's ambient Cech/Koszul total resolution includes the explicit curvature homotopy for that off-variety composition. We reuse its actual `total_cech.py` and `module_action.py`, with hashes checked, rather than replacing it by a dimension count.

For every actual charged normal representative `c_mu`, construct the exact polynomial family

```
f_r(t)=f_r(0)+t (c_mu)_r,
J(t)=partial f(t), E(t)=E(0),
J(t)E = (d_(r,b) f_r(t)).
```

The nine `c_mu` are read from the accepted Serre receipt, not hand-selected new flavors:

```
(x3^3,0,0), (x2*x3^2,0,0), (x2^2*x3,0,0),
(x2^3,0,0), (x1^3,0,0), (x0*x1*x3,0,0),
(x0*x1*x2,0,0), (0,0,y0*y1*y3), (0,0,y0*y1*y2).
```

The computed nine-dimensional terminal-C quotient is the invariant Kodaira–Spencer space. Therefore these polynomial families cover all infinitesimal invariant complex-structure directions, not merely two selected deformations. Smoothness and freeness hold in an open neighborhood of the retained regular point. The normal-polynomial description of standard-embedding tangent matter and its relation to complex structure are the source's Kodaira–Spencer construction.[2]

The total derivative is formed from the actual operators:

```
D(t)=D0+t D_mu,
D_mu = (derivative of Koszul multiplication by f)
       + (derivative of monad arrows J).
```

The Cech coboundary, E arrows and degree-dependent curvature homotopy have zero derivative in this relative ambient frame. The changing defining ideal is **not** held fixed. The code checks the symbolic deformed Euler identity, and `D0 D_mu + D_mu D0=0`, `D_mu^2=0` on nontrivial admissible probes.

### Charged-frame transport and obstruction map

All nine accepted charged cocycles are global terminal-C polynomial cochains, with Koszul degree zero. In the exact relative family they continue as the same ambient polynomials restricted to `Q_t`. Since there is no outgoing terminal-C arrow and no Koszul index for the contracting differential to remove,

```
D(t)c_i(t)=0,        c_i_dot=0 in this relative polynomial frame,
D_mu c_i = 0       for every mu=0,...,8 and i=0,...,8.
```

These are explicitly applied operators on saved chain data, not an assigned mass matrix or the derivative of a JSON zero. Their independence at the base point, inherited from the computed quotient, gives a local frame after shrinking to the constant-rank neighborhood. More generally the smooth standard-embedding family has fixed Hodge dimensions; the finite-group invariant ranks are locally constant. This latter geometric fact is not an additional numerical rank computation.

The induced first-order mass/obstruction operator is the cohomology class

```
H1(TQ) --[D_mu]--> H2(TQ),
U_(mu,i,j) = Serre(beta_j, [D_mu c_i]).
```

It is the derivative of the charged quadratic kinetic complex entering holomorphic Chern–Simons reduction; Serre pairing converts the obstruction to a scalar superpotential coefficient, in the same convention as the inherited neutral Yoneda tensor. The overlap construction and separation of holomorphic couplings from physical kinetic normalization are given in equation (2.2) and section 2 of the Yukawa source.[2] Here every image is the zero **chain**, hence every pairing vanishes independently of residue or metric normalization. The code also loads all six actual dual cocycles and applies their module pairing, producing the full `9 x 9 x 6` zero geometric tensor at this order.

For each of the nine Z directions the requested slice is

```
               beta0 beta1
       c0        0     0
       c1        0     0.
```

This is stronger than the cancellation of its two diagonal entries on the canonical VEV.

### Why this transport is legitimate

A Gauss–Manin-flat de Rham frame generally does **not** remain a frame of a fixed Hodge summand. We do not assume otherwise. The calculation uses a relative holomorphic cohomology frame of the actual tangent resolution; changing this frame to any other differentiable or holomorphic choice adds the usual connection and exact-representative transport terms. For a mass tensor `M`, `nabla_mu M = partial_mu M + connection*M`; the latter terms vanish at the massless point. Variation of Omega and of the dual representatives likewise multiplies the unperturbed zero mass map. Thus the vanishing of the induced obstruction is frame-independent, without declaring arbitrary fixed monomials to be Gauss–Manin parallel.

We explicitly test `c_i'(t)=c_i(t)+D(t)b`. Its derivative is `D_mu b`, not zero. The identity

```
D_mu c_i' + D0(c_i'_dot)=0
```

is checked for admissible **nonzero** degree-zero primitives and nonzero boundaries. A Koszul/Cech primitive has degree `-1+2-1=0`; it detects failure to transport a changed representative. Omitting the transport or omitting the derivative of the ideal produces nonzero residuals. This is the requested protection against differentiating a frozen zero or an inconsistent fixed-geometry quotient.

## 3. Kahler and dilaton holomorphy selection rules

Let `T^I=t^I+i b^I` in a local convention and `S=s+i a`. In the retained ungauged, fluxless perturbative sector, the internal B shifts and universal axion shift give

```
T^I -> T^I+i epsilon^I,  S -> S+i epsilon_S,
L,B,Z unchanged.
```

For a holomorphic Wilsonian superpotential invariant under a continuous shift, `0=delta W=i epsilon partial_M W` implies `partial_M W=0`. Consequently neither `T^I Tr(L_i B_j)` nor `S Tr(L_i B_j)` is generated in this sector. The source gives this heterotic nonrenormalization argument explicitly in section 1.1, including the separate string-coupling and alpha-prime expansions and the nonperturbative exponential exception.[3] The extension from its displayed overall T to each internal B harmonic mode follows directly: the worldsheet change is the topological integral of that closed B form, zero in the homologically trivial perturbative sector. A nontrivial worldsheet curve instead has the exponential B dependence and is excluded from this argument.

The visible parent is semisimple trinification. Its inherited moment-map/FI audit found no continuously shifting geometric singlet under the unbroken gauge generators, so we are not silently discarding a charged/Stueckelberg axion. S-dependent gauge kinetic functions and T-dependent thresholds are allowed and are not superpotential `S L B` couplings. Nonholomorphic `L B` terms in K, or a Giudice–Masiero-type mass after supersymmetry breaking, are not holomorphic cubic W at the supersymmetric massless origin.

This calculation uses the **geometric obstruction map plus holomorphy route**, not an invented table of worldsheet U(1) charges. Gauge invariance alone permits all these species. Geometry/PQ eliminate the geometric ones; bundle `s^a L B` terms are gauge-allowed and actually nonzero. No general statement that `(2,2)` forbids all singlet–matter–mirror interactions is made.

## 4. All-neutral cubic F and the branch

The branch is exactly

```
L0=e32, L1=e33; B0=e23, B1=e33;
all other charged VEVs zero; s^a=0; geometric fluctuations at zero.
```

The geometric backgrounds are the retained CY point and positive finite Kahler/dilaton values: 'fluctuations at zero' does not mean zero volume or zero inverse coupling.

For arbitrary matrices in the supported charged common-kernel flavors the geometric equations are

```
F_Zmu = sum U_(mu,i,j) Tr(L_i B_j)=0,
F_TI = F_S=0 in the perturbative holomorphic sector.
```

The known bundle equations retain precisely

```
T[12,5,1]=-1; T[13,6,1]=-1;
T[14,7,0]=-1; T[15,8,0]=-1,
```

with twelve inherited zero slabs. Their common charged kernel remains `span(c0,...,c4)`, so c0,c1 annihilate all sixteen independently of B. The calculation rereads and checks those four nonzero entries and the actual five-dimensional kernel. It does not regenerate the expensive predecessor Yoneda calculation; the accepted source/receipt manifests are checked before and after this new computation.

Pure neutral cubic gradients vanish at the fluctuation origin. Cubics involving one neutral and colored pairs vanish at the zero colored VEVs, regardless of the missing colored coefficients. The charged gradients are already zero for the common-row/common-column alignment by the predecessor's full polarized determinant analysis. Hence every neutral species in the inventory now clears the massless cubic F test. Linear changes of the neutral splitting can mix the geometrical F covectors with the known bundle F covectors, but cannot change their simultaneous zero.

This also extends to the predecessor's positive-metric adjusted B columns and to complex gauge transforms on the established F locus. The nonlinear-Dflat theorem can therefore use the **complete inventoried cubic F locus**, not merely the earlier bundle-only subset, subject to its unchanged regular analytic positive-K hypotheses. It still does not derive the actual nonlinear K or a full vacuum.

## 5. Precise scope and actual remaining obstructions

1. **Computed directly:** classical relative tangent-monad geometric `Z L B` coefficients at the retained smooth standard-embedding point, including the complete invariant complex-structure tangent space and all invariant charged/dual flavors.
2. **Perturbative protection:** the holomorphic PQ/nonrenormalization argument applies to the Wilsonian W in the fluxless weak-coupling/large-radius perturbative expansions, with ungauged shifts and regular holomorphic coordinates.[3] It does not calculate a corrected worldsheet CFT or prove an all-orders corrected cohomology count. The explicit moduli-decoupling theorem used for the inventory is first-order supergravity, as its authors stress.[1]
3. **Not an all-field-order claim:** higher interactions involving nonzero bundle fields, charged invariants of higher degree, mixed geometric/bundle deformations away from the standard-embedding section, and elimination of heavy fields require their own obstruction/Massey products. Cubic F closure alone does not prove a finite exact Higgsed bundle family. In particular a quartic `Z L L L` is a derivative of a charged Yukawa, not the cubic `Z L B` tested here.
4. **No extension to nonperturbative W:** `exp(-aS)`, `exp(-2pi q_I T^I)`, their moduli-dependent prefactors and matter insertions are outside the shift argument.[3] Nonzero W also changes supergravity equations to `D_A W=partial_A W+K_A W`; the present pure-cubic branch has W=0, but an added condensate changes that.
5. **Existing worldsheet work is preserved, not duplicated:** the completed worldsheet-instanton report constructs actual isolated rational curves and finds tangent-bundle Pfaffian zeros on the standard-embedding locus. A Pfaffian vanishing **at** that locus does not prove its transverse bundle/charged derivatives vanish. Matter insertions can soak zero modes. That predecessor does not compute the instanton-corrected Higgs/bundle derivative tensors, and this lane does not assign them zero. Even a geometric family of zeros does not settle transverse derivatives in the Higgs direction.
6. **Remaining physical gates:** higher/nonperturbative superpotential on the Higgs branch, actual exotic masses and Higgs-eaten spectrum, moduli stabilization, regularity of K, full scalar stability and threshold/observable matching. No genuine geometric-neutral **cubic** obstruction was found; these higher and nonperturbative gates remain genuine unresolved equations, not a discovered no-go.

## 6. Reproduction, controls and provenance

Run natively:

```
C:/Python313/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/tian-yau-geometric-neutral-coupling-gate/calculate.py
C:/Python313/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/tian-yau-geometric-neutral-coupling-gate/verify.py
```

The default calculation requires the saved certificate, checks the full deterministic payload and predecessor/source hashes, and does not recreate a missing receipt. `--create` is exclusive creation only. The verifier pins the release manifest, checks saved receipts before computation, replays the calculation, checks unchanged bytes and tests missing/tampered payload rejection in this lane only.

Executed exact controls: 81 derivative-nilpotence probes; 26 nonzero representative transports; 7 detections each when omitting the changing-ideal derivative or the representative transport. The accepted four nonzero bundle tensors are retained as a physical negative control against universal-singlet vanishing. These counts are test counts, not new physical modes.

Sources and their verbatim-evidence ledger are retained under `sources/`. The code imports actual predecessor chain operators read-only. It temporarily changes differential tables in memory to form the derivative, always restoring them; no predecessor file is edited. Initial successful computation and receipt are preserved under `development/` before strengthening the representative-transport control. They are provenance, not the final replay authority. The Windows filesystem tool writes initially landed in the known Cygwin shadow tree; delivery was repaired to the canonical native lane before execution. No nested delegation or publication occurred. Verification is exact Python/SymPy plus a source-backed written derivation, not Lean-kernel or peer-review certification.

## Sources

[1] https://arxiv.org/html/2409.04350v2 — The decoupling of moduli about the standard embedding
    > "However, in the case of the standard embedding, the extension map ℱ\mathcal{F} is trivial and the long exact sequence splits. To see this, note that the curvature FF is in this case given by the Riemann curvature RR of the Calabi-Yau. Equation ([3.2](#S3.E2 "In 3 The standard embedding")) then takes the form"
[2] https://arxiv.org/html/2401.15078v2 — Physical Yukawa Couplings in Heterotic String Compactifications
    > "These are the unnormalized Yukawa couplings:"
[3] https://arxiv.org/pdf/hep-th/0510213 — Nonrenormalization of Flux Superpotentials in String Theory
    > "We conclude from this that the PQ symmetry precludes W from developing a dependence on S, and so ensures that W receives no corrections in string perturbation theory."
