# Tian–Yau Z3 Wilson line: exact trinification spectrum and the next interaction gate

## Physical outcome

A single Z3 Wilson line **cannot leave exactly the Standard Model gauge algebra** in this standard-embedding E6 model. A single element of compact connected E6 lies in a maximal torus; its centralizer contains that entire torus. The visible rank remains six, whereas su(3)+su(2)+u(1) has rank four. This obstruction applies to every single toral element, not only the representatives below. It is not an obstruction to subsequent Higgs/bundle deformation breaking.

There is a concrete, anomaly-free intermediate:

```
Gvis = (SU(3)C × SU(3)L × SU(3)R)/Z3_diag,
W = [(ω I3, I3, I3)],  ω³=1,
27 = Q + Qc + L
   = (3,bar3,1) + (bar3,1,3) + (1,3,bar3).

7 Q + 7 Qc + 9 L + 4 Qbar + 4 Qcbar + 6 Lbar.
```

Thus each bifundamental has net three, but **four colored pairs and six lepton/Higgs-type pairs remain**. The quotient is not three bare families. Two L/Lbar flavor pairs already present in this spectrum can be aligned so their full common stabilizer is exactly the SM algebra. This alignment is D-flat with canonical equal-norm conjugate pairs and F-flat for the charged-cubic truncation. It is **not yet a vacuum of the actual compactification superpotential**. An allowed neutral-bundle-modulus coupling can obstruct it even when that modulus is zero.

The next missing calculation is therefore precise: the equivariant cup-product tensors coupling the surviving neutral bundle moduli to L Lbar (and the other pairs), together with the charged Q Qc L and conjugate Yukawa tensors, evaluated on a common F/D-flat branch. One must then calculate post-Higgs exotic/mirror mass ranks, not infer them from the index.

## 1. Inputs and scope

The canonical predecessor `../heterotic-e6-three-family-gate/REPORT.md`, `exact_certificate.py`, saved certificate, source evidence and retained primary-source excerpts were read before construction. Its explicit Fermat/bilinear Tian–Yau cover X, free diagonal generator, quotient Q=X/Z3, SU(3) tangent standard embedding and orientation convention are retained unchanged. Upstairs tangent cohomology character multiplicities are `[9,7,7]`; dual-tangent H1 multiplicities are `[6,4,4]`. The latter is the Serre-dual character of H2(TX), so nontrivial characters are interchanged by duality; here their equal dimensions make the displayed arrays identical. Their geometric derivation remains conditional on the predecessor's sourced Hodge/Lefschetz inputs; this lane does not compute a new equivariant cochain complex.

Visible E6 is not E7. The parent remains ten-dimensional E8×E8 heterotic theory, with the sourced large-radius supersymmetric geometry and tangent bundle. The hidden E8 factor is not broken by this visible Wilson line; no hidden charged matter or new visible spectators are introduced. Neutral geometric, dilaton and bundle moduli have not all been enumerated here. Their omission from the charged-spectrum table does not set their superpotential couplings to zero.

Primary support:

* G. Butbaia et al., *Physical Yukawa Couplings in Heterotic String Compactifications*, [arXiv:2401.15078](https://arxiv.org/pdf/2401.15078), sections 1–2 and 4.3: the actual Tian–Yau member/action, standard embedding, cohomology and cubic Yukawa integrals. Its Table 2 supplies the nine invariant tangent modes, not the full new mixed-character Q Qc L tensor.
* V. Braun, P. Candelas and R. Davies, *A Three-Generation Calabi–Yau Manifold with Small Hodge Numbers*, [arXiv:0910.5464](https://arxiv.org/pdf/0910.5464), section 3.2: flat homomorphisms into E6, the SU(3)^3 branching, tensoring cohomology with Wilson representations, and the need for actual D-flat fields and superpotential masses. Its non-Abelian order-12 example is a **different geometry** and is not imported as a Tian–Yau SM solution. Its explicit statement that Abelian Wilson lines cannot lower rank supports the obstruction used here.
* Candelas–de la Ossa–He–Szendrői, *Triadophilia*, [arXiv:0706.3134](https://people.maths.ox.ac.uk/szendroi/atmp_triadophilia.pdf), section 2.1: Tian–Yau quotient topology. All three primary sources are retained and hashed in the predecessor; this certificate records those exact hashes rather than relying on search snippets.

The new finite classification, phase-resolved spectrum and matrix stabilizer below are independent exact calculations, not numerical results attributed to those papers. PDF overbars can disappear in extraction; the explicit weight convention fixes them.

## 2. Correct global group and complete finite enumeration

The subgroup inside E8 is `(E6_sc × SU(3))/Z3`, but the E6 factor maps **injectively** into it: `(g,1)` can be in the diagonal kernel only for g=1. The centralizer of the SU(3) holonomy therefore contains the simply-connected E6, not E6/Z3 acting on a nonexistent standalone 27. Its nontrivial center acts faithfully on 27. A Wilson-line homomorphism from Z3 must obey W³=1 in this group, not merely in the adjoint representation.

Normalize all roots to length squared two. The code reuses the predecessor's full E8 root construction in doubled Euclidean coordinates, takes the perpendicular E6 subsystem to e0−e1,e1−e2, and projects the E8 roots carrying A2 weight `(1,0)` to the 27 weights. It constructs a six-simple-root basis from a lexicographic positive system. In this basis the exact Cartan matrix is

```
 2  0  0  0  0 -1
 0  2 -1  0  0  0
 0 -1  2 -1  0  0
 0  0 -1  2 -1 -1
 0  0  0 -1  2  0
-1  0  0 -1  0  2
```

Its determinant is three. Cocharacters of E6_sc form the coroot lattice Q∨=Q, so every order-dividing-three toral element is

`W_t=exp(2πi Σ_i t_i α_i∨ /3)`, `t∈Q∨/3Q∨ ≅ (Z3)^6`.

All 729 points are enumerated, not a scan over a few convenient shifts. Simple Weyl reflections act on t by `t_i -> t_i − Σ_j A_ij t_j mod3`; breadth-first orbits classify them completely up to E6 conjugacy. This uses the standard maximal-torus conjugacy theorem externally. The 27 phase signatures of all 729 points are distinct. Roots survive exactly when `Σ_i t_i〈α,α_i∨〉=0 mod3`; all six Cartan generators survive independently.

| Representative t | Orbit size | Centralizer Lie algebra | Surviving roots |
|---|---:|---|---:|
| 000000 | 1 | e6 | 72 |
| 000001 | 72 | a5 + u1 | 30 |
| 000011 | 270 | d4 + u1² | 24 |
| 000102 | 240 | a2 + a2 + a2 | 18 |
| 010102 | 72 | a5 + u1 | 30 |
| 010120 | 72 | a5 + u1 | 30 |
| 121002 | 1 | e6, central phase ω | 72 |
| 212001 | 1 | e6, central phase ω² | 72 |

There are eight conjugacy classes of order dividing three, hence seven nonidentity/order-exactly-three classes. The three A5 classes have different matter phases despite identical Lie centralizers. The two nontrivial central elements are not the identity: they retain e6 but select 7×27+4×27bar rather than 9+6.

`certificate.json` includes every surviving root and subgroup simple root, the full 27 weight blocks, highest Dynkin weights, explicit commuting U1 cocharacter directions and charges, phase/conjugate phase and multiplicities for **every class**. This is representation-resolved data, not dimension-only guessing. The U1 directions specify a rational Lie-algebra basis of primitive individual coroot directions; no assertion that these jointly give every global torus quotient is needed. Apart from the explicitly determined trinification group, the table labels Lie algebras, not unverified global product groups.

An adjoint-only enumeration using `λ∨/3` for arbitrary fundamental coweights is invalid here: some such elements cube to a nontrivial E6 center, detected by fractional 27 pairings. The executable negative control exhibits these indices. They would be admissible order-three elements in E6_ad, not the required E6_sc.

### Flat characteristic-class diagnostic

A flat connection has zero real curvature but may still change integral torsion characteristic classes. We therefore do **not** blindly reuse the predecessor's integral Bianchi equality for every class. In the standard basic-class normalization for E8 (restriction index one to this E6), the restriction to BZ3 is, up to sign, `q(t) u²`, where `q(t)=tᵀAt/2 mod3` and `u∈H²(BZ3,Z)`. For the trinification representative q=0: this particular universal torsion contribution vanishes already before pullback to Q. The A5 representatives give q=1 and the D4 representative q=2, so accepting those as string backgrounds would require their pullback/global B-field data rather than just the local anomaly check. The zero result for trinification is a topological consistency diagnostic; we do not claim a new all-orders worldsheet or differential-cohomological global anomaly proof.

## 3. Explicit branching and phases

In the A2³ representative `t=(0,0,0,1,0,2)`, the sorted simple-root indices are grouped as `{0,3},{1,2},{4,5}`. Choose C simples `(4,5)`, L simples `(0,3)`, and R simples `(2,1)` (the R reversal fixes fundamental/conjugate orientation). The highest weights then give exactly

`Q=(3,bar3,1)_1`, `Qc=(bar3,1,3)_2`, `L=(1,3,bar3)_0`.

The subscripts are q with eigenvalue ω^q, **not hypercharge**. The global kernel of the three SU3 centers on these three bifundamentals is the diagonal Z3. Hence their faithful subgroup is `(SU3³)/Z3_diag`, and W is `[(ωI, I, I)]`. The full 27 weight phases, not just the adjoint, identify this element with the lattice representative. Its conjugates have phases −q.

All modes are four-dimensional left-handed chiral superfields. With geometric character a meaning g acts by ω^a, the invariant condition is `a+q=0 mod3`. Thus

`n(R_q)=h1_TX[−q]`, `n(conjugate R_−q)=h1_Tdual[q]`.

| Field | Gauge irrep | q | Geometric character | Multiplicity |
|---|---|---:|---:|---:|
| Q | (3,bar3,1) | 1 | 2 | 7 |
| Qc | (bar3,1,3) | 2 | 1 | 7 |
| L | (1,3,bar3) | 0 | 0 | 9 |
| Qbar | (bar3,3,1) | 2 | 1 | 4 |
| Qcbar | (3,1,bar3) | 1 | 2 | 4 |
| Lbar | (1,bar3,3) | 0 | 0 | 6 |

Discarding the nontrivial cohomology characters would wrongly delete all colored matter. Dividing each upstairs multiplicity by three is also wrong. The constant characterwise difference three makes every corresponding branch have net three, but does not delete a single mirror multiplet.

## 4. Anomalies and gauge-allowed interactions

In fundamental cubic-anomaly normalization A(3)=+1, A(bar3)=−1, including the other-factor dimensions,

```
A_C = 3[(7−4)−(7−4)] = 0,
A_L = 3[−(7−4)+(9−6)] = 0,
A_R = 3[(7−4)−(9−6)] = 0.
```

There are no mixed linear traces for these semisimple factors. More strongly, for every classified Wilson line the code sums the entire linear and cubic Cartan trace tensors of all surviving weighted left-handed states, including conjugate signs. They vanish, covering perturbative abelian and mixed anomalies for the A5 and D4 branches too. This follows structurally because net multiplicities reproduce three restrictions of the E6 27. It is not a claim of all global string anomalies. An explicit asymmetric mirror-deletion control leaves anomaly vector `(0,−12,+12)`.

The complete cubic species list built from the **actual charged fields** is

```
det Q, det Qc, det L, Q Qc L,
det Qbar, det Qcbar, det Lbar, Qbar Qcbar Lbar.
```

Triality enumerates the candidates; for each survivor there is an explicit invariant tensor: two epsilon tensors for a determinant or a closed index contraction for Q Qc L. A determinant of a single commuting bifundamental chiral superfield is nonzero: exchanging two field factors changes both epsilon signs. It is not the vanishing antisymmetric singlet of three identical single fundamentals. Each cubic has total Wilson phase zero and therefore total geometric character zero as well. The actual E6 cubic and overlap tensors can relate coefficients or set entries to zero; we do not assign independent arbitrary nonzero couplings to the compactification.

Allowed bilinears are precisely `Q Qbar`, `Qc Qcbar`, `L Lbar`. Before Higgsing their flavor matrices are 7×4, 7×4 and 9×6, so maximal possible pair-removal ranks are 4,4,6. These are **upper bounds**, not achieved ranks. At the specified massless standard-embedding point these cohomology zero modes are not assigned generic constant masses. Moving away in moduli or adding a justified VEV could generate masses, which has to be computed.

A neutral modulus S can permit `S L_i Lbar_j` and analogous terms. The existence, count, character and coupling tensors of the relevant neutral modes must be computed from the compactification; this statement does not add a spectator S. In particular, a gauge-allowed term is not automatically a nonzero overlap integral.

## 5. Actual-field route from trinification to the SM algebra

Regard L as a 3×3 matrix with a fundamental L index and antifundamental R index. Use two distinct flavors already present:

```
<L1>=v e32, <L2>=w e33,
<Lbar1>=conjugate(v) e23, <Lbar2>=conjugate(w) e33,
v,w nonzero; Q=Qc=their conjugates=0.
```

The exact unit-magnitude witness is in `interactions.py`. Each conjugate pair cancels its non-Abelian D terms with canonical kinetic metrics. For actual noncanonical positive Kähler metrics, physical normalization/alignment and the simultaneous F equations remain to be checked; equal raw coordinates are not asserted universally.

For every off-diagonal root generator and both diagonal generators in sl3_L and sl3_R, the code imposes **both**

`A L_i − L_i B=0`, `B Lbar_i − Lbar_i A=0`.

The full 16-generator constraint matrix has rank 12, hence a four-dimensional stabilizer. The four independent surviving generators are E12_L, E21_L, diag(1,−1,0)_L, and

```
Y_L = diag(−1/6,−1/6,1/3),
Y_R = diag(−2/3,1/3,1/3).
```

Including the untouched eight color generators gives exactly dimension 12 and the explicitly identified algebra `su3_C+su2_L+u1_Y`, not merely a dimension match. Both raising and lowering actions and conjugate-field constraints are included, avoiding the larger parabolic stabilizer one gets from holomorphic L VEVs alone.

The SM branching per Q,Qc,L is

```
Q  -> (3,2)_(1/6) + (3,1)_(-1/3),
Qc -> (bar3,1)_(-2/3) + 2 (bar3,1)_(1/3),
L  -> (1,2)_(1/2) + 2 (1,2)_(-1/2) + (1,1)_1 + 2 (1,1)_0.
```

It contains a quark/lepton family and additional triplet, doublet and neutral fields. The two chosen entries of L have Y=0. Hypercharge here is derived from the actual charges and VEVs; the Wilson phase is never misidentified as Y.

### What the charged potential does and does not prove

Every charged determinant gradient vanishes on this branch: all L VEVs occupy the same row, so all polarized two-row cofactors vanish; the conjugates occupy the same column. The Q Qc L derivatives vanish at Q=Qc=0. Thus arbitrary **charged-cubic** flavor coefficients leave this branch F-flat. The code checks the cofactor polarizations, not only the determinant's value.

But a nonzero bilinear mass gives `F_Lbar = M L`, which can kill the branch. Even with S=0, a term `S Tr(L Lbar)` gives `F_S=Tr(L Lbar)≠0` for the displayed real-paired witness. This executed negative control is the concrete reason that a charged-cubic/D-flat alignment is not yet a compactification vacuum. It may be possible to solve the actual flavor-tensor constraints with complex alignments; no such solution is assumed.

Along a valid branch, Q Qc L couples the Q exotic row to right-handed Qc directions and can generate triplet masses; det L gives doublet mass terms when one L entry acquires a VEV. Their ranks depend on the actual mixed-character and invariant-character Yukawas and on the chosen two flavor vectors. Broken vector multiplets also eat charged modes. No post-Higgs MSSM spectrum or removal of all unwanted states is claimed before including all these contributions.

## 6. Proof and executable boundary

`exact_certificate.py` uses standard-library rational arithmetic for all 729 toral elements, Weyl orbits, roots, weights, charges and anomaly tensors. `interactions.py` supplies exact invariant enumeration and the full matrix stabilizer, D-flat witness and charged-F-term controls. Saved receipt replay is the default; `--create` exclusively creates a missing receipt. `certificate.initial.json` is an explicitly superseded early lattice-only development receipt, not release evidence.

`Formalization.lean` proves universally quantified Peano addition exchange/cancellation and the conditional theorem `paired_mass_preserves_net`: from `n=m+k`, `n=nleft+p`, `m=mleft+p`, it derives `nleft=mleft+k`. It also checks the nonzero four-pair witness. This prevents paired mass removal from being conflated with a change of index. The theorem does not assume its conclusion, but its physical mass-pairing hypotheses and the root/cohomology inputs are external. Lean 4.32.1 kernel-only/no-Init compilation exits zero. Exact axiom reports are retained for five declarations, each with no axioms; no `sorry`, `admit` or unsafe escape is used. This is not a Lean formalization of E6 lattices, the compactification or the scalar potential.

Run from the canonical lane with native Windows Python, for example

```
C:/Python313/python.exe -B exact_certificate.py --verify
C:/Python313/python.exe -B verify.py --verify
```

`verify.py` recompiles Lean, checks all five exact axiom reports, replays the predecessor exact certificate read-only and this saved certificate, and executes missing/tampered-receipt negative controls with restoration in `finally`. It hashes the release inputs and compares an existing verification receipt; replay never silently refreshes it. Local checks only; no hosted CI or publishing performed. Windows file-tool writes initially landed in the documented Cygwin shadow tree; final artifacts were copied into and executed from the canonical native lane. No other research lane was edited.

## Remaining physical gates

1. Compute H1(End TX) characters and the actual descended neutral-coupling tensors; test all F equations on a D-flat two-pair branch.
2. Compute mixed-character Q Qc L and conjugate Yukawas and invariant L³ data in a compatible normalized basis; distinguish sourced nine-mode Yukawa data from the new 7×7×9 tensor.
3. Include Higgs-eaten modes, full mirror and exotic mass matrices and remaining light Higgs doublets. Prove ranks instead of selecting them.
4. Establish moduli stabilization, full Hessian stability, threshold matching and physical couplings. The topology and Wilson line do not fix volume, dilaton or absolute alpha.

Partition/eta, Ramanujan, Dedekind, Kauffman/knot and Dirac/clock links remain hypotheses or predecessor-specific bridges. None has been promoted here to a geometry selection law, a Yukawa tensor, a stable vacuum or a numerical alpha prediction.
