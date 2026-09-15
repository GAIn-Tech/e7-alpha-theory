# Renormalizable boundary anomaly remediation

## Result
An explicit **perturbatively anomaly-free, renormalizable boundary extension exists for n=3**, and by replication n=3r. It uses one complex scalar Phi=1(+3), one new 27/bar27 spectator pair, and six new Weyl singlets per three light families. The heavy pair masses itself, not the original families. The original three 27(+1) and three 1(-3) remain light in the specified block-diagonal action. This is new boundary action data in the non-SUSY bulk-Dirac variant, not a derivation of family multiplicity or a complete E7 quantum UV theory.

For n=1,2,4,5 the declared search is UNSAT. More strongly, an E6-preserving fully massive spectator sector made only of 27,bar27 and singlets cannot cancel a light coefficient n not divisible by three, irrespective of charge/multiplicity bounds. This restricted obstruction does not select three among all possible theories.

## Concrete action, all fermions left handed
The compact group is H=(E6_sc x U1_X)/Z3. In the predecessor's orientation the admissibility rule is q=t mod 3, with central characters t(27)=1, t(bar27)=-1, t(1)=0.

| field | representation | multiplicity | role |
|---|---|---:|---|
| F_i | 27(+1) | 3 | original light |
| s_i | 1(-3) | 3 | original light |
| P | 27(-2) | 1 | new heavy |
| Q | bar27(-1) | 1 | new heavy |
| a_j | 1(0) | 2 | new heavy |
| b_j | 1(+3) | 2 | new heavy |
| c | 1(+6) | 1 | new heavy |
| d | 1(-3) | 1 | new heavy |
| Phi | complex scalar 1(+3) | 1 | radial/phase completion |

With canonical positive kinetic terms choose

L_Y = -[ y_P Phi P Q + sum_(j=1,2) y_j Phi^dagger a_j b_j
         + y_c Phi^dagger c d + h.c. ].

Gauge indices in P Q use the nondegenerate evaluation pairing. Distinct two-component Weyl fields have a nonvanishing Lorentz scalar bilinear; no identical-commuting-field cubic confusion arises. Every interaction has dimension four and total X charge zero. All displayed y are nonzero. Bare spectator masses and other allowed couplings are set to zero as explicit action choices, not as consequences of H.

To keep the named original fields unmixed, impose a classical spectator parity: all new Weyl spectators odd, original fermions and Phi even. This forbids F_i Q and light-heavy singlet mixing. This is an additional perturbative selection rule, **not a newly gauged anomaly-free Z2 claim**; its nonperturbative/global status is not established here. Even without that rule, generic mixing with Q removes only one linear combination of four 27s, leaving net three, but the original named light fields and singlet masses need not stay as chosen. Couplings to a later E6-breaking sector must respect/revisit this selection rule; no full combined-model protection is inferred.

At Phi=v/sqrt(2), the P,Q block has Weyl mass rank 54. The three singlet Dirac blocks have rank six. Exact checks use nonsingular dimensionless Yukawa values (1;1,2,3), with no observed-mass fit. Embedded in all nine singlet flavors the mass matrix has rank six and nullity three. The E6 flavor matrix has shape 4 by 1 and rank one. Thus heavy rank is 60, the E6 net 27 index is 4-1=3, and exactly three original singlets survive for this action. No mirror is required to pair a light family.

## Complete local anomaly arithmetic
Order coefficients as (E6^2 X / T27, gravity^2 X, X^3). The contributions are

- Original light sector: (3,72,0).
- P,Q: (-3,-81,-243).
- Two a,b pairs: (0,6,54).
- c,d: (0,3,189).
- Total heavy: (-3,-72,0); total UV: (0,0,0).

The scalar has no chiral anomaly. E6^3 is zero for each representation because E6 has no invariant degree-three polynomial on its Lie algebra; its symmetric 27-matter cubic is a different tensor. E6 X^2 vanishes by traceless generators. There is no pure gravitational local anomaly in four dimensions. These group/index-theorem inputs are external mathematical premises, not newly Lean-formalized statements.

Place spectators on the same breaking wall L. They cancel that wall's full localized coefficient, not merely an integrated zero-mode anomaly. The identity wall remains unchanged at zero. Cancellation occurs **before** selecting a Higgs vacuum; it is not attributed to making an anomalous vector massive.

## Finite search and obstruction
`checks.py` generates integer multiplicities of all blocks with |q|<=6. A block is 27_q+bar27_r or two singlets, with q+r in {-3,0,3}, hence a Phi, Phi^dagger or bare mass. Limits are two E6 Dirac blocks and six singlet Dirac blocks; multiplicities are nonnegative integers. Search n=1,...,6 solves all three anomaly equations simultaneously. Six saved SMT-LIB inputs replay SAT precisely at n=3,6. The displayed candidate is separately checked, not assumed to be the solver's unique/preferred model. The pair ansatz supplies an explicit full-rank sufficient mass structure; it is not claimed to enumerate every neutral Majorana flavor matrix.

For the stronger mod-three obstruction, an E6-singlet vacuum can only mass a 27 against a bar27. Full rank of the E6 flavor mass matrix requires equal numbers and at least one nonzero determinant permutation. Each such pairing joins q=1 mod3 to r=-1 mod3, so q+r=0 mod3. Therefore the entire heavy mixed coefficient is in 3Z. Singlets cannot alter it. Its cancellation against n requires n=0 mod3. This argument also holds for arbitrary mixing and higher powers of E6-singlet scalars: the quotient charge congruence alone supplies the divisibility. For n=3 the mixed anomaly needs at least one E6 pair; the net heavy singlet charge must be +9. With a single charge-three scalar and independent renormalizable singlet Dirac blocks, each contributes at most +3, so at least three such blocks are needed. The candidate saturates those block minima, not a proved minimum over arbitrary additional representations/VEVs.

For a fixed n not divisible by three, increasing these search bounds or adding more singlets cannot help. A next extension must abandon an assumption: change the light E6-charged spectrum to supply the missing residue (one extra 27(+1)+1(-3) for n=2, two for n=1), or give an E6-nonsinglet Higgs a VEV so that heavy masses need not be E6-vectorlike. Neither is silently included; changing family content is not an acceptable repair if n was fixed by the intended model.

## Stable radial Higgs vacuum, not an E6-to-SM vacuum
Choose V(Phi)=-mu^2 |Phi|^2 + lambda |Phi|^4 with mu^2>0, lambda>0. This polynomial is bounded below and has the complete minima |Phi|^2=mu^2/(2lambda). Writing Phi=(v+h)/sqrt(2) exp(i theta) gives v^2=mu^2/lambda, radial mass squared 2mu^2>0, and a zero angular Hessian eigenvalue that is the eaten gauge direction. The origin is unstable. The explicit exact example mu^2=2, lambda=1 has v^2=2 and m_h^2=4 in arbitrary units. Positivity of the quartic alone would not prove a broken vacuum without the negative quadratic term.

Kinetic terms give (v^2/2)(dtheta-3A)^2 and, in a four-dimensional canonical gauge-field truncation, m_X^2=9g_X^2 v^2. This is not an exact all-KK formula for a boundary mass. The unbroken compact stabilizer is E6, with the apparent U1 Z3 already identified with its center. There is no additional independent Z3 gauge factor claimed. This isolated scalar sector is classically stable modulo gauge. Portal terms and the full physical E6/SM scalar Hessian belong to the separate vacuum gate; loop stability, thresholds and the combined vacuum are not established. Positive couplings and scales remain free, and no target alpha is used.

## Heavy determinant and the local Wess-Zumino term
Use exactly the predecessor convention Q4=6u-p1, I6(light)=n x Q4, delta log Z_light=i n integral lambda Q4, with E6 and gravity Ward identities preserved by the Bardeen scheme. For the displayed spectator content I6(heavy)=-3 x Q4. Consequently its determinant obeys delta log Z_heavy=-i3 integral lambda Q4, independently of its nonzero mass. In the patch Phi != 0, theta=arg Phi and delta theta=3lambda. Integrating out the heavy fermions in a derivative expansion must therefore retain

log Z_heavy,odd = -i integral theta Q4 + (gauge-invariant terms),

or S_WZ=-(n/3) integral theta(6u-p1) for r copies. Its variation is exactly the missing heavy anomaly. The coefficient follows from the computed determinant anomaly and descent, not an adjustable counterterm chosen to fit a numerical target. Net X^3=0 forbids a remaining cohomologically nontrivial theta x^2 term in this consistent scheme, even though separate pair contributions are nonzero. Bardeen representatives/invariant derivative terms can differ. No full finite-momentum determinant has been calculated.

D'Hoker and Farhi [1] explicitly compute the low-energy action of a fermion with Yukawa-generated mass and find a Higgs-dependent Wess-Zumino term reproducing its anomalies. Their primary abstract was retrieved; the full paywalled derivation was not accessed, so no equation from it is asserted verified. Our coefficient is independently derived from the predecessor's normalized index polynomial. Banks and Dabholkar [2], primary abstract and introduction, show why nonperturbative scalar configurations can obstruct replacing heavy fermions by a purely local action; this supports retaining the next limitation rather than declaring a global completion.

A complex Phi admits zeros and is a legitimate associated-line section on nontrivial quotient bundles, unlike an everywhere fixed-modulus phase. The microscopic polynomial Yukawa action is defined there, but heavy masses vanish at zeros. Accordingly the theta-only EFT is not valid across all defects, and its local WZ expression is not the complete global determinant. The added fields remove the **local perturbative UV anomaly** and supply a radial completion; they do not by themselves prove triviality of the spin-H bordism anomaly, a consistent 5D regulator, defect-localized modes, large-gauge/diffeomorphism phases or all boundary/corner data. Those are now definite global questions about this concrete spectrum, rather than an arbitrary axion phase. Matching/running must be recomputed for the new sector.

## Evidence and scope
`checks.py` constructs six integer searches, checks quotient charges, all nonzero local anomaly coefficients, Yukawa neutrality, an exact 60 by 60 mass rank, the surviving flavor indices, the radial example, and eight negative controls. `receipt.json` is exclusive-created and subsequently full-payload compared; saved SMT problems replay. `verification.json` retains real subprocess exits and corruption/missing-receipt controls. The earlier receipt is preserved as `development-receipt-superseded.json` because the final script added the explicit 60-dimensional mass calculation. No new Lean theorem, hosted CI, expert review or full global quantum-completion claim. Only this lane is written.

Reproduce with native Python:
`C:/Users/mikeb/e7-alpha-theory/gap-investigation/.venv/Scripts/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/anomaly-uv-completion-gate/run_checks.py`

[1] E. D'Hoker, E. Farhi, Nuclear Physics B248 (1984) 59-76, https://doi.org/10.1016/0550-3213(84)90586-8 ; primary abstract https://www.sciencedirect.com/science/article/abs/pii/0550321384905868 .
[2] T. Banks, A. Dabholkar, Decoupling a Fermion Whose Mass Comes From a Yukawa Coupling: Nonperturbative Considerations, https://arxiv.org/pdf/hep-lat/9204017 .
