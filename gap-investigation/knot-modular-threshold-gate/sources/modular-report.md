# E7 modular-completion gate

## Outcome: a missing mathematical sector is actually completed

The single E7 vacuum character is replaced by a complete **two-sector modular character vector**, and two explicit completions pass exact checks:

1. The nonchiral torus partition function `Z7=|chi0|^2+|chi1|^2` is invariant under both modular generators.
2. The chiral extension `chiE8=chi7,0 chiA1,0+chi7,1 chiA1,1` closes to the even unimodular E8 lattice. Its S eigenvalue is 1 and its T eigenvalue is `exp(-2pi i/3)`, not 1. Its absolute square is modular invariant.

This closes the previous **missing-sector/worldsheet modular-completion gate**, not compactification to a stable, anomaly-free four-dimensional string vacuum. Neither a single holomorphic E7 character nor the holomorphic c=8 E8 character is an invariant scalar torus partition function by itself. The latter still has the central-charge T multiplier.

## 1. Conventions and discriminant quadratic form

Use Euclidean roots of squared length 2, `q=exp(2pi i tau)` and `e(x)=exp(2pi i x)`. E8 in doubled coordinates is the set of integer vectors with uniform parity and coordinate sum divisible by four. The actual coordinate is half the listed integer. Let `alpha=e7+e8`, with norm 2; `L=E8 intersect alpha-perp` is E7. The seven simple roots reused from `connections/partitions/exact_certificate.py` have exact Gram determinant 2. Thus `D=L*/L` has order two.

Choose an E8 root r with `(r,alpha)=1`. Then `lambda=r-alpha/2` is orthogonal to alpha, belongs to L*, has squared norm 3/2, and is not in the even lattice L. The certificate's explicit example is `lambda=(-1,0,0,0,0,0,-1/2,1/2)`. It checks integrality of its pairings against every simple root, and membership of `2lambda` in the ambient perpendicular lattice. Consequently the nonzero class generates D=Z/2.

The discriminant form is

`Q(0)=0, Q(1)=lambda^2/2=3/4 mod 1`,

`B(x,y)=Q(x+y)-Q(x)-Q(y)=xy/2 mod 1`.

Its nontrivial topological twist is `e(3/4)=-i`: the anti-semion convention. The normalized Gauss sum is `(1-i)/sqrt(2)=e(7/8)`, recording signature 7 modulo 8. It is not a four-dimensional chiral-fermion index. Exact Verlinde evaluation recovers `1 fusion 1=0`, the Z2 fusion law, rather than the ordinary finite-dimensional `56 tensor 56` decomposition.

## 2. Deriving S and T, including all central phases

For the theta vector `Theta_a=sum_(v in L+a) q^(v^2/2)`, Poisson summation gives

`Theta_a(-1/tau)=(-i tau)^(7/2) /sqrt(2) * sum_b e(-B(a,b)) Theta_b(tau)`.

The conventional metaplectic Weil matrix instead uses `tau^(7/2)` and includes the factor `e(-7/8)` in its S matrix. These are the same transformation, not conflicting S conventions. See the arbitrary-signature Weil formula in [3], section 2. Odd rank requires this metaplectic care; an even-rank-only SL2 statement must not be applied blindly.

Set `chi_a=Theta_a/eta^7`. The identities `eta(-1/tau)=(-i tau)^(1/2) eta(tau)` and `eta(tau+1)=e(1/24)eta(tau)` cancel the theta S weight and introduce the T vacuum phase. In basis `(0,1)`:

```
S = 1/sqrt(2) [[1, 1], [1, -1]],
T = e(-7/24) diag(1, e(3/4))
  = diag(e(-7/24), e(11/24)).
```

Here `c=7`, `h0=0`, `h1=3/4`; the T exponents are `h-c/24`. Charge conjugation is the identity since both discriminant classes are self-inverse. Exact algebra gives `S^2=C=I`, `(ST)^3=C=I`, and unitary S,T.

The topological matrix `Ttop=diag(1,-i)` omits the vacuum energy. Then `(S Ttop)^3=e(7/8)I`, **not I**. Multiplying Ttop by `e(-7/24)` cancels this phase on cubing. This is an executed wrong-phase negative control, not a floating-point comparison.

`exact_certificate.py` implements rational coefficient vectors in `Q[z]/(z^8-z^4+1)`, with `z=e(1/24)`. Multiplication reduces by the cyclotomic polynomial Phi24. `sqrt(2)=z^3+z^-3` and `1/sqrt(2)=sqrt(2)/2`. Every reported matrix equality is coefficient-by-coefficient exact Fraction equality. This also supplies a provable algebraic interpretation: equality in the quotient evaluates to equality at the specified primitive root; no tolerance or rounded trigonometric values enter.

## 3. Diagonal nonchiral completion and missing-sector rejection

With independent left and right character spaces, `M=I` yields

`Z7(tau,bar(tau))=chi0(tau) bar(chi0(tau))+chi1(tau) bar(chi1(tau))`.

The certificate checks `S^dagger M S=M` and `T^dagger M T=M`. Thus `cL=cR=7` and the torus amplitude has no left-minus-right central-charge anomaly. This is a standard nonchiral rational lattice CFT, not a spacetime compactification specification.

Uniqueness has a limited but exact scope: among constant two-by-two coefficient matrices with this left/right character vector, T has two distinct eigenvalues, so commuting with T forces off-diagonal entries to vanish. Commuting with S then forces the two diagonal entries equal. With vacuum multiplicity `M00=1`, M=I. This does not classify completions with extra sectors, extensions, other chiral algebras or string projections.

Omitting the nontrivial sector means `M=diag(1,0)`. Under S it becomes `1/2 [[1,1],[1,1]]`, which is unequal to M. An off-diagonal pairing fails T invariance. Both failures are executed. The missing sector is necessary for this completion; it is not an optional correction fitted to a numerical target.

## 4. E7 x A1 gluing really yields E8

For `K=A1=Z alpha`, the nontrivial dual class `mu=alpha/2` has norm 1/2 and `QA(1)=1/4`. The product discriminant form is

`Qproduct(x,y)=(3x+y)/4 mod 1` on `(Z/2)^2`.

Its unique nonzero isotropic element is `(1,1)`. Hence `H={(0,0),(1,1)}` is isotropic, with `H-perp=H`. The corresponding even extension is

`Lglue=(L direct-sum K) union ((lambda+L) direct-sum (mu+K))`.

It has index 2 over `L direct-sum K`, and determinant `2*2 / 2^2=1`. More than this arithmetic is checked: adjoining the explicit E8 root r to the seven E7 simple roots gives an **integral, even Gram matrix with determinant 1**. All generators lie in the coordinate E8 lattice. That coordinate lattice is `D8 union (s+D8)` where D8 has index 2 in Z8 and the half-integer extension has index 2 over D8, so its covolume is 1. An included determinant-one rank-eight sublattice therefore equals coordinate E8. This proves the infinite lattice identification by inclusion and equal covolume; low shell agreement is an independent bounded check, not the whole argument.

The exact product-sector matrices are `S7 tensor SA` and `T7 tensor TA`, with `SA=S7`, `TA=diag(e(-1/24),e(5/24))`. In product order `(00,01,10,11)`, the extension coefficient vector is `v=(1,0,0,1)`. It obeys

`(S7 tensor SA)v=v`, `(T7 tensor TA)v=e(-1/3)v`.

Dropping its 11 component fails S covariance. Gluing two same-sign E7 nonzero classes instead gives `3/4+3/4=1/2 mod 1`, so that diagonal glue is not even: the complementary A1 form matters.

### Exact shells and characters

All E8 points of norm at most 4 are enumerated by an integer-square-budget recursion. E7 is the perpendicular slice. Fixing `(r,alpha)=1` and projecting gives precisely the E7 nontrivial coset shells through norm 7/2: projection and addition of alpha/2 are inverse maps on those shells. Colored oscillator partitions are generated independently by finite products.

| Object | Shifted initial coefficients |
|---|---|
| Theta E7 | `1+126q+756q^2` |
| Theta nontrivial E7 coset | `q^(3/4)(56+576q+...)` |
| chi7,0 | `q^(-7/24)(1+133q+1673q^2+...)` |
| chi7,1 | `q^(11/24)(56+968q+...)` |
| chiA1,0 | `q^(-1/24)(1+3q+4q^2+...)` |
| chiA1,1 | `q^(5/24)(2+2q+...)` |
| Theta E8 | `1+240q+2160q^2` |
| chiE8 | `q^(-1/3)(1+248q+4124q^2+...)` |

The E8 roots split by alpha inner product as `1,56,126,56,1` at `-2,-1,0,1,2`. Equivalently `240=126+2+56*2`. The affine-current count is `248=133+3+56*2`. Without glue the product vacuum character has shifted coefficients `1,136,2076`; adding the coset product supplies `112q+2048q^2`, yielding `1,248,4124`. This is an exact lattice/oscillator calculation; representation dimensions alone were not used to infer the branching.

## 5. What the completion selects—and what it does not

| Proposed arrow | Result and missing input |
|---|---|
| det(E7)=2 -> two sectors | Derived from the lattice discriminant group and sourced affine/lattice correspondence. |
| sectors -> modular consistent worldsheet block | Constructed and checked exactly, including nonchiral and E8 extensions. |
| 133 -> four spacetime dimensions | Unsupported. 133 counts 126 root currents plus seven Cartan oscillators. It is not the number of spacetime coordinates. |
| worldsheet chiral block -> physical Weyl chirality | No map constructed. Complex conjugation gives an equally consistent reversed modular representation; the diagonal partition function is left-right symmetric. An internal Dirac operator, bundle and projections are still needed. |
| 56 states / two primaries -> family count | No. These are a ground representation degeneracy and a sector count, not net spacetime zero modes. No family index was calculated. |
| partition congruences -> prime physical scale | No Hamiltonian normalization, mass map or scale-selection dynamics is supplied by S/T. Modular degree/degeneracy information alone is dimensionless. |
| E8 glue -> full string vacuum | No. It repairs an internal chiral lattice sector, not criticality, GSO/BRST consistency, ghosts, tadpoles, spacetime anomalies or stabilization. |

The certificate checks both the conjugate modular representation and a tensor-product representation. Thus generator relations alone do not choose worldsheet orientation or forbid consistent additional spectator blocks. This is a limited algebraic non-selection test, not a universal theorem that every string completion permits arbitrary spectra. The sourced six-dimensional heterotic K3 E7 example in the predecessor partitions report already defeats selection of four dimensions from E7 symmetry alone. The Dirac predecessor correctly requires geometry, orientation, bundle/flux and index data; none of those can be reconstructed from this two-component character vector.

Knot-lane corroboration is used only within its scope: Mukhi–Poddar support the E7 level-one data, while the Ramanujan/CS eta-product example arXiv:2408.07893 concerns G2 in its exceptional section, not E7. No prime or determinant-sign chirality rule was imported into this completion.

## 6. Genuine Lean boundary and reproducibility

`Formalization.lean` constructs explicit Bit and Z4 inductive types and their addition tables using recursors. It proves, for all elements in their declared finite domains, E7/A1 quadratic polarization, diagonal isotropy, the converse that any isotropic product vector has equal components, and non-isotropy of the E7 nonzero class. These are kernel proof terms, with no assumed polarization or isotropy hypotheses and no axiom/sorry/unsafe escape. All five printed theorem dependencies are empty. The conditional converse actually eliminates the impossible off-diagonal cases using distinct constructors; it does not simply rename the desired conclusion as an assumption.

`Challenge.lean` imports the compiled formalization and exposes the checked public types. This minimal Lean installation lacks Init/Mathlib; no full matrix/complex/Poisson theorem is claimed. The five declarations constitute one finite discriminant-form contribution, not five independent advances in physical validity.

Run from this directory with Python and the adjacent Lean installation:

```
python -B exact_certificate.py --verify
python -B verify.py --verify
```

The first compares the existing deterministic certificate against recomputation, including source hashes. The second compiles Lean, checks axiom reports and public types, replays the existing certificate without overwriting it, validates saved source excerpts, and compares the existing verification receipt. Initial receipt creation uses the corresponding commands without `--verify`. Missing receipts fail; the verifier does not regenerate one to conceal its absence. Hosted CI was not run. Native paths are authoritative: file-tool Cygwin shadow writes were detected and copied into this lane before execution.

## 7. Primary-source closure ledger

[1] I. B. Frenkel, *Representations of Kac-Moody Algebras and Dual Resonance Models*, Lectures in Applied Mathematics 21 (1985), pp. 325–353. Author-hosted full text: https://bpb-us-w2.wpmucdn.com/campuspress.yale.edu/dist/2/3739/files/2021/06/frenkel_representations_kac_moody.pdf . Proposition 1.3 (p.332) gives the level-one lattice-coset/oscillator character; Theorem 2.2 (p.334) identifies root-lattice vertex realizations and coset fundamental modules; equation (2.10) and the following sentence (p.335) give free-boson central charge equal to rank. This is a primary-author exposition of the construction, citing original Frenkel–Kac (1980); we retrieved this full text, not the original 1980 paper. It closes the lattice/affine-character citation gap.

[2] S. Mukhi and R. Poddar, *Universal Correlators and Novel Cosets in 2d RCFT*, https://arxiv.org/pdf/2011.09487 . Section 3.1 (pp.9–10) explicitly says E7,1 has c=7, h=3/4, and the 56 is its only nontrivial primary. The paper distinguishes ordinary tensor-product channels from affine primaries and discusses the A1/E7 pair. Its novel correlator conjectures are not promoted to proved input here; our E8 character identity is independently obtained from lattice gluing.

[3] M. Schwagenscheidt and B. Williams, *Binary theta functions and Borcherds products*, https://btw-47.github.io/binarytheta_paper3.pdf , section 2. Gives the arbitrary-signature discriminant quadratic module and explicit metaplectic Weil S/T phases. Unlike an even-rank-only SL2 formula, this covers the convention required for odd-rank E7. Poisson/eta analytic transformation laws remain external standard mathematics.

[4] K. Lee, K. Sun and H. Wang, *On intermediate Lie algebra E7+1/2*, Letters in Mathematical Physics 114:13 (2024), https://bimsa.net/doc/publication/5729.pdf , DOI 10.1007/s11005-023-01762-z. Page 3 states h-dual(E7)=18 and equation (1.6) gives `c=k dim(g)/(k+h-dual)`. Applied to the ordinary simple E7 algebra at k=1, this gives c=7. The paper's conjectures about its intermediate E7+1/2 algebra are irrelevant to—and are not assumed in—this E7 calculation. This is primary research quoting established Sugawara/WZW background, not the original Sugawara proof.

Complete retrieved texts are in `sources/`; `source_evidence.json` retains verbatim supporting excerpts and hashes. Broken PDF typography is not silently treated as a new theorem: exact conventions and formulas are written out above and independently evaluated. These source closures remove the predecessor's unsupported-citation labels for this mathematical building block; they do not add empirical support to the alpha hypothesis.
