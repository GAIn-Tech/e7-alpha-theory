# Knots, E7, partitions and chirality: strongest bridges and precise limits

## Outcome

There are substantial bridges, not merely similar words: ribbon-category functors turn quantum-group data into link invariants; Chern–Simons quantization relates them to WZW conformal blocks; supersymmetric line-defect indices can be Ramanujan q-series and eta-products; and a specified knotted-soliton/Dirac model relates spectral flow to Hopf charge.[1][10][12] None of these retrieved sources derives a spacetime compactification **133 → 4**, fixes an electromagnetic coupling, or identifies chiral partitions with the net chiral 27 in the existing E7 orbifold scenario. This is a bounded evidence finding, not a universal impossibility theorem.

The strongest actual dimensional bridge located is Witten's six-dimensional ADE theory on a specified two-manifold, with a supersymmetry-preserving twist, giving a four-dimensional theory. The Lie type can be E7; 133 labels the dimension of its gauge algebra, not the number of starting coordinates. The four-dimensional couplings depend on geometric moduli, which are additional input.[11] This does not solve the separate anomaly or E6-breaking gates.

## 1. Three polynomial objects must not be conflated

**Kauffman bracket:** a one-variable state sum on unoriented diagrams, with a writhe correction yielding the Jones polynomial. **HOMFLY-PT:** the oriented two-variable skein invariant, associated to the Hecke/type-A construction. **Kauffman two-variable polynomial:** a different invariant associated to the BMW construction, with classical orthogonal/symplectic specializations. Jones's own survey explicitly distinguishes their algebraic constructions.[15] The notation “Kauffman HOMFLY” therefore does not identify one canonical polynomial.

Our explicit convention is bracket crossing `A I + A^-1 e`, `e^2 = δ e`, `δ = -A^2-A^-2`, unknot-normalized closure, writhe factor `(-A^3)^(-w)`, and `t=A^-4`. Its trefoil result is `V(t)=t+t^3-t^4`; the mirror is `V(t^-1)`. The downloaded Jones survey uses different displayed variable/sign conventions; the certificate defines its own completely rather than mixing them. This is an exact finite calculation, not an extracted tabular value.

A general quantum E7 invariant can be built from the ribbon category of suitable representations of `U_q(e7)`. This is the Reshetikhin–Turaev mechanism; a framed colored link is sent to an endomorphism of the tensor unit.[13] At generic q, the 56 has four tensor-product channels `1 + 133 + 1463 + 1539`, unlike the simple two-channel HOMFLY or three-channel Kauffman patterns.[3][13] Channel counting alone is not a theorem that no specialized identities can occur: a categorical equivalence, specialization or additional skein computation would have to establish one.

Morrison–Peters–Snyder prove real identities among specialized Jones, HOMFLY-PT, Kauffman and G2 invariants through small modular-category coincidences.[13] Their G2 example is not E7. Their `D_2n` planar algebras are expressly **not** the Lie algebras with the same Dynkin name.[13] Neither exceptional terminology nor a shared integer establishes an E7 identification.

## 2. Quantization and state counting, with an E7 example

For a compact simple simply connected group, basic invariant-form normalization and integral level, a Chern–Simons action on a three-manifold has the form

`S = k/(4π) ∫ Tr(A∧dA + (2/3)A∧A∧A)`.

Large gauge transformations shift S by multiples of `2πk`; invariance of `exp(iS)` is the quantization statement. Witten explicitly compares this logic with Dirac monopole quantization.[1] His later knot paper uses `q=exp(2πi/(k+h∨))` and spells out framing and normalization qualifications.[11] Quantum-group authors also use its square root as q; comparisons must state conventions. The quantized coefficient is not automatically the four-dimensional Maxwell/Yang–Mills kinetic coefficient.

At E7 level one, Mukhi–Poddar give `c=7`, nontrivial primary conformal weight `h=3/4`, and explain that the ordinary `133`, `1463`, and `1539` channels decouple as independent affine primaries, leaving the 56 as the only nontrivial primary.[3] Thus `56 fusion 56 = vacuum`, not the ordinary untruncated tensor product. The model has two primary sectors, not 56 or 133 primary sectors.[3]

Using the standard two-sector modular input `S=(1/√2)[[1,1],[1,-1]]`, the exact certificate verifies the Z2 fusion coefficients through the Verlinde sum. It also evaluates `dim H(Σ_g)=Σ_a S_0a^(2-2g)=2^g`: sphere 1, torus 2, genus-two surface 4. These are Hilbert-space dimensions **conditional on that modular input**, not spacetime dimensions. In particular, the appearance of 4 requires choosing genus two; it does not derive four macroscopic coordinates. The supplied `h=3/4` gives twist `exp(2πih)=-i`, the anti-semion convention; orientation reversal complex-conjugates the braiding/topological spin. This modular identification is not independently derived or Lean-checked here.

For rigor, the Fuchs et al. paper offers an affine-representation approach including exceptional Lie algebras, but its section 4.2 expressly assumes a suitable completion/topology conjecture. Its abstract alone must not be cited as an unconditional proof of every claimed step.[14] The certificate checks the finite Verlinde arithmetic, not the analytic/geometric theorem.

A second exact calculation enumerates the E8 lattice vectors orthogonal to `e7+e8`, producing the E7 lattice theta coefficients through norm squared six:

`Θ_E7(q) = 1 + 126q + 756q² + 2072q³ + ...`.

The seven-color partition product has coefficients `1,7,35,140`; multiplying gives `1,133,1673,11914`. In the usual level-one lattice-VOA realization, `Θ_E7/η^7` is the vacuum character: our certificate checks the series arithmetic, **not that representation-theoretic identification**. Even without invoking it, the finite count transparently exhibits `133=126 roots+7 oscillator contributions`, an internal current-state count. It is not a collapse of 133 coordinates into a smaller space. The same distinction separates central charge `c=7` from a spacetime dimension.

## 3. Ramanujan, Dedekind and partitions: a particularly close primary source

Okazaki–Smith, arXiv:2408.07893v2, is an unusually direct match: **Chern–Simons theories with defects, Rogers–Ramanujan type functions and eta-products**. It computes line-defect half-indices of specified 3d N=2 theories, connects fundamental Wilson lines with Rogers–Ramanujan functions, and states an SU(N) theory with adjoint chiral matter has BPS boundary local operators in one-to-one correspondence with N-core partitions.[10] Read especially equations (1.8)–(1.9), section 2.2.3, appendix A, and section 5.

Its exceptional section is **G2**, not E7: full-text checks found G2 section headings, and no literal E6/E7/E8 occurrence. The abstract's “exceptional gauge groups” cannot be silently promoted to an E7 formula. Its N-core partition correspondence is not the determinant-defined chiral-partition condition below. These theories already specify dimension, level, matter and boundary conditions before calculating indices.[10]

The exact certificate compares the sum and product sides of the first Rogers–Ramanujan identity through degree 30 using independent integer dynamic programs. This verifies those finite coefficients only, not the infinite identity. Warnaar–Zudilin give an independent mathematical primary source proving an eta/q-series generalization of Macdonald and Rogers–Ramanujan identities.[7] Neither an eta identity nor this coefficient check quantizes geometric radii or selects a physical prime scale.

Distinguish three q's: a formal knot-polynomial variable; its root-of-unity specialization fixed by a CS level; and a convergent grading/modular parameter in an index or character. A physical dictionary must specify how they are identified; sharing the letter q supplies no map.

Gukov–Schwarz–Vafa provide another precise bridge: their paper proposes an sl(N) knot-homology/BPS-state correspondence in open topological strings, explicitly calling it a conjecture.[5] A graded Euler characteristic or signed protected index is not generally the total number of states: cancellations lose information. This is a plausible state-counting framework to investigate, not a proof that every coefficient of every exceptional knot invariant counts physical compactification vacua.

## 4. Chirality is a productive hint, but several inequivalent structures

### Knot chirality versus orientation

Knot chirality asks whether an embedding is equivalent to its ambient mirror. Reversing a component's orientation is different: Witten says it replaces its representation label by the complex conjugate.[11] For the self-dual/pseudoreal E7 56, charge conjugation is therefore not the same as an ambient mirror test. Jones distinguishes mirror images by variable inversion; inequality of the polynomials proves chirality, but equality of an incomplete invariant is not proof of amphichirality.[15] A TQFT reflection reverses the braiding and, in the unitary case, conjugates amplitudes; the output need not count four-dimensional Weyl fermions.

### “Chiral partitions” genuinely exist, but mean determinant sign

Ayyer–Prasad–Spallone define a chiral partition λ by `det ρ_λ = sgn` for the irreducible symmetric-group representation. Their Theorem 3 counts **self-conjugate chiral partitions**, so self-conjugate is demonstrably not synonymous with achiral in that terminology.[9] The exact example λ=(2,1) is self-transpose, while its standard S3 transposition matrix has determinant -1. Ordinary partition conjugation transposes Young diagrams; the associated sign-twist identity is representation theory, not a spacetime parity operation.

There is a real but lossy bridge through `B_n → S_n` and its Hecke deformation: braids enter knot invariants and Young diagrams label type-A representation sectors.[15] However, a transposition is its own inverse. Consequently the determinant character of the permutation image of a braid equals that of its mirror inverse. Our exact example checks this equality while Jones distinguishes the trefoil mirrors. Thus the simplest determinant/braid functor **forgets exactly the handedness information** needed by the proposed universal identification. This finite counterexample rules out that proposed identification, not every possible refined functor.

### Fermion chirality: a specified Dirac operator is essential

Four-dimensional fermion chirality is the grading by γ5; a chiral spectrum concerns an imbalance of left-handed representations versus their conjugates. In a smooth even-dimensional compactification the usual mathematical index input is `index D_E^+ = ∫_X Â(TX) ch(E)`, with hypotheses and boundary/orbifold corrections when applicable. This general index theorem is background mathematics, not formalized here, and it cannot be evaluated until X, a bundle/flux, the operator and boundary conditions are specified. The existing 5D interval/orbifold projection is not automatically that smooth closed even-dimensional setting.

A direct model-dependent connection does exist: Freyhult–Niemi couple a Dirac fermion to the unit-vector field of a Faddeev knotted soliton. Their equations (9)–(15) use opposite chiral anomalies and spectral flow to relate induced fermion number to a Hopf/self-linking invariant.[12] This is stronger than a verbal analogy. It is **not** an identity with a HOMFLY polynomial, not the determinant of a Specht module, and not a calculation of an E7 compactification's net 27s. A Hopf-charge sign does not fully classify geometric knot chirality.

A further crucial ambiguity: the spectral **eta invariant** of a Dirac operator is not the **Dedekind eta function**. In this soliton model the Hamiltonian spectrum is symmetric and its spectral eta invariant vanishes, while fermion number comes from spectral flow.[12] The two eta objects can meet in particular determinant/anomaly formulas, but equating them by name is invalid.

## 5. Strongest remaining E7 research route

Witten's sections 5.1 and 5.5 provide the best substantive starting point: choose the six-dimensional ADE (2,0) theory of type E7 (his opposite convention calls it (0,2)), a compactification surface D, defects and an R-symmetry twist. On a suitable D this yields four-dimensional N=2 physics and, with the further twist, a topological theory; the moduli of D control couplings.[11] This supplies actual dimensional reduction and a knot-observable framework, but still no moduli stabilization or unique electromagnetic matching. The elementary D-brane presentation naturally covers classical groups and Witten explicitly warns it does not naturally produce exceptional groups; the six-dimensional field-theoretic construction is the appropriate exceptional route.[11]

For the current chiral-E7 target, the next finite gate would have to supply an E7-specific compactification/defect model and compute its charged Dirac index or protected spectrum, with anomaly cancellation, then identify a proven map to its knot/index observables. No partition count can replace that model. An N=2 or topologically twisted construction is not by itself the desired chiral phenomenology.

## Execution, scope and access

`exact_certificate.py` is standard-library Python using exact integer/Fraction arithmetic. `exact_receipt.json` includes its source SHA-256. Replay with `python exact_certificate.py --verify` checks the existing receipt without regeneration. No Lean theorem, RT-functor proof, modular-data derivation, physical Dirac-index calculation, anomaly cancellation, compactification vacuum, or coupling prediction was produced.

Downloaded full papers or complete extractor text are retained locally, with retrieval failures and hashes. Kauffman's original Numdam PDF failed; the distinctions above are grounded in Jones's own survey and other primary research, not an assertion that we read the failed original. Narrow E7 web searches sometimes returned games/clothing; alternate mathematical searches located the general ribbon-category and E7 WZW sources. This is a bounded multi-vector investigation, not an exhaustive literature theorem. All intended deliverables are in this lane; an initial file-tool Cygwin shadow-path misrouting was detected and recovered to the real native directory. No publication or board changes were made.

## Sources

[1] https://webhomes.maths.ed.ac.uk/~v1ranick/papers/witten.pdf — Quantum Field Theory and the Jones Polynomial
[3] https://arxiv.org/pdf/2011.09487 — Universal Correlators and Novel Cosets in 2d RCFT
[5] https://arxiv.org/pdf/hep-th/0412243 — Khovanov-Rozansky Homology and Topological Strings
[7] https://arxiv.org/pdf/1001.1571 — Dedekinds eta-function and Rogers-Ramanujan identities
[9] https://arxiv.org/pdf/1604.08837 — Representations of symmetric groups with non-trivial determinant
[10] https://arxiv.org/pdf/2408.07893 — Chern-Simons theories with defects, Rogers-Ramanujan type functions and eta-products
[11] https://arxiv.org/pdf/1101.3216 — Fivebranes and Knots
[12] https://arxiv.org/pdf/hep-th/0212053 — Chirality and fermion number in a knotted soliton background
[13] https://arxiv.org/pdf/1003.0022 — Knot polynomial identities and quantum group coincidences
[14] https://arxiv.org/pdf/hep-th/9707069 — A representation theoretic approach to the WZW Verlinde formula
[15] https://math.berkeley.edu/~vfr/jones.pdf — The Jones Polynomial
