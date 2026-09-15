# Partitions, primes, modularity, E7, and chirality: connection audit

## Outcome and claim boundary

The strongest useful bridge is **integer partitions → eta-function oscillator counting → lattice theta functions / chiral worldsheet characters → a specified string compactification and its indexed spectrum**. Ramanujan congruences, Dedekind eta multipliers, and mock modular forms are genuine parts of this bridge, not numerological coincidences.[5][8][9] The present investigation does **not** obtain a map from a partition congruence to a mass unit, a preferred compactification radius, four-dimensional spacetime, or the electromagnetic coupling. That is a missing physical construction, not a theorem that such a construction is impossible.

The user's chirality hint has a particularly concrete mathematical success: **“chiral partitions” are a published representation-theoretic notion**, classified using 2-core towers, and they are not merely non-self-conjugate Young diagrams.[7] A second genuine bridge, **elliptic genera → indexed Dirac/supercharge problems**, does connect modular structures to signed state counting, once a sigma model, geometry, bundles, and grading are specified.[11] No source inspected supplies the additional map identifying the first chirality with physical fermion chirality or knot mirror chirality.

All finite mathematical claims below are executable in `exact_certificate.py`; `certificate.json` was replayed without regeneration by `--verify`. This is exact Python integer/rational checking, **not Lean, a proof-assistant kernel certificate, or an independent proof of the infinite congruence theorems**. The physical conclusions are source-based reasoning with stated scope.

## 1. Ramanujan: arithmetic on degeneracies, not a prime energy scale

For ordinary partitions, `P(q)=sum p(n)q^n=product_(m>=1)(1-q^m)^(-1)`, and `eta(tau)=q^(1/24)product_(m>=1)(1-q^m)` with `q=exp(2 pi i tau)`. Thus `P(q)=q^(1/24)/eta(tau)`; the coefficient index and the coefficient itself are different quantities.[5][8]

The classical congruences are `p(5n+4)=0 mod 5`, `p(7n+5)=0 mod 7`, and `p(11n+6)=0 mod 11`.[8] Exact product expansion and an independent Euler pentagonal recurrence agree for every coefficient through 5000; the three progressions have respectively 1000, 714, and 455 checked terms and no failures (`certificate.json`). These are bounded confirmations, not the all-n proof.

Ahlgren–Ono give infinitely many congruences modulo prime powers for every prime at least five, in more general arithmetic progressions; their framework uses half-integral weight cusp forms, Hecke operators, Shimura correspondence, and Galois representations.[8] **“Every prime occurs in some progression” does not mean `p(ell*n+b)=0 mod ell` for every prime.** The certificate gives an explicit violating coefficient for every possible residue b for each of ell=13 and ell=137. Those finite witnesses suffice to refute each proposed simple progression for those two primes, while saying nothing against the broader Ahlgren–Ono progressions.

A divisibility `p(N)=0 mod ell` constrains the number of states if a physical model independently has degeneracy p(N). It neither sets `E_N` nor specifies a physical mass unit. Even a cyclic order-ell symmetry explanation needs an actual action on states; divisibility by itself does not construct such an action. To turn this into “prime-scale quantization,” supply a Hilbert space, self-adjoint Hamiltonian or mass operator, the energy-to-q grading, a normalization scale, and a theorem linking the arithmetic selection rule to permitted eigenvalues. A scale rescaling leaves pure degeneracy data unchanged.

## 2. Three different Dedekind objects

**Dedekind eta** is a modular object directly controlling ordinary partition generating functions; **Dedekind sums** occur in its transformation multipliers and in Rademacher's exact coefficient formula.[5] The relevant operation is modular transformation of tau, not counting Boolean functions. Rademacher therefore supplies an authentic partitions–modularity–Dedekind-sums bridge, but no choice of compactification or coupling follows from the exact coefficient formula alone.

**Dedekind numbers d_n** count monotone Boolean functions on n variables (equivalently antichains of the Boolean subset poset); they are a different sequence and problem.[1] Pawelski–Szepietowski establish actual congruences, including `d_9=6 mod 210`, by symmetry and orbit methods.[1] This is stronger than merely sharing a mathematician's name, but it is a parallel finite group counting mechanism, not an eta identity.

Their duality is `f^d(x)=1-f(1-x)`. Non-self-dual monotone functions form pairs, yielding `d_n=2 k_n+lambda_n` and `d_n=lambda_n mod 2`, where lambda_n counts self-dual functions.[1] Exact exhaustive truth-table enumeration here reproduces `d_0,...,d_4 = 2,3,6,20,168` and self-dual counts `0,1,2,4,12`. This is a concrete common **involution/fixed-point counting** structure shared with partition conjugation. An involution alone does not define a spatial orientation, a spinor chirality operator, or an elliptic complex.

The phrase “Dedekind partitioning” is therefore ambiguous. Specify eta/sums, monotone functions/antichains, or a different Dedekind construction before merging claims. No equation identifying these Dedekind numbers with the E7 lattice character was found in the inspected material.

## 3. Mock theta functions: genuine physics, specified background

Ono's notes explain Ramanujan mock theta functions as holomorphic parts of harmonic Maass forms, with nonholomorphic completion restoring the appropriate modular behavior.[6] Mock modularity is not a synonym for an approximate modular form whose discrepancies can be freely chosen.

Dabholkar–Murthy–Zagier explicitly decompose a meromorphic Jacobi form counting quarter-BPS states in N=4 string theories into a mock Jacobi part and an Appell–Lerch sum: single-centered black-hole quantum degeneracies appear in the former, while multi-centered wall-crossing contributions appear in the latter.[9] Their concrete review begins with Type-II strings on K3 times T2.[9] **The background and charges precede the counting problem**; the theorem is not a derivation that nature must choose that background or four dimensions. This is a viable mathematical technology for an E7 model's protected index only after the model and index have been defined.

## 4. Exact E7 theta/eta candidate retained

We constructed E8 roots in doubled orthonormal coordinates and selected those perpendicular to `e7+e8`, producing the E7 root system. The explicit seven-simple-root Gram matrix has determinant 2. Exhausting lattice vectors through norm squared 4 gives

```
Theta_E7(q) = 1 + 126 q + 756 q^2 + ...
product_m (1-q^m)^(-7) = 1 + 7 q + 35 q^2 + ...
q^(7/24) Theta_E7(q)/eta(q)^7 = 1 + 133 q + 1673 q^2 + ...
```

These coefficients and the determinant are recomputed, not fitted. The term 133 is **126 root currents plus seven Cartan oscillators**, not 133 macroscopic directions. The standard level-one lattice/affine-E7 interpretation identifies this as its vacuum character; that general correspondence is background mathematical knowledge, not formalized in this certificate.[unverified] The standard Sugawara expression gives central charge `c=k dim(g)/(k+h-dual)=7` for E7 at level one; the rational substitution is checked, whereas the Sugawara theorem and `h-dual=18` are external inputs.[unverified]

Determinant 2 is a concrete warning: E7 is **not unimodular**. Its theta function alone is not a closed scalar full-SL(2,Z) partition function; a modular completion must include discriminant/coset information or an embedding and additional sectors (standard lattice-theta transformation theorem, not kernel-checked here).[unverified] The certificate also projects E8 roots of inner product one with the removed root, obtaining 56 vectors of norm squared 3/2 and conformal weight 3/4. This retains a substantive 133/56 modular-state-counting candidate without selecting alpha or spacetime dimension.

A full string construction still needs left/right sectors, spin structures or GSO projections, level matching, ghosts and central-charge cancellation, admissible bundle/flux data, and a physical massless spectrum. The character is an input block, not the completed compactification.

## 5. Consistency versus choosing a vacuum or dimension

Toroidal compactification gives momentum and winding integers, radii and other moduli, enhanced-symmetry points, and Narain lattices with continuous moduli.[2] In the circle convention used by the certificate, `alpha-prime=1`, `p_L=n/R+wR`, `p_R=n/R-wR`, so `(p_L^2-p_R^2)/4=nw` independently of R. We tested the identity on the same integer grid at R=1, 2, and 3/2, while the elementary momentum contribution `1/R^2` changes to 1, 1/4, and 4/9. This is an exact algebraic illustration that charge integrality/level matching does not fix the radius. The cited Narain construction supplies the larger continuous-moduli setting; the finite test does not by itself verify the full modular partition sum.[2]

Louis–Schasny–Valandro supply a direct dimensional counterexample to “E7 selects four”: heterotic compactification on K3 yields a **six-dimensional** effective action; standard SU(2) embedding leaves E7 times E8 and the paper explicitly identifies the 133 as the six-dimensional E7 gauge potential.[3] Thus E7 gauge symmetry is compatible with a sourced compactification not having four noncompact dimensions. This does not rule out an additional dynamical selection rule; it refutes selection from the E7 label alone.

A potentially misleading nearby number is also present in Quevedo's toroidal discussion: choosing d=6 gives a four-dimensional model with **132 toroidal moduli**, before adding the dilaton and axionic sector.[2] Do not turn “132 plus a dilaton” into “133 dimensions compactified to 4”: it mixes field-space dimension, gauge-algebra dimension, and spacetime dimension, and omits the axion included in that discussion. No dynamical minimization or uniqueness theorem follows from the coincidence.

## 6. Chirality: exact definitions and missing maps

### Young-diagram reflection

Partition conjugation transposes the Ferrers/Young diagram: `lambda'_j=#{i:lambda_i>=j}`. A self-conjugate partition is fixed by this transpose; its count equals the number of partitions into distinct odd parts via diagonal hooks.[4] Exhaustive enumeration through n=12 confirms the equality here. Reflection within a planar combinatorial diagram is not automatically ambient isotopy of an embedded knot, nor a grading of spacetime spinors.

### Published chiral partitions are a different criterion

Ayyer–Prasad–Spallone define a representation rho of S_n as chiral when `det o rho = sgn`, and a partition as chiral when its corresponding irreducible representation is chiral. Their classification uses 2-core towers and includes chiral self-conjugate partitions.[7] Consequently “chiral means lambda differs from lambda-prime” is false.

The executable diagnostic computes each Specht dimension by hook lengths, the transposition character by the content sum, and `m_minus=(dimension-character(transposition))/2`; determinant is -1 precisely when m_minus is odd. It reproduces the paper's chiral counts for n=1 through 12: `0,1,2,3,5,4,8,12,20,8,16,24`.[7] In particular lambda=(2,1) is **self-conjugate and chiral**, with dimension 2, trace 0, and one negative transposition eigenvalue. This exact counterexample blocks identifying these two uses of “reflection chirality.”

### The legitimate signed-index bridge

Witten's elliptic-genus construction organizes a sequence of twisted Dirac indices using symmetric and exterior powers and modular generating functions; the sigma-model supercharge plays the corresponding physical role.[11] This genuinely supplies a map from specified graded spectral/geometric data to modular coefficients. It does not identify every eta product or symmetric-group determinant with an internal Dirac index. For spacetime net chirality one must specify the compact spin geometry, gauge bundle, Dirac operator, zero-mode decomposition, and which grading becomes left versus right after compactification.

To connect a partition to knot chirality, define a map `K: partitions -> embedded-knot isotopy classes` and prove `K(lambda-prime)=mirror(K(lambda))`, together with enough injectivity or a chirality-detecting invariant to support the desired conclusion. To connect a chiral Specht representation to physical chirality, define an actual functor/construction into the relevant spinor zero modes and prove its determinant/sign observable computes the required index. Neither map was supplied by the papers inspected. Young diagrams labelling representations or an abstract involution appearing on both sides is insufficient.

For monotone Boolean functions, duality pairs likewise provide a useful structural analogy; an orientation-sensitive geometry and a map intertwining Boolean duality with its physical parity are still missing. The shared finite permutation-group language is a promising place to attempt a map, not evidence that it already exists.

## 7. “Special nimbers”

If “nimbers” was a typo for “numbers,” the candidates above are partition numbers, Dedekind numbers, Fourier coefficients, and prime-power congruence data; the sequence and operation need identification. If literal, Conway nimbers belong to combinatorial game arithmetic, not ordinary integer arithmetic: Nim addition behaves like XOR, and Nim multiplication realizes characteristic-two finite fields in appropriate finite segments; James Propp explains examples including the four-element and sixteen-element fields.[10] There is a real combinatorial-games interpretation for heap partitions, but no canonical conversion of Nim arithmetic to the ordinary congruences modulo 5, 7, 11, or 137 used here. A game rule and a physical interpretation would be extra assumptions.

## 8. Falsifiable next candidate, not a post-hoc formula

Retain the **E7 lattice-character plus indexed compactification** route, and test the following in order:

1. Specify a complete worldsheet model / compact space and gauge bundle independently of alpha or a desired spacetime dimension.
2. Assemble E7 theta-coset sectors with the other left/right sectors; prove modular covariance/invariance and anomaly cancellation with explicit normalizations.
3. Compute the massless spectrum and an internal Dirac/elliptic index; only here test whether the proposed partition chirality has a map to net fermion chirality.
4. Derive, rather than choose, the vacuum conditions and any moduli stabilization selecting radii/dilaton; show competing solutions and their stability.
5. Derive a Hamiltonian/charge rule explaining the relevant prime congruence and demonstrate its effect on energies or couplings, not just degeneracies.
6. Run physical matching to electromagnetism with the selected boundary data. A coefficient coincidence is not a prediction.

Failure of any proposed explicit map or consistency gate would falsify that candidate mechanism. Absence of these maps currently means the bridge is incomplete, not mathematically forbidden.

## Retrieval and reproducibility notes

Independent search vectors covered classical and all-prime partition congruences; scarcity theorems; mock/Maass forms; black-hole wall crossing; eta multipliers/Rademacher; monotone Boolean Dedekind numbers and divisibility; Narain lattices/moduli; E7 theta/affine characters; heterotic K3; E-string/topological-string leads; literal nimbers; Young-diagram self-conjugacy; chiral partitions and 2-quotients; and elliptic/Dirac indices. Search-result-only E-string and quantum-affine-q-character hits were not promoted to evidence for this particular lattice-character claim. “q-character” in quantum affine representation theory is not automatically the torus character used here.

Primary/review full texts and exact source quotes are saved locally; each cited source has a ledger-validated verbatim quote. Several equations in extracted PMC/HTML/PDF material lose typography; quoted prose, raw full texts, and exact local calculations are separated. The scarcity-paper publisher PDF failed, and its arXiv PDF fallback also failed, so its search snippet is not used as an all-prime classification proof. ArXiv abstract extraction initially lost the abstract for the black-hole paper; its full PDF extraction succeeded. Direct HTTP requests had intermittent timeouts/403s; successful web-extraction cache copies are preserved in this directory. The initial collector's failed entries are historical attempts, not the final evidence inventory (`source_evidence.json` is final).

A Windows/Cygwin file-tool shadow-path mismatch was detected when a successful write did not exist for native Python. All deliverables were transferred to and executed at the explicit native directory `C:/Users/mikeb/e7-alpha-theory/gap-investigation/connections/partitions`; native execution and readback are the verification authority. No other research lane, publishing target, or parent card was modified.

## Sources

[1] https://arxiv.org/html/2302.04615v1 — dedekind
    > "andrzej.szepietowski@ug.edu.pl
Abstract
We study some divisibility properties of Dedekind numbers. We show that the ninth Dedekind number is congruent to 6 modulo 210.
1
Introduction
We define
D
n
D_{n}
to be the set of all monotone Boolean"
[2] https://fisica.usac.edu.gt/public/curccaf_proc/quevedo1/node4.html — narain
    > "identified under the 

duality group
.
This is the situation that gets generalized to higher dimensions.

In general, compactification on a
-dimensional torus has the

moduli space
with 

points identified under the duality group
.

For the heterotic string with 16 extra left moving coordinates
with

a similar modification to the duality group.

The left- and right- moving momenta
live on an

even, selfdual lattice of signature
, which

is usually called the Narain lattice
[
9
].

This generalizes the
lattice defined by the

integers
of eq. (
9
).
We can easily verify in this case that the dimension of
is
corresponding to the number of independent

components of
with
. For
we have a 

4D string model with a moduli space of dimension
. To

this we have to add the dilaton field
which, together

with the spacetime components of the antisymmetric

tensor
, can be combined into a new modular

parameter:
(11)
Here the axion field
i"
[3] https://arxiv.org/html/1112.5106v2 — k3
    > "ent bundle
𝒯
K
​
3
{\mathcal{T}}_{K3}
.
The standard embedding breaks one
E
8
E_{8}
to the maximal commutant
E
7
E_{7}
, i.e.
E
8
×
E
8
⟶
E
8
×
E
7
×
⟨
S
​
U
​
(
2
)
⟩
,
E_{8}\times E_{8}\longrightarrow E_{8}\times E_{7}\times\langle SU(2)\rangle\ ,
(3.3)
where
⟨
H
⟩
\langle H\rangle
denotes the broken group factor. For the standard embedding the hermitean Yang-Mills equations
(
2.7
) take the form
ℱ
∈
H
1
,
1
​
(
End
​
𝒯
K
​
3
)
,
ℱ
∧
J
=
0
,
{\mathcal{F}"
[4] https://www.whitman.edu/mathematics/cgt_online/book/section03.03.html — selfconjugate
    > ", as we saw in example
3.3.3
.
Ex 3.3.7
A partition of $n$ is self-conjugate 
if its Ferrers diagram is symmetric around the main diagonal, so that
its conjugate is itself. Show that the number of self-conjugate
partitions of $n$ is equal to the number of partitions of $n$ into
distinct odd parts."
[5] https://btw-47.github.io/rademacher2.pdf — rademacher
    > "express the ﬁnite sum Ac(n) in terms
of Dedekind sums (see, for example, [13, Equations 3, 4]). There is also a simpler (and more illuminating)
formula for Ac(n) due to Selberg [19, Equation 18], whose work is ﬂeshed out in [18, Lectures 22–23].
Rademacher’s original derivation [16] and su"
[6] https://swc-math.github.io/aws/2013/2013OnoNotes.pdf — mocknotes
    > "tion 4.1. Ramanujan’s functions are the
holomorphic parts of special weight 1/2 harmonic Maass forms. This realization makes it
possible to now prove theorems such as Theorem 1.2. We shall give the proof in Section 13.
The connection between Ramanujan’s mock theta functions and harmonic Maass forms
does not immediately shed light on Ramanujan’s vague deﬁnition. Moreover, Ramanujan’s
strange example concerning f(q) and b(q) shows that mo"
[7] https://arxiv.org/html/1604.08837v1
    > "rivial character or the sign character.
We call (ρ,V)(\rho,V) a *chiral representation* if det∘ρ\det\circ\rho is the sign character of SnS\_{n}.

Recall that the irreducible complex representations of SnS\_{n} are parametrized by partitions of nn.
For brevity, we shall say that λ\lambda is a *chiral partition* if the corresponding representation (ρλ,Vλ)(\rho\_{\lambda},V\_{\lambda}) is chiral11
1
The use of the field 𝐂\mathbf{C} is not important. Our results hold over any field of characteristic different from two, so long as VλV\_{\lambda} is interpreted as the representation corresponding to λ\lambda in Young’s seminormal form.."
[8] https://pmc.ncbi.nlm.nih.gov/articles/PMC60793
    > "example, we have

|  |
| --- |
| 1.2 |

We have shown ([13](#B13), [17](#B17)) that if ℓ ≥ 5 is prime and *m* is any positive integer, then there are infinitely many congruences of the form

As in the case of Ramanujan's congruences, all of these arithmetic progressions lie within the class −δℓ (mod ℓ). To summarize, the current state of knowledge consists of a systematic theory of congruences within the progressions −δℓ (mod ℓ), as well as some sporadic examples of congruences that fa"
[9] https://arxiv.org/pdf/1208.4074
    > ", don.zagier@mpim-bonn.mpg.de Abstract: We show that the meromorphic Jacobi form that counts the quarter-BPS states in N = 4 string theories can be canonically decomposed as a sum of a mock Jacobi form and an Appell-Lerch sum.
The quantum degeneracies of single-centered black holes are Fourier coeﬃcients of this mock Jacobi form, while the Appell-Lerch sum captures the degeneracies of multi-centered black holes which decay upon wall-crossing. The completion of the mock Jacobi form restores the modular symmetries expected from AdS3/CFT2 holography but has a holomorphic anomaly reﬂecting the non-compactness of the microscopic CFT. For every positive integral value m of the magnetic charge invariant of the black hole, our analysis leads to a special mock Jacobi form of weight two and index m, which we characterize uniquely up to a Jacobi cusp form. This family of special forms and another closely related family of weight-one forms contain almost all the known mock modular forms including the mock theta functions of Ramanujan, the generating function of Hurwitz-Kronecker class numbers, the mock modular forms appearing in the Mathieu and Umbral moonshine, as well as an inﬁnite number of new examples.
Keywords: black holes, mock modular forms, superstrings, wall-crossing.
arXiv:1208.4074v2 [hep-th] 3 Apr 2014 Contents 1.
Int"
[10] https://mathenchant.wordpress.com/2021/12/17/numbers-from-games
    > "as 0, 1, *α*, and *α*+1 respectively). Conway’s kind of multiplication turns the nimbers \*0, \*1, \*2, and \*3 into a funny incarnation of the finite field of order 4. Nor is this an isolated coincidence. Conway’s multiplication turns the nimbers \*0 through \*15 into a funny incarnation of the finite field of order 16. And for any *n*, if we set *N* equal to 2 to the power of 2*n*, Conway’s multiplication turns the nimbers \*0 through \*(*N*−1) into a funny incarnation of the finite field of order *N*. (See also Peter Cameron’s blog essay, listed in the References.)

Conway didn’t know the full story on that day in 1969; he was discovering it in bits and pieces. He didn’t have t"
[11] https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-109/issue-4/Elliptic-genera-and-quantum-field-theory/cmp/1104117076.pdf — Witten: Elliptic Genera and Quantum Field Theory
    > "e series of operators indicated in (1).
Subsequent work [6, 7, 15] showed, roughly, that it is possible to use elliptic modular forms to write a generating functional for this infinite series of operators.
To be precise, the modular forms in question were modular forms for the congruence subgroup Γo(2) of SL(2, Z), which can be viewed as the subgroup that leaves fixed one of the three non-trivial spin structures on an elliptic curve.
Ochanine introduced [6] the notion of an "elliptic genus" and synthesized the above statements in the following conjecture: for any elliptic genus and any spin manifold M with S 1 action, the character valued elliptic genus is a constant. I will not he"
