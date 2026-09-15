# Knot/modular-to-gauge-threshold gate

## Result

There is a precise but narrow bridge:

`E7_1 WZW modular tensor data -> E7_1 Chern–Simons framed link amplitudes`,

and, separately,

`charge-refined full worldsheet trace -> heterotic E7 gauge threshold`.

The first arrow is exact. The second requires far more data than the first. The finite E7_1 modular/link data does **not** determine the charge-inserted threshold trace or its continuous compactification-modulus dependence. This is a scoped non-identifiability result, not a universal claim that no richer knot/CFT construction could encode a spectrum.

## Exact E7 level-one observables

Use the verified character matrices in basis `(0,56)`:

```
S = 1/sqrt(2) [[1,1],[1,-1]],
T = diag(exp(-7 pi i/12), exp(11 pi i/12)).
```

Thus the topological twists are `theta_a=T_aa/T_00=(1,-i)`, quantum dimensions are `d_a=S_0a/S_00=(1,1)`, total quantum dimension is `D=1/S_00=sqrt(2)`, and Verlinde fusion is `1 x 1=0`. Mukhi–Poddar identify `c=7`, `h_56=3/4`, and the 56 as the only nontrivial affine primary.[3]

With Witten's surgery normalization `Z(S3)=S00`, `Z(S3; unknot_a)=S0a`, so the normalized zero-framed unknot is `d_a`. The normalized Hopf link is `S_ab/S00`, hence exactly

```
H = [[1,1],[1,-1]].
```

A framing shift by `f` multiplies color `1` by `theta_1^f=(-i)^f`; color `0` is unchanged. Witten gives both the unknot/surgery relation and the conformal-weight framing phase.[1] The certificate verifies all values in `Q(zeta_24)`, not floating point.

What survives is only the two labels, Z2 fusion parity, quantum dimensions, mutual Hopf phases, and topological spins/central framing phase. In particular the 56-dimensional affine ground degeneracy is **not** the quantum dimension: the colored unknot is 1, not 56. The real Hopf matrix is unchanged under mirror conjugation, while a singly framed nontrivial unknot changes `-i` to `+i`; therefore even mirror sensitivity depends on the framed observable. None of these quantities is a spacetime Weyl index.

## Charge insertion is additional information

The threshold integrand contains `Q_E7^2` (with its modular contact subtraction), not merely an uncharged character or a topological line label. Kim's formula (3.70–3.71) displays this general charge-inserted trace.[4] In the explicit N=2 heterotic example, Angelantonj–Israël–Sarkis define the E7 integrand by inserting `Q_E7^2-1/(8 pi tau_2)` into the new supersymmetric index, and then integrate over the modular fundamental domain.[5, eqs. 4.20–4.24]

A constructive spectrum constraint does survive if one adds the continuous Cartan refinement `chi_a(tau,z)=Tr_a(q^(L0-c/24) exp(2 pi i z H))`: its second derivative at `z=0` is the charge-squared trace. For the explicit norm-two E7 Cartan vector used by the certificate, Weyl-shell isotropy gives

`sum_{lambda in shell} (lambda,H)^2 = (2/7) |shell| lambda^2`.

Exact shell results are:

| sector | norm squared | degeneracy | charge-square trace |
|---|---:|---:|---:|
| 0 | 2 | 126 | 72 |
| 0 | 4 | 756 | 864 |
| 1 | 3/2 | 56 | 24 |
| 1 | 7/2 | 576 | 576 |

After neutral oscillator dressing the first charge-character coefficients are `K0=q^(-7/24)(72q+1368q^2+...)` and `K1=q^(11/24)(24+744q+...)`. Independently, the certificate checks through these orders the affine Ward/Jacobi identity

`K_a = (4/7) D chi_a + (1/6) E2 chi_a`, `D=q d/dq`,

for `H^2=2`. This is a real invariant-to-spectrum constraint—but it requires the refined affine characters/current algebra. Plain `S,T`, unknot and Hopf data do not contain these shell moments, the right-moving spectrum, Narain momenta, spin signs, or compactification charges.

The “Ramanujan” identities actually used in the sourced threshold calculation are differential identities for Eisenstein series, e.g. `D E4=(E2 E4-E6)/3`, `D E6=(E2 E6-E4^2)/2`, plus `E4^3-E6^2=1728 eta^24`; the certificate checks their q-series through degree 40.[5, eqs. 4.22, 4.30] These are not Ramanujan partition congruences. Nimbers and Dedekind numbers do not enter. Dedekind eta does enter the oscillator characters and threshold integral; it is a different object.

## Physical equal-data/different-threshold test

Declared domain: the sourced four-dimensional **N=2 heterotic `K3 x T2` standard-embedding limit**, zero Wilson lines and trivial torus fibration (`n=24`), not the Tian–Yau N=1 Calabi–Yau model and not a claim about its threshold.

The source derives

`Lambda_E8-Lambda_E7 = -144 I_DKL(T,U)`,

where

`I_DKL=-log(4 pi exp(-gamma) T2 U2 |eta(T) eta(U)|^4)`.[5, eqs. 4.5, 4.32–4.33]

Hold the E7_1 gauge block—and therefore all `S,T`, fusion, unknot, Hopf and framing data—fixed, set `U=5i`, and vary `T=it` from `t=2` to `t=3`. The certificate uses the eta product and exact rational bounds (`pi<22/7`, a finite Taylor lower bound for `e^12`) to prove `d I_DKL(it,5i)/dt > 49/100` throughout this interval. Therefore

`I_DKL(3i,5i)-I_DKL(2i,5i) > 49/100`

and

`[Lambda_E8-Lambda_E7]_(3i)-[Lambda_E8-Lambda_E7]_(2i) < -1764/25`.

This is an explicit sourced physical family with identical finite knot/modular gauge data and provably different continuous gauge-threshold dependence. It establishes that no function of only those finite observables can reconstruct this threshold. The Lean theorem `fiber_target_obstruction` proves the abstract factorization obstruction, while a concrete two-state model and a recoverable-visible-coordinate control make it nonvacuous. The physical premises remain source/exact-certificate facts, not Lean-formalized string theory.

A useful negative control is the source's general prefactor `-6n`: at formal `n=0` the **difference** has no DKL dependence. This is an algebraic control only, not a claim that the same SU(2)-bundle physical model exists at that endpoint. The result is non-identifiability, not “moduli always vary every threshold.”

## Polynomial and chirality boundaries

The user's “Kaufman” is interpreted only as a spelling lead. **Kauffman bracket** is an unoriented diagram state sum whose writhe normalization gives Jones. **HOMFLY-PT** is a distinct oriented two-variable skein polynomial. The **two-variable Kauffman polynomial** is a third object, originally a regular-isotopy invariant for unoriented links; it is not HOMFLY-PT. Jones's survey explicitly presents HOMFLY-PT and the Kauffman bracket separately.[2] A direct Kauffman-author PDF was attempted but timed out and is not represented as read.[6]

No functor from knot mirror chirality to four-dimensional Weyl chirality is constructed or assumed. The Hopf matrix's mirror blindness is only a statement about this small family of observables, not about all E7 link invariants.

## Reproduction and boundary

Run in this directory:

```
C:/Python313/python.exe -B certificate.py --verify
C:/Python313/python.exe -B verify.py --verify
```

Python checks exact cyclotomic link arithmetic, finite lattice shells, charge refinements, modular q-series, and rational analytic bounds. Lean proves six declarations without axioms. No threshold integral for Tian–Yau, no alpha fit, no 133-dimension subtraction, no compactification spectrum reconstruction, and no knot/spacetime-chirality functor is claimed.

## Sources

[1] https://webhomes.maths.ed.ac.uk/~v1ranick/papers/witten.pdf — Witten, *Quantum Field Theory and the Jones Polynomial*
[2] https://math.berkeley.edu/~vfr/jones.pdf — Jones, *The Jones Polynomial*
[3] https://arxiv.org/pdf/2011.09487 — Mukhi and Poddar, *Universal Correlators and Novel Cosets in 2d RCFT*
[4] https://arxiv.org/pdf/2305.08263 — Kim, *On one-loop corrected dilaton action*
[5] https://arxiv.org/pdf/1611.09442 — Angelantonj, Israël and Sarkis, *Threshold corrections in heterotic flux compactifications*
[6] https://homepages.math.uic.edu/~kauffman/IRH.pdf — Kauffman, *An invariant of regular isotopy* (retrieval timed out; search metadata only)
