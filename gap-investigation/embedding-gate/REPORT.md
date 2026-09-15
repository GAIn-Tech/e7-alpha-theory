# E7 electromagnetic embedding and chirality gate

## Verdict

**The regular E6 x U(1) embedding passes the exact representation gate, but neither proposed four-dimensional matter theory passes the chiral Standard Model gate.** The commuting U(1) is not electromagnetism. Its normalization determines a coupling *ratio*, not a value of alpha. A standard SU(5) hypercharge chain supplies a target-independent conditional matching convention, but a breaking vacuum and chiral zero-mode mechanism are still missing.

This is additive work only. The legacy README's alpha and significance claims are not adopted. The prior `next-gate/REPORT.md` and the independent `rg-fixed-point-gate/REPORT.md` were read; their actions remain distinct.

## 1. Exact branching, with charge orientation fixed

Use Bourbaki chain 1-3-4-5-6-7, branch 2-4. Delete node 7, retaining the regular E6 root subsystem. Work with the compact gauge algebra and its complex representations; `E6 x U(1)` here denotes the Lie-algebra embedding, not a assertion about the global subgroup being a direct product.

Let H_i be simple coroots and choose the integral generator

```
X = 2 omega7^vee = 2 H1 + 3 H2 + 4 H3 + 6 H4 + 5 H5 + 4 H6 + 3 H7.
alpha_i(X) = (0,0,0,0,0,0,2)_i.
```

Thus X is fixed by the deleted-root embedding, with primitive integer charges on the 56, rather than selected by an experimental number. `embedding_checks.py` generates all 56 weights as the omega7 Weyl orbit and verifies that its size saturates the independent Weyl dimension. It computes charge sectors, every E6 Weyl orbit and its dominant highest weight, and the 126 roots plus seven zero weights of the E7 adjoint. Results:

| E7 representation | X charge | E6 highest weight (six Dynkin labels) | Dimension |
|---|---:|---|---:|
| 56 | +3 | (0,0,0,0,0,0) | 1 |
| 56 | +1 | (0,0,0,0,0,1) | 27 |
| 56 | -1 | (1,0,0,0,0,0) | 27 |
| 56 | -3 | (0,0,0,0,0,0) | 1 |
| 133 | -2 | (0,0,0,0,0,1) | 27 |
| 133 | +2 | (1,0,0,0,0,0) | 27 |
| 133 | 0 | (0,1,0,0,0,0) plus trivial | 78+1 |

The neutral adjoint sector is explicitly 72 E6 roots and seven zero weights: six belong to the E6 adjoint and one to its commuting generator. The nonzero-charge sectors are single Weyl orbits saturating their E6 Weyl dimensions, so their irreducibility is checked rather than guessed from dimensions.

Calling V(omega6 of E6) `27`, consistently in **both** equations,

```
56  = 27_(+1) + conjugate(27)_(-1) + 1_(+3) + 1_(-3)
133 = 78_0 + 1_0 + 27_(-2) + conjugate(27)_(+2).
```

These agree with the original Exceptional Reductions paper, equations (4.2)-(4.3), printed p.12; its displayed overbars were visually checked because PDF extraction loses them.[3] An overall charge reversal is harmless, but reversing the adjoint orientation alone is not the same convention. The paper's supergravity/real-form applications are not imported as a compact Yang-Mills model.

### Algorithm provenance

The Gaussian inversion and minuscule-orbit construction are adapted from `../next-gate/representation_checks.py`; the existing independent `C:/Users/mikeb/theory2-full/docs/analysis/weyl_verification.py` supplies only Cartan, root closure and Weyl-dimension routines. The receipt hashes both inputs and the new script. No hardcoded old alpha expression is read. Exact integer/Fraction arithmetic, standard highest-weight theory, Weyl dimensions and complete reducibility are the mathematical trust boundary; the root and branching algorithms are **not Lean-kernel formalizations**.

## 2. Generator normalization and tree-level coupling matching

Retain the prior convention B0 with dual long-root squared length 2, B0(H_i,H_j)=A_ij, and Bphys=2 B0. The executed complete weight sums yield

```
Tr_56 X^2 = 72;       Tr_133 X^2 = 216;
B0(X,X) = 6;         Bphys(X,X) = 12;
Tr_56(X H_i) = 0     for i <= 6.
```

The normalized Hermitian generator is t_X=X/sqrt(12); hence Tr_56(t_X^2)=6 and Tr_adj(t_X^2)=18, matching the prior gate without mixing doubled Casimirs. The E6 root subsystem has embedding index one in this convention (the same simple-root Cartan submatrix and long-root length).

**Physical matching assumptions:** a compact E7 Yang-Mills theory with one invariant two-derivative kinetic coefficient; a vacuum or other breaking construction realizing this subgroup; canonical gauge fields; tree level; no threshold corrections, field-dependent gauge kinetic terms or induced abelian mixing. Write D=partial-i g7 A^a t_a, L=-F^a F^a/4. Then at the matching scale M,

```
g6(M) = g7(M),
D_X = partial - i [g7(M)/sqrt(12)] B X,
g_X,integer(M) = g7(M)/sqrt(12),
alpha_X,integer(M) = alpha7(M)/12.
```

The normalized-generator U(1) coupling equals g7; the coupling multiplying the **integer** X charges does not. Equivalently, in connection convention L=-Bphys(F,F)/(4 g7^2), restriction along X gives -12 F_X^2/(4 g7^2). Rescaling X to sX rescales the corresponding coupling to g_X/s (up to a harmless sign orientation); the product acting on a charged field is unchanged. An arbitrary generator rescaling cannot tune a physical alpha.

The X generator commutes with all of E6 and is constant on its whole 27. It therefore cannot supply the varying Standard Model hypercharges within a family, and it is not the generator Q_em=T3+Y. The existing singlet-vacuum SUSY solution leaves all E7 unbroken; the nonsupersymmetric RG family supplies no elementary breaking scalar at all. Neither has an identified isolated photon.

### A fixed, non-fitted Standard Model benchmark chain

Conditionally choose the usual regular chain E7 -> E6 -> Spin(10) -> SU(5) -> SU(3)c x SU(2)L x U(1)Y; extra commuting U(1)s must be removed by actual model data. The original E6SSM papers give this E6/SO(10)/SU(5) chain and the conventional matter assignments, with Q_em=T3+Y.[4][7] This is one explicit conventional choice, not a proof that E7 dynamically selects it.

Within the SU(5) fundamental choose

```
Y=diag(-1/3,-1/3,-1/3,1/2,1/2),
T3=diag(0,0,0,1/2,-1/2),
Bphys|su5=2 Tr_5,
kY=Bphys(Y,Y)=5/3, Bphys(T3,T3)=1, Bphys(Y,T3)=0.
```

All three trace identities are executed exactly. At a common idealized tree matching boundary, regular embedding index one gives g2=g7 and gY=sqrt(3/5) g7. A Higgs doublet with conventional neutral VEV yields the usual neutral-gauge-field massless combination and

```
1/e^2 = 1/g2^2 + 1/gY^2,
e^2/g7^2 = 3/8,        sin^2(thetaW)=3/8.
```

The last line is a high-scale conditional boundary identity, not a low-energy prediction: separately broken scales require running and matching between them, electroweak Higgs data are absent, and below further breaking abelian kinetic mixing/thresholds can matter. This standard Y is fixed by family charges, not by CODATA. It is distinct from X and from the E6SSM's additional U(1)N.[4]

## 3. Chirality: both current four-dimensional candidates fail

Count all matter as **left-handed Weyl fields**. The primary-source E6 branching is 27=16+10+1 under Spin(10), with the conjugate 27 containing a conjugate 16; one source gives the accompanying U(1)psi charges explicitly.[8] Under the conventional SU(5) chain,

```
27 = (10 + 5bar + 1) + (5 + 5bar) + 1.
```

The first bracket contains a family with a sterile neutrino; the second is vectorlike SM exotic/Higgs-type matter. This SU(5) content and the identification of the ordinary fields are given in the original E6SSM model.[4] These lower-chain branching facts are **sourced inputs** to our SM count, not independently E6-to-SM weight-derived output.

Adding the conjugate 27 and the two E7 singlets gives the following executed SM content **per Weyl 56**:

| SM representation | Multiplicity | Conjugate multiplicity |
|---|---:|---:|
| Q=(3,2,1/6) | 1 | 1 |
| u^c=(3bar,1,-2/3) | 1 | 1 |
| e^c=(1,1,1) | 1 | 1 |
| d^c=(3bar,1,1/3) | 3 | 3 |
| L=(1,2,-1/2) | 3 | 3 |
| neutral singlets | 6 | self-conjugate SM charge |

The total dimension is checked as 56. Every SM chiral index n(R)-n(conjugate R) is zero. More generally the executed E7 weight set is invariant under weight negation, so restriction retains conjugation-balanced characters for any subgroup embedding; choosing a different Cartan direction cannot produce missing net chirality.

- **Rigid N=1 candidate:** two chiral-superfield 56s plus a gauge singlet means twice this Weyl matter content. A chiral *superfield* does not mean chiral SM gauge matter. All five family indices remain zero; the adjoint gaugino is in a self-conjugate representation and does not repair them. The analyzed Q1=Q2=0 vacuum does not break E7.
- **Nonsupersymmetric RG family:** N Dirac 56s means 2N Weyl 56s after conjugating right-handed fields; at N=8 the multiplier is 16, not 8. All five indices remain zero. It has no elementary Higgs sector. The independent weak IR zero is a statement about its massless unbroken-E7 action, not about a chiral broken effective theory.

For ordinary four-dimensional bilinear decoupling preserving the unbroken SM group, a mass matrix pairs R with its conjugate. Its rank removes equal numbers from both, preserving their difference. Thus ordinary Higgs breaking and invariant mass terms alone cannot leave three net SM families from these balanced contents. Our finite tests exercise this count, and `Chirality.lean` kernel-checks the abstract equality-preservation statement with **balanced counts and paired ranks explicitly supplied**. It does not prove the representation input, rank theorem, dynamics, or a universal nonperturbative no-go. Exotic strongly interacting mirror removal, new localized fields or higher-dimensional chiral zero modes would be new mechanisms, not solutions supplied by these actions.

The RG gate's target-blind N=8 selection remains meaningful as an unbroken-E7 perturbative example. Once a breaking/compactification scale, new scalar sector, projection, masses or chiral matter is introduced, that massless spectrum and its beta coefficients need rederivation. The conditional coupling ratios above cannot be inserted into its asymptotic fixed point and relabeled a measured alpha: finite-scale approach is extremely slow according to the RG report, and the required matching theory is absent.

## 4. Concrete next model requirement

Do **not** run another alpha fit. A useful next gate is an explicit chiral-zero-mode breaking construction with the standard Y above fixed in advance:

1. Specify spacetime dimension/chirality, bulk E7 representations, compact space plus gauge bundle/flux **or** boundary/orbifold parity operators. Require compatible action and gauge boundary conditions; an adjoint scalar VEV proportional to X could realize the first algebraic centralizer, but adding such a scalar and a stable potential is new model input and still does not generate chirality.
2. Compute the surviving gauge generators and representation-resolved zero modes. A sufficient intermediate target is **three net E6 27s and no mirror excess**, followed by conventional Y breaking; equivalently demonstrate net three copies of each of Q,u^c,d^c,L,e^c at the SM stage. Do not infer three families merely from the presence of 27s in a branching table.
3. Display mirror/exotic masses, surviving Higgs doublets, the neutral VEV and photon generator. Check local/global gauge and mixed anomalies, including localized anomalies/inflow when relevant.
4. Supply the gauge kinetic matching including compactification volume, localized terms and thresholds; recalculate beta functions for the actual surviving spectrum. Only then ask whether the RG attraction and an independently fixed scale hierarchy yield a finite-scale electromagnetic prediction.

Orbifold parity is a concrete known way to remove selected zero modes: Kawamura's original construction explicitly shows odd-parity components have no zero modes and symmetry reduction results.[5] **That paper is SU(5), not a completed E7 construction, and it assumes its three chiral families on a wall.** It supplies a viable mechanism class and precise data to construct, not evidence that the required E7 model already exists. A blanket claim that any compactification automatically produces chirality is also false: Witten's original analysis gives a vectorlike result for Dirac reduction without elementary higher-dimensional gauge fields, with stated restrictions on the stronger higher-spin result.[1] We make no universal compactification impossibility claim.

## 5. Deliverables and executed checks

- `embedding_checks.py`: deterministic exact branching/trace computation; complete 56 weights and input SHA-256 provenance in `embedding-receipt.json`. Default mode reads the existing receipt first and fails on absence/mismatch; `--create` is exclusive initial creation.
- `test_embedding.py`: **11 tests passed**, including saved receipt replay, missing/tampered receipt negative controls, charge conjugation, adjoint/fundamental orientation, centralizer, normalization, rescaling, both-model chirality counts, mass-pair count invariance and electroweak matching.
- `Chirality.lean`: conditional paired-mass-removal balance theorem passed the existing Lean 4.32.1 kernel; `#print axioms` reports no axioms. No Mathlib download, representation formalization, SMT or quantum-dynamics proof is claimed.
- `verification.json`: real subprocess commands, exit codes, outputs and hashes for the code, tests, Lean and receipt. Both subprocesses exited zero.
- `sources/`: primary PDFs, extracted texts, page evidence and citation ledger. Slansky's CERN endpoint and one Euclid endpoint returned bot challenges and are labeled `BLOCKED-NOT-SOURCE`; they support no claim here. Original arXiv papers supplied the branching evidence instead.

Reproduce with native Windows paths from Bash:

```
python -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/embedding-gate/embedding_checks.py
python -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/embedding-gate/test_embedding.py
C:/Users/mikeb/e7-alpha-theory/gap-investigation/lean-4.32.1-windows/bin/lean.exe C:/Users/mikeb/e7-alpha-theory/gap-investigation/embedding-gate/Chirality.lean
```

No pre-existing repository source/history was changed; no commit, push, hosted CI or expert review is claimed. File-tool writes initially used the known shadow Cygwin mapping; new artifacts were copied to the canonical native paths before execution. AI assistance is disclosed; the evidence is the saved sources and real exact/kernel execution, not the assistant's assertions.

## Sources

[1] https://inspirehep.net/files/aafed6325868aabd22bea81c916b789e — Witten, Fermion Quantum Numbers in Kaluza-Klein Theory (1983)
[3] https://arxiv.org/pdf/1012.5797 — Marrani, Orazi, Riccioni, Exceptional Reductions (2010)
[4] https://arxiv.org/pdf/hep-ph/0511256 — King Moretti Nevzorov, Exceptional Supersymmetric Standard Model (2005)
[5] https://arxiv.org/pdf/hep-ph/0012125 — Kawamura, Triplet-Doublet Splitting, Proton Stability and an Extra Dimension (2001)
[7] https://arxiv.org/pdf/hep-ph/0510419 — King Moretti Nevzorov, Theory and Phenomenology of an Exceptional Supersymmetric Standard Model
[8] https://arxiv.org/pdf/1201.6314 — Cacciatori Cerchiai Marrani, Magic Coset Decompositions, arXiv original
