# Heterotic E7 candidate gate: explicit SU(2) compactification and three-family obstruction

## Outcome

A primary-source-established ten-dimensional `E8 x E8` heterotic ansatz was made explicit: compactify on `X=K3 x T2` and use the standard embedding

`V1=pr_K3^*(T K3)`, `V2=O^8`, `[W]=0`.

The rank-two bundle has structure group `SU(2) subset E8`, whose commutant is `E7`; at a generic torus point the four-dimensional theory has `E7 x E8 x U(1)^4` and `N=2`, as stated by Kachru and Vafa [1]. This is a concrete, tadpole-satisfying 4D E7 compactification, but it cannot yield net three chiral `56`s. The obstruction is stronger than a failed catalog search: every honest rank-two `SU(2)` bundle has `c3(V)=0`, hence its CY3 holomorphic Euler characteristic is zero. Thus the bounded `SU(2) -> E7` route cannot provide the requested net-three chiral index without changing the structure group/projection mechanism.

No alpha fit, `133` subtraction, primality condition, or partition congruence is used.

## 1. Ten-dimensional and geometric data

Start with the supersymmetric `E8 x E8` heterotic string on

`M10=Minkowski_4 x K3 x T2`.

`K3 x T2` has trivial canonical bundle and complex dimension three, but reduced `SU(2)` rather than generic `SU(3)` holonomy, so the result is four-dimensional `N=2`, not an `N=1` phenomenological vacuum. Put the K3 spin connection in an visible `SU(2) subset E8`. The adjoint branching is

`248 = (133,1) + (1,3) + (56,2)` under `E7 x SU(2)`,

so the unbroken visible commutant is E7. This branching—not subtraction of 133—identifies the gauge factor and charged bundle representation.

Topological input on the only nontrivial four-cycle is

`integral_K3 c2(TK3)=chi_top(K3)=24`.

Because `TT2` is trivial and `V1=TK3` after pullback,

`c2(TX)=c2(V1)=24 [pt_K3]`, `c2(V2)=0`.

The integrated/cohomological heterotic Bianchi condition

`c2(TX)-c2(V1)-c2(V2)=[W]`

therefore gives `[W]=0` exactly. Kachru–Vafa describe this standard embedding and its E7 spectrum [1]. The underlying K3 tangent connection is the Ricci-flat `SU(2)` holonomy connection, hence an HYM instanton for the standard embedding. This report does **not** prove stability of the pullback as a bundle for every polarization on the product, nor stabilize K3/T2 moduli; those are remaining gates. The established standard-embedding solution is the narrower sourced claim.

## 2. Exact CY3 Dirac/HRR index

For a holomorphic bundle `V` on a CY threefold (`c1(TX)=0`), Hirzebruch–Riemann–Roch gives

`chi(X,V)=integral_X ch(V) Td(TX)`.

With `c1(V)=0`, the degree-six contribution is

`ch3(V)=c3(V)/2`, while the possible `ch1(V)c2(TX)/12` term vanishes. Therefore

`chi(X,V)=1/2 integral_X c3(V)`.

In the `E8 -> E7 x SU(2)` decomposition, the multiplicity index for the E7 `56` is the index of the rank-two associated bundle `V`. But a rank-two complex vector bundle has `c_i(V)=0` for `i>2`; equivalently its formal Chern roots are `x,-x`, so `c3(V)=0`. Hence

`N_56(left)-N_56(right)=chi(X,V)=0`.

On `K3 x T2`, the product geometry also makes the nonchirality manifest and Kachru–Vafa report hypermultiplets rather than an N=1 chiral spectrum [1]. Sign conventions can reverse an index, but cannot turn zero into three.

### Scoped catalog

The bounded catalog had two classes:

1. **K3 x T2 standard embedding** [1]: explicit 4D E7 vacuum, Bianchi exact, `N=2`, index zero.
2. **Smooth CY3 with any stable holomorphic rank-two SU(2) bundle**: if HYM and Bianchi conditions can be met, E7 remains the commutant, but the rank theorem still forces `c3=0`, so net E7-56 chirality is zero. This algebraic obstruction makes searching more rank-two monads for `c3=6` pointless: such data cannot be Chern data of a rank-two bundle.

A rank-three `SU(3)` bundle may have `integral c3=6`, yielding `chi(V)=3`, but its commutant in E8 is E6, not E7. This is the familiar reason the current one-`27` E6 pipeline is structurally different rather than a branch of three chiral E7 `56`s.

## 3. E7 worldsheet block and branching mismatch

The predecessor modular-completion gate constructs the level-one E7 lattice sectors

`chi_0 = q^(-7/24)(1+133q+...)`, `chi_1=q^(11/24)(56+...)`,

with discriminant group `Z2`, `h_56=3/4`, and exact E7 x A1 gluing to E8. This is precisely compatible with choosing an `SU(2)=A1` subgroup of one heterotic E8: the `(56,2)` piece is the nontrivial paired glue sector. It supplies the current-algebra/gauge-lattice origin of E7 and its 56; it does not supply the cohomology multiplicity. That multiplicity is the geometric index above. The coefficient `133` counts E7 currents (126 roots plus seven Cartan oscillators), not compact or spacetime dimensions.

Under `E7 -> E6 x U(1)`,

`56 = 27_1 + 27bar_-1 + 1_3 + 1_-3`

(up to simultaneous charge-sign convention). Thus even a single full 56 branches into an E6-vectorlike `27 + 27bar`, not the current pipeline's isolated chiral `27`. Since the SU2 index is zero, this candidate supplies no net E6 27 after branching. The existing E6 breaking report's algebraic SM stabilizer and 351-prime escape therefore cannot be imported as though this candidate generated its chiral input.

## 4. Partition/prime test and negative controls

Partition coefficients enter the oscillator/current characters, hence worldsheet degeneracies. Neither the heterotic Bianchi identity nor HRR contains `p(n)`, a Ramanujan residue class, or a primality predicate. The actual topological integer here is 24, which is composite and is required by K3 topology. Imposing prime flux would reject a standard exact embedding without any worldsheet derivation.

Executed controls in `exact_candidate_certificate.py`:

- Bianchi: `24-24-0=0`.
- Rank-two control: proposed `c3=6` is rejected because `c3` above rank two vanishes.
- Rank-three comparison: `c3=6` gives index 3 but changes the commutant to E6.
- Composite control: `c2=24` is admitted; no prime requirement occurs.

## 5. Remaining gates and next requirement

This candidate is partially viable only as a consistent 4D E7 string vacuum with exact tadpole arithmetic. It fails the net-three/N=1 phenomenology gate. It also leaves moduli stabilization, full low-energy anomalies after any N=1 projection, and SM breaking unaddressed.

The next non-post-hoc requirement is one of:

1. provide a sourced projection (orbifold/free quotient with equivariant bundle) that reduces N=2 and demonstrably produces an unpaired E7-sector index despite the parent pseudoreal/full-hypermultiplet spectrum, including local/global anomaly checks; or
2. relax exact E7 commutant—e.g. use an SU3 bundle with `c3=6`, accepting visible E6—and then solve Bianchi, stability/HYM, quotient/Wilson-line, and E6-breaking gates as a new candidate.

A line-bundle structure group can leave an E7 factor accompanied by U(1), but that is a different commutant and charge-index problem and requires a fresh, anomaly-consistent model; it is not evidence that the SU2 obstruction was evaded.

## Primary sources and evidence boundary

[1] S. Kachru and C. Vafa, *Exact Results for N=2 Compactifications of Heterotic Strings*, Nucl. Phys. B450 (1995) 69–89, arXiv:hep-th/9505105, https://arxiv.org/pdf/hep-th/9505105 . The paper states that the familiar E8xE8 standard embedding on K3 x T2 gives generic `E7 x E8 x U(1)^4`, ten 56 hypermultiplets, and neutral moduli. This directly sources the concrete ansatz and spectrum.

[2] P. Candelas, G. Horowitz, A. Strominger and E. Witten, *Vacuum Configurations for Superstrings*, Nucl. Phys. B258 (1985) 46–74, DOI 10.1016/0550-3213(85)90602-9. Primary source for Calabi–Yau heterotic compactification and embedding the spin connection in the gauge connection. The present exact characteristic-class arithmetic is independently executable; no inaccessible equation is promoted beyond this standard-embedding scope.

[3] S. Donaldson, *Anti self-dual Yang-Mills connections over complex algebraic surfaces and stable vector bundles*, Proc. Lond. Math. Soc. 50 (1985) 1–26; K. Uhlenbeck and S.-T. Yau, *On the existence of Hermitian-Yang-Mills connections in stable vector bundles*, Comm. Pure Appl. Math. 39 (1986) S257–S293. These establish the stability/HYM bridge in their stated settings. This report does not infer stability for an arbitrary hypothetical rank-two CY3 bundle merely from Chern data.

The local modular-completion, Dirac, partitions, and E6-breaking reports were used as predecessor constraints. No publication target or other lane was modified.
