# Tian–Yau colored Yukawa gate: exact charged cup products, relative slices and gauge rank

## Outcome and unfinished requirement

The geometric cup products in the two requested charged slices have been computed over **QQ**, not assigned generic rank. Relative to the nonzero top class `t = c0 cup c0 cup c0`, their ranks are **7 and 6**. Contracting the actual Higgs matrices `L0=e32`, `L1=e33` gives a **7x14 active triplet mass block of rank 7**, separately for each color. Both four-dimensional nontrivial-character dual bases have also been constructed as actual closed Čech–Koszul cocycles.

**The task is not completely closed:** the absolute adjunction comparison `t -> lambda*g` with the predecessor's fixed scalar H3 generator `g` has not been calculated. `lambda` is provably nonzero, but its numerical value, orientation sign and absolute normalization are not supplied. The displayed matrices are genuine geometric Yukawa **ratios**, not fabricated absolute residue-normalized entries. The conjugate beta0/beta1 4x4 slices remain uncomputed. No complete exotic-removal or compactification-vacuum claim follows.

## 1. Inputs and exact bases

The geometry, standard tangent embedding and Z3 action are exactly the frozen predecessor member:

```
f0=(x0^3+x1^3+x2^3+x3^3)/3
f1=x0*y0+x1*y1+x2*y2+x3*y3
f2=(y0^3+y1^3+y2^3+y3^3)/3
weights(x,y)=(0,2,1,1;0,1,2,2).
```

The ambient monad is `A=O^2 -> B=O(1,0)^4+O(0,1)^4 -> C=O(3,0)+O(1,1)+O(0,3)`, at degrees `-1,0,1`. `E` is the two Euler maps; `J` is the actual Jacobian, including the inherited 1/3 convention. `JE` is the multidegree matrix times the defining equations. Smoothness, freeness, the standard embedding, and the selected massless cubic branch are inherited assumptions/results rather than re-proved here. This remains an E6 commutant construction in the heterotic E8 ansatz, not a derivation from an E7 compactification.

The Higgs report and its certificate are frozen. Its certificate SHA256 is `ee714241c3c2483378afe2cb2a9112ce0075bcea3b015c640d12fcebbf0a6468`, exactly the parent's accepted predecessor. In particular we use geometric flavors `(c0,c1; beta0,beta1)` and not abstract unnamed copies of the gauge representation.

Write `m e_h` for the polynomial normal component in equation h, with h=0,1,2. The ordered character-2 basis, used for Q, is:

```
u0=x1^2*x3 e0    u1=x1^2*x2 e0
u2=x0*x3^2 e0    u3=x0*x2*x3 e0
u4=x0*x2^2 e0    u5=x0^2*x1 e0
u6=y1*y2*y3 e2.
```

The ordered character-1 basis, used for Qc, is:

```
v0=x1*x3^2 e0    v1=x1*x2*x3 e0
v2=x1*x2^2 e0    v3=x0*x1^2 e0
v4=x0^2*x3 e0    v5=x0^2*x2 e0
v6=y0*y2*y3 e2.
```

The invariant nine-element basis is byte-for-coordinate checked against the predecessor labels:

```
c0=x3^3 e0, c1=x2*x3^2 e0, c2=x2^2*x3 e0,
c3=x2^3 e0, c4=x1^3 e0, c5=x0*x1*x3 e0,
c6=x0*x1*x2 e0, c7=y0*y1*y3 e2, c8=y0*y1*y2 e2.
```

These are not merely monomial labels: `certificate.json` saves all 23 actual closed module cocycles on the sixteen product affine charts, at keys `((13,10+h),(),exponent,(chart_x,),(chart_y,))`. The inherited total Čech–Koszul differential is applied to each. H0 normal quotients are derived from the actual equations and Jacobian: polynomial spaces of dimensions `(22,17,17)` have boundary ranks `(13,10,10)`, leaving `(9,7,7)`. The possibly additional H1(B) contributions have actual injective Jacobian maps of ranks `(4,2,2)` on sources of those same dimensions. The remaining H1 diagonal slots and incoming arrows vanish. Thus these are full mixed-character H1(TX) bases, not assumed subsets.

## 2. Actual derived wedge computation

Introduce bookkeeping variables `p0,p1,p2` for the three C summands, of internal degree one and line degrees `(-3,0),(-1,-1),(0,-3)`. A normal section is `p_h*m`; these variables are not physical fields or a phenomenological ansatz.

Compute the multigraded quotient

```
R = QQ[x,y,p] / (f0,f1,f2, sum_h p_h*partial_i f_h for i=0,...,7).
```

The character-zero, line-degree-zero, p-degree-three polynomial space has **2527** monomials. Exact rational elimination derives boundary rank **2526**, with surviving representative

```
t = p0^3*x3^9 = c0^3.
```

The ring calculation alone would not certify a geometric Yukawa. Here it is realized in the **third derived exterior power of the actual curved tangent monad**. A and C are odd internal-degree terms and hence symmetric under graded exterior interchange; B is even and antisymmetric. On the exterior–Koszul complex the implemented differential is

```
D = kappa + (-1)^k d_L - sum_h epsilon_h H_h,
```

where `d_L^2=sum_h f_h H_h`, and H acts as the induced even derivation. This is the exterior-power extension of the predecessor's curvature cancellation. All primitive monomials in the quotient are genuine global cochains:

* an f_h relation has primitive `epsilon_h*(C C C)*m`;
* a Jacobian relation has primitive `B_i*(C C)*m`.

Their total degree is two and their full D-images, with the actual grading and characters, are verified to equal the relation. The stored boundary DAG expresses every pivot as a checked rational linear combination of these primitives and earlier pivots. For all **98** requested products it saves the wedge cocycle and an executable primitive DAG satisfying `u_i wedge v_j wedge c_k = Yhat[k,i,j]*t + D b[k,i,j]`. This is not a prose primitive or an endpoint initialized to zero.

### Why the quotient really survives to geometric H3

The calculation explicitly rules out higher-page erasure and competing total-degree-three slots. All 43 distinct line degrees in the exterior cube are checked against the inherited full ambient Koszul cohomology, character by character; the polynomial H0 calculation is independently checked against the regular-sequence Hilbert series. H2 is zero throughout. H3 occurs only for the trivial-line `Sym^3 A` terms, at monad degree -3, not at degree -1 or 0.

The nonzero H1 line terms are exactly the pure-x or pure-y ones. Their representatives are the cubic-surface polynomial quotient of degree d-1 times the opposite P3 top Laurent generator, with the appropriate two Koszul factors. The full induced exterior Jacobian row has, for p=-3,...,3:

```
E1 dimensions: 0,12,56,132,188,172,74
successive ranks: 0,12,40,90,98,74
E2 dimensions: 0,0,4,2,0,0,0.
```

The row matrices and square-zero checks are saved. In particular `(p,q)=(1,1)` is zero, so no d2 reaches `(3,0)`; `(0,2)` and `(-1,3)` are zero, so no d3 or d4 reaches it either. Larger arrows have no sources. The other total-degree-three slots `(2,1),(1,2),(0,3)` vanish. Consequently `[t]` is a **nonzero basis of H3(exterior^3 TX)**, not an unproved polynomial candidate. The CY determinant isomorphism identifies this one-dimensional group with H3(O).

## 3. The two exact relative slices

Rows are u0,...,u6 and columns v0,...,v6. Let `lambda` denote the as-yet uncomputed image of `[t]` in the predecessor's scalar residue coordinate. Then the **actual** slices obey `Y0=lambda*Yhat0`, `Y1=lambda*Yhat1`, where

```
             [ -1  0  0  0  0  0  0 ]
             [  0  0  1  0  0  0  0 ]
             [  0  0  0  0 -1  0  0 ]
Yhat0 = 1/3  [  0  0  0  0  0  0  1 ]
             [  0  0  0  0  0  1  0 ]
             [  0  0  0  1  0  0  0 ]
             [  0  1  0  0  0  0  0 ]

             [  0  0  1  0  0  0  0 ]
             [  0  1  0  0  0  0  0 ]
             [  0  0  0  0  0  0  1 ]
Yhat1 = 1/3  [  0  0  0  0  0  1  0 ]
             [  0  0  0  0  1  0  0 ]
             [  0  0  0  0  0  0  0 ]
             [  1  0  0  0  0  0  0 ].
```

`det(Yhat0)=-1/2187`, `rank(Yhat0)=7`; `rank(Yhat1)=6`. Both SymPy rational linear algebra and a separate sparse rational elimination reproduce these ranks. The full nine relative slabs, dimensions 7x7x9, are also saved. The c1 slice's zero sixth row is an executed negative control against silently declaring both slices maximal.

### Precise residue-normalization boundary

The predecessor's explicit scalar generator g is copied and rechecked as D-closed. Its ambient H6/Koszul-degree-three scalar projection is exactly one. We **do not set** `lambda=1` merely because both spaces have dimension one. The missing calculation is the adjunction/determinant comparison map from the derived exterior module to the scalar Čech–Koszul resolution, including its orientation and any factorial convention. Applying that map to the saved nonzero t and comparing its scalar cocycle to g would determine lambda. The isomorphism proves lambda is nonzero; therefore all stated ranks are already geometric and independent of this remaining scalar. It does not provide an absolute unnormalized coupling, a quotient-volume factor, or a canonically normalized physical Yukawa.

## 4. Charge, signs and representative controls

The Z3 condition is checked on every basis and polynomial boundary. `2+1+0=0` gives the required mixed character. The exact cyclotomic projector is evaluated modulo `omega^2+omega+1`, giving three in charge zero and zero in charges one and two. A concrete wrong-character monomial is rejected before projection. No floating approximation to a root of unity is used.

Controls executed on actual chains include:

* total D squared zero on **2808** exterior/Koszul basis-sector probes;
* **1224** failures under the wrong curvature sign;
* **676** keywise graded Leibniz identities on nonclosed generators;
* all **98** requested product/primitive equalities, independently reconstructed from the saved boundary DAG;
* **280** nonzero colored representative-boundary products and **735** nonzero Higgs representative-boundary products, each with its actual primitive and vanishing quotient class;
* an incorrect ungraded antisymmetric treatment of C would kill `c0^3`; this is rejected against the independently nonzero geometric top class;
* invertible flavor shears preserve the derived rank, while transposing the Higgs gauge matrices changes the actual component mass matrix.

These are local exact computational checks with mathematical spectral-sequence interpretation, not Lean-kernel or peer-review certification.

## 5. Gauge contraction and what becomes massive

Use exactly the inherited orientation `Q[a,l]`, `Qc[r,a]`, `L[l,r]`, with color index a. The index-loop interaction is

```
W_Q = sum_(i,j,k,a,l,r) Y[k,i,j] Q_i[a,l] Qc_j[r,a] L_k[l,r].
```

For the explicit branch `L0=e32`, `L1=e33` (one-based matrix indices),

```
W_mass = lambda * sum_(a,i,j) Q_i[a,3]
              * (Yhat0[i,j] Qc_j[2,a] + Yhat1[i,j] Qc_j[3,a]).
```

Thus the active block is **`lambda*[Yhat0 | Yhat1]`**, not the sum of the two matrices and not two independent sets of seven masses. Its rank is **7**. The complete per-color Q/Qc component matrix is 21x21, with rank 7 and support only on the l=3 rows; it and its component labels are saved. The active 7x14 block has seven exact right-kernel vectors in the receipt. The L metric parameterization in the predecessor adjusts the dual VEVs, not these two L matrices, so this charged block is unchanged throughout that stated constant-positive-metric family (up to a common nonzero VEV scale).

This gives seven mass bilinears pairing the SU2-singlet color triplets in Q with seven combinations of the two charge-1/3 antitriplet columns of Qc. The remaining seven antitriplet combinations, all Q doublets, and the first Qc column are untouched by this block. Color gives identical copies; it does not multiply a flavor rank or establish removal of all vectorlike matter. These are not Q-Qbar mass terms. Additional neutral backgrounds, conjugate blocks, doublet sectors, eaten directions and other allowed bilinears have not been assembled into a complete Hessian.

## 6. Conjugate partner scope

`charged_dual_bases.py` extends the actual predecessor Serre-chain construction to characters one and two, with the actual weight-shifted line bases. It constructs four H1(TX*) cocycles in each character, each of 84 Čech–Koszul terms, and saves both vertical primitives for every class. In each character the dual E2 rows, in monad degrees -1,0,1, are

```
q0: (0,0,0), q1: (0,0,0), q2: (4,0,0), q3: (7,0,0).
```

Thus the partner domains are no longer missing or guessed. Beta0 and beta1 remain exactly the predecessor's terminal global A* generators. What remains missing is the **dual exterior-cube cup/adjunction trace** on these newly explicit charged-character partners with beta0/beta1. Neither its two 4x4 matrices nor their ranks are assigned. Their domain is H1(TX*)_1 x H1(TX*)_2 x span(beta0,beta1). The earlier `certificate.json` was frozen before this supplementary basis construction and its textual missing-domain inventory is superseded specifically by `charged-dual-bases.json`; its absent cubic matrices remain absent.

## 7. Artifacts, replay and disclosure

All writes are confined to this lane; every predecessor is preserved. `frozen/` holds the native source dependencies, geometry, Serre data and Higgs evidence. Primary calculation, dual-basis calculation and supplementary audit were source-frozen separately before their first executions. `charged-wedge-chains.json` holds exact relation primitives, the acyclic boundary DAG, product lifts and the H1 exterior row matrices. `certificate.json` holds the charged bases, nine relative slabs, rank, scalar generator and gauge blocks. `charged-dual-bases.json` contains the eight genuine dual lifts. `supplementary-audit.json` contains the independent saved-data and sign controls.

Run:

```
C:/Python313/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/tian-yau-colored-yukawa-gate/verify.py
```

The default verifier requires all saved receipts, checks frozen release hashes before and after all three exact replays, and does not recreate receipts. `native-replay.log` and `native-replay-status.json` document the separate completed replay. No hosted CI, Lean, independent expert review or publication is claimed. AI-assisted implementation and mathematical interpretation are disclosed.

The initial exploratory ring script included zero derivative coefficients as monomials and stopped with a KeyError before producing a result. Its contemporaneous native source is preserved as `explore-ring-initial-failed.py`; the filter was repaired before source freezing. As in predecessor lanes, canonical-looking file-tool writes landed in the Cygwin shadow tree; sources were copied once into this native lane and executed using the pinned native interpreter. The successful artifacts and replays are native, not shadow-only claims.

Still open: the absolute charged trace comparison, conjugate Yukawa slices, complete exotic mass Hessian, other neutral F terms, nonlinear field metric corrections, moduli stabilization, thresholds and observable matching. Clock, knot, partition, prime/flux-selection and alpha hypotheses remain separate unproved physical maps; no fitting target enters this calculation.

### Reference context

The geometric member and residue/coupling conventions are discussed in Butbaia et al., *Physical Yukawa Couplings in Heterotic String Compactifications*, https://arxiv.org/html/2401.15078v2, especially equations (2.10), (4.8)–(4.10). Its Tian–Yau comparison uses relative Yukawas and flags one older Candelas–Kalara table entry as incorrect. No old numerical table was substituted for the explicit calculations here, and no unverified external basis conversion was used.
