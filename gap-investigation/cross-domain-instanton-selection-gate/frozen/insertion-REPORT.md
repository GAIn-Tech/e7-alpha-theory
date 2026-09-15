# Instanton Higgs insertions: exact restriction and a nonzero transverse cubic jet

## Outcome and boundary

**The ordinary zero Pfaffian is not a zero charged-insertion polynomial.** On an explicit isolated `(1,0)` orbit, the first two actual dual Euler cocycles restrict as `(beta0,beta1)=(eta,0)`, with integral of eta equal to one in the declared Euler/dlog convention. The standard-embedding A-model divisor three-point function therefore gives the pure conjugate-matter contribution

`W_C^(B^3) = lambda_C q_C det(B0)`.

Here `lambda_C` includes the unspecified holomorphic vertex/field normalization, not a fitted number; `q_C=exp(-2pi T_x)` includes the actual complexified area. This is a **charged cubic correlator**, not the zero-field neutral Pfaffian. The source explicitly relates the divisor-degree cubic instanton coefficient to the heterotic matter superpotential.[1]

At `B0=u e23, B1=v e33`, this polynomial and every first derivative vanish, but its transverse Hessian does not. For an unrestricted matrix perturbation Delta of the effective B matrix,

`det(u e23 + epsilon Delta) = -u epsilon^2 (Delta11 Delta32-Delta12 Delta31) + epsilon^3 det(Delta)`.

For example the coefficient of `Delta11 Delta32` is `-lambda_C q_C u`. This is an actual nonzero transverse insertion coefficient up to the declared normalization, not a scalar mass or stability eigenvalue. In particular, a nonzero instanton insertion is compatible with zero cubic F terms on the common-column Higgs alignment.

**The full requested charged E8 Dirac/Pfaffian derivative gate remains open.** We construct the restricted cocycles, a finite neutral `End(TX|C)` lifting map, and a source-backed charged cubic jet. We do not equate that neutral map with the charged Higgs operator or invent a nonlinear E8 bundle family. Mixed insertions and higher charged orders have not been calculated. The first *established nonzero pure dual-matter interaction* is cubic; we do not promote this to a proved universal lowest order for every mixed charged/bundle interaction.

## 1. Recovered inputs and an actual curve orbit

All inputs are frozen under `frozen/`; `input-manifest.json` binds both their frozen bytes and canonical originals. The exact predecessor calculation was replayed in an owned temporary directory and compared with its existing saved receipt. Its original `--verify` writes before comparing, so it was **not** used as an immutable verifier. No predecessor file was changed.

Use `X={sum x_i^3=0, sum x_i y_i=0, sum y_i^3=0}` with weights `WX=(0,2,1,1)`, `WY=(0,1,2,2)`, and `w^2+w+1=0`. An actual orbit representative is

`x=(-s,s,-t,t), y=(-1,-1,1,1)`.

Its two other members are obtained by the actual diagonal coordinate action; their exact coordinates and predecessor labels are in `certificate.json`. They are different curves, with orbit length three. The code verifies all three defining equations and transports the restriction primitives equivariantly over `Q(w)`.

The original bounded search replays exactly: 81 `(1,0)`, 81 `(0,1)`, 567 isolated `(1,1)` cover curves, giving 27, 27 and 189 quotient orbits. All 729 line-pair bilinear ranks, including 162 rank-one exclusions, are recomputed. These are **not all total-degree-two maps**: `(2,0)`, `(0,2)`, multiple covers and boundary maps were not enumerated. The old phrase that this enumerates the whole degree-two sector must not be used for charged-insertion sums. The universal tangent zero-mode argument at zero charged fields is a separate statement.

For this isolated curve the normal bundle is `O(-1)^2`. The tangent extension splits since `H1(O(3))=0`:

`TX|C=O(2)+O(-1)+O(-1)`.

With spin bundle `O(-1)`, the rank-three complex operator has kernel `H0(O(1))=<1,z>` and cokernel `H1(O(-2))^2`, each of dimension two. Its dual spin-twisted bundle is `O(-3)+O(0)^2`, with two kernel modes. Thus the complexified `TX+TX*` sector contains four kernel modes. These counts do not count four-dimensional universal supersymmetry modes, and do not replace an E8 current-algebra vertex calculation.

## 2. Actual c0,c1 restrictions, not dimension-based guesses

The predecessor JSON cocycles are read and checked, including all sixteen product-chart terms:

`c0=x3^3 e_C0`, `c1=x2*x3^2 e_C0`.

On the displayed curve their normal representatives are `(t^3,0,0)` and `(-t^3,0,0)`. Let J be the restricted differential of the three defining equations on the ambient Euler middle term. The globally regular primitive for c0 is

`delta x=(0,0,t/6,t/6)`, `delta y=(0,0,1/6,-1/6)`.

Direct multiplication gives

`J(delta x,delta y)=(t^3,0,0)`.

The c1 primitive is its negative. In particular the correction in delta y is essential: omitting it leaves a nonzero bilinear-equation residual. Every orbit member is checked after pushing forward these primitives, not after assigning the restrictions zero. Adding the nonzero x-Euler field changes the primitive and leaves its J image unchanged. Therefore both actual classes have zero image in `H1(C,TX|C)`.

This is a restriction statement only. It does **not** set their E8-valued deformation representatives to zero globally, nor eliminate contact terms or second-order corrections after an exact first-order restriction has been gauged away. Restriction is not a substitute for a transferred nonlinear deformation differential.

## 3. Actual beta0,beta1 restrictions

The dual cocycles are the global terminal A* generators, precisely keys `(0,13)` and `(1,13)` with zero exponent, coefficient +1, on all sixteen charts. They are the two ambient dual Euler extension classes. Pulling back `O_x(1)` and `O_y(1)` to the curve gives degrees `(1,0)`. On the two P1 charts with `z=s/t`, their transition logarithmic derivatives are

`beta0 -> dz/z`, `beta1 -> 0`.

The declared trace convention is `Res(dz/z)=+1`; reversing the Euler connecting-map convention changes the corresponding field normalization coherently. Their image lies in `H1(O(-2))` inside `H1(TX*|C)`, not in `H1(End TX|C)`. Transporting around the orbit changes transition functions only by constant roots of unity and hence does not change dlog.

These are charged left-handed fields in the inherited `bar27`, with `B=(1,bar3,3)`; c carries `27` and `L=(1,3,bar3)`. The source uses the opposite overall names for 27 and bar27: its h11-associated 27 is **our beta-associated bar27**. We transfer the formula by cohomology sector, not by a lost conjugation bar.[1]

## 4. A finite zero-mode lifting map, with its exact domain

For a rank-three bundle-neutral deformation on the split curve, the only first-order harmonic components that can lift the two kernel modes into the two cokernel modes are

`Hom(O(2),O(-1))^2=O(-3)^2`.

Take actual Cech classes `a/z+b/z^2` and `c/z+d/z^2`. Multiply them by the kernel basis `1,z` and project to the `z^-1` harmonic coefficient of each `H1(O(-2))`. The resulting **computed** map and its determinant are

`M=[[a,b],[c,d]]`, `det M=a*d-b*c`.

Thus in this neutral restricted deformation space the determinant-line section begins at quadratic order, up to its nonzero-mode normalization. A single neutral insertion cannot saturate a two-dimensional kernel/cokernel pairing. Two independent insertions can. The certificate tests a nonzero determinant specialization and nonzero Cech boundary changes (`z^2` and `z^-3`) that must project away.

This is a constructive local neutral restriction result, **not** a computed restriction of all sixteen global bundle-neutral classes. Most importantly c0,c1 and beta0,beta1 are not parameters a,b,c,d. Charged fluctuations live in `(3,27)+(bar3,bar27)` of the E8 adjoint decomposition, whereas a rank-three End(TX) fluctuation lies in the structure-bundle adjoint. A numeric substitution of c/beta amplitudes into M would be an invented physical map.

A full charged computation needs the restricted E8/current-algebra vertices, their action on the full fermion sector, and the higher transferred terms after the c restrictions are removed by the explicit primitives above. Schematically the next operator involves a projected contact/second-order term and `P A1 h A1 P`; neither is supplied by a zero determinant. No value is assigned here.

## 5. Charged insertion polynomial and explicit transverse order

There is nevertheless a standard-embedding calculation that bypasses guessing that E8 Pfaffian: the A-model divisor three-point sector. The instanton part of the matter Yukawa is proportional to `n_d d_i d_j d_k q^d/(1-q^d)`, with the associated cubic matter superpotential.[1] For an isolated simple embedded `(-1,-1)` curve the local genus-zero contribution has unit complex-oriented multiplicity; we retain only the primitive single-cover term and leave string field normalization in lambda. The cubic divisor insertions saturate the primary three-point topological correlation; this is not a claim that zero-mode counting alone forbids every possible mixed two-point/contact amplitude.

The actual beta restrictions therefore yield the following polynomials in the two supported invariant flavors:

| curve class | pure B cubic polynomial, before its lambda and q |
|---|---|
| `(1,0)` | `det B0` |
| `(0,1)` | `det B1` |
| `(1,1)` | `det(B0+B1)` |

The determinant is the actual trinification singlet, not a determinant of the rank-three tangent Dirac matrix. Its polarization reproduces the divisor-degree flavor tensor. The selected `(1,0)` curve has only the `000` entry in this beta slice, with normalized value one. No absolute Pfaffian number is claimed.

For general degrees `dx,dy`, insert the inherited Higgs point in

`W_C^(B^3) / (lambda_C q_C) = det(dx B0+dy B1)`.

The effective background is `dx*u e23+dy*v e33`. Its exact Taylor polynomial in an arbitrary matrix Delta is

`epsilon^2 [-dx*u(Delta11 Delta32-Delta12 Delta31) + dy*v(Delta11 Delta22-Delta12 Delta21)] + epsilon^3 det Delta`.

There is no constant or linear term. The certificate differentiates with respect to all eighteen B0/B1 matrix entries before substitution. This supplies an explicit order statement: **the pure B cubic sector gives no tadpole at order Higgs-amplitude squared, but generally gives transverse quadratic terms of order Higgs amplitude**. It is not a proof that the full instanton F terms start at any particular higher order. Couplings involving other dual flavors have the same common-column zero-gradient protection at cubic order; colored cubic first derivatives vanish when colored fields are zero, but their mass tensors are not calculated here.

## 6. Orbit phases and sum boundaries

For these invariant L/B flavors the actual geometric character and the Wilson character are both zero. The transported beta restriction therefore has phase one on each orbit member. Exact arithmetic gives character sums `3,0,0` for characters `0,1,2`; the nontrivial-character controls detect an incorrect universal factor-three rule.

For the selected invariant cubic, a cover orbit sum is `3 lambda_C q_C det B0` in a cover normalization. The quotient has **one** curve, not three: the quotient projection/normalization removes that orbit multiplicity when using descended fields. We do not silently add a factor three to a downstairs coupling. Discrete B-field/torsion weights between distinct quotient curves and absolute field normalization are not fixed here.

An isolated curve contribution, its three-member cover orbit, the 27/27/189 bounded primitive orbit sets, all effective curves, and full W are different objects. A simple count does not fix arbitrary relative torsion/B weights, multiple covers, reducible curves, other bidegrees, mixed bundle insertions or the hidden-sector superpotential. No scalar stabilization or alpha prediction follows.

## 7. Reproduction and disclosure

Native canonical replay:

```
C:/Python313/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/tian-yau-instanton-higgs-insertion-gate/calculate.py
C:/Python313/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/tian-yau-instanton-higgs-insertion-gate/verify.py
```

Default replay requires the pre-existing certificate and compares its entire deterministic payload. `--create` is exclusive-only. The verifier binds release source hashes and tests missing/tampered certificates and mutated frozen inputs in disposable owned copies. No Lean theorem or peer review is claimed: this is exact Python/SymPy computation plus the explicitly cited physical A-model identification. The expensive predecessor Yoneda calculation is not rerun; its actual charged/dual cocycle bytes are pinned and checked. All predecessor edits/publication are excluded.

The filesystem tool initially delivered scripts to the known Cygwin shadow path despite reporting a native path. They were copied into the canonical native directory and executed there. The canonical frozen inputs and saved certificate, not shadow copies, are authoritative.

## Sources

[1] https://arxiv.org/html/2402.13563v1 — Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications
    > "However, it will be corrected by instanton contributions."
    > "with standard embedding."
