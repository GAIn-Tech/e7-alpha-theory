# Atomic-clock connection gate: E7, alpha and the SI second

## Verdict

**Atomic clocks provide a real, independent experimental channel for dimensionless frequency ratios and for specified new-physics effects. They do not turn the equality of two unrelated integers into a coupling prediction, fix a free E7 gauge-kinetic coefficient, or explain the residual of `137+9/250`.** The missing bridge is a frozen physical action and a calculable map from its parameters to clock observables, not additional timing digits.

This gate adds **13 new Z3 checks**, saved SMT inputs, exact discrepancy calculations, raw source captures, and a non-regenerating replay. All passed locally with Z3 5.1.0. They establish conditional identifiability properties of the response equations below, not the correctness of atomic many-body theory or an E7 completion. No Lean/Mathlib claim is made for this gate. The earlier normalization/RG checks are not counted as new work.

## 1. What the added HyperPhysics page actually says

The complete HTML page was retrieved successfully (HTTP 200), saved as `hyperphysics.html`, and its text extracted into `hyperphysics.txt`; all four sections are present: Atomic Clocks, Cesium Atomic Clock, Description of the Cesium Atom, and Rubidium Atomic Clock. It explains locking an electronic oscillator to an atomic transition, the caesium ground-state hyperfine splitting, the time-unit convention, and rubidium-clock portability.[1]

The page calls 133 the **mass number A** and states that caesium has 55 protons.[1] Thus its nucleus has 78 neutrons by subtraction. Here 133 counts nucleons; the project's `dim(E7)=133` counts independent Lie-algebra generators. Neither count is a transition energy, coupling, charge normalization, or nuclear magnetic moment. Their numerical equality supplies no map between their physical meanings. This is an inference about what an identification would require, not an experimental disproof of all E7 physics.

HyperPhysics' stability and portability figures are historical figures reported by that page, **not current clock performance benchmarks**.[1] The 2021 primary BACON paper reports Al+, Sr and Yb frequency-ratio fractional uncertainties at or below `8 × 10^-18` and constraints on ultralight-boson couplings; NIST's accompanying account describes the optical network and ratio measurements.[5][6] These are dated examples, not a claim to have established the best performance as of today. The Nature HTML is a subscription preview: its accessible abstract supports these claims; its full body was not accessed. The complete 2008 NIST comparison paper, by contrast, is retained as a 17-page PDF and complete extracted text.[4]

## 2. Definition is not determination of alpha

BIPM defines the second by fixing the numerical value of the **unperturbed ground-state hyperfine transition frequency of caesium-133** to exactly `9 192 631 770 Hz`, where Hz is s^-1.[2] This defines a unit. A realized apparatus still has perturbations and uncertainty; a unit definition is not a measurement of its own defining numerical constant. The complete NIST comparison paper treats clock-systematic errors separately from this convention.[4]

For another clock i, its frequency expressed in SI hertz is operationally proportional to the dimensionless ratio `nu_i/nu_Cs`. If all frequencies acquired the same scale factor, ratios would be unchanged. Conversely, changes in alpha can change ratios even while the SI numerical caesium defining frequency remains exact. Thus **a fixed SI frequency does not imply a physically immutable dimensionless alpha**. This follows algebraically from the definition and ratio cancellation, checked below.

An absolute *dimensionless* ratio can in principle determine alpha if a sufficiently accurate, independently normalized atomic calculation and all nuisance inputs are available. High experimental ratio precision alone does not provide that theoretical normalization. Repeated ratio measurements are especially useful for changes: a constant unknown intercept cancels from temporal differences. The NIST paper explicitly removes the common Rydberg scale in ratios and separates alpha and magnetic-moment responses.[4]

## 3. Response equations and assumptions

We use ordinary frequencies, not angular frequencies, and set `S=R_infinity c` so S has frequency units. Fix isotope, electronic levels, nuclear spin, and conventions. Work locally around a reference alpha, with smooth atomic response functions and first-order changes. After correcting differential gravitational redshift, motion, electromagnetic shifts, temperature shifts and transfer-chain errors, use the leading atomic model:

```text
nu_i,opt = S C_i F_i(alpha)
nu_A,hfs = S C_A alpha^2 (me/mp) g_A F_A(alpha)
K_i = partial ln F_i / partial ln alpha
mu_A = g_A I_A mu_N,    mu_N / mu_B = me/mp
```

Constant spin and angular factors are absorbed into C_A; signs/conventions of g_A are fixed, and logarithmic variations mean fractional variations about its nonzero reference value. The frequency scaling and magnetic-moment factor follow NIST equations (7)-(8); rewriting the magnetic-moment/Bohr-magneton ratio separates mass and nuclear factors.[4] Finite nuclear-size, recoil, QED, isotope and other dependencies are neglected in the simplified equations only, not asserted identically absent in nature. A high-accuracy prediction must restore them and their uncertainties.

Write `a=delta ln alpha`, `m=delta ln(me/mp)`, `g_A'=delta ln g_A`, and `s=delta ln S`. Taking logarithmic differentials gives the following derived identities:

```text
delta ln nu_i,opt = s + K_i a
delta ln nu_A,hfs = s + (2+K_A) a + m + g_A'

delta ln(nu_i,opt/nu_j,opt) = (K_i-K_j) a
delta ln(nu_i,opt/nu_Cs) = (K_i-2-K_Cs) a - m - g_Cs'
delta ln(nu_A,hfs/nu_B,hfs) = (K_A-K_B) a + g_A' - g_B'
```

Every ratio cancels s. Hyperfine/hyperfine comparisons also cancel the explicit common mass factor, but nuclear g factors may themselves depend on quark-mass/QCD ratios. If one instead defines `mu=mp/me`, the optical/Cs mass term is **+delta ln mu**, not minus. Treating g as constant is a nuclear-physics prior, not something the clock measures automatically. The NIST paper explicitly warns that separating mass-ratio variation through a nuclear model is model-dependent.[4]

More generally, for dimensionless inputs `x=(alpha, me/mp, mq/Lambda_QCD, ...)`,

```text
y_ij = delta ln(nu_i/nu_j) = sum_a (K_ia-K_ja) delta ln x_a + epsilon_ij.
```

K is the local Jacobian of a specified atomic calculation, including any nuclear-model dependence; epsilon contains corrected-residual systematics and noise. Identifiability is a rank/nullspace question for the response matrix after priors and nuisance parameters are declared. This is a local linear statement, not global uniqueness of an inverse atomic-structure calculation. For temporal drift replace delta ln with d ln/dt; no static offset follows without integrating with independently specified boundary and time-history data.

### Source sign check

NIST section 6.1 gives rounded sensitivities `K_Hg ≈ -3.2`, `K_Cs ≈ 0.8`, `K_Al ≈ 0`.[4] Therefore the orientation used here is

```text
y_Al/Hg ≈ +3.2 a
y_Hg/Cs ≈ -6 a - m - g_Cs'.
```

The printed coefficient immediately following that paper's equation (12) instead lists `N=NHg-NAl≈-3.2` while the displayed ratio is Al/Hg.[4] This is a sign inconsistency against its own definitions; do not silently copy it. Our subtraction order is derived from equation (8) and explicitly checked in `optical_ratio_orientation.smt2`. No historical drift central value is re-fitted or used to repair this source inconsistency. The rounded coefficients are exact rationals only within our solver model, not precision atomic input data.

## 4. Executed identifiability results

In the simplified two-ratio example the response rows are `(16/5,0,0)` and `(-6,-1,-1)` on `(a,m,g_Cs')`. The kernel contains `(0,1,-1)`; therefore alpha changes are identifiable but mass and nuclear changes remain mutually degenerate. This is independent of the measured central values. For demonstration of nullspaces, zero response or equality of two responses is used as a mathematical condition, **not invented clock data**.

| Saved SMT check | Actual result | Interpretation |
|---|---|---|
| single_microwave_alpha_nonidentifiable | SAT | Nonzero alpha change can be hidden in microwave nuisance response. |
| same_microwave_two_alphas | SAT | One Hg/Cs response need not select alpha. |
| optical_alpha_identifiable | UNSAT | For any fixed nonzero K difference, equal clean optical responses force equal alpha changes. |
| zero_sensitivity_not_identifiable | SAT | An insensitive clock pair supplies no alpha identification. |
| two_ratios_alpha_identifiable | UNSAT | Adding the clean optical ratio identifies alpha changes locally. |
| two_ratios_mass_nuclear_degenerate | SAT | Both ratios still permit different mass changes. |
| nuclear_prior_restores_mass_identifiability | UNSAT | Independently fixing nuclear response restores mass identification. |
| common_scale_cancels | UNSAT | The shared frequency scale cannot survive the ratio subtraction. |
| unknown_absolute_intercept_hides_alpha | SAT | A free theory intercept masks a static alpha offset. |
| fixed_absolute_intercept_restores_alpha | UNSAT | Independently known intercept plus nonzero sensitivity restores local identification. |
| zero_drift_does_not_fix_boundary | SAT | No variation does not select a static positive boundary value. |
| scalar_coupling_amplitude_degenerate | SAT | A doubled field excursion with halved coupling gives the same response. |
| optical_ratio_orientation | UNSAT | Al/Hg minus-order yields +3.2, not -3.2. |

SAT models in the receipt are exact algebraic witnesses; their order-one coordinates are not physical finite perturbations. Linear nullspace witnesses can be scaled arbitrarily small. UNSAT means the contradictory assignment is impossible under the stated equations. These are solver-checked real-arithmetic claims, not Lean-kernel proofs.

## 5. Does the channel explain the CODATA gap?

The newly retrieved primary NIST CODATA page confirms the **2022** recommended inverse constant `137.035999177(21)`.[3] `check_gate.py` recomputes using exact fractions, with no target tuning:

```text
candidate inverse                  = 137 + 9/250
candidate - CODATA inverse         = +823/1000000000
residual / quoted standard u       = 823/21
(alpha_candidate-alpha_CODATA)/alpha_CODATA
                                   = -823/137036000000
                                   ≈ -6.005721124376076e-9
```

This residual divided by quoted experimental uncertainty is **not a discovery significance or a probability**, and includes no model/truncation uncertainty. It remains a discrepancy for the exact candidate. In the frozen-nuisance, rounded Al/Hg response model, the corresponding first-order fractional ratio shift would be about `-1.9218307598003443e-8`. This is an illustrative sensitivity calculation, **not an independently predicted absolute clock ratio and not an additional experimental exclusion**. It substitutes the small exact fractional alpha difference for delta ln alpha at first order; no nonlinear remainder is certified.

A clock's experimental precision cannot be directly read as the accuracy with which many-body theory predicts its absolute ratio or alpha. A drift constraint likewise cannot be turned into a constant `8.23e-7` inverse-alpha correction without a time-dependent model and integration boundary. The SI-second convention supplies neither. Nothing in the retrieved sources or checked response model derives the project's correction from E7. Thus **this gate does not explain or remove the CODATA residual**.

## 6. A legitimate next clock test, with a stopping rule

A candidate E7 completion could predict a scalar-dependent gauge-kinetic function, masses or nuclear interactions. As an explicit conditional parametrization, let a dimensionless field excursion be u and write `delta ln x_a=d_a u`. Then

```text
y_ij = [sum_a (K_ia-K_ja) d_a] u.
```

Time-series clock data can constrain this product, or a drift/oscillation spectrum with specified evolution. Converting it into individual d_a requires a field normalization, amplitude/density/evolution model and enough independent response directions. The SMT amplitude/coupling degeneracy shows why the field history cannot be omitted. Published clock comparisons already exemplify testing ultralight-boson coupling models, rather than merely recording a time unit.[6]

**Go** only when the candidate freezes its action, electromagnetic embedding, kinetic normalization, spectrum, matching, nuclear/atomic response calculation, field history if relevant, nuisance priors, covariance treatment, theory uncertainty and at least one actual ratio/drift prediction **before** using that datum. Fit residual clock-systematic nuisance terms only under an explicit experimental model, not as E7 correction terms. **Stop** the parameter-free claim if a free intercept/boundary or nuisance direction can absorb the signal. Do not fit a new coefficient to the CODATA residual and call it a prediction. These gates leave genuine future E7 theories open while rejecting this proposed numerical shortcut.

## Reproduce and audit

From native Windows Bash:

```bash
# Replay the retained original receipt; does NOT regenerate it first.
C:/Users/mikeb/e7-alpha-theory/gap-investigation/.venv/Scripts/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/atomic-clock-gate/check_gate.py --verify-existing
# Explicitly rebuilding is a separate operation, overwriting the receipt:
C:/Users/mikeb/e7-alpha-theory/gap-investigation/.venv/Scripts/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/atomic-clock-gate/check_gate.py
```

`gate-receipt.json` holds exact inputs, source/code hashes, solver results and SAT witnesses. `replay-receipt.json` holds the original receipt hash, source/hash checks and independent replays of retained SMT inputs. `source-receipt.json` records complete raw fetch sizes, HTTP status, URLs, SHA-256 and retrieval time. `citations.json` records source IDs and verbatim evidence; `citation-verification.json` records the citation check. Source capture uses urllib plus PyMuPDF for PDF extraction; solver execution uses the existing isolated Z3 environment. No measured time series was downloaded or reanalysed. No hosted CI was run, no files in `next-gate` were changed, and nothing was committed or pushed.

The file tool again wrote helper files into the Cygwin shadow despite reporting the native target; they were copied byte-for-byte to the native canonical directory and executed there. The HTTP HyperPhysics source has no TLS transport authenticity; the saved bytes/hash support reproducibility, while primary BIPM/NIST sources corroborate its defining-frequency account. The report is AI-assisted and self-assessed, not externally peer reviewed.

## Sources

[1] http://hyperphysics.phy-astr.gsu.edu/hbase/acloc.html — hyperphysics
    > "Very accurate clocks can be constructed by locking an electronic oscillator to the frequency of an atomic transition. The frequencies associated with such transitions are so reproducible that the definition of the second is now tied to the frequency associated with a transition in cesium-133:
1 second = 9,192, 631,770 cycles of the standard Cs-133 transition
The two most widely used atomic clocks in recent years have been the
cesium beam atomic clock
and the
rubidium clock
. Such clocks have provided the accuracy necessary to test
general relativity
and to track variations in the frequencies o"
[2] https://www.bipm.org/en/si-base-units/second — bipm
    > "It is defined by taking the fixed numerical value of the caesium frequency Δν
Cs
, the unperturbed ground-state hyperfine transition frequency of the caesium-133 atom, to be
9 192 631 770
when expressed in the unit Hz, which is equal to s
–1
.
This definition implies the exact relation Δν
Cs
= 9 192 631 770 Hz. Inverting this relation gives an expression for the unit second in terms of the defining constant
Δν
Cs
:
or
The effect of this definition is that the second is equal to the duration of
9 192 631 770
periods of the radiation corresponding to the transition between the two hyperfine leve"
[3] https://physics.nist.gov/cgi-bin/cuu/Value?alphinv — codata
    > "137.035 999 177
Standard uncertainty
0.000 000 021
Relative standard uncertainty
1.6 x 10
-10
Concise form
137.035 999 177(21)
Click
here
for
correlation coefficient
of this constant with other constants
Source: 2022 CODATA
recommended values
Definition of
uncertainty
Correlation coefficient with
any other constant"
[4] https://tf.nist.gov/general/pdf/2295.pdf — nist-comparison
    > "Temporal variation of Ry is common to all transition frequencies and its contribution is
removed from frequency ratio measurements. The term Nj contains the dependence of the
speciﬁc transition involved; it can be either positive or negative, and tends to be larger for
transitions involving heavier atoms, where relativistic corrections play a more important role
for the atomic energies. Values of Nj have been calculated for several electronic transitions of
atomic and molecules of cosmological and laboratory interest, including Hg+ [4] and Al+ [54],
as well as for HFS transitions in the microw"
[5] https://www.nist.gov/news-events/news/2021/03/nist-team-compares-3-top-atomic-clocks-record-accuracy-over-both-fiber-and — nist-network
    > "frequency ratios, the quantitative relationships between the frequencies of the atoms as measured in three pairs (ytterbium-strontium, ytterbium-aluminum, aluminum-strontium). The results are the three most accurate measurements ever made of natural constants. Frequency ratios are considered constants and are used in some international standards and tests of fundamental physics theories.
Frequency ratios offer an important advantage as a metric for evaluating optical atomic clocks. A direct measurement of an optical clock frequency in the usual units of hertz (one cycle per second) is limited"
[6] https://www.nature.com/articles/s41586-021-03253-4 — network-paper
    > "Here we operate a network of optical clocks based on
27
Al
+
(ref.
6
),
87
Sr (ref.
7
) and
171
Yb (ref.
8
), and measure their frequency ratios with fractional uncertainties at or below 8 × 10
−18
. Exploiting this precision, we derive improved constraints on the potential coupling of ultralight bosonic dark matter to standard model fields
9
,
10
. Our optical clock network utilizes not just optical fibre
11
, but also a 1.5-kilometre free-space link
12
,
13
. This advance in frequency ratio measurements lays the groundwork for future networks of mobile, airborne and remote optical clocks tha"
