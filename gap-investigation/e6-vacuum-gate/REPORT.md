# Nonsupersymmetric E6 stable-vacuum gate

## Outcome

**The specified alignment cannot be an isolated tree-level minimum modulo gauge for an ordinary renormalizable potential with two complex 27(-2) fields and one real 78(0): at least eleven physical adjoint modes are exactly flat.** This is not a tachyon no-go. An explicit positive renormalizable potential realizes the alignment as a degenerate global minimum, and the full 186-real-field Hessian has 109 positive, 77 zero, and no negative directions; only 66 zero directions are gauge Goldstones.

**An explicitly engineered gauge-invariant polynomial EFT does remove precisely those eleven flats.** Adding a spectral sum of squares through operator dimension 16 gives a full Hessian with 120 positive, 66 gauge-zero, and no negative or physical-zero directions. This establishes a strict local minimum modulo the E6 gauge orbit of that *chosen classical potential*. It does not establish a natural renormalizable model, a UV completion, radiative stability, or a prediction for alpha. Spectral coefficients were chosen to accommodate the intended symmetry-breaking pattern; no numerical electromagnetic target appears.

The new fields are independent nonsupersymmetric boundary-sector action choices. Their X=-2 charges allow the earlier FFH Yukawa channel, and bosonic fields introduce no new chiral fermion anomaly. The Green–Schwarz sector remains only conditionally locally repaired, not globally completed.

## 1. Actual representation, field space, and invariant interactions

Write h1,h2 in the unitary minuscule 27 and A=A^a T_a as a Hermitian 27-by-27 matrix in the real compact adjoint subspace. The scalar field space is **108+78=186 real dimensions**, not its SM-singlet restriction. Use positive kinetic forms sum_i |D h_i|² and a positive multiple of Tr27(D A)². The integer Chevalley-derived basis is not orthonormal, but nonsingular positive changes of field metric preserve Hessian inertia.

Under E6 x U1X,

```
h_i -> exp(-2 i lambda) U h_i,
A   -> U A U†.
```

Consequently h_i†h_j, Tr A^n, h_i†A h_j, and h_i†A²h_j are actual gauge-invariant contractions. The cubic d(h_i,h_j,h_k), and any A hhh term, carry X=-6 and are forbidden in the ordinary polynomial potential. A massive X vector does not remove this charge constraint.

We independently construct simple-root raising matrices from the predecessor's full 27-weight orbit: (E_i)_(w+alpha_i,w)=1 for each allowed transition; F_i=E_i^T and H_i=diag(w_i). **102 exact Chevalley/Serre checks** validate these signs and relations. Commutators generate all 36 positive-root matrices; their Hermitian real/imaginary combinations and six H_i give 78 linearly independent generators. This goes beyond testing only whether root transitions exist. No desired weight vector is inserted into a purported invariant tensor.

Primary source [1], equation (48), supplies the mixed tensor

```
H_ab = {T_a,T_b} - (2/9) delta_ab 1_27
```

in its Tr(T_a T_b)=3 delta_ab convention. Its contraction with A^a A^b h_i† ... h_j spans h_i†A²h_j and I2 h_i†h_j, where I2=Tr A². Appendix A, printed p.12 / PDF p.13, lists these two mixed quartics and h_i†A h_j. Flavor indices can be arbitrary; they do not introduce new E6 tensor structures. The pure-h potential below is left completely general, including flavor-sensitive d-dbar contractions. Completeness of the mixed tensor list is an external representation-theoretic/source premise, not a Lean theorem.

The exact code solves *all* homogeneous simple-Weyl-reflection constraints in six Cartan variables and finds invariant dimensions (degree 2,3,4)=(1,0,1). By conjugacy into a Cartan, this excludes an independent single-adjoint cubic or quartic. It also checks every coefficient of

```
Tr27 A³ = 0,
12 Tr27 A⁴ = (Tr27 A²)².
```

Thus the apparently different single-field adjoint quartics in [1] are not independent here. Some other displayed source formulas contain typographical inconsistencies (e.g. repeated delta contractions); we do not use them as independent invariants.

## 2. General renormalizable obstruction — full Hessian, not radial-only

The A-dependent part of the most general ordinary polynomial potential in this field content can therefore be written

```
Vren = V27(h1,h2) + mA² I2 + lambdaA I2²
     + sum_ij [ mu_ij h_i† A h_j
               + eta_ij I2 h_i†h_j
               + kappa_ij h_i† A² h_j ].
```

Coefficient matrices obey the Hermiticity conditions making V real. This is a nonsupersymmetric potential: no F- or D-flatness condition is imposed. We neither transfer the old SUSY lock nor import an E6-only cubic prohibited by X.

Let h1=v1 s0, h2=v2 s1, v1 v2 nonzero, with the predecessor's distinct conventional SU5-singlet directions, and let A0=aY with a nonzero. Every B in su5 annihilates both h_i. In particular A0 h_i=0. Holding h_i fixed and restricting A to su5 gives exactly

```
V|su5 = C0 + C2 Tr A² + lambdaA (Tr A²)².
```

If the *full* alignment is stationary, its nonzero radial adjoint equation forces C2+2 lambdaA I2(A0)=0. For each B in su5 satisfying Tr(A0 B)=0, the full Hessian annihilates (delta h1,delta h2,delta A)=(0,0,B):

* pure-adjoint/norm terms vanish by that radial equation and orthogonality;
* the h-A cross derivatives of h_i†A h_j vanish because B h_i=0;
* those of h_i†A²h_j vanish because A0 h_i=B h_i=0;
* derivatives of I2 h_i†h_j vanish because Tr(A0 B)=0;
* V27 has no A derivative.

This is a **23-dimensional kernel of the full Hessian**, not merely zero curvature of a restricted block with unchecked off-diagonal mixing. At the target, the SU5 orbit SU5/(SU3 x SU2 x U1) is 12-dimensional. It accounts for 12 of these zero modes, leaving the eleven physical modes transforming as (8,1)_0+(1,3)_0. They commute with Y and cannot be gauge tangent directions [T,Y]. For example B=H1 has Tr(A0 B)=0 and is explicitly checked as a physical flat direction.

The fixed-I2 sphere in su5 is a genuine constant-energy family. Changing its adjoint eigenvalues is not a gauge transformation. Thus neither an isolated minimum modulo gauge nor eleven positive physical masses can be obtained at this exact pure-Y alignment from the stated renormalizable action, irrespective of V27. A non-isolated nonnegative minimum remains possible. Additional adjoint-singlet components, extra representations, nonpolynomial axion dressings, higher operators, or a quantum effective potential are outside this obstruction.

## 3. Explicit renormalizable positive example

Choose an arbitrary mass unit M>0 and target

```
h1,0=M s0,  h2,0=M s1,  A0=6 M Y,
Tr27 A0²=180 M².
```

The factor six clears conventional hypercharge denominators; it is not a measured scale or coupling. Take

```
V0 = (h1†h1-M²)² + (h2†h2-M²)²
   + |h1†h2|²
   + (Tr A²-180 M²)²
   + |A h1|² + |A h2|².
```

Every term is a genuine invariant of operator dimension at most four. All squares vanish at the target, so V0>=0 proves global minimality and exact stationarity on the *full* field space. Strictly positive independent coefficients in front of these squares preserve the following kernel. We do not claim this is the most general potential, or that its omitted couplings are symmetry-enforced.

At a common zero of real residuals F, Hess(V0)=2 J^T J, with complex residuals resolved into real and imaginary parts. Exact rational row elimination of the complete Jacobian gives rank 109. Thus its full Hessian inertia is **(positive,zero,negative)=(109,77,0)**. The actual gauge-tangent map (iT h1,iT h2,i[T,A0]) has rank 66, agreeing with stabilizer dimension 12. There are exactly eleven non-gauge zero modes. This example saturates the obstruction rather than disproving it.

Negative control: reverse the coefficient of |A h1|². A perturbation in the first nonzero-Y weight of h1, with A and h2 fixed, has all other residual derivatives zero. The Hessian quadratic form is exactly **-32** in the M=1 coordinate convention. This is a genuine tachyonic stationary counterexample, not a Boolean label called stability.

## 4. Engineered dimension-16 EFT that lifts all physical flats

The exact eigenvalues of A0/M in the 27, computed from all weights, are

```
r = -4,-3,-2,0,1,2,3,6
multiplicities = 3,4,3,2,6,6,2,1.
```

Define a matrix polynomial using only scalar coefficients and the identity,

```
p_M(z) = (z+4M)(z+3M)(z+2M) z (z-M)(z-2M)(z-3M)(z-6M),
VEFT = V0 + (etaP/Lambda^12) Tr27[p_M(A)† p_M(A)],
etaP>0, Lambda finite and much larger than 6M.
```

This is not a penalty involving a fixed basis vector or a matrix A0. For every U,
p_M(U A U†)=U p_M(A) U†. Therefore its trace norm is gauge invariant on all field configurations. Nevertheless its **scalar polynomial roots are deliberately engineered from the desired breaking pattern**, which is a tuning/input, not an independently selected vacuum. The operator has highest dimension **16**, not four. Expansion gives correlated operators up through dimension 16 with powers of M; the cutoff suppression is Lambda^-12. Lower-dimensional pieces in this expression must also be retained. Arbitrary omission of these pieces invalidates the zero-residual construction.

Since p_M(A0)=0, the target remains a common zero of all squares and hence a global minimum of this exact polynomial. The global statement is algebraic; an EFT is not asserted reliable at arbitrarily large fields. For local stability, diagonalize A0. The matrix Frechet derivative has entries

```
Dp_A0[B]_ij = p_M'(a_i) B_ij                    if a_i=a_j,
           = (p_M(a_i)-p_M(a_j))/(a_i-a_j) B_ij if a_i!=a_j.
```

The second case is zero. The first has nonzero coefficient at every eigenvalue because all eight roots are simple. At M=1, the code obtains p' values (-16800,3240,-1920,864,-600,960,-3780,259200), in the stated order. Hence this positive term penalizes every adjoint perturbation commuting with A0 while leaving conjugation directions unpenalized. This is a covariant spectral constraint, not merely fixing I2.

We append these derivative rows to the full V0 Jacobian. Nonzero p' factors and positive etaP/Lambda^12 may be divided from rows **for exact rank/kernel only**, not to claim numerical mass eigenvalues. Result: **rank 120 in all 186 real fields**. We independently express every gauge tangent in the same nonorthogonal 78-coordinate basis using the exact trace Gram matrix, reconstruct its matrix, and check J*g=0 for all 78 generators. Their rank is 66, exactly the Hessian nullity. Therefore

| Potential | Positive | Gauge zero | Physical zero | Negative |
|---|---:|---:|---:|---:|
| V0 | 109 | 66 | 11 | 0 |
| VEFT | 120 | 66 | 0 | 0 |

Positivity on a transverse slice to the compact gauge orbit gives a strict local minimum modulo gauge. This is a full-field classical certificate, not a radial or SM-singlet-only scan. Removing the spectral term restores exactly eleven physical flats, an executed flat negative control.

The formerly flat masses scale parametrically as etaP M^14/Lambda^12 times representation-dependent constants. For M/Lambda small they are very small. Generic allowed radiative corrections can therefore dominate this lifting. No symmetry protecting the correlated polynomial coefficients, loop-corrected Hessian, natural hierarchy, UV origin, or cosmological selection has been supplied. Other disconnected zero-energy orbits are not classified. This construction establishes bounded **engineered EFT existence**, not a natural or unique model.

## 5. External X and the previous Green–Schwarz boundary

The polynomial is invariant under X=-2 on both h_i and X=0 on A. On the target the external X tangent equals the E6 Cartan tangent generated by -2H6, since both singlets have sixth Dynkin label +1 and [H6,Y]=0. Thus gauging X alone does not add an independent scalar-orbit direction; without the separate Stückelberg action an extra abelian combination is unbroken. The SM stabilizer statement is inside E6.

Conditionally adding the previously described healthy nonzero-charge Stückelberg phase introduces one scalar coordinate and one independent gauge tangent. It does not add a physical massless scalar or change the 120 physical scalar directions here. The axion is still eaten, not a varying-alpha scalar. Its global quantization/bundle issues are untouched; this lane does not promote the local anomaly repair to a complete quantum theory. Bosonic scalar charges must also descend to the boundary quotient; 27(-2) is congruent to 27(+1) modulo the shared Z3 and passes that elementary representation descent condition, not the global anomaly problem.

## 6. Source recovery and exact evidence

[1] Thomas Deppisch, *E6Tensors: A Mathematica Package for E6 Tensors*, https://arxiv.org/pdf/1605.05920 (v1, 15 PDF pages). **Original PDF downloaded and parsed.** Equation (48), PDF p.8, and Appendix A, PDF p.13, provide the mixed invariants used here; eqs.(30)-(34) give transformations/products. SHA256 and page-labelled extraction are retained under `sources/`. Our integer representation construction is independent of its Mathematica implementation; we do not claim to have run Mathematica.

[2] O.K. Kalashnikov and S.E. Konshtein, *Hierarchy of interactions and mass relations in asymptotically free E6 model of unified interactions*, Nucl.Phys.B166 (1980) 507–524, **DOI exactly 10.1016/0550-3213(80)90210-2**, report LEBEDEV-79-67. Publisher preview and INSPIRE record 141557 confirm metadata. Full article remains unrecovered: direct publisher response is a Cloudflare error; Wayback returned a 429 body; archive.ph returned a CAPTCHA. No inequalities or full-Hessian result from this paper are imported. The abstract's historical mass claims are not used as evidence of our vacuum.

[3] Kephart–Vaughn, *Tensor Methods for the Exceptional Group E6*, DOI 10.1016/0003-4916(83)90176-8, INSPIRE 167756. Its actual linked KEK scan endpoint returned HTTP 200 with a 188-byte **Request Rejected HTML**, not a PDF. This was detected and retained as a failure, not reported as recovery. Source [1] explicitly develops this tensor method and supplies accessible primary formulas.

`checks.py` replays the predecessor's exact receipt before construction, never modifies the predecessor, and recomputes all finite checks. `receipt.json` is exclusive-created, then compared against the complete recomputed payload including source hashes. An initial smaller development receipt is preserved separately. `test_vacuum.py` exercises full-field inertia, the renormalizable flat obstruction, tachyon sign, invariant dimensions, EFT dimension, X tangent, and missing/tampered receipts/source hashes. `run_checks.py` records real subprocess outputs and hashes in `verification.json`. The native executable and dependency versions are disclosed there; NumPy is used for small integer matrices, Fraction for rank, with no floating eigenvalue tolerances.

Run from native Windows Python with NumPy available:

```
python -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/e6-vacuum-gate/run_checks.py
```

No Lean/Mathlib theorem, hosted CI, expert review, publication, full physical completion, threshold calculation, or absolute-alpha prediction is claimed. The proof boundary is explicit representation theory and source completeness plus exact finite Python linear algebra and the analytic sum-of-squares argument. File-tool shadow-path behavior was corrected by copying only this lane into its verified native canonical directory. No other lane was edited.
