# Simultaneous geometric-flavor Higgs cubic F/D gate

## Result

There is a **nonzero two-pair SM-algebra branch of the available cubic F equations and the D equations for every positive constant Hermitian flavor metric**. Its charged VEVs use the actual common kernel of all sixteen computed bundle-neutral tensors, not a cancellation fitted to tensor coefficients. The canonical-metric point is an exact rational witness. For general metrics the conjugate-flavor/gauge alignment is adjusted explicitly. The actual compactification Kähler metric, its higher-field corrections, and all other neutral couplings are not supplied; consequently this is not an established compactification vacuum.

The nonzero four-survivor tensor does obstruct another explicit embedding of the identical gauge pattern. Neither statement retroactively identifies the unnamed flavors in the earlier Wilson-line witness.

## 1. Model, bases and provenance

Retain the Fermat/bilinear Tian–Yau member, invariant free Z3 quotient, tangent standard embedding and Wilson line of the predecessor. This is the E6 commutant in an E8 heterotic ansatz, **not an E7 repair**. The corrected invariant Ext1 count is sixteen: twelve polynomial classes plus four actual degree-one survivors from the accepted d2/d4 chain. The old assigned-zero d3 construction and its degree-zero source interpretation are not used.

The Wilson convention is Q=(3,bar3,1), Qc=(bar3,1,3), L=(1,3,bar3); gauge phases (1,2,0), opposite phases on conjugates. A geometric character a survives with gauge phase q when a+q=0 modulo three. Thus Q uses H1(TX)_2 of dimension 7, Qc uses H1(TX)_1 of dimension 7, and L uses H1(TX)_0 of dimension 9. Qbar uses H1(TX*)_1 of dimension 4, Qcbar uses H1(TX*)_2 of dimension 4, Lbar uses H1(TX*)_0 of dimension 6. All are left-handed chiral superfields. The actual-survivor calculation constructs the invariant bases only; no missing colored-character basis is invented here.

The zero-based charged invariant quotient coordinates are

```
c0=(x3^3,0,0)      c1=(x2*x3^2,0,0)
c2=(x2^2*x3,0,0)   c3=(x2^3,0,0)
c4=(x1^3,0,0)      c5=(x0*x1*x3,0,0)
c6=(x0*x1*x2,0,0)  c7=(0,0,y0*y1*y3)
c8=(0,0,y0*y1*y2).
```

The map into four-dimensional fields is **tensor product, not equality of a monomial and a gauge matrix**: a fluctuation is sum_i c_i tensor L_i, with L_i a fundamental-L/antifundamental-R matrix. A dual fluctuation is sum_j beta_j tensor B_j, with B_j fundamental-R/antifundamental-L. Gauge action is delta L=A L-L B and delta B=B B_j-B_j A (the generator B and field B_j are distinguished by their subscript).

Beta0 and beta1 are respectively the two global terminal A* generators: constant unit cochains at module keys (0,13) and (1,13), exponent zero, on all sixteen product affine charts. Beta2,...,beta5 are the actual lifted nonpolynomial dual cocycles saved in `../tian-yau-actual-survivor-coupling-gate/serre-tensor.json`, in exactly that order. They are not identified with the first two H2 coordinates: the Serre matrix has rows (0,0,0,0,-1,0), (0,0,0,0,0,-1), (-1,0,0,0,0,0), (0,-1,0,0,0,0), (0,0,1,0,0,0), (0,0,0,1,0,0), determinant one. All basis cocycles and residue normalization are pinned by the predecessor manifest, which this replay checks recursively.

The earlier `interactions.py` specified two abstract flavor slots only. This lane makes a **new explicit embedding**:

```
L0=e32, L1=e33; all other L_i=0;
B0=e23, B1=e33; all other B_j=0;
all Q,Qc,Qbar,Qcbar=0, all sixteen S_a=0.
```

Indices e_ab here are one-based; flavor indices are zero-based. The geometric flavor labels are therefore (c0,c1;beta0,beta1), not unspecified copies of 27.

## 2. All available cubic equations

Write the charged cubic as a sum of polarized determinant invariants for each of Q,Qc,L,Qbar,Qcbar,B, plus the two index-loop invariants Q Qc L and Qbar Qcbar B. Each has its actual, currently unavailable flavor tensor as a symbolic coefficient. No generic nonzero coefficient is assigned. A convenient determinant polarization is the coefficient of abc in det(aX+bY+cZ); factorial conventions can be absorbed in the undefined flavor tensor without affecting the zero-gradient claim.

The known neutral term is

`W_N=sum_(a,i,j) T[a,i,j] S_a Tr(L_i B_j)`.

For a=0,...,11 the entire 9x6 slab is the inherited computed polynomial Yoneda zero. For a=12,...,15 the only nonzero entries, read from the frozen Serre receipt, are

```
T[12,5,1]=-1; T[13,6,1]=-1;
T[14,7,0]=-1; T[15,8,0]=-1.
```

The exact residue signs are algebraic normalization, not physically normalized couplings. Thus

```
F_Sa = sum_ij T[a,i,j] Tr(L_i B_j),
(F_Li)_(mn) = (charged cubic gradient)_(mn)
               + sum_aj S_a T[a,i,j] (B_j)_(nm),
(F_Bj)_(mn) = (conjugate charged cubic gradient)_(mn)
               + sum_ai S_a T[a,i,j] (L_i)_(nm).
```

For the generic gauge pattern L_i=e3 (0,l_i0,l_i1), B_j=(0,b_j0,b_j1)^T e3^T, the four new equations are respectively minus (l_50 b_10+l_51 b_11), (l_60 b_10+l_61 b_11), (l_70 b_00+l_71 b_01), and (l_80 b_00+l_81 b_01). The first twelve equations vanish identically.

The exact stacked tensor kernel on the charged side is span(c0,...,c4), dimension five. Taking every L flavor direction in that kernel kills **all sixteen F_S independently of B**, not only their sum. At S=0, every charged derivative of W_N vanishes. The code differentiates the full actual W_N with respect to all 151 coordinates (16 neutrals and 135 L/B components).

For each charged cubic species the code differentiates a generic polarized invariant with respect to all 27 components of three independent flavor slots. Every gradient vanishes on arbitrary common-row L and common-column B alignments; colored fields vanish. This checks derivatives normal to the alignment, not just W=0 along it. Consequently the result is independent of the missing charged cubic flavor tensors. Pure cubic neutral terms have zero derivatives at the neutral origin, irrespective of their tensors. S_a Q Qbar and S_a Qc Qcbar likewise have all derivatives zero at the tested S/colored origin; their unknown coefficients are unnecessary for this restricted F check.

Other neutral species X_mu could have X_mu L_i B_j terms. Their F_X at X=0 would require the **uncomputed tensors U[mu,i,j]**. No value is assigned to them. Any constant charged mass matrices, nonzero neutral background, linear/quadratic neutral superpotential, or nonzero constant W are outside this massless cubic expansion. In a pure cubic supergravity truncation W=0 here as well, so D_i W reduces to its holomorphic derivative; adding a background superpotential changes that statement.

## 3. Parameterized positive-metric D equations and solution

The supplied evidence contains no physically normalized 9x9 L or 6x6 B metric at this point. Declare instead the quadratic Kähler potential

`K_ch=sum_ij H_ij Tr(L_i^dag L_j)+sum_ij Hb_ij Tr(B_i^dag B_j)`,

with **arbitrary constant positive Hermitian** H and Hb, block-separated by gauge representation. The unprojected moment matrices, up to a common harmless generator convention, are

```
mu_L = sum_ij H_ij L_j L_i^dag - sum_ij Hb_ij B_i^dag B_j,
mu_R = -sum_ij H_ij L_i^dag L_j + sum_ij Hb_ij B_j B_i^dag.
```

D for each SU3 generator is its trace against the corresponding matrix; color D is zero. We solve the stronger mu_L=mu_R=0, not merely traceless projection. The transpose on the dual flavor metric in the following formula is essential for complex off-diagonal metrics.

Let M=H[0:2,0:2], N=Hb[0:2,0:2]^T. Both are positive Hermitian. Choose their Cholesky factors M=R R^dag and N=S S^dag, and set U=R S^(-1). Keep L0=e32,L1=e33 and choose

`B_j=(U[0,j] e2+U[1,j] e3) e3^T`, j=0,1.

Then U N U^dag=M, so the full R moment vanishes and the L moment vanishes by the same trace identity. Cross-metric entries with any zero-VEV flavor contribute zero. This is valid for full positive H,Hb, not only block-diagonal metrics.

An exact symbolic parameterization covering **all** positive 2x2 principal blocks is

```
R=[[r,0],[x+i y,t]], S=[[p,0],[u+i v,q]],
r,t,p,q>0; x,y,u,v real;
U=[[r/p,0],[(x+i y)/p-t*(u+i v)/(p*q),t/q]].
```

The certificate simplifies both 3x3 D matrices to zero for these symbolic parameters and checks all sixteen neutral F equations again. det U=r*t/(p*q)>0. A common real nonzero scale on all VEVs gives arbitrarily small points of the same truncation branch. More general independent flavor amplitudes are unnecessary for this existence proof.

For the **explicit canonical metric assumption** H=I9,Hb=I6, R=S=I2 gives the rational original matrix point, and its full F/D equations vanish. This does not assert that the geometric monomial/Čech coordinates are physically canonical. For a general metric B0 can mix e23 and e33; the VEVs are still in exactly two charged and two dual cohomology flavors, but the cancellation is not pairwise equal-raw-norm cancellation. Positive constant-metric existence is proved; existence for the actual nonlinear field-dependent Kähler potential is not. Metric corrections may involve gradients transverse to this quadratic description and require a separate solution.

## 4. Full stabilizer and negative controls

The code constructs all sixteen sl3_L+sl3_R generators, including all six raising/lowering off-diagonal matrices on each side and both Cartans. On L0,L1,B0,B1 the complete constraint matrix has rank twelve. Its four-dimensional kernel is explicitly spanned by E12_L, E21_L, diag(1,-1,0)_L and

```
Y_L=diag(-1/6,-1/6,1/3),
Y_R=diag(-2/3,1/3,1/3).
```

These act trivially on the whole metric-parameterized family. Since U is invertible, its dual VEV span is exactly span(e23,e33); hence its **entire** stabilizer kernel equals the canonical kernel, rather than merely containing the four exhibited generators. Untouched color adds sl3_C. The compact algebra is su3_C+su2_L+u1_Y. The global quotient after Higgsing is not newly computed here.

Executed controls:

* L5=e32,L7=e33,B1=e23,B0=e33 gives the actual neutral vector (0 twelve times,-1,0,-1,0), although canonical D remains paired. This embedding fails the cubic neutral gate. It is not a universal no-go for those flavor subspaces under other alignments.
* Keep the canonical raw VEVs but change H00 to two and Hb=I: nonzero moment matrices expose the silent-identity-metric mistake.
* Transpose the dual VEVs incorrectly: the full constraint rank changes; representation orientation matters.
* A generic full-rank matrix has a nonzero determinant derivative; the common-row/common-column proof is not an assertion that determinant interactions vanish universally.
* Saved-certificate missing and tampered copies are rejected; immutable replay checks source and receipt bytes before and after computation.

## 5. Mass-rank boundary and missing data

No vectorlike-exotic mass rank is reported. The Hessian needed for colored triplets contains the mixed-character charged tensor Y in H1(TX)_2 x H1(TX)_1 x H1(TX)_0, dimensions **7x7x9**, contracted with c0,c1. Its conjugate needs the **4x4x6** tensor from H1(TX*)_1 x H1(TX*)_2 x H1(TX*)_0, contracted with beta0,beta1. The doublet/neutral charged Hessian needs the symmetric invariant-character **9x9x9 L^3** tensor and **6x6x6 B^3** tensor in these exact bases (or a verified invertible basis conversion from external data). The four known bundle-neutral tensors also induce neutral/charged mixing through the Higgs VEV; those blocks alone cannot determine the full exotic rank. Colored neutral-pair tensors, possible geometric-neutral pair tensors, the Higgs-eaten directions and all additional bilinear/background contributions must be included where nonzero. Merely counting the gauge-allowed maximal 4,4,6 pairing ranks would not establish their achievement.

This result clears a concrete simultaneous **known-cubic/positive-quadratic-metric** consistency gate. It does not stabilize moduli, prove nonlinear bundle unobstructedness, remove all exotics, derive thresholds, or predict alpha. Clock, knot, partition and prime connections remain unresolved physical maps and were not used as targets.

## 6. Reproducibility

`calculate.py` was frozen in `source-manifest.json` before its first calculation. It reads the actual tensor and validates every predecessor artifact-manifest hash plus the accepted native-replay log/status (exit zero; log SHA256 79c522b9981e2c3a6f7c8588ef9ef6241eb61492d61c2ad6842bf236743aa866). It does not rerun the expensive chain derivation or pretend that checking its frozen receipt is a new chain calculation. Polynomial-zero data are inherited explicitly from their saved certificate; the historical preliminary d3 discussion in that predecessor is superseded by d2/d4, not used as an input.

Run `C:/Python313/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/tian-yau-flavor-higgs-consistency-gate/verify.py`. Default replay requires the saved certificate and never regenerates it. Creation was exclusive. `release-manifest.json` freezes this report, source manifest, scripts and certificate. `native-replay.log` and `native-replay-status.json` record the independent completed replay. Local exact SymPy verification only; no Lean/kernel/hosted-CI/peer-review claim and no publication.

Only this lane was written. As in the documented predecessor tooling issue, the file-writing tool initially placed source files in the Cygwin shadow tree despite a canonical-looking path; they were copied to the native canonical lane and executed with C:/Python313/python.exe. A failed pre-freeze native existence check is an operational path issue, not a failed mathematical calculation.
