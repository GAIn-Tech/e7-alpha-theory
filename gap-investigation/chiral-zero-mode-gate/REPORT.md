# E7 orbifold/chiral-zero-mode feasibility gate

## Verdict

**Orbifolding does evade the preceding four-dimensional paired-mass chirality obstruction, but the minimal construction is not a consistent isolated chiral E6 x U(1) gauge theory.** An explicitly specified full 56 hypermultiplet can give **one 27(+1) plus one singlet(-3), with no mirror 27**, on an identity/breaking two-boundary interval. With the same breaking parity at both boundaries it gives **two** such pairs, not one. Neither spectrum cancels its mixed E6-squared-U(1) and gravitational-U(1) anomalies. The singlets cancel the cubic U(1) anomaly, not those mixed anomalies.

This is a finite next-model gate, not a solved E7 theory, not a derived three-family count, and not an alpha calculation. No brane families are inserted.

## 1. Model inputs and geometry

Choose a five-dimensional compact E7 gauge theory on a flat interval, with one massless **full** 5D N=1 hypermultiplet (eight supercharges before the boundary reduction). In 4D N=1 language it comprises independent H in 56 and Hc in 56 dual. The SUSY vector multiplet is V plus adjoint chiral Sigma. Full versus half hypermultiplets matters: no half-hyper reality constraint is imposed here. A non-SUSY bulk Dirac 56 has the same matter-fermion zero-mode counting, without the extra SUSY scalars/gauginos.

Boundary conditions are prescribed model data, not derived vacuum dynamics. No bulk masses, boundary masses, brane matter, Wilson-line backgrounds or anomaly-canceling axions are assumed. Smooth zero-background massless fields have constant zero modes precisely when even at both boundaries. Odd components have no such zero mode; opposite four-dimensional chiralities have opposite parities.[2][4]

- S1/Z2 with periodic fields: interval length L=pi R, identical parities at its two ends.
- S1/(Z2 x Z2') with reflection about 0 and pi R/2: L=pi R/2; use independently specified commuting endpoint operators. Their product gives the half-circle translation and squares to one for our choices, so the full covering circle remains periodic.

We exhaust only endpoint gauge involutions I or P that leave the **same** E6 x U(1) embedding pointwise fixed. This is not an enumeration of all E7 orbifolds, conjugate embeddings, flavor-mixing boundary matrices, fluxes or strong dynamics.

## 2. Explicit automorphism and full representation action

The canonical predecessor `../embedding-gate/REPORT.md`, `embedding_checks.py` and saved receipt were read and its existing receipt is replayed as a prerequisite. Its exact complete weight system supplies

```
X = 2 H1 + 3 H2 + 4 H3 + 6 H4 + 5 H5 + 4 H6 + 3 H7
56 = 27(+1) + bar27(-1) + 1(+3) + 1(-3)
133 = 78(0) + 1(0) + 27(-2) + bar27(+2).
```

Set g=exp(i pi X/2) and P_ad=Ad(g). A root of charge q has parity (-1)^(q/2); Cartan generators are even. Thus P_ad fixes precisely 78+1 and reverses both 27 coset sectors. It is a Lie algebra involution: root charges add in every nonzero root bracket; opposite-root brackets land in the fixed Cartan. Exact code checks all 4,158 nonzero-root/opposite-root bracket pairs.

**Do not use g itself as a Z2 operator on the 56:** all its eigenvalues are plus/minus i, so g squared is -1 there. Use the allowed full-hyper flavor phase to define

```
P_H = -i rho56(g),     P_H squared = 1.
P_H rho(T) P_H^-1 = rho(P_ad T).
```

The extra phase is compensated by its inverse on the dual. It is an explicit boundary lift, not a new gauge generator. Gauge generators are unchanged by the phase. The combined gauge/flavor action is an involution even though g alone has order four on 56. The kinetic action and bulk superpotential Hc(partial_y-Sigma)H are invariant under

```
V(-y) = P_ad V(y),             Sigma(-y) = -P_ad Sigma(y),
H(-y) = eta P_H H(y),          Hc(-y) = -eta Hc(y) P_H^-1,
eta = +1 or -1.
```

For an identity endpoint replace P_ad and P_H by I. The derivative minus sign and the odd Sigma transformation explain the dual field's opposite parity; it cannot be discarded while retaining a full hypermultiplet.[4]

| H charge sector | +1:27 | -1:bar27 | +3:1 | -3:1 |
|---|---:|---:|---:|---:|
| P_H eigenvalue | + | - | - | + |
| Hc parity on its dual | - | + | + | - |
| Hc physical charge | -1 | +1 | -3 | +3 |

The certificate enumerates all 56 actual weights in each of H and Hc, negating the original weight for Hc. It verifies all 1,512 directed nonzero minuscule root transitions. For each endpoint type, SMT excludes every other diagonal sign assignment obeying all these intertwining constraints except the two overall signs. Thus choosing signs separately for the 27 and unwanted singlet is not legal in this representation action. This claim assumes the predecessor's minuscule representation construction; it is not a Lean proof of the E7 representation.

More generally Schur's lemma says any intertwiner for a fixed automorphism on this complex irreducible representation differs from this lift by a scalar; with square one only the overall sign remains. This statement does not include boundary operators that mix separate hypermultiplets or their duals.

## 3. Complete zero-mode outcomes

The exact receipt stores all sixteen (k0,k1,eta0,eta1) cases with k=0 identity and k=1 breaking, including weight-resolved H/Hc modes, vector and Sigma sectors, and endpoint anomaly coefficients. Define S=27(+1)+1(-3); barS is its left-handed conjugate.

| Endpoint types | Intrinsic signs | H zero modes | Hc zero modes | Net 27 |
|---|---|---|---|---:|
| I,I | +,+ | full 56 | none | 0 |
| I,I | -,- | none | full dual 56 | 0 |
| I,I | opposite | none | none | 0 |
| P,P | +,+ | S | S | +2 |
| P,P | -,- | barS | barS | -2 |
| P,P | opposite | none | none | 0 |
| I,P or P,I | identity sign +, P sign + | S | none | +1 |
| I,P or P,I | identity sign +, P sign - | barS | none | -1 |
| I,P or P,I | identity sign -, P sign + | none | S | +1 |
| I,P or P,I | identity sign -, P sign - | none | barS | -1 |

The first and last repeated rows represent the explicitly stated sign/type degeneracies, not omitted choices. The I/P construction is a concrete **one-27-without-mirrors kinematic success**. The periodic single-Z2 P construction gives two and retains two charged singlets. For N separately assigned full hypers, multiplicity N is action input. Three I/P hypers can kinematically yield three S's, but that is **three chosen bulk copies, not a derived family count**, and their anomalies add.

Gauge zero modes: I/I leaves all 133; every case with a P endpoint leaves E6 x U(1), dimension 79. Intrinsic matter signs do not affect the gauge sector. Rank is not reduced and X is not electromagnetism. In the SUSY P/P model Sigma additionally has coset zero modes 27(-2)+bar27(+2), a vectorlike pair; ignoring it would omit actual massless fields. I/P removes these Sigma zero modes. At tree level and zero background these results say nothing about stabilization, loop potentials or subsequent E6-to-SM breaking. The surviving 27 still contains standard-chain vectorlike exotics in addition to its family; no Higgs spectrum, exotic mass mechanism or photon vacuum is supplied.

## 4. Anomaly obstruction and scoped no-go

All matter below is left-handed. For n net copies of S, the exact coefficients are

```
A[E6^2 X] / T(27) = n,
A[gravity^2 X] = 27 n - 3 n = 24 n,
A[X^3] = 27 n - 27 n = 0,
A[E6 X^2] = 0 (E6 generator trace).
```

Pure E6 has no cubic gauge anomaly, despite admitting a cubic invariant of three matter 27s: the latter has fundamental, not adjoint, indices.[5] To avoid mixing trace conventions, the reported mixed nonabelian coefficient is in **T(27) units**, not a casually imported numerical index. Vector/Sigma zero modes have no net contribution to these anomalies.

In unit-integrated endpoint-delta convention, a full bulk Dirac field contributes one half of its parity-weighted representation anomaly at each boundary. This is the representation-resolved application of the localized orbifold anomaly formula; endpoint normalization conventions in the primary papers are recorded separately in `sources/research-findings.md`.[2][3] Our exact local traces yield:

| Boundary configuration | Endpoint E6^2 X / T(27) | Endpoint gravity^2 X |
|---|---|---|
| I(+),P(+) | (0,1) | (0,24) |
| P(+),P(+) | (1,1) | (24,24) |
| P(+),P(-) | (1,-1) | (24,-24) |

The first row does **not** split its anomaly equally between the two walls: the full-E7 identity wall has zero parity-weighted E7 trace; the reduced-symmetry wall carries the obstruction. Opposite P signs show the independent localized constraint even with no massless matter. All sixteen local sums are checked against their zero-mode integrated anomalies.

Ordinary periodic Chern-Simons inflow can redistribute anomalies but cannot cancel a nonzero integrated anomaly. Pilo--Riotto derive the periodicity condition integral f(y)dy=0; Scrucca et al. explicitly state that inflow works only when the integrated anomaly vanishes.[1][2] Zero integrated anomaly is necessary, not a demonstrated sufficient local completion for an E7 action. In particular no E7-invariant inflow operator or its quantized coefficient has been constructed here. The global gauge form, allowed large transformations, possible global anomalies and UV regulator must also be checked for any extension; the present local perturbative failure already blocks promotion.

**Scoped no-go:** any sum of the enumerated independent full-56 hypermultiplets with these identity/E6-U1 boundary involutions, no extra anomaly sector, and unbroken gauged X has mixed gravitational anomaly 24 times its net 27 index. Therefore anomaly cancellation forces net index zero. A total net three and zero mixed gravitational anomaly is an SMT-unsatisfiable constraint. This excludes three chiral families in this **specified minimal class**, not all E7 compactifications. Pairing S and barS cancels the anomaly but also cancels the sought chirality. Charged singlets alone cannot cancel E6-squared-X.

## 5. Bounded alternatives and coupling freedom

Only the following concrete alternatives are retained, each explicitly outside the tested class:

1. Keep the I/P kinematic projection but add a specified anomaly-canceling Green--Schwarz/Stueckelberg sector, or charged boundary matter, and recheck every local anomaly. A genuine axionic sector can modify the obstruction and commonly gives X a mass; simply declaring X broken or adding a scalar VEV does not erase a UV gauge anomaly. The primary orbifold anomaly discussion identifies U(1) breaking in its Green--Schwarz proposal.[1] Extra charged matter is new input and is not a derived family count.
2. Choose a different second gauge involution/embedding that also breaks E6 and permits a different SM-level projection, or investigate a rigorously consistent half-hyper/reality construction. This requires a fresh action, compatibility and full zero-mode calculation; one may not halve the full-hyper result by hand. No such alternative is claimed checked here.
3. Move to flux/bundle index constructions with higher-dimensional chirality and their own anomaly cancellation. This is a new model, not an automatic consequence of E7.

The kinematic I/P result is sufficient progress to stop the present finite search. It does not justify proliferating parity assignments to fit alpha.

With connection-convention kinetic terms, define L as the physical interval length and tau terms as inverse squared couplings in the inherited normalized-generator basis. Tree matching has

```
1/g6,4^2 = L/g7,5^2 + tau6,0 + tau6,L,
1/gX,integer,4^2 = 12 [L/g7,5^2 + tauX,0 + tauX,L].
```

An identity E7 wall relates its normalized coefficients; an E6 x U(1) wall permits separate E6 and X coefficients. The factor 12 is the predecessor's Bphys(X,X), not a fitted constant. Even setting every tau to zero by assumption leaves the continuous input L/g7,5^2. Thresholds and later abelian mixing add matching data. A standard SU5 Y choice remains distinct from X. No geometry, boundary kinetic terms, scale hierarchy, electromagnetic vacuum or coupling boundary value has been independently fixed. The old unbroken nonsupersymmetric eight-Dirac-56 RG coefficients cannot be reused after this projection, addition of SUSY fields or Kaluza--Klein thresholds.

## 6. Verification and disclosure

- `orbifold_checks.py`: predecessor receipt replay; 126 roots, 56 weights, 4,158 bracket checks, 1,512 representation transitions, sixteen full spectra, exact integer/Fraction local/global anomaly arithmetic.
- Three saved SMT-LIB problems: two exhaustive diagonal-lift exclusions and the conditional net-three anomaly contradiction. These are Z3 checks, **not Lean-kernel proofs**. No new Lean theorem or Mathlib build is claimed.
- `test_orbifold.py`: twelve tests including missing/tampered receipt negatives and independent saved-SMT replay. `run_checks.py` records actual subprocess exit codes/output and artifact hashes in `verification.json`.
- `orbifold-receipt.json`: deterministic output with full surviving weights and source hashes. Default mode compares the existing saved receipt before accepting; creation is exclusive and opt-in.
- `sources/research-findings.md` and its ledger: primary-paper excerpts, equation locations and normalization cautions. No primary publication of exactly this E7/full-56 boundary lift was found in the bounded search; its construction is the explicit derivation above, not an attributed paper result.

AI-assisted, self-assessed research. Exact finite computation plus external Lie representation facts and primary field-theory formulas are the trust boundary. No expert review, hosted CI, quantum completion, mass stability, derived families, or alpha prediction is asserted. Only this new directory is written; no publication, commit, push or history rewrite.

## Sources

[1] https://arxiv.org/pdf/hep-th/0110073
    > "observe that the presence and the structure of the anomalies that we have fou"
[2] https://arxiv.org/pdf/hep-th/0202144
    > "n the cases of fermi"
[3] https://arxiv.org/pdf/hep-th/0103135
    > "ing (2.8), we can compute the matrix element of ∂µJµ. Only the"
[4] https://arxiv.org/html/1001.4074v3
    > "two oppositely charged chiral superfields"
[5] https://par.nsf.gov/servlets/purl/10635146
    > "E6 admits complex representations"
