# A sourced three-net-family SU(3)/E6 heterotic candidate

## Result and relationship to the E7 gate

There is a concrete positive alternative: the standard embedding on the **Tian–Yau free Z3 quotient**, with tangent bundle structure group SU(3), gives a four-dimensional N=1 visible E6 theory with **nine 27 and six conjugate 27 multiplets: net three**. The geometry and symmetry are specified below. The integer is computed from the actual Chern polynomial, not assigned as hypothetical `c3=6`.

This changes the model. The predecessor `heterotic-e7-candidate-gate` establishes that an honest rank-two SU(2) bundle on a smooth CY3 has c3=0; its E8 commutant is E7 and its index vanishes. The present rank-three tangent bundle has c3=-6 downstairs; its commutant is E6, **not E7**. The complete E7 56 still branches to 27 plus conjugate 27 and two singlets. No assertion that three chiral E6 families came from three full E7 56s is made.

The successful gate is an established supersymmetric compactification with net-three chirality before further gauge breaking. It is not exactly three massless 27s without mirrors, a Standard Model spectrum, moduli stabilization, or an alpha prediction.

## 1. Explicit geometry and action

Let X be the complete intersection in P3_x × P3_y of bidegrees `(3,0),(1,1),(0,3)`:

```
f(x)=x0^3+x1^3+x2^3+x3^3=0,
b(x,y)=x0 y0+x1 y1+x2 y2+x3 y3=0,
g(y)=y0^3+y1^3+y2^3+y3^3=0.
```

These are precisely the member used in Butbaia et al. [1], section 4.3, equations (4.7)–(4.9), apart from irrelevant factors 1/3 multiplying the cubics. Take ω=exp(2πi/3), and the generator

```
a:x -> (x0, ω²x1, ωx2, ωx3),
  y -> (y0, ωy1, ω²y2, ω²y3).
```

Let `Q=X/<a>`. The three polynomials are invariant, and the residue holomorphic three-form is invariant: the numerator coordinate determinant has exponent `0+2+1+1+0+1+2+2=12=0 mod3`, with invariant denominators. Thus this is not a quotient that secretly twists the canonical bundle. The generator and its square act freely.

### Independent freeness check at this actual member

A fixed projective point of either nonidentity group element belongs to an eigenspace. In each P3, the singleton eigenspaces e0 and e1 cannot meet its Fermat cubic. The only remaining eigenspace is the line spanned by coordinates 2,3. On its intersection with the cubic both coordinates are nonzero. Write `r=x2/x3`, `s=y2/y3`. Fixed points of X would require

`r³=s³=-1`, and `rs+1=0`.

But the first two give `(rs)³=1`, while the third gives `(rs)³=-1`. No complex solution exists. The certificate checks the phase table and this exact contradiction. It does not confuse an ambient fixed line with a fixed line on X.

### Independent smoothness argument

Each Fermat cubic surface Sx,Sy is smooth, since all partial derivatives vanish only at the excluded zero vector. X is the bilinear divisor in their product. A singular point of this divisor would require the bilinear differential to lie in the span of the two cubic differentials. Absorbing factors of 3 into constants gives

`yi=A xi²`, `xi=B yi²`, for every i.

Neither A nor B can vanish, because x and y are projective points. Their supports therefore coincide. For every nonzero xi, `xi³=1/(BA²)=C≠0`. If m is the nonempty support size, f=0 requires `m C=0` with `1≤m≤4`, impossible over C. The exact support-cardinality check is arithmetic supporting this written geometric argument, not a Lean formalization of Jacobian geometry.

Adjunction gives trivial canonical bundle. X is the smooth ample (1,1) divisor in the product of two simply connected cubic del Pezzo surfaces; weak Lefschetz gives simple connectivity and H² inherited from this product. The CY3 has SU(3) restricted holonomy, rather than the reduced SU(2) holonomy of K3×T2. Q is smooth compact Kähler, with π1(Q)=Z3 and invariant nowhere-zero holomorphic volume form. Its spin structure compatible with this Calabi–Yau structure exists; H¹(Q,Z2)=0 makes the spin structure unique. These geometric/topological theorems are external mathematics, not implemented in Lean.

Candelas–de la Ossa–He–Szendrői [2], section 2.1, also construct the same Tian–Yau deformation family using a cyclic coordinate action, explicitly prove generic freeness, and obtain `(h11,h21)=(6,9)`. Their coordinate generator has a different displayed form; the candidate here uses [1]'s explicit diagonal generator rather than mixing these coordinate conventions.

## 2. Model tuple, bundle descent, Bianchi and HYM

Choose the ten-dimensional E8×E8 heterotic theory with the conventional standard-embedding action and trace normalization, on

`M10=Minkowski4 × Q`, with visible bundle `V=TQ`, hidden principal E8 bundle trivial, no five-brane class, H=0 and constant dilaton at the standard-embedding/large-radius supersymmetric level.

This parent dimension and six-real-dimensional internal geometry are **model inputs**. Four dimensions follow from that geometric ansatz, not from a subtraction involving 133.

For the étale map π:X→Q, its derivative gives a canonical isomorphism `TX ≅ π* TQ`. The derivative action on TX satisfies the cocycle law, so the bundle genuinely descends. Invariance of the holomorphic volume form reduces the determinant to the trivial bundle and permits the SU(3) structure. This is not an arbitrary stable bundle whose descent has merely been assumed.

The standard embedding sets the visible gauge connection equal to the SU(3) spin connection. At the level of integral characteristic classes, directly **on Q**,

`c2(TQ)-c2(V)-c2(Vhidden)=[W]=0`.

Because V is the actual tangent bundle downstairs, this equality includes any torsion information; it is stronger than checking equality after pullback, which might lose torsion. No arbitrary assignment of visible Chern numbers, hidden flux, or an invented compensating five-brane is used. With the standard embedding normalization, `Tr F∧F=Tr R∧R`, so the local Bianchi source also vanishes at the stated order, not merely its integral.

Yau's Ricci-flat Kähler metric theorem supplies a Ricci-flat representative in each Kähler class. Its tangent Chern connection has curvature type (1,1) and zero contraction with the Kähler form, hence solves HYM. Equivalently the irreducible SU(3) holonomy connection yields the stable tangent-bundle/HYM standard embedding. One can average an upstairs Kähler class over the finite group; uniqueness then makes its Ricci-flat representative invariant and it descends. [1], sections 1–2, explicitly discuss V=TX, the HYM connection and N=1 supersymmetry. We do not numerically construct the metric or claim an all-orders corrected ten-dimensional background; these analytic/string-theoretic inputs remain external. The generic standard embedding is a sourced supersymmetric compactification family, not a metastable isolated vacuum.

## 3. Chern polynomial, index and representation branching

In the ambient intersection ring `Z[h,k]/(h^4,k^4)`, with h,k the two hyperplane classes,

```
c(TX)=(1+h)^4(1+k)^4/[(1+3h)(1+h+k)(1+3k)],
[X]=(3h)(h+k)(3k),
c1=0,
c2=3h²+hk+3k²,
c3=-8h³-h²k-hk²-8k³.
```

The exact coefficient of h³k³ in `c3 [X]` is **-18**. Only the two mixed c3 terms contribute. For the degree-three étale cover,

`∫Q c3(TQ)=-18/3=-6`, and `χ(Q,TQ)=(1/2)∫Q c3=-3`.

Our convention is `n27=h¹(Q,TQ)` and `n27bar=h¹(Q,T*Q)=h²(Q,TQ)`. Since h⁰ and h³ of TQ vanish, **net27=−χ(Q,TQ)=+3**. This minus sign matters: the holomorphic Euler index is not +3 in this orientation and convention. Reversing representation labels/orientation reverses the signed count, not its magnitude.

The gauge branching is

`248=(78,1)+(1,8)+(27,3)+(27bar,3bar)` under E6×SU(3),

with the common-center quotient understood for the subgroup inside E8. It has been checked beyond dimension addition. The certificate enumerates all 240 E8 roots in doubled Euclidean coordinates, picks the A2 simple roots e0−e1 and e1−e2, and resolves every root by its A2 coroot pairings. The perpendicular root subsystem has 72 roots (E6); the A2 subsystem has six roots. The remaining roots have the three fundamental A2 weights and their negatives, each with multiplicity 27. Orthogonal projection gives one 27-element E6 weight set for all three fundamental A2 weights, and its distinct negative set for the conjugate sector. Every E6 root reflection preserves the set and the reflection orbit has size 27. Adding the six and two Cartan generators gives 78 and 8. Thus the result is a full root/weight check, not recognition of `78+8+81+81` alone.

For a local anomaly cross-check the full cubic Cartan trace tensor `sum_w w_i w_j w_k` of this 27 vanishes exactly. Adjoint-invariant polynomial restriction to a Cartan then gives the absence of a perturbative E6 gauge cubic anomaly; the 27's cubic **field** invariant is a different object and is not a gauge anomaly. Mixed gauge-gravity traces vanish for the simple group. This is not a global string anomaly proof for arbitrary added Wilson lines or new matter. The undeformed standard embedding's broader consistency is the sourced heterotic construction, not the finite trace check alone.

## 4. Quotient cohomology is not division of each upstairs multiplicity

For X, `(h11,h21)=(14,23)`. For Q, they are `(6,9)` [1,2]. Thus:

| Space | n27 | n27bar | net27 | χ(T) |
|---|---:|---:|---:|---:|
| X (cover) | 23 | 14 | 9 | -9 |
| Q=X/Z3 | 9 | 6 | 3 | -3 |

Neither 23/3=9 nor 14/3=6. What divides by the cover degree is the **index**, not every cohomology dimension. Downstairs cohomology is the invariant subspace `H^i(Q,TQ)=H^i(X,TX)^Z3`.

There is also an independent geometric reconstruction of h11(Q). A cubic del Pezzo surface has b2=7. The displayed action on each such surface fixes three isolated points on P1_23. Topological Lefschetz gives trace on H² equal to `3−1−1=1`. Weak Lefschetz for X inside Sx×Sy gives dimension 14 and trace 2 for each nonidentity element. Averaging yields `(14+2+2)/3=6` invariant (1,1)-classes. Euler -6 then gives h21=9. The certificate checks this arithmetic; the cubic-surface topology and Lefschetz theorems are external.

The free action and holomorphic Lefschetz give virtual tangent index character `χ_Z3(TX)=-3 Reg_Z3`. H²(X,TX) identifies via Ω with H²,²(X), whose real structure forces equal nontrivial Z3 character multiplicities. Dimension 14 and invariant dimension 6 give `[6,4,4]`. Subtracting the virtual index then gives H¹(X,TX) multiplicities `[9,7,7]`. These isotypic dimensions are a conditional deduction from sourced Hodge data and Lefschetz, not a separately computed cochain complex. In particular H²,¹ itself need not carry a real action; the reality argument is used for H²,² and then the virtual index transfers the result.

### Wilson lines and mirror pairs

The declared candidate uses the **identity Wilson line**, so E6 remains unbroken. A nontrivial `ρ:π1(Q)=Z3→E6` is extra model data. The spectrum in a remaining gauge representation R would be computed from `(H¹(X,TX)⊗27)^Z3` after inserting ρ and decomposing under its centralizer; conjugate matter uses the dual bundle and conjugate representation. A component of 27 with Z3 phase 1 picks the invariant cohomology multiplicity 9; a component with either nontrivial phase picks 7. Its conjugate partners correspondingly pick 6 or 4, hence net three per corresponding branching component. This formula does **not** choose a Wilson-line embedding, identify a Standard Model gauge group, or provide Yukawa/mass matrices.

The six vectorlike 27+27bar pairs do not disappear because an index was computed. Lifting them requires an allowed full-rank mass mechanism at an appropriate vacuum. Prior E6-breaking lanes cannot simply import a one-27 EFT or a proposed Higgs alignment as if this compactification had generated that action or stabilized its VEVs.

## 5. Partition/prime conjecture: a real divisibility test, not a premise

For a free degree-d quotient with a genuinely descended bundle, the index relation is `I_X=d I_Q`. Thus **d divides the cover index**. In this model `d=3` and `I_X=-9`, producing `I_Q=-3`. This is a genuine discrete constraint on chirality. It is not a proof of freeness, bundle equivariance, HYM, or a selection law choosing the smallest positive index. Topological Euler divisibility alone is weaker: d must divide χ_top, but descent of this SU bundle on a CY3 also forces integrality of χ_top/(2d).

Executed controls include:

* A hypothetical degree-two CY-preserving tangent descent of this cover would give index -9/2, not an integer. Its Euler quotient would be the integer -9, demonstrating why Euler divisibility alone is insufficient. This rules out that stated free CY tangent-descending scenario, not every involution with fixed points or nontrivial canonical character.
* Prime order is **not sufficient** for three families: the bicubic in P2×P2 has Euler -162 and a free Z3 quotient with Euler -54, hence net 27 in its standard embedding [2, section 2.2]. Same prime, different family count.
* Prime order is **not necessary even for net three**: Braun–Candelas–Davies [3] explicitly construct a cover with Euler -72 and freely acting Z12 and Dic3 groups of order 12. The quotients have `(h11,h21)=(1,4)` and Euler -6, with three net E6 generations. Exact control `72/(2·12)=3` reproduces their count. This stronger primary-source counterexample excludes a universal prime-order requirement, without claiming our code reconstructs their different geometry.
* The quintic free Z5×Z5 quotient has Hodge numbers (1,5), Euler -8 and net four [1,2]. Composite group order 25 is allowed.
* The resolved quotients involving B,C in [2] have fixed elliptic curves before resolution. They are **not** examples to which we blindly apply the étale index formula: fixed-locus and resolution terms must be assessed. Equality of Euler ratios in that special example is not a general rule for nonfree actions.
* A c3=6 assignment to rank two remains invalid. Dropping the conjugate mixed-root sector fails the E8 branching check. Taking the covering index as the quotient family number also fails.

What is quantized: integral characteristic classes; integral Dirac indices; finite group order and discrete equivariant/Wilson-line data. What remains continuous: Kähler classes, complex structure deformations, dilaton, bundle deformation choices and therefore physical masses, thresholds, couplings and metric volume. Scaling a Kähler form by a positive real λ preserves Chern numbers, the index and the HYM zero-slope condition while varying volume as λ³. The leading four-dimensional inverse gauge coupling depends on volume and dilaton. The integer three does not fix this continuous parameter.

The partitions predecessor correctly connects ordinary partition coefficients to eta-function oscillator counting and complete lattice characters. The modular-completion predecessor completes E7×A1 to E8 and distinguishes current counts from physical zero modes. Here the new physically meaningful bridge is **the actual internal tangent-bundle Dirac index**. No map from p(n), Ramanujan congruences, Dedekind numbers or primality to this geometry/action is supplied by that completion. Changing to the E6×A2 embedding is compatible with an E8 gauge factor, but we do not claim a newly computed full CY worldsheet partition function.

## 6. Cross-domain scope retained without substituting homonyms

| Proposed connection | Status at this gate |
|---|---|
| Dirac index → net E6 chirality | Concrete model-dependent bridge evaluated above. Not the Dirac large-number hypothesis or monopole charge alone. |
| Partition/eta characters → gauge/current state counting | Established predecessor block; no specified functor selecting Q or its moduli. |
| Ramanujan numbers/congruences and nimbers | Distinct retained questions. No nimber/partition identity is inserted as Chern data or a prime scale. |
| Dedekind eta/sums versus Dedekind numbers | Distinct objects; neither the shared name nor modular multipliers select this quotient. |
| Kauffman / HOMFLY / knot mirror chirality → Weyl chirality | Knots predecessor supplies genuine CS/index routes but no map to this tangent-bundle index. Kauffman is not replaced with Kaufman; a determinant-sign partition is not a γ5 grading. |
| HyperPhysics `acloc` / atomic clocks | Remains an observable/matching task, not solved by this geometry. A clock ratio response needs a scalar-dependent kinetic function, running/threshold matching and scalar history; static integer topology fixes none of these. No atomic-clock source is silently relabeled an index theorem. |
| 133 → four dimensions or absolute alpha | Unsupported by this candidate; no fit attempted. |

These are boundaries for the standing user scope, not a claim that a full new literature search was conducted in every adjacent topic. Existing connections/partitions, connections/dirac, connections/knots, modular-completion and heterotic-e7 reports/code were treated as predecessor constraints and not modified.

## 7. Formal proof, executable evidence and remaining gates

`Formalization.lean` constructs Peano naturals and proves **for all natural a,b** that triple(a)=triple(b) implies a=b by induction and constructor cancellation. It then proves the two-input conditional theorem: if triple(q)=cover and cover=nine, then q=three. A second theorem shows that a degree-three descent of a zero cover index remains zero, and a nonzero three-family witness exercises the first theorem. The formal indices are **magnitudes**; the orientation/sign convention is in the report and signed exact certificate. The Lean declarations have no project axioms and no sorry/admit/unsafe escape. They do not prove index multiplicativity, HRR, bundle descent, or CY geometry. Thus Lean contributes genuine universally quantified cancellation, not a theorem that merely assumes q=three.

The minimal reused Lean 4.32.1 installation is kernel-capable but lacks Init/Mathlib. `Challenge.lean` exposes the public theorem types. The exact certificate uses only the Python standard library; source retrieval used pymupdf, but replay does not. `source_evidence.json` retains supporting source ranges, URLs and hashes. `verify.py` checks source hashes/excerpts, compiles Lean with exit status zero, checks every printed axiom report, replays the saved certificate and compares the saved verification receipt. Missing receipts fail rather than being regenerated by `--verify`.

```
python -B exact_certificate.py --verify
python -B verify.py --verify
```

Initial artifact creation uses the commands without `--verify`. All paths resolve relative to the actual script location. Native Windows execution was used after detecting that file tools' reported canonical paths initially wrote into a Cygwin shadow tree. The affected lane files were copied into the real `C:/Users/mikeb/e7-alpha-theory/gap-investigation/heterotic-e6-three-family-gate` and verified there. Lean is launched with a native subprocess working directory to avoid its source-root containment failure under the shell's shadow working directory. No other lane was modified. Local compilation can emit stylistic def-as-theorem warnings; these are not axioms or failures. Hosted CI was not run.

Open physical gates: choose/derive a Wilson-line or Higgs-breaking sector; determine the full charged and singlet spectrum after it; remove unwanted vectorlike matter with justified masses; establish the scalar potential and moduli stabilization; compute normalized Yukawas and thresholds at that vacuum; match to measured couplings and independent observables. The sourced positive existence result is useful precisely because it replaces invented c3 data with an actual compactification, without pretending those remaining tasks are complete.

## Primary sources and exact provenance

[1] G. Butbaia et al., *Physical Yukawa Couplings in Heterotic String Compactifications*, arXiv:2401.15078, https://arxiv.org/pdf/2401.15078 . Retrieved full PDF/text in `sources/yukawas.*`. Sections 1–2 give the standard embedding, SU3/E6 branching, H¹(TX) multiplicities and HYM discussion. Section 4.3, equations (4.7)–(4.9), gives the actual Fermat/bilinear geometry and diagonal free Z3 action; Table 2 gives nine quotient H¹ modes. This is primary research computing quantities on this specific geometry. Numerical Yukawa claims in the paper are not independently reproduced here. PDF extraction can lose overbars; our conjugate branching convention is fixed explicitly and checked via root weights.

[2] P. Candelas, X. de la Ossa, Y.-H. He and B. Szendrői, *Triadophilia: A Special Corner of the Landscape*, Adv. Theor. Math. Phys. 12 (2008) 429–473, arXiv:0706.3134, https://people.maths.ox.ac.uk/szendroi/atmp_triadophilia.pdf . Full PDF/text retained. Sections 1.1 and 2.1 give Euler/Hodge data and the explicit Tian–Yau family/free action; section 2.2 supplies prime-order bicubic controls; the paper also distinguishes free actions from fixed-torus resolutions. Their original-source reference is G. Tian and S.-T. Yau, *Three-dimensional algebraic manifolds with c1=0 and χ=-6*, Mathematical Aspects of String Theory (1987), pp.543–559. We retrieved [2]'s primary reconstruction, not the original Tian–Yau chapter, and do not claim to have inspected that chapter.

[3] V. Braun, P. Candelas and R. Davies, *A Three-Generation Calabi–Yau Manifold with Small Hodge Numbers*, Fortsch. Phys. 58 (2010) 467–502, arXiv:0910.5464, https://arxiv.org/pdf/0910.5464 . Full PDF/text retained. Abstract and introduction explicitly give Euler -72, free order-12 actions, quotient Hodge numbers (1,4), and standard-embedding E6 three-net-generation models. This is a direct primary composite-order counterexample, not an invented arithmetic cover. Its further Standard Model-breaking results are not claimed for the Tian–Yau candidate.
